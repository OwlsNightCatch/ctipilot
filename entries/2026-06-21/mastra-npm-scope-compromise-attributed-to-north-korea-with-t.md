---
schema: 1
kind: threat
horizon: operational
title: "Mastra npm scope compromise attributed to North Korea, with the access vector our deep dive could not name"
headline: "Mastra npm scope compromise attributed to North Korea, with the access vector our deep dive could not name"
summary: "Microsoft now attributes last week's Mastra npm scope compromise to North Korea's Sapphire Sleet (BlueNoroff) and discloses the access vector our 2026-06-18 coverage could not: a dormant maintainer account that retained publish rights across all 142 @mastra packages (BleepingComputer, 2026-06-20)."
discovered_at: "2026-06-21T04:55:02Z"
event_date: 2026-06-20
run_id: 2026-06-21-2b75e32c
priority: high
immediate_action: null
tags:
  - supply-chain
  - nation-state
  - infostealer
  - north-korea-nexus
regions:
  - global
sectors:
  - technology
  - finance
entities: []
cves: []
sources:
  - url: "https://www.microsoft.com/en-us/security/blog/2026/06/17/postinstall-payload-inside-mastra-npm-supply-chain-compromise/"
    publisher: Microsoft Threat Intelligence
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/microsoft-links-mastra-ai-supply-chain-attack-to-north-korean-hackers/"
    publisher: BleepingComputer
    role: corroborating
  - url: "https://snyk.io/blog/a-forgotten-contributor-account-compromised-the-entire-mastra-npm-package-scope/"
    publisher: Snyk
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: 2026-06-18/mastra-npm-supply-chain-compromise-easy-day-js
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-21.md
---

**UPDATE (originally covered 2026-06-18):** The deep dive on 2026-06-18 documented the `easy-day-js` poisoning of 140+ `@mastra` packages but noted the cited primaries did not disclose *how* the publishing account was obtained, and made no attribution. Microsoft Threat Intelligence has now closed both gaps: it attributes the operation to North Korea's **Sapphire Sleet** (BlueNoroff / UNC1069) and states the access vector was a **dormant former-contributor npm account (`ehindero`) whose publish rights across the entire `@mastra` scope were never revoked** ([BleepingComputer, 2026-06-20](https://www.bleepingcomputer.com/news/security/microsoft-links-mastra-ai-supply-chain-attack-to-north-korean-hackers/)).

Microsoft's analysis details the post-install chain — `easy-day-js` disables TLS verification, pulls a cross-platform Node.js implant that enumerates 166 cryptocurrency-wallet browser extensions and steals browser profiles, then establishes a `scdev` svchost service running as SYSTEM for boot persistence ([Microsoft Threat Intelligence, 2026-06-17](https://www.microsoft.com/en-us/security/blog/2026/06/17/postinstall-payload-inside-mastra-npm-supply-chain-compromise/)). Snyk independently confirms the dormant-account root cause and notes npm does not expire scope-publish permissions on inactivity ([Snyk, 2026-06-16](https://snyk.io/blog/a-forgotten-contributor-account-compromised-the-entire-mastra-npm-package-scope/)). The defender action shifts from "remove `easy-day-js`" to a structural control: audit your own private-registry and package-scope ACLs for dormant accounts with retained publish rights, and enforce time-bound or MFA-gated publish tokens. Microsoft notes this is Sapphire Sleet's second npm scope-takeover of 2026 (after Axios in April) — a systematised dormant-high-privilege-account hunt, not a one-off.
