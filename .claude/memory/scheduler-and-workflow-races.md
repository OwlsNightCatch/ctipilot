---
name: Scheduler outages & workflow races
description: Confirmed scheduler outages and CI workflow race conditions, with their diagnoses and fixes
type: project
---

# Scheduler outages & workflow races

## 2026-07-07 scheduler outage (operator-confirmed)

No fires at all on 2026-07-07 and none until 2026-07-08T2009Z — a ~62 h gap, the largest in the corpus. **The operator confirmed (2026-07-09) this was a real scheduler outage**, not a repo/prompt failure. The pipeline behaved as designed: the 07-08 fire computed `gap_hours: 62`, widened to a catch-up window, and published 11 entries with first-coverage flags. Diagnosis rule for future gaps: a missing `runs/<date>/` directory with a clean previous fire = scheduler-side; the prompt's gap-derived window (PD-7) self-heals coverage, but latency is lost — surface big gaps to the operator, don't re-diagnose the repo.

## compose-profile.yml × auto-merge-claude.yml race (fixed 2026-07-09)

Both workflows fire on the same push to `claude/**`. Auto-merge can merge AND DELETE the branch before compose-profile's shallow fetch runs → `fatal: couldn't find remote ref <branch>` (exit 128, red run — observed on the v3.13 push). Fix in compose-profile.yml: when the fetch fails, a `claude/*` branch is checked with `git ls-remote`; gone ⇒ its content was promoted, so the job falls back to checking the ORG-PROFILE sync on `main` (`COMPOSE_REF=main` via `GITHUB_ENV`) instead of failing. Same commit fixed the workflow's stale v2 path (`prompts/daily-cti-brief.md` → `prompts/cti-run.md` in `paths:` and the operator-branch `git add`) — the filter had silently not been watching the v3 master prompt.

## Runaway main runs + the overtaken-run publish race (audited 2026-07-11, guarded in v3.21)

Two July runs silently ran far past any sane wall-clock: `2026-07-04T1809Z-intel` (**17.8 h**) and `2026-07-09T2009Z-intel` (**11.2 h** — fired 20:09, published 07:56 next day). Consequences observed: entries published up to ~11 h late, and the next scheduled fire overtakes the stalled run — `2026-07-10T0409Z-intel` computed `gap_hours: 16` from `1211Z` because the 2009Z run's record hadn't landed on main yet, i.e. the overtaking run cannot see the overtaken run's in-flight coverage. The 2009Z run improvised the correct recovery (re-pulled main before composing, deduped its 7 candidates against the 0409Z run's 6 entries, published only the 4-delta). v3.21 codifies both: main-run wall-clock watchdog (past ~3 h, land the run — no new research) + mandatory re-sync-and-re-dedup when overtaken; `check_run.py` WARNs on `duration_seconds` > 3 h and (--all) on a v3.14+ record still missing `publish_status` >24 h after start. Root cause of the stalls is scheduler/container-side (long suspensions), same class as the 07-07 outage — don't re-diagnose the repo.

## sources.json serialization drift (re-normalized 2026-07-09)

Despite the canonical `indent=1, ensure_ascii=False` contract (see [state-file-serialization](state-file-serialization.md)), the committed file had drifted to `ensure_ascii=True` escapes (`—` for —) on some earlier run — symptom: only lines containing non-ASCII flip in a diff (~180 lines). Re-normalized to the canonical form on 2026-07-09; if that symptom reappears, some writer used the default `ensure_ascii=True` again.
