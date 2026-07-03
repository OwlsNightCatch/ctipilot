---
schema: 1
kind: incident
horizon: strategic
weekly_section: weekly-incidents-recap
title: "7-Eleven — ShinyHunters Salesforce campaign claims another 600,000+ records"
headline: "7-Eleven — ShinyHunters Salesforce campaign claims another 600,000+ records"
summary: "7-Eleven confirmed on 2026-05-18 that an unauthorised third party accessed franchise-application records (600,000+) in a breach ShinyHunters claimed in April 2026."
discovered_at: "2026-05-18T05:00:21Z"
event_date: 2026-05-18
run_id: 2026-W21-473d6fa5
priority: notable
immediate_action: null
tags:
  - data-breach
  - identity
  - cloud
  - organized-crime
regions:
  - global
  - europe
sectors:
  - retail
  - technology
entities:
  - "actor:shinyhunters"
  - "incident:medtronic-shinyhunters-corporate-it-breach"
cves: []
sources:
  - url: "https://www.securityweek.com/7-eleven-data-breach-confirmed-after-shinyhunters-ransom-demand/"
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
migrated_from: briefs/weekly/2026-W21.md
---

7-Eleven confirmed on [2026-05-18](/briefs/2026-05-19/) that an unauthorised third party accessed franchise-application records (600,000+) in a breach ShinyHunters claimed in April 2026. The operational point for this audience is the campaign, not the victim: 7-Eleven joins Instructure, Vimeo, Wynn Resorts, Vercel and Medtronic as named victims of the same Salesforce-targeting ShinyHunters operation. Any organisation with Salesforce connected apps and OAuth-integrated third parties should re-audit connected-app scopes and refresh-token lifetimes.
