P = 'work/2026-10-21T1148Z-audit/truth-3/bodies/'
CP = 'https://cert.pl/en/posts/2026/05/CVE-2026-7182/'
EU = 'https://euvd.enisa.europa.eu/enisa/eu_vulnerability_database/EUVD-2026-30537'
DOC = 'https://docs.dhtmlx.com/gantt/guides/pdf-export-module-whatsnew/'
EPSS = 'https://api.first.org/data/v1/epss?cve=CVE-2026-41553&date=2026-05-16'
ENTRY = {
 'entry': '2026-05-17/cve-2026-41553-dhtmlx-pdf-export-module-unauthenticated-serv',
 'verdict': 'factual-error',
 'defects': [
  {'where': 'body paragraph 1 (Why it matters); summary; actions[0]',
   'claim': 'DHTMLX Gantt/Scheduler/Diagram are widely OEM-embedded in EU e-Government project-management portals, healthcare scheduling stacks, and municipal infrastructure-planning tools — the export module is often deployed on a separate internal host that operators forget about. / EU public-sector portal ecosystem heavy user / widely-embedded JavaScript scheduling/diagramming libraries',
   'defect': 'No source read states the embedding base, EU public-sector or healthcare use, or where operators deploy the export module. CERT-PL gives vendor, product, versions, CWE and the flaw; the vendor docs describe the module\'s changelog.',
   'ground_truth': 'CERT-PL: Vendor DHTMLX; Product PDF Export Module; Vulnerable versions From 0.3.3 to 0.7.6; no statement on deployments or sectors.',
   'ground_truth_url': CP,
   'fix': 'Remove the deployment and sector claims (or mark them as the entry\'s analysis); this is the sole source of the Swiss/EU nexus and the high priority rests on it.',
   'class': 'factual-error'},
  {'where': 'body paragraph 1 (sentence 1)',
   'claim': 'CERT Polska disclosed three coordinated vulnerabilities in DHTMLX (Dinamika Web) JavaScript scheduling and diagram libraries',
   'defect': '(low confidence on the correction) "Dinamika Web" appears in no source read. CERT-PL names the vendor "DHTMLX"; package copyright notices carry "Dinamenta UAB". The three flaws are in the PDF Export Module (two) and Diagram\'s export module (one), not in the libraries as such.',
   'ground_truth': 'Vendor DHTMLX | Product PDF Export Module / Diagram. CERT-PL: "PDF Export Module used in DHTMLX\'s products Gantt and Scheduler is vulnerable to Remote Code Execution"',
   'ground_truth_url': CP,
   'fix': 'CERT Polska disclosed three coordinated vulnerabilities in DHTMLX software (the PDF Export Module used by Gantt and Scheduler, and the export module of Diagram) on 2026-05-15.',
   'class': 'factual-error'},
  {'where': 'body paragraph 1 (Why it matters, EPSS sentence); CVE Summary Table row CVE-2026-41553',
   'claim': 'EPSS at disclosure is 0.39 with no known exploitation / | CVE-2026-41553 | ... | 0.39 | No | No | Yes (0.7.6) |',
   'defect': 'EPSS is a 0-1 probability; the FIRST EPSS value for CVE-2026-41553 on 2026-05-16 is 0.00388 (0.39 percent, percentile 0.60). "0.39" read as a probability is 100 times too high, and no cited page carries an EPSS figure (the ENISA EUVD page shows 1.05 on 2026-10-21).',
   'ground_truth': '{"cve":"CVE-2026-41553","epss":"0.003880000","percentile":"0.600660000","date":"2026-05-16"}',
   'ground_truth_url': EPSS,
   'fix': 'EPSS 0.0039 (0.39 percent) on 2026-05-16, cited to FIRST; or drop it.',
   'class': 'factual-error'},
  {'where': 'cves[CVE-2026-41552], cves[CVE-2026-7182]; cves[] affected/fixed',
   'claim': '"type": "rce" on CVE-2026-41552 and CVE-2026-7182; "affected": null, "fixed": null on all three',
   'defect': 'CVE-2026-41552 and CVE-2026-7182 are path traversal flaws that read local files into the generated PDF (CWE-22, CVSS 4.0 vectors with VC:H/VI:N/VA:N), not RCE. Affected and fixed versions are missing.',
   'ground_truth': 'CVE-2026-41552: "vulnerable to Path Traversal ... could include local files from the server and display them in the generated PDF" (CWE-22). EUVD: PDF Export Module "0.3.3 <0.7.6" (41552, 41553), Diagram "1.0.0 <1.1.1" (7182). CERT-PL: fixed in 0.7.6 and Diagram 1.1.1',
   'ground_truth_url': CP,
   'fix': 'type file-read / path-traversal for 41552 and 7182; affected "0.3.3 to before 0.7.6" (41552, 41553) and "1.0.0 to before 1.1.1" (7182); fixed "0.7.6" and "1.1.1". CERT-PL writes the ranges "to 0.7.6" / "to 1.1.1" inclusively, which conflicts with its own fixed-in statement; EUVD uses an exclusive bound.',
   'class': 'imprecision'},
  {'where': 'CVE Summary Table (rows CVE-2026-41225 and CVE-2026-44088)',
   'claim': '| CVE-2026-41225 | F5 BIG-IP / BIG-IQ (iControl REST) | 8.6 (v4) / 9.1 (v3.1) | n/a | No | No | Yes (May 2026 Quarterly) | [F5 K000160932] | ... | CVE-2026-44088 | KIR SzafirHost ...',
   'defect': 'The table carries rows for two unrelated findings that have their own entries, copied from the migrated brief, and repeats the F5 entry\'s imprecision (F5\'s CNA record lists BIG-IP only, and a 3.1 score of 7.2 besides 9.1; low confidence for BIG-IQ because the F5 article is unreadable). The F5 K000160932 link is unreadable on every transport.',
   'ground_truth': 'F5 CNA record for CVE-2026-41225: product "BIG-IP"; cvssV3_1 7.2 and 9.1; cvssV4_0 8.6.',
   'ground_truth_url': 'https://cveawg.mitre.org/api/cve/CVE-2026-41225',
   'fix': 'Delete the migrated "CVE Summary Table" from this entry; keep the three DHTMLX rows only if they are cited.',
   'class': 'imprecision'},
  {'where': 'body paragraph 1 (uncited clauses); actions[0]; Detection concepts',
   'claim': 'a CVSS-10.0 unauthenticated RCE in a server-side Node.js component will be scanned for shortly / assume opportunistic scanning starts within days / If the patch cannot land within 48 h / Detection concepts: ... `data=` parameters with JavaScript syntax (e.g. `process.`, `require(`, `child_process`)',
   'defect': 'Speculation and composed detection guidance without a source; "full command execution" in the summary is stronger than CERT-PL\'s "server compromise". Only sentence 1 carries a citation; the CERT-PL quote, the EUVD vector and the fix versions are CERT-PL / EUVD facts. Pipeline self-reference: "Why it matters to us", "Reference: § 2 DHTMLX item".',
   'ground_truth': 'This can lead to server compromise. (CERT-PL); EUVD: baseScore 10.0, CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H',
   'ground_truth_url': CP,
   'fix': 'Cite CERT-PL and EUVD on each clause; mark the detection and scanning statements as the entry\'s analysis or drop them; remove the self-references.',
   'class': 'imprecision'},
 ],
 'upgrade': {
  'techniques': [
   {'id': 'T1190', 'behavior': 'Unauthenticated attacker injects JavaScript into the `data` parameter of the exposed PDF Export Module; path-traversal payloads in HTML sent to the export service', 'url': CP},
   {'id': 'T1059.007', 'behavior': 'Injected JavaScript is processed by Node.js and executed, leading to server compromise', 'url': CP},
   {'id': 'T1005', 'behavior': 'Crafted HTML payload includes local server files in the generated PDF (CVE-2026-41552, CVE-2026-7182)', 'url': CP},
  ],
  'note': 'All three ids active. The export service must be reachable by the attacker; sources do not say how widely it is exposed.',
  'cve_facts': {
   'CVE-2026-41553': {'product': 'DHTMLX PDF Export Module (Gantt, Scheduler)', 'flaw': 'RCE via unsanitized data parameter, CWE-78', 'affected': '0.3.3 to before 0.7.6', 'fixed': '0.7.6', 'cvss_4_0': '10.0 (CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H)', 'euvd': 'EUVD-2026-30537', 'ghsa': 'GHSA-qc73-55rc-fgph', 'epss_2026_05_16': '0.00388'},
   'CVE-2026-41552': {'product': 'DHTMLX PDF Export Module (Gantt, Scheduler)', 'flaw': 'path traversal, local file content included in generated PDF, CWE-22', 'affected': '0.3.3 to before 0.7.6', 'fixed': '0.7.6', 'cvss_4_0': '9.2 (VC:H/VI:N/VA:N/SC:H)', 'euvd': 'EUVD-2026-30538', 'ghsa': 'GHSA-cj88-m5vv-89m3', 'epss_2026_05_16': '0.00043'},
   'CVE-2026-7182': {'product': 'DHTMLX Diagram export module', 'flaw': 'path traversal in `src` attribute, local files in generated PDF, CWE-22', 'affected': '1.0.0 to before 1.1.1', 'fixed': '1.1.1', 'cvss_4_0': '9.2 (VC:H/VI:N/VA:N/SC:H)', 'euvd': 'EUVD-2026-30539', 'ghsa': 'GHSA-hr7c-pw36-w99g', 'epss_2026_05_16': '0.00117'},
   'kev': 'none of the three in CISA KEV 2026-10-21',
   'credit': 'Lukasz Jaworski and Tomasz Holeksa, Pentest Limited',
  },
  'rating': {'reliability': 'A', 'credibility': 2, 'basis': 'CERT-PL is the CNA and coordinator for its own jurisdiction; ENISA EUVD restates the CERT-PL record; the vendor changelog independently lists "Fixed Remote Code Execution and File Read vulnerabilities" for 0.7.6 but is a one-line note, so the assessment stays 2.'},
  'exposure': [
   {'quote': 'PDF Export Module used in DHTMLX\'s products Gantt and Scheduler is vulnerable to Remote Code Execution due to lack of `data` parameter sanitization. An unauthenticated attacker can inject the malicious JavaScript code to the parameter whose value is processed by Node.js and subsequently executed.', 'url': CP},
   {'quote': 'Vendor DHTMLX | Product PDF Export Module | Vulnerable versions From 0.3.3 to 0.7.6', 'url': CP},
  ],
  'detection': [],
  'triage': [],
  'takeaway': [
   {'quote': 'Vulnerabilities CVE-2026-41552 and CVE-2026-41553 were fixed in PDF Export Module version 0.7.6.', 'url': CP},
   {'quote': 'Fixed Remote Code Execution and File Read vulnerabilities', 'url': DOC},
  ],
  'bodies': [P + 'dh-certpl-7182.txt', P + 'dh-euvd-30537.txt', P + 'dh-euvd-30538.txt', P + 'dh-euvd-30539.txt', P + 'dh-docs-whatsnew.txt', P + 'dh-ghsa-qc73.txt'],
 },
 'possible_twin_outside_batch': None,
}
CLAIMS = '''
cb09f9ab4e ¦ ok ¦ https://euvd.enisa.europa.eu/enisa/eu_vulnerability_database/EUVD-2026-30537 ¦ baseScore 10.0, CVSS 4.0, RCE in PDF Export Module; CVE-2026-41552 (9.2) and CVE-2026-7182 (9.2) per EUVD-2026-30538/30539
1954502e4c ¦ F4 ¦ https://cert.pl/en/posts/2026/05/CVE-2026-7182/ ¦ CERT-PL: "This can lead to server compromise" and fixes 0.7.6/1.1.1 confirmed; "widely-embedded libraries" and "EU public-sector portal ecosystem heavy user" in no source
44b09aaddc ¦ F4 ¦ https://cert.pl/en/posts/2026/05/CVE-2026-7182/ ¦ fix versions 0.7.6 and 1.1.1 confirmed; "in EU public-sector portals" and scanning-within-days premise unsupported
3aabe793f3 ¦ ok ¦ https://euvd.enisa.europa.eu/enisa/eu_vulnerability_database/EUVD-2026-30537 ¦ baseScore 10.0 CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N; affected 0.3.3 <0.7.6 (entry has affected/fixed null)
951ffd5482 ¦ ok ¦ https://euvd.enisa.europa.eu/enisa/eu_vulnerability_database/EUVD-2026-30538 ¦ baseScore 9.2 CVSS 4.0 AV:N/PR:N/UI:N; CWE-22 path traversal (entry types it rce; logged)
97cd2be172 ¦ ok ¦ https://euvd.enisa.europa.eu/enisa/eu_vulnerability_database/EUVD-2026-30539 ¦ baseScore 9.2 CVSS 4.0 AV:N/PR:N/UI:N; Diagram 1.0.0 <1.1.1 (entry types it rce; logged)
85ecf66b49 ¦ F4 ¦ https://cert.pl/en/posts/2026/05/CVE-2026-7182/ ¦ Vendor: DHTMLX; 3 vulnerabilities, publication date 15 May 2026; "Dinamika Web" in no source (package notices: Dinamenta UAB)
202efdeefa ¦ F4 ¦ https://cveawg.mitre.org/api/cve/CVE-2026-41225 ¦ (low confidence) F5 CNA lists BIG-IP only; cvssV3_1 7.2 and 9.1; F5 K000160932 unreadable; row belongs to another entry
17a646a10e ¦ F4 ¦ https://api.first.org/data/v1/epss?cve=CVE-2026-41553&date=2026-05-16 ¦ "epss":"0.003880000","percentile":"0.600660000" (0.39 percent, not 0.39); KEV none; fixed 0.7.6 confirmed
448dc24429 ¦ ok ¦ https://euvd.enisa.europa.eu/enisa/eu_vulnerability_database/EUVD-2026-30538 ¦ CVE-2026-41552 PDF Export Module path traversal, CVSS 4.0 9.2, fixed 0.7.6
0c25a61826 ¦ ok ¦ https://euvd.enisa.europa.eu/enisa/eu_vulnerability_database/EUVD-2026-30539 ¦ CVE-2026-7182 Diagram path traversal, CVSS 4.0 9.2, fixed 1.1.1
e8ac478842 ¦ ok ¦ https://euvd.enisa.europa.eu/enisa/eu_vulnerability_database/EUVD-2026-30512 ¦ CVE-2026-44088 baseScore 8.6 (CVSS 4.0), fixed in 1.2.1; not in KEV; row belongs to another entry
f2c5648b39 ¦ F5 ¦ https://cert.pl/en/posts/2026/05/CVE-2026-7182/ ¦ PDF Export Module used in DHTMLX's products Gantt and Scheduler is vulnerable to Remote Code Execution ... processed by Node.js
ab61699fd6 ¦ ok ¦ https://cert.pl/en/posts/2026/05/CVE-2026-7182/ ¦ "PDF Export Module used in DHTMLX's products Gantt and Scheduler is vulnerable to Remote Code Execution due to lack of `data` parameter sanitization." (verbatim)
599f8fa638 ¦ ok ¦ https://cert.pl/en/posts/2026/05/CVE-2026-7182/ ¦ "An unauthenticated attacker can inject the malicious JavaScript code to the parameter whose value is processed by Node.js and subsequently executed." (verbatim)
067743df44 ¦ ok ¦ https://euvd.enisa.europa.eu/enisa/eu_vulnerability_database/EUVD-2026-30537 ¦ "This can lead to server compromise." (CERT-PL); baseScoreVector CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H, score 10.0
9fda214b1d ¦ ok ¦ https://cert.pl/en/posts/2026/05/CVE-2026-7182/ ¦ unauthenticated JS injected and executed by Node.js; T1190 and T1059.007 active in v20 and fit
293faa9933 ¦ F5 ¦ https://cert.pl/en/posts/2026/05/CVE-2026-7182/ ¦ CVE-2026-41552 "Path Traversal ... include local files from the server and display them in the generated PDF"; CVE-2026-7182 Diagram `src` attribute
b44c8d5063 ¦ F5 ¦ https://cert.pl/en/posts/2026/05/CVE-2026-7182/ ¦ Vulnerabilities CVE-2026-41552 and CVE-2026-41553 were fixed in PDF Export Module version 0.7.6; CVE-2026-7182 fixed in Diagram 1.1.1
b206c258d0 ¦ F4 ¦ null ¦ no fetched source states OEM embedding in EU e-Government, healthcare or municipal tools, or where operators deploy the export module
5cd0cec034 ¦ F4 ¦ https://api.first.org/data/v1/epss?cve=CVE-2026-41553&date=2026-05-16 ¦ EPSS 0.00388 on 2026-05-16 (0.39 percent); "will be scanned for shortly" is speculation
9be4822d09 ¦ F5 ¦ null ¦ composed defender guidance; no fetched source states it
5f127117a7 ¦ F5 ¦ null ¦ composed detection concepts; no fetched source gives detection guidance
4c247b10e4 ¦ F5 ¦ null ¦ composed detection concepts (process., require(, child_process); no source
'''
