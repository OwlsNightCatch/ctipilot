---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-sector-patterns
title: Finance — Iberian retail-banking pressure from Grandoreiro plus a parallel Android MaaS
headline: Finance — Iberian retail-banking pressure from Grandoreiro plus a parallel Android MaaS
summary: "WatchGuard documented a Grandoreiro campaign abusing Delphi DLL side-loading across four different software packages, with WebSocket/STUN C2, against banks in Portugal and Spain; ESET mapped a parallel BTMOB Android RAT delivered as malware-as-a-service against the same Iberian banking customers via HTML …"
discovered_at: "2026-05-25T05:00:14Z"
event_date: 2026-05-29
run_id: 2026-W22-da77963d
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
    publisher: WatchGuard — Grandoreiro Europe/LatAm
    role: primary
  - url: "https://www.welivesecurity.com/en/malware/btmob-stealthy-rat-burrowing-deep-android-devices/"
    publisher: ESET WeLiveSecurity — BTMOB
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
migrated_from: briefs/weekly/2026-W22.md
---

WatchGuard documented a **Grandoreiro** campaign abusing Delphi DLL side-loading across four different software packages, with WebSocket/STUN C2, against banks in Portugal and Spain; ESET mapped a parallel **BTMOB** Android RAT delivered as malware-as-a-service against the same Iberian banking customers via HTML injection and Accessibility Service abuse ([2026-05-29](/briefs/2026-05-29/)). The pattern for EU financial-sector defenders is the desktop-plus-mobile pincer from LATAM-origin operators sustaining European targeting: DLL-side-loading detection on the endpoint and Accessibility-Service-abuse heuristics on managed mobile fleets address the two halves.
