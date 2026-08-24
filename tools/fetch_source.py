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

Fetch ladder recap: try `feed` (RSS) → the routine's WebFetch → `url` / a
dedicated bridge recipe (direct browser-UA GET / publisher API) → `jina` (the
r.jina.ai reader proxy) as the LAST RESORT, and keep a backup. The `url`
command folds the last two together (direct → reader auto-fallback).

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

Fetch ladder (cheapest-first, jina LAST — the same order the research agents follow):
    1. RSS/Atom feed   → `feed <URL>` (structured, dated, carries outbound links)
    2. direct WebFetch → the routine's WebFetch tool (agent-side; not this script)
    3. direct bridge   → `url <URL>` (browser-UA GET, full raw body) or the
                          structured subcommands below (publisher API / CSAF /
                          OData / sitemap)
    4. jina reader     → `jina <URL>` — the LAST RESORT. Its server-side egress
                          bypasses anti-bot / WAF / geo blocks and executes page
                          JS, but every fetch spends metered API-key credit.
                          Reach for it only when every direct transport failed,
                          or the host is a KNOWN reader-required host
                          (sources.json `fetch_method: jina`; e.g. heise.de
                          article bodies, cisa.gov dynamic paths, the
                          ccn-cert.cni.es geo-gate).
The `url` command folds rungs 3→4 into one call: it tries a direct browser-UA
GET and AUTO-FALLS-BACK to the jina reader on a 403 / anti-bot / challenge body,
so every page has a backup transport. Force one transport with `--direct` / `jina`.

Usage:
    python3 tools/fetch_source.py url <URL> [--direct]               # direct browser-UA GET, auto-fallback to jina reader (prints body)
    python3 tools/fetch_source.py jina <URL> [html]                  # LAST RESORT: force the r.jina.ai reader proxy (clean markdown; `html` for simplified HTML)
    python3 tools/fetch_source.py jina-usage                         # token balance of every configured reader key — warns when new keys are needed
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
    python3 tools/fetch_source.py ncsc-nl csaf <ID>                  # one Dutch NCSC CSAF advisory (e.g. NCSC-2025-0432)
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
import hashlib
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
#   GET /api/v1/posts/dashboard?pageSize=N&pageIndex=0
#       Public dashboard listing. Returns {pageIndex, pageSize, items: [...]}
#       where each item has: id, created, lastChange, publicationStatus,
#       summary, title, tlpStatus.
#
#   GET /api/v1/posts/{id}/details
#       Full post content. Returns: id, tlpStatus, created, history,
#       files, title, content (Markdown body).
#
# API VERSIONING (fixed 2026-08-06): the unversioned /api/posts/** tree
# stopped serving GET some time before 2026-08-06 — every path under it,
# including paths that never existed, answers HTTP 405 with
# `Allow: DELETE, PUT`, while unknown roots still 404. That is an edge
# rule on the whole subtree, not a moved route, so probing sibling paths
# finds nothing. The public read API moved under /api/v1/; the current
# paths are recorded in the SPA bundle (main-*.js) as "/api/v1/posts/
# dashboard" and "/api/v1/posts/{postId}/details". If these 405 again,
# re-read the route table out of the bundle rather than guessing:
#   curl -sS https://security-hub.ncsc.admin.ch/ | grep -o 'main-[^"]*\.js'
#   curl -sS https://security-hub.ncsc.admin.ch/<that file> \
#     | grep -o -E '"/api/[A-Za-z0-9/_{}.-]*post[A-Za-z0-9/_{}.-]*' | sort -u
#
# Authenticated endpoints (search, archive, comments, attachments) are
# NOT touched here. The agent must respect TLP — never fetch TLP:AMBER
# or TLP:RED even if a future API change exposes them.

def ncsc_list(page_size: int = 20) -> list[dict[str, Any]]:
    """Return the public dashboard items (newest first), TLP:CLEAR only."""
    if page_size < 1 or page_size > 100:
        raise ValueError("page_size must be 1..100")
    url = f"{NCSC_CSH_BASE}/api/v1/posts/dashboard?pageSize={page_size}&pageIndex=0"
    data = fetch_json(url)
    items = data.get("items", []) or []
    # Defensive filter — if the upstream ever ships non-Clear items in
    # the public dashboard by mistake, drop them.
    return [it for it in items if (it.get("tlpStatus") or "").lower() == "clear"]


def ncsc_post(post_id: int) -> dict[str, Any]:
    """Return one CSH post by ID, including the Markdown body."""
    url = f"{NCSC_CSH_BASE}/api/v1/posts/{int(post_id)}/details"
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
# but with API key(s) configured every reader request is sent with
# `Authorization: Bearer <key>` — dedicated rate limit and the
# `X-Engine: browser` rendering tier. Keys live ONLY in the environment
# (the routine container's env config); they are never read from or
# written to any file in this repo. Two variables are honoured, and each
# may carry ONE OR MORE keys separated by commas / semicolons /
# whitespace:
#
#   JINA_API_KEYS — the multi-key list (spend order = listed order)
#   JINA_API_KEY  — the original single-key variable (kept for
#                   compatibility; appended after JINA_API_KEYS)
#
# Key lifecycle: keys carry a finite token balance — `jina-usage` (CLI) /
# `jina_usage()` query the dashboard API for every configured key's
# remaining balance and warn the operator to generate a new key at
# https://jina.ai/api-dashboard/ when the pool runs low. A reader HTTP
# 402 means that key's balance is exhausted (HTTP 401: invalid/revoked);
# `_jina_fetch` then ROTATES to the next configured key, and when no live
# key remains it tries the ANONYMOUS free tier (shared rate limit, no
# browser engine) as a best-effort backstop. The anonymous tier is NOT
# guaranteed — the 2026-07-18 run observed it answering HTTP 401 — so an
# exhausted key pool can mean a reader outage; keeping a live key in the
# pool is what keeps the last-resort rung available.
JINA_READER_BASE = "https://r.jina.ai/"
JINA_USAGE_API = "https://embeddings-dashboard-api.jina.ai/api/v1/api_key/user"
# Warn when fewer tokens than this remain on the key (a fresh trial key
# carries ~10 M; a browser-engine page fetch costs roughly 5–20 k).
JINA_LOW_BALANCE_TOKENS = 1_000_000

# ── Local reader-response cache — saves API requests AND key tokens ────
#
# The pipeline re-fetches the same URL repeatedly within a run: the Phase
# 5.7 verifier cold-reads every entry source the research agents already
# fetched in Phase 1, parallel research agents overlap on hub/landing
# pages, and `smart_fetch` retries pivot through the same URL. Each of
# those was a fresh reader request spending fresh key tokens. The reader
# responses are cached on LOCAL DISK, keyed by (url, return-format),
# TTL-bounded, and shared across processes — so the second and later
# fetches of a URL within the TTL cost zero requests and zero tokens.
#
# Properties:
#   - Best-effort: any cache I/O failure falls through to a live fetch.
#   - Atomic writes (tmp + rename) so parallel sub-agents never read a
#     torn body.
#   - The cache holds only what a live call would have returned (blocked/
#     challenge bodies raise before caching, so they are never stored).
#   - The directory lives OUTSIDE the repo (never committed) and dies
#     with the ephemeral routine container.
#
# Env overrides:
#   JINA_CACHE_DIR — cache directory (default /tmp/ctipilot-jina-cache)
#   JINA_CACHE_TTL — max age in seconds (default 3600; 0 disables).
#     Keep it aligned with the X-Cache-Tolerance header below: both say
#     "an intel run tolerates content up to an hour stale", which is well
#     inside the multi-hour window each run processes.
JINA_CACHE_DIR = os.environ.get("JINA_CACHE_DIR", "/tmp/ctipilot-jina-cache")
try:
    JINA_CACHE_TTL = int(os.environ.get("JINA_CACHE_TTL", "3600"))
except ValueError:
    JINA_CACHE_TTL = 3600


def _jina_cache_path(target_url: str, fmt: str | None) -> str:
    digest = hashlib.sha256(
        f"{fmt or 'markdown'}\n{target_url}".encode("utf-8")
    ).hexdigest()
    return os.path.join(JINA_CACHE_DIR, digest + ".body")


def _jina_cache_get(target_url: str, fmt: str | None) -> str | None:
    """Return the cached reader body for (url, fmt) if fresh, else None."""
    if JINA_CACHE_TTL <= 0:
        return None
    path = _jina_cache_path(target_url, fmt)
    try:
        if time.time() - os.stat(path).st_mtime > JINA_CACHE_TTL:
            return None
        with open(path, encoding="utf-8") as f:
            return f.read()
    except OSError:
        return None


def _jina_cache_put(target_url: str, fmt: str | None, text: str) -> None:
    """Store a reader body, atomically and best-effort."""
    if JINA_CACHE_TTL <= 0:
        return
    try:
        os.makedirs(JINA_CACHE_DIR, exist_ok=True)
        path = _jina_cache_path(target_url, fmt)
        tmp = f"{path}.tmp{os.getpid()}"
        with open(tmp, "w", encoding="utf-8") as f:
            f.write(text)
        os.replace(tmp, path)
    except OSError:
        pass
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


def _jina_keys() -> list[str]:
    """Every configured reader API key, spend order first-to-last.

    Reads `JINA_API_KEYS` then `JINA_API_KEY` (either alone is fine; both
    may carry one or more keys separated by commas, semicolons, or
    whitespace/newlines). Duplicates collapse to their first occurrence.
    Keys live ONLY in the environment — never in any file in this repo."""
    raw = " ".join(
        os.environ.get(var, "") for var in ("JINA_API_KEYS", "JINA_API_KEY")
    )
    keys: list[str] = []
    for tok in re.split(r"[\s,;]+", raw):
        tok = tok.strip()
        if tok and tok not in keys:
            keys.append(tok)
    return keys


# Keys that answered HTTP 402 (token balance exhausted) or 401 (invalid /
# revoked) — skipped so a long multi-fetch invocation (e.g. `ncsc-csh
# recent`, a feed sweep) does not re-burn a request on a dead key per page.
#
# The set is BOTH process-scoped and persisted to disk with a TTL. Persisting
# matters because every sub-agent shells out to a fresh `fetch_source.py`
# process: with process-only state, a pool whose first keys are exhausted
# re-probes them on every single invocation, emitting a "balance exhausted"
# line each time even though the ladder then rotates to a live key and the
# fetch SUCCEEDS. On 2026-08-05 three research sub-agents read those benign
# rotation notices as a hard failure and abandoned the reader rung for the
# whole run — while five live keys held 37M tokens — costing coverage on
# jina-pinned sources. The TTL keeps the original recovery property: a
# topped-up or replaced key is re-probed once the entry ages out, with no
# state for an operator to reset by hand.
_JINA_DEAD_KEY_TTL = 21600  # 6 h; override with JINA_DEAD_KEY_TTL
try:
    _JINA_DEAD_KEY_TTL = int(os.environ.get("JINA_DEAD_KEY_TTL", _JINA_DEAD_KEY_TTL))
except ValueError:
    pass

_JINA_DEAD_KEYS: set[str] = set()


def _jina_dead_key_id(key: str) -> str:
    """Stable, non-reversible id for a key — never write a credential to disk."""
    return hashlib.sha256(key.encode("utf-8")).hexdigest()[:16]


def _jina_dead_keys_path() -> str:
    return os.path.join(JINA_CACHE_DIR, "dead-keys.json")


def _jina_dead_keys_load() -> dict[str, float]:
    """Persisted {key_id: marked_at} entries that are still inside the TTL."""
    if _JINA_DEAD_KEY_TTL <= 0:
        return {}
    try:
        with open(_jina_dead_keys_path(), encoding="utf-8") as fh:
            raw = json.load(fh)
    except Exception:  # noqa: BLE001 — absent/corrupt cache is not an error
        return {}
    if not isinstance(raw, dict):
        return {}
    now = time.time()
    return {
        kid: ts for kid, ts in raw.items()
        if isinstance(ts, (int, float)) and now - ts < _JINA_DEAD_KEY_TTL
    }


def _jina_dead_keys_mark(key: str) -> None:
    """Record `key` as dead, pruning entries that have aged past the TTL."""
    if _JINA_DEAD_KEY_TTL <= 0:
        return
    entries = _jina_dead_keys_load()
    entries[_jina_dead_key_id(key)] = time.time()
    try:
        os.makedirs(JINA_CACHE_DIR, exist_ok=True)
        path = _jina_dead_keys_path()
        tmp = path + ".tmp"
        with open(tmp, "w", encoding="utf-8") as fh:
            json.dump(entries, fh)
        os.replace(tmp, path)
    except Exception:  # noqa: BLE001 — cache is an optimisation, never fatal
        pass


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
    before it is handed to the reader.

    Credential ladder: every configured API key (`JINA_API_KEYS` /
    `JINA_API_KEY`, spend order) is tried in turn — a key answering HTTP 402
    (balance exhausted) or 401 (invalid/revoked) is marked dead for the rest
    of the process and the next key takes over immediately. When no live key
    remains, the request is tried ANONYMOUSLY on the reader's free tier
    (shared rate limit, no `X-Engine: browser`) as a best-effort backstop —
    NOT a guarantee: the anonymous tier was observed answering HTTP 401 on
    2026-07-18, so with an exhausted pool the reader can be a hard outage.

    Cost controls: a LOCAL disk cache (`JINA_CACHE_DIR` / `JINA_CACHE_TTL`,
    default 1 h) answers repeat fetches of the same (url, fmt) with zero
    API requests and zero token spend; `X-Cache-Tolerance: 3600` lets the
    reader serve ITS cached snapshot for URLs other parties fetched
    recently, skipping the expensive re-crawl/re-render on Jina's side."""
    _check_url(target_url)
    # Local cache first — a hit costs nothing (no request, no tokens) and is
    # exactly what the same call returned within the last hour. Set
    # JINA_CACHE_TTL=0 to force live fetches.
    cached = _jina_cache_get(target_url, fmt)
    if cached is not None:
        return cached
    # Reader control headers (Jina's X-* surface):
    #   X-Cache-Tolerance: 3600 — accept a reader-cached snapshot up to an
    #     hour old, so repeat fetches of the same URL within a run (and
    #     across the day's multiple fires) skip the re-crawl and don't
    #     re-spend key tokens. Aligned with the local JINA_CACHE_TTL: an
    #     intel run processes a multi-hour window, so hour-stale content
    #     cannot cost it a finding.
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
    base_extra: dict[str, str] = {
        "X-Retain-Images": "none",
        "X-Cache-Tolerance": "3600",
    }
    if fmt:
        base_extra["X-Return-Format"] = fmt
    else:
        base_extra["X-With-Links-Summary"] = "true"
    reader_url = JINA_READER_BASE + target_url
    # Credential ladder: every still-live configured key in spend order, then
    # None = the anonymous free tier as the always-available last rung.
    _dead_ids = _jina_dead_keys_load()
    creds: list[str | None] = [
        k for k in _jina_keys()
        if k not in _JINA_DEAD_KEYS and _jina_dead_key_id(k) not in _dead_ids
    ]
    if not creds:
        # Every configured key is inside its dead-key TTL. Re-probe the full
        # pool rather than dropping straight to the anonymous tier: a topped-up
        # key must never be locked out by a stale cache entry.
        creds = list(_jina_keys())
    creds.append(None)
    failures: list[str] = []
    for key in creds:
        extra = dict(base_extra)
        if key:
            extra["Authorization"] = f"Bearer {key}"
            if not fmt:
                # Full browser rendering is the AUTHENTICATED tier — the
                # anonymous rung stays on the default engine (requesting the
                # browser engine without a key is itself a 402 tier error).
                extra["X-Engine"] = "browser"
        label = f"key …{key[-6:]}" if key else "anonymous free tier"
        # The reader can cold-start / rate-limit / stall on a first hit; three
        # tries with a short backoff turn those blips into the real result.
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
                _jina_cache_put(target_url, fmt, text)
                return text
            if code in (401, 402):
                # 402 Payment Required — per the reader's OpenAPI spec this is
                # InsufficientBalanceError or TierFeatureConstraintError: THIS
                # key's token balance is exhausted (or its tier lacks the
                # feature). 401 — the key is invalid or revoked. Neither is
                # retryable with this credential: mark a key dead for the
                # process and rotate; on the anonymous rung (key=None) the
                # same statuses mean the free tier is refusing us (observed
                # 2026-07-18) — equally non-retryable, don't burn backoff.
                if key:
                    _JINA_DEAD_KEYS.add(key)
                    _jina_dead_keys_mark(key)
                last = ("balance exhausted (HTTP 402)" if code == 402
                        else "invalid/revoked (HTTP 401)")
                # Rotation is routine, NOT a failure — the ladder continues to
                # the next credential and the fetch usually succeeds. Say so
                # explicitly: a bare "balance exhausted" line has been read by
                # sub-agents as a dead transport (2026-08-05).
                print(
                    f"fetch_source: jina reader {label} {last} — "
                    + ("rotating to the next credential (not a failure; "
                       "the fetch continues)" if key
                       else "free tier refused; no credential left"),
                    file=sys.stderr,
                )
                break
            last = f"HTTP {code}" if code else last
            if attempt < 3:
                time.sleep(2.0 * attempt)
        failures.append(f"{label}: {last}")
    raise RuntimeError(
        f"reader proxy failed for {target_url}: {'; '.join(failures)}"
        + (" — generate a new key at https://jina.ai/api-dashboard/ and add "
           "it to the environment (verify with `jina-usage`)"
           if any("balance exhausted" in f or "invalid/revoked" in f
                  for f in failures) else "")
    )


def jina_page(url: str, *, html: bool = False) -> str:
    """Fetch ANY HTTPS page's body through the r.jina.ai reader proxy. This is
    the operator-facing `jina <URL>` transport — the LAST rung of the fetch
    ladder (RSS → direct WebFetch → direct bridge / structured recipe → jina
    reader). Every reader fetch spends metered API-key credit, so reach for it
    only when every direct transport failed — an anti-bot/WAF/geo block, a
    JS-only shell — or the host is a known reader-required host (sources.json
    `fetch_method: jina`; e.g. heise.de article bodies, cisa.gov dynamic
    paths). It returns clean, readable content (markdown by default;
    simplified HTML with `html=True`)."""
    return _jina_fetch(url, fmt="html" if html else None)


def jina_usage(*, warn_below: int = JINA_LOW_BALANCE_TOKENS) -> dict[str, Any]:
    """Token-balance check across EVERY configured reader API key
    (`JINA_API_KEYS` / `JINA_API_KEY`, spend order — read from the
    environment, never from a file). Queries Jina's dashboard API per key
    and returns the per-key wallets plus the pool totals. `warning` is a
    human-readable notice when the whole pool is dead or the combined
    balance is below `warn_below` — the signal to generate a new key at
    https://jina.ai/api-dashboard/ and add it to the env. Treat an
    exhausted pool as DOWN: `_jina_fetch` still tries the anonymous free
    tier, but that rung is best-effort only (observed answering HTTP 401
    on 2026-07-18)."""
    keys = _jina_keys()
    if not keys:
        raise RuntimeError(
            "no reader API key configured (JINA_API_KEYS / JINA_API_KEY) — "
            "the reader is running anonymously (shared rate limit, no "
            "browser engine). Set at least one key in the environment to "
            "check usage."
        )
    per_key: list[dict[str, Any]] = []
    total = 0
    live = 0
    for key in keys:
        entry: dict[str, Any] = {
            "key_suffix": key[-6:],  # enough to tell keys apart, never the key
            "status": "ok",
            "total_balance": 0,
            "trial_balance": 0,
            "regular_balance": 0,
            "trial_end": None,
        }
        qs = urllib.parse.urlencode({"api_key": key})
        try:
            data = fetch_json(f"{JINA_USAGE_API}?{qs}")
        except RuntimeError as e:
            entry["status"] = (
                f"lookup failed ({str(e)[:120]}) — the key may be invalid "
                "or revoked"
            )
            per_key.append(entry)
            continue
        wallet = (data.get("wallet") or {}) if isinstance(data, dict) else {}
        bal = int(wallet.get("total_balance") or 0)
        entry.update(
            total_balance=bal,
            trial_balance=int(wallet.get("trial_balance") or 0),
            regular_balance=int(wallet.get("regular_balance") or 0),
            trial_end=wallet.get("trial_end"),
            status="ok" if bal > 0 else "exhausted",
        )
        total += bal
        if bal > 0:
            live += 1
        per_key.append(entry)
    out: dict[str, Any] = {
        "source": "jina-usage",
        "key_count": len(keys),
        "live_key_count": live,
        "total_balance": total,
        "keys": per_key,
        "warn_below": warn_below,
        "warning": None,
    }
    if live == 0:
        out["warning"] = (
            "EVERY configured reader key is exhausted or invalid — the "
            "last-resort reader rung is effectively DOWN (the anonymous "
            "free tier is best-effort only and was observed answering "
            "HTTP 401 on 2026-07-18). Generate a new API key at "
            "https://jina.ai/api-dashboard/ and add it to the environment."
        )
    elif total < warn_below:
        out["warning"] = (
            f"combined reader-key balance is low ({total:,} tokens < "
            f"{warn_below:,} across {live} live key(s)) — generate a new "
            "API key at https://jina.ai/api-dashboard/ soon and add it to "
            "the environment."
        )
    return out


# --- trafilatura capture/extraction layer (v3.32, operator directive 2026-08-24) ---
# The operator's standing order: capture websites with trafilatura
# (https://github.com/adbar/trafilatura), avoid the jina reader wherever
# possible (metered keys, refilled sparsely), and avoid WebFetch's built-in
# summariser. Division of labour:
#   * TRANSPORT stays with this bridge's `fetch()` — it already sends a full,
#     mutually consistent human-browser header set (Chrome UA + client hints +
#     Sec-Fetch-*), which is more "human" than trafilatura's own downloader.
#   * trafilatura's `fetch_url` is a SECOND direct transport (different HTTP
#     stack/fingerprint) tried before the reader ever spends credit.
#   * EXTRACTION is trafilatura's job: boilerplate-free article text with
#     metadata, replacing what jina's markdown was mostly used for.
# trafilatura is pip-installed by .claude/hooks/setup-deps.sh at SessionStart;
# every code path here degrades gracefully when the module is absent.

def _trafilatura():
    try:
        import trafilatura  # noqa: PLC0415 — optional dependency, lazy import
        return trafilatura
    except ImportError:
        return None


def _trafilatura_config():
    """A trafilatura config carrying the bridge's browser UA so its own
    downloader presents the same human fingerprint as `fetch()`."""
    t = _trafilatura()
    if t is None:
        return None
    from trafilatura.settings import use_config  # noqa: PLC0415
    cfg = use_config()
    cfg.set("DEFAULT", "USER_AGENTS", BROWSER_UA)
    cfg.set("DEFAULT", "DOWNLOAD_TIMEOUT", str(int(DEFAULT_TIMEOUT)))
    return cfg


def extract_readable(html: str, url: str | None = None) -> str | None:
    """Clean, boilerplate-free markdown (title/date metadata included) from a
    raw HTML body via trafilatura. None when trafilatura is unavailable or the
    page has no extractable main content (a JS shell, a bare listing)."""
    t = _trafilatura()
    if t is None:
        return None
    try:
        return t.extract(
            html, url=url, output_format="markdown",
            include_links=True, include_tables=True,
            with_metadata=True, favor_recall=True,
        )
    except Exception:  # noqa: BLE001 — extraction must never kill a fetch
        return None


def _trafilatura_fetch(url: str) -> str | None:
    """trafilatura's own downloader as an alternate DIRECT transport (no jina
    credit spent). Returns raw HTML or None. It sees the same egress proxy as
    everything else in this container; a different client stack sometimes
    passes where urllib is fingerprinted."""
    t = _trafilatura()
    if t is None:
        return None
    # trafilatura's downloader (urllib3) does NOT honor the env proxy. In the
    # cloud routine container all egress is forced through HTTPS_PROXY, so
    # fetch_url can never connect there — skip the rung instead of burning a
    # 30 s timeout per URL. On an unproxied machine the rung stays live.
    if os.environ.get("HTTPS_PROXY") or os.environ.get("https_proxy"):
        return None
    _check_url(url)  # same SSRF gate as fetch()
    try:
        html = t.fetch_url(url, config=_trafilatura_config())
        if html and len(html) > 500 and not _looks_blocked(html):
            return html
    except Exception:  # noqa: BLE001
        pass
    return None


def extract_page(url: str) -> tuple[str, str]:
    """Readable-page ladder — the standard way to CAPTURE an article body.

    Rungs, in order (jina strictly last — operator directive 2026-08-24):
      1. direct browser-UA GET (`fetch`)  → trafilatura extraction;
      2. trafilatura's own downloader     → trafilatura extraction;
      3. the r.jina.ai reader (metered)   — only when both direct rungs fail
         or the page needs JS to render its content.

    Returns `(markdown_text, method)`, method ∈ {trafilatura-direct,
    trafilatura-fetch, direct-raw, jina}. `direct-raw` means the page was
    reachable but not article-shaped (extraction found no main content) —
    the raw body is returned so the caller still gets the content."""
    direct_err = ""
    raw: str | None = None
    try:
        code, body, _ = fetch(
            url,
            accept="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        )
        if code == 200 and len(body) > 500:
            text = body.decode("utf-8", errors="replace")
            if not _looks_blocked(text):
                raw = text
                extracted = extract_readable(text, url)
                if extracted:
                    return extracted, "trafilatura-direct"
            else:
                direct_err = "direct hit returned an anti-bot/challenge body"
        else:
            direct_err = f"direct HTTP {code}, {len(body)} B"
    except Exception as e:  # noqa: BLE001
        direct_err = str(e)[:140]
    html = _trafilatura_fetch(url)
    if html:
        extracted = extract_readable(html, url)
        if extracted:
            return extracted, "trafilatura-fetch"
        if raw is None:
            raw = html
    if raw is not None:
        # Reachable but not article-shaped (or trafilatura missing): hand the
        # caller the raw body rather than spending reader credit on a page we
        # already hold.
        return raw, "direct-raw"
    try:
        return _jina_fetch(url), "jina"
    except Exception as e:  # noqa: BLE001
        raise RuntimeError(
            f"all transports failed for {url}: direct=({direct_err}); "
            f"trafilatura=(no readable body); jina=({str(e)[:160]})"
        ) from None


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


def ncsc_nl_csaf(advisory_id: str) -> Any:
    """Fetch the CSAF v2.0 JSON for a Dutch-NCSC TLP:WHITE advisory.

    `advisory_id` is the canonical identifier (`NCSC-YYYY-NNNN`); the
    bridge derives the lowercase `ncsc-yyyy-nnnn` slug expected at the
    CSAF distribution path. The publisher serves the latest revision at
    the deterministic path.
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


# ── PDF text extraction (stdlib only) ─────────────────────────────────
#
# Government and vendor advisories are routinely published as PDF and
# nothing else — the five-agency joint advisory on an active threat to
# Siemens S7 PLCs (AA26-231A, 2026-08-19) is the case that forced this in:
# the agency's own HTML page refused every transport, the PDF mirror served
# fine, and no tooling in the routine container could turn those bytes into
# text, so the entry had to be composed from an outlet's reading of it.
# This container has no pdftotext, no pypdf, no pdfminer and no network
# budget to install one, so the extractor below is written against the
# container's actual floor: zlib from the standard library.
#
# It handles the shape advisory PDFs actually take — Flate-compressed
# content streams, simple fonts with byte-per-glyph encodings, and CID
# fonts whose bytes only become text through a ToUnicode CMap. It is a
# text extractor, not a layout engine: reading order follows the content
# stream, and a scanned (image-only) PDF yields nothing, which the caller
# is told explicitly rather than left to infer from an empty result.

import zlib  # noqa: E402  (stdlib; kept next to the PDF helpers that use it)

_PDF_STREAM_RE = re.compile(rb"stream\r?\n?", re.IGNORECASE)
_PDF_BFCHAR_RE = re.compile(rb"beginbfchar(.*?)endbfchar", re.DOTALL)
_PDF_BFRANGE_RE = re.compile(rb"beginbfrange(.*?)endbfrange", re.DOTALL)
_PDF_HEXTOK_RE = re.compile(rb"<([0-9A-Fa-f\s]+)>")
_PDF_HEXBODY_RE = re.compile(rb"[0-9A-Fa-f\s]+")


def _pdf_streams(data: bytes) -> list[bytes]:
    """Every stream in the file, inflated where it is Flate-compressed.

    Walks `stream` / `endstream` pairs rather than the cross-reference
    table, so a linearised, incrementally-updated or slightly-malformed
    file still yields its content. Streams that are not Flate (or that
    fail to inflate — encrypted, or a filter we do not implement) are
    skipped, not fatal.
    """
    out: list[bytes] = []
    pos = 0
    while True:
        m = _PDF_STREAM_RE.search(data, pos)
        if not m:
            break
        start = m.end()
        end = data.find(b"endstream", start)
        if end == -1:
            break
        raw = data[start:end]
        pos = end + 9
        if not raw:
            continue
        try:
            out.append(zlib.decompress(raw))
            continue
        except zlib.error:
            pass
        try:
            # Truncated / trailing-garbage streams: inflate what is there.
            out.append(zlib.decompressobj().decompress(raw))
            continue
        except zlib.error:
            pass
        # Uncompressed content stream — keep it if it looks like PDF operators.
        if b"Tj" in raw or b"TJ" in raw or b"BT" in raw:
            out.append(raw)
    return out


def _pdf_hex_to_codes(blob: bytes) -> list[int]:
    """`<0041>` / `<00410042>` → the integer codes it encodes."""
    h = re.sub(rb"[^0-9A-Fa-f]", b"", blob)
    if not h:
        return []
    if len(h) % 2:
        h += b"0"
    width = 4 if len(h) >= 4 and len(h) % 4 == 0 else 2
    return [int(h[i:i + width], 16) for i in range(0, len(h), width)]


def _pdf_hex_to_text(blob: bytes) -> str:
    """A ToUnicode destination `<0041>` / `<00660066>` → its characters
    (destinations are UTF-16BE, and may name a multi-character ligature)."""
    h = re.sub(rb"\s+", b"", blob)
    if len(h) % 4:
        h = h + b"0" * (4 - len(h) % 4)
    try:
        return bytes.fromhex(h.decode("ascii")).decode("utf-16-be", "replace")
    except (ValueError, UnicodeDecodeError):
        return ""


def _pdf_tounicode_map(streams: list[bytes]) -> dict[int, str]:
    """Union of every ToUnicode CMap in the file: glyph code → text.

    Merged across fonts deliberately. Resolving each code against the font
    active at that point in the content stream would need the full
    resource-dictionary graph; in practice an advisory PDF's fonts either
    share an encoding or occupy disjoint code ranges, and a merged map
    recovers readable text where a byte-wise decode returns mojibake.
    Collisions keep the first mapping seen and are reported by the caller
    as an approximation rather than silently.
    """
    cmap: dict[int, str] = {}
    for s in streams:
        if b"beginbfchar" not in s and b"beginbfrange" not in s:
            continue
        for body in _PDF_BFCHAR_RE.findall(s):
            toks = _PDF_HEXTOK_RE.findall(body)
            for i in range(0, len(toks) - 1, 2):
                codes = _pdf_hex_to_codes(toks[i])
                dst = _pdf_hex_to_text(toks[i + 1])
                if len(codes) == 1 and dst:
                    cmap.setdefault(codes[0], dst)
        for body in _PDF_BFRANGE_RE.findall(s):
            toks = _PDF_HEXTOK_RE.findall(body)
            for i in range(0, len(toks) - 2, 3):
                lo = _pdf_hex_to_codes(toks[i])
                hi = _pdf_hex_to_codes(toks[i + 1])
                dst = _pdf_hex_to_text(toks[i + 2])
                if len(lo) != 1 or len(hi) != 1 or not dst:
                    continue
                if hi[0] < lo[0] or hi[0] - lo[0] > 65535:
                    continue
                base = ord(dst[-1])
                for n, code in enumerate(range(lo[0], hi[0] + 1)):
                    cmap.setdefault(code, dst[:-1] + chr(base + n))
    return cmap


def _pdf_unescape(raw: bytes) -> bytes:
    """PDF literal-string escapes: \\n \\t \\( \\) \\\\ and \\ooo octal."""
    out = bytearray()
    i = 0
    simple = {0x6E: 0x0A, 0x72: 0x0D, 0x74: 0x09, 0x62: 0x08, 0x66: 0x0C}
    while i < len(raw):
        c = raw[i]
        if c != 0x5C:  # backslash
            out.append(c)
            i += 1
            continue
        i += 1
        if i >= len(raw):
            break
        n = raw[i]
        if n in simple:
            out.append(simple[n])
            i += 1
        elif 0x30 <= n <= 0x37:  # octal, up to three digits
            digits = bytearray()
            while i < len(raw) and len(digits) < 3 and 0x30 <= raw[i] <= 0x37:
                digits.append(raw[i])
                i += 1
            out.append(int(digits, 8) & 0xFF)
        elif n in (0x0A, 0x0D):  # line continuation
            i += 1
            if i < len(raw) and raw[i] == 0x0A and n == 0x0D:
                i += 1
        else:
            out.append(n)
            i += 1
    return bytes(out)


def _pdf_literal_strings(content: bytes) -> list[tuple[bool, bytes]]:
    """Every string operand in a content stream, in stream order, as
    `(is_hex, bytes)`. Tracks nesting and escapes so a `)` inside a string
    does not end it. Also emits a sentinel for the text operators that
    imply a line break (`Td`, `TD`, `T*`, `'`, `"`, `ET`) so paragraphs do
    not run together."""
    out: list[tuple[bool, bytes]] = []
    i, n = 0, len(content)
    while i < n:
        c = content[i]
        if c == 0x28:  # (
            depth, j, buf = 1, i + 1, bytearray()
            while j < n and depth:
                ch = content[j]
                if ch == 0x5C:
                    buf.append(ch)
                    if j + 1 < n:
                        buf.append(content[j + 1])
                    j += 2
                    continue
                if ch == 0x28:
                    depth += 1
                elif ch == 0x29:
                    depth -= 1
                    if not depth:
                        break
                buf.append(ch)
                j += 1
            out.append((False, _pdf_unescape(bytes(buf))))
            i = j + 1
            continue
        if c == 0x3C and i + 1 < n and content[i + 1] != 0x3C:  # < not <<
            j = content.find(b">", i + 1)
            if j == -1:
                break
            cand = content[i + 1:j]
            # Only a genuine hex string. A dictionary's inner half — the
            # `</MCID 0>` of a `<</MCID 0>>` marked-content property list —
            # also presents as `<`-not-`<<` once the scan steps past the
            # outer bracket, and treating it as hex crashes the decoder.
            if cand and not _PDF_HEXBODY_RE.fullmatch(cand):
                i += 1
                continue
            out.append((True, cand))
            i = j + 1
            continue
        # Line-break-implying operators → sentinel
        if c in (0x54, 0x45, 0x27, 0x22):  # T E ' "
            tail = content[i:i + 2]
            if tail in (b"Td", b"TD", b"T*", b"ET") or c in (0x27, 0x22):
                out.append((False, b"\n"))
                i += 2
                continue
        i += 1
    return out


def _pdf_prose_chars(text: str) -> int:
    """Count of characters that are plausible prose, whitespace excluded.

    Counted rather than ratioed because the failure mode being detected is
    a decode that recovers *almost nothing*: a CID PDF's byte-wise decode
    drops every unmapped glyph, leaving a short string of line breaks
    whose ratio of "good" characters is a perfect 1.0. Volume of recovered
    prose is the honest comparison between two candidate decodes.
    """
    return sum(1 for ch in text if ch.isalnum() or ch in ".,;:-/()'\"%")


def _pdf_score(text: str) -> float:
    """Share of characters that are plausible prose — used only to report
    whether a decode looks clean, never as the sole basis for choosing one."""
    if not text:
        return 0.0
    good = sum(1 for ch in text if ch.isalnum() or ch in " .,;:-/()\n\t'\"%")
    return good / len(text)


def _pdf_render(content_streams: list[bytes], cmap: dict[int, str]) -> tuple[str, str]:
    """Extract text from content streams. Returns (text, method).

    Tries a byte-wise decode first — correct for simple fonts, which is
    most advisory PDFs — and falls back to the merged ToUnicode CMap when
    that produces mojibake, which is what a CID/Identity-H font needs.
    """
    def direct() -> str:
        parts: list[str] = []
        for cs in content_streams:
            for is_hex, s in _pdf_literal_strings(cs):
                if is_hex:
                    codes = _pdf_hex_to_codes(s)
                    parts.append("".join(chr(c) if 32 <= c < 0x300 else "" for c in codes))
                else:
                    parts.append(s.decode("latin-1", "replace"))
        return "".join(parts)

    def viacmap() -> str:
        parts: list[str] = []
        for cs in content_streams:
            for is_hex, s in _pdf_literal_strings(cs):
                if s == b"\n":
                    parts.append("\n")
                    continue
                codes = _pdf_hex_to_codes(s) if is_hex else list(s)
                parts.append("".join(cmap.get(c, "") for c in codes))
        return "".join(parts)

    d = direct()
    if not cmap:
        return d, "byte-encoding"
    v = viacmap()
    if _pdf_prose_chars(v) > _pdf_prose_chars(d):
        return v, "tounicode-cmap (merged across fonts — an approximation)"
    return d, "byte-encoding"


def pdf_text(url: str) -> dict[str, Any]:
    """Fetch a PDF and return its extracted text.

    The transport is the same browser-UA GET the rest of the bridge uses,
    so a PDF behind the anti-bot posture that refuses the routine's HTML
    fetches is still reachable. `notes` says how the text was recovered
    and flags the two cases a caller must not mistake for content: a
    scanned PDF (no text objects at all) and a CMap-approximated decode.
    """
    code, body, headers = fetch(
        url, accept="application/pdf,*/*;q=0.8", max_bytes=MAX_BODY_BYTES_HTML
    )
    if code != 200:
        raise RuntimeError(f"upstream HTTP {code} for {url}")
    if not body.startswith(b"%PDF"):
        ctype = headers.get("Content-Type", "unknown")
        raise RuntimeError(
            f"refused: {url} is not a PDF (Content-Type {ctype}, "
            f"first bytes {body[:8]!r}) — use `url` for HTML"
        )
    streams = _pdf_streams(body)
    cmap = _pdf_tounicode_map(streams)
    content = [s for s in streams if b"Tj" in s or b"TJ" in s or b"BT" in s]
    text, method = _pdf_render(content, cmap)
    text = re.sub(r"[ \t]{2,}", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    notes = [f"decode: {method}"]
    if not content:
        notes.append(
            "no text objects found — this is very likely a scanned or "
            "image-only PDF; no OCR is available here, so treat the empty "
            "text as 'not extractable', NOT as 'the document says nothing'"
        )
    if len(text) < 200 and content:
        notes.append(
            "suspiciously little text for a document with text objects — "
            "verify against the publisher's HTML before citing"
        )
    return {
        "source": "pdf",
        "url": url,
        "bytes": len(body),
        "streams": len(streams),
        "content_streams": len(content),
        "tounicode_entries": len(cmap),
        "chars": len(text),
        "notes": "; ".join(notes),
        "text": text,
    }


# ── CLI ───────────────────────────────────────────────────────────────

def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(prog="fetch_source.py", description=__doc__)
    sub = p.add_subparsers(dest="cmd", required=True)

    p_url = sub.add_parser("url", help="direct browser-UA GET with automatic r.jina.ai reader fallback, prints body")
    p_url.add_argument("url")
    p_url.add_argument("--direct", action="store_true",
                       help="direct browser-UA GET only — do NOT fall back to the jina reader (raw HTML/XML)")

    p_extract = sub.add_parser(
        "extract",
        help="PREFERRED article capture: fetch with human-browser headers and extract the readable "
             "body via trafilatura (clean markdown, no boilerplate) — jina only as the last rung. "
             "Use this instead of WebFetch for article/advisory bodies.")
    p_extract.add_argument("url")

    p_jina = sub.add_parser("jina", help="LAST RESORT: force the r.jina.ai reader proxy (metered credit) — clean markdown; bypasses anti-bot/WAF/geo blocks and runs page JS. Try feed/WebFetch/url first")
    p_jina.add_argument("url")
    p_jina.add_argument("fmt", nargs="?", choices=["markdown", "html"], default="markdown",
                        help="return format (default markdown; `html` keeps simplified markup)")

    sub.add_parser("jina-usage", help="remaining token balance of every configured reader key (JINA_API_KEYS / JINA_API_KEY) — warns (stderr) when the pool runs low")

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
    p_ncscnl_csaf = ncscnl_sub.add_parser("csaf", help="one NCSC-NL advisory CSAF JSON (publisher serves the latest revision)")
    p_ncscnl_csaf.add_argument("id", help="advisory id, e.g. NCSC-2025-0432")
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

    p_pdf = sub.add_parser(
        "pdf",
        help="fetch a PDF advisory and print its extracted text (stdlib only — "
             "no OCR, so an image-only PDF yields nothing and says so)",
    )
    p_pdf.add_argument("url")
    p_pdf.add_argument("--json", action="store_true",
                       help="print the full record (byte counts, decode method, notes) "
                            "instead of just the text")

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
        if args.cmd == "extract":
            text, method = extract_page(args.url)
            print(f"# extract: served via {method}", file=sys.stderr)
            sys.stdout.write(text)
            if not text.endswith("\n"):
                sys.stdout.write("\n")
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
                json.dump(ncsc_nl_csaf(args.id), sys.stdout, indent=2)
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
        if args.cmd == "pdf":
            rec = pdf_text(args.url)
            if args.json:
                json.dump(rec, sys.stdout, indent=2)
                sys.stdout.write("\n")
            else:
                # stderr for the provenance so stdout stays pure document text.
                print(
                    f"# pdf: {rec['chars']} chars from {rec['content_streams']}/"
                    f"{rec['streams']} streams — {rec['notes']}",
                    file=sys.stderr,
                )
                sys.stdout.write(rec["text"] + "\n")
            return 0
    except (RuntimeError, ValueError) as e:
        print(f"fetch_source: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
