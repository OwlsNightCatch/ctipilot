"""Render docs/cleanup/STATUS.md from work/cleanup/plan.json.

The plan is the single source: each cleanup session edits row statuses,
`next_wave`, `totals_now`, `waves` and `log` in plan.json, then runs

    python3 work/cleanup/render_status.py

so the tracker table and the plan never disagree. Stdlib only.
"""
from __future__ import annotations

import json
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


def main() -> int:
    plan = json.loads(PLAN.read_text())
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
        lines.append(f"| {cell(m['measure'])} | {cell(m['baseline'])} | {cell(m['now'])} |")
    counts: dict[str, int] = {}
    for r in rows:
        key = r["status"].split(" ")[0].rstrip(":")
        counts[key] = counts.get(key, 0) + 1
    lines.append("| Rows done / declined / in a wave / open | "
                 f"{len(rows)} rows | {counts.get('done', 0)} / {counts.get('declined', 0)} / "
                 f"{counts.get('in-wave', 0)} / {counts.get('open', 0)} |")
    lines += ["", "## Waves", "", "| Wave | Rows | Status |", "|---|---|---|"]
    for w in plan["waves"]:
        lines.append(f"| {cell(w['wave'])} | {cell(w['rows'])} | {cell(w['status'])} |")
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
