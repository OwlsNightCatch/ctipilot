---
schema: 1
kind: incident
horizon: strategic
weekly_section: weekly-incidents-recap
title: BWH Hotels — 181-day unauthorised access to guest-reservation web application
headline: BWH Hotels — 181-day unauthorised access to guest-reservation web application
summary: "Six EU brands (Best Western, WorldHotels, Sure Hotels and three sub-brands) in scope; 181-day dwell time indicates absent application-tier telemetry on the affected reservation web application. EU regulatory scope: GDPR Article 33 / 34 obligations for the six EU-brand reservation systems holding EU PII."
discovered_at: "2026-05-11T05:00:22Z"
event_date: 2026-05-13
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
    publisher: SecurityWeek
    role: primary
closed_sources: []
evidence: []
verification: single-source
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

Six EU brands (Best Western, WorldHotels, Sure Hotels and three sub-brands) in scope; 181-day dwell time indicates absent application-tier telemetry on the affected reservation web application. EU regulatory scope: GDPR Article 33 / 34 obligations for the six EU-brand reservation systems holding EU PII. The defender's learning: audit which guest-facing / citizen-facing web applications have no structured access-event telemetry into the SIEM ([daily 2026-05-13](/briefs/2026-05-13/)).
