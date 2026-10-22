P = 'work/2026-10-21T1148Z-audit/truth-3/bodies/'
AE = 'https://www.aerzteblatt.de/news/hackerangriff-auf-rezeptprufer-c259a70c-595b-4770-9d84-87f6c8338c0c'
HE = 'https://www.heise.de/news/Niedersachsen-Datenabfluss-bei-Wirtschaftsprueferverein-im-Gesundheitswesen-11297772.html'
BO = 'https://borncity.com/blog/2026/05/16/cyberangriff-auf-die-arwini-rezeptpruefung-in-niedersachsen-mit-datenabfluss/'
ENTRY = {
 'entry': '2026-05-19/arwini-lower-saxony-statutory-prescription-audit-body-invest',
 'verdict': 'factual-error',
 'defects': [
  {'where': 'title; summary; body paragraph 1 (sentence 2)',
   'claim': 'ARWINI\'s own statement ... said particularly sensitive personal data (besondere Kategorien — GDPR Art. 9) are likely affected, with health and billing data on ≥70,000 patients in scope / ~70,000 GDPR Art. 9 records in scope',
   'defect': 'The 70,000 figure is HAZ/NDR research ("more than 70,000 records could have been captured"), not ARWINI\'s statement; ARWINI said up to 75,000 records in the worst case, its external data protection officer spoke of up to 80,000 anonymised records, and KVN says the patient data it sends is anonymised (pseudonymised). The sources count records, not patients, and none cites GDPR Art. 9. The contradiction is not surfaced.',
   'ground_truth': 'Nach Recherchen von HAZ und NDR könnten mehr als 70.000 Datensätze erbeutet worden sein. (According to HAZ and NDR research, more than 70,000 records may have been captured; translated from German) / Heise: "Arwini hatte erklärt, dass im schlimmsten Fall bis zu 75.000 Datensätze betroffen sein könnten." (Arwini said that in the worst case up to 75,000 records could be affected; translated from German)',
   'ground_truth_url': HE,
   'fix': 'ARWINI says personal and particularly sensitive data are likely affected and up to 75,000 records in the worst case (Heise); HAZ/NDR estimate more than 70,000 records (Ärzteblatt); Contradiction: KVN says the patient data it transmits is anonymised, and ARWINI\'s data protection officer spoke of anonymised records (NDR via Borns IT Blog).',
   'class': 'factual-error'},
  {'where': 'body paragraph 1 (sentence 3)',
   'claim': 'the Landesbeauftragter für Datenschutz Niedersachsen (LfD) and BSI have been notified under the GDPR 72-hour rule and the German KRITIS / NIS2UmsuCG framework',
   'defect': 'Heise reports only that a breach notification reached the LfD, with its timeliness under review; Borns IT Blog (citing NDR) says the LKA and the data-protection authority were notified. No source mentions BSI, KRITIS or NIS2UmsuCG.',
   'ground_truth': 'Inzwischen ist auch eine Meldung über eine Datenschutzverletzung beim Landesbeauftragten für den Datenschutz in Niedersachsen eingegangen. Ob die Meldung fristgerecht erfolgt sei, werde derzeit geprüft. (A data-breach notification has now been received by the Lower Saxony data protection commissioner; whether it was made on time is being examined; translated from German)',
   'ground_truth_url': HE,
   'fix': 'Polizeidirektion Hannover investigates; the Lower Saxony data protection commissioner has received a breach notification and is checking whether it was timely.',
   'class': 'factual-error'},
  {'where': 'body Why it matters paragraph',
   'claim': 'GKV bodies and their mandated third-party auditors are NIS2 entities; the supply-chain relationship between KVN/AOK and ARWINI is precisely the data-processor scope hit by NMDL/IGJ in the Netherlands (covered 2026-05-14).',
   'defect': 'No source states ARWINI\'s NIS2 status or links the case to the Dutch NMDL/IGJ incident; "(covered 2026-05-14)" and "Why it matters to us" are pipeline self-reference. (low confidence on the contradiction) A reader comment under the Borns IT Blog post says ARWINI has under 50 staff and fell outside NIS2 in the BSI self-assessment.',
   'ground_truth': 'Beim NIS-2-Betroffenheitstest des BSI fiel die ARWINI nicht unter NIS-2. (In the BSI NIS-2 applicability test ARWINI did not fall under NIS-2; reader comment, translated from German)',
   'ground_truth_url': BO,
   'fix': 'Drop the NIS2 classification and the NMDL/IGJ link, or attribute them as analysis.',
   'class': 'factual-error'},
  {'where': 'evidence[0]; evidence[1]; evidence[2]',
   'claim': '"Laut ARWINI ist es wahrscheinlich, dass personenbezogene und besonders schützenswerte Daten betroffen sind" / "Kairos ransomware group has claimed the attack" (Heise Security)',
   'defect': 'evidence[1] is not verbatim (the quoted statement reads "Nach derzeitigen Erkenntnissen ist es wahrscheinlich, dass personenbezogene und auch besonders schützenswerte Daten betroffen sind"). evidence[2] is an English sentence that does not appear on the German Heise page, which says the police confirmed Kairos is behind the attack. evidence[0] and evidence[1] are untranslated German without the English-quote plus original format.',
   'ground_truth': 'Hinter der Attacke steckt die Ransomware-Gruppe „Kairos", wie die Polizei heise online bestätigte. (The ransomware group Kairos is behind the attack, as the police confirmed to heise online; translated from German)',
   'ground_truth_url': HE,
   'fix': 'Replace with English translations marked "(translated from German)" and verbatim originals: Heise description; Ärzteblatt\'s quote of the ARWINI statement; Heise\'s police-confirmed Kairos attribution.',
   'class': 'factual-error'},
  {'where': 'body paragraph 1 (sentence 1); headline',
   'claim': 'Investigators confirmed on 2026-05-18 that the cyberattack on ARWINI ... resulted in confirmed exfiltration of personal data / Kairos ransomware group claims 2.87',
   'defect': 'The police confirmed that data flowed out; ARWINI\'s data protection officer said it was still unclear whether and which data left, so "personal data" is not confirmed. Heise also says the police confirmed Kairos is behind the attack (stronger than a claim), the 2.87 TB set was listed on 11 May and still unpublished despite the expired deadline, and the authorities are exchanging with Spanish investigators. The headline is cut mid-figure.',
   'ground_truth': 'sind nach Angaben der Polizeidirektion Hannover Daten aus dem System der Prüfstelle abgeflossen ... dass noch unklar sei, ob und welche Daten überhaupt abgeflossen seien (according to the Hannover police directorate, data left the audit body\'s system ... it was still unclear whether and which data had left; translated from German)',
   'ground_truth_url': HE,
   'fix': 'Police confirmed a data outflow; scope and data types unconfirmed; police confirm Kairos is behind the attack; 2.87 TB listed since 11 May, not yet published. Complete the headline.',
   'class': 'imprecision'},
  {'where': 'body paragraph 1 (Kairos and double-extortion sentences); uncited clauses',
   'claim': 'The technical pattern is consistent with double-extortion ransomware now in the operator-leak-site phase.',
   'defect': 'No source confirms encryption at ARWINI (Borns IT Blog infers ransomware from a left "message" and describes Kairos generically); clauses after sentence 2 carry no inline citation although Heise supports the police, LfD and Kairos facts.',
   'ground_truth': 'Aus der Formulierung "Die Hacker hinterließen demnach eine Botschaft." des NDR schließe ich, dass es eine Ransomware-Infektion gewesen sein könnte. Aber das ist absolute Spekulation (From NDR\'s wording that the hackers left a message I infer it could have been ransomware, but that is pure speculation; translated from German)',
   'ground_truth_url': BO,
   'fix': 'Say data-theft extortion with a leak-site listing; cite Heise on the Kairos and authority facts.',
   'class': 'imprecision'},
  {'where': 'priority',
   'claim': 'priority: high',
   'defect': '(low confidence) A German regional health-insurance audit body breach with no disclosed access vector or TTP and no Swiss exposure; the record count drives the item.',
   'ground_truth': 'Zur konkreten Datenhaltung und technischen Verarbeitung machte Arwini ebenfalls keine Aussagen. (Arwini also made no statement on its data holding or technical processing; translated from German)',
   'ground_truth_url': HE,
   'fix': 'Consider notable; the Kairos actor record carries the transferable signal.',
   'class': 'imprecision'},
 ],
 'upgrade': {
  'techniques': [
   {'id': 'T1657', 'behavior': 'Data-theft extortion: Kairos lists a 2.87 TB dataset on its leak site and threatens to sell it', 'url': HE},
  ],
  'note': 'No source states the access vector, the exfiltration channel or encryption at ARWINI; only the extortion behavior is mappable.',
  'rating': {'reliability': 'B', 'credibility': 2, 'basis': 'Heise and Deutsches Ärzteblatt report statements by the Hannover police (data outflow, Kairos attribution) and by ARWINI (likely affected data); victim and police agree on the breach, figures differ. Borns IT Blog is a C-tier blog restating NDR/HAZ.'},
  'exposure': [
   {'quote': 'Arwini processes health and billing data of statutorily insured people in Lower Saxony and, on behalf of the statutory health insurers and the Kassenärztliche Vereinigung Niedersachsen (KVN), audits the cost-effectiveness of medical prescriptions. (translated from German)', 'original': 'Arwini verarbeitet Gesundheits- und Abrechnungsdaten gesetzlich Versicherter in Niedersachsen und prüft im Auftrag der gesetzlichen Krankenkassen und der Kassenärztlichen Vereinigung Niedersachsen (KVN) die Wirtschaftlichkeit ärztlicher Verordnungen.', 'url': HE},
  ],
  'detection': [],
  'triage': [],
  'takeaway': [
   {'quote': 'Arwini advises potentially affected people to be especially careful with contact attempts and not to open suspicious emails or attachments. (translated from German)', 'original': 'Arwini empfiehlt möglichen Betroffenen, besonders aufmerksam bei Kontaktaufnahmen zu sein und keine verdächtigen E-Mails oder Anhänge zu öffnen.', 'url': AE},
  ],
  'bodies': [P + 'arw-aerzteblatt.txt', P + 'arw-heise.txt', P + 'arw-born.txt'],
 },
 'possible_twin_outside_batch': None,
}
CLAIMS = '''
f33257f43a ¦ ok ¦ https://www.heise.de/news/Niedersachsen-Datenabfluss-bei-Wirtschaftsprueferverein-im-Gesundheitswesen-11297772.html ¦ police: data flowed out; Kairos threatens sale of a 2.87 TB set listed since 11 May; discovery 4 May per KVN (Borns IT Blog); headline truncated (logged)
5b3d71ea9e ¦ ok ¦ https://www.aerzteblatt.de/news/hackerangriff-auf-rezeptprufer-c259a70c-595b-4770-9d84-87f6c8338c0c ¦ "könnten mehr als 70.000 Datensätze erbeutet worden sein" (HAZ/NDR); Träger AOK, KVN; Kairos leak site (Heise); figure attribution logged
4c023bd1a3 ¦ F3 ¦ https://www.heise.de/news/Niedersachsen-Datenabfluss-bei-Wirtschaftsprueferverein-im-Gesundheitswesen-11297772.html ¦ police: "Daten aus dem System der Prüfstelle abgeflossen"; DPO: "noch unklar ..., ob und welche Daten überhaupt abgeflossen seien" (personal data not confirmed)
10cd9d7ea7 ¦ F3 ¦ https://borncity.com/blog/2026/05/16/cyberangriff-auf-die-arwini-rezeptpruefung-in-niedersachsen-mit-datenabfluss/ ¦ "Am 4. Mai 2026 ... entdeckt, worauf alle Systeme sofort heruntergefahren wurden"; DPO: "bis zu 80.000 anonymisierte Datensätze" (no ≥70,000 patients)
e73cf116c5 ¦ F4 ¦ https://www.heise.de/news/Niedersachsen-Datenabfluss-bei-Wirtschaftsprueferverein-im-Gesundheitswesen-11297772.html ¦ Polizeidirektion Hannover confirmed; LfD received a notification (timeliness under review); BSI, KRITIS, NIS2UmsuCG in no source
cecd1949f7 ¦ F5 ¦ https://www.heise.de/news/Niedersachsen-Datenabfluss-bei-Wirtschaftsprueferverein-im-Gesundheitswesen-11297772.html ¦ "Kairos" droht mit dem Verkauf eines 2,87 Terabyte großen Datensatzes, der seit dem 11. Mai auf der Leaksite der Gruppe gelistet ist
9eb463bb4b ¦ F5 ¦ https://borncity.com/blog/2026/05/16/cyberangriff-auf-die-arwini-rezeptpruefung-in-niedersachsen-mit-datenabfluss/ ¦ encryption at ARWINI not confirmed; blog calls the ransomware inference "absolute Spekulation"
ea39f92978 ¦ F4 ¦ https://borncity.com/blog/2026/05/16/cyberangriff-auf-die-arwini-rezeptpruefung-in-niedersachsen-mit-datenabfluss/ ¦ no source states NIS2 status or NMDL/IGJ link; reader comment: "Beim NIS-2-Betroffenheitstest des BSI fiel die ARWINI nicht unter NIS-2"
8bb2cac73c ¦ F5 ¦ null ¦ composed supplier-inventory and 72-hour playbook advice; no fetched source
0991bc632b ¦ F5 ¦ https://www.aerzteblatt.de/news/hackerangriff-auf-rezeptprufer-c259a70c-595b-4770-9d84-87f6c8338c0c ¦ Arwini empfiehlt möglichen Betroffenen, besonders aufmerksam bei Kontaktaufnahmen zu sein und keine verdächtigen E-Mails oder Anhänge zu öffnen
'''
