---
schema: 1
kind: research
horizon: operational
title: "Microsoft: two parallel ACR Stealer intrusion chains — WebDAV/rundll32/Python with blockchain dead-drop C2, and a fileless MSHTA/steganography chain — both rooted in ClickFix"
headline: "Microsoft documents two ClickFix-rooted ACR Stealer chains: WebDAV+EtherHiding and fileless MSHTA+steganography, both ending in DPAPI browser-credential theft"
summary: >
  Microsoft Defender Experts documented two distinct delivery campaigns for ACR Stealer (a MaaS infostealer
  Microsoft ties to the rebranding of Amatera Stealer), both starting from an identical ClickFix lure but
  diverging downstream. Chain 1 uses cmd→rundll32 to load a DLL from a remote WebDAV share, an obfuscated
  PowerShell/Python loader, scheduled-task persistence disguised as an update, and — in a subset — an EtherHiding
  blockchain dead-drop for C2 resolution. Chain 2 is fileless: mshta.exe fetches an HTA that runs in-memory
  PowerShell and extracts an encrypted payload steganographically hidden in a downloaded JPEG. Both converge on
  DPAPI-based theft of Chromium-based browser credential stores plus enumeration of M365/OneDrive documents.
discovered_at: "2026-07-17T04:35:00Z"
event_date: "2026-07-16"
run_id: 2026-07-17T0409Z-intel
priority: notable
immediate_action: null
tags: [infostealer, phishing, identity]
regions: [global]
sectors: []
entities: ["tool:acr-stealer", "tool:amatera"]
techniques: [T1204.004, T1218.011, T1218.005, T1059.001, T1059.006, T1053.005, T1027, T1027.003, T1070.003, T1036, T1620, T1555.003, T1005, T1074.001, T1102.001]
affected_products: []
cves: []
sources:
  - url: "https://www.microsoft.com/en-us/security/blog/2026/07/16/acr-stealer-two-observed-intrusion-chains-amid-increased-threat-activity/"
    publisher: "Microsoft Threat Intelligence (Defender Experts)"
    date: "2026-07-16"
    role: primary
closed_sources: []
evidence:
  - quote: "ACR Stealer is an information-stealing malware family reportedly offered through a malware-as-a-service (MaaS) model and associated with the rebranding of Amatera Stealer."
    publisher: "Microsoft Threat Intelligence"
  - quote: "A notable variation in this campaign is the use of blockchain services for C2 resolution, utilizing a technique known as EtherHiding."
    publisher: "Microsoft Threat Intelligence"
  - quote: "The malware (injected code) aggressively harvests information from browser credential stores. It invokes Windows Data Protection API (DPAPI) routines to decrypt locally stored browser passwords, cookies, and authentication tokens."
    publisher: "Microsoft Threat Intelligence"
verification: single-source
sourcing_note: "Sole primary is Microsoft Threat Intelligence / Defender Experts (Admiralty B for third-party-malware research), uncorroborated at composition. The Amatera-rebranding link is Microsoft's own hedged assessment ('reportedly ... associated with'), recorded as such."
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

Microsoft Defender Experts documented two ACR Stealer delivery campaigns observed across customer environments from late April to mid-June 2026; ACR Stealer is a malware-as-a-service infostealer Microsoft states is "reportedly ... associated with the rebranding of Amatera Stealer" ([Microsoft Threat Intelligence, 2026-07-16](https://www.microsoft.com/en-us/security/blog/2026/07/16/acr-stealer-two-observed-intrusion-chains-amid-increased-threat-activity/)). Both begin with the same ClickFix lure (malvertising/SEO poisoning) but diverge sharply. In Chain 1 the ClickFix command spawns `cmd.exe`, which invokes `rundll32.exe` to load a DLL from a remote WebDAV share over HTTPS using a GUID-based directory structure disguised as legitimate resources; the most evasive variant launches through `conhost.exe --headless` with delayed-expansion obfuscation. A heavily obfuscated PowerShell stage downloads a ZIP into a masqueraded `%LocalAppData%\Temp` directory (e.g. "LogiOptionsPlus"), runs a bundled `pythonw.exe`, persists via a hidden scheduled task disguised as a software update, timestomps against `notepad.exe` and clears PowerShell history; a subset adds an "EtherHiding" loader that queries public blockchain RPC endpoints as a dead-drop resolver so infrastructure can rotate without redeploying malware. Chain 2 is fileless throughout: `mshta.exe` fetches remote HTA content whose VBScript decodes and launches in-memory PowerShell, and its distinguishing technique is steganographic delivery — a JPEG pulled from an image host carries an encrypted payload in its pixel data, decrypted and executed in memory via runtime-resolved `LoadLibrary`/`VirtualAlloc`/`CreateThread`. Both chains converge on DPAPI-based decryption of Chromium-based browser credential stores (passwords, cookies, auth tokens) plus enumeration of PDFs, M365 documents and OneDrive/SharePoint-synced data for exfiltration.

**Defender takeaway:** signature-based detection degrades against the in-memory and steganographic stages, so hunt the two chains' host artifacts, which Microsoft supplies KQL for. Chain 1's RunMRU registry pattern is highly specific — a WebDAV `@ssl` path combined with a GUID (8-4-4-4-12 hex) directory segment invoked through `rundll32` or `pushd` — as is the persistence scheduled task masquerading as an "Autoupdate" with a numeric suffix. Chain 2's anchor is `mshta.exe` launched by a non-interactive PowerShell parent that was itself spawned from `explorer.exe`. **Triage:** legitimate WebDAV use does not produce a RunMRU entry combining `@ssl` with a GUID directory invoked via `rundll32`, and `mshta.exe` is not normally a child of PowerShell — either pattern, captured in registry-modification and process-creation telemetry with parent lineage, separates this activity from benign administrative scripting regardless of the EDR/SIEM in use.
