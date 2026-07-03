---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-sector-patterns
title: Education
headline: Education
summary: "Education was a structural victim class. The ShinyHunters Canvas/Instructure breach hit 160 UK universities per the UK CMC sector review (ransom paid, limited downstream damage)."
discovered_at: "2026-06-29T00:21:09Z"
event_date: null
run_id: 2026-W26-b78503e7
priority: notable
immediate_action: null
tags:
  - data-breach
  - vulnerabilities
  - sqli
regions:
  - uk
  - dach
  - europe
sectors:
  - education
entities:
  - "actor:shinyhunters"
cves: []
sources:
  - url: "https://www.computerweekly.com/news/366645159/Canvas-breach-hit-160-UK-unis-but-caused-limited-damage"
    publisher: Computer Weekly — Canvas
    role: primary
  - url: "https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2016"
    publisher: BSI WID-SEC-2026-2016 — ILIAS
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

Education was a structural victim class. The ShinyHunters Canvas/Instructure breach [hit 160 UK universities](https://www.computerweekly.com/news/366645159/Canvas-breach-hit-160-UK-unis-but-caused-limited-damage) per the UK CMC sector review (ransom paid, limited downstream damage). The unpatched ILIAS 11.0 SQL-injection ([CVE-2026-12789](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2016), PoC-public, no patch) directly exposes the DACH learning-management estate, and self-hosted Gitea CI (§ 3) is concentrated in universities. The common thread: education runs exposed CMS/LMS/forum and developer stacks with thin operational security.
