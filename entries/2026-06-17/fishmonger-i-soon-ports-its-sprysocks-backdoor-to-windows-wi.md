---
schema: 1
kind: threat
horizon: operational
title: FishMonger (I-SOON) ports its SprySOCKS backdoor to Windows with a kernel-driver rootkit
headline: FishMonger (I-SOON) ports its SprySOCKS backdoor to Windows with a kernel-driver rootkit
summary: "ClickFix delivery frameworks are scaling — Sekoia details ErrTraffic (blockchain-resolved C2, EU WordPress targeting) and Huntress documents the Potemkin loader/RMMProject (Chromium App-Bound-Encryption bypass); FishMonger/I-SOON also ported its SprySOCKS backdoor to Windows with a kernel rootkit (§ 1, § 3)."
discovered_at: "2026-06-17T05:14:26Z"
event_date: 2026-06-16
run_id: 2026-06-17-e102009c
priority: high
immediate_action: null
tags:
  - espionage
  - nation-state
  - china-nexus
regions:
  - apac
  - global
sectors:
  - public-sector
  - telco
  - technology
entities: []
cves: []
sources:
  - url: "https://www.welivesecurity.com/en/eset-research/fishmongers-arsenal-upgraded-sprysocks-windows/"
    publisher: "ESET WeLiveSecurity, 2026-06-16"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/windows-version-of-sprysocks-linux-malware-used-to-attack-govt-orgs/"
    publisher: "BleepingComputer, 2026-06-16"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-17.md
---

ESET disclosed two previously undocumented Windows variants of SprySOCKS — a backdoor it attributes to FishMonger (a.k.a. Earth Lusca / Aquatic Panda / TAG-22), assessed with high confidence as operated by Chinese contractor I-SOON ([ESET WeLiveSecurity, 2026-06-16](https://www.welivesecurity.com/en/eset-research/fishmongers-arsenal-upgraded-sprysocks-windows/)). Previously known only as a Linux backdoor, the Windows builds (WIN_PLUS and WIN_DRV) were deployed in 2023–2024 against foreign-affairs, technology and telecom government bodies in Taiwan, Thailand, Pakistan and Honduras. WIN_PLUS persists as a Windows Print Processor (`VSPMsg`) and supports 30+ commands over TCP/UDP/WebSocket. WIN_DRV is the notable one: it loads a kernel driver (`fsdiskbit.sys`, signed with a certificate from the public PastDSE leaked-cert corpus) which memory-loads a second driver to deliver rootkit-class stealth — hiding processes, files, network connections and registry keys, and performing TCP traffic diversion so the backdoor receives operator commands on an arbitrary port that never appears in `netstat` ([BleepingComputer, 2026-06-16](https://www.bleepingcomputer.com/news/security/windows-version-of-sprysocks-linux-malware-used-to-attack-govt-orgs/)). ESET notes limited, unconfirmed telemetry of a possible UEFI bootkit component (potentially CVE-2023-24932-class Secure Boot bypass).

**Why it matters to us:** Post-deployment detection is hard because the driver actively hides artefacts; the leverage is pre-deployment hygiene. Hunt scheduled-task creation (EID 4698 / Sysmon EID 1) referencing binaries under `%SystemRoot%\Fonts\`, Image File Execution Options hijacks of `vds.exe`, and kernel-driver loads (Sysmon EID 6) of drivers signed with PastDSE-derived certificates. Because TCP diversion defeats host network-tab inspection, rely on EDR kernel sensors / ETW for listening-socket enumeration. Validate that vulnerable/revoked drivers are blocked via WDAC/HVCI and the Microsoft vulnerable-driver blocklist.
