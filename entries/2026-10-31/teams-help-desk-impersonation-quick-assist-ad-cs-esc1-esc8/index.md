---
schema: 1
kind: threat
title: "Teams help-desk impersonation to domain-controller identity: Microsoft traces two intrusions from a Quick Assist session to AD CS ESC1 certificates with DCSync, and to PetitPotam relayed to ESC8 Web Enrollment"
headline: "Microsoft: Teams help-desk vishing into Quick Assist ended in AD CS certificates for privileged accounts and a DC"
summary: >
  Microsoft Threat Intelligence describes two human-operated intrusions, not attributed to any actor, in which an external Teams contact impersonating help-desk staff got a user to open Quick Assist, after which the operator staged a portable runtime and used Active Directory Certificate Services to reach privileged identities: a template open to ESC1 issued certificates for privileged accounts and DCSync followed within seconds, and in the second case PetitPotam was relayed to AD CS Web Enrollment (ESC8) for a certificate for a domain controller account. An issued certificate stays valid after a password reset or a reimage of the first workstation, and in the first case one privileged account excluded from automated containment stayed usable and was used to copy data to an external SFTP destination.
discovered_at: "2026-10-31T03:51:00Z"
updated_at: null
event_date: "2026-10-30"
run_id: 2026-10-31T0256Z-intel
priority: notable
immediate_action: null
tags: [phishing, identity]
regions: [global]
sectors: []
entities: ["product:microsoft-teams", "product:microsoft-quick-assist", "product:microsoft-active-directory-certificate-services", "tool:petitpotam", "tool:rclone"]
techniques: [T1566.003, T1566.004, T1219, T1059.007, T1036.003, T1082, T1016, T1187, T1557, T1649, T1003.006, T1078.002, T1048]
affected_products: ["Microsoft Teams", "Microsoft Quick Assist", "Microsoft Active Directory Certificate Services"]
cves: []
sources:
  - url: "https://www.microsoft.com/en-us/security/blog/2026/10/30/help-desk-impersonation-ad-cs-abuse-investigating-esc1-esc8-intrusion-paths/"
    publisher: "Microsoft Threat Intelligence"
    date: "2026-10-30"
    role: primary
closed_sources: []
evidence:
  - quote: "The activity described here is not attributed to a specific threat actor."
    publisher: "Microsoft Threat Intelligence"
    source_url: "https://www.microsoft.com/en-us/security/blog/2026/10/30/help-desk-impersonation-ad-cs-abuse-investigating-esc1-esc8-intrusion-paths/"
  - quote: "Resetting the user’s password or reimaging the first workstation does not revoke an issued certificate or invalidate Kerberos tickets that have already been issued."
    publisher: "Microsoft Threat Intelligence"
    source_url: "https://www.microsoft.com/en-us/security/blog/2026/10/30/help-desk-impersonation-ad-cs-abuse-investigating-esc1-esc8-intrusion-paths/"
  - quote: "One privileged account was excluded from automated response, so containment did not apply to that identity."
    publisher: "Microsoft Threat Intelligence"
    source_url: "https://www.microsoft.com/en-us/security/blog/2026/10/30/help-desk-impersonation-ad-cs-abuse-investigating-esc1-esc8-intrusion-paths/"
verification: single-source
sourcing_note: >
  Microsoft Threat Intelligence is first-hand on both intrusions, which it investigated for its customers, and no other source covers the AD CS branch; the Teams-to-remote-support entry pattern itself is reported elsewhere. The activity is not attributed to an actor and the number of victim organisations is not stated.
confidence: medium
references: ["2026-09-03/teams-helpdesk-impersonation-nodejs-implant-winrm-dc-pivot"]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "In every forest with an enterprise CA, list the AD CS Web Enrollment and Certificate Enrollment Web Service endpoints that lack HTTPS and Extended Protection for Authentication and the certificate templates that accept requester-supplied identity with broad enrollment rights, because both intrusions turned a Quick Assist session into a certificate for a privileged identity."
updates: []
migrated_from: null
---
Microsoft Threat Intelligence describes two human-operated intrusions, not attributed to any threat actor, that began with an external Teams contact (across the broader activity Microsoft saw organisation-themed tenant names and support-style display names) who persuaded a user to open Quick Assist and read out the connection code; the activity did not exploit a Teams vulnerability. In the session the operator placed an archive in Downloads, extracted it into a newly created KB-prefixed folder under the user profile and started the payload with a portable Python, JavaScript or Java runtime, which ran host and network discovery and assessed AD CS ([Microsoft Threat Intelligence, 2026-10-30](https://www.microsoft.com/en-us/security/blog/2026/10/30/help-desk-impersonation-ad-cs-abuse-investigating-esc1-esc8-intrusion-paths/)).

In the first case a certificate template open to ESC1, where the requester supplies the identity, produced certificates for three privileged accounts, and about 90 minutes later for eight more after a second wave against 16 users; DCSync began within seconds of obtaining one privileged certificate. Defender's automated disruption blocked more than 1,000 SMB attempts, but a privileged account excluded from automated response stayed usable, reached a file server and ran a renamed Rclone that copied a share to an external SFTP destination ([Microsoft Threat Intelligence, 2026-10-30](https://www.microsoft.com/en-us/security/blog/2026/10/30/help-desk-impersonation-ad-cs-abuse-investigating-esc1-esc8-intrusion-paths/)). In the second case the operator used PetitPotam to make a domain controller authenticate to the attacker's host, relayed that NTLM authentication to an AD CS Web Enrollment endpoint, obtained a certificate from the Domain Controller template and used it for PKINIT to get a ticket-granting ticket for the controller's account; Defender raised ESC8 alerts and the customer isolated the workstation ([Microsoft Threat Intelligence, 2026-10-30](https://www.microsoft.com/en-us/security/blog/2026/10/30/help-desk-impersonation-ad-cs-abuse-investigating-esc1-esc8-intrusion-paths/)).

**Exposure:** a forest with an enterprise CA whose authentication-capable templates accept requester-supplied identity with broad enrollment rights (ESC1), or whose Web Enrollment or Certificate Enrollment Web Service endpoints lack HTTPS and Extended Protection (ESC8), where Teams accepts external chats and calls and users can start Quick Assist; Defender for Identity's AD CS posture assessments, or an inventory of /certsrv endpoints and template permissions, shows the first two ([Microsoft Threat Intelligence, 2026-10-30](https://www.microsoft.com/en-us/security/blog/2026/10/30/help-desk-impersonation-ad-cs-abuse-investigating-esc1-esc8-intrusion-paths/)).

**Detection:** new external Teams contacts from help-desk-themed tenants; in process telemetry, a portable runtime started from a freshly created KB-prefixed folder under the user profile after a remote-support session; in CA records, certificate requests and issuances correlated by requester, subject alternative name and template with the first authentication using the certificate; and a domain controller account authenticating to Web Enrollment from a device that is not that controller, which Microsoft calls a strong pivot ([Microsoft Threat Intelligence, 2026-10-30](https://www.microsoft.com/en-us/security/blog/2026/10/30/help-desk-impersonation-ad-cs-abuse-investigating-esc1-esc8-intrusion-paths/)). After containment, revoke the unauthorized certificates and assess issued Kerberos tickets separately; a password reset and a reimage of the first workstation leave both in place.

**Triage:** a help-desk Quick Assist session is routine; what separates this one is an external-tenant initiator with no matching ticket and an interpreter runtime launched from a newly created user-writable folder rather than a managed install path.

**Defender takeaway:** require HTTPS and Extended Protection on every enrollment web endpoint, drop the ones nobody needs, review authentication-capable templates and require approval where enrollment is broad, and enable the Certification Services audit subcategory and CA audit filter; limit Teams external access and restrict remote-support tools to approved ones. Treat a containment exclusion as an incident decision with a manual compensating step, because in the first case the one excluded privileged account was the route to the file server ([Microsoft Threat Intelligence, 2026-10-30](https://www.microsoft.com/en-us/security/blog/2026/10/30/help-desk-impersonation-ad-cs-abuse-investigating-esc1-esc8-intrusion-paths/)).
