---
title: "Investigation: Unauthorized Access Through the ConnectWise Cloud Backup Microsoft 365 App | Todyl"
author: Nicholas Koken
url: https://www.todyl.com/blog/investigation-unauthorized-access-through-the-connectwise-cloud-backup-microsoft-365-app
hostname: todyl.com
description: Todyl has uncovered indicators of compromise regarding The ConnectWise Cloud Backup and Microsoft 365 tenants. Read our findings here.
sitename: Todyl
date: "2026-10-15"
categories: ['Threat Intelligence']
fingerprint: "246b129f47bf008d"
---
*This is a running post. We will add findings as the investigation develops, and every change is recorded in the update log at the end. All times are UTC.* 

- In Todyl-monitored tenants, an unauthorized party authenticated to Microsoft Graph as the ConnectWise Cloud Backup application.
- The access inherited the app's existing consent, which permits read/write access to mail and attachments (full mailbox access through Exchange Web Services), OneDrive and SharePoint files, and Teams chats, including the ability to restore data.
- We found no directory changes tied to the activity in any tenant: no new secrets, applications, consents, or role assignments by the backup app.
- Revoking user sessions does not end this access. Disabling the app in a tenant stops new tokens from being issued there, though tokens already issued stay valid for up to 90 minutes. Any tenant where the app is still enabled stays exposed until ConnectWise rotates the credential.

**Pattern:** Tenants were hit in strictly **ascending tenant-GUID order**, about 1–6 minutes apart. There's a 43-minute gap between 3282… (07:26) and 6ff6… (08:09).  This tenant GUID patten confirms this is a tool crawling a sorted list of consenting tenants.. We can assume ALL tenants that have 506e08f9-6e9a-4da4-942b-a099a03644ae enabled are compromised.

Todyl identified that a third-party Microsoft 365 application, ConnectWise Cloud Backup (formerly SkyKick Backup) was used by an unauthorized party to sign in to Microsoft 365 tenants Todyl monitors. In those tenants, the sign-ins occurred on October 15, 2026, between 07:11 and 08:47 UTC. The application is a legitimate, vendor-published backup app that many organizations have approved in their tenant. Todyl's analysis shows that an attacker holding a valid secret for that application used it to authenticate directly to Microsoft 365 as the application itself, not as any individual user, from a rented hosting server unrelated to the backup vendor.

Todyl confirmed successful application sign-ins, one per tenant, performed by an automated script. Because the application already held broad, previously granted permissions in each tenant, those sign-ins gave the attacker the technical ability to read and write mail and attachments, OneDrive and SharePoint files, and Teams chats. We found no evidence that the attacker created accounts, added permissions, changed passwords, or established persistence in any tenant through the backup app. The activity was limited to signing in with the already-approved application. The ascending GUID crawl indicates the usage of an automated tool which explains the lack of follow-up actions.

The central risk is data exposure. Confirming exactly which data was copied is limited by how Microsoft logs application activity, as described under Potential risk. Each affected organization should treat its data as potentially exposed and act on the remediation steps below, most importantly disabling the application in every tenant and confirming with ConnectWise that its credential has been rotated. ConnectWise published an advisory on October 16 stating it is investigating "recent attempts of unauthorized access" associated with the Cloud Backup environment, and the source IP it lists matches the one we observed. The advisory does not mention Microsoft 365, the application, or its credential. The app-credential mechanism described in this post is Todyl's own finding.

Todyl’s Cloud Anomaly Framework detected suspicious behavior correlating to the known IoC IPs and affected Application ID, leading to an immediate threat hunt by Todyl MXDR. The team searched every Todyl-monitored tenant for sign-ins by the application, which appears in Entra ID as "ConnectWise Cloud Backup” (formerly SkyKick Backup; app ID 506e08f9-6e9a-4da4-942b-a099a03644ae).

ConnectWise Cloud Backup is a legitimate multi-tenant Microsoft 365 application. When an organization enables the service, a tenant administrator grants the app application permissions, which let it read data without a signed-in user. The app proves its identity with a client secret or certificate that the publisher holds, and that one credential works in every tenant that has granted consent.

1. **Credential use.** The actor presented the app's client secret to Microsoft Entra ID using the OAuth 2.0 client credentials flow.
2. **Token issuance.** Entra ID issued an app-only access token for Microsoft Graph in each tenant the actor targeted. No user interaction was required, so user-focused controls such as MFA and conditional access for users did not apply.
3. **Sweep.** The actor repeated the request between 07:11 and 08:47 UTC, all from the same IPv4 address.

The legitimate backup service authenticates from Microsoft-internal IPv6 addresses (logged in the fd00:: range). The malicious sign-ins differ on every axis we compared: a single commercial VPS IPv4 address, a Python scripting user agent, a single token per tenant rather than a recurring job pattern, and nine target tenants that have no active backup subscription. Taken together, these rule out a misconfigured or relocated backup job.

The app's consent grants tenant-wide read/write access to mail and attachments (including full mailbox access through Exchange Web Services), OneDrive and SharePoint files, and Teams chats, plus the ability to restore data into the tenant. App-only access is not scoped to a single user, so every mailbox and site in the tenant was within reach once a token was issued.

- **Tenants without an active backup subscription.** A token was obtained, and we found no mailbox or file read records afterward. This is consistent with reconnaissance-stage access, and we have no evidence of bulk copying.
- **Tenants with an active backup subscription.** Read activity exists, but it cannot be attributed to the actor or to the backup service. Both use the same application identity. Microsoft 365 audit records for these reads do have IP fields and name the calling app, but the IP they show is Microsoft's own infrastructure, not the actor's. Per-request source IPs are recorded in MicrosoftGraphActivityLogs, which was not being collected for these tenants.

The absence of confirmed exfiltration is partly a visibility limit rather than a clean result. We recommend every affected organization treat its data as exposed.

Todyl’s Cloud Anomaly Framework detected suspicious behavior correlating to the known IoC IPs and affected Application ID, leading to an immediate threat hunt by Todyl MXDR, who took the following actions:

- Added 144\[.\]172\[.\]64\[.\]128 to Todyl's block list.
- Notified affected partners of the compromise by email and through MXDR channels.
- Initiated a threat hunt for signs of additional compromise based on IOCs.
- Multiple new detections built for IOCs and behaviors observed

1. **Disable the app in every tenant now.** In Entra, open Enterprise applications, set the filter to All applications, and search by App ID 506e08f9-6e9a-4da4-942b-a099a03644ae. The name may show as "ConnectWise Cloud Backup" or "SkyKick Backup". Open Properties and set "Enabled for users to sign-in?" to No. Backups pause while it's disabled. Disabling blocks new tokens immediately; tokens already issued expire on their own.
2. **Record what the app could access before you delete anything.** Export its granted permissions from the app's Permissions page. This scopes potential exposure in that tenant. Huntress also recommends disabling rather than deleting, so the app can be re-enabled without a new consent.
3. **Keep it disabled until ConnectWise confirms the credential has been rotated.** The credential belongs to ConnectWise, so only ConnectWise can rotate it. As of October 16, its advisory says containment measures are in place but doesn't say the credential has been rotated.
4. **Find every SkyKick/ConnectWise app in your tenants, including inherited ones.** All SkyKick apps are published from tenant 3f9cd7a0-127a-4ed4-bf06-2f830d5616b7 ("ConnectWise S-K LLC"). Disable any you don't use.
5. **Hunt from October 1, or as far back as retention allows.** In Entra, use the Service principal sign-ins tab (not User sign-ins) and filter on the app ID. Flag 144\[.\]172\[.\]64\[.\]128, user agents Python-urllib/3.12 and python-requests/2.31, and any non-Microsoft IP for this app. In the directory audit log, look for role assignments, consent grants and new credentials made by any SkyKick/ConnectWise app. In the unified audit log, look for mail, file and Teams read events where ClientAppId is the app ID. Export logs now if you're on Entra ID Free (7-day retention).
6. **Enable Microsoft Graph activity logs (Entra ID P1/P2, not retroactive).** Without them, you can't tell where an app's requests came from, so legitimate and malicious use of the same app can't be separated.
7. **Review other multi-tenant apps with tenant-wide permissions.** Conditional Access can't be applied to third-party multi-tenant apps, so least-privilege consent and removing unused apps are the main controls.

**ConnectWise Published Indicators**

**References**

Evaluate your security posture against AI-powered attacks and get recommendations to close any gaps.

Share

Subscribe to our newsletter to get our latest insights.
