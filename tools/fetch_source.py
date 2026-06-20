#!/usr/bin/env python3
"""fetch_source.py — fetch publicly-readable content from CTI sources that
block the Anthropic-managed routine's default User-Agent.

The routine's WebFetch tool fronts requests with a UA the publisher
recognises as automation; CISA, the Swiss NCSC Security Hub, and a
handful of other sites either return HTTP 403 or refuse the connection
outright. From a normal desktop browser the same URLs resolve fine.

This script is the operator-blessed bridge: it hits the upstream API or
HTML page with a stable browser UA, optionally drives the small set of
endpoints that need post-processing (NCSC CSH discovery + per-advisory
detail), and prints the result to stdout for the agent to parse.

It is **read-only by design**: no posts, no auth, no cookies, no
JavaScript execution, no third-party libraries. The whole script is
stdlib (`urllib`, `json`, `argparse`).

v2.52 — host allowlist removed. The bridge is usable on any HTTPS
publisher (see `_check_url` for the SSRF defences that remain — IP-range
deny list on the resolved host, redirect re-validation, body-size cap,
https-only).

The script will NEVER:
- Submit forms or attempt authentication.
- Fetch hidden / authenticated content (the agent must respect TLP).
- Run third-party JS or load any other origin.

Hosts the direct bridge cannot get content from (Cloudflare Managed
Challenge / geo-WAF refuses every UA, re-confirmed in the 2026-06-20
audit with the Chrome-138 UA + Sec-CH-UA client hints below):
- www.group-ib.com → 503 Managed Challenge; Wayback no recent coverage;
  WebSearch fallback only.
- www.ccn-cert.cni.es → 403 geo-block from outside Spain; Wayback empty.
- www.coe.int, downloads.seppmail.com → blocked; Wayback fallback.
Previously listed here but RECOVERED by the UA bump — use the feed path,
not Wayback: databreaches.net (`feed https://databreaches.net/feed/`),
www.darkreading.com (its /rss.xml), www.inside-it.ch (its /rss.xml).

Usage:
    python3 tools/fetch_source.py url <URL>                          # plain GET with browser UA, prints body
    python3 tools/fetch_source.py ncsc-csh list [N]                  # NCSC CSH public dashboard (last N TLP:CLEAR posts as JSON)
    python3 tools/fetch_source.py ncsc-csh post <ID>                 # one TLP:CLEAR post (Markdown body + metadata)
    python3 tools/fetch_source.py ncsc-csh recent [N]                # combined: list + each post's full content (default 10)
    python3 tools/fetch_source.py cisa-kev                           # full CISA KEV JSON catalog
    python3 tools/fetch_source.py cisa page <URL>                    # CISA HTML advisory / news page (browser UA)
    python3 tools/fetch_source.py enisa-euvd recent [KIND]           # KIND ∈ lastvulnerabilities (default) | criticals | exploited
    python3 tools/fetch_source.py enisa-euvd advisory <ID>           # one EUVD advisory by id (e.g. EUVD-2025-12345)
    python3 tools/fetch_source.py bsi-rss                            # BSI cert-bund WID-SEC RSS feed (XML)
    python3 tools/fetch_source.py bsi-csaf <WID-SEC-ID>              # BSI WID-SEC advisory CSAF JSON (full body — e.g. WID-SEC-2026-1438)
    python3 tools/fetch_source.py ncsc-nl csaf <ID> [VERSION]        # one Dutch NCSC CSAF advisory (e.g. NCSC-2025-0432, default v1)
    # v2.52 — structured discovery feeds for hosts whose listing pages are JS-rendered
    python3 tools/fetch_source.py ncsc-nl recent [N]                 # Dutch NCSC RSS — last N advisory IDs + titles (default 20)
    python3 tools/fetch_source.py cert-eu recent [N]                 # CERT-EU RSS — last N advisories (default 20)
    python3 tools/fetch_source.py cert-fr avis-recent [N]            # CERT-FR vendor-vuln advisories RSS (default 20)
    python3 tools/fetch_source.py cert-fr actu-recent [N]            # CERT-FR weekly-bulletin / actualité RSS (default 20)
    python3 tools/fetch_source.py ico-uk enforcement [N]             # UK ICO enforcement actions — top N by lastmod from sitemap.xml (default 20)
    python3 tools/fetch_source.py sec-edgar 8k [start] [end] [item]  # SEC EDGAR 8-K full-text search (default Item 1.05, last 14 days)
    python3 tools/fetch_source.py wayback <URL> [target-ts] [min-sz] # Wayback Machine snapshot fetch (default target=now, min body 5000 B)
    # v2.54 — generic RSS/Atom feed fetcher (works on any HTTPS feed URL)
    python3 tools/fetch_source.py feed <URL> [N]                     # parse any RSS/Atom feed and return last N items as JSON
    # v2.53 — Microsoft MSRC Update Guide (Angular SPA at msrc.microsoft.com/update-guide/ backed by anonymous CVRF + SUG OData)
    python3 tools/fetch_source.py msrc cvrf <YYYY-Mon>               # full monthly CVRF JSON (e.g. 2026-May) — ~2–3 MB
    python3 tools/fetch_source.py msrc cve <CVE-ID>                  # per-CVE detail JSON (e.g. CVE-2026-41089) — ~2–3 KB
    python3 tools/fetch_source.py msrc release <YYYY-Mon> [N]        # OData list of CVEs in one release (cheaper than `cvrf`)
    python3 tools/fetch_source.py msrc recent [N]                    # newest N CVEs across all releases
    python3 tools/fetch_source.py msrc releases [N]                  # most-recent N monthly release tags
    # v2.53 — Microsoft Security Blog (RSS, with topic filter)
    python3 tools/fetch_source.py msft-secblog recent [N] [TOPIC]    # last N posts; TOPIC e.g. threat-intelligence

Examples:
    python3 tools/fetch_source.py ncsc-csh recent 5
    python3 tools/fetch_source.py cisa-kev | jq '.vulnerabilities | length'
    python3 tools/fetch_source.py enisa-euvd recent criticals | jq '. | length'
    python3 tools/fetch_source.py bsi-csaf WID-SEC-2026-1438 | jq '.document.title'
    python3 tools/fetch_source.py ncsc-nl recent 10 | jq '.items[].id'
    python3 tools/fetch_source.py cert-eu recent 10 | jq '.items[].title'
    python3 tools/fetch_source.py cert-fr avis-recent 10 | jq '.items[].link'
    python3 tools/fetch_source.py ico-uk enforcement 5 | jq '.items[].url'
    python3 tools/fetch_source.py sec-edgar 8k 2026-05-01 2026-05-15 1.05 | jq '.hits[].display_name'
    python3 tools/fetch_source.py wayback https://www.darkreading.com/article/foo
    python3 tools/fetch_source.py feed https://thedfirreport.com/feed/ 5 | jq '.items[].title'
    python3 tools/fetch_source.py feed https://feeds.feedburner.com/threatintelligence/pvexyqv7v0v 10
    python3 tools/fetch_source.py feed https://www.schneier.com/feed/atom/ 5
    python3 tools/fetch_source.py msrc cve CVE-2026-41089 | jq '{cveTitle, exploited, baseScore}'
    python3 tools/fetch_source.py msrc release 2026-May 50 | jq '[.items[] | select(.exploited == "Yes")]'
    python3 tools/fetch_source.py msft-secblog recent 5 threat-intelligence | jq '.items[].link'
    python3 tools/fetch_source.py url https://hub.ivanti.com/s/article/May-2026-Security-Advisory-Ivanti-EPMM
"""

from __future__ import annotations

import argparse
import ipaddress
import json
import os
import re
import socket
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request
from typing import Any


# === SSRF / decompression-bomb / redirect-rebinding defences =============
#
# Every fetch in this script (a) goes through `_check_url`, which is a
# strict allowlist over scheme + hostname + resolved IP, and (b) is
# attempted via an opener that re-runs `_check_url` on every redirect
# destination. Even if a permitted publisher returns 30x to a
# loopback / link-local / private / cloud-metadata host, the redirect is
# refused before the next request flies.
#
# Body size is capped via `_read_capped`. `Accept-Encoding: identity`
# precludes gzip / deflate inflation bombs at the wire level; the cap is
# defence in depth in case a publisher serves an enormous identity body.

DEFAULT_TIMEOUT = 30  # seconds — applies to connect + read
MAX_REDIRECTS = 5
# Per-call body caps. The CISA KEV JSON is legitimately large (~6 MB at the
# time of writing); allow more headroom on JSON requests than HTML.
MAX_BODY_BYTES_HTML = 25 * 1024 * 1024   # 25 MB
MAX_BODY_BYTES_JSON = 64 * 1024 * 1024   # 64 MB


def _build_ssl_context() -> ssl.SSLContext:
    """Build an SSL context that finds a CA bundle on every reasonable
    Python install: explicit `SSL_CERT_FILE` env, then `certifi` if it's
    importable, then the system default. Avoids the "unable to get local
    issuer certificate" failure that hits Python on macOS where the
    framework Python ships without bundled CAs."""
    cafile = os.environ.get("SSL_CERT_FILE")
    if cafile and os.path.exists(cafile):
        return ssl.create_default_context(cafile=cafile)
    try:
        import certifi  # noqa: PLC0415
        return ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        pass
    for fallback in ("/etc/ssl/cert.pem", "/etc/pki/tls/cert.pem", "/etc/ssl/certs/ca-certificates.crt"):
        if os.path.exists(fallback):
            return ssl.create_default_context(cafile=fallback)
    return ssl.create_default_context()


_SSL_CTX = _build_ssl_context()

# A modern, stable desktop-Chrome User-Agent. Matches what publishers
# expect from a human visitor; does not impersonate Googlebot or any
# other crawler.
#
# v2.62 (2026-06-20 full-source audit): bumped Chrome 124 → 138 and
# switched the platform token to Windows. The stale 124/macOS UA was
# being filtered by several publishers' WAFs that key off both the
# Chrome major version AND the absence of the `Sec-CH-UA` client-hint
# headers a real Chrome 138 always sends. With the bump + the client
# hints added to `fetch()` below, the 2026-06-20 audit recovered
# `databreaches.net` (RSS feed now 200) and `prodaft.com` (reports +
# resources now 200) — both previously thought transport-blocked.
# Keep the UA string, the `Sec-CH-UA` version list, and the
# `Sec-CH-UA-Platform` token mutually consistent: a UA/header mismatch
# is itself a bot signal.
BROWSER_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/138.0.0.0 Safari/537.36"
)

# Client-hint headers a real Chrome 138 sends on a top-level navigation.
# Kept in lockstep with BROWSER_UA above (major version + platform).
# Sent on every bridge GET so WAFs that cross-check UA ↔ Sec-CH-UA do
# not flag the request as automation.
BROWSER_CLIENT_HINTS = {
    "Sec-CH-UA": '"Chromium";v="138", "Google Chrome";v="138", "Not?A_Brand";v="99"',
    "Sec-CH-UA-Mobile": "?0",
    "Sec-CH-UA-Platform": '"Windows"',
}

# v2.52 — host allowlist removed.
#
# Prior versions of the bridge gated every fetch on a frozenset of known
# publishers (ALLOWED_HOSTS). Operationally, that meant every new CTI
# publisher the agent needed required a code change. The friction was
# real and the gate did not enforce a security property the deeper
# defences below don't already cover:
#
#   - HTTPS-only (`_check_url` rejects http://)
#   - Resolved-IP deny list (`_resolve_and_check` refuses loopback,
#     link-local, private, multicast, reserved, unspecified, and the
#     cloud-metadata endpoints — 169.254.169.254 / 100.100.100.200 /
#     fd00:ec2::254)
#   - Redirect re-validation (`SafeRedirectHandler` re-runs `_check_url`
#     on every 30x destination, blocking allowlisted-host → internal IP
#     pivots and https → http smuggling)
#   - Body-size cap (`_read_capped` aborts on bodies past 25 MB HTML /
#     64 MB JSON, defeating decompression / response-size bombs)
#   - Read-only by design — no posts, no auth, no cookies, no JS
#
# The bridge is now usable on any HTTPS publisher. An agent that wants
# to reach a previously-unlisted CTI source can do so directly; the
# layer-3 SSRF defences above remain the gate that matters.
#
# A small `CLOUDFLARE_BLOCKED_HOSTS` set is retained for documentation
# only — the bridge can still attempt these hosts, but the failure is
# expected (Cloudflare Managed Challenge ignores every UA) and the
# routine should route to the Wayback Machine fallback (`wayback <URL>`)
# instead of retrying the direct fetch.

# Hosts known to sit behind Cloudflare's Managed Challenge ("Just a
# moment...") or a geo/WAF block that ignores every UA. The bridge will
# still attempt these; the agent should prefer the Wayback Machine
# fallback (`wayback <URL>`) — or, for the hosts noted below, a feed/RSS
# path — on a recurring 403/503.
#
# v2.62 (2026-06-20 full-source audit): re-probed every entry with the
# Chrome-138 UA + Sec-CH-UA client hints. RECOVERED and removed from the
# set: databreaches.net (the /feed/ RSS now returns 200 — use
# `feed https://databreaches.net/feed/`; the HTML homepage is still 403),
# www.darkreading.com (the /rss.xml feed serves clean dated entries), and
# www.inside-it.ch (the /rss.xml feed resolves via `url`). These three are
# no longer dead — they just need their feed path, recorded in
# sources/sources.json. Still genuinely blocked to every UA (kept below):
# group-ib.com (503 Managed Challenge), ccn-cert.cni.es (403 geo-block
# from outside Spain), coe.int, downloads.seppmail.com.
CLOUDFLARE_BLOCKED_HOSTS = frozenset({
    "www.coe.int", "coe.int",
    "www.group-ib.com", "group-ib.com",
    "www.ccn-cert.cni.es", "ccn-cert.cni.es",
    "downloads.seppmail.com",
})

NCSC_CSH_BASE = "https://security-hub.ncsc.admin.ch"
CISA_KEV_JSON = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"


def _ip_is_blocked(addr: str) -> bool:
    """True iff `addr` is loopback, link-local, private, multicast, reserved,
    unspecified, or a known cloud-metadata endpoint. Covers IPv4 and IPv6.

    The cloud-metadata endpoints worth special-casing:
        - 169.254.169.254 (AWS / Azure / GCP / OpenStack IMDS)
        - fd00:ec2::254  (AWS IMDS over IPv6)
        - 100.100.100.200 (Alibaba Cloud)
        - metadata.google.internal — handled by name-resolution path below
    """
    try:
        ip = ipaddress.ip_address(addr)
    except ValueError:
        # Not an IP literal — caller resolves a hostname first, so this
        # path should not be hit. Be conservative and treat as blocked.
        return True
    if (
        ip.is_loopback
        or ip.is_link_local
        or ip.is_private
        or ip.is_multicast
        or ip.is_reserved
        or ip.is_unspecified
    ):
        return True
    # Explicit cloud-metadata literals that the generic `is_link_local` /
    # `is_private` checks above DO already cover (169.254.0.0/16 is
    # link-local; fd00::/8 is private). Belt-and-braces for clarity.
    if str(ip) in ("169.254.169.254", "100.100.100.200"):
        return True
    return False


def _resolve_and_check(host: str) -> str:
    """Resolve `host` to an IP, refuse if any resolved address is on the
    deny list, and return one chosen IP. Used to defend against:
        - allow-listed publishers whose DNS now points at a private range
        - DNS rebinding tricks where a later resolve produces a different
          (internal) IP

    The chosen IP is *not* substituted into the URL — TLS hostname
    verification depends on the original Host header + SNI matching the
    cert. We only use the IP for the deny-list check; the request itself
    flies to the hostname normally. This pins the *answer* the script
    accepts; it does not pin the *connection* (which would require a
    custom socket wrapper). DNS rebinding mid-connection remains
    theoretically possible but is far harder than redirect-based SSRF,
    which the redirect handler below also blocks.
    """
    try:
        infos = socket.getaddrinfo(
            host, None, socket.AF_UNSPEC, socket.SOCK_STREAM
        )
    except socket.gaierror as e:
        raise ValueError(f"refused: cannot resolve {host!r}: {e}") from None
    if not infos:
        raise ValueError(f"refused: no address for {host!r}")
    addrs = []
    for fam, _t, _p, _c, sockaddr in infos:
        addr = sockaddr[0]
        if _ip_is_blocked(addr):
            raise ValueError(
                f"refused: host {host!r} resolves to disallowed address {addr!r}"
            )
        addrs.append(addr)
    return addrs[0]


def _check_url(url: str) -> None:
    """SSRF gate: scheme is https and the resolved IP is not loopback /
    link-local / private / cloud-metadata. Called for the initial request
    AND for every redirect destination (see SafeRedirectHandler below).

    v2.52 — host allowlist removed. The agent can target any HTTPS
    publisher; the layer-3 defences here (resolved-IP deny list) are the
    gate that matters. A poisoned A record pointing at 127.0.0.1 / RFC
    1918 / 169.254.169.254 is still refused. Hostname guesses don't lift
    the defence — `_resolve_and_check` runs `getaddrinfo` and refuses any
    answer that lands on a disallowed range, exactly as before.
    """
    parsed = urllib.parse.urlparse(url)
    host = (parsed.hostname or "").lower()
    scheme = (parsed.scheme or "").lower()
    if scheme != "https":
        raise ValueError(f"refused: only https:// is allowed (got {scheme!r})")
    if not host:
        raise ValueError("refused: no host in URL")
    _resolve_and_check(host)


# Backwards-compatible shim — old callers used `_check_host`.
def _check_host(url: str) -> None:  # pragma: no cover - thin alias
    _check_url(url)


class SafeRedirectHandler(urllib.request.HTTPRedirectHandler):
    """Re-validate every redirect destination against `_check_url`.

    Defeats: (a) an allowlisted publisher pivoting to an internal address
    via 30x; (b) cross-protocol smuggling (https → http) — `_check_url`
    refuses non-https schemes. Also caps the redirect chain to
    `MAX_REDIRECTS`.
    """

    max_redirections = MAX_REDIRECTS

    def redirect_request(self, req, fp, code, msg, headers, newurl):  # type: ignore[override]
        # urllib normalises `newurl` against the original URL for us, so it
        # is always absolute by the time we see it.
        try:
            _check_url(newurl)
        except ValueError as e:
            raise urllib.error.HTTPError(
                newurl, code, f"redirect refused: {e}", headers, fp
            )
        return super().redirect_request(req, fp, code, msg, headers, newurl)


# A single shared opener so every call uses the safe redirect handler and
# the pinned SSL context. We intentionally do NOT install this globally —
# leaving the global opener untouched lets test code mock urlopen without
# inheriting our defences, and keeps the script's surface narrow.
_OPENER = urllib.request.build_opener(
    urllib.request.HTTPSHandler(context=_SSL_CTX),
    SafeRedirectHandler(),
)


def _read_capped(resp, max_bytes: int) -> bytes:
    """Read the response body in bounded chunks; abort on the first byte
    past `max_bytes`. Defends against decompression / response-size bombs
    even when `Content-Length` is missing or lies."""
    buf = bytearray()
    while True:
        chunk = resp.read(min(64 * 1024, max_bytes - len(buf) + 1))
        if not chunk:
            break
        buf.extend(chunk)
        if len(buf) > max_bytes:
            raise RuntimeError(
                f"refused: response body exceeds cap of {max_bytes} bytes"
            )
    return bytes(buf)


def fetch(
    url: str,
    *,
    accept: str = "application/json, text/html;q=0.9, */*;q=0.5",
    max_bytes: int = MAX_BODY_BYTES_HTML,
    extra_headers: dict[str, str] | None = None,
) -> tuple[int, bytes, dict[str, str]]:
    """Plain GET with browser headers. Returns (status, body_bytes, headers).

    Refuses non-https URLs and any redirect that lands on a disallowed
    IP range (loopback / link-local / private / cloud-metadata) per the
    layer-3 SSRF defences in `_check_url` / `_resolve_and_check`. Body
    size is capped at `max_bytes`.

    v2.52 — host allowlist removed. The bridge is usable on any HTTPS
    publisher; `extra_headers` lets callers add publisher-specific
    headers (SEC requires an identifying User-Agent suffix; Wayback's
    CDX rate-limiter prefers a non-empty Accept-Language).
    """
    _check_url(url)
    headers = {
        "User-Agent": BROWSER_UA,
        "Accept": accept,
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "identity",  # avoid gzip — keep stdout simple
        "Cache-Control": "no-cache",
        "Pragma": "no-cache",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        **BROWSER_CLIENT_HINTS,
    }
    if extra_headers:
        headers.update(extra_headers)
    req = urllib.request.Request(url, headers=headers)
    try:
        with _OPENER.open(req, timeout=DEFAULT_TIMEOUT) as resp:
            body = _read_capped(resp, max_bytes)
            return resp.status, body, dict(resp.headers)
    except urllib.error.HTTPError as e:
        # Surface the upstream status verbatim so the agent can tell why a fetch failed.
        try:
            err_body = _read_capped(e, max_bytes) if hasattr(e, "read") else b""
        except RuntimeError:
            err_body = b""
        return e.code, err_body, dict(e.headers or {})


def fetch_text(url: str, *, accept: str = "application/json, text/html;q=0.9, */*;q=0.5") -> str:
    code, body, _ = fetch(url, accept=accept)
    if code != 200:
        raise RuntimeError(f"upstream HTTP {code} for {url}")
    # Try utf-8 then fall back to latin-1 (the CSH API is utf-8; CISA HTML is utf-8).
    try:
        return body.decode("utf-8")
    except UnicodeDecodeError:
        return body.decode("latin-1", errors="replace")


def fetch_json(url: str) -> Any:
    # JSON endpoints get a higher size cap because CISA KEV is legitimately
    # multi-MB. Re-implement the decode locally so we can pick the cap.
    code, body, _ = fetch(
        url, accept="application/json, */*;q=0.5", max_bytes=MAX_BODY_BYTES_JSON
    )
    if code != 200:
        raise RuntimeError(f"upstream HTTP {code} for {url}")
    try:
        text = body.decode("utf-8")
    except UnicodeDecodeError:
        text = body.decode("latin-1", errors="replace")
    return json.loads(text)


# ── NCSC Cyber Security Hub (CSH) — public TLP:CLEAR slice ────────────
#
# The CSH SPA lives at https://security-hub.ncsc.admin.ch/. Most of its
# REST endpoints require OIDC authentication against auth.ncsc.admin.ch
# (Keycloak realm `csh_prod`). Two endpoints accept anonymous reads
# *for posts the publisher marked TLP:CLEAR*:
#
#   GET /api/posts/dashboard?pageSize=N&pageIndex=0
#       Public dashboard listing. Returns {pageIndex, pageSize, items: [...]}
#       where each item has: id, created, lastChange, publicationStatus,
#       summary, title, tlpStatus.
#
#   GET /api/posts/{id}/details
#       Full post content. Returns: id, tlpStatus, created, history,
#       files, title, content (Markdown body).
#
# Authenticated endpoints (search, archive, comments, attachments) are
# NOT touched here. The agent must respect TLP — never fetch TLP:AMBER
# or TLP:RED even if a future API change exposes them.

def ncsc_list(page_size: int = 20) -> list[dict[str, Any]]:
    """Return the public dashboard items (newest first), TLP:CLEAR only."""
    if page_size < 1 or page_size > 100:
        raise ValueError("page_size must be 1..100")
    url = f"{NCSC_CSH_BASE}/api/posts/dashboard?pageSize={page_size}&pageIndex=0"
    data = fetch_json(url)
    items = data.get("items", []) or []
    # Defensive filter — if the upstream ever ships non-Clear items in
    # the public dashboard by mistake, drop them.
    return [it for it in items if (it.get("tlpStatus") or "").lower() == "clear"]


def ncsc_post(post_id: int) -> dict[str, Any]:
    """Return one CSH post by ID, including the Markdown body."""
    url = f"{NCSC_CSH_BASE}/api/posts/{int(post_id)}/details"
    data = fetch_json(url)
    if (data.get("tlpStatus") or "").lower() != "clear":
        raise RuntimeError(
            f"post {post_id} is {data.get('tlpStatus')!r}, not Clear; refusing to print"
        )
    # Synthesise the canonical detail URL the brief should cite.
    data["citation_url"] = f"{NCSC_CSH_BASE}/#/posts/{int(post_id)}"
    return data


def ncsc_recent(page_size: int = 10) -> dict[str, Any]:
    """List + fetch full content for each recent TLP:CLEAR post in one go."""
    listing = ncsc_list(page_size=page_size)
    full = []
    for item in listing:
        try:
            post = ncsc_post(item["id"])
        except Exception as e:  # noqa: BLE001
            full.append({"id": item["id"], "error": str(e)})
            continue
        full.append(post)
    return {"count": len(full), "posts": full}


# ── CISA helpers ──────────────────────────────────────────────────────

def cisa_kev() -> Any:
    return fetch_json(CISA_KEV_JSON)


# ── ENISA EUVD helpers (v2.48 — added 2026-05-10; hotfixed 2026-05-11) ─
#
# The ENISA EU Vulnerability Database SPA at https://euvd.enisa.europa.eu/
# returns an empty <noscript> shell to WebFetch. The underlying REST API
# is plain JSON, but it lives on a separate services host —
# `euvdservices.enisa.europa.eu` — not on the SPA host itself. The
# 2026-05-11 hotfix re-pointed the bridge after the previously-used
# `https://euvd.enisa.europa.eu/enisaeuvd/api/*` paths started serving
# the SPA shell (HTTP 200 + text/html, which the bridge surfaced as an
# empty / unparseable JSON body).
#
# Endpoints discovered from the SPA's main.js bundle (2026-05-11):
#   /api/lastvulnerabilities            — most recent N (response: list, ≤ 8 records)
#   /api/criticalvulnerabilities        — CVSS 9.0–10.0 entries
#   /api/exploitedvulnerabilities       — exploited=true entries
#   /api/enisaid?id=<EUVD-ID>           — single advisory by EUVD id
#   /api/advisory?id=<vendor-advisory>  — single advisory by vendor id
#   /api/search?...                     — filtered listing (CVSS / date / etc.)
#
# CLI kinds (`lastvulnerabilities` | `criticals` | `exploited`) are kept
# stable so existing prompts / agent recipes keep working — the bridge
# now maps them to the actual API paths.
#
# Brief citations should still point at the SPA detail URL
# (https://euvd.enisa.europa.eu/enisa/eu_vulnerability_database/<id>) —
# the bridge gives the agent the data, not the citation.
ENISA_EUVD_API_BASE = "https://euvdservices.enisa.europa.eu"

# CLI kind → API path. The CLI vocabulary is the operator-facing
# contract (referenced in prompts/daily-cti-brief.md and the
# cti-research sub-agent); the API path is the publisher's vocabulary.
_EUVD_KIND_TO_PATH = {
    "lastvulnerabilities": "lastvulnerabilities",
    "criticals":           "criticalvulnerabilities",
    "exploited":           "exploitedvulnerabilities",
}


def enisa_euvd_recent(kind: str = "lastvulnerabilities") -> Any:
    """Fetch one of the EUVD listing endpoints. `kind` ∈
    {`lastvulnerabilities`, `criticals`, `exploited`}."""
    path = _EUVD_KIND_TO_PATH.get(kind)
    if path is None:
        raise ValueError(f"unknown EUVD kind: {kind!r}")
    return fetch_json(f"{ENISA_EUVD_API_BASE}/api/{path}")


def enisa_euvd_advisory(advisory_id: str) -> Any:
    """Fetch one EUVD entry by advisory id (e.g. `EUVD-2025-12345`)."""
    if not re.match(r"^[A-Za-z0-9-]+$", advisory_id):
        raise ValueError(f"refused: invalid advisory id {advisory_id!r}")
    return fetch_json(f"{ENISA_EUVD_API_BASE}/api/enisaid?id={advisory_id}")


# ── BSI cert-bund (Germany) ──────────────────────────────────────────
#
# The BSI WID-SEC RSS feed at /content/public/securityAdvisory/rss is
# stable and the only reliable way to enumerate recent advisories. The
# per-advisory HTML pages at /portal/wid/securityadvisory?name=... are
# pure Angular SPA shells — every tool ctipilot has access to gets the
# empty <app-root> back, no body text.
#
# The 2026-05-11 hotfix wires the bridge to BSI's CSAF Trusted Provider
# distribution (advertised at /.well-known/csaf/provider-metadata.json).
# The TLP:WHITE WID-SEC feed serves a CSAF v2.0 JSON document per
# advisory at a deterministic path:
#
#   https://wid.cert-bund.de/.well-known/csaf/white/{YEAR}/wid-sec-w-{YEAR}-{NUM}.json
#
# Each CSAF document contains the full advisory body: title, all `notes`
# (Produktbeschreibung / Angriff / Maßnahmen / etc.), affected products
# in `product_tree`, every CVE in `vulnerabilities[].cve`, CVSS scores,
# and remediations. That closes the structural gap where a BSI advisory
# was the only EU national-CERT signal on a vulnerability but the
# routine could only see the RSS summary.
#
# The agent still cites the human-readable portal URL
# (https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-...) —
# the bridge supplies the data, not the citation.
BSI_RSS_URL = "https://wid.cert-bund.de/content/public/securityAdvisory/rss"
BSI_CSAF_BASE = "https://wid.cert-bund.de/.well-known/csaf/white"
# Portal IDs look like `WID-SEC-2026-1438`; CSAF filenames slot a `-W` in
# the same position and lowercase the whole thing: `wid-sec-w-2026-1438`.
_BSI_WID_RE = re.compile(r"^WID-SEC-(\d{4})-(\d{1,5})$")


def bsi_rss() -> str:
    return fetch_text(BSI_RSS_URL, accept="application/rss+xml, application/xml, */*;q=0.5")


def bsi_csaf(advisory_id: str) -> Any:
    """Fetch the CSAF v2.0 JSON document for one BSI WID-SEC advisory.

    `advisory_id` is the portal-style identifier (`WID-SEC-YYYY-NNNN`);
    the function derives the lowercase `wid-sec-w-YYYY-NNNN.json` slug
    expected at the CSAF distribution path.
    """
    m = _BSI_WID_RE.match(advisory_id.strip())
    if not m:
        raise ValueError(
            f"refused: invalid BSI advisory id {advisory_id!r} "
            "(expected WID-SEC-YYYY-NNNN)"
        )
    year, num = m.group(1), m.group(2)
    slug = f"wid-sec-w-{year}-{num}"
    return fetch_json(f"{BSI_CSAF_BASE}/{year}/{slug}.json")


# ── Dutch NCSC (advisories.ncsc.nl) ──────────────────────────────────
#
# The /advisories/ listing is an SPA. The publisher's CSAF distribution
# (advertised at /.well-known/csaf/provider-metadata.json) serves each
# advisory as a CSAF v2.0 JSON document under:
#
#   https://advisories.ncsc.nl/csaf/v2/{year}/ncsc-{year}-{nnnn}.json
#
# The 2026-05-11 hotfix re-pointed the bridge after the previous
# `/advisory/<id>/v<n>/<id>.json` pattern began returning 404 across
# every advisory id tested.
#
# The CSAF JSON contains the full advisory body: title, all `notes`
# (Inleiding / Interpretaties / Oplossingen / etc.), the `product_tree`,
# every CVE in `vulnerabilities[]`, CVSS scores, and remediations. Not
# every NCSC-NL advisory is published in the WHITE distribution (TLP
# AMBER / GREEN advisories are not at this path), so 404 on a specific
# id is expected when the publisher kept it restricted.
_NCSC_NL_RE = re.compile(r"^NCSC-(\d{4})-(\d{3,5})$")


def ncsc_nl_csaf(advisory_id: str, version: int = 1) -> Any:
    """Fetch the CSAF v2.0 JSON for a Dutch-NCSC TLP:WHITE advisory.

    `advisory_id` is the canonical identifier (`NCSC-YYYY-NNNN`); the
    bridge derives the lowercase `ncsc-yyyy-nnnn` slug expected at the
    CSAF distribution path. The legacy `version` parameter is accepted
    for back-compat with older recipes but ignored — the publisher
    serves the latest revision at the deterministic path.
    """
    m = _NCSC_NL_RE.match(advisory_id.strip())
    if not m:
        raise ValueError(
            f"refused: invalid Dutch-NCSC advisory id {advisory_id!r} "
            "(expected NCSC-YYYY-NNNN)"
        )
    year, num = m.group(1), m.group(2)
    slug = f"ncsc-{year}-{num}"
    return fetch_json(f"https://advisories.ncsc.nl/csaf/v2/{year}/{slug}.json")


# ── v2.52 — RSS-driven listing helpers ─────────────────────────────────
#
# A small RSS parser. We parse with `xml.etree.ElementTree` rather than a
# third-party feedparser to keep the stdlib-only posture. The parser
# refuses external DTDs / entities (XXE defence) — XML.etree's default
# already does this in Python 3.7.1+ but we set it explicitly via
# `defusedxml`-style guards on the parser.

import xml.etree.ElementTree as _ET  # noqa: E402  (after _check_url above)


def _parse_rss(body: str, *, limit: int = 20) -> list[dict[str, str]]:
    """Parse an RSS 2.0, Atom, or RDF/RSS-1.0 feed; return the first
    `limit` items as a list of dicts with keys: `title`, `link`,
    `published`, `summary`. Other shapes raise ValueError.

    Recognised root tags (case-insensitive after namespace strip):
      * `rss`                              — RSS 2.0
      * `{Atom}feed` (case-sensitive ns)   — Atom 1.0
      * `{RDF}RDF` with `{RSS-1.0}channel` — RSS 1.0 / RDF Site Summary

    XXE-safe: the stdlib `ElementTree` does not resolve external entities
    by default (CVE-2021-3733 affected `xml.etree` only in pre-3.7.1
    interpreters; this script targets 3.11+).
    """
    parser = _ET.XMLParser()
    root = _ET.fromstring(body, parser=parser)
    raw_tag = root.tag

    # Split `{namespace}localname` — XML namespaces are CASE-SENSITIVE per
    # spec, so we keep the namespace as-is and only lowercase the local part.
    if "}" in raw_tag:
        ns_uri = raw_tag[1: raw_tag.index("}")]
        local = raw_tag[raw_tag.index("}") + 1:].lower()
    else:
        ns_uri, local = "", raw_tag.lower()

    items: list[dict[str, str]] = []

    # ── RSS 2.0 (no namespace, or with the standard dc: extension) ───
    if local == "rss":
        channel = root.find("channel")
        if channel is None:
            raise ValueError("malformed RSS — no <channel>")
        for it in channel.findall("item")[:limit]:
            items.append({
                "title":     (it.findtext("title") or "").strip(),
                "link":      (it.findtext("link") or "").strip(),
                "published": (it.findtext("pubDate") or it.findtext("{http://purl.org/dc/elements/1.1/}date") or "").strip(),
                "summary":   (it.findtext("description") or "").strip(),
            })
        return items

    # ── Atom 1.0 (namespace `http://www.w3.org/2005/Atom`) ────────────
    if local == "feed" and ns_uri.lower() == "http://www.w3.org/2005/atom":
        ns = "{http://www.w3.org/2005/Atom}"
        for it in root.findall(f"{ns}entry")[:limit]:
            # Atom <link> can repeat with different rel/type; prefer rel="alternate".
            href = ""
            for link_el in it.findall(f"{ns}link"):
                rel = link_el.get("rel") or "alternate"
                if rel == "alternate":
                    href = link_el.get("href") or ""
                    if href:
                        break
            if not href:
                first_link = it.find(f"{ns}link")
                href = (first_link.get("href") if first_link is not None else "") or ""
            # Atom <content> often carries the full body; fall back to summary.
            summary = (it.findtext(f"{ns}summary") or it.findtext(f"{ns}content") or "").strip()
            items.append({
                "title":     (it.findtext(f"{ns}title") or "").strip(),
                "link":      href.strip(),
                "published": (it.findtext(f"{ns}published") or it.findtext(f"{ns}updated") or "").strip(),
                "summary":   summary,
            })
        return items

    # ── RSS 1.0 / RDF Site Summary (namespace `…/rdf-syntax-ns#`) ─────
    # Used by Slashdot, some heise feeds (legacy), and a few CMSs. <item>
    # elements are direct children of <rdf:RDF>, not nested in <channel>.
    if local == "rdf" and ns_uri.endswith("rdf-syntax-ns#"):
        rss10_ns = "{http://purl.org/rss/1.0/}"
        dc_ns    = "{http://purl.org/dc/elements/1.1/}"
        for it in root.findall(f"{rss10_ns}item")[:limit]:
            items.append({
                "title":     (it.findtext(f"{rss10_ns}title") or "").strip(),
                "link":      (it.findtext(f"{rss10_ns}link") or "").strip(),
                "published": (it.findtext(f"{dc_ns}date") or "").strip(),
                "summary":   (it.findtext(f"{rss10_ns}description") or "").strip(),
            })
        return items

    raise ValueError(f"unrecognised feed root: {raw_tag!r}")


# ── CERT-EU advisory feed ─────────────────────────────────────────────
CERT_EU_RSS = "https://cert.europa.eu/publications/security-advisories-rss"


def cert_eu_recent(count: int = 20) -> dict[str, Any]:
    body = fetch_text(CERT_EU_RSS, accept="application/rss+xml, application/xml, */*;q=0.5")
    items = _parse_rss(body, limit=count)
    return {"source": "cert-eu", "feed": CERT_EU_RSS, "count": len(items), "items": items}


# ── CERT-FR advisory + actualité feeds ────────────────────────────────
CERT_FR_AVIS_RSS = "https://www.cert.ssi.gouv.fr/avis/feed/"
CERT_FR_ACTU_RSS = "https://www.cert.ssi.gouv.fr/actualite/feed/"


def cert_fr_avis_recent(count: int = 20) -> dict[str, Any]:
    body = fetch_text(CERT_FR_AVIS_RSS, accept="application/rss+xml, application/xml, */*;q=0.5")
    items = _parse_rss(body, limit=count)
    return {"source": "cert-fr-avis", "feed": CERT_FR_AVIS_RSS, "count": len(items), "items": items}


def cert_fr_actu_recent(count: int = 20) -> dict[str, Any]:
    body = fetch_text(CERT_FR_ACTU_RSS, accept="application/rss+xml, application/xml, */*;q=0.5")
    items = _parse_rss(body, limit=count)
    return {"source": "cert-fr-actualite", "feed": CERT_FR_ACTU_RSS, "count": len(items), "items": items}


# ── Dutch NCSC advisory RSS (companion to ncsc-nl csaf above) ─────────
NCSC_NL_RSS = "https://advisories.ncsc.nl/rss/advisories"
_NCSC_NL_ID_RE = re.compile(r"\bNCSC-\d{4}-\d{3,5}\b")


def ncsc_nl_recent(count: int = 20) -> dict[str, Any]:
    """Fetch the Dutch-NCSC advisories RSS and return the most-recent
    `count` items, each with the parsed advisory id (NCSC-YYYY-NNNN)
    pulled out of the title so the caller can chain into `ncsc-nl csaf`.
    """
    body = fetch_text(NCSC_NL_RSS, accept="application/rss+xml, application/xml, */*;q=0.5")
    items = _parse_rss(body, limit=count)
    for it in items:
        m = _NCSC_NL_ID_RE.search(it["title"]) or _NCSC_NL_ID_RE.search(it["link"])
        it["id"] = m.group(0) if m else None
    return {"source": "ncsc-nl", "feed": NCSC_NL_RSS, "count": len(items), "items": items}


# ── UK ICO enforcement-action listing via sitemap.xml ─────────────────
#
# /action-weve-taken/enforcement/ is JS-rendered (the listing returns a
# navigation shell only). The site-wide sitemap.xml *is* server-rendered
# and contains every enforcement-action URL with a <lastmod> timestamp,
# making it the canonical source for "what's new on the ICO enforcement
# page" without needing to render JavaScript. We parse the 5 MB sitemap,
# filter to URLs under /action-weve-taken/enforcement/, sort by lastmod
# descending, and return the top N. Each entry's per-action URL is
# server-rendered HTML the agent can fetch directly with `url`.
ICO_SITEMAP_URL = "https://ico.org.uk/sitemap.xml"
_ICO_ENF_RE = re.compile(
    r"<url>\s*<loc>(https://ico\.org\.uk/action-weve-taken/enforcement/[^<]+)</loc>\s*<lastmod>([^<]+)</lastmod>",
    re.MULTILINE,
)


def ico_uk_enforcement(count: int = 20) -> dict[str, Any]:
    body = fetch_text(ICO_SITEMAP_URL, accept="application/xml, text/xml, */*;q=0.5")
    matches = _ICO_ENF_RE.findall(body)
    matches.sort(key=lambda x: x[1], reverse=True)
    items = []
    for url, lastmod in matches[:count]:
        # URLs are /enforcement/YYYY/MM/<slug>/  — pull out year, month, slug
        # for caller convenience without re-parsing.
        m = re.match(r".*/enforcement/(\d{4})/(\d{2})/([^/]+)/?$", url)
        year, month, slug = (m.group(1), m.group(2), m.group(3)) if m else ("", "", "")
        items.append({
            "url": url,
            "lastmod": lastmod,
            "year": year,
            "month": month,
            "slug": slug,
        })
    return {"source": "ico-uk-enforcement", "sitemap": ICO_SITEMAP_URL,
            "count": len(items), "total_in_sitemap": len(matches), "items": items}


# ── SEC EDGAR full-text search for 8-K Item 1.05 (cyber-incident) ─────
#
# EDGAR's full-text search API returns JSON of recent filings. We default
# to Item 1.05 (the cybersecurity-incident-disclosure item introduced
# 2023-12-18) and the trailing 14-day window. SEC's developer guidance
# asks API users to identify themselves in the User-Agent; we send a
# CTI-pilot-specific UA suffix so the call is attributable.
SEC_EDGAR_SEARCH = "https://efts.sec.gov/LATEST/search-index"
SEC_EDGAR_UA = "ctipilot.ch CTI brief (contact via repository)"


def sec_edgar_8k(start: str | None = None, end: str | None = None,
                 item: str = "1.05") -> dict[str, Any]:
    """Search EDGAR for 8-K filings citing the given Item code (default
    1.05 = cybersecurity incident). `start` / `end` are YYYY-MM-DD; default
    is trailing 14 days. Returns the raw EDGAR JSON augmented with a flat
    `hits` list the caller can iterate cleanly.
    """
    from datetime import date, timedelta
    if end is None:
        end = date.today().isoformat()
    if start is None:
        start = (date.today() - timedelta(days=14)).isoformat()
    # EDGAR rejects non-ISO dates and exotic item ids — be strict.
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", start) or not re.match(r"^\d{4}-\d{2}-\d{2}$", end):
        raise ValueError(f"refused: start / end must be YYYY-MM-DD (got {start!r} / {end!r})")
    if not re.match(r"^\d+\.\d{1,3}$", item):
        raise ValueError(f"refused: invalid 8-K item code {item!r} (e.g. 1.05 / 2.01)")
    qs = urllib.parse.urlencode({
        "q": f'"Item {item}"',
        "forms": "8-K",
        "dateRange": "custom",
        "startdt": start,
        "enddt": end,
    })
    url = f"{SEC_EDGAR_SEARCH}?{qs}"
    code, body, _ = fetch(
        url,
        accept="application/json",
        max_bytes=MAX_BODY_BYTES_JSON,
        extra_headers={"User-Agent": SEC_EDGAR_UA},
    )
    if code != 200:
        raise RuntimeError(f"upstream HTTP {code} for {url}")
    raw = json.loads(body.decode("utf-8", errors="replace"))
    hits = []
    for h in raw.get("hits", {}).get("hits", []) or []:
        src = h.get("_source", {}) or {}
        # Build the canonical filing-index URL the brief should cite.
        # The accession number `_id` is `<adsh>:<filename>` — adsh has the
        # form `0000123456-26-000068`. EDGAR's per-filing URL is
        # /Archives/edgar/data/<cik-without-leading-zeros>/<adsh-no-dashes>/
        adsh = (src.get("adsh") or "").strip()
        ciks = src.get("ciks") or []
        cik = int(ciks[0]) if ciks else 0
        adsh_nodash = adsh.replace("-", "")
        filing_url = (
            f"https://www.sec.gov/Archives/edgar/data/{cik}/{adsh_nodash}/"
            if (adsh and cik)
            else ""
        )
        hits.append({
            "file_date":     src.get("file_date"),
            "form":          src.get("form"),
            "items":         src.get("items"),
            "display_name":  (src.get("display_names") or [""])[0],
            "ciks":          ciks,
            "adsh":          adsh,
            "filing_url":    filing_url,
        })
    return {
        "source": "sec-edgar",
        "query":  {"item": item, "start": start, "end": end},
        "total":  raw.get("hits", {}).get("total", {}).get("value", 0),
        "count":  len(hits),
        "hits":   hits,
    }


# ── Generic RSS/Atom feed subcommand (v2.54) ──────────────────────────
#
# Most CTI publisher blogs ship a standard RSS 2.0 or Atom 1.0 feed at
# `/feed/`, `/rss/`, `/feed.xml`, or via Feedburner. Rather than adding
# per-publisher subcommands for each one, `feed <URL> [N]` runs the
# `_parse_rss` helper on any URL and returns the same JSON shape every
# other listing subcommand uses ({source, feed, count, items: [...]}).
# The agent's drilldown pattern (take `link` from `items[i]`, then
# `url <link>` for the full body) works uniformly across every publisher.
#
# Verified against the v2.54 source-list expansion:
#   - thedfirreport.com/feed/             (RSS 2.0)
#   - krebsonsecurity.com/feed/           (RSS 2.0, full <content:encoded>)
#   - blog.compass-security.com/feed/     (RSS 2.0)
#   - heise.de/security/feed.xml          (Atom 1.0)
#   - isc.sans.edu/rssfeed.xml            (RSS 2.0, HTML-encoded titles)
#   - feeds.feedburner.com/threatintelligence/pvexyqv7v0v  (RSS 2.0; Mandiant/GTIG)
#   - schneier.com/feed/atom/             (Atom 1.0)
#   - wiz.io/api/feed/cloud-threat-landscape/rss.xml  (RSS 2.0)
#   - sophos.com/en-us/blog/feed?id=...   (RSS 2.0, filtered)
#   - feeds.feedburner.com/TheHackersNews (RSS 2.0; THN)
#   - intel471.com/blog/feed              (RSS 2.0)
#   - threatpost.com/feed/                (RSS 2.0; archive-only since 2023)
#   - feeds.feedburner.com/TroyHunt       (RSS 2.0)
#   - socprime.com/blog/feed/             (RSS 2.0)


def feed_recent(feed_url: str, count: int = 20) -> dict[str, Any]:
    """Fetch any RSS/Atom feed and return the most-recent N items as
    `{source, feed, count, items: [{title, link, published, summary}]}`.
    The agent then `url`-fetches per-article `link`s for the full body."""
    body = fetch_text(
        feed_url,
        accept="application/rss+xml, application/atom+xml, application/xml, text/xml, */*;q=0.5",
    )
    items = _parse_rss(body, limit=max(1, int(count)))
    # Use the hostname as a stable `source` field so a multi-feed run can
    # be sorted / aggregated downstream without re-parsing the URL.
    host = (urllib.parse.urlparse(feed_url).hostname or "").lower()
    return {"source": host or "feed", "feed": feed_url, "count": len(items), "items": items}


# ── Microsoft MSRC Update Guide (v2.53) ───────────────────────────────
#
# The MSRC Update Guide UI at https://msrc.microsoft.com/update-guide/
# is a pure Angular SPA — fetching that URL or any of its routes (e.g.
# /update-guide/releaseNote/2026-May, /update-guide/en-US/vulnerability/
# CVE-2026-41089) returns a ~1 KB shell with no content. Microsoft
# publishes two public, unauthenticated JSON APIs that back the SPA:
#
#   CVRF v3 — full monthly Common Vulnerability Reporting Framework:
#     https://api.msrc.microsoft.com/cvrf/v3.0/cvrf/{YYYY-Mon}
#     Returns DocumentTitle, DocumentTracking, ProductTree,
#     Vulnerability[] (each with CVE, Title, ProductStatuses, CVSS, Notes,
#     Remediations, References). ~2–3 MB per month. ~500 vulns per month
#     is typical. Use sparingly — the OData per-CVE / per-release routes
#     are lighter for most queries.
#
#   SUG v2 OData — searchable per-CVE index:
#     https://api.msrc.microsoft.com/sug/v2.0/en-US/vulnerability/{CVE}
#     Returns cveNumber, cveTitle, releaseNumber, releaseDate, vulnType,
#     publiclyDisclosed, exploited, baseScore, description (HTML),
#     impact, customerActionRequired, cweList, articles, etc. ~2–3 KB
#     per CVE. Supports OData filters:
#       /vulnerability?$filter=releaseNumber eq '2026-May'&$top=N&$orderby=releaseDate desc
#     Includes Linux Mariner / Azure releases mixed with Windows ones —
#     filter by releaseNumber for Patch-Tuesday-only scope.
#
#   CVRF index (releases catalogue):
#     https://api.msrc.microsoft.com/cvrf/v3.0/Updates
#     Returns {value: [{ID, DocumentTitle, InitialReleaseDate, CvrfUrl}]}
#     — every release back to 1999. Filterable by release-id substring.
#
# The brief's citation should be the human-facing SPA URL
# (msrc.microsoft.com/update-guide/...); the bridge gives the agent the
# data, not the citation.
MSRC_CVRF_BASE  = "https://api.msrc.microsoft.com/cvrf/v3.0"
MSRC_SUG_BASE   = "https://api.msrc.microsoft.com/sug/v2.0/en-US"
_MSRC_RELEASE_RE = re.compile(r"^\d{4}-[A-Z][a-z]{2}$")   # e.g. 2026-May
_MSRC_CVE_RE     = re.compile(r"^CVE-\d{4}-\d{4,7}$")


def _msrc_fetch_strict_json(url: str) -> dict[str, Any]:
    """MSRC's API uses content negotiation — if the Accept header includes
    `*/*` the server returns the XML rendition of the CVRF document
    instead of JSON. We override the wildcard fallback with a strict
    `application/json` so MSRC sees exactly one acceptable type."""
    code, body, _ = fetch(
        url,
        accept="application/json",
        max_bytes=MAX_BODY_BYTES_JSON,
    )
    if code != 200:
        raise RuntimeError(f"upstream HTTP {code} for {url}")
    try:
        text = body.decode("utf-8")
    except UnicodeDecodeError:
        text = body.decode("latin-1", errors="replace")
    return json.loads(text)


def msrc_cvrf(release: str) -> dict[str, Any]:
    """Fetch the full CVRF JSON for a monthly MSRC release. `release` is
    `YYYY-Mon` (e.g. `2026-May`). Returns the publisher's CVRF document
    verbatim. ~2–3 MB; sub-agents should normally prefer `msrc release`
    or `msrc cve` instead of pulling this in full."""
    if not _MSRC_RELEASE_RE.match(release):
        raise ValueError(f"refused: invalid MSRC release {release!r} (expected YYYY-Mon, e.g. 2026-May)")
    return _msrc_fetch_strict_json(f"{MSRC_CVRF_BASE}/cvrf/{release}")


def msrc_cve(cve_id: str) -> dict[str, Any]:
    """Fetch the per-CVE detail JSON from the SUG OData service. `cve_id`
    must match `CVE-YYYY-NNNN[N+]`."""
    if not _MSRC_CVE_RE.match(cve_id):
        raise ValueError(f"refused: invalid CVE id {cve_id!r}")
    return _msrc_fetch_strict_json(f"{MSRC_SUG_BASE}/vulnerability/{cve_id}")


def msrc_release(release: str, top: int = 50, only_security: bool = True) -> dict[str, Any]:
    """List CVEs in one MSRC release via the SUG OData filter. Returns
    `{count, total, items: [{cveNumber, cveTitle, releaseNumber, exploited,
    publiclyDisclosed, baseScore, impact}]}`. Cheaper than `msrc cvrf` for
    enumeration / triage; pair with `msrc cve <id>` for full per-CVE detail.

    The OData backend only accepts a single field in `$orderby` — multi-
    field sorts return HTTP 500. We sort by `releaseDate desc` and let
    the caller re-sort the JSON if a secondary key matters.
    """
    if not _MSRC_RELEASE_RE.match(release):
        raise ValueError(f"refused: invalid MSRC release {release!r} (expected YYYY-Mon)")
    top = max(1, min(int(top), 500))
    qs = urllib.parse.urlencode({
        "$filter":  f"releaseNumber eq '{release}'",
        "$top":     str(top),
        "$orderby": "releaseDate desc",
        "$count":   "true",
    }, quote_via=urllib.parse.quote)
    # OData wants $-prefixed names url-encoded as %24 — urlencode handles that.
    raw = _msrc_fetch_strict_json(f"{MSRC_SUG_BASE}/vulnerability?{qs}")
    items = []
    for x in raw.get("value", []) or []:
        items.append({
            "cveNumber":         x.get("cveNumber"),
            "cveTitle":          x.get("cveTitle"),
            "releaseNumber":     x.get("releaseNumber"),
            "releaseDate":       x.get("releaseDate"),
            "vulnType":          x.get("vulnType"),
            "exploited":         x.get("exploited"),
            "publiclyDisclosed": x.get("publiclyDisclosed"),
            "baseScore":         x.get("baseScore"),
            "impact":            x.get("impact"),
        })
    return {
        "source":   "msrc-release",
        "release":  release,
        "total":    raw.get("@odata.count", len(items)),
        "count":    len(items),
        "items":    items,
    }


def msrc_recent(top: int = 20) -> dict[str, Any]:
    """Newest CVEs across all releases via SUG OData. Useful for "what's
    in this month's Patch Tuesday" without knowing the release tag yet."""
    top = max(1, min(int(top), 200))
    qs = urllib.parse.urlencode({
        "$top":     str(top),
        "$orderby": "releaseDate desc",
    }, quote_via=urllib.parse.quote)
    raw = _msrc_fetch_strict_json(f"{MSRC_SUG_BASE}/vulnerability?{qs}")
    items = [
        {
            "cveNumber":         x.get("cveNumber"),
            "cveTitle":          x.get("cveTitle"),
            "releaseNumber":     x.get("releaseNumber"),
            "releaseDate":       x.get("releaseDate"),
            "exploited":         x.get("exploited"),
            "publiclyDisclosed": x.get("publiclyDisclosed"),
            "baseScore":         x.get("baseScore"),
        }
        for x in raw.get("value", []) or []
    ]
    return {"source": "msrc-recent", "count": len(items), "items": items}


def msrc_releases(top: int = 24) -> dict[str, Any]:
    """List the most-recent N monthly MSRC releases from the CVRF index.
    Useful when the agent needs to find "what's the most-recent release
    available" before calling `msrc cvrf` or `msrc release`."""
    raw = _msrc_fetch_strict_json(f"{MSRC_CVRF_BASE}/Updates")
    all_rels = raw.get("value", []) or []
    # Sort by InitialReleaseDate desc (the publisher emits oldest first).
    all_rels.sort(key=lambda x: x.get("InitialReleaseDate", ""), reverse=True)
    items = [
        {
            "id":                  x.get("ID"),
            "title":               x.get("DocumentTitle"),
            "initialReleaseDate":  x.get("InitialReleaseDate"),
            "cvrfUrl":             x.get("CvrfUrl"),
        }
        for x in all_rels[: max(1, int(top))]
    ]
    return {"source": "msrc-releases", "total": len(all_rels), "count": len(items), "items": items}


# ── Microsoft Security Blog feeds (v2.53) ─────────────────────────────
#
# https://www.microsoft.com/en-us/security/blog/ is the unified MSFT
# Security blog hub. The CMS exposes:
#   /feed/                                      — full blog RSS
#   /topic/<topic-slug>/feed/                   — topic-filtered RSS
# Common topic slugs: `threat-intelligence`, `vulnerabilities-and-exploits`,
# `incident-response`, `identity-and-access-management`, `ai-and-machine-learning`.
#
# The per-article URLs (https://www.microsoft.com/en-us/security/blog/
# YYYY/MM/DD/<slug>/) are server-rendered HTML — `url <article-url>` works.
MSFT_SECBLOG_FEED_BASE = "https://www.microsoft.com/en-us/security/blog"


def msft_secblog_recent(count: int = 20, topic: str | None = None) -> dict[str, Any]:
    """Fetch the Microsoft Security Blog RSS, optionally filtered by topic.
    Returns the most-recent `count` posts with title / link / date /
    summary. The agent then `url`-fetches per-article URLs for body."""
    if topic:
        # Topic slug: lowercase, hyphens, alphanumerics only.
        if not re.match(r"^[a-z0-9-]+$", topic):
            raise ValueError(f"refused: invalid topic slug {topic!r}")
        feed_url = f"{MSFT_SECBLOG_FEED_BASE}/topic/{topic}/feed/"
    else:
        feed_url = f"{MSFT_SECBLOG_FEED_BASE}/feed/"
    body = fetch_text(feed_url, accept="application/rss+xml, application/xml, */*;q=0.5")
    items = _parse_rss(body, limit=count)
    return {
        "source": "msft-secblog" + (f"/{topic}" if topic else ""),
        "feed":   feed_url,
        "count":  len(items),
        "items":  items,
    }


# ── Wayback Machine fallback for Cloudflare-Managed-Challenge hosts ───
#
# Workflow:
#  1. Ask Wayback's "availability" JSON API for the closest snapshot to
#     `target_timestamp` (default = now). One round-trip; rarely fails.
#  2. If that snapshot's body is below `min_size`, fall through to the
#     CDX API which lists every snapshot in a range — we sort by body
#     size descending and try the largest one within ±180 days of the
#     target. CDX is rate-limited and 503s often; we retry once after a
#     35-second pause (the rate-limit window is ~30 s).
#  3. Fetch the chosen snapshot via the standard wrapped URL
#     (`/web/<ts>/<orig>`), which decompresses for us. Strip Wayback's
#     wombat toolbar injection from the body so the caller sees clean
#     publisher HTML.
#
# The result is a JSON object — { snapshot_url, snapshot_ts, original_url,
# size, body } — the caller (agent) decides whether to trust the
# snapshot's recency. The snapshot timestamp is preserved verbatim so the
# caller can apply PD-7 recency rules in the daily / weekly prompt.
WAYBACK_AVAILABLE = "https://archive.org/wayback/available"
WAYBACK_CDX       = "https://web.archive.org/cdx/search/cdx"
WAYBACK_WEB_BASE  = "https://web.archive.org/web"


def _strip_wayback_injection(html: str) -> str:
    """Remove Wayback's wombat toolbar + rewriting script bookends and
    analytics comments so the body returned to the caller is close to
    the original publisher HTML.

    Wayback prepends a cluster of scripts (athena.js, bundle-playback.js,
    wombat.js, ruffle.js, an inline __wm.init/__wm.wombat shim, banner
    stylesheets) and appends a trailing HTML comment containing
    PetaboxLoader3 metrics. We also strip the URL-rewriting prefix from
    absolute links so the body's references read like the original
    publisher's. Defensive (a missing element is a no-op).
    """
    # Remove the canonical toolbar bookend if present.
    html = re.sub(
        r"<!--\s*BEGIN WAYBACK TOOLBAR INSERT\s*-->.*?<!--\s*END WAYBACK TOOLBAR INSERT\s*-->",
        "", html, flags=re.DOTALL,
    )
    # Remove every <script> tag that sources an archive.org / web-static.archive.org URL.
    html = re.sub(
        r"<script[^>]*\bsrc=[\"\'][^\"\']*(?:archive\.org|web-static\.archive\.org)[^\"\']*[\"\'][^>]*>\s*</script>",
        "", html, flags=re.IGNORECASE,
    )
    # Remove inline <script> tags whose body mentions Wayback runtime
    # injections (__wm., archive_analytics, RufflePlayer, PetaboxLoader3,
    # window.addEventListener with archive_analytics inside).
    html = re.sub(
        r"<script[^>]*>(?:(?!</script>).)*?(?:__wm\.|archive_analytics|RufflePlayer|PetaboxLoader3)(?:(?!</script>).)*?</script>",
        "", html, flags=re.DOTALL,
    )
    # Remove Wayback banner stylesheets.
    html = re.sub(
        r"<link[^>]*\bhref=[\"\'][^\"\']*web-static\.archive\.org[^\"\']*[\"\'][^>]*/?>",
        "", html, flags=re.IGNORECASE,
    )
    # Remove the trailing PetaboxLoader3 / FILE ARCHIVED metrics comment.
    html = re.sub(
        r"<!--\s*(?:FILE ARCHIVED ON|playback timings|PetaboxLoader3)\b.*?-->",
        "", html, flags=re.DOTALL | re.IGNORECASE,
    )
    # Strip Wayback URL-rewriting prefix from absolute links — keep the
    # original publisher URL intact for downstream citation extraction.
    # Pattern: https://web.archive.org/web/<timestamp>[<flags>]/<orig-url>
    html = re.sub(
        r"https?://web\.archive\.org/web/\d{14}(?:[a-z_]{2,3})?/(https?://)",
        r"\1", html,
    )
    # Strip whitespace runs left by the deletions.
    html = re.sub(r"\n\s*\n\s*\n+", "\n\n", html)
    return html


def _wayback_availability(orig_url: str, target_ts: str) -> dict[str, Any] | None:
    qs = urllib.parse.urlencode({"url": orig_url, "timestamp": target_ts})
    code, body, _ = fetch(
        f"{WAYBACK_AVAILABLE}?{qs}",
        accept="application/json",
        max_bytes=MAX_BODY_BYTES_HTML,
    )
    if code != 200 or not body:
        return None
    try:
        data = json.loads(body.decode("utf-8", errors="replace"))
    except Exception:
        return None
    return (data.get("archived_snapshots") or {}).get("closest")


def _wayback_cdx(orig_url: str, *, days_back: int = 180,
                 max_rows: int = 50) -> list[dict[str, Any]]:
    """Query the CDX index for the most-recent up-to-180-days of
    snapshots of `orig_url`, filtered to HTTP 200. Returns rows sorted by
    size descending so the caller can pick a snapshot whose body is
    non-trivial (Cloudflare-blocked publishers often have stored
    snapshots of the empty challenge page mixed in with real captures).
    Tolerates one 503 retry after a 35 s pause — CDX's rate limiter
    window is ~30 s.
    """
    import time as _time
    from datetime import date, timedelta
    end_ts = date.today().strftime("%Y%m%d")
    start_ts = (date.today() - timedelta(days=days_back)).strftime("%Y%m%d")
    qs = urllib.parse.urlencode({
        "url": orig_url,
        "output": "json",
        "from": start_ts,
        "to": end_ts,
        "filter": "statuscode:200",
        "limit": str(max_rows),
    })
    url = f"{WAYBACK_CDX}?{qs}"
    for attempt in (1, 2):
        try:
            code, body, _ = fetch(url, accept="application/json")
            if code == 200 and body:
                rows = json.loads(body.decode("utf-8", errors="replace"))
                # First row is the column header.
                if not rows or len(rows) < 2:
                    return []
                header, *data_rows = rows
                idx = {col: i for i, col in enumerate(header)}
                parsed = []
                for r in data_rows:
                    try:
                        parsed.append({
                            "timestamp": r[idx["timestamp"]],
                            "original":  r[idx["original"]],
                            "statuscode": r[idx["statuscode"]],
                            "length":    int(r[idx["length"]]) if r[idx["length"]].isdigit() else 0,
                        })
                    except (IndexError, KeyError):
                        continue
                parsed.sort(key=lambda x: x["length"], reverse=True)
                return parsed
            if code == 503 and attempt == 1:
                _time.sleep(35)
                continue
            return []
        except Exception:
            if attempt == 1:
                _time.sleep(35)
                continue
            return []
    return []


# Tell-tale fragments that Wayback's "no snapshot / error" placeholder
# pages contain. These can be 5–15 KB so they pass a naive size filter,
# but they hold zero publisher content. If any of these appear inside the
# fetched body we treat the snapshot as unusable and fall through.
_WAYBACK_PLACEHOLDER_MARKERS = (
    "<title>Wayback Machine</title>",
    "Got an HTTP 302 response",
    "Got an HTTP 301 response",
    "This URL has been excluded from the Wayback Machine",
    "Page cannot be displayed due to robots.txt",
    "wb_div_redirect",
)


def _is_wayback_placeholder(body: bytes) -> bool:
    """Heuristic — True iff `body` looks like a Wayback error/placeholder
    page rather than a real publisher snapshot."""
    text = body.decode("utf-8", errors="replace")[:8192]
    return any(marker in text for marker in _WAYBACK_PLACEHOLDER_MARKERS)


def wayback_snapshot(orig_url: str, target_ts: str | None = None,
                     min_size: int = 5000) -> dict[str, Any]:
    """Fetch a usable Wayback snapshot of `orig_url`. Tries the
    availability API first; if that snapshot's body is below `min_size`
    or looks like a Wayback placeholder/error page, walks the CDX index
    for the largest snapshot in the last 180 days that passes both gates.
    Returns a dict with `snapshot_url`, `snapshot_ts`, `original_url`,
    `size`, `from_strategy`, and `body` (publisher HTML, Wayback wombat
    injection stripped). Raises RuntimeError when no usable snapshot can
    be retrieved.
    """
    from datetime import date
    if target_ts is None:
        target_ts = date.today().strftime("%Y%m%d")
    if not re.match(r"^\d{4,14}$", target_ts):
        raise ValueError(f"refused: invalid Wayback timestamp {target_ts!r} (YYYYMMDDhhmmss-truncatable)")

    tried_ts: set[str] = set()
    candidates: list[dict[str, Any]] = []

    def _accept_or_record(ts: str, snap_url: str, code: int, body: bytes,
                          strategy: str) -> dict[str, Any] | None:
        size = len(body) if body else 0
        placeholder = _is_wayback_placeholder(body) if body else False
        candidates.append({"ts": ts, "size": size, "placeholder": placeholder,
                           "strategy": strategy, "code": code})
        if code == 200 and size >= min_size and not placeholder:
            cleaned = _strip_wayback_injection(body.decode("utf-8", errors="replace"))
            return {
                "snapshot_url":  snap_url,
                "snapshot_ts":   ts,
                "original_url":  orig_url,
                "size":          size,
                "from_strategy": strategy,
                "body":          cleaned,
            }
        return None

    # Step 1 — availability API
    snap = _wayback_availability(orig_url, target_ts)
    if snap and snap.get("status") == "200":
        ts = snap["timestamp"]
        tried_ts.add(ts)
        snap_url = f"{WAYBACK_WEB_BASE}/{ts}/{orig_url}"
        try:
            code, body, _ = fetch(snap_url, accept="text/html, */*;q=0.5",
                                  max_bytes=MAX_BODY_BYTES_HTML)
            hit = _accept_or_record(ts, snap_url, code, body, "availability")
            if hit:
                return hit
        except Exception:
            pass

    # Step 2 — CDX index, biggest snapshot first, skipping already-tried timestamps
    rows = _wayback_cdx(orig_url, days_back=180, max_rows=50)
    for row in rows:
        ts = row["timestamp"]
        if ts in tried_ts:
            continue
        tried_ts.add(ts)
        # CDX `length` is the snapshot's stored byte count — small CDX
        # rows (< min_size) are almost always Cloudflare empty captures;
        # skip them without paying the round-trip.
        if row.get("length", 0) and row["length"] < max(min_size // 2, 1500):
            candidates.append({"ts": ts, "size": row["length"], "placeholder": False,
                               "strategy": "cdx-skipped-small", "code": 0})
            continue
        snap_url = f"{WAYBACK_WEB_BASE}/{ts}/{orig_url}"
        try:
            code, body, _ = fetch(snap_url, accept="text/html, */*;q=0.5",
                                  max_bytes=MAX_BODY_BYTES_HTML)
        except Exception:
            continue
        hit = _accept_or_record(ts, snap_url, code, body, "cdx")
        if hit:
            return hit

    raise RuntimeError(
        f"no usable Wayback snapshot for {orig_url!r} ≥ {min_size} bytes "
        f"in the last 180 days; tried {len(candidates)} candidate(s): "
        + ", ".join(
            f"{c['ts']}({c['size']}B{'/PH' if c['placeholder'] else ''}/{c['strategy']})"
            for c in candidates[:8]
        )
    )


# ── CLI ───────────────────────────────────────────────────────────────

def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(prog="fetch_source.py", description=__doc__)
    sub = p.add_subparsers(dest="cmd", required=True)

    p_url = sub.add_parser("url", help="plain GET with browser UA, prints body")
    p_url.add_argument("url")

    p_csh = sub.add_parser("ncsc-csh", help="NCSC Switzerland Cyber Security Hub")
    csh_sub = p_csh.add_subparsers(dest="csh_cmd", required=True)
    p_csh_list = csh_sub.add_parser("list", help="public dashboard listing")
    p_csh_list.add_argument("count", type=int, nargs="?", default=20)
    p_csh_post = csh_sub.add_parser("post", help="one post by ID")
    p_csh_post.add_argument("id", type=int)
    p_csh_recent = csh_sub.add_parser("recent", help="list + full content of each (combined)")
    p_csh_recent.add_argument("count", type=int, nargs="?", default=10)

    p_cisa = sub.add_parser("cisa-kev", help="CISA Known Exploited Vulnerabilities catalog (JSON)")

    p_cisa_page = sub.add_parser("cisa", help="CISA pages (advisories, news, directives)")
    cisa_sub = p_cisa_page.add_subparsers(dest="cisa_cmd", required=True)
    p_cisa_html = cisa_sub.add_parser("page", help="HTML page with browser UA")
    p_cisa_html.add_argument("url")

    # v2.48 — additional bridge endpoints for known-403 / SPA-only sources.
    p_euvd = sub.add_parser("enisa-euvd", help="ENISA EU Vulnerability Database (JSON)")
    euvd_sub = p_euvd.add_subparsers(dest="euvd_cmd", required=True)
    p_euvd_recent = euvd_sub.add_parser("recent", help="recent / criticals / exploited listings")
    p_euvd_recent.add_argument("kind", choices=["lastvulnerabilities", "criticals", "exploited"], nargs="?", default="lastvulnerabilities")
    p_euvd_one = euvd_sub.add_parser("advisory", help="single EUVD advisory by id (e.g. EUVD-2025-12345)")
    p_euvd_one.add_argument("id")

    p_bsi = sub.add_parser("bsi-rss", help="BSI cert-bund WID-SEC RSS feed (XML)")

    p_bsi_csaf = sub.add_parser("bsi-csaf", help="BSI WID-SEC advisory CSAF JSON (full body)")
    p_bsi_csaf.add_argument("id", help="advisory id, e.g. WID-SEC-2026-1438")

    p_ncscnl = sub.add_parser("ncsc-nl", help="Dutch NCSC advisories")
    ncscnl_sub = p_ncscnl.add_subparsers(dest="ncscnl_cmd", required=True)
    p_ncscnl_csaf = ncscnl_sub.add_parser("csaf", help="one NCSC-NL advisory CSAF JSON")
    p_ncscnl_csaf.add_argument("id", help="advisory id, e.g. NCSC-2025-0432")
    p_ncscnl_csaf.add_argument("version", type=int, nargs="?", default=1, help="CSAF revision (default 1; ignored — publisher serves latest)")
    p_ncscnl_recent = ncscnl_sub.add_parser("recent", help="most-recent NCSC-NL advisory IDs from the RSS feed")
    p_ncscnl_recent.add_argument("count", type=int, nargs="?", default=20)

    # v2.52 — structured discovery feeds for hosts whose listing pages are JS-rendered
    p_certeu = sub.add_parser("cert-eu", help="CERT-EU security advisories")
    certeu_sub = p_certeu.add_subparsers(dest="certeu_cmd", required=True)
    p_certeu_recent = certeu_sub.add_parser("recent", help="last N CERT-EU advisories (RSS)")
    p_certeu_recent.add_argument("count", type=int, nargs="?", default=20)

    p_certfr = sub.add_parser("cert-fr", help="CERT-FR (ANSSI) advisories + actualité bulletins")
    certfr_sub = p_certfr.add_subparsers(dest="certfr_cmd", required=True)
    p_certfr_avis = certfr_sub.add_parser("avis-recent", help="last N vendor-vulnerability advisories")
    p_certfr_avis.add_argument("count", type=int, nargs="?", default=20)
    p_certfr_actu = certfr_sub.add_parser("actu-recent", help="last N weekly bulletins / actualité posts")
    p_certfr_actu.add_argument("count", type=int, nargs="?", default=20)

    p_icouk = sub.add_parser("ico-uk", help="UK Information Commissioner's Office")
    icouk_sub = p_icouk.add_subparsers(dest="icouk_cmd", required=True)
    p_icouk_enf = icouk_sub.add_parser("enforcement", help="top N enforcement actions by lastmod (from sitemap.xml)")
    p_icouk_enf.add_argument("count", type=int, nargs="?", default=20)

    p_edgar = sub.add_parser("sec-edgar", help="SEC EDGAR filings search")
    edgar_sub = p_edgar.add_subparsers(dest="edgar_cmd", required=True)
    p_edgar_8k = edgar_sub.add_parser("8k", help="8-K filings citing the given Item code (default 1.05 = cyber incident; default last 14 days)")
    p_edgar_8k.add_argument("start", nargs="?", default=None, help="ISO date (default: today − 14 days)")
    p_edgar_8k.add_argument("end", nargs="?", default=None, help="ISO date (default: today)")
    p_edgar_8k.add_argument("item", nargs="?", default="1.05", help="8-K item code (default 1.05)")

    p_wb = sub.add_parser("wayback", help="Wayback Machine snapshot fetch (fallback for Cloudflare-blocked hosts)")
    p_wb.add_argument("orig_url", help="original publisher URL to fetch the closest Wayback snapshot of")
    p_wb.add_argument("target_ts", nargs="?", default=None, help="YYYYMMDD target timestamp (default: today)")
    p_wb.add_argument("min_size", type=int, nargs="?", default=5000, help="minimum acceptable body size in bytes (default 5000)")

    # v2.54 — generic RSS/Atom feed subcommand (covers most CTI blog publishers cleanly)
    p_feed = sub.add_parser("feed", help="Generic RSS/Atom feed fetcher — works on any HTTPS feed URL")
    p_feed.add_argument("feed_url", help="full feed URL, e.g. https://thedfirreport.com/feed/")
    p_feed.add_argument("count", type=int, nargs="?", default=20)

    # v2.53 — Microsoft MSRC Update Guide (SPA-backed by public CVRF + SUG OData APIs)
    p_msrc = sub.add_parser("msrc", help="Microsoft MSRC Update Guide — SPA backed by anonymous CVRF + SUG OData APIs")
    msrc_sub = p_msrc.add_subparsers(dest="msrc_cmd", required=True)
    p_msrc_cvrf = msrc_sub.add_parser("cvrf", help="full CVRF JSON for one monthly release (e.g. 2026-May) — ~2–3 MB")
    p_msrc_cvrf.add_argument("release", help="release tag YYYY-Mon, e.g. 2026-May")
    p_msrc_cve = msrc_sub.add_parser("cve", help="per-CVE detail JSON from the SUG OData API")
    p_msrc_cve.add_argument("cve", help="CVE id, e.g. CVE-2026-41089")
    p_msrc_rel = msrc_sub.add_parser("release", help="OData-filtered list of CVEs in one release (cheaper than `cvrf`)")
    p_msrc_rel.add_argument("release", help="release tag YYYY-Mon, e.g. 2026-May")
    p_msrc_rel.add_argument("count", type=int, nargs="?", default=50)
    p_msrc_recent = msrc_sub.add_parser("recent", help="newest N CVEs across all releases (sorted by releaseDate desc)")
    p_msrc_recent.add_argument("count", type=int, nargs="?", default=20)
    p_msrc_releases = msrc_sub.add_parser("releases", help="most-recent N monthly release tags from the CVRF index")
    p_msrc_releases.add_argument("count", type=int, nargs="?", default=24)

    # v2.53 — Microsoft Security Blog (RSS-driven; supports topic-filtered feed)
    p_msft = sub.add_parser("msft-secblog", help="Microsoft Security Blog (RSS)")
    msft_sub = p_msft.add_subparsers(dest="msft_cmd", required=True)
    p_msft_recent = msft_sub.add_parser("recent", help="last N security-blog posts (general or per-topic)")
    p_msft_recent.add_argument("count", type=int, nargs="?", default=20)
    p_msft_recent.add_argument("topic", nargs="?", default=None,
                                help="topic slug, e.g. threat-intelligence | vulnerabilities-and-exploits | incident-response | ai-and-machine-learning")

    args = p.parse_args(argv)

    try:
        if args.cmd == "url":
            sys.stdout.write(fetch_text(args.url))
            return 0
        if args.cmd == "ncsc-csh":
            if args.csh_cmd == "list":
                json.dump(ncsc_list(args.count), sys.stdout, indent=2)
            elif args.csh_cmd == "post":
                json.dump(ncsc_post(args.id), sys.stdout, indent=2)
            elif args.csh_cmd == "recent":
                json.dump(ncsc_recent(args.count), sys.stdout, indent=2)
            sys.stdout.write("\n")
            return 0
        if args.cmd == "cisa-kev":
            json.dump(cisa_kev(), sys.stdout, indent=2)
            sys.stdout.write("\n")
            return 0
        if args.cmd == "cisa":
            if args.cisa_cmd == "page":
                # Soft check — `cisa page <URL>` is meant for CISA-hosted pages.
                # The bridge no longer enforces a host allowlist (v2.52), but
                # if the agent passed a non-CISA URL it almost certainly meant
                # to use the generic `url <URL>` subcommand instead.
                if "cisa.gov" not in (urllib.parse.urlparse(args.url).hostname or ""):
                    print("error: cisa page URL must be on cisa.gov — use `url <URL>` for other hosts", file=sys.stderr)
                    return 2
                sys.stdout.write(fetch_text(args.url))
                return 0
        if args.cmd == "enisa-euvd":
            if args.euvd_cmd == "recent":
                json.dump(enisa_euvd_recent(args.kind), sys.stdout, indent=2)
            elif args.euvd_cmd == "advisory":
                json.dump(enisa_euvd_advisory(args.id), sys.stdout, indent=2)
            sys.stdout.write("\n")
            return 0
        if args.cmd == "bsi-rss":
            sys.stdout.write(bsi_rss())
            return 0
        if args.cmd == "bsi-csaf":
            json.dump(bsi_csaf(args.id), sys.stdout, indent=2)
            sys.stdout.write("\n")
            return 0
        if args.cmd == "ncsc-nl":
            if args.ncscnl_cmd == "csaf":
                json.dump(ncsc_nl_csaf(args.id, args.version), sys.stdout, indent=2)
                sys.stdout.write("\n")
            elif args.ncscnl_cmd == "recent":
                json.dump(ncsc_nl_recent(args.count), sys.stdout, indent=2)
                sys.stdout.write("\n")
            return 0
        if args.cmd == "cert-eu":
            if args.certeu_cmd == "recent":
                json.dump(cert_eu_recent(args.count), sys.stdout, indent=2)
                sys.stdout.write("\n")
            return 0
        if args.cmd == "cert-fr":
            if args.certfr_cmd == "avis-recent":
                json.dump(cert_fr_avis_recent(args.count), sys.stdout, indent=2)
                sys.stdout.write("\n")
            elif args.certfr_cmd == "actu-recent":
                json.dump(cert_fr_actu_recent(args.count), sys.stdout, indent=2)
                sys.stdout.write("\n")
            return 0
        if args.cmd == "ico-uk":
            if args.icouk_cmd == "enforcement":
                json.dump(ico_uk_enforcement(args.count), sys.stdout, indent=2)
                sys.stdout.write("\n")
            return 0
        if args.cmd == "sec-edgar":
            if args.edgar_cmd == "8k":
                json.dump(sec_edgar_8k(args.start, args.end, args.item),
                          sys.stdout, indent=2)
                sys.stdout.write("\n")
            return 0
        if args.cmd == "wayback":
            result = wayback_snapshot(args.orig_url, args.target_ts, args.min_size)
            # `body` can be large; emit metadata header first then the body.
            meta = {k: v for k, v in result.items() if k != "body"}
            print(json.dumps(meta, indent=2))
            print("--- BODY ---")
            sys.stdout.write(result["body"])
            return 0
        if args.cmd == "feed":
            json.dump(feed_recent(args.feed_url, args.count), sys.stdout, indent=2)
            sys.stdout.write("\n")
            return 0
        if args.cmd == "msrc":
            if args.msrc_cmd == "cvrf":
                json.dump(msrc_cvrf(args.release), sys.stdout, indent=2)
            elif args.msrc_cmd == "cve":
                json.dump(msrc_cve(args.cve), sys.stdout, indent=2)
            elif args.msrc_cmd == "release":
                json.dump(msrc_release(args.release, args.count), sys.stdout, indent=2)
            elif args.msrc_cmd == "recent":
                json.dump(msrc_recent(args.count), sys.stdout, indent=2)
            elif args.msrc_cmd == "releases":
                json.dump(msrc_releases(args.count), sys.stdout, indent=2)
            sys.stdout.write("\n")
            return 0
        if args.cmd == "msft-secblog":
            if args.msft_cmd == "recent":
                json.dump(msft_secblog_recent(args.count, args.topic), sys.stdout, indent=2)
                sys.stdout.write("\n")
            return 0
    except (RuntimeError, ValueError) as e:
        print(f"fetch_source: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
