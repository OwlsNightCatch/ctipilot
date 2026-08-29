---
schema: 1
kind: incident
title: "Medtronic notifies ~9 million people of a ShinyHunters-claimed corporate-IT breach — 2.5 months after containment"
headline: "Medtronic notifies ~9 million people of a ShinyHunters-claimed corporate-IT breach — 2.5 months after containment"
summary: "Medtronic is notifying ~9 million people of a ShinyHunters-claimed April breach of corporate IT systems (names, DOB, SSNs, health data), 2.5 months after containment; it says medical devices were unaffected and segregated from the compromised networks (BleepingComputer, 2026-07-02)."
discovered_at: "2026-07-03T04:48:11Z"
event_date: 2026-07-02
run_id: 2026-07-03-04ba8283
priority: high
immediate_action: null
tags:
  - data-breach
  - organized-crime
regions:
  - us
  - global
sectors:
  - healthcare
entities:
  - "actor:shinyhunters"
  - "incident:medtronic-shinyhunters-corporate-it-breach"
cves: []
sources:
  - url: "https://www.bleepingcomputer.com/news/security/medtronic-notifies-customers-impacted-by-shinyhunters-data-breach/"
    publisher: BleepingComputer
    role: primary
  - url: "https://www.theregister.com/security/2026/07/02/pacemaker-manufacturer-medtronic-warns-patients-cybercrooks-may-have-swiped-health-data/5265768"
    publisher: The Register
    role: corroborating
closed_sources: []
evidence:
  - quote: "The investigation determined that from April 13 to April 19, 2026, an unauthorized actor accessed certain Medtronic corporate IT systems."
    publisher: BleepingComputer
  - quote: "Based on our investigation, this incident did not impact the ability of any Medtronic device to operate safely and deliver intended therapy."
    publisher: The Register
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
migrated_from: briefs/2026-07-03.md
---

Medical-device manufacturer Medtronic began notifying customers on 2026-07-02 of a breach the ShinyHunters extortion group first claimed in April. Medtronic's investigation found an unauthorized actor accessed certain corporate IT systems between 2026-04-13 and 2026-04-19 after unusual activity was noticed on 2026-04-15; ShinyHunters listed the company on its leak portal on 2026-04-18 claiming ~9 million records (names, contact details, dates of birth, Social Security numbers, health-related information) and later pulled the entry — consistent with the group's pattern after a ransom is paid ([BleepingComputer, 2026-07-02](https://www.bleepingcomputer.com/news/security/medtronic-notifies-customers-impacted-by-shinyhunters-data-breach/)). Medtronic states it found "no evidence" the data was published, and that the compromised corporate systems were segregated from device-operating networks so therapy delivery was unaffected ([The Register, 2026-07-02](https://www.theregister.com/security/2026/07/02/pacemaker-manufacturer-medtronic-warns-patients-cybercrooks-may-have-swiped-health-data/5265768)). No initial-access vector is disclosed. This is the same ShinyHunters cluster behind the recent Salesforce/PeopleSoft-adjacent extortion wave (Nissan, NAIC — see prior coverage), but a corporate-IT compromise rather than the SaaS-integration pattern seen elsewhere; the source does not confirm shared tradecraft.

**Defender takeaway:** a delisted extortion-portal entry is not proof of data destruction — treat any listed-then-delisted victim as presumptively breached and monitor for downstream credential-stuffing and DOB/PII-driven targeted phishing regardless of ransom outcome. The 2.5-month detection-to-notification gap is worth benchmarking against your own breach-notification SLAs.
