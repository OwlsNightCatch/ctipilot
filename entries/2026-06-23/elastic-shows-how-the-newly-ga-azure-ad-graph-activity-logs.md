---
schema: 1
kind: research
horizon: operational
title: Elastic shows how the newly-GA Azure AD Graph Activity Logs close a long-standing Entra enumeration blind spot
headline: Elastic shows how the newly-GA Azure AD Graph Activity Logs close a long-standing Entra enumeration blind spot
summary: "Elastic Security Labs published a detection-engineering guide (2026-06-19) on ingesting the newly generally-available AADGraphActivityLogs into SIEM/XDR to catch tooling that has historically been invisible (Elastic Security Labs, 2026-06-19)."
discovered_at: "2026-06-23T04:52:49Z"
event_date: 2026-06-19
run_id: 2026-06-23-165387f6
priority: notable
immediate_action: null
tags:
  - identity
  - cloud
  - espionage
regions:
  - global
  - europe
  - switzerland
sectors:
  - public-sector
  - technology
entities: []
cves: []
sources:
  - url: "https://www.elastic.co/security-labs/aad-graph-activity-logs-threat-detection"
    publisher: Elastic Security Labs
    role: primary
closed_sources: []
evidence:
  - quote: Azure AD Graph Activity Logs land in Elastic with full ECS parsing. Detect ROADrecon and AADInternals enumeration with ready-to-use detection rules.
    publisher: Elastic Security Labs
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
migrated_from: briefs/2026-06-23.md
---

Elastic Security Labs published a detection-engineering guide (2026-06-19) on ingesting the newly generally-available `AADGraphActivityLogs` into SIEM/XDR to catch tooling that has historically been invisible ([Elastic Security Labs, 2026-06-19](https://www.elastic.co/security-labs/aad-graph-activity-logs-threat-detection)). Although Microsoft deprecated Azure AD Graph in favour of Microsoft Graph, the legacy API remains live and is actively used by ROADtools (ROADrecon), AzureHound and AADInternals for Entra ID tenant enumeration — the classic pre-lateral-movement step in identity attacks. The new log source (available from early 2026) records every legacy-Graph call with UPN, `client_id`, user-agent, source IP, HTTP method, resource path and response code. Elastic's rules surface ROADrecon-pattern user-agents, anomalous 4xx bursts (permission probing), FOCI (Family Of Client IDs) mismatches that signal lateral movement, device-code-flow auth immediately followed by Graph enumeration, and unusual ASN origins for Graph calls. `[SINGLE-SOURCE]` — Elastic is a vendor lab, not a national CERT, so the carve-out does not apply; the underlying log source and detections are independently verifiable against Microsoft documentation (.

**Why it matters to us:** Entra ID is the identity backbone for Swiss federal and cantonal administrations, EU institutions and essentially every Microsoft 365 tenant, and legacy-Graph enumeration has been a genuine detection gap for years. The concrete action is cheap and high-value: enable `AADGraphActivityLogs` in Entra diagnostic settings and route them to your SIEM, then build (or import Elastic's) detections on `userAgent.original`, `client_id` against your known app registrations, and `http.response.status_code` 4xx spikes (`T1590` Gather Victim Network Information, `T1087.004` Account Discovery: Cloud Account, `T1078.004` Valid Accounts: Cloud Accounts).
