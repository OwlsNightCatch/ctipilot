---
schema: 1
kind: research
title: "Kaspersky: the HelloNet campaign blinds user-mode security tools by hooking raw AFD IOCTLs, persisting via DLL-sideload into a secure-network product's own auto-updater"
headline: "HelloNet chains trusted-updater DLL sideloading with raw AFD-IOCTL interception to hide network C2 from user-mode EDR"
summary: >
  Kaspersky GReAT documented "HelloNet," an active APT campaign that persists by sideloading a malicious
  wtsapi32.dll into the auto-launched update component of the ViPNet secure-networking suite, then injects a proxy
  module (HelloProxy) into svchost.exe that uses Microsoft Detours to hook NtDeviceIoControlFile and intercept the
  raw Ancillary Function Driver IOCTLs (AFD_RECV, AFD_GET_TDI_HANDLES) — which, per Kaspersky, hinders user-mode
  network-filtering security tools. Direct victimology is Russian government and critical-infrastructure orgs
  (attributed with low confidence to an unknown Chinese-speaking group); the transferable signal for Swiss/EU
  defenders is the technique class — abuse of a trusted client's update mechanism plus AFD-IOCTL interception to
  degrade EDR network visibility.
discovered_at: "2026-07-17T04:35:00Z"
event_date: "2026-07-16"
run_id: 2026-07-17T0409Z-intel
priority: notable
immediate_action: null
tags: [espionage, supply-chain]
regions: [russia-cis]
sectors: [energy, transport, education]
entities: ["campaign:hellonet-vipnet-supply-chain", "tool:hellonet-malware-suite"]
techniques: [T1574.001, T1055, T1685, T1572, T1105, T1070, T1082, T1087.002]
affected_products: ["InfoTeCS ViPNet"]
cves: []
sources:
  - url: "https://securelist.com/hellonet-vipnet/120700/"
    publisher: "Kaspersky Securelist (GReAT)"
    date: "2026-07-16"
    role: primary
closed_sources: []
evidence:
  - quote: "By placing the file in this directory, the attackers implement the DLL Sideloading technique — the ViPNet update system executable file itcsrvup64.exe, which is launched at OS startup, is susceptible to it."
    publisher: "Kaspersky Securelist (GReAT)"
  - quote: "These codes are used during socket operations — their interception allows the malware to hinder security solutions operating in user mode for filtering network connections."
    publisher: "Kaspersky Securelist (GReAT)"
  - quote: "At present, we link this campaign to the activities of an unknown Chinese-speaking APT group with a low degree of confidence."
    publisher: "Kaspersky Securelist (GReAT)"
verification: single-source
sourcing_note: "Sole primary is Kaspersky Securelist/GReAT (Admiralty B research lab), uncorroborated at composition. Attribution is explicitly low-confidence — Kaspersky flags the two supporting artifacts (a news.sina.com string; Rust crates fetched from a USTC mirror) as possibly unintentional or false flags — so no nexus is asserted here. Included for the transferable technique class, not the Russian victimology."
confidence: medium
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

Kaspersky's GReAT team detailed "HelloNet," an APT campaign (active since at least May 2026) that abuses the update mechanism of ViPNet — a Russian GOST-certified secure-networking suite — to persist inside targeted Russian government, energy, transport, education, logistics and industrial organizations ([Kaspersky Securelist, 2026-07-16](https://securelist.com/hellonet-vipnet/120700/)). The attackers drop a malicious `wtsapi32.dll` into the ViPNet update directory that the OS-start-launched updater `itcsrvup64.exe` sideloads. That loader ("HelloInjector") injects a second stage ("HelloProxy") into `svchost.exe` — but only after verifying the target's name is `svchost.exe` and its command line carries `netsvcs`. HelloProxy's distinguishing move is defense evasion at the socket layer: it uses the Microsoft Detours library to hook `NtDeviceIoControlFile`, `closesocket` and `shutdown`, intercepting the raw AFD IOCTL codes `AFD_RECV` (0x12017) and `AFD_GET_TDI_HANDLES` (0x12037) so that, in Kaspersky's words, it can "hinder security solutions operating in user mode for filtering network connections." It then acts as a traffic proxy or in-memory loader for further modules — recovered examples include "HelloExecutor" (shell-command execution) and "HelloCleaner" (deletes ViPNet log files to hide activity) — and on one host the operators opened an SSH reverse tunnel using a legitimate Plink binary renamed `frontpage.exe`.

**Defender takeaway:** for this constituency the ViPNet-specific vector is largely irrelevant, but two technique classes generalize directly. First, any third-party secure-network/VPN client with an auto-launched updater in a writable directory is a DLL-sideload persistence surface — treat vendor-updater directories as monitored locations where an unsigned or unexpected DLL write is high-signal. Second, AFD-IOCTL interception is a portable primitive for blinding user-mode network-filtering EDR; a Detours-style hook on `NtDeviceIoControlFile` in `svchost.exe` is worth surfacing regardless of the product being abused. **Triage:** a `wtsapi32.dll` written into a vendor's update directory has no legitimate reason to be there (the DLL belongs in `System32`); the vendor's own updater loading a DLL whose signature does not carry the vendor's publisher name, and a Plink/PuTTY binary identified by PE metadata rather than filename opening a `-R port:addr:port` tunnel, are the discriminators Kaspersky's hunt guidance keys on.
