#!/usr/bin/env python3
"""Build the per-run dedup index from the entry store (v3).

Scans `entries/` for every entry whose folder date falls within the window
(including entries published by EARLIER RUNS TODAY — multiple fires per day
are first-class) and emits two artefacts under `work/<run-id>/`:

  prior_coverage.json        full records — research sub-agents Read this in
                             their isolated contexts for fetch-time dedup
  prior_coverage_keys.json   keys-only digest — the main agent Reads this
                             (no titles/headlines/URLs, minimal token cost)

Full record shape (one per entry):
  {id, kind, horizon, date, discovered_at, priority, title, headline,
   cves[], entities[], primary_source_url, update_of, deep_dive,
   deep_dive_category, weekly_section}

Keys record shape:
  {id, kind, date, discovered_at, priority, cves[], entities[],
   update_of, deep_dive, deep_dive_category}

Usage:
    python3 tools/build_prior_coverage.py <run-id> <window-days> \
        [--out-dir PATH] [--today YYYY-MM-DD]
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "site"))
import content_model as cm  # noqa: E402


def build_records(window_days: int, today: str) -> list:
    anchor = datetime.strptime(today, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    cutoff = (anchor - timedelta(days=window_days)).strftime("%Y-%m-%d")
    records = []
    for e in cm.collect_entries():
        if not (cutoff <= e.get("date", "") <= today):
            continue
        primary = None
        for s in e.get("sources") or []:
            if isinstance(s, dict) and s.get("url"):
                primary = s["url"]
                break
        records.append({
            "id": e["id"],
            "kind": e.get("kind"),
            "horizon": e.get("horizon"),
            "date": e.get("date"),
            "discovered_at": e.get("discovered_at"),
            "priority": e.get("priority"),
            "title": e.get("title"),
            "headline": e.get("headline"),
            "cves": [c.get("id") for c in (e.get("cves") or []) if isinstance(c, dict)],
            "entities": list(e.get("entities") or []),
            "primary_source_url": primary,
            "update_of": e.get("update_of"),
            "deep_dive": bool(e.get("deep_dive")),
            "deep_dive_category": e.get("deep_dive_category"),
            "weekly_section": e.get("weekly_section"),
        })
    records.sort(key=lambda r: (r["discovered_at"] or "", r["id"]))
    return records


_KEYS_FIELDS = ("id", "kind", "date", "discovered_at", "priority", "cves",
                "entities", "update_of", "deep_dive", "deep_dive_category")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("run_id")
    ap.add_argument("window_days", type=int)
    ap.add_argument("--out-dir", help="override work/<run-id>/")
    ap.add_argument("--today", help="override today's UTC date (testing)")
    args = ap.parse_args()

    today = args.today or datetime.now(timezone.utc).strftime("%Y-%m-%d")
    out_dir = Path(args.out_dir) if args.out_dir else ROOT / "work" / args.run_id
    out_dir.mkdir(parents=True, exist_ok=True)

    records = build_records(args.window_days, today)
    full = {
        "run_id": args.run_id,
        "window_days": args.window_days,
        "today": today,
        "record_count": len(records),
        "records": records,
    }
    keys = {
        "run_id": args.run_id,
        "window_days": args.window_days,
        "today": today,
        "record_count": len(records),
        "records": [{k: r[k] for k in _KEYS_FIELDS} for r in records],
    }
    p_full = out_dir / "prior_coverage.json"
    p_keys = out_dir / "prior_coverage_keys.json"
    p_full.write_text(json.dumps(full, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    p_keys.write_text(json.dumps(keys, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"prior_coverage: {len(records)} records "
          f"({p_full.stat().st_size} B full, {p_keys.stat().st_size} B keys) "
          f"window={args.window_days}d today={today}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
