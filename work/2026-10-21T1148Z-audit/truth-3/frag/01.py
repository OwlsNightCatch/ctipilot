P = 'work/2026-10-21T1148Z-audit/truth-3/bodies/'
REC = 'https://therecord.media/dream-market-admin-arrested-in-germany'
DEA = 'https://www.dea.gov/press-releases/2026/05/13/german-citizen-charged-laundering-funds-linked-prominent-darknet'
ENTRY = {
 'entry': '2026-05-16/bka-arrests-dream-market-lead-administrator-speedstepper-in',
 'verdict': 'factual-error',
 'defects': [
  {'where': 'body paragraph 1 (sentence 2: coordinated operation)',
   'claim': 'with the US DEA Miami, IRS-CI Cyber Crimes Unit, FBI, USPIS, and HSI executing in parallel',
   'defect': 'The DEA release gives DEA Miami and IRS-CI as the case investigators; FBI, USPIS and HSI appear only in the multi-agency task force that investigated Dream Market in 2016-2022, not as agencies executing the 2026 arrest.',
   'ground_truth': 'This case is being investigated by the IRS Criminal Investigation - Cyber Crimes Unit and DEA Miami Counternarcotic Cyber Investigations Task Force ... A multi-agency task force, including the Drug Enforcement Administration, Internal Revenue Service - Criminal Investigation, United States Postal Inspection Service, Federal Bureau of Investigation, Homeland Security Investigations, and the Fort Lauderdale Police Department, initially investigated Dream Market\'s criminal activities between 2016 and 2022.',
   'ground_truth_url': DEA,
   'fix': 'The arrest was a coordinated German and US effort; the case is investigated by IRS-CI Cyber Crimes Unit and DEA Miami with BKA Cybercrime Unit and ZKI Oldenburg assisting; FBI, USPIS and HSI belonged to the earlier 2016-2022 task force.',
   'class': 'factual-error'},
  {'where': 'body paragraph 1 (sentence 4: OPSEC failures)',
   'claim': 'consolidated the contents into a single wallet',
   'defect': 'Sources say funds were moved into new consolidated wallets (plural), not a single wallet.',
   'ground_truth': 'transferred funds into new, consolidated cryptocurrency wallets (the "Consolidated Wallets")',
   'ground_truth_url': DEA,
   'fix': 'consolidated the funds into new wallets',
   'class': 'factual-error'},
  {'where': 'body paragraph 1 (sentence 5: seizure)',
   'claim': 'At arrest, German authorities seized approximately USD 1.7 million in gold bars, USD 23,000 in cash, and approximately USD 1.2 million in cryptocurrency.',
   'defect': 'The sources say law enforcement "located" the gold and cash, and located information identifying bank accounts and crypto wallets holding about 1.2 million of suspected proceeds; neither says German authorities seized 1.2 million in cryptocurrency.',
   'ground_truth': 'law enforcement located approximately $1.7 million of gold bars ... as well as over $23,000 in cash. Law enforcement also located information identifying several bank accounts and cryptocurrency wallets containing approximately $1.2 million of funds believed to be proceeds of the Dream Market.',
   'ground_truth_url': DEA,
   'fix': 'Searches located about 1.7 million USD in gold bars and over 23,000 USD in cash, and identified bank accounts and crypto wallets holding about 1.2 million USD of suspected proceeds (DEA/DOJ release; The Record: "Agents found bank accounts and crypto wallets that held another $1.2 million").',
   'class': 'factual-error'},
  {'where': 'headline / title',
   'claim': 'BKA arrests Dream Market lead administrator "Speedstepper" in Germany',
   'defect': 'Neither source says the BKA made the arrest; the DEA release credits the BKA Cybercrime Unit and ZKI Oldenburg with "substantial assistance" and says he was arrested on German charges; The Record says German and US law enforcement arrested him. The headline also states the identity as fact where sources say "suspected"/"alleged".',
   'ground_truth': 'Owe Martin Andresen, the suspected main administrator of Dream Market ... was arrested last week in Germany on parallel charges brought by the German government. / During a May 7 raid on three locations, German and U.S. law enforcement arrested Owe Martin Andresen',
   'ground_truth_url': DEA,
   'fix': 'German authorities arrest suspected Dream Market main administrator ("Speedstepper") ...',
   'class': 'imprecision'},
  {'where': 'summary / body paragraph 1 (sentence 1)',
   'claim': 'alleged by US and German prosecutors to be "Speedstepper"',
   'defect': 'Only the US indictment/DOJ release links Andresen to the "Speedstepper" administrator role; the German charges described are money-laundering counts. No source says German prosecutors allege he is Speedstepper.',
   'ground_truth': 'Germany also has charged Andresen with several counts of concealment money laundering. / An indictment unsealed this week by the DOJ accused Andresen of being the main administrator of Dream Market.',
   'ground_truth_url': DEA,
   'fix': 'alleged by US prosecutors to be "Speedstepper" ... and also charged in Germany with money laundering',
   'class': 'imprecision'},
  {'where': 'summary',
   'claim': 'publicly identified on 2026-05-13–14 (The …',
   'defect': 'The summary string is cut off mid-sentence ("(The …"), truncated at migration.',
   'ground_truth': 'frontmatter summary ends: "(The …"',
   'ground_truth_url': 'entries/2026-05-16/bka-arrests-dream-market-lead-administrator-speedstepper-in.md',
   'fix': 'Complete the summary sentence; cite the DEA/DOJ release dated 2026-05-13 and The Record dated 2026-05-13.',
   'class': 'imprecision'},
  {'where': 'sources[0].publisher, body paragraph 1 citation, event_date',
   'claim': '[The Record, 2026-05-14] / event_date: 2026-05-14',
   'defect': 'The Record article carries datePublished 2026-05-13T19:56Z and the visible dateline "May 13th, 2026"; the entry cites 2026-05-14 (pipeline processing date).',
   'ground_truth': '"datePublished":"2026-05-13T19:56:19.603Z"; visible dateline "May 13th, 2026"',
   'ground_truth_url': REC,
   'fix': 'The Record, 2026-05-13; event_date 2026-05-13 (DEA/DOJ release also 2026-05-13).',
   'class': 'imprecision'},
  {'where': 'body paragraph 1 (sentence 4: wallet access)',
   'claim': 'providing prosecutors with a definitive on-chain link; ... providing the geographic and identity link',
   'defect': 'The release says the wallet activity "could only have been initiated by someone with access to Dream Market\'s original private keys, believed to be Speedstepper"; it is alleged, not described as a definitive link, and the OPSEC-failure framing ("closed the seven-year gap") is the entry\'s own gloss, uncited.',
   'ground_truth': 'activity that could only have been initiated by someone with access to Dream Market\'s original private keys, believed to be "Speedstepper."',
   'ground_truth_url': DEA,
   'fix': 'Say prosecutors allege the 2022 wallet activity could only have been initiated by the holder of the original private keys; drop "definitive" and attribute the OPSEC framing as analysis.',
   'class': 'imprecision'},
  {'where': 'body paragraph 1 (sentences 3, 4, 6; last sentence)',
   'claim': 'A US federal grand jury in the Northern District of Georgia had returned a sealed indictment on 2026-01-13 ...; Three Dream Market co-administrators ("Oxymonster", "KITT3N", "GOWRON") had been convicted previously; ... long-tail attribution of darknet operators is increasingly driven by post-cessation financial behaviour',
   'defect': 'Everything after the first sentence carries no inline citation (single citation closes sentence 1). Supported by the DEA/DOJ release (indictment date, counts, 20-year maximum per count, convictions of Oxymonster, KITT3N, GOWRON) and The Record ("unsealed", 240 years, five years). "Northern District of Georgia" is not in the page text read (US Attorney Hertzberg, Atlanta dateline; the DOJ release sits under usao-ndga). The "increasingly driven by" trend claim is not in any source.',
   'ground_truth': 'A federal grand jury returned an indictment on January 13, 2026, charging Owe Martin Andresen, 49, of Germany, with six counts of international concealment money laundering and six counts of concealment money laundering. Each federal charge provides for a sentence of up to 20 years in prison.',
   'ground_truth_url': DEA,
   'fix': 'Add inline citations (DEA/DOJ release for the indictment, convictions and amounts; The Record for the 240/5-year maxima); remove or mark as analysis the "increasingly" generalisation.',
   'class': 'imprecision'},
 ],
 'upgrade': {
  'techniques': [],
  'note': 'Law-enforcement action against a marketplace operator; sources describe laundering via consolidated wallets and gold purchases, no intrusion or ATT&CK enterprise behavior and no stated access vector. No technique is supported.',
  'rating': {'reliability': 'A', 'credibility': 2, 'basis': 'DOJ/DEA/IRS-CI release is the prosecuting authority speaking about its own indictment; The Record restates the same DOJ release with the US Attorney quote, so one assessor, uncorroborated by an independent party (allegations, not yet proven).'},
  'exposure': [],
  'detection': [],
  'triage': [],
  'takeaway': [
   {'quote': 'The reintegration of long dormant proceeds demonstrates a hard truth: illicit actors may hide in the shadows, but their financial footprints remain.', 'url': DEA},
  ],
  'bodies': [P + 'bka-record.txt', P + 'bka-dea.txt', P + 'bka-irs.txt'],
 },
 'possible_twin_outside_batch': None,
}
CLAIMS = '''
1ba57b420b ¦ F4 ¦ https://www.dea.gov/press-releases/2026/05/13/german-citizen-charged-laundering-funds-linked-prominent-darknet ¦ Owe Martin Andresen, the suspected main administrator ... was arrested last week in Germany on parallel charges brought by the German government (BKA only "substantial assistance")
d849414527 ¦ F4 ¦ https://www.dea.gov/press-releases/2026/05/13/german-citizen-charged-laundering-funds-linked-prominent-darknet ¦ Germany also has charged Andresen with several counts of concealment money laundering (no source: German prosecutors allege Speedstepper identity); summary truncated "(The …"
2d9aa14344 ¦ F3 ¦ https://therecord.media/dream-market-admin-arrested-in-germany ¦ "An indictment unsealed this week by the DOJ accused Andresen of being the main administrator"; dateline May 13th, 2026 (entry cites 05-14); no German-prosecutor attribution
477bbbb323 ¦ F4 ¦ https://www.dea.gov/press-releases/2026/05/13/german-citizen-charged-laundering-funds-linked-prominent-darknet ¦ investigated by IRS-CI Cyber Crimes Unit and DEA Miami ... task force incl. DEA, IRS-CI, USPIS, FBI, HSI ... initially investigated Dream Market between 2016 and 2022
9dea88322d ¦ F5 ¦ https://www.dea.gov/press-releases/2026/05/13/german-citizen-charged-laundering-funds-linked-prominent-darknet ¦ A federal grand jury returned an indictment on January 13, 2026 ... six counts ... Each federal charge ... up to 20 years; The Record: up to 240 years / five years for German charges
31b6b4932b ¦ F4 ¦ https://www.dea.gov/press-releases/2026/05/13/german-citizen-charged-laundering-funds-linked-prominent-darknet ¦ transferred funds into new, consolidated cryptocurrency wallets (plural); "believed to be Speedstepper" (not "definitive")
f2214287d8 ¦ F4 ¦ https://www.dea.gov/press-releases/2026/05/13/german-citizen-charged-laundering-funds-linked-prominent-darknet ¦ law enforcement located ~$1.7 million of gold bars ... over $23,000 in cash ... located information identifying several bank accounts and cryptocurrency wallets containing approximately $1.2 million
d6edecd28a ¦ F5 ¦ https://www.dea.gov/press-releases/2026/05/13/german-citizen-charged-laundering-funds-linked-prominent-darknet ¦ "Oxymonster" and "KITT3N" were previously convicted ...; "GOWRON" was convicted in a prosecution by the United Kingdom Crown Prosecution Service
9ca6656eff ¦ F5 ¦ null ¦ analytic generalisation ("increasingly driven by post-cessation financial behaviour") found in no fetched source; closure 2019 and arrest 2026 supported by DEA release
'''
