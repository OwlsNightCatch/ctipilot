---
schema: 1
kind: annual-report
horizon: strategic
weekly_section: weekly-annual-reports
title: "Two independent Q2 2026 ransomware reports published three days apart agree the ecosystem is fragmenting without de-concentrating — and the industrial one carries a negative finding OT operators should plan against: no Q2 case reached control-system manipulation"
headline: "Dragos and Check Point both counted Q2: 93 active groups against a 57.6% top-ten share, and zero incidents reaching ICS Stage 2"
summary: >
  Dragos published its Industrial Ransomware Analysis for Q2 2026 on 10 August and Check Point Research
  published The State of Ransomware Q2 2026 on 13 August. From different vantage points — industrial-sector
  incidents and all leak-site victims — they describe the same structure. Dragos identified 1,140 ransomware
  incidents affecting industrial organisations, a 12% increase over Q1's 1,020, with manufacturing the most
  affected sector at 747 incidents or 65%, the United States the most impacted country at 431 incidents or
  38%, and Germany the country with the greatest quarter-over-quarter increase, from 37 incidents to 68.
  Check Point counted 2,139 data-leak-site victims, essentially flat quarter over quarter and up 33% year
  over year, with the top ten groups' share falling from 71% to 57.6% while the number of active groups
  climbed from 71 to 93. The finding with the most direct planning consequence is Dragos's negative one:
  it observed no case in Q2 in which a ransomware operator reached Stage 2 of the ICS Cyber Kill Chain or
  directly manipulated a control system — every operational disruption followed compromise of enterprise
  and virtualisation systems instead.
discovered_at: "2026-08-16T23:59:00Z"
event_date: "2026-08-13"
run_id: 2026-08-16T2315Z-weekly
priority: notable
immediate_action: null
tags: [ransomware, organized-crime, ot-ics, data-breach]
regions: [europe, dach, global]
sectors: [energy, water, transport, healthcare, public-sector, manufacturing]
entities:
  - report:dragos-industrial-ransomware-q2-2026
  - report:checkpoint-state-of-ransomware-q2-2026
  - actor:qilin
  - actor:akira
  - campaign:the-gentlemen-ransomware-storm2697
  - actor:krybit
techniques: [T1486, T1490, T1078, T1133, T1567.002]
affected_products: []
cves: []
sources:
  - url: "https://www.dragos.com/blog/dragos-industrial-ransomware-analysis-q2-2026"
    publisher: "Dragos"
    date: "2026-08-10"
    role: primary
  - url: "https://research.checkpoint.com/2026/the-state-of-ransomware-q2-2026/"
    publisher: "Check Point Research"
    date: "2026-08-13"
    role: primary
closed_sources: []
evidence:
  - quote: "Dragos identified 1,140 ransomware incidents affecting industrial organizations in Q2 2026, an 12% increase over the 1,020 recorded in Q1."
    publisher: "Dragos"
  - quote: "Dragos observed no case in Q2 2026 in which a ransomware operator reached Stage 2 of the ICS Cyber Kill Chain or directly manipulated a control system; where operational disruption occurred, it followed encryption or precautionary shutdown of the enterprise and virtualization systems on which OT depends."
    publisher: "Dragos"
  - quote: "However, the country with the greatest increase from Q1 (37 incidents) to Q2 (68 incidents) was Germany."
    publisher: "Dragos"
  - quote: "The top 10 groups accounted for 57.6% of all victims, down from 71% in Q1, while the number of active groups climbed from 71 to 93, a new high for the period tracked in this report."
    publisher: "Check Point Research"
  - quote: "The exploitation window kept narrowing, with AI increasingly cited as the accelerant."
    publisher: "Check Point Research"
verification: multi-source
sourcing_note: >
  Two independent quarterly reports, each read in full this run and each the primary source for its own
  figures; no figure is attributed to both. The two count different populations — Dragos counts incidents
  affecting industrial organisations, Check Point counts data-leak-site victims across all sectors — so
  their totals are not comparable and are not compared here. Both are vendor telemetry derived largely from
  leak-site postings, which under-counts victims who pay or who are never listed; the convergence claimed
  is structural rather than numerical.
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions: []
migrated_from: null
---

Two quarterly ransomware reports landed three days apart this week, counting different populations from different vantage points, and arriving at compatible descriptions of the same structural shift. Taken together they are the closest thing to an outside check on what the operational entries of the last quarter have shown one incident at a time.

Dragos's Industrial Ransomware Analysis for Q2 2026 counts incidents affecting industrial organisations: "Dragos identified 1,140 ransomware incidents affecting industrial organizations in Q2 2026, an 12% increase over the 1,020 recorded in Q1," with manufacturing the most affected sector at 747 incidents or 65%, and engineering firms, system integrators and equipment manufacturers second at 117 — a distribution that puts the industrial supply chain, not the plant, at the centre. The regional detail is where it becomes a European planning input rather than a US one: the United States remains the most impacted country by a wide margin at 431 incidents or 38% of the total, but "the country with the greatest increase from Q1 (37 incidents) to Q2 (68 incidents) was Germany" ([Dragos, 2026-08-10](https://www.dragos.com/blog/dragos-industrial-ransomware-analysis-q2-2026)) — an eighty-four per cent rise in a neighbouring jurisdiction whose industrial base overlaps heavily with the Swiss one.

Check Point Research's State of Ransomware Q2 2026 counts leak-site victims across all sectors and describes the ecosystem's shape: "The top 10 groups accounted for 57.6% of all victims, down from 71% in Q1, while the number of active groups climbed from 71 to 93, a new high for the period tracked in this report," against a total of 2,139 victims that was essentially flat quarter over quarter and up 33% year over year. Qilin remained the most prolific operator for a fourth straight quarter with 279 victims despite its own count falling 17%, while The Gentlemen surged 62% to 269 and briefly outpaced it; the US share of victims fell from 50% to 42%, which Check Point attributes to the fastest-growing groups — The Gentlemen and the newly active Krybit — targeting the US less often than the ecosystem average ([Check Point Research, 2026-08-13](https://research.checkpoint.com/2026/the-state-of-ransomware-q2-2026/)). That last point is the one European defenders should read twice: a falling US share in a flat total is not a reduction in activity, it is a redistribution toward everyone else. Check Point also records, independently of this pipeline's own observations this week, that "The exploitation window kept narrowing, with AI increasingly cited as the accelerant."

The single most consequential finding in either report is a negative one, and it belongs to Dragos: "Dragos observed no case in Q2 2026 in which a ransomware operator reached Stage 2 of the ICS Cyber Kill Chain or directly manipulated a control system; where operational disruption occurred, it followed encryption or precautionary shutdown of the enterprise and virtualization systems on which OT depends."

**Defender takeaway:** for an operator of critical infrastructure that finding settles a resourcing argument in a specific direction for this quarter. Ransomware reached operational technology repeatedly, but it reached it *through* the enterprise and virtualisation estate every time, and never by acquiring control-system tradecraft — so the marginal defensive spend that reduces OT disruption risk from ransomware is IT-side segmentation, hypervisor and backup hardening, and the discipline of ensuring a precautionary shutdown is a decision rather than a consequence. That is not an argument for neglecting OT-specific detection, which addresses a different adversary class this pipeline covered directly this week; it is an argument about which of the two currently drives ransomware-caused outages. The fragmentation finding carries a second, quieter implication: with 93 active groups and the top ten's share falling, defensive planning keyed to the named tactics of a handful of large brands covers a shrinking fraction of the field, and the durable investment is in the initial-access and impact behaviours all of them share rather than in per-group playbooks. Neither report names a Swiss victim or incident. Per this pipeline's standing practice, these two reports are now registered entities and will be referenced rather than re-summarised in later coverage.
