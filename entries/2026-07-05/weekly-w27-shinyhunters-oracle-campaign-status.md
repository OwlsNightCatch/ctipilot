---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-long-running
title: "ShinyHunters / UNC6240 Oracle campaign — status update: Nissan is the largest named victim, notifications keep landing, and a separate Medtronic claim surfaces"
headline: "ShinyHunters / UNC6240 Oracle campaign status — Nissan named, notifications still landing"
summary: "The ShinyHunters/UNC6240 Oracle PeopleSoft campaign (CVE-2026-35273) added Nissan as its largest named victim this week — employee HR/payroll PII across four countries — while GTIG notifications keep landing across the ~100-organisation tail. Separately, Medtronic is notifying ~9M people of a ShinyHunters-claimed April corporate-IT breach (not attributed to the PeopleSoft path). The campaign remains an active, victim-acquiring, zero-day-capable ERP-extortion operation."
discovered_at: "2026-07-05T23:40:00Z"
event_date: 2026-07-01
run_id: 2026-07-05T2305Z-weekly
priority: notable
immediate_action: null
tags:
  - data-breach
  - actively-exploited
  - organized-crime
  - zero-day
regions:
  - global
  - europe
  - us
sectors:
  - public-sector
  - education
  - finance
  - healthcare
entities:
  - "actor:shinyhunters"
cves: []
sources:
  - url: "https://www.securityweek.com/nissan-employee-data-breached-in-oracle-peoplesoft-hack/"
    publisher: SecurityWeek
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/medtronic-notifies-customers-impacted-by-shinyhunters-data-breach/"
    publisher: BleepingComputer
    role: corroborating
  - url: "https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-targets-education-sector-oracle-exploit"
    publisher: Google GTIG / Mandiant
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
classification:
  reliability: B
  credibility: 1
update_of: "2026-06-29/shinyhunters-unc6240-oracle-peoplesoft-campaign"
references:
  - "2026-07-01/nissan-is-the-largest-named-victim-yet-in-the-shinyhunters-o"
  - "2026-07-03/medtronic-notifies-9-million-people-of-a-shinyhunters-claime"
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions:
  - "Continue treating any internet-reachable Oracle PeopleSoft instance as assume-compromise: patch CVE-2026-35273 and hunt `/PSEMHUB/` and `/PSIGW/HttpListeningConnector` for anomalous unauthenticated access — the notification tail confirms the campaign is still acquiring victims."
  - "EU higher-education and public-finance PeopleSoft operators in the un-notified tail: proactively review for the campaign's MeshCentral-agent and per-victim fanout tradecraft rather than waiting for a GTIG notification."
---

**UPDATE (originally covered 2026-06-29):** the ShinyHunters/UNC6240 Oracle PeopleSoft campaign (CVE-2026-35273, unauthenticated RCE in PeopleTools Environment Management) kept acquiring named victims this week — the delta since the prior weekly's status.

**Nissan is the largest named victim yet.** SecurityWeek reported Nissan disclosed a breach tied to the Oracle PeopleSoft attacks, exposing current and former employee HR/payroll PII across four countries — a different exposure profile than the NAIC breach the W26 weekly led with ([SecurityWeek, 2026-06-30](https://www.securityweek.com/nissan-employee-data-breached-in-oracle-peoplesoft-hack/); § references). It confirms the "still acquiring victims" throughline the W26 looking-ahead flagged, and that named victims now span beyond the education sector GTIG originally emphasised.

**A separate Medtronic claim — attribution precision matters.** Medtronic is notifying ~9 million people of a ShinyHunters-*claimed* breach of corporate IT systems from April 2026 (names, DOB, SSNs, health data), with medical devices reported unaffected ([BleepingComputer, 2026-07-02](https://www.bleepingcomputer.com/news/security/medtronic-notifies-customers-impacted-by-shinyhunters-data-breach/); § references). This is a *distinct* incident from the PeopleSoft campaign — a corporate-IT breach the brand claimed, not tied to the Oracle zero-day path — and the weekly notes it to keep the ShinyHunters cluster's several concurrent operations from being conflated: the PeopleSoft ERP zero-day campaign is one line of effort; opportunistic corporate-IT data extortion under the same brand is another.

**Status:** GTIG's ~100-organisation notification set (68% higher education) is still landing, so more European education and public-finance victims are likely in the un-notified tail ([Google GTIG](https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-targets-education-sector-oracle-exploit)). The separate, unattributed Oracle E-Business Suite RCE now exploited in the wild (this week's Oracle top story) compounds the message: internet-facing Oracle application tiers are a priority patch-and-isolate class regardless of which actor is behind any single CVE.
