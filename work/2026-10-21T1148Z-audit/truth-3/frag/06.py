P = 'work/2026-10-21T1148Z-audit/truth-3/bodies/'
SW = 'https://www.securityweek.com/f5-patches-over-50-vulnerabilities/'
NC = 'https://advisories.ncsc.nl/csaf/v2/2026/ncsc-2026-0162.json'
CNA = 'https://cveawg.mitre.org/api/cve/CVE-2026-41225'
ENTRY = {
 'entry': '2026-05-17/cve-2026-41225-f5-big-ip-big-iq-icontrol-rest-manager-role-a',
 'verdict': 'factual-error',
 'defects': [
  {'where': 'summary (secondary cluster); body paragraph 1 (CVSS-8.7 secondary cluster sentence)',
   'claim': 'The CVSS-8.7 secondary cluster covers iControl REST command injection (CVE-2026-42930, CVE-2026-42924, CVE-2026-42406, CVE-2026-41953), SSH-password leakage in audit log / API response bodies (CVE-2026-40698), and privilege escalation via misconfigured permissions (CVE-2026-40631, CVE-2026-40061, CVE-2026-34176).',
   'defect': 'CVE ids are paired with the wrong flaws. The SSH-password leak is CVE-2026-28758 (CVSS 3.1 4.4), not 40698; CVE-2026-40698 is a command-injection privilege escalation through SNMP configuration objects. CVE-2026-42930 is an Appliance mode bypass (path traversal), CVE-2026-42924 is iControl SOAP not REST, CVE-2026-42406 needs the Certificate Manager role, and CVE-2026-34176 is the iControl REST remote command injection in Appliance mode, CVE-2026-40061 a BIG-IP DNS command injection (neither is "misconfigured permissions").',
   'ground_truth': 'CVE-2026-28758: "BIG-IP DNS\'s gtm_add and bigip_add iControl REST commands exposes the ssh-password parameter in cleartext within responses and audit logs" (3.1 score 4.4); CVE-2026-40698: "create SNMP configuration objects via iControl REST or TMOS shell, resulting in privilege escalation" (8.7); CVE-2026-34176: "An authenticated remote command injection vulnerability exists in an undisclosed iControl REST endpoint in Appliance mode"; CVE-2026-42930: "bypass Appliance mode restrictions"; CVE-2026-42924: "exploit iControl SOAP to create SNMP configuration objects"',
   'ground_truth_url': NC,
   'fix': 'Drop the id lists or correct them: SSH-password cleartext exposure = CVE-2026-28758 (4.4); iControl REST command injection in Appliance mode = CVE-2026-34176; Appliance mode bypass = CVE-2026-42930; SNMP-object command injection / privilege escalation = CVE-2026-40698, CVE-2026-42924, CVE-2026-41953; Certificate Manager command execution = CVE-2026-42406.',
   'class': 'factual-error'},
  {'where': 'title; headline; summary; body (F5 BIG-IP / BIG-IQ)',
   'claim': 'CVE-2026-41225 — F5 BIG-IP / BIG-IQ: iControl REST Manager-role authenticated RCE',
   'defect': '(low confidence; the F5 article K000160916 is unreadable on every transport) F5\'s own CNA record for CVE-2026-41225 lists BIG-IP only (21.0.0 before 21.0.0.2, 17.5.0 before 17.5.1.6, 17.1.0 before 17.1.3.2, 16.1.0 end of support, 21.1.0 unaffected) and no BIG-IQ. The NCSC-NL CSAF marks every F5 product (26 of them, incl. NGINX, Silverline) known_affected with version unknown for this CVE, so it cannot support BIG-IQ.',
   'ground_truth': 'CNA affected: product "BIG-IP", modules "All Modules"; versions 21.0.0 lessThan 21.0.0.2 affected; 17.5.0 lessThan 17.5.1.6; 17.1.0 lessThan 17.1.3.2; 16.1.0 affected; 21.1.0 unaffected. Note: "Software versions which have reached End of Technical Support (EoTS) are not evaluated."',
   'ground_truth_url': CNA,
   'fix': 'CVE-2026-41225 affects BIG-IP (fixed in 21.0.0.2, 17.5.1.6, 17.1.3.2; 16.1.0 is end of support); drop BIG-IQ for this CVE.',
   'class': 'imprecision'},
  {'where': 'body paragraph 1 (sentence 1); sources[0].publisher',
   'claim': 'F5 published its May 2026 Quarterly Security Notification on 2026-05-14. / F5 K000160932, 2026-05-14',
   'defect': 'F5 published the CVE record on 2026-05-13 and SecurityWeek (dated 2026-05-14) says F5 announced fixes "on Wednesday", which is 2026-05-13. 2026-05-14 is the SecurityWeek article date.',
   'ground_truth': 'F5 CNA record: datePublished 2026-05-13T14:12:37.945Z. SecurityWeek: "F5 on Wednesday announced fixes for over 19 high-severity and 32 medium-severity vulnerabilities"',
   'ground_truth_url': CNA,
   'fix': 'F5 published its quarterly notification on 2026-05-13 (F5 article date not readable; CNA record and SecurityWeek agree on Wednesday 2026-05-13); event_date 2026-05-13.',
   'class': 'imprecision'},
  {'where': 'body paragraph 1 (CVSS sentence); title; cves[]',
   'claim': 'NVD and NCSC-NL also publish a CVSS 3.1 base score of 9.1 CRITICAL for the same CVE (the v3.1/v4.0 scale difference, not a vendor disagreement on severity)',
   'defect': 'F5\'s own CNA record carries two CVSS 3.1 scores, 7.2 (scope unchanged) and 9.1 (scope changed, the Appliance mode boundary case), plus CVSS 4.0 8.6. The 9.1 is not simply a v3.1 rendering of the v4.0 score and the 7.2 is omitted. "NVD" is cited as source for a score and quote that the F5 CNA record and NCSC-NL CSAF carry.',
   'ground_truth': 'CNA metrics: cvssV3_1 7.2 CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H; cvssV4_0 8.6; cvssV3_1 9.1 CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H. SecurityWeek quoting F5: "In appliance mode deployments, a successful exploit can allow the attacker to cross a security boundary."',
   'ground_truth_url': CNA,
   'fix': 'F5 scores it CVSS 4.0 8.6 and CVSS 3.1 7.2, or 9.1 where the Appliance mode security boundary is crossed (scope changed); cite F5 and NCSC-NL, not NVD.',
   'class': 'imprecision'},
  {'where': 'cves[CVE-2026-41225]',
   'claim': '"vector": "user-interaction", "affected": null, "fixed": null',
   'defect': 'The CVSS vectors read AV:N/PR:H/UI:N (network, high privileges, no user interaction); "user-interaction" is wrong. Affected and fixed versions are missing.',
   'ground_truth': 'CVSS:4.0/AV:N/AC:L/AT:N/PR:H/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N; affected BIG-IP 21.0.0 <21.0.0.2, 17.5.0 <17.5.1.6, 17.1.0 <17.1.3.2, 16.1.0 (EoTS)',
   'ground_truth_url': CNA,
   'fix': 'vector network (authenticated, PR:H); affected "BIG-IP 21.0.0-21.0.0.1, 17.5.0-17.5.1.5, 17.1.0-17.1.3.1, 16.1.x"; fixed "21.0.0.2, 17.5.1.6, 17.1.3.2".',
   'class': 'imprecision'},
  {'where': 'summary; actions[0]; body paragraph 1 (Why it matters)',
   'claim': 'Affects BIG-IP appliances widely deployed across European public-sector load-balancing / WAF perimeters / the practical attack chain is credential theft → iControl REST object creation → shell execution / the operationally significant chain is initial-access-by-credential-theft → iControl-REST-object-creation → shell command execution',
   'defect': 'No source states European public-sector deployment or a credential-theft chain. F5 (as quoted by SecurityWeek) says a highly privileged attacker with network access to the iControl REST endpoint can create configuration objects leading to command execution, and calls it a control plane issue only.',
   'ground_truth': 'This vulnerability may allow a highly privileged attacker with network access to the affected iControl REST endpoint through the BIG-IP management port or self IP addresses to escalate their privileges or bypass Appliance mode restrictions. ... There is no data plane exposure; this is a control plane issue only',
   'ground_truth_url': SW,
   'fix': 'Remove the public-sector deployment claim and the credential-theft chain, or mark them as the entry\'s analysis; the prerequisite is an authenticated Manager-role principal with network reach to the management port or a self IP.',
   'class': 'factual-error'},
  {'where': 'body paragraph 1 (monitoring and hardening sentences)',
   'claim': 'SOCs should monitor iControl REST audit logs for POST/PATCH requests creating unexpected configuration objects from Manager-role principals; alert on TMSH commands spawning shell subprocesses outside change-windows; restrict iControl REST reachability to jump hosts ...; disable iControl SOAP entirely where unused.',
   'defect': 'Composed hunting and hardening guidance with no inline citation; no readable source states it (the F5 article is unreadable on every transport; SecurityWeek and the CSAF carry none).',
   'ground_truth': 'SecurityWeek and NCSC-NL CSAF contain no monitoring or mitigation guidance.',
   'ground_truth_url': SW,
   'fix': 'Mark as derived hunting concept or cite the F5 article once readable.',
   'class': 'imprecision'},
  {'where': 'body paragraph 1 (uncited clauses; self-reference)',
   'claim': '**Why it matters to us:** ... Reference: § 2 F5 item. / the previously-covered CVE-2026-42945 NGINX heap overflow / No exploitation in the wild reported as of advisory publication.',
   'defect': 'Pipeline self-reference ("to us", "§ 2 F5 item", "previously-covered") in reader text. Several clauses carry no inline citation: the SecurityWeek quote and counts are SecurityWeek\'s, the 43-CVE count and component list are in the NCSC-NL CSAF, the Manager-role prerequisite and no-exploitation line are SecurityWeek\'s ("None of these vulnerabilities appears to have been exploited in the wild"; CISA ADP SSVC reads Exploitation none; not in KEV 2026-10-21).',
   'ground_truth': 'None of these vulnerabilities appears to have been exploited in the wild.',
   'ground_truth_url': SW,
   'fix': 'Cite SecurityWeek for the count, prerequisite and exploitation line and the NCSC-NL CSAF for the 43-CVE count; drop the self-references.',
   'class': 'imprecision'},
  {'where': 'priority',
   'claim': 'priority: high',
   'defect': '(low confidence) A post-authentication, Manager-role-only control-plane flaw, no exploitation, decided inside the regular quarterly patch cycle; the entry itself says "post-auth Manager-role only". The only urgency driver is the fabricated credential-theft chain.',
   'ground_truth': 'F5 via SecurityWeek: "a highly privileged attacker"; "this is a control plane issue only"; SSVC Exploitation: none.',
   'ground_truth_url': SW,
   'fix': 'Consider notable.',
   'class': 'imprecision'},
 ],
 'upgrade': {
  'techniques': [
   {'id': 'T1059', 'behavior': 'Attacker with Manager role creates configuration objects that allow running arbitrary commands', 'url': SW},
   {'id': 'T1068', 'behavior': 'Escalate privileges or bypass Appliance mode restrictions, crossing a security boundary', 'url': SW},
   {'id': 'T1078', 'behavior': 'Prerequisite: an authenticated principal with at least the Manager role over the iControl REST endpoint', 'url': SW},
  ],
  'note': 'No initial-access technique: the sources do not say how the attacker obtains Manager-role access, and the flaw is post-authentication (T1190 not supported).',
  'cve_facts': {'CVE-2026-41225': {'product': 'BIG-IP', 'affected': '21.0.0 <21.0.0.2; 17.5.0 <17.5.1.6; 17.1.0 <17.1.3.2; 16.1.0 (end of technical support, not evaluated); 21.1.0 unaffected', 'fixed': '21.0.0.2, 17.5.1.6, 17.1.3.2', 'cvss_4_0': '8.6', 'cvss_3_1': '7.2 (S:U) and 9.1 (S:C) in the F5 CNA record', 'cwe': 'CWE-648', 'cna_published': '2026-05-13T14:12Z', 'f5_article': 'K000160916 (unreadable)', 'kev': 'not in KEV 2026-10-21', 'ssvc': 'Exploitation none (CISA ADP 2026-05-13)'}},
  'rating': {'reliability': 'A', 'credibility': 2, 'basis': 'F5 CNA record (vendor for own product) is the authority; SecurityWeek and NCSC-NL restate F5. One assessor; F5 article itself unreadable.'},
  'exposure': [
   {'quote': 'This vulnerability may allow a highly privileged attacker with network access to the affected iControl REST endpoint through the BIG-IP management port or self IP addresses to escalate their privileges or bypass Appliance mode restrictions.', 'url': SW},
   {'quote': 'In appliance mode deployments, a successful exploit can allow the attacker to cross a security boundary. There is no data plane exposure; this is a control plane issue only', 'url': SW},
  ],
  'detection': [],
  'triage': [],
  'takeaway': [
   {'quote': 'None of these vulnerabilities appears to have been exploited in the wild.', 'url': SW},
   {'quote': '"lessThan": "21.0.0.2" ... "lessThan": "17.5.1.6" ... "lessThan": "17.1.3.2"', 'url': CNA},
  ],
  'bodies': [P + 'f5-sw.txt', P + 'f5-ncsc.txt', P + 'f5-cverecord-41225.txt'],
 },
 'possible_twin_outside_batch': 'entries/2026-05-15/cve-2026-42945-nginx-open-source-plus-f5-waf-products-18-yea (NGINX CVE-2026-42945 from the same F5 quarterly; the body points to it)',
}
CLAIMS = '''
d15a06d03c ¦ F4 ¦ https://cveawg.mitre.org/api/cve/CVE-2026-41225 ¦ (low confidence) F5 CNA: affected product "BIG-IP" only, CVSS 4.0 8.6 and 3.1 9.1 present; no BIG-IQ; SecurityWeek: CVE-2026-42945 (9.2) is the most severe
4f259cb746 ¦ F4 ¦ https://advisories.ncsc.nl/csaf/v2/2026/ncsc-2026-0162.json ¦ SSH-password exposure is CVE-2026-28758 (3.1 score 4.4), not in an 8.7 cluster; no source states European public-sector deployment
2613ca75cd ¦ F4 ¦ https://www.securityweek.com/f5-patches-over-50-vulnerabilities/ ¦ F5: "a highly privileged attacker with network access to the affected iControl REST endpoint"; no credential-theft chain stated; "§ 2 F5 item" is brief self-reference
f752c6ba78 ¦ F4 ¦ https://cveawg.mitre.org/api/cve/CVE-2026-41225 ¦ CVSS:4.0/AV:N/AC:L/AT:N/PR:H/UI:N (no user interaction, vector "user-interaction" wrong); affected BIG-IP 21.0.0 <21.0.0.2 etc.
e024b514ca ¦ ok ¦ https://advisories.ncsc.nl/csaf/v2/2026/ncsc-2026-0162.json ¦ CSAF summaries cover iControl REST, iControl SOAP, tmsh, TMM, Configuration utility, Advanced WAF/ASM, PEM, DNS, APM, SSL Orchestrator (F5 article unreadable)
c57f3927d8 ¦ F4 ¦ https://cveawg.mitre.org/api/cve/CVE-2026-41225 ¦ F5 CNA metrics: cvssV3_1 7.2 (S:U), cvssV4_0 8.6, cvssV3_1 9.1 (S:C); "A vulnerability exists in iControl REST where a highly privileged, authenticated attacker with at least the Manager role ..."
69b16d3e04 ¦ F4 ¦ https://cveawg.mitre.org/api/cve/CVE-2026-41225 ¦ F5 CNA datePublished 2026-05-13T14:12Z; SecurityWeek: "F5 on Wednesday announced fixes" (Wednesday = 2026-05-13)
cf3c8b7bd8 ¦ F5 ¦ https://www.securityweek.com/f5-patches-over-50-vulnerabilities/ ¦ "over 19 high-severity and 32 medium-severity vulnerabilities impacting BIG-IP, BIG-IQ, and NGINX"; NCSC-NL CSAF lists 43 vulnerabilities, NGINX CVEs absent
5f3b56d7a4 ¦ F4 ¦ https://advisories.ncsc.nl/csaf/v2/2026/ncsc-2026-0162.json ¦ CVE-2026-28758 is the ssh-password exposure (4.4); 40698 is SNMP-object command injection; 34176 is iControl REST command injection in Appliance mode
7a00eda070 ¦ F5 ¦ https://www.securityweek.com/f5-patches-over-50-vulnerabilities/ ¦ network access to the affected iControl REST endpoint through the BIG-IP management port or self IP addresses to escalate their privileges or bypass Appliance mode restrictions
0efe5dbd57 ¦ F5 ¦ https://www.securityweek.com/f5-patches-over-50-vulnerabilities/ ¦ None of these vulnerabilities appears to have been exploited in the wild.
43bcf6bb60 ¦ F4 ¦ https://www.securityweek.com/f5-patches-over-50-vulnerabilities/ ¦ No source states a credential-theft initial-access chain; F5: "a highly privileged attacker"
2bbb8050ff ¦ F5 ¦ null ¦ composed monitoring/hardening guidance; F5 article unreadable on every transport, SecurityWeek and CSAF carry none
ce439085fe ¦ F5 ¦ https://www.securityweek.com/f5-patches-over-50-vulnerabilities/ ¦ CVE-2026-42945 (CVSS v4.0 9.2) NGINX ngx_http_rewrite_module heap buffer overflow; "previously-covered" is self-reference
'''
