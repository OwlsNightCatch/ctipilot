---
schema: 1
kind: research
horizon: operational
title: "Wiz CIRT names JINX-0164 — LinkedIn-recruiter lures, AUDIOFIX macOS infostealer, MINIRAT npm pivot into CI/CD"
headline: "Wiz CIRT names JINX-0164 — LinkedIn-recruiter lures, AUDIOFIX macOS infostealer, MINIRAT npm pivot into CI/CD"
summary: "Wiz CIRT identified and named JINX-0164 on 2026-05-27, a financially motivated cluster active since mid-2025 against cryptocurrency organisations."
discovered_at: "2026-05-29T05:00:12Z"
event_date: 2026-05-27
run_id: 2026-05-29-c7f56b00
priority: notable
immediate_action: null
tags:
  - organized-crime
  - espionage
  - supply-chain
  - identity
  - mobile
  - cloud
regions:
  - global
  - europe
  - switzerland
sectors:
  - finance
  - technology
entities:
  - "campaign:jinx-0164-crypto-firms-linkedin-audiofix-minirat"
cves: []
sources:
  - url: "https://www.wiz.io/blog/threat-actors-target-crypto-orgs"
    publisher: Wiz Research — JINX-0164
    role: primary
  - url: "https://thehackernews.com/2026/05/jinx-0164-targets-cryptocurrency-firms.html"
    publisher: "The Hacker News, 2026-05-28"
    role: corroborating
closed_sources: []
evidence:
  - quote: "JINX-0164 uses LinkedIn social engineering, custom macOS malware, and CI/CD hijacking to target crypto organizations"
    publisher: Wiz Research
  - quote: "JINX-0164 also distributes MiniRAT, a Go-based backdoor previously delivered via a compromised npm package (@velora-dex/sdk), enabling arbitrary command execution and payload retrieval on macOS systems"
    publisher: The Hacker News
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
migrated_from: briefs/2026-05-29.md
---

Wiz CIRT [identified and named JINX-0164 on 2026-05-27](https://www.wiz.io/blog/threat-actors-target-crypto-orgs), a financially motivated cluster active since mid-2025 against cryptocurrency organisations. Initial access is LinkedIn-based social engineering — fake recruiter personas direct targets to fraudulent video-conferencing platforms that deliver **AUDIOFIX**, a compiled-Python macOS binary functioning as both infostealer and backdoor. AUDIOFIX harvests Keychain contents, Chrome / Firefox / Safari credentials, SSH keys, AWS / GCP / Azure cloud-provider credentials, and credentials from 51 cryptocurrency-wallet browser extensions; persistence is a `LaunchAgent` plist under `~/Library/LaunchAgents`. From the endpoint, JINX-0164 pivots into CI/CD infrastructure using stolen developer credentials and injects poisoned commits under legitimate developer identities; any team member building from the affected branches receives **MINIRAT**, a lightweight Go-based backdoor. The supply-chain escalation materialised through the `@velora-dex/sdk` npm package version 4.9.1 (trojanised 2026-04-07), which staged MINIRAT via LaunchCtl persistence. Wiz notes TTP overlap with prior DPRK-adjacent tradecraft (UNC1069, Sapphire Sleet) but stops short of formal attribution. The [Hacker News writeup](https://thehackernews.com/2026/05/jinx-0164-targets-cryptocurrency-firms.html) corroborates with additional MINIRAT detail. Mapped to T1566.003 (Spearphishing via Service: LinkedIn), T1543.001 (Launch Agent), T1555 (Credentials from Password Stores), T1195.002 (Compromise Software Supply Chain) and T1098.005 (Device Registration). For Swiss / EU SOCs the relevant exposure is *Crypto Valley* and any organisation whose developers build from npm dependencies that fan out to internal CI/CD — Sigstore signature verification, lock-file pinning of `@velora-dex/sdk`, and CI runner least-privilege are the operational asks.
