---
schema: 1
kind: incident
title: "Moldova's government digital services: attackers used flaws in services reachable without authentication to query about one million national identification numbers and extract data on about 750,000 of them between 19 and 23 October, and the Prime Minister says AI allegedly helped find the flaws"
headline: "Moldova: unauthenticated e-government services queried for about one million ID numbers; data on 750,000 extracted"
summary: >
  Moldova's Electronic Governance Agency says that between 2026-10-19 and 2026-10-23 attackers exploited flaws in state digital services reachable without authentication
  to query about one million national identification numbers and, on preliminary estimates, extract data sets for about 750,000 of them, then used what they obtained to extract
  more from interconnected systems. The Prime Minister says foreign state involvement is being investigated and that AI allegedly helped find the flaws; Moldova has not attributed
  the attack, and the agency took 82 services under review and disconnected exposed services and more than 30 systems.
discovered_at: "2026-10-29T04:43:00Z"
updated_at: null
event_date: "2026-10-27"
run_id: 2026-10-29T0255Z-intel
priority: notable
immediate_action: null
tags: [data-breach, vulnerabilities]
regions: [europe]
sectors: [public-sector]
entities: ["incident:moldova-egovernment-data-extraction-2026-10"]
techniques: [T1190, T1119]
affected_products: []
cves: []
sources:
  - url: "https://egov.md/ro/node/41145"
    publisher: "Moldova Electronic Governance Agency"
    date: "2026-10-27"
    role: primary
  - url: "https://www.moldpres.md/eng/society/prime-minister-on-cyberattack-targeting-public-digital-services-authorities-are-investigating-the-possible-involvement-of-foreign-state-actors-as-well"
    publisher: "MOLDPRES"
    date: "2026-10-28"
    role: primary
  - url: "https://www.moldpres.md/eng/society/cyberattack-on-digital-public-services-authorities-block-about-11-million-access-requests"
    publisher: "MOLDPRES"
    date: "2026-10-24"
    role: corroborating
  - url: "https://therecord.media/moldova-investigates-possible-foreign-involvement-cyberattacks"
    publisher: "The Record"
    date: "2026-10-28"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The attackers exploited vulnerabilities in services accessible without authentication, then used the data obtained for further extractions. (translated from Romanian)"
    original: "Atacatorii au exploatat vulnerabilități ale unor servicii accesibile fără autentificare, apoi au folosit datele obținute pentru extrageri suplimentare."
    publisher: "Moldova Electronic Governance Agency"
    source_url: "https://egov.md/ro/node/41145"
  - quote: "data sets for about 750,000 national identification numbers were extracted (translated from Romanian)"
    original: "au fost extrase seturi de date aferente la circa 750.000 de IDNP-uri"
    publisher: "Moldova Electronic Governance Agency"
    source_url: "https://egov.md/ro/node/41145"
  - quote: "the use of artificial intelligence allegedly facilitated their identification and exploitation"
    publisher: "MOLDPRES"
    source_url: "https://www.moldpres.md/eng/society/prime-minister-on-cyberattack-targeting-public-digital-services-authorities-are-investigating-the-possible-involvement-of-foreign-state-actors-as-well"
  - quote: "Moldova has not publicly attributed the attack to any country or hacking group."
    publisher: "The Record"
    source_url: "https://therecord.media/moldova-investigates-possible-foreign-involvement-cyberattacks"
verification: single-source-victim
sourcing_note: >
  The agency that runs the services is the source for the dates, counts, mechanism and measures, as a victim's statement about its own incident; MOLDPRES carries the Prime
  Minister's statements and The Record restates the agency's account, so neither is an independent assessment. The counts are preliminary, the Prime Minister stresses that they
  mean at least one data element was extracted for about 750,000 numbers and not that as many accounts were hacked, and the agency and the Prime Minister give different
  numbers of disconnected services.
confidence: medium
references: ["2026-08-29/swiss-cantons-eautoindex-vehicle-registry-data-harvesting"]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

Moldova's Electronic Governance Agency (AGE) reported on 2026-10-27 that between 19 and 23 October attackers queried about one million national identification numbers (IDNPs) through state digital services and that, on preliminary estimates, data sets for about 750,000 of them were extracted; MOLDPRES had put the access requests at about 11 million on 2026-10-24 ([Moldova Electronic Governance Agency, 2026-10-27](https://egov.md/ro/node/41145); [MOLDPRES, 2026-10-24](https://www.moldpres.md/eng/society/cyberattack-on-digital-public-services-authorities-block-about-11-million-access-requests)). AGE's technical explanation is that the attackers exploited vulnerabilities in services reachable without authentication and then used the data they obtained for further extractions; the first attacks hit an electronic service that logged the legal basis of processing incorrectly, which is why citizens saw entries for civil-status document requests and driving-licence issue in the data-access history of the EVO app ([Moldova Electronic Governance Agency, 2026-10-27](https://egov.md/ro/node/41145)). Data that may be affected, not every category for every person, includes name, date and place of birth, first-degree relatives, insured status, family doctor, social benefits, pensions, disability, driving licence, photograph, vehicles and companies owned or run, IBAN, tax debts and payment history; AGE says card data is not held on the platform and it found no unauthorised change to state registers ([Moldova Electronic Governance Agency, 2026-10-27](https://egov.md/ro/node/41145)).

AGE stopped the extraction on 23 October at 11:30, reviewed 82 digital services and suspended the exposed ones, and its timeline says 82 public services and more than 30 information systems and administration panels were disconnected as a precaution on 23 October; it blocked further attempts on 25 and 27 October, and the Prime Minister's account is that 30 of the 82 services were disconnected ([Moldova Electronic Governance Agency, 2026-10-27](https://egov.md/ro/node/41145); [MOLDPRES, 2026-10-28](https://www.moldpres.md/eng/society/prime-minister-on-cyberattack-targeting-public-digital-services-authorities-are-investigating-the-possible-involvement-of-foreign-state-actors-as-well)). The Prime Minister says the incident is not isolated, that foreign state actors are being investigated and that the attackers automated the extraction, with the use of artificial intelligence allegedly facilitating the identification and exploitation of the vulnerabilities ([MOLDPRES, 2026-10-28](https://www.moldpres.md/eng/society/prime-minister-on-cyberattack-targeting-public-digital-services-authorities-are-investigating-the-possible-involvement-of-foreign-state-actors-as-well)). Moldova has not attributed the attack to any country or group ([The Record, 2026-10-28](https://therecord.media/moldova-investigates-possible-foreign-involvement-cyberattacks)).

**Exposure:** a public e-service of a federal, cantonal or communal administration that returns person data for an identifier without authentication, or whose output feeds other registers, since AGE says the extraction chained from unauthenticated services into further data ([Moldova Electronic Governance Agency, 2026-10-27](https://egov.md/ro/node/41145)).

**Detection:** citizens noticed the abuse because the data-access history in the EVO app showed processing for civil-status document requests and driving-licence issue that they had not made, so a data-subject-visible access log is a detection channel ([Moldova Electronic Governance Agency, 2026-10-27](https://egov.md/ro/node/41145)). On the server side the relevant telemetry is per-service request volume and sequential or bulk identifier lookups from one source; the sources give no breakdown of the request pattern, so that is an inference from about 11 million requests against about one million numbers.

**Defender takeaway:** list the public services that answer for a person identifier without authentication and check what each one returns, whether it feeds other registers and whether its access log records the true purpose; rate limits and alerts on bulk lookups belong in front of every such service.
