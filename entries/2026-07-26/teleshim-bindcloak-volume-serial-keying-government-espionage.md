---
schema: 1
kind: research
horizon: operational
title: "TELESHIM / MIXEDKEY / BINDCLOAK — DLL side-loading under a legitimate vendor binary, Telegram-API C2 and volume-serial environmental keying against government networks"
headline: "An espionage toolkit that only decrypts its final implant on the target machine, and talks C2 through the Telegram Bot API"
summary: >
  Zscaler ThreatLabz documents a previously undocumented three-stage toolkit used against government
  entities, attributed with moderate-to-high confidence to an East-Asia-based actor. The chain is a
  hunt-relevant combination rather than a novel exploit: an ISO delivers a legitimate ASUSTek binary that
  side-loads a malicious DLL to execute under a trusted vendor executable; the TELESHIM
  backdoor persists via scheduled tasks and uses the Telegram Bot API for command-and-control so its
  traffic resolves to a mainstream service; and the final BINDCLOAK implant decrypts only with a key
  derived from the victim machine's volume serial number, so it will not run in a sandbox or on an
  analyst's copy.
discovered_at: "2026-07-26T14:15:00Z"
event_date: "2026-07-20"
run_id: 2026-07-26T1308Z-audit
priority: notable
immediate_action: null
tags: [espionage, nation-state]
regions: [middle-east, global]
sectors: [public-sector]
entities: []
techniques: [T1574.001, T1102.002, T1027, T1480.001, T1053.005]
affected_products: []
cves: []
sources:
  - url: "https://www.zscaler.com/blogs/security-research/targeted-attack-government-entities-middle-east-part-1"
    publisher: "Zscaler ThreatLabz"
    date: "2026-07-20"
    role: primary
closed_sources: []
evidence:
  - quote: "ThreatLabz observed new activity by a threat actor with links to East Asia targeting government entities in the Middle East."
    publisher: "Zscaler ThreatLabz"
  - quote: "TELESHIM abuses the Telegram API for C2 communication, a technique used to blend in with legitimate internet traffic."
    publisher: "Zscaler ThreatLabz"
  - quote: "Based on the geolocation of the IP address, the configured system locale, and active operational hours matching regional working timeframes, ThreatLabz assesses with moderate-to-high confidence that the threat actor is operating out of East Asia."
    publisher: "Zscaler ThreatLabz"
verification: single-source
sourcing_note: "Zscaler ThreatLabz is the originating research lab and the sole source; no independent corroboration had appeared by the time of writing. The post is labelled Part 1 of a series, so further technical and attribution detail is expected."
confidence: medium
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
migrated_from: null
---

The victims here are government entities in the Middle East, not Europe, and the actor is assessed as East-Asian — so the reason this matters to a Swiss or European government defender is the tradecraft, which is aimed at exactly their target class and combines three techniques that each defeat a different common control. Zscaler ThreatLabz "observed new activity by a threat actor with links to East Asia targeting government entities in the Middle East", assessing attribution "with moderate-to-high confidence" on the basis of "the geolocation of the IP address, the configured system locale, and active operational hours matching regional working timeframes" ([Zscaler ThreatLabz, 2026-07-20](https://www.zscaler.com/blogs/security-research/targeted-attack-government-entities-middle-east-part-1)) — a hedge worth carrying as stated rather than hardening into a country attribution.

Initial execution comes from an ISO containing a legitimate ASUSTek executable, `RegSchdTask.exe`, which side-loads a malicious library named `AsTaskSched.dll`; at the staging step the legitimate executable is copied to its working path under the name `shimgen.exe` ([Zscaler ThreatLabz, 2026-07-20](https://www.zscaler.com/blogs/security-research/targeted-attack-government-entities-middle-east-part-1)). The first code to run therefore executes under a legitimate vendor binary rather than an attacker-authored one, so controls that key on the executable's identity or reputation see a known-good file. The first-stage TELESHIM backdoor persists through scheduled tasks and, rather than contacting dedicated infrastructure, "abuses the Telegram API for C2 communication, a technique used to blend in with legitimate internet traffic" — which means the egress destination is a mainstream service that many organisations either allow outright or cannot block without business friction, and domain- or reputation-based egress control gives no signal. TELESHIM and the MIXEDKEY reflective loader carry heavy obfuscation (control-flow flattening, mixed boolean arithmetic, opaque predicates), and the final BINDCLOAK implant is decrypted only with a key derived from the victim machine's volume serial number, so the payload cannot be detonated on any machine other than the intended one.

**Defender takeaway:** the environmental-keying step is the one that changes a defender's workflow. A sample pulled from a targeted host will not execute in a sandbox or on an analyst workstation, so a "nothing happened when we ran it" result from dynamic analysis is not evidence of a benign file — the triage decision has to rest on the delivery chain and host artefacts rather than on detonation. For the other two links, the durable controls are boring and effective: treat ISO and other mountable container attachments as a delivery class in mail policy, since the ISO is what allows a legitimate vendor binary and its planted DLL to arrive together with the disk-image origin flag; and decide deliberately whether the Telegram Bot API endpoint is something the estate needs to reach, because it is an allowlisted-service C2 channel here rather than an anomalous destination.

**Triage:** the ASUSTek executable is a legitimate vendor file, and DLL side-loading of this kind produces process telemetry that looks legitimate — so the discriminators are location and provenance rather than the executable's identity. Look for that vendor executable running from a mounted-image path or a user-writable directory instead of its installed application tree, loading a same-directory DLL, on a host with no corresponding ASUS software installed; a scheduled task created shortly afterwards under that lineage raises it further. For the C2 leg, traffic to the Telegram Bot API from a server or from a workstation whose user has no Telegram client installed is the reviewable case — Telegram traffic from staff endpoints that legitimately run the app is noise, and the discriminator is the absence of the client, or a non-browser, non-Telegram process making the connection.
