---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-long-running
title: The Gentlemen
headline: The Gentlemen
summary: "The Gentlemen ransomware makes Switzerland the second-most-targeted European country, claims 478 victims and adds worm propagation — ESET's leaked-data deep-dive shows victims are chosen on FortiGate misconfiguration, tying the pipeline to FortiBleed reconnaissance. (daily 06-27, inside-it.ch)"
discovered_at: "2026-06-29T00:21:21Z"
event_date: null
run_id: 2026-W26-b78503e7
priority: high
immediate_action: null
tags:
  - ransomware
  - organized-crime
  - russia-nexus
regions:
  - switzerland
  - dach
  - europe
sectors:
  - manufacturing
  - healthcare
  - energy
entities:
  - "actor:thegentlemen"
  - "incident:fortibleed-fortigate-credential-exposure"
cves: []
sources:
  - url: "https://www.inside-it.ch/aufstrebende-ransomware-bande-findet-mehr-schweizer-opfer-20260626"
    publisher: inside-it.ch
    role: primary
  - url: "https://www.welivesecurity.com/en/eset-research/killing-me-gently-inside-gentlemens-edr-killer-framework/"
    publisher: ESET WeLiveSecurity
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

The W25 multi-day item now has primary-evidence depth (the ESET deep-dive, § 7) and a sharp Swiss angle: Check Point data, reported by Swiss tech press, makes [Switzerland the second-most-targeted European country](https://www.inside-it.ch/aufstrebende-ransomware-bande-findet-mehr-schweizer-opfer-20260626) for the operation, which now claims 478 victims and has added worm propagation. The operationally important link is that victim selection runs on FortiGate misconfiguration scanning — so a Swiss organisation's FortiBleed exposure (above) is also its Gentlemen-victim-selection exposure. Outstanding for defenders: the same FortiGate hardening that closes FortiBleed reduces Gentlemen targeting, and EDR-tamper-protection plus driver-blocklist enforcement is the GentleKiller counter.
