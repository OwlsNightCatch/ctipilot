---
schema: 1
kind: incident
horizon: operational
title: Novo Nordisk discloses theft of clinical-trial and healthcare-professional data
headline: Novo Nordisk discloses theft of clinical-trial and healthcare-professional data
summary: "Novo Nordisk disclosed theft of clinical-trial and healthcare-professional data, including directly-identifying HCP names, phone and WhatsApp contacts — a ready-made spear-phishing target package for EU clinical-research staff (Novo Nordisk, 2026-06-11)."
discovered_at: "2026-06-13T05:00:00Z"
event_date: 2026-06-12
run_id: 2026-06-13-40b26572
priority: high
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
  - url: "https://www.novonordisk.com/news-and-media/news-and-ir-materials/news-details.html?id=916571"
    publisher: Novo Nordisk
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/pharmaceutical-giant-novo-nordisk-discloses-security-breach/"
    publisher: BleepingComputer
    role: corroborating
  - url: "https://www.theregister.com/security/2026/06/12/novo-nordisk-says-hackers-stole-clinical-trial-data/5254812"
    publisher: The Register
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
migrated_from: briefs/2026-06-13.md
---

Danish pharmaceutical maker Novo Nordisk disclosed on 11 June that an external party gained unauthorised access to a limited number of internal IT systems and copied non-public data, including clinical-trial participant records and healthcare-professional (HCP) contact information ([Novo Nordisk, 2026-06-11](https://www.novonordisk.com/news-and-media/news-and-ir-materials/news-details.html?id=916571)). The clinical-trial data is described as pseudonymised — random alphanumeric participant IDs plus sex, year of birth, biomarkers, immunogenicity and health data, and lifestyle factors — and not directly linked to names. The HCP data, however, is directly identifying: names, registration numbers, email addresses, phone numbers, WhatsApp contact details and office locations ([BleepingComputer, 2026-06-12](https://www.bleepingcomputer.com/news/security/pharmaceutical-giant-novo-nordisk-discloses-security-breach/)). The initial-access vector is not disclosed and no threat actor has been named; affected systems were taken offline and authorities engaged. As an EU-registered controller processing EU/EEA trial data, the breach engages GDPR Article 33 and Danish Datatilsynet notification, and Swiss equivalents under the nDSG for domestic trials.

**Defender takeaway:** The HCP record set (name + phone + WhatsApp for named clinical investigators) is a complete spear-phishing targeting package — brief clinical-research and pharma-partner staff on elevated social-engineering risk, and watch for WhatsApp/SMS pretexting against named researchers, since no malware IOCs are available to anchor a hunt.
