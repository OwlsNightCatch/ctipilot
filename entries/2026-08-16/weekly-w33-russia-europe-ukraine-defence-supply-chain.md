---
schema: 1
kind: research
horizon: strategic
weekly_section: weekly-research
title: "Russia's campaign against Europe's Ukraine defence supply chain is assessed to have widened from collection and sabotage to pressuring the people and firms behind it — and the cyber half is aimed at logistics data, not at the manufacturers"
headline: "Truesec assesses the target set has broadened past logistics disruption to the individuals and suppliers enabling European defence support"
summary: >
  Truesec published an assessment on 14 August 2026 drawing a set of separately-reported European incidents
  into one campaign picture: German authorities reportedly investigating surveillance of the chief executive
  of drone manufacturer Donaustahl and his family in late 2025 and early 2026; the 2024 US-assisted
  disruption of a Russian plot against Rheinmetall's chief executive; Russian publication of European drone
  producer addresses, which Truesec assesses as target signalling rather than disclosure; and GRU-linked
  cyber activity against logistics and technology companies transporting aid to Ukraine. Its judgement is
  that the campaign's focus "is no longer limited to intelligence collection, sabotage or disruption of
  logistics" and now extends to the people, facilities and supply chains that make European defence support
  possible. For defenders the concrete half is the cyber targeting, which Western authorities attributed to
  GRU Unit 26165: attempts to obtain shipment-related information including train schedules, manifests,
  routes, cargo contents and sender and recipient details. This is an assessment resting on reporting
  Truesec cites rather than on new first-hand telemetry, and is carried as such.
discovered_at: "2026-08-16T23:59:00Z"
event_date: "2026-08-14"
run_id: 2026-08-16T2315Z-weekly
priority: notable
immediate_action: null
tags: [nation-state, espionage, russia-nexus, data-breach]
regions: [europe, dach, switzerland]
sectors: [defense, transport, manufacturing, public-sector]
entities: []
techniques: [T1591, T1591.002, T1213, T1005, T1589]
affected_products: []
cves: []
sources:
  - url: "https://www.truesec.com/hub/blog/russia-targets-businesses-and-officials-behind-europes-ukraine-defence-supply-chain"
    publisher: "Truesec"
    date: "2026-08-14"
    role: primary
closed_sources: []
evidence:
  - quote: "GRU-linked cyber activity has focused on logistics and technology companies involved in transporting aid to Ukraine. Observed GRU-linked activity included attempts to access shipment-related information such as train schedules, manifests, routes, cargo contents and sender/recipient details."
    publisher: "Truesec"
  - quote: "The focus is no longer limited to intelligence collection, sabotage or disruption of logistics."
    publisher: "Truesec"
  - quote: "In the cyber and logistics campaign, Western authorities have specifically attributed activity to GRU Unit 26165, while the Donaustahl reporting refers more broadly to Russian intelligence services."
    publisher: "Truesec"
verification: single-source
sourcing_note: >
  Single-source and deliberately so. Truesec's piece is an assessment that synthesises reporting it
  attributes to named third parties — Die Zeit and The Insider for the Donaustahl surveillance investigation,
  CNN and the BBC for the 2024 Rheinmetall plot, Euractiv and IntelliNews for the published drone-producer
  addresses, and a CISA, NSA, FBI and NCSC-UK joint advisory of April 2026 for the GRU logistics targeting.
  None of those underlying items is in-window and none was re-fetched by this run, so every fact here is
  attributed to Truesec's own account of it rather than presented as independently confirmed. What is
  in-window is the assessment itself. The piece can fairly be read as a retrospective compilation as to the
  underlying facts, which is why this entry claims no new incident — the publishable content is the horizon
  judgement and the named data classes.
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
migrated_from: null
---

Truesec's 14 August assessment gathers separately-reported European incidents into a single campaign picture. In late 2025 and early 2026 German authorities were reportedly investigating surveillance of the chief executive of the drone manufacturer Donaustahl and his family; in 2024 US intelligence reportedly helped Germany disrupt a Russian plot against Rheinmetall's chief executive; Russia published the addresses of European drone producers, which Truesec assesses as "target signalling: intimidation, information operations and possible enabling of future targeting by sympathizers or recruited proxies" rather than as disclosure of anything. Set against that physical-domain activity, the cyber half is narrower and more concrete: "GRU-linked cyber activity has focused on logistics and technology companies involved in transporting aid to Ukraine. Observed GRU-linked activity included attempts to access shipment-related information such as train schedules, manifests, routes, cargo contents and sender/recipient details" ([Truesec, 2026-08-14](https://www.truesec.com/hub/blog/russia-targets-businesses-and-officials-behind-europes-ukraine-defence-supply-chain)). Truesec attributes the attribution itself: "In the cyber and logistics campaign, Western authorities have specifically attributed activity to GRU Unit 26165, while the Donaustahl reporting refers more broadly to Russian intelligence services," pointing at an April 2026 joint advisory from CISA, the NSA, the FBI and NCSC UK.

The horizon judgement is the reason to record it. Truesec's assessment is that the campaign's focus "is no longer limited to intelligence collection, sabotage or disruption of logistics" and now reaches the people, facilities and supply chains that make European defence support to Ukraine possible — with the operating model combining state-led intelligence targeting with recruited low-level agents who are not trained intelligence officers.

**Defender takeaway:** the operationally useful part is the data class, because it is unusual and it scopes a hunt precisely. An adversary after train schedules, manifests, routes, cargo contents and sender and recipient details is not after the systems that normally attract attention — it is after transport management systems, freight-forwarding platforms, customs and shipping documentation, and the mailboxes of the people who handle them. For a logistics or transport operator, or a public body that contracts one, that reframes which application owners get an access review and which document repositories are worth a retrospective search, and it does so independently of any indicator. The second point is about scope of protection rather than detection: where reporting describes surveillance and physical targeting of named individuals alongside the network activity, the security question extends past the estate to executive and personnel data — which of the organisation's people are publicly identifiable as connected to defence work, and through which of its own published sources. Nothing here is a Swiss incident, and this entry names none; the relevance is that the profiled sectors include transport and the coverage focus is European critical infrastructure.

**Triage:** collection against shipment data looks like ordinary business use of the same systems, so the discriminators are account context and breadth rather than the access itself. The shapes worth separating from routine operations are a single account querying or exporting consignment records far outside its normal customer or route scope, retrieval of historical manifests with no matching operational request, and searches of document repositories or mailboxes keyed to route, cargo or counterparty terms by accounts that do not perform that role. Legitimate freight and customs work is narrow and tied to a live consignment; bulk retrieval across counterparties and time is not. Where an intrusion is suspected, the personnel dimension is part of the scope: mailbox and directory access touching staff whose work is publicly linked to defence customers.
