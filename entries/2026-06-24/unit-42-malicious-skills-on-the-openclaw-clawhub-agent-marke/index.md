---
schema: 1
kind: research
title: "Unit 42: malicious skills on the OpenClaw \"ClawHub\" agent marketplace deliver macOS infostealers and weaponise AI agents for financial fraud"
headline: "Unit 42: malicious skills on the OpenClaw \"ClawHub\" agent marketplace deliver macOS infostealers and weaponise AI agents for financial fraud"
summary: "Palo Alto Networks Unit 42 (2026-06-23) documented five malicious skills published to ClawHub, the third-party skill marketplace for the OpenClaw AI-agent platform, active February–May 2026 (Unit 42, 2026-06-23; corroborated by Trend Micro)."
discovered_at: "2026-06-24T05:11:51Z"
event_date: 2026-06-23
run_id: 2026-06-24-de656486
priority: notable
immediate_action: null
tags:
  - supply-chain
  - ai-abuse
  - infostealer
  - cryptocrime
regions:
  - global
sectors:
  - technology
entities: []
cves: []
sources:
  - url: "https://unit42.paloaltonetworks.com/openclaw-ai-supply-chain-risk/"
    publisher: Unit 42 (Palo Alto Networks)
    role: primary
  - url: "https://www.trendmicro.com/en_us/research/26/b/openclaw-skills-used-to-distribute-atomic-macos-stealer.html"
    publisher: Trend Micro
    role: corroborating
closed_sources: []
evidence:
  - quote: The skill omnicogg used 22 MB README.md padding to exceed scanner thresholds — bypassed both ClawScan and VirusTotal detection
    publisher: Unit 42
  - quote: "installation results in complete control over the agent's identity"
    publisher: Unit 42
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
migrated_from: briefs/2026-06-24.md
---

Palo Alto Networks Unit 42 (2026-06-23) documented five malicious skills published to ClawHub, the third-party skill marketplace for the OpenClaw AI-agent platform, active February–May 2026 ([Unit 42, 2026-06-23](https://unit42.paloaltonetworks.com/openclaw-ai-supply-chain-risk/); corroborated by [Trend Micro](https://www.trendmicro.com/en_us/research/26/b/openclaw-skills-used-to-distribute-atomic-macos-stealer.html)). Two skills delivered the `cluw` macOS infostealer (an Atomic macOS Stealer / AMOS variant) by redirecting the agent to paste-site URLs (rentry.co, glot.io) carrying Base64-encoded `curl | bash` droppers. A third, `omnicogg`, padded its README to 22 MB to exceed the file-size threshold of both ClawScan and VirusTotal, slipping its payload past automated scanning. The most novel two cross a line into agentic abuse: `money-radar` fetches an attacker-controlled `referrals.json` at runtime to silently rewrite the financial referral links the agent recommends (revenue redirection with no re-publish), and `letssendit` coordinates a pool of agents to accumulate Solana ahead of operator-timed token launches — Unit 42's described first weaponisation of an AI-agent botnet for pump-and-dump fraud.

**Why it matters to us:** The skill-marketplace attack surface behaves like a package registry but is barely covered by existing supply-chain tooling, and "installation results in complete control over the agent's identity." For any organisation piloting agentic AI, treat skills as untrusted code: review them line-by-line before install, validate publisher provenance, and watch for agent processes spawning `curl`/shell, reaching paste sites, or creating cron persistence (`T1195.001` supply-chain compromise, `T1204.003`/`T1202` indirect execution, `T1053.003` cron, `T1555` credential access). The file-padding evasion is a reminder that a scanner with a content-size cutoff is a control with a documented bypass.
