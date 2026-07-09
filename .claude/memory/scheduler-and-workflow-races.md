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

## sources.json serialization drift (re-normalized 2026-07-09)

Despite the canonical `indent=1, ensure_ascii=False` contract (see [state-file-serialization](state-file-serialization.md)), the committed file had drifted to `ensure_ascii=True` escapes (`—` for —) on some earlier run — symptom: only lines containing non-ASCII flip in a diff (~180 lines). Re-normalized to the canonical form on 2026-07-09; if that symptom reappears, some writer used the default `ensure_ascii=True` again.
