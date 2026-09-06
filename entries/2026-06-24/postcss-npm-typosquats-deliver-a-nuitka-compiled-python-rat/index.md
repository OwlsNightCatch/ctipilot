---
schema: 1
kind: threat
title: PostCSS npm typosquats deliver a Nuitka-compiled Python RAT with Chrome DPAPI credential theft
headline: PostCSS npm typosquats deliver a Nuitka-compiled Python RAT with Chrome DPAPI credential theft
summary: "Three malicious npm packages typosquatting postcss-selector-parser (150M weekly downloads) ship an AES-256-GCM-encrypted dropper that pulls a Nuitka-compiled Python RAT with Chrome DPAPI credential theft and Run-key persistence. Any CI runner or developer host that installed postcss-minify-selector(-parser) or aes-decode-runner-pro should be treated as compromised (JFrog, 2026-06-22)."
discovered_at: "2026-06-24T05:11:46Z"
event_date: 2026-06-23
run_id: 2026-06-24-de656486
priority: high
immediate_action: null
tags:
  - supply-chain
  - infostealer
  - organized-crime
  - identity
regions:
  - global
sectors:
  - technology
entities: []
cves: []
sources:
  - url: "https://research.jfrog.com/post/from-postcss-typosquat-to-windows-rat/"
    publisher: JFrog Security Research
    role: primary
  - url: "https://thehackernews.com/2026/06/malicious-npm-packages-pose-as-postcss.html"
    publisher: The Hacker News
    role: corroborating
closed_sources: []
evidence:
  - quote: "The npm publisher observed during the investigation was abdrizak. During the review, we found three related packages: aes-decode-runner-pro, postcss-minify-selector, postcss-minify-selector-parser"
    publisher: JFrog Security Research
  - quote: The decoded blobs we analyzed from postcss-minify-selector-parser and aes-decode-runner-pro both lead to the same PowerShell downloader and Windows payload chain
    publisher: JFrog Security Research
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
migrated_from: briefs/2026-06-24.md
---

JFrog Security Research disclosed (2026-06-22) three malicious npm packages published by the account `abdrizak` — `postcss-minify-selector-parser`, `postcss-minify-selector` and `aes-decode-runner-pro` — that typosquat the legitimate `postcss-selector-parser` (150M+ weekly downloads) ([JFrog, 2026-06-22](https://research.jfrog.com/post/from-postcss-typosquat-to-windows-rat/); [The Hacker News, 2026-06-23](https://thehackernews.com/2026/06/malicious-npm-packages-pose-as-postcss.html)). On import, each package's `index.js` decrypts an AES-256-GCM blob and runs a JavaScript dropper that writes and executes a PowerShell downloader (`settings.ps1`); PowerShell pulls a Windows payload from an attacker-controlled host, a VBScript bootstrapper (`update.vbs`) extracts an archive, and a Nuitka-compiled Python 3.10 RAT (`chost.exe` loading `loader.py` plus six `.pyd` extension modules) activates. The RAT performs RC4-encrypted HTTP POST C2, registry Run-key persistence under `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`, VM detection via WMI and adapter-MAC heuristics, remote shell, file transfer, and Chrome credential and extension-data theft via a DPAPI / app-bound-encryption bypass.

**Why it matters to us:** This is the npm typosquat-to-RAT pattern aimed squarely at developer endpoints and CI/CD runners — the highest-trust hosts in a software supply chain. Mapped to `T1195.001`/`T1195.002` (Supply Chain Compromise), `T1059.001` (PowerShell), `T1027` (obfuscation — AES + Nuitka), `T1547.001` (Registry Run Key), `T1555.003` (Credentials from Web Browsers). Detection concepts (no IOCs): alert on `node`/`npm`/`npx` parent processes spawning `powershell.exe` (Sysmon EID 1 with parent-image filter); `wscript.exe`/`cscript.exe` executing from `%TEMP%`; new `HKCU\...\Run` values written by a Node toolchain; and Python runtimes in `%TEMP%` making outbound HTTP POST. Remediation is not "remove the package" — any host that installed these versions should have all browser-stored and developer credentials rotated and be treated as compromised.
