---
schema: 1
kind: incident
horizon: operational
title: ServiceNow unauthenticated REST endpoint queried customer instance tables before a silent 5 June patch
headline: ServiceNow unauthenticated REST endpoint queried customer instance tables before a silent 5 June patch
summary: "ServiceNow shipped a Scripted REST endpoint (/api/now/related_list_edit/create) with requires_authentication=false, and attackers queried customer instance tables unauthenticated between 2–4 June before a silent server-side patch on 5 June (BleepingComputer, 2026-06-09). NCSC-CH GovCERT flags it \"Actively Exploited\"; ServiceNow's own read is that the activity was \"likely tied to security researchers\" — either way, instance tables holding tickets, tokens and PII were reachable without credentials. No CVE."
discovered_at: "2026-06-11T05:00:00Z"
event_date: 2026-06-10
run_id: 2026-06-11-7edf1d8a
priority: high
immediate_action: null
tags:
  - cloud
  - data-breach
  - identity
  - auth-bypass
  - actively-exploited
regions:
  - global
sectors:
  - public-sector
  - finance
  - technology
entities: []
cves: []
sources:
  - url: "https://security-hub.ncsc.admin.ch/#/posts/12621"
    publisher: NCSC-CH GovCERT
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/servicenow-discloses-security-incident-exposing-customer-data/"
    publisher: BleepingComputer
    role: corroborating
  - url: "https://thehackernews.com/2026/06/servicenow-flaw-exploited-to-gain.html"
    publisher: The Hacker News
    role: corroborating
  - url: "https://techcrunch.com/2026/06/10/servicenow-tells-customers-a-bug-left-some-of-their-data-exposed-to-the-internet/"
    publisher: TechCrunch
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
migrated_from: briefs/2026-06-11.md
---

ServiceNow disclosed on 9 June 2026 that a Scripted REST Resource at `/api/now/related_list_edit/create` was shipped with `requires_authentication=false`, so the endpoint accepted unauthenticated requests and could be used to query arbitrary customer instance tables ([BleepingComputer, 2026-06-09](https://www.bleepingcomputer.com/news/security/servicenow-discloses-security-incident-exposing-customer-data/)). Anomalous activity was observed from 2–4 June from a single source IP, and ServiceNow applied a server-side fix to hosted instances on 5 June, reconfiguring the endpoint to require authentication ([The Hacker News, 2026-06-10](https://thehackernews.com/2026/06/servicenow-flaw-exploited-to-gain.html)). Instances on the "Australia" platform release, or older releases with specific configuration changes, were affected; no CVE has been assigned. ServiceNow's own assessment is that the observed activity was "likely tied to security researchers or customer-led research associated with bug bounty submissions rather than malicious threat actors," while NCSC-CH GovCERT recorded the issue as "Actively Exploited" — the company confirms it saw evidence of successful table queries against a subset of customers regardless of attribution ([TechCrunch, 2026-06-10](https://techcrunch.com/2026/06/10/servicenow-tells-customers-a-bug-left-some-of-their-data-exposed-to-the-internet/)). Technique class: `T1190` Exploit Public-Facing Application → `T1213` Data from Information Repositories, with downstream `T1078` Valid Accounts if tokens stored in tickets were harvested. The advisory (KB3067321) was initially gated behind the customer support portal, so organisations that do not actively monitor it may not know a case was opened on their tenant.

**Why it matters to us:** ServiceNow is a reference ITSM/CMDB/HR platform across the Swiss Confederation, cantonal administrations and EU institutions, and its instances routinely hold support-ticket credentials, embedded API tokens, asset inventories and security-incident records. Audit all Scripted REST Resources for `requires_authentication=false` (filter `sys_ws_operation` on `acl.requires_authentication=false`), review `access_log_transaction` for requests to `/api/now/related_list_edit` in the 2–5 June window, and rotate any secrets exposed in support workflows.
