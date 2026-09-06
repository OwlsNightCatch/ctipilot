---
schema: 1
kind: research
title: >
  Google sues China-based "Outsider" PhaaS network for weaponising Gemini to mass-produce phishing
  pages
headline: >
  Google sues China-based "Outsider" PhaaS network for weaponising Gemini to mass-produce phishing
  pages
summary: >
  Google filed a federal lawsuit against the operators of "Outsider Enterprise," a
  phishing-as-a-service network that prompted Google's own Gemini model with innocuous-seeming
  HTML-generation requests and imported the output directly into its kit to stand up live scam
  pages (Google, 2026-06-12).
discovered_at: "2026-06-13T05:00:06Z"
updated_at: "2026-06-15T04:56:01Z"
event_date: 2026-06-12
run_id: 2026-06-13-40b26572
priority: high
immediate_action: null
tags:
  - phishing
  - ai-abuse
  - organized-crime
  - china-nexus
  - law-enforcement
regions:
  - global
  - us
  - europe
sectors:
  - finance
  - public-sector
entities:
  - "campaign:outsider-phaas-gemini-2026"
techniques: []
affected_products: []
cves: []
sources:
  - url: "https://blog.google/innovation-and-ai/technology/safety-security/combatting-ai-scams/"
    publisher: Google
    role: primary
  - url: "https://thehackernews.com/2026/06/google-sues-chinese-smishing-network.html"
    publisher: The Hacker News
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/fbi-disrupts-massive-ai-powered-phishing-service-using-a-million-urls/"
    publisher: BleepingComputer
    role: primary
  - url: "https://cyberscoop.com/outsider-cybercrime-network-takedown-china-fbi-google-lumen/"
    publisher: CyberScoop
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification: null
watchlist_hit: false
actions: []
updates:
  - at: "2026-06-15T04:56:01Z"
    run_id: 2026-06-15-d964affc
    type: update
    summary: >
      The FBI seized ~1 million phishing URLs and the core infrastructure of the China-based Outsider
      PhaaS network, days after Google's civil suit against the same operation — the
      criminal-enforcement half of a parallel-track takedown (BleepingComputer, 2026-06-14).
    fields:
      - entities
      - priority
      - regions
      - sources
      - tags
      - body
    merged_from: 2026-06-15/fbi-operation-ghost-hook-seizes-the-outsider-phaas-infrastru
migrated_from: briefs/2026-06-13.md
---

Google filed a federal lawsuit against the operators of "Outsider Enterprise," a phishing-as-a-service network that prompted Google's own Gemini model with innocuous-seeming HTML-generation requests and imported the output directly into its kit to stand up live scam pages ([Google, 2026-06-12](https://blog.google/innovation-and-ai/technology/safety-security/combatting-ai-scams/)). The kit, sold via Telegram subscription with built-in credential capture, shipped pre-built templates impersonating financial, retail and government services — including postal, parcel-delivery and tax-authority lures that map directly onto common Swiss/EU smishing themes ([The Hacker News, 2026-06-12](https://thehackernews.com/2026/06/google-sues-chinese-smishing-network.html)). The operationally relevant signal is not the scale numbers in the complaint but the technique: LLM safety filters police the prompt, not the downstream weaponisation, so AI-generated phishing pages are now produced faster and with more visual variety than template-based detection assumes. Defender action: anti-phishing controls that fingerprint known kit templates should expect higher variant churn; brief citizen-facing and finance teams that postal/delivery/tax-impersonation smishing volume is rising.

## Update — 2026-06-15T04:56:01Z

The China-based Outsider Enterprise phishing-as-a-service network — the subject of Google's 13 June civil complaint covered last brief — has now been hit on the criminal-enforcement track. On 14 June the FBI, working with Google and Lumen's Black Lotus Labs, executed "Operation Ghost Hook," seizing thousands of Outsider-registered domains (now redirecting ~1 million phishing URLs to an FBI splash page), core admin servers, a Shopify storefront and roughly $100,000 in USDT ([BleepingComputer, 2026-06-14](https://www.bleepingcomputer.com/news/security/fbi-disrupts-massive-ai-powered-phishing-service-using-a-million-urls/); [CyberScoop, 2026-06-12](https://cyberscoop.com/outsider-cybercrime-network-takedown-china-fbi-google-lumen/)).

The delta beyond Google's civil action: agents accessed an Outsider Telegram bot to enumerate the network's criminal customers, and the operation is folded into the FBI's broader "Operation Riptide" against cybercrime infrastructure. Outsider sold AI-assisted phishing kits (it weaponised Gemini and other tools to generate custom phishing-site code) for $88 per week, using fake package-delivery, toll, parking and brokerage lures across 55 countries including the United States ([CyberScoop, 2026-06-12](https://cyberscoop.com/outsider-cybercrime-network-takedown-china-fbi-google-lumen/)).

Defender takeaway: the domain seizure cuts active infrastructure, but Outsider-derived kits — and the prompt-to-phishing-page generation capability — are portable to fresh domains by affiliates. Continue to hunt for AI-generated package/toll/parking credential-harvest pages and brand-impersonation lures targeting staff; the takedown lowers volume, not technique.
