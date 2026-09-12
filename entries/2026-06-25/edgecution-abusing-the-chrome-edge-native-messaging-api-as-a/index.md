---
schema: 1
kind: threat
title: "Edgecution: abusing the Chrome/Edge Native Messaging API as a browser-sandbox-to-host bridge"
headline: "Edgecution: abusing the Chrome/Edge Native Messaging API as a browser-sandbox-to-host bridge"
summary: "Background. Browser-extension-to-host pivoting is not a new idea — the Native Messaging API (the stdio IPC channel that lets a browser extension talk to a registered local executable) has been a documented abuse surface for years, and EDR coverage of browser child-processes remains uneven."
discovered_at: "2026-06-25T04:59:10Z"
event_date: 2026-06-24
run_id: 2026-06-25-da7fbd23
priority: notable
immediate_action: null
tags:
  - organized-crime
  - ransomware
  - identity
  - phishing
regions:
  - global
sectors:
  - finance
  - public-sector
  - technology
entities:
  - "tool:edgecution-payouts-kings"
cves: []
sources:
  - url: "https://www.zscaler.com/blogs/security-research/payouts-king-ransomware-initial-access-broker-deploys-new-edgecution"
    publisher: Zscaler ThreatLabz — Payouts King / Edgecution
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/malicious-edge-extension-abuses-native-messaging-as-bridge-to-malware/"
    publisher: BleepingComputer
    role: corroborating
closed_sources: []
evidence:
  - quote: "Edgecution has two components: a Microsoft Edge browser extension that beacons to a command-and-control (C2) server and relays host-based commands to a Python-based backdoor"
    publisher: BleepingComputer citing Zscaler ThreatLabz
  - quote: "the attackers gain direct host access, enabling them to manipulate the local filesystem, launch processes, and execute arbitrary code on the compromised host"
    publisher: BleepingComputer citing Zscaler ThreatLabz
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: true
deep_dive_category: endpoint-rce
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-25.md
---

**Background.** Browser-extension-to-host pivoting is not a new idea — the Native Messaging API (the stdio IPC channel that lets a browser extension talk to a registered local executable) has been a documented abuse surface for years, and EDR coverage of browser child-processes remains uneven. What Zscaler ThreatLabz documents in Edgecution is this class turned into a working, in-the-wild initial-access toolset operated by the Payouts Kings group ([Zscaler ThreatLabz, 2026-06-23](https://www.zscaler.com/blogs/security-research/payouts-king-ransomware-initial-access-broker-deploys-new-edgecution) · [BleepingComputer, 2026-06-24](https://www.bleepingcomputer.com/news/security/malicious-edge-extension-abuses-native-messaging-as-bridge-to-malware/)).

**Initial access.** The chain begins with a Microsoft Teams social-engineering lure: attackers impersonate IT support and direct the victim to a fraudulent Outlook "update" portal (`T1204.002` [User Execution: Malicious File](https://attack.mitre.org/techniques/T1204/002/), preceded by `T1656` impersonation). The download is a ZIP bundling an embedded Python 3.13.3 runtime, a malicious Edge extension presented as an "Edge Monitoring Agent", and the native-messaging host components that register the extension-to-executable channel.

**Sandbox-to-host bridge.** The extension runs inside a headless (hidden-window) Edge instance invisible to the user (`T1564.003` [Hide Artifacts: Hidden Window](https://attack.mitre.org/techniques/T1564/003/)), beacons to C2 hosted on `cloudfront.net` subdomains over HTTPS (`T1071.001` [Application Layer Protocol: Web Protocols](https://attack.mitre.org/techniques/T1071/001/)), and relays received commands across the Native Messaging stdio channel (`T1559` [Inter-Process Communication](https://attack.mitre.org/techniques/T1559/)) to a Python backdoor running on the host. The design point is evasion: controls that watch the browser process tree but not the native-messaging-host child process never see the host commands cross the boundary.

**On-host capability.** The Python backdoor (`T1059.006` [Command and Scripting Interpreter: Python](https://attack.mitre.org/techniques/T1059/006/)) implements shell and PowerShell command execution, arbitrary code execution, file writes, process enumeration and system reconnaissance — a full IAB foothold from which ransomware affiliates can be sold access. Zscaler reports the observed C2 used `cloudfront.net` subdomains hosted on AWS, which blend with legitimate CDN traffic.

**Hunt and detection concepts.** (1) Process-tree rule: `msedge.exe` spawning a native-messaging host executable followed by a Python interpreter invocation is the kill-chain signature — the host process is registered under `HKCU\Software\Microsoft\Edge\NativeMessagingHosts\`. (2) Registry monitoring: additions under that key by anything other than a legitimate installer (Sysmon EID 13). (3) Process telemetry: a headless/hidden Edge instance launched outside normal user interaction (Sysmon EID 1, command-line flags indicating an automation/headless profile). (4) Network: CloudFront-subdomain beaconing originating from `msedge.exe` or a Python child in an environment that does not normally use those endpoints.

**Hardening.** Enterprise browsers should restrict extension installation to approved publisher IDs via Group Policy (`ExtensionInstallAllowlist`, and `BlockExternalExtensions`), and allow-list Native Messaging hosts explicitly. Blocking user-profile (`HKCU`) Native Messaging host registration via AppLocker/WDAC removes this persistence and bridging path. Because the entry point is a Teams IT-helpdesk lure, the same control that blunts ClickFix/FileFix — preventing users from running attacker-supplied scripts and constraining who can deliver Teams messages from outside the tenant — applies here too.
