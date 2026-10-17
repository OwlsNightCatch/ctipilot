---
schema: 1
kind: research
title: "Sekoia: APT28 (GRU Unit 26165) tradecraft shifts to LLM-generated payloads and cloud-native C2"
headline: "Sekoia: APT28 (GRU Unit 26165) tradecraft shifts to LLM-generated payloads and cloud-native C2"
summary: "APT28 (GRU Unit 26165) tradecraft has moved to LLM-driven and cloud-native evasion. Sekoia documents LameHug — the first APT28 stealer that generates exfiltration code at runtime via a hosted LLM — plus BeardShell C2 over consumer cloud-storage providers and the FrostArmada SOHO-router DNS-hijack AiTM campaign against Microsoft 365 (Sekoia TDR, 2026-06-11)."
discovered_at: "2026-06-14T05:00:05Z"
event_date: 2026-06-11
run_id: 2026-06-14-e1d80e78
priority: high
immediate_action: null
tags:
  - nation-state
  - espionage
  - russia-nexus
  - ai-abuse
  - identity
regions:
  - europe
  - global
sectors:
  - defense
  - public-sector
  - energy
entities: []
cves: []
sources:
  - url: "https://blog.sekoia.io/apt28-an-evolution-of-tradecraft/"
    publisher: Sekoia TDR
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
migrated_from: briefs/2026-06-14.md
---

Sekoia's Threat Detection & Research team published a tradecraft-evolution retrospective on APT28 (Fancy Bear / Forest Blizzard), and the operationally relevant material is the 2025–2026 tooling ([Sekoia TDR, 2026-06-11](https://blog.sekoia.io/apt28-an-evolution-of-tradecraft/)). Three developments stand out for European defenders. **LameHug** is the first documented APT28 infostealer that delegates its logic to a large language model: base64-encoded prompts are sent to Alibaba's Qwen 2.5-Coder model via the Hugging Face inference API to generate collection and exfiltration code on the fly, observed against Ukrainian government targets — meaning the malicious behaviour is not statically present in the binary. **BeardShell** is a C++ backdoor that rotates its command-and-control across consumer cloud-storage providers (Koofr, Icedrive, Filen), defeating domain/IP blocklisting because the traffic is ordinary HTTPS to legitimate services. **FrostArmada** (April 2026) is a SOHO-router DNS-hijack campaign — 18,000-plus unique IPs across 120-plus countries — that rewrites DHCP/DNS on MikroTik and TP-Link devices to mount adversary-in-the-middle attacks against Microsoft 365 sign-ins (`T1557` Adversary-in-the-Middle, `T1071.001` Web Protocols for the cloud C2). Sekoia notes APT28's GooseEgg implant (CVE-2022-38028) ran for roughly five years before public disclosure — a reminder that current tools likely carry a similar blind-spot horizon.

**Why it matters to us:** NATO European ministries, defence suppliers and critical-infrastructure operators are named in the targeting. The detection priorities are concrete and IoC-free: hunt cloud-storage beaconing to Koofr/Icedrive/Filen from non-user workstations, alert on outbound traffic to Hugging Face inference endpoints from Windows hosts, monitor MikroTik/TP-Link DNS-setting changes in network-device logs, and treat Office documents delivered through Signal Desktop as a Mark-of-the-Web bypass risk — Sekoia notes APT28 uses the messenger to deliver Office lures that arrive without the Mark-of-the-Web protection.
