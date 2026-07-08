---
schema: 1
kind: threat
horizon: operational
title: "CrySome RAT freight-phishing chain: AMSI bypass, ICMLuaUtil UAC bypass and an open-source Defender-disruption tool"
headline: "CrySome RAT delivered via freight-rate phishing, chaining AMSI bypass, ICMLuaUtil UAC bypass and WinDefCtl"
summary: >
  LevelBlue SpiderLabs documented a freight-rate-confirmation phishing chain delivering CrySome, a .NET RAT, via a batch downloader, PowerShell AMSI bypass, ICMLuaUtil UAC bypass and the open-source WinDefCtl Defender-disruption utility. The operators lean almost entirely on off-the-shelf components, so detection must target the individual behaviours, not the final payload.
discovered_at: "2026-07-08T20:35:00Z"
event_date: 2026-07-06
run_id: 2026-07-08T2009Z-intel
priority: notable
immediate_action: null
tags:
  - phishing
  - infostealer
regions:
  - global
sectors:
  - transport
entities:
  - "tool:crysome-rat"
cves: []
sources:
  - url: "https://www.levelblue.com/blogs/spiderlabs-blog/from-phishing-to-persistence-a-crysome-rat-infection-chain-analysis"
    publisher: "LevelBlue (Trustwave) SpiderLabs"
    date: "2026-07-06"
    role: primary
closed_sources: []
evidence:
  - quote: "By combining an AMSI bypass, an open-source Defender tampering utility, and the modular CrySome RAT client, the operators minimize custom development while still achieving privilege escalation, defense evasion, persistence, credential theft, and remote access."
    publisher: "LevelBlue (Trustwave) SpiderLabs"
  - quote: "The actor then targeted host defenses by executing WinDefCtl, an open-source Defender disruption utility, masquerading as svchost.exe from %TEMP%."
    publisher: "LevelBlue (Trustwave) SpiderLabs"
verification: single-source
sourcing_note: "Single reputable research-lab primary (LevelBlue SpiderLabs); no independent corroboration of this specific campaign found this run — generic CrySome-capability write-ups exist but do not cover this freight-phishing chain. Reported as the lab's own original analysis."
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Enforce Microsoft Defender tamper protection via policy so exclusion paths cannot be added by a standard admin token; alert on ICMLuaUtil/CMSTPLUA COM instantiation outside expected system processes."
  - "Hunt for scheduled tasks named 'CrysomeLoader' on a 5-minute trigger, svchost.exe running from %TEMP%, and batch→PowerShell chains carrying AMSI-bypass indicators (Sysmon EID 1)."
migrated_from: null
---

LevelBlue SpiderLabs documented a multi-stage infection chain delivering CrySome RAT — a modular .NET remote-access trojan the lab notes has been covered in prior public reporting — through spear-phishing emails impersonating freight-rate confirmations ([LevelBlue SpiderLabs, 2026-07-06](https://www.levelblue.com/blogs/spiderlabs-blog/from-phishing-to-persistence-a-crysome-rat-infection-chain-analysis)). Victims reach a fake portal hosting a batch-file downloader that launches PowerShell with an AMSI bypass (`T1059.001`, `T1562.001`) to fetch a stage-1 binary, which performs a UAC bypass via the ICMLuaUtil COM interface (`T1548.002`). Stage 2 adds Microsoft Defender exclusions and drops WinDefCtl — an open-source Defender-disruption utility masquerading as `svchost.exe` from `%TEMP%` — to disable real-time protection before launching the RAT. Persistence is a scheduled task ("CrysomeLoader") re-firing every five minutes (`T1053.005`); the RAT provides hidden VNC, arbitrary command execution and Chromium-browser credential theft, defeating Chrome's App-Bound Encryption via a decryptor DLL (`T1555.003`). **Defender takeaway:** the operators combine almost entirely open-source/off-the-shelf components rather than custom development, so — as LevelBlue notes — detecting the individual behavioural stages (AMSI-bypass PowerShell, ICMLuaUtil COM abuse, Defender-exclusion registry writes under `Software\Microsoft\Windows Defender\Exclusions`, svchost.exe from a non-System32 path) gives multiple disruption points before the RAT establishes; freight/logistics lures make transport-sector helpdesks a natural target, but the chain is theme-agnostic and transferable.
