---
schema: 1
kind: research
horizon: operational
title: Deleted Google Cloud API keys keep authenticating for up to 23 minutes
headline: Deleted Google Cloud API keys keep authenticating for up to 23 minutes
summary: "Deleted Google Cloud API keys keep authenticating for up to 23 minutes due to GCP IAM eventual consistency — key revocation is not an immediate containment action; update GCP incident-response runbooks accordingly (Aikido, 2026-05-21)."
discovered_at: "2026-05-24T05:00:03Z"
event_date: 2026-05-21
run_id: 2026-05-24-f1fd8070
priority: high
immediate_action: null
tags:
  - cloud
  - identity
regions:
  - global
sectors:
  - public-sector
  - technology
entities: []
cves: []
sources:
  - url: "https://www.aikido.dev/blog/google-api-keys-deletion"
    publisher: "Aikido, 2026-05-21"
    role: primary
  - url: "https://www.helpnetsecurity.com/2026/05/22/deleted-google-api-keys-risk/"
    publisher: "Help Net Security, 2026-05-22"
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
migrated_from: briefs/2026-05-24.md
---

Aikido Security researcher Joe Leon published findings (2026-05-21, updated 2026-05-22) showing that deleted Google Cloud API keys continue to authenticate API requests for a median of ~16 minutes and up to ~23 minutes, measured across 10 controlled trials against Gemini, BigQuery and Maps APIs ([Aikido, 2026-05-21](https://www.aikido.dev/blog/google-api-keys-deletion)). By contrast, Google service-account keys revoke in ~5 seconds and Gemini-specific keys in ~1 minute. The root cause is eventual consistency in GCP's IAM credential-propagation layer: deletions propagate gradually across distributed authorisation servers rather than atomically. Google first closed the report as "Won't Fix (working as intended)" before reopening it as a P0 after public disclosure ([Aikido, 2026-05-21](https://www.aikido.dev/blog/google-api-keys-deletion)).

**Why it matters to us:** Key rotation/revocation is the reflexive first containment step in most cloud IR runbooks, and this breaks the assumption that it is *immediate*. An attacker holding a stolen key retains a usable window to exfiltrate BigQuery datasets, run Gemini inference, or query Maps billing after the defender believes the key is dead. For any CH/EU public-sector tenant on GCP, treat API-key deletion as a ~30-minute containment action: delete to start the clock, then monitor Cloud Audit Logs for post-deletion use of the key, and — for GDPR Art. 33 / Swiss DSG Art. 24 purposes — count the full post-deletion window as continued exposure when the key reached PII. Where viable, prefer service-account keys (near-instant revocation). Maps to ATT&CK `T1550.001` (Application Access Token).
