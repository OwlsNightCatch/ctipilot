---
schema: 1
kind: incident
horizon: operational
title: "France's Tchap government messenger breached via account takeover — 73,467 civil servants' metadata scraped, CNIL notified"
headline: "France's Tchap government messenger breached via account takeover — 73,467 civil servants' metadata scraped, CNIL notified"
summary: "France's sovereign government messenger Tchap breached — 73,467 civil servants exposed, CNIL notified. A single account takeover on the education shard was pivoted via the Matrix user-directory to scrape user metadata across the federation; DINUM confirms name, email and employing entity exposed (DINUM, 2026-06-08)."
discovered_at: "2026-06-10T05:00:00Z"
event_date: 2026-06-09
run_id: 2026-06-10-c84347b2
priority: high
immediate_action: null
tags:
  - data-breach
  - identity
regions:
  - europe
sectors:
  - public-sector
entities: []
cves: []
sources:
  - url: "https://www.numerique.gouv.fr/sinformer/espace-presse/incident-tchap/"
    publisher: "DINUM, 2026-06-08"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/french-govt-messaging-service-breached-in-account-hijacking-attack/"
    publisher: "BleepingComputer, 2026-06-09"
    role: corroborating
  - url: "https://www.helpnetsecurity.com/2026/06/09/tchap-french-government-secure-messaging-platform-breach/"
    publisher: "Help Net Security, 2026-06-09"
    role: corroborating
  - url: "https://www.theregister.com/security/2026/06/09/france-probes-compromise-of-gov-messaging-platform-after-account-hijack/5252717"
    publisher: "The Register, 2026-06-09"
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
migrated_from: briefs/2026-06-10.md
---

On 7 June 2026 ANSSI detected a compromise of Tchap, the French state's sovereign Matrix-based encrypted messenger used by some 825,000 civil servants across all ministries; DINUM published its disclosure on 8 June ([DINUM, 2026-06-08](https://www.numerique.gouv.fr/sinformer/espace-presse/incident-tchap/)). The attacker obtained a single account on the education shard (`matrix.agent.education.tchap.gouv.fr`) through account impersonation; the attacker further claims to have used a Tchap directory-search function to enumerate accounts across the service, a mechanism DINUM has not confirmed and which The Register reports as part of a set of unverified attacker claims ([Help Net Security, 2026-06-09](https://www.helpnetsecurity.com/2026/06/09/tchap-french-government-secure-messaging-platform-breach/); [The Register, 2026-06-09](https://www.theregister.com/security/2026/06/09/france-probes-compromise-of-gov-messaging-platform-after-account-hijack/5252717)). DINUM confirms 73,467 agents (under 9% of registered users) had name, first name, email address, employing entity and avatar potentially exposed; private rooms protected by Matrix end-to-end encryption were not accessible from a compromised user account, only public-room content ([DINUM, 2026-06-08](https://www.numerique.gouv.fr/sinformer/espace-presse/incident-tchap/)). The unverified actor additionally claims bulk scraping of ~643,000 messages and ~13.5 GB of media, alleging that any media object is retrievable without an auth token once its media ID is known — an unconfirmed content-repository access-control claim that, if true, would widen the exposure considerably ([The Register, 2026-06-09](https://www.theregister.com/security/2026/06/09/france-probes-compromise-of-gov-messaging-platform-after-account-hijack/5252717)). DINUM has notified CNIL and blocked the account; the investigation is ongoing.

**Defender takeaway:** account takeover followed by directory enumeration and bulk metadata scraping is a generic risk for any Matrix homeserver, since user-directory search is reachable by authenticated users across a federation by default. Organisations running Matrix/Element (BwMessenger and several cantonal/government deployments share this architecture) should restrict or disable cross-federation directory search, confirm sensitive comms use private E2EE rooms rather than public rooms, and watch for follow-on phishing that uses the leaked name + email + organisational-affiliation tuples.
