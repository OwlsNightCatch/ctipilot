---
schema: 1
kind: incident
horizon: operational
title: "Martigny-Combe (Valais) municipal email account compromised and used to send a fraudulent message to administration contacts — second Valais municipality hit in 2026"
headline: "A Swiss communal administration's business mailbox is compromised and weaponised against its own contact list"
summary: >
  The municipality of Martigny-Combe (canton Valais) detected unauthorised access to its
  administrative secretariat's business email system on 2026-08-18, used to send a fraudulent
  message to contacts of the administration with possible exposure of personal data. The incident
  was reported to Switzerland's BACS and the cantonal data-protection commissioner, and a criminal
  complaint was filed. It is the second Valais municipality reported hit by a cyberattack in 2026,
  after Vétroz in April (a separate incident of an undisclosed type).
discovered_at: "2026-08-28T06:42:00Z"
updated_at: null
event_date: "2026-08-18"
run_id: 2026-08-28T0409Z-intel
priority: notable
immediate_action: null
tags: [data-breach, phishing]
regions: [switzerland]
sectors: [public-sector]
entities: [incident:martigny-combe-email-compromise-2026-08]
techniques: [T1078]
affected_products: []
cves: []
sources:
  - url: "https://www.swisscybersecurity.net/news/2026-08-24/cyberangriff-kompromittiert-e-mail-system-der-gemeinde-martigny-combe"
    publisher: "SwissCybersecurity.net"
    date: "2026-08-24"
    role: primary
closed_sources: []
evidence:
  - quote: "Die Gemeinde Martigny-Combe im Wallis hat am 18. August einen unbefugten Zugriff auf das geschäftliche E-Mail-System ihres Gemeindesekretariats festgestellt."
    publisher: "Gemeinde Martigny-Combe statement, quoted by SwissCybersecurity.net"
  - quote: "konnte durch den Angriff eine betrügerische Nachricht versendet werden. Diese sei unter anderem an Kontakte der Verwaltung verschickt worden."
    publisher: "Gemeinde Martigny-Combe statement, quoted by SwissCybersecurity.net"
  - quote: "Martigny-Combe hat den Vorfall zudem dem Bundesamt für Cybersicherheit (BACS) sowie dem kantonalen Beauftragten für Datenschutz und Transparenz gemeldet."
    publisher: "SwissCybersecurity.net"
verification: single-source
sourcing_note: >
  Single-sourced to SwissCybersecurity.net's report of the municipality's own statement. A second,
  corroborating article (inside-it.ch) returned HTTP 403 on direct fetch and the jina reader
  fallback failed on exhausted API credit; not recovered this run.
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: C
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

The municipality of Martigny-Combe (canton Valais) detected unauthorised access to its administrative secretariat's business email system on 2026-08-18: "die Gemeinde Martigny-Combe im Wallis hat am 18. August einen unbefugten Zugriff auf das geschäftliche E-Mail-System ihres Gemeindesekretariats festgestellt" ([Gemeinde Martigny-Combe statement, quoted by SwissCybersecurity.net, 2026-08-24](https://www.swisscybersecurity.net/news/2026-08-24/cyberangriff-kompromittiert-e-mail-system-der-gemeinde-martigny-combe)). Per the municipality's own statement, the access was used to send a fraudulent message to contacts of the administration, and personal data contained in that email may have been passed to an unauthorised third party: "konnte durch den Angriff eine betrügerische Nachricht versendet werden. Diese sei unter anderem an Kontakte der Verwaltung verschickt worden" ([Gemeinde Martigny-Combe statement, quoted by SwissCybersecurity.net, 2026-08-24](https://www.swisscybersecurity.net/news/2026-08-24/cyberangriff-kompromittiert-e-mail-system-der-gemeinde-martigny-combe)) — the municipality specifically flags phishing and identity-theft risk for recipients of the fraudulent message.

The compromised access was blocked immediately on discovery, technical security measures were applied, and external specialists are now conducting a scoping analysis. The incident was reported to Switzerland's Bundesamt für Cybersicherheit (BACS) and to the cantonal data-protection and transparency commissioner: "Martigny-Combe hat den Vorfall zudem dem Bundesamt für Cybersicherheit (BACS) sowie dem kantonalen Beauftragten für Datenschutz und Transparenz gemeldet" ([SwissCybersecurity.net, 2026-08-24](https://www.swisscybersecurity.net/news/2026-08-24/cyberangriff-kompromittiert-e-mail-system-der-gemeinde-martigny-combe)), and a criminal complaint has been filed with the Valais cantonal police. This is the second Valais municipality reported hit by a cyberattack in 2026 — Vétroz was disabled by a cyberattack in April, a separate, already-dated incident of an undisclosed type not otherwise covered here — a pattern this pipeline has not previously tracked as a recurring theme for the canton.

No access vector is stated by any source, hence `techniques[]` carries only T1078 (Valid Accounts) for the unauthorised mailbox access itself; no technique is mapped for the onward fraudulent message, since the source does not state whether recipients were internal or external, or what the message contained. `actions[]` is empty: small-scale, single-municipality incident with no transferable technical detail beyond the standard business-email-compromise response already known to this audience.
