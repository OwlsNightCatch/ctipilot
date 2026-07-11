---
schema: 1
kind: research
horizon: operational
title: macOS.Gaslight — a DPRK-aligned Rust backdoor that targets the LLM-assisted analyst
headline: macOS.Gaslight — a DPRK-aligned Rust backdoor that targets the LLM-assisted analyst
summary: "macOS.Gaslight — a DPRK-aligned Rust backdoor that aims its evasion at the analyst, not the sandbox — SentinelLABS documents a 3.5 KB blob of 38 fabricated \"system\" messages embedded to derail LLM-assisted triage, alongside Telegram Bot-API C2 and a com.apple.system.services.activity LaunchAgent (SentinelLABS, 2026-06-23)."
discovered_at: "2026-06-26T04:54:40Z"
event_date: 2026-06-24
run_id: 2026-06-26-6bbe4619
priority: high
immediate_action: null
tags:
  - nation-state
  - espionage
  - north-korea-nexus
  - infostealer
  - ai-abuse
  - identity
regions:
  - global
sectors:
  - technology
  - finance
entities:
  - "tool:macos-gaslight"
cves: []
sources:
  - url: "https://www.sentinelone.com/labs/macos-gaslight-rust-backdoor-turns-prompt-injection-on-the-analyst-not-the-sandbox/"
    publisher: SentinelLABS
    role: primary
  - url: "https://www.infosecurity-magazine.com/news/macos-gaslight-rust-backdoor/"
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
migrated_from: briefs/2026-06-26.md
---

SentinelLABS analysed macOS.Gaslight, a single-binary Rust implant it ties with high confidence to DPRK-aligned activity (Apple's XProtect detects it as `MACOS_BONZAI_COBUCH`, with a sibling sample caught by the AIRPIPE rule SentinelLABS also attributes to North Korea) ([SentinelLABS, 2026-06-23](https://www.sentinelone.com/labs/macos-gaslight-rust-backdoor-turns-prompt-injection-on-the-analyst-not-the-sandbox/)). Its novel evasion is aimed at the *analyst's tooling* rather than a sandbox: the binary carries a 3.5 KB Markdown-fenced blob of 38 fabricated "system" messages whose `{{DATA}}` tokens mimic an LLM triage harness's own prompt scaffold, designed to push an LLM agent into aborting, truncating, or refusing its analysis ([Infosecurity Magazine, 2026-06-24](https://www.infosecurity-magazine.com/news/macos-gaslight-rust-backdoor/)). Beyond that, it is a full stealer — staging a CPython interpreter at runtime to harvest Chrome/Brave/Firefox/Safari credentials, terminal history, `system_profiler` output, and a wholesale copy of `login.keychain-db`. C2 runs over the Telegram Bot-API `getUpdates` polling loop with AES-GCM payloads over certificate-pinned TLS; persistence is a LaunchAgent labelled `com.apple.system.services.activity` (`T1543.001`).

**Why it matters to us:** as LLM-assisted triage moves into SOC and MDR workflows, embedding adversarial prompt payloads in samples to corrupt that pipeline is a technique class to expect generalising — treat "benign" LLM verdicts on submitted macOS binaries as provisional pending human review, and flag any binary carrying large role/content message arrays for secondary analysis. Detection concepts: LaunchAgent plists masquerading under `com.apple.system.services.*` with non-Apple signers; processes spawning Python from non-standard parents; outbound TLS to `api.telegram.org` from non-user-initiated processes on managed Macs.
