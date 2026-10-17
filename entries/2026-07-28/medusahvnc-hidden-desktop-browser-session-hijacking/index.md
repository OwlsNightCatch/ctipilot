---
schema: 1
kind: threat
title: "MedusaHVNC: a malware-as-a-service RAT that drives the victim's own logged-in browser on an invisible second Windows desktop"
headline: "MedusaHVNC rides real logged-in browser sessions on a hidden Windows desktop, defeating device-based fraud checks"
summary: >
  BlackFog analysed MedusaHVNC (2026-07-27), a Windows remote-access trojan sold as malware-as-a-service
  whose hidden-VNC module opens Chrome, Edge or Firefox on a separate, invisible Windows desktop using the
  victim's existing browser profile — so the operator drives live, already-authenticated sessions from the
  victim's own machine while the user sees nothing. The five-stage chain runs from an obfuscated JScript
  launcher through an AutoIt interpreter that XOR-decrypts a loader and injects it into charmap.exe, then
  unpacks the final payload behind repeating-XOR and ChaCha20 layers. Because the session originates from
  the real device with the real profile, controls that key on device fingerprint and session continuity see
  nothing unusual.
discovered_at: "2026-07-28T04:55:00Z"
event_date: "2026-07-27"
run_id: 2026-07-28T0409Z-intel
priority: notable
immediate_action: null
tags: [infostealer, identity]
regions: [global]
sectors: [finance, technology]
entities: ["tool:medusahvnc"]
techniques: [T1059.007, T1140, T1055, T1547.001, T1564.003, T1185, T1539, T1555.003, T1115, T1685]
affected_products: ["Microsoft Windows", "Google Chrome", "Microsoft Edge", "Mozilla Firefox"]
cves: []
sources:
  - url: "https://www.blackfog.com/medusahvnc-a-hidden-desktop/"
    publisher: "BlackFog"
    date: "2026-07-27"
    role: primary
  - url: "https://www.securityweek.com/medusahvnc-malware-uses-hidden-windows-desktops-to-evade-detection/"
    publisher: "SecurityWeek"
    date: "2026-07-27"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The browser still runs on the victim’s device, so it can load an existing profile, including cookies and session state."
    publisher: "BlackFog"
  - quote: "The AutoIt stage then starts C:\\Windows\\System32\\charmap.exe, the standard Windows Character Map utility. The public sandbox process tree shows charmap.exe as a child of the AutoIt process, and the loader is injected into it, using the trusted system binary as a host for the payload."
    publisher: "BlackFog"
  - quote: "Hidden desktops are a legitimate Windows capability, often used by specialized software, and occasionally used by malware."
    publisher: "SecurityWeek"
verification: single-source
sourcing_note: "BlackFog's own sample analysis is the primary (reliability B — a vendor research write-up with original reverse-engineering, partly corroborated against public sandbox data, which the write-up states); SecurityWeek's same-day article reports on that analysis rather than performing its own — every technical element it carries is BlackFog's — so this entry is single-source on BlackFog's research and credibility is 2, not 1; SecurityWeek's observation about the base rate of hidden-desktop use is carried as an attributed editorial point, not as corroboration. Two limits are worth stating: BlackFog derives the hidden-desktop capability set from the payload's imported Windows API surface and from the vendor's own sales material rather than from observed operator activity, and the AMSI-patching and ETW-bypass functionality is an advertised panel feature rather than something confirmed in the analysed sample. The hardcoded command-and-control address and the sample's dropped file names are indicators and are not reproduced here. BlackFog's remediation section ends in a pitch for its own product; only its non-promotional detection reasoning is carried. Despite the shared brand word, neither source claims any relationship to the Medusa or MedusaLocker ransomware families."
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

The interesting property of MedusaHVNC is not that it steals credentials — it does, and advertises a "Browser Recovery" feature for passwords, cookies and history across Chrome, Edge, Brave, Firefox and Telegram — but that it makes stealing them partly unnecessary. Its hidden-VNC module opens a real browser on a second, invisible Windows desktop, and because "[t]he browser still runs on the victim's device, so it can load an existing profile, including cookies and session state", the operator inherits whatever the user is already logged into ([BlackFog, 2026-07-27](https://www.blackfog.com/medusahvnc-a-hidden-desktop/)). The resulting traffic leaves the victim's machine, from the victim's network, with the victim's browser profile and device characteristics — which is the entire point, since the fraud and risk-engine controls that would normally challenge a session key on exactly those signals. SecurityWeek's account of the same research notes that hidden desktops are a legitimate Windows capability used by specialised software and only occasionally by malware ([SecurityWeek, 2026-07-27](https://www.securityweek.com/medusahvnc-malware-uses-hidden-windows-desktops-to-evade-detection/)).

The delivery chain is five stages and leans on trusted components throughout. Windows Script Host executes an obfuscated JScript launcher, which sleeps for just over seven and a half seconds before reconstructing its embedded files into a randomly named subfolder of `%TEMP%` — an AutoIt interpreter, a configuration file and an extensionless encrypted payload — and dropping a batch file into the Startup folder for persistence. The AutoIt component runs without a visible window, decrypts the payload with a single-byte XOR key to produce a native 64-bit loader, and then launches `C:\Windows\System32\charmap.exe`, the Character Map utility, into which the loader is injected; BlackFog notes this stage is corroborated by a public sandbox process tree showing `charmap.exe` as a child of the AutoIt process. Inside that host process two further layers come off — a 16-byte repeating XOR across roughly a megabyte of the `.data` section, then ChaCha20 with a 32-byte key and 12-byte nonce — yielding an unsigned PE32+ console executable carrying a `.pay` section and the family string. Alongside the hidden desktop, the seller's own panel advertises a "Mem Exec" feature described as running .NET and native payloads in memory with an AMSI patch and ETW bypass — security-tooling tampering that BlackFog reports from the marketplace listing rather than from the analysed sample, so it should be treated as claimed capability rather than confirmed behaviour. The payload speaks a custom protocol over raw TCP via native Winsock calls to a hardcoded endpoint, and its imported API surface is what BlackFog reads as the HVNC workflow: `BitBlt`, `EnumWindows` and `PrintWindow` for screen and window capture, `SendInput` and `SetWindowsHookExW` for synthetic input, and the clipboard functions for moving data into and out of the session ([BlackFog, 2026-07-27](https://www.blackfog.com/medusahvnc-a-hidden-desktop/)).

**Defender takeaway:** session-binding assumptions are the thing this breaks, so the response belongs partly outside the endpoint. Any control that treats "same device, same browser profile, continuous session" as evidence of legitimacy is satisfied by this malware by construction, which argues for authentication and authorisation decisions that re-verify at the action rather than at the login — step-up on transaction or privilege changes, and attestation that binds to something the operator cannot inherit along with the cookie jar. On the endpoint, the durable signal is egress: whatever the loader chain looks like next release, the operator's view has to leave the host, so unexpected outbound connections from processes with no business making them remain the detection of last resort.

**Triage:** `charmap.exe` is the sharpest discriminator in the chain. The Character Map is an interactive accessory a user opens from the Start menu; an instance spawned by a scripting or automation interpreter, running with no window, holding a network socket, or hosting injected code is not a benign variant of that behaviour. Around it, look for the sequence rather than any single event — `wscript.exe` executing script content that writes an AutoIt interpreter into a `%TEMP%` subfolder, a Startup-folder write from that same process tree, and an AutoIt binary running from a user-writable path where the organisation does not deploy AutoIt. Legitimate AutoIt use exists in many estates, which is why the parent chain and the write location matter more than the interpreter's presence. The hidden desktop itself is the weakest thing to hunt for, since the capability is a supported Windows feature with genuine software using it.
