---
title: ConnectWise (SkyKick) Vendor Credentials Abused in M365 Attacks | Huntress
author: Jonathan Semon
url: https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access
hostname: huntress.com
description: ConnectWise (SkyKick) vendor credentials are being abused to access Microsoft 365 tenants. Disable the apps now and check your logs here.
sitename: Huntress
date: "2026-10-16"
fingerprint: ac6112974e9642ad
---
*Acknowledgements: Special thanks to Rich Mozeleski, Andrew Brandt, Andrew Kaiser, Dave Kleinatland, and Matt Kiely for their contributions to this investigation and writeup.*

*Update: 10/19/26 @ 1:30 PM ET*

This update covers three topics: additional IP addresses circulating in connection with this activity, what we have learned about the attacker's behavior after gaining access, and the art of precision strikes against adversaries.

**Additional IP addresses**: As more addresses have been shared across the community, we reviewed each against our telemetry. In a review of application sign-ins across more than 10,000 tenants with ConnectWise applications (where we can see those logs), `144.172.64[.]128` and Microsoft-internal ranges are the only addresses that produced application sign-in activity. We did not see application sign-in activity from any of the other addresses listed below, all of which are in the same provider range as `144.172.64[.]128` (AS14956, RouterHosting). We did see password spray and failed login attempts from some of them. At this time, we do not believe those attempts are related to the application sign-ins described in this post.

IPs and characterizations below:

| **IP** | **Description** | 
|---|---|
| `144.172.64[.]128` | Application sign-ins with a vendor credential (primary vector) | 
| `144.172.64[.]99` | Failed user password spray, concentrated (October 10 to 14) | 
| `144.172.64[.]60` | A few failed user logins (October 18) | 
| `144.172.94[.]243` | Broad failed login spray, ongoing, many organizations | 

**What happened after access was gained:** Since our last update, Huntress has identified a second tenant with post-compromise activity. Huntress was not deployed on this tenant originally, but we saw service principal sign-in attempts **from** that tenant to Huntress-protected tenants (from the `*.128` IP address). Working proactively with a partner, we were able to get Huntress deployed to this second tenant in order to collect additional telemetry.

In the two tenants with this activity, the post-compromise behavior was fast, scripted, and notably indiscriminate. In both tenants, the post-compromise activities took place within two minutes of each other around 03:45 UTC on October 15. The procedure was the same each time: the application granted itself Global Administrator, then planted a new secret on a small number of other applications in the tenant to keep a foothold. The choice of which applications to backdoor appeared to be random in the two tenants we reviewed. Across the two compromised tenants, the identical grant flow selected two completely different sets of applications. Notably, one application existed in BOTH tenants but was chosen for secret planting in only one of them. In one tenant, the applications that received planted secrets were among the least privileged in the environment, while far more powerful applications sat untouched. The only consistent criteria we can point to is structural: credentials were planted in applications that are registered inside the affected tenant, without regard to what those applications can actually do.

Just as important is what we did not see: The access may have been used for Microsoft Graph directory reads, which leave no audit record. In the two tenants we reviewed, we also found no evidence of mailbox or file manipulation, or user or policy changes.

**Our surgical response:** You might be wondering why our response did not include mass disabling the ConnectWise/SkyKick apps across ***every*** tenant. Our approach to containment is deliberate, surgical, and evidence-based, and this incident called for a scalpel, not a hammer. We prioritized the tenants with confirmed successful unauthorized sign-ins, and our guidance for everyone else has been to disable the affected apps and check their logs.

When our investigation kicked off, we quickly established a clear picture of the attack window. The malicious application sign-ins were tightly bunched across the morning of October 15 UTC, and the last confirmed successful sign-in we observed with this credential was at 08:44 UTC on October 15. After that, we saw only failed attempts in the tenants where we can see sign-in logs. With evidence in hand that there was no current or repeated activity (in the tenants where we can see sign-in logs), it simply didn't make sense to create a larger-than-necessary blast radius.

This judgment call allowed our experts and agents to focus closely on environments with confirmed unauthorized sign-ins, share what we found with industry partners, and publish guidance for the community.

We believe it's these surgical moments our partners most appreciate and count on when *it* hits the fan, especially when the wrong decision can disrupt working systems and business productivity as collateral damage.

*Update: 10/17/26 @ 5:15 PM ET*

\*\*As of October 17 at 5:15 PM ET, ConnectWise has communicated that they have disabled relevant apps.

During further investigations, Huntress identified a second, targeted wave of attempts from `144.172.64[.]128` on October 15, unsuccessfully targeting a narrow scope of 16 Huntress-protected tenants. These tenants are in the policy, national security, trade, and critical mineral sectors. Unlike the first wave of activity outlined in our initial blog below, most of these tenants do not rely on any ConnectWise products. In tenants without the relevant ConnectWise service principal, the attempts failed because the application was not present.

For the new target set, the first sweep targeted Graph tokens from the SkyKick app and occurred on October 15 between 09:25:04 and 12:35:50 UTC. Several tenants were hit in bursts during that timeframe. The second sweep hit the same tenants on the same date, between 13:54:39 and 14:20:24 UTC. This sweep appeared to be manual and targeted Exchange Online, SharePoint Online, Teams, Azure Resource Manager, Entra, and the Office 365 Management APIs.

In addition to the activity above:

- Huntress has identified almost 1,000 Entra tenants with sign-in activity from the IP address associated with the unauthorized activity (`144.172.64[.]128`). Over 300 of those succeeded.
- While many of these sign-ins were successful, the absence of a service principal in some tenants prevented the threat actor from successfully gaining access to those tenants.
- Huntress have also received external reports and tips from outside our fleet describing similar activity in other tenants, including what appears to be hands-on activity. We have not independently verified these reports.

As mentioned in our initial blog, on October 15 the threat actor appears to have used access from the ConnectWise app family to add a credential to a Huntress application in one customer tenant, and to add a credential to another application in the same tenant. The credential on the Huntress application was used to sign in seven times in quick succession. On October 16, Huntress identified and removed the unauthorized credential on our application. We have not seen the application make changes in that tenant's audit log, but Microsoft does not log everything an application reads, so we cannot rule out access to data the application can read there. Huntress is actively reviewing credential activity associated with our applications across partner environments, validating expected access, and investigating suspicious changes.

**Notably, the access that led to the credential being added to Huntress and another app came from private Azure IPv6 space, not the IP address associated with the previous sign-ins (**`144.172.64[.]128`**). At this time, we advise all ConnectWise users to audit all service principal sign-ins to the apps identified below beginning around 01:00 UTC on October 15 to 02:00 UTC on October 16.**

We're strengthening our safeguards with additional monitoring and preventative controls to help detect and respond to unusual activity even faster. We've enabled App Instance Property Lock across all Huntress applications and are enhancing our fleet health and monitoring capabilities to detect modification attempts.

Huntress is continuing to investigate this incident and will update this blog with any further breaking updates.

**Update: 10/17/26 @ 10:30 AM ET**

After spending the night combing through Azure logs, we have high-confidence that the threat actor has also abused the following M365 applications:

• **ConnectWise Cloud Management - Exchange Online** (`b78f6a77-d4e5-46fb-87e5-d1648bd02519`).

• **ConnectWise Cloud Management - MS Teams** (`24205314-2b89-4e07-a2a4-579e898a5640`).

• **ConnectWise Cloud Management - SharePoint Online** (`b2b55f5b-7758-4719-8d8f-88ae172e6bdb`).

At the moment, it does not look like these apps have been disabled by ConnectWise.

When it comes to early exploitation and post-exploitation behaviors, we’ve observed what might be an affinity towards alphabetical targeting (our most interesting victims start with “A”). Although all tenants should be scrutinized, this pattern is worth sharing for prioritization.

If you’ve been impacted with noteworthy tradecraft relating to this SkyKick incident, our research team would love to learn more so we take actions to protect the community. Hit us up at [\[email protected\]](https://www.huntress.com/cdn-cgi/l/email-protection#1c6f696c6c736e685c746972686e796f6f327f7371).

## Background

ConnectWise Cloud Backup (Formerly SkyKick) is a cloud-based backup and recovery service built for managed service providers (MSPs) to protect their clients' Microsoft 365 or Google Workspace data. To do that job, the app is granted broad access to mailboxes, OneDrive, SharePoint, Teams, and directory data in every tenant it is installed in.

On October 15, the application's identity signed in to customer Microsoft 365 tenants from `144.172.64[.]128`, a hosting provider address, and received Microsoft Graph access tokens. This is not how the app normally behaves: legitimate traffic comes from Azure private IP space. As of 19:00 UTC on October 16, Huntress has confirmed unauthorized sign-ins in 162 tenants.

The authentication itself is certain: It comes from Microsoft's own sign-in logs in each tenant. The credential type was a client assertion, which means the credential lives in the vendor's own tenant. Nothing a customer did in their environment could have produced it.

ConnectWise has [<u>acknowledged the incident</u>](https://www.connectwise.com/company/trust/advisories) on its website and confirmed the IP is associated with unauthorized activity. Todyl has also [<u>reported on this incident</u>](https://www.todyl.com/blog/investigation-unauthorized-access-through-the-connectwise-cloud-backup-microsoft-365-app).

*Figure 1: What the login attempt looks like to an IT admin in the Microsoft Entra Admin Center*

Huntress is continuing to monitor this situation closely alongside our security partners; for all updates, please continue to check this blog post.

## What Happened

- **What do we know?** The app's credential is in hostile hands. It was used to obtain Microsoft Graph tokens in customer tenants from `144.172.64[.]128` on October 15, between 06:13 and 08:34 UTC. The actor moved through tenants in sorted GUID order, a few seconds apart, which points to a script working from a target list.
- **Who is affected?** Any organization with the app installed. The credential works against every tenant the app is consented in, so the actor is not limited to the tenants we have confirmed so far.
- **How does it work?** The attacker authenticates to the app using their own tooling, the same way the backup service does, and gets tokens with the app's existing permissions.
- **What are the potential repercussions?** Because backup and restore both need to read and write data, those permissions are broad. An attacker holding those tokens can read the same mailboxes, files, and directory data the backup service can.

### Huntress observations

Here is the timeline of what Huntress has seen from the same infrastructure:

- **October 13 to 14**: Password spraying against four law firm tenants from `144.172.64[.]128`. Scripted OAuth2 token requests (User-Agent `curl/7.88.1`) from datacenter infrastructure. Two accounts were locked out by smart lockout. We saw no successful user sign-ins from this IP in Huntress telemetry.
- **October 15, from 01:58 UTC:** In roughly 50 tenants monitored by Huntress, service principals for ConnectWise's Cloud Management apps (Exchange Online, Microsoft Teams, and Microsoft Graph) assigned themselves *directory* roles, mostly Exchange Administrator. The User-Agent on these events (`kiota-dotnet`) is the one ConnectWise's own apps use, which points to vendor automation, but we have not confirmed that with ConnectWise.
- **October 15, 03:44 to 03:49 UTC, one customer tenant:** The ConnectWise Cloud Management app for Microsoft Teams (application ID `24205314-2b89-4e07-a2a4-579e898a5640`) added itself to the Global Administrator role, then ran a Python script (User-Agent `Python-urllib/3.12`) that modified two other applications in the tenant: an MSP management application, and Huntress's own application (Huntress Security Platform), adding new client secrets to both. A followup attempt to add a certificate failed. The new secrets were set to expire in 2028.
- **October 15, 06:13 to 08:34 UTC:** The app authenticated from `144.172.64[.]128` in 17 of the first 290\~ tenants Huntress checked, across 17 different partner accounts.
- **Between October 13 and 14:** The same address also made a scripted sign-in attempted using client application IDs belonging to other tools.

In the tenant where we saw persistence, the entire sequence took about five minutes. The ConnectWise Cloud Management app for Microsoft Teams added itself to Global Administrator at 03:44 UTC and again at 03:48. In the same window it made nine changes to two other applications, an MSP management application and Huntress's own application. Six of the changes succeeded and three failed. One failure was a certificate credential that Microsoft rejected with a thumbprint mismatch, and the client secrets that were added afterward succeeded.

A client secret and a certificate are two ways for an application to prove its identity to Entra, and either one gives the holder the same access: sign in as that application, from anywhere, using the permissions already granted to it. App-only sign-ins involve no user, no device, and no MFA prompt. The person who creates a secret sees its value at creation, so the attacker holds working credentials for both applications until someone removes them. Adding credentials to an existing application is a known persistence technique (MITRE ATT&CK T1098.001, [<u>Account Manipulation: Additional Cloud Credentials</u>](https://attack.mitre.org/techniques/T1098/001/)).

The two applications that received new secrets are trusted, privileged tools. Adding a credential to an MSP management application can extend access beyond the one tenant, because those applications are often consented into the MSP's customers' tenants. A credential on a security tool's application gives the holder whatever that tool is permitted to do.

The Global Administrator change and the credential additions happened about two and a half hours before the first app authentications from `144.172.64[.]128` at 06:13 UTC. We have no source address for the earlier activity, so we have not tied the two phases to the same operator. User-Agents helped us distinguish vendor activity from attacker activity. The ConnectWise Cloud Management and Partner Center applications we reviewed make their Graph calls with a .NET SDK User-Agent (`kiota-dotnet`). The application changes in the one tenant came from a Python User-Agent, and the password spray used `curl/7.88.1`. None of these is unique to this actor, and Python and curl are common in ordinary administration, so **the combination of actor, operation, and User-Agent is the useful signal**, not any single one.

Microsoft's audit log records role assignments and application changes along with the acting application, but for app-only actions it carries no source IP, and it does not record the details of the credential that was added or what an application read through Microsoft Graph. Confirming exactly what was added in a tenant takes the Entra audit log or a Graph query for that tenant, which is why we ask partners to review credentials directly.

### What we have not confirmed

- **Impact.** In the one tenant audit log we reviewed in detail, the actor shows no mail or file access. That does not mean no data was taken. Directory reads through Microsoft Graph leave no audit trail, so "tokens issued, nothing visible taken" is the current state.
- **Secondary app exposure.** ConnectWise has multiple applications with very high-level permissions. In one customer tenant, Huntress confirmed that a second ConnectWise application, ConnectWise Cloud Management for Microsoft Teams, was used to grant itself Global Administrator and add credentials to other applications. We cannot verify that the remaining ConnectWise applications are secure.

### What to do next

**Disable the application now, even if you see nothing unusual.**

- In the Microsoft Entra admin center, go to Enterprise applications and search for Application ID `506e08f9-6e9a-4da4-942b-a099a03644ae` (you can also search for "SkyKick" or "ConnectWise Cloud Backup").
- Open Properties and set "Enabled for users to sign-in" to No.
- **Do not delete the application.** Deleting it removes the consent, and you will need to re-consent to restore service.
- Check for other ConnectWise and SkyKick applications in your tenant (search for "SkyKick" and "ConnectWise"). If you cannot verify one is safe, disable it as well, without deleting, until ConnectWise confirms that it is.
- Application IDs to look for: 
  - ConnectWise Cloud Backup 
`506e08f9-6e9a-4da4-942b-a099a03644ae`
  - ConnectWise Cloud Management
`2399d300-6fca-4e6a-a686-399fefe75b83`
  - ConnectWise Cloud Management - MS Teams 
`24205314-2b89-4e07-a2a4-579e898a5640` 
  - ConnectWise Cloud Management - Exchange Online 
`b78f6a77-d4e5-46fb-87e5-d1648bd02519`
  - ConnectWise Cloud Management - MS Graph 
`0de14c77-b9b0-4137-9360-34878a929827`
  - ConnectWise Cloud Management - Partner Center
`412dcf96-176d-4b3a-a1b0-4981ad66971e` 
  - ConnectWise Cloud Management - SharePoint Online
`b2b55f5b-7758-4719-8d8f-88ae172e6bdb`
  - In older tenants the Cloud Management apps may appear as "SkyKick Cloud Manager."

- In older tenants the Cloud Management apps may appear as "SkyKick Cloud Manager."
- If a ConnectWise or SkyKick application holds a directory role in your tenant, especially Global Administrator or Privileged Authentication Administrator, review it, and after the app is disabled remove any role you did not intentionally grant.
- If you use Huntress, include the Huntress Security Platform application in the credential review above.
- Review the credentials (client secrets and certificates) on all of your Enterprise applications and App registrations, especially management and security tools, for any added since October 13 that you did not create. Remove anything unexpected.
- Check your Entra audit logs for ConnectWise or SkyKick applications adding themselves to a directory role, and if that application modifies other applications.
- In those audit events, check the user agent. The ConnectWise Cloud Management and Partner Center apps we reviewed make their Graph calls with a .NET SDK user agent (kiota-dotnet). The application changes we saw in the one tenant came from a Python user agent (Python-urllib/3.12), which differs from the vendor apps we reviewed.
- Do not re-enable any ConnectWise applications until ConnectWise confirms all credentials have been reset.

*Figure 2: Mitigation recommendations*

Disabling the app pauses automated backups until it is re-enabled. Your emails, files, Teams messages, and user sign-ins keep working, and existing backups held by ConnectWise are not deleted. Consider whether a gap in recovery points matters for you.

**If you want to check your logs:** 

- In the Entra admin center, go to Monitoring > Sign-in logs, open the Service principal sign-ins tab, and filter by Application ID `506e08f9-6e9a-4da4-942b-a099a03644ae`. The default User sign-ins tab will not show this data.
- In the IP address column, look for any address outside Microsoft/Azure ranges. The app's normal egress is Azure private IPv6. Search for `144.172.64[.]128` specifically.
- A clean result does not rule out access. Please disable the application regardless.

**Also review Conditional Access**: If any policy excludes this application, for example from a location-based block, the attacker's infrastructure will not be blocked there. Review those exclusions once the app is disabled.

### **Why this matters**

The backup service needs broad access to do its job, and an attacker using its credentials will inherit that level of access for every tenant where the app is installed. Depending on the permissions in the tenant, that can include mailboxes, OneDrive and SharePoint files, Teams data, and directory information, much of it belonging to your clients. Some of that access, such as directory reads through Microsoft Graph, leaves no audit trail, which is why we suggest acting now instead of waiting for proof of access. The full potential impact depends on the permissions in play in each tenant.

### **What could happen**

What an attacker can do with a credential like this depends on the permissions already granted to the application in each tenant. A backup service normally holds read access to mail, files, Teams, and directory data so it can copy them, and write access so it can restore them. An attacker holding tokens for that application inherits the same access: reading mail and files in bulk, downloading mailbox and OneDrive contents, enumerating users, groups, and applications, and, where write permissions exist, changing or deleting data. Because the access is app-only, it does not depend on a user being signed in, and the sign-in protections that apply to people do not apply to it.

The larger risk is what happens when that access is used to gain more. If an application can assign directory roles, as we saw in one tenant, it can make itself a Global Administrator, and an administrator can add credentials to other applications, create new applications and grant them permissions, reset passwords and authentication methods for users, and change Conditional Access policies. Each of those steps gives the attacker another way back in that does not depend on the original vendor credential, which is why rotating the vendor credential is necessary, but not enough.

In managed service provider environments the effect can compound. MSPs use management applications and delegated access to administer many customer tenants, so a foothold in one MSP tenant can become a path to its customers. We have not seen that happen, and the audit log shows changes, not reads, but it is the reason we ask MSPs to review credentials on their management and security tools first.

In ATT&CK terms, the activity we observed maps to valid cloud accounts ([<u>T1078.004</u>](https://attack.mitre.org/techniques/T1078/004/)) for the use of the vendor credential, additional cloud roles ([<u>T1098.003</u>](https://attack.mitre.org/techniques/T1098/003/)) for the self-assigned administrator roles, and additional cloud credentials ([<u>T1098.001</u>](https://attack.mitre.org/techniques/T1098/001/)) for the secrets added to other applications.

### **Detecting this in your own logs**

These events appear in the Entra audit log as Add member to role, Update application, and Add service principal credentials. The fields that matter are the initiating application, the target, the result, and the user agent. A service principal that adds itself to a directory role, or that modifies other applications, is unusual in most tenants and worth investigating on its own.

### **Reducing exposure**

Several Entra controls limit the damage if an application credential is stolen. Application management policies can restrict or block client secrets on app registrations and cap credential lifetimes. Limiting who holds the Application Administrator and Cloud Application Administrator roles reduces who can add credentials to applications. Conditional Access for workload identities, which needs additional licensing, can restrict where an application is allowed to sign in from, and Microsoft Entra ID Protection can flag risky service principals. None of these replaces reviewing credentials, but they make a planted secret harder to use or easier to spot.

### What is Huntress Doing?

Huntress has been working with partners to address the steps above. We have also been:

- Checking tenants where we can see sign-in logs through Microsoft Graph, and recording every public IP the app has signed in from. 
  - That work is ongoing and will tell us who else is affected and whether other attacker IPs are involved.
  - We cannot check tenants without the necessary Entra licensing.
- Disabling the application in tenants where we find activity from `144.172.64[.]128`, and in tenants where a ConnectWise or SkyKick application gave itself a directory role, then notifying the affected partner.
- Sweeping every tenant we can see for current state: ConnectWise and SkyKick service principals that hold privileged roles, and credentials added to any application since October 13, including our own application.
- Looking at how we can add visibility into application sign-ins.

We will continue to update this blog as we learn more.

## Indicators of Compromise (IOCs)

| **Item** | **Description** | 
|---|---|
| `144.172.64[.]128` | Infrastructure used in the unauthorized activity Huntress observed a hosting provider (AS14956, RouterHosting). Used for the October 13 to 14 password spray and the October 15 app authentications. | 
| `144.172.64[.]99` | Additional IP indicator shared by ConnectWise in its advisory (part of its update on 10/18 at 18:45 UTC). | 
| `144.172.64[.]60` | Additional IP indicator shared by ConnectWise in its advisory (part of its update on 10/18 at 18:45 UTC). | 
| `506e08f9-6e9a-4da4-942b-a099a03644ae` | Application ID of ConnectWise Cloud Backup (formerly SkyKick Backup). This is a legitimate application. The credential for it is what was abused. Do not block the ID itself, disable the service principal in your tenant. | 
| `3f9cd7a0-127a-4ed4-bf06-2f830d5616b7` | Application owner tenant ID seen on the app's service principal events (the vendor's tenant). | 
| `24205314-2b89-4e07-a2a4-579e898a5640` | Application ID of ConnectWise Cloud Management - MS Teams (formerly SkyKick Cloud Manager - MS Teams). This is a legitimate application. In one tenant it assigned itself Global Administrator and modified other applications. Do not block the ID itself, disable the service principal in your tenant. | 
| `Python-urllib/3.12` `python-requests/2.31` | User agents ConnectWise lists as observed on the suspicious authentication activity. Low fidelity on their own. Python-urllib/3.12 was also the user agent on the credential changes described above, but it is common and not unique to this activity. | 
| `curl/7.88.1` | User agent seen on the password spray. Low fidelity on its own, but useful with the IP. |
