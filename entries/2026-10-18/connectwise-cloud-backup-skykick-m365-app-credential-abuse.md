---
schema: 1
kind: incident
title: "ConnectWise Cloud Backup (formerly SkyKick): the vendor's Microsoft 365 application credential was used to sign in to customer tenants, with directory-role self-assignments in about 50 tenants and added credentials in one"
headline: "ConnectWise SkyKick app credential used in 162+ Microsoft 365 tenants; disabling it does not undo planted access"
summary: >
  ConnectWise says it identified unauthorized access to application identities of its Cloud Backup (formerly SkyKick) service; Huntress and Todyl report that from 15 October the app's credential was used to obtain app-only Microsoft Graph tokens in customer Microsoft 365 tenants; Huntress alone confirmed unauthorized sign-ins in 162 tenants by 16 October and saw ConnectWise Cloud Management apps assign themselves directory roles in about 50 tenants and, in one, new client secrets added to other applications. ConnectWise disabled seven application identities and suspended the service on 17 October, but says disabling does not reverse changes already made in a tenant, so every tenant that ever consented a ConnectWise or SkyKick app needs the apps disabled and its application credentials, directory roles and consents reviewed. How the credential was obtained, who is behind it and what data was read are not public.
discovered_at: "2026-10-18T03:30:00Z"
updated_at: null
event_date: "2026-10-15"
run_id: 2026-10-18T0256Z-intel
priority: high
immediate_action: null
tags: [supply-chain, cloud, identity, actively-exploited]
regions: [global]
sectors: [technology]
entities: ["incident:connectwise-cloud-backup-skykick-app-credential-abuse-2026-10", "product:connectwise-cloud-backup", "product:connectwise-cloud-management", "product:microsoft-entra-id"]
techniques: [T1199, T1078.004, T1098.003, T1098.001, T1110.003]
affected_products: ["ConnectWise Cloud Backup", "ConnectWise Cloud Management", "Microsoft Entra ID"]
cves: []
sources:
  - url: "https://www.connectwise.com/company/trust/advisories"
    publisher: "ConnectWise Trust Center (advisory)"
    date: "2026-10-18"
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
closed_sources: []
evidence:
  - quote: "We recently identified unauthorized access to application identities within the ConnectWise Cloud Backup environment."
    publisher: "ConnectWise Trust Center (advisory)"
    source_url: "https://www.connectwise.com/company/trust/advisories"
  - quote: "Disabling the affected connections prevents new authentication through those connections; it does not reverse changes previously made inside a tenant."
    publisher: "ConnectWise Trust Center (advisory)"
    source_url: "https://www.connectwise.com/company/trust/advisories"
  - quote: "Whether a product vulnerability contributed has not been established."
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
verification: multi-source
sourcing_note: >
  ConnectWise is the first-party source for its own incident, and Huntress and Todyl each observed the sign-ins in tenants they monitor. Microsoft's statement is a social-media post that BleepingComputer relays, and ConnectWise's advisory page carries the dated updates, the latest of 2026-10-18 01:00 UTC, while Huntress and Todyl run living posts updated after the dates given.
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
  - "In every Entra tenant you or your MSP administer, find the seven ConnectWise application identities by client ID (Cloud Backup is 506e08f9-6e9a-4da4-942b-a099a03644ae; the other six are in ConnectWise's advisory), dormant SkyKick connections included, and disable them without deleting, then keep them disabled until ConnectWise gives restoration instructions; preserve the sign-in and audit logs promptly without delaying containment, because Entra ID Free keeps only 7 days."
  - "In the same tenants review every enterprise application and app registration, MSP management and security tools first, for client secrets, certificates and federated credentials added since 2026-10-13 and remove any you did not create; also check the directory roles, owners and consent grants held by ConnectWise and SkyKick service principals, Conditional Access exclusions for them, and mailbox forwarding, inbox and transport rules and delegated access, because disabling the vendor applications does not remove access planted through them."
updates: []
migrated_from: null
---

ConnectWise says it identified unauthorized access to application identities within its Cloud Backup (formerly SkyKick) environment; on 2026-10-17 it disabled seven application identities, suspended the service, says the shared Cloud Backup credentials are no longer valid, and warns that disabling does not reverse changes already made in a tenant ([ConnectWise, 2026-10-18](https://www.connectwise.com/company/trust/advisories)). Huntress and Todyl report that on 2026-10-15 the app's identity signed in to customer Microsoft 365 tenants from one hosting-provider address and received app-only Microsoft Graph tokens; the credential sits in the vendor's own tenant, so no user, MFA prompt or user Conditional Access was involved, and the app's consent covers read and write access to mail, files and Teams chats ([Huntress, 2026-10-16](https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access); [Todyl, 2026-10-15](https://www.todyl.com/blog/investigation-unauthorized-access-through-the-connectwise-cloud-backup-microsoft-365-app)). Huntress confirmed unauthorized sign-ins in 162 tenants by 2026-10-16 and later counted almost 1,000 tenants with sign-in activity from that address, over 300 successful, after password spraying against four law-firm tenants on 13 and 14 October, and a separate failed wave targeted 16 tenants in policy and national-security sectors ([Huntress, 2026-10-16](https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access)). In about 50 of its tenants, ConnectWise Cloud Management apps assigned themselves directory roles, mostly Exchange Administrator; in one the Teams app added itself to Global Administrator and client secrets were added to an MSP management application and to Huntress's own application within about five minutes, the credential additions from private Azure space ([Huntress, 2026-10-16](https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access)). Microsoft Threat Intelligence, as BleepingComputer relays it, called it an active supply-chain attack and assessed likely abuse of existing permissions including Directory.ReadWrite.All ([BleepingComputer, 2026-10-17](https://www.bleepingcomputer.com/news/security/hackers-breach-microsoft-365-tenants-via-connectwise-supply-chain-attack/)). How the credential was obtained, who is behind it and what was read remain unknown ([ConnectWise, 2026-10-18](https://www.connectwise.com/company/trust/advisories); [BleepingComputer, 2026-10-17](https://www.bleepingcomputer.com/news/security/hackers-breach-microsoft-365-tenants-via-connectwise-supply-chain-attack/)).

**Exposure:** every Entra tenant, including each customer tenant an MSP manages, in which a ConnectWise or SkyKick Cloud Backup or Cloud Management app was ever consented, dormant connections included; ConnectWise lists seven application client IDs, among them Cloud Backup (506e08f9-6e9a-4da4-942b-a099a03644ae), and says to match on client ID ([ConnectWise, 2026-10-18](https://www.connectwise.com/company/trust/advisories)).

**Detection:** Entra service-principal sign-in logs for these apps from any address outside Microsoft and Azure ranges, which misses the credential additions, made from private Azure space ([Huntress, 2026-10-16](https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access)); directory audit events Add member to role, Update application and Add service principal credentials initiated by a ConnectWise or SkyKick app ([Huntress, 2026-10-16](https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access)); Graph activity logs (Entra ID P1 or P2, not retroactive) for per-request source addresses ([Todyl, 2026-10-15](https://www.todyl.com/blog/investigation-unauthorized-access-through-the-connectwise-cloud-backup-microsoft-365-app)); and mailbox forwarding, inbox and transport rule and delegation changes ([ConnectWise, 2026-10-18](https://www.connectwise.com/company/trust/advisories)). Disabling the apps does not remove credentials, roles or consents already planted, and revoking user sessions does not end this access ([ConnectWise, 2026-10-18](https://www.connectwise.com/company/trust/advisories); [Todyl, 2026-10-15](https://www.todyl.com/blog/investigation-unauthorized-access-through-the-connectwise-cloud-backup-microsoft-365-app)).

**Triage:** the vendor's apps sign in from Azure addresses with a .NET SDK user agent, while the credential additions used a Python user agent; Python and curl are common in administration, so Huntress says the combination of actor, operation and user agent is the signal ([Huntress, 2026-10-16](https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access)). Role self-assignments carrying the vendor's own user agent are not proven benign, since Huntress has not confirmed vendor automation ([Huntress, 2026-10-16](https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access)).

**Defender takeaway:** where any ConnectWise or SkyKick app is consented, disable it by client ID without deleting it, keep it disabled until ConnectWise gives restoration instructions, and review credentials, roles, owners, consents and Conditional Access exclusions since 13 October ([ConnectWise, 2026-10-18](https://www.connectwise.com/company/trust/advisories); [Huntress, 2026-10-16](https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access)). An MSP should review its own management and security tools first, since a foothold there can reach its customers ([Huntress, 2026-10-16](https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access)).
