---
schema: 1
kind: threat
horizon: operational
title: "City-Forum: a 17-month campaign reads Salesforce and ServiceNow portal data through the guest identity — and the Lightning Web Runtime data layer it uses had no public tooling or write-up"
headline: "No vulnerability and no credential: one server has been reading over-permissioned Salesforce and ServiceNow guest sessions since March 2025"
summary: >
  Reco published research on 2026-08-12, taken up by The Register the next day, on a still-running campaign it names
  City-Forum, in which a single host has been enumerating and reading records from Salesforce Experience Cloud sites
  and ServiceNow Service Portals worldwide as the anonymous guest user — no exploit, no stolen credential. Alongside
  the well-documented Aura enumeration path, the operator reaches Salesforce's newer Lightning Web Runtime sites
  through the UI-API data layer, sweeping GraphQL API versions v56.0 through v66.0, a surface Reco says it has seen no
  public tool or write-up for and one that Aura-only scanners cannot see at all. On ServiceNow it hammers the native
  Service Portal search endpoint, where a guest query returns an empty HTTP 201 that the transaction log cannot
  distinguish from a genuine no-results answer. Named target sectors are telecoms, banks and financial-services firms,
  enterprise-software vendors and public-sector portals.
discovered_at: "2026-08-14T05:05:00Z"
event_date: "2026-08-12"
run_id: 2026-08-14T0417Z-intel
priority: high
immediate_action: null
tags:
  - cloud
  - identity
  - data-breach
  - default-config
  - info-disclosure
regions:
  - global
  - europe
sectors:
  - public-sector
  - finance
  - telco
  - technology
entities:
  - actor:city-forum
techniques:
  - T1190
  - T1213
  - T1526
  - T1530
affected_products:
  - "Salesforce Experience Cloud"
  - "Salesforce Lightning Web Runtime"
  - "ServiceNow Service Portal"
cves: []
sources:
  - url: "https://www.reco.ai/blog/city-forum-campaign-salesforce-servicenow"
    publisher: "Reco"
    date: "2026-08-12"
    role: primary
  - url: "https://www.theregister.com/cyber-crime/2026/08/13/mystery-attacker-spent-a-year-raiding-salesforce-and-servicenow-portals/5287368"
    publisher: "The Register"
    date: "2026-08-13"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Except for Aura, the attacker reaches Salesforce Lightning Web Runtime (LWR) sites through the UI-API, a data layer we have not seen any public tool or write-up about, and it hammers a native ServiceNow Service Portal search endpoint that has almost no online documentation or well-known open source tools."
    publisher: "Reco"
  - quote: "\"If the guest can read a record, so can anyone on the internet,\" Bachrach warned."
    publisher: "The Register"
verification: multi-source
sourcing_note: "Reco is the single assessor; The Register reports Reco's findings rather than observing the campaign independently, so corroboration confirms the publication and the researcher's framing, not the telemetry."
confidence: high
update_of: null
references: []
deep_dive: true
deep_dive_category: cloud-saas
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "In every Salesforce Experience Cloud site built on Lightning Web Runtime, uncheck **Allow guest users to access public APIs** (Experience Builder → Workspaces → Administration → Preferences) — it is the single toggle that closes both the GraphQL and the UI-API REST surface, and it is *not* the same control as the guest profile's `API Enabled` permission or the site's page-visibility setting, neither of which closes it."
  - "Pull Salesforce Event Monitoring `EventLogFile` rows for the `AuraRequest` and `Sites` event types over your retention window and look for guest requests whose URI contains `/webruntime/api/services/data/v` — a run of them stepping through consecutive API versions is the operator's version sweep, and Reco states this pattern is the only way Lightning Web Runtime activity becomes visible at all."
  - "In ServiceNow, walk each guest-facing portal to its search sources through `sp_portal` → `m2m_sp_portal_search_source` → `sp_search_source`, and detach every source the public portal does not have to serve; for scripted sources confirm they gate on `gs.isLoggedIn()` and query with `GlideRecordSecure` rather than plain `GlideRecord`."
migrated_from: null
---

Reco is tracking an active campaign it calls **City-Forum** in which one server has been reading records out of Salesforce Experience Cloud sites and ServiceNow Service Portals belonging to organisations worldwide, using nothing but the anonymous guest identity every one of those platforms creates and cannot delete ([Reco, 2026-08-12](https://www.reco.ai/blog/city-forum-campaign-salesforce-servicenow)). The infrastructure has been standing since at least March 2025 on passive-DNS evidence, the volume is climbing, and Reco has so far observed only guest activity — never an authenticated session — though it says it cannot rule the latter out. Reco declines to name victims, and describes the visible target set as telecoms, banks and financial-services firms, enterprise-software vendors including security and data-privacy companies, and public-sector portals. There is no vulnerability in the chain: ["If the guest can read a record, so can anyone on the internet," Reco's Nitay Bachrach told The Register, "That is not a platform vulnerability."](https://www.theregister.com/cyber-crime/2026/08/13/mystery-attacker-spent-a-year-raiding-salesforce-and-servicenow-portals/5287368) The tooling also probes whether Salesforce sites permit self-registration, which The Register notes would offer a route from anonymous guest access to an authenticated external account able to see considerably more, and Reco reports seeing those checks across most of the Salesforce targets it examined ([The Register, 2026-08-13](https://www.theregister.com/cyber-crime/2026/08/13/mystery-attacker-spent-a-year-raiding-salesforce-and-servicenow-portals/5287368)). Volume at the busiest single Salesforce target ran to more than 560,000 events across the campaign window, almost all of it guest enumeration ([The Register, 2026-08-13](https://www.theregister.com/cyber-crime/2026/08/13/mystery-attacker-spent-a-year-raiding-salesforce-and-servicenow-portals/5287368)). ServiceNow told The Register it is aware of the post, noted that it contains no allegation of a compromise of the ServiceNow environment, and said it is investigating; Salesforce had not responded by publication.

**Why this is not the ShinyHunters playbook.** Guest-user abuse of Salesforce's older Aura framework is well documented, and Reco names ShinyHunters among the actors that have run it; that path is still where most of this operator's Salesforce volume goes, opening with the host-configuration controller call that enumerates which objects the guest context can reach, then paging each object's records through the selectable-list data provider ([Reco](https://www.reco.ai/blog/city-forum-campaign-salesforce-servicenow)). What separates City-Forum is the second surface. Lightning Web Runtime is Salesforce's newer Experience Cloud framework and its Aura endpoint is disabled outright, so an Aura-only scanner pointed at a pure Lightning Web Runtime site finds nothing — which, Reco notes, is precisely why the framework has been an offensive blind spot. The operator instead reaches its data layer under `/webruntime/api/services/data/{version}/`, which backs a GraphQL endpoint and a set of REST endpoints, and walks it across consecutive API versions v56.0 through v66.0. Guest access to that entire surface hangs off one Experience Builder preference, and Reco is explicit that two adjacent controls give administrators a false sense of safety: removing the guest profile's `API Enabled` permission does not close the UI-API, and tightening the "guest users can see and interact with the site without logging in" page-visibility setting does not close it either.

**The ServiceNow half is worse for retrospective scoping.** The operator posts to the native Service Portal search endpoint, `/api/now/sp/search`, an interface Reco reverse-engineered from the portal's own typeahead widget and describes as having almost no public documentation. That endpoint is public by design, so the exposure lives entirely in which search sources a guest-facing portal exposes and whether those sources enforce access control — a scripted source running a plain, unguarded record query returns rows to anyone, and the stock Knowledge Base source carries no login gate at all, relying wholly on read criteria. Reco flags the specific misconfiguration to hunt for: a user-criteria record that is active, non-advanced, and has every scoping field empty resolves true for the guest identity, which is the built-in "Any User" pattern that ships on every instance and gets attached without administrators appreciating what it grants.

**Detection, and what the telemetry cannot tell you.** In Salesforce, the request-level logs require Event Monitoring — Shield or the standalone add-on — and the tells sit in three columns: the user-agent field carrying a default Go HTTP client string, which has no legitimate explanation on a browser-driven portal; high counts of the two Aura controller actions above in the action-message field; and, on the site rows, any guest URI containing the web-runtime data path. In ServiceNow, the transaction log shows the search endpoint being called by `guest` — already anomalous, because a signed-in user's portal search is attributed to that user's own account — at a cadence no human produces, with the output-length column separating the empty-result baseline from the rows that actually returned content. Two limits are worth carrying into a scoping exercise, both stated by Reco: the ServiceNow transaction log records the request but not the POST body, so a portal-search sweep can be confirmed and sized but the search terms cannot be reconstructed; and Salesforce's audit logging cannot reliably show which records or fields a call returned, which means determining real exposure requires replaying the observed request patterns against your own instance rather than reading it off a log.

**Defender takeaway:** this is a configuration-review obligation, not a patch. Every Experience Cloud site and every ServiceNow portal your organisation publishes carries a persistent guest identity whose sharing rules, object and field permissions, and search-source mappings define what an unauthenticated visitor can read — and the campaign has been quietly exercising exactly those grants for over a year. European public-sector estates that stood up citizen-facing portals on these platforms are in the named target set, and the Swiss authority's advisory of 2026-08-04 on anonymously-readable Dataverse tables behind Power Pages portals is the same failure mode on a third platform: a web role granted more than it needed.

**Triage:** the discriminator is the identity, not the payload. Portal search and record reads are the normal business of these platforms all day, but they are performed by named, signed-in users from browsers; a high-rate sequence of the same operations attributed to the guest or anonymous identity, carrying a programmatic HTTP-client user-agent rather than a browser one, is the signal — and on Lightning Web Runtime the ascending API-version sweep across the web-runtime data path is behaviour no legitimate client produces, because a real front end pins one version.
