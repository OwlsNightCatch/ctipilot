---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-top-stories
title: "Two independently-operating Russian state clusters converged this week on the government user's mailbox and the government user's travel — and both leave persistence that a patch or a password reset does not remove"
headline: "Russian state clusters hit government mail and government travellers in W31 — eviction needs a hunt, not a patch"
summary: >
  Two disclosures inside 2026-W31 describe distinct Russian state-nexus clusters reaching the same population —
  government and diplomatic staff — by different routes. Proofpoint attributed active exploitation of the
  Outlook Web Access stored-XSS flaw CVE-2026-42897 to LAUNDRY BEAR, delivering OWAReaper, a JavaScript
  implant that runs in the reading pane with no file on the host and grants the Exchange "Default" alias Owner
  permission on every mail folder. Microsoft disclosed CaptiveCrunch, attributed to Storm-2945, which has
  manipulated DNS and HTTP traffic on hospitality captive portals worldwide since early May 2026 to serve fake
  update prompts delivering a Go RAT and an in-memory token stealer. The common shape is what defenders must
  act on: server-side mailbox permissions and a self-restoring persistence watchdog both survive credential
  rotation and device re-imaging, so eviction is an active hunt for the artifact rather than an update.
discovered_at: "2026-08-02T23:46:00Z"
event_date: "2026-07-31"
run_id: 2026-08-02T2311Z-weekly
priority: high
immediate_action: null
tags: [nation-state, espionage, actively-exploited, cisa-kev, zero-click, phishing, identity, cloud, russia-nexus]
regions: [europe, switzerland, global]
sectors: [public-sector, defense]
entities:
  - actor:laundry-bear
  - actor:storm-2945
  - actor:midnight-blizzard
  - campaign:captivecrunch-storm-2945-hospitality-wifi
  - tool:owareaper
  - malware:cornflake-go-rat
  - tool:chocoshell-powershell-stealer
techniques: [T1566, T1203, T1185, T1098.002, T1550.001, T1557, T1204.004, T1539, T1528, T1543.003, T1053.005]
affected_products: ["Microsoft Exchange Server", "Microsoft Entra ID"]
cves: []
sources:
  - url: "https://www.proofpoint.com/us/blog/threat-insight/cleaning-out-inboxes-ta488-comes-outlook-another-half-click-exploit"
    publisher: "Proofpoint"
    date: "2026-07-29"
    role: primary
  - url: "https://www.microsoft.com/en-us/security/blog/2026/07/31/captivecrunch-midnight-blizzard-targets-travelers-worldwide-for-malware-delivery-and-credential-theft/"
    publisher: "Microsoft Threat Intelligence"
    date: "2026-07-31"
    role: primary
  - url: "https://techcommunity.microsoft.com/blog/exchange/released-july-2026-exchange-server-security-updates/4534146"
    publisher: "Microsoft Exchange Team Blog"
    date: "2026-07-14"
    role: primary
  - url: "https://reliaquest.com/blog/threat-spotlight-dns-poisoning-tactics-expand-to-hospitality/"
    publisher: "ReliaQuest"
    date: "2026-07-23"
    role: corroborating
  - url: "https://security-hub.ncsc.admin.ch/#/posts/12577"
    publisher: "NCSC Switzerland — Cyber Security Hub"
    date: "2026-07-30"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The messages exploit CVE-2026-42897, a vulnerability in Outlook Web Access in which the server does not adequately sanitize HTML in the message body. This allows a loader piece of JavaScript to use the onload= event handler to parse the rest of the message body, assemble a Base64 fragment, and execute it as encoded JavaScript."
    publisher: "Proofpoint"
  - quote: "This persistent access lives on the server-side and requires deliberate removal from the Exchange server; credential rotation and even full re-imaging of the targeted user's device will not evict the actor."
    publisher: "Proofpoint"
  - quote: "Microsoft Threat Intelligence assesses that Storm-2945 is an operational sub-cluster of Midnight Blizzard based on distinctive technical and operational overlaps."
    publisher: "Microsoft Threat Intelligence"
  - quote: "It establishes redundant persistence mechanisms: Windows service registrations, Registry Run keys, named scheduled tasks, and a persistence watchdog routine that runs continuously to restore any persistence mechanism that is removed by defenders or endpoint protection."
    publisher: "Microsoft Threat Intelligence"
  - quote: "Additionally, ChocoShell collects Microsoft 365 and Azure Active Directory (AD) access tokens, refresh tokens, and Web Account Manager (WAM) tokens from .tbres files in the Token Broker cache. Collection of these tokens represents a significant threat to enterprise environments, as threat actors could replay SSO sessions without browser cookies."
    publisher: "Microsoft Threat Intelligence"
verification: multi-source
sourcing_note: >
  The two clusters are held DISTINCT and each claim is cited to the party that makes it. The OWA exploitation,
  the OWAReaper mechanics and the server-side-persistence consequence are Proofpoint's; the Storm-2945
  sub-cluster assessment, the CornFlake persistence watchdog and the ChocoShell token collection are
  Microsoft's. Microsoft's stated assessment is that Storm-2945 is an operational sub-cluster of Midnight
  Blizzard on the basis of technical and operational overlaps — this entry does not extend that into a
  service attribution, which the cited sentence does not carry. LAUNDRY BEAR carries TA488 as a registry
  alias; it is NOT the same actor as TA458 (Operation RoundPress), which a prior weekly recorded as separate
  on Proofpoint's own statement, and no claim here is transferred between them.
confidence: high
update_of: null
references:
  - 2026-05-18/cve-2026-42897-exchange-owa-em-service-auto-mitigation-depen
  - 2026-08-01/captivecrunch-storm-2945-hospitality-captive-portal-rat
  - 2026-07-10/m365-conditional-access-gaps-railway-lshiy-campaigns
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: null
---

**If you did nothing this week:** if you run Exchange on premises, a mailbox in your estate may be readable by an actor who no longer needs anyone's password; and if your staff travelled and used hotel or conference Wi-Fi since early May, their session tokens may already be replayable from somewhere else.

The two disclosures are unrelated in operator and identical in target logic. Proofpoint attributed active exploitation of CVE-2026-42897 to LAUNDRY BEAR, describing a flaw where "the server does not adequately sanitize HTML in the message body", allowing "a loader piece of JavaScript to use the onload= event handler to parse the rest of the message body, assemble a Base64 fragment, and execute it as encoded JavaScript" ([Proofpoint, 2026-07-29](https://www.proofpoint.com/us/blog/threat-insight/cleaning-out-inboxes-ta488-comes-outlook-another-half-click-exploit)). Opening the message in Outlook Web Access is the whole of the victim interaction. The resulting implant, OWAReaper, is browser-resident with no artifact on the endpoint, and its persistence mechanism is the part that outlasts incident response: it grants the Exchange "Default" alias Owner permission across mail folders, which Proofpoint states plainly means "this persistent access lives on the server-side and requires deliberate removal from the Exchange server; credential rotation and even full re-imaging of the targeted user's device will not evict the actor" ([Proofpoint, 2026-07-29](https://www.proofpoint.com/us/blog/threat-insight/cleaning-out-inboxes-ta488-comes-outlook-another-half-click-exploit)). Only on-premises Exchange is in scope, and the permanent fix is the July 2026 Exchange Security Update — which Microsoft notes does not automatically remove the mitigations an administrator applied earlier for the same CVE ([Microsoft Exchange Team, 2026-07-14](https://techcommunity.microsoft.com/blog/exchange/released-july-2026-exchange-server-security-updates/4534146)). NCSC Switzerland carried the exploitation to its own constituency on 2026-07-30 ([NCSC Switzerland, 2026-07-30](https://security-hub.ncsc.admin.ch/#/posts/12577)).

Microsoft's disclosure moves the same targeting to the travel path. It states that "Microsoft Threat Intelligence assesses that Storm-2945 is an operational sub-cluster of Midnight Blizzard based on distinctive technical and operational overlaps" ([Microsoft Threat Intelligence, 2026-07-31](https://www.microsoft.com/en-us/security/blog/2026/07/31/captivecrunch-midnight-blizzard-targets-travelers-worldwide-for-malware-delivery-and-credential-theft/)). Since early May the cluster has manipulated DNS and HTTP traffic on hospitality networks served by captive portals, answering the browser's own automatic connectivity check with a fake browser or operating-system update prompt — so the lure fires before the user has browsed anywhere. The payloads are built to be difficult to remove and valuable to keep: CornFlake, a Go Windows RAT, "establishes redundant persistence mechanisms: Windows service registrations, Registry Run keys, named scheduled tasks, and a persistence watchdog routine that runs continuously to restore any persistence mechanism that is removed by defenders or endpoint protection" ([Microsoft Threat Intelligence, 2026-07-31](https://www.microsoft.com/en-us/security/blog/2026/07/31/captivecrunch-midnight-blizzard-targets-travelers-worldwide-for-malware-delivery-and-credential-theft/)), while ChocoShell, an in-memory PowerShell stealer, "collects Microsoft 365 and Azure Active Directory (AD) access tokens, refresh tokens, and Web Account Manager (WAM) tokens from .tbres files in the Token Broker cache", which Microsoft assesses lets actors "replay SSO sessions without browser cookies" ([Microsoft Threat Intelligence, 2026-07-31](https://www.microsoft.com/en-us/security/blog/2026/07/31/captivecrunch-midnight-blizzard-targets-travelers-worldwide-for-malware-delivery-and-credential-theft/)). Independent research into the same tradecraft class found compromised Wi-Fi gateways "across multiple US cities and internationally in India and Saudi Arabia, primarily in hotel and hospitality organizations" ([ReliaQuest, 2026-07-23](https://reliaquest.com/blog/threat-spotlight-dns-poisoning-tactics-expand-to-hospitality/)).

The identity layer is where the two paths rejoin, and where a third in-window development sharpens the picture: some CaptiveCrunch landing pages have driven users into the Entra ID device-code authentication flow since 16 July ([Microsoft Threat Intelligence, 2026-07-31](https://www.microsoft.com/en-us/security/blog/2026/07/31/captivecrunch-midnight-blizzard-targets-travelers-worldwide-for-malware-delivery-and-credential-theft/)), the same flow a separate criminal operation ran a fresh wave of this week from commercially-trusted hosting infrastructure. A stolen refresh or WAM token and a mailbox-folder permission grant have the same property: both are authorisations rather than credentials, so the standard incident response of resetting the password and rebuilding the laptop closes neither.

**Defender takeaway:** for a government or public-sector estate the two concrete exposures are self-hosted Exchange and staff travel, and in both cases the remediation is an eviction hunt with a defined artifact to look for. On Exchange, that means auditing mailbox folder permissions for Owner-level grants to the "Default" alias across the estate rather than trusting the update, and removing the older mitigation the July update leaves behind. On the travel side, it means treating token material as compromised for anyone who used venue Wi-Fi in the window and revoking refresh tokens rather than resetting passwords — a password reset does not invalidate a refresh token already in an attacker's hands.

**Triage:** the OWA case produces no endpoint artifact at all, so process-level telemetry will be silent; the signal is server-side, in mailbox-permission change events granting rights to the "Default" alias and in add-in or OAuth grants appearing on accounts that never installed one. For the travel case, the discriminator is sequence and location rather than the update prompt itself — a browser or OS update package fetched moments after a device associated with a new wireless network, from a host that is not the vendor's update infrastructure, with the connectivity-check request immediately preceding it. The lure's mechanics give a second, sharper signal: these are paste-and-run instructions, so Microsoft's own guidance is to teach users to recognise ClickFix-style prompts and fake verification checks "especially when they invoke command interpreters or script hosts such as cmd.exe, PowerShell, rundll32.exe, or mshta.exe" ([Microsoft Threat Intelligence, 2026-07-31](https://www.microsoft.com/en-us/security/blog/2026/07/31/captivecrunch-midnight-blizzard-targets-travelers-worldwide-for-malware-delivery-and-credential-theft/)) — so a script host spawned from a browser process shortly after a captive-portal association is the process-lineage version of the same test. On the collection side, CornFlake carries a ChromeKatz-derived module doing live cookie extraction from Chromium process memory and stored-password extraction from on-disk databases, including an App-Bound Encryption bypass and Firefox NSS decryption ([Microsoft Threat Intelligence, 2026-07-31](https://www.microsoft.com/en-us/security/blog/2026/07/31/captivecrunch-midnight-blizzard-targets-travelers-worldwide-for-malware-delivery-and-credential-theft/)); a non-browser process reading a browser's credential store or its live memory is the detectable artifact, and it sits alongside the token theft rather than replacing it. On the identity side, a successful sign-in whose token was minted through the device-code flow for a user whose role never requires it, or an SSO session replayed from an address class inconsistent with the user's own context, is the shape both clusters ultimately produce.
