---
schema: 1
kind: incident
title: Novo Nordisk discloses theft of clinical-trial and healthcare-professional data
headline: Novo Nordisk discloses theft of clinical-trial and healthcare-professional data
summary: >
  Novo Nordisk disclosed theft of clinical-trial and healthcare-professional data, including
  directly-identifying HCP names, phone and WhatsApp contacts — a ready-made spear-phishing target
  package for EU clinical-research staff (Novo Nordisk, 2026-06-11).
discovered_at: "2026-06-13T05:00:00Z"
updated_at: "2026-06-17T05:14:35Z"
event_date: 2026-06-12
run_id: 2026-06-13-40b26572
priority: high
immediate_action: null
tags:
  - data-breach
  - phishing
  - organized-crime
  - cloud
  - identity
regions:
  - europe
  - dach
  - global
sectors:
  - healthcare
entities: []
techniques: []
affected_products: []
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
  - url: "https://www.novonordisk.com/news-and-media/latest-news/incident-update.html"
    publisher: Novo Nordisk incident update
    role: primary
  - url: "https://securityaffairs.com/193650/security/novo-nordisk-confirms-data-theft-what-attackers-took-and-what-they-didnt.html"
    publisher: Security Affairs
    role: corroborating
  - url: "https://www.globalbankingandfinance.com/hacking-group-claims-major-hack-novo-nordisk-attempted-25/"
    publisher: "Global Banking & Finance Review, 2026-06-16"
    role: primary
  - url: "https://www.insurancebusinessmag.com/us/news/cyber/ozempic-maker-novo-nordisk-hit-with-25-million-ransom-demand-after-claimed-data-breach-579161.aspx"
    publisher: "Insurance Business Magazine, 2026-06-16"
    role: corroborating
  - url: "https://www.moxfive.com/blog/who-is-fulcrumsec-inside-the-cloud-extortion-group-behind-21-victims-and-counting"
    publisher: "MOXFIVE actor profile, 2026-06-10"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification: null
watchlist_hit: false
actions: []
updates:
  - at: "2026-06-16T05:09:03Z"
    run_id: 2026-06-16-38d638e1
    type: update
    summary: >
      UPDATE (originally covered 2026-06-13): Novo Nordisk published an incident update on 2026-06-15
      clarifying the scope of the theft: clinical-trial data taken was pseudonymised (limited direct
      re-identification risk for trial subjects) (Novo Nordisk, 2026-06-15), but separately stolen
      **healthcare-professional …
    fields:
      - sources
      - body
    merged_from: 2026-06-16/novo-nordisk-clarifies-stolen-data-scope-non-pseudonymised-h
  - at: "2026-06-17T05:14:35Z"
    run_id: 2026-06-17-e102009c
    type: update
    summary: >
      UPDATE (originally covered 2026-06-13): The cloud data-extortion group FulcrumSec has publicly
      claimed the Novo Nordisk breach, saying it spent more than two months inside the networks and
      exfiltrated roughly 1.3 TB (~700,000 files) including source code, drug-pipeline data, ~11,500
      pseudonymised clinical-trial …
    fields:
      - regions
      - sources
      - tags
      - body
    merged_from: 2026-06-17/novo-nordisk-fulcrumsec-claims-authorship-25m-demand-refused
migrated_from: briefs/2026-06-13.md
---

Danish pharmaceutical maker Novo Nordisk disclosed on 11 June that an external party gained unauthorised access to a limited number of internal IT systems and copied non-public data, including clinical-trial participant records and healthcare-professional (HCP) contact information ([Novo Nordisk, 2026-06-11](https://www.novonordisk.com/news-and-media/news-and-ir-materials/news-details.html?id=916571)). The clinical-trial data is described as pseudonymised — random alphanumeric participant IDs plus sex, year of birth, biomarkers, immunogenicity and health data, and lifestyle factors — and not directly linked to names. The HCP data, however, is directly identifying: names, registration numbers, email addresses, phone numbers, WhatsApp contact details and office locations ([BleepingComputer, 2026-06-12](https://www.bleepingcomputer.com/news/security/pharmaceutical-giant-novo-nordisk-discloses-security-breach/)). The initial-access vector is not disclosed and no threat actor has been named; affected systems were taken offline and authorities engaged. As an EU-registered controller processing EU/EEA trial data, the breach engages GDPR Article 33 and Danish Datatilsynet notification, and Swiss equivalents under the nDSG for domestic trials.

**Defender takeaway:** The HCP record set (name + phone + WhatsApp for named clinical investigators) is a complete spear-phishing targeting package — brief clinical-research and pharma-partner staff on elevated social-engineering risk, and watch for WhatsApp/SMS pretexting against named researchers, since no malware IOCs are available to anchor a hunt.

## Update — 2026-06-16T05:09:03Z

Novo Nordisk published an incident update on 2026-06-15 clarifying the scope of the theft: clinical-trial data taken was **pseudonymised** (limited direct re-identification risk for trial subjects) ([Novo Nordisk, 2026-06-15](https://www.novonordisk.com/news-and-media/latest-news/incident-update.html)), but separately stolen **healthcare-professional (HCP) data was non-pseudonymised** — names, registration numbers and contact details ([Security Affairs, 2026-06-15](https://securityaffairs.com/193650/security/novo-nordisk-confirms-data-theft-what-attackers-took-and-what-they-didnt.html)).

The non-pseudonymised HCP records bring the incident within GDPR Article 33 breach-notification obligations and raise targeted-phishing risk against named medical professionals ([Security Affairs, 2026-06-15](https://securityaffairs.com/193650/security/novo-nordisk-confirms-data-theft-what-attackers-took-and-what-they-didnt.html)). Healthcare and pharma defenders should expect HCP-impersonation and credential-phishing lures referencing the breach.

## Update — 2026-06-17T05:14:35Z

The cloud data-extortion group FulcrumSec has publicly claimed the Novo Nordisk breach, saying it spent more than two months inside the networks and exfiltrated roughly 1.3 TB (~700,000 files) including source code, drug-pipeline data, ~11,500 pseudonymised clinical-trial records and internal AI artefacts; it demanded $25M, was refused, and is now exploring private sale of the data ([Global Banking & Finance Review, 2026-06-16](https://www.globalbankingandfinance.com/hacking-group-claims-major-hack-novo-nordisk-attempted-25/)).

FulcrumSec is a data-theft-only (non-ransomware) group active since late 2025 with 21+ prior claimed victims; an actor profile characterises its access vectors as unpatched public-facing apps, dormant/embedded credentials and API keys, absent MFA and misconfigured cloud storage ([MOXFIVE, 2026-06-10](https://www.moxfive.com/blog/who-is-fulcrumsec-inside-the-cloud-extortion-group-behind-21-victims-and-counting)). Novo Nordisk has confirmed unauthorised access to a limited number of internal systems and pseudonymised clinical-trial data exposure but has not validated FulcrumSec's scope claims ([Insurance Business Magazine, 2026-06-16](https://www.insurancebusinessmag.com/us/news/cyber/ozempic-maker-novo-nordisk-hit-with-25-million-ransom-demand-after-claimed-data-breach-579161.aspx)). Detection focus for FulcrumSec-style actors: large outbound transfers (DLP), cloud-storage access logs, OAuth grants to unfamiliar apps, and long-dwell reuse of stale service-account credentials. Enforce MFA on all privileged cloud identities and rotate dormant credentials.
