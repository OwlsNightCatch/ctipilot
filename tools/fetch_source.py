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

The bridge enforces no host allowlist and is usable on any HTTPS
publisher (see `_check_url` for the SSRF defences that remain — IP-range
deny list on the resolved host, redirect re-validation, body-size cap,
https-only).

The script will NEVER:
- Submit forms or attempt authentication.
- Fetch hidden / authenticated content (the agent must respect TLP).
- Run third-party JS or load any other origin.

Fetch ladder recap: try `feed` (RSS) → the routine's WebFetch → `jina` (the
r.jina.ai reader proxy) → `url` / a dedicated bridge recipe, and keep a backup.
The `url` command folds the last two together (direct → reader auto-fallback).

Hosts the direct bridge cannot get content from — but the `jina` reader CAN
(it fetches from its own egress and runs page JS, defeating the anti-bot / geo
gate that refuses our egress). Reach these with `jina <URL>` (or `url <URL>`,
which auto-falls-back):
- www.group-ib.com → Cloudflare gate on our egress; recovered (direct now 200; reader as backup).
- www.ccn-cert.cni.es → geo-block from outside Spain; recovered via the reader.
Hosts NO transport reaches (direct, reader, AND bridge all fail — HTTP 401
even to the reader): www.coe.int, downloads.seppmail.com. There is no
archived-snapshot fallback — surface these as a coverage gap and use WebSearch
to find a corroborating publisher instead.
Recovered earlier by the UA bump — use the feed path: databreaches.net
(`feed https://databreaches.net/feed/`), www.darkreading.com (its /rss.xml),
www.inside-it.ch (its /rss.xml).

Fetch ladder (best-content-first — the same order the research agents follow):
    1. RSS/Atom feed   → `feed <URL>` (structured, dated, carries outbound links)
    2. direct WebFetch → the routine's WebFetch tool (agent-side; not this script)
    3. jina reader     → `jina <URL>` (clean markdown; server-side egress bypasses
                          anti-bot / WAF / geo blocks and executes page JS)
    4. dedicated bridge→ the structured subcommands below (browser UA / publisher API)
The `url` command folds tiers 2→3 into one call: it tries a direct browser-UA
GET and AUTO-FALLS-BACK to the jina reader on a 403 / anti-bot / challenge body,
so every page has a backup transport. Force one transport with `--direct` / `jina`.

Usage:
    python3 tools/fetch_source.py url <URL> [--direct]               # direct browser-UA GET, auto-fallback to jina reader (prints body)
    python3 tools/fetch_source.py jina <URL> [html]                  # force the r.jina.ai reader proxy (clean markdown; `html` for simplified HTML)
    python3 tools/fetch_source.py jina-usage                         # JINA_API_KEY token balance — warns when a new key should be generated
    python3 tools/fetch_source.py ncsc-csh list [N]                  # NCSC CSH public dashboard (last N TLP:CLEAR posts as JSON)
    python3 tools/fetch_source.py ncsc-csh post <ID>                 # one TLP:CLEAR post (Markdown body + metadata)
    python3 tools/fetch_source.py ncsc-csh recent [N]                # combined: list + each post's full content (default 10)
    python3 tools/fetch_source.py cisa-kev                           # full CISA KEV JSON catalog
    python3 tools/fetch_source.py cisa page <URL>                    # one cisa.gov page body (direct → r.jina.ai reader fallback; Akamai 403s a direct hit)
    python3 tools/fetch_source.py cisa feed <FEED-URL> [N]           # a cisa.gov RSS/Atom feed → {title, link} items (news.xml / all.xml / blog.xml / ics*.xml)
    python3 tools/fetch_source.py cisa csaf-recent [N]               # recent ICS/OT advisories from the cisagov/CSAF changes.csv index (dated, newest first)
    python3 tools/fetch_source.py cisa csaf <icsa-YY-DDD-NN>         # full CSAF JSON for one ICS advisory (icsa-/icsma-) from the CSAF mirror
    python3 tools/fetch_source.py enisa-euvd recent [KIND]           # KIND ∈ lastvulnerabilities (default) | criticals | exploited
    python3 tools/fetch_source.py enisa-euvd advisory <ID>           # one EUVD advisory by id (e.g. EUVD-2025-12345)
    python3 tools/fetch_source.py bsi-rss                            # BSI cert-bund WID-SEC RSS feed (XML)
    python3 tools/fetch_source.py bsi-csaf <WID-SEC-ID>              # BSI WID-SEC advisory CSAF JSON (full body — e.g. WID-SEC-2026-1438)
    python3 tools/fetch_source.py ncsc-nl csaf <ID> [VERSION]        # one Dutch NCSC CSAF advisory (e.g. NCSC-2025-0432, default v1)
    # Structured discovery feeds for hosts whose listing pages are JS-rendered
    python3 tools/fetch_source.py ncsc-nl recent [N]                 # Dutch NCSC RSS — last N advisory IDs + titles (default 20)
    python3 tools/fetch_source.py cert-eu recent [N]                 # CERT-EU RSS — last N advisories (default 20)
    python3 tools/fetch_source.py cert-fr avis-recent [N]            # CERT-FR vendor-vuln advisories RSS (default 20)
    python3 tools/fetch_source.py cert-fr actu-recent [N]            # CERT-FR weekly-bulletin / actualité RSS (default 20)
    python3 tools/fetch_source.py ico-uk enforcement [N]             # UK ICO enforcement actions — top N by lastmod from sitemap.xml (default 20)
    python3 tools/fetch_source.py sec-edgar 8k [start] [end] [item]  # SEC EDGAR 8-K full-text search (default Item 1.05, last 14 days)
    # Generic RSS/Atom feed fetcher (works on any HTTPS feed URL)
    python3 tools/fetch_source.py feed <URL> [N]                     # parse any RSS/Atom feed and return last N items as JSON
    # Microsoft MSRC Update Guide (Angular SPA at msrc.microsoft.com/update-guide/ backed by anonymous CVRF + SUG OData)
    python3 tools/fetch_source.py msrc cvrf <YYYY-Mon>               # full monthly CVRF JSON (e.g. 2026-May) — ~2–3 MB
    python3 tools/fetch_source.py msrc cve <CVE-ID>                  # per-CVE detail JSON (e.g. CVE-2026-41089) — ~2–3 KB
    python3 tools/fetch_source.py msrc release <YYYY-Mon> [N]        # OData list of CVEs in one release (cheaper than `cvrf`)
    python3 tools/fetch_source.py msrc recent [N]                    # newest N CVEs across all releases
    python3 tools/fetch_source.py msrc releases [N]                  # most-recent N monthly release tags
    # Microsoft Security Blog (RSS, with topic filter)
    python3 tools/fetch_source.py msft-secblog recent [N] [TOPIC]    # last N posts; TOPIC e.g. threat-intelligence
    # OSV.dev — reachable mirror of the GitHub Advisory Database (github.com is egress-proxy-blocked; see the OSV section)
    python3 tools/fetch_source.py osv vuln <GHSA-or-CVE>            # one advisory by GHSA or CVE id (full record)
    python3 tools/fetch_source.py osv query <ecosystem> <package> [version]  # advisories affecting a package

Examples:
    python3 tools/fetch_source.py ncsc-csh recent 5
    python3 tools/fetch_source.py cisa-kev | jq '.vulnerabilities | length'
    python3 tools/fetch_source.py cisa feed https://www.cisa.gov/cybersecurity-advisories/all.xml 10 | jq '.items[].link'
    python3 tools/fetch_source.py cisa csaf-recent 5 | jq '.items[] | {id, released}'
    python3 tools/fetch_source.py cisa csaf icsa-26-183-02 | jq '{title: .document.title, cves: [.vulnerabilities[].cve]}'
    python3 tools/fetch_source.py cisa page https://www.cisa.gov/news-events/directives | head -40
    python3 tools/fetch_source.py enisa-euvd recent criticals | jq '. | length'
    python3 tools/fetch_source.py bsi-csaf WID-SEC-2026-1438 | jq '.document.title'
    python3 tools/fetch_source.py ncsc-nl recent 10 | jq '.items[].id'
    python3 tools/fetch_source.py cert-eu recent 10 | jq '.items[].title'
    python3 tools/fetch_source.py cert-fr avis-recent 10 | jq '.items[].link'
    python3 tools/fetch_source.py ico-uk enforcement 5 | jq '.items[].url'
    python3 tools/fetch_source.py sec-edgar 8k 2026-05-01 2026-05-15 1.05 | jq '.hits[].display_name'
    python3 tools/fetch_source.py feed https://thedfirreport.com/feed/ 5 | jq '.items[].title'
    python3 tools/fetch_source.py feed https://feeds.feedburner.com/threatintelligence/pvexyqv7v0v 10
    python3 tools/fetch_source.py feed https://www.schneier.com/feed/atom/ 5
    python3 tools/fetch_source.py msrc cve CVE-2026-41089 | jq '{cveTitle, exploited, baseScore}'
    python3 tools/fetch_source.py msrc release 2026-May 50 | jq '[.items[] | select(.exploited == "Yes")]'
    python3 tools/fetch_source.py msft-secblog recent 5 threat-intelligence | jq '.items[].link'
    python3 tools/fetch_source.py url https://hub.ivanti.com/s/article/May-2026-Security-Advisory-Ivanti-EPMM
    python3 tools/fetch_source.py osv vuln GHSA-jfh8-c2jp-5v3q | jq '{id, aliases, summary}'
    python3 tools/fetch_source.py osv query npm lodash | jq '.count'
    python3 tools/fetch_source.py osv query PyPI requests 2.19.1 | jq '[.vulns[].id]'
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
import time
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
# 2026-06-20 full-source audit: bumped Chrome 124 → 138 and
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

# No host allowlist.
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
# only — the bridge can still attempt these hosts, but a DIRECT hit is
# expected to fail. The `jina` reader proxy (server-side egress + page-JS
# execution) now defeats most such gates, so the right response is usually
# `jina <URL>` / `url <URL>` (auto-reader-fallback), not a coverage gap.
# Only the hosts the reader ALSO fails on (401 even to r.jina.ai) are true
# coverage gaps served by WebSearch.

# Hosts whose DIRECT fetch sits behind a Cloudflare Managed Challenge / geo /
# WAF gate. The bridge still attempts them; the `url` command auto-falls-back
# to the jina reader, which reaches most of these from its own egress.
#
# 2026-07-06 jina-fallback audit: the reader RECOVERED group-ib.com and
# ccn-cert.cni.es (both once thought transport-dead) — group-ib now even
# fetches direct; ccn-cert resolves via the reader. They moved to
# fetch_method bridge / jina in sources.json and are no longer coverage gaps.
# Kept below only the hosts NO transport reaches — the reader itself gets
# HTTP 401: coe.int, downloads.seppmail.com. (Earlier UA-bump recoveries via
# their feed path: databreaches.net, darkreading.com, inside-it.ch.)
CLOUDFLARE_BLOCKED_HOSTS = frozenset({
    "www.coe.int", "coe.int",
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

    No host allowlist — the agent can target any HTTPS
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

    The bridge enforces no host allowlist and is usable on any HTTPS
    publisher; `extra_headers` lets callers add publisher-specific
    headers (e.g. SEC EDGAR requires an identifying User-Agent suffix).
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


# ── CISA dynamic content — Akamai bypass (reader proxy + CSAF mirror) ──
#
# www.cisa.gov fronts every DYNAMIC path (/news-events/*, the RSS/Atom
# feeds, the CSAF .well-known) with Akamai bot management that 403s the
# routine's egress TLS/behavioural fingerprint for EVERY User-Agent and
# header set (re-confirmed 2026-07-05 across chrome/firefox/googlebot/
# curl/minimal). Only the STATIC /sites/default/files/ path (the KEV JSON
# above) is served directly. Two reachable ways around the block:
#
#   1. r.jina.ai — a reader proxy that fetches the page from ITS OWN
#      infrastructure (not our egress), so it is not subject to the
#      Akamai block. Returns clean markdown (or, with X-Return-Format:
#      html, a simplified HTML). Used by `cisa page` (advisory / news /
#      directive bodies + listings) and `cisa feed` (RSS → item list).
#
#   2. github.com/cisagov/CSAF — CISA mirrors every ICS/OT advisory as a
#      CSAF v2 JSON document in this public repo. github.com itself is
#      egress-proxy-blocked, but raw.githubusercontent.com is NOT — so the
#      raw file path yields fully-structured ICS advisories (CVEs, CVSS,
#      affected products, remediations) with NO third party in the loop.
#      `OT/white/changes.csv` (newest-first, ISO-dated) is the discovery
#      index. Used by `cisa csaf-recent` / `cisa csaf`.
#
# Citations always point at the human cisa.gov URL; the bridge supplies
# the data, not the citation.
#
# Authentication: the reader works anonymously (shared, low rate limit),
# but with `JINA_API_KEY` set in the environment every reader request is
# sent with `Authorization: Bearer <key>` — dedicated rate limit and the
# `X-Engine: browser` rendering tier. The key lives ONLY in the
# environment (the routine container's env config); it is never read
# from or written to any file in this repo. Key lifecycle: keys carry a
# finite token balance — `jina-usage` (CLI) / `jina_usage()` query the
# dashboard API for the remaining balance and warn the operator to
# generate a new key at https://jina.ai/api-dashboard/ when it runs low;
# a reader HTTP 402 means the balance is exhausted.
JINA_READER_BASE = "https://r.jina.ai/"
JINA_USAGE_API = "https://embeddings-dashboard-api.jina.ai/api/v1/api_key/user"
# Warn when fewer tokens than this remain on the key (a fresh trial key
# carries ~10 M; a browser-engine page fetch costs roughly 5–20 k).
JINA_LOW_BALANCE_TOKENS = 1_000_000
CISA_CSAF_RAW_BASE = "https://raw.githubusercontent.com/cisagov/CSAF/develop/csaf_files"
CISA_CSAF_OT_CHANGES = CISA_CSAF_RAW_BASE + "/OT/white/changes.csv"
# ICS advisory ids: icsa-YY-DDD-NN (industrial) and icsma-YY-DDD-NN (medical).
_CISA_ICS_ID_RE = re.compile(r"^ics(?:a|ma)-\d{2}-\d{3}-\d{2}$", re.IGNORECASE)
# r.jina.ai renders a feed as one <hN><a href=…>title</a></hN> per item.
_CISA_FEED_ITEM_RE = re.compile(
    r'<h[1-6]>\s*<a\s+href="(https?://[^"]+)"[^>]*>(.*?)</a>\s*</h[1-6]>',
    re.IGNORECASE | re.DOTALL,
)


# Markers that mean "this 200 body is an anti-bot interstitial / empty SPA
# shell, not the real content". `smart_fetch` treats a direct hit that trips
# any of these as a failure and falls through to the reader proxy — so a WAF
# that serves its challenge with HTTP 200 (Cloudflare Managed Challenge does)
# does not masquerade as success. Kept deliberately specific to avoid a false
# positive on a page that merely quotes the word "access denied".
def _looks_blocked(text: str) -> bool:
    """True iff the fetched body looks like an anti-bot challenge / access-denied
    interstitial rather than real page content (checked over the head only)."""
    head = text[:2500].lower()
    # Akamai "Access Denied" (CISA and others) — the denial always carries an
    # edgesuite reference or the "don't have permission" boilerplate.
    if "access denied" in head and (
        "edgesuite" in head or "reference #" in head
        or "don't have permission" in head or "permission to access" in head
    ):
        return True
    # Cloudflare / generic JS interstitials.
    cf_markers = (
        "just a moment",
        "attention required! | cloudflare",
        "cf-browser-verification",
        "checking your browser before accessing",
        "enable javascript and cookies to continue",
        "please enable javascript to view",
        "verify you are human",
    )
    return any(m in head for m in cf_markers)


def _jina_fetch(target_url: str, *, fmt: str | None = None,
                max_bytes: int = MAX_BODY_BYTES_HTML) -> str:
    """Fetch `target_url` through the r.jina.ai reader proxy and return the
    decoded body. The reader fetches server-side (its OWN egress), so it is not
    subject to the anti-bot / WAF / geo blocks that 403 our egress fingerprint
    (Akamai on www.cisa.gov, Cloudflare Managed Challenge on group-ib.com,
    geo-gates such as ccn-cert.cni.es) AND it executes the page's JavaScript, so
    a client-hydrated SPA that returns an empty shell to a plain GET comes back
    with real content. `fmt` maps to Jina's `X-Return-Format` header ('html'
    keeps simplified markup; default is clean markdown). Same SSRF defences as
    `fetch` — the ORIGIN url is validated (https, not an internal address)
    before it is handed to the reader."""
    _check_url(target_url)
    # Reader control headers (Jina's X-* surface):
    #   X-Cache-Tolerance: 300 — accept a reader-cached snapshot up to 5 min
    #     old, so repeat fetches of the same URL within a run are near-free
    #     and don't re-spend key tokens.
    #   X-Engine: browser — full browser rendering; slower but the highest-
    #     fidelity extraction tier. Recovers bodies the default engine
    #     misses (verified 2026-07-12: heise.de per-article pages, whose
    #     TollBit gate defeats every direct transport, return the complete
    #     article text). Markdown page fetches only — the `fmt="html"` feed
    #     path keeps the default engine so the `<hN><a href>` rendering the
    #     feed parsers depend on stays stable.
    #   X-With-Links-Summary: true — append a Links/Buttons section with
    #     every outbound URL, so discovery pivots survive the markdown
    #     conversion (same rationale as the WebFetch outbound-links
    #     template).
    extra: dict[str, str] = {
        "X-Retain-Images": "none",
        "X-Cache-Tolerance": "300",
    }
    if fmt:
        extra["X-Return-Format"] = fmt
    else:
        extra["X-Engine"] = "browser"
        extra["X-With-Links-Summary"] = "true"
    key = os.environ.get("JINA_API_KEY", "").strip()
    if key:
        extra["Authorization"] = f"Bearer {key}"
    reader_url = JINA_READER_BASE + target_url
    # The reader can cold-start / rate-limit / stall on a first hit; three tries
    # with a short backoff turn those blips into the real (usually 200) result.
    last = ""
    for attempt in (1, 2, 3):
        try:
            code, body, _ = fetch(
                reader_url, accept="text/plain, */*",
                max_bytes=max_bytes, extra_headers=extra,
            )
        except Exception as e:  # noqa: BLE001 — network/timeout: retry
            last = str(e)[:140]
            code, body = 0, b""
        if code == 200:
            text = body.decode("utf-8", errors="replace")
            # Some paths (e.g. cisa.gov's deprecated /blog.xml) return the
            # upstream Akamai "Access Denied" page even through the reader;
            # surface that as a failure rather than handing back the denial
            # page as content.
            if _looks_blocked(text):
                raise RuntimeError(f"reader proxy relayed an upstream block/challenge for {target_url}")
            return text
        if code == 402:
            # Payment Required — per the reader's OpenAPI spec this is
            # InsufficientBalanceError or TierFeatureConstraintError: the
            # JINA_API_KEY token balance is exhausted (or the key's tier lacks
            # the feature). Not retryable with this key; surface the fix
            # instead of burning the backoff budget.
            raise RuntimeError(
                "reader proxy HTTP 402: JINA_API_KEY balance exhausted (or "
                "tier constraint) — generate a new key at "
                "https://jina.ai/api-dashboard/ and update the environment "
                "(verify with `jina-usage`)"
            )
        last = f"HTTP {code}" if code else last
        if attempt < 3:
            time.sleep(2.0 * attempt)
    raise RuntimeError(f"reader proxy failed for {target_url}: {last}")


def jina_page(url: str, *, html: bool = False) -> str:
    """Fetch ANY HTTPS page's body through the r.jina.ai reader proxy. This is
    the operator-facing `jina <URL>` transport — tier 3 of the fetch ladder
    (RSS → direct WebFetch → jina reader → dedicated bridge recipe). Prefer it
    over a raw `url` fetch whenever the host anti-bot-blocks our egress, geo-
    gates it, or serves a JS-only shell: the reader returns clean, readable
    content (markdown by default; simplified HTML with `html=True`)."""
    return _jina_fetch(url, fmt="html" if html else None)


def jina_usage(*, warn_below: int = JINA_LOW_BALANCE_TOKENS) -> dict[str, Any]:
    """Token-balance check for the reader API key. Reads `JINA_API_KEY` from
    the environment (never from a file), queries Jina's dashboard API, and
    returns the wallet balances. `warning` is a human-readable notice when
    the balance is exhausted or below `warn_below` — the signal to generate
    a new key at https://jina.ai/api-dashboard/ and update the env."""
    key = os.environ.get("JINA_API_KEY", "").strip()
    if not key:
        raise RuntimeError(
            "JINA_API_KEY is not set — the reader is running anonymously "
            "(shared rate limit, no browser engine). Set the key in the "
            "environment to check its usage."
        )
    qs = urllib.parse.urlencode({"api_key": key})
    try:
        data = fetch_json(f"{JINA_USAGE_API}?{qs}")
    except RuntimeError as e:
        raise RuntimeError(
            f"jina usage lookup failed ({e}) — the key may be invalid or "
            "revoked; generate a new one at https://jina.ai/api-dashboard/"
        ) from None
    wallet = (data.get("wallet") or {}) if isinstance(data, dict) else {}
    total = int(wallet.get("total_balance") or 0)
    out: dict[str, Any] = {
        "source": "jina-usage",
        "key_suffix": key[-6:],  # enough to tell keys apart, never the key
        "total_balance": total,
        "trial_balance": int(wallet.get("trial_balance") or 0),
        "regular_balance": int(wallet.get("regular_balance") or 0),
        "trial_end": wallet.get("trial_end"),
        "warn_below": warn_below,
        "warning": None,
    }
    if total <= 0:
        out["warning"] = (
            "JINA_API_KEY balance is EXHAUSTED — reader requests will 402. "
            "Generate a new API key at https://jina.ai/api-dashboard/ and "
            "update the environment."
        )
    elif total < warn_below:
        out["warning"] = (
            f"JINA_API_KEY balance is low ({total:,} tokens < "
            f"{warn_below:,}) — generate a new API key at "
            "https://jina.ai/api-dashboard/ soon and update the environment."
        )
    return out


def smart_fetch(url: str) -> tuple[str, str]:
    """Fetch an HTML page's body with an automatic fallback ladder so every
    page has a backup transport. Tries, in order:

      1. a direct browser-UA GET (`fetch`) — cheapest, no third party;
      2. the r.jina.ai reader proxy (`_jina_fetch`) — server-side egress that
         bypasses anti-bot / WAF / geo blocks and executes JavaScript.

    Returns `(text, method)` where `method` ∈ {`direct`, `jina`}. A direct 200
    whose body trips `_looks_blocked` (a WAF challenge served with HTTP 200) is
    NOT accepted — it falls through to the reader. Raises RuntimeError only when
    BOTH transports fail, with the reason from each so the caller can log it.
    This backs the CLI `url` command (and `cisa page`)."""
    direct_err = ""
    try:
        code, body, _ = fetch(
            url,
            accept="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        )
        if code == 200 and len(body) > 500:
            text = body.decode("utf-8", errors="replace")
            if not _looks_blocked(text):
                return text, "direct"
            direct_err = "direct hit returned an anti-bot/challenge body"
        else:
            direct_err = f"direct HTTP {code}, {len(body)} B"
    except Exception as e:  # noqa: BLE001 — fall through to the reader
        direct_err = str(e)[:140]
    try:
        return _jina_fetch(url), "jina"
    except Exception as e:  # noqa: BLE001
        raise RuntimeError(
            f"both transports failed for {url}: direct=({direct_err}); "
            f"jina=({str(e)[:160]})"
        ) from None


def cisa_page(url: str) -> str:
    """Fetch a cisa.gov page body via the standard ladder — a direct browser-UA
    fetch first (so it auto-recovers the moment the Akamai block ever lifts),
    then the r.jina.ai reader proxy (clean markdown with the full body) on the
    403 / anti-bot block that is currently the norm."""
    return smart_fetch(url)[0]


def cisa_feed(feed_url: str, limit: int = 30) -> dict[str, Any]:
    """Fetch a cisa.gov RSS/Atom feed through the reader proxy (which renders
    each item as a `<hN><a href>` heading) and return `{title, link}` items.
    The cisa.gov feed endpoints 403 a direct fetch (Akamai); the reader does
    not. For the ICS feeds, `cisa csaf-recent` gives richer, fully-structured
    data straight from the CSAF mirror — prefer it where the id is icsa/icsma."""
    html = _jina_fetch(feed_url, fmt="html")
    items: list[dict[str, str]] = []
    seen: set[str] = set()
    for m in _CISA_FEED_ITEM_RE.finditer(html):
        link = m.group(1).strip()
        title = re.sub(r"<[^>]+>", "", m.group(2)).strip()
        if "cisa.gov" not in link or not title or link in seen:
            continue
        seen.add(link)
        items.append({"title": title, "link": link})
        if len(items) >= max(1, int(limit)):
            break
    return {"source": "cisa-feed", "feed": feed_url, "count": len(items), "items": items}


def _cisa_ics_advisory_url(adv_id: str) -> str:
    """Human advisory URL for a CISA ICS/OT advisory id (for citation)."""
    low = adv_id.lower()
    kind = "ics-medical-advisories" if low.startswith("icsma") else "ics-advisories"
    return f"https://www.cisa.gov/news-events/{kind}/{low}"


def cisa_csaf_recent(count: int = 25) -> dict[str, Any]:
    """Recent CISA ICS/OT advisories from the cisagov/CSAF `changes.csv`
    index (newest first, ISO-dated). Reachable via raw.githubusercontent.com
    with no Akamai and no third party. Each item carries the CSAF JSON url
    (full structured detail — chain into `cisa csaf <id>`) and the human
    advisory url for citation."""
    txt = fetch_text(CISA_CSAF_OT_CHANGES, accept="text/csv, text/plain, */*;q=0.5")
    rows: list[dict[str, str]] = []
    for line in txt.splitlines():
        m = re.match(r'^\s*"([^"]+\.json)"\s*,\s*"([^"]+)"\s*$', line.strip())
        if not m:
            continue
        path, released = m.group(1), m.group(2)
        adv_id = re.sub(r"^.*/", "", path)[:-5]  # strip dir + ".json"
        rows.append({
            "id": adv_id,
            "released": released,
            "csaf_url": f"{CISA_CSAF_RAW_BASE}/OT/white/{path}",
            "advisory_url": _cisa_ics_advisory_url(adv_id),
        })
    rows.sort(key=lambda r: r["released"], reverse=True)
    count = max(1, int(count))
    return {"source": "cisa-csaf", "index": CISA_CSAF_OT_CHANGES,
            "total": len(rows), "count": min(count, len(rows)), "items": rows[:count]}


def cisa_csaf(adv_id: str) -> Any:
    """Full CSAF v2 JSON for one CISA ICS/OT advisory (icsa-YY-DDD-NN or
    icsma-YY-DDD-NN) from the cisagov/CSAF mirror. Contains the document
    title, tracking dates, every CVE with CVSS, the product tree, and
    remediations — the richest machine-readable form CISA publishes."""
    aid = adv_id.strip().lower()
    if not _CISA_ICS_ID_RE.match(aid):
        raise ValueError(
            f"refused: invalid CISA ICS advisory id {adv_id!r} "
            "(expected icsa-YY-DDD-NN or icsma-YY-DDD-NN)"
        )
    year = "20" + aid.split("-")[1]
    return fetch_json(f"{CISA_CSAF_RAW_BASE}/OT/white/{year}/{aid}.json")


# ── ENISA EUVD helpers (added 2026-05-10; hotfixed 2026-05-11) ─
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


# ── RSS-driven listing helpers ─────────────────────────────────
#
# A small RSS parser. We parse with `xml.etree.ElementTree` rather than a
# third-party feedparser to keep the stdlib-only posture. The parser
# refuses external DTDs / entities (XXE defence) — XML.etree's default
# already does this in Python 3.7.1+ but we set it explicitly via
# `defusedxml`-style guards on the parser.

import xml.etree.ElementTree as _ET  # noqa: E402  (after _check_url above)
from datetime import datetime, timezone  # noqa: E402
from email.utils import parsedate_to_datetime  # noqa: E402


def _parse_feed_date(value: str) -> datetime | None:
    """Best-effort parse of an RSS/Atom timestamp (RFC 822 `pubDate` or
    ISO 8601 `published`/`dc:date`) to an aware UTC datetime; None when
    empty or unparseable. Naive datetimes are assumed UTC."""
    v = (value or "").strip()
    if not v:
        return None
    try:
        dt = parsedate_to_datetime(v)
        if dt is not None:
            return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
    except (TypeError, ValueError):
        pass
    try:
        dt = datetime.fromisoformat(v.replace("Z", "+00:00"))
        return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
    except ValueError:
        return None


def _newest_first(items: list[dict[str, str]], limit: int) -> list[dict[str, str]]:
    """Order feed items newest-first, then truncate to `limit`.

    Some feeds serve items oldest-first in document order (observed on the
    CERT-FR avis/actualite feeds 2026-07-09: a plain `feed <url> 20` call
    returned Nov-2025 archive entries instead of the current bulletin), so
    slicing the first N without sorting silently returns the archive tail.
    Sort by parsed `published` descending whenever at least one item carries
    a parseable date; undated items sort last, keeping document order among
    themselves (list.sort is stable). A feed with no parseable dates at all
    keeps its document order unchanged."""
    keyed = [(_parse_feed_date(it.get("published", "")), it) for it in items]
    if any(k is not None for k, _ in keyed):
        floor = datetime.min.replace(tzinfo=timezone.utc)
        keyed.sort(key=lambda kv: kv[0] or floor, reverse=True)
    return [it for _, it in keyed][:limit]


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
        for it in channel.findall("item"):
            items.append({
                "title":     (it.findtext("title") or "").strip(),
                "link":      (it.findtext("link") or "").strip(),
                "published": (it.findtext("pubDate") or it.findtext("{http://purl.org/dc/elements/1.1/}date") or "").strip(),
                "summary":   (it.findtext("description") or "").strip(),
            })
        return _newest_first(items, limit)

    # ── Atom 1.0 (namespace `http://www.w3.org/2005/Atom`) ────────────
    if local == "feed" and ns_uri.lower() == "http://www.w3.org/2005/atom":
        ns = "{http://www.w3.org/2005/Atom}"
        for it in root.findall(f"{ns}entry"):
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
        return _newest_first(items, limit)

    # ── RSS 1.0 / RDF Site Summary (namespace `…/rdf-syntax-ns#`) ─────
    # Used by Slashdot, some heise feeds (legacy), and a few CMSs. <item>
    # elements are direct children of <rdf:RDF>, not nested in <channel>.
    if local == "rdf" and ns_uri.endswith("rdf-syntax-ns#"):
        rss10_ns = "{http://purl.org/rss/1.0/}"
        dc_ns    = "{http://purl.org/dc/elements/1.1/}"
        for it in root.findall(f"{rss10_ns}item"):
            items.append({
                "title":     (it.findtext(f"{rss10_ns}title") or "").strip(),
                "link":      (it.findtext(f"{rss10_ns}link") or "").strip(),
                "published": (it.findtext(f"{dc_ns}date") or "").strip(),
                "summary":   (it.findtext(f"{rss10_ns}description") or "").strip(),
            })
        return _newest_first(items, limit)

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
# deployment-specific UA (site name from config/branding.yaml, falling
# back to the upstream default) so the call is attributable.
SEC_EDGAR_SEARCH = "https://efts.sec.gov/LATEST/search-index"


def _branded_edgar_ua() -> str:
    try:
        from pathlib import Path
        from compose_prompts import parse_yaml_subset  # sibling module
        cfg_path = Path(__file__).resolve().parent.parent / "config" / "branding.yaml"
        cfg = parse_yaml_subset(cfg_path.read_text(encoding="utf-8"),
                                source=str(cfg_path))
        name = str(cfg.get("site", {}).get("name", "")).strip()
        if name:
            return f"{name} CTI brief (contact via repository)"
    except Exception:
        pass
    return "ctipilot.ch CTI brief (contact via repository)"


SEC_EDGAR_UA = _branded_edgar_ua()


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


# ── Generic RSS/Atom feed subcommand ──────────────────────────
#
# Most CTI publisher blogs ship a standard RSS 2.0 or Atom 1.0 feed at
# `/feed/`, `/rss/`, `/feed.xml`, or via Feedburner. Rather than adding
# per-publisher subcommands for each one, `feed <URL> [N]` runs the
# `_parse_rss` helper on any URL and returns the same JSON shape every
# other listing subcommand uses ({source, feed, count, items: [...]}).
# The agent's drilldown pattern (take `link` from `items[i]`, then
# `url <link>` for the full body) works uniformly across every publisher.
#
# Verified against the source-list expansion:
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


def _jina_feed_items(feed_url: str, limit: int) -> list[dict[str, str]]:
    """Backup feed parse: fetch the feed through the r.jina.ai reader (which
    renders each item as a `<hN><a href>title</a></hN>` heading) and extract
    `{title, link}` items. Used when a direct feed GET is anti-bot-blocked or
    the raw XML fails to parse — so an RSS source behind a WAF still has a
    second transport. Same shape as `cisa_feed`, host-agnostic."""
    html = _jina_fetch(feed_url, fmt="html")
    items: list[dict[str, str]] = []
    seen: set[str] = set()
    for m in _CISA_FEED_ITEM_RE.finditer(html):
        link = m.group(1).strip()
        title = re.sub(r"<[^>]+>", "", m.group(2)).strip()
        if not link or not title or link in seen:
            continue
        seen.add(link)
        items.append({"title": title, "link": link, "published": "", "summary": ""})
        if len(items) >= max(1, int(limit)):
            break
    return items


def feed_recent(feed_url: str, count: int = 20) -> dict[str, Any]:
    """Fetch any RSS/Atom feed and return the most-recent N items as
    `{source, feed, count, items: [{title, link, published, summary}]}`.
    The agent then `url`-fetches per-article `link`s for the full body.

    Backup transport: if the direct feed GET fails (anti-bot 403 / TLS / DNS)
    or the raw body parses to zero items, fall through to the r.jina.ai reader
    (`method: jina` in the result) so a feed behind a WAF is still readable."""
    host = (urllib.parse.urlparse(feed_url).hostname or "").lower()
    method = "direct"
    items: list[dict[str, str]] = []
    direct_err = ""
    try:
        body = fetch_text(
            feed_url,
            accept="application/rss+xml, application/atom+xml, application/xml, text/xml, */*;q=0.5",
        )
        items = _parse_rss(body, limit=max(1, int(count)))
    except Exception as e:  # noqa: BLE001 — try the reader before giving up
        direct_err = str(e)[:140]
    if not items:
        try:
            items = _jina_feed_items(feed_url, max(1, int(count)))
            method = "jina"
        except Exception as e:  # noqa: BLE001
            if direct_err:
                raise RuntimeError(
                    f"feed unreadable via both transports for {feed_url}: "
                    f"direct=({direct_err}); jina=({str(e)[:140]})"
                ) from None
            # Direct parse succeeded but returned 0 items (empty feed) — that
            # is a legitimate empty result, not a transport failure.
    # Use the hostname as a stable `source` field so a multi-feed run can
    # be sorted / aggregated downstream without re-parsing the URL.
    return {"source": host or "feed", "feed": feed_url, "method": method,
            "count": len(items), "items": items}


# ── Microsoft MSRC Update Guide ───────────────────────────────
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


# ── Microsoft Security Blog feeds ─────────────────────────────
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


# ── OSV.dev — reachable mirror of the GitHub Advisory Database ────────
#
# github.com and api.github.com are NOT reachable from the routine's egress:
# the agent proxy binds each session to its configured repository and answers
# every other github.com / api.github.com path with HTTP 403 and the JSON body
# `{"message":"This GitHub API path is not available: sessions are bound to
# their configured repositories. ..."}`. That includes `github.com/advisories`
# and `api.github.com/advisories`. This is a proxy-POLICY block, not an
# anti-bot / UA refusal — no browser UA, header set, or Sec-CH-UA hint recovers
# it (re-confirmed 2026-07-05 across chrome/firefox/googlebot/curl/minimal).
#
# OSV.dev (`api.osv.dev`, operated by Google's OSS security team) ingests the
# FULL GitHub Advisory Database — every GHSA id is present and aliased to its
# CVE — and IS reachable from the routine's egress. It is the supported
# substitute recipe for the `github-advisory` source. Two anonymous JSON
# endpoints, both stdlib-fetchable:
#
#   GET  /v1/vulns/{id}   — one advisory by GHSA or CVE id. Full record:
#                           summary, details (Markdown), severity (CVSS),
#                           affected package ranges, references, aliases.
#   POST /v1/query        — advisories affecting a package. Body:
#                           {"package": {"ecosystem": "npm", "name": "lodash"}}
#                           (add "version" to filter to one version). Returns
#                           {"vulns": [ ...full records... ]}.
#
# The brief still cites the human-readable GitHub advisory URL
# (https://github.com/advisories/<GHSA-ID>) — the bridge supplies the data, not
# the citation. The routine's watchlist-driven model (research specific
# vendors / products) maps cleanly onto the package-query endpoint; per-id
# lookup covers drilldown from a GHSA / CVE surfaced by another source.
OSV_API_BASE = "https://api.osv.dev"
# GHSA ids are `GHSA-` + three 4-char groups; CVE ids are the standard form.
# Both go into a URL path, so the pattern is also the path-safety gate.
_OSV_ID_RE = re.compile(
    r"^(?:GHSA-[0-9a-zA-Z]{4}-[0-9a-zA-Z]{4}-[0-9a-zA-Z]{4}|CVE-\d{4}-\d{4,7})$"
)


def _post_json(url: str, payload: dict[str, Any], *, max_bytes: int = MAX_BODY_BYTES_JSON) -> Any:
    """POST a JSON body and parse the JSON response, under the same SSRF
    defences as `fetch` (`_check_url` + safe-redirect opener + body cap).
    Kept minimal — the only POST endpoint the bridge uses is OSV's read-only
    `/v1/query`, which takes no auth and mutates nothing."""
    _check_url(url)
    data = json.dumps(payload).encode("utf-8")
    headers = {
        "User-Agent": BROWSER_UA,
        "Accept": "application/json",
        "Accept-Encoding": "identity",
        "Content-Type": "application/json",
    }
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        with _OPENER.open(req, timeout=DEFAULT_TIMEOUT) as resp:
            body = _read_capped(resp, max_bytes)
            code = resp.status
    except urllib.error.HTTPError as e:
        try:
            body = _read_capped(e, max_bytes) if hasattr(e, "read") else b""
        except RuntimeError:
            body = b""
        code = e.code
    if code != 200:
        raise RuntimeError(f"upstream HTTP {code} for {url}")
    return json.loads(body.decode("utf-8", errors="replace"))


def osv_vuln(vuln_id: str) -> Any:
    """Fetch one OSV / GitHub-Advisory record by GHSA or CVE id."""
    vid = vuln_id.strip()
    if not _OSV_ID_RE.match(vid):
        raise ValueError(
            f"refused: invalid OSV id {vuln_id!r} "
            "(expected GHSA-xxxx-xxxx-xxxx or CVE-YYYY-NNNN)"
        )
    return fetch_json(f"{OSV_API_BASE}/v1/vulns/{vid}")


def osv_query(ecosystem: str, package: str, version: str | None = None) -> dict[str, Any]:
    """Query OSV for advisories affecting `package` in `ecosystem`
    (npm / PyPI / Go / Maven / crates.io / NuGet / RubyGems / Packagist / …).
    Optionally filter to a single `version`. Returns the publisher's `vulns`
    list wrapped with a flat `count` for convenience."""
    if not re.match(r"^[A-Za-z0-9 ._+-]{1,60}$", ecosystem):
        raise ValueError(f"refused: invalid ecosystem {ecosystem!r}")
    if not package or len(package) > 200:
        raise ValueError(f"refused: invalid package name {package!r}")
    payload: dict[str, Any] = {"package": {"ecosystem": ecosystem, "name": package}}
    if version:
        if len(version) > 100:
            raise ValueError(f"refused: invalid version {version!r}")
        payload["version"] = version
    data = _post_json(f"{OSV_API_BASE}/v1/query", payload)
    vulns = data.get("vulns", []) if isinstance(data, dict) else []
    return {
        "source": "osv",
        "ecosystem": ecosystem,
        "package": package,
        "version": version,
        "count": len(vulns),
        "vulns": vulns,
    }


# ── CLI ───────────────────────────────────────────────────────────────

def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(prog="fetch_source.py", description=__doc__)
    sub = p.add_subparsers(dest="cmd", required=True)

    p_url = sub.add_parser("url", help="direct browser-UA GET with automatic r.jina.ai reader fallback, prints body")
    p_url.add_argument("url")
    p_url.add_argument("--direct", action="store_true",
                       help="direct browser-UA GET only — do NOT fall back to the jina reader (raw HTML/XML)")

    p_jina = sub.add_parser("jina", help="force the r.jina.ai reader proxy — clean markdown; bypasses anti-bot/WAF/geo blocks and runs page JS")
    p_jina.add_argument("url")
    p_jina.add_argument("fmt", nargs="?", choices=["markdown", "html"], default="markdown",
                        help="return format (default markdown; `html` keeps simplified markup)")

    sub.add_parser("jina-usage", help="remaining token balance on JINA_API_KEY — warns (stderr) when a new key should be generated")

    p_csh = sub.add_parser("ncsc-csh", help="NCSC Switzerland Cyber Security Hub")
    csh_sub = p_csh.add_subparsers(dest="csh_cmd", required=True)
    p_csh_list = csh_sub.add_parser("list", help="public dashboard listing")
    p_csh_list.add_argument("count", type=int, nargs="?", default=20)
    p_csh_post = csh_sub.add_parser("post", help="one post by ID")
    p_csh_post.add_argument("id", type=int)
    p_csh_recent = csh_sub.add_parser("recent", help="list + full content of each (combined)")
    p_csh_recent.add_argument("count", type=int, nargs="?", default=10)

    p_cisa = sub.add_parser("cisa-kev", help="CISA Known Exploited Vulnerabilities catalog (JSON)")

    p_cisa_page = sub.add_parser("cisa", help="CISA pages (advisories, news, directives) — Akamai-bypassed via reader proxy + CSAF mirror")
    cisa_sub = p_cisa_page.add_subparsers(dest="cisa_cmd", required=True)
    p_cisa_html = cisa_sub.add_parser("page", help="one cisa.gov page body (direct, then r.jina.ai reader fallback)")
    p_cisa_html.add_argument("url")
    p_cisa_feed = cisa_sub.add_parser("feed", help="a cisa.gov RSS/Atom feed → {title, link} items (via reader proxy)")
    p_cisa_feed.add_argument("url", help="feed URL, e.g. https://www.cisa.gov/cybersecurity-advisories/all.xml")
    p_cisa_feed.add_argument("count", type=int, nargs="?", default=30)
    p_cisa_csafr = cisa_sub.add_parser("csaf-recent", help="recent ICS/OT advisories from the cisagov/CSAF changes.csv index (dated)")
    p_cisa_csafr.add_argument("count", type=int, nargs="?", default=25)
    p_cisa_csaf1 = cisa_sub.add_parser("csaf", help="full CSAF JSON for one ICS advisory (icsa-/icsma-) from the CSAF mirror")
    p_cisa_csaf1.add_argument("id", help="advisory id, e.g. icsa-26-183-02 or icsma-26-181-01")

    # Additional bridge endpoints for known-403 / SPA-only sources.
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

    # Structured discovery feeds for hosts whose listing pages are JS-rendered
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


    # Generic RSS/Atom feed subcommand (covers most CTI blog publishers cleanly)
    p_feed = sub.add_parser("feed", help="Generic RSS/Atom feed fetcher — works on any HTTPS feed URL")
    p_feed.add_argument("feed_url", help="full feed URL, e.g. https://thedfirreport.com/feed/")
    p_feed.add_argument("count", type=int, nargs="?", default=20)

    # Microsoft MSRC Update Guide (SPA-backed by public CVRF + SUG OData APIs)
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

    # Microsoft Security Blog (RSS-driven; supports topic-filtered feed)
    p_msft = sub.add_parser("msft-secblog", help="Microsoft Security Blog (RSS)")
    msft_sub = p_msft.add_subparsers(dest="msft_cmd", required=True)
    p_msft_recent = msft_sub.add_parser("recent", help="last N security-blog posts (general or per-topic)")
    p_msft_recent.add_argument("count", type=int, nargs="?", default=20)
    p_msft_recent.add_argument("topic", nargs="?", default=None,
                                help="topic slug, e.g. threat-intelligence | vulnerabilities-and-exploits | incident-response | ai-and-machine-learning")

    # OSV.dev — reachable GitHub Advisory Database mirror (github.com is egress-proxy-blocked)
    p_osv = sub.add_parser("osv", help="OSV.dev — GitHub Advisory Database mirror (reachable substitute for github.com/advisories)")
    osv_sub = p_osv.add_subparsers(dest="osv_cmd", required=True)
    p_osv_vuln = osv_sub.add_parser("vuln", help="one advisory by GHSA or CVE id (full record)")
    p_osv_vuln.add_argument("id", help="GHSA-xxxx-xxxx-xxxx or CVE-YYYY-NNNN")
    p_osv_query = osv_sub.add_parser("query", help="advisories affecting a package in an ecosystem")
    p_osv_query.add_argument("ecosystem", help="npm | PyPI | Go | Maven | crates.io | NuGet | RubyGems | Packagist | …")
    p_osv_query.add_argument("package", help="package name, e.g. lodash")
    p_osv_query.add_argument("version", nargs="?", default=None, help="optional version filter")

    args = p.parse_args(argv)

    try:
        if args.cmd == "url":
            if args.direct:
                sys.stdout.write(fetch_text(args.url))
            else:
                text, method = smart_fetch(args.url)
                if method != "direct":
                    # Tell the operator which transport served the body without
                    # polluting stdout (which callers parse as page content).
                    print(f"# fetched via {method} reader fallback", file=sys.stderr)
                sys.stdout.write(text)
            return 0
        if args.cmd == "jina":
            sys.stdout.write(jina_page(args.url, html=(args.fmt == "html")))
            return 0
        if args.cmd == "jina-usage":
            usage = jina_usage()
            json.dump(usage, sys.stdout, indent=2)
            sys.stdout.write("\n")
            if usage.get("warning"):
                # stderr so pipelines that parse stdout still see clean JSON.
                print(f"jina-usage: WARNING: {usage['warning']}", file=sys.stderr)
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
                # If the agent passed a non-CISA URL it almost certainly meant
                # to use the generic `url <URL>` subcommand instead.
                if "cisa.gov" not in (urllib.parse.urlparse(args.url).hostname or ""):
                    print("error: cisa page URL must be on cisa.gov — use `url <URL>` for other hosts", file=sys.stderr)
                    return 2
                sys.stdout.write(cisa_page(args.url))
                return 0
            if args.cisa_cmd == "feed":
                if "cisa.gov" not in (urllib.parse.urlparse(args.url).hostname or ""):
                    print("error: cisa feed URL must be on cisa.gov", file=sys.stderr)
                    return 2
                json.dump(cisa_feed(args.url, args.count), sys.stdout, indent=2)
                sys.stdout.write("\n")
                return 0
            if args.cisa_cmd == "csaf-recent":
                json.dump(cisa_csaf_recent(args.count), sys.stdout, indent=2)
                sys.stdout.write("\n")
                return 0
            if args.cisa_cmd == "csaf":
                json.dump(cisa_csaf(args.id), sys.stdout, indent=2)
                sys.stdout.write("\n")
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
        if args.cmd == "osv":
            if args.osv_cmd == "vuln":
                json.dump(osv_vuln(args.id), sys.stdout, indent=2)
            elif args.osv_cmd == "query":
                json.dump(osv_query(args.ecosystem, args.package, args.version), sys.stdout, indent=2)
            sys.stdout.write("\n")
            return 0
    except (RuntimeError, ValueError) as e:
        print(f"fetch_source: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
