---
schema: 1
kind: research
horizon: operational
title: "Unit 42: Gremlin Stealer evolved with .NET-resource XOR obfuscation, real-time crypto-clipper, and WebSocket browser-process session-hijack module"
headline: "Unit 42: Gremlin Stealer evolved with .NET-resource XOR obfuscation, real-time crypto-clipper, and WebSocket browser-process session-hijack module"
summary: "Palo Alto Networks Unit 42 published on 2026-05-15 an analysis of evolved variants of the Gremlin information stealer, adding three new capability tiers operationally relevant to defenders running endpoint detections tuned for older Gremlin samples (Palo Alto Networks Unit 42, 2026-05-15)."
discovered_at: "2026-05-16T05:00:07Z"
event_date: 2026-05-15
run_id: 2026-05-16-5bc123a0
priority: notable
immediate_action: null
tags:
  - infostealer
  - identity
  - cryptocrime
regions:
  - global
sectors:
  - finance
  - technology
entities:
  - "tool:gremlin-stealer-evolution-2026"
cves: []
sources:
  - url: "https://unit42.paloaltonetworks.com/gremlin-stealer-evolution/"
    publisher: "Palo Alto Networks Unit 42, 2026-05-15"
    role: primary
closed_sources: []
evidence: []
verification: single-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-16.md
---

Palo Alto Networks Unit 42 published on 2026-05-15 an analysis of evolved variants of the Gremlin information stealer, adding three new capability tiers operationally relevant to defenders running endpoint detections tuned for older Gremlin samples ([Palo Alto Networks Unit 42, 2026-05-15](https://unit42.paloaltonetworks.com/gremlin-stealer-evolution/)). Obfuscation has shifted to embedding encrypted payloads in .NET resource sections (XOR-keyed) combined with single- or double-character identifier renaming and a runtime string-decoder function (`_003CModule_003E.c()`) — defeating static signature analysis of string literals that previous-generation Gremlin samples used. A new crypto-clipper component continuously monitors the system clipboard and replaces Bitcoin and Ethereum wallet addresses with attacker-controlled equivalents in real time, [T1115](https://attack.mitre.org/techniques/T1115/). The most operationally interesting addition is a WebSocket-based session-hijack module that reads active browser process memory (Chrome-based browsers) to extract session tokens directly from running processes, bypassing the cookie-encryption mitigations modern browsers apply at disk — [T1185](https://attack.mitre.org/techniques/T1185/) Browser Session Hijacking. Credential scope includes browser cookies, session tokens, saved passwords, payment-card details, FTP and VPN credentials, Discord tokens (dedicated regex scanner), clipboard content, and cryptocurrency wallet files. Exfiltration is HTTPS POST to a private web panel; a Telegram Bot API channel is the secondary channel. Detection: Sysmon EID 10 (process access) targeting `chrome.exe` or `msedge.exe` (and other Chrome-based browser processes) from unexpected parent processes; clipboard-monitoring hook registration from non-standard processes (generic Windows clipboard-listener API surface). Hardening: browser isolation for high-value sessions; clipboard-API access audited in EDR telemetry. Single-source — Unit 42 only; flagged for verification.
