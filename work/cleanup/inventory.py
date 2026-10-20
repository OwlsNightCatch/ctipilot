"""Store cleanup inventory (prompts/cleanup-coordinator.md § C0 step 2).

Re-runnable by any cleanup session (needs PyYAML): prints the workstream sizes and writes
work/cleanup/inventory.json (W1 to W4 rows; W5 to W7 are sized by hand in the
tracker). Reads the working tree.

    python3 work/cleanup/inventory.py
"""
from __future__ import annotations
import itertools, json, re, sys
import yaml  # truth YAMLs use full YAML, not the frontmatter subset
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "site"))
import content_model as cm  # noqa: E402

AUDIT = "2026-10-18T1307Z-audit"
LAST_FULL_AUDIT = "2026-10-18T13:07"  # move to the newest full audit's `started` when re-running
OUT_OF_WEEK_PASSES = ["T1", "T2", "T4", "T5", "T6a", "T7", "T8a", "T8b", "T9", "D1", "D2", "D3", "L"]


def primary_scope() -> set:
    """The 2026-10-18 audit's own week (21 new + 9 intel-updated entries)."""
    split = json.loads((ROOT / f"work/{AUDIT}/window-split.json").read_text())
    return set(split["new"]) | set(split["intel_updated"])


def main() -> int:
    entries = {e["id"]: e for e in cm.collect_entries()}
    # Folded ids resolve to their survivor.
    folded = {}
    for e in entries.values():
        for u in e.get("updates") or []:
            for mid in cm.merged_ids(u):
                folded[mid] = e["id"]
    legacy = json.loads((ROOT / "state/legacy_review.json").read_text())["entries"]
    pending = {k for k, v in legacy.items() if v.get("status") == "pending"}

    # --- W1: out-of-week verdicts of the 2026-10-18 audit ---------------------
    w1, scope = [], primary_scope()
    for p in OUT_OF_WEEK_PASSES:
        doc = yaml.safe_load((ROOT / f"work/{AUDIT}/truth-{p}.yaml").read_text())
        for row in doc.get("entries") or []:
            eid = row.get("entry")
            e = entries.get(eid)
            if eid in scope:
                continue  # the 10-18 audit's own scope, fixed there
            later = [u for u in (e or {}).get("updates") or [] if str(u.get("at")) > "2026-10-18T13:07"]
            w1.append({
                "pass": p, "entry": eid, "verdict": row.get("verdict"),
                "defects": len(row.get("defects") or []),
                "exists": e is not None, "folded_into": folded.get(eid),
                "legacy_pending": eid in pending,
                "records_since": [f"{u.get('run_id')}:{u.get('type')}" for u in later],
            })
    # --- verified set (W3) -----------------------------------------------------
    named = set()
    for f in [*ROOT.glob("work/*-audit/truth-*.yaml"), *ROOT.glob("work/*-audit/truth-*.md")]:
        named |= set(re.findall(r"20\d\d-\d\d-\d\d/[a-z0-9-]+", f.read_text(errors="ignore")))
    for f in ROOT.glob("work/*-audit/audit-plan.json"):
        named |= set(re.findall(r"20\d\d-\d\d-\d\d/[a-z0-9-]+", f.read_text(errors="ignore")))
    for f in ROOT.glob("runs/*/*-audit.md"):
        try:
            r = cm.load_run_record(f)
        except Exception:
            continue
        named |= set(r.get("updated_entry_ids") or [])
    # Entries published after the first scheduled audit with truth passes are
    # in some audit's window by construction only if named; keep it literal.
    # Excluded: entries an audit published (its own closing loop verified them)
    # and entries newer than the last full audit (the next scheduled audit's window).
    audit_new = {i for i, e in entries.items() if str(e.get("run_id", "")).endswith("-audit")}
    w3 = sorted(i for i, e in entries.items()
                if i not in named and i not in pending and i not in audit_new
                and str(e.get("discovered_at")) < LAST_FULL_AUDIT)
    # --- W4: CVE-sharing pairs without a link either way -----------------------
    by_cve = defaultdict(set)
    for e in entries.values():
        for c in e.get("cves") or []:
            cid = c.get("id") if isinstance(c, dict) else c
            if cid:
                by_cve[cid].add(e["id"])
    pairs = set()
    for cid, ids in by_cve.items():
        for a, b in itertools.combinations(sorted(ids), 2):
            ra = set(entries[a].get("references") or [])
            rb = set(entries[b].get("references") or [])
            if b in ra or a in rb:
                continue
            pairs.add((a, b))
    shared = defaultdict(list)
    for cid, ids in by_cve.items():
        for a, b in itertools.combinations(sorted(ids), 2):
            if (a, b) in pairs:
                shared[(a, b)].append(cid)
    dup_groups = json.loads((ROOT / f"work/{AUDIT}/dup-groups.json").read_text())
    dg = []
    for g in dup_groups:
        live = [i for i in g if i in entries]
        dg.append({"group": g, "live": live, "folded": {i: folded.get(i) for i in g if i not in entries}})
    out = {
        "entries_total": len(entries),
        "legacy_pending": len(pending),
        "w1": w1,
        "w3_never_verified": w3,
        "w4_cve_pairs_unlinked": [{"a": a, "b": b, "cves": shared[(a, b)]} for a, b in sorted(pairs)],
        "w4_dup_groups_1018": dg,
    }
    (ROOT / "work/cleanup/inventory.json").write_text(json.dumps(out, indent=1) + "\n")
    from collections import Counter
    v = Counter(r["verdict"] for r in w1)
    print("entries", len(entries), "legacy pending", len(pending))
    print("W1 rows", len(w1), dict(v), "missing", sum(not r["exists"] for r in w1),
          "legacy", sum(r["legacy_pending"] for r in w1))
    print("W3 never verified (non-legacy)", len(w3))
    print("W4 unlinked CVE pairs", len(pairs), "dup groups", len(dg),
          "groups still >1 live", sum(len(g["live"]) > 1 for g in dg))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
