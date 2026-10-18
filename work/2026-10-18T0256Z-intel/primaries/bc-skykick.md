---
title: Hackers breach Microsoft 365 tenants via ConnectWise supply-chain attack
author: Ionut Ilascu
url: https://www.bleepingcomputer.com/news/security/hackers-breach-microsoft-365-tenants-via-connectwise-supply-chain-attack/
hostname: bleepingcomputer.com
description: ConnectWise has shut down customer access to its Cloud Backup service (formerly SkyKick Cloud Backup) after hackers accessed application identities and compromised Microsoft 365 tenants.
sitename: BleepingComputer
date: "2026-10-17"
tags: ['computers, windows, linux, mac, support, tech support, spyware, malware, virus, security,virus removal, malware removal, computer help, technical support']
fingerprint: "26410284549e08cf"
---
ConnectWise has shut down customer access to its Cloud Backup service (formerly SkyKick Cloud Backup) after hackers accessed application identities and compromised Microsoft 365 tenants.

Reports of the malicious activity began emerging on Friday, with administrators observing unauthorized access to client data in Microsoft 365 tenants due to a potential “SkyKick/CW breach.”

Later on the same day, managed cybersecurity and threat detection platform Huntress confirmed the worries, saying that it had identified at least 162 compromised tenants in its environment.

In a post today, Microsoft also confirmed malicious activity involving ConnectWise’s Cloud Backup service, saying it identified unauthorized authentication attempts from an IP address on October 15.

ConnectWise’s cloud backup solutions provide backup and recovery services that help managed service providers (MSPs) and IT teams protect and restore customer data, such as emails and files, in cloud environments including Microsoft 365 and Google Workspace.

For Microsoft 365 backups, the service relies on permissions granted through Microsoft Entra ID. An application identity known as a “service principal” represents the software in a customer’s tenant and enables it to access resources according to the permissions granted.

### Microsoft 365 tenant breaches

In a [security advisory](https://www.connectwise.com/company/trust/advisories), ConnectWise said that it “recently identified unauthorized access to application identities within the ConnectWise Cloud Backup environment” and shut down application access for its partners and clients.

“We have no indicators to date that Cloud Backup partner backup data has been compromised. The existing cloud backup archive is not impacted by this service interruption and will be accessible once services are restored,” [ConnectWise says](https://www.connectwise.com/company/trust/advisories).

However, the company has launched an investigation and is engaged in remediation efforts.

Based on reports from Microsoft, Huntress, and administrators, the malicious activity started at least on October 15 from a single IP address: *144.172.64\[.\]128*.

One [user on Reddit said](https://www.reddit.com/r/msp/comments/1x7gw61/comment/ph55a0f/) that they received a notification from the Microsoft Privileged Identity Management (PIM) service on October 15 alerting of a SkyKick service principal assigning itself the role of Exchange Administrator, despite not using the app in years.

Nevertheless, some of the reported IDs for the offensive SkyKick match those provided by Huntress, Microsoft, and Todyl - a cybersecurity platform primarily for MSPs and IT professionals.

According to Todyl researchers, the attacker authenticated directly to Microsoft 365 as the backup application using its secret, gaining the permissions customers had already granted it.

The sign-in requests were performed by an automated script, and since they did not involve a user login, protections such as multi-factor authentication (MFA) were ineffective.

“Because the application already held broad, previously granted permissions in each tenant, those sign-ins gave the attacker the technical ability to read and write mail and attachments, OneDrive and SharePoint files, and Teams chats,” [Todyl said](https://www.todyl.com/blog/investigation-unauthorized-access-through-the-connectwise-cloud-backup-microsoft-365-app).

In the analyzed intrusions on nine tenants, Todyl researchers identified only sign-in activity and did not find evidence that the threat actor “created accounts, added permissions, changed passwords, or established persistence in any tenant through the backup app.”

### Reconnaissance and persistence attempts

However, [Huntress saw](https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access) on nearly 50 tenants it monitors that service principals for “ConnectWise’s Cloud Management apps (Exchange Online, Microsoft Teams, and Microsoft Graph) assigned themselves directory roles, mostly Exchange Administrator.”

In one tenant, Huntress researchers also observed that the attacker established persistence, the operation taking around five minutes.

During the activity, Cloud Management - MS Teams (*24205314-2b89-4e07-a2a4-579e898a5640*) granted itself a Global Administrator role and added credentials to an MSP management tool and to Huntress’s own application.

Microsoft also [observed persistence activity](https://x.com/msftsecintel/status/2111358888125878426?s=12&t=tDVP3ULf1Ou5szxCQAKqjA) via a backdoor after successful service principal authentication, followed by “Microsoft Graph API reconnaissance and attempts to add additional credentials.”

It should be noted that all three cybersecurity companies tracked the malicious company to the same *144.172.64\[.\]128* IP address.

Microsoft Threat Intelligence characterized the incident as an active supply-chain attack, assessing that the attacker likely abused existing permissions, including Directory.ReadWrite.All.

### Indicators and tenant checks

Huntress identified the legitimate Cloud Backup application ID *506e08f9-6e9a-4da4-942b-a099a03644ae* used in the attacks. Its investigation also linked the attacker IP address to scripted sign-in attempts on October 13 and 14, with the user agent *curl/7.88.1*.

Based on current evidence, there are at least three user agents linked to the malicious Cloud Backup service activity: *python-urllib/3.12*, *python-requests/2.31*, *python-requests/2.34.2*.

ConnectWise recommends that administrators check the service principal sign-ins in Entra, filter by the Cloud Backup application ID, and examine unexpected source addresses.

Microsoft also recommends reviewing application credential changes, OAuth grants, and related Graph activity.

Huntress advises administrators to disable the implicated ConnectWise applications, as well as check application credentials for unauthorized additions and review other Cloud Management integrations.

The company notes that older tenants may list Cloud Management apps under ‘SkyKick Cloud Manager’.

The company provides an extended list of application IDs for administrators to look for:

- *ConnectWise Cloud Backup (506e08f9-6e9a-4da4-942b-a099a03644ae)*
- *ConnectWise Cloud Management (2399d300-6fca-4e6a-a686-399fefe75b83)*
- *ConnectWise Cloud Management - MS Teams (24205314-2b89-4e07-a2a4-579e898a5640)*
- *ConnectWise Cloud Management - Exchange Online (b78f6a77-d4e5-46fb-87e5-d1648bd02519)*
- *ConnectWise Cloud Management - MS Graph (0de14c77-b9b0-4137-9360-34878a929827)*
- *ConnectWise Cloud Management - Partner Center (412dcf96-176d-4b3a-a1b0-4981ad66971e)*
- *ConnectWise Cloud Management - SharePoint Online (b2b55f5b-7758-4719-8d8f-88ae172e6bdb)*

The vendor’s shutdown does not remove credentials already planted in customer tenants. Huntress says that admins should review secrets and certificates across all applications for unauthorized additions since October 13 and removing those entries.

Todyl warns that disabling an application stops new tokens from being issued, but existing tokens remain valid until they expire, and revoking user sessions does not end application-based access.

ConnectWise announced the backup service interruption at 05:01 UTC on October 17 but did not provide a timeline for restoring the connection.

The company did not report any evidence that stored backups were compromised and said existing archives would be accessible when reservices are restored.

At the time of publishing the victim count and the extent of data theft remains unclear, as well as the method the attacker used to obtain vendor credentials.

## [Once attackers have valid credentials, only 37% of their actions are blocked](https://hubs.li/Q04sB3fb0)

Overall prevention scores can hide what happens after initial access. Once attackers are using valid credentials, prevention drops sharply.

The Blue Report 2026 measures defenses technique by technique across 338 million simulations run in customer production environments.

[Get the report](https://hubs.li/Q04sB3fb0)

## Comments

## DQ52 - 11 hours ago

We just need more AI, more outsourcing, more cloud services and more software as a service, that will fix everything.

## ThomasMann - 4 hours ago
