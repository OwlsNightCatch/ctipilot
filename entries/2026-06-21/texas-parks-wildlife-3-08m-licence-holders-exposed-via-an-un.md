---
schema: 1
kind: incident
horizon: operational
title: "Texas Parks & Wildlife: 3.08M licence holders exposed via an unnamed third-party vendor — with a public-vs-AG-filing SSN contradiction"
headline: "Texas Parks & Wildlife: 3.08M licence holders exposed via an unnamed third-party vendor — with a public-vs-AG-filing SSN contradiction"
summary: "Two more third-party-vendor breaches land on public-sector and healthcare bodies: 3.08M Texas hunting/fishing-licence holders (with a public-vs-AG-filing contradiction over whether SSNs were taken) and Amazon's One Medical Seniors archive (with ShinyHunters' unverified 8.8TB claim and a deadline that expires today) (BleepingComputer, 2026-06-19)."
discovered_at: "2026-06-21T04:54:58Z"
event_date: 2026-06-19
run_id: 2026-06-21-2b75e32c
priority: high
immediate_action: null
tags:
  - data-breach
  - supply-chain
regions:
  - us
sectors:
  - public-sector
entities: []
cves: []
sources:
  - url: "https://www.bleepingcomputer.com/news/security/texas-govt-data-breach-exposes-over-3-million-drivers-licenses/"
    publisher: BleepingComputer
    role: primary
  - url: "https://www.theregister.com/security/2026/06/19/texas-gov-vendor-breach-exposes-data-of-3m-hunters-anglers/5258815"
    publisher: The Register
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
migrated_from: briefs/2026-06-21.md
---

The Texas Parks and Wildlife Department disclosed on 2026-06-18/19 that a breach at an unnamed third-party vendor handling hunting and fishing licence sales exposed 3,087,721 customers' names, driver's-licence numbers, passport numbers, email addresses, phone numbers and residential addresses ([BleepingComputer, 2026-06-19](https://www.bleepingcomputer.com/news/security/texas-govt-data-breach-exposes-over-3-million-drivers-licenses/)). The Texas Cyber Command flagged the intrusion (reported 13 May). TPWD's public statement said Social Security numbers were *not* involved — but The Register reviewed the agency's own filing to the Texas Attorney General's breach portal and reports it contradicts that, indicating SSNs *were* included ([The Register, 2026-06-19](https://www.theregister.com/security/2026/06/19/texas-gov-vendor-breach-exposes-data-of-3m-hunters-anglers/5258815)). The vendor remains unnamed; Kroll is providing credit monitoring.

**Defender takeaway:** A government agency that minimised breach scope in its public notice while its regulator filing shows broader exposure is the operationally instructive part. Public-sector bodies contracting licence/registry SaaS — including Swiss cantonal systems — should require contractual breach-notification timelines, SOC 2 Type II attestation, and segmentation guarantees on the licence database, and should reconcile public statements against regulator filings before publishing.
