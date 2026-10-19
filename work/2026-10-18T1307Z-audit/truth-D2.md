**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-18T13:28:13Z · ended_at=2026-10-18T14:02:31Z · duration_seconds=2058

## Retrospective truth report — batch D2 (run 2026-10-18T1307Z-audit)

14 batch entries checked whole (all factual-error), 4 lead-only quote decisions. Machine-readable findings, claim verdicts and group records: truth-D2.yaml, truth-D2.claims.yaml.

### 2026-05-11/cve-2026-6722-php-soap-extension-use-after-free-in-soap-glob — factual-error
1. [factual-error] **summary** — claim: "PHP SOAP extension use-after-free patched in all 8.x branches"
   - Defect: Only the 8.2, 8.3, 8.4 and 8.5 branches received fixes; PHP 8.0/8.1 are end-of-life and unpatched, so 'all 8.x branches' overstates coverage
   - Ground truth: php.net ChangeLog lists the SOAP fix only in 8.2.31, 8.3.31, 8.4.21 and 8.5.6 (each dated 07 May 2026); CVE record (CNA PHP Group) affected = PHP 8.2.*, 8.3.*, 8.4.*, 8.5.* below those versions (https://www.php.net/ChangeLog-8.php)
   - Fix: Say 'fixed in the supported 8.2-8.5 branches (8.2.31 / 8.3.31 / 8.4.21 / 8.5.6)'
2. [factual-error] **cves[CVE-2026-7262]** — claim: "cvss: "6.3"; type: rce"
   - Defect: The CVE record scores CVE-2026-7262 as CVSS 4.0 2.9 LOW and the flaw is a NULL-dereference crash (DoS), not RCE; 6.3 is the figure shown on the GHSA page, and the conflict between the two PHP-authored records is not surfaced
   - Ground truth: CVE record (CNA PHP Group, updated 2026-07-15): baseScore 2.9 LOW, CVSS:4.0/AV:N/AC:L/AT:P/PR:N/UI:N/VC:N/VI:N/VA:L/SC:N/SI:N/SA:N/E:P; description "This allows a remote unauthenticated attacker to crash the PHP SOAP serv[er]"; GHSA page still shows "Moderate 6.3" (https://cveawg.mitre.org/api/cve/CVE-2026-7262)
   - Fix: cvss 2.9 (note GHSA shows 6.3), type dos; same in the body line 'CVSS 4.0 6.3 Moderate' and table row
3. [factual-error] **body paragraph 1 and paragraph 2** — claim: "No public proof-of-concept and no in-the-wild exploitation are reported as of this run"
   - Defect: The primary advisory itself embeds a working trigger reproducer and the fix commit adds a regression test with the trigger envelope; 'no public proof-of-concept' is wrong (no ITW report found, no KEV entry is correct)
   - Ground truth: GHSA-85c2-q967-79q5 body contains a Handler/SoapServer script with the apache:Map duplicate-key envelope and says 'The attacker has high control over this memory segment ... leading to Remote Code Execution'; commit 8f228a35cb adds ext/soap/tests/GHSA-85c2-q967-79q5.phpt (https://github.com/php/php-src/security/advisories/GHSA-85c2-q967-79q5)
   - Fix: Replace with 'no in-the-wild exploitation reported; the advisory publishes a trigger reproducer'
4. [imprecision] **body paragraph 1** — claim: "Affected versions are PHP 8.2.0 through 8.5.5"
   - Defect: Range spans branches and wrongly implies e.g. 8.2.31-8.4.20 are affected-and-unfixed in a single span; cited ChangeLog lists fixes only, not affected ranges
   - Ground truth: CVE record affected: 8.2.0-<8.2.31, 8.3.0-<8.3.31, 8.4.0-<8.4.21, 8.5.0-<8.5.6 (https://cveawg.mitre.org/api/cve/CVE-2026-6722)
   - Fix: State affected as 'below 8.2.31 / 8.3.31 / 8.4.21 / 8.5.6 in their respective branches'
5. [imprecision] **CVE Summary Table, CVE-2026-6722 row** — claim: "9.5 (CVSS 4.0)"
   - Defect: The cited GHSA shows only 'Severity High', no numeric score; 9.5 is the CNA's CVE-record score, cited elsewhere as 'NVD'
   - Ground truth: GHSA-85c2 page: 'Severity High CVE ID CVE-2026-6722' (no CVSS number); CVE record CNA CVSS 4.0 9.5 CRITICAL (https://github.com/php/php-src/security/advisories/GHSA-85c2-q967-79q5)
   - Fix: Cite the CVE record/CNA for 9.5 and the GHSA for 'High'
6. [imprecision] **body paragraph 2** — claim: "a runtime present in essentially every Internet-exposed PHP application"
   - Defect: ext-soap is an optional extension and only SoapServer endpoints are reachable; no source supports 'essentially every'
   - Ground truth: GHSA-85c2: bug is in ext-soap; trigger requires SoapServer::handle() on attacker input (https://github.com/php/php-src/security/advisories/GHSA-85c2-q967-79q5)
   - Fix: Drop the quantifier; say 'any PHP application that exposes a SoapServer'
7. [imprecision] **frontmatter classification / techniques[]** — claim: "(absent)"
   - Defect: Entry carries no `classification` block and no `techniques[]` (migrated schema-1 record); a vulnerability entry needs both
   - Ground truth: org profile: every entry carries classification {reliability, credibility}; vulnerability entries need a non-empty techniques[] (docs/pipeline.md)
   - Fix: Add classification (e.g. primary vendor/CNA source, corroborated) and techniques[] (T1190) in the survivor via a changelog record

### 2026-05-11/cve-2026-6722-php-soap-use-after-free-in-soap-global-ref-map — factual-error
1. [imprecision] **summary** — claim: "#### Vulnerability class and primitive"
   - Defect: Summary is a markdown heading and states nothing; event_date is null although all sources date the disclosure 2026-05-07
   - Ground truth: GHSA-85c2-q967-79q5 published May 7, 2026 (https://github.com/php/php-src/security/advisories/GHSA-85c2-q967-79q5)
   - Fix: Write a real one-sentence summary and set event_date 2026-05-07
2. [factual-error] **cves[CVE-2026-7262]** — claim: "cvss: "6.3"; type: rce"
   - Defect: CNA CVE record: CVSS 4.0 2.9 LOW (GHSA page shows 6.3; conflict not surfaced); the flaw is a segfault DoS (body itself says 'NULL deref rather than UAF'), so type rce is wrong
   - Ground truth: CVE record: baseScore 2.9 LOW; "This allows a remote unauthenticated attacker to crash the PHP SOAP serv[er]"; GHSA-hmxp: "the process will segfault with a NULL pointer violation ... DoS becomes trivial" (https://cveawg.mitre.org/api/cve/CVE-2026-7262)
   - Fix: cvss 2.9, type dos; body '(both Moderate, CVSS 4.0 6.3)' should say 7261 only
3. [imprecision] **body, companion CVE paragraph** — claim: "suggesting the upstream review pass that produced GHSA-85c2-q967-79q5 covered the whole apache-map handling surface"
   - Defect: The ChangeLog only lists the three GHSAs in the same releases; CVE-2026-7261 is in SOAP_PERSISTENCE_SESSION header handling, not apache-map; 7262 also needs a typemap configured (omitted)
   - Ground truth: ChangeLog: three separate GHSA entries under SOAP; GHSA-m33r: SOAP_PERSISTENCE_SESSION header fault; GHSA-hmxp: reachable 'when the SOAP server has a typemap configured' (https://www.php.net/ChangeLog-8.php)
   - Fix: Delete the inference; add that 7262 needs SOAP typemap configured
4. [imprecision] **body, Exploitation prerequisites** — claim: "the SoapClient/Server pair used for reverse-direction RPC"
   - Defect: No source says SoapClient is affected; the sentence also contradicts the preceding 'SoapServer ... is sufficient' (a SoapServer must be instantiated)
   - Ground truth: GHSA-85c2 and CVE description reference only SoapServer decoding of an attacker-supplied envelope (https://github.com/php/php-src/security/advisories/GHSA-85c2-q967-79q5)
   - Fix: Remove SoapClient mention; keep 'any application that instantiates a SoapServer on untrusted input'
5. [imprecision] **body, Detection concepts** — claim: "increased `Notice: Trying to access array offset on null` or `Fatal error: Uncaught Error: Call to a member function ... on null` clustered around SOAP request handlers — failed exploitation attempts"
   - Defect: No source ties these PHP log messages to this bug; the documented failure symptom is a worker segfault (7262) or none
   - Ground truth: GHSA-hmxp: 'the process will segfault with a NULL pointer dereference violation' (https://github.com/php/php-src/security/advisories/GHSA-hmxp-6pc4-f3vv)
   - Fix: Remove the unsourced log signature
6. [imprecision] **body, MITRE ATT&CK mapping** — claim: "likely follow-on persistence path observed in prior PHP RCE incidents"
   - Defect: No source describes post-exploitation behaviour (web shell or Unix shell) for this CVE; 'observed in prior PHP RCE incidents' is uncited. Only T1190 is source-supported
   - Ground truth: GHSA-85c2 ends at 'leading to Remote Code Execution' (https://github.com/php/php-src/security/advisories/GHSA-85c2-q967-79q5)
   - Fix: Keep T1190 only or mark T1059.004/T1505.003 as analyst inference
7. [imprecision] **body, Where SOAP commonly lingers** — claim: "Where SOAP commonly lingers in EU public-sector estates"
   - Defect: Uncited generalisation about EU public-sector SOAP prevalence
   - Ground truth: none of the cited pages mention public-sector SOAP usage (https://github.com/php/php-src/security/advisories/GHSA-85c2-q967-79q5)
   - Fix: Cite or drop
8. [imprecision] **frontmatter classification / techniques[]** — claim: "(absent)"
   - Defect: Entry carries no `classification` block and no `techniques[]` (migrated schema-1 record); a vulnerability entry needs both
   - Ground truth: org profile: every entry carries classification {reliability, credibility}; vulnerability entries need a non-empty techniques[] (docs/pipeline.md)
   - Fix: Add classification (e.g. primary vendor/CNA source, corroborated) and techniques[] (T1190) in the survivor via a changelog record

### 2026-05-15/cisco-catalyst-sd-wan-cve-2026-20182-authentication-bypass-a — factual-error
1. [factual-error] **headline; body 'Kill chain (UAT-8616 post-exploitation TTPs)' steps 6-9** — claim: "Godzilla, Behinder, and XenShell webshells deployed for persistent access"
   - Defect: Steps 6-9 (Godzilla/Behinder/XenShell webshells, AdaptixC2/Sliver/Nimplant C2, XMRig) are attributed to UAT-8616, but Talos attributes them to other clusters exploiting CVE-2026-20133/20128/20122
   - Ground truth: Talos: "a series of threat actors, distinct from UAT-8616, that have been observed to be exploiting a different, previously disclosed set of vulnerabilities ... CVE-2026-20133, CVE-2026-20128 and CVE-2026-20122"; for UAT-8616 on 20182: "attempted to add SSH keys, modify NETCONF configurations, and escalate to root privileges" (https://blog.talosintelligence.com/sd-wan-ongoing-exploitation/)
   - Fix: Limit the UAT-8616 kill chain to SSH key injection, NETCONF, root escalation and ORB-network overlap; present Clusters 1-10 separately
2. [factual-error] **body, Vulnerability mechanics** — claim: "checks whether the device type is `VBOND` (0) or `VEDGE` (1) before requiring certificate validation"
   - Defect: Device-type values are wrong; Rapid7's table is vEdge=1, vHub=2, vSmart=3, vBond=4, vManage=5, and the cert checks cover types 3/5 and 1. The authenticated flag is set but a Hello is still required to reach UP, contrary to 'immediately ... transitions the peering state to UP'
   - Ground truth: Rapid7: "| 1 | vEdge ... | 2 | vHub ... | 3 | vSmart ... | 4 | vBond ... | 5 | vManage"; "the attacker must send a Hello message (Message type 5) to transition the peer to the UP state" (https://www.rapid7.com/blog/post/ve-cve-2026-20182-critical-authentication-bypass-cisco-catalyst-sd-wan-controller-fixed/)
   - Fix: Use Rapid7's enumeration: checks for vSmart (3), vManage (5), vEdge (1); none for vHub (2)
3. [factual-error] **body, Kill chain step 6** — claim: "XenShell is a lightweight Python-based variant targeting Linux"
   - Defect: Talos describes XenShell as a JSP-based webshell
   - Ground truth: Talos: "ZeroZenX Labs' proof-of-concept and accompanying JSP-based webshell which we track as \"XenShell.\"" (https://blog.talosintelligence.com/sd-wan-ongoing-exploitation/)
   - Fix: Say 'JSP-based webshell (XenShell)'; and drop 'dynamic key exchange'/'AES-128-CBC' details unless sourced
4. [factual-error] **body, Background** — claim: "CVE-2026-20127 (pre-auth RCE in SD-WAN Manager)"
   - Defect: CVE-2026-20127 is a peering authentication bypass in the Controller (vSmart); Cisco's advisory is titled 'Controller Authentication Bypass' (affects Controller/Manager/Validator), not an RCE in Manager. 'joint advisory from ACSC, NCSC-UK, and Cisco Talos' is also not what the cited Talos post is
   - Ground truth: Talos: "CVE-2026-20127, a vulnerability in Cisco Catalyst SD-WAN Controller, formerly vSmart, that allows an unauthenticated remote attacker to bypass authentication"; CISA KEV: "Cisco Catalyst SD-WAN Controller and Manager Authentication Bypass Vulnerability" (https://blog.talosintelligence.com/uat-8616-sd-wan/)
   - Fix: Describe 20127 as an authentication bypass in the Controller (and Manager); cite Talos blog and ACSC hunt guide separately
5. [factual-error] **body, Background** — claim: "CVE-2026-20182 is that actor's sixth exploited Cisco SD-WAN vulnerability in the ongoing campaign"
   - Defect: No source counts six; Talos ties UAT-8616 to CVE-2026-20127, CVE-2026-20182 and the (reported) CVE-2022-20775 chain
   - Ground truth: Talos (20182 post): "UAT-8616 previously exploited a similar vulnerability in Cisco Catalyst SD-WAN Controller, CVE-2026-20127" (https://blog.talosintelligence.com/sd-wan-ongoing-exploitation/)
   - Fix: Delete the count
6. [imprecision] **body, Background** — claim: "Cisco and CISA have published five previous SD-WAN vulnerability advisories with confirmed in-the-wild exploitation this year alone"
   - Defect: Quantifier not in the cited Talos Feb post; KEV shows five earlier 2026 SD-WAN CVEs (20127, 20122, 20128, 20133 plus 2022-20775) across three Cisco advisories, not five advisories
   - Ground truth: KEV: CVE-2022-20775 and CVE-2026-20127 added 2026-02-25; CVE-2026-20122/20128/20133 added 2026-04-20 (https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)
   - Fix: Cite KEV and state 'five earlier SD-WAN CVEs'
7. [imprecision] **body, Kill chain closing paragraph** — claim: "The 10+ additional clusters (#1–#10 in Talos's taxonomy)"
   - Defect: Talos lists exactly Clusters #1 to #10; they also run C2 implants and a credential stealer, and 'skip the version-downgrade chain' is not stated
   - Ground truth: Talos: "So far, Talos has observed the following clusters of malicious activity ...: Cluster #1 to Cluster #10." (https://blog.talosintelligence.com/sd-wan-ongoing-exploitation/)
   - Fix: Say 'ten clusters'
8. [factual-error] **body, Hunt and detection concepts** — claim: "SD-WAN Controller-to-Controller peering shows as VHUB-type — flag unexpected vHub entries"
   - Defect: Wrong: vSmart peers are type 3 (vManage 5); vHub is the type claimed by the exploit. Cisco's own check is 'state:up' with 'challenge-ack 0' in `show control connections detail`, not `show sdwan control connections`
   - Ground truth: Cisco rpa2: "To check ... the presence of state:up and no challenge-ack ... use the commands show control connections detail or show control connections-history detail" (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-rpa2-v69WY2SW)
   - Fix: Use Cisco's documented command and discriminator
9. [imprecision] **body, Kill chain items 4 and 8; ATT&CK ids** — claim: "T1562.001 Impair Defenses: Disable or Modify Tools ... T1070.002 Indicator Removal: Clear Linux or Mac System Logs"
   - Defect: T1562, T1562.001 and T1070.002 are revoked in ATT&CK v20 (-> T1685 / T1685.006); a software version downgrade is not 'disable or modify tools'
   - Ground truth: attack/enterprise-attack.json: T1562.001 revoked_by T1685; T1070.002 revoked_by T1685.006 (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-rpa2-v69WY2SW)
   - Fix: Map to active ids (T1685 / T1685.006) or drop the version-downgrade mapping
10. [imprecision] **body, Hardening** — claim: "the authentication-bypass function is in the control-plane peering path that cannot be disabled without breaking SD-WAN functionality"
   - Defect: Rationale is in no source; Cisco only says there are no workarounds
   - Ground truth: Cisco rpa2: "There are no workarounds that address this vulnerability." (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-rpa2-v69WY2SW)
   - Fix: Delete the rationale
11. [imprecision] **evidence[0]; summary** — claim: "Background."
   - Defect: evidence quote is the single word 'Background.' (publisher 'ctipilot v2 brief (migrated)'), not a passage of any cited page; summary is a stub 'Background. Cisco SD-WAN has been a sustained exploitation target since 2023.'
   - Ground truth: no cited page contains this quote (https://blog.talosintelligence.com/sd-wan-ongoing-exploitation/)
   - Fix: Replace evidence with a verbatim Talos/Cisco quote and write a real summary
12. [imprecision] **frontmatter classification / techniques[]** — claim: "(absent)"
   - Defect: Entry carries no `classification` block and no `techniques[]` (migrated schema-1 record); a vulnerability entry needs both
   - Ground truth: org profile: every entry carries classification {reliability, credibility}; vulnerability entries need a non-empty techniques[] (docs/pipeline.md)
   - Fix: Add classification (e.g. primary vendor/CNA source, corroborated) and techniques[] (T1190) in the survivor via a changelog record

### 2026-05-15/cve-2026-20182-cisco-catalyst-sd-wan-controller-manager-pre — factual-error
1. [factual-error] **summary; sources[2].publisher** — claim: "CISA Emergency Directive ED-26-03 issued 2026-05-14"
   - Defect: ED 26-03 was issued 2026-02-25 (updated 2026-03-11) and names CVE-2026-20127 and CVE-2022-20775; CVE-2026-20182 reached it through the 2026-05-14 KEV listing, not a new directive
   - Ground truth: CISA ED 26-03 page: "Original Issuance Date: February 25, 2026"; "Updated March 11, 2026"; "involves the following known exploited vulnerabilities identified by Cisco:" CVE-2026-20127, CVE-2022-20775 (https://www.cisa.gov/news-events/directives/ed-26-03-mitigate-vulnerabilities-cisco-sd-wan-systems)
   - Fix: Say 'added to KEV 2026-05-14 under the existing ED 26-03 (issued 2026-02-25)'
2. [imprecision] **body** — claim: "achieving persistent SSH access to the SD-WAN Manager on NETCONF port TCP/830"
   - Defect: Rapid7 demonstrates the key injection against the Controller (vSmart) NETCONF service, not the Manager
   - Ground truth: Rapid7: "target a Cisco Catalyst SD-WAN Controller ... SSH into the NETCONF service over TCP port 830" (https://www.rapid7.com/blog/post/ve-cve-2026-20182-critical-authentication-bypass-cisco-catalyst-sd-wan-controller-fixed/)
   - Fix: Say 'Controller (vSmart); Cisco lists Controller, Manager and Validator as affected'
3. [imprecision] **body** — claim: "network segmentation of the UDP/12346 interface is the only partial mitigation where upgrading is not immediately possible"
   - Defect: Cisco states no workarounds or mitigations for CVE-2026-20182; the segmentation claim is uncited
   - Ground truth: Cisco rpa2: "There are no workarounds that address this vulnerability." (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-rpa2-v69WY2SW)
   - Fix: Delete or attribute to analyst judgement
4. [imprecision] **title/headline/body** — claim: "Controller/Manager"
   - Defect: Cisco advisory v2.0 (2026-06-16) lists Validator (vBond) as affected too
   - Ground truth: Cisco rpa2 summary: "peering authentication in Cisco Catalyst SD-WAN Controller ..., Manager ..., and Validator ... could allow an unauthenticated, remote attacker" (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-rpa2-v69WY2SW)
   - Fix: Add Validator to affected products
5. [imprecision] **evidence[0]** — claim: "CVE-2026-20182 (CVSS 10.0, CWE-287) is a complete authentication bypass in the vdaemon service's DTLS control-plane peering on UDP/12346 (Cisco PSIRT cisco-sa-sdwan-rpa2-v69WY2SW, 2026-05-14 · Rapid7, 2026-05-14)."
   - Defect: Evidence quote is the entry's own sentence (publisher 'ctipilot v2 brief (migrated)'), not a contiguous passage of any cited page
   - Ground truth: Neither the Cisco page nor Rapid7 contains this sentence (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-rpa2-v69WY2SW)
   - Fix: Replace with a verbatim Cisco/Rapid7 quote
6. [imprecision] **frontmatter classification / techniques[]** — claim: "(absent)"
   - Defect: Entry carries no `classification` block and no `techniques[]` (migrated schema-1 record); a vulnerability entry needs both
   - Ground truth: org profile: every entry carries classification {reliability, credibility}; vulnerability entries need a non-empty techniques[] (docs/pipeline.md)
   - Fix: Add classification (e.g. primary vendor/CNA source, corroborated) and techniques[] (T1190) in the survivor via a changelog record

### 2026-06-06/cve-2026-20245-cisco-catalyst-sd-wan-manager-actively-exploi — factual-error
1. [factual-error] **title; headline; summary; actions[0]; main analysis** — claim: "actively-exploited command-injection to root (no patch)"
   - Defect: 'No patch' is false today: Cisco published fixed releases (final table 2026-06-12) and a Live Protect shield; the 2026-06-26/27 sections add Mandiant detail but never correct the headline, summary, action or 'No fixed release is available'. Cisco's advisory guidance was also to upgrade, not 'restrict management-plane access'
   - Ground truth: Cisco privesc advisory Fixed Releases: 20.9.9.2, 20.12.7.2, 20.15.4.5, 20.15.5.3, 20.18.3.1, 26.1.1.2 (v1.8 2026-JUN-12 "Changed advisory status from interim to final"); v1.9 2026-JUL-15 "Live Protect shield availability" (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-privesc-4uxFrdzx)
   - Fix: Correct title/headline/summary/action/analysis to 'fixed in 20.9.9.2 / 20.12.7.2 / 20.15.4.5 / 20.15.5.3 / 20.18.3.1 / 26.1.1.2; Live Protect shield is temporary partial protection'
2. [factual-error] **cves[CVE-2026-20245]** — claim: "type: auth-bypass; vector: zero-click; auth: pre-auth; cvss: n/a"
   - Defect: CVE-2026-20245 is an authenticated local command injection requiring netadmin (CVSS 7.8, AV:L/PR:L); the entry's own body says netadmin is required. It was added to KEV 2026-06-09 (CWE-116) but status omits cisa-kev
   - Ground truth: Cisco: "authenticated, local attacker to execute arbitrary commands as root ... the attacker must have netadmin privileges"; Base 7.8 CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H; KEV dateAdded 2026-06-09 (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-privesc-4uxFrdzx)
   - Fix: type priv-esc, vector local, auth post-auth, cvss 7.8, add cisa-kev
3. [imprecision] **cves[CVE-2026-20127], cves[CVE-2026-20182]** — claim: "cvss: n/a"
   - Defect: Both are scored by Cisco at 10.0 and both are in KEV (2026-02-25 and 2026-05-14) but statuses omit cisa-kev
   - Ground truth: Cisco rpa / rpa2: "Base 10.0"; KEV dateAdded 2026-02-25 (20127), 2026-05-14 (20182) (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-rpa2-v69WY2SW)
   - Fix: cvss 10.0, add cisa-kev
4. [imprecision] **body; summary** — claim: "a second actively-exploited zero-day in Catalyst SD-WAN Manager"
   - Defect: 'Second' is unsupported: Cisco's own advisory names CVE-2026-20182 and CVE-2026-20127 as earlier exploited flaws and NCSC-CH says 'a new actively exploited zero-day'
   - Ground truth: NCSC-CH update 05.06.2026: "A new actively exploited zero-day (CVE-2026-20245, HIGH)" (https://security-hub.ncsc.admin.ch/#/posts/12579)
   - Fix: Drop 'second'
5. [factual-error] **Update 2026-06-26 and record summary** — claim: "zero-day at a communications service provider from late 2025 through March 2026 — months before the patch"
   - Defect: Mandiant dates the CVE-2026-20245 exploit to April 2026; late 2025-January and March 2026 are rogue peering events; the victim is 'a service provider', not 'communications'; Cisco's advisory is 2026-06-04
   - Ground truth: Mandiant: "in April 2026, after establishing an SSH session with the admin account, the threat actor exploited CVE-2026-20245"; "multiple unauthorized peering connections ... From late 2025 to January 2026"; "a threat actor targeting SD-WAN infrastructure at a service provider" (https://cloud.google.com/blog/topics/threat-intelligence/zero-day-exploitation-cisco-catalyst-sd-wan-manager)
   - Fix: Say 'exploited as a zero-day in April 2026 after rogue peering access from late 2025'; delete 'communications'
6. [factual-error] **Update 2026-06-26 / 2026-06-27 (chain)** — claim: "a peering-authentication-bypass foothold (CVE-2026-20127 / CVE-2026-20182) into SSH as `vmanage-admin`"
   - Defect: Mandiant says the peering connections only 'possibly' used 20127/20182 and that March connections hit a device unaffected by 20127 that Cisco confirmed did not use 20182 (stolen certificate material possible); the entry states the link as fact. NCSC-CH asserts it but Mandiant does not
   - Ground truth: Mandiant: "It is possible that these connections occurred due to the exploitation of CVE-2026-20127 or CVE-2026-20182"; "Cisco confirmed that these connections did not leverage CVE-2026-20182 either, and could instead be using stolen certificate material" (https://cloud.google.com/blog/topics/threat-intelligence/zero-day-exploitation-cisco-catalyst-sd-wan-manager)
   - Fix: Hedge: 'possibly 20127/20182 for late-2025 activity; March access not via 20182 per Cisco'
7. [factual-error] **Update 2026-06-26** — claim: "with anti-forensic clean-up (admin-password change-then-revert, history/syslog deletion)"
   - Defect: Mandiant does not report history or syslog deletion; it reports deletion of the actor's own files, config restoration and a validation script
   - Ground truth: Mandiant: "the threat actor deleted all files they created, including evil_tenant.csv, and restored any system configurations they modified" (https://cloud.google.com/blog/topics/threat-intelligence/zero-day-exploitation-cisco-catalyst-sd-wan-manager)
   - Fix: Replace with 'file deletion, config restoration, password revert'
8. [imprecision] **Update 2026-06-27 and record summary** — claim: "the first complete TTP chain"
   - Defect: 'First complete' is not claimed by Mandiant
   - Ground truth: Mandiant post makes no such claim (https://cloud.google.com/blog/topics/threat-intelligence/zero-day-exploitation-cisco-catalyst-sd-wan-manager)
   - Fix: Delete 'first complete'
9. [imprecision] **frontmatter evidence[]; techniques; classification** — claim: "techniques: []"
   - Defect: Vulnerability entry with empty techniques[], classification null and affected_products []; evidence[] quotes are entry sentences ('ctipilot v2 brief (migrated)'), not page passages; attacker-chosen artefact names (`evil_tenant.csv`, `troot`) are file/account indicators
   - Ground truth: org profile: every entry carries classification; vulnerability entries need non-empty techniques[] (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-privesc-4uxFrdzx)
   - Fix: Populate techniques (T1190, T1068, T1136.001), affected_products (Cisco Catalyst SD-WAN Controller/Manager/Validator), classification

### 2026-06-26/cisco-catalyst-sd-wan-manager-cve-2026-20245 — factual-error
1. [factual-error] **summary; body para 1** — claim: "exploited at a communications service provider from late 2025 through March 2026, months before Cisco's advisory"
   - Defect: Mandiant: the CVE-2026-20245 exploit was observed in April 2026 (rogue peering from late 2025/March); the victim is 'a service provider'; Cisco published 2026-06-04
   - Ground truth: Mandiant: "in April 2026 ... the threat actor exploited CVE-2026-20245 by executing the following command to upload a file named evil_tenant.csv" (https://cloud.google.com/blog/topics/threat-intelligence/zero-day-exploitation-cisco-catalyst-sd-wan-manager)
   - Fix: Say 'exploited as a zero-day in April 2026 at a service provider, about two months before Cisco's 2026-06-04 advisory'
2. [factual-error] **body, Kill chain, Initial access** — claim: "the actor reached an authenticated position by abusing peering-authentication-bypass flaws CVE-2026-20127 / CVE-2026-20182 to enrol unauthorised peering and obtain SSH as the `vmanage-admin` account"
   - Defect: Presented as established; Mandiant says 'possible' and records Cisco's confirmation that March connections did not use 20182 on a device unaffected by 20127
   - Ground truth: Mandiant: "It is possible that these connections occurred due to the exploitation of CVE-2026-20127 or CVE-2026-20182" (https://cloud.google.com/blog/topics/threat-intelligence/zero-day-exploitation-cisco-catalyst-sd-wan-manager)
   - Fix: Hedge as Mandiant does
3. [factual-error] **body, Kill chain, Defense evasion** — claim: "and deleted command history, syslog entries, and the uploaded files after use"
   - Defect: Mandiant reports deleted files and restored configurations, not history or syslog deletion; T1070.003 (Clear Command History) is therefore unsupported
   - Ground truth: Mandiant: "deleted all files they created, including evil_tenant.csv, and restored any system configurations they modified" (https://cloud.google.com/blog/topics/threat-intelligence/zero-day-exploitation-cisco-catalyst-sd-wan-manager)
   - Fix: Replace with file deletion/config restoration (T1070.004)
4. [imprecision] **body, The vulnerability** — claim: "the feature that ingests a tenant-list CSV fails to sanitise file content before it reaches a shell context"
   - Defect: Cisco's page (cited) says 'a crafted file' via the CLI of Controller, Manager and Validator; the tenant-list CSV detail is Mandiant's, and Cisco's IOC examples show other upload handlers (vsmart serial numbers, chassis numbers)
   - Ground truth: Cisco: "A vulnerability in the CLI of Cisco Catalyst SD-WAN Controller ..., Manager ..., and Validator ... could allow an authenticated, local attacker to execute arbitrary commands as root by supplying a crafted file" (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-privesc-4uxFrdzx)
   - Fix: Cite Mandiant for the tenant CSV; state all three components affected
5. [imprecision] **cves[CVE-2026-20245].status; body Hardening** — claim: "as there is no workaround"
   - Defect: KEV listing (dateAdded 2026-06-09) missing from status; Cisco added a Live Protect shield (2026-07-15) offering temporary partial protection
   - Ground truth: Cisco: "Cisco has released a Live Protect shield for CVE-2026-20245 ... This shield offers only temporary partial protection." (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-privesc-4uxFrdzx)
   - Fix: Add cisa-kev; mention the shield
6. [imprecision] **body, Hunt and detection concepts** — claim: "vManage's own health dashboards do not surface OS-level account creation"
   - Defect: Uncited claim about vManage dashboards
   - Ground truth: Mandiant and Cisco do not discuss dashboards (https://cloud.google.com/blog/topics/threat-intelligence/zero-day-exploitation-cisco-catalyst-sd-wan-manager)
   - Fix: Cite or delete
7. [imprecision] **ATT&CK ids in prose** — claim: "T1078.004"
   - Defect: T1078.004 is 'Cloud Accounts'; the account is the on-box vmanage-admin default account
   - Ground truth: attack/enterprise-attack.json: T1078.004 Cloud Accounts (docs/pipeline.md)
   - Fix: Use T1078 / T1078.001
8. [imprecision] **evidence[0]** — claim: "Mandiant's Google Threat Intelligence Group published a forensic reconstruction of an intrusion in which Cisco Catalyst SD-WAN Manager (formerly vManage) was compromised through CVE-2026-20245 as a zero-day"
   - Defect: evidence is the entry's own sentence (publisher 'ctipilot v2 brief (migrated)'), not a page passage; no classification/techniques
   - Ground truth: Mandiant page does not contain this sentence (https://cloud.google.com/blog/topics/threat-intelligence/zero-day-exploitation-cisco-catalyst-sd-wan-manager)
   - Fix: Replace with a verbatim Mandiant quote
9. [imprecision] **frontmatter classification / techniques[]** — claim: "(absent)"
   - Defect: Entry carries no `classification` block and no `techniques[]` (migrated schema-1 record); a vulnerability entry needs both
   - Ground truth: org profile: every entry carries classification {reliability, credibility}; vulnerability entries need a non-empty techniques[] (docs/pipeline.md)
   - Fix: Add classification (e.g. primary vendor/CNA source, corroborated) and techniques[] (T1190) in the survivor via a changelog record

### 2026-05-19/cve-2026-42231-42232-44789-44790-44791-n8n-self-hosted-autom — factual-error
1. [factual-error] **body paragraph 1; summary** — claim: "n8n published five Critical security advisories on 2026-05-18, two on 2026-05-18 (`-42231`, `-42232`)"
   - Defect: Wrong dates: the GHSAs for -42231/-42232 were published 2026-04-22 (CVE records 2026-05-04) and for -44789/-44790/-44791 on 2026-05-13 (CVE records 2026-06-23); 2026-05-18 is only The Hacker News' roundup date. The cited GHSA-q5f4 carries 'Apr 22, 2026'
   - Ground truth: GHSA-q5f4-99jv-pgg5: 'published GHSA-q5f4-99jv-pgg5 Apr 22, 2026'; GHSA-c8xv/57g9/wrwr: 'May 13, 2026'; THN article date 2026-05-18 (https://github.com/n8n-io/n8n/security/advisories/GHSA-q5f4-99jv-pgg5)
   - Fix: Give per-advisory dates (Apr 22 and May 13, 2026) and keep 2026-05-18 only as the THN roundup date
2. [factual-error] **cves[] (all five)** — claim: "vector: user-interaction"
   - Defect: Taxonomy: vector encodes victim interaction only (authenticated, no-interaction bug = zero-click + post-auth); every GHSA vector has UI:N, so user-interaction is wrong. CVE-2026-44790 is an arbitrary file read (CWE-88), not type rce (the body says so itself)
   - Ground truth: GHSA vectors CVSS:4.0/AV:N/AC:L/AT:N/PR:L/UI:N/...; GHSA-57g9: 'inject CLI flags on the Git node's Push operation allowing an attacker to read arbitrary files'; CVE record CWE-88 (https://github.com/n8n-io/n8n/security/advisories/GHSA-57g9-58c2-xjg3)
   - Fix: vector zero-click, auth post-auth for all; 44790 type info-disclosure/arg-injection
3. [factual-error] **evidence[0]** — claim: "n8n addresses five critical prototype pollution and injection flaws (CVE-2026-42231/42232/44791/44789/44790, all CVSS 9.4)"
   - Defect: Quote is not on the cited THN page (paraphrase); the page says 'Round off the list is a set of five critical vulnerabilities impacting n8n -' followed by a bullet list
   - Ground truth: THN: "Round off the list is a set of five critical vulnerabilities impacting n8n -" (https://thehackernews.com/2026/05/ivanti-fortinet-sap-vmware-n8n-patch.html)
   - Fix: Replace with a verbatim THN sentence
4. [imprecision] **summary; headline** — claim: "five chained critical CVEs ... chained prototype-pollution and injection flaws"
   - Defect: The five GHSAs are independent; only 42231 names a chain (Git node SSH ops); 42232/44789/44791 need 'other nodes'; 44790 is a standalone file read. The summary itself then calls 44790 'separate'
   - Ground truth: GHSA-hqr4: "leading to RCE when combined with other nodes"; GHSA-57g9: standalone arbitrary file read (https://github.com/n8n-io/n8n/security/advisories/GHSA-hqr4-h3xv-9m3r)
   - Fix: Say 'five separate critical advisories'
5. [imprecision] **body paragraph 1** — claim: "CVE-2026-42231 (CVSS 4.0: 9.4, CWE-1321) is the root cause"
   - Defect: 42231 is one independent flaw; 44791 bypasses the 42232 fix, not 42231; CWE-1321 is from the CVE record (GHSA page shows 'No CWEs')
   - Ground truth: THN: 'CVE-2026-44791 ... A bypass for CVE-2026-42232' (https://thehackernews.com/2026/05/ivanti-fortinet-sap-vmware-n8n-patch.html)
   - Fix: Drop 'root cause'
6. [imprecision] **affected/fixed versions for -44789/-44790/-44791** — claim: "1.123.43 / 2.20.7 / 2.22.1"
   - Defect: CVE records list the 2.21 branch fixed in 2.21.1 (affected '>= 2.21.0, < 2.21.1'), GHSAs say 2.22.1; the discrepancy is not surfaced
   - Ground truth: CVE-2026-44789 record affected: '< 1.123.43', '>= 2.0.0-rc.0, < 2.20.7', '>= 2.21.0, < 2.21.1'; GHSA-c8xv patched '>= 1.123.43, >= 2.22.1, >= 2.20.7' (https://cveawg.mitre.org/api/cve/CVE-2026-44789)
   - Fix: Add a Contradiction line or verify on the n8n release page
7. [imprecision] **body; GHSA workarounds** — claim: "(absent)"
   - Defect: GHSAs publish temporary mitigations (limit workflow permissions; disable the node via NODES_EXCLUDE) that the entry omits
   - Ground truth: GHSA-q5f4: 'Limit workflow creation and editing permissions to fully trusted users only'; GHSA-57g9: 'Disable the Git node by adding n8n-nodes-base.git to the NODES_EXCLUDE environment variable' (https://github.com/n8n-io/n8n/security/advisories/GHSA-57g9-58c2-xjg3)
   - Fix: Add the vendor workarounds as interim measures
8. [imprecision] **frontmatter classification / techniques[]** — claim: "(absent)"
   - Defect: Entry carries no `classification` block and no `techniques[]` (migrated schema-1 record); a vulnerability entry needs both
   - Ground truth: org profile: every entry carries classification {reliability, credibility}; vulnerability entries need a non-empty techniques[] (docs/pipeline.md)
   - Fix: Add classification (e.g. primary vendor/CNA source, corroborated) and techniques[] (T1190) in the survivor via a changelog record

### 2026-05-19/n8n-prototype-pollution-chain-cve-2026-42231-et-al-authentic — factual-error
1. [factual-error] **body paragraph 1; summary** — claim: "n8n disclosed five Critical CVEs at CVSS 9.4 each on 2026-05-18"
   - Defect: Wrong dates: the GHSAs for -42231/-42232 were published 2026-04-22 (CVE records 2026-05-04) and for -44789/-44790/-44791 on 2026-05-13 (CVE records 2026-06-23); 2026-05-18 is only The Hacker News' roundup date. The cited GHSA-q5f4 carries 'Apr 22, 2026'
   - Ground truth: GHSA-q5f4-99jv-pgg5: 'published GHSA-q5f4-99jv-pgg5 Apr 22, 2026'; GHSA-c8xv/57g9/wrwr: 'May 13, 2026'; THN article date 2026-05-18 (https://github.com/n8n-io/n8n/security/advisories/GHSA-q5f4-99jv-pgg5)
   - Fix: Give per-advisory dates (Apr 22 and May 13, 2026) and keep 2026-05-18 only as the THN roundup date
2. [factual-error] **cves[] (all five)** — claim: "vector: user-interaction"
   - Defect: Taxonomy: vector encodes victim interaction only (authenticated, no-interaction bug = zero-click + post-auth); every GHSA vector has UI:N, so user-interaction is wrong. CVE-2026-44790 is an arbitrary file read (CWE-88), not type rce (the body says so itself)
   - Ground truth: GHSA vectors CVSS:4.0/AV:N/AC:L/AT:N/PR:L/UI:N/...; GHSA-57g9: 'inject CLI flags on the Git node's Push operation allowing an attacker to read arbitrary files'; CVE record CWE-88 (https://github.com/n8n-io/n8n/security/advisories/GHSA-57g9-58c2-xjg3)
   - Fix: vector zero-click, auth post-auth for all; 44790 type info-disclosure/arg-injection
3. [factual-error] **evidence[0]; evidence[1]** — claim: "n8n addresses five critical prototype pollution and injection flaws (CVE-2026-42231/42232/44791/44789/44790, all CVSS 9.4)"
   - Defect: Evidence[0] is not on the THN page; evidence[1] appends 'CVSS:4.0/AV:N/AC:L/AT:N/PR:L/UI:N/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H = 9.4' to the GHSA sentence, a splice (the sentence ends with a period; the vector and score are elsewhere on the page)
   - Ground truth: THN: "Round off the list is a set of five critical vulnerabilities impacting n8n -"; GHSA-q5f4 sentence ends "...achieve remote code execution on the n8n host." (https://thehackernews.com/2026/05/ivanti-fortinet-sap-vmware-n8n-patch.html)
   - Fix: Use verbatim, contiguous quotes
4. [factual-error] **body, Exploitation prerequisites and Hardening** — claim: "Upgrade is the only remediation; no workaround."
   - Defect: GHSAs list temporary mitigations (limit workflow permissions, disable XML/HTTP Request/Git node via NODES_EXCLUDE)
   - Ground truth: GHSA-hqr4: 'Disable the XML node by adding n8n-nodes-base.xml to the NODES_EXCLUDE environment variable. These workarounds do not fully remediate the risk' (https://github.com/n8n-io/n8n/security/advisories/GHSA-hqr4-h3xv-9m3r)
   - Fix: State the vendor workarounds and that they are partial
5. [factual-error] **body, Hardening** — claim: "Apply the vendor patch (n8n `1.123.32` / `2.17.4` / `2.18.1`) — that is the only remediation."
   - Defect: Contradicts the entry's own 'Operators must apply the later branch train' and the GHSAs for -44789/-44790/-44791 (fixed in 1.123.43 / 2.20.7 / 2.22.1)
   - Ground truth: GHSA-c8xv/57g9/wrwr: 'The issue has been fixed in n8n versions 1.123.43, 2.20.7, and 2.22.1.' (https://github.com/n8n-io/n8n/security/advisories/GHSA-c8xv-5998-g76h)
   - Fix: Tell operators to apply 1.123.43 / 2.20.7 / 2.22.1 or later
6. [factual-error] **body paragraph 2** — claim: "CVE-2026-44791 (GHSA-wrwr-h859-xh2r) is "XML Node Prototype Pollution Patch Bypass" — a regression / bypass of the initial xml2js fix"
   - Defect: 44791 bypasses the patch for GHSA-hqr4-h3xv-9m3r (CVE-2026-42232, XML node), not the xml2js webhook fix of CVE-2026-42231
   - Ground truth: GHSA-wrwr: "bypass the patch for GHSA-hqr4-h3xv-9m3r in the XML node"; THN: "A bypass for CVE-2026-42232" (https://github.com/n8n-io/n8n/security/advisories/GHSA-wrwr-h859-xh2r)
   - Fix: Say 'bypass of the CVE-2026-42232 XML-node fix'
7. [factual-error] **headline; summary; body paragraph 1; 'Why this matters' section** — claim: "increasingly deployed by Swiss/EU public-sector teams as a low-code integration bus, by federal data offices for pipeline orchestration"
   - Defect: No source supports adoption by Swiss/EU agencies or federal data offices; 'fast-growing automation substrate inside agencies that have replaced bespoke ETL' and 'typically a federated SSO account' are likewise uncited; 'Expect downstream national-CERT advisories (ANSSI / BSI / NCSC-CH)' is speculation
   - Ground truth: GHSA-q5f4 and THN say nothing about public-sector use (https://thehackernews.com/2026/05/ivanti-fortinet-sap-vmware-n8n-patch.html)
   - Fix: Remove or cite a source for the constituency exposure claims
8. [imprecision] **body, ATT&CK / prerequisites** — claim: "webhook handler as the initial-access exposure for the prototype pollution"
   - Defect: The exploit requires an authenticated user with permission to create or modify workflows; 'commonly expose webhook endpoints to the public internet' and the `__proto__` / `constructor.prototype` payload tokens are uncited elaboration
   - Ground truth: GHSA-q5f4: "An authenticated user with permission to create or modify workflows could exploit this ... " (https://github.com/n8n-io/n8n/security/advisories/GHSA-q5f4-99jv-pgg5)
   - Fix: Map initial access as valid account (T1078) and drop the uncited payload detail
9. [imprecision] **body paragraph 2** — claim: "The root flaw, CVE-2026-42231"
   - Defect: Framed as the root of the cluster although the five CVEs are independent
   - Ground truth: GHSA titles show five separate flaws (https://github.com/n8n-io/n8n/security/advisories/GHSA-q5f4-99jv-pgg5)
   - Fix: Drop 'root flaw'
10. [imprecision] **affected/fixed versions for -44789/-44790/-44791** — claim: "`1.123.43` / `2.20.7` / `2.22.1`"
   - Defect: CVE records give 2.21.1 for the 2.21 branch; GHSA says 2.22.1 (not surfaced)
   - Ground truth: CVE-2026-44790 record affected '>= 2.21.0, < 2.21.1' (https://cveawg.mitre.org/api/cve/CVE-2026-44790)
   - Fix: Verify on the release page; add Contradiction line
11. [imprecision] **frontmatter classification / techniques[]** — claim: "(absent)"
   - Defect: Entry carries no `classification` block and no `techniques[]` (migrated schema-1 record); a vulnerability entry needs both
   - Ground truth: org profile: every entry carries classification {reliability, credibility}; vulnerability entries need a non-empty techniques[] (docs/pipeline.md)
   - Fix: Add classification (e.g. primary vendor/CNA source, corroborated) and techniques[] (T1190) in the survivor via a changelog record

### 2026-05-29/forticlient-ems-cve-2026-35616-actively-exploited-to-push-ek — factual-error
1. [imprecision] **frontmatter cves[].cvss; summary** — claim: "CVSS 9.1"
   - Defect: 9.1 is Fortinet's temporal score; the vendor base score is 9.8 (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H)
   - Ground truth: Fortinet PSIRT: 'CVSSv3 Score 9.8 CVSSv3 Temporal Score 9.1'; NVD (Fortinet CNA): 9.8 CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H (https://fortiguard.fortinet.com/psirt/FG-IR-26-099)
   - Fix: cvss 9.8 (temporal 9.1)
2. [factual-error] **body paragraph 1** — claim: "The vulnerable code path trusts the `X-SSL-CLIENT-VERIFY` HTTP header set by a fronting reverse proxy or load balancer instead of validating client-certificate state itself"
   - Defect: No fronting proxy is involved: EMS's own Apache mod_ssl sets the trusted WSGI variables; the Django middleware also accepts user-supplied X-SSL-CLIENT-VERIFY / X-SSL-CLIENT-CERT headers and checks the chain by DN strings only
   - Ground truth: Bishop Fox: "The Django authentication middleware accepts client certificate information from both trusted WSGI environment variables (set by Apache mod_ssl) and user-controllable HTTP request headers, and Apache was never configured to strip the user-controllable variants." (https://bishopfox.com/blog/api-authentication-bypass-in-forticlient-ems-7-4-5-7-4-6-cve-2026-35616)
   - Fix: Describe the Django/Apache header-trust and DN-only chain validation per Bishop Fox
3. [factual-error] **summary; body paragraph 1** — claim: "as a fake FortiEndpoint_Patch.exe signed under the legitimate fortitray.exe parent"
   - Defect: Nothing is described as signed; the payload is launched on VPN tunnel establishment via a Remote Access Profile on_connect script: fortitray.exe or ipsec.exe -> cmd.exe -> powershell.exe -> FortiEndpoint_Patch.exe
   - Ground truth: AW: "fortitray.exe or ipsec.exe └── cmd.exe └── powershell.exe (download script) └── FortiEndpoint_Patch.exe (credential stealer)" (https://arcticwolf.com/resources/blog/forticlient-ems-exploited-via-cve-2026-35616-to-deliver-ekz-infostealer-disguised-as-a-fortinet-patch/)
   - Fix: Replace 'signed under' with the process lineage
4. [factual-error] **summary; body paragraph 1** — claim: "EKZ copies itself into Chromium/Gecko browser-profile directories ... to clear elevation-validation checks, then dumps encrypted credential and cookie stores via `nss3.dll`; managed endpoints need browser-profile-write hunts"
   - Defect: For Chromium EKZ copies itself into the browser's Application\ directory (install path) to pass Elevation Service path validation; nss3.dll is used for Firefox/Gecko stores only; the log goes to ProgramData; profile-directory write hunts would miss it
   - Ground truth: AW: "copies itself into the browser's Application\ directory, and relaunches from that path to pass Chromium Elevation Service path validation"; "For Firefox and Gecko-family browsers, the stealer locates nss3.dll" (https://arcticwolf.com/resources/blog/forticlient-ems-exploited-via-cve-2026-35616-to-deliver-ekz-infostealer-disguised-as-a-fortinet-patch/)
   - Fix: Hunt for executables created in browser Application\ directories and ProgramData staging
5. [factual-error] **body, Why it matters to us** — claim: "FortiClient EMS is widely deployed across Swiss federal and cantonal network-security estates and across EU public-sector networks."
   - Defect: No source supports deployment prevalence in Swiss federal/cantonal or EU public-sector estates
   - Ground truth: AW, Fortinet PSIRT and Bishop Fox say nothing about deployment (https://arcticwolf.com/resources/blog/forticlient-ems-exploited-via-cve-2026-35616-to-deliver-ekz-infostealer-disguised-as-a-fortinet-patch/)
   - Fix: Remove or cite
6. [imprecision] **event_date** — claim: "event_date: 2026-04-06"
   - Defect: event_date is the KEV listing date; the primary source (Arctic Wolf campaign report) is dated 2026-05-27, the entry's own subject
   - Ground truth: Arctic Wolf post date 2026-05-27 (https://arcticwolf.com/resources/blog/forticlient-ems-exploited-via-cve-2026-35616-to-deliver-ekz-infostealer-disguised-as-a-fortinet-patch/)
   - Fix: event_date 2026-05-27
7. [imprecision] **body paragraph 1; CISA KEV link** — claim: "[CISA KEV since 2026-04-06](https://nvd.nist.gov/vuln/detail/CVE-2026-35616)"
   - Defect: Cites a hard-blocked NVD per-CVE page for the KEV date and the 9.1 score; NVD shows 9.8. KEV date itself is correct
   - Ground truth: KEV: CVE-2026-35616 dateAdded 2026-04-06 (https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)
   - Fix: Cite the KEV JSON/ Fortinet PSIRT
8. [imprecision] **body; summary** — claim: "Patch is FortiClient EMS 7.4.7"
   - Defect: Fortinet also published hotfixes for 7.4.5 and 7.4.6 that are 'sufficient to prevent it entirely' until 7.4.7
   - Ground truth: PSIRT: "urges vulnerable customers to install the hotfix for FortiClient EMS 7.4.5 and 7.4.6 ... In the meantime the hotfix above is sufficient" (https://fortiguard.fortinet.com/psirt/FG-IR-26-099)
   - Fix: Mention the hotfix
9. [imprecision] **evidence[0]** — claim: "Arctic Wolf Labs published technical evidence on 2026-05-27 of an in-the-wild campaign abusing CVE-2026-35616"
   - Defect: evidence is the entry's own sentence ('ctipilot v2 brief (migrated)'), not a page passage
   - Ground truth: AW page does not contain this sentence (https://arcticwolf.com/resources/blog/forticlient-ems-exploited-via-cve-2026-35616-to-deliver-ekz-infostealer-disguised-as-a-fortinet-patch/)
   - Fix: Replace with a verbatim AW quote
10. [imprecision] **frontmatter classification / techniques[]** — claim: "(absent)"
   - Defect: Entry carries no `classification` block and no `techniques[]` (migrated schema-1 record); a vulnerability entry needs both
   - Ground truth: org profile: every entry carries classification {reliability, credibility}; vulnerability entries need a non-empty techniques[] (docs/pipeline.md)
   - Fix: Add classification (e.g. primary vendor/CNA source, corroborated) and techniques[] (T1190) in the survivor via a changelog record

### 2026-05-29/forticlient-ems-cve-2026-35616-ekz-infostealer-kill-chain — factual-error
1. [factual-error] **body, Vulnerable component** — claim: "CVSS:3.1 base 9.1 (`AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N`)"
   - Defect: Wrong base score and vector: vendor base is 9.8 with A:H; 9.1 is the temporal score; the vector with A:N is in no source
   - Ground truth: NVD (Fortinet CNA): baseScore 9.8, CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H; PSIRT 'CVSSv3 Score 9.8 ... Temporal Score 9.1' (https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2026-35616)
   - Fix: CVSS 3.1 base 9.8 (temporal 9.1)
2. [factual-error] **body, Background** — claim: "(separate product, same `X-Forwarded-*` trust pattern)"
   - Defect: CVE-2026-45659 is a SharePoint deserialization RCE (CWE-502), not a header-trust flaw
   - Ground truth: MSRC: "Microsoft SharePoint Remote Code Execution Vulnerability ... Deserialization of untrusted data in Microsoft Office SharePoint allows an authorized attacker to execute code over a network." (https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-45659)
   - Fix: Delete the comparison
3. [factual-error] **body, Vulnerable component and Detection concepts** — claim: "The intended deployment model is that a fronting reverse proxy or load balancer performs the mutual-TLS handshake and stamps that header into the upstream request before forwarding to EMS ... sends exactly that header with value `SUCCESS` as the entire exploit payload"
   - Defect: No fronting proxy: Apache mod_ssl on EMS sets trusted variables and the Django middleware also trusts user-supplied headers; the Nuclei template is a detection check, and the full bypass also needs a forged chain in X-SSL-CLIENT-CERT. Detection bullets built on 'EMS logs X-SSL-CLIENT-VERIFY with peer-certificate fingerprint' and 'reverse proxy in front of EMS' are unsupported; AW's EMS log signals are 'Certificate not found in request header.' then 'Certificate user: fortinet-ca2 ... successfully updated'
   - Ground truth: Bishop Fox: "An attacker who sends both X-SSL-CLIENT-VERIFY: SUCCESS and a forged certificate chain in X-SSL-CLIENT-CERT passes the authentication gate"; Nuclei: "Detects whether Fortinet hotfix FG-IR-26-099 ... is missing by comparing behavioral responses" (https://bishopfox.com/blog/api-authentication-bypass-in-forticlient-ems-7-4-5-7-4-6-cve-2026-35616)
   - Fix: Rewrite mechanism and EMS-side detections per Bishop Fox / AW
4. [factual-error] **body, Exploitation chain; Detection concepts** — claim: "EKZ copies itself into per-browser profile directories under each user's `AppData\Local\Google\Chrome\User Data\<profile>`, `AppData\Roaming\Mozilla\Firefox\Profiles\<profile>`"
   - Defect: Chromium: self-copy goes to the browser's Application\ directory; Gecko: no self-copy, loads nss3.dll; the Sysmon EID 11 profile-directory detection would miss the real behaviour
   - Ground truth: AW: "copies itself into the browser's Application\ directory, and relaunches from that path" (https://arcticwolf.com/resources/blog/forticlient-ems-exploited-via-cve-2026-35616-to-deliver-ekz-infostealer-disguised-as-a-fortinet-patch/)
   - Fix: Correct directory and detection
5. [factual-error] **body, Exploitation chain; Detection concepts** — claim: "push an *Update task* to managed FortiClient endpoints — the malicious PowerShell payload is delivered through the EMS update channel under the trusted `fortitray.exe` parent process and is therefore signed in the operational sense; `fortitray.exe` spawning PowerShell with `-EncodedCommand` / `-enc`"
   - Defect: Delivery is a Remote Access Profile on_connect script on VPN tunnel establishment (fortitray.exe/ipsec.exe -> cmd.exe -> base64 PowerShell); no Update task or update channel; PowerShell's parent is cmd.exe; '-enc' is not stated; 'unsigned binary with --silent install flags' is invented
   - Ground truth: AW: "users can define scripts that automatically run on those endpoint devices upon establishing a tunnel using the on_connect and script directives in the XML-based Remote Access Profile"; "fortitray.exe was observed launching .cmd script files via cmd.exe ... the cmd script launched a malicious base64-encoded PowerShell script" (https://arcticwolf.com/resources/blog/forticlient-ems-exploited-via-cve-2026-35616-to-deliver-ekz-infostealer-disguised-as-a-fortinet-patch/)
   - Fix: Describe the on_connect path and the cmd.exe -> powershell.exe lineage
6. [factual-error] **evidence[0]; evidence[1]** — claim: "Arctic Wolf has observed threat actors actively exploiting CVE-2026-35616 in the FortiClient EMS management API to deliver a novel infostealer payload"
   - Defect: Neither quote is on the cited Arctic Wolf pages (paraphrases of the AW summary)
   - Ground truth: AW page: 'Arctic Wolf observed evidence of CVE-2026-35616 being exploited against FortiClient EMS deployments'; 'Threat actors disguised the credential stealer payload as a Fortinet endpoint update' (https://arcticwolf.com/resources/blog/forticlient-ems-exploited-via-cve-2026-35616-to-deliver-ekz-infostealer-disguised-as-a-fortinet-patch/)
   - Fix: Use verbatim AW sentences
7. [imprecision] **body, Background** — claim: "being the first public exploitation-chain narrative tying the bypass to a downstream credential-theft payload"
   - Defect: 'First' and 'vendor coverage at disclosure focused on the auth-bypass primitive' are not stated by Arctic Wolf or Fortinet
   - Ground truth: AW page makes no priority claim (https://arcticwolf.com/resources/blog/forticlient-ems-exploited-via-cve-2026-35616-to-deliver-ekz-infostealer-disguised-as-a-fortinet-patch/)
   - Fix: Delete 'first public'
8. [imprecision] **body, Vulnerable component** — claim: "EPSS 43.2 % at the 97.6th percentile."
   - Defect: Point-in-time figure uncited; EPSS was 0.432 / 97.6th on 2026-05-28 but is 0.091 / 95.3rd on 2026-10-16
   - Ground truth: FIRST EPSS API: 2026-05-28 epss 0.43209 percentile 0.97559; 2026-10-16 epss 0.09098 percentile 0.95252 (https://api.first.org/data/v1/epss?cve=CVE-2026-35616)
   - Fix: Date-stamp or drop EPSS
9. [imprecision] **body, Exploitation chain; sources** — claim: "Compromise Software Supply Chain — EMS as distribution vector ... System Binary Proxy Execution via the trusted FortiTray binary"
   - Defect: ATT&CK mapping is inferential (pushing scripts via the management server fits T1072 Software Deployment Tools); the KEV and NVD links are hard-blocked generic/per-CVE pages
   - Ground truth: attack/enterprise-attack.json: T1072 Software Deployment Tools active (https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)
   - Fix: Map T1072; cite KEV JSON / PSIRT
10. [imprecision] **body, Exploitation prerequisites** — claim: "AD-joined EMS, MFA-protected EMS console accounts, and other authentication controls applied to interactive logons are **not** in the request path the spoofed header bypasses."
   - Defect: Uncited analytic claim
   - Ground truth: Bishop Fox/AW do not discuss these controls (https://bishopfox.com/blog/api-authentication-bypass-in-forticlient-ems-7-4-5-7-4-6-cve-2026-35616)
   - Fix: Cite or delete
11. [imprecision] **frontmatter classification / techniques[]** — claim: "(absent)"
   - Defect: Entry carries no `classification` block and no `techniques[]` (migrated schema-1 record); a vulnerability entry needs both
   - Ground truth: org profile: every entry carries classification {reliability, credibility}; vulnerability entries need a non-empty techniques[] (docs/pipeline.md)
   - Fix: Add classification (e.g. primary vendor/CNA source, corroborated) and techniques[] (T1190) in the survivor via a changelog record

### 2026-06-13/cve-2026-48558-simplehelp-rmm-unauthenticated-oidc-authentic — factual-error
1. [factual-error] **summary; actions[0]; body** — claim: "bypasses IdP MFA"
   - Defect: Wrong MFA claim: Horizon3 says the SimpleHelp MFA requirement is bypassed because a technician can self-register an MFA method on first login; nothing says IdP-enforced MFA is bypassed
   - Ground truth: Horizon3: "Even when the SimpleHelp server is configured to enforce MFA for technicians, this issue allows the attacker to bypass this mechanism because on first login, technicians can self-register their own MFA method." (https://horizon3.ai/attack-research/disclosures/cve-2026-48558-simplehelp-authentication-bypass-iocs/)
   - Fix: Say 'bypasses SimpleHelp-enforced MFA via first-login MFA self-registration'
2. [imprecision] **body paragraph 1** — claim: "fails to verify the cryptographic signature of OIDC identity tokens presented at login when OIDC authentication is enabled ([Horizon3.ai, 2026-06-12]"
   - Defect: Horizon3 withholds technical detail and does not mention signatures; the signature-verification flaw is stated by the CVE record (CWE-347) and KEV. 'forged, unsigned token' is also not what the CVE says ('accepted without verifying their cryptographic signature')
   - Ground truth: Horizon3: "At this time, we will not be releasing any more technical details surrounding the vulnerability"; CVE record: "identity tokens submitted during login are accepted without verifying their cryptographic signature" (https://horizon3.ai/attack-research/disclosures/cve-2026-48558-simplehelp-authentication-bypass-iocs/)
   - Fix: Cite the CVE record/KEV for the signature clause
3. [imprecision] **cves[CVE-2026-48558]; tags** — claim: "poc-public"
   - Defect: poc-public is unsupported by the cited sources (Horizon3 withholds details); the CVE record (CNA VulnCheck, published 2026-06-12) already carried CVSS 3.1 10.0 / 4.0 9.5; the finding is now KEV-listed (2026-06-29) and exploited (Blackpoint/BleepingComputer), so the table's 'KEV No / Exploited No (research PoC)' is superseded
   - Ground truth: CVE record metrics: cvssV3_1 10 CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H; cvssV4_0 9.5; KEV dateAdded 2026-06-29 (https://cveawg.mitre.org/api/cve/CVE-2026-48558)
   - Fix: cvss 10.0 (3.1), add exploited + cisa-kev, drop poc-public unless a primary shows a PoC
4. [imprecision] **body paragraph 1** — claim: "SimpleHelp patched it in versions 5.5.16 and the 6.0 RC2 prerelease (Security Notice 2026-05); servers running 5.5.15 and earlier are affected ([SimpleHelp, 2026-06-12]"
   - Defect: Date is wrong: the vendor notice is the May 2026 notice, 5.5.16 is build 20260526, and the page does not name the CVE or OIDC; the vendor's guide says only some 6.0 pre-releases are affected
   - Ground truth: SimpleHelp release news: "5.5.16 20260526-203544 ... This release closes a critical vulnerability"; guide: "Some 6.0 beta and release candidate builds are affected" (https://simple-help.com/security/simplehelp-security-update-2026-05)
   - Fix: Date the fix 2026-05-26 and cite the vendor guide for scope
5. [factual-error] **frontmatter entities; CVE Summary Table** — claim: "actor:shinyhunters ... CVE-2026-35273 | Oracle PeopleSoft PeopleTools (PSEMHUB)"
   - Defect: The actor entity and the PeopleSoft row belong to a different finding (Mandiant ties UNC6240/ShinyHunters to CVE-2026-35273); no source links ShinyHunters to SimpleHelp
   - Ground truth: GTIG: 'attributed to UNC6240 (ShinyHunters) targeting Oracle PeopleSoft' (https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-targets-education-sector-oracle-exploit/)
   - Fix: Remove the entity link and the PeopleSoft row
6. [imprecision] **body, Detection; actions[0]** — claim: "review SimpleHelp access logs for successful Technician authentications preceded by malformed/no-signature OIDC token exchanges"
   - Defect: No source says SimpleHelp logs expose token signature state; Horizon3's IOCs are unfamiliar technician names/emails and server.log lines ('Registering technician login ...', 'Configuration save requested (Forged Attacker ...)'). 'SAML' is in no source; vendor advice is IP restrictions and OIDC avoidance. Action text is truncated '(.'
   - Ground truth: Horizon3: "Review the listed technicians for any unfamiliar technician names or email addresses." (https://horizon3.ai/attack-research/disclosures/cve-2026-48558-simplehelp-authentication-bypass-iocs/)
   - Fix: Use Horizon3's IOCs and the vendor's login-IP restriction
7. [imprecision] **body paragraph 1; ATT&CK** — claim: "SimpleHelp, a self-hosted remote-support/RMM platform common in European MSP estates ... T1078.004 (Valid Accounts)"
   - Defect: 'Common in European MSP estates' is uncited; T1078.004 is 'Cloud Accounts', not a fit for a self-hosted RMM technician account
   - Ground truth: attack/enterprise-attack.json: T1078.004 Cloud Accounts (https://www.bleepingcomputer.com/news/security/hackers-exploit-critical-simplehelp-flaw-deploy-new-djinn-infostealer-taskweaver-malware/)
   - Fix: Use T1078 and drop the European claim
8. [imprecision] **frontmatter classification / techniques[]** — claim: "(absent)"
   - Defect: Entry carries no `classification` block and no `techniques[]` (migrated schema-1 record); a vulnerability entry needs both
   - Ground truth: org profile: every entry carries classification {reliability, credibility}; vulnerability entries need a non-empty techniques[] (docs/pipeline.md)
   - Fix: Add classification (e.g. primary vendor/CNA source, corroborated) and techniques[] (T1190) in the survivor via a changelog record

### 2026-06-30/cve-2026-48558-simplehelp-rmm-oidc-sso-authentication-bypass — factual-error
1. [factual-error] **body; immediate_action** — claim: "a "TaskWeaver" loader persisting through scheduled tasks (`schtasks.exe`) / launchd plists"
   - Defect: Neither the cited BleepingComputer article nor Blackpoint's report describes scheduled-task or launchd persistence; TaskWeaver is a Node.js loader (jquery.js run via node.exe) that fetches Djinn Stealer
   - Ground truth: Blackpoint: "TaskWeaver is a heavily obfuscated Node.js loader, delivered as jquery.js and executed through node.exe" (https://blackpointcyber.com/blog/a-djinn-in-the-machine-taskweavers-node-js-intrusion-chain/)
   - Fix: Delete the persistence claim
2. [factual-error] **evidence[0]; evidence[1]** — claim: "nearly 14,000 SimpleHelp servers exposed, with roughly 7.2% configured to use the vulnerable OIDC authentication method"
   - Defect: Not a contiguous passage: Horizon3 says 'that number has increased to nearly 14,000' and, separately, 'A random sampling of these servers indicated that roughly 7.2% of them were configured to use the vulnerable OIDC authentication method'. evidence[0] (a headline) reads 'Critical SimpleHelp flaw exploited to deploy new stealer malware' on the live page
   - Ground truth: Horizon3: "A random sampling of these servers indicated that roughly 7.2% of them were configured to use the vulnerable OIDC authentication method." (https://horizon3.ai/attack-research/disclosures/cve-2026-48558-simplehelp-authentication-bypass-iocs/)
   - Fix: Quote the two Horizon3 sentences verbatim; update the BC headline
3. [imprecision] **summary; body** — claim: "Horizon3.ai measured ~14,000 internet-exposed instances with ~1,000 carrying a vulnerable OIDC configuration"
   - Defect: ~1,000 is an extrapolation of a 7.2% random sample (BleepingComputer's 'around 1,000'), not a measurement
   - Ground truth: Horizon3: "A random sampling of these servers indicated that roughly 7.2%" (https://horizon3.ai/attack-research/disclosures/cve-2026-48558-simplehelp-authentication-bypass-iocs/)
   - Fix: Say 'roughly 7.2% of a random sample (about 1,000 of nearly 14,000)'
4. [imprecision] **body paragraph 1** — claim: "The OIDC callback handler accepts an identity token without verifying its cryptographic signature (CWE-347) ... ([Horizon3.ai, 2026-06-12]"
   - Defect: The signature/CWE-347 clause is on the CVE record and KEV, not on the cited Horizon3 page
   - Ground truth: CVE record: "identity tokens submitted during login are accepted without verifying their cryptographic signature"; CWE-347 (https://cveawg.mitre.org/api/cve/CVE-2026-48558)
   - Fix: Cite the CVE record / KEV
5. [imprecision] **body, Hunt** — claim: "`SimpleHelpServer.exe`/`SimpleHelp.exe` spawning `powershell.exe`/`cmd.exe`/`wscript.exe` (Sysmon EID 1, parent-image filter)"
   - Defect: Parent/child process names are uncited and omit what was observed: the RMM session launched node.exe to run TaskWeaver
   - Ground truth: Blackpoint: "Alert when RMM software launches Node.js, PowerShell, Python, Deno, or Bun" (https://blackpointcyber.com/blog/a-djinn-in-the-machine-taskweavers-node-js-intrusion-chain/)
   - Fix: Use Blackpoint's hunt guidance
6. [imprecision] **cves[].cvss; summary; immediate_action** — claim: "CVSS 10.0"
   - Defect: 10.0 is the CVSS v3.1 score from the CNA (VulnCheck); the CVSS 4.0 score is 9.5; version unlabeled
   - Ground truth: CVE record: cvssV3_1 10; cvssV4_0 9.5 (https://cveawg.mitre.org/api/cve/CVE-2026-48558)
   - Fix: Label 'CVSS 3.1 10.0 (4.0: 9.5)'
7. [imprecision] **frontmatter classification / techniques[]** — claim: "(absent)"
   - Defect: Entry carries no `classification` block and no `techniques[]` (migrated schema-1 record); a vulnerability entry needs both
   - Ground truth: org profile: every entry carries classification {reliability, credibility}; vulnerability entries need a non-empty techniques[] (docs/pipeline.md)
   - Fix: Add classification (e.g. primary vendor/CNA source, corroborated) and techniques[] (T1190) in the survivor via a changelog record

### 2026-06-19/cisco-ise-cve-2026-20181-cve-2026-20190-an-unauthenticated-c — factual-error
1. [factual-error] **title; headline; 'Why the chain matters more than either CVE'; 'The two primitives'** — claim: "CVE-2026-20190 removes that barrier: it hands an unauthenticated attacker the hashed admin credentials, which can then be cracked offline ... or ... replayed"
   - Defect: The chain is the entry's own construction: Cisco states the two vulnerabilities are independent, says only 'hashed credentials', and CVE-2026-20190 does not affect ISE 3.3 and earlier where CVE-2026-20181 does
   - Ground truth: Cisco: "The vulnerabilities are not dependent on one another. Exploitation of one of the vulnerabilities is not required to exploit the other vulnerability." (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ise-multi-G5WP8vv)
   - Fix: Describe two independent flaws; if a chain is discussed, label it analyst speculation
2. [factual-error] **body, The two primitives** — claim: "explicitly including hashed administrator credentials"
   - Defect: Cisco says 'hashed credentials that could be used in future attacks' via 'crafted traffic'; 'administrator', 'HTTP' and 'specific ISE/ISE-PIC APIs' are not stated, and the administrator link is what the chain relies on
   - Ground truth: Cisco: "gain access to sensitive information, including hashed credentials that could be used in future attacks" (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ise-multi-G5WP8vv)
   - Fix: Use Cisco's wording
3. [factual-error] **cves[CVE-2026-20181], cves[CVE-2026-20190]** — claim: "auth: pre-auth; type: rce"
   - Defect: CVE-2026-20181 needs valid administrative credentials (PR:H); CVE-2026-20190 is an information-disclosure flaw (CWE-285)
   - Ground truth: Cisco: "To exploit this vulnerability, the attacker must have valid administrative credentials."; "CVE-2026-20190: Cisco ISE and ISE-PIC Information Disclosure Vulnerability" (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ise-multi-G5WP8vv)
   - Fix: 20181 auth admin-required; 20190 type info-disclosure
4. [factual-error] **body, Exposure and prerequisites** — claim: "ISE 3.5 is the gap: Patch 3 closes only the unauthenticated read (CVE-2026-20190), and the full fix (Patch 4) is not scheduled until August 2026 — so 3.5 operators carry the authenticated-RCE half for roughly two months"
   - Defect: Cisco's table gives '3.5 Patch 4 (Aug 2026) or hot patch' for CVE-2026-20181 (hot patch for 3.5 Patch 3 on request via TAC); SecurityWeek (cited) says a 3.5 hotfix is available. The entry also omits ISE 3.1 and 3.2, which are affected by 20181 (Patch 12 / Patch 11, Sep 2026 per advisory v1.2); 20190 affects only 3.4/3.5
   - Ground truth: SecurityWeek: "A hotfix for ISE version 3.5 is also available and will be included in version 3.5 Patch 4 in August."; Cisco: "A hot patch for Cisco ISE Release 3.5 Patch 3 is available upon request." (https://www.securityweek.com/critical-command-execution-vulnerability-patched-in-cisco-ise/)
   - Fix: State the 3.5 hot patch, add 3.1/3.2 fixes, and that 20190 is 3.4/3.5 only
5. [imprecision] **body, The two primitives** — claim: "CVE-2026-20181 (CVSS 9.1, path traversal / CWE-22) ... escapes the intended directory and executes arbitrary operating-system commands"
   - Defect: SecurityWeek (cited) says improper input validation; Cisco shows CWE-22 as the weakness label but describes command execution via insufficient validation; 'escapes the intended directory' is the entry's inference
   - Ground truth: SecurityWeek: "the issue exists because user-supplied input is improperly validated, allowing an attacker to send a crafted HTTP request and obtain user-level access to the underlying operating system" (https://www.securityweek.com/critical-command-execution-vulnerability-patched-in-cisco-ise/)
   - Fix: Drop the directory-escape mechanism
6. [imprecision] **summary; body paragraph 1** — claim: "the policy brain of network access control in most large Swiss and European public-sector estates"
   - Defect: 'Most' is an unsourced quantifier about Swiss/European public-sector deployments
   - Ground truth: no cited page discusses deployment prevalence (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ise-multi-G5WP8vv)
   - Fix: Remove or cite
7. [imprecision] **sources[2]** — claim: "https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1989"
   - Defect: (low confidence) The cited CERT-Bund WID-SEC-2026-1989 page is a JavaScript shell no transport could render; nothing in the entry rests on it, but it is not verifiable
   - Ground truth: fetch returned only the WID portal Angular shell (https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1989)
   - Fix: Drop or replace with a readable BSI/CERT-Bund record
8. [imprecision] **frontmatter classification / techniques[]** — claim: "(absent)"
   - Defect: Entry carries no `classification` block and no `techniques[]` (migrated schema-1 record); a vulnerability entry needs both
   - Ground truth: org profile: every entry carries classification {reliability, credibility}; vulnerability entries need a non-empty techniques[] (docs/pipeline.md)
   - Fix: Add classification (e.g. primary vendor/CNA source, corroborated) and techniques[] (T1190) in the survivor via a changelog record

### 2026-06-19/cve-2026-20181-cve-2026-20190-cisco-identity-services-engine — factual-error
1. [factual-error] **title; headline; summary** — claim: "unauthenticated credential read chaining to authenticated root command execution"
   - Defect: Chain asserted as fact: Cisco says the two vulnerabilities are not dependent on one another; the summary also says the attacker 'reuse[s] them to reach' 20181
   - Ground truth: Cisco: "Exploitation of one of the vulnerabilities is not required to exploit the other vulnerability." (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ise-multi-G5WP8vv)
   - Fix: Describe as two independent flaws
2. [factual-error] **body paragraph 1** — claim: "including hashed administrator credentials — via crafted HTTP requests to specific APIs"
   - Defect: Cisco says 'hashed credentials' via 'crafted traffic'; 'administrator', 'HTTP requests' and 'specific APIs' are not in the advisory
   - Ground truth: Cisco: "view sensitive information on an affected device ... including hashed credentials that could be used in future attacks" (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ise-multi-G5WP8vv)
   - Fix: Use Cisco's wording
3. [factual-error] **cves[CVE-2026-20181], cves[CVE-2026-20190]** — claim: "auth: pre-auth; type: rce"
   - Defect: 20181 requires valid administrative credentials; 20190 is information disclosure
   - Ground truth: Cisco: "the attacker must have valid administrative credentials"; "Information Disclosure Vulnerability" (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ise-multi-G5WP8vv)
   - Fix: auth admin-required; type info-disclosure
4. [factual-error] **summary; body; actions[0]** — claim: "ISE 3.5's full fix slips to August; with 3.5 Patch 3 closing only CVE-2026-20190 in the interim"
   - Defect: A hot patch for 3.5 Patch 3 fixing 20181 is available on request; the action tells 3.5 users to wait for Patch 4; 3.1/3.2 (affected by 20181, fixes Sep 2026) are omitted
   - Ground truth: Cisco table: "3.5 ... 3.5 Patch 4 (Aug 2026) or hot patch"; footnote "A hot patch for Cisco ISE Release 3.5 Patch 3 is available upon request." (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ise-multi-G5WP8vv)
   - Fix: State the hot patch and the 3.1/3.2 fixes
5. [imprecision] **summary** — claim: "A dense critical-patch cycle landed in widely-deployed CH/EU public-sector infrastructure within 36 h: Cisco ISE, pgAdmin 4, NGINX, and Drupal core ... No in-the-wild exploitation is reported for any of these four advisories."
   - Defect: pgAdmin 4, NGINX and Drupal are not discussed or cited anywhere in the entry or its sources; the 36 h window and the no-exploitation statement for them are unsupported
   - Ground truth: Cited sources (Cisco, SecurityWeek, CERT-Bund WID-SEC-2026-1989) cover only Cisco ISE (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ise-multi-G5WP8vv)
   - Fix: Drop the other three products and the claim
6. [imprecision] **sources[2]** — claim: "https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1989"
   - Defect: (low confidence) The cited CERT-Bund WID-SEC-2026-1989 page is a JavaScript shell no transport could render; nothing in the entry rests on it, but it is not verifiable
   - Ground truth: fetch returned only the WID portal Angular shell (https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1989)
   - Fix: Drop or replace with a readable BSI/CERT-Bund record
7. [imprecision] **frontmatter classification / techniques[]** — claim: "(absent)"
   - Defect: Entry carries no `classification` block and no `techniques[]` (migrated schema-1 record); a vulnerability entry needs both
   - Ground truth: org profile: every entry carries classification {reliability, credibility}; vulnerability entries need a non-empty techniques[] (docs/pipeline.md)
   - Fix: Add classification (e.g. primary vendor/CNA source, corroborated) and techniques[] (T1190) in the survivor via a changelog record

## Lead-only quote decisions
### 2026-07-21/hugging-face-autonomous-ai-agent-production-breach — verbatim (extraction artefact, not a real mismatch)
- Quote: "To gain Internet access, the models identified and exploited a previously unknown zero-day vulnerability in Artifactory, a package registry cache proxy."
- Page's actual wording: "The ExploitGym evaluation environment did not provide the models with direct Internet access. To gain Internet access, the models identified and exploited a previously unknown zero-day vulnerability in [Artifactory⁠(opens in a new window)](https://jfrog.com/blog/jfrog-and-openai-collaboration-on-zero-day-security-findings/), a package registry cache proxy."
- Cause: The reader/markdown rendering turns the hyperlink 'Artifactory' into '[Artifactory<U+2060>(opens in a new window)](url)' (hidden accessibility label plus a word-joiner), so the rendered visible sentence 'zero-day vulnerability in Artifactory, a package registry cache proxy.' is not contiguous in the extracted text. The sentence is only on the first page (hugging-face-model-evaluation-security-incident), under 'Update on July 28, 2026'; the page carries later banners (July 29, August 26) so it has been edited since 2026-07-21, but the entry's 2026-07-30 update post-dates the July 28 text. The second OpenAI page describes the same access as an SSRF through Artifactory, not as a zero-day. (https://openai.com/index/hugging-face-model-evaluation-security-incident/)

### 2026-08-29/exchange-mrsproxy-auth-bypass-cve-2026-62911-poc — verbatim (both original: strings); the pre-pass missed them because the Mastodon page is a JS shell whose post text is only in the og:description/description meta tags
- Quote: "Für die kritische Schwachstelle CVE-2026-62911 in Microsoft Exchange wurde ein PoC-Exploit veröffentlicht ... / Aktuell sind jedoch noch rund 85% der on-premises Exchange-Server in Deutschland für diese ..."
- Page's actual wording: "🚨 Für die kritische Schwachstelle CVE-2026-62911 in Microsoft Exchange wurde ein PoC-Exploit veröffentlicht, der die vollständige Übernahme von Systemen aus der Ferne ohne Authentifizierung ermöglicht. Der Hersteller veröffentlichte am 11.08. einen Patch. Aktuell sind jedoch noch rund 85% der on-premises Exchange-Server in Deutschland für diese Schwachstelle verwundbar. CERT-Bund benachrichtigt deutsche Netzbetreiber seit dem 14.08. regelmäßig zu noch verwundbaren Systemen in ihren Netzen."
- Cause: Text sits in <meta name="description"> / og:description of https://social.bund.de/@certbund/117171896801475447 (og:published_time 2026-08-28T07:14:17Z); a body-text search of the extracted page finds nothing. Re-fetched live today: unchanged. The English translations in quote: are faithful to the original: strings. (https://social.bund.de/@certbund/117171896801475447)

### 2026-09-03/kimsuky-seafood-invoice-lnk-backblaze-b2-c2 — verbatim (markdown escaping artefact)
- Quote: "it is configured to execute ping_<FIRST 4 digits of UUID>.Js approximately every 14 minutes via wscript.Exe"
- Page's actual wording: "The task name is formatted as MicrosoftOffice2016\_<FIRST 4 digits of UUID>, and it is configured to execute ping\_<FIRST 4 digits of UUID>.Js approximately every 14 minutes via wscript.Exe."
- Cause: The reader's markdown escapes the underscore as 'ping\_' (a backslash that is not on the rendered page); the rendered words equal the entry's quote. Page published 2026-09-01T15:00Z, text unchanged. (https://asec.ahnlab.com/en/95217/)

### 2026-09-12/japan-digital-agency-gss-vpn-breach-maintenance-account — verbatim on the archived page; live page removed (404)
- Quote: "The agency said it detected suspicious access from the account of a system maintenance administrator on June 25. ... / "We take it seriously that the incident occurred despite our operations under multi-layered security measures and a 24-hour-a-day, 365-day-a-year surveillance system," Chief Cabinet Secretary Minoru Kihara said at a press conference"
- Page's actual wording: "The agency said it detected suspicious access from the account of a system maintenance administrator on June 25. It then began investigating the incident and found on July 9 that an external third party had repeated unauthorized access since around late May. / "We take it seriously that the incident occurred despite our operations under multi-layered security measures and a 24-hour-a-day, 365-day-a-year surveillance system," Chief Cabinet Secretary Minoru Kihara said at a press conference, adding that the agency would work to prevent a recurrence."
- Cause: The cached body is the nippon.com navigation shell only; the article has since been taken down (404, soft-404 serving the homepage). Page was not edited; it was removed. (https://web.archive.org/web/2026/https://www.nippon.com/en/news/yjj2026091100453/)
- [imprecision] Both Jiji quotes are verbatim, but the cited nippon.com article now returns HTTP 404 (the pre-pass cached only the site navigation shell), so the evidence can no longer be re-verified from the cited URL Fix: Add the archive URL or a Digital Agency/other readable primary as a second source

## Groups
- Group 1: same_finding=True; survivor=2026-05-11/cve-2026-6722-php-soap-extension-use-after-free-in-soap-glob; Same finding (identical CVE set, sources and dates). Survivor 1a has a real summary and event_date; carry 1b's verified mechanism/detection content. Both mis-state affected range, CVE-2026-7262 score/type, and 'no PoC'. Neither carries classification or techniques[].
- Group 2: same_finding=False; survivor=None; Group mixes two findings. 20245's Cisco advisory names 20182/20127 as ways to obtain netadmin, so 2c correctly references them; 2c already folded 2026-06-26/mandiant-publishes-... and 2026-06-27/mandiant-documents-... (merged_from). 2d duplicates the 2c update content.
- Group 3: same_finding=True; survivor=2026-05-19/cve-2026-42231-42232-44789-44790-44791-n8n-self-hosted-autom; Same finding (identical five CVEs, sources). Both entries carry the wrong advisory date, vector user-interaction, and a non-verbatim THN quote. Survivor 3a is the shorter entry without the unsupported Swiss/EU adoption narrative; 3b's verified items are the CVSS vector and prerequisites.
- Group 4: same_finding=True; survivor=2026-05-29/forticlient-ems-cve-2026-35616-actively-exploited-to-push-ek; Same finding (same CVE, sources, date). Both mis-describe the exploit mechanism (reverse-proxy model), the EKZ self-copy location and the delivery lineage; 4b adds a wrong CVSS vector and a false CVE-2026-45659 comparison. Survivor 4a, rewritten from AW + Bishop Fox + PSIRT; 4b's verified items are the PSIRT/KEV dates and EPSS. 4b's two evidence quotes are not on the Arctic Wolf pages.
- Group 5: same_finding=True; survivor=2026-06-30/cve-2026-48558-simplehelp-rmm-oidc-sso-authentication-bypass; Same finding; 5b supersedes 5a (KEV 2026-06-29 and exploitation after 5a's 'KEV No / Exploited No'). Keep 5a's June 12-13 coverage as the original delta; correct 5a's IdP-MFA, poc-public, shinyhunters and PeopleSoft content rather than carrying them.
- Group 6: same_finding=True; survivor=2026-06-19/cve-2026-20181-cve-2026-20190-cisco-identity-services-engine; Same finding. Both build on a chain the vendor expressly denies, record 20181 as pre-auth and 20190 as rce, omit the 3.5 hot patch and ISE 3.1/3.2, and say 'hashed administrator credentials'. Survivor 6b; fold in 6a's detection concepts only after removing chain-dependent content.

## Global notes
- 13 of 14 batch entries (all except 2026-06-06/cve-2026-20245-...) carry neither classification nor techniques[] (migrated schema-1 records); 2026-06-06/... has techniques: [] and classification: null. ATT&CK ids appear only in prose; T1562, T1562.001 and T1070.002 (entry 2a) are revoked in v20.
- None of the batch CVEs except CVE-2026-20182, CVE-2026-20245, CVE-2026-20127, CVE-2026-35616 and CVE-2026-48558 is in CISA KEV (catalogue 2026.10.16); CVE-2026-20245 and CVE-2026-20127 are KEV-listed but the entries' status omits cisa-kev.
