---
schema: 1
kind: incident
title: "Zara customer emails exposed through a former Inditex technology provider; ShinyHunters claims Anodot token abuse and leaks the data"
headline: "Have I Been Pwned loads about 197,000 Zara customer emails after ShinyHunters leaked data it says came from Anodot tokens against BigQuery"
summary: >
  Inditex says databases hosted by a former technology provider were accessed, without customers' names,
  phone numbers, addresses, credentials or payment data. Have I Been Pwned found about 197,000 unique email
  addresses with order IDs, product SKUs and the support-ticket market. ShinyHunters claims it used Anodot
  authentication tokens against BigQuery and leaked the data; Inditex has not named the provider or an actor.
discovered_at: "2026-05-09T05:00:01Z"
event_date: 2026-05-08
run_id: 2026-05-09-migrated
priority: routine
immediate_action: null
tags:
  - data-breach
  - supply-chain
  - organized-crime
regions:
  - global
sectors:
  - retail
entities:
  - "incident:inditex-zara-breach-2026"
  - "actor:shinyhunters"
cves: []
sources:
  - url: "https://securityaffairs.com/191859/cyber-crime/zara-data-breach-197000-customers-exposed-in-third-party-security-incident.html"
    publisher: "Security Affairs"
    date: "2026-05-08"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/zara-data-breach-exposed-personal-information-of-197-000-people/"
    publisher: "BleepingComputer"
    date: "2026-05-08"
    role: corroborating
  - url: "https://haveibeenpwned.com/Breach/Zara"
    publisher: "Have I Been Pwned"
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
techniques: [T1528, T1530]
classification:
  reliability: B
  credibility: 3
migrated_from: briefs/2026-05-09.md
updates:
  - at: "2026-10-11T14:33:17Z"
    run_id: 2026-10-11T1307Z-audit
    type: correction
    summary: >
      The headline presented ShinyHunters' analytics-compromise claim as confirmed and described the records as EU customers, which no source says; the data categories came from Have I Been Pwned, not Inditex; Inditex speaks of a former technology provider, not an analytics provider; the 140 GB and one-terabyte figures disagree; and the claim that Inditex declined to engage and the AEPD inference had no source. The entry is rewritten with each statement attributed, a rating, an ATT&CK mapping for the claimed token abuse and priority routine.
    fields: [title, headline, summary, priority, tags, regions, techniques, sources, verification, classification, body]
---

Inditex says databases hosted by a former technology provider, holding information about business relationships with customers in different markets, were accessed, and that customers' names, phone numbers, addresses, credentials and payment information were not; it has notified the relevant authorities but has not named the provider or attributed the breach ([BleepingComputer, 2026-05-08](https://www.bleepingcomputer.com/news/security/zara-data-breach-exposed-personal-information-of-197-000-people/)). Have I Been Pwned found about 197,000 unique email addresses with product SKUs, order IDs and the market each support ticket originated in ([Have I Been Pwned](https://haveibeenpwned.com/Breach/Zara)). ShinyHunters claims it stole the data with Anodot authentication tokens used against BigQuery and leaked a 140 GB archive ([BleepingComputer, 2026-05-08](https://www.bleepingcomputer.com/news/security/zara-data-breach-exposed-personal-information-of-197-000-people/)); Have I Been Pwned describes the group's publication as a terabyte allegedly including 95 million support-ticket records ([Have I Been Pwned](https://haveibeenpwned.com/Breach/Zara)).

**Defender takeaway:** the claimed path is a third-party analytics platform's token reaching a cloud data warehouse, so the control is the scope and lifetime of tokens granted to analytics providers, including former ones, whose access should be revoked when the relationship ends ([BleepingComputer, 2026-05-08](https://www.bleepingcomputer.com/news/security/zara-data-breach-exposed-personal-information-of-197-000-people/)).

## Correction — 2026-10-11T14:33:17Z

Inditex confirms only that a former technology provider's databases were accessed ([BleepingComputer, 2026-05-08](https://www.bleepingcomputer.com/news/security/zara-data-breach-exposed-personal-information-of-197-000-people/)); the analytics-platform route is ShinyHunters' claim about Anodot tokens ([BleepingComputer, 2026-05-08](https://www.bleepingcomputer.com/news/security/zara-data-breach-exposed-personal-information-of-197-000-people/)). The email, order and support-ticket fields come from Have I Been Pwned's analysis, and the records concern customers in different markets, and no source limits them to the EU ([Have I Been Pwned](https://haveibeenpwned.com/Breach/Zara)) ([BleepingComputer, 2026-05-08](https://www.bleepingcomputer.com/news/security/zara-data-breach-exposed-personal-information-of-197-000-people/)). The size of the leak differs between sources, 140 GB ([BleepingComputer, 2026-05-08](https://www.bleepingcomputer.com/news/security/zara-data-breach-exposed-personal-information-of-197-000-people/)) against about a terabyte ([Have I Been Pwned](https://haveibeenpwned.com/Breach/Zara)).
