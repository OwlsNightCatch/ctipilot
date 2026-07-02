#!/usr/bin/env python3
"""tools/source_candidates.py — surface "sources we should add" candidates.

Walks the last 30 days of briefs, counts every outbound link host, subtracts
hosts already in `sources/sources.json` (and the "discovery only" news-
aggregator allowlist that the routine never wants to promote to a primary),
and outputs the top-N missing-but-cited domains with citation counts and a
sample of brief paths where each appeared.

Pure post-hoc analytics; no runtime cost on the brief routine. The operator
runs this manually (or as a weekly cron) to spot publishers worth promoting
to `status: candidate` in `sources.json`.

Usage:
    python3 tools/source_candidates.py                # last 30 days, top 20
    python3 tools/source_candidates.py --window-days 14 --top 30
    python3 tools/source_candidates.py --json         # machine-readable

Design rules: stdlib-only. No mutation of repo files. Read-only.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent.parent
BRIEFS_DIR = ROOT / "briefs"
SOURCES_JSON = ROOT / "sources" / "sources.json"

# News-aggregator hosts the routine never wants to promote to a primary.
# Mirrors the NEWS_AGGREGATOR_HOSTS list in tools/check_brief.py —
# kept as its own constant here so this script doesn't need to import a
# private name from check_brief.py.
AGGREGATOR_HOSTS: tuple[str, ...] = (
    "bleepingcomputer.com",
    "thehackernews.com",
    "feeds.feedburner.com",
    "securityaffairs.com",
    "securityweek.com",
    "helpnetsecurity.com",
    "therecord.media",
    "cyberscoop.com",
    "darkreading.com",
    "infosecurity-magazine.com",
    "risky.biz",
    "news.risky.biz",
    "krebsonsecurity.com",
    "schneier.com",
    "techcrunch.com",
    "techzine.eu",
    "dutchnews.nl",
    "heise.de",
    "inside-it.ch",
    "ictjournal.ch",
    "blick.ch",
    "ictjournal.fr",
    "lemondeinformatique.fr",
    "lemonde.fr",
    "theguardian.com",
    "spiegel.de",
    "meduza.io",
    "piunikaweb.com",
    "cyberkendra.com",
    "malwarebytes.com",
)

# Hosts that are already-tracked-but-via-different-id (CDNs, primary
# documentation hosts that should never appear as a candidate). Add to
# this list as you see noise in the output.
NEVER_PROMOTE_HOSTS: tuple[str, ...] = (
    "github.com",
    "gist.github.com",
    "youtube.com",
    "youtu.be",
    "twitter.com",
    "x.com",
    "linkedin.com",
    "wikipedia.org",
    "en.wikipedia.org",
    "nvd.nist.gov",
    "cve.mitre.org",
    "cve.org",
    "www.cve.org",
    "cwe.mitre.org",
    "attack.mitre.org",
    "docs.google.com",
    "drive.google.com",
    "archive.org",
    "web.archive.org",
)


INLINE_LINK_RE = re.compile(r"\[[^\]]+\]\((https?://[^)]+)\)")


def _root_host(url: str) -> str:
    """Returns the registered domain best-guess. We strip a leading `www.`
    and roll subdomains up to the last two labels for `co.uk` / `com.br`-
    style ccTLDs would over-collapse — but for our purposes the published
    sources are mostly .com / .ch / .de / .fr, where last-two-labels is the
    right answer. The few ccTLD edge cases collapse harmlessly."""
    try:
        u = urlsplit(url)
        host = (u.hostname or "").lower()
    except Exception:
        return ""
    if host.startswith("www."):
        host = host[4:]
    # Roll up to last two labels for the most common gTLD case. Authority-
    # tier ccTLDs (NCSC.ch, BSI.bund.de, cert-bund.de, …) are explicitly
    # in the sources.json allowlist already, so over-collapse here is fine.
    return host


def _is_in_sources(host: str, source_hosts: set[str]) -> bool:
    if not host:
        return True  # treat empty as already-tracked (skip)
    if host in source_hosts:
        return True
    # Match subdomain matches: a candidate host `blog.example.com` should
    # be treated as already-tracked if `example.com` is in sources.
    return any(host.endswith("." + s) or host == s for s in source_hosts)


def _is_noise_host(host: str) -> bool:
    if not host:
        return True
    return any(host == h or host.endswith("." + h) for h in AGGREGATOR_HOSTS + NEVER_PROMOTE_HOSTS)


def _read_briefs(window_days: int) -> list[Path]:
    if not BRIEFS_DIR.exists():
        return []
    today = datetime.now(timezone.utc).date()
    cutoff = today - timedelta(days=window_days)
    out: list[Path] = []
    for p in sorted(BRIEFS_DIR.glob("*.md")):
        m = re.match(r"^(\d{4}-\d{2}-\d{2})$", p.stem)
        if not m:
            continue
        try:
            y, mo, d = (int(x) for x in m.group(1).split("-"))
            d_iso = date(y, mo, d)
        except Exception:
            continue
        if d_iso >= cutoff:
            out.append(p)
    # Plus the most-recent ~5 weeklies since they extract source-date drift.
    weekly_dir = BRIEFS_DIR / "weekly"
    if weekly_dir.exists():
        weeklies = sorted(weekly_dir.glob("*.md"), reverse=True)[:5]
        out.extend(weeklies)
    return out


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--window-days", type=int, default=30,
                   help="how many days back to walk briefs (default 30)")
    p.add_argument("--top", type=int, default=20,
                   help="how many top missing-but-cited hosts to print (default 20)")
    p.add_argument("--json", action="store_true",
                   help="machine-readable JSON output instead of the human report")
    args = p.parse_args()

    # Load source.json hosts.
    source_hosts: set[str] = set()
    if SOURCES_JSON.exists():
        try:
            data = json.loads(SOURCES_JSON.read_text(encoding="utf-8"))
            for s in data.get("sources", []):
                u = s.get("url", "")
                h = _root_host(u)
                if h:
                    source_hosts.add(h)
        except Exception as e:
            print(f"WARN: cannot parse sources.json: {e}", file=sys.stderr)

    briefs = _read_briefs(args.window_days)
    if not briefs:
        print("No briefs in window.")
        return 0

    counts: dict[str, int] = defaultdict(int)
    samples: dict[str, list[str]] = defaultdict(list)
    total_links = 0
    for brief in briefs:
        try:
            text = brief.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        seen_in_brief: set[str] = set()
        for m in INLINE_LINK_RE.finditer(text):
            url = m.group(1)
            host = _root_host(url)
            total_links += 1
            if not host:
                continue
            if _is_in_sources(host, source_hosts):
                continue
            if _is_noise_host(host):
                continue
            if host in seen_in_brief:
                continue
            seen_in_brief.add(host)
            counts[host] += 1
            if len(samples[host]) < 3:
                samples[host].append(brief.name)

    ranked = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    top = ranked[: args.top]

    if args.json:
        out = {
            "window_days": args.window_days,
            "briefs_walked": len(briefs),
            "total_inline_links": total_links,
            "tracked_hosts": sorted(source_hosts),
            "candidates": [
                {"host": h, "citations": n, "sample_briefs": samples[h]}
                for h, n in top
            ],
        }
        print(json.dumps(out, indent=2))
        return 0

    print(f"# source-candidate suggestions (window: {args.window_days} d)")
    print(f"#  briefs walked:       {len(briefs)}")
    print(f"#  total inline links:  {total_links}")
    print(f"#  tracked hosts:       {len(source_hosts)} in sources.json")
    print(f"#  noise hosts skipped: {len(AGGREGATOR_HOSTS) + len(NEVER_PROMOTE_HOSTS)}")
    print(f"#  candidates shown:    top {len(top)} of {len(ranked)} missing-but-cited hosts")
    print()
    if not top:
        print("(no missing-but-cited hosts — every cited domain in window is in sources.json or noise list)")
        return 0
    width = max(len(h) for h, _ in top)
    for host, n in top:
        sb = ", ".join(samples[host])
        print(f"  {n:>3}× {host:<{width}}  [{sb}]")
    print()
    print("Operator review: pick 1–2 to add as `status: \"candidate\"` in sources.json")
    print("with a short `notes` line explaining what they cover. The brief routine")
    print("will promote them to `status: \"active\"` after 3 distinct runs that fetch")
    print("and contribute content from the new source (autonomous source lifecycle).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
