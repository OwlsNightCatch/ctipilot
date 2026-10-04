**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** see `verify.iter4.s4.started_at` / `verify.iter4.s4.ended_at`

## Verification report — 2026-09-30T0639Z-audit (iteration 4, slice s4, post-fix pass)

Scope: 16 entries of `scope.iter1.s4.txt` (395 ledger claims, every one answered in `verification.iter4.s4.claims.yaml`: 388 ok, 3 F3, 3 F4, 1 F14), the run record, and the audit report `docs/audits/2026-09-30-correction-audit.md`. About 70 URLs read this pass (extract/url/pdf/ncsc-csh/WebFetch for the cisa.gov alert; jina fallback only where extract served the hub shell).

### Prior-iteration deltas (iteration 3, slice s4): each remediation re-fetched

| Item | Result |
|---|---|
| ABW title, headline, record summary, Correction carry "in some cases" | Confirmed; ABW PDF p.37: "By gaining access, in some cases, to industrial control systems, the attackers were able to alter the technical parameters of the equipment". Every earlier statement the Correction names is in `git show origin/main` (summary "Manual overrides prevented service disruption", 2026-05-09 APT28/APT29/UNC1151 and NIS2 text). |
| Kemp CVE-2026-33691 + dated Progress statement cited to THN; Correction/record summary without "no readable source" | Confirmed against THN 2026-06-30 ("Progress published its advisory on June 4 and says it has not received any reports of exploitation"; "CVE-2026-33691, a WAF bypass where whitespace padding in filenames could circumvent file upload extension checks"). |
| Kemp LTSF 7.2.54.18 in cves[].fixed, actions[0], main text with THN | Confirmed ("GA v7.2.63.2 and LTSF v7.2.54.18"). New finding on the headline (F11 below). |
| Kemp 9.8 (ZDI) / 9.6 (eSentire) attributed | Confirmed; ZDI-26-342 raw HTML "CVSS Score 9.8", eSentire "CVSS: 9.6". |
| FortiSandbox: no flat all-three exploitation claim; each position cited to its source | Confirmed; the three Fortinet pages show "Known Exploited No", HNS "the vendor has yet to confirm", kev.json lists CVE-2026-25089 and CVE-2026-39808 only. One new F3 on "5.2 is not affected" (FG-IR-26-100 has no 5.2 row). |
| FortiSandbox poc-public gone from status and tags, tags in record fields | Confirmed. |
| macOS: each branch cites its own Apple bulletin; 148171/148172 in sources[] | Confirmed (all three pages "Released August 6, 2026", CVE-2026-65400). |
| macOS: no "no benign explanation" outside the Correction's naming of it | Confirmed (grep). Huntress "suspicious indicator ... few administrators would both enable that user and use it". |
| macOS 2026-08-16 Detection limited to what NCSC-NL published | Confirmed against BleepingComputer. A neighbouring sentence in the same section still over-reads the same source (F4 below). |
| macOS evidence: three NCSC-NL items translated, Dutch in `original:` | Confirmed verbatim on advisories.ncsc.nl/2026/ncsc-2026-0280.html; translations faithful. |
| Eurail summary/title/event_date; body is cited paragraph + Contradiction + takeaway | Confirmed; summary no longer claims a regulator step beyond the Commission's EDPS statement; event_date 2026-04-09 = BleepingComputer date. Length residual re-listed as F7 (low confidence). |
| Gitea BSI evidence `original:` is a contiguous substring of the CSAF; release date and severity | Confirmed: the German summary is a verbatim substring of `wid-sec-w-2026-2027.json`; `initial_release_date 2026-06-21T22:00Z` (22 June local), `aggregate_severity hoch`. |
| Storm-3168 headline separates the two principals; Correction names the published headline | Confirmed against Microsoft ("One performed reconnaissance and resource discovery. The other performed discovery, destructive operations, and credential collection"). |
| Cisco ISE uncited deployment sentence gone; named in Correction and record summary | Confirmed (grep; sentence absent from main text). |
| Report Method line 26 of 36 / none for 10 | Confirmed: `findings.R1.yaml` 15 new + 11 existing + 10 none. |
| "48 of 54 CVE-sharing pairs" (report, CHANGELOG 4.19, quality-audit item 13) | Reproduced at origin/main: 54 pairs, 48 with no `references`/`merged_from`/`update_of` link either way. |
| Stale-exploitation row sources "NCSC-CH, NCSC-NL, eSentire and CISA" | Confirmed per entry (Gitea/ServiceNow NCSC-CH, macOS NCSC-NL, Kemp eSentire, KEV flags). |
| Tools bullet (claim_ledger.py, new entry-shape WARN) and its documentation | Confirmed in tools diff and docs/pipeline.md:1178, prompts/CHANGELOG.md. |
| `sources_changed` two sources | Confirmed: sources.json diff changes `anssi-fr` (2026-09-29 to 2026-09-30) and `fortinet-psirt` (null to 2026-09-30); `cisa-kev` and `helpnetsecurity` already read 2026-09-30 at origin/main. |
| ABW row "in some cases"; FortiSandbox row (Defused vs Fortinet) | Confirmed. |
| Die Linke text in report and run record | Run record and aggregator warning text hold; one report-row wording issue (F4 below). |

### v4.18 / v4.19 marker check

`grep v4.18` over CLAUDE.md, docs, prompts, tools, site, `.claude`: every remaining "v4.18" belongs to the parallel run's WebFetch release (CLAUDE.md:58, prompts/cti-run.md:937, `.claude/agents/cti-research.md`, `.claude/memory/source-fetch-blocks.md`, `tools/fetch_source.py`, `tools/source_health.py`, `site/build.py:8164`, CHANGELOG `## 4.18`), and the diff removes no 4.18 text other than the two prompt banners now at v4.19. The run record's `prompt_version` is v4.19. Residual: three comments for this run's fold feature say "v4.17" (F11).

### Citation does not support the claim (F3)

1. `2026-05-08/pro-russian-hacktivists-modify-ot-pump-settings-at-five-poli` (low confidence): citations `[ABW, 2026-05-06](.../InternalSecurityAgencyABW2024-2025Selectedactvities.pdf)`, `sources[].date`, `event_date` and the Update section's "published 2026-05-06". ABW's news page lists the Polish PDF as "06.05.2026" and the English PDF cited as "(pdf, 11.04 MB, 25.05.2026)"; PDF CreationDate 2026-05-22. Date the English edition 2026-05-25 or cite the Polish edition/news page for 05-06.
2. `2026-06-12/cve-2026-25089-fortinet-...` (low confidence): "(5.0.6 or 4.4.9 fixes all three, 5.2 is not affected)" cited to FG-IR-26-141, -112 and -100, plus actions[0] "(or move to 5.2) ... fixes all three" and the summary. FG-IR-26-100 lists only "FortiSandbox 5.0 Not affected" and 4.4.0-4.4.8; it has no 5.2 row.

### Unsupported / hallucinated facts (F4)

3. `2026-07-29/cve-2026-0769-langflow-...` (low confidence): "Two identifiers differing in the final digit" and the headline's "one digit away". CVE-2026-0769 vs CVE-2026-0770 differ in the last two digits.
4. `2026-09-04/cve-2026-85046-chrome-...` (low confidence): Correction "a CVSS 8.8 score that no cited source supports" and record summary "no cited source carries". origin/main sources[] cited the CISA-ADP record via NVD/MITRE API URLs and the body attributed the 8.8 to "CISA's ADP Vulnrichment"; the NVD API carries a CISA-ADP `cvssMetricV31` 8.8. The score was real and sourced to a record the store may not cite.
5. `2026-08-08/cve-2026-65400-macos-...` (low confidence): 2026-08-16 section "The observed outcome is cryptomining, not data theft or ransomware". BleepingComputer: "NSCS has not shared any details ... if they extend beyond cryptocurrency mining".
6. `docs/audits/2026-09-30-correction-audit.md`, Die Linke row (low confidence): "cannot yet say whether data was stolen". The party: "Ob und in welchem Umfang dies gelingt oder bereits erfolgt ist, lässt sich nicht beurteilen" (publication of the targeted data), member data not obtained; Heise "which internal data has been compromised". The entry's record summary deliberately moved away from the data-stolen wording.

### Quantifier without source (F14)

7. `2026-06-16/cve-2026-48611-...phpbb...` (low confidence): headline "only phpBB 3.3.17 fixes it"; Aikido says 4.0.0-a2 users go to `master` and "no safe 4.x release yet".

### Needs more research (F8)

8. `2026-09-04/cve-2026-85046-chrome-...` (low confidence): Detection says "Google withholds exploit specifics, so the generic tell available is ..." while the entry now cites Proofpoint, which describes the broker process running a default `curl` download-and-execute and "multiple high-signal detection opportunities".

### Drop (F7)

9. `2026-05-08/eurail-breach-...` (low confidence, previously raised and partly remediated): four sentences remain on a routine incident with no vector or actor. Acceptable if the operator accepts the length.

### Editorial / less-is-more flags (advisory, F11)

Cisco ISE Update "CERT-FR ... states that Cisco reports only CVE-2026-76460" (CERT-FR does not say only); FortiSandbox "this week's emergency change"; Kemp headline names only the GA build; Storm-3168 and Eurail Corrections do not name two changed statements each; fold feature labelled v4.17 in `tools/fold_entries.py:2`, `site/content_model.py:1103`, `tools/check_run.py`; stale `site/assets/js/brief.js:18-19` comment ("spans at least the 7-day alerts window") after the revert the report claims; `polyfill[.]io` still defanged in `entries/2026-06-07/hijacked-polyfill-io-domain-...` against the Mandate's "every defanged indicator"; Langflow `sourcing_note` is analysis, not two sentences of provenance; phpBB "never checks the password" drops the non-empty requirement.

### Report and run-record checks that held

Counts and states verified on disk: 75 entries with a record from this run and `updated_entry_ids` match; 966 entries at origin/main, 478 migrated, 963 after the three folds; 7 legacy entries reviewed and 468 pending in `state/legacy_review.json`; 36 banned citations in 30 entries (24 repaired, 4 removed with the folded duplicates, 8 on seven entries remain); 8 Cisco ISE CVEs added to `cves_seen.json`; coverage backlog 26 to 15 open rows (net +4 from the 0404Z fire); 3 registry product keys; `kev-window.txt` leaves only PAN-OS CVE-2026-0257; TeamCity KEV ransomware flag Unknown in the 2026-09-18 snapshot, Known in kev.json; iteration 1 raised 150 truth and 87 editorial findings; the parallel run 0634Z touched no common entry; the 0404Z fire committed at 06:44 to 06:50 after this run's 06:39 start. Not raised, as instructed: the priority and record-type counts (current disk: 36 priority changes = 23 high to notable, 2 high to routine, 11 notable to routine; the run record's notes still say "30", the report "35"), `completed`, `duration_seconds`, the verification block, and the absent `build-timing.txt`.

### Missed angles

None found for this slice; the KEV window shows 19 additions since 2026-09-16 and 0 uncovered.

### Verdict

NEEDS_FIXES (truth: 7, editorial: 2, advisory: 9). Every truth item is low confidence; none is a hallucinated headline fact. Findings YAML: `work/2026-09-30T0639Z-audit/verification.iter4.s4.findings.yaml`.
