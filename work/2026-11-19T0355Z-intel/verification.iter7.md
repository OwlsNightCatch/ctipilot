**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-19T08:03:47Z · ended_at=2026-11-19T08:32:35Z · duration_seconds=1728

## Verification report — 2026-11-19T0355Z-intel (iteration 7)

Scope: confirmation pass after the iteration-6 CLEAN, cold read, no deltas block. All 312 ledger claims have a verdict row in `verification.iter7.claims.yaml` (312 ok; `tools/claim_ledger.py --coverage 7`: 312/312 answered, 0 missing). Beyond the ledger I read every title, `sourcing_note`, record summary, run-record note and `techniques[]` list, because the ledger does not carry the `sourcing_note` field and three defects sit there. Pages read this pass (84 cited URLs plus raw/CSAF/CVE-record cross-reads): every claim page fetched with `extract` or `url`; CISA alerts (3), Drupal SA-CORE-2026-017/018, PSA-2026-11-16 and the Drupal risk legend through WebFetch; NCSC.ch hub posts through `ncsc-csh`; ENISA EUVD records and the NetApp advisory data through `url`; the HPE bulletin portal page is a JavaScript shell on every rung (extract, WebFetch), so its claims were checked on HPE's own CSAF JSON and text advisory, which carry the same bulletin. Not machine-readable by `extract`: Calif (read through the raw page), the Trend Micro advisory DDI rows (read in the raw HTML), the CERT-Bund bulletin (read through its CSAF), the GHSA risk fields (raw page).

Coverage looks complete: all four KEV additions in the window are covered (REDCap new, three updates), no new CVE of the six new entries was in `state/cves_seen.json` or the 14-day prior-coverage index, and the two held backlog rows (PHP pre-announcement, Basel-Landschaft incident) carry a named condition and expiry. No missed angle I can evidence from a named in-window source.

### Citation does not support the claim

1. **F3 #1** — `entries/2026-11-18/cve-2026-114938-java4shell-openjdk-avx512-base64-decoder-rce` sourcing_note: "An early source-reading analysis (Equixly) expected a JVM crash; Calif's later write-up and Upwind's update say code execution was demonstrated."
   - source: https://equixly.com/blog/2026/11/17/cve-2026-114938-pre-auth-heap-overflow-in-java-17-21-and-25/
   - Equixly does not expect a crash. Its "What is the impact?" section reads "The worst case is code execution as the user running the JVM" and its TL;DR "Calif reports remote code execution against Keycloak, Jira, Confluence, Artifactory, Jenkins, and PingFederate; a misplaced write can crash the JVM". The sentence invents a crash-versus-RCE contrast. Drop the Equixly sentence or reword to what the page says.

2. **F3 #2** — `entries/2026-09-22/cve-2026-13684-synology-dsm-unauth-file-read-write` sourcing_note: "Synology's notice says December 2024 while SA-24:20's revision table runs from 2024-11-05 to 2024-11-14 and BleepingComputer calls it a November 2024 advisory."
   - source: https://www.synology.com/en-global/security/advisory/Synology_SA_24_20
   - The revision table runs to 2025-03-27: rev 1 2024-11-05, rev 2 2024-11-12, rev 3 2024-11-14, rev 4 2024-11-26 (DSM 7.1 fix), rev 5 and 6 2024-12-05 (DSM 6.2 added and fixed), rev 7 to 9 2025-03. December 2024 revisions exist, so Synology's "patched in December 2024" is consistent with the table and the sentence manufactures a date conflict. Reword to the real table or drop it.

3. **F3 #3 (low confidence)** — `entries/2026-11-17/optimjack-poisoned-vendor-scripts-skimmer-iphone-router` sourcing_note: "so its citations carry 2026-11-17, the latest date its text carries."
   - source: https://ohey.ca/threats/ios-exploits/darksword/
   - The live page text carries "counted on 18 November 2026" and "Latest match | 18 November" (fetch metadata 2026-11-19). The stated reason is wrong by a day; the citation label itself is harmless. Say 2026-11-18 or drop the clause.

### Needs more research

4. **F8 #4 (low confidence)** — `entries/2026-11-18/cve-2026-114938-java4shell-openjdk-avx512-base64-decoder-rce` action: "update the JDK to 17.0.21.1, 21.0.13.1, 25.0.5.1 or 27.0.1.1 (Oracle builds; other distributions use their own build numbers)".
   - source: https://www.tenable.com/blog/java4shell-cve-2026-114938-frequently-asked-questions-about-openjdk-rce-vulnerability (cited four times)
   - Tenable: "As of November 18, Red Hat and Ubuntu had not released fixes, and Debian had fixed only its unstable branch", and "On November 18, the Keycloak project recommended starting its server with -XX:-UseBASE64Intrinsics as an interim mitigation. It said its x86-64 container images tagged 26.8.2-1 and 26.8.2-2 include an affected Java build". A responder on Red Hat, Ubuntu or Debian-stable, or running the Keycloak container, cannot execute "update" today; the JVM-flag interim is the action. One sourced sentence in Exposure or the takeaway closes it.

### Editorial / less-is-more flags (advisory)

5. **F11 #5 (low confidence)** — Java4Shell record 2026-11-19T05:03:07Z summary ends "...with the BACS citation for the post-update compromise check moved to that warning." Record-keeping narration in a reader-facing record summary, and the clause is absent from the update section (4c(d)). Drop it.
6. **F11 #6 (low confidence)** — Airlock actions[0]: "Update every Airlock Gateway on 8.5.0 to 8.5.2 to 8.5.3 and every 8.6.0 to 8.6.1" chains the affected range and the target build with the same word. Add a separator ("on 8.5.0 to 8.5.2: move to 8.5.3").
7. **F11 #7 (low confidence)** — `techniques[]` omit behaviours the cited sources describe (all ids active in the pinned dataset): nginx, Xint's chain to host root and Docker escape (T1068, T1611); OptimJack, Optimizely's exploited signup-flow flaw (T1190); tcherber, LDAP group enumeration and the nmap.go port scanner (T1069.002, T1046); REDCap, Unit 42's "Steganographic payload delivery disguised as image files" (T1027.003).
8. **F11 #8 (low confidence)** — run-record notes: "Unit 42 had seen exploitation since 2026-10-07"; the note is dated 2026-10-07 and states no start date (the entry already says "as of").

### Verdict

NEEDS_FIXES (truth: 3, editorial: 1, advisory: 4)

The three truth findings sit in `sourcing_note` text that the claim ledger does not carry; two were introduced or kept by earlier remediation sentences. The rest of the output (312 ledger claims, 14 entries, run record, record-vs-section agreement, `updated_at` mirrors, HPE counts recomputed from the CSAF: 76 CVEs, 33 at 9.0+, 19 network, 14 adjacent) holds.

### Findings summary (machine-readable)

See `work/2026-11-19T0355Z-intel/verification.iter7.findings.yaml` (8 records).
