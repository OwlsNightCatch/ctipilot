---
schema: 1
kind: policy
horizon: strategic
weekly_section: weekly-policy
title: "Netherlands NIS2 transposition slips past its 1 July target — Senate vote set for 7 July, entry into force now 15 August 2026"
headline: "Netherlands NIS2 (Cyberbeveiligingswet) slips — Senate vote 7 July, entry into force now 15 August 2026"
summary: "The Dutch NIS2 transposition (Cyberbeveiligingswet) missed the 1 July 2026 entry-into-force target reported in prior coverage. The Eerste Kamer (Senate) tabled its response to the second committee report on 29 June — the last written step before debate — and its bill-tracking page now sets the floor vote for 7 July, with the government's revised entry-into-force target 15 August 2026. Substantive scope is unchanged (NCSC-NL supervisor, 24h/72h/1-month notification, fines to EUR 10M/2%, board liability, ~1,000→~8,000 in-scope entities)."
discovered_at: "2026-07-05T23:42:00Z"
event_date: 2026-07-01
run_id: 2026-07-05T2305Z-weekly
priority: notable
immediate_action: null
tags:
  - law-enforcement
regions:
  - europe
sectors:
  - public-sector
  - energy
  - water
  - transport
  - healthcare
  - finance
  - telco
entities: []
cves: []
sources:
  - url: "https://www.eerstekamer.nl/wetsvoorstel/36764_cyberbeveiligingswet"
    publisher: Eerste Kamer der Staten-Generaal (official bill page)
    role: primary
  - url: "https://ibestuur.nl/digitale-weerbaarheid/digitale-veiligheid/eerste-kamer-stemt-7-juli-over-cyberbeveiligingswet"
    publisher: iBestuur
    role: corroborating
closed_sources: []
evidence:
  - quote: "De stemming in de Eerste Kamer vindt plaats op 7 juli 2026."
    publisher: Eerste Kamer der Staten-Generaal (official bill page)
  - quote: "Het voorstel (EK, A) is op 15 april 2026 aangenomen door de Tweede Kamer."
    publisher: Eerste Kamer der Staten-Generaal (official bill page)
verification: multi-source
sourcing_note: "Vote date and legislative-status quotes are from the Eerste Kamer's own bill page (authoritative primary); the 15 August 2026 revised entry-into-force date is iBestuur-reported."
confidence: high
classification:
  reliability: A
  credibility: 2
update_of: "2026-06-29/netherlands-nis2-cyberbeveiligingswet-clears-the-lower-house"
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions:
  - "Swiss/EU public-sector or CI operators with Dutch group entities, Dutch-hosted infrastructure, or Dutch suppliers/counterparties: re-anchor internal NIS2-readiness milestones on 15 August 2026 rather than 1 July."
  - "Review whether contractual NIS2-compliance-by-date clauses with Dutch counterparties that reference '1 July 2026' need re-negotiation to the revised timeline."
---

**UPDATE (originally covered 2026-06-29):** the Dutch NIS2 transposition — the Cyberbeveiligingswet (Cbw) plus the companion Wet weerbaarheid kritieke entiteiten — has missed the 1 July 2026 entry-into-force target the prior weekly reported as the government's goal.

The Eerste Kamer (Senate) tabled its government response to the second committee report ("nota naar aanleiding van het tweede verslag") on 29 June 2026 — the last written-preparation step before plenary debate — and the Senate's own bill-tracking page now states the floor vote will take place on **7 July 2026**, noting the bill was adopted by the Tweede Kamer on 15 April 2026 ([Eerste Kamer, bill 36764](https://www.eerstekamer.nl/wetsvoorstel/36764_cyberbeveiligingswet)). iBestuur reports the government's revised entry-into-force target is now **15 August 2026**, roughly six weeks later than previously communicated ([iBestuur, 2026-07-01](https://ibestuur.nl/digitale-weerbaarheid/digitale-veiligheid/eerste-kamer-stemt-7-juli-over-cyberbeveiligingswet)).

The substantive scope is unchanged from prior coverage: NCSC-NL as designated supervisor, a three-step 24h/72h/one-month incident-notification protocol, essential-entity fines up to EUR 10M or 2% of global turnover, personal board liability for security-measure oversight, and an expansion of in-scope Dutch entities from roughly 1,000 to roughly 8,000. This is the fourth documented slip in the Dutch NIS2 timetable (originally targeted Q3 2025). **Defender takeaway:** the only action for a Swiss/EU reader is administrative — re-anchor readiness milestones and contractual compliance-date references onto 15 August 2026 for any Dutch group entities, hosting, or counterparties. No technical control change follows from the date shift itself.
