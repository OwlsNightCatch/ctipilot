---
schema: 1
kind: incident
horizon: strategic
weekly_section: weekly-incidents-recap
title: "Škoda Auto Deutschland — online-shop breach exposes customer PII and password hashes"
headline: "Škoda Auto Deutschland — online-shop breach exposes customer PII and password hashes"
summary: "Customer PII and password hashes exposed; logging-gap prevented exfiltration confirmation. The defender's learning is the logging-coverage point: a breach where the victim cannot confirm what was exfiltrated is a logging-design failure."
discovered_at: "2026-05-11T05:00:25Z"
event_date: 2026-05-12
run_id: 2026-W20-71c96b25
priority: notable
immediate_action: null
tags:
  - data-breach
regions:
  - europe
sectors:
  - retail
  - manufacturing
entities: []
cves: []
sources:
  - url: "https://www.skoda-auto.de/unternehmen/sicherheitsvorfall-skoda-shop"
    publisher: Heise Security
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

Customer PII and password hashes exposed; logging-gap prevented exfiltration confirmation. The defender's learning is the logging-coverage point: a breach where the victim **cannot confirm** what was exfiltrated is a logging-design failure. Pattern-match: which of your own citizen-facing / customer-facing e-commerce flows would leave you with the same uncertainty after an intrusion? ([daily 2026-05-12](/briefs/2026-05-12/)).
