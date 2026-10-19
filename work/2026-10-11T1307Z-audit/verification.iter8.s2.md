**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-19T18:42:44Z · ended_at=2026-10-19T18:59:29Z · duration_seconds=1005

## Verification report — 2026-10-11T1307Z-audit (iteration 8, slice s2)

Scope: 27 entries (`verify-scope.iter8.s2.txt`), 292 ledger claims, all answered in `verification.iter8.s2.claims.yaml` (291 ok, 1 F4). Post-fix pass: every ledger claim was walked, not a sample; the four changed claims (824cf3b4f8, 32d7aef1a2, d3837f49a8, 7a2286447a) and every claim of the remediated entries (DAEMON Tools, Patch Tuesday/Netlogon, Everest Forms, ShieldBreak, GitLab) were checked first. Every entry was read whole (frontmatter, analysis, labelled lines, every changelog section) with `git diff HEAD` for this fire's change. About 100 cited pages were fetched this iteration: `extract` for pages, `url` for raw HTML and the GitHub API (PoC repository, GHSA CVSS vector, GLPI advisory), `pdf` for the IC3 joint advisory, `ncsc-csh post` for hub posts 12622 and 12985 and cached hub JSON for 12575, 12615, 12935, `cisa-kev` for the catalogue (KEV rows for CVE-2026-0300, -50751, -85046, -85706, -86950, forensicTriage flags), api.first.org for the CVE-2026-86950 EPSS value, MSRC pages for CVE-2026-41089, -50656, -62911, -69414 (read via `extract`). No `WebFetch` or `jina` call was needed.

### Deltas from iteration 7

| Prior finding | Remediation | Result |
|---|---|---|
| Exchange F11 (sourcing_note length, "see body") | Declined | Rationale ("an earlier fire's note, length is style") does not meet the two-sentence standard; re-raised as advisory F11 #1. |
| Conference phishing F11 (Correction overstates; sourcing_note) | Declined | Rationale holds for the title hedge, but the record summary still says the title "no longer present[s] the campaign as conference-targeted"; kept as advisory F11 #2 (low confidence). |
| cve-2026-3300 F11 ("after April") | Applied | Holds. Takeaway reads "since 2026-04-13"; Wordfence: "attackers started exploiting the issue on April 13th, 2026". |
| 41089 F3 (Netlogon indicator) | Applied | Holds. Detection now reads "anomalous Netlogon traffic patterns from source addresses that are not domain controllers"; Help Net Security: "Anomalous Netlogon traffic patterns from non-DC source addresses". |
| ShieldBreak F4 (08-18 Detection/Triage paragraph) | Applied (pointer added) | Holds in part: the paragraph now says LevelBlue's mechanism "later replaced this reasoning", but the unsourced engine-parent-shell heuristic is still there; advisory F11 #5 (low confidence). |
| ShieldBreak F9 (engine build date) | Applied (frontmatter only) | Does not hold as a whole. `cves[CVE-2026-50656].fixed` now says 2026-07-08, the body still says "on 2026-07-09". New F4 #1. |
| DAEMON Tools F3 ("is clean") | Applied | Holds. Summary: "no longer includes the malicious behaviour Kaspersky describes"; Securelist: "no longer includes the malicious behavior described in this article". |
| GitLab F3 (PoC publication date) | Applied | Holds. The section says the repository "dates from 2026-09-11"; GitHub API `created_at: 2026-09-11T15:24:22Z`, extract dateline 2026-09-11; source record carries 2026-09-11. |

### Unsupported / hallucinated facts
- F4 #1 ShieldBreak (claim a6ec5c57e5): body "RoguePlanet ... was fixed in engine build 1.1.26060.3008 on 2026-07-09" against frontmatter "Engine build 1.1.26060.3008, released 2026-07-08 per Microsoft". MSRC CVE-2026-50656 Revisions: "Jul 8, 2026 ... Microsoft has released an update to the Microsoft Malware Protection Engine that addresses the vulnerability identified by CVE-2026-50656"; Cyber Kendra says "shipped engine build 1.1.26060.3008 on July 9"; the sibling 2026-07-09 entry says "a revision dated 2026-07-08 confirms Microsoft has now shipped". The remediation made the frontmatter agree with Microsoft and left the body on Cyber Kendra's date with no Contradiction line. Fix: set the body to 2026-07-08 or add a one-line Contradiction.

### Drop (low relevance / off-audience / duplicate)
- F7 #1 Austria NISG (low confidence): the entry's own 2026-09-30 correction says it "changes no decision for Swiss entities"; marginal, held at routine.

### Editorial / less-is-more flags (advisory)
- F11 #1 Exchange: sourcing_note about seven sentences with two "see body" pointers (re-raised after decline).
- F11 #2 Conference phishing: record summary says the title no longer presents the campaign as conference-targeted, but the title reads "reported against conference attendees"; Huntress's write-up says the actor reached "a large number of conference attendees" (low confidence).
- F11 #3 DAEMON Tools: the correction record summary says both that the detection line leads with the helper-to-PowerShell chain and that it now leads with the beacon (the beacon is right).
- F11 #4 Patch Tuesday/Netlogon: `status: exploited` and tag `actively-exploited` assert what the body presents as a disputed single-CERT claim; MSRC still records "Exploited: No" (low confidence).
- F11 #5 ShieldBreak 08-18 Update: engine-parent-shell hunting heuristic kept, contradicted by LevelBlue's mechanism, though marked as replaced (low confidence).
- F11 #6 nginx: example capture syntax `(?P<foo>...)` is not in any cited source, which show `(?<user_id>...)`; PCRE accepts both (low confidence).
- F11 #7 Austria: Improvement section restates the takeaway the same record adds to the main analysis (previously raised).

### Considered, not raised
- GitLab 9d99bc7eb8: one sentence chains GitLab facts (scope-changed vector, 2026-09-23 backports) with a closing watchTowr citation; the facts are on the GitLab pages cited in the same paragraph, so no F3 raised.
- Polyfill: BleepingComputer attributes "late May, HTTP 401" to researcher Pasquale Pillitteri; the entry states it as BleepingComputer's report without naming him. Accurate as reported; not raised.
- Check Point (2026-06-09 entry) and Palo Alto: KEV dates (2026-06-08, 2026-05-06) match the live catalogue; PSIRT conditions and Unit 42 timeline match.
- Apple CVE-2026-86950: CISA's `forensicTriage` is "No" while its `requiredAction` text still mentions the forensics requirement as boilerplate; the Correction's statement concerns the flag, which is right. EPSS 0.01242 confirmed via api.first.org.
- Kiteworks, Telerik, Kaspersky PAYLOAD, WaterPlum, Gentlemen, Chosen Brick, Flink, Kairos, Belnet, NCSC-CH Week 23, Ghost CMS, Spring Cloud Config, Everest Forms, Amazon SES: every checked clause matches its page; internal records (NCSC week 23 relabel, Chrome techniques, Belnet T1190) are source-supported with no reader-facing delta.
- Priority, classification, action discipline: no F16, F17 or F18 raised. Coverage: no missed angle named for this slice.

### Verdict
NEEDS_FIXES (truth: 1, editorial: 1, advisory: 7). The one truth finding is a firm internal inconsistency introduced by the last remediation (ShieldBreak fix date); the F7 and all F11 items are low-severity.

### Findings summary (machine-readable)
See `work/2026-10-11T1307Z-audit/verification.iter8.s2.findings.yaml` (9 records: 1 truth, 1 editorial, 7 advisory).
