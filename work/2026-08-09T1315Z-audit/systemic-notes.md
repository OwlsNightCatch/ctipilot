# Phase 3 — systemic & operational review (main context, local files)

Window: 2026-08-02T13:09:58Z → 2026-08-09T13:15:57Z (168.1 h). 12 run records, 80 entries.

## 1. Telemetry

| run | dur_s | gap_h | win_h | published | iters | final | residual | publish |
|---|---|---|---|---|---|---|---|---|
| 2026-08-02T1309Z-audit | 2402 | 168.0 | 168 | 5 (+2 upd) | 8 | CLEAN (waived) | 0 | ok |
| 2026-08-02T2311Z-weekly | 3285 | — | — | 15 (+3) | 4 | NEEDS_FIXES | 1 | ok |
| 2026-08-03T0110Z-weekly | 4193 | — | — | 0 (stand-down) | 8 | CLEAN (waived) | 0 | ok |
| 2026-08-03T0409Z-intel | 2524 | 3 | 24 | 3 | 8 | CLEAN (confirmed) | 0 | ok |
| 2026-08-04T0411Z-intel | 2611 | 24 | 26 | 7 (+2) | 8 | NEEDS_FIXES (cap) | 1 | ok |
| 2026-08-05T0412Z-intel | 2751 | 24 | 26 | 15 (+4) | 5 | NEEDS_FIXES (early) | 0 | ok |
| 2026-08-06T0411Z-intel | 2743 | 24 | 26 | 9 (+2) | 5 | NEEDS_FIXES (early) | 1 | ok |
| 2026-08-07T0411Z-intel | 2751 | 24 | 26 | 8 | 4 | NEEDS_FIXES (early) | 1 | ok |
| 2026-08-08T0409Z-intel | 7932 | 24 | 26 | 14 (+4) | 2 | NEEDS_FIXES (early) | 1 | ok |
| 2026-08-09T0412Z-intel | 2151 | 24 | 26 | 4 (+1) | 2 | NEEDS_FIXES (early) | 2 | ok |

- **No runaway.** Longest 2026-08-08 at 7932 s (2.2 h), inside the ~3 h watchdog. No gap without a run record; the 3 h gap on 08-03 is the weekly landing an hour before the intel fire and the 24 h floor self-healed it correctly.
- **Publish follow-through: 12/12 `publish_status: ok`.** No stale or missing Phase 7 amendment anywhere in the window.
- **Cadence** is operator-owned and not a finding (operator decision 2026-07-18). Every fire's gap-derived window self-healed; no coverage hole between runs.

## 2. Verification convergence — the watch item escalates

Confirmed two-model double-CLEAN: **2 of 12** (2026-08-01 and 2026-08-03 intel). Previous window 4 of 9; the one before 7 of 10. Mean iterations 5.8 (prev 6.6). The previous audit's escalation condition ("confirmed-CLEAN share falling further, or two or more fires reaching the cap unconverged") is **met**.

Shape of the fall: iteration counts collapse across the window (8, 8, 8, 8, 5, 5, 4, 2, 2) and every fire from 08-05 onward publishes on the **low-residual early exit** (decision rule 5) rather than converging to CLEAN. Residuals are genuinely low (0–2) and none carried an F1 or F4, so every exit was rule-legal. But two fires exited at iteration 2, which means no pass ever cold-read the *final* state — iteration 2 found new defects, they were remediated, and the run published with nobody verifying those last fixes. That is precisely the gap the double-CLEAN gate exists to close, reached legally through a different door.

## 3. Rotation collapse — mechanism identified, gate blind to it

`2026-08-06T0411Z-intel` ran **all five verification iterations on `cti-verification` (Opus)**. Every `cti-verification-alt` spawn — four of them — was terminated by a provider-side content safeguard. The run disclosed it fully (per-iteration `rotation_note` plus a waiver). Two research spawns on the same fire were killed the same way and had to be respawned.

This is recurring, not exceptional: 2026-07-23 ran all 8 iterations on Opus for the same reason; the 2026-08-03 weekly lost all four of its Sonnet-pinned *research* spawns and recovered them with an explicit `model: opus` override.

Two gate defects found:
1. `check_verification_confirmation` returns early on a `NEEDS_FIXES` final verdict, so a fully collapsed rotation on any non-CLEAN publish path is **invisible** store-wide.
2. `2026-08-06` recorded its waiver at top level as `verification_confirmation_waived`; the check reads `verification.confirmation_waived`. Had that fire converged to CLEAN, its fully-documented fail-open would have been reported as an undocumented one.

Both fixed in `tools/check_run.py` this run; the recovery ladder (override before waiver) shipped in `prompts/cti-run.md` Phase 5.7.

## 4. Coverage backlog — nine verified items lost

`2026-08-03T0110Z-weekly` stood down as `duplicate-week` after researching and verifying the full ISO week, and listed nine items the primary weekly did not carry. **A grep of every entry published 08-03 → 08-09 finds none of them.** Both recency gates made them structurally unreachable: the next intel window is 24–26 h, the next weekly's is the following ISO week. Fixed with `state/coverage_backlog.md` + a Phase 0 read duty + a stand-down write duty (v3.31), seeded with the eight recoverable rows.

## 5. Source health — reachability ≠ readability

96 of 157 active sources contributed zero cited sources across the whole 7-day window. Five of them are **essential**-tier and all show a successful fetch on 2026-08-09: `cert-at`, `cert-eu`, `enisa`, `enisa-euvd`, `ncsc-uk` (quiet=2 — the same source the 2026-07-11 audit found dark-but-green).

The **whole OT/ICS research-lab surface is dark**: `dragos` (quiet 2), `nozomi-networks` (quiet 3), `claroty-team82`, `sans-ics`, `industrialcyber-co` — zero contribution, on a deployment whose additional sectors include energy, water and transport. The 2026-08-03 weekly flagged this same surface as entirely unread with "a cause that remains unestablished". Spot-checks queued for after the research sub-agents return.

## 6. Discipline drift

| metric | this window | prev window | store |
|---|---|---|---|
| operational entries | 65 | 60 | 817 |
| `high` share (operational) | **52.3 %** | 41.7 % | 43.1 % |
| actions per operational entry | **1.09** | 0.88 | 0.58 |
| entries with ≥2 actions | 20 | 17 | 116 |
| entries with **no** action | **23.1 %** | 41.7 % | 61.6 % |
| techniques[] on behaviour kinds | 3.64 mean, 0 empty | 4.27, 0 empty | — |
| classification present | 80/80 | 71/71 | — |
| `update_of` | 18 | 18 | 128 |

- **`actions[]` density is on a three-window monotonic rise** (0.53 → 0.88 → 1.09) and the "empty is normal" shape is eroding fast (59 % → 58 % → 77 % of operational entries now carry at least one action). Hand review of all 71 actions found the great majority concrete, product-named and finding-derived; roughly four are soft (a hedged "where the estate allows it", two least-privilege/hardening-programme items that would be true had the entry never been published, one archive-hygiene recommendation). Not yet a defect class, but the trend is the watch item's escalation trigger and the verifier caught 3 F18s this window against 0 last.
- **`high` share jumped 10.6 points to 52.3 %.** Phase 3b calibration is **not due** — the 2026-08-02 report already carries this calendar month's `## Priority calibration` section — so no calibration section ships here. Recorded as a watch item with the number pre-computed for the September fire.

## 7. Gate & pin

- `check_run.py --all` at preflight: 19 pass · 3 warn · 0 fail · 11 acknowledged. After this run's fixes and ledger review: **21 pass · 0 warn · 0 fail · 14 acknowledged**. `site/build.py` emits no self-check warnings.
- **ATT&CK pin drift: local v19.1 → upstream v19.2** (published 2026-08-05T21:33Z), unmentioned by any run record in the window. The weekly maintenance duty ran on 08-03 and correctly reported v19.1 as current *at that time*; v19.2 landed two days later and no fire since has re-checked. Update deferred until the retrospective truth passes finish, because they validate `techniques[]` ids against the pin and changing ground truth mid-flight would invalidate their results.

## 8. Fix effectiveness — previous audit's v3.30 changes

| Fix | Evidence | Verdict |
|---|---|---|
| PD-8(b) disclosure-stream scoping | Per-product vulnerability entries published normally this window; no round-up swallowing | **Took** |
| Per-fact attribution (v3.29, re-check) | F3 49 → 38 per 10 runs, continuing its fall | **Holding** |
| `grep -F` quote-fidelity mechanisation | F4 59 → 65 per 10 runs — did **not** fall. Breakdown shows most F4s are run-record/report self-description defects rather than entry quote splices, and two quote defects that did land were the documented extraction failure mode (a tag-strip inserting whitespace) | **Partial** |
| ATT&CK evidence floor | 0 empty `techniques[]` on behaviour kinds; no bolted-on access vectors found by the truth passes | **Took** |
| Classification independence definition | F17 2 → 7 — a *rise*, but reading the findings shows the verifier now catching "one assessor, several publishers" precisely. The check got sharper; composition still over-awards credibility 1 | **Took at the verifier, not at composition** — now mechanised in the gate |
| Weekly duplicate-week pre-verifier re-check | Caught the 08-03 race at 02:10Z instead of at the Phase 6 sync, saving the eight-iteration cost | **Took** — extended this run to sweep unpromoted branches |
