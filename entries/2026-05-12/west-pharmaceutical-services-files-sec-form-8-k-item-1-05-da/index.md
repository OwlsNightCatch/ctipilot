---
schema: 1
kind: incident
title: "West Pharmaceutical Services 8-K Item 1.05: data exfiltrated and systems encrypted, global operations partly restarted"
headline: "West Pharmaceutical discloses data theft and encryption in an 8-K; core systems restored, sites restarting"
summary: "West Pharmaceutical Services, a maker of injectable drug packaging, syringe and vial components and drug delivery devices, disclosed in a Form 8-K filed on 2026-05-11 that an intrusion detected on 2026-05-04, judged material on 2026-05-07, led to data exfiltration and the encryption of some systems. Core enterprise systems were restored and shipping, receiving and manufacturing had restarted at some sites with no timeline for full restoration; no ransomware group had claimed the attack as of 2026-05-13."
discovered_at: "2026-05-12T05:00:02Z"
event_date: 2026-05-11
run_id: 2026-05-12-cd1ab844
priority: routine
immediate_action: null
tags:
  - ransomware
  - data-breach
  - supply-chain
regions:
  - us
  - global
sectors:
  - healthcare
  - manufacturing
entities:
  - "incident:west-pharma-8k-2026"
techniques: [T1486]
affected_products: []
cves: []
sources:
  - url: "https://www.sec.gov/Archives/edgar/data/105770/000010577026000068/wst-20260507.htm"
    publisher: "SEC EDGAR (West Pharmaceutical Services Form 8-K)"
    date: "2026-05-11"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/west-pharmaceutical-says-hackers-stole-data-encrypted-systems/"
    publisher: "BleepingComputer"
    date: "2026-05-13"
    role: corroborating
closed_sources: []
evidence:
  - quote: "On May 7, 2026, West Pharmaceutical Services, Inc. (the “Company”) determined that the Company has experienced a material cybersecurity attack, in which certain data was exfiltrated by an unauthorized party and certain systems were encrypted."
    publisher: "SEC EDGAR (West Pharmaceutical Services Form 8-K)"
    source_url: "https://www.sec.gov/Archives/edgar/data/105770/000010577026000068/wst-20260507.htm"
  - quote: "While the Company has restored its core enterprise systems, and critical processes for shipping, receiving, and manufacturing have restarted at some sites with restoration of the remaining sites in process, the timeline for a complete restoration has not yet been finalized."
    publisher: "SEC EDGAR (West Pharmaceutical Services Form 8-K)"
    source_url: "https://www.sec.gov/Archives/edgar/data/105770/000010577026000068/wst-20260507.htm"
  - quote: "No ransomware groups have taken credit for the attack on West Pharmaceutical Services at the time of writing."
    publisher: "BleepingComputer"
    source_url: "https://www.bleepingcomputer.com/news/security/west-pharmaceutical-says-hackers-stole-data-encrypted-systems/"
verification: single-source-victim
sourcing_note: >
  The facts come from West's own 8-K and a company spokesperson's statement to BleepingComputer; no independent party has reported
  on the intrusion.
confidence: medium
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-12.md
updates:
  - at: "2026-10-21T20:45:48Z"
    run_id: 2026-10-21T1148Z-audit
    type: improvement
    summary: >
      West's 8-K states data exfiltration and encryption of some systems but not how the data left or how
      the attacker got in. As of 2026-05-13 no ransomware group had claimed the attack, the company
      specialises in injectable drug packaging, syringe and vial components and delivery devices, and the
      open question for customers was supply continuity while sites were restored.
    fields: [affected_products, body, classification, confidence, entities, evidence, headline, priority, sources, sourcing_note, summary, techniques, title, verification]
---

West Pharmaceutical Services determined on 2026-05-07 that it had suffered a material cybersecurity attack in which an unauthorized party exfiltrated data and encrypted some systems; after detecting the intrusion on 2026-05-04 it took systems offline globally, notified law enforcement and engaged external forensic experts, and the 8-K filed on 2026-05-11 says the business was disrupted globally, core enterprise systems were restored and shipping, receiving and manufacturing had restarted at some sites, with no timeline yet for complete restoration and no access vector or exfiltration method stated ([SEC 8-K, 2026-05-11](https://www.sec.gov/Archives/edgar/data/105770/000010577026000068/wst-20260507.htm)). The company, which specialises in injectable drug packaging, syringe and vial components, containment systems and drug delivery devices, engaged Palo Alto Networks' Unit 42 for incident response, and no ransomware group had taken credit as of 2026-05-13 ([BleepingComputer, 2026-05-13](https://www.bleepingcomputer.com/news/security/west-pharmaceutical-says-hackers-stole-data-encrypted-systems/)).

**Defender takeaway:** no detection or patching decision follows, since the filing gives no access vector; for West's customers the question was supply continuity while its sites were being restored ([SEC 8-K, 2026-05-11](https://www.sec.gov/Archives/edgar/data/105770/000010577026000068/wst-20260507.htm)).

## Improvement — 2026-10-21T20:45:48Z

The 8-K says that data was exfiltrated and some systems encrypted, but not how the data left or how the attacker got in, and that the investigation into the scope and the data affected was ongoing ([SEC 8-K, 2026-05-11](https://www.sec.gov/Archives/edgar/data/105770/000010577026000068/wst-20260507.htm)). No ransomware group had taken credit as of 2026-05-13, and West specialises in injectable drug packaging, syringe and vial components, containment systems and drug delivery devices ([BleepingComputer, 2026-05-13](https://www.bleepingcomputer.com/news/security/west-pharmaceutical-says-hackers-stole-data-encrypted-systems/)); no cited source describes which European supply lines depend on it or what detection preceded the encryption.
