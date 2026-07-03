---
schema: 1
kind: incident
horizon: strategic
weekly_section: weekly-incidents-recap
title: "AFC Ajax — 300,000+ fan accounts exposed via misconfigured API access control; Dutch suspect arrested"
headline: "AFC Ajax — 300,000+ fan accounts exposed via misconfigured API access control; Dutch suspect arrested"
summary: "The Dutch National Police arrested a 35-year-old over the breach of AFC Ajax's fan app, in which misconfigured API access control and shared keys exposed 300,000+ accounts and 42,000 season-ticket records (2026-05-28)."
discovered_at: "2026-05-25T05:00:15Z"
event_date: 2026-05-28
run_id: 2026-W22-da77963d
priority: notable
immediate_action: null
tags:
  - data-breach
  - law-enforcement
  - identity
regions:
  - europe
sectors:
  - media
entities: []
cves: []
sources:
  - url: "https://www.bleepingcomputer.com/news/security/dutch-police-arrests-suspect-linked-to-ajax-football-club-hack/"
    publisher: BleepingComputer — Dutch police arrest
    role: primary
  - url: "https://therecord.media/dutch-police-arrest-man-over-cyber-breach-ajax-football"
    publisher: The Record
    role: corroborating
  - url: "https://english.ajax.nl/articles/information-about-data-breach-at-ajax/"
    publisher: AFC Ajax statement
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
migrated_from: briefs/weekly/2026-W22.md
---

The Dutch National Police arrested a 35-year-old over the breach of AFC Ajax's fan app, in which **misconfigured API access control and shared keys** exposed 300,000+ accounts and 42,000 season-ticket records ([2026-05-28](/briefs/2026-05-28/)). Two things make this instructive for this audience: the root cause is a textbook broken-object-level-authorization / over-shared-credential failure in a mobile-app back end — the class of defect that automated DAST and an API-inventory review catch cheaply — and the rapid arrest is a reminder that these cases do sometimes attribute to an individual rather than an organised crew. Re-audit API authorization on customer/citizen-facing apps for object-level checks, and retire shared API keys in favour of per-client credentials.
