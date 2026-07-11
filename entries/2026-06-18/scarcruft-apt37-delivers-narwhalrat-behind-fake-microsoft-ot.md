---
schema: 1
kind: threat
horizon: operational
title: "ScarCruft (APT37) delivers NarwhalRAT behind fake Microsoft OTP \"security alert\" lures"
headline: "ScarCruft (APT37) delivers NarwhalRAT behind fake Microsoft OTP \"security alert\" lures"
summary: "ScarCruft (APT37) deploys NarwhalRAT behind fake Microsoft OTP alerts; China arrests 67 Silver Fox/ValleyRAT operators. North Korean spearphishing impersonating Microsoft MFA notices delivers a compiled-Python RAT with a pCloud dead-drop resolver (Genians, 2026-06-16); separately, Chinese police dismantled the supply chain behind the Winos/ValleyRAT operator network."
discovered_at: "2026-06-18T05:10:29Z"
event_date: 2026-06-17
run_id: 2026-06-18-aa7ee817
priority: high
immediate_action: null
tags:
  - nation-state
  - espionage
  - phishing
  - north-korea-nexus
regions:
  - apac
  - europe
sectors:
  - public-sector
  - defense
entities:
  - "actor:scarcruft"
cves: []
sources:
  - url: "https://www.genians.co.kr/en/blog/threat_intelligence/narwhalrat"
    publisher: Genians Security Center
    role: primary
  - url: "https://thehackernews.com/2026/06/fake-microsoft-alerts-used-to-deploy.html"
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

Genians Security Center attributed a new campaign to ScarCruft / APT37 (North Korea nexus) deploying a previously-undocumented RAT it calls NarwhalRAT ([Genians, 2026-06-16](https://www.genians.co.kr/en/blog/threat_intelligence/narwhalrat)). The lure is a spearphishing email impersonating a Microsoft multi-factor authentication / OTP security alert; the attached ZIP carries a Windows shortcut (LNK) that launches PowerShell with `-ExecutionPolicy Bypass` to pull a batch loader, which establishes persistence via a scheduled task running on a one-minute interval (`T1053.005`). The payload is a compiled-Python binary loading obfuscated bytecode and providing keylogging (`T1056.001`), screenshot and audio capture, USB collection and remote command execution; C2 resilience comes from a pCloud dead-drop resolver (`T1102.001`) that hands out current relay addresses, defeating static domain/IP blocking ([The Hacker News, 2026-06-17](https://thehackernews.com/2026/06/fake-microsoft-alerts-used-to-deploy.html)).

**Why it matters to us:** APT37 targets government, diplomatic, policy-research and Korean-diaspora organisations, including in Europe. The behavioural chain is hunt-friendly without IOCs: alert on `schtasks.exe` creating tasks under an unusual `Microsoft…`-style name from a non-installer parent, on LNK→PowerShell `-ExecutionPolicy Bypass` execution trees, and on compiled-Python process images making outbound calls to consumer cloud-storage APIs. Treat the cloud dead-drop pattern as the durable detection surface — blocking one relay does not break C2.
