---
schema: 1
kind: incident
title: "ConnectWise Cloud Backup (formerly SkyKick): the vendor's Microsoft 365 application credential was used to sign in to customer tenants, with directory-role self-assignments in about 50 tenants and, Huntress reports, added credentials in two"
headline: "ConnectWise SkyKick app credential used in 162+ Microsoft 365 tenants; disabling it does not undo planted access"
summary: >
  ConnectWise says it identified unauthorized access to application identities of its Cloud Backup (formerly SkyKick) service; Huntress and Todyl report that from 15 October the app's credential was used to obtain app-only Microsoft Graph tokens in customer Microsoft 365 tenants; Huntress alone confirmed unauthorized sign-ins in 162 tenants by 16 October and saw ConnectWise Cloud Management apps assign themselves directory roles in about 50 tenants and, in two tenants, a scripted Global Administrator self-grant followed by new client secrets planted on apparently random applications. ConnectWise disabled seven application identities and suspended the service on 17 October, but says disabling does not reverse changes already made in a tenant, so every tenant that ever consented a ConnectWise or SkyKick app needs the apps disabled and its application credentials, directory roles and consents reviewed. Microsoft assesses that the China-state aligned actor Storm-0940 is behind it, using the ARTEX agentic-AI framework, and says it attempted sign-ins to more than 2,250 tenants; how the credential was obtained and what data was read are not public.
discovered_at: "2026-10-18T03:30:00Z"
updated_at: "2026-10-22T03:46:23Z"
event_date: "2026-10-15"
run_id: 2026-10-18T0256Z-intel
priority: high
immediate_action: null
tags: [supply-chain, cloud, identity, actively-exploited]
regions: [global]
sectors: [technology]
entities: ["incident:connectwise-cloud-backup-skykick-app-credential-abuse-2026-10", "product:connectwise-cloud-backup", "product:connectwise-cloud-management", "product:microsoft-entra-id", "actor:storm-0940"]
techniques: [T1199, T1078.004, T1098.003, T1098.001, T1110.003]
affected_products: ["ConnectWise Cloud Backup", "ConnectWise Cloud Management", "Microsoft Entra ID"]
cves: []
sources:
  - url: "https://www.connectwise.com/company/trust/advisories"
    publisher: "ConnectWise Trust Center (advisory)"
    date: "2026-10-21"
    role: primary
  - url: "https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access"
    publisher: "Huntress"
    date: "2026-10-16"
    role: corroborating
  - url: "https://www.todyl.com/blog/investigation-unauthorized-access-through-the-connectwise-cloud-backup-microsoft-365-app"
    publisher: "Todyl"
    date: "2026-10-15"
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/hackers-breach-microsoft-365-tenants-via-connectwise-supply-chain-attack/"
    publisher: "BleepingComputer"
    date: "2026-10-17"
    role: corroborating
  - url: "https://specterops.io/blog/2026/10/17/connectwise-skykick-breach-microsoft-365/"
    publisher: "SpecterOps"
    date: "2026-10-17"
    role: corroborating
  - url: "https://www.sophos.com/en-us/blog/connectwise-cloud-backup-application-abused-in-token-sweep"
    publisher: "Sophos X-Ops"
    date: "2026-10-19"
    role: corroborating
  - url: "https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/"
    publisher: "Microsoft Threat Intelligence"
    date: "2026-10-21"
    role: corroborating
  - url: "https://expel.com/blog/storm-0940-artex-attacks-connectwise-app-abuse-and-okta-sign-ups/"
    publisher: "Expel"
    date: "2026-10-21"
    role: corroborating
  - url: "https://www.heise.de/news/Angriffe-via-ConnectWise-Cloud-Backup-11495835.html"
    publisher: "heise online"
    date: "2026-10-21"
    role: corroborating
  - url: "https://www.huntress.com/blog/connectwise-attack-ai"
    publisher: "Huntress (AI, Scripts, Operator: Inside the ConnectWise Attack)"
    date: "2026-10-26"
    role: corroborating
closed_sources: []
evidence:
  - quote: "We recently identified unauthorized access to application identities within the ConnectWise Cloud Backup environment."
    publisher: "ConnectWise Trust Center (advisory)"
    source_url: "https://www.connectwise.com/company/trust/advisories"
  - quote: "Disabling the affected connections prevents new authentication through those connections; it does not reverse changes previously made inside a tenant."
    publisher: "ConnectWise Trust Center (advisory)"
    source_url: "https://www.connectwise.com/company/trust/advisories"
  - quote: "Whether a product vulnerability contributed has not been established"
    publisher: "ConnectWise Trust Center (advisory)"
    source_url: "https://www.connectwise.com/company/trust/advisories"
  - quote: "As of 19:00 UTC on October 16, Huntress has confirmed unauthorized sign-ins in 162 tenants."
    publisher: "Huntress"
    source_url: "https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access"
  - quote: "The credential type was a client assertion, which means the credential lives in the vendor's own tenant."
    publisher: "Huntress"
    source_url: "https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access"
  - quote: "These tenants are in the policy, national security, trade, and critical mineral sectors."
    publisher: "Huntress"
    source_url: "https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access"
  - quote: "Because the application already held broad, previously granted permissions in each tenant, those sign-ins gave the attacker the technical ability to read and write mail and attachments, OneDrive and SharePoint files, and Teams chats."
    publisher: "Todyl"
    source_url: "https://www.todyl.com/blog/investigation-unauthorized-access-through-the-connectwise-cloud-backup-microsoft-365-app"
  - quote: "Revoking user sessions does not end this access."
    publisher: "Todyl"
    source_url: "https://www.todyl.com/blog/investigation-unauthorized-access-through-the-connectwise-cloud-backup-microsoft-365-app"
  - quote: "Previously issued access tokens may remain usable until they expire or are otherwise invalidated."
    publisher: "ConnectWise Trust Center (advisory)"
    source_url: "https://www.connectwise.com/company/trust/advisories"
  - quote: "Disabling the app in a tenant stops new tokens from being issued there, though tokens already issued stay valid for up to 90 minutes."
    publisher: "Todyl"
    source_url: "https://www.todyl.com/blog/investigation-unauthorized-access-through-the-connectwise-cloud-backup-microsoft-365-app"
  - quote: "Older tenants may list them under SkyKick names."
    publisher: "SpecterOps"
    source_url: "https://specterops.io/blog/2026/10/17/connectwise-skykick-breach-microsoft-365/"
  - quote: "Since implementing mitigations, we have not observed successful threat activity in the environments we monitor."
    publisher: "ConnectWise Trust Center (advisory)"
    source_url: "https://www.connectwise.com/company/trust/advisories"
  - quote: "the last confirmed successful sign-in we observed with this credential was at 08:44 UTC on October 15"
    publisher: "Huntress"
    source_url: "https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access"
  - quote: "Huntress has identified a second tenant with post-compromise activity"
    publisher: "Huntress"
    source_url: "https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access"
  - quote: "the application granted itself Global Administrator, then planted a new secret on a small number of other applications in the tenant to keep a foothold"
    publisher: "Huntress"
    source_url: "https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access"
  - quote: "The choice of which applications to backdoor appeared to be random in the two tenants we reviewed."
    publisher: "Huntress"
    source_url: "https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access"
  - quote: "The access may have been used for Microsoft Graph directory reads, which leave no audit record."
    publisher: "Huntress"
    source_url: "https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access"
  - quote: "we also found no evidence of mailbox or file manipulation, or user or policy changes"
    publisher: "Huntress"
    source_url: "https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access"
  - quote: "Tenants were accessed in strictly ascending tenant GUID order."
    publisher: "Sophos X-Ops"
    source_url: "https://www.sophos.com/en-us/blog/connectwise-cloud-backup-application-abused-in-token-sweep"
  - quote: "As of this publication, there is no evidence that the application created new secrets, applications, consents, or role assignments in the reviewed tenants."
    publisher: "Sophos X-Ops"
    source_url: "https://www.sophos.com/en-us/blog/connectwise-cloud-backup-application-abused-in-token-sweep"
  - quote: "Microsoft assesses that Storm-0940 was responsible for the recently disclosed"
    publisher: "Microsoft Threat Intelligence"
    source_url: "https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/"
  - quote: "Storm-0940 used ARTEX to attempt to sign-in to more than 2,250 tenants."
    publisher: "Microsoft Threat Intelligence"
    source_url: "https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/"
  - quote: "These changes can remain active as a backdoor even after the original compromised application is mediated."
    publisher: "Microsoft Threat Intelligence"
    source_url: "https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/"
  - quote: "On our own telemetry alone, we put our confidence that an LLM was involved in the escalation tooling at low to medium."
    publisher: "Huntress (AI, Scripts, Operator: Inside the ConnectWise Attack)"
    source_url: "https://www.huntress.com/blog/connectwise-attack-ai"
  - quote: "Alert when a service principal assigns itself"
    publisher: "Huntress (AI, Scripts, Operator: Inside the ConnectWise Attack)"
    source_url: "https://www.huntress.com/blog/connectwise-attack-ai"
verification: multi-source
sourcing_note: >
  ConnectWise is the first-party source for its own incident, and Huntress, Todyl and Sophos X-Ops each observed the
  sign-ins in tenants they monitor. The attribution to Storm-0940 is Microsoft's assessment from its own telemetry, relayed
  by Expel; ConnectWise says only that it appears a China state-aligned group was responsible, and Huntress has not tied its Global
  Administrator observation to the same operator. The Huntress figures are those of its update of 2026-10-19 13:30 ET, ConnectWise's
  advisory is cited as of 2026-10-19 01:15 UTC and, for 2026-10-21, as read from an archived copy, and Sophos saw no new secrets,
  applications, consents or role assignments in the subset of tenants it reviewed, where Huntress saw role grants and added secrets. Huntress's analysis of 2026-10-26 says its own telemetry alone supports only low to medium confidence that an LLM was involved in the escalation tooling and medium to high once Microsoft's attribution is included.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions:
  - "In every Entra tenant you or your MSP administer, disable without deleting the seven ConnectWise application identities that ConnectWise lists by client ID (Cloud Backup is 506e08f9-6e9a-4da4-942b-a099a03644ae; the other six are in ConnectWise's advisory), dormant connections included, and keep them disabled until ConnectWise gives restoration instructions; where Graph activity logs were enabled, review them for these apps until at least 90 minutes after you disabled them, because a token issued before the disable stays valid for up to 90 minutes, and preserve the sign-in and audit logs promptly without delaying containment, because Entra ID Free keeps only 7 days."
  - "In the same tenants list the apps owned by the ConnectWise S-K LLC tenant (3f9cd7a0-127a-4ed4-bf06-2f830d5616b7), and disable each that you do not use or cannot verify as safe."
  - "In the same tenants review every enterprise application and app registration, MSP management and security tools first but none skipped (Huntress saw the secrets planted on apparently random applications, in one tenant on some of the least privileged ones), for client secrets, certificates and federated credentials added since 2026-10-13 and remove any you did not create; also check the directory roles, owners and consent grants held by ConnectWise and SkyKick service principals, Conditional Access exclusions for them, and mailbox forwarding, inbox and transport rules and delegated access, because disabling the vendor applications does not remove access planted through them."
updates:
  - at: "2026-10-19T03:47:00Z"
    run_id: 2026-10-19T0256Z-intel
    type: improvement
    summary: >
      ConnectWise's update of 2026-10-18 01:00 UTC took SaaS Security and Cloud Management offline in addition to Cloud Backup, which had been suspended since 2026-10-17, so its monitoring and alerting is out of service, and its latest update (2026-10-19 01:15 UTC) gives no restoration time; Todyl and SpecterOps say a token issued before an app is disabled stays valid for up to 90 minutes, and ConnectWise says previously issued tokens may remain usable until they expire; and Todyl says to find every SkyKick and ConnectWise app in a tenant, inherited ones included, while Todyl and SpecterOps point to the apps owned by ConnectWise's vendor tenant.
    fields: [actions, sources, evidence, sourcing_note, body]
  - at: "2026-10-20T03:57:49Z"
    run_id: 2026-10-20T0256Z-intel
    type: update
    summary: >
      Huntress's update of 2026-10-19 reports a second tenant with scripted post-compromise activity (the application granting itself Global Administrator and planting a secret on other applications, the choice of applications apparently random), bounds the sign-in activity to the morning of 2026-10-15 UTC with the last successful sign-in at 08:44 UTC, and says Graph directory reads leave no audit record; the secret check therefore has to cover every application.
    fields: [title, summary, actions, sources, evidence, sourcing_note, body]
  - at: "2026-10-21T03:47:47Z"
    run_id: 2026-10-21T0256Z-intel
    type: improvement
    summary: >
      Sophos X-Ops reports the same token sweep from its own telemetry, from a single server in ascending
      tenant order and including tenants with no active backup subscription, and found no planted secrets,
      applications, consents or role assignments in the tenants it reviewed, unlike Huntress's two
      tenants.
    fields: [sources, evidence, sourcing_note, body]
  - at: "2026-10-22T03:46:23Z"
    run_id: 2026-10-22T0256Z-intel
    type: update
    summary: >
      Microsoft Threat Intelligence assesses that Storm-0940, a China-state aligned actor, was responsible
      for the compromise, using the ARTEX agentic-AI framework to attempt sign-ins to more than 2,250
      tenants after an automated password spray from the same network range, and warns that credential
      changes planted in tenants can persist after the vendor application is remediated. ConnectWise itself
      says it appears a China state-aligned group was responsible and began restoring services in controlled
      phases on 2026-10-21.
    fields: [body, entities, evidence, sources, sourcing_note, summary]
  - at: "2026-10-25T13:43:07Z"
    run_id: 2026-10-25T1308Z-audit
    type: correction
    summary: >
      Corrects the 2026-10-22 update: Microsoft's 2,900-a-minute figure is the peak of failed logons in
      the separate 10 to 14 October password spray, not the rate of the ARTEX sign-ins to more than 2,250
      tenants.
    fields: [body, evidence]
  - at: "2026-10-27T03:46:02Z"
    run_id: 2026-10-27T0256Z-intel
    type: improvement
    summary: >
      Huntress's analysis of 2026-10-26 reads the activity as scripted tooling steered by an operator,
      rates LLM involvement low to medium on its own telemetry, adds a detection for service principals
      that assign themselves or a sibling a directory role, and notes that Graph reads leave no Entra
      audit record.
    fields: [evidence, sources, sourcing_note]
migrated_from: null
---

ConnectWise says it identified unauthorized access to application identities within its Cloud Backup (formerly SkyKick) environment; on 2026-10-17 it disabled seven application identities, suspended the service, says the shared Cloud Backup credentials are no longer valid, and warns that disabling does not reverse changes already made in a tenant ([ConnectWise, 2026-10-19](https://www.connectwise.com/company/trust/advisories)). As of ConnectWise's update of 2026-10-19 01:15 UTC, Cloud Backup, SaaS Security and Cloud Management remained suspended with no confirmed restoration time, which also took ConnectWise's SaaS Security monitoring and alerting out of service ([ConnectWise, 2026-10-19](https://www.connectwise.com/company/trust/advisories)), and heise reports on 2026-10-21 that ConnectWise has since begun restoring the services step by step over several days ([heise online, 2026-10-21](https://www.heise.de/news/Angriffe-via-ConnectWise-Cloud-Backup-11495835.html)); ConnectWise reports no successful threat activity in the environments it monitors since it implemented mitigations ([ConnectWise, 2026-10-19](https://www.connectwise.com/company/trust/advisories)) and says it cannot independently determine whether a given partner or customer tenant was affected ([ConnectWise, 2026-10-19](https://www.connectwise.com/company/trust/advisories)). Huntress and Todyl report that on 2026-10-15 the app's identity signed in to customer Microsoft 365 tenants from one hosting-provider address and received app-only Microsoft Graph tokens; the credential sits in the vendor's own tenant, so no user, MFA prompt or user Conditional Access was involved, and the app's consent covers read and write access to mail, files and Teams chats ([Huntress, 2026-10-16](https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access); [Todyl, 2026-10-15](https://www.todyl.com/blog/investigation-unauthorized-access-through-the-connectwise-cloud-backup-microsoft-365-app)). Huntress confirmed unauthorized sign-ins in 162 tenants by 2026-10-16 and later counted almost 1,000 tenants with sign-in activity from that address, over 300 successful, after password spraying against four law-firm tenants on 13 and 14 October, and a separate failed wave targeted 16 tenants in policy and national-security sectors ([Huntress, 2026-10-16](https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access)). In about 50 of its tenants, ConnectWise Cloud Management apps assigned themselves directory roles, mostly Exchange Administrator; in one the Teams app added itself to Global Administrator and client secrets were added to an MSP management application and to Huntress's own application within about five minutes, the credential additions from private Azure space ([Huntress, 2026-10-16](https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access)). Huntress later identified a second tenant with the same sequence, the application granting itself Global Administrator and then planting a new secret on a small number of other applications, within two minutes of the first around 03:45 UTC on 2026-10-15, with the choice of applications apparently random ([Huntress, 2026-10-16](https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access)). It says the unauthorized sign-ins with the credential were bunched across the morning of 2026-10-15 UTC, that the last successful one it observed was at 08:44 UTC that day with only failed attempts afterwards in the tenants where it can read sign-in logs, and that in the two tenants it reviewed it found no mailbox or file manipulation and no user or policy changes ([Huntress, 2026-10-16](https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access)). Microsoft Threat Intelligence, as BleepingComputer relays it, called it an active supply-chain attack and assessed likely abuse of existing permissions including Directory.ReadWrite.All ([BleepingComputer, 2026-10-17](https://www.bleepingcomputer.com/news/security/hackers-breach-microsoft-365-tenants-via-connectwise-supply-chain-attack/)). Microsoft Threat Intelligence later assessed that Storm-0940, a China-state aligned actor, was responsible, using the ARTEX agentic-AI framework to attempt sign-ins to more than 2,250 tenants ([Microsoft, 2026-10-21](https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/)). How the credential was obtained and what was read remain unknown ([ConnectWise, 2026-10-19](https://www.connectwise.com/company/trust/advisories); [BleepingComputer, 2026-10-17](https://www.bleepingcomputer.com/news/security/hackers-breach-microsoft-365-tenants-via-connectwise-supply-chain-attack/)).

**Exposure:** every Entra tenant, including each customer tenant an MSP manages, in which a ConnectWise or SkyKick Cloud Backup or Cloud Management app was ever consented, dormant connections included; ConnectWise lists seven application client IDs, among them Cloud Backup (506e08f9-6e9a-4da4-942b-a099a03644ae), and says to match on client ID ([ConnectWise, 2026-10-19](https://www.connectwise.com/company/trust/advisories)). Todyl says to find every SkyKick and ConnectWise app in a tenant, inherited ones included, and that all SkyKick apps are published from one vendor tenant (named ConnectWise S-K LLC, ID 3f9cd7a0-127a-4ed4-bf06-2f830d5616b7); SpecterOps hunts for apps owned by that tenant and notes that older tenants may list them under SkyKick names ([Todyl, 2026-10-15](https://www.todyl.com/blog/investigation-unauthorized-access-through-the-connectwise-cloud-backup-microsoft-365-app); [SpecterOps, 2026-10-17](https://specterops.io/blog/2026/10/17/connectwise-skykick-breach-microsoft-365/)).

**Detection:** Entra service-principal sign-in logs for these apps from any address outside Microsoft and Azure ranges, which misses the credential additions, made from private Azure space ([Huntress, 2026-10-16](https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access)); the sweep of sign-ins itself, which Sophos saw come from a single virtual private server in strictly ascending tenant-ID order with Python HTTP-library user agents ([Sophos, 2026-10-19](https://www.sophos.com/en-us/blog/connectwise-cloud-backup-application-abused-in-token-sweep)); directory audit events Add member to role, Update application and Add service principal credentials initiated by a ConnectWise or SkyKick app ([Huntress, 2026-10-16](https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access)); Graph activity logs (Entra ID P1 or P2, not retroactive) for per-request source addresses ([Todyl, 2026-10-15](https://www.todyl.com/blog/investigation-unauthorized-access-through-the-connectwise-cloud-backup-microsoft-365-app)); and mailbox forwarding, inbox and transport rule and delegation changes ([ConnectWise, 2026-10-19](https://www.connectwise.com/company/trust/advisories)). Huntress notes that Microsoft Graph directory reads leave no audit record, so a clean audit log does not rule out reads of the directory ([Huntress, 2026-10-16](https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access)). Disabling the apps does not remove credentials, roles or consents already planted, and revoking user sessions does not end this access ([ConnectWise, 2026-10-19](https://www.connectwise.com/company/trust/advisories); [Todyl, 2026-10-15](https://www.todyl.com/blog/investigation-unauthorized-access-through-the-connectwise-cloud-backup-microsoft-365-app)). Disabling an app stops new tokens only: a token issued before the disable stays valid for up to 90 minutes ([Todyl, 2026-10-15](https://www.todyl.com/blog/investigation-unauthorized-access-through-the-connectwise-cloud-backup-microsoft-365-app); [SpecterOps, 2026-10-17](https://specterops.io/blog/2026/10/17/connectwise-skykick-breach-microsoft-365/)), and ConnectWise says that after its own certificate revocation previously issued tokens may remain usable until they expire ([ConnectWise, 2026-10-19](https://www.connectwise.com/company/trust/advisories)). The service-principal sign-in log records an application's authentication ([ConnectWise, 2026-10-19](https://www.connectwise.com/company/trust/advisories)), while per-request use of a token appears in the Graph activity logs named above ([Todyl, 2026-10-15](https://www.todyl.com/blog/investigation-unauthorized-access-through-the-connectwise-cloud-backup-microsoft-365-app)), so the review of that period belongs there. Microsoft asks tenants to review service-principal sign-ins from at least 2026-10-15, and from 2026-10-01 where records exist, and to search by application ID rather than display name ([Microsoft, 2026-10-21](https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/)). Any alerting a tenant took from ConnectWise SaaS Security is out of service while that service is suspended ([ConnectWise, 2026-10-19](https://www.connectwise.com/company/trust/advisories)).

**Triage:** the vendor's apps sign in from Azure addresses with a .NET SDK user agent, while the credential additions used a Python user agent; Python and curl are common in administration, so Huntress says the combination of actor, operation and user agent is the signal ([Huntress, 2026-10-16](https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access)). Role self-assignments carrying the vendor's own user agent are not proven benign, since Huntress has not confirmed vendor automation ([Huntress, 2026-10-16](https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access)).

**Defender takeaway:** where any ConnectWise or SkyKick app is consented, disable it by client ID without deleting it, keep it disabled until ConnectWise gives restoration instructions, and review credentials, roles, owners, consents and Conditional Access exclusions since 13 October ([ConnectWise, 2026-10-19](https://www.connectwise.com/company/trust/advisories); [Huntress, 2026-10-16](https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access)). An MSP should review its own management and security tools first, since a foothold there can reach its customers, but the review covers every application, because Huntress saw secrets planted on apparently random ones ([Huntress, 2026-10-16](https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access)). ConnectWise cannot independently determine whether a given partner or customer tenant was affected, so the answer for a tenant has to come from its own sign-in and audit logs ([ConnectWise, 2026-10-19](https://www.connectwise.com/company/trust/advisories)).

## Improvement — 2026-10-19T03:47:00Z

ConnectWise's update of 2026-10-18 01:00 UTC took SaaS Security and Cloud Management offline in addition to Cloud Backup, which had been suspended since 2026-10-17, so ConnectWise SaaS Security monitoring and alerting is out of service as well, and the update of 2026-10-19 01:15 UTC still gives no restoration time ([ConnectWise, 2026-10-19](https://www.connectwise.com/company/trust/advisories)). Disabling an app stops new tokens only: Todyl and SpecterOps each state that tokens already issued stay valid for up to 90 minutes, and ConnectWise says that after it revoked the Cloud Backup certificates previously issued tokens may remain usable until they expire ([Todyl, 2026-10-15](https://www.todyl.com/blog/investigation-unauthorized-access-through-the-connectwise-cloud-backup-microsoft-365-app); [SpecterOps, 2026-10-17](https://specterops.io/blog/2026/10/17/connectwise-skykick-breach-microsoft-365/); [ConnectWise, 2026-10-19](https://www.connectwise.com/company/trust/advisories)). Todyl says to find every SkyKick and ConnectWise app in a tenant, inherited ones included, and that all SkyKick apps are published from one vendor tenant, and SpecterOps hunts for apps owned by that tenant, noting that older tenants may list them under SkyKick names ([Todyl, 2026-10-15](https://www.todyl.com/blog/investigation-unauthorized-access-through-the-connectwise-cloud-backup-microsoft-365-app); [SpecterOps, 2026-10-17](https://specterops.io/blog/2026/10/17/connectwise-skykick-breach-microsoft-365/)).

## Update — 2026-10-20T03:57:49Z

Huntress's update of 2026-10-19 13:30 ET identified a second tenant with post-compromise activity, a tenant Huntress did not originally protect, where it got deployed to collect telemetry ([Huntress, 2026-10-16](https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access)). In both tenants the activity was fast and scripted, within two minutes of each other around 03:45 UTC on 2026-10-15: the application granted itself Global Administrator and then planted a new secret on a small number of other applications to keep a foothold ([Huntress, 2026-10-16](https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access)). The choice of applications appeared random: the same flow picked two different sets, one application present in both was backdoored in only one, and in one tenant the applications that received secrets were among the least privileged in the environment while far more powerful ones were untouched ([Huntress, 2026-10-16](https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access)).

Huntress says the unauthorized sign-ins with the credential were tightly bunched across the morning of 2026-10-15 UTC, the last confirmed successful sign-in it observed was at 08:44 UTC, and it saw only failed attempts afterwards in the tenants where it can read sign-in logs ([Huntress, 2026-10-16](https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access)). The access may have been used for Microsoft Graph directory reads, which leave no audit record, and in the two tenants Huntress reviewed it found no evidence of mailbox or file manipulation or of user or policy changes ([Huntress, 2026-10-16](https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access)). The check for planted credentials therefore has to cover every application registration and enterprise application in the tenant, and a clean audit log does not exclude directory reads. ConnectWise's latest readable update (2026-10-19 01:15 UTC) gives no restoration time ([ConnectWise, 2026-10-19](https://www.connectwise.com/company/trust/advisories)).

## Improvement — 2026-10-21T03:47:47Z

Sophos X-Ops independently observed the token requests: on 2026-10-15 a single virtual private server authenticated as the ConnectWise Cloud Backup application and requested app-only Microsoft Graph tokens for about 96 minutes, from 07:11 UTC, in strictly ascending tenant-ID order, one to six minutes apart, using Python HTTP-library user agents, and the sweep included tenants with no active backup subscription ([Sophos X-Ops, 2026-10-19](https://www.sophos.com/en-us/blog/connectwise-cloud-backup-application-abused-in-token-sweep)). Sophos found no hands-on-keyboard activity and no evidence that the application created new secrets, applications, consents or role assignments in the tenants it reviewed, which differs from the role grants and added secrets Huntress reports in other tenants; Sophos says it is unclear how the credential was obtained and what was done with the tokens ([Sophos X-Ops, 2026-10-19](https://www.sophos.com/en-us/blog/connectwise-cloud-backup-application-abused-in-token-sweep)). The two vendors' sweep timings differ: Huntress puts the first app sign-ins at 06:13 to 08:34 UTC on 2026-10-15 with tenants taken in sorted GUID order a few seconds apart ([Huntress, 2026-10-16](https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access)), where Sophos gives about 96 minutes from 07:11 UTC, one to six minutes apart; the vantage points differ, so both are reported as stated.

## Update — 2026-10-22T03:46:23Z

Microsoft Threat Intelligence assesses that Storm-0940, a China-state aligned actor active since 2021, was responsible for the compromise. It says AI agents running the ARTEX framework kept signing in to customer tenants as the ConnectWise applications, without an interactive user sign-in, and in multiple tenants went on to Microsoft Graph reconnaissance, application credential changes and attempts to change privileges ([Microsoft, 2026-10-21](https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/)). It counts attempted sign-ins to more than 2,250 tenants and links the activity to an automated cross-tenant password spray between 2026-10-10 and 2026-10-14 against 327 accounts at eight organizations, from the same network range and including an address that ConnectWise's advisory later listed among its indicators; the spray peaked on 2026-10-11 at 2,900 failed logons a minute and produced no successful authentication ([Microsoft, 2026-10-21](https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/)).

Microsoft warns that the application credential changes can remain active as a backdoor after the vendor application is remediated, and asks tenants to review service-principal sign-ins from at least 2026-10-15, and from 2026-10-01 where records exist, together with the Entra audit trail for credential additions, role assignments, consents and owner changes ([Microsoft, 2026-10-21](https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/)). Expel, which analysed the activity separately, relays the attribution, notes that ConnectWise's fix leaves secrets planted on other applications in place and that Graph directory reads leave no Entra audit record, and says Huntress has not tied its Global Administrator observation to the same operator ([Expel, 2026-10-21](https://expel.com/blog/storm-0940-artex-attacks-connectwise-app-abuse-and-okta-sign-ups/)). ConnectWise itself says that, based on the evidence available to it, including threat intelligence shared by Microsoft, it appears a China state-aligned group was responsible and used an openly available agentic AI framework ([ConnectWise, 2026-10-21](https://www.connectwise.com/company/trust/advisories)). It began restoring services in controlled phases on 2026-10-21, expects it to take several days, says the start of restoration does not mean all capabilities are available, and tells partners to keep affected connections disabled until formal instructions apply to their service, while noting that its actions do not remove unauthorized access already established in individual customer tenants ([ConnectWise, 2026-10-21](https://www.connectwise.com/company/trust/advisories); [heise online, 2026-10-21](https://www.heise.de/news/Angriffe-via-ConnectWise-Cloud-Backup-11495835.html)).

## Correction — 2026-10-25T13:43:07Z

The update of 2026-10-22 attached a rate of 2,900 attempts a minute to the ARTEX sign-ins against more than 2,250 tenants. Microsoft gives no rate for those sign-ins: 2,900 a minute is the peak of failed logons in the separate password spray of 10 to 14 October, reached on 11 October ([Microsoft, 2026-10-21](https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/)). The figure now sits with the spray.

## Improvement — 2026-10-27T03:46:02Z

Huntress published its analysis of what drove the 2026-10-15 activity on 2026-10-26, working from Entra sign-in and directory audit logs in the tenants it monitors. It says its telemetry aligns with Microsoft's Storm-0940 and ARTEX account without independently confirming it, that it is highly confident an operator, a person or an LLM, adapted the tooling between runs, and that its confidence that an LLM was involved in the escalation tooling is low to medium on its own telemetry and medium to high once Microsoft's attribution is included ([Huntress, 2026-10-26](https://www.huntress.com/blog/connectwise-attack-ai)). Its evidence for adaptation: a certificate upload that failed on a thumbprint mismatch ended one run with no retry, and the next run 55 seconds later retried the same error with growing waits until it worked; in a second tenant that refused removal of the Global Administrator role, the actor granted a different role to a sibling principal and the original service principal was then deleted ([Huntress, 2026-10-26](https://www.huntress.com/blog/connectwise-attack-ai)). Microsoft Graph reads are not recorded in the Entra audit log and no victim Huntress knows of had Graph activity logging enabled, so a clean audit log does not show that no Graph access took place ([Huntress, 2026-10-26](https://www.huntress.com/blog/connectwise-attack-ai)). Huntress recommends alerting when a service principal assigns itself Global Administrator or Privileged Role Administrator, deletes itself, or when one vendor principal grants a role to a sibling, and turning on Graph activity logs where licensing allows ([Huntress, 2026-10-26](https://www.huntress.com/blog/connectwise-attack-ai)).
