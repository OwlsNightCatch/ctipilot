---
schema: 1
kind: threat
title: "M365 token spray and replay: Huntress tracks a 10-week campaign that replays stolen post-MFA tokens from rented hosting within minutes, registers rogue Entra devices, wipes and re-registers MFA methods and hides mail with inbox rules of one to three characters or punctuation only"
headline: "Huntress: stolen post-MFA M365 tokens replayed within minutes; a password reset leaves planted devices and MFA methods"
summary: >
  Huntress reports that between 2026-07-14 and 2026-09-22 it detected 497 Microsoft 365 sign-in events in 79 organizations that
  replayed tokens stolen through adversary-in-the-middle relays, device-code phishing and social engineering, within minutes
  of capture and from one rented hosting range. The operators then registered rogue Entra devices, wiped and replaced MFA methods in
  19 organizations and hid mail with inbox rules; a password reset alone removes none of it.
discovered_at: "2026-10-23T03:39:00Z"
updated_at: null
event_date: "2026-10-22"
run_id: 2026-10-23T0256Z-intel
priority: notable
immediate_action: null
tags: [phishing, identity, cloud]
regions: [global]
sectors: []
entities: ["campaign:m365-token-spray-replay-huntress-2026", "product:microsoft-entra-id", "product:microsoft-365", "product:microsoft-exchange-online", "product:microsoft-sharepoint-online"]
techniques: [T1557, T1566.002, T1550.001, T1078.004, T1098.005, T1556.006, T1564.008, T1090.003]
affected_products: ["Microsoft Entra ID", "Microsoft 365", "Microsoft Exchange Online", "Microsoft SharePoint Online"]
cves: []
sources:
  - url: "https://www.huntress.com/blog/token-replay-spray"
    publisher: "Huntress"
    date: "2026-10-22"
    role: primary
closed_sources: []
evidence:
  - quote: "Between July 14, 2026 and September 22, 2026, Huntress detected 497 Microsoft 365 sign-in events across 79 victim organizations related to a token replay campaign"
    publisher: "Huntress"
    source_url: "https://www.huntress.com/blog/token-replay-spray"
  - quote: "In 19 organizations, the victim's existing MFA methods were wiped and a new method registered within three hours of the first sign-in from a campaign address."
    publisher: "Huntress"
    source_url: "https://www.huntress.com/blog/token-replay-spray"
  - quote: "A password reset alone does not remove attacker-registered devices or MFA methods."
    publisher: "Huntress"
    source_url: "https://www.huntress.com/blog/token-replay-spray"
verification: single-source
sourcing_note: >
  Huntress is the only source; every count comes from its own incident telemetry. Huntress also states that Microsoft Entra ID
  Protection independently flagged several of the replay addresses, which is Huntress's statement and not
  a Microsoft one. Huntress names no victim, sector or country, and none of the attacker infrastructure is reproduced here.
confidence: medium
references: ["2026-10-18/connectwise-cloud-backup-skykick-m365-app-credential-abuse", "2026-10-19/ics-calendar-invite-phishing-auto-added-outlook-gmail", "2026-10-22/artex-storm-0940-agentic-llm-pentest-spraying-oauth-abuse"]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "In every Entra tenant, list the devices registered since 2026-07-14 whose names are DESKTOP- followed by eight uppercase hexadecimal characters, the authenticators that were deleted and re-registered within minutes, and the inbox rules whose names are one to three characters or punctuation only or that move mail to RSS Feeds, RSS Subscriptions or Conversation History, and remove what nobody created; then revoke the sessions of any affected user, because a password reset leaves the devices, MFA methods and a roughly 90-minute access token in place."
updates: []
migrated_from: null
---
Between 2026-07-14 and 2026-09-22 Huntress detected 497 Microsoft 365 sign-in events across 79 victim organizations that replayed stolen sign-in tokens instead of guessing passwords ([Huntress, 2026-10-22](https://www.huntress.com/blog/token-replay-spray)). The tokens came from adversary-in-the-middle relays behind fake sign-in pages, from device-code phishing and from social engineering during a genuine sign-in; a relay passes the real login page and MFA prompt through and keeps the token Microsoft issues afterwards, so its holder does not face MFA again ([Huntress, 2026-10-22](https://www.huntress.com/blog/token-replay-spray)). Replay followed within minutes, after 12 minutes on 2026-07-21 and four minutes on 2026-09-22, from one of six addresses in a single rented range used in turn, so blocking one address stops at most one phase ([Huntress, 2026-10-22](https://www.huntress.com/blog/token-replay-spray)).

A scripted replayer with the user agent `node` requests tokens with the Microsoft Office and Microsoft Authentication Broker client applications against Microsoft Graph, Exchange Online, SharePoint Online and the Device Registration Service and joins 48 rogue Entra devices named DESKTOP- plus exactly eight uppercase hexadecimal characters, where the Windows default is seven alphanumeric characters; a browser-session replayer uses current Chrome or Edge through the OfficeHome client ([Huntress, 2026-10-22](https://www.huntress.com/blog/token-replay-spray)). What outlives a password reset is the persistence: in 19 organizations the victim's MFA methods were wiped and a new authenticator registered within three hours, the rogue devices stay in the directory until deleted, and hidden inbox rules with names of one to three characters or punctuation only, created from VPN or other rented addresses, moved mail to RSS Feeds, RSS Subscriptions or Conversation History or deleted it, one keyed on payroll and bank terms ([Huntress, 2026-10-22](https://www.huntress.com/blog/token-replay-spray)). Conditional Access blocks reported as AADSTS53003 fire only after authentication has succeeded, so they signal a valid credential, and ranking tenants by failed attempts points responders at the wrong ones ([Huntress, 2026-10-22](https://www.huntress.com/blog/token-replay-spray)).

**Exposure:** any Entra tenant where users can sign in to Microsoft 365 from unmanaged networks and Conditional Access does not require MFA or block for all users, all cloud apps and all client app types unconditionally, or where the device-code flow is open; Huntress names no victim, sector or country ([Huntress, 2026-10-22](https://www.huntress.com/blog/token-replay-spray)).

**Detection:** in Entra sign-in logs, OAuth2:Token and Cmsi:Cmsi requests from hosting infrastructure that use the Microsoft Office or Authentication Broker client with a `node` or bare `Mozilla/5.0` user agent, above all those that touch user mailboxes or the Device Registration Service; in the Entra audit log, device registrations from hosting addresses with the DESKTOP-plus-eight-hex name shape and MFA methods deleted and re-added within minutes; in Exchange audit data, inbox rules with the short names described above, especially created through the REST API ([Huntress, 2026-10-22](https://www.huntress.com/blog/token-replay-spray)).

**Triage:** a `node` user agent with an Office client identifier can be legitimate automation, so Huntress focuses on sign-ins that touch user mailboxes or the Device Registration Service from hosting infrastructure, and it says the device-name pattern is rare but not unique to this campaign, so a device should be confirmed before it is deleted ([Huntress, 2026-10-22](https://www.huntress.com/blog/token-replay-spray)).

**Defender takeaway:** revoke sessions as well as resetting the password, because the access token lives about 90 minutes after a reset, then audit devices, MFA methods, inbox rules and newly consented enterprise applications; as controls, require MFA or block for all users, all cloud apps and all client app types unconditionally, restrict the device-code flow with authentication-flow policies, and disable user consent to new applications ([Huntress, 2026-10-22](https://www.huntress.com/blog/token-replay-spray)).
