---
schema: 1
kind: annual-report
horizon: operational
title: "Check Point Research March-April 2026 AI Threat Landscape Digest: a single operator runs two AI platforms in parallel to breach nine Mexican government agencies"
headline: "Check Point Research March-April 2026 AI Threat Landscape Digest: a single operator runs two AI platforms in parallel to breach nine Mexican government agencies"
summary: "Check Point Research's March-April 2026 AI Threat Landscape Digest (published 2026-05-22) is the operationally most striking annual / periodic AI report of the past month."
discovered_at: "2026-05-23T05:00:09Z"
event_date: null
run_id: 2026-05-23-852c21c8
priority: notable
immediate_action: null
tags:
  - ai-abuse
  - espionage
  - supply-chain
  - organized-crime
regions:
  - global
  - latam
sectors:
  - public-sector
  - healthcare
  - finance
entities:
  - "report:checkpoint-research-ai-threat-landscape-march-april-2026-mexico-nine-agencies-ev"
  - "campaign:tds-security-tool-impersonation-checkpoint"
cves: []
sources:
  - url: "https://blog.checkpoint.com/research/ai-attacks-are-no-longer-experimental-key-findings-from-the-march-april-2026-ai-threat-landscape/"
    publisher: Check Point Research
    role: primary
closed_sources: []
evidence: []
verification: single-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-23.md
---

Check Point Research's [March-April 2026 AI Threat Landscape Digest](https://blog.checkpoint.com/research/ai-attacks-are-no-longer-experimental-key-findings-from-the-march-april-2026-ai-threat-landscape/) (published 2026-05-22) is the operationally most striking annual / periodic AI report of the past month. The centrepiece — researched by Gambit Security and summarised in the Check Point post — documents a single unidentified operator compromising **nine Mexican government agencies** between December 2025 and February 2026, covering tax records, civil registry, patient files and electoral infrastructure. The structural innovation: the attacker ran two commercial AI platforms in parallel — one managing live exploitation and issuing >5,000 AI-executed commands, a second processing harvested data and feeding instructions back into the first. Persistence for the AI itself was simple: modifying the AI client's startup configuration file to embed persistent instructions inherited by every subsequent session.

Two further findings have direct EU/CH public-sector implications. First, the **EvilTokens** platform — a commercial jailbreak-as-a-service tool packaging AI-driven phishing generation, financial-data extraction and similar capabilities as a subscription — represents the same commoditisation curve as Kali365 (§ 1) but for AI-assisted intrusion. Second, CPR explicitly calls out that **stolen API keys for Anthropic, OpenAI, Groq and Mistral are now high-value criminal targets**, since they grant access to powerful AI services without an account; Swiss federal and cantonal agencies using commercial AI APIs should treat key rotation cadence and source-IP scoping (Conditional Access on the API layer) on par with classic privileged-credential hygiene. Detection vantage: bulk exfiltration events temporally co-located with anomalous API call patterns to commercial AI services from non-standard processes; process trees in which AI client libraries spawn data-collection subprocesses; cloud audit logs showing API key issuance followed immediately by large-volume inference calls from unusual source IPs.
