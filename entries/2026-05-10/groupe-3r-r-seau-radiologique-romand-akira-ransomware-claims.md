---
schema: 1
kind: incident
title: >
  Groupe 3R (Réseau Radiologique Romand): Akira ransomware attack on 20 Swiss imaging centres,
  administrative data stolen and published, medical data encrypted
headline: >
  Akira ransomware hits Swiss imaging network Groupe 3R; administrative data stolen and published, medical data encrypted
summary: >
  Groupe 3R (Réseau Radiologique Romand), which runs 20 medical-imaging centres in seven Swiss cantons,
  was hit on 2026-04-30 by a ransomware attack that encrypted administrative and medical data; Akira
  listed the operator on its leak site on 2026-05-08. Groupe 3R, which attributes the attack to Akira and
  refused to pay, confirmed that administrative data including employee personal information was stolen
  and internal documents published, and says it cannot establish whether patient medical data was also taken.
discovered_at: "2026-05-10T05:00:00Z"
updated_at: "2026-07-09T12:25:00Z"
event_date: 2026-04-30
run_id: 2026-05-10-001
priority: high
immediate_action: null
tags:
  - ransomware
  - organized-crime
  - data-breach
regions:
  - switzerland
sectors:
  - healthcare
entities:
  - "incident:groupe-3r-akira-2026"
  - "actor:akira"
techniques: [T1486]
affected_products: []
cves: []
sources:
  - url: "https://www.groupe3r.ch/fr/information-importante-perturbation-de-nos-services-7268/"
    publisher: "Groupe 3R statement"
    date: "2026-09-22"
    role: primary
  - url: "https://www.ictjournal.ch/news/2026-05-06/le-reseau-radiologique-romand-a-nouveau-victime-dune-cyberattaque-ses-systemes"
    publisher: "ICTjournal.ch"
    date: "2026-05-06"
    role: corroborating
  - url: "https://www.blick.ch/fr/suisse/romande/cyberattaque-le-groupe-romand-3r-de-radiologie-cible-id21930477.html"
    publisher: "Blick.ch"
    date: "2026-05-07"
    role: corroborating
  - url: "https://www.swisscybersecurity.net/news/2026-05-07/cyberangriff-legt-westschweizer-radiologie-netzwerk-erneut-lahm"
    publisher: SwissCybersecurity.net
    date: 2026-05-07
    role: corroborating
  - url: "https://www.ictjournal.ch/news/2026-07-06/donnees-volees-systemes-retablis-le-groupe-3r-fait-le-point-apres-la-cyberattaque"
    publisher: ICTjournal.ch
    date: 2026-07-06
    role: corroborating
  - url: "https://ransomware.live/id/UsOpc2VhdSBSYWRpb2xvZ2lxdWUgUm9tYW5kQGFraXJh"
    publisher: "ransomware.live"
    date: "2026-05-08"
    role: corroborating
  - url: "https://www.dexpose.io/?p=32553"
    publisher: "DeXpose"
    date: "2026-05-09"
    role: corroborating
  - url: "https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a"
    publisher: "CISA (AA24-109A, revised 2025-11-13)"
    date: "2025-11-13"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Administrative data of the company was encrypted and stolen, including personal information of current and former employees. (translated from French)"
    original: "Des données administratives de l’entreprise ont été cryptées et volées, incluant des informations personnelles de collaborateurs actuels et anciens."
    publisher: "Groupe 3R statement"
    source_url: "https://www.groupe3r.ch/fr/information-importante-perturbation-de-nos-services-7268/"
  - quote: "However, it is not possible to say with certainty whether this patient medical data was also stolen. (translated from French)"
    original: "Il n’est par contre pas possible d’indiquer avec certitude si ces données médicales de patients ont aussi été volées."
    publisher: "Groupe 3R statement"
    source_url: "https://www.groupe3r.ch/fr/information-importante-perturbation-de-nos-services-7268/"
  - quote: "the attack is attributed to the Akira gang, whose methods match the elements observed by its specialist cybersecurity partners (translated from French)"
    original: "l'attaque est attribuée au gang Akira, dont les méthodes correspondent aux éléments observés par ses partenaires spécialisés en cybersécurité"
    publisher: "ICTjournal.ch"
    source_url: "https://www.ictjournal.ch/news/2026-07-06/donnees-volees-systemes-retablis-le-groupe-3r-fait-le-point-apres-la-cyberattaque"
  - quote: "At the time, the attackers stole medical and administrative data, but without disrupting operations. (translated from German)"
    original: "Damals stahlen die Angreifer medizinische und administrative Daten, ohne jedoch den Betrieb zu stören."
    publisher: SwissCybersecurity.net
    source_url: "https://www.swisscybersecurity.net/news/2026-05-07/cyberangriff-legt-westschweizer-radiologie-netzwerk-erneut-lahm"
  - quote: "We will upload 48gb of corporate data soon."
    publisher: "DeXpose"
    source_url: "https://www.dexpose.io/?p=32553"
  - quote: "obtaining initial access to organizations through a virtual private network (VPN) service"
    publisher: "CISA (AA24-109A, revised 2025-11-13)"
    source_url: "https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a"
verification: multi-source
sourcing_note: >
  Groupe 3R's own statements carry the attack, the data stolen and its attribution to Akira; ICTjournal, SwissCybersecurity.net
  and Blick relay them. Akira's leak-site claim, recorded by ransomware.live and DeXpose, agrees on the attribution but is the
  criminal group's own assertion. No source states how the attackers got in.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
updates:
  - at: "2026-07-09T12:25:00Z"
    run_id: 2026-07-09T1211Z-intel
    type: update
    summary: >
      Groupe 3R (Réseau Radiologique Romand), a 20-site medical-imaging network across seven Romandie
      cantons, has now confirmed through its own forensic investigation that the 2026-04-30 ransomware
      attack was carried out by Akira and that stolen corporate/administrative documents have since
      been published on the darknet — closing the attribution gap left when Akira first listed the
      victim on 2026-05-08. The operator refused to pay, rebuilt all 20 sites, and acknowledged it may
      never establish with certainty whether medical data was exfiltrated.
    fields:
      - actions
      - sources
      - body
    merged_from: 2026-07-09/groupe-3r-akira-forensic-confirmation-darknet-publication
  - at: "2026-10-21T20:31:42Z"
    run_id: 2026-10-21T1148Z-audit
    type: correction
    summary: >
      Groupe 3R confirmed that administrative data including employee personal information was stolen and
      internal documents published, so exfiltration is no longer only Akira's claim; whether patient
      medical data was taken cannot be established. Its 20 centres span seven cantons including Zurich,
      the 2025 attack stole data without disrupting operations, and Groupe 3R attributes the 2026 attack
      to Akira on the basis of methods its partners observed rather than a forensic finding. No source
      states the access vector, so the edge-device playbook and the generic actions give way to the
      operator's fraud warning.
    fields: [actions, body, classification, event_date, evidence, headline, sources, sourcing_note, summary, techniques, title]
migrated_from: briefs/2026-05-10.md
---

Groupe 3R (Réseau Radiologique Romand), which runs 20 medical-imaging centres in seven Swiss cantons ([ICTjournal.ch, 2026-05-06](https://www.ictjournal.ch/news/2026-05-06/le-reseau-radiologique-romand-a-nouveau-victime-dune-cyberattaque-ses-systemes)), lists its centres in Vaud, Valais, Fribourg, Geneva, Neuchâtel, Berne and Zurich ([Groupe 3R](https://www.groupe3r.ch/fr/information-importante-perturbation-de-nos-services-7268/)). It was hit on Thursday 2026-04-30 by a ransomware attack with data encryption; patient care was affected above all on 1 and 2 May, all centres stayed open, the attack was reported to the Federal Office for Cybersecurity, a criminal complaint was filed and no ransom will be paid ([Groupe 3R](https://www.groupe3r.ch/fr/information-importante-perturbation-de-nos-services-7268/)). Akira listed the operator on its leak site, where ransomware.live recorded it on 2026-05-08 with an estimated attack date of 2026-04-30 ([ransomware.live, 2026-05-08](https://ransomware.live/id/UsOpc2VhdSBSYWRpb2xvZ2lxdWUgUm9tYW5kQGFraXJh)), announcing it would upload 48 GB of corporate data including employee identity documents, patient information, payment details and NDAs ([DeXpose, 2026-05-09](https://www.dexpose.io/?p=32553)).

Groupe 3R now states that administrative data, including personal information of current and former employees, was encrypted and stolen, that medical data (exam results) was encrypted and made unusable, and that it is not possible to say with certainty whether patient medical data was also stolen ([Groupe 3R](https://www.groupe3r.ch/fr/information-importante-perturbation-de-nos-services-7268/)). It acknowledged that internal documents stolen in the attack were published on the darknet, and attributes the attack to Akira because the gang's methods match what its specialist cybersecurity partners observed ([ICTjournal.ch, 2026-07-06](https://www.ictjournal.ch/news/2026-07-06/donnees-volees-systemes-retablis-le-groupe-3r-fait-le-point-apres-la-cyberattaque)). This is its second attack in about a year: in April 2025 attackers stole medical and administrative data without disrupting operations ([SwissCybersecurity.net, 2026-05-07](https://www.swisscybersecurity.net/news/2026-05-07/cyberangriff-legt-westschweizer-radiologie-netzwerk-erneut-lahm)), and Groupe 3R says the two attacks have different perpetrators and methods ([Groupe 3R](https://www.groupe3r.ch/fr/information-importante-perturbation-de-nos-services-7268/)). Since 2026-06-26 all centres run on a rebuilt IT infrastructure with RIS, PACS, telephony and teleradiology restored, although some past examination data was still inaccessible in the operator's update of 2026-09-22 ([Groupe 3R](https://www.groupe3r.ch/fr/information-importante-perturbation-de-nos-services-7268/)). No source states how the attackers got in; CISA's Akira advisory describes initial access mostly through VPN services using known CVEs, and encryption that is full or partial depending on file type and size ([CISA AA24-109A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a)).

**Exposure:** current and former Groupe 3R employees, whose personal information was stolen, and patients of its centres, whose medical data was encrypted and may or may not have been taken ([Groupe 3R](https://www.groupe3r.ch/fr/information-importante-perturbation-de-nos-services-7268/)).

**Defender takeaway:** Groupe 3R expects stolen data to be used for fraud such as fake supplementary invoices by email or post, and asks patients to check any invoice with it; patients insured under the LAMal system normally receive only a copy of the invoice sent to their insurer ([Groupe 3R](https://www.groupe3r.ch/fr/information-importante-perturbation-de-nos-services-7268/)). With no access vector public, the case changes no patching or detection decision for other healthcare operators.

## Update — 2026-07-09T12:25:00Z

Groupe 3R (Réseau Radiologique Romand), the network of 20 medical-imaging centres in seven Swiss cantons, attributes the 30 April 2026 ransomware attack to Akira, saying the gang's methods match what its specialist cybersecurity partners observed, and has acknowledged that internal documents stolen in the attack were published on the darknet ([SwissCybersecurity.net, 2026-07-07](https://www.swisscybersecurity.net/news/2026-05-07/cyberangriff-legt-westschweizer-radiologie-netzwerk-erneut-lahm); [ICTjournal.ch, 2026-07-06](https://www.ictjournal.ch/news/2026-07-06/donnees-volees-systemes-retablis-le-groupe-3r-fait-le-point-apres-la-cyberattaque)). The operator confirms that company administrative data was stolen and that medical data was encrypted and temporarily unusable; no publication of medical data has been observed so far, but whether it was also exfiltrated may never be established with certainty ([ICTjournal.ch, 2026-07-06](https://www.ictjournal.ch/news/2026-07-06/donnees-volees-systemes-retablis-le-groupe-3r-fait-le-point-apres-la-cyberattaque)).

Groupe 3R refused to pay the ransom, filed a criminal complaint with the Valais cantonal police on 30 April, forwarded to the Office of the Attorney General of Switzerland on 12 May, and reported the attack to the Federal Office for Cybersecurity ([ICTjournal.ch, 2026-07-06](https://www.ictjournal.ch/news/2026-07-06/donnees-volees-systemes-retablis-le-groupe-3r-fait-le-point-apres-la-cyberattaque)). As of 2026-07-06 all 20 centres run on a fully rebuilt infrastructure secured with ISO 27001-certified cybersecurity partners, with RIS, PACS, telephony and teleradiology restored, while the portal for referring physicians was still in security testing ([ICTjournal.ch, 2026-07-06](https://www.ictjournal.ch/news/2026-07-06/donnees-volees-systemes-retablis-le-groupe-3r-fait-le-point-apres-la-cyberattaque)).

## Correction — 2026-10-21T20:31:42Z

Exfiltration is confirmed by the operator, not only claimed by Akira: administrative data including personal information of current and former employees was encrypted and stolen, while whether patient medical data was also stolen cannot be said with certainty ([Groupe 3R](https://www.groupe3r.ch/fr/information-importante-perturbation-de-nos-services-7268/)), and internal documents were published on the darknet ([ICTjournal.ch, 2026-07-06](https://www.ictjournal.ch/news/2026-07-06/donnees-volees-systemes-retablis-le-groupe-3r-fait-le-point-apres-la-cyberattaque)). The attribution to Akira rests on methods matching what Groupe 3R's specialist partners observed ([ICTjournal.ch, 2026-07-06](https://www.ictjournal.ch/news/2026-07-06/donnees-volees-systemes-retablis-le-groupe-3r-fait-le-point-apres-la-cyberattaque)), and Akira's leak-site listing was recorded on 2026-05-08 ([ransomware.live, 2026-05-08](https://ransomware.live/id/UsOpc2VhdSBSYWRpb2xvZ2lxdWUgUm9tYW5kQGFraXJh)). The seventh canton is Zurich ([Groupe 3R](https://www.groupe3r.ch/fr/information-importante-perturbation-de-nos-services-7268/)). The April 2025 attack stole medical and administrative data without disrupting operations, so 2026 is the first outage rather than the second ([SwissCybersecurity.net, 2026-05-07](https://www.swisscybersecurity.net/news/2026-05-07/cyberangriff-legt-westschweizer-radiologie-netzwerk-erneut-lahm)). No source states how the attackers got in; CISA describes Akira's usual access as VPN services exploited mostly through known CVEs ([CISA AA24-109A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a)), and the operator's concrete advice is to verify any invoice that appears to come from it ([Groupe 3R](https://www.groupe3r.ch/fr/information-importante-perturbation-de-nos-services-7268/)).
