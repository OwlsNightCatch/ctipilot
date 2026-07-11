---
schema: 1
kind: threat
horizon: operational
title: The Gentlemen ransomware — Microsoft publishes full technical dissection of the Storm-2697 Go-encryptor
headline: The Gentlemen ransomware — Microsoft publishes full technical dissection of the Storm-2697 Go-encryptor
summary: "UPDATE (originally covered 2026-05-20; consolidated in weekly W21): Microsoft Threat Intelligence published a full dissection of The Gentlemen ransomware on 2026-05-28, giving Storm-2697 a much sharper technical profile than the victim-list reporting available in week 21."
discovered_at: "2026-05-29T05:00:14Z"
event_date: 2026-05-28
run_id: 2026-05-29-c7f56b00
priority: notable
immediate_action: null
tags:
  - ransomware
  - actively-exploited
  - identity
  - organized-crime
regions:
  - europe
  - switzerland
  - global
sectors:
  - healthcare
  - manufacturing
  - education
entities:
  - "actor:thegentlemen"
cves: []
sources:
  - url: "https://www.microsoft.com/en-us/security/blog/2026/05/28/the-gentlemen-ransomware-dissecting-a-self-propagating-go-encryptor/"
    publisher: Microsoft Threat Intelligence — The Gentlemen dissection
    role: primary
  - url: "https://www.huntress.com/blog/the-gentlemen-ransomware-defense-evasion-ttps"
    publisher: Huntress Labs
    role: corroborating
  - url: "https://research.checkpoint.com/2026/thus-spoke-the-gentlemen/"
    publisher: Check Point Research
    role: corroborating
  - url: "https://thedfirreport.com/2026/05/11/flash-alert-etherrat-and-tuktuk-c2-end-in-the-gentleman-ransomware/"
    publisher: The DFIR Report — flash alert
    role: corroborating
closed_sources: []
evidence:
  - quote: Storm-2697 affiliates that combines per-file ephemeral key encryption with an aggressive self-propagation module to deploy itself across an entire network using series of simultaneous lateral movement techniques per target
    publisher: Microsoft Threat Intelligence
  - quote: "Both incidents employed Scheduled Tasks and PowerShell commands to disable Microsoft Defender, add antivirus exclusions, and clear Security/System/Application Event Logs"
    publisher: Huntress Labs
verification: multi-source
sourcing_note: "migration: update target unresolved (originally covered 2026-05-20)"
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-29.md
---

**UPDATE (originally covered 2026-05-20; consolidated in [weekly W21](/weekly/2026-W21/)):** [Microsoft Threat Intelligence published a full dissection of The Gentlemen ransomware on 2026-05-28](https://www.microsoft.com/en-us/security/blog/2026/05/28/the-gentlemen-ransomware-dissecting-a-self-propagating-go-encryptor/), giving Storm-2697 a much sharper technical profile than the victim-list reporting available in week 21. The encryptor is a single-binary Go executable (obfuscated through Garble to strip symbol tables), uses Curve25519 + XChaCha20 with per-file ephemeral keys (no bulk-decryption shortcut), and ships a self-propagation module that **executes a series of lateral-movement techniques in parallel per host** — PsExec, WMIC, scheduled tasks, services, PowerShell remoting — maximising the probability that at least one pivot path succeeds in any AD-joined environment.

[Check Point Research's 2026-05-13 writeup](https://research.checkpoint.com/2026/thus-spoke-the-gentlemen/) adds the actor-side context that Microsoft's dissection does not — Check Point counts approximately 332 victim organisations on the operator's leak site, and documents that on Domain Admin compromise The Gentlemen deploys itself across the estate through a Group Policy Object linked at all relevant OUs. [Huntress Labs' 2026-05-21 IR report](https://www.huntress.com/blog/the-gentlemen-ransomware-defense-evasion-ttps) corroborates the defense-evasion playbook: PowerShell disables Microsoft Defender real-time monitoring (`Set-MpPreference -DisableRealtimeMonitoring`), stops `WinDefend`, adds broad `Add-MpPreference -ExclusionProcess` and drive-level exclusions, disables Controlled Folder Access, and clears Security / System / Application event logs (EID 104, EID 1102). Huntress documented two April / May 2026 incidents whose entry vector was RDP with compromised credentials, lateral movement reached domain controllers via the `NETLOGON` share and SCCM's `CcmExec.exe`, and process names were masqueraded as `svchost32.exe`. [The DFIR Report's 2026-05-11 alert](https://thedfirreport.com/2026/05/11/flash-alert-etherrat-and-tuktuk-c2-end-in-the-gentleman-ransomware/) confirmed a related chain in which EtherRAT (delivered via a malicious Sysinternals MSI) and TukTuk C2 preceded Gentleman deployment. Microsoft's Defender detection name is `Ransom:Win64/Gentlemen.A`; recommended Attack Surface Reduction posture per Microsoft's [ASR rules reference](https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-reference) is *Block process creations originating from PsExec and WMI commands* combined with EDR-in-block-mode enforcement.

Material new development vs. last coverage: full encryption + propagation mechanism, named-cluster identity (Storm-2697), the GPO-spread pathway documented by Check Point Research, and Check Point's count of approximately 332 victims. Detection focus: hunt for `wevtutil cl Security|System|Application` chained with `sc stop WinDefend` or `msconfig`; flag `svchost32.exe` spawned outside `%SystemRoot%\System32`; alert on `CcmExec.exe` launching non-SCCM payloads. Hardening: enforce SMB signing GPO, restrict GPO-creation rights to a hardened OU, enable Credential Guard, monitor Event ID 5136 for GPO modifications and 5140 for the hidden `share` SMB share.
