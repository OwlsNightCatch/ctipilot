---
schema: 1
kind: annual-report
horizon: operational
title: "CrowdStrike 2026 Technology Threat Landscape Report: technology is now the most-targeted sector"
headline: "CrowdStrike 2026 Technology Threat Landscape Report: technology is now the most-targeted sector"
summary: "CrowdStrike published its 2026 Technology Threat Landscape Report on 9 June 2026 (CrowdStrike, 2026-06-09)."
discovered_at: "2026-06-11T05:00:05Z"
event_date: 2026-06-09
run_id: 2026-06-11-7edf1d8a
priority: notable
immediate_action: null
tags:
  - nation-state
  - espionage
  - supply-chain
  - ai-abuse
  - china-nexus
  - north-korea-nexus
regions:
  - global
sectors:
  - technology
entities:
  - "report:crowdstrike-tech-threat-landscape-2026"
cves: []
sources:
  - url: "https://www.crowdstrike.com/en-us/blog/crowdstrike-2026-technology-threat-landscape-report/"
    publisher: CrowdStrike
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
migrated_from: briefs/2026-06-11.md
---

CrowdStrike published its 2026 Technology Threat Landscape Report on 9 June 2026 ([CrowdStrike, 2026-06-09](https://www.crowdstrike.com/en-us/blog/crowdstrike-2026-technology-threat-landscape-report/)). The findings most relevant to a Swiss/EU public-sector SOC running AI and cloud DevOps infrastructure: China-nexus adversaries (named clusters include MURKY PANDA, MUSTANG PANDA and WARP PANDA) drove more than 58% of state-sponsored intrusions against the technology sector, focused on AI capabilities, training data, ML infrastructure and semiconductor IP; and DPRK-nexus FAMOUS CHOLLIMA accounted for 47% of state-sponsored hands-on-keyboard activity through IT-worker infiltration using AI-enhanced personas and front companies across North America, Europe and Asia. The report frames AI/ML development pipelines and model weights as espionage targets warranting the same protection as source code and credentials. CrowdStrike also names a compromise of the `axios` npm package as part of a DPRK-linked supply-chain operation — a notable claim, but in this run only CrowdStrike asserts it, so treat the `axios` element as single-source pending independent corroboration.
