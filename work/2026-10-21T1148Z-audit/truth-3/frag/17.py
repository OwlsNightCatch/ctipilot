P = 'work/2026-10-21T1148Z-audit/truth-3/bodies/'
IP = 'https://www.interpol.int/en/News-and-Events/News/2026/201-arrests-in-first-of-its-kind-cybercrime-operation-in-MENA-region'
TH = 'https://thehackernews.com/2026/05/interpol-operation-ramz-disrupts-mena.html'
HN = 'https://www.helpnetsecurity.com/2026/05/18/interpol-mena-cybercrime-operation-ramz-201-arrests/'
ENTRY = {
 'entry': '2026-05-19/interpol-operation-ramz-13-country-mena-cybercrime-sweep-201',
 'verdict': 'factual-error',
 'defects': [
  {'where': 'body Why it matters paragraph',
   'claim': 'MENA-based PhaaS kits routinely target EU banking customers and EU payment rails (SEPA-Inst flagging, IBAN-based phishing lures); the disruption reduces commodity-kit availability and the Shadowserver / Group-IB intelligence shared via the operation will surface in NCSC / BSI / NCSC-CH advisories over the coming weeks. The trafficking-to-scam pipeline confirmed in Jordan is the same operator model EUROPOL has been mapping for fraud-compound disruption.',
   'defect': 'No source says the disrupted operations targeted EU customers or payment rails, predicts national-CERT advisories, or links the Jordan case to Europol\'s fraud-compound work; INTERPOL frames the scams as costing "the region". These claims carry the entry\'s only EU/CH nexus.',
   'ground_truth': 'The operation focused on neutralizing phishing and malware threats, as well as tackling cyber scams that inflict severe cost to the region.',
   'ground_truth_url': IP,
   'fix': 'Remove the EU-targeting, advisory prediction and Europol claims, or mark them as the entry\'s analysis with a source; relevance then rests on the transferable trafficking-to-scam and PhaaS lessons.',
   'class': 'factual-error'},
  {'where': 'body paragraph 1 (Jordan sentence)',
   'claim': 'Jordanian police rescued 15 human-trafficking victims who had been coerced into running cybercrime operations — the same forced-labour-to-cyber-scam pipeline documented in Southeast Asian fraud compounds.',
   'defect': 'INTERPOL says a raid uncovered 15 people running investment scams who were trafficking victims recruited from Asia, and that two suspected organisers were arrested; it does not say "rescued" or link the case to Southeast Asian compounds.',
   'ground_truth': 'A raid uncovered 15 individuals carrying out the scams, but investigators determined that they were victims of human trafficking who had been recruited under the false promise of employment from their home countries in Asia. Upon arrival in Jordan, their passports were confiscated, and they were forced or coerced into participating in the scheme. Two individuals suspected of orchestrating the operation were arrested.',
   'ground_truth_url': IP,
   'fix': 'Jordanian police found 15 people running a fake trading-platform investment scam who were trafficking victims recruited from Asia with passports confiscated; two suspected organisers were arrested.',
   'class': 'imprecision'},
  {'where': 'summary; body paragraph 1 (uncited clauses)',
   'claim': 'summary ends "(Algeria, Bahrain, Egypt, Iraq, Jordan, Lebanon, Libya, Morocco, Oman …" / Outcomes: ... Algerian authorities dismantled ... Industry partners ... CyberSouth+',
   'defect': 'The summary is truncated mid-list at migration. All outcome sentences after sentence 1 carry no inline citation although INTERPOL\'s release carries them; the Algeria item omits the seized mobile phone and the arrest, and the Qatar compromised-devices finding is missing.',
   'ground_truth': 'In Algeria, a website offering phishing as a service was identified and dismantled ... authorities successfully seized a server, a computer, a mobile phone and hard drives containing phishing software and scripts. One suspect was taken into custody.',
   'ground_truth_url': IP,
   'fix': 'Complete the summary; cite INTERPOL on each outcome; add the Algeria arrest and the Qatar finding (compromised devices used unknowingly to spread malicious threats).',
   'class': 'imprecision'},
 ],
 'upgrade': {
  'techniques': [
   {'id': 'T1566', 'behavior': 'Phishing operations, including a phishing-as-a-service website dismantled in Algeria and phishing software seized in Morocco', 'url': IP},
   {'id': 'T1584', 'behavior': 'Compromised devices in Qatar unknowingly used to spread malicious threats', 'url': IP},
   {'id': 'T1657', 'behavior': 'Investment fraud through a fake trading platform that shut down after deposits (Jordan)', 'url': IP},
  ],
  'note': 'Law-enforcement roundup; techniques describe the disrupted activity at a high level only.',
  'rating': {'reliability': 'A', 'credibility': 2, 'basis': 'INTERPOL speaking about its own operation; THN and Help Net Security restate the release.'},
  'exposure': [],
  'detection': [],
  'triage': [],
  'takeaway': [
   {'quote': 'investigators determined that they were victims of human trafficking who had been recruited under the false promise of employment from their home countries in Asia. Upon arrival in Jordan, their passports were confiscated, and they were forced or coerced into participating in the scheme.', 'url': IP},
  ],
  'bodies': [P + 'ramz-interpol.txt', P + 'ramz-thn.txt', P + 'ramz-hns.txt'],
 },
 'possible_twin_outside_batch': None,
}
CLAIMS = '''
8b4fa79f81 ¦ ok ¦ https://www.interpol.int/en/News-and-Events/News/2026/201-arrests-in-first-of-its-kind-cybercrime-operation-in-MENA-region ¦ arrest of 201 individuals ... 53 servers were seized ... In Algeria, a website offering phishing as a service was identified and dismantled; 13 countries
b4d4523005 ¦ ok ¦ https://www.interpol.int/en/News-and-Events/News/2026/201-arrests-in-first-of-its-kind-cybercrime-operation-in-MENA-region ¦ "first cyber operation of its scale coordinated by INTERPOL in the MENA region"; October 2025 – 28 February 2026; summary truncated (logged)
fc2811f690 ¦ ok ¦ https://www.interpol.int/en/News-and-Events/News/2026/201-arrests-in-first-of-its-kind-cybercrime-operation-in-MENA-region ¦ Participating countries: Algeria, Bahrain, Egypt, Iraq, Jordan, Lebanon, Libya, Morocco, Oman, Palestine, Qatar, Tunisia, UAE; dated 2026-05-18 (THN, HNS same day)
948e86850e ¦ F5 ¦ https://www.interpol.int/en/News-and-Events/News/2026/201-arrests-in-first-of-its-kind-cybercrime-operation-in-MENA-region ¦ 201 individuals, a further 382 suspects ... 3,867 victims ... 53 servers ... nearly 8,000 pieces of crucial data and intelligence were disseminated
64aed0bd0b ¦ F5 ¦ https://www.interpol.int/en/News-and-Events/News/2026/201-arrests-in-first-of-its-kind-cybercrime-operation-in-MENA-region ¦ seized a server, a computer, a mobile phone and hard drives containing phishing software and scripts. One suspect was taken into custody.
1347820c57 ¦ F5 ¦ https://www.interpol.int/en/News-and-Events/News/2026/201-arrests-in-first-of-its-kind-cybercrime-operation-in-MENA-region ¦ Moroccan authorities seized computers, smartphones and external hard drives containing banking data ... Oman: server in a private residence ... including malware infection
be80cd0fed ¦ F13 ¦ https://www.interpol.int/en/News-and-Events/News/2026/201-arrests-in-first-of-its-kind-cybercrime-operation-in-MENA-region ¦ 15 trafficking victims recruited from Asia, forced or coerced; two organisers arrested; no "rescued" and no Southeast Asian compound link
1bc4d21581 ¦ F5 ¦ https://www.interpol.int/en/News-and-Events/News/2026/201-arrests-in-first-of-its-kind-cybercrime-operation-in-MENA-region ¦ INTERPOL worked closely with its partners, Group-IB, Kaspersky, the Shadowserver Foundation, Team Cymru and TrendAI
723a8047f1 ¦ F5 ¦ https://www.interpol.int/en/News-and-Events/News/2026/201-arrests-in-first-of-its-kind-cybercrime-operation-in-MENA-region ¦ partially funded by the European Union and the Council of Europe under the CyberSouth+ project
dd3347f079 ¦ F4 ¦ https://www.interpol.int/en/News-and-Events/News/2026/201-arrests-in-first-of-its-kind-cybercrime-operation-in-MENA-region ¦ no source on EU banking/SEPA targeting or forthcoming NCSC/BSI/NCSC-CH advisories; scams "inflict severe cost to the region"
52fde357de ¦ F13 ¦ https://www.interpol.int/en/News-and-Events/News/2026/201-arrests-in-first-of-its-kind-cybercrime-operation-in-MENA-region ¦ no source links the Jordan case to a Europol fraud-compound mapping
'''
