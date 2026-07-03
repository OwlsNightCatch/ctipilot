---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-long-running
title: "UAT-8302 (China-nexus, Talos; SE European government victims)"
headline: "UAT-8302 (China-nexus, Talos; SE European government victims)"
summary: "Current state: long-term gov-network access operations against South American government networks since late 2024 and southeastern European government agencies in 2025 — Talos disclosure published 2026-05-05 was the first detailed write-up."
discovered_at: "2026-05-04T05:00:32Z"
event_date: null
run_id: 2026-W19-a5788b22
priority: notable
immediate_action: null
tags:
  - nation-state
  - espionage
  - china-nexus
regions:
  - europe
  - global
sectors:
  - public-sector
entities:
  - "actor:uat-8302"
cves: []
sources:
  - url: "https://blog.talosintelligence.com/uat-8302/"
    publisher: Cisco Talos — UAT-8302
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
migrated_from: briefs/weekly/2026-W19.md
---

Current state: long-term gov-network access operations against South American government networks since late 2024 and southeastern European government agencies in 2025 — Talos disclosure published 2026-05-05 was the first detailed write-up. Tooling overlap links UAT-8302 to multiple Chinese-quartermaster-shared clusters (Ink Dragon, Earth Alux, Jewelbug, REF7707, LongNosedGoblin, Erudite Mogwai / Space Pirates). No new in-window developments beyond the original Talos disclosure (2026-05-05), and `state/covered_items.json` carries it as first-covered 2026-05-06. Outstanding defender question: whether southeastern European government victim list will expand publicly. Initial-access CVE not yet disclosed; Talos referenced post-compromise tooling (gogo scanner, Impacket, NetDraft/NosyDoor, CloudSorcerer v3.0, SNOWLIGHT/SNOWRUST, Deed RAT/Snappybee, Zingdoor, Draculoader, Stowaway, SoftEther VPN) rather than the entry vector.
