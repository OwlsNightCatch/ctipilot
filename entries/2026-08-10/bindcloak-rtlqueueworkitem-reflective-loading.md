---
schema: 1
kind: threat
horizon: operational
title: "UPDATE — BINDCLOAK unpacked: a modular C++ backdoor that routes every DLL load through RtlQueueWorkItem to keep LoadLibraryW off unbacked memory, assessed high-confidence an OctLurk variant"
headline: "Zscaler's second instalment details the toolkit's final stage and extends the campaign to Middle East energy targets"
summary: >
  Part 2 of Zscaler ThreatLabz's series on the actor behind TELESHIM and MIXEDKEY is a full teardown
  of BINDCLOAK, a 64-bit modular C++ backdoor whose plugin DLLs are reflectively loaded, with each
  import resolved by queueing LoadLibraryW through RtlQueueWorkItem specifically because a
  LoadLibraryW call originating from unbacked executable memory is what endpoint tooling treats as
  suspicious. It derives a per-victim host identifier from the computer name and volume serial
  number, encodes command-and-control traffic under two XOR layers over TLS, and exposes eleven
  commands centred on collecting and impersonating user and process tokens. ThreatLabz assesses with
  high confidence that BINDCLOAK is a variant of OctLurk, and reports the July 2026 campaign
  expanding into the Middle East energy sector.
discovered_at: "2026-08-10T04:46:00Z"
event_date: "2026-08-03"
run_id: 2026-08-10T0411Z-intel
priority: notable
immediate_action: null
tags: [espionage, nation-state, infostealer]
regions: [middle-east, global]
sectors: [public-sector, energy]
entities: [malware:bindcloak, malware:teleshim, tool:mixedkey, malware:octlurk]
techniques: [T1134.001, T1134.003, T1620, T1057, T1132.002, T1095]
affected_products: []
cves: []
sources:
  - url: "https://www.zscaler.com/blogs/security-research/targeted-attack-government-entities-middle-east-part-2"
    publisher: "Zscaler ThreatLabz"
    date: "2026-08-03"
    role: primary
  - url: "https://securelist.com/octlurk-silklurk-backdoors-central-asia/120840/"
    publisher: "Kaspersky GReAT"
    date: "2026-07-30"
    role: corroborating
closed_sources: []
evidence:
  - quote: "BINDCLOAK is a 64-bit modular backdoor written in C++ that uses a complex message routing mechanism to manage the C2 communication channel."
    publisher: "Zscaler ThreatLabz"
  - quote: "When resolving imports, each DLL is loaded via RtlQueueWorkItem with LoadLibraryW and the DLL name as arguments to evade EDRs since LoadLibraryW calls from unbacked executable memory regions are considered highly suspicious by EDRs."
    publisher: "Zscaler ThreatLabz"
  - quote: "ThreatLabz assesses with high-confidence that BINDCLOAK is a variant of OctLurk."
    publisher: "Zscaler ThreatLabz"
  - quote: "the new campaign we identified in July 2026 highlights a notable expansion of operations to target the Middle East with a key focus on the energy vertical."
    publisher: "Zscaler ThreatLabz"
verification: multi-source
sourcing_note: >
  Zscaler is the sole assessor of BINDCLOAK itself; Kaspersky's independent OctLurk analysis
  corroborates the family BINDCLOAK is assessed to belong to, not the BINDCLOAK teardown. The
  OctLurk relationship is carried at the confidence Zscaler states — high confidence, an assessment,
  not an established identity.
confidence: high
update_of: 2026-07-26/teleshim-bindcloak-volume-serial-keying-government-espionage
references: []
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

**UPDATE (originally covered 2026-07-26):** the earlier entry covered Part 1 of this series — the TELESHIM backdoor and the MIXEDKEY loader, and the environmental keying that ties a payload to the host it infected. Zscaler ThreatLabz has now published Part 2, a teardown of the toolkit's final stage ([Zscaler ThreatLabz, 2026-08-03](https://www.zscaler.com/blogs/security-research/targeted-attack-government-entities-middle-east-part-2)). Two things in it are new rather than restatement: the loading tradecraft, and a targeting expansion.

BINDCLOAK is described as "a 64-bit modular backdoor written in C++ that uses a complex message routing mechanism to manage the C2 communication channel," running two built-in modules alongside plugin DLLs delivered from the command server. The detail worth carrying into detection engineering is *how* those DLLs get loaded. Plugin modules are reflectively loaded, and when resolving their imports the backdoor queues `LoadLibraryW` through `RtlQueueWorkItem` rather than calling it directly — Zscaler is explicit about the reason, which is that a `LoadLibraryW` call originating from an unbacked executable memory region is exactly what endpoint tooling flags. This is evasion aimed at a specific, widely deployed heuristic: the call still happens, but the thread that makes it belongs to the thread pool rather than to the injected region, so the stack the detection inspects no longer points where it expects.

The rest of the design continues Part 1's environmental-keying theme without repeating it. A four-byte per-victim identifier is derived by summing the ASCII values of the computer name and adding the volume serial number, and travels in every command-and-control message. Traffic is encoded under two layers of XOR and carried over TLS on TCP. Eleven commands are grouped around tokens — collecting user tokens through an authentication call, enumerating processes to decide which tokens are worth taking, and starting modules under either a stolen user token or a duplicated process token — with the remainder covering module lifecycle and one command whose purpose ThreatLabz says it has not determined.

The attribution language matters and is carried exactly as published: ThreatLabz "assesses with high-confidence that BINDCLOAK is a variant of OctLurk." That is an assessment of family relationship, not an identity claim, and OctLurk itself is a family Kaspersky separately documented against Central Asian and Syrian government targets ([Kaspersky GReAT, 2026-07-30](https://securelist.com/octlurk-silklurk-backdoors-central-asia/120840/)). The targeting delta is that the July 2026 campaign shows "a notable expansion of operations to target the Middle East with a key focus on the energy vertical."

Detection, telemetry class first. The reflective-loading behaviour surfaces in image-load and thread telemetry rather than on disk: a module load whose initiating thread belongs to the process thread pool while the corresponding executable memory region has no backing file is the shape, and it is precisely the correlation that a stack-based `LoadLibraryW` heuristic alone will miss. Token activity is the second class — process enumeration immediately followed by token duplication with primary-token assignment rights, then a new module executing under a different user context within the same process. Network telemetry shows TLS over TCP with a fixed short identifier repeated across sessions from the same host. **Triage:** thread-pool work items and `LoadLibraryW` are both entirely ordinary in benign software, and legitimate services duplicate tokens routinely; the discriminator is the combination of an unbacked executable region in the same process, a module load initiated from a pool thread, and token duplication following process enumeration — no single element is anomalous alone. **Defender takeaway:** if a detection for reflective loading keys on the origin of the `LoadLibraryW` call, this backdoor is built specifically to defeat it — pair it with a check on whether the executable region backing the caller has a file behind it.
