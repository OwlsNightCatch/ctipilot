---
schema: 1
kind: threat
horizon: operational
title: "\"RoguePlanet\" Microsoft Defender zero-day: TOCTOU race in the scan engine yields a SYSTEM shell, no CVE, no patch"
headline: "\"RoguePlanet\" Microsoft Defender zero-day: TOCTOU race in the scan engine yields a SYSTEM shell, no CVE, no patch"
summary: "A new Microsoft Defender SYSTEM-LPE zero-day, \"RoguePlanet,\" dropped as a public PoC hours after June Patch Tuesday — a TOCTOU race in the Defender scan engine, no CVE and no patch (BleepingComputer, 2026-06-09). No in-the-wild use reported yet; monitoring is the only mitigation."
discovered_at: "2026-06-11T05:00:01Z"
event_date: 2026-06-10
run_id: 2026-06-11-7edf1d8a
priority: high
immediate_action: null
tags:
  - vulnerabilities
  - zero-day
  - lpe
  - priv-esc
  - poc-public
  - no-patch
regions:
  - global
sectors:
  - public-sector
entities:
  - "campaign:nightmare-eclipse-microsoft-dcu-threat-greenplasma-miniplasmaaac"
  - "trend:nightmare-eclipse-rogueplanet-defender-toctou-lpe-2026-06"
cves: []
sources:
  - url: "https://www.bleepingcomputer.com/news/microsoft/microsoft-defender-rogueplanet-zero-day-grants-system-privileges/"
    publisher: BleepingComputer
    role: primary
  - url: "https://www.securityweek.com/new-windows-zero-day-exploit-rogueplanet-released/"
    publisher: SecurityWeek
    role: corroborating
  - url: "https://security-hub.ncsc.admin.ch/#/posts/12622"
    publisher: NCSC-CH GovCERT
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
migrated_from: briefs/2026-06-11.md
---

A researcher operating as "Nightmare Eclipse" (also tracked as Chaotic Eclipse) published a working proof-of-concept named RoguePlanet on 9 June 2026 — hours after Microsoft patched two of the researcher's earlier disclosures (YellowKey/CVE-2026-45585 and GreenPlasma/CVE-2026-50507) in June Patch Tuesday ([BleepingComputer, 2026-06-09](https://www.bleepingcomputer.com/news/microsoft/microsoft-defender-rogueplanet-zero-day-grants-system-privileges/)). RoguePlanet abuses a time-of-check/time-of-use race condition in the Microsoft Defender real-time scan engine (`MsMpEng.exe`, running as SYSTEM): an attacker times a file-system operation to coincide with Defender's scan pass and redirects it, achieving local privilege escalation to SYSTEM on fully-patched Windows 10 and 11 ([SecurityWeek, 2026-06-10](https://www.securityweek.com/new-windows-zero-day-exploit-rogueplanet-released/)). NCSC-CH GovCERT consolidated this disclosure alongside the researcher's prior 2026 Defender drops — BlueHammer, RedSun, UnDefend, YellowKey and GreenPlasma ([NCSC-CH GovCERT, 2026-06-10](https://security-hub.ncsc.admin.ch/#/posts/12622)). The primitive requires local code execution first (a standard-user foothold is sufficient) and is reliability-limited by the race; no in-the-wild exploitation has been reported and Microsoft has not assigned a CVE or issued an advisory. Technique class: `T1068` Exploitation for Privilege Escalation.

**Why it matters to us:** Microsoft Defender is the default endpoint protection on Windows fleets across Swiss federal and EU public-sector environments, so the affected component is universal. With no patch, detection is the control: alert on `MsMpEng.exe` spawning `cmd.exe`/`powershell.exe` child processes (Sysmon EID 1 / Windows 4688 with parent image in the Defender path) and on SYSTEM-context shells not tied to a service restart.
