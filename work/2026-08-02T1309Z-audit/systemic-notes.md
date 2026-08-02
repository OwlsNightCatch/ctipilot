# Phase 3 — systemic & operational review (main context, local files)

Window: 2026-07-26T13:08:25Z → 2026-08-02T13:09:58Z (~168 h). 71 entries, 11 run records
(10 with `started` inside the window; the 2026-07-26T1308Z-audit record anchors it).

## 1. Telemetry

| run_id | dur | gap_h | win_h | publish | entries | updates | iters | final |
|---|---|---|---|---|---|---|---|---|
| 2026-07-26T1308Z-audit | 2.6 h | 168 | 193 | ok | 9 | 4 | 5 | CLEAN (waived) |
| 2026-07-26T2309Z-weekly | 0.5 h | – | – | ok | 11 | 2 | 8 | CLEAN (confirmed) |
| 2026-07-27T0110Z-weekly | 2.3 h | – | – | ok | 0 | 0 | 8 | NEEDS_FIXES (resid 1) |
| 2026-07-27T0409Z-intel | 0.5 h | 3 | 24 | ok | 3 | 1 | 7 | CLEAN (confirmed) |
| 2026-07-28T0409Z-intel | 1.9 h | 24 | 26 | ok | 6 | 1 | 5 | CLEAN (confirmed) |
| 2026-07-29T0408Z-intel | 2.6 h | 24 | 26 | ok | 11 | 1 | 5 | NEEDS_FIXES (resid 2) |
| 2026-07-30T0409Z-intel | 0.8 h | 24 | 26 | ok | 8 | 1 | 4 | NEEDS_FIXES (resid 1) |
| 2026-07-31T0409Z-intel | 0.9 h | 24 | 26 | ok | 11 | 5 | 6 | NEEDS_FIXES (resid 2) |
| 2026-08-01T0409Z-intel | 2.7 h | 24 | 26 | ok | 8 | 2 | 8 | CLEAN (confirmed) |
| 2026-08-02T0409Z-intel | 2.1 h | 24 | 26 | ok | 4 | 1 | 8 | CLEAN (waived, cap) |

- **No runaway runs.** Longest 9,666 s (2.69 h) against the ~3 h threshold. The v3.21 watchdog holds.
- **Publish follow-through 10/10 `ok`.** No stale `pending`.
- **Gap-derived windows self-healed** across the one off-cadence gap (3 h after the backup weekly);
  24 h floor applied throughout; no record-less day.
- Cadence: one daily 0409Z intel fire + the weekly pair. Operator-owned; not a finding.

## 2. Verifier loop

Rotation held perfectly in every fire (strict `cti-verification` / `cti-verification-alt` alternation,
no same-model consecutive pair anywhere in the window).

- Confirmed CLEAN (two consecutive CLEANs, two models): **4 of 9** post-audit fires
  (07-26 weekly, 07-27 intel, 07-28, 08-01). Previous window: 7 of 10.
- Fail-open at the cap on a single CLEAN: 1 (08-02, iteration 8 CLEAN after a NEEDS_FIXES at 7).
- Low-residual early exit / NEEDS_FIXES final: 4 (07-27 weekly resid 1, 07-29 resid 2,
  07-30 resid 1, 07-31 resid 2). Previous window: 2 of 10.
- Mean iterations 6.6 (window) — 5 of 9 fires reached ≥ 7.

## 3. Verifier finding distribution — July + August run records

F4 154 · F11 92 · F3 80 · F5 30 · F14 24 · F9 16 · F8 15 · F17 14 · F12 12 · F2 10 ·
F1 7 · F6 7 · F13 6 · F7 5 · F10 4 · **F16 1** · **F18 1** · F15 1.

The single F16 is mis-coded (a machine-surface contradiction, not a priority call).
So across ~40 fires the editorial gate's two discipline checks produced **effectively zero signal**.

## 4. Discipline metrics

| metric | this window | prior window |
|---|---|---|
| operational entries | 61 | 58 |
| `high` share (operational) | 25/61 = 41.0 % | 13/58 = 22.4 % |
| `critical` | 1 (07-28 Arista VeloCloud) | 0 |
| actions / operational entry | 53/61 = 0.87 | 28/58 = 0.48 |
| entries with 0 actions | 25/61 = 41 % | 34/58 = 59 % |
| entries with ≥2 actions | 17 | 4 |
| empty `techniques[]` | 3 (2 policy, 1 outlook — legitimate kinds) | 2 |
| `update_of` deltas | 18 | 11 |
| Admiralty ratings | 71/71 (A1 20 · A2 8 · B1 11 · B2 28 · B3 1 · C2 2 · C3 1) | 57/57 |
| `watchlist_hit` | 0 (no watchlist configured) | 0 |

Store-wide priority: 1,101 entries — 15 critical · 399 high (36.2 %) · 685 notable · 2 routine.
2026-07 full month: 277 entries, 33.2 % high, 1 critical. 2026-08 MTD: 12 entries, 41.7 % high.

## 5. Source health

- 6 of 15 active essential sources contributed **zero** window citations: `cert-at`,
  `cert-eu`, `cert-pl`, `enisa-euvd`, `ncsc-ch-focus`, `ncsc-ch-incidents`.
  Four sit at `consecutive_quiet_periods` = 4 (cert-at, cert-pl, ncsc-ch-focus, ncsc-ch-incidents).
  Five of the six were the same set last audit; `enisa-euvd` is new to the list (quiet counter 0,
  so it is being fetched and read but never cited).
- `state/source_health.json` snapshot is 2026-08-02T04:40Z, taken **during** the reader-pool
  outage: 8 sources classed `reader-quota`, 3 carry `action: needs-demote`
  (`ico-uk`, `siemens-productcert-csaf`, `fbi-cyber-alerts`). All three were diagnosed by the
  fires as reader-pool exhaustion or probe-target mismatch, not recipe death, and
  `siemens-productcert-csaf` was already repaired (`probe_url` added) after the snapshot was
  written — so the committed snapshot advertises three repair orders that no longer hold.
  → re-probe this fire now the pool is refilled.

## 6. Reader pool

`jina-usage`: 7 live keys, 70,000,000 tokens, no warning; every key's trial window opened
2026-08-02 09:37–09:51Z. The pool **was** exhausted for the 0409Z fire (8 sources classed
`reader-quota` in its health sweep) and the operator refilled it ~5 h later. Third refill in
15 days. Recommendation 1 stands, resized.

## 7. Fix effectiveness — 2026-07-26 audit

| fix | verdict |
|---|---|
| `wordpress-org-news` unreachable (candidate rotation) | **took.** `last_successful_fetch` null → 2026-07-27, fetched via the documented feed, recorded 200-but-quiet |
| `sources.promotion_due[]` digest field | **took.** Empty this fire; `zscaler-threatlabz` and `siemens-productcert-csaf` were promoted off it by the 07-27 and 07-30 fires with the counts recorded |
| PD-11(b) "otherwise requiring an out-of-band response" clarification | **took.** Fires now name the mechanical reason when declining an unexploited flaw (osTicket CVE-2026-18363 "abuse presupposes the attacker already holds a valid reset token"; MOVEit 2026.0.3 "adjacent-network with high attack complexity") |
| PD-13 KEV split + re-read duty | **no counter-example.** No KEV exploitation-status flip went unrecorded in the window (pending G1) |
| one-citation-per-clause + verifier adjacency sweep (attribution limb b) | measured by the truth passes — see § Findings |
| five named clusters registered (`sectoprat`, TELESHIM toolkit) | **did not take.** None of `sectoprat`, `arechclient2`, `teleshim`, `mixedkey`, `bindcloak`, `fakeagent` exists in `entities/registry.yaml` |
| GTIG cryptonym alias hygiene | **took.** `SANDWORM RELIC` added as an alias on `actor:sandworm` by the 07-27 backup weekly; no duplicate key created from a cryptonym anywhere in the window |

## 8. Gate & pin

`check_run.py --all`: 20 pass · **2 warn** · 0 fail · 9 acknowledged.
`attack_data.py --check`: local v19.1 == upstream latest v19.1.
`site/build.py`: clean, no self-check warnings (entries=1105, days=84, weeklies=11, entities=1199, cves=692).

Open warnings, both `verification-confirmation`:
1. `2026-07-26T1308Z-audit` — the previous audit's own wall-clock waiver.
2. `2026-08-02T0409Z-intel` — single CLEAN at the 8-iteration cap.
