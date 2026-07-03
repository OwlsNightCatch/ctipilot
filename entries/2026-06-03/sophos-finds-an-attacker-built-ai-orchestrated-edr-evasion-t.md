---
schema: 1
kind: research
horizon: operational
title: "Sophos finds an attacker-built, AI-orchestrated EDR-evasion testing lab during incident response"
headline: "Sophos finds an attacker-built, AI-orchestrated EDR-evasion testing lab during incident response"
summary: "Sophos X-Ops disclosed an EDR-evasion development-and-testing environment recovered during an incident-response engagement and linked to an active (unnamed, still-under-investigation) ransomware group (Sophos X-Ops, 2026-06-02)."
discovered_at: "2026-06-03T05:00:04Z"
event_date: 2026-06-02
run_id: 2026-06-03-ee0eae61
priority: notable
immediate_action: null
tags:
  - ai-abuse
  - ransomware
  - organized-crime
regions:
  - global
sectors:
  - technology
entities:
  - "campaign:underground-ai-adoption-sophos"
cves: []
sources:
  - url: "https://www.sophos.com/en-us/blog/pointing-a-cursor-at-evading-detection"
    publisher: Sophos X-Ops
    role: primary
  - url: "https://www.helpnetsecurity.com/2026/06/02/ai-agents-edr-evasion-techniques/"
    publisher: Help Net Security
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-03.md
---

Sophos X-Ops disclosed an EDR-evasion development-and-testing environment recovered during an incident-response engagement and linked to an active (unnamed, still-under-investigation) ransomware group ([Sophos X-Ops, 2026-06-02](https://www.sophos.com/en-us/blog/pointing-a-cursor-at-evading-detection)). The framework's Python payload generator — many modules partly AI-generated, with Russian-language comments — carried nearly 80 modules covering more than 70 evasion techniques. What distinguishes the lab is its agentic structure: a coordinator agent set rules for role-separated agents (EDR testing, OPSEC hardening, documentation, proxy stress-testing, VM deployment) connected over the Model Context Protocol to a Git repository, with the operator using the Cursor AI IDE and Ludus for rapid VM provisioning ([Help Net Security, 2026-06-02](https://www.helpnetsecurity.com/2026/06/02/ai-agents-edr-evasion-techniques/)). Payloads were tested against three isolated Windows Server 2022 VMs — one Sophos-equipped, one CrowdStrike-equipped, one EDR-free as baseline — with a Sliver/Cobalt Strike C2 stack and a Cloudflare Worker fronting the backend.

**Why it matters to us:** This is a concrete data point on adversaries operationalising agentic AI for detection-engineering against the exact EDR products (Sophos, CrowdStrike) deployed across CH/EU public-sector estates. The defensive principle is unchanged — the productivity multiplier is on the attacker's tooling, not a new bypass class — but it raises the priority of behavioural telemetry on payload-origin paths: Sophos noted the customer detection fired on "malicious payloads originating from a testing directory," a useful hunt pivot for anomalous build/test artefacts on endpoints.
