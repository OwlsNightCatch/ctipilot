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
"""

from __future__ import annotations

import argparse
import ipaddress
import json
import socket
import ssl
import sys
import time
import urllib.error
import urllib.request
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

DESKTOP_UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
)


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


def _check(url: str, *, timeout: float) -> tuple[int | None, int, str]:
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
            if e.code in (405, 501) and method == "HEAD":
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


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--dry-run", action="store_true",
                   help="print results, do not write state/source_health.json")
    p.add_argument("--timeout", type=float, default=12.0,
                   help="per-request timeout in seconds (default 12)")
    p.add_argument("--history-cap", type=int, default=12,
                   help="how many runs to retain per source (default 12)")
    args = p.parse_args()

    if not SOURCES_JSON.exists():
        print(f"FATAL: {SOURCES_JSON} not found", file=sys.stderr)
        return 2
    try:
        sources_data = json.loads(SOURCES_JSON.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"FATAL: cannot parse sources.json: {e}", file=sys.stderr)
        return 2
    sources = [s for s in sources_data.get("sources", []) if s.get("status") == "active"]
    if not sources:
        print("No active sources to check.")
        return 0

    fetched_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print(f"# source-health snapshot — {fetched_at}")
    print(f"# checking {len(sources)} active source(s); timeout={args.timeout}s")

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

    results: list[dict[str, Any]] = []
    for s in sources:
        sid = s.get("id", "")
        url = s.get("url", "")
        if not url:
            continue
        host = (urlparse(url).hostname or "").lower()
        status, latency_ms, err = _check(url, timeout=args.timeout)
        cls = _classify(status, host)
        rec = {
            "id": sid,
            "url": url,
            "host": host,
            "status_code": status,
            "latency_ms": latency_ms,
            "class": cls,
            "fetched_at": fetched_at,
        }
        if err:
            rec["error"] = err
        results.append(rec)
        # Human-readable line.
        st_disp = str(status) if status is not None else "—"
        print(f"  [{cls:>13}] {st_disp:>3}  {latency_ms:>5} ms  {sid:<32}  {host}")

    # Group counts for quick top-line.
    by_class: dict[str, int] = {}
    for r in results:
        by_class[r["class"]] = by_class.get(r["class"], 0) + 1
    print()
    print("# class breakdown:")
    for cls in ("ok", "redirect-ok", "ua-blocked", "client-error", "server-error", "unreachable"):
        n = by_class.get(cls, 0)
        if n:
            print(f"  {n:>3}× {cls}")

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
    runs.append({"fetched_at": fetched_at, "results": results, "by_class": by_class})
    runs = runs[-args.history_cap :]
    out = {
        "schema_version": 1,
        "schema": "Independent weekly source-health snapshot. Surface in /ops/.",
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
