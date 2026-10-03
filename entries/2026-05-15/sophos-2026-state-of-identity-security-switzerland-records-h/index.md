---
schema: 1
kind: research
title: "Sophos 2026 State of Identity Security: Switzerland records highest identity-breach incidence globally; energy and federal government hardest-hit sectors"
headline: "Sophos 2026 State of Identity Security: Switzerland records highest identity-breach incidence globally; energy and federal government hardest-hit sectors"
summary: "Sophos published its _State of Identity Security 2026_ survey on 2026-05-14, drawing on responses from IT and cybersecurity leaders across 17 countries (Help Net Security, 2026-05-14)."
discovered_at: "2026-05-15T05:00:08Z"
event_date: 2026-05-14
run_id: 2026-05-15-58b94fbd
priority: notable
immediate_action: null
tags:
  - identity
  - data-breach
  - nation-state
regions:
  - switzerland
  - europe
sectors:
  - public-sector
  - energy
entities:
  - "actor:teampcp"
cves: []
sources:
  - url: "https://www.helpnetsecurity.com/2026/05/14/sophos-2026-identity-breach-costs-report/"
    publisher: "Help Net Security, 2026-05-14"
    role: primary
closed_sources: []
evidence: []
verification: single-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-15.md
---

Sophos published its _State of Identity Security 2026_ survey on 2026-05-14, drawing on responses from IT and cybersecurity leaders across 17 countries ([Help Net Security, 2026-05-14](https://www.helpnetsecurity.com/2026/05/14/sophos-2026-identity-breach-costs-report/)). The headline finding is that more than 70% of surveyed organisations experienced at least one identity-related breach in the prior 12 months. Swiss organisations recorded the highest breach incidence among all surveyed countries. Sector analysis places energy, oil/gas, and utilities alongside federal government as the verticals with the highest breach rates — and two-thirds of ransomware victims in the survey attributed initial access to an identity compromise: stolen credentials, session hijacking, or MFA bypass. The survey corroborates NCSC-CH's sustained advisory focus on credential abuse and the trend visible across this brief series (Lumma Stealer takedown, FamousSparrow credential harvesting, TeamPCP OIDC token theft). Defenders in CH/EU public-sector environments should audit conditional access policies and MFA resilience controls — particularly for energy-sector service accounts and Entra ID/ADFS federations — against the pattern of phishing-resistant MFA requirements in NCSC-CH guidance.
