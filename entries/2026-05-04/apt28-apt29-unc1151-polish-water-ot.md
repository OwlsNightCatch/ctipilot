---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-long-running
title: APT28 / APT29 / UNC1151 (Polish water OT)
headline: APT28 / APT29 / UNC1151 (Polish water OT)
summary: "Current state: ABW 2025 Annual Report (2026-05-07 publication, covered 2026-05-09) is the formal-attribution development this week."
discovered_at: "2026-05-04T05:00:35Z"
event_date: null
run_id: 2026-W19-a5788b22
priority: notable
immediate_action: null
tags:
  - nation-state
  - ot-ics
  - russia-nexus
  - hacktivism
  - disinformation
regions:
  - europe
sectors:
  - water
  - public-sector
entities: []
cves: []
sources:
  - url: "https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-207a"
    publisher: CISA AA24-207A (background reference)
    role: primary
closed_sources: []
evidence: []
verification: single-source-national-cert
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/weekly/2026-W19.md
---

Current state: ABW 2025 Annual Report (2026-05-07 publication, covered 2026-05-09) is the formal-attribution development this week. Per SecurityWeek's coverage of the ABW report, the campaign against the five small Polish municipal water facilities is attributed to **APT28** (GRU) and **APT29** (SVR) — with **UNC1151** (Belarusian-linked) named in the same attribution discussion. The granular per-facility breakdown and disinformation-overlay specifics carried in the daily 2026-05-09 UPDATE trace back to the Polish-language ABW report itself rather than the English secondary coverage; defenders relying on the English reporting should treat the actor-cluster trio as attributed jointly without per-facility specificity unless the ABW primary is consulted. The same APT28 cluster is in active operation against EU government ministries via CVE-2026-32202 (Windows Shell NTLM coercion, § 3). Outstanding defender question: whether ABW-recommended NIS2 expansion to critical-function entities below the headcount threshold gains EU-level momentum in coming weeks.
