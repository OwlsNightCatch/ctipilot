---
schema: 1
kind: vulnerability
horizon: operational
title: "Turla's STOCKSTAY: a four-component .NET backdoor for diplomatic intelligence collection"
headline: "Turla's STOCKSTAY: a four-component .NET backdoor for diplomatic intelligence collection"
summary: "Background. Google Threat Intelligence Group (GTIG, formerly Mandiant) published a full technical analysis of STOCKSTAY on 2026-06-25, a modular .NET backdoor it attributes with high confidence to Turla — also tracked as Secret Blizzard, SUMMIT and FSB Center 16 — with activity dating to December 2022 (Google …"
discovered_at: "2026-06-27T05:17:52Z"
event_date: 2026-06-26
run_id: 2026-06-27-40e791d4
priority: notable
immediate_action: null
tags:
  - nation-state
  - espionage
  - russia-nexus
regions:
  - europe
  - switzerland
  - global
sectors:
  - public-sector
  - defense
entities:
  - "report:gtig-europe-2025"
cves:
  - id: CVE-2025-8088
    cvss: n/a
    epss: null
    type: null
    vector: user-interaction
    auth: post-auth
    status:
      - exploited
      - patch-available
sources:
  - url: "https://cloud.google.com/blog/topics/threat-intelligence/stockstay-turla-intelligence-gathering"
    publisher: Google Cloud / GTIG
    role: primary
  - url: "https://therecord.media/russia-turla-espionage-ukraine-stockstay-malware"
    publisher: The Record
    role: corroborating
  - url: "https://thehackernews.com/2026/06/google-details-turlas-new-stockstay.html"
    publisher: The Hacker News
    role: corroborating
closed_sources: []
evidence:
  - quote: Background.
    publisher: ctipilot v2 brief (migrated)
verification: multi-source
sourcing_note: "migration: evidence backfilled from v2 brief body (item predates the Evidence footer field)"
confidence: high
update_of: null
references: []
deep_dive: true
deep_dive_category: apt-campaign
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-27.md
---

**Background.** Google Threat Intelligence Group (GTIG, formerly Mandiant) published a full technical analysis of STOCKSTAY on 2026-06-25, a modular .NET backdoor it attributes with high confidence to **Turla** — also tracked as Secret Blizzard, SUMMIT and FSB Center 16 — with activity dating to December 2022 ([Google Cloud / GTIG, 2026-06-25](https://cloud.google.com/blog/topics/threat-intelligence/stockstay-turla-intelligence-gathering)). GTIG ties STOCKSTAY to Turla's long-running **Kazuar** implant lineage through shared code: the `K1MORPHER` Squirrel3-based string obfuscator Turla introduced in April 2025, identical environmental-keying logic, and the same component-separation design pattern — placing this tool in the same toolset GTIG and others have tracked across European diplomatic targeting for years ([The Record, 2026-06-26](https://therecord.media/russia-turla-espionage-ukraine-stockstay-malware)). Primary targets are Ukrainian government and military organisations and European entities with Italian foreign-policy interests.

**Architecture and mechanics.** STOCKSTAY is partitioned into four .NET assemblies that communicate over Windows `WM_COPYDATA` inter-process messages, deliberately decoupling the network layer from command execution. `MARKETMAKER` is the downloader/installer that establishes Registry Run-key persistence masquerading as `MicrosoftUpdateOneDrive` ([`T1547.001`](https://attack.mitre.org/techniques/T1547/001/)); `STOCKMARKET` ("cor") is the orchestrator that generates a 4096-bit RSA key pair on first run; `STOCKBROKER` ("net") is a proxy-aware WebSocket tunneller built on the open-source `websocket-sharp` library; and `STOCKTRADER` ("sys") is the backdoor executor supporting 13 commands (directory listing, file get/put, process execution, registry read/write/delete, screenshot capture, WMI-based system reconnaissance, archive unpacking, and self-destruct). Configuration is AES-encrypted using hostname/domain-name **environmental keying** ([`T1480`](https://attack.mitre.org/techniques/T1480/)) once past the reconnaissance phase, so the payload will not decrypt or execute off-target — a standard Turla anti-analysis measure.

**Command-and-control.** C2 responses are wrapped in an RSA-4096-encrypted "CryptoContainer" JSON structure and tunnelled over encrypted WebSocket sessions hosted on **legitimate PaaS platforms (Render.com, Glitch)** ([`T1071.001`](https://attack.mitre.org/techniques/T1071/001/)). The controller — a Python Tornado WebSocket server storing victim data in a SQLite database — was found in a public GitHub repository, and the use of third-party PaaS prevents the platform operator from introspecting the encrypted traffic. The implant enforces working hours (09:00–18:00, Mon–Fri) to blend with normal activity.

**Delivery / kill chain.** Initial access is via spearphishing ([`T1566.001`/`.002`](https://attack.mitre.org/techniques/T1566/)) using diplomatic-themed lures (drone content, military logistics, diplomatic-education platforms), with malicious RDP configuration files and RAR archives exploiting **WinRAR path traversal `CVE-2025-8088`** for code drop, followed by MSI/HTA execution. STOCKSTAY is then installed, keys to its environment, establishes Run-key persistence, and beacons out over PaaS-hosted WebSockets — staging the operator's interactive command set (`T1059`) for collection (`T1005`) and exfiltration over the C2 channel ([`T1041`](https://attack.mitre.org/techniques/T1041/)). GTIG notes deployment alongside other confirmed Turla tools (`WILDDAY`, `DIAMONDBACK`).

**Detection concepts (no IOCs).** Alert on outbound WebSocket connections to `*.onrender.com` / `*.glitch.me` from non-browser processes; `WM_COPYDATA` messages between unrelated processes in EDR telemetry (Sysmon EID 8/10 process-injection/access correlation); Registry Run-key creation pointing at user-space paths masquerading as Microsoft/OneDrive updaters (Sysmon EID 13 / Windows EID 4657); LNK or RDP-config writes into staging directories (Sysmon EID 11); and the WinRAR `CVE-2025-8088` exploitation pattern (archive extraction writing files outside the target directory). GTIG published YARA and Google SecOps detection rules with the report.

**Hardening / mitigation.** Patch WinRAR to 7.11+ to close `CVE-2025-8088`; enable AMSI and ETW for .NET assemblies and block the AppDomainManager-hijack DLL-placement path; apply GPO to restrict RDP-config auto-connection; and where not operationally required, block Render/Glitch WebSocket egress at the perimeter for diplomat and ministry workstations. For Swiss federal and cantonal foreign-affairs, defence and diplomatic environments, the named Italian-foreign-policy targeting puts this squarely in scope.
