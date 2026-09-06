---
schema: 1
kind: research
title: >
  TELESHIM / MIXEDKEY / BINDCLOAK — DLL side-loading under a legitimate vendor binary,
  Telegram-API C2 and volume-serial environmental keying against government networks
headline: >
  An espionage toolkit that only decrypts its final implant on the target machine, and talks C2
  through the Telegram Bot API
summary: >
  Zscaler ThreatLabz documents a previously undocumented three-stage toolkit used against
  government entities, attributed with moderate-to-high confidence to an East-Asia-based actor.
  The chain is a hunt-relevant combination rather than a novel exploit: an ISO delivers a
  legitimate ASUSTek binary that side-loads a malicious DLL to execute under a trusted vendor
  executable; the TELESHIM backdoor persists via scheduled tasks and uses the Telegram Bot API for
  command-and-control so its traffic resolves to a mainstream service; and the final BINDCLOAK
  implant decrypts only with a key derived from the victim machine's volume serial number, so it
  will not run in a sandbox or on an analyst's copy.
discovered_at: "2026-07-26T14:15:00Z"
updated_at: "2026-08-10T04:46:00Z"
event_date: 2026-07-20
run_id: 2026-07-26T1308Z-audit
priority: notable
immediate_action: null
tags:
  - espionage
  - nation-state
  - infostealer
regions:
  - middle-east
  - global
sectors:
  - public-sector
  - energy
entities:
  - "malware:bindcloak"
  - "malware:teleshim"
  - "tool:mixedkey"
  - "malware:octlurk"
techniques:
  - T1574.001
  - T1102.002
  - T1027
  - T1480.001
  - T1053.005
  - T1134.001
  - T1134.003
  - T1620
  - T1057
  - T1132.002
  - T1095
affected_products: []
cves: []
sources:
  - url: "https://www.zscaler.com/blogs/security-research/targeted-attack-government-entities-middle-east-part-1"
    publisher: Zscaler ThreatLabz
    date: 2026-07-20
    role: primary
  - url: "https://www.zscaler.com/blogs/security-research/targeted-attack-government-entities-middle-east-part-2"
    publisher: Zscaler ThreatLabz
    date: 2026-08-03
    role: primary
  - url: "https://securelist.com/octlurk-silklurk-backdoors-central-asia/120840/"
    publisher: Kaspersky GReAT
    date: 2026-07-30
    role: corroborating
closed_sources: []
evidence:
  - quote: ThreatLabz observed new activity by a threat actor with links to East Asia targeting government entities in the Middle East.
    publisher: Zscaler ThreatLabz
  - quote: "TELESHIM abuses the Telegram API for C2 communication, a technique used to blend in with legitimate internet traffic."
    publisher: Zscaler ThreatLabz
  - quote: "Based on the geolocation of the IP address, the configured system locale, and active operational hours matching regional working timeframes, ThreatLabz assesses with moderate-to-high confidence that the threat actor is operating out of East Asia."
    publisher: Zscaler ThreatLabz
  - quote: BINDCLOAK is a 64-bit modular backdoor written in C++ that uses a complex message routing mechanism to manage the C2 communication channel.
    publisher: Zscaler ThreatLabz
  - quote: "When resolving imports, each DLL is loaded via RtlQueueWorkItem with LoadLibraryW and the DLL name as arguments to evade EDRs since LoadLibraryW calls from unbacked executable memory regions are considered highly suspicious by EDRs."
    publisher: Zscaler ThreatLabz
  - quote: ThreatLabz assesses with high-confidence that BINDCLOAK is a variant of OctLurk.
    publisher: Zscaler ThreatLabz
  - quote: the new campaign we identified in July 2026 highlights a notable expansion of operations to target the Middle East with a key focus on the energy vertical.
    publisher: Zscaler ThreatLabz
verification: single-source
sourcing_note: >
  Zscaler ThreatLabz is the originating research lab and the sole source; no independent
  corroboration had appeared by the time of writing. The post is labelled Part 1 of a series, so
  further technical and attribution detail is expected.
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates:
  - at: "2026-08-10T04:46:00Z"
    run_id: 2026-08-10T0411Z-intel
    type: update
    summary: >
      Part 2 of Zscaler ThreatLabz's series on the actor behind TELESHIM and MIXEDKEY is a full
      teardown of BINDCLOAK, a 64-bit modular C++ backdoor whose plugin DLLs are reflectively loaded,
      with each import resolved by queueing LoadLibraryW through RtlQueueWorkItem specifically because
      a LoadLibraryW call originating from unbacked executable memory is what endpoint tooling treats
      as suspicious. It derives a per-victim host identifier from the computer name and volume serial
      number, encodes command-and-control traffic under two XOR layers over TLS, and exposes eleven
      commands centred on collecting and impersonating user and process tokens. ThreatLabz assesses
      with high confidence that BINDCLOAK is a variant of OctLurk, and reports the July 2026 campaign
      expanding into the Middle East energy sector.
    fields:
      - entities
      - evidence
      - sectors
      - sources
      - tags
      - techniques
      - body
    merged_from: 2026-08-10/bindcloak-rtlqueueworkitem-reflective-loading
migrated_from: null
---

The victims here are government entities in the Middle East, not Europe, and the actor is assessed as East-Asian — so the reason this matters to a Swiss or European government defender is the tradecraft, which is aimed at exactly their target class and combines three techniques that each defeat a different common control. Zscaler ThreatLabz "observed new activity by a threat actor with links to East Asia targeting government entities in the Middle East", assessing attribution "with moderate-to-high confidence" on the basis of "the geolocation of the IP address, the configured system locale, and active operational hours matching regional working timeframes" ([Zscaler ThreatLabz, 2026-07-20](https://www.zscaler.com/blogs/security-research/targeted-attack-government-entities-middle-east-part-1)) — a hedge worth carrying as stated rather than hardening into a country attribution.

Initial execution comes from an ISO containing a legitimate ASUSTek executable, `RegSchdTask.exe`, which side-loads a malicious library named `AsTaskSched.dll`; at the staging step the legitimate executable is copied to its working path under the name `shimgen.exe` ([Zscaler ThreatLabz, 2026-07-20](https://www.zscaler.com/blogs/security-research/targeted-attack-government-entities-middle-east-part-1)). The first code to run therefore executes under a legitimate vendor binary rather than an attacker-authored one, so controls that key on the executable's identity or reputation see a known-good file. The first-stage TELESHIM backdoor persists through scheduled tasks and, rather than contacting dedicated infrastructure, "abuses the Telegram API for C2 communication, a technique used to blend in with legitimate internet traffic" — which means the egress destination is a mainstream service that many organisations either allow outright or cannot block without business friction, and domain- or reputation-based egress control gives no signal. TELESHIM and the MIXEDKEY reflective loader carry heavy obfuscation (control-flow flattening, mixed boolean arithmetic, opaque predicates), and the final BINDCLOAK implant is decrypted only with a key derived from the victim machine's volume serial number, so the payload cannot be detonated on any machine other than the intended one.

**Defender takeaway:** the environmental-keying step is the one that changes a defender's workflow. A sample pulled from a targeted host will not execute in a sandbox or on an analyst workstation, so a "nothing happened when we ran it" result from dynamic analysis is not evidence of a benign file — the triage decision has to rest on the delivery chain and host artefacts rather than on detonation. For the other two links, the durable controls are boring and effective: treat ISO and other mountable container attachments as a delivery class in mail policy, since the ISO is what allows a legitimate vendor binary and its planted DLL to arrive together with the disk-image origin flag; and decide deliberately whether the Telegram Bot API endpoint is something the estate needs to reach, because it is an allowlisted-service C2 channel here rather than an anomalous destination.

**Triage:** the ASUSTek executable is a legitimate vendor file, and DLL side-loading of this kind produces process telemetry that looks legitimate — so the discriminators are location and provenance rather than the executable's identity. Look for that vendor executable running from a mounted-image path or a user-writable directory instead of its installed application tree, loading a same-directory DLL, on a host with no corresponding ASUS software installed; a scheduled task created shortly afterwards under that lineage raises it further. For the C2 leg, traffic to the Telegram Bot API from a server or from a workstation whose user has no Telegram client installed is the reviewable case — Telegram traffic from staff endpoints that legitimately run the app is noise, and the discriminator is the absence of the client, or a non-browser, non-Telegram process making the connection.

## Update — 2026-08-10T04:46:00Z

The earlier entry covered Part 1 of this series — the TELESHIM backdoor and the MIXEDKEY loader, and the environmental keying that ties a payload to the host it infected. Zscaler ThreatLabz has now published Part 2, a teardown of the toolkit's final stage ([Zscaler ThreatLabz, 2026-08-03](https://www.zscaler.com/blogs/security-research/targeted-attack-government-entities-middle-east-part-2)). Two things in it are new rather than restatement: the loading tradecraft, and a targeting expansion.

BINDCLOAK is described as "a 64-bit modular backdoor written in C++ that uses a complex message routing mechanism to manage the C2 communication channel," running two built-in modules alongside plugin DLLs delivered from the command server. The detail worth carrying into detection engineering is *how* those DLLs get loaded. Plugin modules are reflectively loaded, and when resolving their imports the backdoor queues `LoadLibraryW` through `RtlQueueWorkItem` rather than calling it directly — Zscaler is explicit about the reason, which is that a `LoadLibraryW` call originating from an unbacked executable memory region is exactly what endpoint tooling flags. This is evasion aimed at a specific, widely deployed heuristic: the call still happens, but the thread that makes it belongs to the thread pool rather than to the injected region, so the stack the detection inspects no longer points where it expects.

The rest of the design continues Part 1's environmental-keying theme without repeating it. A four-byte per-victim identifier is derived by summing the ASCII values of the computer name and adding the volume serial number, and travels in every command-and-control message. Traffic is encoded under two layers of XOR and carried over TLS on TCP. Eleven commands are grouped around tokens — collecting user tokens through an authentication call, enumerating processes to decide which tokens are worth taking, and starting modules under either a stolen user token or a duplicated process token — with the remainder covering module lifecycle and one command whose purpose ThreatLabz says it has not determined.

The attribution language matters and is carried exactly as published: ThreatLabz "assesses with high-confidence that BINDCLOAK is a variant of OctLurk." That is an assessment of family relationship, not an identity claim, and OctLurk itself is a family Kaspersky separately documented against Central Asian and Syrian government targets ([Kaspersky GReAT, 2026-07-30](https://securelist.com/octlurk-silklurk-backdoors-central-asia/120840/)). The targeting delta is that the July 2026 campaign shows "a notable expansion of operations to target the Middle East with a key focus on the energy vertical."

Detection, telemetry class first. The reflective-loading behaviour surfaces in image-load and thread telemetry rather than on disk: a module load whose initiating thread belongs to the process thread pool while the corresponding executable memory region has no backing file is the shape, and it is precisely the correlation that a stack-based `LoadLibraryW` heuristic alone will miss. Token activity is the second class — process enumeration immediately followed by token duplication with primary-token assignment rights, then a new module executing under a different user context within the same process. Network telemetry shows TLS over TCP with a fixed short identifier repeated across sessions from the same host. **Triage:** thread-pool work items and `LoadLibraryW` are both entirely ordinary in benign software, and legitimate services duplicate tokens routinely; the discriminator is the combination of an unbacked executable region in the same process, a module load initiated from a pool thread, and token duplication following process enumeration — no single element is anomalous alone. **Defender takeaway:** if a detection for reflective loading keys on the origin of the `LoadLibraryW` call, this backdoor is built specifically to defeat it — pair it with a check on whether the executable region backing the caller has a file behind it.
