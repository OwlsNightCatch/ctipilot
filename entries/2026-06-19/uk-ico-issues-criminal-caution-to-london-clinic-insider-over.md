---
schema: 1
kind: incident
horizon: operational
title: UK ICO issues criminal caution to London Clinic insider over Princess of Wales medical-record access
headline: UK ICO issues criminal caution to London Clinic insider over Princess of Wales medical-record access
summary: "The UK Information Commissioner's Office closed a two-year criminal investigation into the deliberate misuse of Catherine, Princess of Wales' medical records at The London Clinic, issuing a formal caution to a former staff member under s.170(5) of the Data Protection Act 2018 (ICO, 2026-06; Infosecurity Magazine …"
discovered_at: "2026-06-19T05:20:51Z"
event_date: 2026-06-18
run_id: 2026-06-19-c306b105
priority: notable
immediate_action: null
tags:
  - insider-threat
  - data-breach
  - law-enforcement
regions:
  - uk
  - europe
sectors:
  - healthcare
entities: []
cves: []
sources:
  - url: "https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2026/06/ico-statement-conclusion-of-criminal-investigation/"
    publisher: ICO statement
    role: primary
  - url: "https://www.infosecurity-magazine.com/news/ico-cautions-healthcare-worker/"
    publisher: Infosecurity Magazine
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
migrated_from: briefs/2026-06-19.md
---

The UK Information Commissioner's Office closed a two-year criminal investigation into the deliberate misuse of Catherine, Princess of Wales' medical records at The London Clinic, issuing a formal caution to a former staff member under s.170(5) of the Data Protection Act 2018 ([ICO, 2026-06](https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2026/06/ico-statement-conclusion-of-criminal-investigation/); [Infosecurity Magazine, 2026-06-18](https://www.infosecurity-magazine.com/news/ico-cautions-healthcare-worker/)). Section 170 — unlawful obtaining/disclosing of personal data, carrying up to two years' imprisonment — is pursued under the ICO's own criminal-prosecution authority, distinct from its civil UK GDPR fine regime; the s.170(5) caution requires an admission of guilt. The ICO found no evidence records were sold, treated the offer to disclose for financial gain as the aggravating element, and concluded the clinic's own information-governance arrangements did not warrant regulatory action.
**Defender takeaway:** this is a textbook clinical-insider pattern — privileged Electronic Patient Record access, a high-profile data subject creating monetisation incentive, opportunistic abuse. Comparable Swiss and EU controllers face criminal exposure too (Swiss DPA Art. 60; GDPR Art. 84 member-state criminal competence). Detection posture: alert on EPR accesses outside an accessor's assigned care team (RBAC-violation hunting on access-audit logs, `T1078` legitimate-access abuse), which the NHS IG Toolkit and equivalents already mandate logging for.
