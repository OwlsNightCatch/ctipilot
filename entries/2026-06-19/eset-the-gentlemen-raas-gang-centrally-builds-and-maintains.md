---
schema: 1
kind: research
horizon: operational
title: "ESET: the Gentlemen RaaS gang centrally builds and maintains its affiliates' EDR-killer framework"
headline: "ESET: the Gentlemen RaaS gang centrally builds and maintains its affiliates' EDR-killer framework"
summary: "ESET's months-long investigation into the Gentlemen ransomware-as-a-service operation reveals a structural departure from the affiliate norm: rather than each affiliate sourcing its own evasion tooling, the operators build, maintain and distribute a modular EDR-killing framework — GentleKiller — centrally (ESET …"
discovered_at: "2026-06-19T05:20:58Z"
event_date: 2026-06-18
run_id: 2026-06-19-c306b105
priority: notable
immediate_action: null
tags:
  - ransomware
  - organized-crime
regions:
  - global
  - europe
sectors:
  - manufacturing
  - technology
  - public-sector
entities:
  - "actor:gentlemen-raas-gentlekiller"
  - "actor:thegentlemen"
cves: []
sources:
  - url: "https://www.welivesecurity.com/en/eset-research/killing-me-gently-inside-gentlemens-edr-killer-framework/"
    publisher: ESET WeLiveSecurity
    role: primary
  - url: "https://www.helpnetsecurity.com/2026/06/18/eset-gentlemen-edr-killers/"
    publisher: Help Net Security
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
migrated_from: briefs/2026-06-19.md
---

ESET's months-long investigation into the Gentlemen ransomware-as-a-service operation reveals a structural departure from the affiliate norm: rather than each affiliate sourcing its own evasion tooling, the operators build, maintain and distribute a modular EDR-killing framework — *GentleKiller* — centrally ([ESET, 2026-06-18](https://www.welivesecurity.com/en/eset-research/killing-me-gently-inside-gentlemens-edr-killer-framework/); [Help Net Security, 2026-06-18](https://www.helpnetsecurity.com/2026/06/18/eset-gentlemen-edr-killers/)). GentleKiller comprises at least eight variants, each abusing a different legitimately-signed driver via BYOVD (`T1543.003`), targeting 400+ named security processes mapped to 48 EDR/AV/XDR product families. The defining operational pattern is speed: ESET documents the gang operationalising newly disclosed BYOVD proof-of-concepts within days of public release, and in one case wielding a Huawei-audio-driver kill technique *before* its public disclosure — ESET telemetry shows the gang using it since at least 2026-01-23, weeks ahead of the technique's public write-up (by Huntress) on 2026-03-19. Common evasion across variants includes Enigma/Themida packing and invalid copies of digital certificates impersonating major AV vendors; a Rust-based credential stealer (*OxideHarvest*) handles browser-credential theft. The gang reached top-5 most-active RaaS in Q1 2026, offers affiliates a 90% cut, and shows globally distributed victimology including Western Europe — a profile overlapping Swiss critical-sector exposure.
**Why it matters to us:** an operator-curated EDR-killer means affiliates of even modest skill get current BYOVD capability on day one of a PoC. Enable the Microsoft Vulnerable Driver Blocklist (HVCI) and enforce WDAC driver allowlisting; hunt for service creation loading unexpected kernel drivers and `DeviceIoControl` calls from non-security processes, plus process-termination loops targeting security software (Sysmon EID 6 / kernel-callback telemetry).
