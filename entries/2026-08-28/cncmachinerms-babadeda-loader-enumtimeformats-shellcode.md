---
schema: 1
kind: threat
horizon: operational
title: "CNCMachineRMS — an undocumented remote-access trojan delivered through a four-stage BabaDeda loader chain that smuggles shellcode via a benign Windows date-formatting API"
headline: "A ClickFix lure abuses a signed IBM SPSS binary's own scripting engine, then hides its final shellcode injection inside a Windows time-formatting call"
summary: >
  LevelBlue SpiderLabs documents CNCMachineRMS, a previously undocumented 1.14 MB x64 remote-
  access trojan delivered through a four-stage BabaDeda loader chain. A ClickFix-style lure
  launches a legitimately signed IBM SPSS IDE executable, abusing its scripting engine to load a
  malicious DLL; the final stage smuggles shellcode into execution via EnumTimeFormatsEx, a benign
  date-formatting Windows API that hides the injection point from analysts watching conventional
  process-injection calls.
discovered_at: "2026-08-28T06:30:00Z"
updated_at: null
event_date: "2026-08-10"
run_id: 2026-08-28T0409Z-intel
priority: notable
immediate_action: null
tags: [infostealer]
regions: [global]
sectors: [public-sector]
entities: [malware:cncmachinerms]
techniques: [T1204.002, T1574.001, T1055, T1027, T1547]
affected_products: ["Microsoft Windows", "IBM SPSS Statistics"]
cves: []
sources:
  - url: "https://www.levelblue.com/blogs/spiderlabs-blog/cncmachinerms-the-undocumented-rat-at-the-end-of-a-babadeda-chain"
    publisher: "LevelBlue SpiderLabs"
    date: "2026-08-10"
    role: primary
closed_sources: []
evidence:
  - quote: "A ClickFix lure launches a legitimately signed IBM SPSS IDE executable, whose scripting engine is abused to load a malicious DLL."
    publisher: "LevelBlue SpiderLabs"
  - quote: "The final stage smuggles shellcode into execution via EnumTimeFormatsEx, a benign date-formatting API."
    publisher: "LevelBlue SpiderLabs"
  - quote: "It takes a screenshot on first contact, then beacons every 600 seconds, with seven persistence mechanisms."
    publisher: "LevelBlue SpiderLabs"
verification: single-source
sourcing_note: >
  LevelBlue SpiderLabs is the sole publisher; its full technical report is a companion PDF not
  independently fetched this run — the blog post itself carries the load-bearing technical detail
  used above.
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

LevelBlue SpiderLabs documents CNCMachineRMS, a previously undocumented 1.14 MB x64 remote-access trojan delivered through a four-stage BabaDeda loader chain. A ClickFix-style lure launches a legitimately signed IBM SPSS IDE executable (`WinWrapIDE.exe`), abusing its scripting engine to load a malicious DLL: "a ClickFix lure launches a legitimately signed IBM SPSS IDE executable, whose scripting engine is abused to load a malicious DLL" ([LevelBlue SpiderLabs, 2026-08-10](https://www.levelblue.com/blogs/spiderlabs-blog/cncmachinerms-the-undocumented-rat-at-the-end-of-a-babadeda-chain)). Four decoy DLLs then load in sequence through standard Windows DLL import resolution before the final stage smuggles its shellcode into execution via `EnumTimeFormatsEx`, a benign date-formatting Windows API: "the final stage smuggles shellcode into execution via EnumTimeFormatsEx, a benign date-formatting API" ([LevelBlue SpiderLabs, 2026-08-10](https://www.levelblue.com/blogs/spiderlabs-blog/cncmachinerms-the-undocumented-rat-at-the-end-of-a-babadeda-chain)) — a technique that hides the injection point from analysts looking for conventional process-injection APIs.

The final implant has no import table and resolves its APIs by hash at runtime, builds its strings on the stack rather than storing them statically, uses a custom C2 protocol, takes a screenshot on first contact, beacons roughly every 600 seconds, and installs seven distinct persistence mechanisms: "it takes a screenshot on first contact, then beacons every 600 seconds, with seven persistence mechanisms" ([LevelBlue SpiderLabs, 2026-08-10](https://www.levelblue.com/blogs/spiderlabs-blog/cncmachinerms-the-undocumented-rat-at-the-end-of-a-babadeda-chain)). Capabilities include interactive shell access, file management, screen capture and local account backdoors. BabaDeda-chain ClickFix lures are a recurring initial-access vector across the sectors this pipeline tracks, making the delivery mechanism as relevant as the payload itself.

**Triage:** the API-hashing and stack-built-strings design defeats static string-based detection, so behavioural signals carry the weight here — a legitimately signed application (IBM SPSS or any similarly abused signed binary) spawning a scripting-engine child process that loads an unsigned DLL is the first anomaly, and a process invoking `EnumTimeFormatsEx` immediately followed by execution flow transferring into memory it just wrote (rather than into a legitimate formatting routine) is the discriminator against the API's ordinary, benign use — no legitimate application calls this function as a prelude to code execution elsewhere in its own address space.
