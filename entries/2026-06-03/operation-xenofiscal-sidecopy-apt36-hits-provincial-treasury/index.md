---
schema: 1
kind: research
title: "Operation XENOFISCAL: SideCopy (APT36) hits provincial treasury officials with XenoRAT via an mshta/HTA chain"
headline: "Operation XENOFISCAL: SideCopy (APT36) hits provincial treasury officials with XenoRAT via an mshta/HTA chain"
summary: "Seqrite Labs documented Operation XENOFISCAL, a SideCopy (Transparent Tribe / APT36, Pakistan-attributed) campaign against finance officials across Afghanistan's 34 provincial treasury directorates (Mustoufiats) (Seqrite Labs, 2026-05-29)."
discovered_at: "2026-06-03T05:00:07Z"
event_date: 2026-06-02
run_id: 2026-06-03-ee0eae61
priority: notable
immediate_action: null
tags:
  - espionage
  - nation-state
  - phishing
regions:
  - apac
  - europe
sectors:
  - public-sector
  - finance
entities:
  - "campaign:operation-xenofiscal-sidecopy"
cves: []
sources:
  - url: "https://www.seqrite.com/blog/operation-xenofiscal-sidecopy-deploying-persistent-xenorat-targeting-the-mof-afghanistan/"
    publisher: Seqrite Labs
    role: primary
  - url: "https://thehackernews.com/2026/06/pakistan-linked-sidecopy-targets.html"
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
migrated_from: briefs/2026-06-03.md
---

Seqrite Labs documented Operation XENOFISCAL, a SideCopy (Transparent Tribe / APT36, Pakistan-attributed) campaign against finance officials across Afghanistan's 34 provincial treasury directorates (Mustoufiats) ([Seqrite Labs, 2026-05-29](https://www.seqrite.com/blog/operation-xenofiscal-sidecopy-deploying-persistent-xenorat-targeting-the-mof-afghanistan/)). The chain is the group's long-standing signature — a spear-phishing ZIP carrying a Pashto-language LNK that invokes `mshta.exe` to pull an obfuscated HTA/JavaScript stage from a compromised education domain, which stages .NET loaders in memory before dropping the publicly available XenoRAT (keylogging, screen capture, remote shell) ([The Hacker News, 2026-06-02](https://thehackernews.com/2026/06/pakistan-linked-sidecopy-targets.html)). Persistence uses a Registry Run key typosquatting Microsoft Edge ("Edgre") plus a Scheduled Task; C2 ran on an EU-hosted bulletproof AS (AS59711) previously tied to the group. ATT&CK: `T1566.001`, `T1218.005` (mshta proxy execution), `T1547.001`, `T1053.005`.

**Why it matters to us:** The victimology is South-Central Asian, but the LNK→`mshta.exe`→HTA→RAT pattern and the typosquatted-product Run-key persistence are directly transferable hunt content for any public-sector treasury/finance environment: alert on `mshta.exe` spawning `wscript.exe` or making outbound HTTP, and on Run-key values that misspell legitimate Microsoft product names.
