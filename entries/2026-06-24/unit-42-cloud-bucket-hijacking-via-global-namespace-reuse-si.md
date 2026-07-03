---
schema: 1
kind: research
horizon: operational
title: "Unit 42: cloud-bucket hijacking via global-namespace reuse silently redirects log and replication streams"
headline: "Unit 42: cloud-bucket hijacking via global-namespace reuse silently redirects log and replication streams"
summary: "Unit 42 detailed an architectural attack abusing the global uniqueness of object-storage bucket names across AWS S3, Google Cloud Storage and (less so) Azure Blob Storage (Unit 42, 2026-06-22)."
discovered_at: "2026-06-24T05:11:52Z"
event_date: 2026-06-22
run_id: 2026-06-24-de656486
priority: notable
immediate_action: null
tags:
  - cloud
  - info-disclosure
  - supply-chain
regions:
  - global
sectors:
  - technology
  - public-sector
entities:
  - "campaign:cloud-bucket-hijacking-namespace-reuse"
cves: []
sources:
  - url: "https://unit42.paloaltonetworks.com/cloud-bucket-hijacking-risks/"
    publisher: Unit 42 (Palo Alto Networks)
    role: primary
closed_sources: []
evidence:
  - quote: Unit 42 research details how attackers could exploit global name uniqueness in bucket hijacking to redirect cloud data streams across major CSPs
    publisher: Unit 42
verification: single-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-24.md
---

Unit 42 detailed an architectural attack abusing the global uniqueness of object-storage bucket names across AWS S3, Google Cloud Storage and (less so) Azure Blob Storage ([Unit 42, 2026-06-22](https://unit42.paloaltonetworks.com/cloud-bucket-hijacking-risks/)). An actor holding bucket-delete rights deletes a destination bucket and immediately recreates it under their own account; existing log sinks, replication jobs, Pub/Sub-to-Storage subscriptions and Data Firehose streams keep writing to the now attacker-owned bucket with no config change and no entry in the source account's audit trail. No named in-the-wild exploitation is reported — this is offensive-research surfacing of an exposure class — but the impact on audit-log integrity is exactly what a SOC's detection pipeline depends on. `[SINGLE-SOURCE]` (Unit 42, a vendor lab, so the national-CERT carve-out does not apply; the underlying CSP behaviours are independently verifiable). Detection: alert on storage bucket-deletion API calls (GCP `storage.buckets.delete`, AWS CloudTrail `DeleteBucket`, Azure `Microsoft.Storage/storageAccounts/delete`) and on recreation of sink/replication targets; hardening: require multi-party approval for bucket deletion, enforce GCP VPC Service Controls / AWS account-region namespace isolation, and track sensitive-bucket ownership with DSPM. Maps to `T1485`/`T1578` (resource manipulation) and the effective outcome of `T1530` (data from cloud storage).
