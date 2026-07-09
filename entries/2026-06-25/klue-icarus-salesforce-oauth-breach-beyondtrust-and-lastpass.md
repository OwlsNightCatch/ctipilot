---
schema: 1
kind: incident
horizon: operational
title: Klue/Icarus Salesforce OAuth breach — BeyondTrust and LastPass added to the named-victim list
headline: Klue/Icarus Salesforce OAuth breach — BeyondTrust and LastPass added to the named-victim list
summary: "UPDATE (originally covered 2026-06-19): BeyondTrust and LastPass have both disclosed that business-contact and sales-related data was exfiltrated from their Salesforce environments via the compromised Klue integration, pushing the confirmed named-victim count past 14 (SecurityWeek, 2026-06-24 · Help Net Security …"
discovered_at: "2026-06-25T04:59:09Z"
event_date: 2026-06-24
run_id: 2026-06-25-da7fbd23
priority: notable
immediate_action: null
tags:
  - data-breach
  - supply-chain
  - identity
  - cloud
regions:
  - global
sectors:
  - technology
  - finance
entities:
  - "campaign:icarus-klue-salesforce-oauth"
cves: []
sources:
  - url: "https://www.securityweek.com/beyondtrust-lastpass-impacted-by-klue-salesforce-incident/"
    publisher: SecurityWeek
    role: primary
  - url: "https://www.helpnetsecurity.com/2026/06/24/lastpass-klue-data-breach-salesforce-environment/"
    publisher: Help Net Security
    role: corroborating
  - url: "https://thehackernews.com/2026/06/salesforce-disables-klue-app.html"
    publisher: The Hacker News
    role: corroborating
closed_sources: []
evidence:
  - quote: BeyondTrust also said business contact and sales-related information was stolen from its Salesforce instance
    publisher: SecurityWeek
  - quote: "an unauthorized actor was able to obtain OAuth tokens Klue held for many of its customers, including LastPass"
    publisher: Help Net Security citing LastPass
verification: multi-source
sourcing_note: null
confidence: high
update_of: 2026-06-21/klue-oauth-token-breach-victim-list-grows-crm-api-abuse-chai
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-25.md
---

**UPDATE (originally covered 2026-06-19):** BeyondTrust and LastPass have both disclosed that business-contact and sales-related data was exfiltrated from their Salesforce environments via the compromised Klue integration, pushing the confirmed named-victim count past 14 ([SecurityWeek, 2026-06-24](https://www.securityweek.com/beyondtrust-lastpass-impacted-by-klue-salesforce-incident/) · [Help Net Security, 2026-06-24](https://www.helpnetsecurity.com/2026/06/24/lastpass-klue-data-breach-salesforce-environment/)).

The BeyondTrust exposure is the notable delta: a privileged-access-management vendor losing its CRM contact and support-case data to a SaaS supply-chain compromise illustrates that security-vendor customer lists are a deliberate targeting priority for the Icarus extortion crew. LastPass states customer vaults were not affected. Salesforce had already disabled the Klue Battlecards connection on 17 June ([The Hacker News, 2026-06-19](https://thehackernews.com/2026/06/salesforce-disables-klue-app.html)). Any organisation receiving a Salesforce "Connected App disabled" notice for Klue should treat it as an incident trigger and audit Event Log File `ApiTotalUsage` / `ApiAnomalyEventStore` records for bulk REST API reads in the June 11–17 window (`T1199`, `T1528`, `T1213.003`).
