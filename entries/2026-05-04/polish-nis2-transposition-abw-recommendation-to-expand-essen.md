---
schema: 1
kind: policy
horizon: strategic
weekly_section: weekly-policy
title: Polish NIS2 transposition + ABW recommendation to expand essential-entity coverage below headcount threshold
headline: Polish NIS2 transposition + ABW recommendation to expand essential-entity coverage below headcount threshold
summary: "ABW's 2025 Annual Report (covered 2026-05-09) notes that Poland transposed NIS2 into national law effective 2026-02-01 (Ustawa z dnia 28 listopada 2025 r. o krajowym systemie cyberbezpieczeństwa) with water-distribution operators above the 50-employee threshold now classified as Essential Entities subject to mandatory …"
discovered_at: "2026-05-04T05:00:44Z"
event_date: 2026-05-09
run_id: 2026-W19-a5788b22
priority: notable
immediate_action: null
tags:
  - law-enforcement
  - ot-ics
  - eu-nexus
regions:
  - europe
sectors:
  - water
  - public-sector
entities: []
cves: []
sources:
  - url: "https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-207a"
    publisher: CISA AA24-207A (background)
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

ABW's 2025 Annual Report (covered 2026-05-09) notes that Poland transposed NIS2 into national law effective 2026-02-01 (Ustawa z dnia 28 listopada 2025 r. o krajowym systemie cyberbezpieczeństwa) with water-distribution operators above the 50-employee threshold now classified as Essential Entities subject to mandatory incident notification to CSIRT GOV (ABW) within 24/72 hours. **What changed in 2026-W19:** ABW explicitly notes the five named water-OT-attack facilities fell below the NIS2 threshold at the time of intrusion and is recommending legislative action to extend NIS2 obligations to critical-function entities regardless of headcount ([daily 2026-05-09 UPDATE](/briefs/2026-05-09/)). **What defenders need to do differently:** small CH/EU municipal CI operators (water, energy distribution, transport, healthcare) below NIS2 essential-entity thresholds should not assume regulatory-coverage absence implies threat-coverage absence; the ABW evidence demonstrates state-sponsored targeting concentrates *toward* under-regulated operators rather than away from them. Operators in this category should pre-emptively adopt NIS2-equivalent incident-notification and asset-inventory baselines. Dragos's 81% flat-network finding (§ 6) lands at the same operational target.
