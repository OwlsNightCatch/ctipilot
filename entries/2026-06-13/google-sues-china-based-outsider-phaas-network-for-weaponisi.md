---
schema: 1
kind: research
horizon: operational
title: "Google sues China-based \"Outsider\" PhaaS network for weaponising Gemini to mass-produce phishing pages"
headline: "Google sues China-based \"Outsider\" PhaaS network for weaponising Gemini to mass-produce phishing pages"
summary: "Google filed a federal lawsuit against the operators of \"Outsider Enterprise,\" a phishing-as-a-service network that prompted Google's own Gemini model with innocuous-seeming HTML-generation requests and imported the output directly into its kit to stand up live scam pages (Google, 2026-06-12)."
discovered_at: "2026-06-13T05:00:06Z"
event_date: 2026-06-12
run_id: 2026-06-13-40b26572
priority: notable
immediate_action: null
tags:
  - phishing
  - ai-abuse
  - organized-crime
  - china-nexus
regions:
  - global
sectors:
  - finance
  - public-sector
entities: []
cves: []
sources:
  - url: "https://blog.google/innovation-and-ai/technology/safety-security/combatting-ai-scams/"
    publisher: Google
    role: primary
  - url: "https://thehackernews.com/2026/06/google-sues-chinese-smishing-network.html"
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
migrated_from: briefs/2026-06-13.md
---

Google filed a federal lawsuit against the operators of "Outsider Enterprise," a phishing-as-a-service network that prompted Google's own Gemini model with innocuous-seeming HTML-generation requests and imported the output directly into its kit to stand up live scam pages ([Google, 2026-06-12](https://blog.google/innovation-and-ai/technology/safety-security/combatting-ai-scams/)). The kit, sold via Telegram subscription with built-in credential capture, shipped pre-built templates impersonating financial, retail and government services — including postal, parcel-delivery and tax-authority lures that map directly onto common Swiss/EU smishing themes ([The Hacker News, 2026-06-12](https://thehackernews.com/2026/06/google-sues-chinese-smishing-network.html)). The operationally relevant signal is not the scale numbers in the complaint but the technique: LLM safety filters police the prompt, not the downstream weaponisation, so AI-generated phishing pages are now produced faster and with more visual variety than template-based detection assumes. Defender action: anti-phishing controls that fingerprint known kit templates should expect higher variant churn; brief citizen-facing and finance teams that postal/delivery/tax-impersonation smishing volume is rising.
