---
schema: 1
kind: vulnerability
title: "Splunk Enterprise SVD-2026-1103: two unauthenticated REST API authentication bypasses that accept an empty shared secret (CVE-2026-76536 in the cluster configuration endpoint, CVSS 3.1 9.4; CVE-2026-76535 in RapidDiag task collection, which runs searches as an authenticated user, 9.1) and three more unauthenticated rows at 7.5; fixed in 10.6.1, 10.4.5, 10.2.9, 10.0.12 and 9.4.17, no exploitation reported"
headline: "Splunk Enterprise: unauthenticated REST bypasses accept an empty pass4SymmKey (CVSS 9.4, 9.1); set the key, upgrade"
summary: >
  Splunk's SVD-2026-1103 of 2026-11-18 fixes 38 flaws in Splunk Enterprise, among them unauthenticated authentication bypasses in the REST API that rest on an empty shared secret: CVE-2026-76536 (CVSS 3.1 9.4, reads and changes clustering configuration on a standalone instance) and CVE-2026-76535 (9.1, runs search queries as an authenticated user), plus three rows at 7.5, two on an empty or factory-default shared key and one that crashes splunkd. Splunk lists fixes in 10.6.1, 10.4.5, 10.2.9, 10.0.12 and 9.4.17 and a workaround of setting a non-empty pass4SymmKey; it does not say an empty secret is the out-of-the-box state, and no source reports exploitation.
discovered_at: "2026-11-25T04:51:00Z"
updated_at: null
event_date: "2026-11-18"
run_id: 2026-11-25T0356Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, auth-bypass, pre-auth, patch-available]
regions: [global]
sectors: [technology]
entities: [product:splunk-enterprise]
techniques: [T1190]
affected_products: ["Splunk Enterprise"]
cves:
  - id: CVE-2026-76536
    cvss: "9.4"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Splunk Enterprise below 10.4.5, 10.2.9, 10.0.12 and 9.4.17, on a standalone instance with clustering turned off"
    fixed: "10.4.5, 10.2.9, 10.0.12, 9.4.17"
  - id: CVE-2026-76535
    cvss: "9.1"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Splunk Enterprise below 10.6.1, 10.4.5, 10.2.9, 10.0.12 and 9.4.17"
    fixed: "10.6.1, 10.4.5, 10.2.9, 10.0.12, 9.4.17"
  - id: CVE-2026-131192
    cvss: "7.5"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Splunk Enterprise below 10.6.1, 10.4.5, 10.2.9, 10.0.12 and 9.4.17, on a standalone instance or a search head that is not an indexer cluster member"
    fixed: "10.6.1, 10.4.5, 10.2.9, 10.0.12, 9.4.17"
  - id: CVE-2026-131190
    cvss: "7.5"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Splunk Enterprise below 10.4.5, 10.2.9, 10.0.12 and 9.4.17"
    fixed: "10.4.5, 10.2.9, 10.0.12, 9.4.17"
sources:
  - url: "https://advisory.splunk.com/advisories/SVD-2026-1103"
    publisher: "Splunk"
    date: "2026-11-18"
    role: primary
  - url: "https://advisories.ncsc.nl/advisory?id=NCSC-2026-0512"
    publisher: "NCSC-NL"
    date: "2026-11-23"
    role: corroborating
closed_sources: []
evidence: []
verification: single-source
sourcing_note: "Splunk is the vendor and the only first-hand source; NCSC-NL's advisory of 2026-11-23 relays the fixed versions and rates the likelihood medium and the damage high. Scores are Splunk's CVSS 3.1 figures. The advisory names no management port and does not state that the empty secret is the default on a stock install."
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Set a strong pass4SymmKey of at least 12 characters in server.conf on every Splunk Enterprise instance below the fixed versions (the [clustering] stanza for CVE-2026-76536 and CVE-2026-131192; Splunk names no stanza for CVE-2026-76535), with the same value on every node that participates in the service, restart it, remove the RapidDiag app where it is not needed and upgrade to 10.6.1, 10.4.5, 10.2.9, 10.0.12 or 9.4.17, instances whose management API is reachable from user or internet networks first, because the unauthenticated REST bypasses accept an empty shared secret."
updates: []
migrated_from: null
---

Splunk's advisory SVD-2026-1103 of 2026-11-18 fixes 38 flaws in Splunk Enterprise, two rated Critical and unauthenticated ([Splunk, 2026-11-18](https://advisory.splunk.com/advisories/SVD-2026-1103)). CVE-2026-76536 (CVSS 3.1 9.4) lets an unauthenticated user use an empty clustering shared secret to read and modify clustering configuration through the cluster configuration REST endpoint on a standalone instance with clustering turned off, and CVE-2026-76535 (9.1) lets an unauthenticated user run arbitrary SPL searches through RapidDiag task collection as an authenticated user, because Splunk Enterprise accepts an empty shared secret on those requests ([Splunk, 2026-11-18](https://advisory.splunk.com/advisories/SVD-2026-1103)). Three further unauthenticated rows are rated 7.5: CVE-2026-131192 gives access to live event data from the indexing pipeline on a standalone instance or a search head that is not an indexer cluster member, on an empty shared key, and CVE-2026-131190 exposes RapidDiag process metadata and a log file inventory through endpoints that accept a factory-default shared key, and a third lets an unauthenticated user crash the Splunk daemon through the S2S data-forwarding receiver, for which Splunk lists no workaround ([Splunk, 2026-11-18](https://advisory.splunk.com/advisories/SVD-2026-1103)).

Splunk lists fixes in 10.6.1, 10.4.5, 10.2.9, 10.0.12 and 9.4.17, with CVE-2026-76536 and CVE-2026-131190 not listed for the 10.6 branch ([Splunk, 2026-11-18](https://advisory.splunk.com/advisories/SVD-2026-1103)). For CVE-2026-76535 Splunk says to set a non-empty pass4SymmKey in server.conf, using the same value on each node that participates in the service, and restart; for CVE-2026-76536 the workaround is a strong, unique pass4SymmKey of at least 12 characters in the [clustering] stanza of server.conf, standalone instances included, followed by a restart; CVE-2026-131190 is closed by turning off or removing the RapidDiag app ([Splunk, 2026-11-18](https://advisory.splunk.com/advisories/SVD-2026-1103)). The advisory does not say any flaw is exploited; NCSC-NL rates the likelihood medium and the damage high ([NCSC-NL, 2026-11-23](https://advisories.ncsc.nl/advisory?id=NCSC-2026-0512)).

**Exposure:** a Splunk Enterprise instance whose pass4SymmKey is empty or unset (for CVE-2026-131190, one that accepts RapidDiag's factory-default key) and whose management REST API can be reached by an untrusted host; Splunk does not say an empty secret is the default on a stock install, so the effective value in server.conf is the thing to read on each instance, and Splunk Cloud impact is not addressed in the advisory.

**Defender takeaway:** set a non-empty pass4SymmKey on every Splunk Enterprise instance now, since that is the workaround for the two Critical rows, and take the upgrade at the next window if the management API is internal; instances reachable from user or internet networks are the ones to do first.
