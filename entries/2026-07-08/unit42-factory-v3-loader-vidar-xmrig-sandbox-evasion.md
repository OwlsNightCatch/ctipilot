---
schema: 1
kind: threat
horizon: operational
title: "Unit 42: Factory-v3 loader-builder abuses fraudulent code-signing and 491 MB file inflation to smuggle Vidar and XMRig past sandboxes"
headline: "Unit 42: Factory-v3 loaders use fake Authenticode signing and 491 MB file inflation to evade sandboxes"
summary: >
  Palo Alto Unit 42 documented a malvertising campaign distributing Vidar stealer and XMRig via loaders built with Factory-v3, a Go loader-builder. The loaders defeat detection with per-build UUIDs, fraudulent Authenticode certificates impersonating real firms, in-memory AMSI patching, MpClient.dll DLL-sideloading against Defender, and "file inflation" padding binaries to 491 MB to exceed sandbox upload limits.
discovered_at: "2026-07-08T20:35:00Z"
event_date: 2026-07-07
run_id: 2026-07-08T2009Z-intel
priority: notable
immediate_action: null
tags:
  - infostealer
  - cryptocrime
  - phishing
regions:
  - us
  - europe
sectors:
  - technology
entities:
  - "tool:factory-v3-loader-builder"
cves: []
sources:
  - url: "https://unit42.paloaltonetworks.com/vidar-stealer-xmrig-miner-campaign-analysis/"
    publisher: "Palo Alto Networks Unit 42"
    date: "2026-07-07"
    role: primary
closed_sources: []
evidence:
  - quote: "Loaders in Clusters A and C append hundreds of megabytes of null bytes after the last PE section, pushing the total file size to as high as 491 MB"
    publisher: "Palo Alto Networks Unit 42"
  - quote: "The builder generates a unique binary per build. For example, we observed 27 unique build UUIDs across 43 samples, defeating hash-based detection"
    publisher: "Palo Alto Networks Unit 42"
verification: single-source
sourcing_note: "Single reputable research-lab primary (Palo Alto Unit 42); no independent corroborating source found this run. Attributed to Unit 42 as the originating research."
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
actions:
  - "Tune sandbox/EDR heuristics for PE file-inflation (section-table size vs. file-size mismatch; anomalously large files) so 491 MB null-padded loaders are not silently skipped past detonation size limits."
  - "Flag Authenticode signer/product mismatches (e.g. binaries signed as JustWatch GmbH or BleacherReport that are not those products) and MpClient.dll load-path anomalies / NisSrv.exe running from %AppData%."
migrated_from: null
---

Unit 42 documented a financially motivated malvertising campaign, active since April 2026, distributing Vidar stealer and the XMRig cryptominer via loaders built with "Factory-v3", a malware-as-a-service Go loader-builder ([Unit 42, 2026-07-07](https://unit42.paloaltonetworks.com/vidar-stealer-xmrig-miner-campaign-analysis/)). Victims are lured to password-protected archives masquerading as cracked software; the Go loaders (43 samples, 27 unique build UUIDs — defeating hash-based detection) are signed with fraudulent Authenticode certificates impersonating real companies (JustWatch GmbH, later BleacherReport) (`T1553.002`), strip PE metadata, and DLL-sideload via a fake `MpClient.dll` export that hijacks Windows Defender's DLL search order to execute as `NisSrv.exe` from AppData (`T1574.002`). Before dropping the payload the loader patches AMSI in memory — resolving `AmsiScanBuffer` and overwriting its first six bytes to force an `E_INVALIDARG` return (`T1562.001`). The standout evasion is "file inflation": appending hundreds of megabytes of null bytes to push loader size to as high as 491 MB, exceeding the 50–100 MB detonation limits of many automated sandboxes. Persistence uses Run keys, scheduled tasks and startup-folder scripts, and each victim is fingerprinted via an 8-character HWID; the operator monitors yield through a Telegram channel branded "X3D MINER". **Defender takeaway:** with US/EU victim concentration and a builder that regenerates a unique binary per build, signature/hash detection is a dead end here — the durable hooks are the *evasion mechanics themselves*: file-inflation size/section heuristics, Authenticode signer-vs-product mismatch policy, Defender-binary DLL-sideload anomalies, and in-memory AMSI-patch telemetry.
