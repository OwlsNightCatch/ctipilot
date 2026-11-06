---
title: "Stolen App Credentials, Real Access: An Actor Is Signing Into Entra ID and Azure DevOps as Your Workloads | Todyl"
author: Andrew Scott
url: https://www.todyl.com/blog/stolen-app-credentials-real-access-an-actor-is-signing-into-entra-id-and-azure-devops-as-your-workloads
hostname: todyl.com
description: Todyl is investigating an actor that signs in to Microsoft Entra ID as application service principals using valid, pre-existing credentials.
sitename: Todyl
date: "2026-11-03"
categories: ['Threat Intelligence']
fingerprint: bc30425b4fd4e41e
---
*This is an ongoing incident and Todyl’s MXDR team will be updating as new information becomes available.*

*Investigation Update (11/3/2026 - 4:36pm MT)*

Since November 1, one operator has been signing in to MSPs' Microsoft 365 and Azure environments as their own applications, using stolen credentials that are still valid. About 45 app registrations at roughly 18 organizations were targeted, and more than 33 of them authenticated successfully. Through those apps the actor has reached 27 organizations so far, including the MSPs' downstream clients in government, energy, food and agriculture, transportation, construction and engineering, legal, education and nonprofits.

It has run searches across about 25 tenants, downloaded 81 files and accessed around 2,279 mailbox items. No Microsoft vulnerability is involved. Its latest attempt, at 21:31 UTC on November 3, was blocked. The activity is ongoing, and these numbers are a floor because they only cover organizations that send logs to Todyl.

The speed is what makes it look self-propagating. In three MSP families, the actor used material it had just harvested to sign in to more apps within minutes. In one case, it downloaded a connector archive and signed in as that connector's app about 2.5 minutes later.

But nothing is jumping between MSPs on its own. The evidence points to a single operator working from one VPS through a stockpile of stolen app secrets assembled before November 1, then expanding inside each MSP family at machine speed. Scripted clients made 95% of sign-ins, with bursts of up to 24 sign-ins in 10 seconds and fixed retry loops of about 11 seconds. Multi-hour idle gaps, and a switch to spoofed browser signatures once detections fired, show a person steering the tooling.

That speed and consistency fit automated, possibly AI-assisted agentic tooling. We have not tied the activity to a specific agentic workflow or offensive framework, and our telemetry does not show an AI model directing it, so we hold that possibility at low confidence. The activity is unattributed. We assess it as unrelated to the October 2026 ConnectWise Cloud Backup (formerly SkyKick) compromise attributed to Storm-0940.

- **It spreads through MSP access.** One compromised MSP app exposes every client it manages. In one case, a single multi-tenant app swept 15 client tenants in about 10-second loops.
- **Each hop leads to the next one.** The stolen files are what an attacker needs to move beyond Microsoft 365: password lists, private keys, VPN profiles, MFA and RMM API keys, backup-storage credentials, firewall and RDP configs, Azure environment inventories and service-account maps. We expect them to be used against VPNs, MFA services, RMM and monitoring platforms, backup storage and network devices, which is exposure Todyl can't see from Microsoft 365 logs.
- **Rotating credentials isn't enough on its own.** The actor keeps retrying credentials against disabled and rotated apps, and it has moved on to replaying users' refresh tokens. Conditional Access blocked every token replay we saw on November 3, so check that your policies cover scripted clients signing in from hosting providers.
- **It uses trusted integrations.** Integration credentials for security tools, including Todyl's own integration apps in two MSP tenants, were among those abused. There's no sign any vendor platform was compromised.
- **AI services are on the target list.** Four AI-service tokens were issued at two MSPs (three Cognitive Services, one Azure ML), and AI configuration files were among the files collected. That pattern fits LLM-jacking, though a token being issued doesn't prove it was used.
- **More victims are likely outside our view.** The campaign works from a fixed stockpile, and one compromised MSP exposes many clients. Organizations that don't send logs to Todyl may already be affected.

1. **Get in.** The actor signs in as an app using a stolen secret, and has also used an Azure DevOps federated workload identity and replayed a user's Azure DevOps session token. How it first got these credentials is still unknown. Several of the seed secrets had only ever been used from staff devices and office networks, and some arrived as current-and-expired pairs, which points to a file store or live backend rather than configurations crawled from the internet.
2. **Harvest more credentials.** For nearly every credential it requests an Azure Resource Manager token, then a Key Vault token, often followed within seconds by Graph, Storage and Cognitive Services tokens. Within minutes, apps that had never been used before start authenticating. The timing suggests Key Vault reads are one source of the new material; Key Vault audit logs are needed to confirm it.
3. **Search and collect.** It runs single-wildcard (\*) Microsoft Graph searches, 29 of them across about 25 tenants, then bulk-downloads files from SharePoint at about one per second, focusing on file names related to credentials and configuration.
4. **Reach downstream.** It uses MSP multi-tenant and delegated-admin (GDAP) apps, plus Partner Center tokens, to reach client tenants. One MSP's app obtained a Partner Center token; its GDAP automation app was tried against client tenants without success.
5. **Adapt.** After detections fired at 07:57 UTC on Nov 3, it switched from curl and Python to spoofed browser user agents. By 18:12 UTC it was replaying multiple users' refresh tokens with scripted clients, all blocked by Conditional Access. We have not seen it set up persistence (no new consents, credentials, roles or users), but it keeps retrying in bursts hours apart and may move to new infrastructure as blocking takes effect.

- **Nov 1, 08:45:** First access with a stolen app credential.
- **Nov 1, 14:39:** AzureDevOps federated workload identity used.
- **Nov 2, 10:39:** First replay of a user's Azure DevOps session token.
- **Nov 2, 17:40:** First Microsoft Graph search inside a victim tenant.
- **Nov 2, 20:36:** Bulk file downloads begin, about one file per second.
- **Nov 3, 07:56:** Sweep of 15 client tenants in about 10-second loops; spoofed browser signatures from 07:57.
- **Nov 3, 15:16:** Last successful action (app-only downloads at one MSP).
- **Nov 3, 18:12:** Multiple users' refresh tokens replayed with scripted clients; all blocked by Conditional Access.
- **Nov 3, 21:31:** Latest attempt, a blocked token replay.

- **199.19.77.84:** the operator; all confirmed app sign-ins, downloads and token replays, with 412sign-in attempts in seven days. First seen Nov 1 08:45 UTC, last seen Nov 321:31 UTC (last success 15:16). High confidence.
- **199.19.77.18:** AzureCLI password spray, plus probing of FortiGate and public web services, Nov 1 toNov 3. Low to moderate confidence link to the operator: it shares hosting, but the pattern also fits a generic spray.
- **65.87.223.26:** the same Azure CLI password spray, Oct 4 to 27, on the same ASN. Low to moderate confidence link. Between them, the two spray addresses tried 16 accounts at 16organizations, and every attempt failed.
- **199.19.77.0/24:** contains the operator and spray addresses, hosted on AS203662 (Poland), with no activity observed Oct 6 to Nov 1. Other addresses on this ASN show unrelated activity and are not attributed.
- **Not actor infrastructure:** 20.20.34.96, 20.20.34.160 and 20.231.130.224 are Microsoft service addresses where the actor's searches and mail reads get logged. Don't block them.

These are meaningful onservice-principal and app-only traffic. Several also show up in unrelatedpassword spraying against user accounts.

- **Unique to the actor:** task177-f2267/1.0 and sait-tenant-deep/37346.
- **Strong:** a truncated Mozilla/5.0 (Windows NT 10.0; Win64; x64); Mozilla/5.0 (Windows NT10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0Safari/537.36 with its malformed version; bare Mozilla/5.0; and curl/7.88.1.
- **Used, but not distinctive:** python-requests/2.34.2, Python-urllib/3.12 and curl/8.5.0.

- **•	A secret ID tried before the secret.** AADSTS7000215 with no credential type, followed within minutes by a successful sign-in for the same app from the same IP.
- **One IP, many unrelated tenants.** A single source address authenticating as service principals across multiple unrelated organizations within 24 hours.
- **ResourceManager, then Key Vault, then new apps.** An Azure Resource Manager token immediately followed by a Key Vault token for the same app, then previously unused apps in the same tenant authenticating within minutes.
- **Machine-speed downloads.** App-only SharePoint downloads from non-Microsoft addresses at about one file per second, concentrated on credential- or configuration-related file names, often right after a single wildcard (\*) search.
- **Retries against dead credentials.** Fixed retry loops of about 11 seconds and bursts of up to24 sign-ins in 10 seconds, including against disabled or rotated apps.
- **Token replay from hosting providers.** Refresh tokens for an in-house app's users replayed with Python-urllib or curl from hosting addresses, several users within minutes.
- **Failures with no success.** Failed service-principal sign-ins from hosting providers that never succeed. Detection logic keyed on successful sign-ins will miss these.
- **Azure CLI password grants.** Sign-ins to the Azure CLI public client (04b07795-8ddb-461a-bbee-02f9e1bf7b46) using the password grant (ROPC) from hosting providers.

*End Update*


*Investigation Update (11/3/2026 - 1:03pm MT)*

Based upon our current investigation activity so far, This activity appears to be part of a broader shift that accelerated through October: attackers using workload identities (such as app credentials, federated trust and developer sessions) instead of user accounts to reach Microsoft 365 and Azure, often with AI-assisted automation and a focus on secrets stores such as Key Vault. This activity is not yet tied to a specific actor or prior campaign.

Todyl is tracking three possible connections and will continue to provide updates as our investigation continues:

1. **Storm-0940 / ConnectWise Cloud Backup (formerly SkyKick) connection:** In mid-October, Storm-0940, which Microsoft assesses as China state-aligned, abused that vendor’s multi-tenant app credentials to sign in to customer tenants (https://www.todyl.com/blog/investigation-unauthorized-access-through-the-connectwise-cloud-backup-microsoft-365-app). Microsoft reported AI-automated attempts against 2,250+ tenants, added credentials, role changes and Key Vault reads.

Similar behaviors observed as part of this current campaign are app-identity sign-ins without a user, specific MSP tool targeting, scripted speed, and Key Vault interest. However, what differs is victims’ own app credentials being targeted rather than one single vendor app, different attacker infrastructure and no persistence observed, and no meaningful overlap with SkyKick-affected tenants.

1. **Trojanized Claude Code extension (Cursor marketplace):** On October 29, ([https://www.securityweek.com/malicious-claude-code-extension-served-in-cursor-supply-chain-attack/](https://www.securityweek.com/malicious-claude-code-extension-served-in-cursor-supply-chain-attack/)) tampered versions 2.1.312 and 2.1.313 of anthropic.claude-code were live in Cursor’s marketplace for about 11 hours, planting an SSH key and establishing a reverse tunnel to 134\[.\]209\[.\]82\[.\]225 as well as ongoing persistence. Cursor estimated up to 5,000 users were affected by the incident. The official Visual Studio Marketplace and npm releases were not affected, and Anthropic has stated its systems were not compromised.

The timing (three days before our first sighting) and the target (developer machines holding app secrets, PATs and Azure DevOps sessions) make it a plausible credential source, but we have not tied any affected organization to an install or seen its infrastructure here.

1. **Spike in unauthorized AI model usage:** Todyl is seeing a large increase in AI model usage as part of our investigation, including Anthropic Claude models, which coincides with AI token consumption the affected organizations did not authorize. This can potentially be explained by:

- theft of AI resources (“LLMjacking”) via keys stored in Key Vault,
- AI-assisted automation of the intrusion itself, consistent with the per-task user agents and machine-speed access
- or compromised AI developer tooling as the entry point. **Judgment:** moderate confidence the spike is related; low confidence on the mechanism.

Currently, Todyl has not confirmed that any AI provider’s platform is indicated as compromised. We recommend that all concerned and/or impacted organizations inventory current AI resources and keys utilized, leverage Entra ID authentication over keys, rotate any AI keys in reachable vaults, and set quotas and cost or token-usage alerts.

*Todyl Recommended Mitigation Guidance*

For impacted and/or concerned organizations, unless you are unable to rotate keys for all impacted applications, please follow the 2 steps outlined below to restrict access and potential for compromise. Both steps are required to ensure full enforcement.

Current Todyl partners can leverage the following knowledge base articles to help with mitigation:

*Conditional Access to Entra – Enforcement Steps *

**Part 1: Block the IP with Entra Conditional Access**

The block takes two objects. A named location holds the IP, and a CA policy blocks sign-ins from that location. A named location does nothing until a policy references it.

**Step 1: Create the named location**

- Sign in to the Microsoft Entra admin center at [https://entra.microsoft.com](https://entra.microsoft.com/) as a Conditional Access Administrator.
- Go to **Entra ID > Conditional Access > Named locations**. (In older menus this is **Protection > Conditional Access > Named locations**.)
- Select **+ IP ranges location**. ****
- **Name:** BLOCK - 203.0.113.45 - \<ticket #>.
- Select **+** and enter the IP in CIDR form: 203.0.113.45/32 for one IPv4 address, /128 for one IPv6 address.
- Leave **Mark as trusted location unchecked**. A trusted location can lower sign-in risk and skip MFA, which is the opposite of what you want.
- Select **Create**. Confirm the location appears in the list.

**Step 2: Create the block policy in report-only mode**

- Go to **Entra ID > Conditional Access > Policies** and select **+ New policy**. ****
- **Name:** CA-BLOCK - IP 203.0.113.45 - \<ticket #>. ****
- **Users:**
  - Include: **All users**.
  - Exclude: **Users and groups** → your break-glass account(s) or break-glass group.
- **Target resources: Resources (formerly cloud apps)** → Include **All resources**.
- **Network** (older menus: **Conditions > Locations**):
  - Set **Configure** to **Yes**.
  - Include: **Selected networks and locations** → choose BLOCK - 203.0.113.45 - \<ticket #> → **Select**.
  - Exclude: nothing.
- Leave every other condition (client apps, device platforms, risk) unconfigured, so the block applies to all of them, including legacy authentication. ****
- **Grant:** select **Block access** → **Select**. ****
- **Enable policy: Report-only**. Select **Create**.

**Step 3: Test before enforcing**

- Open the policy list and select **What If**.
- Pick a normal user, enter **IP address** 203.0.113.45, and run it. The CA-BLOCK policy must appear under **Policies that will apply** with **Block**.
- Run it again with a break-glass account. The policy must not apply.
- Run it with your office or VPN egress IP. The policy must not apply.
- Optional: wait 15–60 minutes, then check **Sign-in logs → Report-only** tab for any sign-ins the policy would have blocked. Anything other than the target IP means a mistake in the range.

**Step 4: Enforce**

- Open the policy, set **Enable policy** to **On**, and select **Save**.
- New sign-ins from the IP fail immediately. Existing sessions end when their tokens refresh, usually within an hour.
- For faster cutoff on a compromised account, also go to **Users > \<user> > Revoke sessions** and reset the password.
- Optional hardening: on the policy, **Session > Customize continuous access evaluation > Strictly enforce location policies** makes CAE-capable apps (Exchange, SharePoint, Teams, Graph) reject tokens presented from the blocked IP in near real time. Test it in report-only first; it can break users behind split-tunnel VPNs.

**Deny the IP at the Azure edge**

Azure Front Door with a WAF policy is the true edge: it drops the request at Microsoft's global points of presence with a 403 before it reaches your origin. Use the alternatives at the end of this section if your app isn't behind Front Door.

**Step 1: Open or create the Front Door WAF policy**

- Sign in to [https://portal.azure.com](https://portal.azure.com/).
- Go to **Front Door and CDN profiles** → your profile → **Security policies**. If a WAF policy is already attached, open it and skip to Step 2.
  - If none is attached, search **Web Application Firewall policies (WAF)** → **+ Create**:
  - **Policy for:** Global WAF (Front Door). ****
  - **Front Door tier:** match your profile (Standard supports custom rules only; Premium adds managed rule sets). ****
  - **Name:** wafFdBlockIps. **Policy state:** Enabled. **Policy mode: Prevention**.

**Step 2: Confirm the policy is in Prevention mode**

- In the WAF policy, open **Overview** (or **Policy settings**). ****
- **Mode** must read **Prevention**. In **Detection** mode the rule only logs and nothing is blocked.
- Optional: set **Block response status code** to 403 and a short **Block response body** such as Access denied.

**Step 3: Add the deny rule**

- Open **Custom rules → + Add custom rule**.
- Fill in the following fields:  ****
  - **Custom rule name:** DenyIp20311345 (letters and numbers only) ****
  - **Status:** Enabled ****
  - **Rule type:** Match ****
  - **Priority:** 10 (lower numbers run first; keep it ahead of any allow rules) ****
  - **Match type:** IP address ****
  - **Match variable:** SocketAddr (the address that actually opened the connection) ****
  - **Operation:** Does contain ****
  - **IP address or range:** 203.0.113.45/32 ****
  - **Then:** Deny traffic
- Select **Add**, then **Save** at the top of the Custom rules page.
- If clients reach you through another proxy or CDN that sets X-Forwarded-For, add a second rule identical to the first, but with **Match variable** set to **RemoteAddr** and **Priority** set to **11**.

**Step 4: Attach the policy to your endpoints**

- In the WAF policy, open **Associations** (or in the Front Door profile, **Security policies → + Add**).
- Select the Front Door profile, then every domain and endpoint that should be protected.
- Select **Save**. Changes propagate to the edge in a few minutes.

**Step 5: Close the side door**

A WAF on Front Door only filters traffic that goes through Front Door. If your origin is still reachable at its own address (for example myapp.azurewebsites.net), the blocked IP can go around the edge.

- On the origin App Service: **Networking → Access restrictions** → add an Allow rule with **Type = Service Tag**, **Service tag = AzureFrontDoor.Backend**, and **X-Azure-FDID** = your Front Door profile ID (from the profile's **Overview**).
- Set **Unmatched rule action** to **Deny**.

Todyl is investigating an actor that signs in to Microsoft Entra ID as application service principals using valid, pre-existing credentials. This has involved the use of client secrets and, in at least one case, a workload identity federated credential. This is an active incident that began on November 1, 2026 and spans multiple unrelated organizations, including MSPs and the customer tenants they manage. Because these are app sign-ins, there is no MFA prompt, user-scoped Conditional Access doesn’t apply, and firewall rules never see the traffic. If the credential is valid, the app is in.

- **One source address.** All confirmed malicious activity comes from 199\[.\]19\[.\]77\[.\]84 (AS203662, 3K33 sp. z o.o., Poland-geolocated hosting), first seen Nov 1 and last seen Nov 3 (UTC).
- **Same playbook per app.** For almost every credential, the actor hits Azure Resource Manager first, then Key Vault, Storage, Microsoft Graph and, where available, Partner Center. A failed client-secret attempt and a successful one often appear for the same app seconds to minutes apart.
- **Broad reach from one address.** In one tenant, nearly every legitimate address touched a single service principal; the actor’s address touched every tenant it held credentials for, and was the only source with failures.
- **Azure DevOps.** A federated credential tied to Azure DevOps was used from the actor’s address starting Nov 1, 14:39 UTC, and two users’ Azure DevOps sessions were replayed on Nov 2. Reported PAT use is being examined.
- **Collection, not dwell.** File downloads from Microsoft 365, with interest in keys, API credentials and client documentation. No persistence observed; time in each tenant is short. Scripted clients and custom user agents that change per task.
- **MSP-to-customer reach.** In at least one case, access to an MSP was followed within seconds by access to several downstream customer tenants via delegated admin.

NOTE: Todyl is currently investigating the root cause around this investigationnand will provide more details once confirmed.

**Don’t block the whole ASN.** Other addresses in this provider’s space are doing unrelated things (scanning, a file-sync relay, Azure CLI password attempts) and are not attributed to this actor. Block the exact IP only; we’ll publish further indicators only once confirmed. How the credentials were obtained, and who is behind this, is not yet known.

- **Secrets unlock more secrets.** The path from ARM to Key Vault and Storage means one compromised app can expose the keys and connection strings for many other systems.
- **MSP and supply-chain blast radius.** Partner Center, delegated admin and Azure DevOps service connections turn one app into access to customer tenants, source code and production deployments.
- **False assurance.** Firewall blocks and user-focused Conditional Access don’t stop this. Treat confirmed access as a potential data-exposure event and involve legal and privacy stakeholders early.

Create a named location for 199.19.77.84/32 and block it in a policy targeting workload identities, assigned directly to service principals (group assignment isn’t enforced for them). Add it to a user-scoped block policy to cover replayed sessions and turn on Conditional Access policy validation in Azure DevOps. Note the limits: workload identity policies require the standalone Workload ID Premium license and cover only single-tenant apps registered in your tenant, not managed identities, multitenant apps or third-party SaaS.

Check Entra Service principal and non-interactive sign-in logs for the IP, or run:

union AADServicePrincipalSignInLogs, AADNonInteractiveUserSignInLogs

| where IPAddress == "199.19.77.84"

| project TimeGenerated, AppId, ServicePrincipalName, UserPrincipalName,

ClientCredentialType, ResultType, ResourceDisplayName

- **Failures count.** AADSTS7000215 (invalid secret) or AADSTS7000222 (expired secret) means someone holds a credential for your app and observing a failure followed by a success is urgent.
- **Azure DevOps.** Filter Organization settings → Auditing (or AzureDevOpsAuditing) by IpAddress. Review PAT creation and first use, federated service connections, pipeline runs and edits, and unfamiliar user agents. If auditing is off, enable it.
- **Behavior, not just IP.** Alert on one address authenticating to three or more service principals in a tenant with mixed success, or one app fanning out across ARM, Key Vault, Storage and Graph in a short window.
- **Look back further.** Earliest sightings sit at the edge of current query windows; search as far back as retention allows.

1. **Contain.** Remove all secrets, certificates and federated credentials on the affected app, watch for ones you didn’t add, and disable the service principal if needed. Issued tokens otherwise stay valid until expiry. For affected users, revoke Entra sessions, Azure DevOps PATs and SSH keys.
2. **Scope.** Review the app’s API permissions, directory and Azure RBAC roles, Key Vault access, Partner Center access and Azure DevOps service connections.
3. **Audit.** Search Azure activity, Key Vault and Storage diagnostics, Entra audit, Azure DevOps audit and M365 unified audit logs for the IP, including secret reads, blob and file downloads, and changes to apps, permissions or pipelines.
4. **Rotate downstream.** Rotate everything in any Key Vault the app could read and any credentials in accessed documents, then find where the original credential was stored and who had it.
5. **MSPs.** Check Partner Center, GDAP relationships and customer tenants, and notify affected customers per your agreements.

Regardless of how these credentials were obtained, client secrets, PATs, and session cookies commonly leak from developer and admin workstations (infostealers), scripts and .env files, repositories and CI/CD variables, and runbooks or client documentation. Federation removes the stored secret but moves trust to the system issuing tokens. In this case that’s Azure DevOps, so protect that system just as carefully.

- **Retire client secrets.** Prefer managed identities, then workload identity federation, then vault-held certificates. Use Entra app management policies to block new secrets and cap credential lifetimes.
- **Put data behind the network.** Restrict Key Vault and Storage to selected networks or private endpoints so a valid token from an unknown address can’t reach the data; use Key Vault RBAC and enable diagnostic logging.
- **Harden Azure DevOps.** Restrict PAT creation and scope, enforce short lifetimes, limit who can create and use service connections, scope them narrowly, require approvals for production, and stream auditing to your SIEM.
- **Shrink the surface.** Inventory apps and service principals, remove unused ones and stale credentials, enforce least privilege, limit app ownership and app-admin roles, and alert on new secrets, certificates or federated credentials.
- **Protect the endpoints that hold the keys.** Defend developer and admin machines against infostealers, keep secrets out of code, wikis and tickets, shorten privileged session lifetimes, and use token protection where supported. Turn on risk detection for workload identities if licensed.
- **MSPs.** Audit partner-tenant apps (especially those with Partner Center access), move to least-privilege time-bound GDAP, and never store customer app secrets in runbooks, PSA/RMM notes or client documentation.

**MITRE ATT&CK:** T1078.004 Cloud Accounts, T1550.001 Application Access Token, T1550.004 Web Session Cookie, T1580 Cloud Infrastructure Discovery, T1555.006 Cloud Secrets Management Stores, T1530 Data from Cloud Storage, T1199 Trusted Relationship.

If you’ve seen 199\[.\]19\[.\]77\[.\]84 or this behavior, please share first and last timestamps (UTC) including Azure DevOps audit entries and first PAT use, as well as any service principal sign-ins or SharePoint downloads from other AS203662 addresses. We’ll continue to update this post as the investigation develops.

*References: Microsoft Learn documentation on Conditional Access and continuous access evaluation for workload identities, Workload ID licensing, Entra error codes, and Azure DevOps auditing; RIPE/RIPEstat registration and routing data.*

Evaluate your security posture against AI-powered attacks and get recommendations to close any gaps.

Share

Subscribe to our newsletter to get our latest insights.
