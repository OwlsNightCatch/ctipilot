P = 'work/2026-10-21T1148Z-audit/truth-3/bodies/'
CP = 'https://cert.pl/en/posts/2026/05/CVE-2026-44088/'
EU = 'https://euvd.enisa.europa.eu/enisa/eu_vulnerability_database/EUVD-2026-30512'
BK = 'https://www.bakom.admin.ch/en/electronic-signature'
ENTRY = {
 'entry': '2026-05-17/cert-pl-cve-2026-44088-szafirhost-jar-zip-polyglot-bypass-in',
 'verdict': 'factual-error',
 'defects': [
  {'where': 'body paragraph 1 (Why it matters, eIDAS sentence)',
   'claim': 'Under eIDAS, qualified electronic signatures issued by a Polish QTSP enjoy cross-border legal recognition across EU member states and Switzerland\'s eIDAS-equivalent framework.',
   'defect': 'The Swiss federal authority states the opposite for Switzerland: no mutual recognition agreement with the EU exists, and a foreign-law qualified signature is not recognised as a Swiss qualified electronic signature. The sentence also supplies the entry\'s only Swiss nexus.',
   'ground_truth': 'To date, no agreement on the mutual recognition of electronic signatures has been concluded between Switzerland and another third country (or the European Union). Where no such agreement exists, a qualified electronic signature based on a qualified certificate under foreign law is not recognised as being equivalent to a qualified electronic signature under Swiss law.',
   'ground_truth_url': BK,
   'fix': 'Delete the Switzerland clause (eIDAS recognition applies across EU member states; Switzerland has no mutual recognition agreement with the EU as of 2026-10-21). Without it the entry has no Swiss nexus; reassess relevance and the high priority.',
   'class': 'factual-error'},
  {'where': 'body paragraph 1 (attacker path and fraudulent-signature sentences; actions[0])',
   'claim': 'An attacker who controls the JAR download path (MitM on the SzafirHost CDN/update channel, DNS interception, or a compromised mirror) can therefore execute arbitrary code inside SzafirHost — and silently sign fraudulent documents in the context of an authenticated KIR user session. / A successful zip-polyglot attack ... silently weaponises every signature produced on the compromised endpoint / could have produced silently-fraudulent signatures during the disclosure window',
   'defect': 'CERT-PL and EUVD state only that an attacker can combine a signed JAR with a malicious ZIP so a malicious class loads (RCE). They name no attacker position, no MitM/DNS/mirror vector, no signing of fraudulent documents and no "disclosure window". The EUVD CVSS 4.0 vector is AV:N/UI:A, but the attack path is not described.',
   'ground_truth': 'It can lead to remote code execution by allowing an attacker to combine a genuine, signed JAR file with a malicious ZIP file, causing the verification to pass but the malicious class to be loaded.',
   'ground_truth_url': CP,
   'fix': 'State the RCE mechanism as CERT-PL does; present the download-path scenario and any signing impact as the entry\'s analysis, clearly marked, or drop them; rewrite the action to "update SzafirHost to 1.2.1 or later on every signing workstation".',
   'class': 'factual-error'},
  {'where': 'body paragraph 1 (Technique class sentence)',
   'claim': 'Technique class: `T1574.002` DLL Side-Loading equivalent for Java class-path hijack.',
   'defect': 'T1574.002 is REVOKED in the pinned ATT&CK v20 dataset, and the flaw is a signature-verification bypass in a client helper, not DLL side-loading or class-path hijack.',
   'ground_truth': 'attack/enterprise-attack.json: T1574.002 "DLL Side-Loading" revoked=true. CERT-PL: verification passes "but the malicious class to be loaded"',
   'ground_truth_url': CP,
   'fix': 'Remove T1574.002; techniques[] T1203 (RCE in a client-side helper through a crafted JAR) and T1553 (signature verification bypass).',
   'class': 'factual-error'},
  {'where': 'summary; body paragraph 1 (Why it matters, first sentence)',
   'claim': 'Direct impact on Polish public administration, courts, procurement and healthcare workflows that produce qualified electronic signatures cross-recognised under eIDAS. / Szafir QES is one of the established Polish qualified signature ecosystems used in Polish public procurement, court e-filing, tax administration and healthcare e-signature workflows.',
   'defect': 'No page read carries these use cases or "direct impact". CERT-PL gives only vendor, product, affected versions and the flaw; KIR\'s Szafir site markets qualified signatures and seals with customer testimonials from companies, one of which mentions reporting to tax authorities.',
   'ground_truth': 'CERT-PL page: Vendor Krajowa Izba Rozliczeniowa; Product SzafirHost; Vulnerable versions All before 1.2.1; no statement on sectors or workflows.',
   'ground_truth_url': CP,
   'fix': 'Remove the sector list or attribute it to a source that states it.',
   'class': 'factual-error'},
  {'where': 'body paragraph 1 (sentence 1; SzafirHost description sentence)',
   'claim': 'SzafirHost, the browser-integration component of Poland\'s Szafir qualified electronic signature (QES) ecosystem operated by KIR, an eIDAS-recognised qualified trust service provider ... SzafirHost is the helper that downloads and loads signed JAR plugins to bridge smart-card signing into Chrome, Firefox, and Opera.',
   'defect': '(low confidence) The cited CERT-PL page names KIR as vendor and SzafirHost as the product only. A KIR customer help page (wFirma) says signing with a personal qualified certificate needs Java, a KIR browser plugin and the "Szafir Host" application; no page read names Chrome, Firefox or Opera or says SzafirHost "loads signed JAR plugins" (CERT-PL says it downloads a JAR, verifies its signature and loads classes from it). KIR\'s site describes eIDAS-compliant qualified products.',
   'ground_truth': 'wFirma: "najnowszej wersji JAVA, wtyczki do przeglądarki internetowej autorstwa KIR, aplikacji Szafir Host" (signing with a personal qualified certificate requires Java, a KIR browser plugin and the Szafir Host application)',
   'ground_truth_url': 'https://pomoc.wfirma.pl/-podpisywanie-deklaracji-i-dokumentow-wlasnym-podpisem-kwalifikowanym',
   'fix': 'SzafirHost is the helper application from Krajowa Izba Rozliczeniowa (KIR) used with its browser plugin and Java for qualified-signature signing; drop the browser list or cite it.',
   'class': 'imprecision'},
  {'where': 'cves[CVE-2026-44088]',
   'claim': '"cvss": "8.6", "affected": null, "fixed": null, "type": null',
   'defect': 'Affected and fixed versions are in the CERT-PL record; the 8.6 is CVSS 4.0 (stated in the body, not in the field); type is CWE-434 per CERT-PL.',
   'ground_truth': 'Vulnerable versions: All before 1.2.1; This issue was fixed in version 1.2.1; CWE-434 Unrestricted Upload of File with Dangerous Type. EUVD: baseScore 8.6, baseScoreVersion 4.0, CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:A/VC:H/VI:H/VA:H/SC:L/SI:L/SA:L, assigner CERT-PL, EPSS 0.71 (2026-10-21).',
   'ground_truth_url': CP,
   'fix': 'affected "< 1.2.1", fixed "1.2.1"; keep cvss 8.6 and say CVSS 4.0 (ENISA EUVD, CERT-PL is the CNA).',
   'class': 'imprecision'},
  {'where': 'body paragraph 1 (sentence 2); actions[0]; closing',
   'claim': 'records the CVSS 4.0 base 8.6 score used in this brief\'s footer / **Why it matters to us:** / Reference: § 1 SzafirHost item.',
   'defect': 'Pipeline self-reference to the v2 brief ("this brief\'s footer", "§ 1 SzafirHost item") and first-person "to us" in reader text; the EUVD and CERT-PL citation also does not cover the several uncited clauses after sentence 2.',
   'ground_truth': 'EUVD-2026-30512: baseScore 8.6, CVSS:4.0 vector; the migrated brief section is not a source.',
   'ground_truth_url': EU,
   'fix': 'Remove the brief references; cite CERT-PL for the version facts and ENISA EUVD for the score.',
   'class': 'imprecision'},
  {'where': 'priority',
   'claim': 'priority: high',
   'defect': '(low confidence) On the facts of 2026-05-17: no exploitation reported (CERT-PL, EUVD; not in CISA KEV on 2026-10-21), a Poland-specific signing helper, and the only Swiss nexus is the false eIDAS statement above. Fails the exposure-of-this-constituency test unless a Swiss user base is shown.',
   'ground_truth': 'CERT-PL post carries no exploitation statement; BAKOM: no EU-Swiss mutual recognition.',
   'ground_truth_url': BK,
   'fix': 'Consider notable or routine once the Swiss clause is removed.',
   'class': 'imprecision'},
 ],
 'upgrade': {
  'techniques': [
   {'id': 'T1203', 'behavior': 'Remote code execution in the client-side SzafirHost helper: genuine signed JAR combined with a malicious ZIP so the malicious class loads', 'url': CP},
   {'id': 'T1553', 'behavior': 'Signature verification bypass: JarInputStream verifies the signed JAR from the file start while JarFile/URLClassLoader loads classes from the Central Directory at the end', 'url': CP},
  ],
  'note': 'CERT-PL does not say how the malicious JAR reaches SzafirHost (no download-path, MitM or phishing vector); no initial-access technique mapped. T1574.002 in the entry is revoked.',
  'cve_facts': {'CVE-2026-44088': {'vendor': 'Krajowa Izba Rozliczeniowa (KIR)', 'product': 'SzafirHost', 'affected': '< 1.2.1', 'fixed': '1.2.1', 'cwe': 'CWE-434', 'cvss_4_0': '8.6 (ENISA EUVD, CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:A/VC:H/VI:H/VA:H/SC:L/SI:L/SA:L)', 'euvd': 'EUVD-2026-30512', 'ghsa': 'GHSA-j8f8-frc5-vgc6', 'cna': 'CERT-PL', 'kev': 'not in CISA KEV 2026-10-21', 'credit': 'Mariusz Maik'}},
  'rating': {'reliability': 'A', 'credibility': 2, 'basis': 'CERT-PL is the CNA and coordinating CERT for its own jurisdiction; ENISA EUVD restates the CERT-PL CNA record, so one assessor.'},
  'exposure': [
   {'quote': 'Vendor Krajowa Izba Rozliczeniowa | Product SzafirHost | Vulnerable versions All before 1.2.1', 'url': CP},
  ],
  'detection': [],
  'triage': [],
  'takeaway': [
   {'quote': 'This issue was fixed in version 1.2.1.', 'url': CP},
  ],
  'bodies': [P + 'szh-certpl.txt', P + 'szh-euvd.txt', P + 'szh-ghsa.txt', P + 'szh-bakom.txt', P + 'szh-wfirma.txt', P + 'szh-elektr.txt', P + 'szh-apps.txt'],
 },
 'possible_twin_outside_batch': 'entries/2026-06-30/cert-polska-discloses-a-jar-parser-confusion-rce-in-the-szaf (same product SzafirHost, different flaw CVE-2026-13165; not a twin, but cross-reference candidate)',
}
CLAIMS = '''
2e78f923bd ¦ ok ¦ https://cert.pl/en/posts/2026/05/CVE-2026-44088/ ¦ Vendor Krajowa Izba Rozliczeniowa; Product SzafirHost; JarInputStream vs JarFile/URLClassLoader with a malicious ZIP; fixed in 1.2.1
3f7dae32e0 ¦ F4 ¦ https://cert.pl/en/posts/2026/05/CVE-2026-44088/ ¦ CERT-PL: no "national eIDAS-recognised" helper, no sector impact; fixed in 1.2.1 and mechanism confirmed; Polish/Swiss cross-recognition and sector impact unsupported
53b056c8ec ¦ F4 ¦ https://cert.pl/en/posts/2026/05/CVE-2026-44088/ ¦ CERT-PL describes only RCE via signed-JAR plus malicious-ZIP; no fraudulent-signature or "disclosure window" statement
b5cd33a10e ¦ ok ¦ https://euvd.enisa.europa.eu/enisa/eu_vulnerability_database/EUVD-2026-30512 ¦ baseScore 8.6 CVSS 4.0 AV:N/UI:A; affected "0 <1.2.1"; entry has affected/fixed null (imprecision logged)
1fd9ef9553 ¦ F3 ¦ https://cert.pl/en/posts/2026/05/CVE-2026-44088/ ¦ CERT-PL carries Publication date 15 May 2026, vendor KIR, SzafirHost and the flaw; not "browser-integration component", Szafir QES ecosystem or KIR as eIDAS QTSP
e1c72caf44 ¦ ok ¦ https://euvd.enisa.europa.eu/enisa/eu_vulnerability_database/EUVD-2026-30512 ¦ "baseScore": 8.6, "baseScoreVersion": "4.0"; CERT-PL page has no CVSS
97b111152e ¦ F4 ¦ https://pomoc.wfirma.pl/-podpisywanie-deklaracji-i-dokumentow-wlasnym-podpisem-kwalifikowanym ¦ (low confidence) wFirma: requires Java, KIR browser plugin and Szafir Host; no page names Chrome/Firefox/Opera or "loads signed JAR plugins"
9f3a5a67d2 ¦ F5 ¦ https://cert.pl/en/posts/2026/05/CVE-2026-44088/ ¦ SzafirHost verifies the signature ... using class JarInputStream (reading from the beginning of the file), but loads classes using class JarFile/URLClassLoader (reading the Central Directory from the end)
60a8344e36 ¦ F4 ¦ https://cert.pl/en/posts/2026/05/CVE-2026-44088/ ¦ Quote is verbatim; MitM/DNS/mirror vector and "sign fraudulent documents in the context of an authenticated KIR user session" appear in no source
a1a79d6614 ¦ F4 ¦ https://cert.pl/en/posts/2026/05/CVE-2026-44088/ ¦ T1574.002 is revoked in attack/enterprise-attack.json; flaw is signature-verification bypass, not DLL side-loading
55ea452186 ¦ F5 ¦ https://cert.pl/en/posts/2026/05/CVE-2026-44088/ ¦ This issue was fixed in version 1.2.1.
5fbd2b7f6e ¦ F4 ¦ null ¦ No fetched page lists public procurement, court e-filing, tax administration or healthcare use of Szafir QES
f33f1c9d76 ¦ F4 ¦ https://www.bakom.admin.ch/en/electronic-signature ¦ no agreement on the mutual recognition of electronic signatures has been concluded between Switzerland ... (or the European Union); foreign-law QES not recognised as equivalent under Swiss law
004b30946f ¦ F4 ¦ https://cert.pl/en/posts/2026/05/CVE-2026-44088/ ¦ CERT-PL states RCE via crafted JAR only; no statement about "every signature produced on the compromised endpoint"
'''
