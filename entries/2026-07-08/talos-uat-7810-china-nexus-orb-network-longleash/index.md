---
schema: 1
kind: threat
title: "Cisco Talos: China-nexus UAT-7810 expands its ORB network with LONGLEASH/DOGLEASH/JARLEASH via unpatched Ruckus and ASUS routers"
headline: "Talos: China-nexus UAT-7810 builds ORB relay networks from unpatched Ruckus/ASUS routers for secondary APTs"
summary: >
  Cisco Talos profiled UAT-7810, a China-nexus actor it assesses builds Operational Relay Box (ORB) networks from compromised Ruckus and ASUS routers for secondary China-nexus APTs (e.g. UAT-5918, documented against Taiwanese critical infrastructure). Initial access is known, unpatched router CVEs; the malware suite now adds LONGLEASH, DOGLEASH and JARLEASH. Detection is network-telemetry-based, on the CPE itself.
discovered_at: "2026-07-08T20:35:00Z"
event_date: 2026-07-07
run_id: 2026-07-08T2009Z-intel
priority: notable
immediate_action: null
tags:
  - nation-state
  - espionage
  - botnet
  - china-nexus
regions:
  - global
  - apac
sectors:
  - telco
  - public-sector
entities:
  - "actor:uat-7810"
  - "actor:uat-5918"
  - "tool:longleash-orb-malware-suite"
cves: []
sources:
  - url: "https://blog.talosintelligence.com/uat-7810/"
    publisher: "Cisco Talos"
    date: "2026-07-07"
    role: primary
closed_sources: []
evidence:
  - quote: "Talos assesses with high confidence that UAT-7810 is a China-nexus threat actor based on the infrastructure that it provides to secondary China-nexus APTs such as UAT-5918."
    publisher: "Cisco Talos"
  - quote: "Talos has observed UAT-7810 primarily exploit known vulnerabilities in unpatched Ruckus wireless routers, a tactic UAT-7810 has used since 2025."
    publisher: "Cisco Talos"
verification: single-source
sourcing_note: "Single reputable research-lab primary (Cisco Talos); same-day rewrites by other outlets are not independent corroboration. Attributed to Talos as the originating research."
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
  - "Patch or retire EoL Ruckus wireless APs and ASUS AiCloud routers exposed to CVE-2020-22653/-22658, CVE-2023-25717 and CVE-2025-2492; disable unneeded remote-management interfaces on edge/CPE devices."
  - "Baseline and alert on multi-protocol relay/fan-out behaviour (simultaneous HTTP/DNS/SOCKS/TCP/ICMP/UDP) from a single consumer-grade router or AP; treat inbound connections from residential/SOHO ranges into VPN/remote-access portals as a stronger signal than IP reputation alone."
migrated_from: null
---

Cisco Talos profiled UAT-7810, a China-nexus actor Talos assesses with high confidence is tasked with building and maintaining Operational Relay Box (ORB) networks — relay/proxy infrastructure built from compromised networking gear that secondary China-nexus APTs use to launder the origin of operations against high-value targets ([Cisco Talos, 2026-07-07](https://blog.talosintelligence.com/uat-7810/)). Talos names UAT-5918 — previously documented targeting Taiwanese critical infrastructure — as one such downstream consumer. Initial access is exploitation of known, unpatched vulnerabilities in Ruckus wireless routers (CVE-2020-22653, CVE-2020-22658, CVE-2023-25717) and ASUS AiCloud routers (CVE-2025-2492), a tactic UAT-7810 has used since 2025 rather than a fresh zero-day (`T1190`). The malware suite, internally "ff-agent", now includes LONGLEASH — an enhanced successor to the SHORTLEASH backdoor adding reverse-shell and HTTP/DNS/SOCKS/TCP/ICMP/UDP multi-protocol proxying (`T1090.003`) — plus DOGLEASH, a passive C-based Linux backdoor, and JARLEASH, a Java-based admin tool for file management and FTP/SFTP access; it is built with Boost.Asio, custom protobuf encoding and MbedTLS TLS proxying, compiled for MIPS/ARM/x64, and self-deletes if tampering or a suspicious connection is detected (`T1070`). **Defender takeaway:** the relevance here is the *actor and infrastructure model*, not a specific victim — a China-nexus ORB builder feeding critical-infrastructure-targeting APTs is exactly the same-actor read that matters for Swiss/European CI and government defenders, whose exposure is twofold: their own edge/CPE being conscripted into the relay mesh, and adversary traffic arriving *from* residential/SOHO ranges that IP-reputation alone will not flag. Detection is network-telemetry-based since the implants live on embedded CPE, not managed endpoints.
