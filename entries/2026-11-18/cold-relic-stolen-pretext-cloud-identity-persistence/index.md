---
schema: 1
kind: threat
title: "COLD RELIC: Mandiant shows the FSB-linked group reusing data stolen from one US organisation as the impersonation pretext for the next, then holding cloud tenants through MFA push fatigue and enrolled passkeys, backup codes and MFA devices that survive password and session resets"
headline: "Mandiant: COLD RELIC turns one cloud compromise into the pretext for the next; enrolled passkeys outlive password resets"
summary: >
  Mandiant reports that COLD RELIC, the name Google Threat Intelligence Group now uses for the group formerly tracked as COLDRIVER and UNC4057 (Star Blizzard), reused the staff directory and identities stolen from one US organisation in late 2025 to impersonate a contact when approaching a second in 2026. In the late-2025 case it took over a Super Admin account through push-notification fatigue, kept access with enrolled passkeys, MFA backup codes and rogue MFA devices that survived password and session resets, and exported the whole tenant; in 2026 it phished Entra ID credentials and registered a new MFA device to download one user's drive. GTIG names government officials, defense contractors and NGOs in Europe and North America as targets and says new phishing operations continued into November 2026.
discovered_at: "2026-11-18T05:05:00Z"
updated_at: null
event_date: "2026-11-17"
run_id: 2026-11-18T0356Z-intel
priority: notable
immediate_action: null
tags: [nation-state, espionage, phishing, identity, cloud, russia-nexus]
regions: [us, europe]
sectors: [public-sector, defense]
entities: ["actor:star-blizzard"]
techniques: [T1566.002, T1621, T1078.004, T1098.005, T1114.002, T1528, T1530, T1119, T1567.002, T1087.004, T1083, T1552.001, T1685.002]
affected_products: ["Google Workspace", "Microsoft Entra ID"]
cves: []
sources:
  - url: "https://cloud.google.com/blog/topics/threat-intelligence/cold-relic-a-case-study-in-impersonation-and-compromise/"
    publisher: "Google Threat Intelligence Group and Mandiant"
    date: "2026-11-17"
    role: primary
closed_sources: []
evidence:
  - quote: "COLD RELIC is a Russian state-sponsored threat group that the US Department of Justice (DOJ) has assessed operates within Russia's Federal Security Service (FSB)."
    publisher: "Google Threat Intelligence Group and Mandiant"
    source_url: "https://cloud.google.com/blog/topics/threat-intelligence/cold-relic-a-case-study-in-impersonation-and-compromise/"
  - quote: "COLD RELIC leveraged passkeys, MFA backup codes, and rogue MFA devices to retain access throughout the intrusion."
    publisher: "Google Threat Intelligence Group and Mandiant"
    source_url: "https://cloud.google.com/blog/topics/threat-intelligence/cold-relic-a-case-study-in-impersonation-and-compromise/"
  - quote: "Reauthentication using unrevoked attacker-enrolled passkeys that persisted across password and session resets and bypassed device registration controls"
    publisher: "Google Threat Intelligence Group and Mandiant"
    source_url: "https://cloud.google.com/blog/topics/threat-intelligence/cold-relic-a-case-study-in-impersonation-and-compromise/"
verification: single-source
sourcing_note: >
  Single source: Mandiant's and GTIG's own incident-response findings, with no independent coverage found. The FSB statement is GTIG's paraphrase of a US Department of Justice assessment that was not checked against the DOJ page, and GTIG publishes no infrastructure or malware overlap that ties the two intrusions to the cluster, so the cluster assignment rests on tradecraft and on GTIG's say-so.
confidence: medium
references: ["2026-09-30/star-blizzard-redflick-cosmicpulse-single-click-chain"]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "In every Google Workspace and Entra ID tenant you run, search the administrator and sign-in logs for passkey, backup-code and MFA-device enrolments on privileged accounts and for tenant-wide Customer Takeout exports, because COLD RELIC's enrolled authenticators survived password and session resets."
updates: []
migrated_from: null
---

Mandiant reports a series of linked intrusions in which COLD RELIC, the name Google Threat Intelligence Group (GTIG) now uses for the group formerly tracked as COLDRIVER and UNC4057 (also Star Blizzard, Callisto and Gossamer Bear), turned data stolen in one US organisation into the pretext for the next ([GTIG, 2026-11-17](https://cloud.google.com/blog/topics/threat-intelligence/cold-relic-a-case-study-in-impersonation-and-compromise/)). GTIG cites a US Department of Justice assessment that the group operates within Russia's FSB and names government officials, defense contractors and NGOs in Europe and North America among its targets ([GTIG, 2026-11-17](https://cloud.google.com/blog/topics/threat-intelligence/cold-relic-a-case-study-in-impersonation-and-compromise/)). In 2026 the operators approached a second US organisation over an encrypted messaging app while impersonating an employee of the first, shared phishing links that stole Entra ID credentials and tokens and sent the victim on to document lures matching the conversation, and registered a new MFA device on the account ([GTIG, 2026-11-17](https://cloud.google.com/blog/topics/threat-intelligence/cold-relic-a-case-study-in-impersonation-and-compromise/)).

In the late-2025 case the operators used the stolen credentials of a Super Admin account from a US residential proxy network close to the victim, pressed the user with MFA push notifications until one was accepted, registered a device model new to the tenant and kept access with passkeys, MFA backup codes and rogue MFA devices ([GTIG, 2026-11-17](https://cloud.google.com/blog/topics/threat-intelligence/cold-relic-a-case-study-in-impersonation-and-compromise/)). They took the whole cloud drive by mass sharing to an operator-run mailbox and by direct download, queried the admin investigation and email audit logs to check defensive visibility, viewed, modified and deleted Alert Center notifications, exported the employee list and ran a tenant-wide Customer Takeout export ([GTIG, 2026-11-17](https://cloud.google.com/blog/topics/threat-intelligence/cold-relic-a-case-study-in-impersonation-and-compromise/)). Access lasted several months through OAuth mail sync to an external client and re-authentication with enrolled passkeys that survived password and session resets, and in one case a password reset without revoking sessions did not evict the operators ([GTIG, 2026-11-17](https://cloud.google.com/blog/topics/threat-intelligence/cold-relic-a-case-study-in-impersonation-and-compromise/)). They searched for credentials, personnel data and .pst archives ([GTIG, 2026-11-17](https://cloud.google.com/blog/topics/threat-intelligence/cold-relic-a-case-study-in-impersonation-and-compromise/)).

**Exposure:** Google Workspace tenants, and Entra ID tenants that federate sign-in to Workspace as in the second case, whose privileged or staff accounts accept push, SMS or voice MFA or let users enrol passkeys, backup codes and devices without a second approval ([GTIG, 2026-11-17](https://cloud.google.com/blog/topics/threat-intelligence/cold-relic-a-case-study-in-impersonation-and-compromise/)).

**Detection:** in authentication logs, repeated failed logins or MFA challenges followed by a success from the same address, privileged sign-ins from residential-proxy networks that geolocate near the user, logins with a backup code, and new passkey or device registrations. In administrator audit logs, Customer Takeout creation, user-list downloads, audit-log investigation queries and Alert Center batch deletions. In Drive and OAuth logs, download spikes, external sharing to free mail providers, and authorisations of broad mail scopes to unapproved clients such as Thunderbird or Proton ([GTIG, 2026-11-17](https://cloud.google.com/blog/topics/threat-intelligence/cold-relic-a-case-study-in-impersonation-and-compromise/)). After a compromise, password changes alone are insufficient: revoke all sessions, refresh tokens and third-party OAuth permissions and remove unauthorised passkeys, backup codes and MFA devices ([GTIG, 2026-11-17](https://cloud.google.com/blog/topics/threat-intelligence/cold-relic-a-case-study-in-impersonation-and-compromise/)).

**Triage:** a directory export, a Customer Takeout or a passkey or device enrolment by an administrator can be routine; the cues in GTIG's account are an unfamiliar device, a non-corporate or residential-proxy network, or an enrolment right after an MFA-fatigue pattern ([GTIG, 2026-11-17](https://cloud.google.com/blog/topics/threat-intelligence/cold-relic-a-case-study-in-impersonation-and-compromise/)).

**Defender takeaway:** move administrators and exposed staff to FIDO2 or WebAuthn hardware keys, which GTIG says cannot be approved through fatigue or intercepted by reverse proxies, require existing-administrator or out-of-band approval for new MFA devices and passkeys, and write session and OAuth revocation into compromise playbooks ([GTIG, 2026-11-17](https://cloud.google.com/blog/topics/threat-intelligence/cold-relic-a-case-study-in-impersonation-and-compromise/)).
