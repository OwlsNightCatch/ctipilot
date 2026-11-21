---
schema: 1
kind: threat
title: "TELEPUZ — a modular Windows RAT/MaaS spread through ClickFix→Vidar chains, executing syscalls from patched trusted DLLs"
headline: "Elastic details TELEPUZ, a MaaS RAT hiding syscalls in patched Windows DLLs, with C2 discovery via Telegram, Steam, DNS and a Polygon smart contract"
summary: >
  Elastic Security Labs is tracking TELEPUZ, a full-featured modular Windows RAT active since
  late April 2026 and spreading via a ClickFix→Vidar chain that ends in a rundll32-loaded DLL.
  It executes indirect syscalls from the .text section of a randomly chosen legitimate DLL to
  bypass user-mode hooking, patches AMSI/ETW, escalates via UAC bypass and token theft, and
  discovers its WebSocket C2 through four decentralized fallbacks (a Telegram bio, a Steam
  profile, a DNS TXT record and a Polygon smart contract). It ships a keylogger, stealer and a
  CDP/WebDriver-BiDi banking web-injection module. Relevant to any Windows fleet exposed to
  ClickFix lures; Elastic released a public YARA rule.
discovered_at: "2026-07-16T04:40:00Z"
event_date: "2026-07-16"
run_id: 2026-07-16T0409Z-intel
priority: notable
immediate_action: null
tags: [phishing, infostealer]
regions: [global]
sectors: [finance, technology]
entities: [tool:telepuz-maas-malware]
techniques: [T1204.004, T1105, T1218.011, T1106, T1620, T1055.012, T1685, T1548.002, T1134.001, T1543.003, T1614.001, T1497.001, T1622, T1056.001, T1071.001, T1573.002]
affected_products: []
cves: []
sources:
  - url: "https://www.elastic.co/security-labs/telepuz-maas-malware-clickfix"
    publisher: "Elastic Security Labs"
    date: "2026-07-16"
    role: primary
closed_sources: []
evidence:
  - quote: "Given the significant number of builds uploaded to VirusTotal daily, it is likely that we are dealing with a MaaS."
    publisher: "Elastic Security Labs"
  - quote: "Finally, the malware selects a random library from a set of standard libraries (dfscli.dll, davhlpr.dll, msdtclog.dll, dsrole.dll, and secur32.dll) and loads it via LoadLibrary. It then patches the library's .text section with the previously generated trampolines, so indirect syscalls are now executed from this location."
    publisher: "Elastic Security Labs"
verification: single-source
sourcing_note: "Single-source technical analysis from Elastic Security Labs (a reputable vendor research lab; write-up ships a public YARA rule and full ATT&CK mapping). No independent second-lab corroboration yet — treated as single-source research, not attacker-claim, so no fake-news carve-out is needed."
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

Elastic Security Labs is tracking **TELEPUZ**, a full-featured, fast-evolving modular Windows RAT active since late April 2026 and, on Elastic's telemetry, a likely malware-as-a-service given the daily volume of new builds uploaded to VirusTotal ([Elastic Security Labs, 2026-07-16](https://www.elastic.co/security-labs/telepuz-maas-malware-clickfix)). Delivery runs through a **ClickFix** social-engineering lure that pastes a PowerShell one-liner into the Run dialog, which downloads a Go variant of the Vidar stealer; Vidar then fetches a small stager (`install.exe`) that loads the main payload — a 64-bit DLL executed via `rundll32` from domain-rotating staging infrastructure ([Elastic Security Labs, 2026-07-16](https://www.elastic.co/security-labs/telepuz-maas-malware-clickfix)).

The payload's headline evasion is an indirect-syscall engine: it maps a fresh copy of `ntdll.dll`, parses syscall numbers from its export table, then patches the `.text` section of a randomly chosen legitimate DLL (`dfscli.dll`, `davhlpr.dll`, `msdtclog.dll`, `dsrole.dll` or `secur32.dll`) with syscall trampolines so calls execute from inside a trusted-looking module, defeating user-mode API hooking and ETW ([Elastic Security Labs, 2026-07-16](https://www.elastic.co/security-labs/telepuz-maas-malware-clickfix)). It additionally patches AMSI/ETW to neutered return values, unhooks NTDLL, reflectively loads modules and runs downloaded PEs via process hollowing, escalates through two UAC-bypass techniques and SYSTEM token theft, and persists as a service named `CipherAllocator`. Command-and-control runs over WebSocket (optionally SChannel TLS) at a `/cdn/health?sid=` URI, with four fallback address-discovery channels — a Telegram channel bio, a Steam profile, a DNS TXT record and a Polygon smart-contract call (also a kill switch). Modules include a keylogger, an infostealer with a Chrome App-Bound-Encryption cookie helper, and a browser web-injection module that uses Chrome DevTools Protocol / Firefox WebDriver BiDi (not code injection) to swap IBAN/amount fields in banking web forms; the malware also runs anti-analysis checks — debugger evasion (`ProcessDebugPort`/`ThreadHideFromDebugger`) and sandbox/host geofencing on CIS country, sandbox hostnames and usernames.

**Defender takeaway:** signature and user-mode-hook-based detection degrade against the indirect-syscall-from-patched-DLL design, so hunt on behaviour and lineage — process-creation telemetry showing `rundll32` (or a service process) making outbound network connections it never normally makes, and integrity anomalies where a signed system DLL's `.text` section has been modified in memory. ClickFix delivery means the earliest observable is a user-spawned `PowerShell.exe` from the Run dialog (`explorer.exe` parent) fetching a remote binary. **Triage:** a legitimate `rundll32`-hosted process does not open outbound WebSocket connections; a `rundll32` (or `CipherAllocator` service) process reaching a `/cdn/health?sid=` WebSocket endpoint, combined with fixed-return-value AMSI/ETW patch stubs in that process, is the distinguishing sequence — either signal alone is weaker than the two together. Elastic published a YARA rule (`Windows_Trojan_Telepuz`) alongside the write-up.
