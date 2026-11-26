**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-26T08:08:41Z · ended_at=2026-11-26T08:26:29Z · duration_seconds=1068

## Verification report — 2026-11-26T0356Z-intel (iteration 8)

Scope walked: all 229 ledger claims (claims.iter8.yaml, 229/229 answered; claims.changed.iter8.yaml 10/10), the five deltas from iteration 7, every cited page fetched live this pass (extract, direct GET, `ncsc-csh`, `cisa-kev`, and `WebFetch` for cisa.gov, drupal.org SA-017/018 and the Juniper portal) or read from the gate's quote-bodies where the host answers a client challenge.

### Prior-iteration deltas (all five verified against live pages)
1. nginx2root summary and 2026-11-26 section (Fortinet): FG-IR-26-279 timeline shows "2026-11-26: Products not impacted list updated"; FortiOS, FortiProxy, FortiMail, FortiManager and FortiAnalyzer are under "Products confirmed NOT impacted", FortiAuthenticator and 27 further products under investigation. Correct. (A separate Synology staleness defect in the same entry is finding #1.)
2. Drupal: SA-CORE-2026-019 page carries "TD:Uncommon" in its risk line and no other source does for the quoted claim; the Uncommon sentence now cites it, Searchlight's page supports the technique only (Docker official images, database and source-port exhaustion). Correct.
3. Java4Shell: Siemens SSA-810379 V1.1 (2026-11-23) "Added Desigo CC Advanced Reporting extension V8 and V9 to the list of affected products", both rows "Currently no fix is available". HPE bulletin facts (affected list, fixed builds, ClearPass 2026-12-01, hypervisor workaround, no JVM option) match. Cisco v1.4 matches. Correct; frontmatter lag is advisory finding #6.
4. Danfoss incident cves[CVE-2025-41450]: Danfoss DSA-2025-03-01 gives Base Score 8.2, "prior to version 4.2", patch 4.2; CNA record (cveawg) carries CVSS 3.1 8.2 with UI:R, PR:N, so user-interaction and pre-auth are supported; CISA KEV lists it. Correct. CVE-2023-25914/25915 rows match DSA-2023-08-01 (7.5, 9.8, below 3.3) and the contradiction with Synacktiv is surfaced in the section.
5. Mitel record summary: no out-of-cycle sentence remains; the summary matches the section and Mitel's revision 2.0 page (Last Updated 2026-11-24). Correct.

### Unsupported / hallucinated facts
- F4 #1 (nginx2root actions[2], current state). Entry: "on DSM 7.2.x, 7.1 and BeeStation OS, where the fix is listed as ongoing, turn HTTP/2 off under Control Panel, Network, Connectivity". Synology SA-26:20 (fetched this pass) shows "DSM 7.2.2 | Critical | Upgrade to 7.2.2-72806-11 or above.", "DSM 7.2.1 ... 7.2.1-69057-14", "DSM 7.1 ... 7.1.1-42962-10", "BeeStation OS 1.5 ... 1.5.6-68000", "APM 2.0 ... 2.0.2-88107"; only "DSM Enterprise 1.0 | OnGoing". Revision 3 (2026-11-24) "Update fix status for APM 1.2, APM 2.0, DSM 7.1, DSM 7.2.1, and DSM 7.2.2", revision 5 (2026-11-26) "Update fix status for BeeStation OS 1.5". The run's section of 2026-11-26 did not re-read Synology, so the action asserts a falsehood now. The 2026-11-22 section's snapshot was true at revision 2. This line is not a ledger claim (the ledger carries only actions[0] for this entry).
- F4 #2 (low confidence, SEPPmail cves[CVE-2026-124839]). `type: rce`, `vector: zero-click`, `auth: pre-auth` against "A specially crafted GINA account address could lead to command execution with elevated privileges by a maintenance script during system start." The page states no vector or authentication precondition; vendor score 7.7 sits well below the 9.2/9.3 unauthenticated rows. Run record defers it.

### Quantifier without source
- F14 #3 (low confidence, nginx2root 2026-11-26 section). "Its one log signal is the error-log warning ..." Unit 42 Table 3 lists two signals (process exit and the warning) and the indicator list adds shell processes as the worker account.

### Strengthen primary source
- F6 #4 (low confidence, Juniper). Sources are CISA, BSI and ENISA only; the vendor bulletin (JSA112183, and the on-demand bulletin URL that CISA's KEV notes field names) renders as a Salesforce shell on extract, raw GET and WebFetch. Disclosed in the entry; no verifiable strengthening exists.

### Drop (low relevance / off-audience / duplicate)
- F7 #5 (low confidence, 1Password). Victim-named incident entry with no stated Swiss or public-sector nexus and no named ground from the stricter breach bar; the takeaway's last sentence holds a transferable lesson that could carry it.

### Editorial / less-is-more flags (advisory)
- F11 #6 (Java4Shell frontmatter). `summary` and `cves[0].fixed` omit the HPE fixed builds and the Desigo CC Advanced Reporting no-fix status that the new section carries.
- F11 #7 (low confidence, registry). Four Microsoft designations registered with `aliases: []` although the run record says Microsoft's naming page lists Andariel, FamousSparrow and GhostEmperor as aliases; documented choice, no edit demanded.

### Checked and clean (no finding)
New entries: Okta (all claims against the live post and the Okta press release, closing date 2026-08-26 is on the page), SEPPmail (eleven rows, scores and descriptions match the revision history; 15.0.7 and 15.1.0 file-type note present), Juniper (ENISA records for CVE-2026-103406 and CVE-2026-103409, BSI CSAF revision 2 of 2026-11-24, KEV record, EPSS 0.0086 on 2026-11-25 from FIRST), 1Password (post and BleepingComputer match, including the six-to-ten character code change). Updated entries: Mitel, Drupal (SA-017 20 of 25, SA-018 14 of 25, SA-019 21 of 25, KEV listing of 2026-11-24, StepSecurity and Searchlight), GeoServer (watchTowr FAQ table marks only CVE-2026-129245, The Hacker News names 120705 with 129243 and 129244, NCSC.ch 13242 labels only 120705; CVE-2026-120704 7.2), Danfoss incident and Claroty (KEV, DSA-2023-08-01, DSA-2025-03-01, DSA-2025-08-01 8.7 and 6.8, DSA-2026-12-01 and -02, CISA CSAF), ARTEX (Microsoft guide six actors, ThreatBook claim, detections, Microsoft 2026-10-29 "Since late October 2026", The Record, Nextgov, Macau Business), PolinRider (SafeDep 375 repositories and 260 accounts, StepSecurity 576 of 622 and 311 accounts, 315 tabs, 40 installers), nginx2root (Unit 42, PAN-OS page timeline of 2026-11-24, Cisco v1.5 change log, CERT-EU, NCSC.ch, NCSC-NL 9.2 on all five, Siemens SSA-935812 unchanged, USN-9159-1). Style scan of reader-facing text: no em dash outside headings, no workflow vocabulary. Priorities and Admiralty codes are consistent with the cited sources' tiers (seppmail-gateway-revision-history, danfoss and mitel advisories are A in sources.json). Missed angles: none found; the ten KEV additions of 2026-11-25 are all covered (Xen Orchestra by the 2026-11-11 entry).

### Verdict
NEEDS_FIXES (truth: 3, editorial: 2, advisory: 2)

Truth finding #1 is the only high-confidence one; per the cap the run publishes with it logged as a residual.

### Findings summary (machine-readable)
See work/2026-11-26T0356Z-intel/verification.iter8.findings.yaml
