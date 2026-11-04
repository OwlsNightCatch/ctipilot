---
schema: 1
kind: incident
title: "Canton Vaud: unauthorised access to the IT-support platform of its Gymnases and professional schools copied the names, school e-mail addresses and support requests of about 3,500 teachers and 38,000 pupils; police arrested a 16-year-old pupil of the schools on 2026-10-31"
headline: "Canton Vaud: school IT-support platform breached, data of about 3,500 teachers and 38,000 pupils copied; pupil arrested"
summary: >
  The canton of Vaud said on 2026-10-31 that its education directorate detected on 2026-10-26 unauthorised access to the IT-support platform
  of the canton's Gymnases and professional schools, which copied the names and school e-mail addresses of about 3,500 teachers and 38,000
  pupils and the content of support requests; passwords are not stored on the platform and no grades or pupil files are affected. The canton
  names targeted fraudulent messages that pose as the school or IT support as the main risk. Vaud police announced on 2026-11-03 the arrest, on
  2026-10-31, of a 16-year-old pupil of the schools, suspected of the intrusion between 23 and 26 October; the juvenile court is investigating how it happened
  and whether data were downloaded or passed to third parties, and no source gives the access method or the platform product.
discovered_at: "2026-11-01T03:35:00Z"
updated_at: "2026-11-04T03:27:46Z"
event_date: "2026-10-26"
run_id: 2026-11-01T0256Z-intel
priority: routine
immediate_action: null
tags: [data-breach, phishing, law-enforcement]
regions: [switzerland]
sectors: [public-sector, education]
entities: ["incident:vaud-dgep-it-support-platform-data-theft-2026-10"]
techniques: [T1213]
affected_products: []
cves: []
sources:
  - url: "https://www.vd.ch/actualites/communiques-de-presse-de-letat-de-vaud/detail/communique/la-plateforme-de-support-informatique-des-gymnases-et-des-ecoles-professionnelles-du-canton-victime-dun-vol-de-donnees"
    publisher: "Etat de Vaud (press release of the Bureau d'information et de communication)"
    date: "2026-10-31"
    role: primary
  - url: "https://www.rts.ch/info/regions/vaud/2026/article/vaud-les-donnees-de-plus-de-40-000-eleves-et-profs-volees-29401382.html"
    publisher: "RTS"
    date: "2026-10-31"
    role: corroborating
  - url: "https://www.inside-it.ch/cyberangriff-auf-waadtlaender-schulen-20261102"
    publisher: "Inside IT (relaying Keystone-SDA)"
    date: "2026-11-02"
    role: corroborating
  - url: "https://www.letemps.ch/suisse/vaud/cyberattaque-contre-les-ecoles-vaudoises-un-adolescent-de-16-ans-a-ete-interpelle"
    publisher: "Le Temps (ATS, relaying the Vaud cantonal police communiqué)"
    date: "2026-11-03"
    role: corroborating
  - url: "https://www.inside-it.ch/16-jaehriger-hackte-wohl-waadtlaender-schulen-20261103"
    publisher: "Inside IT (relaying Keystone-SDA)"
    date: "2026-11-03"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The names, first names and school e-mail addresses of about 3,500 teachers and 38,000 pupils were copied, as was the content of support requests. (translated from French)"
    original: "Les noms, prénoms et adresses électroniques scolaires d’environ 3500 enseignants et 38'000 élèves ont été copiés, ainsi que le contenu de demandes d’assistance."
    publisher: "Etat de Vaud"
    source_url: "https://www.vd.ch/actualites/communiques-de-presse-de-letat-de-vaud/detail/communique/la-plateforme-de-support-informatique-des-gymnases-et-des-ecoles-professionnelles-du-canton-victime-dun-vol-de-donnees"
  - quote: "The main risk for the people concerned is the receipt of targeted fraudulent messages posing as the school or IT support. (translated from French)"
    original: "Le principal risque pour les personnes concernées est la réception de messages frauduleux ciblés, se faisant passer pour l’école ou le support informatique."
    publisher: "Etat de Vaud"
    source_url: "https://www.vd.ch/actualites/communiques-de-presse-de-letat-de-vaud/detail/communique/la-plateforme-de-support-informatique-des-gymnases-et-des-ecoles-professionnelles-du-canton-victime-dun-vol-de-donnees"
  - quote: "According to the latest information given by the State of Vaud, everything points to the theft having been committed by a pupil. (translated from French)"
    original: "Selon les dernières informations données par l'Etat de Vaud, tout porte cependant à croire que le vol a été commis par un élève."
    publisher: "RTS"
    source_url: "https://www.rts.ch/info/regions/vaud/2026/article/vaud-les-donnees-de-plus-de-40-000-eleves-et-profs-volees-29401382.html"
  - quote: "The Vaud police, contacted by Keystone-SDA, did not confirm this information but promised a statement in the coming days. (translated from German)"
    original: "Die von 'Keystone-SDA' kontaktierte Waadtländer Polizei hat diese Information nicht bestätigt, versprach jedoch eine Stellungnahme in den kommenden Tagen."
    publisher: "Inside IT (relaying Keystone-SDA)"
    source_url: "https://www.inside-it.ch/cyberangriff-auf-waadtlaender-schulen-20261102"
  - quote: "At present much points to this being an internal matter (translated from German)"
    original: "Zum jetzigen Zeitpunkt deute vieles darauf hin, dass es sich um eine interne Angelegenheit handle"
    publisher: "Inside IT (relaying Keystone-SDA)"
    source_url: "https://www.inside-it.ch/cyberangriff-auf-waadtlaender-schulen-20261102"
  - quote: "A 16-year-old was arrested in connection with the cyberattack on the IT support of the canton of Vaud's gymnases and vocational schools, the cantonal police announced on Tuesday. (translated from French)"
    original: "Un adolescent de 16 ans a été interpellé dans le cadre de la cyberattaque contre le support informatique des gymnases et écoles professionnelles du canton de Vaud, a annoncé ce mardi la police cantonale."
    publisher: "Le Temps (ATS, relaying the Vaud cantonal police communiqué)"
    source_url: "https://www.letemps.ch/suisse/vaud/cyberattaque-contre-les-ecoles-vaudoises-un-adolescent-de-16-ans-a-ete-interpelle"
  - quote: "They aim to establish the circumstances of this intrusion and to determine whether data was downloaded and/or passed to third parties. (translated from French)"
    original: "Elles visent à établir les circonstances de cette intrusion et à déterminer si des données ont été téléchargées et/ou transmises à des tiers."
    publisher: "Le Temps (ATS, relaying the Vaud cantonal police communiqué)"
    source_url: "https://www.letemps.ch/suisse/vaud/cyberattaque-contre-les-ecoles-vaudoises-un-adolescent-de-16-ans-a-ete-interpelle"
verification: multi-source
sourcing_note: >
  The canton's press release is the victim's own statement. The arrest is the cantonal police's own announcement of 2026-11-03, read through the ATS and Keystone-SDA wire reports that Le Temps and Inside IT carry, with the education directorate's own note on the pupil's status in the same reports; the police communiqué itself was not read. A person arrested is a suspect, and the investigation has not said whether data left the suspect's hands. The canton gives no access method, actor or platform product.
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
  - at: "2026-11-03T03:46:23Z"
    run_id: 2026-11-03T0256Z-intel
    type: improvement
    summary: >
      The education directorate's deputy director says that at present much points to an internal matter,
      with the case passed to the police, and the police have not confirmed the media report that a pupil
      is suspected.
    fields: [summary, sources, evidence, sourcing_note, body]
  - at: "2026-11-04T03:27:46Z"
    run_id: 2026-11-04T0256Z-intel
    type: update
    summary: >
      Vaud cantonal police announced on 2026-11-03 the arrest, on 2026-10-31, of a 16-year-old pupil of
      the affected schools, suspected of the intrusion into the IT-support platform between 23 and 26
      October; he was questioned and released, his equipment was seized, and the juvenile court leads an
      investigation into how the intrusion happened and whether data were downloaded or passed to third
      parties.
    fields: [title, headline, summary, tags, sources, evidence, sourcing_note, verification, body]
migrated_from: null
---

The Swiss canton of Vaud says unauthorised access, detected on 2026-10-26, to the IT-support platform of its Gymnases and professional schools copied the names, school e-mail addresses and support requests of about 3,500 teachers and 38,000 pupils; passwords are not stored on the platform and no grades or pupil files are affected ([Etat de Vaud, 2026-10-31](https://www.vd.ch/actualites/communiques-de-presse-de-letat-de-vaud/detail/communique/la-plateforme-de-support-informatique-des-gymnases-et-des-ecoles-professionnelles-du-canton-victime-dun-vol-de-donnees)). The canton names targeted fraudulent messages that pose as the school or IT support as the main risk ([Etat de Vaud, 2026-10-31](https://www.vd.ch/actualites/communiques-de-presse-de-letat-de-vaud/detail/communique/la-plateforme-de-support-informatique-des-gymnases-et-des-ecoles-professionnelles-du-canton-victime-dun-vol-de-donnees)); it gives no access method, actor or platform product. Vaud police announced on 2026-11-03 the arrest, on 2026-10-31, of a 16-year-old pupil of the affected schools, suspected of the intrusion between 23 and 26 October; he was questioned and released, his equipment was seized, and the juvenile court's investigation aims to establish how the intrusion happened and whether data were downloaded or passed to third parties ([Le Temps, 2026-11-03](https://www.letemps.ch/suisse/vaud/cyberattaque-contre-les-ecoles-vaudoises-un-adolescent-de-16-ans-a-ete-interpelle), translated from French; [Inside IT, 2026-11-03](https://www.inside-it.ch/16-jaehriger-hackte-wohl-waadtlaender-schulen-20261103)).

**Defender takeaway:** the sources give no access method, so there is no patch or configuration change to prescribe; school and cantonal IT teams should brief users to expect impersonation of IT support and to report urgent or unusual messages, as the canton advises ([Etat de Vaud, 2026-10-31](https://www.vd.ch/actualites/communiques-de-presse-de-letat-de-vaud/detail/communique/la-plateforme-de-support-informatique-des-gymnases-et-des-ecoles-professionnelles-du-canton-victime-dun-vol-de-donnees)).

## Improvement — 2026-11-03T03:46:23Z

The education directorate's deputy director said that at present much points to an internal matter, with the case and several indications passed to the police (translated from German) ([Inside IT, 2026-11-02](https://www.inside-it.ch/cyberangriff-auf-waadtlaender-schulen-20261102)).

## Update — 2026-11-04T03:27:46Z

Vaud's cantonal police announced on 2026-11-03 that a 16-year-old was arrested on Saturday 2026-10-31, suspected of intruding into the IT-support platform of the canton's post-compulsory schools and extracting data from it between 23 and 26 October 2026 (translated from French) ([Le Temps, 2026-11-03](https://www.letemps.ch/suisse/vaud/cyberattaque-contre-les-ecoles-vaudoises-un-adolescent-de-16-ans-a-ete-interpelle)). The education directorate says the suspect is one of its pupils and faces an administrative sanction, up to exclusion, that runs apart from the criminal case; he was questioned and released, his IT equipment was seized and is being analysed, and the investigation, led by the juvenile court, aims to establish the circumstances of the intrusion and whether data were downloaded or passed to third parties ([Le Temps, 2026-11-03](https://www.letemps.ch/suisse/vaud/cyberattaque-contre-les-ecoles-vaudoises-un-adolescent-de-16-ans-a-ete-interpelle); [Inside IT, 2026-11-03](https://www.inside-it.ch/16-jaehriger-hackte-wohl-waadtlaender-schulen-20261103)). The platform was disconnected from the internet on detection and then secured with the support of the canton's security operations centre, according to the police communiqué; the access method and the platform product are still not stated ([Le Temps, 2026-11-03](https://www.letemps.ch/suisse/vaud/cyberattaque-contre-les-ecoles-vaudoises-un-adolescent-de-16-ans-a-ete-interpelle)).
