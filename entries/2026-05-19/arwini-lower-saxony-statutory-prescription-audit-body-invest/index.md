---
schema: 1
kind: incident
title: "ARWINI, Lower Saxony's prescription audit body: police confirm a data outflow and name the Kairos group, which lists 2.87 TB for sale"
headline: "Lower Saxony prescription auditor ARWINI: police confirm data theft by Kairos, which lists 2.87 TB for sale"
summary: "The Hannover police directorate confirmed that data left the systems of ARWINI, the body that audits prescriptions for Lower Saxony's statutory health insurers and the regional doctors' association (KVN), and told heise online on 2026-05-18 that the Kairos ransomware group is behind the attack discovered on 2026-05-04. ARWINI says personal and particularly sensitive data are likely affected, up to 75,000 records in the worst case, while the KVN says the patient data it supplies are anonymised; Kairos has listed a 2.87 TB dataset for sale since 2026-05-11, and no source states how the attackers got in."
discovered_at: "2026-05-19T05:00:00Z"
event_date: 2026-05-18
run_id: 2026-05-19-2505c918
priority: routine
immediate_action: null
tags:
  - ransomware
  - data-breach
regions:
  - dach
sectors:
  - healthcare
  - public-sector
entities:
  - "incident:arwini-lower-saxony-statutory-prescription-audit-body-data"
  - "actor:kairos-extortion"
techniques: [T1657]
affected_products: []
cves: []
sources:
  - url: "https://www.aerzteblatt.de/news/hackerangriff-auf-rezeptprufer-c259a70c-595b-4770-9d84-87f6c8338c0c"
    publisher: "Deutsches Ärzteblatt"
    date: "2026-05-18"
    role: primary
  - url: "https://www.heise.de/news/Niedersachsen-Datenabfluss-bei-Wirtschaftsprueferverein-im-Gesundheitswesen-11297772.html"
    publisher: Heise
    date: "2026-05-18"
    role: corroborating
  - url: "https://borncity.com/blog/2026/05/16/cyberangriff-auf-die-arwini-rezeptpruefung-in-niedersachsen-mit-datenabfluss/"
    publisher: Borns IT Blog
    date: "2026-05-16"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The ransomware group \"Kairos\" is behind the attack, as the police confirmed to heise online."
    original: "Hinter der Attacke steckt die Ransomware-Gruppe „Kairos“, wie die Polizei heise online bestätigte."
    publisher: Heise
    source_url: "https://www.heise.de/news/Niedersachsen-Datenabfluss-bei-Wirtschaftsprueferverein-im-Gesundheitswesen-11297772.html"
  - quote: "Arwini had stated that in the worst case up to 75,000 records could be affected."
    original: "Arwini hatte erklärt, dass im schlimmsten Fall bis zu 75.000 Datensätze betroffen sein könnten."
    publisher: Heise
    source_url: "https://www.heise.de/news/Niedersachsen-Datenabfluss-bei-Wirtschaftsprueferverein-im-Gesundheitswesen-11297772.html"
  - quote: "Based on current findings, it is likely that personal and also particularly sensitive data are affected"
    original: "Nach derzeitigen Erkenntnissen ist es wahrscheinlich, dass personenbezogene und auch besonders schützenswerte Daten betroffen sind"
    publisher: ARWINI (quoted by Deutsches Ärzteblatt)
    source_url: "https://www.aerzteblatt.de/news/hackerangriff-auf-rezeptprufer-c259a70c-595b-4770-9d84-87f6c8338c0c"
  - quote: "A notification of a data breach has meanwhile also been received by the Lower Saxony data protection commissioner."
    original: "Inzwischen ist auch eine Meldung über eine Datenschutzverletzung beim Landesbeauftragten für den Datenschutz in Niedersachsen eingegangen."
    publisher: Heise
    source_url: "https://www.heise.de/news/Niedersachsen-Datenabfluss-bei-Wirtschaftsprueferverein-im-Gesundheitswesen-11297772.html"
verification: multi-source
sourcing_note: >
  Heise reports the police's confirmation of the outflow and of Kairos and ARWINI's figure, Deutsches Ärzteblatt quotes ARWINI's statement, and Borns IT
  Blog relays NDR and KVN reporting on the discovery date; the victim's and the KVN's accounts of what data were held conflict, and the 2.87 TB figure is
  the attackers' unverified claim.
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-19.md
updates:
  - at: "2026-10-21T20:34:28Z"
    run_id: 2026-10-21T1148Z-audit
    type: correction
    summary: >
      ARWINI put the worst case at up to 75,000 records and HAZ and NDR estimated more than 70,000;
      neither speaks of 70,000 patient records with health and billing data, and the KVN says the patient
      data it supplies are anonymised. The Lower Saxony data protection commissioner received a breach
      notification and is checking whether it was timely; no source mentions a BSI notification, KRITIS
      obligations or NIS2 status, and the police, not Kairos's claim alone, confirm the data outflow and
      the Kairos attribution.
    fields: [affected_products, body, classification, evidence, headline, priority, regions, sources, sourcing_note, summary, techniques, title]
---

According to the Hannover police directorate, data left the system of the Arbeitsgemeinschaft Wirtschaftlichkeitsprüfung Niedersachsen (ARWINI), which processes health and billing data of statutorily insured people in Lower Saxony and audits the cost-effectiveness of prescriptions on behalf of the statutory health insurers and the Kassenärztliche Vereinigung Niedersachsen (KVN), and the police confirmed to heise online that the Kairos ransomware group is behind the attack ([Heise, 2026-05-18](https://www.heise.de/news/Niedersachsen-Datenabfluss-bei-Wirtschaftsprueferverein-im-Gesundheitswesen-11297772.html)). The attack was discovered on 2026-05-04 and all systems were shut down at once, according to the KVN as relayed by Borns IT Blog ([Borns IT Blog, 2026-05-16](https://borncity.com/blog/2026/05/16/cyberangriff-auf-die-arwini-rezeptpruefung-in-niedersachsen-mit-datenabfluss/)). ARWINI said that "based on current findings, it is likely that personal and also particularly sensitive data are affected" (translated from German), potentially contact and health data and billing information of statutorily insured patients, and that the extent of the outflow was not yet established ([Deutsches Ärzteblatt, 2026-05-18](https://www.aerzteblatt.de/news/hackerangriff-auf-rezeptprufer-c259a70c-595b-4770-9d84-87f6c8338c0c)); it put the worst case at up to 75,000 records, while its external data protection officer told heise online it was still unclear whether and which data had left ([Heise, 2026-05-18](https://www.heise.de/news/Niedersachsen-Datenabfluss-bei-Wirtschaftsprueferverein-im-Gesundheitswesen-11297772.html)). The KVN says the records it sends each quarter are pseudonymised, with patient data anonymised but doctor and practice numbers included ([Heise, 2026-05-18](https://www.heise.de/news/Niedersachsen-Datenabfluss-bei-Wirtschaftsprueferverein-im-Gesundheitswesen-11297772.html)), and HAZ and NDR estimated more than 70,000 records ([Deutsches Ärzteblatt, 2026-05-18](https://www.aerzteblatt.de/news/hackerangriff-auf-rezeptprufer-c259a70c-595b-4770-9d84-87f6c8338c0c)).

Kairos has listed a 2.87 TB dataset on its leak site since 2026-05-11 and threatens to sell it, with sample files that include letters from health insurers and doctors; as of 2026-05-18 the data had not been published, and whether the attackers hold that much is unverified ([Heise, 2026-05-18](https://www.heise.de/news/Niedersachsen-Datenabfluss-bei-Wirtschaftsprueferverein-im-Gesundheitswesen-11297772.html)). The Lower Saxony data protection commissioner has received a breach notification and is examining whether it came in time, and the police are in contact with foreign authorities over Kairos, among them Spanish investigators ([Heise, 2026-05-18](https://www.heise.de/news/Niedersachsen-Datenabfluss-bei-Wirtschaftsprueferverein-im-Gesundheitswesen-11297772.html)). The case matters as a statutory health-insurance audit body in the DACH region holding health and billing data; no source states how the attackers got in.

**Exposure:** health insurers, doctors and patients in Lower Saxony whose data ARWINI holds for prescription audits; the KVN says the data it supplies identify doctors and practices ([Heise, 2026-05-18](https://www.heise.de/news/Niedersachsen-Datenabfluss-bei-Wirtschaftsprueferverein-im-Gesundheitswesen-11297772.html)).

**Defender takeaway:** no technical decision follows, since no source names an access vector; for people possibly affected, ARWINI advises particular care with contact attempts and not opening suspicious emails or attachments (translated from German) ([Deutsches Ärzteblatt, 2026-05-18](https://www.aerzteblatt.de/news/hackerangriff-auf-rezeptprufer-c259a70c-595b-4770-9d84-87f6c8338c0c)).

## Correction — 2026-10-21T20:34:28Z

The 70,000 figure is not ARWINI's: ARWINI said personal and particularly sensitive data were likely affected and put the worst case at up to 75,000 records, while HAZ and NDR estimated more than 70,000 ([Deutsches Ärzteblatt, 2026-05-18](https://www.aerzteblatt.de/news/hackerangriff-auf-rezeptprufer-c259a70c-595b-4770-9d84-87f6c8338c0c); [Heise, 2026-05-18](https://www.heise.de/news/Niedersachsen-Datenabfluss-bei-Wirtschaftsprueferverein-im-Gesundheitswesen-11297772.html)). The KVN says the patient data it sends are anonymised, with doctor and practice numbers included, so the scope of patient data remains disputed ([Heise, 2026-05-18](https://www.heise.de/news/Niedersachsen-Datenabfluss-bei-Wirtschaftsprueferverein-im-Gesundheitswesen-11297772.html)). The authorities involved are the Hannover police directorate, which confirmed the outflow and named Kairos, and the Lower Saxony data protection commissioner, which received a breach notification and is examining whether it was made in time ([Heise, 2026-05-18](https://www.heise.de/news/Niedersachsen-Datenabfluss-bei-Wirtschaftsprueferverein-im-Gesundheitswesen-11297772.html)); no source reports a notification to the BSI or classifies ARWINI under KRITIS or NIS2 rules. The discovery date of 2026-05-04 comes from the KVN as relayed by Borns IT Blog ([Borns IT Blog, 2026-05-16](https://borncity.com/blog/2026/05/16/cyberangriff-auf-die-arwini-rezeptpruefung-in-niedersachsen-mit-datenabfluss/)).
