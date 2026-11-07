---
schema: 1
kind: research
title: "Kaspersky GReAT: \"StrikeShark\" loader deploys Cobalt Strike via \"Perfect DLL Hijacking\" against government targets"
headline: "Kaspersky GReAT: \"StrikeShark\" loader deploys Cobalt Strike via \"Perfect DLL Hijacking\" against government targets"
summary: "Kaspersky GReAT published a full technical analysis (2026-06-26) of SharkLoader, an undocumented loader used in a cluster it tracks as StrikeShark and assesses with low confidence as a Chinese-speaking actor (based on the Chinese-authored FScan/Searchall/Pillager toolkit it deploys) (Kaspersky …"
discovered_at: "2026-06-27T05:17:43Z"
event_date: 2026-06-26
run_id: 2026-06-27-40e791d4
priority: notable
immediate_action: null
tags:
  - espionage
  - nation-state
  - china-nexus
regions:
  - global
  - europe
sectors:
  - public-sector
  - defense
  - technology
entities:
  - "campaign:strikeshark-sharkloader"
cves: []
sources:
  - url: "https://securelist.com/strikeshark-campaign/120326/"
    publisher: Kaspersky Securelist (GReAT)
    role: primary
  - url: "https://www.helpnetsecurity.com/2026/06/26/sharkloader-dropper-governments-software-developers/"
    publisher: Help Net Security
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
migrated_from: briefs/2026-06-27.md
---

Kaspersky GReAT published a full technical analysis (2026-06-26) of **SharkLoader**, an undocumented loader used in a cluster it tracks as **StrikeShark** and assesses with *low confidence* as a Chinese-speaking actor (based on the Chinese-authored `FScan`/`Searchall`/`Pillager` toolkit it deploys) ([Kaspersky Securelist, 2026-06-24](https://securelist.com/strikeshark-campaign/120326/)). The loader's signature is "Perfect DLL Hijacking": it sideloads through legitimate signed binaries (`SystemSettings.exe`, `msedge.exe`), then forcibly releases `LdrpLoaderLock` and decrements `LdrpWorkInProgress` so it can spawn threads from `DllMain` without deadlocking the Windows loader — an unusually sophisticated pattern. Two encrypted modules (`DscCoreR.mui`, Blowfish; `SyncRes.dat`, AES-128) install Microsoft Detours hooks across 50+ APIs to null ETW (`EtwEventWrite`), spoof `svchost.exe` as parent PID (`T1134.004`), and demote Beacon memory from RWX to RW during sleep via MinHook on `VirtualAlloc`/`Sleep` to evade memory scanners ([Help Net Security, 2026-06-26](https://www.helpnetsecurity.com/2026/06/26/sharkloader-dropper-governments-software-developers/)). Initial access is via a long list of public-facing RCEs (ProxyLogon `CVE-2021-26855`, Openfire `CVE-2023-32315`, GeoServer `CVE-2024-36401`, F5 BIG-IP `CVE-2023-46747`, FortiOS `CVE-2024-21762`), with European targets including North Macedonia and Serbia.
**Why it matters to us:** Swiss/EU organisations still exposed on any of the listed CVE versions are in the initial-access set. Hunt for `SystemSettings.exe` executing from `%APPDATA%` subdirectories, `PrintDialog.dll` loaded outside `system32` (Sysmon EID 7), and processes whose ETW subsystem produces zero events.
