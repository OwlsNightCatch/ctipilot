---
schema: 1
kind: incident
horizon: strategic
weekly_section: weekly-incidents-recap
title: "Mass third-party exposures: Xsolis, Texas Parks & Wildlife, Canvas"
headline: "Mass third-party exposures: Xsolis, Texas Parks & Wildlife, Canvas"
summary: "Three large data exposures all traced to a third party rather than the named organisation: Xsolis (1.4M patients via a healthcare-AI processor), Texas Parks & Wildlife (3.08M licence holders via an unnamed licence-sales vendor, with a public-vs-AG-filing SSN contradiction noted in § 11), and the Canvas/Instructure LMS …"
discovered_at: "2026-06-29T00:21:12Z"
event_date: null
run_id: 2026-W26-b78503e7
priority: notable
immediate_action: null
tags:
  - data-breach
  - supply-chain
regions:
  - us
  - uk
sectors:
  - public-sector
  - healthcare
  - education
entities: []
cves: []
sources:
  - url: "https://www.hipaajournal.com/xsolis-data-breach/"
    publisher: HIPAA Journal — Xsolis
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/texas-govt-data-breach-exposes-over-3-million-drivers-licenses/"
    publisher: BleepingComputer — Texas
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

Three large data exposures all traced to a third party rather than the named organisation: [Xsolis](https://www.hipaajournal.com/xsolis-data-breach/) (1.4M patients via a healthcare-AI processor), [Texas Parks & Wildlife](https://www.bleepingcomputer.com/news/security/texas-govt-data-breach-exposes-over-3-million-drivers-licenses/) (3.08M licence holders via an unnamed licence-sales vendor, with a public-vs-AG-filing SSN contradiction noted in § 11), and the Canvas/Instructure LMS breach (160 UK universities). The recurring control gap is vendor data-minimisation and breach-notification SLAs.
