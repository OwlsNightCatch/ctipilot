---
schema: 1
kind: threat
title: "Check Point: Iran MOIS-linked \"Cavern Manticore\" ships a modular .NET C2 that uses three compilation formats as an anti-analysis layer, delivered via SysAid RMM abuse"
headline: "Cavern Manticore's C2 splits across IL, Mixed-Mode and NativeAOT binaries to break RE toolchains — pushed through SysAid's legitimate deployment feature"
summary: >
  Check Point Research documented Cavern Manticore, an Iran MOIS-linked APT (overlaps with
  MuddyWater and OilRig's Lyceum) targeting Israeli government and IT-sector orgs. Its modular
  .NET C2 "Cavern" is deliberately compiled across three binary formats (IL-only, Mixed-Mode
  C++/CLI, .NET 8 NativeAOT), each needing a different reverse-engineering toolchain; NativeAOT
  hides sensitive P/Invoke calls from import-based triage. Delivery abused SysAid's legitimate
  software-deployment feature (no SysAid vuln) to sideload a trojanized uxtheme.dll. Transferable
  hunt: uxtheme.dll outside System32 and RMM push actions staging binaries to non-standard paths.
discovered_at: "2026-07-09T04:32:59Z"
event_date: "2026-07-06"
run_id: 2026-07-09T0409Z-intel
priority: notable
immediate_action: null
tags: [espionage, nation-state, iran-nexus]
regions: [global, middle-east]
sectors: [public-sector, telco, technology]
entities: ["actor:cavern-manticore", "tool:cavern-c2-framework"]
cves: []
sources:
  - url: "https://research.checkpoint.com/2026/cavern-manticore-exposing-iran-linked-modular-c2-framework/"
    publisher: "Check Point Research"
    date: "2026-07-06"
    role: primary
closed_sources: []
evidence:
  - quote: "Cavern Manticore is an Iran MOIS (Ministry of Intelligence and Security)-linked actor, with links to the OilRig subgroup named Lyceum"
    publisher: "Check Point Research"
  - quote: "the compilation format itself becomes the anti-analysis layer, since each of the three formats has to be reversed with a different toolchain"
    publisher: "Check Point Research"
  - quote: "SysAid was not compromised, and no SysAid vulnerability was involved. The attacker had already gained access to the victim environment and abused a legitimate software-deployment feature"
    publisher: "Check Point Research"
verification: single-source
sourcing_note: "Single-source: Check Point Research (Admiralty B) original analysis; primary targeting is Israeli government/IT. Included on the transferable technique class (compilation-format anti-analysis, RMM-deployment-feature abuse) and same-actor-class relevance (Iran MOIS also targets EU public sector)."
confidence: medium
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 3
watchlist_hit: false
actions:
  - "Hunt for uxtheme.dll loaded outside its legitimate System32 location, especially by non-standard parents (e.g. WinDirStat.exe), and for RMM/software-deployment tools (SysAid and equivalents) pushing executables to non-standard ProgramData paths."
  - "For reverse engineers, resource NativeAOT-capable tooling (e.g. ghidra-nativeaot / ida-nativeaot metadata recovery) — standard .NET decompilers do not handle Native-only compiled output, so import-table triage misses the capability."
migrated_from: null
---

Check Point Research documented **Cavern Manticore**, an Iran MOIS-linked APT it assesses shares technical and infrastructure overlap with MuddyWater and OilRig's Lyceum subgroup, targeting Israeli government and IT-sector organisations ([Check Point Research, 2026-07-06](https://research.checkpoint.com/2026/cavern-manticore-exposing-iran-linked-modular-c2-framework/)). Its namesake framework, **Cavern**, is a modular post-exploitation .NET C2 whose components are deliberately compiled into three different binary formats: pure IL-only .NET (the `mhm.dll` file-ops/DPAPI-decrypt module, `db.dll` SQL browser, `ode.dll` LDAP/AD-recon module), Mixed-Mode C++/CLI IL+native (the `uxtheme.dll` Cavern Agent core), and .NET 8 NativeAOT native-only (`n-HTCommp.dll` HTTPS/WebSocket transport, `n-ten.dll` network recon/SMB brute-force, `n-sws.dll` SOCKS5/WSS tunnel). The compilation-format diversity is itself the anti-analysis layer: each format demands a different reverse-engineering toolchain, and NativeAOT strips framework symbols and resolves security-sensitive P/Invoke calls (`WNetAddConnection2`, `NetShareEnum`, `NetLocalGroupGetMembers`) through runtime descriptor tables rather than the PE import table, hiding capability from import-based triage ([Check Point Research, 2026-07-06](https://research.checkpoint.com/2026/cavern-manticore-exposing-iran-linked-modular-c2-framework/)).

Delivery is the transferable part: the actor abused SysAid's legitimate software-update/deployment feature — not a SysAid vulnerability — to push a WinDirStat DLL-sideloading package that loads the trojanized `uxtheme.dll` as the Cavern Agent, which exports 83 functions mimicking the real Windows theming library (82 empty stubs; the one live export, `EnableThemeDialogTexture`, is the C2 entry point) — a sandbox trap for automated analysis that only invokes default exports. Each loaded module is isolated in its own .NET AppDomain via a `MarshalByRefObject` proxy so modules can be unloaded cleanly after use, leaving minimal forensic residue; most samples score zero or near-zero on VirusTotal. ATT&CK: `T1574.002 DLL Side-Loading`, `T1027 Obfuscated Files or Information` (via compilation-format diversity), `T1620 Reflective Code Loading` (AppDomain-isolated modules), `T1219 Remote Access Software` (SysAid deployment abuse).

**Defender takeaway:** the primary targeting is Israeli government, but Iran MOIS clusters (MuddyWater/OilRig lineage) also target European public-sector and critical-infrastructure networks, and the two techniques here transfer regardless of victim: hunt `uxtheme.dll` loaded outside System32 by anomalous parents, and treat RMM/deployment-tool (SysAid and equivalents) push actions that stage binaries to non-standard `ProgramData` paths as suspicious — abuse of a legitimate deployment feature leaves no CVE to patch, so the control is behavioural. Reversers triaging suspected NativeAOT payloads need dedicated metadata-recovery tooling, since import-table inspection will under-report the sample's real capability.
