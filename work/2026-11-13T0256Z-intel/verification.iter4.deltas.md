# Iteration 4 findings and the remediation applied (for the iteration 5 pass)

1. [F3] citrix-netscaler-adc-gateway-ctx697305-28-memory-flaws (sourcing_note, cves[])
   finding: The bulletin was revised after the run captured it (cached capture: 'Modified 11-12-2026 04:52', rows 111343-111349, history 'Initial Publication' only; live page now 'Modified 11-12-2026 20:27' with history '2026-11-12 | Fixed a 
   remediation_applied: fixed: Citrix revised CTX697305 after the slice captured it; the sourcing note and the run-record note now say the seven mistyped CVE numbers were corrected to CVE-2026-111333 to CVE-2026-111339

2. [F8] citrix-netscaler-adc-gateway-ctx697305-28-memory-flaws (cves[])
   finding: With the vendor's corrected ids the seven omitted rows have valid ids; one of them (CVE-2026-111334, 9.3) is among the 'nine scored 9.0 or above' the summary counts but is absent from cves[], and the log-file row the Detection lin
   remediation_applied: fixed: the seven records added, 29 in total with the Console

3. [F3] citrix-netscaler-adc-gateway-ctx697305-28-memory-flaws (body paragraph 2)
   finding: The cited CTX697305 page lists only the four ADC/Gateway builds and the Secure Private Access note; the Console build 14.1-74.34 is on CTX697320 ('Citrix NetScaler Console 14.1-74.34 and later releases'). Add the CTX697320 citatio
   remediation_applied: fixed: the Console build 14.1-74.34 cites CTX697320

4. [F3] citrix-netscaler-adc-gateway-ctx697305-28-memory-flaws (Defender takeaway)
   finding: (low confidence) CERT-EU carries the Gateway/AAA-first advice and the no-feature point but says nothing about the bulletins offering no workaround; that statement belongs to the bulletins (cite them) or should be cut.
   remediation_applied: fixed: the takeaway cites CERT-EU for the no-feature point and both bulletins for the absence of a workaround

5. [F3] check-point-php2shell-sk1000302-portal-and-vpn-gateways (Exposure)
   finding: The single citation ends a sentence that chains the PHP-flaw scope (Mobile Access Portal, SSL Network Extender, SAML realm VPN, captive portal, UserCheck, Zero Phishing; R81.20-R82.20 and Spark) with the CVE-2026-123039 scope. sk1
   remediation_applied: fixed: the Exposure line splits the sk1000302 and sk1000362 citations

6. [F3] check-point-php2shell-sk1000302-portal-and-vpn-gateways (Defender takeaway)
   finding: (low confidence) The sentence ends on the Check Point Research citation, which names neither the Jumbo takes, the cp-httpd.conf mitigation nor the dynamic_server stop (sk1000302 and sk1000362 carry them). Co-cite the two sk pages 
   remediation_applied: fixed: the takeaway cites sk1000302 and sk1000362 for the mitigation and the Jumbo takes

7. [F3] check-point-php2shell-sk1000302-portal-and-vpn-gateways (sources[], citation date)
   finding: (low confidence) The page's own data says dateCreated 2026-11-08, lastModified 2026-11-12. The sk1000302 records are labelled 'modified 2026-11-12'; this one is not, so the inline date reads as a publication date four days later t
   remediation_applied: fixed: the sk1000362 source labelled 'modified 2026-11-12' like the sk1000302 records (the page was created 2026-11-08)

8. [F3] confluence-dc-cve-2026-90436-apache-axis-remote-api-rce (body, paragraph 1); n-able-n-central-33-unpatched-flaws-public-
   finding: (low confidence) Neither Huntback nor Previdian names CVE-2026-90436 (Previdian's page says 'No CVE Assigned Yet'; Huntback says 'Axis RCE to root to XMRig' and describes the SOAP-fault class instantiation without the id). Bleepin
   remediation_applied: fixed: BleepingComputer cited at the CVE link in the Confluence and N-able bodies

9. [F4] dixell-copeland-xweb-evo-vulncheck-cves-end-of-service (summary)
   finding: (low confidence) The cited warnings are CERT-FR (France) and NCSC/BACS (Switzerland); no cited source names an EU-level authority warning about the attacks (ENISA's EUVD is cited only as a CVE database, and a grep of the Ransom-IS
   remediation_applied: fixed: the summary says French and Swiss authorities

10. [F18] wfx-phantom-github-actions-ci-secret-stealer-stolen-tokens (actions[0])
   finding: (low confidence) The action defers the search terms to 'the Detection line', so a team working the aggregated Action Items cannot execute it without re-reading the entry (check 10b c). Name the probe PR title, the wfx-docs branch 
   remediation_applied: fixed: actions[0] rewritten with the search terms in place

11. [F11] darklunnen-group-ib-fortios-super-admin-swiss-scan-list (sourcing_note)
   finding: Stray ',.' left by the iteration-3 edit in a reader-facing field; remove the comma.
   remediation_applied: fixed: stray comma removed

12. [F11] wfx-phantom-github-actions-ci-secret-stealer-stolen-tokens (title, action, Defender takeaway)
   finding: (low confidence) The iteration-3 fix hedged the headline and body ('meant to outlast rotation'; StepSecurity: 'designed to outlast credential rotation', 'tries to stay in your AWS and Azure accounts after you rotate') but the titl
   remediation_applied: fixed: the title and the takeaway say designed to outlast rotation

13. [F11] php2shell-trend-micro-apex-quest-kace-netapp-ontap; cve-2026-119618-apache-httpd-mod-http2-assign-headers-rce; check-poi
   finding: (low confidence) Record summaries narrate which entry fields changed (record-keeping language) and, for Brotli, carry a delta the section does not state (check 4c d); say what changed in the world, not which fields moved.
   remediation_applied: fixed: the Trend Micro, Apache httpd and Check Point record summaries no longer narrate fields; Cisco's version 1.12 change added to the Brotli/Desigo section

14. [F11] dixell-copeland-xweb-evo-vulncheck-cves-end-of-service (sources[])
   finding: (low confidence) The page is an undated download list (items dated 2016-06-23, 2017-07-24, 2018-07-09); 2026-11-13 is the retrieval date, not a publication date (check 2e). Note it as read on that date or drop the date.
   remediation_applied: declined: advisory; the Copeland list is the only source for the end-of-support state and its source record carries the reading date

15. [F11] check-point-php2shell-sk1000302-portal-and-vpn-gateways (body paragraph 2)
   finding: (low confidence) CPR: 'A second scanning wave on November 2nd targeted some Israeli organizations ... alongside additional organizations worldwide' and 'A broader second wave on November 2 targeted organizations across multiple co
   remediation_applied: fixed: the Check Point body says targeted, as the research post does
