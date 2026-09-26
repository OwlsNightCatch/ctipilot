---
schema: 1
kind: research
title: SmartApeSG ClickFix stages an unnamed RAT that pivots to a weaponised NetSupport Manager
headline: SmartApeSG ClickFix stages an unnamed RAT that pivots to a weaponised NetSupport Manager
summary: "SmartApeSG ClickFix lures now stage a custom RAT that then drops NetSupport Manager — a same-day SANS ISC forensic diary maps a processor.vbs → token.bat → setup.cab chain that self-deletes its droppers and persists a weaponised NetSupport build (SANS ISC, 2026-06-01)."
discovered_at: "2026-06-01T05:00:02Z"
event_date: 2026-06-01
run_id: 2026-06-01-7f55e064
priority: high
immediate_action: null
tags:
  - phishing
  - organized-crime
regions:
  - global
  - europe
sectors:
  - public-sector
entities: []
cves: []
sources:
  - url: "https://isc.sans.edu/diary/rss/33034"
    publisher: SANS Internet Storm Center
    role: primary
closed_sources: []
evidence: []
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
migrated_from: briefs/2026-06-01.md
---

SANS ISC handler Brad Duncan published a same-day forensic diary (2026-06-01) reconstructing an infection observed on 2026-05-27 that began with the SmartApeSG ClickFix campaign — fake browser-verification / "press Win+R" lures served from compromised pages — and ended in a full NetSupport Manager RAT deployment ([SANS ISC, 2026-06-01](https://isc.sans.edu/diary/rss/33034)). The ClickFix execution (`T1204.001`) drops a ZIP carrying an unnamed staging RAT that, per Duncan, has been beaconing a custom *encoded — not TLS* protocol over TCP/443 to its C2 since at least April 2026; that staging RAT then fetched the NetSupport payload as a ~17 MB Microsoft Cabinet (`setup.cab`). The install chain is `processor.vbs` (a 109-byte VBScript launcher in `C:\ProgramData\`, `T1059.005`) → `token.bat` (extracts the CAB into `C:\ProgramData\UpdateInstaller\`, sets persistence, then self-deletes all three dropper components, `T1070.004`) → NetSupport RAT C2 over port 443 (`T1219 Remote Access Tools`). Because NetSupport is legitimate commercial software, its presence and traffic blend with benign remote-support telemetry.

This is a single-source handler diary (HIGH-reliability source, single-day observation) and carries no independent corroboration of the identical chain in-window — treat the specifics as one analyst's forensic account. Detection concepts a SOC can apply without IOCs: browser process (`chrome.exe`/`msedge.exe`/`firefox.exe`) spawning `wscript.exe`/`mshta.exe`/`cmd.exe` (Sysmon EID 1 with browser parent-image); short-lived `.vbs`/`.bat` file-creates in `C:\ProgramData\` (Sysmon EID 11); CAB expansion via `expand.exe`/`wusa.exe` from `ProgramData`; and registry Run-key persistence pointing at a non-standard NetSupport path (`C:\ProgramData\UpdateInstaller\` rather than the legitimate `C:\Program Files\NetSupport\`). Where TLS inspection is in place, unencrypted payload on port 443 from a NetSupport process is anomalous.
