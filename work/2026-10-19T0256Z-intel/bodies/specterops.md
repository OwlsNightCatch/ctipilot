---
title: "ConnectWise SkyKick Breach: How to Check Your Microsoft 365 Tenant"
author: Justin Kohler; Duane Michael
url: https://specterops.io/blog/2026/10/17/connectwise-skykick-breach-microsoft-365/
hostname: specterops.io
description: The ConnectWise SkyKick breach exposed Microsoft 365 tenants. Check yours and map vendor app access with AzureHound and BloodHound.
sitename: SpecterOps
date: "2026-10-17"
categories: ['Blog', 'Research & Tradecraft', 'BloodHound']
fingerprint: ac6b18d7ceb620cd
---
# ConnectWise SkyKick Breach: How to Check Your Microsoft 365 Tenant

*Last updated October 17, 2026*

An attacker used a compromised credential belonging to ConnectWise Cloud Backup (formerly SkyKick) to sign in to customers’ Microsoft 365 tenants. The credential belongs to the application itself, so the attacker inherited the permissions granted to it. Here’s what’s known so far and what to check in your own tenant.

*This blog will be updated and cross-linked as more information becomes available.*

## tl;dr

- On October 15, an attacker used the ConnectWise Cloud Backup application’s credential to get Microsoft Graph tokens in customer tenants.

- Huntress has confirmed unauthorized sign-ins in 162 tenants. Any tenant with the app installed is exposed.

- Disable the affected ConnectWise applications now, and review every application in your tenant for credentials added since October 13.

## What happened in the ConnectWise SkyKick breach?

On October 15, 2026, between 06:13 and 08:34 UTC, the ConnectWise Cloud Backup application signed in to customer tenants from 144.172.64\[.\]128, a hosting provider address. According to Huntress, which first [broke the news](https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access) of the breach, the attacker moved through tenants a few seconds apart, which points to a script working from a target list.

According to [The Hacker News](https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access), Microsoft is calling this an active supply chain attack, with the attackers likely abusing permissions customers had already granted the app, including Directory.ReadWrite.All.

As of the publication of this blog, ConnectWise has shut off Cloud Backup application access while it investigates. The company says it has found no evidence that partner backup data was compromised. How the attacker obtained the credential has not been disclosed.

## Why doesn’t MFA stop this attack?

MFA doesn’t apply because this is an application sign-in, so no user, device, or MFA prompt is involved. Backup tools need broad access to read and restore data. Anyone holding the app’s credential can reach the same mailboxes, OneDrive and SharePoint files, Teams data, and directory information the backup service can.

In one tenant, Huntress also saw a second ConnectWise application grant itself Global Administrator and add new client secrets to two other trusted applications. That gives an attacker a way back in even after the original credential is reset.

## Which known ConnectWise applications are affected?

Based on recommendations from Huntress and others, SpecterOps built and is actively running cypher queries (below) for the following known ConnectWise applications. The queries hunt for applications owned by the ConnectWise tenant (ID: 3f9cd7a0-127a-4ed4-bf06-2f830d5616b7). Older tenants may list them under SkyKick names. ant (ID: 3f9cd7a0-127a-4ed4-bf06-2f830d5616b7). Older tenants may list them under SkyKick names.

| **Application** | **Application ID** | 
| ConnectWise Cloud Backup | 506e08f9-6e9a-4da4-942b-a099a03644ae | 
| ConnectWise Cloud Management | 2399d300-6fca-4e6a-a686-399fefe75b83 | 
| Cloud Management – MS Teams | 24205314-2b89-4e07-a2a4-579e898a5640 | 
| Cloud Management – Exchange Online | b78f6a77-d4e5-46fb-87e5-d1648bd02519 | 
| Cloud Management – MS Graph | 0de14c77-b9b0-4137-9360-34878a929827 | 
| Cloud Management – Partner Center | 412dcf96-176d-4b3a-a1b0-4981ad66971e | 
| Cloud Management – SharePoint Online | b2b55f5b-7758-4719-8d8f-88ae172e6bdb | 

## How do I check if my Microsoft 365 tenant was affected?

1. **Immediately disable** application 506e08f9-6e9a-4da4-942b-a099a03644ae in the Entra admin center. Keep the apps disabled until ConnectWise confirms that all credentials have been reset. Tokens that were already issued can stay valid for up to 90 minutes after you disable an app.

1. **Download the** [**open-source version of AzureHound**](https://github.com/SpecterOps/AzureHound) and run the collector.

1. **Review your sign-in logs** for service principal authentication tied to the application IDs listed above. Pay special attention to activity from the source IP 144.172.64\[.\]128.

1. **Revoke unneeded application consents.** If you don’t actively use SkyKick or ConnectWise Cloud Backup, remove their application consents from your tenant.

## Use Bloodhound to map impact of ConnectWise applications

BloodHound users may run the below cypher queries to identify potential impact to their environments.

*Identify outbound control of ConnectWise application*

MATCH p=(sp:AZServicePrincipal)-\[r\]->(target) 

WHERE toLower(sp.appownerorganizationid) = ‘3f9cd7a0-127a-4ed4-bf06-2f830d5616b7’ 

RETURN p

*Identify paths from the impacted service principal to Tier Zero.*

MATCH p=shortestPath((sp:AZServicePrincipal)-\[\*1..6\]->(t)) 

WHERE toLower(sp.appownerorganizationid) = ‘3f9cd7a0-127a-4ed4-bf06-2f830d5616b7’ 

AND t.system\_tags CONTAINS ‘admin\_tier\_0’

## Map your vendor apps before the next breach

This won’t be the last time a trusted vendor’s credential is compromised. Every third-party app with consent in your tenant is a potential attack path, and most organizations can’t easily say which apps hold which permissions. The open source AzureHound gives you that map: every service principal, every permission, and every path from those apps to your most sensitive assets.

[Download AzureHound on GitHub →](https://github.com/SpecterOps/AzureHound)

Stay tuned for additional updates from our threat research as they become available.
