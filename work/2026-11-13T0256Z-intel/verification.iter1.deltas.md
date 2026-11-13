# Iteration 1 findings and the remediation applied (for the iteration 2 pass)

Verify each fix in the entry before the cold pass. Declined items carry their rationale; judge them on the cited facts.

1. [F3] citrix-netscaler-adc-gateway-ctx697305-28-memory-flaws
   finding: The cited record EUVD-2026-102489 carries only CVE-2026-111345 (Trudesk). The other six colliding ids resolve to EUVD-2026-102487 (111343, pig), 102488 (111344, APITable), 102490 (111346, ZenTao), 102491 (111347, go-ldap-admin), 1
   remediation_applied: fixed: clause narrowed to the one record the cited page carries (a Trudesk flaw), row identification kept by row text
   verify_in_this_iteration: re-read the changed clause/field against its cited source

2. [F3] ptc-windchill-flexplm-cve-2026-126325-deserialization-rce
   finding: (low confidence) The clause chains three facts and cites only the PTC Trust Center page. NCSC's 'UNKNOWN' status is on security-hub post 13174; 'the press' (THN) is not on the PTC page, which only supports 'no exploitation in its 
   remediation_applied: fixed: NCSC's exploitation status cited to NCSC post 13174, the change-log silence to the PTC page, the press clause dropped
   verify_in_this_iteration: re-read the changed clause/field against its cited source

3. [F3] signdrop-windows-clfs-authentication-lpe-public-poc-no-patch
   finding: Cyderes only says 'Systems where Mode is set to 1 (learning) or 0 (enforcement) are in scope'; it never states that Mode 2 or 3 is not vulnerable. That sentence is in the exploit author's GitHub README ('If it's set to 2 or 3 then
   remediation_applied: fixed: the Mode 2 or 3 clause dropped; the sentence states only what Cyderes says (0 or 1 in scope)
   verify_in_this_iteration: re-read the changed clause/field against its cited source

4. [F3] n-able-n-central-33-unpatched-flaws-public-pocs-offline
   finding: Huntback describes the nable_wrapper.pl setLDFileOwner escalation but never says it has no CVE. Previdian's page says 'No CVE Assigned Yet' for the whole chain. Re-cite or hedge. Claims 71473de8dc, f4a1a92460.
   remediation_applied: fixed: 'has no CVE' removed from the Huntback clauses in the body and the section; the sourcing note says Previdian's page shows no CVE assigned yet
   verify_in_this_iteration: re-read the changed clause/field against its cited source

5. [F3] n-able-n-central-33-unpatched-flaws-public-pocs-offline; confluence-dc-cve-2026-90436-apache-axis-remote-api-rce
   finding: The Previdian page reports '2 Attempts observed, 1 Unique attacker IP' and says its observations 'do not show that the target was vulnerable or that the attempt succeeded'. 'Full chain' comes from BleepingComputer ('later confirme
   remediation_applied: fixed: 'recorded attempts at the chain' in the N-able body, section and summary and in the Confluence section
   verify_in_this_iteration: re-read the changed clause/field against its cited source

6. [F3] confluence-dc-cve-2026-90436-apache-axis-remote-api-rce
   finding: Huntback never states the 21 servers had the Legacy API enabled (Tenable: 'Huntback ... does not say whether the Legacy API was enabled on those servers'); the Legacy API prerequisite is the researcher's and N-able's. Inference at
   remediation_applied: fixed: the Legacy API clause removed from the Huntback attributions in the Confluence body and section
   verify_in_this_iteration: re-read the changed clause/field against its cited source

7. [F3] cve-2026-119618-apache-httpd-mod-http2-assign-headers-rce
   finding: (low confidence) Wordfence says only that the repository has '2.4.71 and HTTP/1.1-only comparison runs'. The clean-run statement is on the researcher's README ('shows httpd 2.4.71 clean under the same traffic'), which is cited onl
   remediation_applied: fixed: the clean-run clause cites the researcher repository, Wordfence kept for the no-RCE clause
   verify_in_this_iteration: re-read the changed clause/field against its cited source

8. [F3] cve-2026-111497-brotli-desigo-cc-mitel-openscape-cisco-duo
   finding: support.apple.com/en-us/149715 is 'iOS 27.2.1 and iPadOS 27.2.1' only. The other releases are on separate Apple pages: 149716 (iOS 26.7.3), 149718 (macOS Golden Gate 27.2.1), 149719 (Tahoe 26.7.3), 149720 (Sequoia 15.8.3), 149722 
   remediation_applied: fixed: seven Apple pages added to sources[] and cited per clause; the Defender takeaway cites the iPhone/iPad, Mac, Watch and Vision Pro pages
   verify_in_this_iteration: re-read the changed clause/field against its cited source

9. [F3] check-point-php2shell-sk1000302-portal-and-vpn-gateways
   finding: sk1000362 says nothing about the standalone PHP hotfix; that text ('This Hotfix implements the PHP 7.4 published fix for CVE-2026-109618 and CVE-2026-109619') is on sk1000302. Split the clause and cite each. Claim aecc0cbfd9.
   remediation_applied: fixed: the clause split, the hotfix text cited to sk1000302 and the missing Jumbo take to sk1000362
   verify_in_this_iteration: re-read the changed clause/field against its cited source

10. [F3] darklunnen-group-ib-fortios-super-admin-swiss-scan-list
   finding: (low confidence) The advisory's own Published Date is Jan 14, 2025; 2025-03-31 is its Updated Date. Citation date should be the publication date, or the label should say 'updated'.
   remediation_applied: fixed: Fortinet PSIRT cited at its published date 2025-01-14
   verify_in_this_iteration: re-read the changed clause/field against its cited source

11. [F4] darklunnen-group-ib-fortios-super-admin-swiss-scan-list
   finding: Group-IB never says no Swiss victim exists. It says the scanning lists 'do not confirm vulnerability or successful exploitation' and that for several operations (incl. the Swiss S3 restic row with 'Production snapshots enumerated'
   remediation_applied: fixed: title now says Group-IB does not confirm any Swiss victim
   verify_in_this_iteration: re-read the changed clause/field against its cited source

12. [F4] huntress-teams-booking-device-code-phishing-encrypted-kit
   finding: Huntress says it 'quickly identified and contained the incident, barring the attack from escalating'; it does not say it saw no post-compromise activity, and the same page lists 'Subsequent Programmatic User Agents such as python-
   remediation_applied: fixed: now says Huntress contained the incident before it escalated
   verify_in_this_iteration: re-read the changed clause/field against its cited source

13. [F4] n-able-n-central-33-unpatched-flaws-public-pocs-offline
   finding: That sentence is from Huntress's 'UPDATE: 11/12 @ 1:10 AM ET'. Huntress's later 'UPDATE: 11/12 @ 6:30 AM ET' says 'New information from N-able changes our guidance from earlier this morning ... Servers running 2026.4 HF2 with Lega
   remediation_applied: fixed: summary states Huntress's later guidance; the evidence quote replaced with the 6:30 AM ET sentence (found verbatim in the saved body)
   verify_in_this_iteration: re-read the changed clause/field against its cited source

14. [F4] cve-2026-119618-apache-httpd-mod-http2-assign-headers-rce
   finding: USN-9090-1 lists Ubuntu-versioned backports (26.10 2.4.68-1ubuntu6.2, 26.04 2.4.66-2ubuntu2.8, 24.04 2.4.58-1ubuntu8.19, 22.04 2.4.52-1ubuntu4.27, 20.04 2.4.41-4ubuntu3.23+esm11), not 2.4.71. Only Debian (2.4.71-1~deb12u1/deb13u1)
   remediation_applied: fixed: summary and record summary say Debian and Alpine ship 2.4.71 and Ubuntu ships backported fixes
   verify_in_this_iteration: re-read the changed clause/field against its cited source

15. [F4] cve-2026-111497-brotli-desigo-cc-mitel-openscape-cisco-duo
   finding: The cited advisory is now version 1.12 of 2026-NOV-12 ('Updated products under investigation, vulnerable products, and products confirmed not vulnerable') and its priority-product table lists 'Identity Services Engine (ISE) Not im
   remediation_applied: fixed: paragraph rewritten to advisory version 1.12 of 2026-11-12 with ISE not impacted (read live)
   verify_in_this_iteration: re-read the changed clause/field against its cited source

16. [F4] check-point-php2shell-sk1000302-portal-and-vpn-gateways
   finding: Check Point Research calls TSGA 'persistent' (boot persistence directory, 'backup and snapshot persistence') but never states that a Jumbo hotfix leaves the implant, web shells or persistence in place; no source discusses what pat
   remediation_applied: fixed: summary and record summary say persistent backdoor; the Defender takeaway labels the patching point an inference; the bare sentence removed
   verify_in_this_iteration: re-read the changed clause/field against its cited source

17. [F4] confluence-dc-cve-2026-90436-apache-axis-remote-api-rce
   finding: (low confidence) Source: 'The Apache Axis project does not expect to create an Axis 1.x release fixing this problem'. 'will not' removes the hedge (the section text keeps 'does not expect'). Claim 6700fd73d3.
   remediation_applied: fixed: record summary says Apache does not expect to release an Axis 1.x fix
   verify_in_this_iteration: re-read the changed clause/field against its cited source

18. [F4] run-record
   finding: The published entry carries verification: multi-source with PTC's Trust Center as primary and NCSC Switzerland, BSI, ENISA and The Hacker News as corroborating; it is not single-source-national-cert. The note describes a prior sta
   remediation_applied: fixed: the run-record inclusion note rewritten to the entry's multi-source state
   verify_in_this_iteration: re-read the changed clause/field against its cited source

19. [F9] n-able-n-central-33-unpatched-flaws-public-pocs-offline
   finding: (low confidence) The Hacker News (cited) quotes Previdian's CEO that patches for CVE-2026-90436 'were released on November 6, 2026'; Apache's own post offers a patch commit but no release. The entry does not note the discrepancy.
   remediation_applied: fixed: the cves[] fixed text notes the source patch and Previdian's quoted 2026-11-06 patch claim
   verify_in_this_iteration: re-read the changed clause/field against its cited source

20. [F5] confluence-dc-cve-2026-90436-apache-axis-remote-api-rce
   finding: (low confidence) Labelled line carries no citation and no 'inference, not a source statement' disclaimer (the Citrix and Apache entries of the same run carry one); no cited source gives these indicators. Claim 459e8ca995.
   remediation_applied: fixed: the Detection line labelled an inference from the attack mechanics
   verify_in_this_iteration: re-read the changed clause/field against its cited source

21. [F16] citrix-netscaler-adc-gateway-ctx697305-28-memory-flaws
   finding: (low confidence) The entry itself states the vendor impact is crash or DoS, no exploitation, no PoC and no confirmed code-execution path. The run record's justification (default-configuration edge gateway) is defensible for a 7-da
   remediation_applied: declined: unauthenticated default-configuration flaws on internet-facing gateways scored up to 9.3 decide the 7-day patch window for the constituency edge although no source reports code execution or exploitation; the body states both limits
   verify_in_this_iteration: re-read the changed clause/field against its cited source

22. [F16] saxony-emergency-pager-messages-readable-on-social-network
   finding: (low confidence) Incident floor (Phase 4): an incident whose sources give no access vector, no actor and no behavior beyond the impact is routine and at most two sentences plus its transfer ground. The entry has no vector and no a
   remediation_applied: fixed: entry dropped (below the incident floor: no vector, no actor, one informant)
   verify_in_this_iteration: re-read the changed clause/field against its cited source

23. [F12] saxony-emergency-pager-messages-readable-on-social-network
   finding: (low confidence) Both sources are news outlets, heise relays Spiegel, and the Spiegel body was not read; the substantive claims rest on heise plus one informant. 'single-source' (with the existing note) may describe it more honest
   remediation_applied: fixed: entry dropped with finding 22
   verify_in_this_iteration: re-read the changed clause/field against its cited source

24. [F17] saxony-emergency-pager-messages-readable-on-social-network
   finding: (low confidence) The note says both outlets 'rest on an informant for the content of the messages and the cipher keys' and no authority confirmed content or numbers; only the LKA's receipt of the report and investigation are autho
   remediation_applied: fixed: entry dropped with finding 22
   verify_in_this_iteration: re-read the changed clause/field against its cited source

25. [F18] wfx-phantom-github-actions-ci-secret-stealer-stolen-tokens
   finding: (low confidence) The first half restates the body's Detection line verbatim (title and commit-message strings) and then bundles revoke, rotate and AWS/Azure cleanup into one sentence. A task such as 'revoke tokens and rotate secre
   remediation_applied: fixed: actions[0] rewritten as one task without the search strings
   verify_in_this_iteration: re-read the changed clause/field against its cited source

26. [F10] coverage
   finding: (low confidence) The S3 slice records a legitimate Swiss (.ch) site serving the ClickFix lure and concrete host telemetry (RuntimeBroker.exe outside System32, WindowsUpdate.exe in Startup, hidden-window PowerShell from the Run dia
   remediation_applied: declined: the compromised Swiss site is unnamed, the sample is single and ClickFix delivery is already covered; drop reason restated in the notes
   verify_in_this_iteration: re-read the changed clause/field against its cited source

27. [F8] cve-2026-111497-brotli-desigo-cc-mitel-openscape-cisco-duo
   finding: (low confidence) The run's own saved body of 'About the security content of HomeView Software Version 27.2' (https://support.apple.com/en-us/149851, 2026-11-12) carries the same brotli CVE-2026-111497 fix; HomeView is not in the A
   remediation_applied: fixed: HomeView Software 27.2 added to the body, summary, sources[] and affected_products
   verify_in_this_iteration: re-read the changed clause/field against its cited source

28. [F11] signdrop-windows-clfs-authentication-lpe-public-poc-no-patch; wfx-phantom-github-actions-ci-secret-stealer-stolen-tokens
   finding: Style rule: no file-name indicators. These are actor-chosen file/branch/commit/credential names that the sources list under indicators or detection. They read as behavioral detection hooks, but WFX's strings are also in the action
   remediation_applied: partly fixed: the WFX strings left the action; the SignDrop file name stays as the source's ranked detection hook
   verify_in_this_iteration: re-read the changed clause/field against its cited source

29. [F11] darklunnen-group-ib-fortios-super-admin-swiss-scan-list; wfx-phantom-github-actions-ci-secret-stealer-stolen-tokens; sig
   finding: (low confidence) DarkLunnen (a Group-IB-tracked operator) and WFX Phantom / wfx-loot (a named campaign and stealer) have no actor/campaign/malware key in entities[]; entities_added in the run record lists only products. Registry g
   remediation_applied: fixed: actor:darklunnen and malware:wfx-phantom registered and linked
   verify_in_this_iteration: re-read the changed clause/field against its cited source

30. [F11] huntress-teams-booking-device-code-phishing-encrypted-kit
   finding: The source's ATT&CK table maps this to T1550.004 (and T1539 for the captured session cookie); techniques[] omits both although the behaviour is described and quoted.
   remediation_applied: fixed: T1550.004 and T1539 added to techniques[]
   verify_in_this_iteration: re-read the changed clause/field against its cited source

31. [F11] php2shell-trend-micro-apex-quest-kace-netapp-ontap
   finding: (low confidence) The section carries a genuine vendor delta (advisory revised 2026-11-12, Analyzer ETA moved six days, patch names added) that a defender would act on; typed improvement it never floats the entry. If the section is
   remediation_applied: fixed: the record retyped update (the Analyzer ETA move is a reader-facing delta), heading and updated_at follow
   verify_in_this_iteration: re-read the changed clause/field against its cited source

32. [F11] cve-2026-119618-apache-httpd-mod-http2-assign-headers-rce; dixell-copeland-xweb-evo-vulncheck-cves-end-of-service
   finding: (low confidence) These are rolling tracker or download-listing pages with no publication date; the date shown is the reading date. Label them 'as read' or drop the date so it is not mistaken for the source's date.
   remediation_applied: declined: advisory, rolling pages are dated with the reading date in their source records
   verify_in_this_iteration: re-read the changed clause/field against its cited source


Not a finding but a change this pass must check: the Saxony emergency pager entry (saxony-emergency-pager-messages-readable-on-social-network) was DROPPED, its file removed. Registry additions this iteration: actor:darklunnen, malware:wfx-phantom (linked from the DarkLunnen and WFX Phantom entries), product:apple-homeview-software.
