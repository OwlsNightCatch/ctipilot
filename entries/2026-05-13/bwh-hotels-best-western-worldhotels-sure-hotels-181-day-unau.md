---
schema: 1
kind: incident
title: "BWH Hotels (Best Western, WorldHotels, Sure Hotels): attackers had access to a guest-reservation web application for about six months"
headline: "BWH Hotels says attackers had access to a guest-reservation web application from October 2025 until April 2026"
summary: "BWH Hotels, which owns the Best Western Hotels & Resorts, WorldHotels and Sure Hotels brands, told guests that attackers had access to a web application holding reservation data from 2025-10-14 until the intrusion was discovered on 2026-04-22, exposing names, contact details, home addresses and reservation details; payment data was not stored there. Neither the access vector nor the number of affected guests is disclosed."
discovered_at: "2026-05-13T05:00:01Z"
event_date: 2026-05-12
run_id: 2026-05-13-c148b9a5
priority: routine
immediate_action: null
tags:
  - data-breach
  - identity
regions:
  - global
sectors:
  - retail
entities:
  - "incident:bwh-hotels-breach-2026"
techniques: [T1213]
cves: []
sources:
  - url: "https://www.theregister.com/security/2026/05/11/best-western-hotels-confirms-web-app-data-breach/5238020"
    publisher: "The Register"
    date: "2026-05-11"
    role: primary
  - url: "https://www.securityweek.com/bwh-hotels-says-hackers-had-access-to-reservation-data-for-6-months/"
    publisher: "SecurityWeek"
    date: "2026-05-12"
    role: corroborating
closed_sources: []
evidence:
  - quote: "the intrusion was discovered on April 22, and an investigation showed that threat actors had access since October 14, 2025."
    publisher: "SecurityWeek"
    source_url: "https://www.securityweek.com/bwh-hotels-says-hackers-had-access-to-reservation-data-for-6-months/"
  - quote: "identified the intrusion on April 22, but the affected data goes back to October 14, 2025."
    publisher: "The Register"
    source_url: "https://www.theregister.com/security/2026/05/11/best-western-hotels-confirms-web-app-data-breach/5238020"
  - quote: "It’s unclear how many individuals were affected by the incident."
    publisher: "SecurityWeek"
    source_url: "https://www.securityweek.com/bwh-hotels-says-hackers-had-access-to-reservation-data-for-6-months/"
  - quote: "The hotel group seems concerned that the attackers may leverage the stolen data for scams and phishing."
    publisher: "SecurityWeek"
    source_url: "https://www.securityweek.com/bwh-hotels-says-hackers-had-access-to-reservation-data-for-6-months/"
verification: single-source-victim
sourcing_note: >
  Every fact comes from BWH Hotels' guest notification and its CTO's statement, as The Register and SecurityWeek relay them. SecurityWeek
  says the attackers had access since 2025-10-14, while The Register says the affected data goes back to that date.
confidence: medium
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
migrated_from: briefs/2026-05-13.md
updates:
  - at: "2026-10-21T20:46:47Z"
    run_id: 2026-10-21T1148Z-audit
    type: correction
    summary: >
      BWH Hotels owns three brands, WorldHotels, Best Western Hotels & Resorts and Sure Hotels, and the
      exposed fields are contact and reservation data, not passport data. The access ran from 2025-10-14
      until discovery on 2026-04-22 according to the guest emails SecurityWeek quotes, while The Register
      says the affected data goes back to that date; no source discloses the access vector, the number or
      location of affected guests, or an infostealer or contractor-account route.
    fields: [body, classification, confidence, entities, evidence, headline, priority, sources, sourcing_note, summary, title, verification, techniques]
---

BWH Hotels, which operates more than 4,000 hotels including WorldHotels, Best Western Hotels & Resorts and Sure Hotels, told affected guests that it discovered the intrusion on 2026-04-22 and that the attackers had had access since 2025-10-14 to a web application holding guest names, email addresses, phone numbers and reservation details; payment and other financial information was not stored there, and how many guests are affected is unclear ([SecurityWeek, 2026-05-12](https://www.securityweek.com/bwh-hotels-says-hackers-had-access-to-reservation-data-for-6-months/)). The Register says the affected data goes back to 2025-10-14 and also includes home addresses, reservation numbers, dates of stay and special requests, that BWH took the application offline and revoked the unauthorised access, and that BWH has notified the appropriate regulatory agencies ([The Register, 2026-05-11](https://www.theregister.com/security/2026/05/11/best-western-hotels-confirms-web-app-data-breach/5238020)). No source states how the attackers got in, and no known cybercrime group has claimed the attack ([SecurityWeek, 2026-05-12](https://www.securityweek.com/bwh-hotels-says-hackers-had-access-to-reservation-data-for-6-months/)).

**Defender takeaway:** with no access vector disclosed there is no detection or patching decision; guests should expect scams and phishing that reuse their reservation details, the misuse BWH itself is concerned about ([SecurityWeek, 2026-05-12](https://www.securityweek.com/bwh-hotels-says-hackers-had-access-to-reservation-data-for-6-months/)).

## Correction — 2026-10-21T20:46:47Z

BWH Hotels owns three brands, WorldHotels, Best Western Hotels & Resorts and Sure Hotels, and the exposed fields are names, email addresses, telephone numbers, home addresses and reservation details, with no payment, bank or passport data involved ([The Register, 2026-05-11](https://www.theregister.com/security/2026/05/11/best-western-hotels-confirms-web-app-data-breach/5238020)). SecurityWeek, quoting the guest emails, says the attackers had access from 2025-10-14 until the intrusion was discovered on 2026-04-22, while The Register says the affected data goes back to 2025-10-14; neither source discloses how the attackers got in or how many guests are affected ([SecurityWeek, 2026-05-12](https://www.securityweek.com/bwh-hotels-says-hackers-had-access-to-reservation-data-for-6-months/)), and BWH says only that it notified the appropriate regulatory agencies ([The Register, 2026-05-11](https://www.theregister.com/security/2026/05/11/best-western-hotels-confirms-web-app-data-breach/5238020)).
