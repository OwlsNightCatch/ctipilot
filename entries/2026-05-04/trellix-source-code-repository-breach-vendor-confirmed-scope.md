---
schema: 1
kind: incident
horizon: strategic
weekly_section: weekly-incidents-recap
title: "Trellix source code repository breach — vendor confirmed, scope undisclosed, supply-chain integrity question open"
headline: "Trellix source code repository breach — vendor confirmed, scope undisclosed, supply-chain integrity question open"
summary: "Trellix, a major endpoint-security / XDR vendor serving enterprise and government customers globally, confirmed on 2026-05-04 that an unauthorised party accessed a portion of its internal source code repository."
discovered_at: "2026-05-04T05:00:20Z"
event_date: 2026-05-06
run_id: 2026-W19-a5788b22
priority: notable
immediate_action: null
tags:
  - data-breach
  - supply-chain
regions:
  - global
sectors:
  - technology
entities:
  - "incident:trellix-source-code-2026"
cves: []
sources:
  - url: "https://www.bleepingcomputer.com/news/security/trellix-discloses-data-breach-after-source-code-repository-hack/"
    publisher: BleepingComputer — Trellix data breach
    role: primary
  - url: "https://thehackernews.com/2026/05/trellix-confirms-source-code-breach.html"
    publisher: The Hacker News — Trellix source code
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

Trellix, a major endpoint-security / XDR vendor serving enterprise and government customers globally, confirmed on 2026-05-04 that an unauthorised party accessed a portion of its internal source code repository. The company engaged external forensic specialists and notified law enforcement; Trellix stated no evidence was found that its product code-release or distribution pipeline was affected and no evidence the accessed code was exploited or altered. The initial access vector, duration of access, scope of repositories affected, and customer data impact have not been disclosed ([BleepingComputer, 2026-05-04](https://www.bleepingcomputer.com/news/security/trellix-discloses-data-breach-after-source-code-repository-hack/) · [The Hacker News, 2026-05-04](https://thehackernews.com/2026/05/trellix-confirms-source-code-breach.html) · [daily 2026-05-06](/briefs/2026-05-06/)). **Defender takeaway:** organisations running Trellix endpoint or XDR products should maintain elevated scrutiny on Trellix software updates until the forensic investigation publicly concludes; the supply-chain integrity question — could the accessed code be re-used by an attacker for bug discovery or implant tailoring? — remains unresolved.
