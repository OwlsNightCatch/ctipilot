---
schema: 1
kind: incident
horizon: operational
title: >
  Maine's breach-notification portal abused for fraudulent filings against VRChat and Discord —
  both companies deny any breach
headline: >
  Maine's breach-notification portal abused for fraudulent filings against VRChat and Discord —
  both companies deny any breach
summary: >
  Maine's Attorney-General breach-notification portal published fraudulent data-breach filings —
  one claiming a 2.4-million-user VRChat cloud compromise, another a 10-million-user Discord
  breach — because submissions are published without filer-identity verification
  (BleepingComputer, 2026-06-11).
discovered_at: "2026-06-12T05:00:04Z"
updated_at: "2026-06-13T05:00:08Z"
event_date: 2026-06-11
run_id: 2026-06-12-5ab9a319
priority: notable
immediate_action: null
tags:
  - disinformation
  - data-breach
  - law-enforcement
regions:
  - us
sectors:
  - technology
  - public-sector
entities: []
techniques: []
affected_products: []
cves: []
sources:
  - url: "https://www.bleepingcomputer.com/news/security/maine-breach-portal-abused-to-publish-fake-data-breach-disclosures/"
    publisher: BleepingComputer
    role: primary
  - url: "https://www.maine.gov/ag/news-and-library/press-releases/statement-office-maine-attorney-general-abuse-data-breach-reporting"
    publisher: Maine AG
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/maine-disables-data-breach-notification-portal-after-fake-disclosures/"
    publisher: BleepingComputer
    role: corroborating
closed_sources: []
evidence: []
verification: single-source
sourcing_note: null
confidence: high
references: []
weekly_section: null
deep_dive: false
deep_dive_category: null
org_triage: null
classification: null
watchlist_hit: false
actions: []
updates:
  - at: "2026-06-13T05:00:08Z"
    run_id: 2026-06-13-40b26572
    type: update
    summary: >
      UPDATE (originally covered 2026-06-12): The Maine Attorney General's Office issued a formal
      statement on 12 June confirming that the VRChat and Discord breach filings surfaced through its
      public portal were hoaxes submitted by an unknown entity unrelated to either company, and that
      it has no record of any recent …
    fields:
      - sectors
      - sources
      - tags
      - body
    merged_from: 2026-06-13/maine-ag-takes-its-breach-notification-portal-offline-after
migrated_from: briefs/2026-06-12.md
---

Maine's Attorney-General breach-notification portal published fraudulent data-breach filings — one claiming a 2.4-million-user VRChat cloud compromise, another a 10-million-user Discord breach — because submissions are published without filer-identity verification ([BleepingComputer, 2026-06-11](https://www.bleepingcomputer.com/news/security/maine-breach-portal-abused-to-publish-fake-data-breach-disclosures/)). VRChat stated: "VRChat did not submit this Notice of Data Incident, and the employee/email cited does not exist. We have no reason to believe that our data or systems have been compromised." Discord likewise denied filing. The Maine AG's office acknowledged the fraudulent notices and moved to remove them. [SINGLE-SOURCE — BleepingComputer.]

**Why it matters to us:** CTI teams routinely treat state breach portals as authoritative collection sources — this incident shows they can be poisoned. Require victim confirmation or regulator follow-up before acting on (or republishing) portal-only breach claims; the same trust-exploitation pattern would work against any unauthenticated notification channel.

## Update — 2026-06-13T05:00:08Z

The Maine Attorney General's Office issued a formal statement on 12 June confirming that the VRChat and Discord breach filings surfaced through its public portal were hoaxes submitted by an unknown entity unrelated to either company, and that it has no record of any recent legitimate breach reports from either ([Maine AG, 2026-06-12](https://www.maine.gov/ag/news-and-library/press-releases/statement-office-maine-attorney-general-abuse-data-breach-reporting)).

The office took the public-facing breach database offline while it reviews and hardens its submission procedures ([BleepingComputer, 2026-06-12](https://www.bleepingcomputer.com/news/security/maine-disables-data-breach-notification-portal-after-fake-disclosures/)). The material delta on yesterday's coverage is the regulator's own confirmation that the filings were fraudulent and the portal's suspension — a reminder that self-certification breach portals are an unauthenticated data-integrity surface, and that breach "disclosures" sourced solely from such portals warrant corroboration before action.
