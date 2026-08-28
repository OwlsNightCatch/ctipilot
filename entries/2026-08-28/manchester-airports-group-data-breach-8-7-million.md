---
schema: 1
kind: incident
horizon: operational
title: "Manchester Airports Group confirms a breach touching roughly 8.7 million customers across Manchester, Stansted and East Midlands — car-park, lounge and airport-WiFi sign-up data taken, no operational or payment-card impact, no actor named"
headline: "One of Europe's largest airport-group operators discloses an 8.7M-record breach with no access vector confirmed"
summary: >
  Manchester Airports Group confirmed on 2026-08-27 that an unauthorised third party obtained
  customer data relating to car-park, lounge, Fast Track bookings and in-airport WiFi sign-ups
  across Manchester, Stansted and East Midlands airports, affecting roughly 8.7 million customers
  — the large majority with only an email address exposed. MAG states no bank or payment-card
  data was held, no operational or aviation-security system was touched, and no actor has claimed
  the incident. The UK ICO has confirmed receipt of a breach report.
discovered_at: "2026-08-28T06:10:00Z"
updated_at: null
event_date: "2026-08-27"
run_id: 2026-08-28T0409Z-intel
priority: high
immediate_action: null
tags: [data-breach]
regions: [europe, uk]
sectors: [transport]
entities: [incident:manchester-airports-group-data-breach-2026-08]
techniques: [T1213]
affected_products: []
cves: []
sources:
  - url: "https://www.manchesterairport.co.uk/help/data-security-incident/"
    publisher: "Manchester Airports Group (first-party statement)"
    date: "2026-08-27"
    role: primary
  - url: "https://www.theregister.com/security/2026/08/27/cybercrooks-jet-off-with-manchester-airports-group-customer-data/5292943"
    publisher: "The Register"
    date: "2026-08-27"
    role: corroborating
  - url: "https://www.infosecurity-magazine.com/news/manchester-airports-data-breach/"
    publisher: "Infosecurity Magazine"
    date: "2026-08-27"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Manchester Airports group has been subject to a cyber security incident by an unauthorised third party. A quantity of customer data has been obtained that relates to car park, lounge and Fast Track bookings and in-airport WIFI sign-ups at Manchester, Stansted, and East Midlands airports."
    publisher: "Manchester Airports Group"
  - quote: "At no point has passenger safety or aviation security been compromised."
    publisher: "Manchester Airports Group"
  - quote: "The overwhelming majority of those affected have only had their email addresses compromised."
    publisher: "The Register"
verification: multi-source
sourcing_note: >
  Manchester Airports Group's own first-party incident statement is the primary source; The
  Register and Infosecurity Magazine corroborate independently. The Register attributes "a hack,
  not a lapse" to MAG's own spokesperson, not to the outlet's own characterisation; the
  unconfirmed detail (a lower-than-typical ransom demand, a specific third-party-hosted database)
  is the outlet's own reporting rather than MAG's statement, and is flagged as such rather than
  adopted as fact.
confidence: medium
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
  - at: "2026-08-28T15:00:00Z"
    run_id: 2026-08-28T1500Z-audit
    type: improvement
    internal: true
    summary: >
      Operator-directed editorial pass (v4.2): removed composition-rationale narration and 
      pipeline-internal jargon from reader-facing text; tightened or cut paragraphs that 
      restated the summary or padded without responder value. No factual claim changed.
    fields: [body]
migrated_from: null
---

Manchester Airports Group (MAG), operator of Manchester, London Stansted and East Midlands airports, confirmed on 2026-08-27 that "an unauthorised third party" obtained "a quantity of customer data" relating to car-park, lounge and Fast Track bookings and in-airport WiFi sign-ups ([Manchester Airports Group, 2026-08-27](https://www.manchesterairport.co.uk/help/data-security-incident/)). Roughly 8.7 million customers are affected, the large majority with only an email address exposed — collected during public-WiFi signup: "the overwhelming majority of those affected have only had their email addresses compromised" ([The Register, 2026-08-27](https://www.theregister.com/security/2026/08/27/cybercrooks-jet-off-with-manchester-airports-group-customer-data/5292943)) — a smaller subset also had phone numbers, vehicle registrations and postcodes taken.

MAG states neither it nor the accessed system holds bank or payment-card data, and that no operational or aviation-security system was touched: "at no point has passenger safety or aviation security been compromised" ([Manchester Airports Group, 2026-08-27](https://www.manchesterairport.co.uk/help/data-security-incident/)). The group has suspended its Manage My Booking self-service portal as a precaution while investigating. The Register reports — attributed to the outlet, not confirmed by MAG's own statement — that the intrusion compromised one internal system and then pulled files from a third-party-hosted database, that the attacker's ransom demand was notably lower than the group's typical extortion demand and was not paid, and that MAG characterises the incident internally as "a hack, not a lapse." No extortion group or actor has claimed the incident publicly at time of writing, and neither MAG nor any outlet has named an access vector, an exploited product, or a CVE. The UK ICO has confirmed receipt of a breach report and is assessing it.

No source states an access vector, exploited product or CVE, and no extortion actor has claimed responsibility; per The Register's reporting the data was obtained from an internal system and a third-party-hosted database. The transferable point is scale rather than mechanism: 8.7 million records exposed through apparently low-sensitivity WiFi-signup collection shows how ancillary customer-facing services (guest WiFi, parking bookings) can carry disproportionate downstream exposure.
