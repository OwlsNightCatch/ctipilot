---
schema: 1
kind: incident
horizon: operational
title: Maine AG takes its breach-notification portal offline after confirming the VRChat/Discord filings were a hoax
headline: Maine AG takes its breach-notification portal offline after confirming the VRChat/Discord filings were a hoax
summary: "UPDATE (originally covered 2026-06-12): The Maine Attorney General's Office issued a formal statement on 12 June confirming that the VRChat and Discord breach filings surfaced through its public portal were hoaxes submitted by an unknown entity unrelated to either company, and that it has no record of any recent …"
discovered_at: "2026-06-13T05:00:08Z"
event_date: 2026-06-12
run_id: 2026-06-13-40b26572
priority: notable
immediate_action: null
tags:
  - data-breach
  - disinformation
  - law-enforcement
regions:
  - us
sectors:
  - public-sector
entities: []
cves: []
sources:
  - url: "https://www.maine.gov/ag/news-and-library/press-releases/statement-office-maine-attorney-general-abuse-data-breach-reporting"
    publisher: Maine AG
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/maine-disables-data-breach-notification-portal-after-fake-disclosures/"
    publisher: BleepingComputer
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: 2026-06-12/maine-s-breach-notification-portal-abused-for-fraudulent-fil
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-13.md
---

**UPDATE (originally covered 2026-06-12):** The Maine Attorney General's Office issued a formal statement on 12 June confirming that the VRChat and Discord breach filings surfaced through its public portal were hoaxes submitted by an unknown entity unrelated to either company, and that it has no record of any recent legitimate breach reports from either ([Maine AG, 2026-06-12](https://www.maine.gov/ag/news-and-library/press-releases/statement-office-maine-attorney-general-abuse-data-breach-reporting)).

The office took the public-facing breach database offline while it reviews and hardens its submission procedures ([BleepingComputer, 2026-06-12](https://www.bleepingcomputer.com/news/security/maine-disables-data-breach-notification-portal-after-fake-disclosures/)). The material delta on yesterday's coverage is the regulator's own confirmation that the filings were fraudulent and the portal's suspension — a reminder that self-certification breach portals are an unauthenticated data-integrity surface, and that breach "disclosures" sourced solely from such portals warrant corroboration before action.
