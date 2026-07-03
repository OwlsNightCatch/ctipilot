---
schema: 1
kind: annual-report
horizon: strategic
weekly_section: weekly-annual-reports
title: Datadog Security Labs — Shai-Hulud framework static analysis
headline: Datadog Security Labs — Shai-Hulud framework static analysis
summary: Datadog Security Labs published a static analysis of the leaked Shai-Hulud framework source on 2026-05-13 (covered daily 2026-05-15).
discovered_at: "2026-05-11T05:00:32Z"
event_date: null
run_id: 2026-W20-71c96b25
priority: notable
immediate_action: null
tags:
  - supply-chain
  - ai-abuse
regions:
  - global
sectors:
  - technology
entities:
  - "actor:teampcp"
cves: []
sources:
  - url: "https://securitylabs.datadoghq.com/articles/shai-hulud-open-source-framework-static-analysis/"
    publisher: Datadog Security Labs
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

Datadog Security Labs published a static analysis of the **leaked Shai-Hulud framework source** on 2026-05-13 (covered daily 2026-05-15). The synthesis the daily had room for was the high-level capability summary; the cross-finding lens worth surfacing here: this is the first publicly-available **complete-source reverse-engineering of an active npm-supply-chain operator's toolkit**, comparable to the value the leaked Conti chats provided in 2022 for ransomware-affiliate defender intelligence. Detection-engineering teams now have a non-IOC behavioural reference for the entire TeamPCP toolchain: IDE-persistence hook patterns, OIDC-token extraction from `/proc/<pid>/mem`, Sigstore-provenance forgery primitives, GitHub Actions dead-drop conventions. The Datadog post-leak ecosystem-monitoring methodology (matching commits, repo names, hook configurations) is portable to any organisation with developer-workstation file-integrity monitoring; the broader implication is that **publication-provenance verification is no longer sufficient as a sole supply-chain control** ([Datadog Security Labs](https://securitylabs.datadoghq.com/articles/shai-hulud-open-source-framework-static-analysis/)).
