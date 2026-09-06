---
schema: 1
kind: research
title: "Microsoft Threat Intelligence: AI-brand impersonation drives Lumma Stealer and Vidar delivery via signed binaries"
headline: "Microsoft Threat Intelligence: AI-brand impersonation drives Lumma Stealer and Vidar delivery via signed binaries"
summary: "Microsoft Threat Intelligence documents a campaign by Storm-3075 (initial-access broker) and Fox Tempest (malware-signing-as-a-service operator) that weaponises public enthusiasm for AI tools, impersonating ChatGPT, Claude, DeepSeek and Microsoft Copilot through SEO poisoning, malvertising and multi-stage redirection …"
discovered_at: "2026-06-09T05:00:05Z"
event_date: 2026-06-08
run_id: 2026-06-09-40d562df
priority: notable
immediate_action: null
tags:
  - infostealer
  - phishing
  - ai-abuse
  - organized-crime
  - supply-chain
regions:
  - global
sectors:
  - technology
entities:
  - "actor:fox-tempest"
cves: []
sources:
  - url: "https://www.microsoft.com/en-us/security/blog/2026/06/08/ai-brands-as-bait-how-threat-actors-are-using-the-ai-hype-in-social-engineering/"
    publisher: Microsoft — AI brands as bait
    role: primary
  - url: "https://www.microsoft.com/en-us/security/blog/2026/05/19/exposing-fox-tempest-a-malware-signing-service-operation/"
    publisher: Microsoft — Exposing Fox Tempest
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
migrated_from: briefs/2026-06-09.md
---

Microsoft Threat Intelligence documents a campaign by Storm-3075 (initial-access broker) and Fox Tempest (malware-signing-as-a-service operator) that weaponises public enthusiasm for AI tools, impersonating ChatGPT, Claude, DeepSeek and Microsoft Copilot through SEO poisoning, malvertising and multi-stage redirection chains (Rebrandly → CAPTCHA gate → credential-harvesting landing) ([Microsoft, 2026-06-08](https://www.microsoft.com/en-us/security/blog/2026/06/08/ai-brands-as-bait-how-threat-actors-are-using-the-ai-hype-in-social-engineering/)). Downloaded binaries are code-signed with certificates obtained through Fox Tempest's MSaaS operation (T1553.002), suppressing initial detection; payloads include Lumma Stealer, Vidar, Hijack Loader and Oyster, with fraudulent GitHub repositories used for payload staging. Microsoft's separate analysis details the Fox Tempest malware-signing-as-a-service operation that supplies the certificates ([Microsoft, 2026-05-19](https://www.microsoft.com/en-us/security/blog/2026/05/19/exposing-fox-tempest-a-malware-signing-service-operation/)).

**Why it matters to us:** Code-signing is no longer a trust anchor here — a valid Authenticode signature on a fresh "AI tool" installer is consistent with this chain. Detection concepts: Sysmon EID 1 for browser-parented processes spawning infostealer-family command lines; EDR process-injection alerts for Hijack Loader. Phish-resistant MFA (FIDO2/passkeys) removes the downstream AiTM credential-replay value even when an endpoint is seeded.
