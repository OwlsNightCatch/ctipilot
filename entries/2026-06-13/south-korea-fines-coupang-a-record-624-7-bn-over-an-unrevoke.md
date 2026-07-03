---
schema: 1
kind: incident
horizon: operational
title: "South Korea fines Coupang a record ₩624.7 bn over an unrevoked signing key held by a former employee"
headline: "South Korea fines Coupang a record ₩624.7 bn over an unrevoked signing key held by a former employee"
summary: "South Korea's Personal Information Protection Commission (PIPC) issued its largest-ever data-protection penalty against e-commerce platform Coupang, attributing a breach of tens of millions of customer records to a former engineer who developed the company's alternative authentication system, retained its signing key …"
discovered_at: "2026-06-13T05:00:02Z"
event_date: 2026-06-12
run_id: 2026-06-13-40b26572
priority: notable
immediate_action: null
tags:
  - data-breach
  - insider-threat
  - identity
  - law-enforcement
regions:
  - apac
sectors:
  - retail
  - technology
entities: []
cves: []
sources:
  - url: "https://therecord.media/south-korea-data-breach-record-fine-coupang"
    publisher: The Record
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/south-korea-hits-coupang-with-record-409-million-fine-over-data-breach/"
    publisher: BleepingComputer
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
migrated_from: briefs/2026-06-13.md
---

South Korea's Personal Information Protection Commission (PIPC) issued its largest-ever data-protection penalty against e-commerce platform Coupang, attributing a breach of tens of millions of customer records to a former engineer who developed the company's alternative authentication system, retained its signing key on departure, and used forged authentication tokens to query customer delivery and account pages undetected for seven months ([The Record, 2026-06-12](https://therecord.media/south-korea-data-breach-record-fine-coupang)). PIPC characterised the failure as "deficiencies in basic safety management rather than a sophisticated hacking attack": the signing key was never revoked during offboarding and no anomaly detection flagged the overseas access pattern. Coupang separately drew an evidence-obstruction finding for deleting roughly six months of web-access logs after a preservation order ([BleepingComputer, 2026-06-11](https://www.bleepingcomputer.com/news/security/south-korea-hits-coupang-with-record-409-million-fine-over-data-breach/)).

**Why it matters to us:** This is a clean enforcement model for "offboarding token-revocation failure → maximum regulatory exposure," and the logic transfers directly to GDPR Article 32 and nDSG Article 8. Identity teams should audit all signing keys and OAuth client secrets tied to departed staff/contractors, confirm access logs fall under legal-hold retention covering a full incident window, and add anomaly detection for credential use from unexpected geographies (T1078.004, T1550.001).
