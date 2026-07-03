---
schema: 1
kind: annual-report
horizon: strategic
weekly_section: weekly-annual-reports
title: "Sophos 2026 State of Identity Security — 71% of orgs breached via identity, 41% root-caused to non-human-identity mismanagement, Switzerland records highest incidence"
headline: "Sophos 2026 State of Identity Security — 71% of orgs breached via identity, 41% root-caused to non-human-identity mismanagement, Switzerland records highest"
summary: "Published 2026-05-15. Vendor-agnostic survey of 5,000 IT and security leaders across 17 countries (Q1 2026 fieldwork)."
discovered_at: "2026-05-11T05:00:29Z"
event_date: 2026-05-15
run_id: 2026-W20-71c96b25
priority: notable
immediate_action: null
tags:
  - identity
  - supply-chain
regions:
  - global
  - switzerland
sectors:
  - public-sector
entities: []
cves: []
sources:
  - url: "https://www.sophos.com/en-us/blog/sophos-state-of-identity-security-2026"
    publisher: Sophos blog
    role: primary
  - url: "https://www.sophos.com/en-us/press/press-releases/2026/05/71-percent-organizations-suffered-identity-breach-state-of-identity-security-2026"
    publisher: Sophos press release
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

Published 2026-05-15. Vendor-agnostic survey of 5,000 IT and security leaders across 17 countries (Q1 2026 fieldwork). The defender-relevant findings beyond the headline 71% identity-breach figure: (a) **identity-to-ransomware pipeline dominant** — 67% of ransomware victims attributed their ransomware incident directly to a prior identity attack, establishing identity-protocol abuse as the operationally dominant initial-access pattern; (b) **non-human identity (NHI) mismanagement is the leading root cause** — service accounts, API keys, AI-agent identities outnumber human identities by ratios up to 100:1 in surveyed organisations, weak NHI lifecycle management was the root cause in 41% of successful identity breaches, only 34% of organisations regularly audit NHI accounts; (c) **Switzerland records the highest identity-breach incidence globally** in the survey period; the daily 2026-05-15 also reported energy as the hardest-hit sector ([Sophos blog](https://www.sophos.com/en-us/blog/sophos-state-of-identity-security-2026); [Help Net Security — Sophos 2026 identity-breach costs report](https://www.helpnetsecurity.com/2026/05/14/sophos-2026-identity-breach-costs-report/); [daily 2026-05-15](/briefs/2026-05-15/)).

The synthesis lens the daily did not have room for: the Sophos data corroborates the W19 Mandiant M-Trends finding that identity-rooted intrusions dominate IR-case data, and it converges with the Verizon DBIR 2026 finding (below) that stolen credentials remain the most common initial-access vector. The composite picture: for Swiss federal / cantonal estates with high service-account density and no NHI lifecycle governance, the **NHI inventory + lifecycle gap is the single highest-leverage control deficit** disclosed in this week's research output. The Sophos data is the empirical basis for prioritising NHI governance over endpoint-EDR upgrades, where budget pressure forces a choice. Detection focus: anomalous service-account Kerberos TGS requests (T1558.003 Kerberoasting), unusual OAuth token grants from CI/CD service identities, API key usage from unexpected source IPs or geographies.
