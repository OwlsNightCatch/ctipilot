---
schema: 1
kind: annual-report
horizon: strategic
weekly_section: weekly-annual-reports
title: "ESET \"Killing me gently\" — a de-facto mid-year RaaS-tooling report"
headline: "ESET \"Killing me gently\" — a de-facto mid-year RaaS-tooling report"
summary: "Background. The Gentlemen emerged in late 2025 as a RaaS operation founded by \"hastalamuerte\" (a former Qilin affiliate per Group-IB, previously affiliated with Embargo, LockBit, Medusa and BlackLock per PRODAFT)."
discovered_at: "2026-06-29T00:21:17Z"
event_date: null
run_id: 2026-W26-b78503e7
priority: notable
immediate_action: null
tags:
  - ransomware
  - organized-crime
  - russia-nexus
regions:
  - global
  - europe
  - switzerland
sectors:
  - manufacturing
  - healthcare
  - energy
entities:
  - "actor:thegentlemen"
  - "campaign:tds-security-tool-impersonation-checkpoint"
  - "actor:dragonforce"
  - "incident:fortibleed-fortigate-credential-exposure"
  - "actor:embargo"
cves: []
sources:
  - url: "https://www.welivesecurity.com/en/eset-research/killing-me-gently-inside-gentlemens-edr-killer-framework/"
    publisher: ESET WeLiveSecurity
    role: primary
  - url: "https://www.eset.com/us/about/newsroom/research/eset-research-gentlemen-ransomware-gang-edr-killers/"
    publisher: ESET Newsroom
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
migrated_from: briefs/weekly/2026-W26.md
---

**Background.** The Gentlemen emerged in late 2025 as a RaaS operation founded by "hastalamuerte" (a former Qilin affiliate per Group-IB, previously affiliated with Embargo, LockBit, Medusa and BlackLock per PRODAFT). ESET first hypothesised an in-house EDR-killer in February 2026; Group-IB and Check Point independently corroborated before the gang's own internal data leaked. By April 2026 the group accounted for ~10% of global ransomware activity, and Krebs (06-10) linked the alias to a named individual in Izhevsk, Russia.

ESET's 06-26 deep-dive into the leaked internal data is the most substantive published-in-window documentation of RaaS tooling structure, and reads as a mid-year complement to the W25 Check Point State of Ransomware Q1 2026. Three structural findings a detection engineer should register: (1) GentleKiller is a modular in-house framework with at least eight BYOVD variants, each impersonating a different vendor and abusing a different kernel driver — driver allow-listing alone is insufficient without process-injection-chain detection; (2) the group integrates *rival gangs'* EDR killers (HexKiller from Warlock, ThrottleBlood shared with MedusaLocker/DragonForce, HavocKiller), so tooling overlap no longer implies operational overlap; (3) victims are selected centrally on FortiGate misconfiguration rather than geography, tying the Gentlemen victim pipeline directly to FortiBleed-style reconnaissance (§ 8). New BYOVD PoCs are operationalised within days of public release. ([daily 06-27](/briefs/2026-06-27/))
