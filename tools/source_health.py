#!/usr/bin/env python3
"""tools/source_health.py — independent weekly health-check of every active source.

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
import ipaddress
import json
import socket
import ssl
import subprocess
import sys
import time
import urllib.error
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
}
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
TRANSPORT_BLOCKED_UNREACHABLE: frozenset = frozenset()


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
    argv = API_BRIDGE_CMD.get(source_id) or default
    why = ""
    # One transient retry — the same Cloudflare/rate-limit blip handling as _check.
    for attempt in (1, 2):
        try:
            proc = subprocess.run(
                [sys.executable, str(FETCH_SOURCE), *argv],
                capture_output=True, text=True, timeout=timeout,
            )
        except subprocess.TimeoutExpired:
            why = f"timed out after {timeout:.0f}s"
        except Exception as e:  # noqa: BLE001
            why = f"error: {str(e)[:120]}"
        else:
            out = proc.stdout or ""
            if proc.returncode == 0 and len(out.strip()) >= BRIDGE_MIN_BYTES:
                return "bridge-ok", f"bridge `{' '.join(argv)}` → {len(out)} B"
            tail = (proc.stderr or out or "").strip().splitlines()
            why = tail[-1][:140] if tail else f"rc={proc.returncode}, {len(out)} B"
        if attempt == 1:
            time.sleep(1.5)
    detail = f"bridge `{' '.join(argv)}` failed: {why}"
    # A jina reader HTTP 402 is an ACCOUNT-level block, not a per-source recipe
    # death: the JINA_API_KEY token balance is exhausted, so EVERY jina fetch
    # (and every `url` auto-fallback) this run 402s identically regardless of
    # the source. The hard rule forbids demoting on a transport block (402 /
    # 403 / 429), so this must not churn every jina-method source as an unsolved
    # `needs-demote` while the key is down — it is a single operator fix (top up
    # JINA_API_KEY; `jina-usage` confirms the balance), not N source regressions.
    # Its own class keeps it visible without flagging it as an unsolved fault.
    if "402" in why and ("balance exhausted" in why.lower()
                         or "jina_api_key" in why.lower()
                         or "reader proxy http 402" in why.lower()):
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


def _feed_ok(feed_url: str, *, timeout: float) -> bool:
    """True iff the bridge can parse `feed_url` as a feed AND it carries ≥1
    item. A homepage that isn't a feed parses to 0 items → False, so this does
    not give a false OK on a non-feed URL."""
    try:
        proc = subprocess.run(
            [sys.executable, str(FETCH_SOURCE), "feed", feed_url, "3"],
            capture_output=True, text=True, timeout=timeout,
        )
    except Exception:  # noqa: BLE001
        return False
    if proc.returncode != 0:
        return False
    try:
        data = json.loads(proc.stdout or "{}")
    except Exception:  # noqa: BLE001
        return False
    return int(data.get("count") or 0) > 0


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
    # jina reader key balance exhausted (HTTP 402) — an account-level transport
    # block hitting every jina source uniformly this run, not a source fault.
    # 402 never demotes (same hard rule as 403/429); the fix is operator-side.
    if cls == "reader-quota":
        return "none", ("jina reader key balance exhausted (HTTP 402) — account-level "
                        "transport block affecting every jina source uniformly this run, "
                        "not a source fault; 402 never demotes. Top up JINA_API_KEY "
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
    p.add_argument("--budget", type=float, default=420.0,
                   help="overall wall-clock budget in seconds (default 420; 0 = "
                        "unlimited). On exhaustion, un-probed sources carry the "
                        "previous snapshot's result forward and the snapshot "
                        "still writes complete.")
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
        if fetch_method in ("api", "bridge", "jina"):
            cls, detail = _bridge_check(sid, url, timeout=max(args.timeout, 45.0),
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
    print("# class breakdown:")
    for cls in ("ok", "redirect-ok", "bridge-ok", "jina-ok", "ua-blocked", "bridge-blocked",
                "reader-quota", "client-error", "server-error", "unreachable", "bridge-fail",
                "not-probed"):
        n = by_class.get(cls, 0)
        if n:
            print(f"  {n:>3}× {cls}")
    print("# action breakdown (dashboard floats non-`none`):")
    for act in ("none", "needs-bridge", "needs-demote"):
        n = by_action.get(act, 0)
        if n:
            print(f"  {n:>3}× {act}")
    flagged = [r for r in results if r["action"] != "none"]
    if flagged:
        print("# UNSOLVED — needs a dedicated bridge fetcher or demotion:")
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
                 "by_class": by_class, "by_action": by_action})
    runs = runs[-args.history_cap :]
    out = {
        "schema_version": 2,
        "schema": ("Periodic source-accessibility snapshot (every source, "
                   "api/bridge verified through tools/fetch_source.py). Each result "
                   "carries `status`, `fetch_method`, `class`, and a derived `action` "
                   "(none | needs-bridge | needs-demote). The Ops dashboard floats only "
                   "non-`none` actions — sources that need a dedicated bridge or demotion."),
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
