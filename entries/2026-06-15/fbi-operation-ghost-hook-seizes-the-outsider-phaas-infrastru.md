---
schema: 1
kind: threat
horizon: operational
title: "FBI \"Operation Ghost Hook\" seizes the Outsider PhaaS infrastructure Google had sued"
headline: "FBI \"Operation Ghost Hook\" seizes the Outsider PhaaS infrastructure Google had sued"
summary: "The FBI seized ~1 million phishing URLs and the core infrastructure of the China-based Outsider PhaaS network, days after Google's civil suit against the same operation — the criminal-enforcement half of a parallel-track takedown (BleepingComputer, 2026-06-14)."
discovered_at: "2026-06-15T04:56:01Z"
event_date: 2026-06-14
run_id: 2026-06-15-d964affc
priority: high
immediate_action: null
tags:
  - phishing
  - law-enforcement
  - ai-abuse
  - china-nexus
regions:
  - us
  - europe
sectors:
  - finance
  - public-sector
entities: []
cves: []
sources:
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
update_of: 2026-06-13/google-sues-china-based-outsider-phaas-network-for-weaponisi
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-15.md
---

**UPDATE (originally covered 2026-06-13):** the China-based Outsider Enterprise phishing-as-a-service network — the subject of Google's 13 June civil complaint covered last brief — has now been hit on the criminal-enforcement track. On 14 June the FBI, working with Google and Lumen's Black Lotus Labs, executed "Operation Ghost Hook," seizing thousands of Outsider-registered domains (now redirecting ~1 million phishing URLs to an FBI splash page), core admin servers, a Shopify storefront and roughly $100,000 in USDT ([BleepingComputer, 2026-06-14](https://www.bleepingcomputer.com/news/security/fbi-disrupts-massive-ai-powered-phishing-service-using-a-million-urls/); [CyberScoop, 2026-06-12](https://cyberscoop.com/outsider-cybercrime-network-takedown-china-fbi-google-lumen/)).

The delta beyond Google's civil action: agents accessed an Outsider Telegram bot to enumerate the network's criminal customers, and the operation is folded into the FBI's broader "Operation Riptide" against cybercrime infrastructure. Outsider sold AI-assisted phishing kits (it weaponised Gemini and other tools to generate custom phishing-site code) for $88 per week, using fake package-delivery, toll, parking and brokerage lures across 55 countries including the United States ([CyberScoop, 2026-06-12](https://cyberscoop.com/outsider-cybercrime-network-takedown-china-fbi-google-lumen/)).

Defender takeaway: the domain seizure cuts active infrastructure, but Outsider-derived kits — and the prompt-to-phishing-page generation capability — are portable to fresh domains by affiliates. Continue to hunt for AI-generated package/toll/parking credential-harvest pages and brand-impersonation lures targeting staff; the takedown lowers volume, not technique.
