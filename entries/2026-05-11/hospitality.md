---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-sector-patterns
title: Hospitality
headline: Hospitality
summary: "BWH Hotels (Best Western, WorldHotels, Sure Hotels) 181-day unauthorised access to a guest-reservation web application (daily 2026-05-13), six EU brands in scope."
discovered_at: "2026-05-11T05:00:18Z"
event_date: null
run_id: 2026-W20-71c96b25
priority: notable
immediate_action: null
tags:
  - data-breach
regions:
  - europe
  - us
sectors:
  - retail
entities: []
cves: []
sources:
  - url: "https://www.theregister.com/security/2026/05/11/best-western-hotels-confirms-web-app-data-breach/5238020"
    publisher: The Register — Best Western confirms web-app breach
    role: primary
  - url: "https://www.securityweek.com/bwh-hotels-says-hackers-had-access-to-reservation-data-for-6-months/"
    publisher: SecurityWeek — BWH Hotels reservation data
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
migrated_from: briefs/weekly/2026-W20.md
---

**BWH Hotels (Best Western, WorldHotels, Sure Hotels) 181-day unauthorised access** to a guest-reservation web application (daily 2026-05-13), six EU brands in scope. The 181-day dwell time is the operational lesson: a web-application access vector that escapes detection for half a year indicates absent application-tier telemetry — the right SOC-management response is to audit which guest / customer-facing web applications have **no** structured access-event telemetry feeding into the SIEM. EU regulatory scope: any of the six EU-brand reservation systems holding EU PII triggers GDPR Article 33 / 34 obligations and likely informs CEF 2026 enforcement attention (see Policy section below).
