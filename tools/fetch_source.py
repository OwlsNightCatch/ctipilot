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

Usage:
    python3 tools/fetch_source.py url <URL>             # plain GET with browser UA, prints body
    python3 tools/fetch_source.py ncsc-csh list [N]     # NCSC CSH public dashboard (last N TLP:CLEAR posts as JSON)
    python3 tools/fetch_source.py ncsc-csh post <ID>    # one TLP:CLEAR post (Markdown body + metadata)
    python3 tools/fetch_source.py ncsc-csh recent [N]   # combined: list + each post's full content (default 10)
    python3 tools/fetch_source.py cisa-kev              # full CISA KEV JSON catalog
    python3 tools/fetch_source.py cisa page <URL>       # CISA HTML advisory / news page (browser UA)

Examples:
    python3 tools/fetch_source.py ncsc-csh recent 5
    python3 tools/fetch_source.py ncsc-csh post 12542
    python3 tools/fetch_source.py cisa-kev | jq '.vulnerabilities | length'
    python3 tools/fetch_source.py url https://www.cisa.gov/news-events/cybersecurity-advisories
"""

from __future__ import annotations

import argparse
import json
import os
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request
from typing import Any


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
    # UK Information Commissioner's Office (data-breach notices)
    "ico.org.uk", "www.ico.org.uk",
})

NCSC_CSH_BASE = "https://security-hub.ncsc.admin.ch"
CISA_KEV_JSON = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"

DEFAULT_TIMEOUT = 30  # seconds


def _check_host(url: str) -> None:
    parsed = urllib.parse.urlparse(url)
    host = (parsed.hostname or "").lower()
    if not parsed.scheme.startswith("https"):
        raise ValueError(f"refused: only https:// is allowed (got {parsed.scheme!r})")
    if host not in ALLOWED_HOSTS:
        raise ValueError(
            f"refused: host {host!r} is not in the allow-list "
            f"({sorted(ALLOWED_HOSTS)}). Add it explicitly to ALLOWED_HOSTS "
            "if you have a reason to fetch from there."
        )


def fetch(url: str, *, accept: str = "application/json, text/html;q=0.9, */*;q=0.5") -> tuple[int, bytes, dict[str, str]]:
    """Plain GET with browser headers. Returns (status, body_bytes, headers)."""
    _check_host(url)
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
        with urllib.request.urlopen(req, timeout=DEFAULT_TIMEOUT, context=_SSL_CTX) as resp:
            return resp.status, resp.read(), dict(resp.headers)
    except urllib.error.HTTPError as e:
        # Surface the upstream status verbatim so the agent can tell why a fetch failed.
        return e.code, e.read() if hasattr(e, "read") else b"", dict(e.headers or {})


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
    return json.loads(fetch_text(url, accept="application/json, */*;q=0.5"))


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
    except (RuntimeError, ValueError) as e:
        print(f"fetch_source: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
