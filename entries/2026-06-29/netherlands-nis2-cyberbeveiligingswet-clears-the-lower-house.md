---
schema: 1
kind: policy
horizon: strategic
title: >
  Netherlands NIS2 (Cyberbeveiligingswet) clears the lower house — entry into force targeted for 1
  July 2026
headline: >
  Netherlands NIS2 (Cyberbeveiligingswet) clears the lower house — entry into force targeted for 1
  July 2026
summary: >
  Policy: the Netherlands' NIS2 law cleared its lower house (entry into force targeted for 1
  July); the EU CRA reporting obligation is ~75 days out (11 September) — enforceable Dutch
  notification clocks are imminent and CRA SRP onboarding should start. (NL Digital Government,
  ENISA SRP)
discovered_at: "2026-06-29T00:21:23Z"
updated_at: "2026-07-12T23:52:00Z"
event_date: null
run_id: 2026-W26-b78503e7
priority: high
immediate_action: null
tags:
  - law-enforcement
  - eu-nexus
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
techniques: []
affected_products: []
cves: []
sources:
  - url: "https://www.rijksoverheid.nl/actueel/nieuws/2026/04/15/tweede-kamer-stemt-in-met-wetsvoorstellen-cyberbeveiligingswet-en-wet-weerbaarheid-kritieke-entiteiten"
    publisher: Rijksoverheid — Tweede Kamer vote
    role: primary
  - url: "https://www.nldigitalgovernment.nl/nis2-directive-cyberbeveiligingswet-cbw/"
    publisher: NL Digital Government — Cyberbeveiligingswet
    role: corroborating
  - url: "https://ucomply.cloud/en/blog/cyberbeveiligingswet-1-juli-2026-wat-moet-u-nu-regelen/"
    publisher: uComply advisory
    role: corroborating
  - url: "https://www.eerstekamer.nl/wetsvoorstel/36764_cyberbeveiligingswet"
    publisher: Eerste Kamer der Staten-Generaal (official bill page)
    role: primary
  - url: "https://ibestuur.nl/digitale-weerbaarheid/digitale-veiligheid/eerste-kamer-stemt-7-juli-over-cyberbeveiligingswet"
    publisher: iBestuur
    role: corroborating
  - url: "https://www.rijksoverheid.nl/actueel/nieuws/2026/07/07/cyberbeveiligingswet-en-wet-weerbaarheid-kritieke-entiteiten-vanaf-15-augustus-2026-van-kracht"
    publisher: Rijksoverheid.nl (Dutch national government)
    role: primary
  - url: "https://www.ncsc.nl/nieuws/de-cyberbeveiligingswet-in-laatste-fase-van-vaststelling"
    publisher: NCSC-NL
    role: corroborating
closed_sources: []
evidence:
  - quote: De stemming in de Eerste Kamer vindt plaats op 7 juli 2026.
    publisher: Eerste Kamer der Staten-Generaal (official bill page)
  - quote: "Het voorstel (EK, A) is op 15 april 2026 aangenomen door de Tweede Kamer."
    publisher: Eerste Kamer der Staten-Generaal (official bill page)
  - quote: De wetten treden op 15 augustus 2026 in werking.
    publisher: Rijksoverheid.nl (Dutch national government)
verification: multi-source
sourcing_note: null
confidence: high
references: []
weekly_section: weekly-policy
deep_dive: false
deep_dive_category: null
org_triage: null
classification: null
watchlist_hit: false
actions:
  - "Swiss/EU public-sector or CI operators with Dutch group entities, Dutch-hosted infrastructure, or Dutch suppliers/counterparties: re-anchor internal NIS2-readiness milestones on 15 August 2026 rather than 1 July."
  - "Review whether contractual NIS2-compliance-by-date clauses with Dutch counterparties that reference '1 July 2026' need re-negotiation to the revised timeline."
updates:
  - at: "2026-07-05T23:42:00Z"
    run_id: 2026-07-05T2305Z-weekly
    type: update
    summary: >
      The Dutch NIS2 transposition (Cyberbeveiligingswet) missed the 1 July 2026 entry-into-force
      target reported in prior coverage. The Eerste Kamer (Senate) tabled its response to the second
      committee report on 29 June — the last written step before debate — and its bill-tracking page
      now sets the floor vote for 7 July, with the government's revised entry-into-force target 15
      August 2026. Substantive scope is unchanged (NCSC-NL supervisor, 24h/72h/1-month notification,
      fines to EUR 10M/2%, board liability, ~1,000→~8,000 in-scope entities).
    fields:
      - actions
      - evidence
      - sectors
      - sources
      - body
    merged_from: 2026-07-05/weekly-w27-netherlands-nis2-slip
  - at: "2026-07-12T23:52:00Z"
    run_id: 2026-07-12T2309Z-weekly
    type: update
    summary: >
      The Dutch First Chamber passed the Cyberbeveiligingswet (the NIS2 transposition) and the
      companion Wet weerbaarheid kritieke entiteiten (CER transposition) on 7 July 2026; both enter
      into force 15 August 2026. This closes the 'slipped past 1 July' status prior weeklies tracked
      and fixes a hard date. The Cbw covers ~8,000 organisations across 18 sectors with a duty of care
      including supply-chain risk management, mandatory incident reporting to the CSIRT,
      entity-register registration, and board-level accountability. For Swiss-domiciled organisations
      with Dutch subsidiaries, NL critical suppliers, or cross-border NIS2-equivalent reporting
      relationships, 15 August 2026 is now the operative compliance clock.
    fields:
      - evidence
      - sources
      - body
    merged_from: 2026-07-12/weekly-w28-netherlands-nis2-in-force
migrated_from: briefs/weekly/2026-W26.md
---

The Dutch transposition is in its final step: the Tweede Kamer (lower house) approved the Cyberbeveiligingswet on 15 April 2026 ([Rijksoverheid](https://www.rijksoverheid.nl/actueel/nieuws/2026/04/15/tweede-kamer-stemt-in-met-wetsvoorstellen-cyberbeveiligingswet-en-wet-weerbaarheid-kritieke-entiteiten)), with the Eerste Kamer (upper-house) ratification vote still pending in late June and the government targeting 1 July 2026 for entry into force. NCSC-NL is the designated supervisor; the regime runs a three-step 24h / 72h / one-month incident-notification protocol, essential-entity penalties up to €10M or 2% of turnover, and personal board liability for security-measure oversight ([NL Digital Government](https://www.nldigitalgovernment.nl/nis2-directive-cyberbeveiligingswet-cbw/)). This is the fresh delta on the W25 NIS2-transposition item, which listed the Netherlands as pending; France, Ireland, Luxembourg and Spain remain non-transposed. What changes for defenders: any essential/important entity with Dutch operations or Dutch counterparties is about to face an enforceable notification clock and a named supervisor — wire NCSC-NL's 24/72-hour flow into the incident-response runbook now, and re-check which group entities fall in scope.

## Update — 2026-07-05T23:42:00Z

The Dutch NIS2 transposition — the Cyberbeveiligingswet (Cbw) plus the companion Wet weerbaarheid kritieke entiteiten — has missed the 1 July 2026 entry-into-force target the prior weekly reported as the government's goal.

The Eerste Kamer (Senate) tabled its government response to the second committee report ("nota naar aanleiding van het tweede verslag") on 29 June 2026 — the last written-preparation step before plenary debate — and the Senate's own bill-tracking page now states the floor vote will take place on **7 July 2026**, noting the bill was adopted by the Tweede Kamer on 15 April 2026 ([Eerste Kamer, bill 36764](https://www.eerstekamer.nl/wetsvoorstel/36764_cyberbeveiligingswet)). iBestuur reports the government's revised entry-into-force target is now **15 August 2026**, roughly six weeks later than previously communicated ([iBestuur, 2026-07-01](https://ibestuur.nl/digitale-weerbaarheid/digitale-veiligheid/eerste-kamer-stemt-7-juli-over-cyberbeveiligingswet)).

The substantive scope is unchanged from prior coverage: NCSC-NL as designated supervisor, a three-step 24h/72h/one-month incident-notification protocol, essential-entity fines up to EUR 10M or 2% of global turnover, personal board liability for security-measure oversight, and an expansion of in-scope Dutch entities from roughly 1,000 to roughly 8,000. This is the fourth documented slip in the Dutch NIS2 timetable (originally targeted Q3 2025). **Defender takeaway:** the only action for a Swiss/EU reader is administrative — re-anchor readiness milestones and contractual compliance-date references onto 15 August 2026 for any Dutch group entities, hosting, or counterparties. No technical control change follows from the date shift itself.

## Update — 2026-07-12T23:52:00Z

The Dutch NIS2 transposition status this pipeline tracked as "slipped past its 1 July target, Senate vote set for 7 July" has resolved. On 7 July 2026 the Eerste Kamer (First Chamber) passed both the **Cyberbeveiligingswet** (Cbw, the NIS2 transposition) and the companion **Wet weerbaarheid kritieke entiteiten** (Wwke, the CER-directive transposition) — the Tweede Kamer had passed them on 15 April — and "de wetten treden op 15 augustus 2026 in werking" ("the laws enter into force on 15 August 2026") ([Rijksoverheid.nl, 2026-07-07](https://www.rijksoverheid.nl/actueel/nieuws/2026/07/07/cyberbeveiligingswet-en-wet-weerbaarheid-kritieke-entiteiten-vanaf-15-augustus-2026-van-kracht)). The parliamentary vote record confirms broad cross-party support ([Eerste Kamer, 2026-07-07](https://www.eerstekamer.nl/wetsvoorstel/36764_cyberbeveiligingswet)). The Cbw covers roughly 8,000 organisations across 18 designated essential/important sectors and imposes a cybersecurity duty of care (including supply-chain risk management), mandatory registration in the NCSC entity register, significant-incident reporting to the relevant CSIRT, and board-level accountability with director training ([NCSC-NL](https://www.ncsc.nl/nieuws/de-cyberbeveiligingswet-in-laatste-fase-van-vaststelling)).

**Why this matters to the constituency:** beyond direct applicability to any covered Dutch entity, this is a concrete datapoint for the deployment's standing EU NIS2-transposition watch — a member state moving from indefinite slip to a fixed enforcement date. For Swiss-domiciled organisations with Dutch subsidiaries, NL-incorporated critical suppliers, or cross-border NIS2-equivalent reporting relationships, 15 August 2026 is the operative clock, five weeks out from this brief. The next checkpoint is confirmation the NCSC-NL entity register is live and accepting registrations ahead of the date.
