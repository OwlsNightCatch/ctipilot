---
schema: 1
kind: research
title: "macOS infostealer campaign shifts to ClickFix Terminal commands to deliver MacSync, SHub Stealer and AMOS"
headline: "Microsoft: macOS infostealer campaign moves from disk images to ClickFix Terminal-paste lures for MacSync, SHub and AMOS"
summary: "Microsoft reported on 2026-05-06 that a macOS infostealer campaign which earlier shipped disk images now hosts ClickFix-style instructions on standalone sites, Medium posts and Craft pages that tell users to paste a Base64-encoded command into Terminal, loading MacSync, SHub Stealer or AMOS. The stealers take Keychain entries, browser credentials, iCloud data and wallet data, and in some campaigns replace installed Ledger Wallet, Trezor Suite and Exodus apps with trojanized versions; macOS 26.4 and later blocks the paste of such commands."
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
entities:
  - "campaign:clickfix-macos-2026"
  - "malware:macsync"
techniques: [T1204.004, T1059.004, T1059.002, T1140, T1105, T1082, T1614.001, T1497.001, T1056.002, T1555.001, T1555.003, T1539, T1005, T1074.001, T1560, T1041, T1071.001, T1070.004, T1543.001, T1543.004, T1036.005, T1553.001, T1102.001, T1554]
affected_products: ["Apple macOS"]
cves: []
sources:
  - url: "https://www.microsoft.com/en-us/security/blog/2026/05/06/clickfix-campaign-uses-fake-macos-utilities-lures-deliver-infostealers/"
    publisher: "Microsoft Security Blog"
    date: "2026-05-06"
    role: primary
  - url: "https://www.malwarebytes.com/blog/threat-intel/2026/03/fake-cleanmymac-site-installs-shub-stealer-and-backdoors-crypto-wallets"
    publisher: "Malwarebytes"
    date: "2026-03-06"
    role: corroborating
closed_sources: []
evidence:
  - quote: "This recent activity reflects a shift in tradecraft, where threat actors instruct users to run Terminal commands that leverage native utilities to retrieve remotely hosted content, followed by script‑based loader execution."
    publisher: "Microsoft Security Blog"
    source_url: "https://www.microsoft.com/en-us/security/blog/2026/05/06/clickfix-campaign-uses-fake-macos-utilities-lures-deliver-infostealers/"
  - quote: "These commands, which are purported to install system utilities, load an infostealing malware like Macsync, Shub Stealer, and AMOS into the targets’ devices instead."
    publisher: "Microsoft Security Blog"
    source_url: "https://www.microsoft.com/en-us/security/blog/2026/05/06/clickfix-campaign-uses-fake-macos-utilities-lures-deliver-infostealers/"
  - quote: "The stealer was also observed replacing legitimate cryptocurrency wallets apps with attacker-controlled or trojanized ones:"
    publisher: "Microsoft Security Blog"
    source_url: "https://www.microsoft.com/en-us/security/blog/2026/05/06/clickfix-campaign-uses-fake-macos-utilities-lures-deliver-infostealers/"
  - quote: "Additionally, in macOS 26.4 and later, Apple has introduced a mitigation that directly addresses the ClickFix delivery mechanism."
    publisher: "Microsoft Security Blog"
    source_url: "https://www.microsoft.com/en-us/security/blog/2026/05/06/clickfix-campaign-uses-fake-macos-utilities-lures-deliver-infostealers/"
  - quote: "Flag unusual sequences of macOS utilities (curl, Base64, Gunzip, osascript, and dscl)."
    publisher: "Microsoft Security Blog"
    source_url: "https://www.microsoft.com/en-us/security/blog/2026/05/06/clickfix-campaign-uses-fake-macos-utilities-lures-deliver-infostealers/"
  - quote: "It can even modify wallet apps such as Exodus, Atomic Wallet, Ledger Wallet, and Ledger Live so attackers can later steal the wallet’s recovery phrase."
    publisher: "Malwarebytes"
    source_url: "https://www.malwarebytes.com/blog/threat-intel/2026/03/fake-cleanmymac-site-installs-shub-stealer-and-backdoors-crypto-wallets"
verification: single-source
sourcing_note: >
  The three campaigns and the shift from disk images to Terminal commands are Microsoft's own observations. Malwarebytes documented
  SHub Stealer's Terminal-paste delivery and wallet-app tampering independently, from a fake CleanMyMac site in March 2026, which
  corroborates that behaviour but not Microsoft's campaign findings.
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-10.md
updates:
  - at: "2026-10-21T20:25:53Z"
    run_id: 2026-10-21T1148Z-audit
    type: correction
    summary: >
      The campaign already targeted macOS through disk images; what Microsoft reported on 2026-05-06 is
      its shift to ClickFix Terminal commands, along three execution paths of which only one is a one-line
      shell pipeline. The stealers replace installed Ledger Wallet, Trezor Suite and Exodus apps with
      trojanized versions fetched from their C2, not DMG copies, and detection follows Microsoft's
      guidance on Terminal sessions, utility sequences and data staging.
    fields: [affected_products, body, classification, entities, evidence, headline, sources, sourcing_note, summary, techniques, title, verification]
---

Microsoft reported on 2026-05-06 that an infostealer campaign targeting macOS, whose earlier iterations delivered the stealers in disk-image (.dmg) files that users installed by hand, now instructs users to run Terminal commands that retrieve remote content with native utilities and then execute a script-based loader ([Microsoft, 2026-05-06](https://www.microsoft.com/en-us/security/blog/2026/05/06/clickfix-campaign-uses-fake-macos-utilities-lures-deliver-infostealers/)). The ClickFix-style instructions sit on standalone sites, on the note-taking platform Craft and in fake troubleshooting posts on Medium that promise to fix common macOS problems such as low disk space, and the pasted Base64 command decodes and runs an AppleScript or Bash loader ([Microsoft, 2026-05-06](https://www.microsoft.com/en-us/security/blog/2026/05/06/clickfix-campaign-uses-fake-macos-utilities-lures-deliver-infostealers/)). Scripts launched from Terminal do not undergo the code-signing and notarization evaluation Gatekeeper can apply to application bundles opened through Finder ([Microsoft, 2026-05-06](https://www.microsoft.com/en-us/security/blog/2026/05/06/clickfix-campaign-uses-fake-macos-utilities-lures-deliver-infostealers/)).

Microsoft tracks three execution paths. In the loader campaign, seen since February 2026, curl fetches a loader, a zsh script decodes a Base64 and Gzip payload and runs it with eval, fingerprints the host, stops on a Russian or CIS keyboard layout and runs a remote AppleScript stealer in memory through osascript; the stealer, which calls itself SHub Stealer, asks for the user's password as if installing a helper, validates it with dscl, stages browser credentials, Keychain entries, iCloud and Telegram data, wallets and small documents in a temporary folder, compresses and exfiltrates them and deletes the staging files, then persists as a LaunchAgent disguised as a Google software-update agent that runs Base64 commands returned by its C2 ([Microsoft, 2026-05-06](https://www.microsoft.com/en-us/security/blog/2026/05/06/clickfix-campaign-uses-fake-macos-utilities-lures-deliver-infostealers/)). The script campaign, seen in April 2026, streams a remote script straight into the shell from a one-line pipeline and persists an obfuscated AppleScript in a LaunchAgent that probes hard-coded C2 candidates with curl, falls back to a server identifier hidden on a Telegram bot page and pipes the server's response into osascript ([Microsoft, 2026-05-06](https://www.microsoft.com/en-us/security/blog/2026/05/06/clickfix-campaign-uses-fake-macos-utilities-lures-deliver-infostealers/)). The helper campaign (AMOS), seen since late January 2026, decodes and gunzips a first stage that downloads a Mach-O executable, strips its extended attributes, checks for virtualisation with system_profiler, copies Keychain databases and Chromium browser passwords and session cookies, exfiltrates a ZIP archive and installs a LaunchDaemon that runs a bash wrapper with root privileges at every boot to keep a backdoor running ([Microsoft, 2026-05-06](https://www.microsoft.com/en-us/security/blog/2026/05/06/clickfix-campaign-uses-fake-macos-utilities-lures-deliver-infostealers/)). In the loader and helper campaigns the stealer replaces installed Ledger Wallet and Trezor Suite apps, and in the loader campaign also Exodus, with trojanized versions fetched from its C2 ([Microsoft, 2026-05-06](https://www.microsoft.com/en-us/security/blog/2026/05/06/clickfix-campaign-uses-fake-macos-utilities-lures-deliver-infostealers/)); Malwarebytes documented SHub Stealer modifying wallet apps after a Terminal-paste lure on a fake CleanMyMac site in March 2026 ([Malwarebytes, 2026-03-06](https://www.malwarebytes.com/blog/threat-intel/2026/03/fake-cleanmymac-site-installs-shub-stealer-and-backdoors-crypto-wallets)).

**Exposure:** Mac users who can paste commands into Terminal; Apple has updated XProtect signatures, and macOS 26.4 and later blocks the paste of a potentially malicious command into Terminal, so earlier releases lack that mitigation ([Microsoft, 2026-05-06](https://www.microsoft.com/en-us/security/blog/2026/05/06/clickfix-campaign-uses-fake-macos-utilities-lures-deliver-infostealers/)).

**Detection:** process lineage: Terminal or shell sessions spawned by installers or user apps, and unusual sequences of curl, base64, gunzip, osascript and dscl; file telemetry for LaunchAgent and LaunchDaemon plists written by script interpreters; archive creation of collected data followed by an HTTP POST with curl ([Microsoft, 2026-05-06](https://www.microsoft.com/en-us/security/blog/2026/05/06/clickfix-campaign-uses-fake-macos-utilities-lures-deliver-infostealers/)).

**Defender takeaway:** managed Macs on macOS 26.4 or later get Apple's paste blocking against this delivery; on a Mac where the chain ran, treat the Keychain, browser passwords and session cookies as stolen and reinstall wallet apps from their vendors, because the stealer replaces Ledger Wallet, Trezor Suite and Exodus with trojanized copies ([Microsoft, 2026-05-06](https://www.microsoft.com/en-us/security/blog/2026/05/06/clickfix-campaign-uses-fake-macos-utilities-lures-deliver-infostealers/)).

## Correction — 2026-10-21T20:25:53Z

The campaign did not newly expand to macOS: its earlier iterations already delivered the stealers to Macs in disk-image files, and the change Microsoft reported is the move to Terminal commands that fetch remote content and run a script-based loader ([Microsoft, 2026-05-06](https://www.microsoft.com/en-us/security/blog/2026/05/06/clickfix-campaign-uses-fake-macos-utilities-lures-deliver-infostealers/)). Only the script campaign uses a one-line pipeline into the shell; the loader campaign runs a zsh loader through eval and the helper campaign downloads a Mach-O executable ([Microsoft, 2026-05-06](https://www.microsoft.com/en-us/security/blog/2026/05/06/clickfix-campaign-uses-fake-macos-utilities-lures-deliver-infostealers/)). The wallet tampering replaces installed Ledger Wallet, Trezor Suite and Exodus apps with trojanized archives fetched from the C2 ([Microsoft, 2026-05-06](https://www.microsoft.com/en-us/security/blog/2026/05/06/clickfix-campaign-uses-fake-macos-utilities-lures-deliver-infostealers/)). Detection rests on Microsoft's guidance: Terminal or shell sessions spawned by installers or user apps, unusual curl, base64, gunzip, osascript and dscl sequences, and archive creation followed by an HTTP POST ([Microsoft, 2026-05-06](https://www.microsoft.com/en-us/security/blog/2026/05/06/clickfix-campaign-uses-fake-macos-utilities-lures-deliver-infostealers/)).
