---
schema: 1
kind: incident
horizon: strategic
weekly_section: weekly-incidents-recap
title: Social engineering and SSO abuse opened the highest-profile intrusions
headline: Social engineering and SSO abuse opened the highest-profile intrusions
summary: "Madison Square Garden was breached by a single vishing call into its identity platform; the operators talked a low-level employee into authorising access. This is the same human-layer entry that has driven the year's most damaging extortion."
discovered_at: "2026-06-29T00:21:11Z"
event_date: null
run_id: 2026-W26-b78503e7
priority: notable
immediate_action: null
tags:
  - phishing
  - identity
  - data-breach
  - organized-crime
regions:
  - us
  - global
sectors:
  - media
  - technology
entities: []
cves: []
sources:
  - url: "https://www.404media.co/how-hackers-broke-into-madison-square-garden/"
    publisher: 404 Media
    role: primary
  - url: "https://abnormal.ai/blog/shinyhunters-sso-social-engineering-mfa-identity-compromise"
    publisher: Abnormal Security
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
migrated_from: briefs/weekly/2026-W26.md
---

Madison Square Garden was breached by [a single vishing call](https://www.404media.co/how-hackers-broke-into-madison-square-garden/) into its identity platform; the operators talked a low-level employee into authorising access. This is the same human-layer entry that has driven the year's most damaging extortion. The defensive lesson is process, not product: callback verification on help-desk identity changes, no MFA reset on an inbound call, and alerting on anomalous SSO grants from new devices.
