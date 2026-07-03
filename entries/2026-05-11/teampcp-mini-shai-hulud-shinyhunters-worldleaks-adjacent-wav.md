---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-long-running
title: TeamPCP / Mini Shai-Hulud (ShinyHunters / WorldLeaks adjacent) — wave 4 + framework leak + IDE persistence
headline: TeamPCP / Mini Shai-Hulud (ShinyHunters / WorldLeaks adjacent) — wave 4 + framework leak + IDE persistence
summary: Full coverage in § 2 (multi-day chain).
discovered_at: "2026-05-11T05:00:37Z"
event_date: null
run_id: 2026-W20-71c96b25
priority: notable
immediate_action: null
tags:
  - supply-chain
  - ai-abuse
  - organized-crime
regions:
  - global
sectors:
  - technology
entities:
  - "campaign:mini-shai-hulud"
  - "actor:shinyhunters"
  - "actor:teampcp"
cves: []
sources:
  - url: "https://securitylabs.datadoghq.com/articles/shai-hulud-open-source-framework-static-analysis/"
    publisher: Datadog Security Labs
    role: primary
  - url: "https://www.wiz.io/blog/mini-shai-hulud-strikes-again-tanstack-more-npm-packages-compromised"
    publisher: Wiz Blog
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
migrated_from: briefs/weekly/2026-W20.md
---

Full coverage in § 2 (multi-day chain). Status-update register: long-running operator-family pattern continues; wave 4 (170+ packages / 400+ versions per daily-brief tracking) is the largest documented npm-supply-chain wave to date; the **leaked framework source** materially changes both attacker and defender posture and elevates the risk of secondary operators applying the same techniques against PyPI / Cargo / Maven Central in 2026-W21. The ShinyHunters / WorldLeaks family logged in W19's long-running record (`item:shinyhunters-worldleaks-family`) overlaps in operator targeting (AI-tooling SaaS, multi-tenant credential aggregation) with TeamPCP's npm-side ecosystem — the two clusters appear to be operating in parallel across the SaaS and registry attack surfaces with no public attribution merging them.
