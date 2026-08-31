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
  persistent SOCKS-style proxy access into the victim's internal network.
discovered_at: "2026-08-31T05:10:00Z"
updated_at: null
event_date: "2026-08-28"
run_id: 2026-08-31T0411Z-intel
priority: high
immediate_action: null
tags: [phishing]
regions: [global]
sectors: []
entities: ["campaign:terminalfix-clickfix-reverse-tunnel-2026"]
techniques: [T1189, T1204.004, T1059.001, T1574.001, T1036.005, T1027.003, T1564.001, T1547.001, T1053.005, T1482, T1069.002, T1087.002, T1018, T1082, T1572, T1071.001, T1105]
affected_products: []
cves: []
sources:
  - url: "https://www.microsoft.com/en-us/security/blog/2026/08/28/terminalfix-campaign-deploys-reverse-tunnel-through-multistage-intrusion/"
    publisher: "Microsoft Threat Intelligence"
    date: "2026-08-28"
    role: primary
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
verification: single-source
sourcing_note: "First-party vendor telemetry (Microsoft Threat Intelligence) on its own detection surface; no independent corroborating report identified as of 2026-08-31."
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

Microsoft Threat Intelligence documents TerminalFix, a ClickFix variant targeting organizations across multiple industries ([Microsoft Threat Intelligence, 2026-08-28](https://www.microsoft.com/en-us/security/blog/2026/08/28/terminalfix-campaign-deploys-reverse-tunnel-through-multistage-intrusion/)). A compromised website displays a fake Cloudflare Turnstile verification overlay that silently copies a malicious PowerShell command to the clipboard and instructs the user to paste it into Windows Terminal or PowerShell rather than Windows' Run dialog, which traditional ClickFix lures use — a console that runs complex, multi-line scripts far more reliably ([Microsoft Threat Intelligence, 2026-08-28](https://www.microsoft.com/en-us/security/blog/2026/08/28/terminalfix-campaign-deploys-reverse-tunnel-through-multistage-intrusion/)). Once pasted, the command downloads a ZIP archive containing a legitimate signed binary (`LockScreenContentServer.exe`) alongside a malicious `dui70.dll` masquerading as the Windows DirectUI Engine; the signed binary's static import dependency loads the planted DLL from its own working directory instead of System32, a DLL side-loading technique that starts execution inside a trusted, signed process ([Microsoft Threat Intelligence, 2026-08-28](https://www.microsoft.com/en-us/security/blog/2026/08/28/terminalfix-campaign-deploys-reverse-tunnel-through-multistage-intrusion/)).

The sideloaded DLL runs an elaborate second stage: PowerShell downloads three PNG images from attacker domains, extracts binary data hidden in their pixel channels — the first eight bytes of each embedded payload encode its length — and reassembles an executable and a DLL split across two of the images, deleting the source images afterward to reduce forensic artifacts ([Microsoft Threat Intelligence, 2026-08-28](https://www.microsoft.com/en-us/security/blog/2026/08/28/terminalfix-campaign-deploys-reverse-tunnel-through-multistage-intrusion/)). Persistence lands through both an `HKCU\...\Run` registry key and a scheduled task re-executing every 60 minutes, both under a masquerading name chosen to blend with the abused Lock Screen component, with the payload directory hidden via system and hidden file attributes. The malware then conducts extensive Active Directory reconnaissance — domain trust enumeration, domain admin group membership, user and computer discovery, and targeted pings of named infrastructure roles (domain controllers, databases, backup, gateways, mail), with the system-information-collection step run in English, Spanish and German locale variants — consistent with an operator or automated pre-assessment scoring whether the compromised host sits near high-value, domain-joined infrastructure ([Microsoft Threat Intelligence, 2026-08-28](https://www.microsoft.com/en-us/security/blog/2026/08/28/terminalfix-campaign-deploys-reverse-tunnel-through-multistage-intrusion/)).

The most significant capability is the final stage: an unmodified, signed embeddable Python 3.14.5 runtime pulled directly from python.org, launched with no visible window via `pythonw.exe`, running a custom `client.py` tunneling implant that dials out over TLS on port 443, upgrades to a WebSocket, and relays arbitrary TCP connections to any internal host and port the operator specifies — SOCKS5-style addressing over a custom 7-byte multiplexed protocol, indistinguishable on the wire from an ordinary encrypted web session ([Microsoft Threat Intelligence, 2026-08-28](https://www.microsoft.com/en-us/security/blog/2026/08/28/terminalfix-campaign-deploys-reverse-tunnel-through-multistage-intrusion/)). Combined with the reconnaissance data already gathered, this turns the compromised host into a full network pivot point. Microsoft states it did not observe the downstream hands-on-keyboard actions this access typically enables — privilege escalation, security-control tampering, data exfiltration, ransomware deployment — in the analyzed chain, but assesses the access itself makes those the expected next step ([Microsoft Threat Intelligence, 2026-08-28](https://www.microsoft.com/en-us/security/blog/2026/08/28/terminalfix-campaign-deploys-reverse-tunnel-through-multistage-intrusion/)).

**Defender takeaway:** any host found running `LockScreenContentServer.exe` from a path other than `C:\Windows\SystemApps` has been compromised by this technique and must be treated as a network pivot point — prioritise credential rotation for anything reachable from that host, including domain admin accounts if it was domain-joined. Detection concepts: process-creation telemetry for `LockScreenContentServer.exe` executing from a non-standard directory and immediately loading `dui70.dll` from that same directory; PowerShell logs showing a `cmd.exe`/`LockScreenContentServer.exe` chain launched from a `ProgramData` path shortly after clipboard-paste activity into Terminal or PowerShell; process lineage showing `pythonw.exe` or `python.exe` invoking a script with `client.py` and `--uuid` arguments with no visible console window; and outbound TLS-443 connections from an otherwise-idle host that establish a WebSocket upgrade and sustain long-lived, low-and-slow traffic patterns rather than a normal page-load profile. **Triage:** legitimate `LockScreenContentServer.exe` only ever runs from `C:\Windows\SystemApps`; the same binary name executing from `ProgramData` or a user-writable temp path, with a co-located `dui70.dll` bearing a forged future timestamp, is the discriminator — a benign lock-screen component never side-loads from an application directory. Restrict PowerShell execution for standard users via AppLocker or Application Control, enable PowerShell script-block logging, and train users to recognise that a legitimate CAPTCHA never asks them to paste a command into a terminal.
