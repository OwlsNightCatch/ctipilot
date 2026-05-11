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
stdlib (`urllib`, `json`, `argparse`). Outbound requests are restricted
to HTTPS hosts the agent already has WebFetch permission for.

The script will NEVER:
- Submit forms or attempt authentication.
- Fetch hidden / authenticated content (the agent must respect TLP).
- Bypass robots.txt-blocked paths.
- Run third-party JS or load any other origin.

Hosts the bridge cannot get content from (recorded here so the routine
prompt can route them to WebSearch fallback without the agent retrying
the bridge first):
- inside-it.ch — Cloudflare Managed Challenge ("Just a moment..."),
  refuses every UA. WebSearch fallback only.
- databreaches.net — Cloudflare Managed Challenge, same posture.
  WebSearch fallback only.
- prodaft.com /blogs — Next.js SPA; the /sitemap.xml route is
  server-rendered XML and per-post URLs are server-rendered HTML;
  bridge recipe: `url https://www.prodaft.com/sitemap.xml` for
  discovery, then `url <per-post URL>` for content.
- ico.org.uk /action-weve-taken/enforcement/ — JS-rendered listing;
  per-enforcement URLs are server-rendered. Bridge recipe:
  `url https://ico.org.uk/sitemap.xml` (5 MB), filter for
  `/action-weve-taken/enforcement/`, then `url <per-action URL>`.
- bleepingcomputer.com article URLs — Cloudflare 403 on article pages
  even when the listing returns 200. Recipe: `url
  https://www.bleepingcomputer.com/news/security/` for discovery,
  WebSearch fallback for article content.

Usage:
    python3 tools/fetch_source.py url <URL>                          # plain GET with browser UA, prints body
    python3 tools/fetch_source.py ncsc-csh list [N]                  # NCSC CSH public dashboard (last N TLP:CLEAR posts as JSON)
    python3 tools/fetch_source.py ncsc-csh post <ID>                 # one TLP:CLEAR post (Markdown body + metadata)
    python3 tools/fetch_source.py ncsc-csh recent [N]                # combined: list + each post's full content (default 10)
    python3 tools/fetch_source.py cisa-kev                           # full CISA KEV JSON catalog
    python3 tools/fetch_source.py cisa page <URL>                    # CISA HTML advisory / news page (browser UA)
    # v2.48 — additional bridge endpoints for known-403 / SPA-only sources
    python3 tools/fetch_source.py enisa-euvd recent [KIND]           # KIND ∈ lastvulnerabilities (default) | criticals | exploited
    python3 tools/fetch_source.py enisa-euvd advisory <ID>           # one EUVD advisory by id (e.g. EUVD-2025-12345)
    python3 tools/fetch_source.py bsi-rss                            # BSI cert-bund WID-SEC RSS feed (XML)
    python3 tools/fetch_source.py bsi-csaf <WID-SEC-ID>              # BSI WID-SEC advisory CSAF JSON (full body — e.g. WID-SEC-2026-1438)
    python3 tools/fetch_source.py ncsc-nl csaf <ID> [VERSION]        # Dutch NCSC CSAF advisory (e.g. NCSC-2025-0432, default v1)

Examples:
    python3 tools/fetch_source.py ncsc-csh recent 5
    python3 tools/fetch_source.py ncsc-csh post 12542
    python3 tools/fetch_source.py cisa-kev | jq '.vulnerabilities | length'
    python3 tools/fetch_source.py enisa-euvd recent criticals | jq '. | length'
    python3 tools/fetch_source.py bsi-rss | grep -c '<item>'
    python3 tools/fetch_source.py bsi-csaf WID-SEC-2026-1438 | jq '.document.title'
    python3 tools/fetch_source.py ncsc-nl csaf NCSC-2025-0432 1
    python3 tools/fetch_source.py url https://www.cisa.gov/news-events/cybersecurity-advisories
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
BROWSER_UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"
)

# Hostname allow-list — every fetch must target one of these. Keeps the
# script narrowly scoped to publishers documented in the prompt's
# fallback recipe; protects against an agent passing in an arbitrary
# attacker-controlled URL. Each host was verified to return HTTP 200
# with a stable desktop-Chrome User-Agent (see test matrix in the prompt).
ALLOWED_HOSTS = frozenset({
    # NCSC Switzerland Cyber Security Hub (TLP:CLEAR public slice)
    "security-hub.ncsc.admin.ch",
    # CISA — pages, news, directives, KEV catalog
    "www.cisa.gov", "cisa.gov",
    # NCSC.ch press releases / CVE list
    "www.ncsc.admin.ch", "ncsc.admin.ch",
    # CSIRT Italy / Agenzia per la Cybersicurezza Nazionale
    "www.acn.gov.it", "acn.gov.it",
    # Cisco Talos research blog
    "blog.talosintelligence.com",
    # PRODAFT threat reports
    "www.prodaft.com", "prodaft.com",
    # Inside-IT Switzerland (Swiss IT industry news)
    "www.inside-it.ch", "inside-it.ch",
    # UK Information Commissioner's Office (data-breach notices) — JS-rendered listing,
    # but per-incident /action-weve-taken/<slug>/ pages render server-side
    "ico.org.uk", "www.ico.org.uk",
    # DataBreaches.net — independent breach tracker (403's WebFetch UA, added 2026-05-08)
    "databreaches.net", "www.databreaches.net",
    # NCC Group research blog (403's WebFetch UA via Akamai edge, added 2026-05-08)
    "www.nccgroup.com", "nccgroup.com",
    # Dragos OT/ICS research (TLS / cert handshake quirks on routine fetcher, added 2026-05-08 as fallback)
    "www.dragos.com", "dragos.com",
    # Sygnia IR (Cloudflare interstitial fallback, added 2026-05-08)
    "www.sygnia.co", "sygnia.co",
    # CCN-CERT Spain (kept in case the geo block ever lifts; currently 403 even via bridge)
    "www.ccn-cert.cni.es", "ccn-cert.cni.es",
    # ─── v2.48 expansion (added 2026-05-10) ───────────────────────────
    # ENISA EUVD — SPA dashboard at euvd.enisa.europa.eu (this is the human-
    # reader landing the brief cites), backed by a JSON REST API at the
    # *separate* host euvdservices.enisa.europa.eu (path `/api/...`). The
    # 2026-05-11 hotfix points the bridge at the services host after the
    # `/enisaeuvd/api/*` paths on the SPA host started returning the SPA
    # shell with HTTP 200 (== empty body for callers expecting JSON).
    "euvd.enisa.europa.eu",
    "euvdservices.enisa.europa.eu",
    # BSI cert-bund — RSS feed at /content/public/securityAdvisory/rss
    # works; the per-advisory HTML pages return empty without browser
    # rendering. Bridge supports the RSS feed and per-WID-SEC pages.
    "wid.cert-bund.de",
    # Dutch NCSC — CSAF advisories. The /advisories/ listing is an SPA;
    # the publisher's CSAF distribution lives at
    # /csaf/v2/{year}/ncsc-{year}-{nnnn}.json (per the well-known
    # provider-metadata advertisement on advisories.ncsc.nl).
    "advisories.ncsc.nl", "www.ncsc.nl", "ncsc.nl",
    # CERT-FR France — /avis/ index is RSS-only; per-advisory pages need
    # a browser UA. Bridge handles both.
    "www.cert.ssi.gouv.fr", "cert.ssi.gouv.fr",
    # CERT-EU — security advisories index is RSS-only; per-advisory pages
    # need the browser UA.
    "cert.europa.eu", "www.cert.europa.eu",
    # NCSC-NL — main site (separate from CSAF advisories above).
    # CERT-PL — /en/news/ listing returns empty without browser UA.
    "cert.pl", "www.cert.pl",
    # NCSC-UK — /section/keep-up-to-date/reports-advisories
    "www.ncsc.gov.uk", "ncsc.gov.uk",
    # ─── v2.49 expansion (added 2026-05-11) ───────────────────────────
    # BleepingComputer — root, RSS feed and /news/security/ listing all
    # respond 200 to the bridge's desktop-Chrome UA; individual article
    # pages may still return 403 (Cloudflare anti-bot on article URLs).
    # Listing-level discovery is the supported recipe; article-level
    # content falls back to WebSearch.
    "www.bleepingcomputer.com", "bleepingcomputer.com",
})

# Hosts that sit behind Cloudflare's Managed Challenge ("Just a moment...")
# and reject every UA / header combination the bridge can construct. They
# remain on `ALLOWED_HOSTS` for the rare path that does respond (e.g. an
# RSS feed Cloudflare exempts), but the canonical recipe is WebSearch
# fallback; the bridge will record the 403 in `fetch_failures` and the
# routine prompt directs the agent to WebSearch from there.
CLOUDFLARE_BLOCKED_HOSTS = frozenset({
    # inside-it.ch — every path returns the CF challenge body inside an
    # HTTP 403 response. Confirmed 2026-05-11.
    "www.inside-it.ch", "inside-it.ch",
    # databreaches.net — same posture across root + /feed/ + per-article
    # URLs. Confirmed 2026-05-11.
    "databreaches.net", "www.databreaches.net",
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
    """Strict allowlist gate: scheme is https, host is on ALLOWED_HOSTS,
    and the resolved IP is not loopback / link-local / private /
    cloud-metadata. Called for the initial request AND for every redirect
    destination (see SafeRedirectHandler below)."""
    parsed = urllib.parse.urlparse(url)
    host = (parsed.hostname or "").lower()
    scheme = (parsed.scheme or "").lower()
    if scheme != "https":
        raise ValueError(f"refused: only https:// is allowed (got {scheme!r})")
    if not host:
        raise ValueError("refused: no host in URL")
    if host not in ALLOWED_HOSTS:
        raise ValueError(
            f"refused: host {host!r} is not in the allow-list. "
            "Add it explicitly to ALLOWED_HOSTS if you have a reason to fetch from there."
        )
    # Resolve and check. Even an allowlisted host with a poisoned A record
    # pointing at 127.0.0.1 must be refused.
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
) -> tuple[int, bytes, dict[str, str]]:
    """Plain GET with browser headers. Returns (status, body_bytes, headers).

    Refuses non-https URLs, hosts outside ALLOWED_HOSTS, and any redirect
    that lands outside the same allowlist. Body size is capped at
    `max_bytes`.
    """
    _check_url(url)
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": BROWSER_UA,
            "Accept": accept,
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "identity",  # avoid gzip — keep stdout simple
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Upgrade-Insecure-Requests": "1",
        },
    )
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

    p_ncscnl = sub.add_parser("ncsc-nl", help="Dutch NCSC CSAF advisories (JSON)")
    ncscnl_sub = p_ncscnl.add_subparsers(dest="ncscnl_cmd", required=True)
    p_ncscnl_csaf = ncscnl_sub.add_parser("csaf", help="one NCSC-NL advisory CSAF JSON")
    p_ncscnl_csaf.add_argument("id", help="advisory id, e.g. NCSC-2025-0432")
    p_ncscnl_csaf.add_argument("version", type=int, nargs="?", default=1, help="CSAF revision (default 1)")

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
                if "cisa.gov" not in (urllib.parse.urlparse(args.url).hostname or ""):
                    print("error: cisa page URL must be on cisa.gov", file=sys.stderr)
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
            return 0
    except (RuntimeError, ValueError) as e:
        print(f"fetch_source: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
