---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-long-running
title: "Webworm (China-aligned; FishMonger / Aquatic Panda) — pivots to EU government targets"
headline: "Webworm (China-aligned; FishMonger / Aquatic Panda) — pivots to EU government targets"
summary: "ESET documented Webworm's 2025–2026 pivot to European government victims (Belgian, Italian, Serbian, Polish and Spanish governmental organisations), deploying EchoCreep (Discord-based C2) and GraphWorm (Microsoft Graph / OneDrive C2) backdoors (daily 2026-05-21)."
discovered_at: "2026-05-18T05:00:29Z"
event_date: 2026-05-21
run_id: 2026-W21-473d6fa5
priority: notable
immediate_action: null
tags:
  - nation-state
  - espionage
  - identity
  - cloud
  - china-nexus
regions:
  - europe
sectors:
  - public-sector
  - education
entities: []
cves: []
sources:
  - url: "https://www.welivesecurity.com/en/eset-research/webworm-new-burrowing-techniques/"
    publisher: ESET WeLiveSecurity — Webworm
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
migrated_from: briefs/weekly/2026-W21.md
---

ESET documented Webworm's 2025–2026 pivot to European government victims (Belgian, Italian, Serbian, Polish and Spanish governmental organisations), deploying **EchoCreep** (Discord-based C2) and **GraphWorm** (Microsoft Graph / OneDrive C2) backdoors ([daily 2026-05-21](/briefs/2026-05-21/)). The use of Graph/OneDrive as C2 is the defender-relevant shift — it blends with legitimate M365 traffic. Hunt for anomalous Graph API usage patterns and Discord egress from server subnets that have no business reason to reach either.
