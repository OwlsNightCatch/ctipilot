---
schema: 1
kind: research
horizon: operational
title: "Symantec: five-month, low-and-slow mailbox-espionage campaign against a global stock exchange"
headline: "Symantec: five-month, low-and-slow mailbox-espionage campaign against a global stock exchange"
summary: "Broadcom's Symantec and Carbon Black documented a targeted espionage operation (Oct 2025–Mar 2026) against a senior executive at an unnamed global stock exchange (Broadcom/Symantec, 2026-06-03 · SecurityWeek, 2026-06-03)."
discovered_at: "2026-06-04T05:00:12Z"
event_date: 2026-06-03
run_id: 2026-06-04-51b23ffa
priority: notable
immediate_action: null
tags:
  - espionage
  - cloud
  - identity
regions:
  - global
sectors:
  - finance
entities:
  - "campaign:stock-exchange-mailbox-espionage-2026"
cves: []
sources:
  - url: "https://www.security.com/threat-intelligence/stock-exchange-espionage"
    publisher: Broadcom / Symantec Threat Intelligence
    role: primary
  - url: "https://www.securityweek.com/hackers-target-global-stock-exchange-in-espionage-operation/"
    publisher: SecurityWeek
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
migrated_from: briefs/2026-06-04.md
---

Broadcom's Symantec and Carbon Black documented a targeted espionage operation (Oct 2025–Mar 2026) against a senior executive at an unnamed global stock exchange ([Broadcom/Symantec, 2026-06-03](https://www.security.com/threat-intelligence/stock-exchange-espionage) · [SecurityWeek, 2026-06-03](https://www.securityweek.com/hackers-target-global-stock-exchange-in-espionage-operation/)). The actor persisted with masqueraded binaries (`armsvc.exe`, `oneservice.exe` — `T1036.005`) and scheduled tasks, then ran a custom Aspose-based OST stealer to incrementally exfiltrate the target's entire Outlook mailbox in small batches via the Dropbox API and OneDrive Personal (`T1114.001`, `T1567.002`), deliberately using hard-coded Microsoft IP addresses instead of hostnames to defeat DNS-based detection. Tooling also included FRPC, SharpDecryptPwd and Secretsdump (`T1003.001`). No attribution is offered; the assessed motive is intelligence collection. Detection concepts: scheduled-task creation by non-SYSTEM processes (EID 4698 / Sysmon 12), `.ost` reads by processes other than `Outlook.exe` (Sysmon 11), and outbound HTTPS to Dropbox API endpoints from non-browser processes.
