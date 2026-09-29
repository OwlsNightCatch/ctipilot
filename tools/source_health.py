#!/usr/bin/env python3
"""tools/source_health.py — health check of every source: reachable AND returning relevant, current content.

Hits HEAD on every `status: "active"` source in `sources/sources.json`,
records `(id, status_code, latency_ms, fetched_at)` to
`state/source_health.json`. Intended to run as a GitHub Action on a weekly
cron (and on manual `workflow_dispatch`) — independently of the daily
brief routine — so the source-demotion logic can key off a *consistent*
failing pattern rather than the day-of-week luck of the routine's daily
fire.

The Ops dashboard surfaces `state/source_health.json` once it exists.

Design rules:
- Stdlib-only. No third-party deps.
- Read-only on `sources.json`; write-only on `state/source_health.json`.
- Bounded history: keep the last 12 runs per source (about 3 months at
  weekly cadence).
- Non-zero exit only on script-level error (cannot read sources.json,
  cannot write source_health.json). Per-source HTTP failures are normal
  data, not script errors.
- SSRF prevention: refuse to follow redirects to loopback / link-local /
  private addresses. Same defence the URL-liveness gate in
  tools/check_brief.py uses.

Usage:
    python3 tools/source_health.py                # health-check every active source
    python3 tools/source_health.py --dry-run      # print results, don't write state
    python3 tools/source_health.py --timeout 15   # per-request timeout in seconds
    python3 tools/source_health.py --workers 10   # parallel probe workers (default 10)
    python3 tools/source_health.py --budget 420   # overall wall-clock budget in seconds
                                                  # (default 420; 0 = unlimited). On
                                                  # exhaustion the sweep still WRITES a
                                                  # complete snapshot: un-probed sources
                                                  # carry the previous snapshot's result
                                                  # forward (`carried_forward: true`) so
                                                  # `latest` never silently shrinks.
"""

from __future__ import annotations

import argparse
import html
import ipaddress
import json
import re
import socket
import ssl
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
SOURCES_JSON = ROOT / "sources" / "sources.json"
STATE_JSON = ROOT / "state" / "source_health.json"

# Hosts the daily routine knows reliably 403 the default UA but are alive.
# Treat 403 / 429 from these as "OK (UA-blocked)" so the health snapshot
# doesn't oscillate on signals the bridge fetcher already mitigates.
KNOWN_UA_BLOCKED_HOSTS: tuple[str, ...] = (
    "www.cisa.gov", "cisa.gov",
    "ncsc.admin.ch", "www.ncsc.admin.ch",
    "talosintelligence.com", "blog.talosintelligence.com",
    "csirt.gov.it", "acn.gov.it",
    "prodaft.com", "www.prodaft.com",
    "inside-it.ch", "www.inside-it.ch",
    "ico.org.uk", "www.ico.org.uk",
)

# Kept in lockstep with tools/fetch_source.py BROWSER_UA / BROWSER_CLIENT_HINTS
# (Chrome 138 + Sec-CH-UA). The probe must mimic exactly what the
# bridge sends, so "reachable in the health probe" == "reachable via the bridge".
DESKTOP_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
)
BROWSER_CLIENT_HINTS = {
    "Sec-CH-UA": '"Chromium";v="138", "Google Chrome";v="138", "Not?A_Brand";v="99"',
    "Sec-CH-UA-Mobile": "?0",
    "Sec-CH-UA-Platform": '"Windows"',
}

FETCH_SOURCE = ROOT / "tools" / "fetch_source.py"

# `api`/`bridge` sources are served by tools/fetch_source.py, not by a
# plain GET of their `url` (the url is often an SPA shell or a catalog page).
# To verify the bridge *recipe* still works we invoke the documented subcommand
# and check it returns a non-trivial body. `api` sources map to their specific
# subcommand below; `bridge` sources fall back to `url <url>`. Anything not
# mapped also falls back to `url <url>`.
API_BRIDGE_CMD: dict[str, list[str]] = {
    "cisa-kev": ["cisa-kev"],
    # 2026-07-09 structured-listing recipes: the /news-events/* listing pages
    # are JS shells (client-rendered from a Drupal view) — `cisa page` on them
    # returns only the filter UI. The Drupal RSS endpoints carry the same
    # listings fully structured and fetch cleanly through `cisa feed` (reader
    # proxy). Directives has no feed; its listing DOES hydrate through the
    # reader (grep /news-events/directives/ hrefs), and new directives are
    # announced in news.xml as well.
    "cisa-advisories": ["cisa", "feed", "https://www.cisa.gov/cybersecurity-advisories/all.xml", "3"],
    "cisa-news": ["cisa", "feed", "https://www.cisa.gov/news.xml", "3"],
    "cisa-directives": ["cisa", "page", "https://www.cisa.gov/news-events/directives"],
    "ncsc-ch-security-hub": ["ncsc-csh", "recent", "1"],
    "anssi-fr": ["cert-fr", "avis-recent", "1"],
    "cert-eu": ["cert-eu", "recent", "1"],
    "sec-disclosures-edgar": ["sec-edgar", "8k"],
    "ransomware-live": ["url", "https://api.ransomware.live/v2/recentvictims"],
    # github.com/advisories is blocked by the egress proxy (repo-scoped session,
    # not a UA refusal); the reachable substitute is OSV.dev, which mirrors the
    # full GitHub Advisory Database. Canary on a permanent GHSA id (Log4Shell)
    # verifies the OSV recipe still resolves.
    "github-advisory": ["osv", "vuln", "GHSA-jfh8-c2jp-5v3q"],
    # The EUVD front page is a JS app; its documented recipe is the JSON API.
    "enisa-euvd": ["enisa-euvd", "recent", "exploited"],
}
# Per-source recipe overrides read from sources.json `health_cmd` (a list of
# fetch_source.py arguments), filled in main(). Data beats code: a recipe fix
# found by an audit lands in the source record, not in this file.
_HEALTH_CMD_OVERRIDES: dict[str, list[str]] = {}

# Minimum stdout bytes for a bridge invocation to count as "served content".
BRIDGE_MIN_BYTES = 200

# Essential sources fronted by an anti-bot WAF (Akamai 403s the egress
# fingerprint on every UA) whose bridge recipe reaches the content through a
# server-side reader proxy (r.jina.ai) — so they normally probe `bridge-ok`.
# They stay listed here as a TRANSIENT-OUTAGE SAFETY NET: if the reader proxy
# is momentarily rate-limited / down and the direct fetch 403s, the bridge
# fails with a transport reason, and for these hard-rule-protected essentials
# that failure is a HANDLED state (class `bridge-blocked`, action `none`) — a
# 403 never demotes — rather than an unsolved `needs-demote`. A NON-transport
# recipe break (parse error / 404 / empty body) still surfaces as `bridge-fail`
# → needs-demote, so a real regression is not masked. Recipes + fallbacks are
# documented in sources/sources.json notes + .claude/memory/source-fetch-blocks.md.
TRANSPORT_BLOCKED_HANDLED: frozenset = frozenset({
    "cisa-advisories", "cisa-directives", "cisa-news",
})

# `fetch_method: blocked` hosts that NO transport reaches — direct fetch, the
# jina reader proxy, AND the bridge all fail (e.g. coe.int / downloads.seppmail.com
# return HTTP 401 even to the reader). The hard rule forbids demoting on a
# transport 403, and these are documented in sources.json notes as coverage
# gaps served by WebSearch, so a probe 403/429 for one of them is a HANDLED
# state (action `none`), never an unsolved `needs-demote` that churns every
# sweep. A NON-transport break (404 / 5xx / dead host) still surfaces, so a
# genuine removal is not masked. Documented source-ids only — see sources.json
# notes and .claude/memory/source-fetch-blocks.md.
#
# 2026-07-06 jina-fallback recovery: `group-ib` and `ccn-cert-es` were REMOVED
# from this set — the r.jina.ai reader proxy reaches both (group-ib now fetches
# direct too), so they moved to fetch_method bridge / jina and probe healthy.
# The reader is the universal fallback; a host only belongs here if the reader
# fails on it as well. Add one ONLY after confirming direct AND jina AND bridge
# all fail (transport block, not death).
TRANSPORT_BLOCKED_UNREACHABLE: frozenset = frozenset({
    # Hosts verified unreachable by EVERY transport — direct browser-UA fetch,
    # the bridge's structured recipes, AND the jina reader (which fetches from
    # its own egress and runs page JS, so it normally defeats anti-bot/geo
    # gates). Membership is earned by a probe, never assumed, and the evidence
    # goes in the source's `notes`. These keep `status: active` — a 403 is a
    # transport block, never a content-death signal — and are reported as
    # handled so they stop churning as unsolved every sweep.
    #
    # censys-blog (2026-08-05): censys.com challenge-gates the whole origin.
    # The documented feed (/feed/), the blog index (/blog, /resources/blog/)
    # and /sitemap.xml all return 403 direct and relay an upstream block through
    # the reader; the legacy www.censys.io/blog/rss.xml is 404. Re-probe each
    # run and drop it from this set the moment the origin relaxes.
    "censys-blog",
})


def _ip_blocked(addr: str) -> bool:
    try:
        ip = ipaddress.ip_address(addr)
    except ValueError:
        return True
    return bool(
        ip.is_loopback or ip.is_link_local or ip.is_private
        or ip.is_multicast or ip.is_reserved or ip.is_unspecified
    )


def _host_blocked(host: str) -> bool:
    try:
        infos = socket.getaddrinfo(host, None, socket.AF_UNSPEC, socket.SOCK_STREAM)
    except socket.gaierror:
        return True
    return any(_ip_blocked(s[4][0]) for s in infos)


class _SafeRedirectHandler(urllib.request.HTTPRedirectHandler):
    max_redirections = 5

    def redirect_request(self, req, fp, code, msg, headers, newurl):  # type: ignore[override]
        parsed = urlparse(newurl)
        scheme = (parsed.scheme or "").lower()
        host = (parsed.hostname or "").lower()
        if scheme not in ("http", "https"):
            raise urllib.error.HTTPError(
                newurl, code, f"redirect refused: scheme {scheme!r}",
                headers, fp,
            )
        if not host or _host_blocked(host):
            raise urllib.error.HTTPError(
                newurl, code, f"redirect refused: host {host!r} resolves to disallowed address",
                headers, fp,
            )
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def _check(url: str, *, timeout: float, retries: int = 1) -> tuple[int | None, int, str]:
    """`_check_once` with a transient-failure retry. Cloudflare-fronted hosts
    intermittently 403/429/5xx a single request under a rapid sweep; one retry
    after a short backoff turns those blips into the true (usually 2xx) result,
    so the dashboard floats only PERSISTENT problems, not transient noise. A
    definitive result (2xx/3xx, or 404/410 = gone) returns immediately."""
    last = _check_once(url, timeout=timeout)
    status = last[0]
    if status is not None and (200 <= status < 400 or status in (404, 410)):
        return last
    for _ in range(max(0, retries)):
        time.sleep(1.5)
        last = _check_once(url, timeout=timeout)
        status = last[0]
        if status is not None and (200 <= status < 400 or status in (404, 410)):
            return last
    return last


def _check_once(url: str, *, timeout: float) -> tuple[int | None, int, str]:
    """Returns `(status_code, latency_ms, error_message)`. status_code is
    None on transport errors. latency_ms is the wall-clock time the request
    took, regardless of outcome. error_message is empty on success."""
    parsed = urlparse(url)
    host = (parsed.hostname or "").lower()
    if not host or _host_blocked(host):
        return None, 0, "host blocked (loopback/link-local/private/DNS-fail)"
    opener = urllib.request.build_opener(_SafeRedirectHandler())
    headers = {
        "User-Agent": DESKTOP_UA,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        **BROWSER_CLIENT_HINTS,
    }
    t0 = time.monotonic()
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, headers=headers, method=method)
            with opener.open(req, timeout=timeout) as resp:
                # Drain a small bounded chunk for HEAD-fallback-to-GET.
                try:
                    resp.read(64 * 1024)
                except Exception:
                    pass
                return resp.status, int((time.monotonic() - t0) * 1000), ""
        except urllib.error.HTTPError as e:
            # Many sites refuse HEAD (405/501) or anti-bot-block it (403/429)
            # while serving GET fine — retry as GET before concluding.
            if e.code in (403, 405, 429, 501) and method == "HEAD":
                continue
            return e.code, int((time.monotonic() - t0) * 1000), ""
        except (urllib.error.URLError, socket.timeout, ssl.SSLError, ConnectionError) as e:
            return None, int((time.monotonic() - t0) * 1000), str(e)[:160]
        except Exception as e:  # noqa: BLE001
            return None, int((time.monotonic() - t0) * 1000), str(e)[:160]
    return None, int((time.monotonic() - t0) * 1000), "exhausted methods"


def _classify(status: int | None, host: str) -> str:
    """Returns a short label that the Ops dashboard can colour-code:
    `ok` (2xx), `redirect-ok` (3xx), `ua-blocked` (4xx but on known UA-blocked
    host), `client-error` (4xx other), `server-error` (5xx), `unreachable`
    (transport error / DNS fail)."""
    if status is None:
        return "unreachable"
    if 200 <= status < 300:
        return "ok"
    if 300 <= status < 400:
        return "redirect-ok"
    if status in (403, 429) and host in KNOWN_UA_BLOCKED_HOSTS:
        return "ua-blocked"
    if 400 <= status < 500:
        return "client-error"
    if 500 <= status < 600:
        return "server-error"
    return f"http-{status}"


def _jina_reachable(url: str, *, timeout: float) -> bool:
    """True iff the r.jina.ai reader proxy returns non-trivial content for
    `url`. Used as the universal-fallback reachability probe: a source that
    anti-bot-blocks / geo-gates / JS-shells our direct fetch is still
    `reachable cleanly` if the reader gets its body (the `url` command's own
    auto-fallback, and the agents' tier-3 transport, both go through this)."""
    try:
        proc = subprocess.run(
            [sys.executable, str(FETCH_SOURCE), "jina", url],
            capture_output=True, text=True, timeout=max(timeout, 45.0),
        )
    except Exception:  # noqa: BLE001
        return False
    return proc.returncode == 0 and len((proc.stdout or "").strip()) >= BRIDGE_MIN_BYTES


def _bridge_check(source_id: str, url: str, *, timeout: float,
                  fetch_method: str = "bridge") -> tuple[str, str]:
    """Invoke the documented bridge recipe for an `api` / `bridge` / `jina`
    source and report whether it still returns usable content. Returns
    `(class, detail)` where class is `bridge-ok` or `bridge-fail`. This is how
    we verify the sources that go through tools/fetch_source.py are still
    working, rather than only HEAD-probing a URL that may be an SPA shell.

    `jina` sources force the reader recipe (`jina <url>`); `bridge` sources
    with no dedicated subcommand use `url <url>`, which itself auto-falls-back
    to the reader — so a bridge source behind a fresh WAF still probes ok."""
    default = ["jina", url] if fetch_method == "jina" else ["url", url]
    argv = _HEALTH_CMD_OVERRIDES.get(source_id) or API_BRIDGE_CMD.get(source_id) or default
    why = ""
    # `why` is truncated for display; `why_full` keeps the untruncated stderr so
    # classification never depends on where the truncation happened to fall.
    # (2026-08-19: it did. The reader-quota test below searched the 140-char
    # `why`, so a source whose bridge argv + URL pushed the literal "402" past
    # that limit was misclassified `bridge-fail` → unsolved `needs-demote`,
    # while a shorter-URL source failing on the identical exhausted-key
    # condition classified correctly as `reader-quota`. ccn-cert-es and
    # ssd-disclosure diverged that way on the same run with the same root cause.)
    why_full = ""
    # One transient retry — the same Cloudflare/rate-limit blip handling as _check.
    for attempt in (1, 2):
        try:
            proc = subprocess.run(
                [sys.executable, str(FETCH_SOURCE), *argv],
                capture_output=True, text=True, timeout=timeout,
            )
        except subprocess.TimeoutExpired:
            why = why_full = f"timed out after {timeout:.0f}s"
        except Exception as e:  # noqa: BLE001
            why_full = f"error: {str(e)}"
            why = f"error: {str(e)[:120]}"
        else:
            out = proc.stdout or ""
            if proc.returncode == 0 and len(out.strip()) >= BRIDGE_MIN_BYTES:
                return "bridge-ok", f"bridge `{' '.join(argv)}` → {len(out)} B"
            # A QUERY recipe that succeeds and legitimately matches nothing is
            # working, not broken. Search/API subcommands (SEC EDGAR full-text
            # search, OSV queries, KEV filters) return a small, well-formed JSON
            # envelope with an empty result set in a quiet window — under
            # BRIDGE_MIN_BYTES, so the size test alone read it as `bridge-fail`
            # and floated an unsolved `needs-demote` against a recipe that runs
            # correctly on the very next call. (2026-08-23: sec-disclosures-edgar
            # was the whole UNSOLVED list for the weekly sweep on exactly this —
            # `sec-edgar 8k 2026-08-17 2026-08-23 1.05` exits 0 with total 0
            # because no Item 1.05 8-K was filed that week.) Recognise the
            # zero-result envelope explicitly; a malformed or error payload still
            # falls through to bridge-fail.
            if proc.returncode == 0 and out.strip().startswith(("{", "[")):
                try:
                    payload = json.loads(out)
                except ValueError:
                    payload = None
                if isinstance(payload, dict):
                    counts = [payload.get(k) for k in ("count", "total", "total_count")]
                    lists = [payload.get(k) for k in ("hits", "results", "items", "vulns")]
                    empty_count = any(c == 0 for c in counts if isinstance(c, int))
                    empty_list = any(isinstance(v, list) and not v for v in lists)
                    if empty_count or empty_list:
                        return "bridge-ok", (f"bridge `{' '.join(argv)}` → {len(out)} B, "
                                             "well-formed empty result set (recipe works, "
                                             "query matched nothing this window)")
            raw = (proc.stderr or out or "").strip()
            tail = raw.splitlines()
            why_full = raw if tail else f"rc={proc.returncode}, {len(out)} B"
            why = tail[-1][:140] if tail else f"rc={proc.returncode}, {len(out)} B"
        if attempt == 1:
            time.sleep(1.5)
    detail = f"bridge `{' '.join(argv)}` failed: {why}"
    # A jina reader HTTP 402 is an ACCOUNT-level block, not a per-source recipe
    # death: every configured reader key's token balance is exhausted, so EVERY
    # jina fetch (and every `url` auto-fallback) this run degrades identically
    # regardless of the source. Since the multi-key + anonymous-fallback ladder
    # shipped in fetch_source.py, this class only surfaces when the whole key
    # pool is dead AND the anonymous free-tier rung also failed for the fetch.
    # The hard rule forbids demoting on a transport block (402 / 403 / 429), so
    # this must not churn every jina-method source as an unsolved `needs-demote`
    # while the pool is down — it is a single operator fix (add a fresh key to
    # JINA_API_KEYS; `jina-usage` confirms the pool balance), not N source
    # regressions. Its own class keeps it visible without flagging it as an
    # unsolved fault.
    _quota_hay = f"{why_full}\n{why}".lower()
    if ("402" in _quota_hay or "balance exhausted" in _quota_hay) and (
            "balance exhausted" in _quota_hay
            or "jina_api_key" in _quota_hay
            or "reader proxy" in _quota_hay):
        return "reader-quota", detail
    # An essential reachable ONLY through an anti-bot bridge (server-side reader
    # proxy) has no other transport, and the hard rule forbids demoting it on a
    # transport failure. So ANY bridge failure for it — a relayed 403, a reader
    # rate-limit, or a reader timeout under a heavy sweep — is a HANDLED state
    # (`bridge-blocked`, action none), never an unsolved `needs-demote`. It
    # probes `bridge-ok` whenever the reader responds; a persistent run of
    # `bridge-blocked` across many sweeps is the signal to investigate. Real
    # per-run fetch failures still surface in the run record's fetch_failures.
    if source_id in TRANSPORT_BLOCKED_HANDLED:
        return "bridge-blocked", detail
    return "bridge-fail", detail


def _feed_ok(feed_url: str, *, timeout: float, attempts: int = 2) -> bool:
    """True iff the bridge can parse `feed_url` as a feed AND it carries ≥1
    item. A homepage that isn't a feed parses to 0 items → False, so this does
    not give a false OK on a non-feed URL.

    Retried once by default. Under the sweep's worker concurrency a healthy
    feed intermittently times out or gets a transient edge error, and a single
    such miss used to fall through to a plain GET of the feed URL — which on
    anti-bot hosts answers 403/404 to a bare client and produced an UNSOLVED
    `needs-demote` for a source whose recipe works on the very next call
    (observed 2026-07-31 on darkreading, whose `feed` recipe returned dated
    items immediately after the sweep flagged it "resource gone"). One bounded
    retry removes that whole class of false demotion signals; a genuinely dead
    feed still fails both attempts."""
    for attempt in range(max(1, attempts)):
        try:
            proc = subprocess.run(
                [sys.executable, str(FETCH_SOURCE), "feed", feed_url, "3"],
                capture_output=True, text=True, timeout=timeout,
            )
        except Exception:  # noqa: BLE001
            continue
        if proc.returncode != 0:
            continue
        try:
            data = json.loads(proc.stdout or "{}")
        except Exception:  # noqa: BLE001
            continue
        if int(data.get("count") or 0) > 0:
            return True
    return False


# Common feed paths to try when an `rss` source's `url` is a homepage/index
# rather than the feed itself (the feed URL otherwise lives only in `notes`).
_FEED_SUFFIXES = ("/feed/", "/rss/", "/feed.xml", "/rss.xml", "/atom.xml", "/feed", "/rss")


def _rss_check(s: dict[str, Any], host: str, *, timeout: float) -> tuple[str, str, int | None]:
    """Verify an `rss` source by actually fetching its FEED (the recipe), not by
    HEAD-probing its `url` (which may be a hostile homepage while the feed is
    fine). Tries, in order: an explicit `rss_url` field, the `url` itself, then
    common feed paths under the url's base. Returns `(class, detail, status)`.
    `bridge-ok` when a feed parses with items; otherwise falls back to a GET of
    `url` so the failure is classified (so a genuinely-dead source still flags)."""
    seen: set[str] = set()
    candidates: list[str] = []
    for c in [s.get("rss_url"), s.get("url")]:
        if isinstance(c, str) and c and c not in seen:
            seen.add(c); candidates.append(c)
    base = (s.get("url") or "").rstrip("/")
    if base:
        for suf in _FEED_SUFFIXES:
            u = base + suf
            if u not in seen:
                seen.add(u); candidates.append(u)
    # Per-source cap: up to 9 candidates × 25 s each is a 4-minute worst case
    # for ONE source — the historical way a full sweep blew its wall-clock
    # budget. Stop walking suffix guesses after ~75 s; the explicit rss_url /
    # url candidates run first, so a real feed is found long before the cap.
    t0 = time.monotonic()
    for feed_url in candidates:
        if _feed_ok(feed_url, timeout=max(timeout, 25.0)):
            return "bridge-ok", f"feed ok: {feed_url}", None
        if time.monotonic() - t0 > 75.0:
            break
    # No feed worked — classify the homepage fetch so a real outage still shows.
    status, _lat, err = _check(s.get("url", ""), timeout=timeout)
    return _classify(status, host), (err or "no working feed found"), status


# ---------------------------------------------------------------------------
# Content assessment (2026-09-29): "reachable" is not "working".
#
# Until now a source passed the sweep on transport alone: a 200 status, a feed
# that parsed with at least one item, or 200+ bytes out of a bridge recipe. That
# passes a Cloudflare challenge page, a cookie-consent shell, a parked domain, a
# JS app shell and a feed that stopped publishing in 2024. Every source now also
# gets its CONTENT read through its own recipe and judged on three questions:
#   readable  — real text, not a challenge / consent / redirect / JS shell;
#   relevant  — security vocabulary in the source's own languages;
#   current   — the newest dated item is recent enough for the source.
# The verdict and its evidence (text volume, matched terms, newest item date)
# are written next to the reachability class, and a reachable source whose
# content fails is floated as `needs-content-fix`, never silently green.
# ---------------------------------------------------------------------------

# Challenge / shell markers, matched on the first part of the fetched body.
_SHELL_MARKERS = (
    "just a moment", "checking your browser", "attention required", "cf-browser-verification",
    "cf-chl", "enable javascript", "please enable js", "javascript is required",
    "you need to enable javascript", "access denied", "request blocked", "are you a robot",
    "captcha", "verify you are human", "ddos protection", "redirecting...",
    "please wait while", "403 forbidden", "404 not found", "page not found",
    "this domain is for sale", "domain parked", "buy this domain",
)

# Security vocabulary in the languages the source list covers. A source is
# relevant when at least RELEVANCE_MIN distinct terms appear (or any CVE id).
_SECURITY_TERMS = (
    # en
    "vulnerab", "exploit", "malware", "ransomware", "threat", "attack", "security", "advisory",
    "patch", "breach", "phishing", "backdoor", "botnet", "cyber", "incident", "zero-day",
    "zero day", "apt", "trojan", "espionage", "compromise", "hacker", "credential",
    "brute", "jailbreak", "prompt injection", "supply chain", "supply-chain", "infostealer",
    # de
    "sicherheitslücke", "schwachstelle", "angriff", "sicherheit", "warnung", "cyberangriff",
    "datenleck", "schadsoftware",
    # fr
    "vulnérabilité", "attaque", "sécurité", "menace", "rançongiciel", "faille", "alerte",
    # it
    "vulnerabilità", "attacco", "sicurezza", "minaccia",
    # nl / pl / es / pt / ja
    "kwetsbaarheid", "beveiliging", "podatność", "atak", "bezpieczeństw", "vulnerabilidad",
    "ataque", "seguridad", "segurança", "脆弱性", "攻撃", "セキュリティ",
)
RELEVANCE_MIN = 3
# Below this many letters/digits a body counts as unread (the same floor the
# gate's cited-page checks use for JS shells).
CONTENT_MIN_ALNUM = 600
# Newest dated item older than this many days ⇒ `stale` (a per-source
# `max_staleness_days` in sources.json overrides it for low-cadence publishers).
DEFAULT_MAX_STALENESS_DAYS = 60

_MONTHS = {
    "jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6, "jul": 7, "aug": 8,
    "sep": 9, "oct": 10, "nov": 11, "dec": 12,
    # de / fr / it / nl / es long and short forms (lowercased, prefix-matched)
    "januar": 1, "februar": 2, "märz": 3, "maerz": 3, "mai": 5, "juni": 6, "juli": 7,
    "oktober": 10, "dezember": 12,
    "janvier": 1, "février": 2, "fevrier": 2, "mars": 3, "avril": 4, "juin": 6,
    "juillet": 7, "août": 8, "aout": 8, "septembre": 9, "octobre": 10, "novembre": 11,
    "décembre": 12, "decembre": 12,
    "gennaio": 1, "febbraio": 2, "marzo": 3, "aprile": 4, "maggio": 5, "giugno": 6,
    "luglio": 7, "agosto": 8, "settembre": 9, "ottobre": 10, "dicembre": 12,
    "maart": 3, "mei": 5, "augustus": 8,
    "enero": 1, "febrero": 2, "abril": 4, "junio": 6, "julio": 7, "septiembre": 9,
    "octubre": 10, "noviembre": 11, "diciembre": 12,
}
_MONTH_RE = r"([A-Za-zÀ-ÿ]{3,10})\.?"
_DATE_PATTERNS = (
    # `(?!\d)`, not `\b`: an ISO timestamp ("2026-08-27T09:00:00") has a letter
    # right after the day, and `\b` between two word characters never matches.
    ("ymd", re.compile(r"(?<!\d)(20[12]\d)[-/](0[1-9]|1[0-2])[-/](0[1-9]|[12]\d|3[01])(?!\d)")),
    ("dmy_dot", re.compile(r"\b(0?[1-9]|[12]\d|3[01])\.(0?[1-9]|1[0-2])\.(20[12]\d)\b")),
    ("d_mon_y", re.compile(r"\b(0?[1-9]|[12]\d|3[01])\.?\s+" + _MONTH_RE + r",?\s+(20[12]\d)\b")),
    ("mon_d_y", re.compile(r"\b" + _MONTH_RE + r"\s+(0?[1-9]|[12]\d|3[01])(?:st|nd|rd|th)?,?\s+(20[12]\d)\b")),
)


def _month_num(word: str) -> int | None:
    w = word.lower().rstrip(".")
    if w in _MONTHS:
        return _MONTHS[w]
    for k, v in _MONTHS.items():
        if len(w) >= 3 and (k.startswith(w) or w.startswith(k)):
            return v
    return None


def _dates_in(text: str, now: datetime) -> list[datetime]:
    """Every plausible calendar date in `text`, never in the future and never
    before 2015 (copyright lines and version numbers fall outside)."""
    out: list[datetime] = []
    horizon = now.timestamp() + 86400
    for kind, rx in _DATE_PATTERNS:
        for m in rx.finditer(text):
            try:
                if kind == "ymd":
                    y, mo, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
                elif kind == "dmy_dot":
                    d, mo, y = int(m.group(1)), int(m.group(2)), int(m.group(3))
                elif kind == "d_mon_y":
                    d, mo, y = int(m.group(1)), _month_num(m.group(2)), int(m.group(3))
                else:
                    mo, d, y = _month_num(m.group(1)), int(m.group(2)), int(m.group(3))
                if not mo:
                    continue
                dt = datetime(y, mo, d, tzinfo=timezone.utc)
            except (ValueError, TypeError):
                continue
            if 2015 <= dt.year and dt.timestamp() <= horizon:
                out.append(dt)
    return out


def _alnum_len(text: str) -> int:
    return sum(1 for ch in text if ch.isalnum())


def _strip_html(raw: str) -> str:
    raw = re.sub(r"(?is)<(script|style|noscript)\b.*?</\1>", " ", raw)
    return html.unescape(re.sub(r"<[^>]+>", " ", raw))


def _run_fetch(argv: list[str], timeout: float) -> str:
    try:
        proc = subprocess.run([sys.executable, str(FETCH_SOURCE), *argv],
                              capture_output=True, text=True, timeout=timeout)
    except Exception:  # noqa: BLE001
        return ""
    return proc.stdout if proc.returncode == 0 else ""


def _content_fetch(s: dict[str, Any], *, timeout: float) -> tuple[str, str, str, list[str]]:
    """Read the source through its own recipe. Returns `(transport, text,
    raw_for_dates, feed_dates)`: `text` is what a reader would get (feed item
    titles + summaries, or extracted page text), `raw_for_dates` the raw body
    (HTML `datetime=` attributes and JSON-LD carry the dates listing pages
    hide), `feed_dates` the feed's own item timestamps."""
    sid = s.get("id", "")
    fm = s.get("fetch_method", "")
    url = s.get("probe_url") or s.get("url") or ""
    if fm == "rss":
        for feed_url in [s.get("rss_url"), s.get("url")]:
            if not feed_url:
                continue
            out = _run_fetch(["feed", feed_url, "15"], timeout)
            try:
                data = json.loads(out) if out else {}
            except ValueError:
                data = {}
            items = data.get("items") or []
            if items:
                text = "\n".join(f"{i.get('title', '')} {i.get('summary', '')}" for i in items)
                return "feed", text, "", [str(i.get("published") or "") for i in items]
    if isinstance(s.get("health_cmd"), list) and s["health_cmd"]:
        out = _run_fetch([str(a) for a in s["health_cmd"]], timeout)
        return "health_cmd", _strip_html(out) if out.lstrip().startswith("<") else out, out, []
    if fm == "api" and sid in API_BRIDGE_CMD:
        # The reachability probe asks for one item; the content read asks for a
        # real listing, since one advisory is too thin to judge volume or cadence.
        argv = [("10" if a in ("1", "3") and i == len(API_BRIDGE_CMD[sid]) - 1 else a)
                for i, a in enumerate(API_BRIDGE_CMD[sid])]
        out = _run_fetch(argv, timeout)
        return "api", _strip_html(out) if out.lstrip().startswith("<") else out, out, []
    raw_home = ""
    if fm == "rss":
        # An `rss` record without a working `rss_url`: follow the page's own
        # <link rel="alternate"> feed before judging the HTML (exodus-intelligence
        # and xlab-qianxin were probed as homepages and misread as stale).
        raw_home = _run_fetch(["url", url, "--direct"], timeout)
        for m in re.finditer(r'<link[^>]+type="application/(?:rss|atom)\+xml"[^>]*>', raw_home, re.I):
            href = re.search(r'href="([^"]+)"', m.group(0))
            if not href:
                continue
            feed_url = urllib.parse.urljoin(url, html.unescape(href.group(1)))
            out = _run_fetch(["feed", feed_url, "15"], timeout)
            try:
                items = (json.loads(out) if out else {}).get("items") or []
            except ValueError:
                items = []
            if items:
                text = "\n".join(f"{i.get('title', '')} {i.get('summary', '')}" for i in items)
                return f"feed (discovered {feed_url})", text, "", [str(i.get("published") or "") for i in items]
    # Pages: the trafilatura capture is what a reader gets; the direct raw body
    # carries the listing's titles and dates when the capture keeps only the
    # page chrome. The metered reader is used only for records pinned to it.
    ext = _run_fetch(["extract", url], timeout)
    ext_body = ext.split("\n---\n", 1)[-1] if ext.lstrip().startswith(("---", "#")) else ext
    raw = raw_home or _run_fetch(["url", url, "--direct"], timeout)
    text = ext_body + "\n" + _strip_html(raw)
    transport = "extract+direct"
    if _alnum_len(text) < CONTENT_MIN_ALNUM and fm == "jina":
        jr = _run_fetch(["jina", url], max(timeout, 45.0))
        if jr:
            text, raw, transport = jr, jr, "jina"
    return transport, text, raw, []


def _content_assess(s: dict[str, Any], *, timeout: float, now: datetime) -> dict[str, Any]:
    """Verdict on what the source actually returns: `relevant`, `stale`,
    `irrelevant`, `shell`, or `unreadable`, with the evidence behind it."""
    transport, text, raw, feed_dates = _content_fetch(s, timeout=timeout)
    low = text.lower()
    n_alnum = _alnum_len(text)
    head = low[:4000]
    shell_hits = [m for m in _SHELL_MARKERS if m in head]
    terms = sorted({t for t in _SECURITY_TERMS if t in low})
    has_cve = bool(re.search(r"\bcve-\d{4}-\d{4,}\b", low))
    dates: list[datetime] = []
    for d in feed_dates:
        try:
            dates.append(datetime.fromisoformat(d.replace("Z", "+00:00")).astimezone(timezone.utc))
        except ValueError:
            dates.extend(_dates_in(d, now))
    dated = True
    if not dates:
        dates = _dates_in(text + "\n" + (raw or ""), now)
        # A listing that shows its posts' dates carries several of them; one or
        # two dates on a page are its own metadata (published / modified), which
        # says nothing about the newest post (ibm-xforce read as 551 days stale
        # from its page date while its newest post was four weeks old).
        if len({d.date() for d in dates}) < 3:
            dated = False
            dates = []
    newest = max(dates) if dates else None
    age = int((now - newest).total_seconds() // 86400) if newest else None
    limit = int(s.get("max_staleness_days") or DEFAULT_MAX_STALENESS_DAYS)
    # A query API (SEC EDGAR full-text search, OSV, a KEV filter) that returns a
    # well-formed empty envelope is working; judge it by structure, not volume.
    empty_envelope = False
    structured_hits = False
    if transport in ("api", "health_cmd") and text.lstrip().startswith(("{", "[")):
        try:
            payload = json.loads(text)
        except ValueError:
            payload = None
        if isinstance(payload, (dict, list)):
            if isinstance(payload, dict):
                counts = [payload.get(k) for k in ("count", "total", "total_count")]
                hits = payload.get("hits")
                if isinstance(hits, dict):
                    counts.append((hits.get("total") or {}).get("value")
                                  if isinstance(hits.get("total"), dict) else hits.get("total"))
                empty_envelope = any(c == 0 for c in counts if isinstance(c, int))
                lists = [payload.get(k) for k in ("hits", "items", "results", "vulnerabilities", "vulns")]
                structured_hits = any(isinstance(v, list) and v for v in lists)
                item_lists = [v for v in lists if isinstance(v, list) and v]
                if item_lists:
                    # Date a query API by its results, not by the query window it
                    # echoes back (SEC EDGAR's `end` is always today).
                    item_dates = _dates_in(json.dumps(item_lists, ensure_ascii=False), now)
                    if item_dates:
                        newest = max(item_dates)
                        age = int((now - newest).total_seconds() // 86400)
            else:
                structured_hits = bool(payload)
    min_terms = 1 if s.get("content_scope") == "general-news" else RELEVANCE_MIN
    if empty_envelope:
        verdict = "relevant"
    elif structured_hits and not (age is not None and age > limit):
        # A security-scoped query API returning well-formed results is working
        # however small the payload (one Item 1.05 8-K is 241 letters of JSON).
        verdict = "relevant"
    elif not text.strip():
        verdict = "unreadable"
    elif (n_alnum < CONTENT_MIN_ALNUM and not shell_hits and dated and dates
          and len({d.date() for d in dates}) >= 3 and age is not None and age <= limit
          and (terms or has_cve)):
        # A legitimately small static index (three dated posts on swarmcha.se is
        # 896 bytes) is readable: dated, current, on topic and not a challenge.
        verdict = "relevant"
    elif n_alnum < CONTENT_MIN_ALNUM or (shell_hits and n_alnum < 4 * CONTENT_MIN_ALNUM):
        verdict = "shell"
    elif len(terms) < min_terms and not has_cve:
        verdict = "irrelevant"
    elif age is not None and age > limit:
        verdict = "stale"
    else:
        verdict = "relevant"
    return {
        "content_verdict": verdict,
        "content_transport": transport,
        "content_alnum": n_alnum,
        "content_terms": terms[:12],
        "content_has_cve": has_cve,
        "content_shell_markers": shell_hits[:4],
        "newest_item": newest.strftime("%Y-%m-%d") if newest else None,
        "newest_item_age_days": age,
        "max_staleness_days": limit,
        "content_empty_result_set": empty_envelope,
        "content_dated": dated,
    }


_CONTENT_FAIL_REASON = {
    "unreadable": "no transport in the recipe returned any content",
    "shell": "the recipe returns a challenge, consent, redirect or JS shell instead of content",
    "irrelevant": "the recipe returns content with no security vocabulary (wrong URL, parked or "
                  "repurposed page)",
    "stale": "reachable and relevant, but its newest dated item is older than the source's "
             "staleness limit (dark source, or the listing URL no longer shows new posts)",
}


# Probe classes that mean "reachable / handled" — no operator action needed.
# `jina-ok` = a direct probe that anti-bot-blocked / geo-gated / JS-shelled,
# but whose body the r.jina.ai reader proxy (the `url` auto-fallback, the
# agents' tier-3 transport) reaches cleanly.
_HEALTHY_CLASSES = frozenset({"ok", "redirect-ok", "bridge-ok", "jina-ok"})


def _action(status: str, fetch_method: str, cls: str, code: int | None,
            source_id: str = "") -> tuple[str, str]:
    """Derive the operator action for a source from its lifecycle status, its
    configured fetch_method, and the probe outcome. The Ops dashboard floats
    ONLY sources whose action is not `none` — i.e. unsolved problems.

    Returns `(action, reason)` where action ∈ {none, needs-bridge, needs-demote}.
      - none         → reachable, or already handled (demoted / served via a
                       working bridge / known UA-blocked host already bridged).
      - needs-bridge → a browser-grade UA is refused (403/429) on a source that
                       is NOT yet on the bridge → build a dedicated bridge recipe
                       (or demote if even the bridge can't reach it).
      - needs-demote → the source is dead/erroring (404/5xx/unreachable) OR its
                       already-implemented bridge/api recipe is now failing →
                       fix the recipe or demote.
    """
    on_bridge = fetch_method in ("bridge", "api")
    # Already-demoted sources are a handled state — never surface them.
    if status == "demoted":
        return "none", "already demoted (handled)"
    if cls in _HEALTHY_CLASSES:
        return "none", ""
    # jina reader key pool exhausted (HTTP 402) — an account-level transport
    # block hitting every jina source uniformly this run, not a source fault.
    # 402 never demotes (same hard rule as 403/429); the fix is operator-side.
    if cls == "reader-quota":
        return "none", ("jina reader key pool exhausted (HTTP 402, anonymous free-tier "
                        "fallback also failed) — account-level transport block affecting "
                        "every jina source uniformly this run, not a source fault; 402 "
                        "never demotes. Add a fresh key to JINA_API_KEYS "
                        "(verify with `fetch_source.py jina-usage`).")
    # Known transport-blocked essential: 403 on every UA (Akamai/anti-bot),
    # no reachable content recipe, substitute documented, and the hard rule
    # forbids demoting a 403. Handled — do not float it as unsolved.
    if cls == "bridge-blocked":
        return "none", ("transport-blocked essential (403 never demotes) — "
                        "KEV JSON + WebSearch substitute; see sources.json notes")
    # Documented Cloudflare-Managed-Challenge / geo-blocked host with no reachable
    # transport (direct fetch AND bridge both 403). A transport 403/429 is a
    # handled coverage gap — the hard rule forbids demoting on a 403 — so it must
    # not churn as unsolved. Only a NON-transport break (404 / 5xx / dead host)
    # for such a host still falls through to needs-demote below.
    if fetch_method == "blocked" and source_id in TRANSPORT_BLOCKED_UNREACHABLE \
            and cls == "client-error" and code in (403, 429):
        return "none", ("documented transport-blocked host (Cloudflare/geo 403 never "
                        "demotes) — coverage gap, WebSearch substitute; see sources.json notes")
    # A source already routed through the bridge whose bridge now fails, or any
    # `blocked` source that is still active, is an unsolved problem to fix/demote.
    if cls == "bridge-fail" or fetch_method == "blocked":
        return "needs-demote", "bridge/api recipe is failing now — fix the recipe or demote"
    if cls == "ua-blocked":
        # Known UA-blocked host. Handled iff it is already on the bridge.
        if on_bridge:
            return "none", "UA-blocked host, already served via the bridge"
        return "needs-bridge", f"host blocks the browser UA (HTTP {code}) — add a bridge recipe or demote"
    if cls == "client-error":
        if code in (403, 429):
            # Anti-bot / UA / geo refusal of a browser UA.
            return ("needs-demote", "bridge/api recipe is failing (403/429) — fix or demote") if on_bridge \
                else ("needs-bridge", f"browser UA refused (HTTP {code}) — needs a dedicated bridge recipe or demote")
        # 404 / 410 / other 4xx → the resource is gone.
        return "needs-demote", f"resource gone (HTTP {code}) — update the URL or demote"
    if cls in ("server-error", "unreachable"):
        return "needs-demote", f"source unreachable ({cls}{f', HTTP {code}' if code else ''}) — recheck and demote if persistent"
    return "needs-demote", f"unexpected probe class {cls!r} — review"


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--dry-run", action="store_true",
                   help="print results, do not write state/source_health.json")
    p.add_argument("--timeout", type=float, default=12.0,
                   help="per-request timeout in seconds (default 12)")
    p.add_argument("--history-cap", type=int, default=12,
                   help="how many runs to retain per source (default 12)")
    p.add_argument("--workers", type=int, default=10,
                   help="parallel probe workers (default 10)")
    p.add_argument("--budget", type=float, default=0.0,
                   help="optional overall wall-clock budget in seconds (default 0 = "
                        "unlimited: every probe is bounded by its own subprocess "
                        "timeouts, so the sweep always ends). With a budget, "
                        "un-probed sources carry the previous snapshot's result "
                        "forward and the snapshot still writes complete.")
    args = p.parse_args()

    if not SOURCES_JSON.exists():
        print(f"FATAL: {SOURCES_JSON} not found", file=sys.stderr)
        return 2
    try:
        sources_data = json.loads(SOURCES_JSON.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"FATAL: cannot parse sources.json: {e}", file=sys.stderr)
        return 2
    # Check EVERY source (active + candidate + demoted), not just the
    # active ones, so the snapshot is a complete periodic accessibility sweep.
    # The Ops dashboard then floats only the ones that need operator action.
    sources = [s for s in sources_data.get("sources", []) if s.get("url")]
    for s in sources:
        if isinstance(s.get("health_cmd"), list) and s["health_cmd"]:
            _HEALTH_CMD_OVERRIDES[s["id"]] = [str(a) for a in s["health_cmd"]]
    if not sources:
        print("No sources to check.")
        return 0

    fetched_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print(f"# source-health snapshot — {fetched_at}")
    print(f"# checking {len(sources)} source(s); timeout={args.timeout}s "
          "(api/bridge sources verified through tools/fetch_source.py)")

    # Pre-flight: probe a single high-availability HTTPS host. If the SSL
    # handshake fails because the local Python has no CA trust store
    # (a common macOS footgun), warn and continue — every per-source result
    # will land in the `unreachable` bucket because of the cert error, but
    # that's distinguishable from a real source-side outage in the dashboard
    # if the operator sees the pre-flight WARN. CI (Linux + bundled
    # certifi) is unaffected.
    try:
        opener = urllib.request.build_opener(_SafeRedirectHandler())
        probe = urllib.request.Request(
            "https://www.google.com/",
            headers={"User-Agent": DESKTOP_UA},
            method="HEAD",
        )
        opener.open(probe, timeout=5).close()
        print("# pre-flight: HTTPS reachable, CA bundle OK")
    except Exception as e:
        msg = str(e)
        if "CERTIFICATE_VERIFY_FAILED" in msg or "SSL" in msg:
            print(
                "# WARN pre-flight: local Python has no CA bundle "
                "(SSL: CERTIFICATE_VERIFY_FAILED on https probe) — every "
                "per-source result will land in 'unreachable'. CI runs unaffected."
            )
        else:
            print(f"# WARN pre-flight: {msg[:160]}")
    print()

    def _probe(s: dict[str, Any]) -> dict[str, Any]:
        sid = s.get("id", "")
        url = s.get("url", "")
        src_status = s.get("status", "")
        fetch_method = s.get("fetch_method", "")
        host = (urlparse(url).hostname or "").lower()
        # Probe each source via its ACTUAL recipe, not a blind HEAD of `url`:
        #   api / bridge → exercise the documented tools/fetch_source.py recipe
        #   rss          → fetch the FEED (url may be a hostile homepage)
        #   webfetch/etc → browser-UA HEAD→GET of the url
        #
        # `probe_url` (optional) overrides the probe target for sources whose
        # `url` is a directory/index the publisher blocks while the documented
        # per-item recipe works fine. Probing the blocked index reports a
        # recipe break that does not exist — siemens-productcert-csaf is the
        # worked example: its CSAF directory listing 403s every UA, while the
        # per-advisory `ssa-NNNNNN.json` documents the recipe the runs use and
        # fetches cleanly. `url` stays the human-facing landing page.
        probe_target = s.get("probe_url") or url
        if fetch_method in ("api", "bridge", "jina"):
            cls, detail = _bridge_check(sid, probe_target, timeout=max(args.timeout, 45.0),
                                        fetch_method=fetch_method)
            status = None
            latency_ms = 0
            err = "" if cls == "bridge-ok" else detail
        elif fetch_method == "rss":
            cls, detail, status = _rss_check(s, host, timeout=args.timeout)
            latency_ms = 0
            err = "" if cls in _HEALTHY_CLASSES else detail
        else:
            status, latency_ms, err = _check(url, timeout=args.timeout)
            cls = _classify(status, host)
            # Universal fallback: a direct probe that anti-bot-blocked (403/429)
            # or was transport-unreachable may still be readable through the
            # r.jina.ai reader — the same auto-fallback the `url` command and the
            # agents' tier-3 transport use. If the reader reaches it, the source
            # IS fetchable cleanly, so class it `jina-ok` (healthy) rather than
            # floating it as an unsolved block.
            if cls not in _HEALTHY_CLASSES and (status in (403, 429) or status is None):
                if _jina_reachable(url, timeout=args.timeout):
                    cls = "jina-ok"
                    err = ""
        action, action_reason = _action(src_status, fetch_method, cls, status, sid)
        content = _content_assess(s, timeout=max(args.timeout, 30.0),
                                  now=datetime.now(timezone.utc))
        verdict = content["content_verdict"]
        if src_status != "demoted" and verdict != "relevant":
            if action == "none":
                action = "stale-content" if verdict == "stale" else "needs-content-fix"
                action_reason = _CONTENT_FAIL_REASON[verdict]
                if cls in ("reader-quota", "bridge-blocked") and verdict == "unreadable":
                    action_reason = ("no free transport reads this host and the metered reader "
                                     "pool is empty, so nothing verifies its content this sweep "
                                     "(refill JINA_API_KEYS or find a direct recipe)")
                if verdict == "stale":
                    action_reason += (f" (newest {content['newest_item']}, "
                                      f"{content['newest_item_age_days']} d > "
                                      f"{content['max_staleness_days']} d)")
            else:
                action_reason += f"; content: {verdict}"
        elif fetch_method == "blocked" and verdict == "relevant":
            action, action_reason = ("needs-content-fix",
                                     "marked `blocked` but a direct transport now reads relevant "
                                     f"content ({content['content_transport']}) — restore a working "
                                     "fetch_method")
        elif fetch_method == "jina" and verdict == "relevant" \
                and content["content_transport"] != "jina":
            action_reason = ("pinned to the metered jina reader, but the free direct transports "
                             "read it; consider fetch_method bridge")
        rec = {
            "id": sid,
            "url": url,
            "host": host,
            "status": src_status,
            "fetch_method": fetch_method,
            "status_code": status,
            "latency_ms": latency_ms,
            "class": cls,
            "action": action,
            "action_reason": action_reason,
            "fetched_at": fetched_at,
            **content,
        }
        if err:
            rec["error"] = err
        return rec

    # Previous snapshot's `latest` — carried forward for sources the budget
    # doesn't reach, so the written snapshot always covers EVERY source.
    prev_latest: dict[str, Any] = {}
    if STATE_JSON.exists():
        try:
            prev_latest = dict(json.loads(
                STATE_JSON.read_text(encoding="utf-8")).get("latest") or {})
        except Exception:  # noqa: BLE001
            prev_latest = {}

    # Parallel sweep with an overall wall-clock budget. Sequentially, 150+
    # sources × (retry + jina fallback + 45 s bridge subprocesses) has blown
    # every in-run budget it was given (observed 2026-06-21, 2026-07-05,
    # 2026-07-08); parallel workers bring the typical sweep to ~2–4 min and
    # the budget guarantees a bounded, complete write even on a bad day.
    # NOTE: probes already running at the deadline are bounded by their own
    # subprocess timeouts (≤ ~90 s), so worst-case overrun ≈ one probe.
    t_sweep0 = time.monotonic()
    deadline = (t_sweep0 + args.budget) if args.budget > 0 else None
    results_by_id: dict[str, dict[str, Any]] = {}
    budget_hit = False
    pool = ThreadPoolExecutor(max_workers=max(1, args.workers))
    try:
        pending = {pool.submit(_probe, s): s.get("id", "") for s in sources}
        while pending:
            budget_left = None if deadline is None else deadline - time.monotonic()
            if budget_left is not None and budget_left <= 0:
                budget_hit = True
                break
            done, _ = wait(set(pending), timeout=budget_left,
                           return_when=FIRST_COMPLETED)
            if not done:
                budget_hit = True
                break
            for fut in done:
                sid = pending.pop(fut)
                try:
                    rec = fut.result()
                except Exception as e:  # noqa: BLE001 — a probe crash is data, not fatal
                    rec = {"id": sid, "url": "", "host": "", "status": "",
                           "fetch_method": "", "status_code": None, "latency_ms": 0,
                           "class": "unreachable", "action": "needs-demote",
                           "action_reason": f"probe crashed: {str(e)[:120]}",
                           "fetched_at": fetched_at, "error": str(e)[:160]}
                results_by_id[rec["id"]] = rec
                st_disp = str(rec["status_code"]) if rec["status_code"] is not None else "—"
                flag = "" if rec["action"] == "none" else f"  ⚠ {rec['action']}"
                print(f"  [{rec['class']:>13}] {st_disp:>3}  {rec['latency_ms']:>5} ms  "
                      f"{rec['id']:<32}  {rec['host']}{flag}")
    finally:
        pool.shutdown(wait=False, cancel_futures=True)

    # Assemble the complete result set in source order: fresh probes first
    # choice, previous snapshot carried forward second, `not-probed` last.
    results: list[dict[str, Any]] = []
    carried = 0
    unprobed_new = 0
    for s in sources:
        sid = s.get("id", "")
        if sid in results_by_id:
            results.append(results_by_id[sid])
            continue
        prev = prev_latest.get(sid)
        if isinstance(prev, dict) and prev.get("id") == sid:
            rec = dict(prev)
            rec["carried_forward"] = True
            carried += 1
        else:
            rec = {"id": sid, "url": s.get("url", ""),
                   "host": (urlparse(s.get("url", "")).hostname or "").lower(),
                   "status": s.get("status", ""),
                   "fetch_method": s.get("fetch_method", ""),
                   "status_code": None, "latency_ms": 0, "class": "not-probed",
                   "action": "none",
                   "action_reason": "probe budget exhausted before this source; no prior snapshot to carry",
                   "fetched_at": fetched_at}
            unprobed_new += 1
        results.append(rec)
    if budget_hit:
        print(f"\n# WARN budget: {args.budget:.0f}s budget exhausted after "
              f"{time.monotonic() - t_sweep0:.0f}s — probed {len(results_by_id)}/"
              f"{len(sources)}; carried forward {carried} from the previous "
              f"snapshot; {unprobed_new} not-probed (no prior)")
    else:
        print(f"\n# sweep complete: {len(results_by_id)}/{len(sources)} probed "
              f"in {time.monotonic() - t_sweep0:.0f}s "
              f"(workers={args.workers}, budget={args.budget:.0f}s)")

    # Group counts for quick top-line.
    by_class: dict[str, int] = {}
    by_action: dict[str, int] = {}
    for r in results:
        by_class[r["class"]] = by_class.get(r["class"], 0) + 1
        by_action[r["action"]] = by_action.get(r["action"], 0) + 1
    print()
    by_verdict: dict[str, int] = {}
    for r in results:
        v = r.get("content_verdict") or "not-assessed"
        by_verdict[v] = by_verdict.get(v, 0) + 1
    print("# content verdicts:")
    for v in ("relevant", "stale", "irrelevant", "shell", "unreadable", "not-assessed"):
        if by_verdict.get(v):
            print(f"  {by_verdict[v]:>3}× {v}")
    print("# class breakdown:")
    for cls in ("ok", "redirect-ok", "bridge-ok", "jina-ok", "ua-blocked", "bridge-blocked",
                "reader-quota", "client-error", "server-error", "unreachable", "bridge-fail",
                "not-probed"):
        n = by_class.get(cls, 0)
        if n:
            print(f"  {n:>3}× {cls}")
    print("# action breakdown (dashboard floats non-`none`):")
    for act in ("none", "needs-bridge", "needs-demote", "needs-content-fix", "stale-content"):
        n = by_action.get(act, 0)
        if n:
            print(f"  {n:>3}× {act}")
    flagged = [r for r in results if r["action"] != "none"]
    if flagged:
        print("# UNSOLVED — needs a bridge, a recipe/URL fix, a staleness review, or demotion:")
        for r in flagged:
            print(f"  - {r['id']:<28} [{r['action']}] {r['action_reason']}")

    if args.dry_run:
        print("\n(dry-run — state/source_health.json not written)")
        return 0

    # Append-with-cap to state/source_health.json. The schema is two top-level
    # arrays: `runs` (one entry per snapshot, bounded) and `latest` (the most
    # recent snapshot's results indexed by source id, for fast Ops-dashboard
    # consumption without walking history).
    if STATE_JSON.exists():
        try:
            existing = json.loads(STATE_JSON.read_text(encoding="utf-8"))
        except Exception:
            existing = {}
    else:
        existing = {}
    runs = list(existing.get("runs") or [])
    runs.append({"fetched_at": fetched_at, "results": results,
                 "by_class": by_class, "by_action": by_action, "by_verdict": by_verdict})
    runs = runs[-args.history_cap :]
    out = {
        "schema_version": 3,
        "schema": ("Periodic source health snapshot (every source, read through its own "
                   "recipe). Each result carries reachability (`status`, `fetch_method`, "
                   "`class`) and content (`content_verdict` relevant|stale|irrelevant|shell|"
                   "unreadable, with `content_alnum`, `content_terms`, `newest_item`, "
                   "`newest_item_age_days`), and a derived `action` (none | needs-bridge | "
                   "needs-demote | needs-content-fix | stale-content). The Ops dashboard "
                   "floats only non-`none` actions."),
        "last_updated": fetched_at,
        "history_cap": args.history_cap,
        "runs": runs,
        "latest": {r["id"]: r for r in results},
    }
    STATE_JSON.parent.mkdir(parents=True, exist_ok=True)
    tmp = STATE_JSON.with_suffix(".tmp")
    tmp.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    tmp.replace(STATE_JSON)
    print(f"\nwrote {STATE_JSON.relative_to(ROOT)} ({len(runs)} run(s) retained)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
