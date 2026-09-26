---
schema: 1
kind: research
title: "macOS ClickFix evolves: hdiutil attach -nobrowse mounts the malicious DMG invisibly before dropping AMOS"
headline: "macOS ClickFix evolves: hdiutil attach -nobrowse mounts the malicious DMG invisibly before dropping AMOS"
summary: "A new macOS ClickFix variant (Palo Alto Unit 42, via BleepingComputer 2026-06-23) drops the visible-DMG step: the fake-CAPTCHA Terminal lure now has the user paste a curl command that uses hdiutil attach -nobrowse to mount the disk image without it appearing in Finder or on the desktop, then launches a self-signed …"
discovered_at: "2026-06-24T05:11:53Z"
event_date: 2026-06-23
run_id: 2026-06-24-de656486
priority: notable
immediate_action: null
tags:
  - phishing
  - infostealer
regions:
  - global
sectors:
  - technology
entities: []
cves: []
sources:
  - url: "https://www.bleepingcomputer.com/news/security/new-macos-clickfix-attack-silently-mounts-dmgs-to-push-infostealer/"
    publisher: BleepingComputer
    role: primary
closed_sources: []
evidence:
  - quote: "Command then executes 'hdiutil attach -nobrowse' to mount the downloaded disk image without displaying it in Finder or on the desktop"
    publisher: BleepingComputer
verification: single-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-24.md
---

A new macOS ClickFix variant (Palo Alto Unit 42, via BleepingComputer 2026-06-23) drops the visible-DMG step: the fake-CAPTCHA Terminal lure now has the user paste a `curl` command that uses `hdiutil attach -nobrowse` to mount the disk image without it appearing in Finder or on the desktop, then launches a self-signed app via `open` ([BleepingComputer, 2026-06-23](https://www.bleepingcomputer.com/news/security/new-macos-clickfix-attack-silently-mounts-dmgs-to-push-infostealer/)). The payload is Atomic macOS Stealer (AMOS): it presents a fake System Preferences authentication prompt to capture the local password, then steals browser credentials across numerous Chromium- and Firefox-derived browsers, cryptocurrency-wallet data, and Keychain contents. `[SINGLE-SOURCE]` — BleepingComputer attributes to Unit 42 but a separate primary Unit 42 article for this specific technique was not located this run (. Detection on macOS: `hdiutil attach -nobrowse` invoked by a shell parented by Terminal; Terminal executing pasted commands referencing external download URLs; apps launched from `/Volumes/` mounts; user awareness that legitimate CAPTCHAs never require Terminal input (`T1204.001`, `T1105`, `T1555`).
