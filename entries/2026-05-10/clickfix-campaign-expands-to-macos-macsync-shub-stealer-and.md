---
schema: 1
kind: research
horizon: operational
title: "ClickFix campaign expands to macOS — Macsync, Shub Stealer and AMOS delivered via Base64 Terminal commands that bypass Gatekeeper"
headline: "ClickFix campaign expands to macOS — Macsync, Shub Stealer and AMOS delivered via Base64 Terminal commands that bypass Gatekeeper"
summary: "Microsoft Threat Intelligence on 2026-05-06 documented an active ClickFix social-engineering campaign now targeting macOS users via fake utility-installation guides hosted on Medium, Squarespace, and Craft-built blogs (Microsoft Security Blog, 2026-05-06 · Malwarebytes — Shub Stealer earlier wave, 2026-03)."
discovered_at: "2026-05-10T05:00:07Z"
event_date: 2026-05-06
run_id: 2026-05-10-001
priority: notable
immediate_action: null
tags:
  - phishing
  - infostealer
regions:
  - global
sectors:
  - technology
  - finance
entities: []
cves: []
sources:
  - url: "https://www.microsoft.com/en-us/security/blog/2026/05/06/clickfix-campaign-uses-fake-macos-utilities-lures-deliver-infostealers/"
    publisher: "Microsoft Security Blog, 2026-05-06"
    role: primary
  - url: "https://www.malwarebytes.com/blog/threat-intel/2026/03/fake-cleanmymac-site-installs-shub-stealer-and-backdoors-crypto-wallets"
    publisher: "Malwarebytes — Shub Stealer earlier wave, 2026-03"
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
migrated_from: briefs/2026-05-10.md
---

Microsoft Threat Intelligence on 2026-05-06 documented an active ClickFix social-engineering campaign now targeting macOS users via fake utility-installation guides hosted on Medium, Squarespace, and Craft-built blogs ([Microsoft Security Blog, 2026-05-06](https://www.microsoft.com/en-us/security/blog/2026/05/06/clickfix-campaign-uses-fake-macos-utilities-lures-deliver-infostealers/) · [Malwarebytes — Shub Stealer earlier wave, 2026-03](https://www.malwarebytes.com/blog/threat-intel/2026/03/fake-cleanmymac-site-installs-shub-stealer-and-backdoors-crypto-wallets)). The lure pages instruct the visitor to copy a Base64-encoded command into Terminal; the decoded one-liner pipes a remote shell payload directly to `bash`, bypassing Gatekeeper because no signed application bundle is ever launched. Three distinct infostealers — **Macsync**, **Shub Stealer**, and **AMOS (Atomic macOS Stealer)** — are delivered across campaign variants per Microsoft, harvesting macOS Keychain entries, browser-profile credentials, iCloud data, and cryptocurrency wallet keys (Trezor, Ledger, Exodus, Electrum, Atomic, Coinomi, MetaMask, Phantom). Some variants substitute backdoored DMG copies of legitimate wallet applications (Ledger Live, Trezor Suite). Persistence uses LaunchAgent / LaunchDaemon plists with Telegram-fallback C2.

ATT&CK mapping: [T1204.002 User Execution: Malicious File](https://attack.mitre.org/techniques/T1204/002/), [T1059.004 Unix Shell](https://attack.mitre.org/techniques/T1059/004/), [T1555.001 Credentials from Password Stores: Keychain](https://attack.mitre.org/techniques/T1555/001/). **Detection concepts:** alert on Terminal spawning `curl` / `wget` immediately followed by pipe-to-shell execution from a non-developer profile; LaunchAgent file-creation events from outside `/Applications` or `/Library/Application Support/<vendor>` paths; anomalous Keychain API calls from processes without UI entitlements (Endpoint Security framework `ES_EVENT_TYPE_NOTIFY_OPENSSH`-style hooks expose this on EDR-instrumented Macs).
