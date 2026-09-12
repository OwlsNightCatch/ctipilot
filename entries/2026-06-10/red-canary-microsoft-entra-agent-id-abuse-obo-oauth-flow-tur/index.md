---
schema: 1
kind: research
title: "Red Canary: Microsoft Entra Agent ID abuse — OBO OAuth flow turns a compromised AI agent into a delegated phishing sender"
headline: "Red Canary: Microsoft Entra Agent ID abuse — OBO OAuth flow turns a compromised AI agent into a delegated phishing sender"
summary: "Red Canary's latest Entra ID AI-agent analysis examines the On-Behalf-Of (OBO) OAuth flow exploited through assistive agents (Red Canary, 2026-06-08)."
discovered_at: "2026-06-10T05:00:14Z"
event_date: 2026-06-08
run_id: 2026-06-10-c84347b2
priority: notable
immediate_action: null
tags:
  - identity
  - ai-abuse
  - phishing
  - cloud
regions:
  - global
sectors:
  - public-sector
entities:
  - "trend:entra-agent-id-obo-abuse-redcanary"
cves: []
sources:
  - url: "https://redcanary.com/blog/threat-detection/entra-id-ai-workflows-assistive-agents/"
    publisher: "Red Canary, 2026-06-08"
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

Red Canary's latest Entra ID AI-agent analysis examines the On-Behalf-Of (OBO) OAuth flow exploited through assistive agents ([Red Canary, 2026-06-08](https://redcanary.com/blog/threat-detection/entra-id-ai-workflows-assistive-agents/)). An agent blueprint configured with `access_agent` scope and broad Graph permissions (Mail.Send, Mail.ReadWrite, Group.Read.All) can send phishing email via the Graph `sendMail` endpoint with full delegated authority, appearing to originate from the impersonated user; standard sign-in and Exchange audit logs show the agent acting for the user, not an attacker (T1199, T1078.004). Detection requires correlating three sources — MicrosoftGraphActivityLogs (`Agent.agentType == agenticAppInstance AND Agent.agentSubjectType == notAgentic`), AADNonInteractiveUserSignInLogs, and Exchange Purview audit logs — joined on `ClientRequestId`. Defenders should audit Entra agent-blueprint permission grants for dangerous scope combinations and apply least privilege. As Microsoft 365 Copilot/agent features roll into CH/EU public-sector tenants, this becomes a near-term identity-monitoring gap. [SINGLE-SOURCE] (Red Canary primary research).
