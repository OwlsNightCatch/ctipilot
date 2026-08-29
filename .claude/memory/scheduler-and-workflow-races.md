---
name: Scheduler outages & workflow races
description: Cadence is operator-owned; overtaken-run recovery procedure; auto-merge conflict paths; run-clock history caveat
type: project
---

# Scheduler outages & workflow races (condensed 2026-08-28)

## Cadence and gaps

- **Cadence is operator-owned and variable at will** (2026-07-18): work off the gap to the last run; a changed cadence is never a finding. Only a *record-less* gap on a schedule that should have fired is an availability signal (2026-07-07: confirmed 62 h scheduler outage; missing `runs/<date>/` + clean previous fire = scheduler-side; the gap-derived window self-heals coverage — surface big gaps, don't re-diagnose the repo).
- Runaway/stalled runs are container-side (worst: 53 h). The ~3 h main-run watchdog stands: past it, land the run — no new research.

## Two local sessions, one working tree (2026-08-29)

Interactive sessions on this repo can run CONCURRENTLY IN THE SAME WORKING TREE (`ListAgents` shows the peers). During the legacy-strategic purge a peer session saw the store drop 1222 -> 829 files mid-build, read it as filesystem corruption, and ran `git checkout HEAD -- entries/ entities/registry.yaml`, which discarded a staged 393-file deletion and every unstaged edit under those paths in one shot.

- **Commit destructive work the moment it is coherent.** A commit is the only thing a peer's `git checkout` cannot undo; a staged deletion is not safe.
- Before restoring anything that looks like corruption, run `git status` and look for staged deletions — another session may be mid-task.
- `ListAgents` + `SendMessage` to the peer name is the coordination channel; agree on path ownership up front (they kept `site/build.py`+assets, I took `entries/`, `entities/`, `state/`, `tools/`).
- Untracked conflict copies (`site/build 2.py`, `styles 2.css`) live in this tree and make a healthy repo look corrupted. They are noise, not signal.

## Overtaken-run recovery (worst case 2026-08-22: 3 fires past, 8 of 16 entries stood down)

- An overtaking fire's window is gap-to-last-**published**-run, so it swallows yours whole. Check `origin/main` at every phase boundary, not only Phase 6.
- Dedup by **reading**, not by index: two of the eight duplicates had no CVE and no shared entity key.
- Resolve the merge by taking `main`'s shared state and re-applying only your genuinely-new records — `--ours` on registry/`cves_seen`/source_health discards other fires' work (union-merge `cves_seen.json` keyed on `id`). Check your *tooling* diffs the same way: a local fix may be a rediscovery of a better one already on `main`.
- A still-valuable duplicate survives as a changelog record appended to the overtaking entry; its `at` must be later than that entry's last activity. **The audit fire appends records too** — re-read the target entry on `origin/main` for a newer record before appending yours (one record per fire; `at` strictly increasing; a second correction of the same defect is no record at all). A dropped entry's non-actionable extra fact goes to a correction-owed row in `state/coverage_backlog.md`.

## Auto-merge conflicts

- **`state/coverage_backlog.md` ALWAYS conflicts on interleaved pushes** — it is outside the workflow's four auto-resolution paths (`cves_seen`/`source_health` →ours, registry →ours, sources.json →theirs) and every fire touches it. Resolve locally: union both sides' rows, published rows move to `## Struck`, push clean. Same row can appear twice after the merge (conflict hunk + common context) — diff the row sets via `git show :1:/:2:/:3:`.
- compose-profile × auto-merge branch-delete race: compose falls back to checking `main` when the branch is gone (fixed 2026-07-09).

## Reading history

- **Pre-v3.33 `duration_seconds`/`completed` is a FLOOR** — stamped in Phase 5 before the verifier loop (worst skew 125 min); v3.33 re-stamps in Phase 6 and `check_run.py` gates it (`run-clock`). A verifier finding repaired only in the record it was found in is a fix that did not ship — if the finding names a mechanism, the mechanism is the work item.
