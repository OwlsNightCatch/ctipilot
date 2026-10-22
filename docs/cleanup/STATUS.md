# Store cleanup tracker

Program: [`prompts/cleanup-coordinator.md`](../../prompts/cleanup-coordinator.md). Machine-readable plan with every row's entry ids: [`work/cleanup/plan.json`](../../work/cleanup/plan.json); this file is rendered from it (`python3 work/cleanup/render_status.py`). Inventory: `python3 work/cleanup/inventory.py`. Each cleanup session takes the next wave, updates the rows it touched in plan.json, re-renders, and names the next wave below.

**Next wave:** Waves 02, 03 and 04 are done. In flight: 05 (lane C). Ready now, one session each and in parallel: 06, 07, 08, 09 and 10 (kickoff lines in work/cleanup/wave-<NN>/HANDOVER.md; 09 takes lane A, freed by wave 03, and 10 takes lane B, freed by wave 04). Planned: 12 (twins and links found by waves 03 and 04; waits for 05) and 11 (W7-08, W7-17, C9 retirement), which is last. Earliest start: any time, except Saturday 18:00Z until the Sunday audit's record lands on main.

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
| Entries in the store | 996 | 1006 |
| Legacy queue pending | 408 | 308 |
| 2026-10-18 out-of-week verdicts not yet applied (factual error / imprecision / clean) | 77 / 63 / 42 (182 rows, 25 on entries since folded) | 61 / 6 / 37 (wave 01 closed W1-A's 16 factual-error rows, wave 02 W1-B's 57 imprecision and W1-C's 5 clean rows) |
| Never-verified non-legacy entries (W3) | 71 | 71 |
| Known duplicate groups open (W4) | 4 + scan | W4-01, W4-03 to W4-05 done (wave 03); open: W4-02, W4-06 to W4-11 |
| Registry orphans (no entry key, no relation) | 179 non-product + 4 product | 183, none a duplicate (W5-04, W5-05) |
| check_run.py --all | 0 fail, 1 warn, 25 acknowledged | 0 fail, 0 warn, 26 acknowledged |
| Rows done / declined / in a wave / open | 69 rows | 36 / 2 / 1 / 30 |

## Waves

Waves marked `ready` can start now, each in its own session and in parallel; `after` names the waves that must be done first (`python3 work/cleanup/render_status.py --check-lanes` proves the ready and in-flight waves share no entry).

| Wave | Lane | Rows | After | Status |
|---|---|---|---|---|
| 01 | - | W7-01, W7-02, W6-04, W1-A (16 entries); standalone W5/W6/W7 rows shipped during it | - | done 2026-10-20T0835Z-audit: 5 verifier iterations, residual 1, 8 of 20 spawns |
| 02 | - | W1-B (57), W1-C (5), W1-E (34 items), W1-F (8), W1-H; inputs in work/cleanup/wave-02/ | - | done 2026-10-21T0800Z-audit: 8 verifier iterations (cap, fail-open), residual 2, 72 records on 85 entries, 18 legacy entries reviewed, 19 of 20 spawns |
| 03 | A | W4-01, W4-03, W4-04, W4-05, W1-D (33 entries); inputs in work/cleanup/wave-03/ | - | done 2026-10-21T1149Z-audit: 23 records, 1 fold, 4 links, 6 new W4 rows; 8 verifier iterations (cap), residual 4, 17 of 20 spawns |
| 04 | B | W2-01 (76 legacy entries) | - | done 2026-10-21T1148Z-audit: 74 records on W2-01 (68 corrections, 6 improvements), 1 fold closing W4-09, 11 new rows; 2 verifier iterations, budget cut at 20 of 20 spawns, residual 12 |
| 05 | C | W2-02 (76 legacy entries) | - | in-flight 2026-10-21T1147Z-audit |
| 06 | - | W4-02, W1-D2 (10 entries), W1-I (45 worker residuals and 7 verifier advisories), W4-15 (wave 04) | 02 | ready |
| 07 | - | W2-03 (77 legacy entries), W4-13 (wave 04) | 02 | ready |
| 08 | - | W2-04 (76 legacy entries), W4-06 (2) | 02 | ready |
| 09 | A | W2-05 (76 legacy entries), W4-17 (wave 04) | - | ready |
| 10 | B | W3-01 (71), W6-05 (4 entry-scoped acknowledgments) | - | ready |
| 11 | - | W7-08, W7-17, C9 retirement | 03, 04, 05, 06, 07, 08, 09, 10, 12 | planned |
| 12 | - | W4-07, W4-08, W4-09, W4-10, W4-11 (twins and a missing link found by wave 03 across waves 02, 03, 04 and 05); W4-12, W4-14, W4-16, W5-08 (wave 04) | 04, 05 | planned |

W5, W6 and W7 rows marked `standalone` ship as small merges of their own between waves, the moment they are green. Inputs prepared for a wave live under `work/cleanup/wave-<NN>/`.

## Rows

| Row | WS | Item | Size | Wave | Status |
|---|---|---|---|---|---|
| W7-01 | W7 | tools/entry_record.py: tested record tool (add / amend / diff), CLAUDE.md Key commands row | 1 | 01 | done 2026-10-20T0835Z-audit (commit 6c75002) |
| W7-02 | W7 | Gate false positives: _page_text (extract skips the tag stripper, description metas kept, 'opens in a new window' labels removed, cache header dropped), image-only PDF unreadable for citation-cve and quote-literal; tools/test_check_run.py | 1 | 01 | done 2026-10-20T0835Z-audit (commit 4ca3e3b) |
| W6-04 | W6 | Acknowledge the one open WARN: 2026-10-18T1307Z-audit duration_seconds=117266 (settled history, the fire spanned the v4.21 pause) | 1 | 01 | done 2026-10-20T0835Z-audit |
| W1-A | W1 | Non-legacy-batch factual errors, passes T1-T9 (2 of them legacy-pending: mark reviewed after repair) | 16 | 01 | done 2026-10-20T0835Z-audit: 13 records (9 corrections, 3 updates, 1 improvement); Kairos Libercourt, Bitget and Apple CoreGraphics already fixed by 2026-10-11T1307Z-audit |
| W1-B | W1 | Imprecisions, passes T1-T9 (13 legacy-pending: mark reviewed after repair, add rating and mapping) | 57 | 02 | done 2026-10-21T0800Z-audit: 50 of 57 entries carry a record, 7 needed none (already fixed by 2026-10-11T1307Z-audit, or declined with reason); 13 legacy entries reviewed |
| W1-C | W1 | Clean verdicts on legacy-pending entries, passes T4/T5: mark reviewed after the rating and mapping their kind requires | 5 | 02 | done 2026-10-21T0800Z-audit: 5 improvement records (labelled lines and mapping); left the legacy queue |
| W1-E | W1 | Carried residuals and (pre-existing) advisories, audits 2026-09-27 to 10-18 (labelled lines on RoguePlanet 07-09 and SAP 08-12, LiteLLM affected_products, OpenAI agents marker strings, WinRAR/Splunk event_date, PHP SOAP CVE-2026-7262 score, ShinyHunters PeopleSoft action scope and 'external', Instructure uncited source, Acronis JSON primary, Exchange 10-14 10-16 section citation, Ivanti 10-14 25.1.3.0 framing; em dashes fixed wherever a wave writes a record, else declined: stripped at render); plus the VWBP untranslated German evidence quotes, the TeamCity Triage line and the UNCTAD Triage examples (wave 01 residuals). Wave 01 applied the UNCTAD marker-string item and declined the Acronis JSON-primary item (the readable advisory page is an empty script shell). Input: work/cleanup/wave-02/findings-W1-E.yaml (34 items) | 26 | 02 | done 2026-10-21T0800Z-audit: 19 of its 26 entries carry a record (Virtualizor's only for its W1-B findings, its W1-E item stays declined), 7 none; every item applied or declined with reason in docs/audits/2026-10-21-cleanup-wave-02.md |
| W1-F | W1 | Portable reference-branch entry hunks (re-derive on main, re-verify, re-record) | 8 | 02 | done 2026-10-21T0800Z-audit: all 8 hunks re-derived and re-verified on main, folded into each entry's wave 02 record |
| W1-D | W1 | Duplicate and legacy batch verdicts (D1-D3, L) on entries the 2026-10-11 audit corrected after the pass read them: re-derive each defect on the current text (25 rows were folded, their defects re-checked on the survivor) | 33 | 03 | done 2026-10-21T1149Z-audit: 21 records (2 updates, 5 corrections, 14 improvements); 12 entries already fixed by 2026-10-11T1307Z-audit |
| W1-D2 | W1 | W1-D verdicts on the entries wave 02 also changed, and on the 2026-06-19 RoguePlanet entry that the W4-02 fold takes: re-derive each defect on the current text (input: work/cleanup/wave-03/findings-W1-D-and-groups.yaml, these entries only) | 10 | 06 | open |
| W4-01 | W4 | YellowKey 2026-05-15 vs Nightmare Eclipse 2026-05-30: distinct findings sharing CVE-2026-45585, link through references[]; Nightmare Eclipse re-verified and rewritten (watch item) | 2 | 03 | done 2026-10-21T1149Z-audit: linked (Nightmare Eclipse references YellowKey, CVE-2026-45585 record corrected); both rewritten, both fixed 2026-06-09 |
| W4-02 | W4 | RoguePlanet 2026-06-19 vs 2026-07-09: same finding, fold into 2026-07-09 (ShieldBreak 2026-08-12 stays distinct) | 2 | 06 | open |
| W4-03 | W4 | Ghost CMS 2026-05-25: the ClickFix deep dive and the 'large-scale ClickFix campaign' entry are the same finding per D3; decide fold | 2 | 03 | done 2026-10-21T1149Z-audit: 2026-05-25 large-scale ClickFix entry folded into the Ghost CMS CVE-2026-26980 ClickFix entry with its verified facts |
| W4-04 | W4 | Pwn2Own Berlin 2026 roundup 2026-05-17 vs the DEVCORE Exchange chain entry: re-verify the roundup, then fold or link | 2 | 03 | done 2026-10-21T1149Z-audit: linked (the DEVCORE entry lists the roundup); roundup rewritten from ZDI's pages, refiled as routine research |
| W4-05 | W4 | Store-wide non-CVE twin scan (same entity and similar title or same primary URL, no references[] link); fold or link each pair found | TBD | 03 | done 2026-10-21T1149Z-audit: 118 candidate pairs in two passes; Adobe APSB26-120 linked to APSB26-114; four twin pairs on other rows became W4-06 to W4-09 |
| W4-06 | W4 | The Gentlemen ransomware 2026-06-12 vs 2026-06-27: same finding (one group profile, the later entry adds Check Point's Swiss victim share via inside-it.ch); fold 2026-06-27 into 2026-06-12, carrying its verified facts (found by the W4-05 scan) | 2 | 08 | open |
| W4-07 | W4 | Calypso / Red Lamassu (Bronze Medley) Showboat and JFMBackdoor, two 2026-05-22 entries from the same four sources: same finding, fold one into the other (found by the W4-05 scan; the members sit in W2-01 and W2-02, in flight in waves 04 and 05) | 2 | 12 | open |
| W4-08 | W4 | 7-Eleven ShinyHunters breach 2026-05-19 vs the 2026-05-27 Charter and 7-Eleven entry: the later entry carries a 7-Eleven development (about 185,000 individuals) beside a separate victim; link 2026-05-27 to 2026-05-19 through references[] or move the 7-Eleven delta onto 2026-05-19 (found by the W4-05 scan; members in W2-01 and W2-02) | 2 | 12 | open |
| W4-09 | W4 | Drupal PSA-2026-05-18 twins, both 2026-05-20: 'Prepare emergency Drupal patch window' duplicates 'Drupal core highly critical pre-patch warning' (the survivor, with CVE-2026-9082 and two update records); fold unless wave 04 already folded them inside W2-01 | 2 | 12 | done 2026-10-21T1148Z-audit: the patch-window entry folded into the PSA-2026-05-18 entry |
| W4-10 | W4 | 2026-05-19 'Chaotic Eclipse Windows zero-days: MiniPlasma is third PoC' is an unfolded legacy 'UPDATE (originally covered 2026-05-15)' entry on the YellowKey thread (2026-05-15, re-verified by wave 03); fold it into 2026-05-15 or link it as the distinct MiniPlasma finding (now fixed through the 2026-06-09 re-release of CVE-2020-17103, which the entry lacks). Found by wave 03 repair-5; the entry sits in W2-01 (wave 04) | 2 | 12 | open |
| W4-11 | W4 | Fragnesia (2026-05-15, CVE-2026-46300) builds on Dirty Frag (2026-05-09): Red Hat's RHSB-2026-003 counts it in the Dirty Frag set and the Dirty Frag entry calls it tracked in its own entry, but the Fragnesia entry's references[] is empty; add 2026-05-09 Dirty Frag to it (an internal record). Found by wave 03's confirmation pass; the Fragnesia entry sat in W1-B (wave 02) | 1 | 12 | open |
| W2-01 | W2 | Legacy queue batch 1, oldest first (2026-05-10 to 2026-05-22) | 76 | 04 | done 2026-10-21T1148Z-audit |
| W2-02 | W2 | Legacy queue batch 2, oldest first (2026-05-22 to 2026-05-31) | 76 | 05 | in-wave 05 (2026-10-21T1147Z-audit) |
| W2-03 | W2 | Legacy queue batch 3, oldest first (2026-05-31 to 2026-06-10) | 77 | 07 | open |
| W2-04 | W2 | Legacy queue batch 4, oldest first (2026-06-10 to 2026-06-21) | 76 | 08 | open |
| W2-05 | W2 | Legacy queue batch 5, oldest first (2026-06-21 to 2026-07-03) | 76 | 09 | open |
| W3-01 | W3 | Entries no audit truth pass ever covered (not legacy, filed before the 2026-10-18 audit, not audit-published) | 71 | 10 | open |
| W5-01 | W5 | Eurail incident summary: drop the retracted 'Dutch DPA and EDPS are reviewing' claim (reference-branch registry hunk) | 1 | standalone | done 2026-10-20T0835Z-audit (commit 8678b51) |
| W5-02 | W5 | incident:daemon-tools-supply-chain-2026 'EU governments targeted' | 1 | done-before | done 2026-10-11T1307Z-audit |
| W5-03 | W5 | malware:beavertail summary 'an initial loader' (re-read the 2026-09-18 joint advisory) | 1 | standalone | done 2026-10-20T0835Z-audit (commit 8678b51; malware:invisibleferret corrected with it) |
| W5-04 | W5 | 179 non-product registry records keyed by no entry and in no relation: tombstone each that duplicates a canonical key (merged_into), leave the rest | 179 | standalone | done 2026-10-20T0835Z-audit: no orphan duplicates a live key (exact name/alias match, key-token and fuzzy-name checks); all 179 stay |
| W5-05 | W5 | 4 product records no entry's affected_products resolves to: tombstone onto the surviving product or leave | 4 | standalone | done 2026-10-20T0835Z-audit: no canonical twin for any of the 4 (Siemens Mendix Runtime, Unisoc T606, Unisoc T7250, Veeam Backup & Replication); keys are permanent, they stay |
| W5-06 | W5 | Relations whose source entry is gone: 0 on 2026-10-20; re-check after every fold wave | 0 | each wave | open |
| W6-01 | W6 | Red Canary (2026-10-11 rec. 5): record `redcanary` now points at the Zscaler blog, last success 2026-09-13: retire or repoint on the evidence | 1 | standalone | done 2026-10-20T0835Z-audit: repointed by 2026-10-20T0256Z-intel, decision noted (commit f5df6fe) |
| W6-02 | W6 | ssd-disclosure (rec. 6): candidate, fetch_method blocked on every transport: accept the gap or retire | 1 | standalone | done 2026-10-20T0835Z-audit: keep, the record reads again (commit f5df6fe) |
| W6-03 | W6 | google-tag vs mandiant-gtig overlap (rec. 7): fold google-tag into mandiant-gtig or keep both with a reason | 1 | standalone | done 2026-10-20T0835Z-audit: keep separate, distinct content (commit f5df6fe) |
| W6-05 | W6 | Four entry-scoped attack-mapping acknowledgments (research entries with empty techniques[]): entries are fixed through records, never acknowledged; map the tradecraft or justify and keep | 4 | 10 | open |
| W6-06 | W6 | state/coverage_backlog.md: trim the 98 struck rows surfaced before 2026-09-20 (over 30 days) | 98 | standalone | done 2026-10-20T0835Z-audit (commit f06331d) |
| W6-07 | W6 | Ack ledger rows matching nothing: 0 of 25 on 2026-10-20 (check_run ack-ledger PASS); re-check at C9 | 0 | each wave | open |
| W7-03 | W7 | Remove tools/migrate_briefs.py (2003 lines) and tools/migrate_updates.py (404 lines), one-time v2/v4 migrations no workflow, prompt, test or command uses; update README.md, docs/architecture.md, docs/pipeline.md, site/README.md and code comments | 2 | standalone | done 2026-10-20T0835Z-audit (commit bfded2c) |
| W7-04 | W7 | tools/source_candidates.py: keep (operator command in docs/operating.md), fix its docstring pointer to the removed tools/check_brief.py | 1 | standalone | done 2026-10-20T0835Z-audit (commit 7864387) |
| W7-05 | W7 | content_model.ENTRY_DEFAULTS `update_of: None` default for a retired field (check_run known-field list derives from it; the FAIL guard stays) | 1 | standalone | declined: 654 entries carry `update_of: null`; dropping the default would make the key unknown to the changelog-fields check on all of them (654 internal records for no reader value). The non-null FAIL guard stays. |
| W7-06 | W7 | Stale docs: README.md tree and '/live/' line, site/README.md horizon lines and migrate_briefs consumer, docs/architecture.md state list and migration pointer, docs/pipeline.md state list | 6 | standalone | done 2026-10-20T0835Z-audit (commit 7864387) |
| W7-07 | W7 | Committed junk under work/ the .gitignore negation lets through (2 __pycache__ .pyc, 5 *.ended_at.tmp, 4 .log, cisa-kev-full.json) and the ignore rules that admit it | 12 | standalone | done 2026-10-20T0835Z-audit (commit f06331d) |
| W7-08 | W7 | work/ directories older than 60 days (143, about 112 MB): only check_run's url-liveness ledger glob (no age bound) and this inventory read them; bound the glob, then remove them from the tree (after W3, which reads 5 old audit plans) | 143 | 11 | open |
| W7-09 | W7 | site/assets/vendor marked.min.js and purify.min.js are never loaded (hash-checked only): remove with their HASHES rows | 2 | standalone | done 2026-10-20T0835Z-audit (commit 11ff607) |
| W7-10 | W7 | site/assets/js/spa-redirect.js still routes #/weekly to the removed weekly/ page | 1 | standalone | done 2026-10-20T0835Z-audit (commit 11ff607) |
| W7-11 | W7 | Root .nojekyll is read by nothing (the build writes its own into the deploy) | 1 | standalone | done 2026-10-20T0835Z-audit (commit 11ff607) |
| W7-12 | W7 | /live/ redirect stub in site/build.py | 1 | declined | declined: operator-documented legacy redirect |
| W7-13 | W7 | Tool tests (test_entry_record, test_check_run, test_source_health, test_fetch_source_pdf) are run by no workflow or gate: wire them into check_run.py's build-side smoke tests | 4 | standalone | done 2026-10-20T0835Z-audit (commit f037aa0) |
| W1-G | W1 | Reference-branch tool hunk (_page_skeletons) and registry hunk (Eurail): ported as W7-02 and W5-01 | 2 | 01 | done 2026-10-20T0835Z-audit: tool hunk as W7-02, registry hunk as W5-01 |
| C9 | C9 | Retirement: remove § Secondary work, tools/legacy_review.py, state/legacy_review.json; banner; memory note; final report; delete the reference branch | 1 | 11 | open |
| W1-H | W1 | Page-check lead: Drupal SA-CORE-2026-014 entry, an evidence quote not contiguous on drupal.org/sa-core-2026-014 and a CVE-2026-108097 clause citing a page without the id (found by the W7-02 smoke run); folded into W1-E's findings file | 1 | 02 | done 2026-10-21T0800Z-audit: entry correct, the lead was a gate false positive (drupal.org challenge page), fixed as W7-15 |
| W1-I | W1 | Residuals the wave 02 repair workers noticed outside their findings and left unfixed (headlines over 120 characters, non-canonical Detection labels, stale cves_seen titles, priority calibration on Check Point IKEv1, PeopleSoft and JFrog, retired update_of keys, sync_products.py --report writing the registry, and more); check each against its source, then fix or decline. Input: work/cleanup/wave-06/findings-W1-I.md | 52 | 06 | open |
| W7-14 | W7 | tools/claim_ledger.py: claims for sentences a fire edits inside earlier ## <Type> — <at> sections are not listed (the ledger takes this fire's own sections plus declared fields), so a post-fix verifier pass can miss them; list changed sentences of earlier sections against base.sha and add a test | 1 | standalone | done 2026-10-21T0800Z-audit (commit 731706f) |
| W7-15 | W7 | tools/check_run.py page checks: a bot-challenge interstitial (drupal.org 'Client Challenge', Cloudflare, Anubis) cleared the size floor and was compared as page text; treat it as unread, with a test | 1 | standalone | done 2026-10-21T0800Z-audit (commit 1f8d69e) |
| W7-16 | W7 | tools/entry_record.py add stops with 'frontmatter has no updates: key' on the 581 entries without one; make add insert the key itself, with a test | 1 | standalone | open |
| W7-17 | W7 | § C1 run-id collision: waves 03 and 05 both computed 2026-10-21T1147Z-audit in the same minute; add a uniqueness check (take the next free minute when work/<RUN_ID>/ exists on origin/main) to prompts/cleanup-coordinator.md | 1 | 11 | open |
| W4-12 | W4 | Tycoon 2FA after the March 2026 takedown, 2026-05-18 (OAuth device authorization) vs 2026-05-27 (two-tier AiTM operation): check whether they are one finding; fold or link through references[]. The 2026-05-18 member was re-verified by wave 04, the 2026-05-27 one sits in W2-02 (wave 05) | 2 | 12 | open |
| W4-13 | W4 | Datadog Security Labs on the leaked TeamPCP Shai-Hulud framework (2026-05-15) vs TeamPCP open-sourcing its Mini Shai-Hulud framework (2026-06-09): check whether the later entry is a development of the same finding; fold, link or leave. The 2026-05-15 member was re-verified by wave 04 | 2 | 07 | open |
| W4-14 | W4 | West Pharmaceutical Services 8-K Item 1.05 (2026-05-12) and its 8-K/A confirming full operational restoration (2026-05-22): one incident, the later filing a development of it; fold 2026-05-22 into 2026-05-12 carrying its verified facts. The 2026-05-12 member was re-verified by wave 04, the 2026-05-22 one sits in W2-02 (wave 05) | 2 | 12 | open |
| W4-15 | W4 | Link candidates (references[] only, internal records): Microsoft MDASH (2026-05-13), which Microsoft says found CVE-2026-41089 and CVE-2026-41096, and the 2026-05-13 entry covering those CVEs; the Grafana Labs CoinbaseCartel breach (2026-05-19) and the 2026-05-28 Nx Console / TanStack / Daemon Tools cascade entry, which says Grafana Labs traced its breach to the TanStack compromise. Check each against its sources before linking | 4 | 06 | open |
| W4-16 | W4 | Link candidate (references[] only): F5 BIG-IP/BIG-IQ iControl REST CVE-2026-41225 (2026-05-17) and the 2026-05-15 nginx / F5 WAF CVE-2026-42945 entry; SecurityWeek counts BIG-IP, BIG-IQ and NGINX fixes in one F5 notification, so link only if the two entries cover the same release | 2 | 12 | open |
| W4-17 | W4 | Link candidate (references[] only): CERT Polska's SzafirHost CVE-2026-44088 JAR/ZIP polyglot (2026-05-17) and CERT Polska's 2026-06-30 JAR parser confusion RCE (CVE-2026-13165) in the same product, a different flaw; link the later entry to the earlier one if its sources build on it | 2 | 09 | open |
| W5-07 | W5 | actor:webworm-fishmonger-aquatic-panda-eset-echocreep-graphworm-eu lists FishMonger, Aquatic Panda, SixLittleMonkeys and Space Pirates as aliases, which ESET (2026-05-20) treats as related or tenuously linked groups, not other names; campaign:fishmonger-isoon-sprysocks-windows-kernel-rootkit is attributed-to Webworm (source 2026-06-17/fishmonger-i-soon-ports-its-sprysocks-backdoor-to-windows-wi) only through that alias. Move the aliases to typed relations (related-to / overlaps-with) where a source states them and re-key the FishMonger edge | 1 | standalone | open |
| W5-08 | W5 | Registry summaries wave 04 found unsupported on records keyed by entries of other waves: actor:kimsuky (HTTPSpy RAT and European targets, check against 2026-05-30/kimsuky-velvet-chollima-deploys-httpspy-rat-and-rust-based-h); campaign:nightmare-eclipse-microsoft-dcu-threat-greenplasma-miniplasmaaac (MiniPlasma 'the third PoC', no June 2026 CVE-2020-17103 fix); actor:akira ('edge-device CVE chains and intermittent-encryption EDR evasion' is unsourced, CISA AA24-109A gives VPN access through known CVEs and full or partial encryption); campaign:clickfix-macos-2026 ('expands to macOS ... bypass Gatekeeper': per Microsoft 2026-05-06 the campaign shifted from disk images to ClickFix Terminal commands) | 1 | 12 | open |
| W5-09 | W5 | incident:drupal-core-highly-critical-pre-patch-warning-psa-2026-05-18 is keyed by no entry and its summary says no CVE at announcement (CVE-2026-9082 since); wave 04 folded the Drupal twin into 2026-05-20/drupal-core-highly-critical-pre-patch-warning-unauthenticate. Fix the summary and key it from the survivor, or tombstone it if it duplicates a live key | 1 | standalone | open |
| W6-08 | W6 | Coverage gap: CVE-2026-41940 (cPanel & WHM authentication bypass, CISA KEV since 2026-04-30 with known ransomware use) has no entry of its own; the 2026-05-10 cPanel entry mentions it in passing. Research it from cPanel's advisory and the KEV record and publish it, or record why it does not clear the gate | 1 | standalone | open |
| W7-18 | W7 | Operator decision: law-enforcement entries without attacker TTP content (2026-05-16 BKA Dream Market arrest, kind threat, a laundering indictment) cannot meet the threat/incident attack-mapping gate honestly; wave 04 kept T1597.002 (the market sold stolen personal data) as the only sourced behavior. Decide on a kind or a gate rule for such entries | 1 | standalone | open |

## Log

- 2026-10-20: § C0 bootstrap by the coordinator session (inventory: main agent plus one Explore spawn, explore-1, counted in wave 01's budget); tracker and plan landed on main as 0f2be64.
- 2026-10-20: wave 01 (2026-10-20T0835Z-audit) claim landed; standalone merges W7-01, W7-02, W7-03, W6-06 with W7-07, W7-09 to W7-11, W7-04 with W7-06, W7-13, W6-01 to W6-03, W5-01 with W5-03.
- 2026-10-20: wave 01 (2026-10-20T0835Z-audit) applied W1-A (13 records, 3 declined as already fixed), acknowledged the one open warning, and prepared the inputs of waves 02 and 03; report docs/audits/2026-10-20-cleanup-wave-01.md.
- 2026-10-21: operator directive, waves run in parallel lanes (v4.23): wave 02's rows marked in flight on main, W1-D split (W1-D2 waits for wave 02), the W4 duplicate members moved out of the legacy batches, waves 03 to 05 ready in lanes A, B and C; merge_state.py merges plan.json, legacy_review.json and STATUS.md.
- 2026-10-21: lane fix: the 2026-06-19 RoguePlanet entry moved from W1-D (wave 03) to W1-D2 (wave 06), with the W4-02 fold that takes it.
- 2026-10-21: wave 05 (lane C) claimed by 2026-10-21T1147Z-audit.
- 2026-10-21: wave 04 (2026-10-21T1148Z-audit) claimed, lane B: W2-01 (76 legacy entries).
- 2026-10-21: wave 03 (2026-10-21T1149Z-audit) claim, lane A: rows W4-01, W4-03, W4-04, W4-05 and W1-D in flight (first claim attempt as 2026-10-21T1147Z-audit collided with wave 05's run id and was withdrawn).
- 2026-10-21: wave 03 (2026-10-21T1149Z-audit) done: W1-D, W4-01, W4-03, W4-04 and W4-05 closed (23 records, one fold, four links); new rows W4-06 to W4-11, W7-16, W7-17 and wave 12; wave 09 marked ready on lane A. Report docs/audits/2026-10-21-cleanup-wave-03.md.
- 2026-10-21: wave 02 (2026-10-21T0800Z-audit) claim landed; standalone merges W7-14 (claim ledger, 731706f) and W7-15 (challenge pages, 1f8d69e); 72 records on 85 entries (W1-B, W1-C, W1-E, W1-F, W1-H), 18 legacy entries reviewed (406 to 388 pending); report docs/audits/2026-10-21-cleanup-wave-02.md.
- 2026-10-22: wave 04 (2026-10-21T1148Z-audit) done: W2-01 closed (74 records, one fold that closes W4-09); new rows W4-12, W4-13, W4-14, W4-15, W4-16, W4-17, W5-07, W5-08, W5-09, W6-08, W7-18; notes on W4-07, W4-08 and W4-10; wave 10 marked ready on lane B. Report docs/audits/2026-10-21-cleanup-wave-04.md.
