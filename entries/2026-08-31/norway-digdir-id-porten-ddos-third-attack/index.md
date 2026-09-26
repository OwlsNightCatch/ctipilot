---
schema: 1
kind: incident
title: "Norway's shared national identity gateway ID-porten knocked out for 64 hours by the third escalating DDoS against Digdir since June"
headline: "A 64-hour DDoS against Norway's ID-porten shows what happens when one gateway authenticates health, tax and business-registry logins at once"
summary: >
  A distributed denial-of-service attack against Digdir's IT partner Vivicta disrupted ten Norwegian
  government digital services from 24 to 26 August 2026, including ID-porten, the shared identity
  gateway used by more than 4.5 million people to reach health, tax and business-registry logins;
  Digdir says it was two to three times larger than the prior attack and no sensitive data was
  accessed. It is the third such attack against Digdir's infrastructure since June 2026.
discovered_at: "2026-08-31T04:50:00Z"
updated_at: null
event_date: "2026-08-24"
run_id: 2026-08-31T0411Z-intel
priority: notable
immediate_action: null
tags: [ddos, identity]
regions: [nordics]
sectors: [public-sector]
entities: ["incident:norway-digdir-idporten-ddos-2026-08"]
techniques: [T1498]
affected_products: []
cves: []
sources:
  - url: "https://status.digdir.no/incidents/d7tgwqgzd742"
    publisher: "Digitaliseringsdirektoratet (Digdir) status page"
    date: "2026-08-28"
    role: primary
  - url: "https://therecord.media/norway-cyberattack-ddos-government"
    publisher: "The Record (Recorded Future News)"
    date: "2026-08-25"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The attack started during the night of Monday at 03:38 and stopped around 19:30 Wednesday evening. Except for short periods, ID-porten and the shared solutions have been available the whole time."
    original: "Angrepet startet natt til mandag kl. 03.38 og stoppet ved 19.30-tiden onsdag kveld. Med unntak av korte perioder har ID-porten og fellesløsningene vært tilgjengelige hele tiden."
    publisher: "Digitaliseringsdirektoratet (Digdir) status page"
    source_url: "https://status.digdir.no/incidents/d7tgwqgzd742"
  - quote: "What is special about this latest attack, which has now been ongoing for a day, is that it is two to three times larger than what we experienced last time"
    publisher: "The Record (Recorded Future News)"
    source_url: "https://therecord.media/norway-cyberattack-ddos-government"
verification: multi-source
sourcing_note: null
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

A distributed denial-of-service attack against Vivicta, the IT partner operating infrastructure for Norway's Digitalisation Agency (Digdir), disrupted ten government digital services from the early hours of Monday 24 August through roughly 19:30 on Wednesday 26 August 2026 — about 64 hours, with intensity varying and short recovery windows in between ([Digdir status page, 2026-08-28](https://status.digdir.no/incidents/d7tgwqgzd742)). The disrupted services include ID-porten, the shared identity gateway more than 4.5 million people use to log into government services via BankID and MinID, plus eFormidling, eSignering, Maskinporten and several other cross-agency data-exchange and access-management systems. Because ID-porten authenticates far beyond Digdir's own services, the disruption also affected parts of Norway's health infrastructure — several health services rely on ID-porten for authentication, and authorities warned of possible problems accessing online pharmacies and the electronic prescription system ([The Record, 2026-08-25](https://therecord.media/norway-cyberattack-ddos-government)).

Digdir press officer Are Kvistad told Norwegian broadcaster NRK the attack was two to three times larger than the previous one, and it is the third DDoS incident to hit Digdir's infrastructure since June 2026 ([The Record, 2026-08-25](https://therecord.media/norway-cyberattack-ddos-government)). Digdir states no sensitive data stored in the affected systems was accessed, and as of the incident's close, normal operation was expected to resume within days; some disruption from foreign traffic persisted afterward. No attribution has been made public, and it remains unclear whether the three 2026 incidents are connected or represent a broader campaign.

**Defender takeaway:** the operationally transferable lesson is architectural, not attack-specific — a single shared identity gateway authenticating unrelated critical services (health, tax, business registries) turns a volumetric attack against one component into a cross-sector outage, and the failure mode surfaces in services that were never themselves targeted. This lands directly on any public-sector operator consolidating authentication behind one gateway, Switzerland's own eID consolidation included: stress-test DDoS resilience and downstream-dependency failure modes for that gateway specifically, including which unrelated services silently inherit its availability, before an incident forces the exercise.
