---
schema: 1
kind: research
horizon: operational
title: "Unit 42 \"Pickle in the Middle\": cross-tenant code execution in Google Vertex AI via predictable staging buckets (CVE-2026-2473)"
headline: "Unit 42 \"Pickle in the Middle\": cross-tenant code execution in Google Vertex AI via predictable staging buckets (CVE-2026-2473)"
summary: "Unit 42 disclosed a cross-tenant RCE class in the Google Cloud Vertex AI SDK for Python (Unit 42, 2026-06-16)."
discovered_at: "2026-06-17T05:14:28Z"
event_date: 2026-06-16
run_id: 2026-06-17-e102009c
priority: notable
immediate_action: null
tags:
  - cloud
  - supply-chain
  - ai-abuse
  - vulnerabilities
regions:
  - global
sectors:
  - technology
entities: []
cves: []
sources:
  - url: "https://unit42.paloaltonetworks.com/hijacking-vertex-ai-model/"
    publisher: "Unit 42, 2026-06-16"
    role: primary
  - url: "https://thehackernews.com/2026/06/google-vertex-ai-sdk-flaw-let-attackers.html"
    publisher: "The Hacker News, 2026-06-16"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: "migration: CVE fields incomplete in v2 footer (CVE-2026-2473)"
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-17.md
---

Unit 42 disclosed a cross-tenant RCE class in the Google Cloud Vertex AI SDK for Python ([Unit 42, 2026-06-16](https://unit42.paloaltonetworks.com/hijacking-vertex-ai-model/)). When a caller uploads a model without specifying a custom staging bucket, the SDK's `stage_local_data_in_gcs()` builds a deterministic, globally-unique bucket name from the project ID and region (`{project-id}-vertex-staging-{region}`). Because GCS bucket names are publicly claimable, an attacker who knows the target project ID can pre-register that bucket, attach a Cloud Function on `object.finalize`, and silently receive the victim's uploaded `model.joblib` — then swap in a malicious pickle. Vertex AI's serving agent deserialises the pickle and executes attacker code inside Google's serving container with the platform service account's privileges ([The Hacker News, 2026-06-16](https://thehackernews.com/2026/06/google-vertex-ai-sdk-flaw-let-attackers.html)). Google added bucket-name randomization (UUID4) in `google-cloud-aiplatform` 1.144.0 (2026-03-31) and the bucket-ownership check in the fully hardened 1.148.0 (2026-04-15); versions from 1.139.0 are affected and orgs on 1.144.0–1.147.x are only partially protected, so 1.148.0 is the version to target. No in-the-wild exploitation was observed.

**Why it matters to us:** Any EU/CH org running Vertex AI ML pipelines on the affected SDK that did not pin a staging bucket is exposed to the broader "resource-squatting" class — predictable cloud resource names without ownership verification. Upgrade the SDK to ≥ 1.148.0, audit jobs for default `staging_bucket` use, and alert on GCS objectCreate / ownership changes for any bucket matching the `{project-id}-vertex-staging-{region}` pattern not owned by your org.
