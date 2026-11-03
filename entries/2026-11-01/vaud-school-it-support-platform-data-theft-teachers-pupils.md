---
schema: 1
kind: incident
title: "Canton Vaud: unauthorised access to the IT-support platform of its Gymnases and professional schools copied the names, school e-mail addresses and support requests of about 3,500 teachers and 38,000 pupils, and RTS reports a pupil is suspected"
headline: "Canton Vaud: school IT-support platform breached; data of about 3,500 teachers and 38,000 pupils copied"
summary: >
  The canton of Vaud said on 2026-10-31 that its education directorate detected on 2026-10-26 unauthorised access to the IT-support platform
  of the canton's Gymnases and professional schools, which copied the names and school e-mail addresses of about 3,500 teachers and 38,000
  pupils and the content of support requests; passwords are not stored on the platform and no grades or pupil files are affected. The canton
  names targeted fraudulent messages that pose as the school or IT support as the main risk; RTS reports that a pupil is suspected, which
  the police have not confirmed, and the education directorate's deputy director says much points to an internal matter. No source gives
  the access method or the platform product.
discovered_at: "2026-11-01T03:35:00Z"
updated_at: null
event_date: "2026-10-26"
run_id: 2026-11-01T0256Z-intel
priority: routine
immediate_action: null
tags: [data-breach, phishing]
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
verification: single-source-victim
sourcing_note: >
  The canton's press release is the victim's own statement and the only first-hand source. RTS repeats it and adds, on the strength of the
  canton's latest information and without a further named source, that a pupil is suspected; Inside IT, relaying Keystone-SDA, reports that the
  police did not confirm that report and that the education directorate's deputy director says much points to an internal matter, so the pupil
  claim rests on media reports, RTS among them, and "internal" is the directorate's own wording. The canton gives no access method, actor or platform product.
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
migrated_from: null
---

The Swiss canton of Vaud says unauthorised access, detected on 2026-10-26, to the IT-support platform of its Gymnases and professional schools copied the names, school e-mail addresses and support requests of about 3,500 teachers and 38,000 pupils; passwords are not stored on the platform and no grades or pupil files are affected ([Etat de Vaud, 2026-10-31](https://www.vd.ch/actualites/communiques-de-presse-de-letat-de-vaud/detail/communique/la-plateforme-de-support-informatique-des-gymnases-et-des-ecoles-professionnelles-du-canton-victime-dun-vol-de-donnees)). The canton names targeted fraudulent messages that pose as the school or IT support as the main risk, and RTS reports, from the canton's latest information, that everything points to a pupil, with no context, reason or objective known ([Etat de Vaud, 2026-10-31](https://www.vd.ch/actualites/communiques-de-presse-de-letat-de-vaud/detail/communique/la-plateforme-de-support-informatique-des-gymnases-et-des-ecoles-professionnelles-du-canton-victime-dun-vol-de-donnees); [RTS, 2026-10-31](https://www.rts.ch/info/regions/vaud/2026/article/vaud-les-donnees-de-plus-de-40-000-eleves-et-profs-volees-29401382.html), translated from French); the canton gives no access method, actor or platform product. Vaud police, contacted by Keystone-SDA, did not confirm the media report that a pupil is suspected ([Inside IT, 2026-11-02](https://www.inside-it.ch/cyberangriff-auf-waadtlaender-schulen-20261102)).

**Defender takeaway:** the sources give no access method, so there is no patch or configuration change to prescribe; school and cantonal IT teams should brief users to expect impersonation of IT support and to report urgent or unusual messages, as the canton advises ([Etat de Vaud, 2026-10-31](https://www.vd.ch/actualites/communiques-de-presse-de-letat-de-vaud/detail/communique/la-plateforme-de-support-informatique-des-gymnases-et-des-ecoles-professionnelles-du-canton-victime-dun-vol-de-donnees)).

## Improvement — 2026-11-03T03:46:23Z

The education directorate's deputy director said that at present much points to an internal matter, with the case and several indications passed to the police (translated from German) ([Inside IT, 2026-11-02](https://www.inside-it.ch/cyberangriff-auf-waadtlaender-schulen-20261102)).
