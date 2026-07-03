---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-long-running
title: "UNC6671 / BlackFile — GTIG publishes the full profile; group announced shutdown \"under this name\", rebrand probable"
headline: "UNC6671 / BlackFile — GTIG publishes the full profile; group announced shutdown \"under this name\", rebrand probable"
summary: "Resolving a W21 carry-forward watch item: GTIG published a definitive UNC6671 / BlackFile profile in mid-May 2026, characterising the operation as an adversary-in-the-middle vishing specialist targeting Microsoft 365 and Okta SSO environments in retail and hospitality (vishing impersonating IT support → …"
discovered_at: "2026-05-25T05:00:24Z"
event_date: null
run_id: 2026-W22-da77963d
priority: notable
immediate_action: null
tags:
  - organized-crime
  - identity
  - phishing
regions:
  - global
  - europe
sectors:
  - retail
  - finance
entities:
  - "actor:unc6671"
cves: []
sources:
  - url: "https://cloud.google.com/blog/topics/threat-intelligence/blackfile-vishing-extortion-operation"
    publisher: Google Cloud / GTIG — BlackFile vishing-extortion operation
    role: primary
  - url: "https://cyberscoop.com/blackfile-data-theft-extortion-retail-unit-42-rh-isac/"
    publisher: CyberScoop
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
migrated_from: briefs/weekly/2026-W22.md
---

Resolving a W21 carry-forward watch item: GTIG published a definitive **UNC6671 / BlackFile** profile in mid-May 2026, characterising the operation as an **adversary-in-the-middle vishing specialist** targeting Microsoft 365 and Okta SSO environments in retail and hospitality (vishing impersonating IT support → MFA-bypass / credential grant → AiTM session-token harvest → exfiltration → extortion over the Session messenger). The leak-site went offline in late April, briefly resumed on 2026-05-11 to announce "BlackFile is shutting down… **under this name**," and went dark again — GTIG's phrasing and the qualifier point to a **probable rebrand** rather than a genuine exit. Defenders should keep the AiTM-vishing → rogue-MFA → SSO-token-theft TTP set on watch under any new brand; the tradecraft, not the name, is the durable indicator.
