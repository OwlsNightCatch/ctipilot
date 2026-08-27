---
schema: 1
kind: synthesis
horizon: strategic
title: ShinyHunters / UNC6240 Oracle PeopleSoft campaign
headline: ShinyHunters / UNC6240 Oracle PeopleSoft campaign
summary: The campaign behind the § 1 NAIC breach.
discovered_at: "2026-06-29T00:21:20Z"
updated_at: "2026-07-05T23:40:00Z"
event_date: null
run_id: 2026-W26-b78503e7
priority: notable
immediate_action: null
tags:
  - data-breach
  - zero-day
  - actively-exploited
  - organized-crime
regions:
  - global
  - us
  - europe
sectors:
  - education
  - finance
  - public-sector
  - healthcare
entities:
  - "actor:shinyhunters"
techniques: []
affected_products: []
cves:
  - id: CVE-2026-35273
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status:
      - exploited
sources:
  - url: "https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-targets-education-sector-oracle-exploit"
    publisher: Google GTIG / Mandiant
    role: primary
  - url: "https://www.securityweek.com/google-confirms-exploitation-of-oracle-peoplesoft-zero-day-by-shinyhunters/"
    publisher: SecurityWeek
    role: corroborating
  - url: "https://www.securityweek.com/nissan-employee-data-breached-in-oracle-peoplesoft-hack/"
    publisher: SecurityWeek
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/medtronic-notifies-customers-impacted-by-shinyhunters-data-breach/"
    publisher: BleepingComputer
    role: corroborating
closed_sources: []
evidence:
  - quote: The campaign behind the § 1 NAIC breach.
    publisher: ctipilot v2 brief (migrated)
verification: multi-source
sourcing_note: "migration: evidence backfilled from v2 brief body (item predates the Evidence footer field)"
confidence: high
references:
  - 2026-06-28/naic-breached-via-oracle-peoplesoft-zero-day-shinyhunters-pu
  - 2026-07-03/medtronic-notifies-9-million-people-of-a-shinyhunters-claime
weekly_section: weekly-long-running
deep_dive: false
deep_dive_category: null
org_triage: null
classification: null
watchlist_hit: false
actions:
  - "Continue treating any internet-reachable Oracle PeopleSoft instance as assume-compromise: patch CVE-2026-35273 and hunt `/PSEMHUB/` and `/PSIGW/HttpListeningConnector` for anomalous unauthenticated access — the notification tail confirms the campaign is still acquiring victims."
  - "EU higher-education and public-finance PeopleSoft operators in the un-notified tail: proactively review for the campaign's MeshCentral-agent and per-victim fanout tradecraft rather than waiting for a GTIG notification."
updates:
  - at: "2026-07-05T23:40:00Z"
    run_id: 2026-07-05T2305Z-weekly
    type: update
    summary: >
      The ShinyHunters/UNC6240 Oracle PeopleSoft campaign (CVE-2026-35273) added Nissan as its largest
      named victim this week — employee HR/payroll PII across four countries — while GTIG
      notifications keep landing across the ~100-organisation tail. Separately, Medtronic is notifying
      ~9M people of a ShinyHunters-claimed April corporate-IT breach (not attributed to the PeopleSoft
      path). The campaign remains an active, victim-acquiring, zero-day-capable ERP-extortion
      operation.
    fields:
      - actions
      - references
      - sectors
      - sources
      - body
    merged_from: 2026-07-05/weekly-w27-shinyhunters-oracle-campaign-status
migrated_from: briefs/weekly/2026-W26.md
---

The campaign behind the § 1 NAIC breach. GTIG/Mandiant attributes to UNC6240 an active zero-day exploitation of Oracle PeopleSoft (CVE-2026-35273) between May 27 and June 9, predating Oracle's advisory; staging environments deployed customised MeshCentral agents masquerading as cloud endpoints, then ran a per-victim `[victim]_fanout.sh` lateral-movement-and-defacement script ([Google GTIG](https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-targets-education-sector-oracle-exploit)). ~300 PeopleSoft instances compromised, ~100 organisations notified, 68% higher education, with the University of Nottingham among the first named public victims ([SecurityWeek](https://www.securityweek.com/google-confirms-exploitation-of-oracle-peoplesoft-zero-day-by-shinyhunters/)). The status this week: NAIC confirmed (§ 1), and notifications are still landing, so more European education and public-finance victims are likely. The weekly lens: this is ShinyHunters operating as a zero-day-capable ERP attacker — a capability shift from the brand's 2021–2024 credential-stuffing persona. Outstanding question: which EU universities running PeopleSoft are in the un-notified tail.

## Update — 2026-07-05T23:40:00Z

The ShinyHunters/UNC6240 Oracle PeopleSoft campaign (CVE-2026-35273, unauthenticated RCE in PeopleTools Environment Management) kept acquiring named victims this week — the delta since the prior weekly's status.

**Nissan is the largest named victim yet.** SecurityWeek reported Nissan disclosed a breach tied to the Oracle PeopleSoft attacks, exposing current and former employee HR/payroll PII across four countries — a different exposure profile than the NAIC breach the W26 weekly led with ([SecurityWeek, 2026-06-30](https://www.securityweek.com/nissan-employee-data-breached-in-oracle-peoplesoft-hack/); § references). It confirms the "still acquiring victims" throughline the W26 looking-ahead flagged, and that named victims now span beyond the education sector GTIG originally emphasised.

**A separate Medtronic claim — attribution precision matters.** Medtronic is notifying ~9 million people of a ShinyHunters-*claimed* breach of corporate IT systems from April 2026 (names, DOB, SSNs, health data), with medical devices reported unaffected ([BleepingComputer, 2026-07-02](https://www.bleepingcomputer.com/news/security/medtronic-notifies-customers-impacted-by-shinyhunters-data-breach/); § references). This is a *distinct* incident from the PeopleSoft campaign — a corporate-IT breach the brand claimed, not tied to the Oracle zero-day path — and the weekly notes it to keep the ShinyHunters cluster's several concurrent operations from being conflated: the PeopleSoft ERP zero-day campaign is one line of effort; opportunistic corporate-IT data extortion under the same brand is another.

**Status:** GTIG's ~100-organisation notification set (68% higher education) is still landing, so more European education and public-finance victims are likely in the un-notified tail ([Google GTIG](https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-targets-education-sector-oracle-exploit)). The separate, unattributed Oracle E-Business Suite RCE now exploited in the wild (this week's Oracle top story) compounds the message: internet-facing Oracle application tiers are a priority patch-and-isolate class regardless of which actor is behind any single CVE.
