P = 'work/2026-10-21T1148Z-audit/truth-3/bodies/'
SW = 'https://www.securityweek.com/7-eleven-data-breach-confirmed-after-shinyhunters-ransom-demand/'
SA = 'https://securityaffairs.com/192336/data-breach/shinyhunters-hack-7-eleven-franchisee-data-and-salesforce-records-exposed.html'
CD = 'https://www.cybersecuritydive.com/news/7-eleven-cyberattack-franchisee-data/820698/'
CI = 'https://cyberinsider.com/charter-communications-confirms-data-breach-as-hackers-threaten-leak-of-42-million-records/'
TH = 'https://www.troyhunt.com/weekly-update-505/'
MA = 'https://www.maine.gov/agviewer/content/ag/985235c7-cb95-4be2-8792-a1252b4f8318/4fe778c0-a3a9-4dbe-8e79-2c229ac5c36b.html'
ENTRY = {
 'entry': '2026-05-19/7-eleven-confirms-shinyhunters-breach-of-600-000-salesforce',
 'verdict': 'factual-error',
 'defects': [
  {'where': 'title; headline; summary',
   'claim': '7-Eleven confirms ShinyHunters breach of 600,000+ Salesforce franchise-application records',
   'defect': '7-Eleven confirmed unauthorized access to systems storing franchisee documents; the 600,000+ Salesforce records figure is ShinyHunters\' leak-site claim, and 7-Eleven did not respond on the ShinyHunters claim. State filings put the affected people at about 50 (47 Massachusetts, 2 Maine, 1 Vermont). The 600,000 claimed records are described as PII and corporate data, not franchise applications.',
   'ground_truth': 'ShinyHunters listed 7-Eleven on its leak website on April 17, claiming to have stolen more than 600,000 Salesforce records, including personal information and corporate data. (SecurityWeek) / The breach impacted 47 people in Massachusetts, 2 in Maine and one in Vermont ... 7-Eleven\'s spokesperson did not respond by press time when asked about this information. (Cybersecurity Dive)',
   'ground_truth_url': CD,
   'fix': '7-Eleven confirms breach of franchisee documents after ShinyHunters claims 600,000+ Salesforce records',
   'class': 'factual-error'},
  {'where': 'title; headline; summary; body paragraph 1 (campaign sentence)',
   'claim': 'same campaign as Instructure, Vimeo, Wynn Resorts, Vercel, Medtronic / SecurityWeek attributes the broader campaign — Instructure (Canvas), Vimeo, Wynn Resorts (21,000 employees), Vercel and Medtronic among confirmed co-victims — ... customer-side misconfiguration of Salesforce Connected Apps',
   'defect': 'SecurityWeek says only that the group and affiliated actors "took credit" for those attacks; it does not place them in the Salesforce campaign or call them confirmed co-victims, and it says "misconfigurations", not Connected Apps.',
   'ground_truth': 'The intrusions resulted from phishing, abuse of third-party integrations, or misconfigurations, rather than vulnerabilities in Salesforce products or systems. The hacker group and affiliated threat actors recently took credit for attacks on Instructure, Vimeo, Wynn Resorts, Vercel, and Medtronic.',
   'ground_truth_url': SW,
   'fix': 'ShinyHunters has targeted Salesforce instances since mid-2025 via phishing, third-party-integration abuse or misconfigurations (SecurityWeek); the group also recently claimed Instructure, Vimeo, Wynn Resorts, Vercel and Medtronic.',
   'class': 'factual-error'},
  {'where': 'section 2026-05-25T05:00:03Z (pattern sentence); updates[0].summary',
   'claim': 'the same vector behind the confirmed 7-Eleven breach (600k records, covered 2026-05-19) / a fresh victim in the Salesforce-credential campaign tracked here via 7-Eleven',
   'defect': 'No source states the 7-Eleven intrusion vector (7-Eleven disclosed none) and the 600k figure is the actor\'s claim, not confirmed. CyberInsider says the Charter breach "appears linked" to the Salesforce campaign.',
   'ground_truth': 'The breach appears linked to an ongoing large-scale campaign targeting Salesforce environments and enterprise cloud infrastructure. ... The company did not disclose how attackers may have gained access to its systems',
   'ground_truth_url': CI,
   'fix': 'Charter, like 7-Eleven, was listed by ShinyHunters; CyberInsider links the Charter claim to the Salesforce-focused campaign. Drop the 7-Eleven vector claim.',
   'class': 'factual-error'},
  {'where': 'body paragraph 1 (Maine sentence); sources[2]',
   'claim': '7-Eleven filed a Maine Attorney General notification dated 2026-05-01 confirming 24 months of IDX identity-theft protection',
   'defect': 'The cited Maine AG page is unreadable on every transport (403 authentication required on extract, raw bridge, reader and WebFetch). Cybersecurity Dive confirms IDX for up to 24 months and 2 Maine residents, but May 1 is the date of the letter to individuals; the state filings were made the week before 2026-05-20.',
   'ground_truth': 'Jim Kastle ... said in a letter sent to impacted individuals on May 1 ... 7-Eleven has arranged for impacted individuals to enroll in identity theft protection services with theft protection agency IDX for up to 24 months. ... according to data breach filings presented to those states last week.',
   'ground_truth_url': CD,
   'fix': 'Notification letters dated 2026-05-01 offer up to 24 months of IDX identity protection; filings in Massachusetts, Maine and Vermont count about 50 affected (cite Cybersecurity Dive, or the Massachusetts filing it links).',
   'class': 'imprecision'},
  {'where': 'body paragraph 1 (sentence 1)',
   'claim': '7-Eleven, Inc. confirmed on 2026-05-18 that an unauthorised third party accessed systems storing franchisee documents on 2026-04-08',
   'defect': '2026-05-18 is the press date; the confirmation is the 2026-05-01 letter and state filings (SecurityWeek: "has started sending out security incident notices"). The April 8 access date is right per the letter.',
   'ground_truth': 'We recently discovered that on April 8, 2026, an unauthorized third party gained access to certain 7-Eleven systems used to store franchisee documents. (letter quoted by Security Affairs)',
   'ground_truth_url': SA,
   'fix': '7-Eleven\'s notification letters (2026-05-01, reported 2026-05-18) say an unauthorized party accessed systems storing franchisee documents on 2026-04-08.',
   'class': 'imprecision'},
  {'where': 'section 2026-05-25T05:00:03Z (Charter statement sentence)',
   'claim': 'Charter issued a narrowly-worded statement confirming it is "following security protocols"',
   'defect': 'Misquote: the statement reads "following our security protocols".',
   'ground_truth': '"We are aware of the situation, following our security protocols, and are in the process of alerting appropriate authorities. No sensitive personal information (PI) or customer proprietary network information (CPNI) data was exfiltrated by the threat actor."',
   'ground_truth_url': CI,
   'fix': 'Quote "following our security protocols".',
   'class': 'imprecision'},
  {'where': 'section 2026-05-25T05:00:03Z; updates[0]; entry scope',
   'claim': 'By our own campaign tracking Charter is the first telco/ISP victim of this wave to respond publicly ... (600k records, covered 2026-05-19) ... tracked here via 7-Eleven',
   'defect': 'Pipeline self-reference ("our own campaign tracking", "covered 2026-05-19", "tracked here", "Why it matters to us") and an unsourced "first" quantifier in reader text. The section also appends a different victim (Charter) to the 7-Eleven entry; a separate entry, 2026-05-27/shinyhunters-salesforce-campaign-charter-and-7-eleven-both-c, covers both.',
   'ground_truth': 'CyberInsider: Charter "confirmed a cybersecurity incident after the ShinyHunters extortion group claimed it breached" it; no source ranks it first among telcos.',
   'ground_truth_url': CI,
   'fix': 'Drop the self-reference and the "first" claim; decide with the twin entry which one carries Charter.',
   'class': 'imprecision'},
  {'where': 'section 2026-05-25T05:00:03Z (non-CPNI PII sentence); entry status',
   'claim': 'The exclusion of *non*-CPNI PII (billing name, address, email) from that denial is conspicuous and leaves room for lower-sensitivity data exposure even if the denial holds.',
   'defect': 'Superseded: CyberInsider\'s later update says the dataset was leaked and Have I Been Pwned counted 4.9 million unique email addresses with names, phone numbers and physical addresses. The entry has no record of this.',
   'ground_truth': 'UPDATE: The attackers later leaked the stolen dataset publicly. According to Have I Been Pwned, the exposure impacted 4.9 million unique email addresses and included associated names, phone numbers, and physical addresses.',
   'ground_truth_url': CI,
   'fix': 'Add an update record: Charter dataset leaked; HIBP 4.9 million unique emails with names, phone numbers, addresses.',
   'class': 'imprecision'},
  {'where': 'body Why it matters paragraph (T-ids; vector and recommendations); frontmatter',
   'claim': 'Connected App OAuth grant abuse, phishing of admin sessions, mis-scoped third-party SaaS integrations ... T1078.004 (Cloud Accounts), T1530 (Data from Cloud Storage Object), T1567.002 (Exfiltration to Cloud Storage). / techniques: [] / classification: null / entities: incident:medtronic-shinyhunters-corporate-it-breach',
   'defect': 'The vector detail goes beyond SecurityWeek\'s "phishing, abuse of third-party integrations, or misconfigurations"; no source supports exfiltration to cloud storage (T1567.002) and T1530 is cloud storage, not a SaaS CRM. The ids sit in prose while techniques[] is empty; classification is null; the Medtronic incident key is linked although the entry is about 7-Eleven. Recommendations (Event Monitoring alerts, Trusted-IP, Shield encryption, SELECT baselines) are composed and uncited.',
   'ground_truth': 'The intrusions resulted from phishing, abuse of third-party integrations, or misconfigurations, rather than vulnerabilities in Salesforce products or systems.',
   'ground_truth_url': SW,
   'fix': 'Move mapping to techniques[] with only supported ids (see upgrade); set classification; replace the Medtronic incident link with a 7-Eleven incident key or the actor only; mark recommendations as derived.',
   'class': 'imprecision'},
  {'where': 'priority',
   'claim': 'priority: high',
   'defect': '(low confidence) A US retailer franchisee-document breach of about 50 people with no disclosed vector; the record-count claim is the main driver, a listed high disqualifier.',
   'ground_truth': 'The breach impacted 47 people in Massachusetts, 2 in Maine and one in Vermont',
   'ground_truth_url': CD,
   'fix': 'Consider notable (actor relevance) or fold into a ShinyHunters campaign entry.',
   'class': 'imprecision'},
 ],
 'upgrade': {
  'techniques': [
   {'id': 'T1213', 'behavior': 'Theft of records from Salesforce CRM instances (claimed 600,000+ for 7-Eleven)', 'url': SW},
   {'id': 'T1657', 'behavior': 'Extortion: leak-site listing with ransom deadline, then data offered for sale', 'url': SW},
   {'id': 'T1566', 'behavior': 'Campaign-level: intrusions via phishing (not stated for 7-Eleven specifically)', 'url': SW},
   {'id': 'T1199', 'behavior': 'Campaign-level: abuse of third-party integrations (not stated for 7-Eleven specifically)', 'url': SW},
  ],
  'note': 'Neither 7-Eleven nor Charter disclosed an access vector; campaign-level vectors come from SecurityWeek and CyberInsider and must be labelled as such.',
  'rating': {'reliability': 'B', 'credibility': 2, 'basis': 'Outlets quoting the victim\'s notification letter and state filings (breach confirmed); the 600,000-record and 42M figures are actor claims (credibility 3-4 on their own). Victim notice page itself unreadable.'},
  'exposure': [
   {'quote': 'an intrusion into 7-Eleven systems used to store franchisee documents was detected on April 8. ... The exposed information was provided to the company during franchise applications.', 'url': SW},
   {'quote': 'ShinyHunters has been targeting the Salesforce instances of major organizations since mid-2025, stealing millions of data records. The intrusions resulted from phishing, abuse of third-party integrations, or misconfigurations, rather than vulnerabilities in Salesforce products or systems.', 'url': SW},
  ],
  'detection': [],
  'triage': [],
  'takeaway': [
   {'quote': 'ShinyHunters has recently claimed responsibility for multiple intrusions involving companies whose environments allegedly contained exposed credentials, authentication tokens, or improperly secured integrations.', 'url': CI},
  ],
  'bodies': [P + '7e-sw.txt', P + '7e-sa.txt', P + '7e-csdive.txt', P + '7e-ci.txt', P + '7e-th.txt'],
 },
 'possible_twin_outside_batch': 'entries/2026-05-27/shinyhunters-salesforce-campaign-charter-and-7-eleven-both-c (covers both the 7-Eleven confirmation and the Charter listing, with a ~185,000 7-Eleven count)',
}
CLAIMS = '''
ef93d7dbe3 ¦ F4 ¦ https://www.cybersecuritydive.com/news/7-eleven-cyberattack-franchisee-data/820698/ ¦ 7-Eleven confirmed franchisee-document access; 600,000 is ShinyHunters' claim; ~50 people in MA/ME/VT filings; spokesperson did not respond on the claim
7fd0ca38b1 ¦ F4 ¦ https://www.securityweek.com/7-eleven-data-breach-confirmed-after-shinyhunters-ransom-demand/ ¦ "The hacker group and affiliated threat actors recently took credit for attacks on Instructure, Vimeo..." (not confirmed co-victims of the Salesforce campaign)
7b54ea6ba7 ¦ ok ¦ https://securityaffairs.com/192336/data-breach/shinyhunters-hack-7-eleven-franchisee-data-and-salesforce-records-exposed.html ¦ "on April 8, 2026, an unauthorized third party gained access to certain 7-Eleven systems used to store franchisee documents"; listed April 17 (SW); confirm date imprecise (logged)
521484927c ¦ unreadable ¦ https://www.maine.gov/agviewer/content/ag/985235c7-cb95-4be2-8792-a1252b4f8318/4fe778c0-a3a9-4dbe-8e79-2c229ac5c36b.html ¦ Maine AG page 403 on all rungs; CSDive: letter of May 1, IDX up to 24 months; SW: 600k claim, April 21 deadline, $250,000 sale
4b690923a1 ¦ F5 ¦ https://www.securityweek.com/7-eleven-data-breach-confirmed-after-shinyhunters-ransom-demand/ ¦ said only two Maine residents were impacted ... claiming to have stolen more than 600,000 Salesforce records
dc50f3d03b ¦ F13 ¦ https://www.securityweek.com/7-eleven-data-breach-confirmed-after-shinyhunters-ransom-demand/ ¦ SW lists Instructure, Vimeo, Wynn, Vercel, Medtronic as attacks the group "took credit for"; no co-victim statement, no "Connected Apps"
a51b0592db ¦ F5 ¦ https://www.securityweek.com/7-eleven-data-breach-confirmed-after-shinyhunters-ransom-demand/ ¦ The hacker group and affiliated threat actors recently took credit for attacks on Instructure
272cc00555 ¦ F4 ¦ https://www.securityweek.com/7-eleven-data-breach-confirmed-after-shinyhunters-ransom-demand/ ¦ (low confidence) SW: "phishing, abuse of third-party integrations, or misconfigurations"; Connected App OAuth grant abuse and admin-session phishing not stated
805ee74e8e ¦ F5 ¦ null ¦ composed Salesforce hardening recommendations; no fetched source states them
2e5cb01182 ¦ F4 ¦ https://www.securityweek.com/7-eleven-data-breach-confirmed-after-shinyhunters-ransom-demand/ ¦ no source describes exfiltration to cloud storage (T1567.002) or cloud storage object access (T1530); vector undisclosed
26fe0c73df ¦ ok ¦ https://cyberinsider.com/charter-communications-confirms-data-breach-as-hackers-threaten-leak-of-42-million-records/ ¦ "over 42M records containing PII" ... leaked if negotiations are not opened before May 27, 2026; Troy Hunt shows the May 22 listing
2e7aedfd3e ¦ ok ¦ https://www.troyhunt.com/weekly-update-505/ ¦ "ShinyHunters Claims 3 New Victims ... Charter Communications, Inc." (Dark Web Informer, May 22, 2026)
3abcecebb3 ¦ F5 ¦ https://cyberinsider.com/charter-communications-confirms-data-breach-as-hackers-threaten-leak-of-42-million-records/ ¦ the exact nature of the allegedly stolen data has not been independently verified
bddca55e3d ¦ F4 ¦ https://cyberinsider.com/charter-communications-confirms-data-breach-as-hackers-threaten-leak-of-42-million-records/ ¦ statement reads "following our security protocols" (entry drops "our"); PI/CPNI denial quote verbatim
8fea65b395 ¦ F5 ¦ https://cyberinsider.com/charter-communications-confirms-data-breach-as-hackers-threaten-leak-of-42-million-records/ ¦ analysis; superseded: dataset leaked, HIBP 4.9 million unique emails with names, phone numbers, physical addresses
35e0a319e4 ¦ F14 ¦ https://cyberinsider.com/charter-communications-confirms-data-breach-as-hackers-threaten-leak-of-42-million-records/ ¦ no source says Charter is the first telco/ISP victim to respond; self-declared inference ("by our own campaign tracking")
3a2534838f ¦ F13 ¦ https://cyberinsider.com/charter-communications-confirms-data-breach-as-hackers-threaten-leak-of-42-million-records/ ¦ CI: breach "appears linked" to the Salesforce campaign; no source states 7-Eleven's vector; 600k is a claim
cfbbf6afb0 ¦ F5 ¦ null ¦ composed recommendations (connected-app scopes, guest-user access, Shield Event Monitoring); no fetched source
597d886c4e ¦ F14 ¦ https://cyberinsider.com/charter-communications-confirms-data-breach-as-hackers-threaten-leak-of-42-million-records/ ¦ 42M claim, 27 May deadline and PI/CPNI denial confirmed; "first telco/ISP victim" unsourced; "tracked here" self-reference
'''
