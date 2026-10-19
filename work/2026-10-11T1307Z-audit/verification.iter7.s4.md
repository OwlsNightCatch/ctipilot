**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-19T18:09:14Z · ended_at=2026-10-19T18:33:51Z · duration_seconds=1477

## Verification report: 2026-10-11T1307Z-audit (iteration 7, slice s4, plus the fire's own documents)

Scope: 26 entries, 183 ledger claims, all answered in `verification.iter7.s4.claims.yaml` (183 ok; both findings below sit in text the ledger does not carry; the one claim changed since iteration 6, GitLab `actions[0]`, was re-read against watchTowr and the GitLab release notes and holds). Every cited page was fetched this pass (fresh fetches, no cached gate bodies reused): MSRC update-guide pages through the MSRC SUG API, NCSC-CH posts through `ncsc-csh post`, FortiGuard PSIRT through the raw page for the CVSS and "Known Exploited" header fields, CVE records through cveawg.mitre.org, the FBI/USSS advisory through `pdf`, the CloudSEK victim chart as an image. All 26 entries were read whole.

### Citation does not support the claim (F3)
- **#1 GitLab CVE-2026-85706, 2026-09-16 section and sources[] record** (low confidence): "linking a public working proof-of-concept published the same day ([guneykabel, 2026-09-15])". The cited repository page's JSON says `"createdAt":"2026-09-11T15:24:22.000Z"`, so the PoC repository predates NCSC-CH's 2026-09-15 link by four days; the source record date 2026-09-15 drifts four days from the page. Older text, not in this fire's diff.

### Claims missing inline citation (F5)
- **#2 FortiBleed, Update 2026-10-08 final sentence** (low confidence): "On the FortiGate itself, the administrator accounts, passwords and REST API keys the advisory says to review are recorded in the device's configuration and administrator audit log, which is where an unexpected change shows." No citation, no analyst marker. `git diff HEAD` shows this fire wrote it (it replaced a cited sentence), and this fire's Correction calls the mapping "a reading of the advisory, not part of it". Neither the FBI/USSS PDF nor Fortinet's blog says where these changes are logged. The iteration-6 decline ("an earlier fire's section outside this fire's changes") fails against the diff.

### Editorial / less-is-more flags (advisory, F11)
- **#3 SonicWall SMA1000**: summary clause "no fix exists short of upgrading" (tautological; reads as "no workaround", which SNWLID-2026-0016 and the outlets do not state) and "the headline here" in the Correction.
- **#4 Sector tags** (FortiSandbox, SonicWall, Check Point) beyond public-sector appear on no cited page.
- **#5 Austria NISG** Improvement section duplicates the takeaway this record adds; **Virtualizor** Correction asserts the estate fact unsourced.
- **#6 OpenAI agents/UNCTAD** reproduces attacker marker strings `CHATGPTTEST1`, `OAI_META_1312`.

### Prior-iteration deltas, one by one (deltas.iter7.s4.yaml, 17 rows)
| Delta | Result |
|---|---|
| F11 em dashes (nginx, WinRAR, SAP, FortiSandbox, FortiBleed, OpenAI/Medicare, ChainDrop, Mandiant, Liechtenstein, PeopleSoft, Cisco ISE) | Declined as style-only. Rationale holds: `prompts/cti-run.md` says "The site strips any that survive, so an em dash in an entry is a silent style defect, never a reader-visible one." Not re-raised. |
| F11 priority narration (G7 warning, Virtualizor) | Declined; carried as advisory #5 for Virtualizor (the estate sentence is unsourced). The G7 entry is another slice's. |
| F11 sector tags (SAP, FortiSandbox, SonicWall, Check Point) | Declined as profile call; holds for public-sector only. Carried as advisory #4. |
| F11 SonicWall "no workaround" wording | Declined; I could not confirm the clause is wrong, only unsupported as a workaround claim. Carried as advisory #3. |
| F11 file-name/marker strings (FortiClient EMS, OpenAI/UNCTAD) | Declined; OpenAI markers are the researcher's published labels in older text. Carried as advisory #6. FortiClient is another slice's. |
| F11 FortiBleed audit-log sentence | Decline rationale fails (the diff shows this fire wrote it). Now F5 #2. |
| F11 em dashes in multiple entries | Declined; rationale holds (above). |
| F3 Exchange side-effects clause | Fixed and correct: the May post lists the known issues; the July FAQ ties their clearing to "when July 2026 SU is installed and mitigation is removed"; no "indefinitely". |
| F5 Exchange rollback sentence | Fixed: it now cites the July post, which says "Installing the July 2026 update does not automatically remove already applied CVE-2026-42897 mitigations ... Remove the mitigation M2.1.0 IIS rules ... Roll back the mitigation". |
| F4 Exchange Proofpoint hedge | Fixed: Proofpoint's "the same sized, invisible pop-up" and "highly similar error-handling" are kept. |
| F4 Exchange NCSC-CH | Fixed: the NCSC-CH post's own "Update 30.07" is only a Proofpoint link. |
| F11 Exchange evidence quote underscores | Fixed: the quote is a verbatim substring of the July post. |
| F4 GitLab action ("CI/CD credentials") | Fixed and correct: the action now reads "configuration files, secrets or other sensitive server-side data", which is watchTowr's wording; the backport and CVE-2026-88765 statements match the 19.0.9 and 19.3.2 notes ("These versions contain no other changes"). |
| F11 Austria improvement duplicates the takeaway | Declined; advisory #5. |
| F4 audit report candidate-source list | Resolved: section 8 lists seven candidates (UK AISI blog, veeam-kb, hashicorp, Apache httpd, solutions-numeriques, leto-legal-news, presseportal-ch); the G findings files hold exactly these seven new publishers (netzwoche in G2a is a recipe addition for an existing record, not a source). |
| F11 Exchange Pwn2Own/RoguePlanet/PHP SOAP/n8n priority sections | Other slices' entries; not read here. |

### Fire documents against disk (verified true)
- Run record: 17 sub-agents, all Sonnet 5.5; truth passes 10+14+0+1+3+1+6+0 = 35 clean, 84 imprecision, 14 error over 133 entries; L1 0/0/20; D1+D2 0/3/40 over 43; 196 total; urls_checked sums to 889; G ledgers 25, 32, 26, 26, 27, 36; dropped leads 17+18+13+9+12 = 69. `updated_entry_ids` 117 equals the disk set (102 corrections, 13 improvements, 2 updates, 25 internal; no entry has two records from this fire); 27 `merged_from` ids into 21 survivors, none of the 27 files exists; iteration finding counts 1-6 equal the iteration files (iter 6: 19/8/20 recomputed from the four findings files).
- Calibration table recomputed from commit 430fbdf: store 997 = 30/408/540/19, August 196 (1/96/98/1), September 128 (13/36/66/13), October 34 (2/6/23/3). The 15 September-October criticals are all exploited or KEV-listed, with two Check Point, two JFrog and three Cisco entries as the report lists.
- `sources.json`: 13 changed records exactly as listed; no additions or removals. Registry: +22 entities (20 products plus `malware:needymantis`, `actor:storm-3069`), 11 `first_seen` moves, four summaries, DAEMON Tools relations. `cves_seen`: +CVE-2026-55008, five refreshed. Legacy queue 408 pending, 69 reviewed. Warning ledger: 24 entries (23 plus the 363056 s acknowledgment).
- CHANGELOG 4.20 against `git diff HEAD`: banners v4.20 in both master prompts, `LAST_AUDIT` loop and partial-audit list, duplicate guard, step 5b clause removal, `docs/architecture.md`, `_page_skeletons` meta-description keep, `_pdf_streams` image-stream skip (DCT/JPX/CCITT/JBIG2 plus the abbreviations DCT and CCF, `/Subtype /Image`, 85 % printable of the first 64 KB), new test; `tools/test_fetch_source_pdf.py` 14/14 pass.
- `check_run.py --pre-verify`: one FAIL (run-clock, expected, filled after the loop) and one WARN (entry-run-binding, the Citrix record dated 2026-10-19 described in the brief); nothing else.

### Considered, no finding
Em dashes (declined class, rationale holds); the Check Point CVE-2026-50751 entry still at `critical` four months on (the audit's monthly calibration owns it and this fire did not touch priority); Gambit page JSON-LD date 2026-10-08 against the visible dateline "September 22, 2026" used by the CLOSEDQUORUM citation (the visible dateline matches); heise's Plugin4Shell update note carries no date, so "By 2026-09-30" is a bound, not contradicted; SonicWall advisory "updated 2026-09-01" cannot be read from the JS-shell advisory page (SecurityWeek and BleepingComputer say published "Tuesday", which is 2026-09-01); CloudSEK victim chart (read as an image): 22 victims, ten named countries, six unknown, matching the sourcing note.

### Verdict
NEEDS_FIXES (truth: 1, editorial: 1, advisory: 4). Both non-advisory findings are low confidence and one-sentence fixes; the F3 sits in text this fire did not change.

Findings: `verification.iter7.s4.findings.yaml`; claim verdicts: `verification.iter7.s4.claims.yaml`.
