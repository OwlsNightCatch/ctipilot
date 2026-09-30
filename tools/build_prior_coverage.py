#!/usr/bin/env python3
"""Build the per-run dedup index from the entry store (v3).

Scans `entries/` for every entry whose ACTIVITY falls within the window —
folder date (first publication) OR the date of its latest `updates[]`
changelog record (v4.0: one living entry per finding; an entry first
published 40 days ago but updated 3 days ago is in-window coverage) —
including entries published or updated by EARLIER RUNS TODAY (multiple fires
per day are first-class) and emits two artefacts under `work/<run-id>/`:

  prior_coverage.json        full records — the main agent AND the research
                             sub-agents Read this. The main agent loads every
                             in-window brief (title/headline/summary + keys)
                             into context for content-level compose-time dedup
                             (v3.1: 14-day window); sub-agents Read it in their
                             isolated contexts for fetch-time dedup.
  prior_coverage_keys.json   keys-only digest — the lean metadata index
                             (no titles/headlines/summaries/URLs)

The full record carries `summary` — the entry's own TL;DR — so that reading
prior_coverage.json is equivalent to loading every brief in the window; that
is what makes the main agent's in-context dedup a content check, not just a
key match. Coverage OUTSIDE this window is caught by the store-wide metadata
check (state/cves_seen.json + the mechanical gate), not by this file.

Full record shape (one per entry):
  {id, kind, date, discovered_at, updated_at, last_changed_at, update_count,
   last_update: {at, type, summary} | null,
   last_development: {at, summary} | null  (last non-internal `update`),
   priority, title, headline,
   summary, cves[], entities[], actions[], primary_source_url, deep_dive,
   deep_dive_category}

Plus one top-level list the window cannot carry by itself:
  deep_dive_history          every `deep_dive: true` entry of the last 30
                             days as {id, date, deep_dive_category} — the
                             Phase 3 category-rotation input, which reaches
                             further back than the dedup window.

`actions` is the entry's CURRENT do-now list, so the composer can see that an
in-window entry already carries an action before it writes the same one again
(the rendered brief's action list is a union).

A candidate matching a record's CVEs or entity keys is never a new entry —
it is an `updates[]` record appended to that entry (or nothing when there is
no material delta); `last_update` tells the composer what the entry already
says about the latest development.

Keys record shape:
  {id, kind, date, discovered_at, updated_at, update_count, priority,
   cves[], entities[], deep_dive, deep_dive_category}

Usage:
    python3 tools/build_prior_coverage.py <run-id> <window-days> \
        [--out-dir PATH] [--today YYYY-MM-DD]
"""

from __future__ import annotations

import argparse
import json
import re
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
        activity = (cm.entry_activity_ts(e) or "")[:10] or e.get("date", "")
        if not (cutoff <= e.get("date", "") <= today) and not (cutoff <= activity <= today):
            continue
        updates = [u for u in (e.get("updates") or []) if isinstance(u, dict)]
        last = updates[-1] if updates else None
        # The last material development (non-internal `update`): what the story
        # last did in the world, as opposed to the last bookkeeping fix.
        devs = [u for u in updates if u.get("type") == "update" and not u.get("internal")]
        last_dev = devs[-1] if devs else None
        visible = [u for u in updates if not u.get("internal")]
        last_changed = max([e.get("discovered_at") or ""] + [str(u.get("at") or "") for u in visible])
        primary = None
        for s in e.get("sources") or []:
            if isinstance(s, dict) and s.get("url"):
                primary = s["url"]
                break
        records.append({
            "id": e["id"],
            "kind": e.get("kind"),
            "date": e.get("date"),
            "discovered_at": e.get("discovered_at"),
            "updated_at": e.get("updated_at"),
            "update_count": len(updates),
            "last_update": (
                {"at": last.get("at"), "type": last.get("type"),
                 "summary": last.get("summary")} if last else None
            ),
            "last_development": (
                {"at": last_dev.get("at"), "summary": last_dev.get("summary")}
                if last_dev else None
            ),
            "last_changed_at": last_changed,
            "priority": e.get("priority"),
            "title": e.get("title"),
            "headline": e.get("headline"),
            "summary": e.get("summary"),
            "cves": [c.get("id") for c in (e.get("cves") or []) if isinstance(c, dict)],
            "entities": list(e.get("entities") or []),
            "actions": [a for a in (e.get("actions") or []) if isinstance(a, str)],
            "primary_source_url": primary,
            "deep_dive": bool(e.get("deep_dive")),
            "deep_dive_category": e.get("deep_dive_category"),
        })
    # Newest activity FIRST: the file is larger than one Read, and a truncated
    # read must lose the oldest coverage, never today's earlier runs (the most
    # likely duplicates).
    records.sort(key=lambda r: (r["last_changed_at"] or "", r["id"]), reverse=True)
    return records


def build_deep_dive_history(today: str, days: int = 30) -> list:
    anchor = datetime.strptime(today, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    cutoff = (anchor - timedelta(days=days)).strftime("%Y-%m-%d")
    out = [
        {"id": e["id"], "date": e.get("date"), "deep_dive_category": e.get("deep_dive_category")}
        for e in cm.collect_entries()
        if e.get("deep_dive") and cutoff <= (e.get("date") or "") <= today
    ]
    out.sort(key=lambda r: (r["date"] or "", r["id"]))
    return out


_KEYS_FIELDS = ("id", "kind", "date", "discovered_at", "updated_at", "last_changed_at",
                "update_count", "priority", "cves", "entities", "deep_dive",
                "deep_dive_category")


def _dump_lines(doc: dict) -> str:
    """JSON with one record per line (valid JSON, compact, chunk-readable)."""
    head = {k: v for k, v in doc.items() if k not in ("records", "deep_dive_history")}
    out = ["{"]
    for k, v in head.items():
        out.append(f" {json.dumps(k)}: {json.dumps(v, ensure_ascii=False)},")
    for key in ("deep_dive_history", "records"):
        if key not in doc:
            continue
        items = doc[key]
        out.append(f" {json.dumps(key)}: [")
        for i, r in enumerate(items):
            out.append("  " + json.dumps(r, ensure_ascii=False, separators=(",", ":"))
                       + ("," if i < len(items) - 1 else ""))
        out.append(" ],")
    out[-1] = out[-1].rstrip(",")
    out.append("}")
    return "\n".join(out) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("run_id")
    ap.add_argument("window_days", type=int)
    ap.add_argument("--out-dir", help="override work/<run-id>/")
    ap.add_argument("--today", help="override today's UTC date (testing)")
    args = ap.parse_args()

    # The run id carries the Phase 0 network-verified date; the container clock
    # has been days wrong before (2026-08-24), and a wrong "today" silently
    # drops the newest coverage from the dedup index.
    m = re.match(r"^(\d{4}-\d{2}-\d{2})T\d{4}Z-", args.run_id)
    today = args.today or (m.group(1) if m else datetime.now(timezone.utc).strftime("%Y-%m-%d"))
    out_dir = Path(args.out_dir) if args.out_dir else ROOT / "work" / args.run_id
    out_dir.mkdir(parents=True, exist_ok=True)

    records = build_records(args.window_days, today)
    full = {
        "run_id": args.run_id,
        "window_days": args.window_days,
        "today": today,
        "record_count": len(records),
        "records": records,
        "deep_dive_history": build_deep_dive_history(today),
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
    # One record per line, no indentation: the reader pays tokens for text,
    # not whitespace, and a line-oriented file can be read in offset chunks.
    p_full.write_text(_dump_lines(full), encoding="utf-8")
    p_keys.write_text(_dump_lines(keys), encoding="utf-8")
    est = p_full.stat().st_size // 4
    print(f"prior_coverage: {len(records)} records "
          f"({p_full.stat().st_size} B full ≈ {est} tokens, {p_keys.stat().st_size} B keys) "
          f"window={args.window_days}d today={today} — newest activity first; if one Read "
          f"truncates, continue with offset until the last line")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
