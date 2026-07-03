---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-long-running
title: VerdantBamboo / UNC5221 / WARP PANDA — 18-month undetected China-nexus intrusion through MSP pfSense
headline: VerdantBamboo / UNC5221 / WARP PANDA — 18-month undetected China-nexus intrusion through MSP pfSense
summary: "VerdantBamboo (UNC5221 / WARP PANDA): 18-month undetected China-nexus espionage through an MSP's pfSense, living on EDR-blind edge appliances and proxying into M365 past Conditional Access. (daily, Volexity)"
discovered_at: "2026-06-01T05:00:18Z"
event_date: 2026-06-05
run_id: 2026-W23-9118e7bd
priority: high
immediate_action: null
tags:
  - nation-state
  - espionage
  - supply-chain
  - china-nexus
regions:
  - europe
sectors:
  - public-sector
  - technology
entities: []
cves: []
sources:
  - url: "https://www.volexity.com/blog/2026/06/04/verdantbamboo-just-another-brickstorm-in-the-firewall/"
    publisher: "Volexity, 2026-06-04"
    role: primary
closed_sources: []
evidence: []
verification: single-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/weekly/2026-W23.md
---

First disclosed this week by Volexity's incident-response case ([Volexity, 2026-06-04](https://www.volexity.com/blog/2026/06/04/verdantbamboo-just-another-brickstorm-in-the-firewall/); [daily 2026-06-05](/briefs/2026-06-05/)). VerdantBamboo — assessed with high confidence as UNC5221 (WARP PANDA) — entered a European organisation through its MSP's pfSense firewall with a BSD build of the BRICKSTORM Golang backdoor, then persisted across three appliances (pfSense, Synology NAS, Egnyte Storage Sync VM) that cannot run EDR by design. The M365 Conditional Access bypass — routing authentication through the Egnyte appliance's trusted egress IP — is the novel operational technique. Two previously undocumented implants: AGENTPSD (PyInstaller Python HTTPS reverse shell) and PLENET/GRIMBOLT (.NET Native AOT on Linux NAS). Outstanding question: Volexity found access dating at least 18 months back, raising the question of what else the actor collected during that window and whether the MSP has other affected European clients. The disclosure is Volexity primary IR only — no second corroborating source is available. `[SINGLE-SOURCE]`
