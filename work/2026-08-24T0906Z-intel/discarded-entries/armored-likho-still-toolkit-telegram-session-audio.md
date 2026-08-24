---
schema: 1
kind: threat
horizon: operational
title: "Armored Likho's Still Toolkit: a stealer that logs in to the victim's Telegram account with the stolen session, and an audio implant that decides for itself when someone is speaking"
headline: "Two Rust implants on one channel — a stolen session folder becomes live API access to every chat, and the audio module records only when it hears a voice"
summary: >
  Kaspersky GReAT documented a new Armored Likho campaign on 2026-08-13 distributing a Rust dropper disguised as a
  charitable-donation app, which delivers a previously unseen two-part toolkit. Still Sync steals the Telegram Desktop
  session folder and then authenticates to Telegram with it, pulling the account's chats, membership lists and media
  through the API rather than merely holding the credential; where files are locked it falls back on three
  SeBackupPrivilege-based mechanisms including Volume Shadow Copy and Robocopy backup mode. Still Audio implements its
  own voice-activity detection to record only when someone speaks, keeps a pre-buffer so the start of speech is not
  clipped, makes no attempt to hide from the Windows microphone-usage list, and — if its server stays unreachable for
  three days — retrieves a fresh address from an encrypted blob parked in a forked public code repository. Targeting is
  Russia-domestic.
discovered_at: "2026-08-14T05:06:00Z"
event_date: "2026-08-13"
run_id: 2026-08-14T0417Z-intel
priority: notable
immediate_action: null
tags:
  - espionage
  - infostealer
  - nation-state
regions:
  - russia-cis
sectors:
  - public-sector
  - education
  - technology
entities:
  - actor:armored-likho
techniques:
  - T1204.002
  - T1123
  - T1102.001
  - T1539
  - T1006
  - T1005
  - T1071.001
affected_products:
  - "Telegram Desktop"
cves: []
sources:
  - url: "https://securelist.com/armored-likho-still-toolkit/121033/"
    publisher: "Kaspersky Securelist (GReAT)"
    date: "2026-08-13"
    role: primary
closed_sources: []
evidence:
  - quote: "we found a new cyber-espionage toolkit – the Still Toolkit – made up of two components: Still Sync and Still Audio."
    publisher: "Kaspersky Securelist (GReAT)"
  - quote: "Still Audio also uses the Dead Drop Resolver technique as a fallback mechanism for obtaining the C2 address. If the current server stays unreachable for three days, the tool tries to pull the current C2 URL from a GitHub repository."
    publisher: "Kaspersky Securelist (GReAT)"
  - quote: "Based on these overlaps, along with additional technical artifacts, we’re highly confident the Armored Likho group is behind the campaign."
    publisher: "Kaspersky Securelist (GReAT)"
verification: single-source
sourcing_note: "Kaspersky GReAT is the sole source; the analysis is its own and no independent corroboration was found this run. The entry is included for the transferable tradecraft, not for a regional nexus — the reported victimology is entirely inside Russia and the body says so."
confidence: high
update_of: null
references: []
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

Kaspersky GReAT published analysis on 2026-08-13 of a May 2026 Armored Likho campaign — the group is also tracked as Eagle Werewolf — whose initial lure is a fake charitable-donation application built in Rust on the Tauri framework, complete with a working item catalogue pulled from the operator's own server to hold the user's attention. The lure is not the interesting part; the payload is. GReAT reports that ["we found a new cyber-espionage toolkit – the Still Toolkit – made up of two components: Still Sync and Still Audio"](https://securelist.com/armored-likho-still-toolkit/121033/). Both are written in Rust, talk to their server over gRPC with FlatBuffers serialisation, and register the host under a hash derived from motherboard serial, CPU identifier, system UUID, BIOS serial and domain name.

**Still Sync does not stop at the session folder.** It locates the Telegram Desktop `tdata` directory — checking the standard installation path and, for the Microsoft Store build, the package-local cache — and exfiltrates it. What separates it from a commodity session stealer is the next step: with an option enabled, it authenticates to Telegram using the stolen session and pulls the account's data through the API, retrieving the username, chat and channel membership, dialogs and media. GReAT also records that where Sync cannot read the files through standard means it falls back on three mechanisms that abuse `SeBackupPrivilege` — the privilege that lets a backup process bypass file ACLs — including Volume Shadow Copy and backup-mode file copying. Before transferring, it sends a file listing to the server so the operator does not re-collect what they already hold, and it supports an option to skip channel dialogs.

**Still Audio listens selectively and finds its way home through a public repository.** The implant extracts a bundled MP3 encoding library, then processes raw audio samples from the input device using its own Root Mean Square implementation — no third-party library — to distinguish speech from silence, starting a recording when the signal's average power crosses a configurable threshold and stopping after a run of below-threshold samples. A pre-buffer holds samples from just before the trigger so the beginning of speech is not lost. Recordings are encoded and POSTed to the server with a header identifying the machine. Two properties are worth carrying into a hunt. First, the implant makes no attempt to hide its microphone use: in the sample GReAT examined it appeared in the Windows list of apps using the microphone under a generic chipset-vendor name. Second, its resilience mechanism is a dead drop on a public code-hosting service — ["Still Audio also uses the Dead Drop Resolver technique as a fallback mechanism for obtaining the C2 address. If the current server stays unreachable for three days, the tool tries to pull the current C2 URL from a GitHub repository"](https://securelist.com/armored-likho-still-toolkit/121033/) — where the address sits Base64-encoded and encrypted inside a fork of a popular project, using the same algorithm and key GReAT observed in the group's earlier AquilaRAT samples.

**Attribution and victimology.** GReAT states that ["Based on these overlaps, along with additional technical artifacts, we’re highly confident the Armored Likho group is behind the campaign"](https://securelist.com/armored-likho-still-toolkit/121033/), citing identical dropper architecture and payload encryption format against the group's February campaign, the shared dead-drop algorithm and key, host-fingerprint generation logic matching down to the PowerShell commands used, and infrastructure overlap. Targets are in Russia — mostly private individuals, with corporate, government, IT and education organisations also affected. There is no European or Swiss victim here, and this entry claims none.

**Defender takeaway:** three mechanics in this toolkit are actor-agnostic and worth hunting for regardless of who runs them. A stolen messenger session used to authenticate to the platform's own API is a class of account takeover that leaves no trace on the endpoint after the theft and no failed-login signal at the service — the exposure is every chat and file the account can reach, and the remedy is terminating other sessions at the application, not resetting a password. `SeBackupPrivilege` abuse to read files a process has no ACL rights to is a general-purpose primitive for reaching locked application data. And a dead drop on a public code-hosting service means the malware's first outbound connection can be to a domain no reputation system will ever flag.

**Triage:** each of these looks like something ordinary. Microphone access is normal for conferencing software — the discriminator is a background service-like process holding the microphone while no conferencing application is running, particularly one whose display name suggests a hardware or chipset component rather than an application the user installed. Fetching a raw file from a public code-hosting service is normal on a developer workstation and anomalous everywhere else: an outbound request retrieving a single data file from a code-hosting content domain, from a host with no development role, is worth alerting on independently of this campaign. And a process reading the Telegram Desktop data directory that is not the Telegram client — or a shadow copy created immediately before such a read — is the file-access shape here, since the legitimate client does not need a backup privilege to read its own state.
