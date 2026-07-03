---
schema: 1
kind: threat
horizon: operational
title: "Nimbus Manticore (UNC1549 / Screening Serpens) — Check Point details MiniFast backdoor, Zoom-task hijacking and SEO-poisoning delivery"
headline: "Nimbus Manticore (UNC1549 / Screening Serpens) — Check Point details MiniFast backdoor, Zoom-task hijacking and SEO-poisoning delivery"
summary: "UPDATE (originally covered 2026-05-23): Following Unit 42's coverage of UNC1549 / Screening Serpens AppDomainManager hijacking, Check Point Research (published 2026-05-22, widely re-reported this week) adds material technical depth on three February–April 2026 campaign waves keyed to Operation Epic Fury (Check …"
discovered_at: "2026-05-27T05:00:04Z"
event_date: 2026-05-26
run_id: 2026-05-27-0b6f12dd
priority: notable
immediate_action: null
tags:
  - nation-state
  - espionage
  - iran-nexus
regions:
  - europe
  - middle-east
  - us
sectors:
  - aviation
  - defense
  - telco
entities:
  - "campaign:tds-security-tool-impersonation-checkpoint"
cves: []
sources:
  - url: "https://research.checkpoint.com/2026/fast-and-furious-nimbus-manticore-operations-during-the-iranian-conflict/"
    publisher: "Check Point Research, 2026-05-22"
    role: primary
  - url: "https://thehackernews.com/2026/05/iranian-hackers-deploy-minifast-and.html"
    publisher: "The Hacker News, 2026-05-26"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: 2026-05-23/unit-42-iran-s-screening-serpens-unc1549-smoke-sandstorm-nim
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-27.md
---

**UPDATE (originally covered 2026-05-23):** Following Unit 42's coverage of UNC1549 / Screening Serpens AppDomainManager hijacking, Check Point Research (published 2026-05-22, widely re-reported this week) adds material technical depth on three February–April 2026 campaign waves keyed to Operation Epic Fury ([Check Point Research, 2026-05-22](https://research.checkpoint.com/2026/fast-and-furious-nimbus-manticore-operations-during-the-iranian-conflict/); [The Hacker News, 2026-05-26](https://thehackernews.com/2026/05/iranian-hackers-deploy-minifast-and.html)). The IRGC-affiliated actor replaced its MiniJunk family with a new backdoor, MiniFast — a 64-bit DLL with a single `CheckForUpdates` export and a JSON HTTP C2 using API-style endpoints (`/agent/init`, `/agent/poll`, `/upload/`) and a 14-opcode command set including DLL injection, UAC elevation and scheduled-task persistence.

Two persistence/delivery techniques are new versus the prior coverage: (1) **Zoom scheduled-task hijacking** (`T1053.005`) — instead of creating a suspicious new task, the malware watches for the legitimate `ZoomUpdateTaskUser-<SID>` task and hijacks it; (2) **SEO poisoning** (`T1598.003`) via a fake SQL Developer download domain ranked on Bing/DuckDuckGo, alongside `T1574.008` AppDomain hijacking via redirected `.config` files. The loader chain validates `parent=svchost.exe` before proceeding and abused two SSL.com-issued code-signing certificates ([Check Point Research, 2026-05-22](https://research.checkpoint.com/2026/fast-and-furious-nimbus-manticore-operations-during-the-iranian-conflict/)). Hunt for `ZoomUpdateTaskUser-*` task modifications by non-Zoom processes, non-default `AppDomainManager` values in .NET `.config` files, and execution from user-writable AppData paths.
