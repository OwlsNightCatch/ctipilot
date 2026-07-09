---
schema: 1
kind: incident
horizon: operational
title: "Klue OAuth-token breach — victim list grows, CRM-API abuse chain detailed"
headline: "Klue OAuth-token breach — victim list grows, CRM-API abuse chain detailed"
summary: "UPDATE (originally covered 2026-06-19): The Klue compromise first covered on 2026-06-19 (Icarus obtaining a legacy Klue credential) now has a named, growing victim list and a documented post-access technique."
discovered_at: "2026-06-21T04:55:03Z"
event_date: 2026-06-19
run_id: 2026-06-21-2b75e32c
priority: notable
immediate_action: null
tags:
  - data-breach
  - identity
  - cloud
  - organized-crime
regions:
  - global
  - us
sectors:
  - technology
entities: []
cves: []
sources:
  - url: "https://klue.com/blog/an-update-on-recent-klue-security-incident"
    publisher: Klue
    role: primary
  - url: "https://www.huntress.com/blog/klue-breach-investigation"
    publisher: Huntress
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/klue-oauth-breach-victim-list-grows-as-icarus-hackers-claim-attack/"
    publisher: BleepingComputer
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
migrated_from: briefs/2026-06-21.md
---

**UPDATE (originally covered 2026-06-19):** The Klue compromise first covered on 2026-06-19 (Icarus obtaining a legacy Klue credential) now has a named, growing victim list and a documented post-access technique. Klue confirms the attacker harvested customer-provisioned OAuth tokens for connected platforms — principally Salesforce, plus Gong, HubSpot, SharePoint and others — and used them to query customer CRM instances directly ([Klue, 2026-06-19](https://klue.com/blog/an-update-on-recent-klue-security-incident)).

Huntress forensics show the stolen tokens were used to hit Salesforce REST endpoints at `/services/data/v59.0/query/<STRING>` with a `python-urllib` User-Agent — anomalous in a legitimate Klue-integration context ([Huntress, 2026-06-18](https://www.huntress.com/blog/klue-breach-investigation)). Confirmed affected organisations now include Huntress, Recorded Future, Tanium, Jamf and Sprout Social; Icarus has publicly claimed the attack and is demanding contact via Session messenger ([BleepingComputer, 2026-06-19](https://www.bleepingcomputer.com/news/security/klue-oauth-breach-victim-list-grows-as-icarus-hackers-claim-attack/)). The chain — compromise an integration platform's legacy credential, harvest downstream OAuth tokens, query customer CRM APIs from the platform's legitimate IP range — bypasses perimeter controls. Detection surface: Salesforce Event Monitoring for a `python-urllib` API caller, unusual `/services/data/v*/query/` volumes from non-user principals, and out-of-hours API sessions from unexpected source orgs. Hardening: audit and revoke OAuth grants to third-party SaaS vendors (especially inactive integrations), enforce IP restrictions on Salesforce connected-app policies, and scope integration-platform credentials so one compromised account cannot chain to every downstream tenant.
