---
schema: 1
kind: threat
title: "\"Mistic\" backdoor: signed-Defender DLL sideloading and in-memory tradecraft by access broker Woodgnat/KongTuke"
headline: "\"Mistic\" backdoor: signed-Defender DLL sideloading and in-memory tradecraft by access broker Woodgnat/KongTuke"
summary: "Two new initial-access-broker toolsets surface — Mistic and Edgecution — Symantec details Mistic, sideloaded via a signed Microsoft Defender binary so its activity reads as legitimate Defender behaviour (Symantec, 2026-06-24); Zscaler details Edgecution, a malicious Edge extension that bridges the browser sandbox to a host Python backdoor via the Native Messaging API (today's deep dive) (Zscaler, 2026-06-23)."
discovered_at: "2026-06-25T04:59:06Z"
event_date: 2026-06-24
run_id: 2026-06-25-da7fbd23
priority: high
immediate_action: null
tags:
  - ransomware
  - organized-crime
  - infostealer
regions:
  - global
sectors:
  - education
  - technology
  - legal-services
entities:
  - "actor:akira"
  - "tool:mistic-mltbackdoor"
cves: []
sources:
  - url: "https://www.broadcom.com/support/security-center/protection-bulletin/backdoor-mistic-new-backdoor-may-be-linked-to-ransomware-access-broker"
    publisher: Broadcom/Symantec protection bulletin
    role: primary
  - url: "https://www.securityweek.com/new-mistic-rat-opens-door-to-several-ransomware-families/"
    publisher: SecurityWeek
    role: corroborating
  - url: "https://www.csoonline.com/article/4189132/be-on-the-lookout-for-mistic-a-new-backdoor-used-by-ransomware-broker.html"
    publisher: CSO Online
    role: corroborating
closed_sources: []
evidence:
  - quote: Mistic achieves DLL sideloading via a digitally-signed Microsoft Defender executable (MpExtMs.exe) loading a malicious DLL named EndpointDlp.dll
    publisher: CSO Online citing Symantec
  - quote: "Woodgnat maintains relationships with six ransomware families including Qilin, Interlock, Rhysida, Akira, 8Base, and Black Basta"
    publisher: SecurityWeek
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
migrated_from: briefs/2026-06-25.md
---

Symantec disclosed Backdoor.Mistic (also tracked as MLTBackdoor), deployed since April 2026 by initial-access broker Woodgnat (a.k.a. KongTuke) that sells footholds to ransomware affiliates including Qilin, Interlock, Rhysida, Akira, 8Base and Black Basta ([Symantec, 2026-06-24](https://www.broadcom.com/support/security-center/protection-bulletin/backdoor-mistic-new-backdoor-may-be-linked-to-ransomware-access-broker) · [SecurityWeek, 2026-06-24](https://www.securityweek.com/new-mistic-rat-opens-door-to-several-ransomware-families/)). Mistic achieves DLL sideloading via a digitally-signed Microsoft Defender executable (`MpExtMs.exe`) loading a malicious `EndpointDlp.dll` (`T1574.002`, `T1036.005`), so its activity reads as legitimate Defender behaviour to EDR. Per Symantec it also supports in-memory tradecraft and file manipulation/arbitrary code execution with a kill switch for stealth. Delivery uses ClickFix / FileFix / CrashFix lures (fake CAPTCHAs, browser-crash pages, Teams IT-helpdesk impersonation directing victims to run PowerShell).
**Why it matters to us:** The downstream affiliates are all active public-sector ransomware actors. Detection is precise: legitimate Defender DLPs load from `%ProgramFiles%\Windows Defender\` under a Microsoft certificate — any `EndpointDlp.dll` loaded from a user-writable path or with a non-Microsoft signature is high-confidence (Sysmon EID 7). Pair with EID 1 parent-chains for PowerShell spawned by Teams/Office clients.
