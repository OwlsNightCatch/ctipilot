---
schema: 1
kind: threat
horizon: operational
title: "Operation Endgame expands to SocGholish/TA569 — 106 C2 servers down, FakeUpdates loader stripped from 14,971 WordPress sites"
headline: "Operation Endgame expands to SocGholish/TA569 — 106 C2 servers down, FakeUpdates loader stripped from 14,971 WordPress sites"
summary: "Law enforcement extended Operation Endgame to SocGholish/TA569, taking down 106 C2 servers and stripping the FakeUpdates loader from 14,971 compromised WordPress sites in a Dutch-led, Europol-coordinated action (Politie, 2026-06-18)."
discovered_at: "2026-06-19T05:20:50Z"
event_date: 2026-06-18
run_id: 2026-06-19-c306b105
priority: high
immediate_action: null
tags:
  - law-enforcement
  - organized-crime
  - supply-chain
  - phishing
regions:
  - europe
  - global
sectors:
  - public-sector
  - technology
entities:
  - "incident:operation-endgame-socgholish-ta569"
  - "campaign:operation-endgame-amadey-stealc"
cves: []
sources:
  - url: "https://www.politie.nl/en/news/2026/juni/18/11-international-law-enforcement-initiate-hunt-on-malware-group-socgholish.html"
    publisher: Politie
    role: primary
  - url: "https://www.proofpoint.com/us/blog/threat-insight/sayonara-socgholish-operation-endgame-disrupts-major-cybercrime-operation"
    publisher: Proofpoint
    role: corroborating
  - url: "https://www.helpnetsecurity.com/2026/06/18/law-enforcement-socgholish-operation-endgame/"
    publisher: Help Net Security
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
migrated_from: briefs/2026-06-19.md
---

A coordinated law-enforcement action on 2026-06-18 — an expansion of the May 2024 Operation Endgame — dismantled infrastructure tied to TA569, the long-running operator of the SocGholish (FakeUpdates) initial-access framework ([Politie, 2026-06-18](https://www.politie.nl/en/news/2026/juni/18/11-international-law-enforcement-initiate-hunt-on-malware-group-socgholish.html); [Help Net Security, 2026-06-18](https://www.helpnetsecurity.com/2026/06/18/law-enforcement-socgholish-operation-endgame/)). The Dutch National High Tech Crime Unit led the operation with the RCMP, FBI, BKA and Europol; 106 command-and-control servers were taken down and the malicious JavaScript loader was removed from 14,971 compromised WordPress sites. SocGholish injects obfuscated JavaScript into legitimate WordPress sites (typically via stolen `wp-admin` credentials or vulnerable plugins), fingerprints visitors and renders a fake browser-update lure; accepting it drives a ZIP download of a `.js`/`.lnk` stage-1 that executes through `wscript.exe` or `mshta.exe` (`T1189` Drive-by Compromise → `T1059.007` JavaScript → `T1204.002` User Execution), historically passing access to Evil Corp downstream affiliates ([Proofpoint, 2026-06-18](https://www.proofpoint.com/us/blog/threat-insight/sayonara-socgholish-operation-endgame-disrupts-major-cybercrime-operation)). This is the first Endgame phase to directly target the FakeUpdates component, an initial-access mechanism in continuous use since roughly 2017.
**Defender takeaway:** the takedown does not retire the technique — hunt for `wscript.exe`/`mshta.exe` spawned from a browser process (Sysmon EID 1, high-fidelity), correlate web-proxy logs for browser-initiated downloads of `.zip` payloads from WordPress hosts, and audit `wp-admin` credentials plus theme-file integrity on any WordPress estate you operate.
