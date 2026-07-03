---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-long-running
title: "TA4922 — China-nexus cybercrime cluster expands from Japan into Germany, UK and Italy with native-language lures and Atlas RAT"
headline: "TA4922 — China-nexus cybercrime cluster expands from Japan into Germany, UK and Italy with native-language lures and Atlas RAT"
summary: "Proofpoint reported this week that TA4922, a Chinese-speaking financially-motivated cluster running the highest campaign tempo of any cybercrime actor Proofpoint tracks, pivoted in March–April 2026 to localised campaigns against German, UK, Italian and South African organisations (The Hacker News, 2026-06-04 …"
discovered_at: "2026-06-01T05:00:19Z"
event_date: 2026-06-05
run_id: 2026-W23-9118e7bd
priority: notable
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
    publisher: The Hacker News
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/chinese-hackers-use-new-atlas-rat-malware-in-european-cyberattacks/"
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
migrated_from: briefs/weekly/2026-W23.md
---

Proofpoint reported this week that TA4922, a Chinese-speaking financially-motivated cluster running the highest campaign tempo of any cybercrime actor Proofpoint tracks, pivoted in March–April 2026 to localised campaigns against German, UK, Italian and South African organisations ([The Hacker News, 2026-06-04](https://thehackernews.com/2026/06/china-linked-ta4922-expands-phishing.html); [BleepingComputer, 2026-06-04](https://www.bleepingcomputer.com/news/security/chinese-hackers-use-new-atlas-rat-malware-in-european-cyberattacks/); [daily 2026-06-05](/briefs/2026-06-05/)). Native-language tax-authority, HR/payroll and invoice lures now pair the known ValleyRAT (Winos 4.0) with newly observed Atlas RAT (C-based), RomulusLoader, and SilentRunLoader (Python infostealer targeting Chrome credentials). A notable TTP shift: conversations are moved to LINE, WhatsApp and Microsoft Teams before payload delivery, pulling targets off enterprise email controls. DACH public-sector and finance staff are in direct scope. Hunt for DLL side-loading chains where AnyDesk/SyncFuture load from unexpected user-profile paths, for Python processes reaching Chrome DPAPI, and for unsolicited inbound contact on Teams/WhatsApp that pivots to a "document."
