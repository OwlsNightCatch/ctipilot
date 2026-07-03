---
schema: 1
kind: annual-report
horizon: strategic
weekly_section: weekly-annual-reports
title: Dragos 2025 OT Cybersecurity Year in Review — Frontlines IR Edition
headline: Dragos 2025 OT Cybersecurity Year in Review — Frontlines IR Edition
summary: "Dragos's 8th annual OT industrial-IR retrospective (covered 2026-05-08) is the week's most directly actionable annual-report reference for Swiss / EU CI operators reading after the Polish water OT attribution: Dragos's blog announcement records that **65 percent of sites assessed had insecure remote-access conditions …"
discovered_at: "2026-05-04T05:00:28Z"
event_date: 2026-05-08
run_id: 2026-W19-a5788b22
priority: notable
immediate_action: null
tags:
  - ot-ics
  - ai-abuse
regions:
  - global
  - europe
sectors:
  - water
  - energy
  - manufacturing
entities:
  - "report:dragos-2025-ot-frontlines"
cves: []
sources:
  - url: "https://www.dragos.com/blog/dragos-8th-annual-ot-cybersecurity-year-in-review-is-now-available"
    publisher: Dragos — 8th Annual OT Cybersecurity Year in Review blog announcement
    role: primary
  - url: "https://www.dragos.com/blog/ai-assisted-ics-attack-water-utility/"
    publisher: Dragos — AI-assisted ICS attack water utility
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
migrated_from: briefs/weekly/2026-W19.md
---

Dragos's 8th annual OT industrial-IR retrospective (covered 2026-05-08) is the week's most directly actionable annual-report reference for Swiss / EU CI operators reading after the Polish water OT attribution: Dragos's blog announcement records that **65 percent of sites assessed had insecure remote-access conditions, including default credentials, unpatched VPNs, and exposed RDP sessions**, and that many organisations believe they have proper IT/OT network segmentation while routine penetration tests reveal hidden connections. The report's NIS2 Annex-I compliance discussion directly contextualises the ABW 2025 Annual Report observation (§ 4) that the five Polish water-treatment facilities fell below the NIS2 essential-entity threshold and that legislative action is being considered to extend NIS2 obligations to critical-function entities regardless of headcount. The IEC 62443 zoning and conduit model is the recommended remediation reference architecture; the Swiss NCSC sector-specific ICS guidance (SARI framework) is the equivalent CH-side baseline. The defender lesson from the Dragos AI-assisted water utility attack item (2026-05-07) lands in the same line: AI tooling is progressively reducing the technical bar for OT-targeting attacks; prevention-only OT security strategies are inadequate as primary defences ([daily 2026-05-08](/briefs/2026-05-08/), [daily 2026-05-07 — AI-assisted ICS attack](/briefs/2026-05-07/)).
