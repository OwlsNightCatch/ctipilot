---
schema: 1
kind: research
horizon: strategic
weekly_section: weekly-research
title: "Threat actor: INC ransomware's Rust rewrite and BYOVD evolution"
headline: "Threat actor: INC ransomware's Rust rewrite and BYOVD evolution"
summary: "Acronis and The Hacker News documented the evolution of INC ransomware into a top-tier RaaS — 830+ victims since 2023, fourth in Q1 2026 — with a Rust rewrite of its Windows and Linux/ESXi encryptors, BYOVD EDR-termination using the drivers filwfp.sys / filnk.sys / fildds.sys (the same set seen in earlier …"
discovered_at: "2026-06-22T00:15:00Z"
event_date: 2026-06-19
run_id: 2026-W25-0aacfe65
priority: notable
immediate_action: null
tags:
  - ransomware
  - organized-crime
regions:
  - global
  - us
sectors:
  - healthcare
entities:
  - "actor:inc-ransom"
cves: []
sources:
  - url: "https://www.acronis.com/en/tru/posts/from-emerging-threat-to-top-tier-ransomware-as-a-service-the-evolution-of-inc-ransomware/"
    publisher: Acronis TRU
    role: primary
  - url: "https://thehackernews.com/2026/06/inc-ransomware-claims-830-victims-since.html"
    publisher: The Hacker News
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
migrated_from: briefs/weekly/2026-W25.md
---

Acronis and The Hacker News documented the evolution of **INC ransomware** into a top-tier RaaS — 830+ victims since 2023, fourth in Q1 2026 — with a Rust rewrite of its Windows and Linux/ESXi encryptors, BYOVD EDR-termination using the drivers `filwfp.sys` / `filnk.sys` / `fildds.sys` (the same set seen in earlier Vanilla Tempest campaigns), a Veeam credential dumper for backup infrastructure, and two source-code-leak-derived variants (Lynx, Sinobi) ([Acronis TRU, 2026-06-18](https://www.acronis.com/en/tru/posts/from-emerging-threat-to-top-tier-ransomware-as-a-service-the-evolution-of-inc-ransomware/); [The Hacker News, 2026-06-19](https://thehackernews.com/2026/06/inc-ransomware-claims-830-victims-since.html)). The geography is incidental for a CH/EU SOC — the cited reporting puts the majority of INC's victims in the US — but the tradecraft is not: the three BYOVD drivers (shared with earlier Vanilla Tempest campaigns), the Veeam backup-credential dumper, and the cross-platform Rust encryptor are detection content that generalises to any victim. Detect the three BYOVD drivers via driver-load events with a hash blocklist, alert on Veeam process-memory access from unexpected parents, and keep backup systems MFA-protected and network-isolated.
