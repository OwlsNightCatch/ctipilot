#!/usr/bin/env python3
"""Emit a compact dedup summary of state files for the routine main agent.

The full state files (`state/covered_items.json`, `state/cves_seen.json`,
`state/run_log.json`, `sources/sources.json`) collectively run >300 KB
on a mature repo and consume tens of thousands of tokens just to load.
The main agent only needs the *keys* for dedup decisions plus a few
recent records — not the full structured data.

This script emits a single JSON to stdout (or a file) that the main
agent can `Read` instead of loading the four full state files. Sub-agents
that need the full files still `Read` them directly.

Schema:
    {
      "today": "2026-05-11",
      "cves": {                               # from cves_seen.json
        "count": 184,
        "ids": ["CVE-2026-0300", ...],        # all ids
        "recent": [                            # last_seen within last N days
          {"id": "...", "first_seen": "...", "last_seen": "...", "title": "..."}
        ]
      },
      "items": {                              # from covered_items.json
        "count": 89,
        "keys": ["actor:Akira", ...],         # all keys (small)
        "recent": [                            # last_covered within last N days
          {"key": "...", "type": "...", "title": "...", "last_covered": "...",
           "primary_source_url": "..."}
        ]
      },
      "sources": {                            # from sources/sources.json
        "active_count": 78,
        "active_ids": ["ncsc-ch-security-hub", ...],
        "demoted_ids": ["..."],
        "candidate_ids": ["..."]
      },
      "runs": {                               # from run_log.json
        "count": 35,
        "last_run": {"run_id": "...", "date": "...", "kind": "..."},
        "fetch_gaps_in_window": [             # source-ids hit by 2+ runs
          {"id": "...", "runs_failing": 3, "last_status": 403}
        ]
      }
    }

Token cost: typical mature repo ~5–10 KB / ~1.5–3K tokens, vs ~120 KB /
~30K tokens for the four full files.

Usage:
    python3 tools/run_summary.py [--out PATH] [--recent-days N] [--gap-runs N]
    python3 tools/run_summary.py --out work/<run-id>/state-summary.json

Exit 0 on success; 1 on missing/malformed state file.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from datetime import date, datetime, timedelta
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

STATE_FILES = {
    "covered_items": REPO_ROOT / "state" / "covered_items.json",
    "cves_seen": REPO_ROOT / "state" / "cves_seen.json",
    "run_log": REPO_ROOT / "state" / "run_log.json",
    "sources": REPO_ROOT / "sources" / "sources.json",
}


def _load(path: Path) -> dict:
    if not path.exists():
        print(f"warn: {path.relative_to(REPO_ROOT)} missing — skipped", file=sys.stderr)
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"error: {path.relative_to(REPO_ROOT)} parse failure: {e}", file=sys.stderr)
        sys.exit(1)


def _parse_date(s: str | None) -> date | None:
    if not s:
        return None
    try:
        return datetime.strptime(s, "%Y-%m-%d").date()
    except ValueError:
        return None


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", help="Output path (default: stdout)")
    ap.add_argument("--recent-days", type=int, default=14,
                    help="Records 'recent' if last_seen/last_covered within N days (default 14)")
    ap.add_argument("--gap-runs", type=int, default=2,
                    help="Source flagged 'gap' if it failed in ≥ N recent runs (default 2)")
    ap.add_argument("--gap-window", type=int, default=7,
                    help="How many recent runs to scan for gap detection (default 7)")
    ap.add_argument("--today", help="Override today's date YYYY-MM-DD (testing)")
    args = ap.parse_args(argv)

    today = (
        datetime.strptime(args.today, "%Y-%m-%d").date() if args.today else date.today()
    )
    cutoff = today - timedelta(days=args.recent_days)

    out: dict = {"today": today.isoformat()}

    # ─── cves_seen.json ──────────────────────────────────────────────
    cves_data = _load(STATE_FILES["cves_seen"])
    cves = cves_data.get("cves", []) if isinstance(cves_data, dict) else []
    out["cves"] = {
        "count": len(cves),
        "ids": [c["id"] for c in cves if "id" in c],
        "recent": [
            {
                "id": c.get("id"),
                "last_seen": c.get("last_seen"),
                "title": (c.get("title") or "")[:100],
            }
            for c in cves
            if (d := _parse_date(c.get("last_seen"))) and d >= cutoff
        ],
    }

    # ─── covered_items.json ──────────────────────────────────────────
    ci_data = _load(STATE_FILES["covered_items"])
    items = ci_data.get("items", []) if isinstance(ci_data, dict) else []
    out["items"] = {
        "count": len(items),
        "keys": [i["key"] for i in items if "key" in i],
        "recent": [
            {
                "key": i.get("key"),
                "type": i.get("type"),
                "title": (i.get("title") or "")[:100],
                "last_covered": i.get("last_covered"),
            }
            for i in items
            if (d := _parse_date(i.get("last_covered"))) and d >= cutoff
        ],
    }

    # ─── sources/sources.json ────────────────────────────────────────
    src_data = _load(STATE_FILES["sources"])
    src_list = src_data.get("sources", []) if isinstance(src_data, dict) else []
    by_status: dict[str, list[str]] = {}
    for s in src_list:
        sid, status = s.get("id"), s.get("status", "unknown")
        if sid:
            by_status.setdefault(status, []).append(sid)
    out["sources"] = {
        "active_count": len(by_status.get("active", [])),
        "active_ids": sorted(by_status.get("active", [])),
        "demoted_ids": sorted(by_status.get("demoted", [])),
        "candidate_ids": sorted(by_status.get("candidate", [])),
    }

    # ─── run_log.json ────────────────────────────────────────────────
    rl_data = _load(STATE_FILES["run_log"])
    runs = rl_data.get("runs", []) if isinstance(rl_data, dict) else []
    out["runs"] = {"count": len(runs)}
    if runs:
        last = runs[-1]
        out["runs"]["last_run"] = {
            "run_id": last.get("run_id"),
            "date": last.get("date"),
            "iso_week": last.get("iso_week"),
            "kind": last.get("kind", "daily"),
            "model": last.get("model"),
        }
        # Gap detection: scan the last `gap_window` runs for repeated
        # fetch_failures on the same source id.
        gap_counter: Counter[str] = Counter()
        last_status: dict[str, int | str] = {}
        for r in runs[-args.gap_window:]:
            for ff in r.get("fetch_failures") or []:
                sid = ff.get("id")
                if not sid:
                    continue
                gap_counter[sid] += 1
                last_status[sid] = ff.get("status_code") or ff.get("status") or "?"
        out["runs"]["fetch_gaps_in_window"] = sorted(
            (
                {"id": sid, "runs_failing": n, "last_status": last_status.get(sid, "?")}
                for sid, n in gap_counter.items()
                if n >= args.gap_runs
            ),
            key=lambda x: (-x["runs_failing"], x["id"]),
        )

    payload = json.dumps(out, indent=2, ensure_ascii=False)
    if args.out:
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(payload + "\n", encoding="utf-8")
        cves_n = out["cves"]["count"]
        items_n = out["items"]["count"]
        print(
            f"state-summary: path={out_path} bytes={len(payload)+1} "
            f"cves={cves_n} items={items_n} "
            f"sources_active={out['sources']['active_count']} runs={out['runs']['count']}"
        )
    else:
        sys.stdout.write(payload + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
