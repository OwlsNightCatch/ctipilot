---
schema: 1
kind: research
horizon: operational
title: "WatchGuard documents Grandoreiro's Delphi-DLL-side-loading + WebSocket/STUN C2 against Portuguese & Spanish banks; ESET maps parallel Android BTMOB MaaS"
headline: "WatchGuard documents Grandoreiro's Delphi-DLL-side-loading + WebSocket/STUN C2 against Portuguese & Spanish banks; ESET maps parallel Android BTMOB MaaS"
summary: "WatchGuard's Secplicity team published telemetry on 2026-05-26 covering a sustained 2026 Grandoreiro banking-trojan campaign against banks in Portugal and Spain (and across Latin America)."
discovered_at: "2026-05-29T05:00:13Z"
event_date: 2026-05-26
run_id: 2026-05-29-c7f56b00
priority: notable
immediate_action: null
tags:
  - organized-crime
  - mobile
  - phishing
  - infostealer
regions:
  - europe
  - latam
sectors:
  - finance
entities: []
cves: []
sources:
  - url: "https://www.watchguard.com/wgrd-security-hub/secplicity-blog/grandoreiro-malware-campaign-targets-europe-and-latin-america"
    publisher: WatchGuard Secplicity
    role: primary
  - url: "https://www.welivesecurity.com/en/malware/btmob-stealthy-rat-burrowing-deep-android-devices/"
    publisher: ESET WeLiveSecurity — BTMOB
    role: corroborating
  - url: "https://thehackernews.com/2026/05/grandoreiro-malware-and-btmob-rat.html"
    publisher: The Hacker News
    role: corroborating
closed_sources: []
evidence:
  - quote: "WatchGuard telemetry identified a campaign associated to Grandoreiro that uses the DLL Side-Loading technique abusing four different softwares, targeting banks in Portugal"
    publisher: WatchGuard
  - quote: BTMOB is a sophisticated Android RAT distributed as a MaaS targeting banking customers in Spain and Portugal through HTML injection and Accessibility Service abuse
    publisher: ESET WeLiveSecurity
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
migrated_from: briefs/2026-05-29.md
---

WatchGuard's Secplicity team [published telemetry on 2026-05-26 covering a sustained 2026 Grandoreiro banking-trojan campaign](https://www.watchguard.com/wgrd-security-hub/secplicity-blog/grandoreiro-malware-campaign-targets-europe-and-latin-america) against banks in Portugal and Spain (and across Latin America). The campaign deploys Delphi-11-compiled DLLs through DLL side-loading against four abused legitimate signed binaries; the Grandoreiro core has been re-tooled to use the `sgcWebSockets` library for command-and-control, with **STUN and ICE protocols enabling NAT traversal** — C2 traffic visually blends with web-conferencing data and bypasses standard protocol-inspection rules. WatchGuard names Abanca, Banco de Portugal, BBVA PT, Caixa Geral Depositos, Santander, Revolut and Wise as targeted institutions. A parallel Latin American mobile-banking strand: [ESET WeLiveSecurity documents BTMOB](https://www.welivesecurity.com/en/malware/btmob-stealthy-rat-burrowing-deep-android-devices/), an Android RAT (evolved from SpySolr) sold malware-as-a-service, documented by ESET as targeting users in Brazil and Argentina. BTMOB requests Accessibility Service permissions and uses them for full device takeover — HTML-injected overlay phishing, keylogging and on-demand screen recording. [The Hacker News](https://thehackernews.com/2026/05/grandoreiro-malware-and-btmob-rat.html) provides a combined writeup with the WatchGuard / ESET coverage.
