---
schema: 1
kind: threat
title: "FamousSparrow retires SparrowDoor for SparroWocky, a modular backdoor with BOF-loading and call-stack spoofing, deployed almost exclusively against Latin American governments"
headline: "ESET: a China-aligned actor's new backdoor forges call stacks with legitimate kernel32.dll gadgets so its hooked API calls look native"
summary: >
  ESET documents FamousSparrow's shift to SparroWocky, a new modular C++ backdoor active since
  August 2025 that has replaced SparrowDoor as the group's flagship implant; 90% of observed
  2025-2026 targeting hit Latin America, with government entities named among the targets, and attribution
  based on SparrowDoor deploying the new backdoor in early attacks.
discovered_at: "2026-09-18T04:56:00Z"
updated_at: null
event_date: "2026-09-17"
run_id: 2026-09-18T0410Z-intel
priority: notable
immediate_action: null
tags: [nation-state, espionage]
regions: [latam]
sectors: [public-sector]
entities: ["actor:famoussparrow", "malware:sparrowocky"]
techniques: [T1583.003, T1587.001, T1608.001, T1190, T1059.003, T1569.002, T1106, T1559, T1574.001, T1547.001, T1543.003, T1134.002, T1140, T1480.002, T1564.010, T1027.007, T1620, T1070.004, T1070.009, T1036.001, T1036.004, T1083, T1680, T1082, T1033, T1120, T1005, T1113, T1573.002, T1573.001, T1090.001, T1090.002, T1095, T1041]
affected_products: []
cves: []
sources:
  - url: "https://www.welivesecurity.com/en/eset-research/beware-sparrowock-backdoor-bites-commands-catch/"
    publisher: "ESET (WeLiveSecurity)"
    date: "2026-09-17"
    role: primary
closed_sources: []
evidence:
  - quote: "We believe that this focus is not coincidental and likely reflects China's reaction to various recent US initiatives in the region."
    publisher: "ESET (WeLiveSecurity)"
    source_url: "https://www.welivesecurity.com/en/eset-research/beware-sparrowock-backdoor-bites-commands-catch/"
  - quote: "Based on our investigation, we attribute the latest campaign and the SparroWocky backdoor to FamousSparrow with high confidence, since in some of the first attacks involving this backdoor, SparroWocky was deployed by the FamousSparrow-exclusive SparrowDoor."
    publisher: "ESET (WeLiveSecurity)"
    source_url: "https://www.welivesecurity.com/en/eset-research/beware-sparrowock-backdoor-bites-commands-catch/"
verification: single-source
sourcing_note: >
  ESET's own primary research; no independent corroboration found in-window. This is the
  discovering lab's own detailed telemetry-based write-up with a self-published, complete
  MITRE ATT&CK mapping table.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

ESET documents FamousSparrow's shift to a new flagship backdoor, SparroWocky, replacing SparrowDoor as the group's main implant since August 2025 ([ESET, 2026-09-17](https://www.welivesecurity.com/en/eset-research/beware-sparrowock-backdoor-bites-commands-catch/)). From mid-2025 into 2026, 90% of FamousSparrow's observed targets were in Latin America — Argentina, Ecuador, Guatemala, Honduras, Panama, Peru, Puerto Rico and Venezuela — with government entities named among the targets, an unusually sustained single-region focus for a China-aligned group ESET otherwise tracks globally; ESET assesses the focus likely reflects Chinese state interest in monitoring regional government reactions to renewed US engagement, citing a Panamanian port-concession dispute as a specific target-motive match ([ESET, 2026-09-17](https://www.welivesecurity.com/en/eset-research/beware-sparrowock-backdoor-bites-commands-catch/)). SparroWocky deploys via a "trident loader": a legitimate executable, a side-loading DLL with a patched .text-section entry point that keeps the impersonated module's export table and metadata intact, and an RC4-encrypted .dat payload whose decrypted PE has its MZ/PE header bytes stripped before being reflectively mapped into memory. The backdoor incorporates Mbed TLS for its C2 channel and MinHook for API hooking, and runs a modified TrustedSec COFF loader that executes Cobalt Strike, Brute Ratel, Metasploit and Sliver-compatible Beacon Object Files, redirecting BOF-imported-symbol calls through a stack-spoofing subroutine. Its anti-analysis techniques include a SilentMoonwalk-style call-stack forger that uses JOP/ROP gadgets inside legitimate kernel32.dll so hooked API calls appear to originate from RtlUserThreadStart or BaseThreadInitThunk, and a MinHook-based CreateThread hook that reports the benign-looking AnimateWindow as the thread's start address; for dynamically loaded PE payloads, the backdoor also forges a fake LDR_DATA_TABLE_ENTRY structure in the PEB_LDR_DATA doubly linked list Windows uses to track loaded modules, a list security products routinely monitor. Persistence is operator-configurable via a Windows service or a registry Run key. ESET attributes SparroWocky to FamousSparrow with high confidence, since early attacks show the FamousSparrow-exclusive SparrowDoor deploying the new backdoor directly.

**Defender takeaway:** any government-sector defender building detection content for DLL side-loading, in-memory BOF execution or call-stack-spoofing anti-analysis should treat this as a current reference implementation — hunt for a CreateThread call whose reported start address is a benign-looking API rather than a loader-internal function, and for hooked API calls whose return-address chain traces through legitimate kernel32.dll gadgets instead of a normal call stack.

**Triage:** call-stack forgery targeting RtlUserThreadStart or BaseThreadInitThunk is not something a legitimate application produces; a stack walk that resolves cleanly to one of those two entry points via JOP/ROP gadgets in kernel32.dll, rather than a normal thread-creation call chain, is the discriminator ESET's own analysis supports.
