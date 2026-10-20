# Store cleanup tracker

Program: [`prompts/cleanup-coordinator.md`](../../prompts/cleanup-coordinator.md). Machine-readable plan with every row's entry ids: [`work/cleanup/plan.json`](../../work/cleanup/plan.json) (inventory: `python3 work/cleanup/inventory.py`). Each cleanup session reads this file, takes the next wave, updates the rows it touched and names the next wave below.

**Next wave:** 01 (W7-01, W7-02, W6-04, W1-A), coordinator session of 2026-10-20. No wave starts between Saturday 18:00Z and the Sunday audit's record landing on `main`.

## Definition of done (§ Mandate)

1. Every published entry truth-verified under the current standard since its last substantive change: legacy queue empty (`python3 tools/legacy_review.py --stats` 0 pending) and no entry left that no audit truth pass covered.
2. Every known finding applied or declined with a reason: the 2026-10-18 out-of-week verdicts, carried residuals and `(pre-existing)` advisories, portable reference-branch hunks.
3. No duplicate findings: each pair folded with `tools/fold_entries.py` or linked through `references[]`.
4. Registry clean: duplicate orphans tombstoned, no relation with a missing source entry, the known summaries fixed.
5. Sources and state current: 2026-10-11 recommendations 5 to 7 decided, no dead acknowledgment row, backlog holds only live rows.
6. No dead weight: unused tools, stale docs, retired code paths, stale `work/` material removed; gate false positives fixed.
7. Program retired (§ C9).

After every wave: `python3 tools/check_run.py --all` ends `0 warn · 0 fail`, `python3 site/build.py` is warning-free.

## Totals (baseline 2026-10-20)

| Measure | Baseline | Now |
|---|---|---|
| Entries in the store | 996 | 996 |
| Legacy queue pending | 408 | 408 |
| 2026-10-18 out-of-week verdicts not applied (factual error / imprecision / clean) | 77 / 63 / 42 (182 rows, 25 on entries since folded) | 77 / 63 / 42 |
| Never-verified non-legacy entries (W3) | 71 | 71 |
| Known duplicate groups open (W4) | 4 + scan | 4 + scan |
| Registry records / orphans without entry or relation | 1521 / 179 non-product + 4 product | 1521 / 183 |
| `check_run.py --all` | 0 fail · 1 warn · 25 acknowledged | 0 fail · 1 warn |
| Rows done / declined / open | 0 / 1 / 43 (+1 done before the program) | see table |

## Waves

| Wave | Rows | Status |
|---|---|---|
| 01 | W7-01, W7-02, W6-04, W1-A (16 entries) | planned |
| 02 | W1-B (57), W1-C (5), W1-E (12), W1-F (8) | planned |
| 03 | W4-01 to W4-05, W1-D (43) | planned |
| 04 | W2-01 (77 legacy) | planned |
| 05 | W2-02 (77) | planned |
| 06 | W2-03 (77) | planned |
| 07 | W2-04 (77) | planned |
| 08 | W2-05 (77) | planned |
| 09 | W3-01 (71) | planned |
| 10 | W7-08, C9 retirement | planned |

W5, W6 and W7 rows marked `standalone` ship as small merges of their own between waves, the moment they are green.

## Rows

| Row | WS | Item | Size | Wave | Status |
|---|---|---|---|---|---|
| W7-01 | W7 | tools/entry_record.py: tested record tool (add / amend / diff), CLAUDE.md Key commands row | 1 | 01 | open |
| W7-02 | W7 | Gate false positives: _page_text (extract skips the tag stripper, description metas kept, 'opens in a new window' labels removed, cache header dropped), image-only PDF unreadable for citation-cve and quote-literal; tools/test_check_run.py | 1 | 01 | open |
| W6-04 | W6 | Acknowledge the one open WARN: 2026-10-18T1307Z-audit duration_seconds=117266 (settled history, the fire spanned the v4.21 pause) | 1 | 01 | open |
| W1-A | W1 | Non-legacy-batch factual errors, passes T1-T9 (2 of them legacy-pending: mark reviewed after repair) | 16 | 01 | open |
| W1-B | W1 | Imprecisions, passes T1-T9 (13 legacy-pending: mark reviewed after repair, add rating and mapping) | 57 | 02 | open |
| W1-C | W1 | Clean verdicts on legacy-pending entries, passes T4/T5: mark reviewed after the rating and mapping their kind requires | 5 | 02 | open |
| W1-E | W1 | Carried residuals and (pre-existing) advisories, audits 2026-09-27 to 10-18 (labelled lines on RoguePlanet 07-09 and SAP 08-12, LiteLLM affected_products, OpenAI agents marker strings, WinRAR/Splunk event_date, PHP SOAP CVE-2026-7262 score, ShinyHunters PeopleSoft action scope and 'external', Instructure uncited source, Acronis JSON primary, Exchange 10-14 10-16 section citation, Ivanti 10-14 25.1.3.0 framing; em dashes fixed wherever a wave writes a record, else declined: stripped at render) | 12 | 02 | open |
| W1-F | W1 | Portable reference-branch entry hunks (re-derive on main, re-verify, re-record) | 8 | 02 | open |
| W1-D | W1 | Duplicate and legacy batch verdicts (D1-D3, L) on entries the 2026-10-11 audit corrected after the pass read them: re-derive each defect on the current text (25 rows were folded, their defects re-checked on the survivor) | 43 | 03 | open |
| W4-01 | W4 | YellowKey 2026-05-15 vs Nightmare Eclipse 2026-05-30: distinct findings sharing CVE-2026-45585, link through references[]; Nightmare Eclipse re-verified and rewritten (watch item) | 2 | 03 | open |
| W4-02 | W4 | RoguePlanet 2026-06-19 vs 2026-07-09: same finding, fold into 2026-07-09 (ShieldBreak 2026-08-12 stays distinct) | 2 | 03 | open |
| W4-03 | W4 | Ghost CMS 2026-05-25: the ClickFix deep dive and the 'large-scale ClickFix campaign' entry are the same finding per D3; decide fold | 2 | 03 | open |
| W4-04 | W4 | Pwn2Own Berlin 2026 roundup 2026-05-17 vs the DEVCORE Exchange chain entry: re-verify the roundup, then fold or link | 2 | 03 | open |
| W4-05 | W4 | Store-wide non-CVE twin scan (same entity and similar title or same primary URL, no references[] link); fold or link each pair found | TBD | 03 | open |
| W2-01 | W2 | Legacy queue batch 1, oldest first (2026-05-10 to 2026-05-22) | 77 | 04 | open |
| W2-02 | W2 | Legacy queue batch 2, oldest first (2026-05-22 to 2026-05-31) | 77 | 05 | open |
| W2-03 | W2 | Legacy queue batch 3, oldest first (2026-05-31 to 2026-06-10) | 77 | 06 | open |
| W2-04 | W2 | Legacy queue batch 4, oldest first (2026-06-10 to 2026-06-21) | 77 | 07 | open |
| W2-05 | W2 | Legacy queue batch 5, oldest first (2026-06-21 to 2026-07-03) | 77 | 08 | open |
| W3-01 | W3 | Entries no audit truth pass ever covered (not legacy, filed before the 2026-10-18 audit, not audit-published) | 71 | 09 | open |
| W5-01 | W5 | Eurail incident summary: drop the retracted 'Dutch DPA and EDPS are reviewing' claim (reference-branch registry hunk) | 1 | standalone | open |
| W5-02 | W5 | incident:daemon-tools-supply-chain-2026 'EU governments targeted' | 1 | done-before | done 2026-10-11T1307Z-audit |
| W5-03 | W5 | malware:beavertail summary 'an initial loader' (re-read the 2026-09-18 joint advisory) | 1 | standalone | open |
| W5-04 | W5 | 179 non-product registry records keyed by no entry and in no relation: tombstone each that duplicates a canonical key (merged_into), leave the rest | 179 | standalone | open |
| W5-05 | W5 | 4 product records no entry's affected_products resolves to: tombstone onto the surviving product or leave | 4 | standalone | open |
| W5-06 | W5 | Relations whose source entry is gone: 0 on 2026-10-20; re-check after every fold wave | 0 | each wave | open |
| W6-01 | W6 | Red Canary (2026-10-11 rec. 5): record `redcanary` now points at the Zscaler blog, last success 2026-09-13: retire or repoint on the evidence | 1 | standalone | open |
| W6-02 | W6 | ssd-disclosure (rec. 6): candidate, fetch_method blocked on every transport: accept the gap or retire | 1 | standalone | open |
| W6-03 | W6 | google-tag vs mandiant-gtig overlap (rec. 7): fold google-tag into mandiant-gtig or keep both with a reason | 1 | standalone | open |
| W6-05 | W6 | Four entry-scoped attack-mapping acknowledgments (research entries with empty techniques[]): entries are fixed through records, never acknowledged; map the tradecraft or justify and keep | 4 | standalone | open |
| W6-06 | W6 | state/coverage_backlog.md: trim the 98 struck rows surfaced before 2026-09-20 (over 30 days) | 98 | standalone | open |
| W6-07 | W6 | Ack ledger rows matching nothing: 0 of 25 on 2026-10-20 (check_run ack-ledger PASS); re-check at C9 | 0 | each wave | open |
| W7-03 | W7 | Remove tools/migrate_briefs.py (2003 lines) and tools/migrate_updates.py (404 lines), one-time v2/v4 migrations no workflow, prompt, test or command uses; update README.md, docs/architecture.md, docs/pipeline.md, site/README.md and code comments | 2 | standalone | open |
| W7-04 | W7 | tools/source_candidates.py: keep (operator command in docs/operating.md), fix its docstring pointer to the removed tools/check_brief.py | 1 | standalone | open |
| W7-05 | W7 | content_model.ENTRY_DEFAULTS `update_of: None` default for a retired field (check_run known-field list derives from it; the FAIL guard stays) | 1 | standalone | open |
| W7-06 | W7 | Stale docs: README.md tree and '/live/' line, site/README.md horizon lines and migrate_briefs consumer, docs/architecture.md state list and migration pointer, docs/pipeline.md state list | 6 | standalone | open |
| W7-07 | W7 | Committed junk under work/ the .gitignore negation lets through (2 __pycache__ .pyc, 5 *.ended_at.tmp, 4 .log, cisa-kev-full.json) and the ignore rules that admit it | 12 | standalone | open |
| W7-08 | W7 | work/ directories older than 60 days (143, about 112 MB): only check_run's url-liveness ledger glob (no age bound) and this inventory read them; bound the glob, then remove them from the tree (after W3, which reads 5 old audit plans) | 143 | 10 | open |
| W7-09 | W7 | site/assets/vendor marked.min.js and purify.min.js are never loaded (hash-checked only): remove with their HASHES rows | 2 | standalone | open |
| W7-10 | W7 | site/assets/js/spa-redirect.js still routes #/weekly to the removed weekly/ page | 1 | standalone | open |
| W7-11 | W7 | Root .nojekyll is read by nothing (the build writes its own into the deploy) | 1 | standalone | open |
| W7-12 | W7 | /live/ redirect stub in site/build.py | 1 | declined | declined: operator-documented legacy redirect |
| W7-13 | W7 | Tool tests (test_entry_record, test_check_run, test_source_health, test_fetch_source_pdf) are run by no workflow or gate: wire them into check_run.py's build-side smoke tests | 4 | standalone | open |
| W1-G | W1 | Reference-branch tool hunk (_page_skeletons) and registry hunk (Eurail): ported as W7-02 and W5-01 | 2 | 01 | open |
| C9 | C9 | Retirement: remove § Secondary work, tools/legacy_review.py, state/legacy_review.json; banner; memory note; final report; delete the reference branch | 1 | 10 | open |

## Log

- 2026-10-20: § C0 bootstrap by the coordinator session (inventory: main agent plus one `Explore` spawn, `explore-1`, counted in wave 01's budget).
