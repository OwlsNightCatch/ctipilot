---
schema: 1
kind: vulnerability
horizon: operational
title: "GeoServer: an unauthenticated SQL injection in jsonArrayContains was dropped as a zero-day with no CVE and no patch, and scanning for it started within hours"
headline: "The server behind Europe's public map portals has an open pre-auth injection, and its database account decides whether that becomes code execution"
summary: >
  A researcher using the handle @q1uf3ng published an unauthenticated SQL-injection flaw in GeoServer's
  jsonArrayContains function on X at 10:46 UTC on 2026-08-12, stating that where the backing database account is the
  SQL Server system administrator it follows naturally to remote code execution. No CVE has been assigned, GeoServer's
  project blog carries no advisory, and no national CERT has picked it up. watchTowr told two outlets it began seeing
  exploitation attempts within hours and has recorded hundreds from a small pool of addresses — but describes what it
  sees as probing that triggers errors and goes no further, not payload delivery. The same function carried a
  SQL-injection flaw fixed in 2023 for PostGIS and Oracle datastores, so the current path is a different backend the
  earlier fix did not close.
discovered_at: "2026-08-14T07:45:00Z"
event_date: "2026-08-12"
run_id: 2026-08-14T0417Z-intel
priority: high
immediate_action: null
tags:
  - vulnerabilities
  - zero-day
  - pre-auth
  - sqli
  - rce
  - no-patch
regions:
  - global
  - europe
sectors:
  - public-sector
  - energy
  - water
  - transport
entities: []
techniques:
  - T1190
  - T1595.002
affected_products:
  - "GeoServer"
cves: []
sources:
  - url: "https://thehackernews.com/2026/08/unpatched-geoserver-zero-day-targeted.html"
    publisher: "The Hacker News"
    date: "2026-08-13"
    role: primary
  - url: "https://www.csoonline.com/article/4209388/attackers-target-zero-day-vulnerability-in-geospatial-data-platform-geoserver.html"
    publisher: "CSO Online"
    date: "2026-08-13"
    role: corroborating
  - url: "https://osv.dev/vulnerability/GHSA-7g5f-wrx8-5ccf"
    publisher: "GitHub Advisory Database (via OSV)"
    date: "2023-02-22"
    role: corroborating
  - url: "https://geoserver.org/blog/"
    publisher: "GeoServer project"
    date: "2026-06-11"
    role: corroborating
closed_sources: []
evidence:
  - quote: "It was first disclosed on August 12, 2026, at 10:46 UTC, by a researcher named @q1uf3ng on X. \"GeoServer jsonArrayContains unauthorized SQL injection, and in the case of the sa [system administrator] database, it's naturally possible to achieve RCE,\" the researcher said."
    publisher: "The Hacker News"
  - quote: "Currently, we're seeing attackers probe to identify vulnerable systems across the internet, triggering errors and not proceeding further,"
    publisher: "The Hacker News"
  - quote: "The threat intelligence and exposure management platform said it began to observe exploitation attempts within hours of public disclosure, and that it has seen hundreds of attempts originating from a small pool of IP addresses."
    publisher: "The Hacker News"
verification: multi-source
sourcing_note: >
  No CVE identifier exists for this flaw and no vendor advisory has been published — the GeoServer project blog's
  most recent post is its 3.0.0 release of 2026-06-11 and does not mention it, and the flaw is not on the CISA
  exploited-vulnerabilities catalogue, which does already carry earlier GeoServer entries (and one for a library it
  uses); no source states a count and none is asserted here. The exploitation-attempt
  figures come from watchTowr alone, given as statements to two outlets rather than published as research with a
  stated methodology, and neither outlet observed the activity independently; they are reported here as one vendor's
  self-reported telemetry. No affected version range is stated by any source, which is why none appears here. A
  proof-of-concept repository describing a PostgreSQL variant of the same function's injection path was found during
  research but could not be tied to this disclosure by any primary source and is not carried. Searching for this flaw
  surfaces a false CVE mapping — the identifier that circulates alongside it belongs to an unrelated SAP Commerce
  Cloud vulnerability — and this entry deliberately carries no CVE at all.
confidence: medium
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Inventory GeoServer instances reachable from untrusted networks and check what database account each one connects with — the injection needs no authentication to GeoServer, but whether it becomes code execution is decided by whether that account holds administrative rights on the database. Reducing the GeoServer service account to least privilege on its datastore is the control available today, because no patch exists to apply."
migrated_from: null
---

A researcher posting as @q1uf3ng published an unauthenticated SQL-injection flaw in GeoServer on 2026-08-12 without warning the project. The Hacker News records both the timing and the claim: ["It was first disclosed on August 12, 2026, at 10:46 UTC, by a researcher named @q1uf3ng on X. \"GeoServer jsonArrayContains unauthorized SQL injection, and in the case of the sa [system administrator] database, it's naturally possible to achieve RCE,\" the researcher said."](https://thehackernews.com/2026/08/unpatched-geoserver-zero-day-targeted.html) That sentence contains the whole risk model. The injection itself needs no GeoServer credential. What decides whether it stops at reading the database or continues to running commands on the host is the privilege of the account GeoServer authenticates to its datastore with — CSO Online puts it plainly, that where the database runs with administrator permissions on Microsoft SQL Server the account can also execute operating-system commands, so the injection becomes a code-execution vector ([CSO Online, 2026-08-13](https://www.csoonline.com/article/4209388/attackers-target-zero-day-vulnerability-in-geospatial-data-platform-geoserver.html)).

**Nothing to patch, and nobody has claimed it.** No CVE identifier has been assigned. The GeoServer project's blog carries no advisory — its most recent post is the 3.0.0 release announcement of 2026-06-11 ([GeoServer project](https://geoserver.org/blog/)) — and no source states which release lines or version boundary are affected, so an operator cannot even scope exposure by version today. That absence is itself the operational fact: the only levers available are network position and database privilege.

**What is actually being seen, stated precisely.** watchTowr told both outlets that ["The threat intelligence and exposure management platform said it began to observe exploitation attempts within hours of public disclosure, and that it has seen hundreds of attempts originating from a small pool of IP addresses."](https://thehackernews.com/2026/08/unpatched-geoserver-zero-day-targeted.html) Its own characterisation of that traffic is deliberately modest: ["Currently, we're seeing attackers probe to identify vulnerable systems across the internet, triggering errors and not proceeding further,"](https://thehackernews.com/2026/08/unpatched-geoserver-zero-day-targeted.html) said principal security researcher Jake Knott, who added that this is unlikely to remain the case, that GeoServer has a track record of being targeted and exploited at scale with multiple entries in the exploited-vulnerabilities catalogue, and that under certain configurations this flaw could ultimately lead to remote code execution. CSO Online reports the same picture — no malicious payloads or commands seen yet, the attempts looking like probes to identify vulnerable instances — and notes a second-hand claim on X of reproduction in a non-default configuration, which no technical write-up corroborates. So the honest status is mass fingerprinting of an open flaw, not mass exploitation of it, with a named reason to expect the second to follow the first.

**Why this matters here specifically.** GeoServer is the open-source engine under a great many European public-sector geospatial services — cadastral viewers, environmental and hydrological portals, the map services published under the INSPIRE directive — and under utility and transport asset systems. Those deployments are internet-facing by design, because publishing map data to the public is what they are for, and they are frequently operated by small teams inside cantonal, municipal or agency IT rather than by a central SOC. Two GeoServer flaws are already on the exploited-vulnerabilities catalogue, and the mass exploitation of the 2024 one is the precedent this most resembles.

**The function has been here before, and the previous fix does not cover this.** GeoServer patched a SQL injection in the same `jsonArrayContains` function in 2023, in releases 2.21.4, 2.22.2, 2.20.7, 2.19.7 and 2.18.7; that advisory scoped the flaw to the function being [used "with a String or JSON field and with a PostGIS or Oracle DataStore (GeoServer 2.22.0+ only)"](https://osv.dev/vulnerability/GHSA-7g5f-wrx8-5ccf). The current reporting centres on a Microsoft SQL Server backend, a different datastore than that fix addressed — which is the most useful thing an operator can take from the history: being patched against the 2023 issue says nothing about today's, and the sanitisation problem in this function has evidently been solved per-backend rather than at the source.

**Detection and interim controls.** With no patch and no version boundary, the work is exposure reduction and hunting. Take GeoServer's Web Feature Service and OGC filter endpoints off the public internet where the service does not genuinely need anonymous access, and put an authenticating reverse proxy in front of the ones that do. Reduce the datastore account GeoServer uses to the minimum rights its layers require — that single change converts the worst case from host compromise to unauthorised reads, and it is the only mitigation available today that touches the RCE path rather than the injection. In telemetry, the observable that matches what watchTowr describes is a burst of requests to GeoServer's feature endpoints carrying filter expressions that provoke database errors, from a small number of sources, against many hosts; in the application and database logs the equivalent is a rise in SQL syntax errors originating from the GeoServer service account. **Triage:** malformed OGC filter requests and database errors are ordinary background noise on a public map server, produced by broken clients and hand-written queries all day. The discriminators are the sequence and the source — many distinct GeoServer instances probed from the same small address pool inside the same window, error-generating requests with no accompanying legitimate map or feature retrieval from that client, and any database error whose text indicates statement stacking rather than a malformed value. A single error from a client that also renders maps normally is a broken client; a client that only ever produces errors is not one.
