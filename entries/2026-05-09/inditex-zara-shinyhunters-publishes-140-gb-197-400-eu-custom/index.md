---
schema: 1
kind: incident
title: "Inditex (Zara) — ShinyHunters publishes 140 GB; 197,400 EU customer records confirmed via third-party analytics compromise"
headline: "Inditex (Zara) — ShinyHunters publishes 140 GB; 197,400 EU customer records confirmed via third-party analytics compromise"
summary: "Have I Been Pwned confirmed on 2026-05-08 that 197,400 unique email addresses from Inditex (Zara's parent, headquartered in A Coruña, Spain) were exposed following a breach of a former third-party analytics provider."
discovered_at: "2026-05-09T05:00:01Z"
event_date: 2026-05-08
run_id: 2026-05-09-migrated
priority: notable
immediate_action: null
tags:
  - data-breach
  - organized-crime
regions:
  - europe
sectors:
  - retail
entities:
  - "incident:inditex-zara-breach-2026"
  - "actor:shinyhunters"
cves: []
sources:
  - url: "https://securityaffairs.com/191859/cyber-crime/zara-data-breach-197000-customers-exposed-in-third-party-security-incident.html"
    publisher: "SecurityAffairs, 2026-05-08"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/zara-data-breach-exposed-personal-information-of-197-000-people/"
    publisher: "BleepingComputer, 2026-05-08"
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
migrated_from: briefs/2026-05-09.md
---

Have I Been Pwned confirmed on 2026-05-08 that 197,400 unique email addresses from Inditex (Zara's parent, headquartered in A Coruña, Spain) were exposed following a breach of a former third-party analytics provider. Inditex confirmed attackers accessed customer relationship data — email addresses, geographic locations, purchase history (order IDs and product SKUs), and support ticket content — across international markets ([SecurityAffairs, 2026-05-08](https://securityaffairs.com/191859/cyber-crime/zara-data-breach-197000-customers-exposed-in-third-party-security-incident.html) · [BleepingComputer, 2026-05-08](https://www.bleepingcomputer.com/news/security/zara-data-breach-exposed-personal-information-of-197-000-people/)). Names, passwords, payment card data, addresses, and phone numbers were stated to be out of scope. ShinyHunters claimed responsibility, alleging access via compromised authentication tokens for the Anodot analytics platform against BigQuery instances; this claim has not been independently verified. Data publication (approximately 140 GB) followed after Inditex declined to engage. Inditex stated it had "started notifying the relevant authorities" but did not specify which supervisory authority or whether the GDPR Article 33 72-hour notification clock was met; as a Spanish company the lead supervisory authority is the AEPD.

**Defender takeaway:** Third-party analytics and BI platforms with OAuth or service-account access to production data warehouses (BigQuery, Snowflake, Redshift) represent a persistent supply-chain data-exfiltration vector. Audit delegated access grants for analytics tooling; enforce token scoping and expiry; review whether analytics platform service accounts have read-all access to customer-facing databases.
