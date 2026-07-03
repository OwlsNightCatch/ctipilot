---
schema: 1
kind: research
horizon: operational
title: Crypto clipboard-hijacker campaign weaponises VirusTotal community reputation to suppress detection
headline: Crypto clipboard-hijacker campaign weaponises VirusTotal community reputation to suppress detection
summary: "Check Point Research detailed a Rust-based clipboard-hijacker campaign against cryptocurrency users whose distinguishing feature is the systematic manipulation of security-tool reputation signals (Check Point Research, 2026-06-17)."
discovered_at: "2026-06-18T05:10:35Z"
event_date: 2026-06-17
run_id: 2026-06-18-aa7ee817
priority: notable
immediate_action: null
tags:
  - cryptocrime
  - organized-crime
  - phishing
regions:
  - global
sectors:
  - finance
  - technology
entities:
  - "campaign:tds-security-tool-impersonation-checkpoint"
cves: []
sources:
  - url: "https://research.checkpoint.com/2026/from-stars-to-upvotes-fake-reputation-fueling-a-crypto-clipboard-hijacker/"
    publisher: Check Point Research
    role: primary
  - url: "https://thehackernews.com/2026/06/crypto-clipper-campaign-abuses-fake.html"
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
migrated_from: briefs/2026-06-18.md
---

Check Point Research detailed a Rust-based clipboard-hijacker campaign against cryptocurrency users whose distinguishing feature is the systematic manipulation of security-tool reputation signals ([Check Point Research, 2026-06-17](https://research.checkpoint.com/2026/from-stars-to-upvotes-fake-reputation-fueling-a-crypto-clipboard-hijacker/)). The operator runs a network of GitHub ghost accounts, SourceForge pages with inflated download counts, AI-narrated YouTube channels and Telegram channels advertising fake crypto "edge" tools (Solana/Pump.fun sniper bots, Aviator predictors), funnelling victims through a WordPress phishing site to download the Rust payloads for Windows and macOS. Critically, the actor submits fake benign community votes and comments on VirusTotal to lower the apparent threat score, so triage analysts relying on community reputation see the sample as pre-vetted. The payload watches the clipboard for wallet-address patterns and silently substitutes attacker addresses. The operational takeaway for SOC triage: **VirusTotal community votes/comments are not a trust signal** for this malware class — weight first-party engine verdicts and behaviour, and add clipboard-modification (`T1115`) hooks plus Rust binaries executing from user Downloads/Temp without code-signing to hunt hypotheses.
