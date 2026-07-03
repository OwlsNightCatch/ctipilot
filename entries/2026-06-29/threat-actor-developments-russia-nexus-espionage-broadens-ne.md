---
schema: 1
kind: research
horizon: strategic
weekly_section: weekly-research
title: "Threat-actor developments: Russia-nexus espionage broadens; new China-nexus and DPRK clusters"
headline: "Threat-actor developments: Russia-nexus espionage broadens; new China-nexus and DPRK clusters"
summary: "Turla's new STOCKSTAY backdoor (GTIG) broadens Russia-nexus espionage toward Western-European foreign-policy targets — delivered via WinRAR CVE-2025-8088 and malicious RDP files; relevant to Swiss/EU governmental entities with Ukraine-adjacent policy work. (daily 06-26, Google GTIG)"
discovered_at: "2026-06-29T00:21:15Z"
event_date: null
run_id: 2026-W26-b78503e7
priority: high
immediate_action: null
tags:
  - nation-state
  - espionage
  - russia-nexus
  - china-nexus
  - north-korea-nexus
regions:
  - europe
  - switzerland
  - apac
  - global
sectors:
  - public-sector
  - defense
entities:
  - "tool:macos-gaslight"
  - "campaign:sentinelone-living-off-the-pipeline-2026"
cves: []
sources:
  - url: "https://cloud.google.com/blog/topics/threat-intelligence/stockstay-turla-intelligence-gathering"
    publisher: Google GTIG — STOCKSTAY
    role: primary
  - url: "https://www.ic3.gov/PSA/2026/PSA260626"
    publisher: FBI IC3 PSA I-062626-PSA
    role: corroborating
  - url: "https://unit42.paloaltonetworks.com/cl-sta-1062-tinyrct-backdoor/"
    publisher: Unit 42 — CL-STA-1062
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

The most significant new actor finding the dailies did not carry is Turla's **STOCKSTAY** — Google GTIG [characterised](https://cloud.google.com/blog/topics/threat-intelligence/stockstay-turla-intelligence-gathering) a multi-component .NET/Windows Forms backdoor that communicates C2 over secure WebSocket and shares significant code overlap with Kazuar (Turla's staple implant since 2017). Delivery used malicious RDP files by phishing and, as recently as November 2025, RAR archives exploiting WinRAR's CVE-2025-8088 (a flaw also abused by Sandworm, Gamaredon and RomCom). Current targeting is Ukrainian government and military, but earlier victims had Italian, Dutch, Polish and German foreign-policy interest — a direct read-across for Swiss federal and European governmental entities with Ukraine-adjacent policy work ([The Hacker News](https://thehackernews.com/2026/06/google-details-turlas-new-stockstay.html)). This sits alongside the week's other Russia-nexus signal: FBI/CISA escalated their warning that Russian intelligence (tracked as UNC5792) is now [phishing Signal Backup Recovery Keys](https://www.ic3.gov/PSA/2026/PSA260626) for persistent account takeover, and ESET's Gamaredon retrospective (§ 7) shows the FSB-linked group moving exfil and C2 wholesale onto trusted cloud services.

Two non-Russian clusters round out the picture. Unit 42 documented **CL-STA-1062**, a Chinese-speaking cluster (overlapping Talos's UAT-7237) deploying the new TinyRCT .NET backdoor via AppDomainManager injection against Southeast-Asian government and state-owned energy targets ([Unit 42](https://unit42.paloaltonetworks.com/cl-sta-1062-tinyrct-backdoor/)); Kaspersky GReAT analysed the **StrikeShark** cluster's SharkLoader deploying Cobalt Strike via "Perfect DLL Hijacking" against government targets ([Securelist](https://securelist.com/strikeshark-campaign/120326/)). And SentinelLABS' **macOS.Gaslight**, a DPRK-aligned Rust backdoor, notably turns prompt injection on the LLM-assisted analyst rather than the sandbox ([SentinelLABS](https://www.sentinelone.com/labs/macos-gaslight-rust-backdoor-turns-prompt-injection-on-the-analyst-not-the-sandbox/)) — an early instance of tradecraft built specifically to poison AI-assisted triage. Attribute the claim to the research outfit, not the state, where the source itself hedges.
