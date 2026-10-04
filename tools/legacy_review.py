#!/usr/bin/env python3
"""Legacy re-verification queue: the v2-brief entries no audit has checked (v4.19).

Why this exists. 478 of the store's 966 entries (May to July 2026) were
migrated from the v2 daily briefs by tools/migrate_briefs.py, before claim
verification, inline citations and the entry lifecycle existed. The weekly
quality audit re-verifies only its trailing window, so before 2026-09-30 only 3
of those entries had ever received a record from an audit. When the 2026-09-30 audit
did look, it found claims no source makes: a state attribution a national
authority never published (ABW water plants), victims attributed to the wrong
exploitation wave and five CVEs marked exploited where the vendor reported one
(Ivanti EPMM), invented kernel package versions, a regulator review that never
opened (Eurail), statistics absent from the cited report (Dragos), plus 24
legacy "UPDATE" entries that were never folded into the finding they update.

The queue makes the backlog finite and visible. Each audit takes the next
batch (oldest first), re-verifies every entry against fetched primaries,
fixes what is wrong through the entry's changelog (a correction, or a fold of
a duplicate with tools/fold_entries.py), and marks the batch done.

    python3 tools/legacy_review.py --init            # (re)build the queue from the store, keeping statuses
    python3 tools/legacy_review.py --next 20         # the next pending batch, oldest first
    python3 tools/legacy_review.py --done <run-id> <entry-id> [...]   # mark reviewed
    python3 tools/legacy_review.py --stats           # pending / reviewed counts

State: state/legacy_review.json, {"entries": {id: {"status": "pending"|"reviewed"|"folded",
"run_id": …}}}. An entry that no longer exists (folded into its survivor) is
marked "folded" by --init. Stdlib only.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "site"))
import content_model as cm  # noqa: E402

STATE = ROOT / "state" / "legacy_review.json"


def _load() -> dict:
    if STATE.is_file():
        return json.loads(STATE.read_text(encoding="utf-8"))
    return {"schema": 1, "description": "", "entries": {}}


def _save(d: dict) -> None:
    d["entries"] = dict(sorted(d["entries"].items()))
    STATE.write_text(json.dumps(d, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")


def _legacy_ids() -> tuple[set[str], dict[str, set[str]]]:
    ids: set[str] = set()
    audited: dict[str, set[str]] = {}
    for e in cm.collect_entries():
        if str(e.get("migrated_from") or "").startswith("briefs/"):
            ids.add(e["id"])
            audited[e["id"]] = {str(r.get("run_id")) for r in (e.get("updates") or [])
                                if isinstance(r, dict) and "audit" in str(r.get("run_id") or "")}
    return ids, audited


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--init", action="store_true")
    g.add_argument("--next", type=int, metavar="N")
    g.add_argument("--done", nargs="+", metavar="RUN_ID ENTRY_ID")
    g.add_argument("--stats", action="store_true")
    a = ap.parse_args(argv)
    d = _load()
    d["description"] = ("Re-verification queue for entries migrated from the v2 daily briefs "
                        "(tools/legacy_review.py; prompts/quality-audit.md Phase 1).")
    if a.init:
        ids, audited = _legacy_ids()
        for eid in ids:
            d["entries"].setdefault(eid, {"status": "pending", "run_id": None})
        for eid, rec in d["entries"].items():
            if eid not in ids and rec.get("status") == "pending":
                rec["status"] = "folded"
        _save(d)
    elif a.next:
        ids, _ = _legacy_ids()
        pending = sorted(eid for eid, r in d["entries"].items() if r.get("status") == "pending" and eid in ids)
        for eid in pending[:a.next]:
            print(eid)
        return 0
    elif a.done:
        run_id, *eids = a.done
        for eid in eids:
            d["entries"][eid] = {"status": "reviewed", "run_id": run_id}
        _save(d)
    counts: dict[str, int] = {}
    for r in d["entries"].values():
        counts[r.get("status") or "?"] = counts.get(r.get("status") or "?", 0) + 1
    print("legacy review:", ", ".join(f"{k} {v}" for k, v in sorted(counts.items())))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
