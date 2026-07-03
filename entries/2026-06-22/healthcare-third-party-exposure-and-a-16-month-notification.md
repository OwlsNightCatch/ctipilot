---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-sector-patterns
title: Healthcare — third-party exposure and a 16-month notification gap
headline: Healthcare — third-party exposure and a 16-month notification gap
summary: "Healthcare breaches this week were dominated by third-party and disclosure-timing failures rather than direct perimeter compromise. iRhythm filed an SEC 8-K reporting data theft via social engineering of a third-party-hosted application (SEC 8-K, 2026-06-15; daily 06-16)."
discovered_at: "2026-06-22T00:14:50Z"
event_date: 2026-06-20
run_id: 2026-W25-0aacfe65
priority: notable
immediate_action: null
tags:
  - data-breach
  - ransomware
regions:
  - uk
  - us
sectors:
  - healthcare
entities: []
cves: []
sources:
  - url: "https://www.sec.gov/Archives/edgar/data/0001388658/000138865826000055/irtc-20260610.htm"
    publisher: iRhythm SEC 8-K
    role: primary
  - url: "https://hipaapulse.com/uk-more-than-one-year-later-hcrg-is-first-notifying-patients-of-33ec763c"
    publisher: HIPAA Pulse — HCRG
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
migrated_from: briefs/weekly/2026-W25.md
---

Healthcare breaches this week were dominated by third-party and disclosure-timing failures rather than direct perimeter compromise. iRhythm filed an SEC 8-K reporting data theft via social engineering of a third-party-hosted application ([SEC 8-K, 2026-06-15](https://www.sec.gov/Archives/edgar/data/0001388658/000138865826000055/irtc-20260610.htm); [daily 06-16](/briefs/2026-06-16/)). HCRG Care Group began notifying patients in June 2026 of a Medusa ransomware attack that occurred in **February 2025** — a 16-month gap between incident and notification ([HIPAA Pulse, 2026-06-20](https://hipaapulse.com/uk-more-than-one-year-later-hcrg-is-first-notifying-patients-of-33ec763c); [daily 06-21](/briefs/2026-06-21/)). Amazon's One Medical confirmed a legacy-storage breach (§ 2). The defender takeaway: most healthcare exposure this week entered through suppliers and legacy systems, not the front door.
