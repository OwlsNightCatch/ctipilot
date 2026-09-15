---
schema: 1
kind: threat
title: "Cisco Talos: UAT-11795 deploys the Python-based Starland RAT and a bespoke PowerShell C2 implant (WLDR), resolving fallback C2 through a Polygon blockchain dead-drop"
headline: "Talos details UAT-11795 — ClickFix-delivered Starland RAT with a blockchain dead-drop C2 and a bespoke WLDR PowerShell implant"
summary: >
  Cisco Talos disclosed UAT-11795, a Russian-speaking, financially motivated actor active since at least June 2025
  against victims in the US and Europe (Germany, Romania observed). A ClickFix lure runs mshta.exe to stage a
  trojanized installer (impersonating MobaXterm, WebEx, Zoom, DBeaver, FACEIT) that XOR-decrypts and runs the
  in-memory Python "Starland RAT," which persists, harvests crypto-wallet and host data, and — if primary C2
  fails — resolves a fallback C2 domain from a Polygon smart contract dead-drop. Starland can inject shellcode
  (CastleStealer or a Remcos variant) after patching AMSI/ETW, and separately deploys a bespoke PowerShell C2
  implant the actor labels "WLDR."
discovered_at: "2026-07-17T04:35:00Z"
event_date: "2026-07-16"
run_id: 2026-07-17T0409Z-intel
priority: notable
immediate_action: null
tags: [infostealer, phishing, organized-crime, cryptocrime]
regions: [us, europe]
sectors: []
entities: ["actor:uat-11795", "tool:starland-rat", "tool:wldr-c2-implant", "tool:castlestealer"]
techniques: [T1204.004, T1218.005, T1036, T1547.001, T1053.005, T1059.006, T1059.001, T1055, T1620, T1685, T1102.001, T1082]
affected_products: []
cves: []
sources:
  - url: "https://blog.talosintelligence.com/uat-11795-deploys-novel-starland-rat-and-bespoke-wldr-c2-implant-in-financially-motivated-campaign/"
    publisher: "Cisco Talos"
    date: "2026-07-16"
    role: primary
closed_sources: []
evidence:
  - quote: "Cisco Talos is disclosing UAT-11795, a sophisticated, Russian-speaking, financially motivated adversary that has been conducting a malicious campaign targeting users in the U.S. and Europe since at least June 2025."
    publisher: "Cisco Talos"
verification: single-source
sourcing_note: "Sole primary is Cisco Talos, a high-reliability threat-research lab reporting its own investigation (Admiralty B); no independent corroboration at composition. Attribution to a Russian-speaking operator rests on a Russian-language developer comment in the VBScript, per Talos."
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

Cisco Talos documented UAT-11795, a financially motivated actor whose intrusions begin with a ClickFix lure: a clipboard-pasted command invokes `mshta.exe` to fetch a weaponized HTA, whose VBScript drops a batch file that stages an NSIS-packaged installer masquerading as a legitimate IT/collaboration tool (MobaXterm, Cisco WebEx, Zoom, DBeaver, the FACEIT client) and writes a `HKCU\...\Run\MyApp` value pointing back at `mshta.exe` ([Cisco Talos, 2026-07-16](https://blog.talosintelligence.com/uat-11795-deploys-novel-starland-rat-and-bespoke-wldr-c2-implant-in-financially-motivated-campaign/)). The installer bundles `pythonw.exe` plus a compiled Python loader disguised as `LICENSE.txt` that XOR-decrypts and runs "Starland RAT" entirely in memory. Starland checks for sandbox usernames/hostnames and a Downloads `Zone.Identifier` ADS before proceeding, persists via a scheduled task named `PythonLauncher-{3 random chars}` (AtLogOn, RunLevel Highest) plus a Startup-folder LNK, enumerates 40+ desktop and browser-extension crypto wallets, and beacons a Telegram bot before registering to its primary C2. If that registration fails it calls a Polygon smart contract via `eth_call`/JSON-RPC and XOR-decrypts the returned string to recover a fallback C2 domain — a blockchain dead-drop resolver that survives conventional domain/IP takedown ([Cisco Talos, 2026-07-16](https://blog.talosintelligence.com/uat-11795-deploys-novel-starland-rat-and-bespoke-wldr-c2-implant-in-financially-motivated-campaign/)). On command, Starland fetches shellcode via APC-based injection that first patches AMSI/ETW in memory (hash-resolved `AmsiScanBuffer`/`EtwEventWrite` overwritten, with a `VirtualProtect` fallback) and reflectively loads either CastleStealer (.NET credential/wallet stealer, x64 path) or a Remcos variant (x32). Separately it has been seen shell-executing a `curl` download of a bespoke PowerShell C2 framework the actor's own scripts label "WLDR" — HWID-bound, AES-encrypted 10-second beaconing with a Chrome-124 User-Agent, executing operator PowerShell through a 10-thread RunspacePool.

**Defender takeaway:** the C2-resilience and in-memory-patching tradecraft blunt domain-blocklist and AMSI-based detection, so anchor on the host-side behavioral chain. The strongest, low-false-positive hunt anchors are the fixed persistence pattern — a scheduled task named `PythonLauncher-{3 chars}` and a Startup LNK launching `pythonw.exe` with a `LICENSE.txt` argument — and outbound JSON-RPC to a public Polygon RPC endpoint originating from a non-browser process (the dead-drop resolver). In process-creation telemetry with parent lineage, `mshta.exe` spawned from a ClickFix-style parent and an NSIS installer running `pythonw.exe` against a non-`.py` `LICENSE.txt` argument are the entry-chain signals. **Triage:** legitimate Python tooling does not run `pythonw.exe` against a `LICENSE.txt` file from a Startup shortcut, nor register scheduled tasks under a `PythonLauncher-{3 chars}` name — either, combined with Polygon RPC egress from that process tree, distinguishes this activity from a developer's normal Python use.
