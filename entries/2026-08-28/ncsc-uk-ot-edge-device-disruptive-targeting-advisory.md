---
schema: 1
kind: threat
title: "NCSC UK advisory: increased targeting of internet-exposed OT and edge devices globally, including the UK, by state and non-state actors, with 'some limited real-world disruption'"
headline: "The UK's national CERT tells operators to stop assuming their OT is inaccessible from the internet — and to go verify it"
summary: >
  NCSC UK published an advisory on 2026-08-27 stating it has observed increased targeting of
  operational technology systems across multiple sectors globally, including the UK, by a range
  of threat actors, resulting in some limited real-world disruption. The advisory names no
  specific actor, CVE or victim and links to its July 2026 joint advisory on Russian state actors
  exploiting poorly configured routers, framing this as a continuation of that threat pattern.
discovered_at: "2026-08-28T06:56:00Z"
updated_at: null
event_date: "2026-08-27"
run_id: 2026-08-28T0409Z-intel
priority: high
immediate_action: null
tags: [ot-ics, nation-state]
regions: [global, europe, uk]
sectors: [energy, water, transport]
entities: []
techniques: [T1190]
affected_products: []
cves: []
sources:
  - url: "https://www.ncsc.gov.uk/news/disruptive-cyber-activity-highlights-risk-from-internet-exposed-systems-and-edge-devices"
    publisher: "NCSC UK"
    date: "2026-08-27"
    role: primary
closed_sources: []
evidence:
  - quote: "The NCSC has seen increased targeting of operational technology (OT) systems across multiple sectors globally, including in the UK. This has been carried out by a range of threat actors and resulted in some limited real-world disruption."
    publisher: "NCSC UK"
  - quote: "the NCSC assesses that the threat from state use of offensive cyber, including outside of conflict, has almost certainly increased"
    publisher: "NCSC UK"
  - quote: "Organisations should not assume that their OT is inaccessible from the internet without verifying it, as unintended exposure can arise through misconfigurations, legacy connections, or unmanaged assets."
    publisher: "NCSC UK"
verification: single-source-national-cert
sourcing_note: >
  NCSC UK is a high-reliability national CERT publishing an advisory in its own jurisdiction and
  authority — the standard carve-out for this class of source; no independent second source was
  sought or needed.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Build or refresh a definitive OT asset and connectivity inventory for every internet-facing or potentially internet-reachable PLC, HMI or edge device, and confirm none is directly internet-exposed — NCSC-UK states unintended exposure commonly arises through misconfiguration, legacy connections or unmanaged assets rather than deliberate design, so the audit needs to check actual reachability, not documented network diagrams."
  - "Migrate every internet-reachable OT/edge management interface to a secured protocol variant (DNP3-SAv5, CIP Security, Modbus Security, OPC UA) and disable telnet and SNMPv1/v2 — NCSC-UK names these as the specific protocol-hardening steps for the exposure class its advisory describes."
updates:
  - at: "2026-08-28T15:00:00Z"
    run_id: 2026-08-28T1500Z-audit
    type: improvement
    internal: true
    summary: >
      Operator-directed editorial pass (v4.2): removed composition-rationale narration and 
      pipeline-internal jargon from reader-facing text; tightened or cut paragraphs that 
      restated the summary or padded without responder value. No factual claim changed.
    fields: [body]
migrated_from: null
---

NCSC UK published an advisory on 2026-08-27 stating it has observed increased targeting of operational technology (OT) systems across multiple sectors globally, including in the UK, carried out by "a range of threat actors" and resulting in "some limited real-world disruption": "the NCSC has seen increased targeting of operational technology (OT) systems across multiple sectors globally, including in the UK. This has been carried out by a range of threat actors and resulted in some limited real-world disruption" ([NCSC UK, 2026-08-27](https://www.ncsc.gov.uk/news/disruptive-cyber-activity-highlights-risk-from-internet-exposed-systems-and-edge-devices)). The advisory names no specific actor, CVE or victim, and is framed as a national-resilience notice rather than an incident disclosure: it instructs organisations with internet-exposed OT not to assume their systems are inaccessible from the internet without verifying it, citing misconfiguration, legacy connections and unmanaged assets as the typical exposure paths — "organisations should not assume that their OT is inaccessible from the internet without verifying it, as unintended exposure can arise through misconfigurations, legacy connections, or unmanaged assets" ([NCSC UK, 2026-08-27](https://www.ncsc.gov.uk/news/disruptive-cyber-activity-highlights-risk-from-internet-exposed-systems-and-edge-devices)).

NCSC UK assesses that "the threat from state use of offensive cyber, including outside of conflict, has almost certainly increased" ([NCSC UK, 2026-08-27](https://www.ncsc.gov.uk/news/disruptive-cyber-activity-highlights-risk-from-internet-exposed-systems-and-edge-devices)) against a backdrop of technology-enabled capability uplift and geopolitical instability, and explicitly links this to its July 2026 joint advisory (with partners) on Russian state actors exploiting poorly configured routers — a continuation of an already-flagged threat pattern rather than a new, isolated incident. It also connects topically to the prior coverage here of the Minnesota/US water-utility PLC campaign and the associated European exposure count (86% of 4,117 internet-facing Siemens SIMATIC S7-1200 units concentrated in four EU countries, reached through mobile-carrier connectivity).

The advisory's guidance is standard OT hardening: definitive asset/connectivity inventory, no direct internet exposure for PLCs/HMIs, no default or shared credentials (MFA or key-based authentication on management interfaces), segregated management, migration to secured protocol variants (DNP3-SAv5, CIP Security, Modbus Security, OPC UA) with telnet/SNMPv1/v2 disabled, and tested ransomware-resistant backups; its one distinctive instruction is to verify actual internet reachability against the documented architecture rather than trusting the documentation.

The only attacker behaviour the advisory itself describes is exploitation of internet-exposed PLC/HMI management interfaces; default/shared-credential access appears only in its mitigation guidance, not as observed adversary behaviour. **Triage:** this is a resilience notice naming an exposure class rather than a specific observed intrusion chain, so no benign-lookalike discriminator applies; the actionable step is verifying actual internet reachability against documented network architecture — the advisory's own framing is that the gap between the two is where exposure lives.
