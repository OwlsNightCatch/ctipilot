---
schema: 1
kind: research
horizon: operational
title: "Unit 42: Chinese-speaking cluster CL-STA-1062 deploys the new TinyRCT .NET backdoor against SE-Asian government and energy targets via AppDomainManager injection"
headline: "Unit 42: Chinese-speaking cluster CL-STA-1062 deploys the new TinyRCT .NET backdoor against SE-Asian government and energy targets via AppDomainManager"
summary: "Palo Alto Unit 42 (2026-06-25) documented CL-STA-1062, a Chinese-speaking cluster overlapping with Cisco Talos's UAT-7237, targeting government and state-owned energy infrastructure across Southeast Asia (Unit 42, 2026-06-25; The Hacker News, 2026-06-26)."
discovered_at: "2026-06-28T05:05:41Z"
event_date: 2026-06-26
run_id: 2026-06-28-1b30612a
priority: notable
immediate_action: null
tags:
  - nation-state
  - espionage
  - china-nexus
regions:
  - apac
  - global
sectors:
  - public-sector
  - energy
entities: []
cves: []
sources:
  - url: "https://unit42.paloaltonetworks.com/cl-sta-1062-tinyrct-backdoor/"
    publisher: Palo Alto Networks Unit 42
    role: primary
  - url: "https://thehackernews.com/2026/06/chinese-speaking-apt-deploys-new.html"
    publisher: The Hacker News
    role: corroborating
closed_sources: []
evidence:
  - quote: "TinyRCT is a .NET-based RAT with capabilities including arbitrary command execution, file enumeration and exfiltration, screen capture, and self-destruct functionality. The malware communicates via HTTP with AES-128 encrypted payloads."
    publisher: Unit 42
  - quote: "CL-STA-1062 represents a sustained, sophisticated threat targeting critical infrastructure across Asia-Pacific."
    publisher: Unit 42
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
migrated_from: briefs/2026-06-28.md
---

Palo Alto Unit 42 (2026-06-25) documented **CL-STA-1062**, a Chinese-speaking cluster overlapping with Cisco Talos's UAT-7237, targeting government and state-owned energy infrastructure across Southeast Asia ([Unit 42, 2026-06-25](https://unit42.paloaltonetworks.com/cl-sta-1062-tinyrct-backdoor/); [The Hacker News, 2026-06-26](https://thehackernews.com/2026/06/chinese-speaking-apt-deploys-new.html)). Initial access is via internet-facing web apps and ASPX web shells (`T1505.003`), pivoting to a custom .NET backdoor, **TinyRCT**, delivered through AppDomainManager injection (`T1574.014`): a benign signed `chrome_setup.exe` ships in a ZIP alongside a malicious `chrome_setup.exe.config`, causing the .NET CLR to load `MyAppDomainManager.dll` from the same directory and bootstrap TinyRCT *in-process* — no child process, so it is low-visibility to EDR. TinyRCT beacons over HTTP with AES-128-CBC payloads, supports command execution via `cmd.exe`, chunked file exfiltration, and screen capture, and self-terminates unless run from `%LOCALAPPDATA%` or `%USERPROFILE%\Downloads` (anti-sandbox). Observed tooling includes Mimikatz, JuicyPotato and SoftEther VPN masqueraded as `vmtools.exe`. The defender value is the technique: `T1574.014` AppDomainManager injection is widely under-detected, and the same web-shell-to-in-process-.NET pattern is directly applicable to European public-sector web estates. Hunt for .NET `.config` files written into user-writable directories adjacent to signed executables, and DLL loads of `MyAppDomainManager.dll` from a signed PE's own directory (Sysmon EID 7).
