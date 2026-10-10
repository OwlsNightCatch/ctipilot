---
schema: 1
kind: incident
title: TheGentlemen RaaS lists Czech university and Swiss engineering firm on leak site
headline: TheGentlemen RaaS lists Czech university and Swiss engineering firm on leak site
summary: "UPDATE (originally covered 2026-05-14 backend database leak analysis): The TheGentlemen RaaS group's leak site listed two new European victims this week: University of Finance and Administration (VSFS, vsfs.cz) in the Czech Republic on 2026-05-19 and Swiss engineering firm DEVO-Tech AG (devo-tech.ch …"
discovered_at: "2026-05-20T05:00:13Z"
event_date: 2026-05-19
run_id: 2026-05-20-a0f7b07f
priority: notable
immediate_action: null
tags:
  - ransomware
  - organized-crime
  - data-breach
regions:
  - europe
  - switzerland
sectors:
  - education
  - manufacturing
entities: []
cves: []
sources:
  - url: "https://www.dexpose.io/thegentlemen-target-university-of-finance-and-administration-in-czech-republic/"
    publisher: "DeXpose, 2026-05-19"
    role: primary
  - url: "https://www.dexpose.io/thegentlemen-ransomware-group-targets-swiss-engineering-firm-devo-tech-ag/"
    publisher: "DeXpose, 2026-05-18"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: "migration: update target unresolved (originally covered 2026-05-14)"
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-20.md
---

**UPDATE (originally covered 2026-05-14 backend database leak analysis):** The TheGentlemen RaaS group's leak site listed two new European victims this week: **University of Finance and Administration (VSFS, vsfs.cz)** in the Czech Republic on [2026-05-19](https://www.dexpose.io/thegentlemen-target-university-of-finance-and-administration-in-czech-republic/) and Swiss engineering firm **DEVO-Tech AG** (devo-tech.ch, Ziefen / BL) on [2026-05-18](https://www.dexpose.io/thegentlemen-ransomware-group-targets-swiss-engineering-firm-devo-tech-ag/). The DeXpose write-ups are aggregator coverage of the leak-site listings themselves; neither victim has publicly confirmed the breach as of this brief. TTPs, infrastructure, and the Go-based locker remain unchanged from the Check Point Research deep coverage of 2026-05-14 — the new data point is geographic spread continuing into EU higher education and Swiss SMB engineering.

Higher-education and public-sector defenders in the DACH region should confirm offline-backup integrity and revisit SD-WAN / VPN gateway patch posture (the primary initial-access vectors documented for TheGentlemen in prior reporting). Listings are not victim confirmation; both organisations were listed by TheGentlemen and not confirmed by the victims themselves.
