---
schema: 1
kind: research
title: "Cisco Talos: a field guide to Windows COM abuse — ITaskService, BITS, WMI and DCOM as EDR-evasion primitives"
headline: "Cisco Talos: a field guide to Windows COM abuse — ITaskService, BITS, WMI and DCOM as EDR-evasion primitives"
summary: "Cisco Talos published a reverse-engineering primer (2026-06-25) on how Windows threats weaponise Component Object Model (COM) interfaces to hide operations inside legitimate service call stacks (Cisco Talos, 2026-06-25)."
discovered_at: "2026-06-28T05:05:42Z"
event_date: 2026-06-25
run_id: 2026-06-28-1b30612a
priority: notable
immediate_action: null
tags:
  - infostealer
  - botnet
regions:
  - global
sectors:
  - technology
entities: []
cves: []
sources:
  - url: "https://blog.talosintelligence.com/introduction-to-com-usage-by-windows-threats/"
    publisher: Cisco Talos
    role: primary
closed_sources: []
evidence:
  - quote: COM—a fundamental Windows inter-process communication and object activation mechanism—provides attackers convenient access to legitimate Windows functionality while obfuscating malicious activity behind indirect vtable calls
    publisher: Cisco Talos
  - quote: "Task Scheduler COM interfaces (ITaskService, ITaskScheduler) enable scheduled task creation without visible schtasks.exe process execution"
    publisher: Cisco Talos
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
migrated_from: briefs/2026-06-28.md
---

Cisco Talos published a reverse-engineering primer (2026-06-25) on how Windows threats weaponise Component Object Model (COM) interfaces to hide operations inside legitimate service call stacks ([Cisco Talos, 2026-06-25](https://blog.talosintelligence.com/introduction-to-com-usage-by-windows-threats/)). Four technique classes with a shared detection gap — function calls routed through vtable indirection rather than direct API imports limit EDR visibility: ITaskService/ITaskScheduler persistence creates scheduled tasks with no visible `schtasks.exe` (`T1053.005`); `IBackgroundCopyJob` (BITS) moves C2/files attributed to the trusted BITS service process (`T1197`); `IWbemLocator`/WMI blends discovery into `svchost.exe` (`T1082`, `T1518.001`); and DCOM/`IDispatch` enables remote object activation for lateral movement (`T1021.003`). Families studied include Gh0stRAT (ITaskService persistence), Attor (BITS C2 + WMI), Qakbot (WMI) and WarmCookie (ITaskScheduler 1.0). The actionable takeaway for detection engineers: scheduled-task-creation rules keyed on `schtasks.exe`/PowerShell miss COM-based task creation, which emits different event logs; build coverage for task creation where the creating image is unexpected, WMI activity from non-system parents, and BITS jobs created by non-`svchost` processes.
