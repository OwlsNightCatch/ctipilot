# runs/

One Markdown record per pipeline fire, at `runs/<YYYY-MM-DD>/<run-id>.md`
(`run_id = <YYYY-MM-DD>T<HHMM>Z-<intel|weekly>` — multiple runs per day are
first-class). Written by the run's final phase, immutable once committed.

Two halves (normative contract in [`docs/pipeline.md`](../docs/pipeline.md)):

- **Frontmatter = the machine-readable telemetry record** — models per role,
  timing, gap/window hours, per-sub-agent allocation, fetch failures,
  bridge uses, source-list changes, entities added, entry counts, and the
  full verification-loop breakdown (per-iteration verdicts and findings).
  The Ops dashboard at `/ops/` is built entirely from these files.
- **Body = the verification & coverage notes** — the human-readable audit
  trail formerly in each brief's § 7: borderline drops with reasons,
  single-source items and carve-outs, reduced-confidence inclusions,
  contradictions, out-of-window drops, stalled sub-agents, and the
  parseable `Coverage gaps:` / `Watchlist:` / `Closed-source intake:` /
  `Essential-coverage:` lines the next run's preflight reads.

The rendered window brief (`/brief/` and the per-day archive pages)
concatenates the bodies of every run in the window as its § Verification
Notes — so the reader always sees the caveats attached to exactly the
content in view.

Records migrated from the v2 `state/run_log.json` keep their historical
run ids as filenames; consumers treat `run_id` as an opaque sortable string.
