---
schema: 1
kind: incident
title: "Swiss commune Manno (TI) confirms a cyberattack that encrypted part of its servers on 4 August 2026; SafePay is recorded listing the commune on a leak site on 28 September"
headline: "Manno restored from backup within an afternoon; SafePay was recorded listing the commune on 28 September"
summary: >
  The Ticino commune of Manno stated in a signed notice of 2026-09-16 that part of its servers were hit by an
  attack that encrypted data on 4 August 2026; it isolated the server and restored from existing backups.
  On 2026-09-28 the ransomware group SafePay was recorded listing manno.ch on its leak site, with a countdown
  timer pointing to about 1 October. The commune's notice names no actor, no access vector and no data theft.
discovered_at: "2026-09-30T04:41:00Z"
updated_at: null
event_date: "2026-08-04"
run_id: 2026-09-30T0404Z-intel
priority: notable
immediate_action: null
tags: [ransomware]
regions: [switzerland]
sectors: [public-sector]
entities: ["actor:safepay", "incident:manno-ti-commune-ransomware-2026-08"]
techniques: [T1486]
affected_products: []
cves: []
sources:
  - url: "https://www.manno.ch/manno/Informazione/albo-comunale/2026/09/Attacco-informatico.html"
    publisher: "Comune di Manno (Municipio)"
    date: "2026-09-16"
    role: primary
  - url: "https://www.manno.ch/manno/Informazione/albo-comunale/2026/09/Attacco-informatico/sidebar/0/items/0/file/Pubblicazione%20avviso%20attacco%20informatico.pdf.pdf"
    publisher: "Comune di Manno (Municipio), signed notice 'Avviso attacco informatico'"
    date: "2026-09-16"
    role: primary
  - url: "https://www.ransomware.live/id/bWFubm8uY2hAc2FmZXBheQ=="
    publisher: "Ransomware.live (leak-site tracker, claim record)"
    date: "2026-09-28"
    role: corroborating
  - url: "https://www.inside-it.ch/tessiner-gemeinde-wird-opfer-von-cyberkriminellen-20260929"
    publisher: "Inside IT (teaser and lead paragraph from its feed; article body not readable)"
    date: "2026-09-29"
    role: corroborating
closed_sources: []
evidence:
  - quote: "on 4 August 2026 part of the commune's servers suffered an attack (translated from Italian)"
    original: "il 4 agosto 2026 una parte dei server del Comune ha subito un attacco"
    publisher: "Comune di Manno (Municipio)"
    source_url: "https://www.manno.ch/manno/Informazione/albo-comunale/2026/09/Attacco-informatico/sidebar/0/items/0/file/Pubblicazione%20avviso%20attacco%20informatico.pdf.pdf"
  - quote: "which resulted in the encryption of the data (translated from Italian)"
    original: "che ha comportato il criptaggio dei dati"
    publisher: "Comune di Manno (Municipio)"
    source_url: "https://www.manno.ch/manno/Informazione/albo-comunale/2026/09/Attacco-informatico/sidebar/0/items/0/file/Pubblicazione%20avviso%20attacco%20informatico.pdf.pdf"
  - quote: "subsequently a complaint was lodged against (translated from Italian)"
    original: "in seguito è stata sporta denuncia contro"
    publisher: "Comune di Manno (Municipio)"
    source_url: "https://www.manno.ch/manno/Informazione/albo-comunale/2026/09/Attacco-informatico/sidebar/0/items/0/file/Pubblicazione%20avviso%20attacco%20informatico.pdf.pdf"
  - quote: "the population is urged to pay attention to unexpected communications (translated from Italian)"
    original: "Si invita la popolazione a prestare attenzione a comunicazioni inattese"
    publisher: "Comune di Manno (Municipio)"
    source_url: "https://www.manno.ch/manno/Informazione/albo-comunale/2026/09/Attacco-informatico/sidebar/0/items/0/file/Pubblicazione%20avviso%20attacco%20informatico.pdf.pdf"
  - quote: "Ransomware.live discovered on 2026-09-28 that manno.ch has been claimed by Safepay ransomware group"
    publisher: "Ransomware.live"
    source_url: "https://www.ransomware.live/id/bWFubm8uY2hAc2FmZXBheQ=="
  - quote: "A ransomware gang attacked servers of the Manno municipal administration and encrypted part of the data (translated from German)"
    original: "Eine Ransomware-Bande hat Server der Gemeindeverwaltung Manno angegriffen und einen Teil der Daten verschlüsselt."
    publisher: "Inside IT"
    source_url: "https://www.inside-it.ch/tessiner-gemeinde-wird-opfer-von-cyberkriminellen-20260929"
verification: single-source-victim
sourcing_note: >
  The incident facts come from the commune's own signed notice about its own event. SafePay's role rests
  only on a leak-site tracker's record of the group's listing; the notice names no actor. Inside IT's
  article body is not readable, so only its teaser is cited, and a reported stolen-data claim could not
  be corroborated and is left out. The countdown is read from the tracker's screenshot, not from text. The restoration
  sentence of the PDF notice is stored with a shifted font encoding, and its plain reading is that data and
  operations were restored from existing backups during the afternoon.
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

The Ticino commune of Manno stated in a signed notice dated 2026-09-16 that on 4 August 2026 part of its servers suffered an attack that encrypted data ([Comune di Manno, 2026-09-16](https://www.manno.ch/manno/Informazione/albo-comunale/2026/09/Attacco-informatico/sidebar/0/items/0/file/Pubblicazione%20avviso%20attacco%20informatico.pdf.pdf)). The commune isolated the affected server immediately and, per the notice, restored data and operations from existing backups in the course of the afternoon ([Comune di Manno, 2026-09-16](https://www.manno.ch/manno/Informazione/albo-comunale/2026/09/Attacco-informatico/sidebar/0/items/0/file/Pubblicazione%20avviso%20attacco%20informatico.pdf.pdf)). It reported the case to the competent authorities, filed a criminal complaint against persons unknown, and told residents to distrust unexpected letters or e-mails that demand urgent payments or personal or financial data and to verify through official channels ([Comune di Manno, 2026-09-16](https://www.manno.ch/manno/Informazione/albo-comunale/2026/09/Attacco-informatico/sidebar/0/items/0/file/Pubblicazione%20avviso%20attacco%20informatico.pdf.pdf)). The notice names no actor, no intrusion vector, and does not say whether data left the network. Inside IT's teaser of 2026-09-29 calls it a ransomware attack and says a backup allowed a quick return to normal operation ([Inside IT, 2026-09-29](https://www.inside-it.ch/tessiner-gemeinde-wird-opfer-von-cyberkriminellen-20260929)). The tracker's leak-post screenshot shows a countdown timer of about three days eleven hours when it was captured on 2026-09-28, which points to expiry around 1 October; the post describes no dataset ([Ransomware.live, 2026-09-28](https://www.ransomware.live/id/bWFubm8uY2hAc2FmZXBheQ==)).

On 2026-09-28, 55 days after the encryption, Ransomware.live recorded that the ransomware group SafePay had listed manno.ch on its leak site ([Ransomware.live, 2026-09-28](https://www.ransomware.live/id/bWFubm8uY2hAc2FmZXBheQ==)). That is the group's claim as recorded by a tracker: the commune has not confirmed it, and the record shows neither what data the listing claims nor that it concerns the 4 August event.

**Defender takeaway:** existing backups and immediate isolation turned an encryption event into a recovery within an afternoon, per the notice, but a leak-site listing, which the commune has not confirmed, appeared 55 days later with a countdown timer pointing to about 1 October, so a communal response to an encryption attack should not close its data-theft assessment on the strength of a clean restore. The resident-fraud warning the commune issued belongs in the same response plan.
