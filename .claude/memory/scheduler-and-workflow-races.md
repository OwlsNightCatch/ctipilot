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

## Cadence is operator-owned and intentionally variable (operator decision 2026-07-18)

The post-07-14 drop to a single daily fire (0409Z) was **intended** — the operator confirmed it responding to the 07-18 audit. Standing policy: the scheduler cadence may be raised or lowered at will, at any time, without notice; the entire setup must work off the **gap to the last run** (PD-7's gap-derived window — which is exactly what it does). Consequences: (a) a changed cadence is never an audit finding, an outage diagnosis, or an operator recommendation — audits check only that the gap-derived windows self-healed with no coverage hole (codified in `prompts/quality-audit.md` Phase 3, v3.27); (b) never treat "fewer fires than before" as a defect signal — only a *record-less* gap on a schedule that was supposed to fire (the 07-07 pattern above) is an availability signal; (c) latency effects of a lower cadence may appear as context in a miss's root cause, never as a flagged defect. Same date, related decisions: Phase 5.7 verifier iteration cap raised 5 → 8 (v3.27; double-CLEAN gate unchanged), and the `bd.zh.ch` MedusaLocker watch item CLOSED by operator decision (no dedicated tracking; new info flows through normal runs as `update_of`).

## `completed` / `duration_seconds` understated the whole fire (audited 2026-08-24, fixed in v3.32)

The wall-clock watchdog above was checking a number that could not see the overrun it exists to catch. Through v3.31 `prompts/cti-run.md` stamped `work/<run-id>/main.ended_at` in **Phase 5** — before the mechanical gate and before the Phase 5.7 verifier loop — and the record's `completed` was read straight from that stamp. Every run therefore recorded a duration that stopped roughly where its verifier loop began. Measured store-wide on 2026-08-24: **the majority of records have a `completed` that precedes one of their own children's `ended_at`** — three independent recomputations during the audit gave 103 of 146, 100 of 141 and 104 of 148, so quote the shape and the worst case, not a fraction, worst skew 125 min (`2026-08-04T0411Z-intel`); `2026-08-10T0411Z-intel` recorded 3103 s (~52 min) for a fire its own run notes place at ~2 h 55 m, and its last verifier iteration returned at 06:58Z against a `completed` of 05:02Z.

The defect had already been *diagnosed once and not fixed*: the 2026-08-10T0110Z weekly's verifier caught the same shape on that record ("a `main.ended_at` stamp taken at the end of the state phase, before the pre-verifier guard ran"), the run corrected its own frontmatter, and the mechanism stayed broken for every subsequent fire. **A verifier finding that is repaired only in the record it was found in is a fix that did not ship** — ask whether the finding names a mechanism, and if it does, the mechanism is the work item.

v3.32 fix, two halves: `cti-run.md` Phase 5 marks the stamp provisional and Phase 6 step 0 re-stamps immediately before the commit (after the loop, before staging); `tools/check_run.py` `check_completion_covers_run` FAILs a v3.32+ record whose `completed` precedes any `verification.iterations[].ended_at` or `sub_agents.*.ended_at` it carries (WARN under `--all`, silent on pre-v3.32 records so ~100 immutable legacy records do not become that many acknowledgment-ledger rows). Phase 7 polling stays outside the figure by design: `completed` is when the run finished producing, `publish_checked_at` is when it confirmed the result landed. **Consequence for reading history: every pre-v3.32 `duration_seconds` in the store is a floor, not a measurement** — including the "no runaway this window" lines in earlier audit reports.
