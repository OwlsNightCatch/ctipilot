---
schema: 1
kind: incident
horizon: operational
title: "BWH Hotels (Best Western, WorldHotels, Sure Hotels) — 181-day unauthorised access to a guest-reservation web application, six EU brands in scope"
headline: "BWH Hotels (Best Western, WorldHotels, Sure Hotels) — 181-day unauthorised access to a guest-reservation web application, six EU brands in scope"
summary: "BWH Hotels — the parent operating Best Western Hotels & Resorts, WorldHotels and Sure Hotels — disclosed that an unauthorised third party had access to a guest-reservation web application from 2025-10-14 to 2026-04-22, a 181-day dwell, before detection on 2026-04-22 prompted BWH to take the affected application …"
discovered_at: "2026-05-13T05:00:01Z"
event_date: 2026-05-12
run_id: 2026-05-13-c148b9a5
priority: notable
immediate_action: null
tags:
  - data-breach
  - identity
regions:
  - global
sectors:
  - retail
entities: []
cves: []
sources:
  - url: "https://www.theregister.com/security/2026/05/11/best-western-hotels-confirms-web-app-data-breach/5238020"
    publisher: "The Register, 2026-05-11"
    role: primary
  - url: "https://www.securityweek.com/bwh-hotels-says-hackers-had-access-to-reservation-data-for-6-months/"
    publisher: "SecurityWeek, 2026-05-12"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-13.md
---

BWH Hotels — the parent operating Best Western Hotels & Resorts, WorldHotels and Sure Hotels — disclosed that an unauthorised third party had access to a guest-reservation web application from 2025-10-14 to 2026-04-22, a 181-day dwell, before detection on 2026-04-22 prompted BWH to take the affected application offline ([The Register, 2026-05-11](https://www.theregister.com/security/2026/05/11/best-western-hotels-confirms-web-app-data-breach/5238020); [SecurityWeek, 2026-05-12](https://www.securityweek.com/bwh-hotels-says-hackers-had-access-to-reservation-data-for-6-months/)). Disclosed data fields: guest names, email addresses, phone numbers, home addresses, reservation numbers, dates of stay and special requests; payment / financial data is stated as unaffected. BWH Hotels operates properties across multiple EEA jurisdictions, so EEA-resident guest data is in scope; the company has not yet published a per-country DPA notification list, and the cited disclosures do not enumerate per-country exposure. No attribution; no extortion demand reported.

**Defender takeaway:** The pattern — third-party web application held attacker access for 181 days before discovery — fits the IAB / data-theft tradecraft we have been seeing repeatedly against EU SaaS estates: the asset is a *single application* sitting outside the corporate SOC's primary telemetry, with credentials likely harvested via infostealer or vishing of a contractor account. Detection concepts: instrument **every** customer-facing reservation / CRM / loyalty SaaS with download-volume alerting at the API tier (mapped to `T1530 Data from Cloud Storage Object` and `T1213.003 Data from Information Repositories: Code Repositories`-equivalent for SaaS DBs); push CASB DLP policies that flag bulk export of PII fields by any non-batch service account; require step-up auth on any session exporting more than N records per hour. Public-sector implication: government staff travelling on official duty and using BWH-brand properties had itinerary + contact data exposed; review whether any travel-booking integrations route through this application and, if so, treat the in-scope passport-data fields as compromised.
