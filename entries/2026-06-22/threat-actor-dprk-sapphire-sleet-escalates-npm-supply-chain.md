---
schema: 1
kind: research
horizon: strategic
weekly_section: weekly-research
title: "Threat actor: DPRK Sapphire Sleet escalates npm supply-chain attacks with the Mastra compromise"
headline: "Threat actor: DPRK Sapphire Sleet escalates npm supply-chain attacks with the Mastra compromise"
summary: "Microsoft attributed the Mastra npm scope compromise — first covered as an unattributed supply-chain event on 2026-06-18 — to Sapphire Sleet (BlueNoroff / UNC1069), making it the actor's second major npm strike of 2026 after the April Axios attack (Microsoft Security, 2026-06-17; BleepingComputer, 2026-06-18 …"
discovered_at: "2026-06-22T00:14:58Z"
event_date: 2026-06-18
run_id: 2026-W25-0aacfe65
priority: notable
immediate_action: null
tags:
  - supply-chain
  - nation-state
  - north-korea-nexus
  - infostealer
regions:
  - global
sectors:
  - technology
entities: []
cves: []
sources:
  - url: "https://www.microsoft.com/en-us/security/blog/2026/06/17/postinstall-payload-inside-mastra-npm-supply-chain-compromise/"
    publisher: Microsoft Security — Mastra
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/microsoft-links-mastra-ai-supply-chain-attack-to-north-korean-hackers/"
    publisher: BleepingComputer
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

Microsoft attributed the Mastra npm scope compromise — first covered as an unattributed supply-chain event on 2026-06-18 — to **Sapphire Sleet** (BlueNoroff / UNC1069), making it the actor's second major npm strike of 2026 after the April Axios attack ([Microsoft Security, 2026-06-17](https://www.microsoft.com/en-us/security/blog/2026/06/17/postinstall-payload-inside-mastra-npm-supply-chain-compromise/); [BleepingComputer, 2026-06-18](https://www.bleepingcomputer.com/news/security/microsoft-links-mastra-ai-supply-chain-attack-to-north-korean-hackers/); [daily 06-21](/briefs/2026-06-21/)). The operators compromised a maintainer account whose scope access was never revoked and published 140+ malicious `@mastra` packages within a ~20-minute window, using an `easy-day-js` typosquat of `dayjs` to run a `postinstall` dropper with cross-platform persistence (Registry Run key, macOS LaunchAgent, Linux systemd unit) that exfiltrated browser-wallet extensions, cloud credentials, LLM API keys, CI/CD tokens and SSH keys. The recurrence establishes a clear DPRK pattern of targeting the **AI developer toolchain's** supply chain specifically — the same surface § 6's first item flags. Run `npm install --ignore-scripts` in CI, pin lockfile versions, and rotate credentials on any host that pulled `@mastra` packages in the days before the 17 June disclosure.
