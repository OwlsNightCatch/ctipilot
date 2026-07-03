---
schema: 1
kind: threat
horizon: operational
title: "Proofpoint TA4922: a China-nexus cybercrime cluster expands from Japan into Germany, the UK and Italy with native-language lures and DLL-side-loaded Atlas RAT"
headline: "Proofpoint TA4922: a China-nexus cybercrime cluster expands from Japan into Germany, the UK and Italy with native-language lures and DLL-side-loaded Atlas RAT"
summary: "Proofpoint's TA4922 — a China-nexus financially-motivated cluster now running the highest campaign tempo it tracks — has pivoted from Japan to Germany, the UK and Italy with native-language HR/payroll/tax lures, DLL-side-loaded Atlas RAT, and a deliberate move to LINE/WhatsApp/Teams to escape email controls (The Hacker News, 2026-06-04)."
discovered_at: "2026-06-05T05:00:01Z"
event_date: 2026-06-04
run_id: 2026-06-05-2c6574c4
priority: high
immediate_action: null
tags:
  - organized-crime
  - phishing
  - infostealer
  - china-nexus
regions:
  - europe
  - dach
  - uk
sectors:
  - finance
  - public-sector
entities:
  - "actor:ta4922"
cves: []
sources:
  - url: "https://thehackernews.com/2026/06/china-linked-ta4922-expands-phishing.html"
    publisher: "The Hacker News, 2026-06-04"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/chinese-hackers-use-new-atlas-rat-malware-in-european-cyberattacks/"
    publisher: "BleepingComputer, 2026-06-04"
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
migrated_from: briefs/2026-06-05.md
---

Proofpoint reports that **TA4922**, a Chinese-speaking, financially-motivated cluster it assesses as running the highest campaign tempo of any cybercrime actor it tracks, expanded in March–April 2026 from its historical Japanese focus to localised campaigns against UK, German, Italian and South African organisations ([The Hacker News, 2026-06-04](https://thehackernews.com/2026/06/china-linked-ta4922-expands-phishing.html); [BleepingComputer, 2026-06-04](https://www.bleepingcomputer.com/news/security/chinese-hackers-use-new-atlas-rat-malware-in-european-cyberattacks/)). Lures are carefully tailored in the target's native language — tax-authority, HR/payroll and invoice themes — and the toolkit now pairs the known **ValleyRAT (Winos 4.0)** with newly observed families: **Atlas RAT** (a C-based RAT) and **RomulusLoader**, which DLL-side-loads (`T1574.002`) AnyDesk and SyncFuture, plus **SilentRunLoader**, a Python infostealer pulling Chrome credentials and cookies (`T1555.003`). A notable TTP shift is the deliberate move of conversations to **LINE, WhatsApp and Microsoft Teams** to pull targets off enterprise email controls before payload delivery.

**Why it matters to us:** German and UK targeting with native-language tax/payroll lures puts DACH public-sector and finance staff squarely in scope. Hunt for DLL side-loading chains where trusted binaries (AnyDesk, SyncFuture) load from unexpected working directories, for Python processes reaching DPAPI / Chrome credential stores, and for unsolicited inbound contact on LINE/WhatsApp/Teams that pivots to a "document" — the out-of-band channel is where the email gateway loses visibility.
