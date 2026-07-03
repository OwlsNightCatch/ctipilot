---
schema: 1
kind: annual-report
horizon: strategic
weekly_section: weekly-annual-reports
title: "Check Point State of Ransomware Q1 2026 — ecosystem consolidation, with Switzerland and Germany named"
headline: "Check Point State of Ransomware Q1 2026 — ecosystem consolidation, with Switzerland and Germany named"
summary: "Surfaced this week for its CH/EU-specific findings, Check Point's Q1 2026 ransomware report (published 11 May, not covered in the dailies) documents a structural consolidation: the top 10 groups now hold 71.1% of all leak-site victims, the highest concentration since early 2024 and a reversal of two years of …"
discovered_at: "2026-06-22T00:15:03Z"
event_date: null
run_id: 2026-W25-0aacfe65
priority: notable
immediate_action: null
tags:
  - ransomware
  - organized-crime
regions:
  - switzerland
  - europe
  - global
sectors:
  - technology
entities:
  - "actor:thegentlemen"
  - "campaign:tds-security-tool-impersonation-checkpoint"
  - "actor:akira"
cves: []
sources:
  - url: "https://research.checkpoint.com/2026/the-state-of-ransomware-q1-2026/"
    publisher: Check Point Research — State of Ransomware Q1 2026
    role: primary
  - url: "https://www.emsisoft.com/en/blog/47562/the-state-of-ransomware-in-q1-2026/"
    publisher: Emsisoft
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

Surfaced this week for its CH/EU-specific findings, Check Point's Q1 2026 ransomware report (published 11 May, not covered in the dailies) documents a structural consolidation: the top 10 groups now hold **71.1% of all leak-site victims**, the highest concentration since early 2024 and a reversal of two years of fragmentation — meaning defenders face fewer but more professionalised adversaries ([Check Point Research](https://research.checkpoint.com/2026/the-state-of-ransomware-q1-2026/); corroborated by [Emsisoft](https://www.emsisoft.com/en/blog/47562/the-state-of-ransomware-in-q1-2026/)). The Gentlemen grew +315% quarter-on-quarter (explaining this week's Mackay Sugar and GentleKiller coverage in § 2) and LockBit 5.0 resurged +106% on a Rust rewrite. The geography is the operative detail for this audience: **Switzerland — Check Point notes Akira accounts for roughly 31% of Swiss ransomware victims**, and Germany is the #2 country globally for ransomware victims (Emsisoft). The synthesis a Swiss SOC should take: Akira is the dominant ransomware threat to model against domestically, and the consolidation trend favours investing detection effort against a smaller set of high-capability operators (Qilin, Akira, The Gentlemen, LockBit 5.0).
