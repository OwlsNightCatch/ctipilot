---
schema: 1
kind: threat
title: "Ghost Stadium PhaaS — 300+ FIFA domain clones, multi-language fake SSO, targeting UK/Germany/Portugal/Spain fan credentials before June 11 kickoff"
headline: "Ghost Stadium PhaaS — 300+ FIFA domain clones, multi-language fake SSO, targeting UK/Germany/Portugal/Spain fan credentials before June 11 kickoff"
summary: "Ghost Stadium PhaaS — 300+ pixel-perfect FIFA domain clones targeting UK, Germany, Portugal, Spain fan credentials ahead of 11 June kickoff (FBI IC3 PSA260527, 2026-05-27); Chinese-speaking operator running multi-language fake SSO."
discovered_at: "2026-05-30T05:00:01Z"
event_date: 2026-05-28
run_id: 2026-05-30-aca445cc
priority: high
immediate_action: null
tags:
  - phishing
  - organized-crime
  - china-nexus
regions:
  - europe
  - uk
  - global
sectors:
  - public-sector
entities:
  - "campaign:ghost-stadium-phaas-300-fifa-domain-clones-eu-fan-credentials"
cves: []
sources:
  - url: "https://www.ic3.gov/PSA/2026/PSA260527"
    publisher: FBI IC3 PSA260527
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/fbi-warns-of-fake-fifa-websites-running-world-cup-fraud-schemes/"
    publisher: BleepingComputer
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
migrated_from: briefs/2026-05-30.md
---

The FBI issued PSA260527 on 27 May 2026 warning that a Chinese-speaking financially-motivated threat actor tracked by Group-IB as Ghost Stadium has deployed more than 300 phishing sites impersonating `fifa.com`, all reproducing the official site pixel-for-pixel including a fake single-sign-on authentication flow in multiple languages ([FBI IC3 PSA260527, 2026-05-27](https://www.ic3.gov/PSA/2026/PSA260527); [BleepingComputer, 2026-05-28](https://www.bleepingcomputer.com/news/security/fbi-warns-of-fake-fifa-websites-running-world-cup-fraud-schemes/)). Typosquatted domains span alternative TLDs (`.org`, `.xyz`, `.live`, `.sale`) and character substitutions; additional fake employment portals impersonate FIFA HR functions. Criminal objectives include credential and financial-data theft via the fake SSO, counterfeit ticket and hospitality sales, fake merchandise and streaming-rights fraud. UK, Germany, Portugal, and Spain are explicitly named as target demographics. Browser-based security controls (Safe Browsing, SmartScreen) do not protect against freshly-registered domains before abuse is reported. For defenders at organisations with large employee populations purchasing World Cup tickets: advise bookmarking `https://www.fifa.com` directly; treat any search-result-sponsored result for FIFA ticket purchases as unverified. The high-intensity fraud window is the lead-up to the July 19 final.
