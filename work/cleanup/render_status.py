"""Render docs/cleanup/STATUS.md from work/cleanup/plan.json.

The plan is the single source: each cleanup session edits row statuses,
`next_wave`, `totals_now`, `waves` and `log` in plan.json, then runs

    python3 work/cleanup/render_status.py
    python3 work/cleanup/render_status.py --check-lanes   # parallel waves (v4.23)

so the tracker table and the plan never disagree. Two totals are read from
disk at render time (entries in the store, legacy queue pending), so parallel
waves never leave them stale.

Waves run in parallel lanes (prompts/cleanup-coordinator.md, v4.23). A wave's
`status` is `planned`, `ready`, `in-flight <run-id>` or `done <run-id>: ...`,
and `after` lists the waves that must be done first. `--check-lanes` exits 1
when two waves that are ready or in flight share an entry (through their
rows' `entries`), or when a ready or in-flight wave waits on a wave that is
not done. Stdlib only.
"""
from __future__ import annotations

import itertools
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PLAN = ROOT / "work/cleanup/plan.json"
OUT = ROOT / "docs/cleanup/STATUS.md"

DONE = """1. Every published entry truth-verified under the current standard since its last substantive change: legacy queue empty (`python3 tools/legacy_review.py --stats` 0 pending) and no entry left that no audit truth pass covered.
2. Every known finding applied or declined with a reason: the 2026-10-18 out-of-week verdicts, carried residuals and `(pre-existing)` advisories, portable reference-branch hunks.
3. No duplicate findings: each pair folded with `tools/fold_entries.py` or linked through `references[]`.
4. Registry clean: duplicate orphans tombstoned, no relation with a missing source entry, the known summaries fixed.
5. Sources and state current: 2026-10-11 recommendations 5 to 7 decided, no dead acknowledgment row, backlog holds only live rows.
6. No dead weight: unused tools, stale docs, retired code paths, stale `work/` material removed; gate false positives fixed.
7. Program retired (§ C9)."""


def cell(text) -> str:
    return str(text if text is not None else "").replace("|", "\\|").replace("\n", " ")


def derived_totals() -> dict[str, object]:
    """Totals read from disk, so no wave has to remember to update them."""
    out: dict[str, object] = {}
    entries = ROOT / "entries"
    if entries.is_dir():
        out["Entries in the store"] = sum(1 for _ in entries.glob("*/*.md"))
    legacy = ROOT / "state/legacy_review.json"
    if legacy.is_file():
        rows = json.loads(legacy.read_text()).get("entries") or {}
        out["Legacy queue pending"] = sum(1 for v in rows.values() if v.get("status") == "pending")
    return out


def _word(status) -> str:
    return str(status or "").split(" ")[0].rstrip(":").lower()


def check_lanes(plan: dict) -> int:
    """Waves that are ready or in flight must be disjoint and unblocked."""
    rows_by_wave: dict[str, list] = {}
    for r in plan["rows"]:
        rows_by_wave.setdefault(str(r.get("wave")), []).append(r)
    waves = {str(w["wave"]): w for w in plan["waves"]}
    live = [k for k, w in waves.items() if _word(w.get("status")) in ("ready", "in-flight")]
    problems = []
    scope = {}
    for k in live:
        ents = set()
        for r in rows_by_wave.get(k, []):
            if _word(r.get("status")) not in ("done", "declined"):
                ents.update(r.get("entries") or [])
        scope[k] = ents
        for dep in waves[k].get("after") or []:
            if _word(waves.get(str(dep), {}).get("status")) != "done":
                problems.append(f"wave {k} waits on wave {dep}, which is not done")
    for a, b in itertools.combinations(live, 2):
        shared = scope[a] & scope[b]
        if shared:
            problems.append(f"waves {a} and {b} share {len(shared)} entries, e.g. {sorted(shared)[0]}")
    for k in live:
        print(f"wave {k}: {_word(waves[k].get('status'))}, {len(scope[k])} entries")
    for p in problems:
        print(f"LANE CONFLICT: {p}")
    if not problems:
        print(f"lanes ok: {len(live)} waves ready or in flight, pairwise disjoint")
    return 1 if problems else 0


def main() -> int:
    plan = json.loads(PLAN.read_text())
    if "--check-lanes" in sys.argv[1:]:
        return check_lanes(plan)
    derived = derived_totals()
    rows = plan["rows"]
    lines = [
        "# Store cleanup tracker",
        "",
        "Program: [`prompts/cleanup-coordinator.md`](../../prompts/cleanup-coordinator.md). "
        "Machine-readable plan with every row's entry ids: [`work/cleanup/plan.json`](../../work/cleanup/plan.json); "
        "this file is rendered from it (`python3 work/cleanup/render_status.py`). Inventory: `python3 work/cleanup/inventory.py`. "
        "Each cleanup session takes the next wave, updates the rows it touched in plan.json, re-renders, and names the next wave below.",
        "",
        f"**Next wave:** {plan['next_wave']}",
        "",
        "## Definition of done (§ Mandate)",
        "",
        DONE,
        "",
        "After every wave: `python3 tools/check_run.py --all` ends `0 warn · 0 fail`, `python3 site/build.py` is warning-free.",
        "",
        f"## Totals (baseline {plan['created']})",
        "",
        "| Measure | Baseline | Now |",
        "|---|---|---|",
    ]
    for m in plan["totals"]:
        now = derived.get(m["measure"], m["now"])
        lines.append(f"| {cell(m['measure'])} | {cell(m['baseline'])} | {cell(now)} |")
    counts: dict[str, int] = {}
    for r in rows:
        key = r["status"].split(" ")[0].rstrip(":")
        counts[key] = counts.get(key, 0) + 1
    lines.append("| Rows done / declined / in a wave / open | "
                 f"{len(rows)} rows | {counts.get('done', 0)} / {counts.get('declined', 0)} / "
                 f"{counts.get('in-wave', 0)} / {counts.get('open', 0)} |")
    lines += ["", "## Waves", "",
              "Waves marked `ready` can start now, each in its own session and in parallel; "
              "`after` names the waves that must be done first "
              "(`python3 work/cleanup/render_status.py --check-lanes` proves the ready and "
              "in-flight waves share no entry).", "",
              "| Wave | Lane | Rows | After | Status |", "|---|---|---|---|---|"]
    for w in plan["waves"]:
        after = ", ".join(str(x) for x in (w.get("after") or [])) or "-"
        lines.append(f"| {cell(w['wave'])} | {cell(w.get('lane') or '-')} | {cell(w['rows'])} | "
                     f"{cell(after)} | {cell(w['status'])} |")
    lines += ["", "W5, W6 and W7 rows marked `standalone` ship as small merges of their own between "
              "waves, the moment they are green. Inputs prepared for a wave live under "
              "`work/cleanup/wave-<NN>/`.", "", "## Rows", "",
              "| Row | WS | Item | Size | Wave | Status |", "|---|---|---|---|---|---|"]
    for r in rows:
        lines.append(f"| {r['id']} | {r['workstream']} | {cell(r['item'])} | {cell(r['size'])} | "
                     f"{cell(r['wave'])} | {cell(r['status'])} |")
    lines += ["", "## Log", ""] + [f"- {cell(x)}" for x in plan.get("log", [])]
    OUT.write_text("\n".join(lines) + "\n")
    print(f"wrote {OUT.relative_to(ROOT)}: {len(rows)} rows, {counts}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
