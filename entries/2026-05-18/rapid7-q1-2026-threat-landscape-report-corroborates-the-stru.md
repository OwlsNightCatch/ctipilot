---
schema: 1
kind: annual-report
horizon: strategic
weekly_section: weekly-annual-reports
title: "Rapid7 Q1 2026 Threat Landscape Report — corroborates the structural shift; KEV-to-listing window collapsing"
headline: "Rapid7 Q1 2026 Threat Landscape Report — corroborates the structural shift; KEV-to-listing window collapsing"
summary: "Rapid7's Q1 2026 report (published 2026-05-21, covering Jan–Mar 2026 IR data, covered 2026-05-23) independently finds vulnerability exploitation as the top initial-access vector at ~38%."
discovered_at: "2026-05-18T05:00:27Z"
event_date: 2026-05-23
run_id: 2026-W21-473d6fa5
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - ransomware
  - nation-state
  - ai-abuse
regions:
  - global
sectors:
  - public-sector
entities:
  - "report:rapid7-q1-2026-threat-landscape-report-vulnerability-exploitation-top-iav"
cves: []
sources:
  - url: "https://www.rapid7.com/blog/post/tr-q1-2026-threat-landscape-report-geopolitics-ransomware/"
    publisher: Rapid7 Q1 2026 Threat Landscape Report
    role: primary
  - url: "https://www.globenewswire.com/news-release/2026/05/21/3299378/36514/en/Rapid7-Q1-2026-Threat-Landscape-Report-Finds-Vulnerability-Exploitation-Overtakes-Social-Engineering-as-the-Top-Initial-Access-Vector.html"
    publisher: GlobeNewswire — Rapid7 Q1 2026 release
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
migrated_from: briefs/weekly/2026-W21.md
---

Rapid7's Q1 2026 report (published 2026-05-21, covering Jan–Mar 2026 IR data, covered [2026-05-23](/briefs/2026-05-23/)) independently finds vulnerability exploitation as the top initial-access vector at ~38%. Read alongside the Verizon DBIR, the two datasets agree on direction even where the absolute percentages differ (different windows, different telemetry) — the synthesis a daily reader could not see is that this is a *corroborated* structural change, not a single-vendor artefact. For CH/EU defenders this argues for prioritising edge-device and public-facing-application patch SLAs over generic awareness programmes.
