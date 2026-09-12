---
schema: 1
kind: incident
title: "Shared booking-software breach exposes guests at 100+ Dutch, Belgian and Irish hotels; phishing wave already underway"
headline: "Shared booking-software breach exposes guests at 100+ Dutch, Belgian and Irish hotels; phishing wave already underway"
summary: "A shared hotel-booking SaaS breach exposed guests at 100+ Dutch, Belgian and Irish hotels, and a separate UN World Food Programme breach exposed ~600,000 Gaza households' IDs and locations — both already weaponised for follow-on fraud / physical-safety risk."
discovered_at: "2026-06-04T05:00:01Z"
event_date: 2026-06-03
run_id: 2026-06-04-51b23ffa
priority: high
immediate_action: null
tags:
  - data-breach
  - supply-chain
  - phishing
regions:
  - europe
sectors:
  - technology
entities: []
cves: []
sources:
  - url: "https://www.dutchnews.nl/2026/06/mass-data-breach-on-over-100-dutch-hotels-hits-guests/"
    publisher: DutchNews.nl
    role: primary
  - url: "https://www.techzine.eu/news/security/141806/dozens-of-dutch-hotels-affected-by-data-breach/"
    publisher: Techzine EU
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
migrated_from: briefs/2026-06-04.md
---

More than 100 hotels in the Netherlands plus properties in Belgium and Ireland had guest reservation records (names, contact details, arrival/departure dates) exposed through a shared booking / channel-management / property-management SaaS layer rather than any single hotel's own systems ([DutchNews.nl, 2026-06-03](https://www.dutchnews.nl/2026/06/mass-data-breach-on-over-100-dutch-hotels-hits-guests/) · [Techzine EU, 2026-06-03](https://www.techzine.eu/news/security/141806/dozens-of-dutch-hotels-affected-by-data-breach/)). Hospecs, coordinating the response, attributes the root cause to the upstream provider; the Dutch DPA (Autoriteit Persoonsgegevens) has opened an investigation and GDPR Art. 33/34 clocks are running for each hotel as an independent controller. Criminals are already sending contextually accurate "confirm and pay for your reservation" phishing referencing real upcoming stays.
**Defender takeaway:** a textbook upstream-SaaS supply-chain breach where every downstream customer carries controller liability with zero visibility into the compromise — hunt for anomalous bulk-read API calls against reservation endpoints and treat reservation-context phishing as a known follow-on.
