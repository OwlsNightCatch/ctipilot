---
schema: 1
kind: incident
title: California AG sues former 23andMe (Chrome Holding Co.) over the 2023 genetic-data breach — bulk-enumeration coding error plus absent credential-stuffing defences
headline: California AG sues former 23andMe (Chrome Holding Co.) over the 2023 genetic-data breach — bulk-enumeration coding error plus absent credential-stuffing
summary: "California's Attorney General sued the former 23andMe (now Chrome Holding Co.) over the 2023 genetic-data breach, alleging a DNA-Relatives bulk-enumeration coding error and an absence of credential-stuffing defences amplified ~14,000 stuffed accounts into ~6.9M exposed records (California OAG, 2026-05-28). A second jurisdiction's enforcement after the UK ICO's 2025 fine; the failure pattern transfers directly to special-category-data registries."
discovered_at: "2026-05-31T05:00:02Z"
event_date: 2026-05-29
run_id: 2026-05-31-d742bed9
priority: high
immediate_action: null
tags:
  - data-breach
  - identity
  - law-enforcement
regions:
  - us
sectors:
  - healthcare
entities: []
cves: []
sources:
  - url: "https://oag.ca.gov/news/press-releases/attorney-general-bonta-sues-chrome-holding-co-formerly-known-23andme-over-2023"
    publisher: California Office of the Attorney General
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/california-ag-sues-23andme-over-2023-breach-exposing-health-data/"
    publisher: BleepingComputer
    role: corroborating
  - url: "https://www.theregister.com/legal/2026/05/29/rob-bonta-sues-23andmes-new-owners-over-2023-breach/5248565"
    publisher: The Register
    role: corroborating
closed_sources: []
evidence:
  - quote: "The breach exposed information for approximately 6.9 million customers, including 855,541 Californians"
    publisher: BleepingComputer
  - quote: "Bonta's office claims 23andMe negotiated and paid ransom to the threat actor in exchange for removal of breach information posted online and details about multiple 23andMe security vulnerabilities"
    publisher: The Register
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
migrated_from: briefs/2026-05-31.md
---

California Attorney General Rob Bonta announced suit against Chrome Holding Co. (formerly 23andMe) on 2026-05-28, filed in San Francisco Superior Court over the October 2023 breach affecting ~6.9 million users worldwide, including 855,541 Californians ([California OAG, 2026-05-28](https://oag.ca.gov/news/press-releases/attorney-general-bonta-sues-chrome-holding-co-formerly-known-23andme-over-2023); [BleepingComputer, 2026-05-29](https://www.bleepingcomputer.com/news/security/california-ag-sues-23andme-over-2023-breach-exposing-health-data/)). The complaint describes a two-stage failure: an actor compromised ~14,000 accounts via credential stuffing (reusing credentials from earlier breaches), then abused the DNA Relatives kinship-matching feature — which carried a coding error permitting bulk enumeration of matched records without per-record access checks — to reach data belonging to the remaining ~6.9 million. Alleged data classes include raw DNA, ancestry and genetic health-predisposition data and family connections. The AG additionally alleges the company ignored a July 2023 suspicious-login spike, made misleading public statements, and negotiated and paid a ransom for deletion of the leaked data — an unusual allegation to surface in a state-enforcement complaint ([The Register, 2026-05-29](https://www.theregister.com/legal/2026/05/29/rob-bonta-sues-23andmes-new-owners-over-2023-breach/5248565)).

**Defender takeaway:** This is the second jurisdiction to act after the UK ICO's 2025 fine over the same breach, and the failure pattern transfers directly to any operator of special-category-data registries (health, genetic, civil-registry): the breach scaled not through a software RCE but through (a) no breach-credential blocking / velocity checks on login, and (b) a social-graph / kinship feature that enumerated records without per-request authorization. Concrete controls: enforce MFA on all accounts holding special-category data; block known-breached credentials (e.g. HIBP range API) and rate-limit repeated login failures; impose bulk-export and per-request authorization checks on relationship/kinship/lookup endpoints so a single account cannot enumerate the population.
