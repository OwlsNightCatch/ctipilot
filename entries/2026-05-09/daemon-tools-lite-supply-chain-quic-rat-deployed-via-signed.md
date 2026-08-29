---
schema: 1
kind: threat
title: "DAEMON Tools Lite supply chain — QUIC RAT deployed via signed installer; EU governments among targeted victims"
headline: "DAEMON Tools Lite supply chain — QUIC RAT deployed via signed installer; EU governments among targeted victims"
summary: "DAEMON Tools supply chain compromise — QUIC RAT delivered via signed, legitimate-looking Lite installer since 8 April 2026; Germany, France, Spain, and Italy among top victim countries; ~10% of infections on enterprise systems with government/scientific sector specifically targeted (Kaspersky Securelist, 2026-05-05 updated 2026-05-08)."
discovered_at: "2026-05-09T05:00:00Z"
event_date: 2026-05-06
run_id: 2026-05-09-migrated
priority: high
immediate_action: null
tags:
  - supply-chain
  - espionage
  - china-nexus
regions:
  - europe
  - global
sectors:
  - public-sector
  - technology
entities:
  - "incident:daemon-tools-supply-chain-2026"
cves: []
sources:
  - url: "https://www.kaspersky.com/blog/daemon-tools-supply-chain-attack/55691/"
    publisher: "Kaspersky blog — DAEMON Tools supply chain attack, 2026-05-05/08"
    role: primary
  - url: "https://www.helpnetsecurity.com/2026/05/06/daemon-tools-compromised-backdoors-supply-chain-attack/"
    publisher: "Help Net Security, 2026-05-06"
    role: corroborating
  - url: "https://therecord.media/hackers-compromise-daemon-tools-global-supply-chain-attack"
    publisher: "The Record, 2026-05-07"
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
migrated_from: briefs/2026-05-09.md
---

Since 8 April 2026, trojanised versions of DAEMON Tools Lite (12.5.0.2421 through 12.5.0.2434) have been distributed from the legitimate vendor website, signed with valid AVB Disc Soft digital certificates. Kaspersky researchers documented a three-stage architecture: an initial profiling component (`envchk.exe`) fingerprinting the system; a minimalistic backdoor enabling remote command execution on selected targets; and **QUIC RAT**, an advanced implant that injects into `notepad.exe` and `conhost.exe`, supports C2 over QUIC (evading proxy inspection), and implements shell execution, file management, process injection, keylogging, SOCKS proxy, and TCP tunnelling ([Kaspersky Securelist, 2026-05-05 updated 2026-05-08](https://www.kaspersky.com/blog/daemon-tools-supply-chain-attack/55691/) · [Help Net Security, 2026-05-06](https://www.helpnetsecurity.com/2026/05/06/daemon-tools-compromised-backdoors-supply-chain-attack/)). Several thousand installation attempts were observed across ~100 countries; Germany, France, Spain, and Italy are among the top victim countries. Targeted QUIC RAT deployment was limited to approximately a dozen machines in government, scientific, manufacturing, and retail sectors — indicating selective activation consistent with intelligence-collection objectives. Artefacts including Chinese-language strings suggest a Chinese-speaking actor; no formal attribution has been made. The clean release is version 12.6.0.2445 (released 2026-05-06).

MITRE ATT&CK coverage: [T1195.002 Supply Chain Compromise](https://attack.mitre.org/techniques/T1195/002/); [T1036.004 Masquerade Task or Service](https://attack.mitre.org/techniques/T1036/004/) (kworker/ksoftirqd masquerade); [T1573.002 Asymmetric Cryptography / QUIC](https://attack.mitre.org/techniques/T1573/002/); [T1055 Process Injection](https://attack.mitre.org/techniques/T1055/).

**Defender takeaway:** Audit endpoints for DAEMON Tools Lite versions 12.5.0.2421–12.5.0.2434; check for `envchk.exe`, unsigned processes injected into `notepad.exe` or `conhost.exe`, and outbound QUIC (UDP 443) to non-sanctioned destinations. Sysmon EID 1 with parent-process image path filters for `notepad.exe` or `conhost.exe` spawning child processes will surface post-injection activity. Update to 12.6.0.2445.
