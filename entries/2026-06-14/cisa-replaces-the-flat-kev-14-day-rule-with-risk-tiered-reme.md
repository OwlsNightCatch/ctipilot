---
schema: 1
kind: policy
horizon: strategic
weekly_section: weekly-policy
title: CISA replaces the flat KEV 14-day rule with risk-tiered remediation (BOD 26-04)
headline: CISA replaces the flat KEV 14-day rule with risk-tiered remediation (BOD 26-04)
summary: "CISA issued Binding Operational Directive 26-04 on 10 June, superseding BOD 19-02 and BOD 22-01 and replacing the flat 14-day KEV remediation rule with risk-tiered deadlines, including a 3-day class for the worst exposures (CISA; daily 06-12)."
discovered_at: "2026-06-14T23:57:42Z"
event_date: null
run_id: 2026-W24-bd5a7519
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - us-nexus
regions:
  - us
sectors:
  - public-sector
entities: []
cves: []
sources:
  - url: "https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk"
    publisher: CISA BOD 26-04
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
migrated_from: briefs/weekly/2026-W24.md
---

CISA issued Binding Operational Directive 26-04 on 10 June, superseding BOD 19-02 and BOD 22-01 and replacing the flat 14-day KEV remediation rule with risk-tiered deadlines, including a 3-day class for the worst exposures ([CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk); [daily 06-12](/briefs/2026-06-12/)). The deadlines bind only US Federal Civilian Executive Branch agencies and carry no compliance weight in CH/EU. **What to do differently — and what not to:** the useful signal for a Swiss/EU SOC is the *risk-tiering model* (exploitation status and exposure driving remediation urgency), not the deadlines themselves; the KEV listing flag remains jurisdiction-agnostic confirmation of in-the-wild exploitation, but a KEV deadline is never the reason an item is urgent for this audience.
