**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-19T05:23:27Z · ended_at=2026-11-19T05:56:24Z · duration_seconds=1977

## Verification report — 2026-11-19T0355Z-intel (iteration 1)

Scope: 6 new entries, 8 updated entries, the run record; every one of the 305 ledger claims has a verdict row in `verification.iter1.claims.yaml` (288 ok, 9 F4, 5 F3, 1 F5, 1 F13, 1 unreadable). First pass, cold read, no deltas block. Pages were read from the gate-saved quote bodies where they existed and re-fetched otherwise (Calif, Oracle CSPU, OpenJDK, Upwind, Equixly, Talos, Tenable, VulnCheck, Cisco, Fortinet, BACS, CVE JSON records via cveawg, Drupal advisory feed, CERT-Bund CSAF, HPE CSAF, NCSC.ch hub posts, CISA alert through WebFetch). The CISA alert quote "based on evidence of active exploitation" was confirmed on the live alert page. Not readable by any rung: the HPE support portal bulletin page (JS shell; WebFetch empty) and drupal.org SA-CORE-2026-018 and PSA pages (client challenge; fields read from Drupal's own security RSS feed items).

### Citation does not support the claim

1. **F3 #1** — `entries/2026-06-16/obsidian-security-a-three-cve-chain-turns-any-litellm-user-i` — LiteLLM: Obsidian source and inline citations dated 2026-06-15 (sources[0].date, three '[Obsidian Security, 2026-06-15]' cites, event_date)
   - source: https://www.obsidiansecurity.com/blog/litellm-privilege-escalation-rce
   - The Obsidian page's own byline reads 'Published: June 11, 2026 | Updated: September 7, 2026' and its timeline ends 'June 11, 2026 - Published the research'; 2026-06-15 is The Hacker News's date. A 4-day drift on a primary source; cite 2026-06-11.

2. **F3 #2** — `entries/2026-06-16/obsidian-security-a-three-cve-chain-turns-any-litellm-user-i` — LiteLLM body: 'VulnCheck scores CVE-2026-47102 at CVSS 8.8 (3.1), and Obsidian rates the chained impact CVSS 9.9; ... man-in-the-gateway' cited only to Obsidian
   - source: https://www.obsidiansecurity.com/blog/litellm-privilege-escalation-rce
   - Adjacency: the Obsidian page carries the 9.9 chain score, master/salt key, DATABASE_URL and man-in-the-gateway text but no VulnCheck 8.8 (3.1) score (0 matches); that figure is on https://thehackernews.com/2026/06/litellm-vulnerability-chain-lets-low.html ('VulnCheck ... scores it 8.7 under CVSS 4.0, 8.8 under 3.1'). Add the THN citation to the clause.

3. **F3 #3** — `entries/2026-11-11/confluence-dc-cve-2026-90436-apache-axis-remote-api-rce` — Confluence body: 'BSI CERT-Bund's bulletin rates the issue high'
   - source: https://wid.cert-bund.de/.well-known/csaf/white/2026/wid-sec-w-2026-4427.json
   - The CERT-Bund CSAF for WID-SEC-W-2026-4427 carries aggregate_severity 'kritisch' (critical), and the bulletin's revision 2 (2026-11-16/17, summary 'Exploit aufgenommen') records that an exploit exists; the entry still says 'high' and dates the source 2026-11-10. Correct to critical and note the revision.

4. **F3 #4** — `entries/2026-11-19/redcap-cve-2026-90817-unauth-survey-rce-exploited-kev` — REDCap Detection: 'web access logs for POSTs ... and for a php:// stream in the file-name field; transient Blade-template files ...' cited to Unit 42
   - source: https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2026-10-07-XMRig-campaign-through-CVE-2026-90817.txt
   - Adjacency: Unit 42 gives the POST URL with __passthru=%2569ndex.php and route=DataImportController:index but says nothing of a php:// stream or the file-name field; that detail is Securifera's (POST[fname]). A POST-body field is also not visible in ordinary web access logs; say it needs body-capable (WAF/proxy) logging and cite Securifera for it.

5. **F3 #5** — `entries/2026-11-19/airlock-gateway-cve-2026-19707-smart-form-protection` — Airlock title/summary: 'overflows a heap buffer in the Smart Form Protection entity decoder' / 'overflow a heap buffer in the Smart Form Protection feature' (low confidence)
   - source: https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-128505
   - The cited ENISA record says 'buffer overflow' and never 'heap' (0 matches); 'heap' and 'HTML entity decoder' come from the CVE record's CNA title 'Heap out-of-bounds write in the Smart Form Protection HTML entity decoder' (CWE-122) at https://cveawg.mitre.org/api/cve/CVE-2026-19707, which no source on the entry cites. True per the CNA, but not supported by the cited page.

6. **F3 #6** — `entries/2026-11-19/tcherber-access-broker-fortigate-sonicwall-vpn-ldap-sweep` — tcherber body: VMRay 'calls the same developer the likely author of an HVNC remote-control sample, without mentioning VPN access' (low confidence)
   - source: https://www.vmray.com/news/one-leftover-build-path-links-an-infostealer-a-remote-access-tool-and-a-ransomware-family/
   - VMRay says newer Zer0day Stealer versions show 'file-extension-based theft targeting Office documents and VPN configuration files'. It says nothing of VPN access brokerage (the sourcing_note wording is right), but 'without mentioning VPN access' is not literally true; reword to 'without mentioning VPN access brokerage'.

7. **F3 #7** — `entries/2026-11-19/cyberpower-powerpanel-business-system-shell-on-dc; airlock-gateway-cve-2026-19707-smart-form-protection; entries/2026-11-11/confluence-dc-cve-2026-90436-apache-axis-remote-api-rce` — Citation dates equal to the run date rather than the page's own date (low confidence): '[CyberPower, 2026-11-19]' product page; four Airlock docs pages all dated 2026-11-18; Apache announcement thread dated 2026-11-06
   - source: https://www.cyberpower.com/uk/en/product/series/powerpanel_business
   - The CyberPower product page's metadata date is 2022-01-13 and it carries no dateline, so 2026-11-19 is the retrieval date; the Airlock docs pages (changelog 8.6.1, 8.5.3, Smart Form Protection, release/support) show no dateline either (metadata 2011/2024); lists.apache.org shows 'Published Time: Sun, 01 Nov 2026' for the Axis thread against the entry's 2026-11-06 (the oss-security copy is 2026-11-06). Undated pages should say so, as the OptimJack sourcing_note does for Ohey.

8. **F3 #8** — `entries/2026-11-19/nginx-nginx2root-five-unauth-memory-corruption-flaws` — nginx summary: '... which CERT-EU says can lead to code execution with the privileges of the worker process (CVSS 4.0 9.2, high attack complexity)' (low confidence)
   - source: https://cert.europa.eu/publications/security-advisories/2026-022/
   - The parenthetical sits in the clause attributed to CERT-EU, whose page scores all five CVSS 8.1 (3.1) and never mentions 9.2 or attack complexity; the 9.2/AC:H comes from F5's CNA record, NCSC.ch, NCSC-NL, Rapid7 and Wiz. The sourcing_note explains the choice, but the summary reads as CERT-EU's figure; move the parenthetical out of the CERT-EU clause.

### Unsupported / hallucinated facts

9. **F4 #9** — `entries/2026-11-18/cve-2026-114938-java4shell-openjdk-avx512-base64-decoder-rce` — Java4Shell title 'no exploitation reported', headline 'update Java, no attacks yet', summary 'and no source reports attacks'; Tenable relay 'a working, unreleased exploit'
   - source: https://www.tenable.com/blog/java4shell-cve-2026-114938-frequently-asked-questions-about-openjdk-rce-vulnerability
   - The cited Tenable page (updated Nov 18) says 'As of November 18, GreyNoise has reported exploitation attempts against CVE-2026-114938, though GreyNoise has not confirmed any successful exploitation against its sensors' and that GreyNoise saw scanning from a public scanner; it also relays VulnCheck's working RCE exploit 'available to its customers' (VulnCheck: 'A full RCE exploit ... is available to Initial Access Intelligence customers as of 6 PM EST on November 17') and says of Breen's exploit only that 'The post does not say that the exploit has been released' (not 'unreleased'). Rewrite title/headline/summary to say exploitation attempts are reported unconfirmed, a commercial RCE exploit exists, and no confirmed compromise.

10. **F4 #10** — `entries/2026-11-19/idunno-anticsrf-cve-2026-131914-exploited-no-patch-w3wp-rce` — Idunno summary: 'so the fix is to remove the module, rotate the secrets held in the web configuration and check the web root'; actions[0]: 'on any server that ran it while internet-reachable, check IIS logs ... and rotate the machineKey, encryption keys and database credentials'
   - source: https://github.com/mandiant/Vulnerability-Disclosures/blob/master/2026/MNDT-2026-0048.md
   - Mandiant limits rotation and web-root inspection to 'Environments with evidence of exploitation should rotate all secrets stored in Web.config and applicationHost.config ... and inspect webroots for unauthorized files'. The body's Defender takeaway states the condition; the summary and action drop it and attribute an unconditional rotation to Mandiant. State the condition or label the broader step as the entry's own judgement (POST bodies are rarely logged, so evidence may be absent).

11. **F4 #11** — `entries/2026-11-19/cyberpower-powerpanel-business-system-shell-on-dc` — CyberPower techniques: [T1072, T1059.003, T1059.001, T1105, T1003.003, T1574.001]
   - source: https://www.security.com/threat-intelligence/power-management-software-attack-vector
   - Symantec describes 'the typical pattern of the DLL side-loading technique' (upnpcont.exe loading atl.dll). In the pinned ATT&CK v20.1 T1574.001 is 'DLL' (search-order hijacking) and T1574.002 is 'DLL Side-Loading'. Replace T1574.001 with T1574.002.

12. **F4 #12** — `entries/2026-11-19/cyberpower-powerpanel-business-system-shell-on-dc` — CyberPower actions[0]: 'look for pp?????.cmd scripts and for cmd.exe or powershell.exe started under ppbed.exe; where either is found, assume Active Directory credentials are exposed and plan a krbtgt reset' (low confidence)
   - source: https://www.security.com/threat-intelligence/power-management-software-attack-vector
   - Symantec says the product's own event-action feature runs administrator-chosen .cmd scripts via cmd /c under ppbed.exe ('looks like a power-management product launching cmd.exe'); its krbtgt advice applies only 'If you find [the techniques and indicators in this document]'. The action's trigger (any cmd.exe or powershell.exe under ppbed.exe) contradicts the entry's own Triage line (children that are not shutdown or notification routines, no preceding power event) and would drive krbtgt resets on benign installs. Tie the trigger to the Triage discriminators.

13. **F4 #13** — `entries/2026-06-16/obsidian-security-a-three-cve-chain-turns-any-litellm-user-i` — LiteLLM body: 'The chain is fixed in v1.83.14-stable, but Obsidian reports broad under-deployment of the fix.'
   - source: https://www.obsidiansecurity.com/blog/litellm-privilege-escalation-rce
   - Neither the Obsidian page nor The Hacker News says this: Obsidian only says 'Upgrade to v1.83.14-stable or later. This is the first release that contains the complete fix set' (searches for under-deploy, unpatched, adoption, still running return nothing). Inherited from the pre-migration text; remove or source it.

14. **F4 #14** — `entries/2026-11-19/tcherber-access-broker-fortigate-sonicwall-vpn-ldap-sweep` — tcherber actions[0] and Detection: 'sustained sessions ... that reconnect about every 30 seconds' (low confidence)
   - source: https://www.cyderes.com/howler-cell/exposing-tcherber
   - Cyderes says only that forti_vpn.go 'Maintains persistent connectivity with a 30-second reconnect loop' (a retry interval in the wrapper). A session that is sustained does not reconnect every 30 seconds; that rate would appear only while the tunnel fails repeatedly. Present it as the client's retry interval, not as an observable session cadence.

15. **F4 #15** — `entries/2026-11-18/drupal-core-critical-release-2026-11-18-psa-2026-11-16` — Drupal Update section: 'the advisories list neither a component beyond the installer nor any exploitation' (low confidence)
   - source: https://www.drupal.org/security/rss.xml
   - SA-CORE-2026-018 (listed in the same sentence's section) is a 'Gadget chain' in core's unserialize path, a flaw outside the installer; the sentence contradicts the section's first paragraph. If it means the PSA's 'more than one configuration is affected' is not itemised, say that.

16. **F4 #16** — `entries/2026-06-16/obsidian-security-a-three-cve-chain-turns-any-litellm-user-i` — LiteLLM cves[CVE-2026-47102]: affected 'LiteLLM before v1.83.14-stable', fixed 'v1.83.14-stable' (low confidence)
   - source: https://cveawg.mitre.org/api/cve/CVE-2026-47102
   - The per-CVE authority (VulnCheck CNA record) says 'LiteLLM prior to 1.83.10' (CVE-2026-47101: prior to 1.83.14). The chain-level fix is v1.83.14, but the per-CVE field should follow the record, or the chain-level reading should be labelled as such.

### Claims missing inline citation

17. **F5 #17** — `entries/2026-11-18/cve-2026-114938-java4shell-openjdk-avx512-base64-decoder-rce` — Java4Shell cves[].fixed: 'Oracle builds ... and 8u513-perf' (also actions[0])
   - source: https://www.oracle.com/java/technologies/javase/8u513-perf-relnotes.html
   - No cited page names 8u513-perf as a fixed build: Oracle's CSPU lists only 8u511b33-perf as affected and Upwind lists fixed .1 builds for 17, 21, 25 and 27 only. Oracle's 8u513-perf release notes (dated 2026-11-17) exist and say only 'fixes for security vulnerabilities described in the Oracle Critical Patch Update'. Cite that page or soften (low confidence that the build is wrong).

18. **F5 #18** — `entries/2026-10-23/hpesbnw05162-hpe-aruba-aos-8-aos-10-72-cves-19-unauth` — HPE Exposure: 'HPE says every compatible hardware model is affected and that its own hardware list is illustrative only' (low confidence)
   - source: https://support.hpe.com/hpesc/public/docDisplay?docId=hpesbnw05162en_us&docLocale=en_US
   - The cited portal page is a JavaScript shell on extract and WebFetch returned nothing; the statement is not in the CSAF JSON or the text advisory read this pass (both carry the version ranges, workaround and revision text). Re-source to a readable page or drop; claim verdict unreadable.

### Needs more research

19. **F8 #19** — `entries/2026-11-19/nginx-nginx2root-five-unauth-memory-corruption-flaws` — nginx action/takeaway: 'disable HTTP/2 ... blocks only CVE-2026-123007 and CVE-2026-123633' and nothing for the other three
   - source: https://xint.io/blog/nginx2root-remote-code-execution
   - The cited sources give interim measures for the rest: Xint 3.3.2 (fixed upstream group instead of request-time DNS lookups for CVE-2026-123634), 3.3.3 (remove QUIC listeners and http3 for CVE-2026-121810), 3.3.4 (bind or firewall the mail listeners for CVE-2026-113425); CERT.at: 'Als Mitigation fuer CVE-2026-113425 empfiehlt F5, die Mail-Listener auf vertrauenswuerdige Netzwerke zu beschraenken'; F5's CNA workarounds for CVE-2026-123634 ('Avoid using SSI or mirror directives ...') and CVE-2026-113425 ('Restrict listeners to trusted networks'). A reader who cannot patch is told only about two of five.

20. **F8 #20** — `entries/2026-11-19/nginx-nginx2root-five-unauth-memory-corruption-flaws` — nginx2root title/body: no explanation of 'root'; body quotes only Rapid7's 'execution as the master process or root is not established'
   - source: https://xint.io/blog/nginx2root-remote-code-execution
   - Xint, the source of the name, chained CVE-2026-123007 with a separate unpatched Linux kernel SCTP flaw to 'gain root privileges on the host' and escape a Docker container ('Until a kernel patch is available, we are withholding most of the details'). The entry omits the chain, so the worker-only privilege assumption and the container/kernel hardening angle are missing; mention it with Xint as the source.

21. **F8 #21** — `entries/2026-11-19/nginx-nginx2root-five-unauth-memory-corruption-flaws` — nginx headline/actions: 'five unauthenticated worker-RCE flaws' ... 'five unauthenticated flaws reach code execution as the worker'
   - source: https://www.cert.at/de/warnungen/2026/11/kritische-sicherheitslucken-in-nginx-plus-und-nginx-open-source-updates-verfugbar
   - F5's own framing (CNA records, CERT.at 'Auswirkungen') is worker crash or memory corruption, with code execution 'on systems with ASLR disabled or when the attacker can bypass ASLR'; CERT-EU, Wiz, Rapid7 and Xint show ASLR-bypassing RCE for the flaws they tested. The sibling entry of 2026-10-20 states the ASLR condition; this one drops it, leaving the exploitation prerequisite and the vendor's DoS-first rating out of the exposure picture.

22. **F8 #22** — `entries/2026-11-18/cve-2026-114938-java4shell-openjdk-avx512-base64-decoder-rce` — Java4Shell update: Detection line trimmed and Fortinet impact reduced to 'lists none as affected' (record fields name body, summary does not)
   - source: https://www.upwind.io/blog/java4shell-what-we-know-now-and-what-comes-next/
   - The update removed three source-supported hunting facts without saying so: Upwind's 'bursts of IllegalArgumentException from java.util.Base64$Decoder' and 'bursts of restarts', Equixly's 'Do not expect the log to name Base64: the crash comes later', and Talos's Snort coverage of malformed Base64 (SIDs 1:67502-1:67513). It also reduces Fortinet's page to 'lists none as affected' although the page names some 50 products under investigation (FortiManager, FortiAnalyzer, FortiMail, FortiAuthenticator, FortiSandbox, FortiEDR and others) and confirms FortiOS, FortiProxy and FortiWeb not impacted. Restore the detection hooks and state the FortiOS-not-impacted/under-investigation split.

23. **F8 #23** — `entries/2026-06-16/obsidian-security-a-three-cve-chain-turns-any-litellm-user-i` — LiteLLM Exposure/Detection/action name only POST /guardrails/test_custom_code; takeaway omits the post-compromise audit
   - source: https://www.obsidiansecurity.com/blog/litellm-privilege-escalation-rce
   - Obsidian says the production routes 'POST /guardrails and PUT /guardrails/{id}' run user code with exec() and are 'tracked under CVE-2026-40217', so the vendor workaround of blocking only test_custom_code leaves the Obsidian-demonstrated route reachable by a proxy_admin the chain mints. For a CVE CISA lists as exploited, Obsidian also gives the post-compromise checks the entry lacks: audit every Custom Code Guardrail, callbacks loaded under litellm_settings.callbacks, and holders of proxy_admin, besides key rotation.

24. **F8 #24** — `entries/2026-11-19/cyberpower-powerpanel-business-system-shell-on-dc` — CyberPower: Defender takeaway has no hardening step; behaviour list omits download, reflective-load and AV-killer stages
   - source: https://www.security.com/threat-intelligence/power-management-software-attack-vector
   - Symantec's Recommendations give the levers ('restrict TCP port 3052 to named administrator hosts', 'Change the default administrator password, ensure patches are up to date') and CISA's ICSA-24-123-01 (cited) names 4.10.1 as the fixed build; the entry offers none. Symantec's Stage 3 table (certutil -urlcache and -decode, curl download, reflective .NET load through powershell -ep bypass, an AV killer, netstat) is the observable behaviour behind the T1105 mapping and is absent from the prose; the ifm.cmd to ifm4.cmd scripts were also staged via extcmd, so the pp?????.cmd-only hunt is incomplete.

25. **F8 #25** — `entries/2026-11-19/idunno-anticsrf-cve-2026-131914-exploited-no-patch-w3wp-rce` — Idunno Detection: 'carrying the module's default cookie __CSRFCOOKIE and form field __CSRFTOKEN' (low confidence)
   - source: https://github.com/mandiant/Vulnerability-Disclosures/blob/master/2026/MNDT-2026-0048.md
   - Mandiant notes that if the <csrfSettings> section is omitted from Web.config, 'a setter bug in CsrfSettings.DetectionResult overwrites the fallback FormFieldName value with "RaiseException"', so the default field name is not a reliable hunting key on every deployment; the entry presents the defaults without the caveat.

26. **F8 #26** — `entries/2026-11-18/drupal-core-critical-release-2026-11-18-psa-2026-11-16` — Drupal body: rating cited as 'exploit status Proof and target distribution Uncommon' with the gloss dropped (low confidence)
   - source: https://www.drupal.org/security/rss.xml
   - The advisory's risk legend reads 'E - Exploit: Proof of concept exists (documented methods for developing exploit exist in the wild)' and 'TD: Only uncommon module configurations are exploitable'. The earlier version glossed TD; the update keeps the raw labels, says 'any Drupal site' in Exposure and leaves cves[].status without poc-public. A reader cannot tell that Drupal itself rates a PoC as existing and the target set as uncommon.

27. **F8 #27** — `entries/2026-09-22/cve-2026-13684-synology-dsm-unauth-file-read-write` — Synology action: 'Update every Synology DSM to the fixed build of its branch ... 7.2-64570-4, 7.1.1-42962-7 or 6.2.4-25556-8 on the branches for which SA-26:13 names no fix' (low confidence)
   - source: https://www.synology.com/en-global/security/advisory/Synology_SA_26_13
   - SA-26:13's table lists fixes only for DSM 7.4, 7.3, 7.2.2 and 7.2.1; the SA-24:20 builds named for 7.2, 7.1 and 6.2 close CVE-2024-10441 but leave the September flaws (no mitigation, no fix) open on those branches. The action does not say that DSM 7.1, 7.2 and 6.2 owners also need to move to a branch with an SA-26:13 fix.

### Surface contradiction

28. **F9 #28** — `entries/2026-11-18/cve-2026-114938-java4shell-openjdk-avx512-base64-decoder-rce` — Java4Shell body: 'Talos has seen no exploitation in the wild yet and expects probing' next to NCSC.ch 'does not establish malicious exploitation'
   - source: https://www.tenable.com/blog/java4shell-cve-2026-114938-frequently-asked-questions-about-openjdk-rce-vulnerability
   - Talos (2026-11-18) and the NCSC.ch hub say no malicious exploitation is established; Tenable (cited, updated Nov 18) relays GreyNoise exploitation attempts and scanning, and VulnCheck reports a commercial RCE exploit. The entry picks the quiet reading silently; add a Contradiction line.

29. **F9 #29** — `entries/2026-06-16/obsidian-security-a-three-cve-chain-turns-any-litellm-user-i` — LiteLLM cves[CVE-2026-40217].cvss '5.9' (unlabelled) beside '8.8' for the other two (low confidence)
   - source: https://cveawg.mitre.org/api/cve/CVE-2026-40217
   - The CVE record (MITRE CNA) scores CVSS 3.1 8.8 AV:N/AC:L/PR:L (low privileges), while the vendor GHSA scores CVSS 4.0 5.9 Moderate and says a proxy-admin credential is needed. The entry follows the GHSA, but neither the scale (4.0 vs 3.1) nor the CNA conflict is surfaced. Label '5.9 (CVSS 4.0, vendor)' and add a Contradiction line.

30. **F9 #30** — `entries/2026-09-22/cve-2026-13684-synology-dsm-unauth-file-read-write` — Synology: 'a vulnerability patched in December 2024' pointing to SA-24:20 (low confidence)
   - source: https://www.synology.com/en-global/security/advisory/Synology_SA_24_20
   - SA-24:20's revision table runs 2024-11-05 to 2024-11-14 (fixes for DSM 7.2.1 published 2024-11-12) and BleepingComputer calls it 'a November 2024 security advisory'; Synology's notice says December 2024. The entry repeats the notice and says 'first published 2024-11-05' in the sourcing_note without flagging that the dates disagree.

### Missed angles

31. **F10 #31** — `run record coverage telemetry (backlog row)` — Basel-Landschaft cantonal-administration cyberattack held on the backlog (expiry 2026-12-03)
   - source: https://www.inside-it.ch/cyberangriff-auf-baselbieter-verwaltung-20261118
   - A confirmed, ongoing incident at a Swiss canton (attacks since 2026-11-15, servers isolated from the Internet, about 20 applications on six servers being reinstalled, a precautionary Alertswiss notice on 112/117/118, BORS unaffected) reached the run through S2 with ten sources and a drafted entry. It sits in the coverage focus (cantonal public sector, emergency services). With no vector or actor it is a short routine entry, not a drop. Search: 'Cyberangriff Kanton Basel-Landschaft Verwaltung Landeskanzlei Teilstab Cybersicherheit Update'.

32. **F10 #32** — `nginx2root research lead` — Xint's unpatched Linux kernel SCTP use-after-free/double-free privilege escalation
   - source: https://xint.io/blog/nginx2root-remote-code-execution
   - Section 6 of the Xint write-up describes a kernel SCTP flaw (association transferred to another socket, freed by the waiting send) chained to root and container escape, with details withheld until a kernel patch exists: a defender-relevant unpatched Linux LPE. Search: 'Xint SCTP kernel vulnerability sctp association use-after-free double free nginx2root kernel patch'.

### Editorial / less-is-more flags (advisory)

33. **F11 #33** — `entries/2026-11-19/cyberpower-powerpanel-business-system-shell-on-dc; entries/2026-09-22/cve-2026-13684-synology-dsm-unauth-file-read-write` — File-name indicators: 'upnpcont.exe and atl.dll' (CyberPower Detection), '.L0CK3D' and 'read-me3.txt' (Synology actions/Detection)
   - source: https://www.security.com/threat-intelligence/power-management-software-attack-vector
   - Style rule: zero IOCs including file-name indicators. The implant and side-loaded DLL names and the ransomware extension and note name are family-specific file-name indicators; describe the behaviour (a signed-looking binary beside a same-named system DLL in a SYSTEM profile path; renames to a fixed extension plus a note per directory) and keep the names to the sources.

34. **F11 #34** — `entries/2026-11-11/confluence-dc-cve-2026-90436-apache-axis-remote-api-rce` — Confluence record typed 'improvement' for the CISA KEV listing
   - source: work/2026-11-19T0355Z-intel/kev-window.txt
   - The KEV window tool states for this row: 'the KEV listing is an exploitation-status change (PD-13), an `update` record on that entry'; the run used `improvement` (no re-float) while the same listing on Synology, LiteLLM and REDCap is an `update`. The section's first sentence is a new dated event (CISA, 2026-11-18) and cves[].status moves to exploited and cisa-kev; type it `update` or explain the exception.

35. **F11 #35** — `entries/2026-11-17/optimjack-poisoned-vendor-scripts-skimmer-iphone-router` — OptimJack summary: 'Zscaler ThreatLabz counts more than 450 domains, among them a crypto clipper and card skimmer in the Optimizely files'
   - The relative clause attaches the clipper and skimmer to the 450 domains; say the Optimizely files carry a clipper and skimmer.

36. **F11 #36** — `entries/2026-06-16/obsidian-security-a-three-cve-chain-turns-any-litellm-user-i` — LiteLLM update section last sentence: 'The analysis above now uses the advisory's description in place of the earlier statement that the guardrail runs attacker-supplied Python through exec()'
   - Record-keeping narration in reader-facing text. Obsidian (cited) still describes the production guardrail routes as running user code with exec() and builtins available, so the 'correction' also narrows what the entry says; fold the facts into the analysis and keep the narration in the record summary.

37. **F11 #37** — `entries/2026-11-19/airlock-gateway-cve-2026-19707-smart-form-protection; nginx-nginx2root-five-unauth-memory-corruption-flaws; idunno-anticsrf-cve-2026-131914-exploited-no-patch-w3wp-rce; redcap-cve-2026-90817-unauth-survey-rce-exploited-kev; cyberpower-powerpanel-business-system-shell-on-dc` — Entity linking and unsourced region tag: entities: [] on nginx, REDCap, Idunno and Airlock; regions include switzerland on Airlock
   - The run registered product:redcap, product:airlock-gateway, product:idunno-anticsrf and product:cyberpower-powerpanel-business, and the registry already holds product:f5-nginx-open-source and product:f5-nginx-plus, yet the entries carry none of them in entities[] (the sibling PHP2Shell, Confluence and HPE entries do link products). The Airlock Swiss nexus (Ergon, Switzerland) is stated by no cited page and the body never gives it; S1 itself marked the footprint as unsourced. Either source it or drop the region.

38. **F11 #38** — `entries/2026-11-19/nginx-nginx2root-five-unauth-memory-corruption-flaws; entries/2026-11-18/drupal-core-critical-release-2026-11-18-psa-2026-11-16` — sourcing_note wording: 'could not be read by any fetch tool' (nginx), 'answered the fetch tools with a client challenge' (Drupal)
   - Fetch-transport vocabulary in a reader-facing field; two sentences of provenance suffice ('F5's K-articles are not publicly readable; Plus builds are taken from CERT.at, Rapid7 and Wiz').

39. **F11 #39** — `entries/2026-11-19/tcherber-access-broker-fortigate-sonicwall-vpn-ldap-sweep` — tcherber techniques: [T1133, T1078.001, T1087.002, T1016]
   - source: https://www.cyderes.com/howler-cell/exposing-tcherber
   - The body relays Cyderes's reading of 'brute-force harvesting and credential dump sourcing' and the broker's brute-force claim but no Brute Force id is mapped (T1110); either map it as the reported behaviour or word it as the broker's claim only.

### Analytical-link-as-fact

40. **F13 #40** — `entries/2026-11-19/airlock-gateway-cve-2026-19707-smart-form-protection` — Airlock body: 'Airlock's release notes for 8.6.1 and 8.5.3 list the same fix as a buffer overflow when decoding HTML entities' (low confidence)
   - source: https://docs.airlock.com/gateway/latest/index/1781491741687.html
   - The changelog line 'FIX: AP-38633 Fix buffer overflow when decoding HTML entities' carries no CVE id, no mention of Smart Form Protection and no security label; no cited page states that it is the CVE-2026-19707 fix (the sourcing_note concedes this). The link is plausible (same fixed releases; the CNA title says 'HTML entity decoder') but is an inference presented as fact; say 'a fix in the same releases' or cite the CNA record.

### Org-triage line missing / inconsistent

41. **F16 #41** — `entries/2026-11-19/redcap-cve-2026-90817-unauth-survey-rce-exploited-kev` — REDCap priority: notable (low confidence)
   - source: https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2026-10-07-XMRig-campaign-through-CVE-2026-90817.txt
   - An unauthenticated RCE exploited since 2026-10-07 (Unit 42), on the CISA KEV list since 2026-11-18, with a public PoC and a fix, on a product the store's own entry of 2026-06-16 (PRC UNC6508 via REDCap, references[] not linked) describes as deployed at Swiss and EU university hospitals and research bodies. Public survey pages are internet-facing by design. This plainly reaches the high bar (exposure plus a decision inside 7 days); notable under-calibrates, and the body gives no constituency nexus. Raise to high and link the earlier REDCap entry in references[].

### Checked and found sound (no finding)

- NGINX: all five CVE ranges, fixed builds (nginx.org, CNA records, CERT.at, Rapid7), PoC caveats (Rapid7 repository), Wiz/Xint statements, NCSC.ch/NCSC-NL/CERT-EU wording and the six evidence quotes check out; classification A/1 and priority high are defensible.
- REDCap: CNA (Securifera) record, CVSS 3.1 9.8, fixed builds (CNA record), Unit 42 chain and persistence details, CISA listing and the mechanism text all check out; techniques map to Unit 42 behaviours.
- Idunno.AntiCsrf: the Mandiant disclosure text, ENISA 9.3 and the CISA-ADP "Exploitation: none" statement noted in sourcing_note are accurate; Airlock: ENISA record text, CVSS 9.5 AC:H, support-lifecycle table accurate.
- Drupal, Synology (KEV record notes link SA-24:20; EPSS 0.01251), Confluence (Atlassian, Apache, EPSS 0.01128), OptimJack (Optimizely status, Zscaler, Report URI, Hudson Rock, Ohey), PHP2Shell (Trend Micro advisory table of 2026-11-18, Download Center dates, Quest KB, NetApp advisory data, KEV 2026-10-26) and HPE revision 2 (76 CVEs, 33 at 9.0 or higher, CVE-2026-79845 replaced by CVE-2026-95787, FIPS note) all verified against the live pages or CSAF files.
- Admiralty classifications, verification flags and carve-outs, em-dash and IOC scans (no IPs, hashes, attacker domains) are clean on all 14 entries; no priority is `critical`; update-vs-new decisions for the six new entries are right (no CVE or entity overlap with prior_coverage.json; nginx references the two earlier nginx entries). Record `updated_at` mirrors match the non-internal update `at` values on Drupal, Java4Shell, Synology, LiteLLM, OptimJack, PHP2Shell and HPE; Confluence's improvement correctly does not move it.
- Run record notes: counts (6 new, 8 updated), sub-agent windows (S1-S4, DR1 04:39:20Z-05:05:15Z, DR2 04:39:21Z-04:58:45Z), the four KEV dispositions and the PHP and Basel-Landschaft backlog rows match disk. The only note that does not hold as a coverage judgement is the Basel-Landschaft hold (finding in F10).

### Verdict

NEEDS_FIXES (truth: 17, editorial: 17, advisory: 7)

Highest-weight items: F4 #9 (Java4Shell states no attacks while the cited Tenable page reports GreyNoise exploitation attempts and a commercial RCE exploit), the Idunno rotation condition, the LiteLLM unsupported under-deployment claim and wrong Obsidian date, the CERT-Bund severity, the CyberPower ATT&CK id, and the missing interim mitigations on the nginx entry. Several items are marked low confidence in their text.

### Findings summary (machine-readable)

See `verification.iter1.findings.yaml` (41 records).
