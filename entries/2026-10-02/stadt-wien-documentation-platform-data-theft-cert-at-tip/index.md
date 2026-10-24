---
schema: 1
kind: incident
title: "Stadt Wien discloses 26,000 documents copied from an internal documentation platform; Austria's CERT.at reported a forum offer to buy a vulnerability in a city system"
headline: "Vienna says a CERT.at tip about a forum bid for a vulnerability led to its probe of 26,000 copied documents"
summary: >
  Stadt Wien says an attacker had web access to parts of an internal documentation platform of the city administration
  between 2026-09-03 and 2026-09-11 and copied about 26,000 documents and pages (roughly nine gigabytes) holding test
  data, training material and project documentation, including personal data. The investigation started on
  2026-09-09 when CERT.at reported an offer in an online forum to buy a vulnerability in a technical system of the city.
discovered_at: "2026-10-02T04:47:00Z"
updated_at: null
event_date: "2026-09-30"
run_id: 2026-10-02T0404Z-intel
priority: notable
immediate_action: null
tags: [data-breach]
regions: [europe, dach]
sectors: [public-sector]
entities: []
techniques: [T1190, T1213]
affected_products: []
cves: []
sources:
  - url: "https://www.ots.at/presseaussendung/OTS_20260930_OTS0034/wien-datensicherheit-hat-hohen-stellenwert-sicherheitsluecke-umgehend-geschlossen"
    publisher: "Stadt Wien Kommunikation und Medien (APA-OTS)"
    date: "2026-09-30"
    role: primary
closed_sources: []
evidence:
  - quote: "The trigger for the current investigation was a tip from the Austrian Computer Emergency Response Team (CERT.at) on 9 September 2026 about an offer in an online forum to buy a vulnerability in a technical system of the City of Vienna. (translated from German)"
    original: "Auslöser der aktuellen Untersuchung war ein Hinweis des österreichischen Computer Emergency Response Teams (CERT.at) am 9. September 2026 auf ein Angebot in einem Onlineforum zum Kauf einer Schwachstelle in einem technischen System der Stadt Wien."
    publisher: "Stadt Wien Kommunikation und Medien (APA-OTS)"
    source_url: "https://www.ots.at/presseaussendung/OTS_20260930_OTS0034/wien-datensicherheit-hat-hohen-stellenwert-sicherheitsluecke-umgehend-geschlossen"
  - quote: "an attacker had access to parts of an internal documentation platform of the Magistrat via web access between 3 September and 11 September 2026 (translated from German)"
    original: "ein Angreifer zwischen 3. September und 11. September 2026 über einen Webzugang auf Teile einer internen Dokumentationsplattform des Magistrats Zugriff hatte"
    publisher: "Stadt Wien Kommunikation und Medien (APA-OTS)"
    source_url: "https://www.ots.at/presseaussendung/OTS_20260930_OTS0034/wien-datensicherheit-hat-hohen-stellenwert-sicherheitsluecke-umgehend-geschlossen"
verification: single-source-victim
sourcing_note: >
  Every fact comes from the city's own press release; the vulnerability, the platform product and the actor are not
  named, and the statements that the attacker never controlled IT systems or user accounts and that no publication is
  known are the city's assertions.
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
updates: []
migrated_from: null
---

Stadt Wien's own press release of 2026-09-30 says an attacker had web access to parts of an internal documentation platform of the city administration between 2026-09-03 and 2026-09-11 and copied internal content, in particular test data, training material and project documentation ([Stadt Wien, 2026-09-30](https://www.ots.at/presseaussendung/OTS_20260930_OTS0034/wien-datensicherheit-hat-hohen-stellenwert-sicherheitsluecke-umgehend-geschlossen)). The copied set is about 26,000 documents and pages, roughly nine gigabytes, and includes personal data, which may in places be special categories under the GDPR, plus business and infrastructure information ([Stadt Wien, 2026-09-30](https://www.ots.at/presseaussendung/OTS_20260930_OTS0034/wien-datensicherheit-hat-hohen-stellenwert-sicherheitsluecke-umgehend-geschlossen)). The investigation started when CERT.at flagged on 2026-09-09 an offer in an online forum to buy a vulnerability in a technical system of the city; the city's WienCERT and its IT department then analysed the system and, with the Directorate for State Protection and Intelligence, identified and closed the flaw ([Stadt Wien, 2026-09-30](https://www.ots.at/presseaussendung/OTS_20260930_OTS0034/wien-datensicherheit-hat-hohen-stellenwert-sicherheitsluecke-umgehend-geschlossen)). The city filed a voluntary incident report under the Austrian NIS Act on 2026-09-10 and the statutory data-protection report on 2026-09-15, and will notify 2,885 citizens, 2,083 employees and 856 contractors within a week; its CIO says the attacker never controlled IT systems or user accounts and that no indication of publication exists ([Stadt Wien, 2026-09-30](https://www.ots.at/presseaussendung/OTS_20260930_OTS0034/wien-datensicherheit-hat-hohen-stellenwert-sicherheitsluecke-umgehend-geschlossen)). The release names no product, no flaw and no actor, and public disclosure came 19 days after the access window ended.

**Exposure:** any internal documentation, wiki or project platform of an administration that is reachable through a web access path; the city says the copied content included technical documentation, personal data and business and infrastructure information, so what the platform stores matters as much as its patch state.

**Detection:** web access logs of the platform for one client reading content in bulk over several days (here an access window of 3 to 11 September and about nine gigabytes), and external monitoring for offers that name your systems, which is how this intrusion surfaced: the city names the CERT tip as the trigger of its investigation.

**Defender takeaway:** review what internal documentation platforms hold (test data and training material can carry personal data) and who can reach them over the web, and confirm the national CERT or BACS has current contact data for your organization so a tip about a forum sale reaches the right team the same day.
