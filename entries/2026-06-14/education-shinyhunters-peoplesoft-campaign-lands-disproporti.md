---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-sector-patterns
title: "Education — ShinyHunters' PeopleSoft campaign lands disproportionately on universities"
headline: "Education — ShinyHunters' PeopleSoft campaign lands disproportionately on universities"
summary: "The week's clearest sectoral concentration. Mandiant/GTIG's attribution of the Oracle PeopleSoft zero-day campaign (§ 1) explicitly noted that the education sector was hit hardest, with the University of Nottingham confirming ~455,000 affected records (Google GTIG; daily 06-13)."
discovered_at: "2026-06-14T23:57:28Z"
event_date: null
run_id: 2026-W24-bd5a7519
priority: notable
immediate_action: null
tags:
  - data-breach
  - supply-chain
regions:
  - uk
  - europe
sectors:
  - education
entities:
  - "actor:shinyhunters"
cves: []
sources:
  - url: "https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-targets-education-sector-oracle-exploit/"
    publisher: Google GTIG
    role: primary
  - url: "https://www.careers.ox.ac.uk/article/careerconnect-secured-and-safe-to-use-following-data-security-incident"
    publisher: Oxford University
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
migrated_from: briefs/weekly/2026-W24.md
---

The week's clearest sectoral concentration. Mandiant/GTIG's attribution of the Oracle PeopleSoft zero-day campaign (§ 1) explicitly noted that the education sector was hit hardest, with the University of Nottingham confirming ~455,000 affected records ([Google GTIG](https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-targets-education-sector-oracle-exploit/); [daily 06-13](/briefs/2026-06-13/)). It rhymes with the earlier Oxford University CareerConnect breach, where third-party provider Group GTI's compromise exposed students across multiple UK universities ([Oxford](https://www.careers.ox.ac.uk/article/careerconnect-secured-and-safe-to-use-following-data-security-incident); [daily 06-09](/briefs/2026-06-09/)). European higher-education ICT teams running PeopleSoft or relying on shared careers/HR SaaS should treat both as direct warnings.
