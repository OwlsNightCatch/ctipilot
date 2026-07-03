---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-long-running
title: "Screening Serpens / UNC1549 (Iran; Smoke Sandstorm / Nimbus Manticore) — AppDomainManager hijacking in six new RATs"
headline: "Screening Serpens / UNC1549 (Iran; Smoke Sandstorm / Nimbus Manticore) — AppDomainManager hijacking in six new RATs"
summary: Unit 42 detailed Screening Serpens using AppDomainManager hijacking to silently disable ETW and strong-name verification across six newly-documented RATs (daily 2026-05-23).
discovered_at: "2026-05-18T05:00:32Z"
event_date: 2026-05-23
run_id: 2026-W21-473d6fa5
priority: notable
immediate_action: null
tags:
  - nation-state
  - espionage
  - iran-nexus
regions:
  - middle-east
  - global
sectors:
  - defense
  - aviation
  - telco
entities: []
cves: []
sources:
  - url: "https://unit42.paloaltonetworks.com/tracking-iran-apt-screening-serpens/"
    publisher: Unit 42 — Screening Serpens
    role: primary
  - url: "https://www.cybersecuritydive.com/news/iran-cyberattacks-espionage-us-israel-uae/820990/"
    publisher: Cybersecurity Dive
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
migrated_from: briefs/weekly/2026-W21.md
---

Unit 42 detailed Screening Serpens using **AppDomainManager hijacking** to silently disable ETW and strong-name verification across six newly-documented RATs ([daily 2026-05-23](/briefs/2026-05-23/)). The ETW-blinding plus strong-name-check bypass is the detection-relevant tradecraft — it defeats both behavioural telemetry and signature-trust controls in one step. Where AppDomainManager-redirection is not required by an application, monitor for the `appDomainManagerAssembly` / `appDomainManagerType` config and environment-variable hijack vectors.
