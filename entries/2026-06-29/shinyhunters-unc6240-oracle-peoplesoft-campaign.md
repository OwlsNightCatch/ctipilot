---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-long-running
title: ShinyHunters / UNC6240 Oracle PeopleSoft campaign
headline: ShinyHunters / UNC6240 Oracle PeopleSoft campaign
summary: The campaign behind the § 1 NAIC breach.
discovered_at: "2026-06-29T00:21:20Z"
event_date: null
run_id: 2026-W26-b78503e7
priority: notable
immediate_action: null
tags:
  - data-breach
  - zero-day
  - actively-exploited
  - organized-crime
regions:
  - global
  - us
  - europe
sectors:
  - education
  - finance
  - public-sector
entities:
  - "actor:shinyhunters"
cves:
  - id: CVE-2026-35273
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status:
      - exploited
sources:
  - url: "https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-targets-education-sector-oracle-exploit"
    publisher: Google GTIG / Mandiant
    role: primary
  - url: "https://www.securityweek.com/google-confirms-exploitation-of-oracle-peoplesoft-zero-day-by-shinyhunters/"
    publisher: SecurityWeek
    role: corroborating
closed_sources: []
evidence:
  - quote: The campaign behind the § 1 NAIC breach.
    publisher: ctipilot v2 brief (migrated)
verification: multi-source
sourcing_note: "migration: evidence backfilled from v2 brief body (item predates the Evidence footer field)"
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

The campaign behind the § 1 NAIC breach. GTIG/Mandiant attributes to UNC6240 an active zero-day exploitation of Oracle PeopleSoft (CVE-2026-35273) between May 27 and June 9, predating Oracle's advisory; staging environments deployed customised MeshCentral agents masquerading as cloud endpoints, then ran a per-victim `[victim]_fanout.sh` lateral-movement-and-defacement script ([Google GTIG](https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-targets-education-sector-oracle-exploit)). ~300 PeopleSoft instances compromised, ~100 organisations notified, 68% higher education, with the University of Nottingham among the first named public victims ([SecurityWeek](https://www.securityweek.com/google-confirms-exploitation-of-oracle-peoplesoft-zero-day-by-shinyhunters/)). The status this week: NAIC confirmed (§ 1), and notifications are still landing, so more European education and public-finance victims are likely. The weekly lens: this is ShinyHunters operating as a zero-day-capable ERP attacker — a capability shift from the brand's 2021–2024 credential-stuffing persona. Outstanding question: which EU universities running PeopleSoft are in the un-notified tail.
