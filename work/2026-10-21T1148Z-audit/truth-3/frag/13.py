P = 'work/2026-10-21T1148Z-audit/truth-3/bodies/'
G = 'https://github.com/bigbluebutton/bigbluebutton/security/advisories/'
G1 = G + 'GHSA-7959-pf2v-xc4h'; G2 = G + 'GHSA-43hc-5g2m-cqff'; G3 = G + 'GHSA-xqm3-6q7q-4v5h'
BSI = 'https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1568'
ENTRY = {
 'entry': '2026-05-19/bigbluebutton-bbb-web-3-0-21-3-0-23-three-flaws-in-eu-educat',
 'verdict': 'factual-error',
 'defects': [
  {'where': 'body paragraph 1 (sentences 1-4 citations); summary',
   'claim': 'published three GitHub Security Advisories on 2026-05-17 ... [BBB GHSA-7959-pf2v-xc4h, 2026-05-17] ... [BBB GHSA-43hc-5g2m-cqff, 2026-05-17] ... [BBB GHSA-xqm3-6q7q-4v5h, 2026-05-17]',
   'defect': 'All three advisories were published on 2026-05-13 (21:40-21:45 UTC), four days earlier than the cited date. 2026-05-17/18 is the BSI WID release.',
   'ground_truth': 'GHSA-7959-pf2v-xc4h published 2026-05-13T21:40:42Z; GHSA-xqm3-6q7q-4v5h 2026-05-13T21:43:23Z; GHSA-43hc-5g2m-cqff 2026-05-13T21:45:14Z. BSI WID-SEC-2026-1568 initial_release_date 2026-05-17T22:00Z.',
   'ground_truth_url': G1,
   'fix': 'BigBlueButton published the advisories on 2026-05-13; BSI WID-SEC-2026-1568 followed on 2026-05-18 (CEST); event_date 2026-05-13.',
   'class': 'factual-error'},
  {'where': 'body paragraph 1 (sentence 1); Why it matters; actions[0]; summary',
   'claim': 'the de facto open-source virtual classroom platform deployed across German DFN, Swiss SWITCH, and pan-European GÉANT academic networks, including cantonal school deployments / BBB is operated at scale by Swiss cantonal Volksschule deployments, German Länder ministries of education and university IT, EU national-research-and-education networks / widely-deployed EU academic & government virtual-classroom platform',
   'defect': 'No source read names DFN, SWITCH, GÉANT, cantonal schools, Länder ministries or NRENs as operators; BSI describes BBB only as an open-source web conferencing system. These deployment claims carry the entry\'s Swiss nexus and its high priority.',
   'ground_truth': 'Produktbeschreibung: BigBlueButton ist ein Open-Source-Web-Konferenzsystem. (Product description: BigBlueButton is an open-source web conferencing system; translated from German)',
   'ground_truth_url': BSI,
   'fix': 'Remove the operator list or cite a source for each deployment; state only that BBB is an open-source web-conferencing system used in education.',
   'class': 'factual-error'},
  {'where': 'evidence[0]',
   'claim': '"Insecure SessionToken Generation in BigBlueButton" (BBB GHSA-7959-pf2v-xc4h)',
   'defect': 'The advisory\'s title and text do not contain this string; the title is "Insecure Randomness allows to guess user\'s conference session token and impersonate them".',
   'ground_truth': 'Insecure Randomness allows to guess user\'s conference session token and impersonate them / Without the fix it is possible for a user to determine the sesionTokens of other users in the session.',
   'ground_truth_url': G1,
   'fix': 'Quote the advisory\'s impact sentence verbatim.',
   'class': 'factual-error'},
  {'where': 'cves[] (all three)',
   'claim': '"vector": "user-interaction", "affected": null, "fixed": null; type auth-bypass on CVE-2026-46351 and CVE-2026-46404',
   'defect': 'All three CVSS 3.1 vectors have UI:N; "user-interaction" is wrong. Affected/fixed versions are on the advisories. CVE-2026-46404 is SSRF (CWE-918) and CVE-2026-46351 insecure randomness (CWE-330), not authentication bypasses.',
   'ground_truth': 'GHSA-7959: CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N, bbb-web < 3.0.21, patched >= 3.0.21; GHSA-43hc: same vector, < 3.0.21; GHSA-xqm3: CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:N/A:N, < 3.0.23',
   'ground_truth_url': G1,
   'fix': 'vector network, auth post-auth (PR:L / PR:H); affected "< 3.0.21" (46351, 46353) and "< 3.0.23" (46404); fixed 3.0.21 and 3.0.23; types session-token prediction (46351), checksum/auth bypass (46353), SSRF (46404).',
   'class': 'imprecision'},
  {'where': 'body paragraph 1 (CVE-2026-46351 and CVE-2026-46353 sentences); Why it matters (impact sentence)',
   'claim': 'an authenticated low-privilege attacker who shares or has observed a meeting ... / send valid API requests to restricted endpoints without proper authentication / send arbitrary authenticated API calls; SSRF on the server gives a presenter-role lateral-movement primitive into RFC1918 networks (KVM hosts, internal LDAP, SIS endpoints)',
   'defect': 'The advisories say a user can determine session tokens of other users "in the session" (not one who merely observed a meeting), and that any user could send valid requests to "some endpoints without a checksum" (not arbitrary calls or restricted endpoints without authentication). For the SSRF the vendor says private-address assets "may be compromised if the attacker has gained additional access"; "presenter-role", KVM, LDAP and SIS targets are the entry\'s speculation.',
   'ground_truth': 'Without this fix it is possible for any user to send valid requests to some endpoints without a checksum. / Private addresses assets may be compromised if the attacker has gained additional access.',
   'ground_truth_url': G2,
   'fix': 'Use the advisories\' own impact statements; mark any lateral-movement scenario as analysis.',
   'class': 'imprecision'},
  {'where': 'evidence[1]; headline; monitoring guidance',
   'claim': '"Ein entfernter, authentisierter Angreifer kann mehrere Schwachstellen in BigBlueButton ausnutzen, um Sicherheitsvorkehrungen zu umgehen und vertrauliche Informationen offenzulegen" / ... weak session-token randomness, API checksum / monitor bbb-web logs for anomalous joins using close-by sessionTokens ... egress ... to RFC1918 / 169.254/16',
   'defect': 'evidence[1] is verbatim but untranslated German without the English-plus-original format. The headline is cut mid-phrase. The monitoring advice is composed (the advisories give no detection guidance; "close-by sessionTokens" assumes a predictability pattern not described). The literal 169.254.0.0/16 range may trip the IOC scan.',
   'ground_truth': 'Workarounds: We recommend updating to the patched version of BigBlueButton.',
   'ground_truth_url': G1,
   'fix': 'Translate the BSI quote with original; complete the headline; mark detection as derived; write "link-local addresses" instead of the literal range.',
   'class': 'imprecision'},
  {'where': 'priority',
   'claim': 'priority: high',
   'defect': '(low confidence) Post-authentication flaws, no exploitation (none in CISA KEV on 2026-10-21), patched in the regular release; the Swiss deployment nexus that justifies high is unsourced.',
   'ground_truth': 'BSI: "Ein entfernter, authentisierter Angreifer" (a remote, authenticated attacker); CVSS PR:L / PR:H',
   'ground_truth_url': BSI,
   'fix': 'Consider notable unless a Swiss deployment base is sourced.',
   'class': 'imprecision'},
 ],
 'upgrade': {
  'techniques': [
   {'id': 'T1212', 'behavior': 'A session participant derives other users\' sessionTokens from insecure randomness and impersonates them (CVE-2026-46351)', 'url': G1},
   {'id': 'T1190', 'behavior': 'API checksum validation bypassed with specific URL parameters on presentationUploadExternalUrl, letting any user send valid requests to some endpoints (CVE-2026-46353)', 'url': G2},
  ],
  'note': 'The SSRF (CVE-2026-46404) reaches site-local and link-local addresses from the server; the advisories do not describe follow-on behavior, so no discovery or lateral-movement technique is mapped.',
  'cve_facts': {
   'CVE-2026-46351': {'ghsa': 'GHSA-7959-pf2v-xc4h', 'package': 'bbb-web', 'affected': '< 3.0.21', 'fixed': '3.0.21', 'cvss_3_1': '8.1 (AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N)', 'cwe': 'CWE-330'},
   'CVE-2026-46353': {'ghsa': 'GHSA-43hc-5g2m-cqff', 'package': 'bbb-web', 'affected': '< 3.0.21', 'fixed': '3.0.21', 'cvss_3_1': '8.1 (AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N)', 'cwe': 'CWE-284'},
   'CVE-2026-46404': {'ghsa': 'GHSA-xqm3-6q7q-4v5h', 'package': 'bbb-web', 'affected': '< 3.0.23', 'fixed': '3.0.23', 'cvss_3_1': '6.8 (AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:N/A:N)', 'cwe': 'CWE-918'},
   'published': 'GHSAs 2026-05-13; CVE records 2026-07-16 (GitHub CNA); BSI WID-SEC-2026-1568 2026-05-17T22:00Z',
   'kev': 'none in CISA KEV 2026-10-21',
  },
  'rating': {'reliability': 'A', 'credibility': 2, 'basis': 'Vendor GitHub advisories for its own product; BSI WID restates them for Germany. One assessor.'},
  'exposure': [
   {'quote': 'Package bbb-web (bigbluebutton) Affected versions < 3.0.21 Patched versions >= 3.0.21', 'url': G1},
   {'quote': 'BigBlueButton versions prior to 3.0.23.', 'url': G3},
   {'quote': 'A remote, authenticated attacker can exploit several vulnerabilities in BigBlueButton to bypass security measures and disclose confidential information. (translated from German)', 'original': 'Ein entfernter, authentisierter Angreifer kann mehrere Schwachstellen in BigBlueButton ausnutzen, um Sicherheitsvorkehrungen zu umgehen und vertrauliche Informationen offenzulegen.', 'url': BSI},
  ],
  'detection': [],
  'triage': [],
  'takeaway': [
   {'quote': 'We recommend updating to the patched version of BigBlueButton.', 'url': G1},
  ],
  'bodies': [P + 'bbb-GHSA-7959-pf2v-xc4h.txt', P + 'bbb-GHSA-43hc-5g2m-cqff.txt', P + 'bbb-GHSA-xqm3-6q7q-4v5h.txt', P + 'bbb-bsi-wid-1568.txt'],
 },
 'possible_twin_outside_batch': None,
}
CLAIMS = '''
0834076a1c ¦ ok ¦ https://github.com/bigbluebutton/bigbluebutton/security/advisories/GHSA-7959-pf2v-xc4h ¦ bbb-web < 3.0.21 (46351, 46353), < 3.0.23 (46404); insecure randomness, checksum bypass, SSRF; "EU education and government" framing unsourced (logged)
fd6431dac1 ¦ F3 ¦ https://github.com/bigbluebutton/bigbluebutton/security/advisories/GHSA-7959-pf2v-xc4h ¦ GHSA published 2026-05-13T21:40Z (entry cites 2026-05-17); scores 8.1/8.1/6.8 and BSI 2026-05-18 confirmed; "widely-deployed EU ... government" unsourced
c9fa04fb9d ¦ F4 ¦ https://github.com/bigbluebutton/bigbluebutton/security/advisories/GHSA-7959-pf2v-xc4h ¦ upgrade targets 3.0.21/3.0.23 confirmed; cantonal Volksschule/Länder deployments and log-audit patterns in no source
00862798fc ¦ F4 ¦ https://github.com/bigbluebutton/bigbluebutton/security/advisories/GHSA-7959-pf2v-xc4h ¦ CVSS:3.1/AV:N/AC:L/PR:L/UI:N ... 8.1 (score right; vector "user-interaction" contradicts UI:N); affected < 3.0.21
99509a2e45 ¦ F4 ¦ https://github.com/bigbluebutton/bigbluebutton/security/advisories/GHSA-43hc-5g2m-cqff ¦ CVSS 8.1 AV:N/PR:L/UI:N (vector "user-interaction" wrong); affected < 3.0.21
c100783c08 ¦ F4 ¦ https://github.com/bigbluebutton/bigbluebutton/security/advisories/GHSA-xqm3-6q7q-4v5h ¦ CVSS 6.8 AV:N/PR:H/UI:N/S:C (vector "user-interaction" wrong); affected < 3.0.23; SSRF typed auth-bypass
8a968f17b5 ¦ F3 ¦ https://github.com/bigbluebutton/bigbluebutton/security/advisories/GHSA-7959-pf2v-xc4h ¦ CWE-330, 8.1 confirmed; "determine the sesionTokens of other users in the session" (not "has observed a meeting"); dated 2026-05-13 not 05-17
22c3bd1b32 ¦ F3 ¦ https://github.com/bigbluebutton/bigbluebutton/security/advisories/GHSA-43hc-5g2m-cqff ¦ "possible for any user to send valid requests to some endpoints without a checksum" (not restricted endpoints without authentication); dated 2026-05-13
8ead7080c5 ¦ F3 ¦ https://github.com/bigbluebutton/bigbluebutton/security/advisories/GHSA-xqm3-6q7q-4v5h ¦ "restrict access to site local and link local addresses. Modifies redirect following logic to pin resolved IPs"; CVSS 6.8 PR:H; dated 2026-05-13 not 05-17
75656b873d ¦ ok ¦ https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1568 ¦ BigBlueButton: Mehrere Schwachstellen; initial_release_date 2026-05-17T22:00Z (2026-05-18 CEST); CVEs 46351, 46353, 46404
4974bf1c8f ¦ F4 ¦ https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1568 ¦ no source names DFN, SWITCH, GÉANT or cantonal schools; advisories published 2026-05-13, not 05-17
f9962d506e ¦ F4 ¦ null ¦ no fetched source states Swiss cantonal Volksschule, Länder ministry or NREN operation of BBB
e05e4127b1 ¦ F5 ¦ https://github.com/bigbluebutton/bigbluebutton/security/advisories/GHSA-xqm3-6q7q-4v5h ¦ analysis; vendor: "Private addresses assets may be compromised if the attacker has gained additional access" (KVM/LDAP/SIS speculative)
73480e9570 ¦ F5 ¦ https://github.com/bigbluebutton/bigbluebutton/security/advisories/GHSA-7959-pf2v-xc4h ¦ upgrade versions confirmed; log-monitoring guidance composed (advisories: "We recommend updating to the patched version")
862aed20f0 ¦ ok ¦ https://github.com/bigbluebutton/bigbluebutton/security/advisories/GHSA-7959-pf2v-xc4h ¦ T1212 fits token guessing; T1190 fits the exposed API checksum bypass; both active (mapping, not a source claim)
'''
