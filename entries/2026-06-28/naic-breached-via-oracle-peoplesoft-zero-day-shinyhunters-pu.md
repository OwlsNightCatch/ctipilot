---
schema: 1
kind: incident
horizon: operational
title: >
  NAIC breached via Oracle PeopleSoft zero-day; ShinyHunters publishes 3.1 TB of US
  insurance-regulatory data and rating-agency feeds pause
headline: >
  NAIC breached via Oracle PeopleSoft zero-day; ShinyHunters publishes 3.1 TB of US
  insurance-regulatory data and rating-agency feeds pause
summary: >
  NAIC — the standard-setting body for all 50 US state insurance regulators — confirms a breach
  via an Oracle PeopleSoft zero-day; ShinyHunters published ~3.1 TB of insurance regulatory and
  credit-rating-agency data, and rating-agency feeds paused, forcing NAIC to suspend assigning
  investment-risk designations. Part of a 100+ org PeopleSoft zero-day campaign; any organisation
  running Oracle PeopleSoft should verify patch status against the campaign (NAIC, 2026-06-26).
discovered_at: "2026-06-28T05:05:36Z"
updated_at: "2026-07-01T04:41:20Z"
event_date: 2026-06-26
run_id: 2026-06-28-1b30612a
priority: high
immediate_action: null
tags:
  - data-breach
  - zero-day
  - actively-exploited
  - organized-crime
  - vulnerabilities
regions:
  - us
  - europe
  - global
sectors:
  - finance
  - public-sector
  - manufacturing
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
  - url: "https://content.naic.org/about/security-update"
    publisher: NAIC security update
    role: primary
  - url: "https://www.insurancejournal.com/news/national/2026/06/25/875334.htm"
    publisher: Insurance Journal
    role: corroborating
  - url: "https://www.techradar.com/pro/security/naic-confirms-data-breach-with-shinyhunters-claiming-3-1tb-of-data-stolen-in-oracle-zero-day-attack"
    publisher: TechRadar
    role: corroborating
  - url: "https://www.insurancebusinessmag.com/us/news/cyber/naic-confirms-peoplesoft-breach-as-cybercriminals-target-insurance-regulators-580134.aspx"
    publisher: Insurance Business Mag
    role: corroborating
  - url: "https://www.securityweek.com/nissan-employee-data-breached-in-oracle-peoplesoft-hack/"
    publisher: SecurityWeek
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/nissan-discloses-employee-data-breach-linked-to-oracle-zero-day-attacks/"
    publisher: BleepingComputer
    role: corroborating
closed_sources: []
evidence:
  - quote: "Unauthorized access to a portion of the NAIC's environment was identified on June 11 via an Oracle PeopleSoft vulnerability. While in PeopleSoft, the unauthorized party was able to obtain information needed to gain temporary access to certain data storage areas."
    publisher: NAIC
  - quote: "Due to the incident, certain credit rating agencies have paused their data feeds and consequently, the NAIC has temporarily suspended assigning designations to insurer investments."
    publisher: NAIC
  - quote: "UPDATE (originally covered 2026-06-28 as the NAIC breach): Nissan disclosed that current and former employees' data was exposed via CVE-2026-35273, the Oracle PeopleSoft PeopleTools pre-auth flaw exploited as a zero-day between 2026-05-27 and 2026-06-09 as part of the wider ShinyHunters campaign …"
    publisher: ctipilot v2 brief (migrated)
verification: multi-source
sourcing_note: null
confidence: high
references: []
weekly_section: null
deep_dive: false
deep_dive_category: null
org_triage: null
classification: null
watchlist_hit: false
actions:
  - "**Confirm CVE-2026-35273 (Oracle PeopleSoft PeopleTools) is patched and PeopleSoft PeopleTools is off the public internet** — the ShinyHunters campaign is still acquiring named victims (Nissan)."
updates:
  - at: "2026-07-01T04:41:20Z"
    run_id: 2026-07-01-af9e697d
    type: update
    summary: >
      The ShinyHunters Oracle PeopleSoft campaign adds Nissan as its largest named victim yet —
      current and former employee HR/payroll PII across four countries, a different exposure profile
      than the NAIC breach covered 2026-06-28 (SecurityWeek, 2026-06-30).
    fields:
      - actions
      - cves
      - evidence
      - regions
      - sectors
      - sources
      - tags
      - body
    merged_from: 2026-07-01/nissan-is-the-largest-named-victim-yet-in-the-shinyhunters-o
migrated_from: briefs/2026-06-28.md
---

The National Association of Insurance Commissioners (NAIC) — the US standard-setting body governing all 50 state insurance regulators — confirmed on 2026-06-26 that an unauthorised party gained access to part of its environment on 2026-06-11 by exploiting an Oracle PeopleSoft vulnerability that was unknown to the vendor at the time, then used the PeopleSoft foothold to obtain credentials that pivoted into NAIC data-storage areas ([NAIC, 2026-06-26](https://content.naic.org/about/security-update)). The flaw is reported as **CVE-2026-35273**, a critical unauthenticated remote-code-execution vulnerability in Oracle PeopleSoft Enterprise PeopleTools 8.61 and 8.62 ([Insurance Business Mag, 2026-06-24](https://www.insurancebusinessmag.com/us/news/cyber/naic-confirms-peoplesoft-breach-as-cybercriminals-target-insurance-regulators-580134.aspx)). NAIC states the access path has since been blocked and remediated and that the FBI plus external forensics are engaged. The extortion group **ShinyHunters** claimed responsibility on 2026-06-18 and by 2026-06-25 had published the data, which corroborating reporting puts at ~3.1 TB ([TechRadar, 2026-06-26](https://www.techradar.com/pro/security/naic-confirms-data-breach-with-shinyhunters-claiming-3-1tb-of-data-stolen-in-oracle-zero-day-attack)); the corpus is reported to include insurer statutory financial-reporting documents and files from major credit-rating agencies ([Insurance Journal, 2026-06-25](https://www.insurancejournal.com/news/national/2026/06/25/875334.htm)). NAIC says it has not confirmed ShinyHunters' claim to have taken SERFF, OPTins, UCAA, EDP and RDC, and that employee PII, EFT, policyholder and producer data were not accessed. The operationally significant consequence: several rating agencies paused their data feeds to NAIC, forcing it to temporarily suspend assigning investment-risk designations to insurer portfolios — a direct disruption to US insurance-sector solvency monitoring. The incident is reported as part of a broader PeopleSoft campaign affecting 100+ organisations ([Insurance Business Mag, 2026-06-24](https://www.insurancebusinessmag.com/us/news/cyber/naic-confirms-peoplesoft-breach-as-cybercriminals-target-insurance-regulators-580134.aspx)).

**Why it matters to us:** Oracle PeopleSoft is widely deployed for HR/finance in European and Swiss public-sector and large enterprises; the kill chain here is `T1190` (exploit a public-facing PeopleSoft app) → `T1078` (abuse the obtained credentials/session to pivot to data stores) → `T1567` (web-service exfiltration). Verify PeopleSoft patch status against the in-the-wild zero-day campaign, segment PeopleSoft data-bus/integration accounts to least privilege, and put DLP/volume alerting on bulk export from PeopleSoft repositories. EU/Swiss insurance supervisors (EIOPA, national NCAs) and reinsurers whose data is in the rating-agency corpus should treat affected feeds as potentially tampered until NAIC confirms integrity restoration.

## Update — 2026-07-01T04:41:20Z

Nissan disclosed that current and former employees' data was exposed via CVE-2026-35273, the Oracle PeopleSoft PeopleTools pre-auth flaw exploited as a zero-day between 2026-05-27 and 2026-06-09 as part of the wider ShinyHunters campaign ([SecurityWeek, 2026-06-30](https://www.securityweek.com/nissan-employee-data-breached-in-oracle-peoplesoft-hack/)). The exposure spans current and former employees in the US, Canada, Mexico and Brazil, potentially including Social Security numbers, banking/direct-deposit information and tax records.

This is a materially different victim profile from the previously-covered NAIC breach — employee HR/payroll PII rather than regulatory data — showing the campaign spreading across both regulatory-body and corporate-HR PeopleSoft deployments. As mitigation, Nissan restricted pay-slip viewing and direct-deposit changes to company-network/VPN-authenticated sessions and is offering credit/dark-web monitoring ([BleepingComputer, 2026-06-29](https://www.bleepingcomputer.com/news/security/nissan-discloses-employee-data-breach-linked-to-oracle-zero-day-attacks/)). ShinyHunters' self-reported scale of "over 300 PeopleSoft instances across ~100 organizations" is an unverified actor claim — attribute the claim, not confirmed fact. No new technical detail beyond victim-count expansion; the operative guidance from the 2026-06-28 NAIC item stands (patch CVE-2026-35273; remove internet-exposed PeopleSoft PeopleTools from public reachability).
