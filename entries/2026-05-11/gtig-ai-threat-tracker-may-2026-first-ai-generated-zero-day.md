---
schema: 1
kind: annual-report
horizon: strategic
weekly_section: weekly-annual-reports
title: GTIG AI Threat Tracker (May 2026) — first AI-generated zero-day exploit ITW
headline: GTIG AI Threat Tracker (May 2026) — first AI-generated zero-day exploit ITW
summary: "GTIG's May 2026 AI Threat Tracker (covered as daily 2026-05-12 deep dive) documents the first confirmed AI-generated zero-day exploit observed in-the-wild and presents the behavioural class of AI-augmented malware."
discovered_at: "2026-05-11T05:00:34Z"
event_date: 2026-05-12
run_id: 2026-W20-71c96b25
priority: notable
immediate_action: null
tags:
  - ai-abuse
  - nation-state
regions:
  - global
sectors:
  - public-sector
entities:
  - "report:gtig-ai-threat-tracker-may-2026"
cves: []
sources:
  - url: "https://cloud.google.com/blog/topics/threat-intelligence/ai-threat-tracker-may-2026/"
    publisher: GTIG AI Threat Tracker May 2026
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

GTIG's May 2026 AI Threat Tracker (covered as daily 2026-05-12 deep dive) documents the **first confirmed AI-generated zero-day exploit observed in-the-wild** and presents the behavioural class of AI-augmented malware. The synthesis worth elevating for the weekly: the "AI-augmented" malware category is no longer hypothetical for SOC defenders — the behavioural-class taxonomy GTIG provides (LLM-assisted code generation in payload, AI-driven C2 dialogue, model-mediated lateral movement decisions) is the right detection-engineering reference for SOCs building hunt content for the next 12 months. The relevant SOC capability investment: behavioural baselines for "what does AI-mediated execution look like in our telemetry" — not new IOC ingestion ([GTIG AI Threat Tracker May 2026](https://cloud.google.com/blog/topics/threat-intelligence/ai-threat-tracker-may-2026/); [daily 2026-05-12 deep dive](/briefs/2026-05-12/)).
