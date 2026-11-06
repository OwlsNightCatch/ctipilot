---
title: Hackers Use Stolen Microsoft Entra ID and Azure DevOps Credentials to Access 27 Organizations
author: Guru Baran
url: https://cybersecuritynews.com/stolen-entra-id-and-azure-credentials/
hostname: cybersecuritynews.com
description: Hackers are abusing stolen Microsoft Entra ID application credentials and Azure DevOps identities to access Microsoft 365 and Azure environments, reaching at least 27 organizations.
sitename: Cyber Security News
date: "2026-11-04"
categories: ['Cyber Security']
fingerprint: "3e5132921fac4045"
---
Hackers are abusing stolen Microsoft Entra ID application credentials and Azure DevOps identities to access Microsoft 365 and Azure environments, reaching at least 27 organizations.

Todyl’s latest investigation update describes an ongoing campaign targeting managed service providers (MSPs) and their customers since November 1, 2026.

The operator targeted about 45 app registrations across roughly 18 organizations, with more than 33 authenticating successfully. Downstream access expanded the victim count to government, energy, agriculture, transportation, construction, legal, education, and nonprofit organizations. These figures cover only environments sending logs to Todyl, so the actual reach could be wider.

Investigators recorded searches across about 25 tenants, downloads of 81 files, and access to approximately 2,279 mailbox items. The latest reported attempt, at 21:31 UTC on November 3, was blocked. No Microsoft vulnerability was involved. Instead, the attacker used valid credentials to act as trusted applications.

This distinction matters because application identities operate without a user signing in. Their existing permissions can allow access without an MFA prompt, while user-focused Conditional Access policies do not govern app-only authentication. Cybersecurity News previously covered how [stolen credentials and excessive permissions](https://cybersecuritynews.com/stolen-credentials-are-only-half-the-breach-how-excessive-permissions-turn-logins-into-disasters/) can turn limited access into broader exposure.

The attacker also used an Azure DevOps federated workload identity and replayed user session tokens. How the attacker stole the original credentials remains unknown. Todyl found no evidence that a vendor platform was compromised, even though credentials belonging to trusted security integrations were among those abused.

## **Attack Moves Through Cloud Environments**

According to [Todyl’s investigation](https://www.todyl.com/blog/stolen-app-credentials-real-access-an-actor-is-signing-into-entra-id-and-azure-devops-as-your-workloads), the operator typically requests an Azure Resource Manager token, followed by tokens for Key Vault, Microsoft Graph, and Storage. This sequence gives investigators a useful pattern to hunt, particularly when previously unused applications begin authenticating shortly afterward.

The latest update describes 29 wildcard Microsoft Graph searches followed by SharePoint downloads at roughly one file per second. Collected material included password lists, private keys, VPN profiles, backup credentials, and remote access settings. Such files could enable further attacks beyond Microsoft 365, where Todyl’s cloud logs provide limited visibility.

MSP relationships increased the damage. One multi-tenant application reached 15 customer tenants in repeated loops of about 10 seconds. The broader risk resembles earlier reporting on [compromised accounts reaching Azure DevOps and cloud resources](https://cybersecuritynews.com/hackers-turn-one-compromised-account/), although that case involved a different intrusion.

Scripted clients accounted for 95% of observed sign-ins, with bursts reaching 24 attempts in 10 seconds. However, long pauses and changing browser signatures suggest human control.

Todyl describes automation, not confirmed self-spreading malware. AI involvement remains a low-confidence possibility, and the operator has not been identified.

Defenders should review service-principal sign-ins and non-interactive user logs for 199.19.77.84, the confirmed source address. Failed attempts matter alongside successful ones. Todyl recommends blocking the exact address rather than its entire hosting network, where unrelated activity exists.

Response should include disabling affected applications where needed, removing compromised credentials, revoking user sessions, and rotating secrets in accessible vaults and documents.

Workload-specific Conditional Access has licensing and coverage limits, so user policies alone are insufficient. MSPs should also review delegated customer access, preserve audit logs, and notify affected clients.

**Give your SOC the alert context to stops incidents quickly.Integrate Threat Intel from 16K SOCs**.
