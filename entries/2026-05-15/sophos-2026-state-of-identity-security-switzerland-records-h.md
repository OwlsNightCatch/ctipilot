---
schema: 1
kind: research
title: "Sophos State of Identity Security 2026: Swiss respondents report the highest identity-breach rate of 17 countries, at 89%"
headline: "Sophos survey: Swiss organisations reported the highest identity-breach rate of 17 countries, at 89%"
summary: "Sophos's State of Identity Security 2026, published on 2026-05-12, surveyed 5,000 IT and security leaders in 17 countries: 71% reported at least one identity-related breach in the past year, Switzerland the most at 89%, and two-thirds of ransomware victims said their ransomware incident was directly tied to their most significant identity attack. Help Net Security adds that energy, oil and gas, utilities and federal government recorded the highest breach rates."
discovered_at: "2026-05-15T05:00:08Z"
event_date: 2026-05-12
run_id: 2026-05-15-58b94fbd
priority: notable
immediate_action: null
tags:
  - identity
  - data-breach
regions:
  - switzerland
  - global
sectors:
  - public-sector
  - energy
entities:
  - "report:sophos-identity-security-2026"
techniques: []
affected_products: []
cves: []
sources:
  - url: "https://www.helpnetsecurity.com/2026/05/14/sophos-2026-identity-breach-costs-report/"
    publisher: "Help Net Security"
    date: "2026-05-14"
    role: primary
  - url: "https://www.sophos.com/blog/sophos-state-of-identity-security-2026"
    publisher: "Sophos"
    date: "2026-05-12"
    role: primary
closed_sources: []
evidence:
  - quote: "Geographically, Switzerland reported the highest breach rate at 89%, followed by Mexico at 83%"
    publisher: Sophos
    source_url: "https://www.sophos.com/blog/sophos-state-of-identity-security-2026"
  - quote: "Two-thirds of ransomware victims (67%) reported that their ransomware incident was directly tied to their most significant identity attack."
    publisher: Sophos
    source_url: "https://www.sophos.com/blog/sophos-state-of-identity-security-2026"
  - quote: "oil and gas, utilities, and federal government sectors recorded the highest breach rates."
    publisher: Help Net Security
    source_url: "https://www.helpnetsecurity.com/2026/05/14/sophos-2026-identity-breach-costs-report/"
verification: multi-source
sourcing_note: "Sophos's own survey of 5,000 respondents is the only data source; the figures are self-reported, and Help Net Security reports the same survey."
confidence: medium
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 3
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-15.md
updated_at: null
updates:
  - at: "2026-10-21T20:37:00Z"
    run_id: 2026-10-21T1148Z-audit
    type: correction
    summary: >
      Sophos published its State of Identity Security 2026 on 2026-05-12, two days before Help Net
      Security's report, and its finding is that two-thirds of ransomware victims tied the incident to
      their most significant identity attack, not that they attributed initial access to stolen
      credentials, session hijacking or MFA bypass. Neither source mentions NCSC-CH, the Lumma takedown,
      FamousSparrow or TeamPCP, so those links and the guidance built on them are removed.
    fields: [affected_products, body, classification, confidence, entities, event_date, evidence, headline, regions, sources, sourcing_note, summary, tags, techniques, title, verification]
---

Sophos's State of Identity Security 2026, published on 2026-05-12, surveyed 5,000 IT and cybersecurity leaders across 17 countries and 14 industries: 71% reported at least one identity-related breach in the past 12 months, Switzerland reported the highest rate at 89%, followed by Mexico at 83%, and two-thirds of ransomware victims (67%) said their ransomware incident was directly tied to their most significant identity attack ([Sophos, 2026-05-12](https://www.sophos.com/blog/sophos-state-of-identity-security-2026)). Weak management of non-human identities such as API keys and service accounts was a root cause in 41% of successful identity breaches ([Sophos, 2026-05-12](https://www.sophos.com/blog/sophos-state-of-identity-security-2026)). Help Net Security reports that the energy, oil and gas, utilities and federal government sectors recorded the highest breach rates ([Help Net Security, 2026-05-14](https://www.helpnetsecurity.com/2026/05/14/sophos-2026-identity-breach-costs-report/)).

**Defender takeaway:** no decision changes on survey figures alone; the two gaps the survey measures are checkable in one's own estate: more than half of companies reviewed unusual login attempts no more than once every three months, and only 34.3% rotated and audited non-human identities weekly or more often ([Help Net Security, 2026-05-14](https://www.helpnetsecurity.com/2026/05/14/sophos-2026-identity-breach-costs-report/)).

## Correction — 2026-10-21T20:37:00Z

Sophos published the survey on 2026-05-12 ([Sophos, 2026-05-12](https://www.sophos.com/blog/sophos-state-of-identity-security-2026)); 2026-05-14 is the date of Help Net Security's report ([Help Net Security, 2026-05-14](https://www.helpnetsecurity.com/2026/05/14/sophos-2026-identity-breach-costs-report/)). Its ransomware finding is that two-thirds of ransomware victims (67%) said their ransomware incident was directly tied to their most significant identity attack ([Sophos, 2026-05-12](https://www.sophos.com/blog/sophos-state-of-identity-security-2026)); neither source says they attributed initial access to an identity compromise or breaks it down into stolen credentials, session hijacking and MFA bypass. Neither source mentions NCSC-CH, the Lumma Stealer takedown, FamousSparrow or TeamPCP, so the cross-links and the NCSC-CH guidance built on them are removed.
