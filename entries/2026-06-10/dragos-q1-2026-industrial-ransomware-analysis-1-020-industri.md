---
schema: 1
kind: threat
horizon: operational
title: "Dragos Q1 2026 Industrial Ransomware Analysis: 1,020 industrial incidents, The Gentleman's 4× surge against Romanian energy, and the IT-adjacent intrusion pattern"
headline: "Dragos Q1 2026 Industrial Ransomware Analysis: 1,020 industrial incidents, The Gentleman's 4× surge against Romanian energy, and the IT-adjacent intrusion"
summary: "Dragos' quarterly industrial-ransomware report (published 3 June) is the single periodic landscape report treated in this brief; the focus below is only on what changes a Swiss/EU public-sector and critical-infrastructure SOC's posture, not the full survey (Dragos, 2026-06-03)."
discovered_at: "2026-06-10T05:00:19Z"
event_date: 2026-06-03
run_id: 2026-06-10-c84347b2
priority: notable
immediate_action: null
tags:
  - ransomware
  - ot-ics
  - organized-crime
  - iran-nexus
regions:
  - europe
  - global
sectors:
  - energy
  - water
  - manufacturing
entities:
  - "report:dragos-industrial-ransomware-q1-2026"
  - "actor:akira"
cves: []
sources:
  - url: "https://www.dragos.com/dragos-industrial-ransomware-analysis-q1-2026"
    publisher: "Dragos, 2026-06-03"
    role: primary
closed_sources: []
evidence: []
verification: single-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: true
deep_dive_category: annual-report
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-10.md
---

Dragos' quarterly industrial-ransomware report (published 3 June) is the single periodic landscape report treated in this brief; the focus below is only on what changes a Swiss/EU public-sector and critical-infrastructure SOC's posture, not the full survey ([Dragos, 2026-06-03](https://www.dragos.com/dragos-industrial-ransomware-analysis-q1-2026)). This treatment is logged once under the annual/periodic-report rule and will not be re-summarised; specific findings may be cited as context in later briefs.

**The shape of the quarter.** Dragos recorded 1,020 ransomware incidents against industrial organisations in Q1 2026, with manufacturing accounting for 62% of victims and Europe representing roughly a quarter of all incidents ([Dragos, 2026-06-03](https://www.dragos.com/dragos-industrial-ransomware-analysis-q1-2026)). The defining operational characteristic — and the most important point for defenders — is that the overwhelming majority of these incidents struck enterprise IT systems adjacent to OT rather than ICS-specific malware touching SCADA/PLC logic; OT processes generally remained technically intact even where operational disruption occurred. The practical implication is that the OT ransomware threat for European operators is, in the near term, an IT-segmentation and identity problem at the IT/OT boundary, not a protocol-level ICS-exploitation problem.

**Initial-access and post-compromise tradecraft.** The dominant access vectors Dragos attributes are exploitation of internet-facing services, credentials harvested by infostealers, and abuse of VPN infrastructure — the same access classes this brief covers daily (edge-appliance RCE, infostealer credential theft, VPN auth bypass). Post-compromise, operators leaned on legitimate remote-management tooling — AnyDesk, SimpleHelp, Atera, N-able, ConnectWise ScreenConnect — for persistence and lateral movement, which is the detection-engineering takeaway: RMM-tool execution is the high-yield hunt surface (T1133 External Remote Services, T1078 Valid Accounts, T1219 Remote Access Software, T1486 Data Encrypted for Impact). Notably, ICS engineering firms (≈90 incidents) and equipment manufacturers (≈49) were disproportionately hit — these are supply-chain stepping-stones into operator networks, so European operators should treat their ICS integrators and engineering-services vendors as part of their own attack surface.

**The European energy signal.** The quarter's sharpest regional finding is the surge of "The Gentleman" RaaS, which more than quadrupled from Q4 2025 to 83 incidents and explicitly targeted Romanian energy and water infrastructure: coal producer Complexul Energetic Oltenia (December 2025), national water authority Apele Române (≈1,000 systems), and — alongside Qilin — oil-pipeline operator Conpet (February 2026) ([Dragos, 2026-06-03](https://www.dragos.com/dragos-industrial-ransomware-analysis-q1-2026)). Qilin (198 incidents) led overall, followed by Akira (100), The Gentleman (83), LockBit 5.0 (71) and Play (53). Dragos also flags the Iranian-linked Pay2Key RaaS intensifying since the July 2025 Israel-Iran conflict resumption — a geopolitical-nexus actor worth tracking for European critical-infrastructure operators given spillover targeting patterns.

**Defender actions this report supports.** Treat the IT/OT boundary as the primary ransomware containment line: enforce strict segmentation and unidirectional/jump-host access between enterprise IT and OT, deny RMM tooling on OT-adjacent hosts by default and alert on any execution, and prioritise the same internet-facing-service and VPN patching this brief tracks for OT-adjacent enterprise estates. For operators dependent on ICS engineering/integration vendors, extend monitoring and access controls to those vendors' remote-access paths. [SINGLE-SOURCE] — Dragos is a HIGH-reliability OT/ICS specialist; specific victim attributions trace to Dragos' own reporting.
