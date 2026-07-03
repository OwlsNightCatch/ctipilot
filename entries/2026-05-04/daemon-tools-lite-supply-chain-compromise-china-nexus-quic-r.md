---
schema: 1
kind: incident
horizon: strategic
weekly_section: weekly-incidents-recap
title: "DAEMON Tools Lite supply-chain compromise — China-nexus QUIC RAT delivered via signed installers; ~12 selective government / scientific / manufacturing targets"
headline: "DAEMON Tools Lite supply-chain compromise — China-nexus QUIC RAT delivered via signed installers; ~12 selective government / scientific / manufacturing targets"
summary: "Official DAEMON Tools Lite Windows installers (versions 12.5.0.2421 → 12.5.0.2434) were trojanised on the Disc Soft vendor distribution server from 8 April to 5 May 2026, with malicious installers maintaining the authentic AVB Disc Soft code-signing certificate."
discovered_at: "2026-05-04T05:00:21Z"
event_date: 2026-05-07
run_id: 2026-W19-a5788b22
priority: notable
immediate_action: null
tags:
  - supply-chain
  - espionage
  - china-nexus
  - infostealer
regions:
  - europe
  - global
sectors:
  - public-sector
  - manufacturing
  - technology
entities: []
cves: []
sources:
  - url: "https://www.kaspersky.com/blog/daemon-tools-supply-chain-attack/55691/"
    publisher: Kaspersky — DAEMON Tools supply chain attack
    role: primary
  - url: "https://therecord.media/hackers-compromise-daemon-tools-global-supply-chain-attack"
    publisher: The Record — DAEMON Tools global supply-chain attack
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/daemon-tools-trojanized-in-supply-chain-attack-to-deploy-backdoor/"
    publisher: BleepingComputer — DAEMON Tools trojanized
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
migrated_from: briefs/weekly/2026-W19.md
---

Official DAEMON Tools Lite Windows installers (versions 12.5.0.2421 → 12.5.0.2434) were trojanised on the Disc Soft vendor distribution server from 8 April to 5 May 2026, with malicious installers maintaining the authentic AVB Disc Soft code-signing certificate. The campaign deployed three stages: a `.NET` information collector (`envchk.exe`) for host fingerprinting deployed broadly across more than 100 countries (Germany, France, Spain, and Italy appear explicitly in first-stage victim telemetry); a shellcode-based backdoor; and **QUIC RAT** — a C++ implant supporting HTTP / UDP / TCP / WebSocket / QUIC / HTTP/3 C2 channels — *selectively* deployed to approximately twelve targets in government, scientific, manufacturing, and retail sectors in Russia, Belarus, and Thailand per Kaspersky. Chinese-language strings in the information collector suggest a Chinese-speaking actor; no formal attribution to a named group. The C2 domain was registered 2026-03-27 — approximately two weeks before the first trojanised installer (2026-04-08) — confirming pre-planned operation. Disc Soft acknowledged 2026-05-05, released clean version 12.6.0.2445, resolved the distribution compromise within 12 hours ([Kaspersky Securelist](https://www.kaspersky.com/blog/daemon-tools-supply-chain-attack/55691/) · [The Record, 2026-05-06](https://therecord.media/hackers-compromise-daemon-tools-global-supply-chain-attack) · [BleepingComputer, 2026-05-06](https://www.bleepingcomputer.com/news/security/daemon-tools-trojanized-in-supply-chain-attack-to-deploy-backdoor/) · [Help Net Security, 2026-05-06](https://www.helpnetsecurity.com/2026/05/06/daemon-tools-compromised-backdoors-supply-chain-attack/) · [daily 2026-05-07 and 2026-05-09 UPDATE](/briefs/2026-05-09/)). **Defender takeaway:** audit endpoints for DAEMON Tools Lite versions 12.5.0.2421 – 12.5.0.2434 installed on any government, scientific, or manufacturing endpoint since 8 April 2026; hunt for `envchk.exe`, unsigned processes injected into `notepad.exe` or `conhost.exe`, and outbound UDP 443 (QUIC) to non-sanctioned destinations; Sysmon EID 1 with parent-image filters surfaces post-injection activity. The pattern — selective QUIC-channel deployment behind broad-targeting reconnaissance staging — is the operationally important detail; it explains why telemetry hit-rate alone underestimates targeted-actor presence.
