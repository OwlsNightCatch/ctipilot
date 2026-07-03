---
schema: 1
kind: research
horizon: operational
title: Unit 42 catalogues cloud-logging defense-evasion across AWS CloudTrail and Google Cloud Logging — with concrete detection mappings
headline: Unit 42 catalogues cloud-logging defense-evasion across AWS CloudTrail and Google Cloud Logging — with concrete detection mappings
summary: "Unit 42 enumerates seven cloud-logging attack categories — five evasion, two visibility (Unit 42, 2026-06-09)."
discovered_at: "2026-06-10T05:00:13Z"
event_date: 2026-06-09
run_id: 2026-06-10-c84347b2
priority: notable
immediate_action: null
tags:
  - cloud
  - identity
regions:
  - global
sectors:
  - finance
  - public-sector
entities: []
cves: []
sources:
  - url: "https://unit42.paloaltonetworks.com/cloud-logging-defense-evasion/"
    publisher: "Unit 42, 2026-06-09"
    role: primary
closed_sources: []
evidence: []
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
migrated_from: briefs/2026-06-10.md
---

Unit 42 enumerates seven cloud-logging attack categories — five evasion, two visibility ([Unit 42, 2026-06-09](https://unit42.paloaltonetworks.com/cloud-logging-defense-evasion/)). Evasion techniques: stopping CloudTrail trails (`StopLogging`), deleting S3/GCS log destinations, removing GCP log-routing sinks, impairing customer-managed encryption keys (CMEK) so logs become unreadable, and log poisoning to mask activity with benign-looking entries; visibility techniques redirect logs to attacker accounts via cross-account delivery for long-term reconnaissance of defender detections (T1562.008, T1070, T1530). Hardening: S3 Object Lock / GCS locked-bucket immutable retention; IAM restrictions on `cloudtrail:StopLogging`, `cloudtrail:DeleteTrail`, `logging.sinks.delete`; alert on `cloudtrail:UpdateTrail` modifying KMS-key associations and on KMS key-policy changes affecting CloudTrail encryption. Log-integrity monitoring is a NIS2 incident-detection expectation, making this directly relevant to EU cloud-resident public-sector and financial workloads. [SINGLE-SOURCE] (Unit 42 primary research).
