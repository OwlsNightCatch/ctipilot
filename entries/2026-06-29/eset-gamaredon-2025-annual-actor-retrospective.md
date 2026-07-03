---
schema: 1
kind: annual-report
horizon: strategic
weekly_section: weekly-annual-reports
title: ESET Gamaredon 2025 — annual actor retrospective
headline: ESET Gamaredon 2025 — annual actor retrospective
summary: "Background. Gamaredon (FSB-linked, Russia-nexus) has been ESET's most-tracked Ukraine-focused operator for years; its prior annual papers documented a high-tempo, PowerShell-heavy toolset and aggressive infrastructure churn."
discovered_at: "2026-06-29T00:21:18Z"
event_date: null
run_id: 2026-W26-b78503e7
priority: notable
immediate_action: null
tags:
  - nation-state
  - espionage
  - russia-nexus
regions:
  - europe
sectors:
  - public-sector
  - defense
entities: []
cves: []
sources:
  - url: "https://www.welivesecurity.com/en/eset-research/gamaredon-2025-leveraging-tunnels-workers-dead-drops-new-alliances/"
    publisher: ESET WeLiveSecurity
    role: primary
  - url: "https://www.sekoia.com/blog/fsbs-matryoshka-3-3-gamaredons-gifts-that-keeps-unpacking-gammasteel"
    publisher: Sekoia
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
migrated_from: briefs/weekly/2026-W26.md
---

**Background.** Gamaredon (FSB-linked, Russia-nexus) has been ESET's most-tracked Ukraine-focused operator for years; its prior annual papers documented a high-tempo, PowerShell-heavy toolset and aggressive infrastructure churn.

ESET's [2025 Gamaredon paper](https://www.welivesecurity.com/en/eset-research/gamaredon-2025-leveraging-tunnels-workers-dead-drops-new-alliances/) (covered 06-26) documents six new PowerShell tools and the wholesale migration of exfiltration and C2 onto trusted cloud services, tunnels and "workers" — the horizon implication for European public-sector defenders is detection-oriented: Gamaredon-class C2 increasingly hides inside legitimate cloud-service traffic (Cloudflare workers, Telegram, dead-drop resolvers), so network-indicator blocking degrades and behavioural detection on the endpoint and on anomalous cloud-service egress becomes the durable control.
