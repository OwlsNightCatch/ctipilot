---
schema: 1
kind: incident
horizon: operational
title: "UN World Food Programme breach exposes IDs and locations of ~600,000 Gaza households"
headline: "UN World Food Programme breach exposes IDs and locations of ~600,000 Gaza households"
summary: "WFP confirmed on 2 June that unauthorised actors accessed its Palestine Self-Registration Application (breach dated 14 May), exposing names, national ID numbers, mobile numbers and location data for roughly 600,000 registered households — described as potentially the largest-ever breach of humanitarian beneficiary …"
discovered_at: "2026-06-04T05:00:02Z"
event_date: 2026-06-02
run_id: 2026-06-04-51b23ffa
priority: notable
immediate_action: null
tags:
  - data-breach
regions:
  - middle-east
sectors:
  - public-sector
entities: []
cves: []
sources:
  - url: "https://www.upguard.com/news/world-food-programme-data-breach-2026-06-02"
    publisher: UpGuard
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
migrated_from: briefs/2026-06-04.md
---

WFP confirmed on 2 June that unauthorised actors accessed its Palestine Self-Registration Application (breach dated 14 May), exposing names, national ID numbers, mobile numbers and location data for roughly 600,000 registered households — described as potentially the largest-ever breach of humanitarian beneficiary data ([UpGuard, 2026-06-02](https://www.upguard.com/news/world-food-programme-data-breach-2026-06-02)). No actor has claimed responsibility and the access vector is undisclosed.
**Why it matters to us:** distinct from a standard PII breach, the ID-plus-precise-location combination creates physical-safety risk for recipients in an active conflict zone — a reminder for Geneva-based international organisations and any agency running citizen-scale registration portals that aid/identity platforms need government-grade identity-system controls (MFA, dedicated monitoring, segmented backups).
