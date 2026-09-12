---
schema: 1
kind: incident
title: "Braintrust AI evaluation platform AWS account breach — multi-tenant LLM-provider keys and SaaS credentials at risk; mandatory key rotation across customer base"
headline: "Braintrust AI evaluation platform AWS account breach — multi-tenant LLM-provider keys and SaaS credentials at risk; mandatory key rotation across customer base"
summary: "Braintrust, a US-based AI evaluation and observability platform, confirmed on 2026-05-06 that an attacker accessed one of its AWS accounts on 2026-05-04 (TechCrunch, 2026-05-06 · SecurityWeek, 2026-05-08)."
discovered_at: "2026-05-10T05:00:01Z"
event_date: 2026-05-08
run_id: 2026-05-10-001
priority: notable
immediate_action: null
tags:
  - data-breach
  - supply-chain
  - cloud
  - ai-abuse
regions:
  - global
sectors:
  - technology
entities:
  - "incident:braintrust-aws-breach-2026"
cves: []
sources:
  - url: "https://techcrunch.com/2026/05/06/ai-evaluation-startup-braintrust-confirms-breach-tells-every-customer-to-rotate-sensitive-keys/"
    publisher: "TechCrunch, 2026-05-06"
    role: primary
  - url: "https://www.securityweek.com/ai-firm-braintrust-prompts-api-key-rotation-after-data-breach/"
    publisher: "SecurityWeek, 2026-05-08"
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
migrated_from: briefs/2026-05-10.md
---

Braintrust, a US-based AI evaluation and observability platform, confirmed on 2026-05-06 that an attacker accessed one of its AWS accounts on 2026-05-04 ([TechCrunch, 2026-05-06](https://techcrunch.com/2026/05/06/ai-evaluation-startup-braintrust-confirms-breach-tells-every-customer-to-rotate-sensitive-keys/) · [SecurityWeek, 2026-05-08](https://www.securityweek.com/ai-firm-braintrust-prompts-api-key-rotation-after-data-breach/)). The compromised account contained organisation-level API keys customers use to connect to upstream LLM providers (OpenAI, Anthropic, Azure OpenAI). SecurityWeek separately notes that customers commonly federate access from Braintrust into Box, Cloudflare, Dropbox, Notion, Ramp, and Stripe, framing those as adjacent SaaS providers whose credentials warrant the same audit posture; the Braintrust statement itself does not enumerate exposed third-party credentials. Braintrust locked the account, audited related infrastructure, rotated internal secrets, and instructed every customer to rotate organisation-level AI provider credentials regardless of whether their specific keys were confirmed exposed. One customer was confirmed compromised and three others reported anomalous AI usage spikes consistent with credential abuse during the post-incident review. No specific Swiss/EU customer impact was identified in available sources at this run's window close.

The incident class is architecturally significant for European public-sector AI pilots: AI-evaluation and observability platforms aggregate API credentials for many LLM providers per customer organisation, so a single SaaS-tier compromise propagates into a multi-provider credential event for every downstream tenant. The same risk profile applies to AI gateways (LiteLLM,, agent-evaluation harnesses, prompt-rule-based observability, and AI prompt-management platforms.

**Defender takeaway:** Inventory which AI-tooling SaaS vendors hold organisation-level upstream-provider keys; require per-environment scoping (dev / staging / prod) and short TTLs; require provider-side anomaly alerts for unusual call-volume or geographic-origin shifts; treat any 2026-05-04 → 2026-05-06 audit-log gap on Braintrust as potentially related to this incident, even when keys were not labelled as confirmed exposed.
