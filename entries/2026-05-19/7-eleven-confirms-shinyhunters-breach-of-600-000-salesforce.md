---
schema: 1
kind: incident
horizon: operational
title: "7-Eleven confirms ShinyHunters breach of 600,000+ Salesforce franchise-application records — same campaign as Instructure, Vimeo, Wynn Resorts, Vercel, Medtronic"
headline: "7-Eleven confirms ShinyHunters breach of 600,000+ Salesforce franchise-application records — same campaign as Instructure, Vimeo, Wynn Resorts, Vercel"
summary: "7-Eleven confirms ShinyHunters breach of 600,000+ Salesforce franchise-application records (SecurityWeek, 2026-05-18). Part of the broader ShinyHunters Salesforce-targeting campaign with co-victims Instructure, Vimeo, Wynn Resorts, Vercel, Medtronic — phishing / OAuth / misconfiguration, not Salesforce-product vulnerabilities."
discovered_at: "2026-05-19T05:00:03Z"
event_date: 2026-05-18
run_id: 2026-05-19-2505c918
priority: high
immediate_action: null
tags:
  - data-breach
  - identity
  - cloud
  - organized-crime
regions:
  - global
  - europe
  - us
sectors:
  - retail
  - technology
entities:
  - "actor:shinyhunters"
  - "incident:medtronic-shinyhunters-corporate-it-breach"
cves: []
sources:
  - url: "https://www.securityweek.com/7-eleven-data-breach-confirmed-after-shinyhunters-ransom-demand/"
    publisher: SecurityWeek
    role: primary
  - url: "https://securityaffairs.com/192336/data-breach/shinyhunters-hack-7-eleven-franchisee-data-and-salesforce-records-exposed.html"
    publisher: Security Affairs
    role: corroborating
  - url: "https://www.maine.gov/agviewer/content/ag/985235c7-cb95-4be2-8792-a1252b4f8318/4fe778c0-a3a9-4dbe-8e79-2c229ac5c36b.html"
    publisher: Maine AG breach notification
    role: corroborating
closed_sources: []
evidence:
  - quote: "7-Eleven confirmed a breach after ShinyHunters claimed theft of over 600,000 Salesforce records and franchisee data"
    publisher: Security Affairs
  - quote: "The intrusions resulted from phishing, abuse of third-party integrations, or misconfigurations, rather than vulnerabilities in Salesforce products"
    publisher: SecurityWeek
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
migrated_from: briefs/2026-05-19.md
---

7-Eleven, Inc. confirmed on 2026-05-18 that an unauthorised third party accessed systems storing franchisee documents on 2026-04-08, in a breach claimed by ShinyHunters on or around 2026-04-17 ([SecurityWeek, 2026-05-18](https://www.securityweek.com/7-eleven-data-breach-confirmed-after-shinyhunters-ransom-demand/); [Security Affairs, 2026-05-18](https://securityaffairs.com/192336/data-breach/shinyhunters-hack-7-eleven-franchisee-data-and-salesforce-records-exposed.html)). ShinyHunters listed over 600,000 Salesforce CRM records covering personal and corporate data from franchise applications, initially demanding a ransom with a 2026-04-21 deadline and then offering the data for sale at $250,000 on a hacker forum. 7-Eleven filed a Maine Attorney General notification dated 2026-05-01 confirming 24 months of IDX identity-theft protection for affected individuals ([Maine AG breach notification, 2026-05-01](https://www.maine.gov/agviewer/content/ag/985235c7-cb95-4be2-8792-a1252b4f8318/4fe778c0-a3a9-4dbe-8e79-2c229ac5c36b.html)). The Maine filing lists only 2 Maine residents but the ShinyHunters claim covers 600,000+ records globally. SecurityWeek attributes the broader campaign — Instructure (Canvas), Vimeo, Wynn Resorts (21,000 employees), Vercel and Medtronic among confirmed co-victims — not to Salesforce-product vulnerabilities but to phishing, third-party-integration abuse, and customer-side misconfiguration of Salesforce Connected Apps.

**Why it matters to us:** ShinyHunters is the same actor that hit Instructure last week, with the broader Salesforce-targeting campaign continuing across sectors. The campaign vector is identity-side rather than Salesforce-product-side — Connected App OAuth grant abuse, phishing of admin sessions, mis-scoped third-party SaaS integrations. EU/CH public-sector and finance tenants using Salesforce for partner / supplier / case-management data should audit Connected App OAuth grants (particularly to third-party AI SaaS integrations), enable Salesforce Event Monitoring with alerts on bulk `Report Export` events and high-volume SOQL API calls, enforce IP-range / Trusted-IP session policies, and consider Salesforce Shield field-level encryption for PII. T1078.004 (Cloud Accounts), T1530 (Data from Cloud Storage Object), T1567.002 (Exfiltration to Cloud Storage).
