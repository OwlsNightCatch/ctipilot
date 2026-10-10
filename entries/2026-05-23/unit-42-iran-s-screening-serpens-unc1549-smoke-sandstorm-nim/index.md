---
schema: 1
kind: research
title: >
  Unit 42 — Iran's Screening Serpens (UNC1549 / Smoke Sandstorm / Nimbus Manticore):
  AppDomainManager hijacking silently disables ETW + strong-name checks in six new RATs
headline: >
  Unit 42 — Iran's Screening Serpens (UNC1549 / Smoke Sandstorm / Nimbus Manticore):
  AppDomainManager hijacking silently disables ETW + strong-name checks in six
summary: >
  Iran's Screening Serpens (UNC1549) operationalises AppDomainManager hijacking against aerospace,
  defence and telecom. Unit 42 documents six new RAT variants (four MiniUpdate, two MiniJunk V2)
  deployed via legitimate Microsoft .NET binaries paired with weaponised .runtimeconfig.json files
  that silently disable ETW tracing and strong-name validation before the RAT runs (Unit 42,
  2026-05-22).
discovered_at: "2026-05-23T05:00:06Z"
updated_at: "2026-05-27T05:00:04Z"
event_date: 2026-05-22
run_id: 2026-05-23-852c21c8
priority: high
immediate_action: null
tags:
  - nation-state
  - espionage
  - iran-nexus
regions:
  - middle-east
  - global
  - europe
  - us
sectors:
  - defense
  - aviation
  - telco
entities:
  - "actor:screening-serpens-unc1549-smoke-sandstorm-nimbus-manticore-iran-apt"
techniques: []
affected_products: []
cves: []
sources:
  - url: "https://unit42.paloaltonetworks.com/tracking-iran-apt-screening-serpens/"
    publisher: Unit 42
    role: primary
  - url: "https://www.cybersecuritydive.com/news/iran-cyberattacks-espionage-us-israel-uae/820990/"
    publisher: Cybersecurity Dive
    role: corroborating
  - url: "https://research.checkpoint.com/2026/fast-and-furious-nimbus-manticore-operations-during-the-iranian-conflict/"
    publisher: "Check Point Research, 2026-05-22"
    role: primary
  - url: "https://thehackernews.com/2026/05/iranian-hackers-deploy-minifast-and.html"
    publisher: "The Hacker News, 2026-05-26"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification: null
watchlist_hit: false
actions: []
updates:
  - at: "2026-05-27T05:00:04Z"
    run_id: 2026-05-27-0b6f12dd
    type: update
    summary: >
      UPDATE (originally covered 2026-05-23): Following Unit 42's coverage of UNC1549 / Screening
      Serpens AppDomainManager hijacking, Check Point Research (published 2026-05-22, widely
      re-reported this week) adds material technical depth on three February–April 2026 campaign waves
      keyed to Operation Epic Fury (Check …
    fields:
      - regions
      - sources
      - body
    merged_from: 2026-05-27/nimbus-manticore-unc1549-screening-serpens-check-point-detai
migrated_from: briefs/2026-05-23.md
---

Unit 42 published a comprehensive write-up on **Screening Serpens** (a.k.a. UNC1549, Smoke Sandstorm, Nimbus Manticore) on 2026-05-22 covering operations from February through April 2026 timed to the onset of the U.S.–Israeli Middle East conflict that began 2026-02-28 ([Unit 42, 2026-05-22](https://unit42.paloaltonetworks.com/tracking-iran-apt-screening-serpens/) · [Cybersecurity Dive, 2026-05-22](https://www.cybersecuritydive.com/news/iran-cyberattacks-espionage-us-israel-uae/820990/)). The group deployed new RAT variants across two malware families: **MiniUpdate** in four variants used between 2026-03-26 and 2026-04-17 with lures impersonating aviation, healthcare and financial-services firms, and **MiniJunk V2** in two variants used between 2026-02-17 and 2026-03-27 against Middle Eastern and U.S. targets.

The technically significant evolution is **AppDomainManager hijacking** (T1574.014) paired with classic DLL sideloading (T1574.001): the infection chain drops a legitimate Microsoft .NET executable alongside a weaponised `UpdateChecker.dll` / `InitInstall.dll` / `Updater.dll` and — critically — a malicious `.runtimeconfig.json` that redirects the CLR's AppDomainManager loading at process startup, *silently disabling ETW tracing and strong-name validation before the RAT executes*. That leaves the host's EDR operating in a reduced-telemetry mode on every infected workstation. Delivery is high-touch — fake recruitment PDFs, spoofed video-conference meeting invitations, and ZIP archives containing a legitimate executable as the trigger; persistence uses scheduled tasks; C2 routes through Azure-hosted domains. Confirmed targets: U.S., Israel, UAE, plus at least two further Middle Eastern entities consistent with prior UNC1549 focus on aerospace, defence and telecommunications. The CH/EU nexus is indirect but real — Swiss aerospace and defence suppliers (RUAG, Pilatus and defence export channels) sit squarely in the sector profile, as do EU R&D firms historically swept up in Iranian collection campaigns.

Detection vantage: alert on `.runtimeconfig.json` writes by non-installer processes; watch the `Microsoft-Windows-DotNETRuntime` ETW provider for `StrongNameVerification=0` startup events and CLR debug-mode initialisation; watch scheduled-task creation from processes with `.dll` parent images loading via `rundll32.exe` / `svchost.exe`. Hardening: enforce a code-integrity policy (UMCI + trusted-signers allowlist) so unsigned DLLs cannot load into the .NET CLR; restrict `.runtimeconfig.json` writes outside install paths via FIM.

## Update — 2026-05-27T05:00:04Z

Following Unit 42's coverage of UNC1549 / Screening Serpens AppDomainManager hijacking, Check Point Research (published 2026-05-22, widely re-reported this week) adds material technical depth on three February–April 2026 campaign waves keyed to Operation Epic Fury ([Check Point Research, 2026-05-22](https://research.checkpoint.com/2026/fast-and-furious-nimbus-manticore-operations-during-the-iranian-conflict/); [The Hacker News, 2026-05-26](https://thehackernews.com/2026/05/iranian-hackers-deploy-minifast-and.html)). The IRGC-affiliated actor replaced its MiniJunk family with a new backdoor, MiniFast — a 64-bit DLL with a single `CheckForUpdates` export and a JSON HTTP C2 using API-style endpoints (`/agent/init`, `/agent/poll`, `/upload/`) and a 14-opcode command set including DLL injection, UAC elevation and scheduled-task persistence.

Two persistence/delivery techniques are new versus the prior coverage: (1) **Zoom scheduled-task hijacking** (`T1053.005`) — instead of creating a suspicious new task, the malware watches for the legitimate `ZoomUpdateTaskUser-<SID>` task and hijacks it; (2) **SEO poisoning** (`T1598.003`) via a fake SQL Developer download domain ranked on Bing/DuckDuckGo, alongside `T1574.008` AppDomain hijacking via redirected `.config` files. The loader chain validates `parent=svchost.exe` before proceeding and abused two SSL.com-issued code-signing certificates ([Check Point Research, 2026-05-22](https://research.checkpoint.com/2026/fast-and-furious-nimbus-manticore-operations-during-the-iranian-conflict/)). Hunt for `ZoomUpdateTaskUser-*` task modifications by non-Zoom processes, non-default `AppDomainManager` values in .NET `.config` files, and execution from user-writable AppData paths.
