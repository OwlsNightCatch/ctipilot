---
schema: 1
kind: research
horizon: strategic
weekly_section: weekly-research
title: "State-nexus tradecraft this week targeted defenders' own visibility — HelloNet blinds user-mode network EDR by intercepting raw AFD IOCTLs from a trusted-updater sideload, and GoSerpent shows weeks-long silent collection as deliberate design"
headline: "APT tradecraft targeting EDR visibility — HelloNet intercepts raw AFD IOCTLs via a ViPNet updater sideload; GoSerpent stages documents silently for weeks"
summary: >
  Two Kaspersky GReAT disclosures in 2026-W29 describe state-nexus tradecraft whose transferable lesson is about defeating the tools defenders rely on. HelloNet persists by sideloading a malicious wtsapi32.dll into the auto-launched update component of the ViPNet secure-networking suite, then injects a proxy module into svchost.exe that uses Microsoft Detours to hook NtDeviceIoControlFile and intercept the raw Ancillary Function Driver IOCTLs (AFD_RECV, AFD_GET_TDI_HANDLES) — degrading user-mode network-filtering security tools by operating below the API layer those tools monitor. GoSerpent, a Go-based backdoor used since 2021 against Southeast-Asian government and diplomatic targets, deploys a document-harvesting Windows service, then deliberately waits weeks while files accumulate before returning with a proxy and a dedicated exfiltration toolset — patience engineered to sit under alerting thresholds. Both victim sets are out-of-nexus (Russian and SEA government), but the AFD-IOCTL network-visibility-blinding technique and the trusted-updater-sideload path are directly transferable capability shifts European CI and government detection engineers should account for now.
discovered_at: "2026-07-19T23:32:00Z"
event_date: 2026-07-16
run_id: 2026-07-19T2310Z-weekly
priority: notable
immediate_action: null
tags:
  - nation-state
  - espionage
  - supply-chain
regions:
  - global
  - europe
sectors:
  - public-sector
cves: []
techniques:
  - T1574.001
  - T1055
  - T1685
  - T1543.003
  - T1573.001
affected_products:
  - "ViPNet"
sources:
  - url: "https://securelist.com/hellonet-vipnet/120700/"
    publisher: "Kaspersky Securelist (GReAT)"
    date: "2026-07-16"
    role: primary
  - url: "https://securelist.com/goserpent-backdoor-in-southeast-asia/120687/"
    publisher: "Kaspersky Securelist (GReAT)"
    date: "2026-07-16"
    role: primary
closed_sources: []
evidence: []
verification: single-source
sourcing_note: "Both items are single-source (Kaspersky GReAT) primary technical analyses of distinct campaigns — reliability B (a research lab of consistent standard), credibility 2 (single-lab, not independently corroborated; the GoSerpent–TetrisPhantom link is Kaspersky's own potential, not confirmed, association). Carried for the transferable technique, not the out-of-nexus victimology."
confidence: medium
update_of: null
references:
  - 2026-07-17/kaspersky-hellonet-vipnet-updater-sideload-afd-ioctl
  - 2026-07-18/goserpent-backdoor-evolution-sea-government-diplomatic
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: null
---

Both of the week's notable APT disclosures share a target that is not the victim's data but the defender's ability to see the intrusion — worth surfacing together because the techniques transfer regardless of who was hit.

**HelloNet blinds network EDR from below the API.** Kaspersky GReAT documented an active campaign that persists by sideloading a malicious `wtsapi32.dll` into the auto-launched update component of the ViPNet secure-networking suite, then injects a proxy module (HelloProxy) into `svchost.exe` that uses Microsoft Detours to hook `NtDeviceIoControlFile` and intercept the raw Ancillary Function Driver IOCTLs — `AFD_RECV`, `AFD_GET_TDI_HANDLES` — which, per Kaspersky, hinders user-mode network-filtering security tools ([Kaspersky, 2026-07-16](https://securelist.com/hellonet-vipnet/120700/)). The significance for detection engineering is the layer: many endpoint tools observe network activity at the Winsock/API level, and an implant intercepting AFD IOCTLs is operating beneath that vantage, so it can proxy C2 traffic that user-mode network telemetry never records. Victimology is Russian government and CI (attributed with low confidence to an unknown Chinese-speaking group), but the technique is stack-agnostic.

**GoSerpent makes dwell time a design choice.** Kaspersky's analysis of the evolved GoSerpent backdoor — Go-based, used since 2021 against Southeast-Asian government and diplomatic entities — shows a chain that deploys a document-harvesting Windows service plus credential tools, then "deliberately waits a few weeks while files accumulate" before returning with the Stowaway proxy and a dedicated exfiltration toolset, talking ChaCha20 to its C2 ([Kaspersky, 2026-07-16](https://securelist.com/goserpent-backdoor-in-southeast-asia/120687/)); Kaspersky notes a potential, unconfirmed link to the TetrisPhantom actor.

**Defender takeaway:** the transferable capability shift is HelloNet's AFD-IOCTL interception — detection engineers should not assume user-mode network telemetry is complete on a host, and should weight kernel-callback/driver-level and flow-based (network-appliance) telemetry accordingly, and treat DLL sideloading through a trusted security/VPN client's update mechanism as a live initial-foothold path (integrity-monitor the update components of trusted networking clients, not just the OS). GoSerpent's lesson is temporal: collection that stages silently for weeks defeats point-in-time and short-window alerting, so long-baseline hunts for a new persistent service writing to a staging directory, and for dormant footholds that only periodically beacon, are the counter. **Triage:** a signed networking client loading its own updater DLL is normal — the discriminator is that updater component making outbound connections it never made before, or a module in `svchost.exe` issuing raw AFD IOCTLs, and a newly-created Windows service that harvests documents but stays network-quiet for an extended period before any egress.
