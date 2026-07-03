---
schema: 1
kind: annual-report
horizon: strategic
weekly_section: weekly-annual-reports
title: "ESET APT Activity Report Q4 2025–Q1 2026 — three state programmes converging on EU energy, defence and edge appliances"
headline: "ESET APT Activity Report Q4 2025–Q1 2026 — three state programmes converging on EU energy, defence and edge appliances"
summary: "ESET's APT Activity Report covering Q4 2025–Q1 2026 landed mid-window (first covered 2026-05-30)."
discovered_at: "2026-05-25T05:00:18Z"
event_date: 2026-05-30
run_id: 2026-W22-da77963d
priority: notable
immediate_action: null
tags:
  - nation-state
  - espionage
  - supply-chain
  - russia-nexus
  - north-korea-nexus
  - china-nexus
regions:
  - europe
  - global
sectors:
  - energy
  - defense
  - technology
entities:
  - "report:eset-apt-activity-report-q4-2025-q1-2026-sandworm-lazarus"
cves: []
sources:
  - url: "https://www.welivesecurity.com/en/eset-research/eset-apt-activity-report-q4-2025-q1-2026/"
    publisher: ESET WeLiveSecurity — APT Activity Report Q4 2025–Q1 2026
    role: primary
  - url: "https://www.infosecurity-magazine.com/news/chinese-hackers-exploit-iran-war/"
    publisher: Infosecurity Magazine
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
migrated_from: briefs/weekly/2026-W22.md
---

ESET's APT Activity Report covering Q4 2025–Q1 2026 landed mid-window ([first covered 2026-05-30](/briefs/2026-05-30/)). The daily recapped the headline findings — a rare out-of-Ukraine Sandworm destructive incident (a medium-confidence December 2025 attack on a single Polish energy company), Lazarus targeting the EU drone/defence sector, and UNC5221 pivoting to the Ivanti SPAWN toolset. The synthesis a daily reader could not see from those three bullets is that they are the *same story told by three different state programmes*: Russia-, North-Korea- and China-nexus operators are independently converging on (a) European energy and **defence-industrial-base supply chains** as the target set — Sandworm's move against a Polish energy target being notable precisely because the operator rarely acts destructively outside Ukraine — and (b) **internet-facing edge appliances** (Ivanti) as the entry vector. For a Swiss / European public-sector SOC the implication is a prioritisation argument rather than a new IOC list: edge-appliance patch SLAs and defence-supplier third-party-risk review are where all three programmes are applying pressure simultaneously, so they should outrank generic campaign awareness in the next planning cycle. The report reinforces, with cross-actor telemetry, the structural shift the W21 Verizon DBIR and Rapid7 reports flagged — exploitation of exposed software as the dominant access vector.
