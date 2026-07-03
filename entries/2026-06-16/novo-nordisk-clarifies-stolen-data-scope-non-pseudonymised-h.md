---
schema: 1
kind: incident
horizon: operational
title: Novo Nordisk clarifies stolen-data scope — non-pseudonymised HCP data in play
headline: Novo Nordisk clarifies stolen-data scope — non-pseudonymised HCP data in play
summary: "UPDATE (originally covered 2026-06-13): Novo Nordisk published an incident update on 2026-06-15 clarifying the scope of the theft: clinical-trial data taken was pseudonymised (limited direct re-identification risk for trial subjects) (Novo Nordisk, 2026-06-15), but separately stolen **healthcare-professional …"
discovered_at: "2026-06-16T05:09:03Z"
event_date: 2026-06-15
run_id: 2026-06-16-38d638e1
priority: notable
immediate_action: null
tags:
  - data-breach
  - phishing
regions:
  - europe
  - dach
sectors:
  - healthcare
entities: []
cves: []
sources:
  - url: "https://www.novonordisk.com/news-and-media/latest-news/incident-update.html"
    publisher: Novo Nordisk incident update
    role: primary
  - url: "https://securityaffairs.com/193650/security/novo-nordisk-confirms-data-theft-what-attackers-took-and-what-they-didnt.html"
    publisher: Security Affairs
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: 2026-06-13/novo-nordisk-discloses-theft-of-clinical-trial-and-healthcar
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-16.md
---

**UPDATE (originally covered 2026-06-13):** Novo Nordisk published an incident update on 2026-06-15 clarifying the scope of the theft: clinical-trial data taken was **pseudonymised** (limited direct re-identification risk for trial subjects) ([Novo Nordisk, 2026-06-15](https://www.novonordisk.com/news-and-media/latest-news/incident-update.html)), but separately stolen **healthcare-professional (HCP) data was non-pseudonymised** — names, registration numbers and contact details ([Security Affairs, 2026-06-15](https://securityaffairs.com/193650/security/novo-nordisk-confirms-data-theft-what-attackers-took-and-what-they-didnt.html)).

The non-pseudonymised HCP records bring the incident within GDPR Article 33 breach-notification obligations and raise targeted-phishing risk against named medical professionals ([Security Affairs, 2026-06-15](https://securityaffairs.com/193650/security/novo-nordisk-confirms-data-theft-what-attackers-took-and-what-they-didnt.html)). Healthcare and pharma defenders should expect HCP-impersonation and credential-phishing lures referencing the breach.
