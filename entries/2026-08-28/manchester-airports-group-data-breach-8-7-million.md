---
schema: 1
kind: incident
title: "Manchester Airports Group confirms a breach touching roughly 8.7 million customers across Manchester, Stansted and East Midlands — car-park, lounge and airport-WiFi sign-up data taken; FulcrumSec later claims credit and a client-side API-credential access vector"
headline: "One of Europe's largest airport-group operators discloses an 8.7M-record breach, later claimed by FulcrumSec via an exposed marketing-API credential"
summary: >
  Manchester Airports Group confirmed on 2026-08-27 that an unauthorised third party obtained
  customer data relating to car-park, lounge, Fast Track bookings and in-airport WiFi sign-ups
  across Manchester, Stansted and East Midlands airports, affecting roughly 8.7 million customers
  — the large majority with only an email address exposed. The extortion group FulcrumSec has since
  claimed responsibility, telling BleepingComputer it stole roughly 86GB via airport-specific
  Iterable marketing-platform API credentials exposed in client-side JavaScript; MAG has not
  addressed the specific claims.
discovered_at: "2026-08-28T06:10:00Z"
updated_at: "2026-08-31T05:35:00Z"
event_date: "2026-08-27"
run_id: 2026-08-28T0409Z-intel
priority: high
immediate_action: null
tags: [data-breach]
regions: [europe, uk]
sectors: [transport]
entities: [incident:manchester-airports-group-data-breach-2026-08, actor:fulcrumsec]
techniques: [T1213, T1552.001]
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
  - url: "https://www.bleepingcomputer.com/news/security/fulcrumsec-claims-manchester-airports-hack-theft-of-86-gb-of-data/"
    publisher: "BleepingComputer"
    date: "2026-08-30"
    role: corroborating
  - url: "https://securityaffairs.com/198143/cyber-crime/extortion-group-fulcrumsec-claims-86gb-manchester-airports-group-data-theft.html"
    publisher: "Security Affairs"
    date: "2026-08-30"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Manchester Airports group has been subject to a cyber security incident by an unauthorised third party. A quantity of customer data has been obtained that relates to car park, lounge and Fast Track bookings and in-airport WIFI sign-ups at Manchester, Stansted, and East Midlands airports."
    publisher: "Manchester Airports Group"
  - quote: "At no point has passenger safety or aviation security been compromised."
    publisher: "Manchester Airports Group"
  - quote: "The overwhelming majority of those affected have only had their email addresses compromised."
    publisher: "The Register"
  - quote: "The group claims it obtained access using airport-specific Iterable API credentials exposed in client-side JavaScript and that the stolen material includes nearly 200,000 records related to upcoming travel during the remainder of 2026."
    publisher: "BleepingComputer (Ax Sharma)"
    source_url: "https://www.bleepingcomputer.com/news/security/fulcrumsec-claims-manchester-airports-hack-theft-of-86-gb-of-data/"
  - quote: "MAG is confident that we have taken effective measures to protect our customers and we have contacted all those affected, including reaching out to all those with upcoming bookings to advise them of additional support"
    publisher: "MAG spokesperson, via BleepingComputer"
    source_url: "https://www.bleepingcomputer.com/news/security/fulcrumsec-claims-manchester-airports-hack-theft-of-86-gb-of-data/"
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
  - at: "2026-08-30T13:12:06Z"
    run_id: 2026-08-30T1312Z-audit
    type: correction
    summary: >
      The claim that the UK ICO had confirmed receipt of a breach report and was assessing it is
      not stated by any source this entry cites and has been removed from the summary and the
      body. What the reporting does establish is narrower: The Register says the ICO asked MAG
      not to disclose details of the ransom note, the demands or the group name, and MAG's own
      statement names no regulator at all. Regulator engagement is real; a confirmed filing is
      not on the record.
    fields: [summary, body]
  - at: "2026-08-31T05:35:00Z"
    run_id: 2026-08-31T0411Z-intel
    type: update
    summary: >
      The extortion group FulcrumSec claimed responsibility on 2026-08-30, telling BleepingComputer
      it stole roughly 86GB — considerably more than MAG's own disclosure suggested — and naming an
      access vector for the first time: airport-specific Iterable (marketing-platform) API
      credentials exposed in client-side JavaScript. MAG has not addressed the specific claims and
      continues to point to its existing customer statement.
    fields: [title, headline, entities, techniques, summary, sources, evidence, body]
migrated_from: null
---

Manchester Airports Group (MAG), operator of Manchester, London Stansted and East Midlands airports, confirmed on 2026-08-27 that "an unauthorised third party" obtained "a quantity of customer data" relating to car-park, lounge and Fast Track bookings and in-airport WiFi sign-ups ([Manchester Airports Group, 2026-08-27](https://www.manchesterairport.co.uk/help/data-security-incident/)). Roughly 8.7 million customers are affected, the large majority with only an email address exposed — collected during public-WiFi signup: "the overwhelming majority of those affected have only had their email addresses compromised" ([The Register, 2026-08-27](https://www.theregister.com/security/2026/08/27/cybercrooks-jet-off-with-manchester-airports-group-customer-data/5292943)) — a smaller subset also had phone numbers, vehicle registrations and postcodes taken.

MAG states neither it nor the accessed system holds bank or payment-card data, and that no operational or aviation-security system was touched: "at no point has passenger safety or aviation security been compromised" ([Manchester Airports Group, 2026-08-27](https://www.manchesterairport.co.uk/help/data-security-incident/)). The group has suspended its Manage My Booking self-service portal as a precaution while investigating. The Register reports — attributed to the outlet, not confirmed by MAG's own statement — that the intrusion compromised one internal system and then pulled files from a third-party-hosted database, that the attacker's ransom demand was notably lower than the group's typical extortion demand and was not paid, and that MAG characterises the incident internally as "a hack, not a lapse." At the time of MAG's initial disclosure, no extortion group had claimed the incident publicly and no outlet had named an access vector, an exploited product, or a CVE — that changed three days later, when FulcrumSec claimed responsibility and named an access vector (see the 2026-08-31 update below). The Register reports that the Information Commissioner's Office "asked MAG not to share details of the ransom note, the extortion demands, or the group name" ([The Register, 2026-08-27](https://www.theregister.com/security/2026/08/27/cybercrooks-jet-off-with-manchester-airports-group-customer-data/5292943)); no source states that the ICO has confirmed receiving a breach report, and MAG says only that it has "informed and are working with the relevant authorities".

No source states an access vector, exploited product or CVE, and no extortion actor has claimed responsibility; per The Register's reporting the data was obtained from an internal system and a third-party-hosted database. The transferable point is scale rather than mechanism: 8.7 million records exposed through apparently low-sensitivity WiFi-signup collection shows how ancillary customer-facing services (guest WiFi, parking bookings) can carry disproportionate downstream exposure.

## Correction — 2026-08-30T13:12:06Z

This entry stated that the UK Information Commissioner's Office had confirmed receipt of a breach report and was assessing it. No source cited here says that. MAG's own statement names no regulator, saying only that it has "informed and are working with the relevant authorities" ([Manchester Airports Group, 2026-08-27](https://www.manchesterairport.co.uk/help/data-security-incident/)), and the closest the reporting comes is The Register's account that the ICO "asked MAG not to share details of the ransom note, the extortion demands, or the group name" ([The Register, 2026-08-27](https://www.theregister.com/security/2026/08/27/cybercrooks-jet-off-with-manchester-airports-group-customer-data/5292943)). The distinction matters for anyone reading this as a regulatory-timeline signal: engagement is on the record, a confirmed statutory filing is not.

## Update — 2026-08-31T05:35:00Z

The extortion group FulcrumSec claimed responsibility on 2026-08-30, telling BleepingComputer it stole approximately 86GB of data — considerably more than MAG's original disclosure suggested ([BleepingComputer, 2026-08-30](https://www.bleepingcomputer.com/news/security/fulcrumsec-claims-manchester-airports-hack-theft-of-86-gb-of-data/)). The group says it obtained access using airport-specific Iterable (marketing-platform) API credentials exposed in client-side JavaScript — code that runs in the customer's own browser, so anyone inspecting network calls or page source could read the credentials — and claims the haul includes nearly 200,000 records tied to upcoming travel through the rest of 2026, alongside a roughly 21.5GB Manchester customer export combining identifiers, historical booking activity and marketing classifications. BleepingComputer validated one sample record against a real traveller's known purchase history, matching Fast Track bookings, arrival times, terminal and amounts paid, though it could not independently verify the claimed scope. MAG has not addressed the specific claims (the exposed credentials, the 86GB figure, the future-travel data) and continues to point to its existing customer-notification statement: "MAG is confident that we have taken effective measures to protect our customers and we have contacted all those affected, including reaching out to all those with upcoming bookings to advise them of additional support" ([BleepingComputer, 2026-08-30](https://www.bleepingcomputer.com/news/security/fulcrumsec-claims-manchester-airports-hack-theft-of-86-gb-of-data/)). No payment-card or banking data is reported exposed.

The exposure class this adds is distinct from the original disclosure: a third-party marketing or analytics SaaS API key embedded directly in browser-delivered JavaScript is effectively a public credential the moment the page is inspectable, independent of any server-side hardening. Organisations embedding third-party API keys client-side should verify with the vendor whether the key's scope can be restricted to write-only/track-only actions rather than full read access to customer records, and review outbound API call patterns from public web front-ends for tokens visible in bundled JS or the browser's network tab.
