---
schema: 1
kind: research
horizon: operational
title: "15 malicious JetBrains Marketplace plugins exfiltrate AI provider API keys on \"Apply\""
headline: "15 malicious JetBrains Marketplace plugins exfiltrate AI provider API keys on \"Apply\""
summary: "Aikido Security documented a coordinated campaign of at least 15 IDE plugins published under seven vendor accounts on the JetBrains Marketplace between October 2025 and June 2026, posing as AI coding assistants (built on DeepSeek, OpenAI, SiliconFlow) with roughly 70,000 combined installs (Aikido Security, 2026-06-16)."
discovered_at: "2026-06-18T05:10:34Z"
event_date: 2026-06-17
run_id: 2026-06-18-aa7ee817
priority: notable
immediate_action: null
tags:
  - supply-chain
  - identity
  - infostealer
regions:
  - global
  - europe
sectors:
  - technology
  - public-sector
entities: []
cves: []
sources:
  - url: "https://www.aikido.dev/blog/multiple-jetbrains-ide-plugins-caught-stealing-ai-keys"
    publisher: Aikido Security
    role: primary
  - url: "https://www.infosecurity-magazine.com/news/fifteen-jetbrains-marketplace/"
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
migrated_from: briefs/2026-06-18.md
---

Aikido Security documented a coordinated campaign of at least 15 IDE plugins published under seven vendor accounts on the JetBrains Marketplace between October 2025 and June 2026, posing as AI coding assistants (built on DeepSeek, OpenAI, SiliconFlow) with roughly 70,000 combined installs ([Aikido Security, 2026-06-16](https://www.aikido.dev/blog/multiple-jetbrains-ide-plugins-caught-stealing-ai-keys)). The plugins function as advertised but hook the plugin settings-save handler so that the moment a user enters an AI provider API key and clicks Apply, the credential is exfiltrated to an attacker-controlled server; stolen keys are then resold as discounted "paid-tier" access while the legitimate owner pays the bill ([Infosecurity Magazine, 2026-06-17](https://www.infosecurity-magazine.com/news/fifteen-jetbrains-marketplace/)). The two largest plugins (CodeGPT AI Assistant, DeepSeek AI Assist) account for most of the ~70,000 installs. Maps to `T1195.001` and `T1552.001` (credentials in IDE storage). Defenders should **not** assume the plugins have been removed from the Marketplace — inventory JetBrains plugin installs across developer fleets, rotate any AI provider keys entered into an AI-assistant plugin since October 2025, and move to IDE plugin allowlisting where possible.
