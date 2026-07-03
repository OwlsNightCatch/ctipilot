---
schema: 1
kind: vulnerability
horizon: operational
title: Nissan is the largest named victim yet in the ShinyHunters Oracle PeopleSoft campaign
headline: Nissan is the largest named victim yet in the ShinyHunters Oracle PeopleSoft campaign
summary: "The ShinyHunters Oracle PeopleSoft campaign adds Nissan as its largest named victim yet — current and former employee HR/payroll PII across four countries, a different exposure profile than the NAIC breach covered 2026-06-28 (SecurityWeek, 2026-06-30)."
discovered_at: "2026-07-01T04:41:20Z"
event_date: 2026-06-30
run_id: 2026-07-01-af9e697d
priority: high
immediate_action: null
tags:
  - data-breach
  - vulnerabilities
  - actively-exploited
regions:
  - global
sectors:
  - manufacturing
entities:
  - "actor:shinyhunters"
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
  - url: "https://www.securityweek.com/nissan-employee-data-breached-in-oracle-peoplesoft-hack/"
    publisher: SecurityWeek
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/nissan-discloses-employee-data-breach-linked-to-oracle-zero-day-attacks/"
    publisher: BleepingComputer
    role: corroborating
closed_sources: []
evidence:
  - quote: "UPDATE (originally covered 2026-06-28 as the NAIC breach): Nissan disclosed that current and former employees' data was exposed via CVE-2026-35273, the Oracle PeopleSoft PeopleTools pre-auth flaw exploited as a zero-day between 2026-05-27 and 2026-06-09 as part of the wider ShinyHunters campaign …"
    publisher: ctipilot v2 brief (migrated)
verification: multi-source
sourcing_note: "migration: evidence backfilled from v2 brief body (item predates the Evidence footer field)"
confidence: high
update_of: 2026-06-28/naic-breached-via-oracle-peoplesoft-zero-day-shinyhunters-pu
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions:
  - "**Confirm CVE-2026-35273 (Oracle PeopleSoft PeopleTools) is patched and PeopleSoft PeopleTools is off the public internet** — the ShinyHunters campaign is still acquiring named victims (Nissan)."
migrated_from: briefs/2026-07-01.md
---

**UPDATE (originally covered 2026-06-28 as the NAIC breach):** Nissan disclosed that current and former employees' data was exposed via CVE-2026-35273, the Oracle PeopleSoft PeopleTools pre-auth flaw exploited as a zero-day between 2026-05-27 and 2026-06-09 as part of the wider ShinyHunters campaign ([SecurityWeek, 2026-06-30](https://www.securityweek.com/nissan-employee-data-breached-in-oracle-peoplesoft-hack/)). The exposure spans current and former employees in the US, Canada, Mexico and Brazil, potentially including Social Security numbers, banking/direct-deposit information and tax records.

This is a materially different victim profile from the previously-covered NAIC breach — employee HR/payroll PII rather than regulatory data — showing the campaign spreading across both regulatory-body and corporate-HR PeopleSoft deployments. As mitigation, Nissan restricted pay-slip viewing and direct-deposit changes to company-network/VPN-authenticated sessions and is offering credit/dark-web monitoring ([BleepingComputer, 2026-06-29](https://www.bleepingcomputer.com/news/security/nissan-discloses-employee-data-breach-linked-to-oracle-zero-day-attacks/)). ShinyHunters' self-reported scale of "over 300 PeopleSoft instances across ~100 organizations" is an unverified actor claim — attribute the claim, not confirmed fact. No new technical detail beyond victim-count expansion; the operative guidance from the 2026-06-28 NAIC item stands (patch CVE-2026-35273; remove internet-exposed PeopleSoft PeopleTools from public reachability).
