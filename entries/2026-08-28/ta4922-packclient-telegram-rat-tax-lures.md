---
schema: 1
kind: threat
horizon: operational
title: "TA4922 adds PackClient, a Telegram-sold modular RAT/C2 framework, to its toolkit — dual-channel C2, registry-resident configuration, and tax-themed lures against mainland China and India"
headline: "A China-nexus financially-motivated cluster already tracked for EU expansion picks up a commodity, Telegram-proliferated RAT"
summary: >
  Proofpoint documents PackClient, a modular remote-access trojan and C2 framework actively sold
  on Telegram, now in use by TA4922 — a China-nexus, financially-motivated cluster this pipeline
  already tracks. PackClient uses rundll32 execution, reflective DLL loading, registry-resident
  configuration and a custom dual-channel TCP protocol. Observed campaigns used tax-themed
  phishing against mainland China and India, deploying legitimate ManageEngine RMM tooling
  post-compromise.
discovered_at: "2026-08-28T06:38:00Z"
updated_at: null
event_date: "2026-08-27"
run_id: 2026-08-28T0409Z-intel
priority: notable
immediate_action: null
tags: [organized-crime, infostealer, phishing]
regions: [apac, europe]
sectors: [public-sector, finance]
entities: [actor:ta4922, tool:packclient]
techniques: [T1547.001, T1620, T1056.001, T1113, T1105]
affected_products: []
cves: []
sources:
  - url: "https://www.proofpoint.com/us/blog/threat-insight/carry-compromise-ta4922-packs-packclient"
    publisher: "Proofpoint"
    date: "2026-08-27"
    role: primary
closed_sources: []
evidence:
  - quote: "With this new payload, TA4922 is expanding its arsenal of initial-access malware, much of which originates in the Chinese-speaking cybercrime ecosystem."
    publisher: "Proofpoint"
  - quote: "PackClient is a full featured, modular command and control (C2) framework that supports data theft, surveillance, and downloading of additional plugins and payloads."
    publisher: "Proofpoint"
  - quote: "Distinct Rundll32 command line used to launch PackClient. PackClient config stored in registry (HKCU\\SOFTWARE\\PackClientConsole\\). Distinct process tree and command line flags."
    publisher: "Proofpoint"
verification: single-source
sourcing_note: >
  Proofpoint is the sole source. The observed campaign targets mainland China and India, not this
  constituency's home region directly; included because TA4922 is an already-tracked actor this
  store separately notes is expanding tooling and targeting into Germany, the UK and Italy, so a
  new Telegram-proliferated C2 framework is transferable tradecraft, and a MaaS tool sold on
  Telegram is not exclusive to one actor.
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

Proofpoint documents PackClient, a modular remote-access trojan and command-and-control framework actively sold on Telegram, now in use by TA4922 — a China-nexus, financially-motivated cluster this pipeline already tracks (registry `actor:ta4922`, first seen 2026-06-05, previously associated with Atlas RAT, RomulusLoader and SilentRunLoader, and separately noted by this pipeline as expanding into DE/UK/IT): "with this new payload, TA4922 is expanding its arsenal of initial-access malware, much of which originates in the Chinese-speaking cybercrime ecosystem" ([Proofpoint, 2026-08-27](https://www.proofpoint.com/us/blog/threat-insight/carry-compromise-ta4922-packs-packclient)).

PackClient's delivery chain uses `rundll32` execution and reflective DLL loading, with persistence via a registry RunOnce key, and stores its configuration under `HKCU\SOFTWARE\PackClientConsole`: "distinct Rundll32 command line used to launch PackClient. PackClient config stored in registry (HKCU\SOFTWARE\PackClientConsole\). Distinct process tree and command line flags" ([Proofpoint, 2026-08-27](https://www.proofpoint.com/us/blog/threat-insight/carry-compromise-ta4922-packs-packclient)). It supports keylogging, webcam and screen capture, file exfiltration and plugin/payload management over dual C2 channels using a custom TCP protocol with distinctive handshake byte sequences (Proofpoint names them PLH1/PLC1): "PackClient is a full featured, modular command and control (C2) framework that supports data theft, surveillance, and downloading of additional plugins and payloads" ([Proofpoint, 2026-08-27](https://www.proofpoint.com/us/blog/threat-insight/carry-compromise-ta4922-packs-packclient)).

In the observed campaigns TA4922 used tax-themed phishing lures against organisations in mainland China and India, with post-compromise activity that included deploying ManageEngine remote-monitoring-and-management tooling — a legitimate RMM abused for continued access, consistent with this actor's established pattern of using commodity or legitimate management tools post-compromise. Proofpoint does not name a MITRE ATT&CK technique explicitly, but the described behaviours map to registry Run-key persistence, DLL side-loading/reflective loading defence evasion, and collection via keylogging and screen capture.

The campaign targeting is mainland China and India, not this constituency's home region or profiled sectors directly, but the relevance rests on two points: TA4922 is separately tracked by this pipeline as expanding tooling and targeting into Germany, the UK and Italy, so a new Telegram-proliferated C2 framework in this actor's toolkit is transferable tradecraft to watch for; and a MaaS tool sold on Telegram is not exclusive to one actor and may surface again against a different, more directly-relevant target set. **Triage:** a registry key at `HKCU\SOFTWARE\PackClientConsole` on any endpoint has no legitimate application association and is a direct compromise indicator; process trees showing `rundll32` launched with non-standard command-line flags followed by reflective DLL-loading behaviour (no corresponding file on disk for the loaded module) are the discriminator against ordinary `rundll32` usage, which normally loads a named, on-disk DLL export.
