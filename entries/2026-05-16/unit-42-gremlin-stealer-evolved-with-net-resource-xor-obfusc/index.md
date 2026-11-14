---
schema: 1
kind: research
title: "Unit 42: Gremlin stealer hides its payload in XOR-encoded .NET resources and adds a crypto clipper, Discord token theft and WebSocket session hijacking"
headline: "Unit 42: evolved Gremlin stealer hides its payload in .NET resources and hijacks live Chromium browser sessions"
summary: "Unit 42 reported on 2026-05-15 a Gremlin stealer variant that moves its payload into an XOR-encoded .NET resource section, decrypts functions only when needed and, in one sample, sits under a commercial packer with instruction virtualization. New modules steal Discord tokens, swap copied cryptocurrency wallet addresses for the attacker's in real time and hijack live Chromium-based browser sessions over WebSocket; stolen data leaves as a ZIP uploaded to an attacker-controlled web panel, with the Telegram Bot API as an alternative channel."
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
techniques: [T1027.013, T1027.002, T1140, T1115, T1565.002, T1185, T1539, T1555.003, T1528, T1005, T1560, T1041, T1567]
affected_products: []
cves: []
sources:
  - url: "https://unit42.paloaltonetworks.com/gremlin-stealer-evolution/"
    publisher: "Palo Alto Networks Unit 42"
    date: "2026-05-15"
    role: primary
closed_sources: []
evidence:
  - quote: "In this version, the malware authors have shifted the malicious payload into the .NET Resource section, masking it with XOR encoding to bypass signature-based detection and heuristic scanning."
    publisher: Unit 42
    source_url: "https://unit42.paloaltonetworks.com/gremlin-stealer-evolution/"
  - quote: "When it detects a match, the malware replaces the victim's address with the attacker’s wallet in real time, diverting funds during transactions."
    publisher: Unit 42
    source_url: "https://unit42.paloaltonetworks.com/gremlin-stealer-evolution/"
  - quote: "This allows Gremlin stealer to hijack active, live browser sessions and bypass modern cookie protections by requesting the data directly from the running browser process."
    publisher: Unit 42
    source_url: "https://unit42.paloaltonetworks.com/gremlin-stealer-evolution/"
  - quote: "The malware names the file using the victim’s public IP address to identify the source, and then uploads it to the attacker-controlled site, as shown in Figure 3."
    publisher: Unit 42
    source_url: "https://unit42.paloaltonetworks.com/gremlin-stealer-evolution/"
verification: single-source
sourcing_note: >
  A single Unit 42 research post on samples from Palo Alto Networks' own threat intelligence; no other party reports this variant, and the post does not
  say how Gremlin reaches or first runs on a victim.
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
migrated_from: briefs/2026-05-16.md
updates:
  - at: "2026-10-21T20:19:32Z"
    run_id: 2026-10-21T1148Z-audit
    type: correction
    summary: >
      The analyzed Gremlin variant uploads a ZIP of stolen data, named with the victim's public IP
      address, to an attacker-controlled web panel, with the Telegram Bot API as an alternative path,
      rather than using HTTPS POST with Telegram as a secondary channel. Its clipper swaps any copied
      cryptocurrency wallet address matching its patterns, not only Bitcoin and Ethereum addresses, and
      Unit 42 does not list saved passwords among the stolen data. The session-hijack module requests
      session data from the running Chromium browser process over WebSocket, and one sample is protected
      by a commercial packer with instruction virtualization.
    fields: [affected_products, body, classification, evidence, headline, sources, sourcing_note, summary, techniques, title]
---

Unit 42 identified a new Gremlin stealer variant that bundles stolen browser cookies, session tokens, clipboard contents, cryptocurrency wallet data and FTP and VPN credentials into a ZIP archive named with the victim's public IP address and uploads it to an attacker-controlled site, while exfiltration through private web panels or the Telegram Bot API stays as in earlier builds ([Unit 42, 2026-05-15](https://unit42.paloaltonetworks.com/gremlin-stealer-evolution/)). The variant moves its payload into the .NET resource section masked with single-byte XOR encoding, decrypts and maps each critical function into memory only when needed, and hides its strings behind a runtime decoder that reads them from an embedded encrypted resource; one sample is wrapped in a commercial packer that turns the code into custom bytecode run by a private virtual machine ([Unit 42, 2026-05-15](https://unit42.paloaltonetworks.com/gremlin-stealer-evolution/)). New modules extract Discord tokens by scanning multiple paths with regex validation, watch the clipboard for wallet-address patterns and replace the victim's address with the attacker's in real time, and hijack live sessions in Chromium-based browsers over WebSocket by requesting the data directly from the running browser process, which bypasses modern cookie protections ([Unit 42, 2026-05-15](https://unit42.paloaltonetworks.com/gremlin-stealer-evolution/)). The post does not describe how Gremlin is delivered.

**Exposure:** endpoints with Chromium-based browsers; Gremlin targets web browsers, the clipboard and local storage for payment card details, cookies, session tokens, cryptocurrency wallet data and FTP and VPN credentials ([Unit 42, 2026-05-15](https://unit42.paloaltonetworks.com/gremlin-stealer-evolution/)).

**Detection:** in egress telemetry, a ZIP archive named after the host's public IP address uploaded to an unfamiliar web panel, and Telegram Bot API traffic from a process that is not a messaging client; in endpoint telemetry, a process requesting session data from a running Chromium browser process, and a process that rewrites clipboard contents matching wallet-address patterns ([Unit 42, 2026-05-15](https://unit42.paloaltonetworks.com/gremlin-stealer-evolution/)). Signatures on strings and exports miss current builds, because the strings and functions only appear decrypted at runtime ([Unit 42, 2026-05-15](https://unit42.paloaltonetworks.com/gremlin-stealer-evolution/)).

**Defender takeaway:** replace detections tuned to legacy Gremlin samples, whose function exports and internal symbols were left intact, with behavioral ones ([Unit 42, 2026-05-15](https://unit42.paloaltonetworks.com/gremlin-stealer-evolution/)). On an infected host, revoke its browser sessions and rotate the Discord, FTP and VPN credentials it held, since hijacked sessions and stolen credentials stay usable after the malware is removed.

## Correction — 2026-10-21T20:19:32Z

The analyzed variant bundles its haul into a ZIP archive named with the victim's public IP address and uploads it to an attacker-controlled site, with private web panels or the Telegram Bot API as the exfiltration methods carried over from earlier builds; Unit 42 does not describe an HTTPS POST with Telegram as a secondary channel ([Unit 42, 2026-05-15](https://unit42.paloaltonetworks.com/gremlin-stealer-evolution/)). The clipper replaces any copied address matching its cryptocurrency wallet patterns, not only Bitcoin and Ethereum addresses, and saved passwords are not among the data Unit 42 lists ([Unit 42, 2026-05-15](https://unit42.paloaltonetworks.com/gremlin-stealer-evolution/)). The session-hijack module works by requesting the data directly from the running Chromium-based browser process over WebSocket, and one sample is protected by a commercial packer that runs the code as custom bytecode on a private virtual machine ([Unit 42, 2026-05-15](https://unit42.paloaltonetworks.com/gremlin-stealer-evolution/)).
