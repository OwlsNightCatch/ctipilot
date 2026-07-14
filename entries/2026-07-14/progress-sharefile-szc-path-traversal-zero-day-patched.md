---
schema: 1
kind: vulnerability
horizon: operational
title: "Progress confirms the ShareFile Storage Zone Controller shutdown was forced by a path-traversal zero-day; patches 5.12.5 / 6.0.2 ship and service is restored"
headline: "Progress names the ShareFile Storage Zone Controller root cause — a path-traversal flaw — and ships the fix; a CVE is reserved but withheld for two weeks"
summary: >
  Progress has confirmed the root cause behind its emergency ShareFile Storage Zone Controller (SZC) shutdown:
  a high-severity path-traversal flaw in SZC 5.x/6.x that an authenticated administrative user can use to read
  arbitrary service-account files, write to server directories, and enumerate the filesystem. Progress shipped
  patched versions 5.12.5 and 6.0.2 and is restoring customer access; a CVE identifier is reserved but will not
  be published for two weeks. On-prem SZC operators should patch and follow Progress's recovery steps now.
discovered_at: "2026-07-14T20:21:02Z"
event_date: "2026-07-14"
run_id: 2026-07-14T2009Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, path-traversal, zero-day, patch-available]
regions: [global, europe, us]
sectors: [public-sector, finance, healthcare]
entities: [incident:progress-sharefile-storage-zone-controller-shutdown-2026-07]
techniques: [T1190]
affected_products: ["Progress ShareFile Storage Zone Controller"]
cves: []
sources:
  - url: "https://www.bleepingcomputer.com/news/security/progress-confirms-sharefile-zero-day-flaw-behind-storage-zone-shutdown/"
    publisher: "BleepingComputer"
    date: "2026-07-14"
    role: primary
  - url: "https://status.sharefile.com/"
    publisher: "Progress — ShareFile Status Page"
    date: "2026-07-14"
    role: corroborating
closed_sources: []
evidence:
  - quote: "An authenticated administrative user can read arbitrary files accessible to the application's service account"
    publisher: "BleepingComputer"
  - quote: "Currently, we have no indication of unauthorized access to any ShareFile customer account or data"
    publisher: "BleepingComputer"
  - quote: "Storage Zones Controller customer access is currently being restored. Recovery instructions have been provided directly to account owners."
    publisher: "Progress — ShareFile Status Page"
verification: multi-source
sourcing_note: "Progress's own statements (relayed by BleepingComputer) and the vendor status page are the primary sources; Progress is the authority for its own product. The reserved CVE identifier is withheld for two weeks — no CVE number is asserted here."
confidence: high
update_of: 2026-07-14/progress-sharefile-szc-active-exploitation-confirmed
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions:
  - "Apply ShareFile Storage Zone Controller 5.12.5 or 6.0.2 to every on-prem SZC now and follow Progress's account-owner recovery instructions before returning the component to service — this is the fix for the flaw behind the 2026-07-10 emergency shutdown, against which in-the-wild exploitation attempts were already observed."
migrated_from: null
---

**UPDATE (originally covered 2026-07-13):** Progress Software has confirmed the root cause behind its emergency ShareFile Storage Zone Controller (SZC) shutdown order: a high-severity path-traversal vulnerability affecting SZC versions 5.x and 6.x that lets an authenticated administrative user read arbitrary files accessible to the application's service account, write malicious content to server directories, and enumerate the filesystem layout ([BleepingComputer, 2026-07-14](https://www.bleepingcomputer.com/news/security/progress-confirms-sharefile-zero-day-flaw-behind-storage-zone-shutdown/)) — a CWE-22-class flaw reachable through the SZC's internet-facing IIS component. Progress has shipped patched versions 5.12.5 and 6.0.2, and a CVE identifier is reserved but will not be published for two weeks. The vendor states it has "no indication of unauthorized access to any ShareFile customer account or data," a claim that sits alongside this run's earlier finding that Shadowserver honeypots recorded in-the-wild exploitation attempts against the same component from 2026-07-10. Progress's status page confirms Storage Zone Controller customer access "is currently being restored," with recovery instructions issued directly to account owners ([Progress — ShareFile Status Page, 2026-07-14](https://status.sharefile.com/)), closing out the multi-day outage that began with the 2026-07-10 shutdown order.

**Defender takeaway:** the new detail is the fix — patched versions (5.12.5, 6.0.2) and a named vulnerability class (path traversal, authenticated-admin scope) that the two prior entries in this thread lacked. Any organization that took SZC offline under the shutdown order should patch to the fixed build and complete Progress's recovery procedure before re-exposing the component; do not re-enable an unpatched controller. **Triage:** path-traversal exploitation of this component surfaces in the SZC's IIS/web request telemetry as requests carrying directory-traversal sequences to the storage-controller endpoints and in file-access telemetry as the service account reading or writing paths outside its normal content directories — legitimate SZC operation confines the service account to its configured storage paths, so out-of-tree file access under that account is the discriminator.
