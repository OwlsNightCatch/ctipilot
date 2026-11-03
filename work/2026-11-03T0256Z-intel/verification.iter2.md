**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-03T04:29:55Z · ended_at=2026-11-03T04:54:15Z · duration_seconds=1460

## Verification report — 2026-11-03T0256Z-intel (iteration 2)

Scope: post-fix pass, cold read. All 213 ledger claims carry a verdict row (`verification.iter2.claims.yaml`; the 28 changed claims, every claim of the seven entries named in the deltas block, and the Node2Shell claims, of which about half were re-fetched at the source, the rest rest on iteration 1 and the gate's quote check). Eight entries read whole with `git diff HEAD`; run record and the new registry record `malware:c3rb3r-ransomware` read. About 75 cited pages fetched live this iteration (extract, bridge, ENISA EUVD API, NCSC hub posts, KEV feed, WebFetch for cisa.gov, github.com and the Akamai post).

### Prior-iteration deltas, walked first

- **1 F1 Danfoss AFP URL:** Fixed. All four occurrences now point at the Khaleej Times AFP text (byline AFP, dateline 12 Oct 2026). It says 'E. Leclerc, Intermarche and Cooperative U confirmed to AFP they suffered a cyberattack', 'Paris prosecutors confirmed the attack' and quotes Danfoss's 'legacy ... no longer receive software or security updates'; the dead afp.com URL no longer appears in the entry.
- **2 F3 'hit the same way':** Fixed. Summary, title and record summary now say refrigeration failures, 'in some cases remotely changed settings' (BleepingComputer: 'hackers remotely changed temperature settings'; 'In some cases, hackers shut down refrigerators or activated defrosting systems'), 'unclear whether they were hit in a coordinated attack', and attribute the same-vulnerability claim to Sabcobel ('According to Sabcobel's director, Stephan Moelans, the attacker leveraged the same vulnerability').
- **3 F9 Danfoss vs CyberInsider:** Reads honestly. Euronews ('Danfoss, the company that supplied the software ... in both the latest incident and the one in France') and Tagesschau (Estonia, older Danfoss system) are set against CyberInsider ('The manufacturer, controller models, and initial access method ... remain unknown'), each attributed. The closing 'so the vendor ... is not established' is the entry's own inference (advisory in F11 below).
- **4 F17 truncated quote:** Fixed. The evidence quote now ends 'the attacker leveraged the same vulnerability' and is a verbatim substring of the BleepingComputer page.
- **5 F9 SIMATIC 'first':** Fixed in the entry (title, headline, summary, record summary and section carry no 'first'; grep confirms). Not fixed in the run-record notes (F14 below).
- **6 F4 kernel CIQ:** Fixed. CIQ's table (read live) lists RLC Pro 8 and FIPS 8.10 kernel-4.18.0-553.178.1+2.1.el8_10_ciq, FIPS 8.6 ...el8_6.ciqfips, RLC Pro 9 kernel-5.14.0-687.60.1+2.1.el9_8_ciq and RLC Pro 10 kernel-6.12.0-211.68.1+2.1.el10_2_ciq, all 2026-11-01, plus LTS 9.6/9.2/8.6 on 2026-10-31; every string in cves[].fixed matches. AWS ('Publication Date: 10/30/2026 ... Last Updated Date: 11/02/2026') and CloudLinux ('last updated November 2, 2026') labels now say so. actions[] is split in two and each half is a start-now task.
- **7 F4 Trend Micro:** Mostly fixed. The page reads 'Last updated: 2026/11/02' and 'Current Status as of Nov. 2'; summary and opening sentence say 2026-11-02; TMWS Cloud 'Fixed (Oct. 30)', TWS Authentication Agent 'Impacted - Mitigation', on-premises gateway and enforcement agent 'Not Impacted' all match; NetApp's 'aware of public discussion of this vulnerability' is verbatim on the advisory page. The sourcing_note still says the table is 'dated as of 2026-10-30' (F4 below).
- **8 F4 Synology:** Partly fixed. 'or file services' is gone and the registry summary no longer says internet-exposed; the title still says 'encrypting exposed NAS' and the Exposure line ends 'with the management interface reachable from the internet' with no citation (F5 below).
- **9 F3 WS_FTP:** Fixed. NCSC post 13128 names four of the six critical flaws in its chain (CVE-2026-90868, CVE-2026-90865, CVE-2026-90863, CVE-2026-90866); the summary now says 'four of which'.
- **10 F14 Vaud:** Fixed: 'media reports, RTS among them' (Inside IT: 'berichteten Medien'). The Improvement section is one sentence now but still repeats the body sentence (F11 below).
- **11 F11 record summaries:** Fixed for all eight record summaries (reader-facing deltas, no field names). One section sentence in WS_FTP and one phrase in its sourcing_note still narrate the edit (F11 below).
- **12 F8 NetApp revision 11.0:** Judgement: can wait for the next fire on defender risk, but the stated reason is wrong. The adv_api URL the entry already cites returns the revision (kb_fixes lists 9.12.1P20HF1 and 9.13.1P21HF1; kb_rev_history '11.0 20261103: ONTAP 9.12.1P20HF1 and 9.13.1P21HF1 added'). Folding in costs one clause in the body and summary, the cves[].fixed string and a source record. Recorded as F8; a deferral will be re-flagged by the next cold pass.
- **13 F18 kernel:** Fixed. Two actions, each executable; the AWS target list stays in the body.

### Citation does not support the claim

1. **F3** `2026-10-29/php2shell-trend-micro-apex-quest-kace-netapp-ontap`: (low confidence) citation label '[NetApp, 2026-10-26](https://security.netapp.com/advisory/NTAP-20261021-0021)' and sources[] date 2026-10-26 for the NetApp advisory; the new clause 'NetApp says it is aware of public discussion of the vulnerability' carries the same label. Evidence: https://security.netapp.com/adv_api/advisory/NTAP-20261021-0021. Advisory data: published_date 2026-10-21 (revision 1.0 'Initial Public Release' 20261021), updated_date 2026-11-03; 2026-10-26 equals neither the publication date nor the latest revision (it is revision 8.0 and 9.0). The label predates this fire and is a revision date for a living page; date it 2026-10-21 or name the revision.

### Unsupported / hallucinated facts

2. **F4** `2026-10-29/php2shell-trend-micro-apex-quest-kace-netapp-ontap (sourcing_note)`: sourcing_note: 'Trend Micro's table is dated as of 2026-10-30 and the company says it keeps updating it, so a patch date can move'. Evidence: https://success.trendmicro.com/en-US/solution/KA-0024802. The page now reads 'Last updated: 2026/11/02' and 'Current Status as of Nov. 2', and this entry's own summary and analysis say 2026-11-02; the record's fields are [sources, body, summary], so sourcing_note was not revisited and states a superseded table date. Change it to 2026-11-02 (record fields must then name sourcing_note).

### Claims missing inline citation

3. **F5** `2026-09-22/cve-2026-13684-synology-dsm-unauth-file-read-write`: (low confidence) Exposure tail 'with the management interface reachable from the internet.' (after the SA-24:20 citation) and title 'C3RB3R ransomware is now encrypting exposed NAS'. Evidence: https://security-hub.ncsc.admin.ch/#/posts/12960. NCSC states the prerequisite as 'Network access to the DSM management interface' (not the internet); Synology says only 'devices running outdated versions of DSM'; 360 advises not to map the management port to the internet and BleepingComputer advises blocking management-interface access from the Internet, but no cited source says the encrypted NAS were internet-exposed. Cite BleepingComputer or 360 for the advice, or reword 'exposed' to 'outdated' in the title and drop 'from the internet' as a precondition.

### Needs more research

4. **F8** `2026-10-29/php2shell-trend-micro-apex-quest-kace-netapp-ontap`: NetApp fixed-build list ends at 9.19.1P4: 'lists the hotfix builds 9.14.1P18HF1, ... 9.19.1P3HF1 and, since revision 10.0 of 2026-10-29, 9.19.1P4'; summary 'hotfix builds from 9.14.1P18HF1 to 9.19.1P4'. Evidence: https://security.netapp.com/adv_api/advisory/NTAP-20261021-0021. Read live this iteration with tools/fetch_source.py url: kb_fixes now also lists 9.12.1P20HF1 and 9.13.1P21HF1 and kb_rev_history has '11.0 20261103: ONTAP 9.12.1P20HF1 and 9.13.1P21HF1 added to Software Versions and Fixes' (inserted 2026-11-03T04:15Z, after the run's read). The remediation note says the table is unreadable, but the adv_api URL the entry already cites carries it. Low defender risk (the interface-restriction advice is unchanged and the advisory is linked), so deferral to the next fire is acceptable; folding in now is one clause in the body and summary, the cves[].fixed string, and a source record at revision 11.0. If deferred, expect the next cold pass to flag it again.

### Surface contradiction

5. **F9** `2026-09-22/cve-2026-13684-synology-dsm-unauth-file-read-write`: (low confidence) 'Synology said on 2026-10-29 that threat actors are exploiting a vulnerability patched in December 2024 ... pointing to Synology-SA-24:20', with SA-24:20 listed as 'Synology PSIRT, 2024-11-05'. Evidence: https://www.synology.com/en-global/security/advisory/Synology_SA_24_20. SA-24:20's revision table reads '1 | 2024-11-05 | Initial public release', '2 | 2024-11-12', '3 | 2024-11-14', and BleepingComputer calls it 'a November 2024 security advisory', while Synology's notice says 'patched in December 2024'. The entry says the accounts conflict but does not surface this date mismatch between Synology's wording and the advisory it links; add one clause naming it.

### Editorial / less-is-more flags (advisory)

6. **F11** `2026-10-31/progress-ws-ftp-server-cve-2026-84295-unauth-cvss-10`: workflow narration in reader-facing text: Improvement section opens 'The entry first listed three of the bulletin's fifteen flaws.' and sourcing_note says 'The four critical records added later (CVE-2026-90868, ...)'. Evidence: ## Improvement — 2026-11-03T03:32:33Z. Iteration 1 flagged this wording ('where the entry first listed three'); the record summary was rewritten but the section sentence and the sourcing_note phrase remain. Open the section with the fact ('Six of the bulletin's fifteen flaws are critical: ...') and say 'the four other critical records rest on GitHub's advisory pages'.

7. **F11** `2026-11-01/vaud-school-it-support-platform-data-theft-teachers-pupils`: Improvement section repeats the analysis sentence; routine incident still three sentences plus takeaway. Evidence: Vaud police, contacted by Keystone-SDA, did not confirm the pupil report, and the education directorate's deputy director says that at present much points to an internal matter (translated from German). The body sentence and the '## Improvement' section carry the same police and deputy-director content (the section only adds 'with the case and several indications passed to the police'), so the run-record note 'the Improvement section no longer duplicates the analysis' does not hold. Under the routine bar (two sentences at most) fold the 'case passed to the police' clause into the body sentence and make the section one different fact, or keep the section and shorten the body. The development was published 2026-11-02, so an 'update' typing is also defensible (it would float a routine item, which is why improvement was chosen).

8. **F11** `2026-10-31/cve-2026-98432-linux-kernel-tcp-uaf-mptcp-remote-root`: record/section mismatch and 'among' dropped: record summary says 'CIQ's RLC Pro 8, 9 and 10 kernels are now fixed', which the 2026-11-03 section never states; the 2026-11-01 section still says 'RLC Pro LTS 8.10 and RLC Pro 10 are still waiting'; summary/headline/record summary list six Fortinet products 'as under investigation' without 'among'. Evidence: https://kb.ciq.com/article/security-advisories/cve-2026-98432-mitigation. CIQ's table lists RLC Pro 8, 9, 10 and FIPS 8.6/8.10 kernels released 2026-11-01. The delta is in the main analysis and cves[] but not in the 2026-11-03 section, so the record summary states more than the section and the earlier 'still waiting' sentence has no newer section correcting it; add one clause with the CIQ citation to the 2026-11-03 section. Fortinet's page lists roughly sixty products under investigation (FortiADC Manager ... FortiZTP) of which the entry names six; say 'among them' in the summary, as the body does.

9. **F11** `2026-10-13/danfoss-ak-sm-ak-sc-french-supermarket-refrigeration-attack`: headline 'Refrigeration sabotage reaches six more countries on 2 Nov' and title '... more than 115 shops in six more countries' while the body adds Finland per The Guardian; main analysis still about 690-735 words against the 550 bound. Evidence: https://www.theguardian.com/world/2026/nov/02/supermarket-freezers-across-europe-hit-by-second-suspected-cyber-attack. Guardian and Euronews list seven countries (Belgium, Estonia, Ireland, Finland, Luxembourg, the Netherlands, Sweden); BleepingComputer's six (and its 115 stores) is the narrower count. Say 'at least six' or 'seven'. The reconciliation of Euronews/Tagesschau (Danfoss) against CyberInsider (unknown) reads honestly; the closing 'so the vendor of the Belgian and Swedish sites is not established' is the entry's own inference and could say 'is not independently confirmed by CyberInsider'. Length is acknowledged in the run record.

10. **F11** `2026-08-13/cve-2026-58115-simatic-iot2050-node-red-unauth-root`: title 'one unauthenticated HTTP request runs code as root on an OT edge gateway'. Evidence: https://cert-portal.siemens.com/productcert/html/ssa-834709.html. (low confidence) Siemens says 'execute arbitrary code on the underlying server with maximum privileges'; no cited source says root. The wording predates this fire and is a fair reading of CVSS scope-changed full impact on Linux, but the body and summary say 'maximum privileges'; align the title.

11. **F11** `2026-10-29/php2shell-trend-micro-apex-quest-kace-netapp-ontap`: record typed 'improvement' for a vendor status change. Evidence: ## Improvement — 2026-11-03T03:47:17Z. (low confidence) The 2026-11-02 table shows Trend Micro Web Security in the cloud fixed (the 2026-10-31 section said due 2026-11-06) and a newly listed impacted TWS Authentication Agent, which is a vendor status development; 4c(i) warns against 'update' for re-reads, and the inverse (an improvement that carries a new vendor state) is a judgement call. Also the trim to 546 words dropped the 'Apex One as a Service addressed 2026-10-23' clause that the table still carries.

### Quantifier without source

12. **F14** `runs/2026-11-03/2026-11-03T0256Z-intel.md (Verification & coverage notes)`: run-record notes: 'first in-the-wild exploitation of CVE-2026-58115 on the SIMATIC IoT2050 entry (VulnCheck canary, one source)'. Evidence: https://www.vulncheck.com/blog/exploitation-targeting-node-red. The entry dropped 'first' after iteration 1, but the published run-record notes still say 'first in-the-wild exploitation'. VulnCheck writes only 'On October 30, 2026, one of our canaries caught an attacker exploiting CVE-2026-58115' and The Register has no sentence containing 'first'. Replace with 'VulnCheck's canary caught exploitation on 2026-10-30'.

### Missed angles

None found. NCSC hub posts since 2026-10-29 are all covered (13120 kernel, 13124 Drupal Commerce, 13128 WS_FTP; 13121-13123 already in the store or below the bar); KEV has no addition after 2026-10-30 (feed read this pass); in-window web searches for new exploited zero-days and Swiss incidents returned nothing indexed for 2026-11-02/03. Coverage looks complete.

### Verdict

NEEDS_FIXES (truth: 3, editorial: 3, advisory: 6)

Truth items are small (a stale table date in a sourcing_note, a run-record 'first', a NetApp citation date marked low confidence). The substantive iteration-1 defects (dead AFP source, same-way claim, kernel CIQ state, 'first', Trend Micro dates, WS_FTP chain wording) are fixed and re-verified against live pages. No priority, classification, org-triage or action-item defects found; classification blocks are present and in vocabulary on all eight entries.

### Findings summary (machine-readable)

```yaml
- code: F14
  category: quantifier-without-source
  section: runs/2026-11-03/2026-11-03T0256Z-intel.md (Verification & coverage notes)
  item: "run-record notes: 'first in-the-wild exploitation of CVE-2026-58115 on the SIMATIC IoT2050 entry (VulnCheck canary, one source)'"
  url_or_quote: "https://www.vulncheck.com/blog/exploitation-targeting-node-red"
  summary: "The entry dropped 'first' after iteration 1, but the published run-record notes still say 'first in-the-wild exploitation'. VulnCheck writes only 'On October 30, 2026, one of our canaries caught an attacker exploiting CVE-2026-58115' and The Register has no sentence containing 'first'. Replace with 'VulnCheck's canary caught exploitation on 2026-10-30'."
- code: F4
  category: hallucinated-fact
  section: 2026-10-29/php2shell-trend-micro-apex-quest-kace-netapp-ontap (sourcing_note)
  item: "sourcing_note: 'Trend Micro's table is dated as of 2026-10-30 and the company says it keeps updating it, so a patch date can move'"
  url_or_quote: "https://success.trendmicro.com/en-US/solution/KA-0024802"
  summary: "The page now reads 'Last updated: 2026/11/02' and 'Current Status as of Nov. 2', and this entry's own summary and analysis say 2026-11-02; the record's fields are [sources, body, summary], so sourcing_note was not revisited and states a superseded table date. Change it to 2026-11-02 (record fields must then name sourcing_note)."
- code: F3
  category: claim-not-supported
  section: 2026-10-29/php2shell-trend-micro-apex-quest-kace-netapp-ontap
  item: "(low confidence) citation label '[NetApp, 2026-10-26](https://security.netapp.com/advisory/NTAP-20261021-0021)' and sources[] date 2026-10-26 for the NetApp advisory; the new clause 'NetApp says it is aware of public discussion of the vulnerability' carries the same label"
  url_or_quote: "https://security.netapp.com/adv_api/advisory/NTAP-20261021-0021"
  summary: "Advisory data: published_date 2026-10-21 (revision 1.0 'Initial Public Release' 20261021), updated_date 2026-11-03; 2026-10-26 equals neither the publication date nor the latest revision (it is revision 8.0 and 9.0). The label predates this fire and is a revision date for a living page; date it 2026-10-21 or name the revision."
- code: F9
  category: surface-contradiction
  section: 2026-09-22/cve-2026-13684-synology-dsm-unauth-file-read-write
  item: "(low confidence) 'Synology said on 2026-10-29 that threat actors are exploiting a vulnerability patched in December 2024 ... pointing to Synology-SA-24:20', with SA-24:20 listed as 'Synology PSIRT, 2024-11-05'"
  url_or_quote: "https://www.synology.com/en-global/security/advisory/Synology_SA_24_20"
  summary: "SA-24:20's revision table reads '1 | 2024-11-05 | Initial public release', '2 | 2024-11-12', '3 | 2024-11-14', and BleepingComputer calls it 'a November 2024 security advisory', while Synology's notice says 'patched in December 2024'. The entry says the accounts conflict but does not surface this date mismatch between Synology's wording and the advisory it links; add one clause naming it."
- code: F5
  category: missing-citation
  section: 2026-09-22/cve-2026-13684-synology-dsm-unauth-file-read-write
  item: "(low confidence) Exposure tail 'with the management interface reachable from the internet.' (after the SA-24:20 citation) and title 'C3RB3R ransomware is now encrypting exposed NAS'"
  url_or_quote: "https://security-hub.ncsc.admin.ch/#/posts/12960"
  summary: "NCSC states the prerequisite as 'Network access to the DSM management interface' (not the internet); Synology says only 'devices running outdated versions of DSM'; 360 advises not to map the management port to the internet and BleepingComputer advises blocking management-interface access from the Internet, but no cited source says the encrypted NAS were internet-exposed. Cite BleepingComputer or 360 for the advice, or reword 'exposed' to 'outdated' in the title and drop 'from the internet' as a precondition."
- code: F8
  category: needs-more-research
  section: 2026-10-29/php2shell-trend-micro-apex-quest-kace-netapp-ontap
  item: "NetApp fixed-build list ends at 9.19.1P4: 'lists the hotfix builds 9.14.1P18HF1, ... 9.19.1P3HF1 and, since revision 10.0 of 2026-10-29, 9.19.1P4'; summary 'hotfix builds from 9.14.1P18HF1 to 9.19.1P4'"
  url_or_quote: "https://security.netapp.com/adv_api/advisory/NTAP-20261021-0021"
  summary: "Read live this iteration with tools/fetch_source.py url: kb_fixes now also lists 9.12.1P20HF1 and 9.13.1P21HF1 and kb_rev_history has '11.0 20261103: ONTAP 9.12.1P20HF1 and 9.13.1P21HF1 added to Software Versions and Fixes' (inserted 2026-11-03T04:15Z, after the run's read). The remediation note says the table is unreadable, but the adv_api URL the entry already cites carries it. Low defender risk (the interface-restriction advice is unchanged and the advisory is linked), so deferral to the next fire is acceptable; folding in now is one clause in the body and summary, the cves[].fixed string, and a source record at revision 11.0. If deferred, expect the next cold pass to flag it again."
- code: F11
  category: editorial-advisory
  section: 2026-10-31/progress-ws-ftp-server-cve-2026-84295-unauth-cvss-10
  item: "workflow narration in reader-facing text: Improvement section opens 'The entry first listed three of the bulletin's fifteen flaws.' and sourcing_note says 'The four critical records added later (CVE-2026-90868, ...)'"
  url_or_quote: "## Improvement — 2026-11-03T03:32:33Z"
  summary: "Iteration 1 flagged this wording ('where the entry first listed three'); the record summary was rewritten but the section sentence and the sourcing_note phrase remain. Open the section with the fact ('Six of the bulletin's fifteen flaws are critical: ...') and say 'the four other critical records rest on GitHub's advisory pages'."
- code: F11
  category: editorial-advisory
  section: 2026-11-01/vaud-school-it-support-platform-data-theft-teachers-pupils
  item: "Improvement section repeats the analysis sentence; routine incident still three sentences plus takeaway"
  url_or_quote: "Vaud police, contacted by Keystone-SDA, did not confirm the pupil report, and the education directorate's deputy director says that at present much points to an internal matter (translated from German)"
  summary: "The body sentence and the '## Improvement' section carry the same police and deputy-director content (the section only adds 'with the case and several indications passed to the police'), so the run-record note 'the Improvement section no longer duplicates the analysis' does not hold. Under the routine bar (two sentences at most) fold the 'case passed to the police' clause into the body sentence and make the section one different fact, or keep the section and shorten the body. The development was published 2026-11-02, so an 'update' typing is also defensible (it would float a routine item, which is why improvement was chosen)."
- code: F11
  category: editorial-advisory
  section: 2026-10-31/cve-2026-98432-linux-kernel-tcp-uaf-mptcp-remote-root
  item: "record/section mismatch and 'among' dropped: record summary says 'CIQ's RLC Pro 8, 9 and 10 kernels are now fixed', which the 2026-11-03 section never states; the 2026-11-01 section still says 'RLC Pro LTS 8.10 and RLC Pro 10 are still waiting'; summary/headline/record summary list six Fortinet products 'as under investigation' without 'among'"
  url_or_quote: "https://kb.ciq.com/article/security-advisories/cve-2026-98432-mitigation"
  summary: "CIQ's table lists RLC Pro 8, 9, 10 and FIPS 8.6/8.10 kernels released 2026-11-01. The delta is in the main analysis and cves[] but not in the 2026-11-03 section, so the record summary states more than the section and the earlier 'still waiting' sentence has no newer section correcting it; add one clause with the CIQ citation to the 2026-11-03 section. Fortinet's page lists roughly sixty products under investigation (FortiADC Manager ... FortiZTP) of which the entry names six; say 'among them' in the summary, as the body does."
- code: F11
  category: editorial-advisory
  section: 2026-10-13/danfoss-ak-sm-ak-sc-french-supermarket-refrigeration-attack
  item: "headline 'Refrigeration sabotage reaches six more countries on 2 Nov' and title '... more than 115 shops in six more countries' while the body adds Finland per The Guardian; main analysis still about 690-735 words against the 550 bound"
  url_or_quote: "https://www.theguardian.com/world/2026/nov/02/supermarket-freezers-across-europe-hit-by-second-suspected-cyber-attack"
  summary: "Guardian and Euronews list seven countries (Belgium, Estonia, Ireland, Finland, Luxembourg, the Netherlands, Sweden); BleepingComputer's six (and its 115 stores) is the narrower count. Say 'at least six' or 'seven'. The reconciliation of Euronews/Tagesschau (Danfoss) against CyberInsider (unknown) reads honestly; the closing 'so the vendor of the Belgian and Swedish sites is not established' is the entry's own inference and could say 'is not independently confirmed by CyberInsider'. Length is acknowledged in the run record."
- code: F11
  category: editorial-advisory
  section: 2026-08-13/cve-2026-58115-simatic-iot2050-node-red-unauth-root
  item: "title 'one unauthenticated HTTP request runs code as root on an OT edge gateway'"
  url_or_quote: "https://cert-portal.siemens.com/productcert/html/ssa-834709.html"
  summary: "(low confidence) Siemens says 'execute arbitrary code on the underlying server with maximum privileges'; no cited source says root. The wording predates this fire and is a fair reading of CVSS scope-changed full impact on Linux, but the body and summary say 'maximum privileges'; align the title."
- code: F11
  category: editorial-advisory
  section: 2026-10-29/php2shell-trend-micro-apex-quest-kace-netapp-ontap
  item: "record typed 'improvement' for a vendor status change"
  url_or_quote: "## Improvement — 2026-11-03T03:47:17Z"
  summary: "(low confidence) The 2026-11-02 table shows Trend Micro Web Security in the cloud fixed (the 2026-10-31 section said due 2026-11-06) and a newly listed impacted TWS Authentication Agent, which is a vendor status development; 4c(i) warns against 'update' for re-reads, and the inverse (an improvement that carries a new vendor state) is a judgement call. Also the trim to 546 words dropped the 'Apex One as a Service addressed 2026-10-23' clause that the table still carries."
```
