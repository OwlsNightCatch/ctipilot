---
schema: 1
kind: research
horizon: operational
title: "Huntress: Potemkin loader delivers RMMProject RAT and bypasses Chromium App-Bound Encryption"
headline: "Huntress: Potemkin loader delivers RMMProject RAT and bypasses Chromium App-Bound Encryption"
summary: "Huntress documented a ClickFix chain delivering a previously undocumented x64 loader named Potemkin (active since at least February 2026): a ClickFix lure installs an MSI that drops Potemkin via an HTA payload; the loader uses a domain-generation algorithm for C2 and reflectively loads follow-on modules in memory …"
discovered_at: "2026-06-17T05:14:30Z"
event_date: 2026-06-16
run_id: 2026-06-17-e102009c
priority: notable
immediate_action: null
tags:
  - infostealer
  - phishing
  - identity
regions:
  - global
sectors:
  - technology
  - public-sector
entities: []
cves: []
sources:
  - url: "https://www.huntress.com/blog/potemkin-loader-rmmproject-clickfix-attack"
    publisher: "Huntress, 2026-06-16"
    role: primary
  - url: "https://thehackernews.com/2026/06/clickfix-campaigns-expand-malware.html"
    publisher: "The Hacker News, 2026-06-16"
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
migrated_from: briefs/2026-06-17.md
---

Huntress documented a ClickFix chain delivering a previously undocumented x64 loader named Potemkin (active since at least February 2026): a ClickFix lure installs an MSI that drops Potemkin via an HTA payload; the loader uses a domain-generation algorithm for C2 and reflectively loads follow-on modules in memory ([Huntress, 2026-06-16](https://www.huntress.com/blog/potemkin-loader-rmmproject-clickfix-attack)). Its payloads are EtherRAT (Node.js RAT with blockchain C2) and RMMProject, a Lua-scriptable DLL providing hidden remote desktop, keylogging and browser credential theft — including a module specifically built to defeat Chromium's App-Bound Encryption (the credential-storage protection added in Chrome 127) ([The Hacker News, 2026-06-16](https://thehackernews.com/2026/06/clickfix-campaigns-expand-malware.html)). Huntress observed lateral movement across 11+ hosts in one intrusion, indicating network-wide credential harvesting rather than single-host compromise.

**Why it matters to us:** The ABE bypass means saved Chrome credentials are again at risk on infected hosts. Hunt for `mshta.exe` spawned by `msiexec.exe`/`cmd.exe`, reflective-load memory anomalies, DGA-style DNS from `mshta.exe` children, and non-browser processes calling Chrome's DPAPI/LocalState decryption. Block `mshta.exe` via AppLocker/WDAC where feasible.
