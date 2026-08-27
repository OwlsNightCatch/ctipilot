# runs/

One Markdown record per pipeline fire, at `runs/<YYYY-MM-DD>/<run-id>.md`
(`run_id = <YYYY-MM-DD>T<HHMM>Z-<intel|audit>` — multiple runs per day are
first-class; `-weekly` records are legacy history of the routine retired on
2026-08-27). Written by the run's final phase, immutable once the fire
completes (unlike entries, which are living records — a run record is
telemetry about one fire and has no current state to maintain) — the only sanctioned in-place updates are same-fire: the
same-minute retry and the Phase 7 publish-status amendment
(`publish_status` / `publish_checked_at` / `publish_note`, v3.14+; a record
still `pending` on main means the fire died before Phase 7 or its
amendment push failed).

Two halves (normative contract in [`docs/pipeline.md`](../docs/pipeline.md)):

- **Frontmatter = the machine-readable telemetry record** — models per role,
  timing, gap/window hours, per-sub-agent allocation, fetch failures,
  bridge uses, source-list changes, entities added, entry counts —
  `entries_published` (new entry files with this run_id) and
  `entries_updated` + `updated_entry_ids[]` (the existing entries this
  fire appended an `updates[]` changelog record to) — and the full
  verification-loop breakdown (per-iteration verdicts and findings).
  The Ops dashboard at `/ops/` is built entirely from these files.
- **Body = the verification & coverage notes** — the human-readable audit
  trail formerly in each brief's § 7: borderline drops with reasons,
  single-source items and carve-outs, reduced-confidence inclusions,
  contradictions, out-of-window drops, stalled sub-agents, and the
  parseable `Coverage gaps:` / `Watchlist:` / `Closed-source intake:` /
  `Essential-coverage:` lines the next run's preflight reads.

The rendered window brief (`/live/` and the per-day archive pages)
concatenates the bodies of every run in the window as its § Verification
Notes — so the reader always sees the caveats attached to exactly the
content in view.

Records migrated from the v2 `state/run_log.json` keep their historical
run ids as filenames; consumers treat `run_id` as an opaque sortable string.
