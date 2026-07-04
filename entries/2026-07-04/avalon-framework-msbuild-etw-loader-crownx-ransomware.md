---
schema: 1
kind: research
horizon: operational
title: "Blackpoint Cyber documents \"Avalon\": a modular framework bundling credential theft, lateral movement and CrownX ransomware behind an MSBuild loader"
headline: "**Avalon** framework chains a signed-binary MSBuild loader, ETW/AMSI patching and the CrownX ransomware payload in one implant"
summary: >
  Blackpoint Cyber's Adversary Pursuit Group detailed Avalon, a previously
  undocumented Windows malware framework delivered by a legal-themed phishing
  lure and an ISO-mounted LNK that proxy-executes inline C# through MSBuild.exe,
  patches ETW/AMSI, and consolidates browser/wallet/credential-manager theft,
  admin-share lateral movement and the embedded CrownX ransomware component in a
  single payload. Detection engineers on Windows fleets — including public-sector
  endpoints — should tighten controls on trusted-developer-utility execution.
discovered_at: "2026-07-04T06:24:38Z"
event_date: "2026-07-02"
run_id: 2026-07-04T0609Z-intel
priority: notable
immediate_action: null
tags: [ransomware, infostealer, phishing, ai-abuse]
regions: [global]
sectors: []
entities: [tool:avalon-malware-framework]
cves: []
sources:
  - url: "https://blackpointcyber.com/blog/avalons-path-from-legal-lure-to-crownx-ransom-capabilities/"
    publisher: "Blackpoint Cyber (Adversary Pursuit Group)"
    date: "2026-07-02"
    role: primary
  - url: "https://thehackernews.com/2026/07/new-avalon-malware-framework-packs.html"
    publisher: "The Hacker News"
    date: "2026-07-03"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Avalon is operationally significant because it consolidates credential theft, persistence, and ransom functionality under one recovered payload rather than distributing them across discrete malware families."
    publisher: "Blackpoint Cyber"
  - quote: "The framework bears the hallmarks of AI assisted development, assembled rapidly from functional components with little regard for tradecraft refinement or operational security"
    publisher: "Blackpoint Cyber"
verification: single-source
sourcing_note: >
  Single first-hand observer: Blackpoint Cyber (Adversary Pursuit Group) vendor
  research. The Hacker News (2026-07-03) is a rewrite of that primary — it
  outbound-links to and names Blackpoint's researchers — and adds no independent
  first-hand observation, so this is single-source in substance under
  prompts/verification.md (rewrites of one report are one source).
confidence: medium
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions:
  - "Block execution of MSBuild.exe, InstallUtil.exe and csc.exe via WDAC or AppLocker on all non-developer endpoints; these trusted developer utilities have no business running on a standard user workstation."
  - "Hunt for MSBuild.exe spawned by cmd.exe with a command line referencing a .tmp or .csproj file outside a build pipeline (Sysmon EID 1, ParentImage=cmd.exe, Image=MSBuild.exe)."
  - "Disable automatic ISO/IMG mounting from mail clients and browser downloads, and alert on LNK files whose displayed icon does not match their target extension delivered inside a mounted image."
  - "Enforce Credential Guard and LSA protection to blunt the framework's credential-harvesting stage."
migrated_from: null
---

Blackpoint Cyber's Adversary Pursuit Group published an analysis of **Avalon**, a modular Windows malware framework recovered from an endpoint and not previously documented ([Blackpoint Cyber, 2026-07-02](https://blackpointcyber.com/blog/avalons-path-from-legal-lure-to-crownx-ransom-capabilities/)). Delivery starts with a spoofed legal-document phishing email pointing to a password-protected archive; the mounted image contains a weaponised LNK that presents a document-themed filename behind a Microsoft Edge icon so the victim believes they are opening a secure PDF rather than launching commands ([Blackpoint Cyber, 2026-07-02](https://blackpointcyber.com/blog/avalons-path-from-legal-lure-to-crownx-ransom-capabilities/)). The shortcut runs `cmd.exe`, which invokes `MSBuild.exe` against a malicious project file carrying inline C# — a trusted-developer-utility proxy-execution chain (`T1127.001`) — and the managed downloader then patches ETW and AMSI functions with return stubs (`T1562.001`) before pulling an encrypted PE payload over HTTPS with certificate-validation bypass.

The recovered payload is notable for consolidating capability that would previously have been spread across several discrete families: browser, cryptocurrency-wallet, Discord/Teams, RDP-session, SSH-key and Windows Credential Manager theft (`T1555`, `T1552.001`), lateral movement over admin shares and scheduled tasks (`T1021.002`, `T1053.005`), and the embedded **CrownX** ransomware component that AES-GCM-encrypts a targeted extension set and disables Volume Shadow Copies, WinRE and System Restore to inhibit recovery (`T1490`, `T1486`) ([Blackpoint Cyber, 2026-07-02](https://blackpointcyber.com/blog/avalons-path-from-legal-lure-to-crownx-ransom-capabilities/)). Secondary reporting describes the framework as bringing these diverse functions under one umbrella ([The Hacker News, 2026-07-03](https://thehackernews.com/2026/07/new-avalon-malware-framework-packs.html)). Defence evasion includes syscall-obfuscation techniques (HalosGate/TartarusGate) and named checks against a broad list of EDR products. Blackpoint assesses that the framework "bears the hallmarks of AI assisted development, assembled rapidly from functional components with little regard for tradecraft refinement or operational security" ([Blackpoint Cyber, 2026-07-02](https://blackpointcyber.com/blog/avalons-path-from-legal-lure-to-crownx-ransom-capabilities/)) — a signal that a single operator can now assemble multi-stage capability quickly, even if the tradecraft is sloppy.

**Defender takeaway:** the operational chokepoint is the same regardless of who or what wrote the code — trusted-developer-utility proxy execution and defence-tampering. Alert on `MSBuild.exe` launched by `cmd.exe` referencing a project/temp file outside a build pipeline (Sysmon EID 1 with parent-image filtering), flag ETW trace-session termination and AMSI in-memory patch signatures via image-load and memory-permission-change telemetry, and block `MSBuild.exe`/`InstallUtil.exe`/`csc.exe` on non-developer endpoints with WDAC or AppLocker. Enforcing Credential Guard and LSA protection reduces the value of a successful credential-harvesting stage.
