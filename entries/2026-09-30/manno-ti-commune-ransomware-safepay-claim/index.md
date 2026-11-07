---
schema: 1
kind: incident
title: "Swiss commune Manno (TI) confirms a cyberattack that encrypted part of its servers on 4 August 2026; SafePay has now published about 30 GB, which Risikomonitor reads as social-assistance decisions with AHV numbers, naturalisation files and a near-complete address book"
headline: "Inside IT: SafePay published about 30 GB from Manno, social-assistance files with AHV numbers; no commune statement"
summary: >
  The Ticino commune of Manno stated in a signed notice of 2026-09-16 that part of its servers were hit by an attack that encrypted data on
  4 August 2026; it isolated the server and restored from existing backups. SafePay, recorded on 2026-09-28 listing manno.ch on its leak
  site, has since put about 30 GB of stolen data into the darknet, and Inside IT reports of 2026-10-27 that the security firm Risikomonitor
  found social-assistance decisions with AHV numbers and health insurers from 2014 to December 2025, debt-enforcement extracts, naturalisation
  files and data on the whole population of 1,381; the commune says it will make no statement.
discovered_at: "2026-09-30T04:41:00Z"
updated_at: "2026-10-28T03:43:10Z"
event_date: "2026-08-04"
run_id: 2026-09-30T0404Z-intel
priority: notable
immediate_action: null
tags: [ransomware, data-breach]
regions: [switzerland]
sectors: [public-sector]
entities: ["actor:safepay", "incident:manno-ti-commune-ransomware-2026-08"]
techniques: [T1486, T1657]
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
    publisher: "Inside IT (article of 2026-09-29)"
    date: "2026-09-29"
    role: corroborating
  - url: "https://www.inside-it.ch/kritische-schweizer-infrastrukturen-attackiert-20261027"
    publisher: "Inside IT (article of 2026-10-27, with Risikomonitor's analysis)"
    date: "2026-10-27"
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
  - quote: "SafePay has put stolen data packages from these two attacks into the darknet, about 30 gigabytes in the case of Manno (translated from German)"
    original: "Safepay hat erbeutete Datenpakete aus diesen beiden Angriffen ins Darknet gestellt – rund 30 Gigabyte im Fall von Manno"
    publisher: "Inside IT"
    source_url: "https://www.inside-it.ch/kritische-schweizer-infrastrukturen-attackiert-20261027"
  - quote: "documents on social-assistance decisions with name, address, monthly amount, AHV numbers and health insurer from 2014 to December 2025 (translated from German)"
    original: "Dokumente zu Sozialhilfeentscheiden mit Name, Adresse, Monatsbetrag, AHV-Nummern und Krankenkasse von 2014 bis Dezember 2025"
    publisher: "Inside IT"
    source_url: "https://www.inside-it.ch/kritische-schweizer-infrastrukturen-attackiert-20261027"
  - quote: "The municipality of Manno will not issue a statement in this matter. (translated from German)"
    original: "Die Gemeinde Manno wird in dieser Angelegenheit keine Stellungnahme abgeben."
    publisher: "Inside IT"
    source_url: "https://www.inside-it.ch/kritische-schweizer-infrastrukturen-attackiert-20261027"
verification: single-source
sourcing_note: >
  The encryption event comes from the commune's own signed notice about its own event. SafePay's role rests on a leak-site tracker's record of
  the group's listing and on Inside IT's report of 2026-10-27, the only source for the publication of the data; the contents come from an
  analysis by the security firm Risikomonitor that Inside IT relays and that has not been verified independently. The commune's notice
  names no actor and does not say whether data left the network. The notice's restoration sentence says that data and operations were restored from existing backups during the afternoon.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 3
watchlist_hit: false
actions: []
updates:
  - at: "2026-10-28T03:43:10Z"
    run_id: 2026-10-28T0256Z-intel
    type: update
    summary: >
      Inside IT reported on 2026-10-27 that SafePay has put about 30 GB of data stolen from Manno into the
      darknet and relays Risikomonitor's analysis of its contents (social-assistance decisions with AHV
      numbers, debt-enforcement and naturalisation files, a near-complete address book); the commune will
      make no statement. This replaces the entry's statement that the listing described no data and could
      not be corroborated.
    fields: [title, headline, summary, tags, techniques, sources, evidence, verification, sourcing_note, classification, body]
migrated_from: null
---

The Ticino commune of Manno stated in a signed notice dated 2026-09-16 that on 4 August 2026 part of its servers suffered an attack that encrypted data ([Comune di Manno, 2026-09-16](https://www.manno.ch/manno/Informazione/albo-comunale/2026/09/Attacco-informatico/sidebar/0/items/0/file/Pubblicazione%20avviso%20attacco%20informatico.pdf.pdf)). The commune isolated the affected server immediately and, per the notice, restored data and operations from existing backups in the course of the afternoon ([Comune di Manno, 2026-09-16](https://www.manno.ch/manno/Informazione/albo-comunale/2026/09/Attacco-informatico/sidebar/0/items/0/file/Pubblicazione%20avviso%20attacco%20informatico.pdf.pdf)). It reported the case to the competent authorities, filed a criminal complaint against persons unknown, and told residents to distrust unexpected letters or e-mails that demand urgent payments or personal or financial data and to verify through official channels ([Comune di Manno, 2026-09-16](https://www.manno.ch/manno/Informazione/albo-comunale/2026/09/Attacco-informatico/sidebar/0/items/0/file/Pubblicazione%20avviso%20attacco%20informatico.pdf.pdf)). The notice names no actor, no intrusion vector, and does not say whether data left the network; Inside IT's article of 2026-09-29 calls it a ransomware attack and says a backup allowed a quick return to normal operation ([Inside IT, 2026-09-29](https://www.inside-it.ch/tessiner-gemeinde-wird-opfer-von-cyberkriminellen-20260929)).

On 2026-09-28, 55 days after the encryption, Ransomware.live recorded that the ransomware group SafePay had listed manno.ch on its leak site ([Ransomware.live, 2026-09-28](https://www.ransomware.live/id/bWFubm8uY2hAc2FmZXBheQ==)). Inside IT reported on 2026-10-27 that SafePay has put the stolen data into the darknet, about 30 GB in the case of Manno, and that the security firm Risikomonitor analysed it ([Inside IT, 2026-10-27](https://www.inside-it.ch/kritische-schweizer-infrastrukturen-attackiert-20261027)). Risikomonitor's reading, relayed by Inside IT and not verified independently: files with about 5,300 e-mail addresses and more than 2,000 identifiable persons; social-assistance decisions with name, address, monthly amount, AHV numbers and health insurer from 2014 to December 2025; debt-enforcement register extracts, naturalisation dossiers from 2018 and payment orders against tax debtors; employees' bank statements with IBANs; and mass letters, a youth-protection survey and a list of property owners with parcel and water-meter numbers that together give a near-complete address book of a commune of 1,381 inhabitants ([Inside IT, 2026-10-27](https://www.inside-it.ch/kritische-schweizer-infrastrukturen-attackiert-20261027)). Asked by Inside IT, the commune said it will make no statement on the publication ([Inside IT, 2026-10-27](https://www.inside-it.ch/kritische-schweizer-infrastrukturen-attackiert-20261027)).

**Defender takeaway:** a clean restore did not close the data-theft question here: the leak-site listing appeared 55 days after the encryption and the data has since been published, so a communal response to an encryption attack should keep its data-theft assessment open and plan for notification of affected persons, residents on social assistance first, and for the fraud that published AHV numbers, addresses and payment histories enable. The resident-fraud warning the commune issued belongs in the same response plan.

## Update — 2026-10-28T03:43:10Z

Inside IT reported on 2026-10-27 that SafePay has put the data stolen from Manno into the darknet, about 30 GB, and that the security firm Risikomonitor analysed it ([Inside IT, 2026-10-27](https://www.inside-it.ch/kritische-schweizer-infrastrukturen-attackiert-20261027)). Risikomonitor's analysis, relayed by Inside IT and not verified independently, finds files with about 5,300 e-mail addresses and more than 2,000 identifiable persons, social-assistance decisions with name, address, monthly amount, AHV numbers and health insurer from 2014 to December 2025, debt-enforcement extracts, naturalisation dossiers from 2018 and payment orders against tax debtors, and information on the whole population of 1,381 inhabitants ([Inside IT, 2026-10-27](https://www.inside-it.ch/kritische-schweizer-infrastrukturen-attackiert-20261027)). The commune told Inside IT it will make no statement. The claim as Inside IT reported it on 2026-09-29 named no dataset ([Inside IT, 2026-09-29](https://www.inside-it.ch/tessiner-gemeinde-wird-opfer-von-cyberkriminellen-20260929)).
