---
schema: 1
kind: threat
title: "TerminalFix: a ClickFix variant that pastes into Terminal or PowerShell instead of Windows' Run dialog, then chains DLL sideloading, steganographic payload delivery and a custom reverse-tunnel implant"
headline: "The fake-CAPTCHA lure now targets a console that can run multi-line scripts, not the one-line Run box"
summary: >
  Microsoft Threat Intelligence documents TerminalFix, a ClickFix variant that tricks users into
  pasting a malicious command into Windows Terminal or PowerShell via a fake Cloudflare CAPTCHA
  overlay, then runs a multi-stage chain of DLL sideloading, PNG-steganography payload delivery,
  domain reconnaissance and a custom Python reverse-tunnel implant that gives the attacker
  persistent SOCKS-style proxy access into the victim's internal network. Sophos reports the campaign running
  since March, with TerminalFix lures from late May and 19 pairings of a legitimate executable and a malicious DLL, so
  a detection keyed to one file name misses most of it.
discovered_at: "2026-08-31T05:10:00Z"
updated_at: "2026-10-05T04:34:00Z"
event_date: "2026-08-28"
run_id: 2026-08-31T0411Z-intel
priority: high
immediate_action: null
tags: [phishing, ransomware, organized-crime]
regions: [global]
sectors: []
entities: ["campaign:terminalfix-clickfix-reverse-tunnel-2026", "actor:rhysida", "campaign:stac4924", "malware:loremipsumloader"]
techniques: [T1189, T1204.004, T1059.001, T1574.001, T1036.005, T1027.003, T1564.001, T1547.001, T1053.005, T1482, T1069.002, T1087.002, T1018, T1082, T1572, T1071.001, T1105, T1102.001, T1027.013, T1001.002, T1608.006, T1204.002, T1588.003]
affected_products: []
cves: []
sources:
  - url: "https://www.microsoft.com/en-us/security/blog/2026/08/28/terminalfix-campaign-deploys-reverse-tunnel-through-multistage-intrusion/"
    publisher: "Microsoft Threat Intelligence"
    date: "2026-08-28"
    role: primary
  - url: "https://www.bsi.bund.de/SharedDocs/Cybersicherheitswarnungen/DE/2026/2026-287419-1032.pdf?__blob=publicationFile"
    publisher: "BSI (Bundesamt für Sicherheit in der Informationstechnik), BITS-2026-287419-1032, v1.0"
    date: "2026-09-04"
    role: corroborating
  - url: "https://www.heise.de/news/BSI-erklaert-ersten-Angriffsvektor-auf-Berliner-Behoerden-11444072.html"
    publisher: "heise online (Nico Ernst)"
    date: "2026-09-07"
    role: corroborating
  - url: "https://www.sophos.com/en-us/blog/terminalfix-and-lorem-ipsum-loader-enable-covert-tunneling"
    publisher: "Sophos X-Ops"
    date: "2026-09-30"
    role: corroborating
  - url: "https://social.bund.de/@bsi/117212729947889443"
    publisher: "BSI (Mastodon)"
    date: "2026-09-04"
    role: corroborating
closed_sources: []
evidence:
  - quote: "While traditional ClickFix campaigns direct victims to the Windows Run dialog, TerminalFix campaigns apply the same technique but direct users to Windows Terminal or PowerShell instead, increasing the likelihood that complex, multi-line scripts execute successfully."
    publisher: "Microsoft Threat Intelligence"
    source_url: "https://www.microsoft.com/en-us/security/blog/2026/08/28/terminalfix-campaign-deploys-reverse-tunnel-through-multistage-intrusion/"
  - quote: "The client.py script is a compact but full-featured reverse tunnel. It dials outbound to the C2 over TLS/443, upgrades the session to a WebSocket, and uses that channel to relay arbitrary TCP connections on behalf of the operator. On the wire, the traffic is indistinguishable from an ordinary encrypted web session to a single destination"
    publisher: "Microsoft Threat Intelligence"
    source_url: "https://www.microsoft.com/en-us/security/blog/2026/08/28/terminalfix-campaign-deploys-reverse-tunnel-through-multistage-intrusion/"
  - quote: "Organizations should treat affected devices as potential network pivot points and investigate for lateral movement and credential exposure."
    publisher: "Microsoft Threat Intelligence"
    source_url: "https://www.microsoft.com/en-us/security/blog/2026/08/28/terminalfix-campaign-deploys-reverse-tunnel-through-multistage-intrusion/"
  - quote: "To the BSI's knowledge, this malware is attributed to the same financially motivated group responsible for the Rhysida ransomware and leak site. (translated from German)"
    original: "Nach Kenntnislage des BSI wird diese Malware derselben finanziell motivierten Gruppe zugeordnet, welche für die Ransomware und Leak-Seite Rhysida verantwortlich ist."
    publisher: "BSI (Bundesamt für Sicherheit in der Informationstechnik), BITS-2026-287419-1032, v1.0"
    source_url: "https://www.bsi.bund.de/SharedDocs/Cybersicherheitswarnungen/DE/2026/2026-287419-1032.pdf?__blob=publicationFile"
  - quote: "TerminalFix is not linked to a specific threat group or a single campaign."
    publisher: "Sophos X-Ops"
    source_url: "https://www.sophos.com/en-us/blog/terminalfix-and-lorem-ipsum-loader-enable-covert-tunneling"
  - quote: "Table 1 lists the sideload pairings that Sophos analysts observed between March and September."
    publisher: "Sophos X-Ops"
    source_url: "https://www.sophos.com/en-us/blog/terminalfix-and-lorem-ipsum-loader-enable-covert-tunneling"
  - quote: "This loader attempts to evade entropy-based detections by storing shellcode bytes as English words rather than raw binary data."
    publisher: "Sophos X-Ops"
    source_url: "https://www.sophos.com/en-us/blog/terminalfix-and-lorem-ipsum-loader-enable-covert-tunneling"
  - quote: "However, Sophos analysts have not observed encryption in the STAC4924 campaign."
    publisher: "Sophos X-Ops"
    source_url: "https://www.sophos.com/en-us/blog/terminalfix-and-lorem-ipsum-loader-enable-covert-tunneling"
verification: multi-source
sourcing_note: >
  Microsoft Threat Intelligence published first-party detection telemetry on its own detection surface. Germany's BSI
  (BITS-2026-287419-1032, 2026-09-04) independently confirms the technique against a real-world case it investigated
  and names the group behind it. Sophos X-Ops (2026-09-30) adds first-hand managed-detection telemetry on a campaign
  whose tooling closely aligns with this chain; it reports BlueVoyant's attribution of the loader and says its own
  observations support that attribution.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions: []
updates:
  - at: "2026-09-08T04:50:00Z"
    run_id: 2026-09-08T0411Z-intel
    type: update
    summary: >
      Germany's BSI independently confirms this campaign's technique against a real-world case it
      investigated (the Berlin Landesnetz compromise) and supplies the campaign's first named-actor
      attribution: Rhysida's operators, tracked by BSI as Vice Spider. Verification moves from
      single-source to multi-source; credibility moves from 2 to 1 on the same independent
      national-CERT confirmation that moved the sibling Berlin entry.
    fields: [updated_at, entities, tags, sources, evidence, verification, classification, sourcing_note, body]
  - at: "2026-10-05T04:34:00Z"
    run_id: 2026-10-05T0404Z-intel
    type: update
    summary: >
      Sophos X-Ops reports a campaign it tracks as STAC4924, active since at least March and closely aligned with this
      chain, with 19 pairings of a legitimate executable and a malicious DLL rather than one, a loader that stores shellcode as English
      words, C2 addresses read from a profile on a legitimate community platform, and a first phase of trojanized Teams
      installers before the TerminalFix lures. Sophos says its observations support BlueVoyant's attribution to the
      group linked to Vice Society and Rhysida, and that it has seen no encryption.
    fields: [updated_at, summary, entities, techniques, sources, evidence, sourcing_note, body]
migrated_from: null
---

Microsoft Threat Intelligence documents TerminalFix, a ClickFix variant targeting organizations across multiple industries ([Microsoft Threat Intelligence, 2026-08-28](https://www.microsoft.com/en-us/security/blog/2026/08/28/terminalfix-campaign-deploys-reverse-tunnel-through-multistage-intrusion/)). A compromised website displays a fake Cloudflare Turnstile verification overlay that silently copies a malicious PowerShell command to the clipboard and instructs the user to paste it into Windows Terminal or PowerShell rather than Windows' Run dialog, which traditional ClickFix lures use; a console runs complex, multi-line scripts far more reliably ([Microsoft Threat Intelligence, 2026-08-28](https://www.microsoft.com/en-us/security/blog/2026/08/28/terminalfix-campaign-deploys-reverse-tunnel-through-multistage-intrusion/)). Once pasted, the command downloads a ZIP archive containing a legitimate signed binary (`LockScreenContentServer.exe`) alongside a malicious `dui70.dll` masquerading as the Windows DirectUI Engine; the signed binary's static import dependency loads the planted DLL from its own working directory instead of System32, a DLL side-loading technique that starts execution inside a trusted, signed process ([Microsoft Threat Intelligence, 2026-08-28](https://www.microsoft.com/en-us/security/blog/2026/08/28/terminalfix-campaign-deploys-reverse-tunnel-through-multistage-intrusion/)).

The sideloaded DLL runs an elaborate second stage: PowerShell downloads three PNG images from attacker domains, extracts binary data hidden in their pixel channels (the first eight bytes of each embedded payload encode its length) and reassembles an executable and a DLL split across two of the images, deleting the source images afterward to reduce forensic artifacts ([Microsoft Threat Intelligence, 2026-08-28](https://www.microsoft.com/en-us/security/blog/2026/08/28/terminalfix-campaign-deploys-reverse-tunnel-through-multistage-intrusion/)). Persistence lands through both an `HKCU\...\Run` registry key and a scheduled task re-executing every 60 minutes, both under a masquerading name chosen to blend with the abused Lock Screen component, with the payload directory hidden via system and hidden file attributes ([Microsoft Threat Intelligence, 2026-08-28](https://www.microsoft.com/en-us/security/blog/2026/08/28/terminalfix-campaign-deploys-reverse-tunnel-through-multistage-intrusion/)). The malware then conducts extensive Active Directory reconnaissance: domain trust enumeration, domain admin group membership, user and computer discovery, and targeted pings of named infrastructure roles (domain controllers, databases, backup, gateways, mail), with the system-information-collection step run in English, Spanish and German locale variants, consistent with an operator or automated pre-assessment scoring whether the compromised host sits near high-value, domain-joined infrastructure ([Microsoft Threat Intelligence, 2026-08-28](https://www.microsoft.com/en-us/security/blog/2026/08/28/terminalfix-campaign-deploys-reverse-tunnel-through-multistage-intrusion/)).

The most significant capability is the final stage: an unmodified, signed embeddable Python 3.14.5 runtime pulled directly from python.org, launched with no visible window via `pythonw.exe`, running a custom `client.py` tunneling implant that dials out over TLS on port 443, upgrades to a WebSocket, and relays arbitrary TCP connections to any internal host and port the operator specifies: SOCKS5-style addressing over a custom 7-byte multiplexed protocol, indistinguishable on the wire from an ordinary encrypted web session ([Microsoft Threat Intelligence, 2026-08-28](https://www.microsoft.com/en-us/security/blog/2026/08/28/terminalfix-campaign-deploys-reverse-tunnel-through-multistage-intrusion/)). Combined with the reconnaissance data already gathered, this turns the compromised host into a full network pivot point. Microsoft states it did not observe the downstream hands-on-keyboard actions this access typically enables (privilege escalation, security-control tampering, data exfiltration, ransomware deployment) in the analyzed chain, but assesses the access itself makes those the expected next step ([Microsoft Threat Intelligence, 2026-08-28](https://www.microsoft.com/en-us/security/blog/2026/08/28/terminalfix-campaign-deploys-reverse-tunnel-through-multistage-intrusion/)).

**Defender takeaway:** any host found running `LockScreenContentServer.exe` from a path other than `C:\Windows\SystemApps` has been compromised by this technique and must be treated as a network pivot point; prioritise credential rotation for anything reachable from that host, including domain admin accounts if it was domain-joined. That file name is one of 19 pairings of a legitimate executable and a malicious DLL that Sophos lists for the same campaign ([Sophos X-Ops, 2026-09-30](https://www.sophos.com/en-us/blog/terminalfix-and-lorem-ipsum-loader-enable-covert-tunneling)), so detections should look for any legitimate executable loading a planted DLL, as in this chain, and not only this file name. Detection concepts: process-creation telemetry for `LockScreenContentServer.exe` executing from a non-standard directory and immediately loading `dui70.dll` from that same directory, and the same pattern for the other pairings Sophos lists; PowerShell logs showing a `cmd.exe`/`LockScreenContentServer.exe` chain launched from a `ProgramData` path shortly after clipboard-paste activity into Terminal or PowerShell; process lineage showing `pythonw.exe` or `python.exe` invoking a script with `client.py` and `--uuid` arguments with no visible console window; and outbound TLS-443 connections from an otherwise-idle host that establish a WebSocket upgrade and sustain long-lived, low-and-slow traffic patterns rather than a normal page-load profile. **Triage:** legitimate `LockScreenContentServer.exe` only ever runs from `C:\Windows\SystemApps`; the same binary name executing from `ProgramData` or a user-writable temp path, with a co-located `dui70.dll` bearing a forged future timestamp, is the discriminator: a benign lock-screen component never side-loads from an application directory. Sophos lists the other pairings as the same DLL sideloading technique ([Sophos X-Ops, 2026-09-30](https://www.sophos.com/en-us/blog/terminalfix-and-lorem-ipsum-loader-enable-covert-tunneling)), so the discriminator generalises beyond the executable's name: a DLL named like a Windows component, such as `dui70.dll`, `faultrep.dll`, `sspicli.dll` or `secur32.dll` in Sophos's table, loading from the executable's own directory instead of System32. Restrict PowerShell execution for standard users via AppLocker or Application Control, enable PowerShell script-block logging, and train users to recognise that a legitimate CAPTCHA never asks them to paste a command into a terminal.

## Update — 2026-09-08T04:50:00Z

Germany's BSI published an advisory on 2026-09-04 describing the compromise of an anonymized "state institution" whose technique matches this campaign; the advisory itself never names Berlin ([BSI, BITS-2026-287419-1032, 2026-09-04](https://www.bsi.bund.de/SharedDocs/Cybersicherheitswarnungen/DE/2026/2026-287419-1032.pdf?__blob=publicationFile)). The same day, BSI posted on its official Mastodon account that it was intensively involved in handling the Berlin incident and separately linked to its detailed TerminalFix security notice ([BSI on Mastodon, 2026-09-04](https://social.bund.de/@bsi/117212729947889443)); heise reports that juxtaposition as confirmation that TerminalFix is specifically the vector Rhysida's operators used against Berlin's two affected Senate administrations ([heise online, citing BSI, 2026-09-07](https://www.heise.de/news/BSI-erklaert-ersten-Angriffsvektor-auf-Berliner-Behoerden-11444072.html)), the first independent confirmation of this campaign beyond Microsoft's own telemetry, and its first named-actor attribution. BSI attributes the campaign, via a malware family it names LoremIpsumLoader (also known as AxolotLoader) observed in incident reports, to a financially motivated group it tracks as Vice Spider, the same group responsible for the Rhysida ransomware and leak site, cross-referenced against the aliases Vice Society, WhiteNefas, White Hekate, DEV-0832 and Vanilla Tempest ([BSI, BITS-2026-287419-1032, 2026-09-04](https://www.bsi.bund.de/SharedDocs/Cybersicherheitswarnungen/DE/2026/2026-287419-1032.pdf?__blob=publicationFile)). BSI assesses the campaign as opportunistic, purely financially motivated cybercrime with no established state or political link, and notes the CAPTCHA lure's own JavaScript has been observed on several hundred historical websites, evidence of a reusable watering-hole kit rather than one-off, victim-specific infrastructure ([BSI, BITS-2026-287419-1032, 2026-09-04](https://www.bsi.bund.de/SharedDocs/Cybersicherheitswarnungen/DE/2026/2026-287419-1032.pdf?__blob=publicationFile)).

## Update — 2026-10-05T04:34:00Z

Sophos X-Ops reports a campaign it tracks as STAC4924, active since at least March, in two phases, whose tooling and tradecraft closely align with this chain ([Sophos X-Ops, 2026-09-30](https://www.sophos.com/en-us/blog/terminalfix-and-lorem-ipsum-loader-enable-covert-tunneling)). The first, in March and April, used SEO-poisoned websites distributing trojanized Microsoft Teams installer packages; from late May the campaign moved to TerminalFix lures, a shift Sophos says coincided with Microsoft's takedown of the malware-signing service that supplied the fraudulently obtained certificates ([Sophos X-Ops, 2026-09-30](https://www.sophos.com/en-us/blog/terminalfix-and-lorem-ipsum-loader-enable-covert-tunneling)). Sophos assesses with moderate confidence that the two phases are linked to the same group or closely associated actors, on the shared per-victim identifier callback and the use of a legitimate community platform as a dead-drop resolver for C2 addresses, and adds that the TerminalFix lure itself is not linked to a specific threat group or a single campaign, since several 2026 campaigns have used it ([Sophos X-Ops, 2026-09-30](https://www.sophos.com/en-us/blog/terminalfix-and-lorem-ipsum-loader-enable-covert-tunneling)).

Sophos lists 19 pairings of a legitimate executable and a malicious DLL observed between March and September, not only the lock-screen binary with `dui70.dll`: they include `changepk.exe`, `werfaultsecure.exe`, `wuauclt.exe` and `embeddedapplauncher.exe`, and helper executables named after Microsoft Edge and Teams ([Sophos X-Ops, 2026-09-30](https://www.sophos.com/en-us/blog/terminalfix-and-lorem-ipsum-loader-enable-covert-tunneling)). The loader stores shellcode bytes as English words with a separate lookup table to evade entropy-based detections, reads an attacker-controlled profile on the community platform to decode the current C2 server list, and then talks to C2 over HTTP POST requests that appear to carry JPEG images but hold encoded data ([Sophos X-Ops, 2026-09-30](https://www.sophos.com/en-us/blog/terminalfix-and-lorem-ipsum-loader-enable-covert-tunneling)).

BlueVoyant attributed the loader to the Rapid Brigantine group, which Sophos tracks as GOLD VICTOR (also known as Vanilla Tempest, DEV-0832, VICE SPIDER and Vice Society) and which has been linked to the Vice Society and Rhysida ransomware families; Sophos says its STAC4924 observations support that attribution but that it has not observed encryption in the campaign ([Sophos X-Ops, 2026-09-30](https://www.sophos.com/en-us/blog/terminalfix-and-lorem-ipsum-loader-enable-covert-tunneling)).
