---
schema: 1
kind: research
horizon: operational
title: "Atos TRC: \"hardware-gated\" Windows drivers can be made BYOVD-exploitable in software"
headline: "Atos TRC: \"hardware-gated\" Windows drivers can be made BYOVD-exploitable in software"
summary: "Research from the Atos Trusted Research Center (referenced by NDSS Symposium 2026 paper 2026-s1491), resurfaced in in-window reporting on 2026-05-22, argues that a large class of Windows kernel-mode drivers previously treated as BYOVD-resistant — because triggering their vulnerable IOCTL paths supposedly required …"
discovered_at: "2026-05-24T05:00:04Z"
event_date: 2026-05-22
run_id: 2026-05-24-f1fd8070
priority: notable
immediate_action: null
tags:
  - priv-esc
regions:
  - global
sectors:
  - technology
entities:
  - "trend:atos-byovd-hardware-gate-bypass-2026"
cves: []
sources:
  - url: "https://atos.net/en/lp/cybershield/making-vulnerable-drivers-exploitable-without-hardware-the-byovd-perspective"
    publisher: "Atos TRC, 2026-04-17"
    role: primary
  - url: "https://thehackernews.com/2026/05/making-vulnerable-drivers-exploitable.html"
    publisher: "The Hacker News, 2026-05-22"
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
migrated_from: briefs/2026-05-24.md
---

Research from the Atos Trusted Research Center (referenced by NDSS Symposium 2026 paper 2026-s1491), resurfaced in in-window reporting on 2026-05-22, argues that a large class of Windows kernel-mode drivers previously treated as BYOVD-resistant — because triggering their vulnerable IOCTL paths supposedly required physical hardware — can be made fully exploitable without that hardware ([The Hacker News, 2026-05-22](https://thehackernews.com/2026/05/making-vulnerable-drivers-exploitable.html)). Three techniques remove the gate: binding a PnP driver's `AddDevice` callback to a software-emulated device with an attacker-chosen hardware ID (via SetupAPI / the Software Device API); filter-driver restacking on disk/storage device stacks to bind otherwise-unloadable drivers; and direct registry manipulation under `HKLM\SYSTEM\CurrentControlSet\Control\Class` to associate a vulnerable driver with an existing device object. The write-up frames these against real-world example drivers to show IOCTL code paths reachable without the assumed hardware ([Atos TRC, 2026-04-17](https://atos.net/en/lp/cybershield/making-vulnerable-drivers-exploitable-without-hardware-the-byovd-perspective)).

**Why it matters to us:** BYOVD is a staple kernel-level EDR-bypass technique for ransomware affiliates and APTs operating against EU/CH targets, and this work expands the effective LOLDrivers attack surface — vulnerable-driver blocklists that implicitly assume a hardware prerequisite need re-evaluation. Hunt `HKLM\SYSTEM\CurrentControlSet\Control\Class` writes to `UpperFilters`/`LowerFilters`/`ClassFilters` from non-SYSTEM processes (Sysmon EID 13), driver-load events (Sysmon EID 6) for drivers loaded from user-writable paths, and streaming/thunk-class kernel drivers loaded by a non-system process. Hardening: enforce the Microsoft Vulnerable Driver Blocklist (WDAC) and HVCI/Memory Integrity, and re-test blocklist coverage against these hardware-gate-bypass techniques. ATT&CK `T1068`, `T1014`, `T1562.001`.
