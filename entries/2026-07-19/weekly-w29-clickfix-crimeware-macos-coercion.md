---
schema: 1
kind: research
horizon: strategic
weekly_section: weekly-research
title: "ClickFix was the week's universal crimeware delivery vector, and macOS gained a coercion playbook — five families this week converged on paste-into-terminal delivery, local password validation before theft, and decentralized dead-drop C2"
headline: "Crimeware convergence — ClickFix delivered CrashStealer, ClickLock, ACR Stealer, TELEPUZ and Starland RAT; macOS stealers now coerce the login password"
summary: >
  Five independently-reported crimeware families in 2026-W29 converged on the same delivery and tradecraft patterns, making the shape more useful to defenders than any one sample. ClickFix (paste-a-command-into-terminal social engineering) was the shared initial-access vector for the macOS stealers CrashStealer and ClickLock, the Windows infostealer ACR Stealer (two distinct chains), the modular Windows RAT TELEPUZ, and UAT-11795's Starland RAT. Two macOS families independently reached the same escalation — coercing the user's own login password: CrashStealer validates it locally with dscl before unlocking the keychain, and ClickLock kills every visible application every ~210 ms for up to ~83 hours until the victim types it, with more than half of ~100 identified victims in Europe. On Windows, TELEPUZ and Starland share indirect-syscall execution, AMSI/ETW tampering and — notably — a Polygon smart-contract dead-drop as a C2-resolution fallback. The transferable signal is that ClickFix removes the exploit from the intrusion, macOS is now a first-class credential-theft target for European organisations, and blockchain dead-drops are becoming a resilient C2 fallback that ordinary domain/IP blocking does not reach.
discovered_at: "2026-07-19T23:20:00Z"
event_date: 2026-07-19
run_id: 2026-07-19T2310Z-weekly
priority: high
immediate_action: null
tags:
  - infostealer
  - phishing
  - organized-crime
regions:
  - switzerland
  - europe
  - global
sectors:
  - public-sector
  - technology
entities:
  - tool:crashstealer
  - tool:clicklock-stealer
  - tool:acr-stealer
  - tool:amatera
  - tool:telepuz-maas-malware
  - actor:uat-11795
  - tool:starland-rat
cves: []
techniques:
  - T1204
  - T1059.001
  - T1555.001
  - T1555.003
  - T1685
  - T1102
affected_products:
  - "Apple macOS"
  - "Microsoft Windows"
sources:
  - url: "https://www.group-ib.com/blog/clicklock-stealer-macos-malware/"
    publisher: "Group-IB Threat Intelligence"
    date: "2026-07-16"
    role: primary
  - url: "https://www.jamf.com/blog/crashstealer-macos-infostealer-analysis/"
    publisher: "Jamf Threat Labs"
    date: "2026-07-13"
    role: primary
  - url: "https://www.elastic.co/security-labs/telepuz-maas-malware-clickfix"
    publisher: "Elastic Security Labs"
    date: "2026-07-16"
    role: primary
  - url: "https://www.microsoft.com/en-us/security/blog/2026/07/16/acr-stealer-two-observed-intrusion-chains-amid-increased-threat-activity/"
    publisher: "Microsoft Threat Intelligence (Defender Experts)"
    date: "2026-07-16"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: "Each family is sourced to its own first-party research lab (Group-IB, Jamf, Elastic, Microsoft, Talos); the convergence claims (ClickFix as shared vector, macOS coercion, Polygon dead-drops) are cross-family observations drawn only from what those primaries state."
confidence: high
update_of: null
references:
  - 2026-07-19/clicklock-stealer-macos-clickfix-forced-password-coercion
  - 2026-07-14/crashstealer-macos-native-cpp-infostealer
  - 2026-07-17/microsoft-acr-stealer-two-clickfix-intrusion-chains
  - 2026-07-16/telepuz-modular-windows-rat-maas-clickfix-vidar
  - 2026-07-17/talos-uat-11795-starland-rat-wldr-c2
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions: []
migrated_from: null
---

The week's crimeware is best read as one pattern with five instances, because the reuse is where the detection leverage is.

**ClickFix removed the exploit from the intrusion.** All five families started from paste-a-command-into-a-terminal social engineering rather than a vulnerability: ClickLock and CrashStealer on macOS, ACR Stealer's two chains, TELEPUZ (via a ClickFix→Vidar hand-off), and UAT-11795's Starland RAT (a ClickFix lure running `mshta.exe`). When the initial access is the user pasting a command, the earliest reliable telemetry is process lineage — a shell, `mshta`, `rundll32` or `osascript` spawned shortly after a browser/clipboard interaction, with no dropped-file exploit stage to catch upstream.

**macOS gained a credential-coercion playbook, and Europe is the target.** Two independent macOS families reached the same escalation this week. Jamf's CrashStealer prompts for the login password and "validates it locally with `dscl -authonly`" before unlocking the keychain and profiling installed EDR ([Jamf, 2026-07-13](https://www.jamf.com/blog/crashstealer-macos-infostealer-analysis/)). Group-IB's ClickLock is more aggressive: it kills every visible application roughly every 210 ms — for up to ~83 hours — leaving only a fake password dialog on screen until the victim surrenders the macOS password (validated locally, so only the correct one is exfiltrated), and a parallel module coerces a real Keychain-authorization dialog to steal Chrome's Safe Storage key; more than 50% of the ~100 identified victims across 33 countries are in Europe ([Group-IB, 2026-07-16](https://www.group-ib.com/blog/clicklock-stealer-macos-malware/)). For a constituency issuing macOS endpoints, this is the week macOS credential theft stopped being a footnote.

**Windows RATs shared evasion and a blockchain fallback.** Elastic's TELEPUZ executes indirect syscalls from the `.text` section of a randomly chosen legitimate DLL to bypass user-mode hooking, patches AMSI/ETW, and resolves its C2 through four decentralized fallbacks — a Telegram bio, a Steam profile, a DNS TXT record and a Polygon smart contract ([Elastic, 2026-07-16](https://www.elastic.co/security-labs/telepuz-maas-malware-clickfix)); Talos's Starland RAT independently uses a Polygon smart-contract dead-drop as its fallback C2 and patches AMSI/ETW before injecting shellcode. Microsoft's ACR Stealer chains both end in DPAPI theft of Chromium credential stores ([Microsoft, 2026-07-16](https://www.microsoft.com/en-us/security/blog/2026/07/16/acr-stealer-two-observed-intrusion-chains-amid-increased-threat-activity/)).

**Defender takeaway:** the leverage points this week are behavioural and shared across families — hunt for interpreter/`mshta`/`rundll32` execution in the seconds after a browser or clipboard event (the ClickFix signature), treat macOS the same as Windows for credential-theft monitoring (a non-browser process reading the keychain or a burst of app terminations preceding a password prompt is the ClickLock/CrashStealer signal), and recognise that a Polygon/Telegram/Steam C2 fallback means a resilient dead-drop that egress domain/IP blocking will not fully cover — DNS-TXT and outbound smart-contract-RPC lookups from endpoints are the observable. **Triage:** developers and admins legitimately paste terminal commands and read the keychain during setup — the discriminators are a terminal command sourced from a web page immediately before an unexpected password or Keychain-authorization prompt, and repeated forced application termination, which no benign workflow produces.
