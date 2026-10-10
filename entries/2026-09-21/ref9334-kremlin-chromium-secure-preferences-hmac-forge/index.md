---
schema: 1
kind: threat
title: "REF9334/KREMLIN forges Chromium's own Secure Preferences integrity hashes to silently install a banking-fraud browser extension outside the Web Store, resolving C2 through an Ethereum smart contract"
headline: "Elastic Security Labs: a Brazilian banking-fraud toolkit defeats Chromium's extension-integrity check by extracting the browser's own signing keys from memory"
summary: >
  Elastic Security Labs tracked REF9334, a Brazilian-banking-focused operation active across seven
  campaigns since May 2025, whose KREMLIN toolkit recovers Chromium's App-Bound encryption key
  directly from browser process memory, uses it to forge the HMACs and hashes Chromium's Secure
  Preferences integrity mechanism requires, and manually installs a malicious extension into the
  browser profile exactly as if a user had approved it through the Chrome Web Store — with no user
  interaction and no visible warning. The toolkit resolves its payload configuration through an
  Ethereum smart contract and abuses a legitimate SentinelOne binary for DLL sideloading.
discovered_at: "2026-09-21T04:46:00Z"
updated_at: null
event_date: "2026-09-14"
run_id: 2026-09-21T0410Z-intel
priority: notable
immediate_action: null
tags:
  - infostealer
  - cryptocrime
  - identity
regions:
  - latam
sectors: []
entities:
  - "actor:ref9334"
  - "malware:kremlin"
techniques:
  - T1204.002
  - T1497
  - T1027.007
  - T1574.001
  - T1176
  - T1553
  - T1555.003
  - T1102.001
  - T1105
affected_products: ["Google Chrome", "Microsoft Edge", "SentinelOne SentinelMemoryScanner.exe"]
cves: []
sources:
  - url: "https://www.elastic.co/security-labs/threat-command/malicious-browser-extension-kremlin-banking-malware"
    publisher: "Elastic Security Labs"
    date: "2026-09-14"
    role: primary
closed_sources: []
evidence:
  - quote: "Malicious browser extensions bypass Chromium integrity mechanisms by manipulating Secure Preferences and regenerating required HMACs and App-Bound encrypted hashes."
    publisher: "Elastic Security Labs"
    source_url: "https://www.elastic.co/security-labs/threat-command/malicious-browser-extension-kremlin-banking-malware"
  - quote: "KREMLIN uses a documented technique rarely observed in malware: it manually copies the extension into the browser's profile directories and registers it in the Secure Preferences file."
    publisher: "Elastic Security Labs"
    source_url: "https://www.elastic.co/security-labs/threat-command/malicious-browser-extension-kremlin-banking-malware"
  - quote: "Threat Command temporarily disrupted over 1,500 (and counting) infections in this reported campaign by registering the network canary (kill switch) domain"
    publisher: "Elastic Security Labs"
    source_url: "https://www.elastic.co/security-labs/threat-command/malicious-browser-extension-kremlin-banking-malware"
verification: single-source
sourcing_note: >
  Elastic Security Labs is the sole publisher. Its own reporting explicitly notes the "KREMLIN" name is
  the malware author's own coinage and that nothing about the operation indicates a Russian nexus
  (Portuguese-language lures/comments and Ethereum transaction timestamps that Elastic's own executive summary
  describes as clustering during São Paulo working hours; its technical analysis separately finds only a small
  minority of transactions falling in late-night hours, none extending into early morning, and reasons this is
  more consistent with operators working late than waking before dawn — corroborating, not diverging from, the
  same São Paulo conclusion — together point to Brazil);
  this entry's title and body preserve that clarification to avoid implying a Russian state connection.
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

Elastic Security Labs has tracked REF9334, a Brazilian-banking-focused operation, across seven campaigns since May 2025 ([Elastic Security Labs, 2026-09-14](https://www.elastic.co/security-labs/threat-command/malicious-browser-extension-kremlin-banking-malware)). Its toolkit, KREMLIN — a name the malware's own author chose; Elastic states nothing about the operation is actually Russian: Portuguese-language lures and code comments, and Ethereum transaction timestamps its executive summary describes as clustering during São Paulo working hours — its technical analysis separately finds only a small minority of transactions falling in late-night hours, none extending into early morning, and reasons this is more consistent with operators working late than waking before dawn, corroborating rather than contradicting the same São Paulo conclusion — instead point to Brazil. KREMLIN's infection chain begins with an obfuscated, multi-stage JavaScript loader (trivially de-obfuscated by an LLM, per Elastic) that checks sandbox indicators such as desktop file count and WMI process count before decoding a second stage via `certutil` and downloading Node.js to run it. That second stage installs persistence disguised as a scheduled task named "MicrosoftNodeRuntimeUpdater," then queries an Ethereum smart contract for three configuration parameters: a main module URL, a .NET RunPE injector hidden as Base64-encoded JPEG data, and a legitimate SentinelOne `SentinelMemoryScanner.exe` binary abused for DLL sideloading — a technique Symantec first documented in a separate Seedworm intrusion. The main C++ installer resolves NTDLL syscall numbers indirectly, by correlating export names against the `.pdata` exception-directory `RUNTIME_FUNCTION` table rather than parsing `Nt*`/`Zw*` stubs directly, and runs extensive sandbox and analysis-tool checks — process-name blacklists, a hardcoded username blacklist, CPU/RAM thresholds, a deliberately-unregistered-domain network canary, and VMware/VirtualBox artifact checks — before proceeding.

The extension-installation step is the toolkit's most technically striking element, documented in detail by Synacktiv's "Phantom Extension" research and rarely seen deployed in the wild: KREMLIN waits for the browser to close, or for the user to idle for two minutes and then force-terminates it if still open, then relaunches the browser under a debugger specifically to catch the `LOAD_DLL_DEBUG_EVENT` for `chrome.dll` or `msedge.dll`, scans that module's memory for a string cross-reference to `OSCrypt.AppBoundProvider.Decrypt.ResultCode` to locate and read the in-memory App-Bound encryption key via `ReadProcessMemory`, and separately recovers the legacy DPAPI-protected OSCrypt key from Local State. Using the recovered keys plus a seed extracted from `resources.pak`, a sibling file in the Chrome installation directory, KREMLIN regenerates the legacy HMAC and the newer OSCrypt-encrypted SHA-256 hash that Chromium's Secure Preferences integrity mechanism requires, then manually copies the extension's files into the browser profile and edits Secure Preferences directly — enabling developer mode, registering the extension under `extensions.settings.<id>`, and writing the forged `protection.macs` values — installing the extension exactly as if a user had approved it through the Web Store, with no user interaction and no visible warning. Elastic disrupted over 1,500 infections by registering the operation's network-canary kill-switch domain.

**Defender takeaway:** any Chrome or Edge estate should treat the discovery of a browser extension present in a profile's Secure Preferences without a corresponding Web Store installation event in the browser's own history as a high-confidence compromise indicator, since KREMLIN's entire installation method exists specifically to produce that mismatch. Organizations running SentinelOne should confirm `SentinelMemoryScanner.exe` is only ever loaded from its expected install path and flag any DLL-sideload attempt against it. A browser being force-relaunched under a debugger by another process is itself an anomalous, alertable event on an endpoint with no legitimate debugging workflow for that browser.

**Triage:** extensions are routinely installed and removed through the Web Store's own mechanism, so an extension's mere presence is not the signal — the discriminator is provenance: an extension entry in Secure Preferences with no matching Web Store installation event, or `extensions.settings` entries whose `protection.macs` values were written outside a normal browser-update or user-installation flow.
