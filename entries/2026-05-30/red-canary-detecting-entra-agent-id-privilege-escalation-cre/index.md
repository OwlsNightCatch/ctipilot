---
schema: 1
kind: research
title: "Red Canary: detecting Entra Agent ID privilege escalation — credential injection into agent blueprints enables lateral movement across the entire tenant"
headline: "Red Canary: detecting Entra Agent ID privilege escalation — credential injection into agent blueprints enables lateral movement across the entire tenant"
summary: "Red Canary published a detection-engineering primer on 27 May 2026 on the AgentIdentityBlueprint.AddRemoveCreds.All role in Microsoft Entra's new Agent ID identity class — autonomous app identities that act in a tenant without human interaction (Red Canary, 2026-05-27)."
discovered_at: "2026-05-30T05:00:10Z"
event_date: 2026-05-27
run_id: 2026-05-30-aca445cc
priority: notable
immediate_action: null
tags:
  - identity
  - cloud
  - ai-abuse
regions:
  - global
sectors:
  - public-sector
  - technology
entities:
  - "trend:entra-agent-id-obo-abuse-redcanary"
cves: []
sources:
  - url: "https://redcanary.com/blog/threat-detection/entra-id-ai-workflows/"
    publisher: Red Canary
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
migrated_from: briefs/2026-05-30.md
---

Red Canary published a detection-engineering primer on 27 May 2026 on the `AgentIdentityBlueprint.AddRemoveCreds.All` role in Microsoft Entra's new Agent ID identity class — autonomous app identities that act in a tenant without human interaction ([Red Canary, 2026-05-27](https://redcanary.com/blog/threat-detection/entra-id-ai-workflows/)). A misconfigured or adversary-controlled agent identity holding this role can add client secrets to any agent blueprint, then authenticate as any agent identity in the tenant — including high-privilege ones — after legitimate credential rotation. The full privilege-escalation chain: agent app → malicious role assignment (`AgentIdentityBlueprint.AddRemoveCreds.All`) → credential injection into target blueprint → authenticate as high-privilege agent → pivot to all downstream resources that blueprint can access. Relevant log sources: `AuditLogs` — look for "Update application – Certificates and secrets management" with a non-human `InitiatedBy.app.servicePrincipalId`; `MicrosoftGraphActivityLogs` — Graph API calls from agent service principals with unusual IP and UserAgent fields; `AADServicePrincipalSignInLogs` — filter on `Agent.agentType: agenticAppInstance`. Correlation: match `SignInActivityId` from Graph logs to `UniqueTokenIdentifier` in sign-in logs to reconstruct credential-add-to-authentication chains. MITRE ATT&CK: T1098 (Account Manipulation), T1078.004 (Valid Accounts: Cloud Accounts). Swiss public-sector M365 deployments adopting AI agents via Copilot Studio or Azure AI Foundry should establish baselines for each agent identity's API scope and alert on credential additions to blueprints by any identity other than the provisioning pipeline. [SINGLE-SOURCE]
