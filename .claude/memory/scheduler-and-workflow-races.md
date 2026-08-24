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

## 2026-08-22 — the worst overtake yet: 53 h alive, three fires past it, half the run stood down

`2026-08-22T0410Z-intel` composed, gated and triple-verified **sixteen** entries, then discovered at the
pre-push sync that `origin/main` had advanced by **three** fires. Elapsed from open to that discovery: about
**53 h** — the container survived across two calendar days, so every file mtime and composition timestamp in
the run still read 08-22 while the publish happened on 08-24. Its own ~3 h watchdog fired correctly and was
obeyed; the stall was container-side, same class as the July cases above. **Eight of the sixteen were
duplicates and were stood down; eight shipped as the delta.**

Four things worth carrying:

- **Two of the eight duplicates had NO CVE and NO shared entity key.** The Defender BTR.sys research
  (neither entry carried a CVE; this run's carried no entity) and a Swiss communal mailbox compromise
  (this run registered `incident:martigny-combe-…`, the overtaking fire registered nothing) were caught
  only by *reading* the candidates against the store. A CVE-and-entity index pass would have shipped both.
  The mechanical index is what a rushed run leans on, and it is exactly then that it is not enough.
- **An overtaking fire's window is computed from the gap to the last *published* run, so it deliberately
  swallows yours.** The 08-23 intel fire ran `window_hours: 74` *because* this fire had never published.
  Expect the overlap to be near-total, not partial.
- **Check `origin/main` at every phase boundary, not only at Phase 6.** Twelve of sixteen
  entry-verifications were spent on material that could not publish. A cheap `git fetch` + run-record
  listing at each boundary would have caught it hours earlier. (Recorded as a recommendation to the
  operator in the run record rather than pushed into the prompt unilaterally at 53 h.)
- **Resolve the merge by taking `main`'s shared state, then re-applying only your genuinely-new records.**
  The habitual `--ours` on `entities/registry.yaml` / `state/*.json` assumes your side is purely additive.
  After an overtake it is not: `--ours` would have discarded three fires of registry, CVE-index and
  source-health work. Took `main` for registry/cves_seen/source_health/sources.json, then re-added 3
  registry records, 11 CVE records and 1 candidate source. Also check your *tooling* diffs the same way —
  this run's `source_health.py` fix turned out to be a rediscovery of one `main` already carried from the
  same `sec-disclosures-edgar` case, and `main`'s was more thorough, so ours was discarded.

One reshape worth copying: a duplicated-but-still-valuable entry can survive as an `update_of` on the
overtaking entry when it carries a real correction (here the weekly rollup had 8 of 9 Cisco CVEs and called
the whole set unauthenticated when 3 of 9 are `PR:L`). Two gate rules bite when you do it: `update_of`
cannot point at an entry with a *later* `discovered_at`, and the entry's folder date must equal its
`discovered_at` — so the reshaped entry moves to the folder of the day you found the divergence, not the
day you read the primary.

## auto-merge-claude.yml aborts on `state/coverage_backlog.md` (observed twice, 2026-08-24)

**The auto-merge workflow's auto-resolution list does not include `state/coverage_backlog.md`**, and that
file is touched by *every* fire — intel, weekly and audit alike. So whenever two fires' pushes interleave,
the workflow dies with `::error::Merge conflict in paths outside the auto-resolution rules; resolve
manually.` It only resolves `state/cves_seen.json`, `state/source_health.json`, `entities/registry.yaml`
(→ours) and `sources/sources.json` (→theirs). Two consecutive runs of `2026-08-24T0410Z-intel` failed this
way before the merge was done by hand locally. **The fix is always local: merge `origin/main` into the
feature branch, resolve the backlog by hand, commit, push — then the workflow sees a clean fast-forward.**
An `--ours`/`--theirs` rule would be wrong for this file in either direction, which is probably why it is
absent: both sides legitimately add rows and notes, so the only correct resolution is a *union* with the
published rows moved to `## Struck`. Worth proposing to the operator that the workflow learn a union
strategy for it; until then, expect to resolve it by hand on every overtake.

Two mechanical traps in that resolution, both hit on 2026-08-24:

- **The same row can appear twice after the merge** — once inside the conflict hunk (your side, moved) and
  once as *common context* (main's side, in place). Git will happily leave you both. Extract all three
  stages (`git show :1: / :2: / :3:`) and diff the row sets rather than editing the conflicted file in
  place.
- **`state/cves_seen.json` is NOT safe to take `--ours` after an overtake**, exactly as the 08-22 lesson
  says for the registry: ours had 917 records, main had 941. Union-merge keyed on `id` with your changed
  records overlaid on main's.

## Triple overtake, 2026-08-24: the second entry lost was a *correction*, and the audit fire found it too

`2026-08-24T0410Z-intel` (11.3 h — container stall of ~4.7 h before Phase 1, then an account session limit
mid-verification) was overtaken by three fires. Two entries were dropped as duplicates: the SOCRadar
FTP-banner research (a delayed 08-22 fire landed its own) and a Keycloak CVE-2026-18963 product-state
correction — **the weekly quality audit's retrospective truth pass had independently reached the same
finding and published it first**. New lesson on top of 08-22: *the audit fire is a publisher too*, so
an intel run's `update_of` corrections of the store's own errors are the most collision-prone entries it
composes. Check `entries/<today>/` on `origin/main` for the same `update_of` target before spending a
verification round on a correction.

Also: when your dropped entry carried a fact the surviving one lacks, and that fact is not
defender-actionable on its own (here: the vendor's VEX document was revised the day after the erroneous
entry, which bears on the surviving entry's claim that the record never read differently), the right home
is a **correction-owed row in `state/coverage_backlog.md`** for the audit to weigh — not a third entry on
one CVE, and not silence.

## sources.json serialization drift (re-normalized 2026-07-09)

Despite the canonical `indent=1, ensure_ascii=False` contract (see [state-file-serialization](state-file-serialization.md)), the committed file had drifted to `ensure_ascii=True` escapes (`—` for —) on some earlier run — symptom: only lines containing non-ASCII flip in a diff (~180 lines). Re-normalized to the canonical form on 2026-07-09; if that symptom reappears, some writer used the default `ensure_ascii=True` again.

## Cadence is operator-owned and intentionally variable (operator decision 2026-07-18)

The post-07-14 drop to a single daily fire (0409Z) was **intended** — the operator confirmed it responding to the 07-18 audit. Standing policy: the scheduler cadence may be raised or lowered at will, at any time, without notice; the entire setup must work off the **gap to the last run** (PD-7's gap-derived window — which is exactly what it does). Consequences: (a) a changed cadence is never an audit finding, an outage diagnosis, or an operator recommendation — audits check only that the gap-derived windows self-healed with no coverage hole (codified in `prompts/quality-audit.md` Phase 3, v3.27); (b) never treat "fewer fires than before" as a defect signal — only a *record-less* gap on a schedule that was supposed to fire (the 07-07 pattern above) is an availability signal; (c) latency effects of a lower cadence may appear as context in a miss's root cause, never as a flagged defect. Same date, related decisions: Phase 5.7 verifier iteration cap raised 5 → 8 (v3.27; double-CLEAN gate unchanged), and the `bd.zh.ch` MedusaLocker watch item CLOSED by operator decision (no dedicated tracking; new info flows through normal runs as `update_of`).
