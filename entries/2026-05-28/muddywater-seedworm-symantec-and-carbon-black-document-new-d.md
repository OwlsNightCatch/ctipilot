---
schema: 1
kind: research
horizon: operational
title: "MuddyWater / Seedworm — Symantec and Carbon Black document new DLL-side-loading pair via signed Fortemedia and SentinelOne binaries, ChromElevator for Chromium App-Bound Encryption bypass, Node.js orchestration"
headline: "MuddyWater / Seedworm — Symantec and Carbon Black document new DLL-side-loading pair via signed Fortemedia and SentinelOne binaries, ChromElevator for Chromium"
summary: "Symantec's Threat Hunter Team and Broadcom's Carbon Black published findings on 2026-05-12 documenting a Q1 2026 MuddyWater (a.k.a. Seedworm, Static Kitten, MERCURY, TEMP.Zagros — attributed to Iran's Ministry of Intelligence and Security) espionage campaign across at least nine organisations on four continents."
discovered_at: "2026-05-28T05:00:08Z"
event_date: 2026-05-26
run_id: 2026-05-28-3e33200a
priority: notable
immediate_action: null
tags:
  - nation-state
  - espionage
  - iran-nexus
regions:
  - middle-east
  - apac
  - europe
sectors:
  - education
  - public-sector
  - manufacturing
  - finance
  - aviation
entities:
  - "actor:muddywater"
cves: []
sources:
  - url: "https://www.security.com/threat-intelligence/iran-seedworm-electronics"
    publisher: Symantec / Broadcom Threat Intelligence (2026-05-12)
    role: primary
  - url: "https://thehackernews.com/2026/05/muddywater-uses-dll-side-loading-in.html"
    publisher: The Hacker News (2026-05-26)
    role: corroborating
  - url: "https://industrialcyber.co/threats-attacks/symantec-uncovers-iran-linked-seedworm-espionage-campaign-targeting-airport-government-manufacturing-sectors/"
    publisher: Industrial Cyber (2026-05-13)
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
migrated_from: briefs/2026-05-28.md
---

Symantec's Threat Hunter Team and Broadcom's Carbon Black published findings on 2026-05-12 documenting a Q1 2026 MuddyWater (a.k.a. Seedworm, Static Kitten, MERCURY, TEMP.Zagros — attributed to Iran's Ministry of Intelligence and Security) espionage campaign across at least nine organisations on four continents. The story re-surfaced this run via fresh aggregator coverage on 2026-05-26 (The Hacker News) — included in window on that basis. Named victim categories include industrial and electronics manufacturing, education and public-sector bodies, financial services, and an international airport in the Middle East ([Symantec / Broadcom Threat Intelligence, 2026-05-12](https://www.security.com/threat-intelligence/iran-seedworm-electronics); [The Hacker News, 2026-05-26](https://thehackernews.com/2026/05/muddywater-uses-dll-side-loading-in.html); [Industrial Cyber, 2026-05-13](https://industrialcyber.co/threats-attacks/symantec-uncovers-iran-linked-seedworm-espionage-campaign-targeting-airport-government-manufacturing-sectors/)).

The differentiating TTPs from prior MuddyWater coverage are twofold. First, DLL side-loading via two pairs of *legitimately signed third-party binaries*: Fortemedia audio-driver binary `fmapp.exe` side-loading a malicious `fmapp.dll`; SentinelOne's `sentinelmemoryscanner.exe` side-loading a rogue `sentinelagentcore.dll` — abuse of a signed security-product binary specifically chosen to bypass signature-based detection. Both malicious DLLs embed `ChromElevator`, an open-source post-exploitation tool that bypasses Chromium App-Bound Encryption to extract passwords, cookies and payment-card data without triggering AV. Second, orchestration moved to Node.js: `node.exe` appears as a parent-process ancestor of `cmd.exe` before any operator commands — i.e. a Node.js script (not a human operator) drives the kill chain. PowerShell scripts pulled from a staging server perform discovery (`T1087`, `T1482`), screenshot capture, SAM-hive theft via VSS (`T1003.002`), and SOCKS5 reverse-proxy tunnelling (`T1090.003`). A credential harvester calls `CredUIPromptForWindowsCredentialsW` to display a Windows security dialogue and trick targets into entering credentials. A Kerberos TGT extractor via GSS-API was also observed.

**Why it matters to us:** signed-binary side-loading abusing a security-product binary is the highest-value evasion class — signature-based controls are bypassed by design. Detection: Sysmon EID 7 image-loads from `fmapp.exe` or `sentinelmemoryscanner.exe` outside their expected installation directories; alert on `node.exe` as a parent of `cmd.exe` or `powershell.exe -enc` in non-developer environments; flag `CredUIPromptForWindowsCredentialsW` calls from non-standard parents. Hardening: AppLocker / WDAC enforcing signed-and-known-path DLL loads; restrict `node.exe` execution to development OUs.
