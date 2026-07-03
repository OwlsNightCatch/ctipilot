---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-long-running
title: Midnight Blizzard and others operationalise ROADtools for Entra ID abuse
headline: Midnight Blizzard and others operationalise ROADtools for Entra ID abuse
summary: "An unusually active espionage week — Webworm pivoted to EU government targets (Graph/OneDrive C2), Midnight Blizzard and others operationalised ROADtools against Entra ID, and Iran's Screening Serpens used AppDomainManager hijacking to blind ETW. (daily 2026-05-21; daily 2026-05-23)"
discovered_at: "2026-05-18T05:00:31Z"
event_date: 2026-05-23
run_id: 2026-W21-473d6fa5
priority: high
immediate_action: null
tags:
  - nation-state
  - espionage
  - identity
  - cloud
  - russia-nexus
  - iran-nexus
regions:
  - global
  - europe
sectors:
  - public-sector
  - defense
  - technology
entities: []
cves: []
sources:
  - url: "https://unit42.paloaltonetworks.com/roadtools-cloud-attacks/"
    publisher: Unit 42 — ROADtools cloud attacks
    role: primary
  - url: "https://www.volexity.com/blog/2025/04/22/phishing-for-codes-russian-threat-actors-target-microsoft-365-oauth-workflows/"
    publisher: Volexity — OAuth device-code background
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

Unit 42 documented systematic nation-state operationalisation of the open-source **ROADtools** Entra ID framework by Midnight Blizzard, Curious Serpens and UTA0355 for device registration, token theft and tenant enumeration ([daily 2026-05-23](/briefs/2026-05-23/)). This is the most broadly relevant item in the section — every M365/Entra tenant is in scope. Hunt for unexpected device-registration events, anomalous service-principal token requests, and ROADtools-characteristic enumeration patterns; tighten conditional-access on device-registration and review legacy-auth exposure.
