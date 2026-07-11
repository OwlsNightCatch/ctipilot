---
schema: 1
kind: threat
horizon: operational
title: "\"GreatXML\": unpatched BitLocker bypass via crafted XML on the recovery partition — PoC public, practical severity contested"
headline: "\"GreatXML\": unpatched BitLocker bypass via crafted XML on the recovery partition — PoC public, practical severity contested"
summary: "\"GreatXML\": unpatched BitLocker bypass with public PoC — crafted XML files on the recovery partition yield a SYSTEM shell in WinRE; severity is contested (an initial Defender offline scan, which requires admin, must have run once) (SecurityWeek, 2026-06-11)."
discovered_at: "2026-06-12T05:00:01Z"
event_date: 2026-06-11
run_id: 2026-06-12-5ab9a319
priority: high
immediate_action: null
tags:
  - vulnerabilities
  - zero-day
  - auth-bypass
  - poc-public
  - no-patch
regions:
  - global
sectors:
  - public-sector
entities:
  - "campaign:nightmare-eclipse-microsoft-dcu-threat-greenplasma-miniplasmaaac"
  - "trend:nightmare-eclipse-rogueplanet-defender-toctou-lpe-2026-06"
  - "trend:greatxml-bitlocker-bypass-2026"
cves: []
sources:
  - url: "https://www.securityweek.com/greatxml-zero-day-exploit-bypasses-bitlocker/"
    publisher: SecurityWeek
    role: primary
  - url: "https://www.theregister.com/security/2026/06/11/nightmare-eclipse-drops-claimed-bitlocker-bypass-for-microsoft-windows/5254371"
    publisher: The Register
    role: corroborating
  - url: "https://security-hub.ncsc.admin.ch/#/posts/12622"
    publisher: NCSC-CH Security Hub
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
migrated_from: briefs/2026-06-12.md
---

The researcher operating as Nightmare Eclipse (also tracked as Chaotic Eclipse) published GreatXML on 11 June — a working proof-of-concept that bypasses BitLocker full-volume encryption and spawns a SYSTEM command prompt inside the Windows Recovery Environment (WinRE), with no CVE assigned and no Microsoft patch available ([SecurityWeek, 2026-06-11](https://www.securityweek.com/greatxml-zero-day-exploit-bypasses-bitlocker/)). The technique places a crafted `unattend.xml` at the root of the recovery partition plus a second malformed XML under `Recovery/`, then reboots into WinRE; the Microsoft Defender Offline scan path processes the attacker-controlled XML while the volume is unlocked. Per the researcher, "any Windows machine becomes vulnerable to GreatXML as soon as Defender's offline scanning is initiated" — i.e. the bypass arms itself once an offline scan has ever run on the host ([SecurityWeek, 2026-06-11](https://www.securityweek.com/greatxml-zero-day-exploit-bypasses-bitlocker/)). Independent researcher Will Dormann disputes the practical severity, noting that triggering the prerequisite Defender Offline scan requires an existing Windows logon with admin credentials — an attacker in that position could already disable BitLocker outright ([The Register, 2026-06-11](https://www.theregister.com/security/2026/06/11/nightmare-eclipse-drops-claimed-bitlocker-bypass-for-microsoft-windows/5254371)). NCSC-CH is tracking the disclosure as part of the same researcher's zero-day series (BlueHammer, RedSun, UnDefend, YellowKey, GreenPlasma, RoguePlanet — RoguePlanet covered 2026-06-11) ([NCSC-CH CSH, 2026-06-11](https://security-hub.ncsc.admin.ch/#/posts/12622)). Maps to [T1542.001](https://attack.mitre.org/techniques/T1542/001/) (Pre-OS Boot) territory: code execution from the recovery path while the BitLocker-protected volume is mounted.

**Why it matters to us:** evil-maid and stolen-laptop scenarios against BitLocker-protected fleets get cheaper where an offline scan has previously run. Until a patch lands: audit recovery-partition contents for unexpected `unattend.xml`/`ReAgent.xml` modifications, require TPM+PIN pre-boot authentication on high-value mobile assets, and weigh `reagentc /disable` on machines where recovery capability is dispensable.
