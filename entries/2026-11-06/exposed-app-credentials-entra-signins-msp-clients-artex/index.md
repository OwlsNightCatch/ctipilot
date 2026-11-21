---
schema: 1
kind: threat
title: "Exposed application credentials: Microsoft sees an agentic framework search GitHub for OAuth and cloud application secrets and then sign in as the applications from 2026-10-28, and Todyl sees an operator use MSP applications to reach 27 organisations, government clients among them"
headline: "Entra app-credential abuse: agents hunt GitHub for secrets, an operator reaches MSP clients, government among them"
summary: >
  Microsoft reports that since August threat actors have used the agentic framework ARTEX to query public GitHub for OAuth application secrets and cloud keys, and that from 2026-10-28 valid
  application credentials were used for service-principal sign-ins across dozens of applications in several tenants, a vendor-owned multitenant application among them. Todyl's telemetry
  shows one operator since 2026-11-01 targeting about 45 application registrations at MSPs, more than 33 of which authenticated, and reaching 27 organisations, government clients among them; Microsoft says a similar
  campaign involving the same addresses was reported by Todyl, and Todyl's update of 2026-11-06 now assesses its operator as an automated agentic credential crawler, likely fed by secrets exposed in public repositories or web apps.
discovered_at: "2026-11-06T03:46:00Z"
updated_at: "2026-11-08T13:59:00Z"
event_date: "2026-11-05"
run_id: 2026-11-06T0255Z-intel
priority: high
immediate_action: null
tags: [identity, cloud, ai-abuse, supply-chain]
regions: [global]
sectors: [public-sector]
entities: ["campaign:exposed-app-credentials-entra-service-principal-signins-2026-11", "tool:artex", "product:microsoft-entra-id", "product:microsoft-azure", "product:microsoft-azure-devops", "incident:connectwise-cloud-backup-skykick-app-credential-abuse-2026-10"]
techniques: [T1593.003, T1552.001, T1078.004, T1550.001, T1555.006, T1530, T1213.002, T1114.002, T1651, T1580, T1199]
affected_products: ["Microsoft Entra ID", "Microsoft Azure", "Microsoft Azure DevOps", "Microsoft 365"]
cves: []
sources:
  - url: "https://www.microsoft.com/en-us/security/blog/2026/11/05/threat-actors-use-agentic-ai-tooling-to-find-and-abuse-exposed-secrets/"
    publisher: "Microsoft Threat Intelligence"
    date: "2026-11-05"
    role: primary
  - url: "https://www.todyl.com/blog/stolen-app-credentials-real-access-an-actor-is-signing-into-entra-id-and-azure-devops-as-your-workloads"
    publisher: "Todyl"
    date: "2026-11-03"
    role: primary
closed_sources: []
evidence:
  - quote: "Starting in August 2026, Microsoft observed threat actors using an agentic AI offensive framework to submit large volumes of queries to GitHub for secrets."
    publisher: "Microsoft Threat Intelligence"
    source_url: "https://www.microsoft.com/en-us/security/blog/2026/11/05/threat-actors-use-agentic-ai-tooling-to-find-and-abuse-exposed-secrets/"
  - quote: "Sign-in errors AADSTS7000215 (invalid secret) or AADSTS7000222 (expired secret) indicate someone holds a credential for your app; a failure followed by a success is urgent."
    publisher: "Microsoft Threat Intelligence"
    source_url: "https://www.microsoft.com/en-us/security/blog/2026/11/05/threat-actors-use-agentic-ai-tooling-to-find-and-abuse-exposed-secrets/"
  - quote: "Through those apps the actor has reached 27 organizations so far, including the MSPs' downstream clients in government, energy, food and agriculture, transportation, construction and engineering, legal, education and nonprofits."
    publisher: "Todyl"
    source_url: "https://www.todyl.com/blog/stolen-app-credentials-real-access-an-actor-is-signing-into-entra-id-and-azure-devops-as-your-workloads"
  - quote: "This activity is an automated, agentic credential crawler: AI-driven tooling that finds exposed secrets, signs in with them, and acts on what it collects with little human direction."
    publisher: "Todyl"
    source_url: "https://www.todyl.com/blog/stolen-app-credentials-real-access-an-actor-is-signing-into-entra-id-and-azure-devops-as-your-workloads"
verification: multi-source
sourcing_note: >
  Microsoft and Todyl each hold their own telemetry. Microsoft states that a similar campaign involving the same addresses was reported by Todyl, so the overlap rests on an address match that Microsoft draws; Todyl's first account (2026-11-03) left the credential source open and read several seed secrets as pointing away from internet-crawled configurations; its update of 2026-11-06 assesses the activity as an automated agentic credential crawler and takes the ARTEX name and the GitHub access path from Microsoft, so on those two points it adds no second observation. Todyl assesses the activity as unrelated to the October ConnectWise Cloud Backup compromise. Microsoft names no actor cluster for this activity. Todyl's counts cover only organisations that send logs to it and are a floor.
confidence: medium
references:
  - 2026-10-22/artex-storm-0940-agentic-llm-pentest-spraying-oauth-abuse
  - 2026-10-18/connectwise-cloud-backup-skykick-m365-app-credential-abuse
  - 2026-10-30/vapor-panda-artex-agentic-campaign-foreign-ministries
  - 2026-10-23/m365-token-spray-replay-rogue-entra-devices-mfa-wipe
  - 2026-10-26/jpcert-nict-app-to-backend-api-attacks-ai-scanning-japan
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "In every Entra tenant you run or manage for others, list the app registrations that hold client secrets, starting with multitenant, delegated-admin (GDAP) and Partner Center apps, security-tool integration apps and Azure DevOps service connections, and search the service-principal and non-interactive sign-in logs for the invalid-secret or expired-secret errors AADSTS7000215 and AADSTS7000222 followed by a success for the same app; on any hit remove all client secrets, certificates and federated credentials on that app, including ones you did not add, disable its service principal if needed and rotate everything stored in any Key Vault it could read, because issued tokens stay valid until they expire."
updates:
  - at: "2026-11-08T13:59:00Z"
    run_id: 2026-11-08T1309Z-audit
    type: update
    summary: >
      Todyl updated its investigation on 2026-11-06: it now assesses its operator as an automated agentic
      credential crawler, accepts Microsoft's ARTEX naming and GitHub access path, and names AI agents
      writing secrets in cleartext on the command line as the largest source of exposed credentials it has
      seen.
    fields: [body, evidence, sourcing_note, summary]
migrated_from: null
---

Microsoft reports that since August 2026 threat actors have used the agentic offensive framework ARTEX to submit large volumes of queries to public GitHub for secrets ([Microsoft Threat Intelligence, 2026-11-05](https://www.microsoft.com/en-us/security/blog/2026/11/05/threat-actors-use-agentic-ai-tooling-to-find-and-abuse-exposed-secrets/)). As early as 2026-10-28 it saw successful service-principal sign-ins from two IP addresses, one a Tor exit node that may carry unrelated activity, across dozens of applications in several tenants, including a vendor-owned multitenant application whose credential was compromised at the source and used to reach multiple downstream tenants ([Microsoft Threat Intelligence, 2026-11-05](https://www.microsoft.com/en-us/security/blog/2026/11/05/threat-actors-use-agentic-ai-tooling-to-find-and-abuse-exposed-secrets/)). Microsoft states that a similar campaign involving the same addresses was also reported by Todyl ([Microsoft Threat Intelligence, 2026-11-05](https://www.microsoft.com/en-us/security/blog/2026/11/05/threat-actors-use-agentic-ai-tooling-to-find-and-abuse-exposed-secrets/)).

Todyl, from its managed-detection telemetry, describes one operator who since 2026-11-01 has signed in to MSPs' Microsoft 365 and Azure environments as their own applications with stolen credentials that are still valid: about 45 app registrations at roughly 18 organisations were targeted, more than 33 authenticated, and 27 organisations were reached, among them the MSPs' downstream clients in government ([Todyl, 2026-11-03](https://www.todyl.com/blog/stolen-app-credentials-real-access-an-actor-is-signing-into-entra-id-and-azure-devops-as-your-workloads)). For nearly every credential the operator requests an Azure Resource Manager token, then a Key Vault token, and within minutes applications that had never been used start authenticating; MSP multitenant and delegated-admin apps and Partner Center tokens reach client tenants, one app sweeping 15 client tenants in about 10-second loops ([Todyl, 2026-11-03](https://www.todyl.com/blog/stolen-app-credentials-real-access-an-actor-is-signing-into-entra-id-and-azure-devops-as-your-workloads)). Todyl says no Microsoft vulnerability is involved and that it saw no persistence ([Todyl, 2026-11-03](https://www.todyl.com/blog/stolen-app-credentials-real-access-an-actor-is-signing-into-entra-id-and-azure-devops-as-your-workloads)). Its update of 2026-11-06 assesses the operator as an automated agentic credential crawler and the likely credential source as public repositories or web apps, citing credential scanning from the actor's address before the first sign-in, no sign of earlier compromise and custom-built affected apps ([Todyl, 2026-11-03](https://www.todyl.com/blog/stolen-app-credentials-real-access-an-actor-is-signing-into-entra-id-and-azure-devops-as-your-workloads)). After its detections fired on 2026-11-03 the operator switched to spoofed browser user agents and replayed users' refresh tokens, all blocked by Conditional Access ([Todyl, 2026-11-03](https://www.todyl.com/blog/stolen-app-credentials-real-access-an-actor-is-signing-into-entra-id-and-azure-devops-as-your-workloads)).

**Exposure:** any Entra tenant, an MSP's or a customer's, that holds app registrations with client secrets, above all multitenant, delegated-admin and Partner Center applications and Azure DevOps service connections, security-tool integration apps among those abused ([Todyl, 2026-11-03](https://www.todyl.com/blog/stolen-app-credentials-real-access-an-actor-is-signing-into-entra-id-and-azure-devops-as-your-workloads)); Conditional Access for workload identities needs the Workload ID Premium licence and covers only single-tenant apps ([Microsoft Threat Intelligence, 2026-11-05](https://www.microsoft.com/en-us/security/blog/2026/11/05/threat-actors-use-agentic-ai-tooling-to-find-and-abuse-exposed-secrets/)).

**Detection:** in Entra service-principal and non-interactive sign-in logs, an invalid-secret or expired-secret error for an application followed by a success, one address authenticating as service principals in several unrelated tenants within 24 hours, an Azure Resource Manager token followed at once by a Key Vault token and then by previously unused apps authenticating, and failed service-principal sign-ins from hosting space that never succeed, which success-only logic misses ([Todyl, 2026-11-03](https://www.todyl.com/blog/stolen-app-credentials-real-access-an-actor-is-signing-into-entra-id-and-azure-devops-as-your-workloads)). In Azure DevOps auditing, personal access token creation and first use, federated service connections and pipeline edits ([Microsoft Threat Intelligence, 2026-11-05](https://www.microsoft.com/en-us/security/blog/2026/11/05/threat-actors-use-agentic-ai-tooling-to-find-and-abuse-exposed-secrets/)).

**Triage:** the invalid-secret and expired-secret errors alone only show that someone holds an old or wrong credential for the app; Microsoft treats a failure followed by a success as the urgent case ([Microsoft Threat Intelligence, 2026-11-05](https://www.microsoft.com/en-us/security/blog/2026/11/05/threat-actors-use-agentic-ai-tooling-to-find-and-abuse-exposed-secrets/)).

**Defender takeaway:** inventory the client secrets on app registrations and hunt the sign-in pattern above in every tenant you run or manage, MSP-managed communal tenants included; on an affected app remove every client secret, certificate and federated credential, including those the actor added, and rotate what any Key Vault it could read holds, because tokens already issued stay valid until expiry ([Microsoft Threat Intelligence, 2026-11-05](https://www.microsoft.com/en-us/security/blog/2026/11/05/threat-actors-use-agentic-ai-tooling-to-find-and-abuse-exposed-secrets/)).

## Update — 2026-11-08T13:59:00Z

Todyl updated its post on 2026-11-06 after Microsoft's research of 2026-11-05: it says Microsoft's findings match its assessment that the activity is an automated, agentic credential crawler, and it now names public repositories or web apps as the likely source of the stolen secrets, citing credential scanning from the actor's address before the first sign-in, no sign of earlier compromise and custom-built affected apps ([Todyl, 2026-11-03](https://www.todyl.com/blog/stolen-app-credentials-real-access-an-actor-is-signing-into-entra-id-and-azure-devops-as-your-workloads)). It quotes Microsoft for the GitHub access path and the ARTEX name, and adds that the operator replays harvested material within minutes, in one case signing in as a connector's app about 2.5 minutes after downloading its archive ([Todyl, 2026-11-03](https://www.todyl.com/blog/stolen-app-credentials-real-access-an-actor-is-signing-into-entra-id-and-azure-devops-as-your-workloads)). Todyl says AI agents using or posting credentials in cleartext on the command line have been the largest contributor to the exposed credentials it has observed, and advises hunting service-principal and non-interactive sign-in logs back to at least 2026-10-28 ([Todyl, 2026-11-03](https://www.todyl.com/blog/stolen-app-credentials-real-access-an-actor-is-signing-into-entra-id-and-azure-devops-as-your-workloads)).
