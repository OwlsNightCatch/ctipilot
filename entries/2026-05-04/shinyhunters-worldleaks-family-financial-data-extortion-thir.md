---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-long-running
title: "ShinyHunters / WorldLeaks family (financial-data extortion, third-party-SaaS pivot)"
headline: "ShinyHunters / WorldLeaks family (financial-data extortion, third-party-SaaS pivot)"
summary: "Current state: most-active operator family of 2026-W19. Confirmed parallel involvement across Vimeo/Anodot, Inditex/Zara/Anodot, ADT/Okta-SSO/Salesforce, and Canvas/Instructure (second-intrusion claim despite May 8 patches)."
discovered_at: "2026-05-04T05:00:33Z"
event_date: null
run_id: 2026-W19-a5788b22
priority: notable
immediate_action: null
tags:
  - organized-crime
  - data-breach
  - supply-chain
regions:
  - europe
  - global
sectors:
  - technology
  - education
  - retail
entities:
  - "actor:shinyhunters"
cves: []
sources:
  - url: "https://www.bleepingcomputer.com/news/security/instructure-confirms-data-breach-shinyhunters-claims-attack/"
    publisher: BleepingComputer — Instructure data breach
    role: primary
  - url: "https://securityaffairs.com/191859/cyber-crime/zara-data-breach-197000-customers-exposed-in-third-party-security-incident.html"
    publisher: SecurityAffairs — Zara breach
    role: corroborating
  - url: "https://vimeo.com/blog/post/anodot-third-party-security-incident"
    publisher: Vimeo official blog
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

Current state: most-active operator family of 2026-W19. Confirmed parallel involvement across Vimeo/Anodot, Inditex/Zara/Anodot, ADT/Okta-SSO/Salesforce, and Canvas/Instructure (second-intrusion claim despite May 8 patches). The architectural pattern across these incidents — third-party analytics, BI, integration, or LTI service accounts holding broad read access to tenant data — is consistent and converging. The Canvas/Instructure extortion deadline is 2026-05-12 (two days out at week-end). Outstanding defender question: which AI-tooling SaaS or analytics SaaS vendor will be the next confirmed pivot point. ()
