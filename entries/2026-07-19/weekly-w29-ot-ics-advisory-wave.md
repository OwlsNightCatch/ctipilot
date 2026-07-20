---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-sector-patterns
title: "OT/ICS carried a full week of high-severity advisories across energy, water, transport and manufacturing — a CVSS-10 debug-port takeover, a persistent-root switch chain, an early-boot coupler backdoor, and a KEV-listed building-automation lockout with no software fix"
headline: "W29 OT/ICS advisory wave — Rockwell 1715-AENTR (CVSS 10.0), Siemens RUGGEDCOM ROX II root chain, WAGO early-boot coupler, and the actively-exploited KNX lockout"
summary: >
  The operational-technology estate took a dense run of high-severity advisories in 2026-W29, spanning exactly the energy, water, transport and manufacturing sectors in the profiled constituency. The headline is CVE-2026-10577 in the Rockwell 1715-AENTR EtherNet/IP adapter (CVSS 10.0): an unauthenticated network-reachable debug port that lets an attacker read/delete files, stop tasks and change I/O states, with network isolation the interim control. Unit 42 published a full three-CVE RUGGEDCOM ROX II chain (CVE-2025-40947/40948/40949) reaching persistent, reboot-surviving root on Siemens OT switches that sit at rail/utility/water network boundaries. CERT@VDE disclosed a hidden early-boot diagnostic interface in WAGO I/O System Field couplers (CVE-2026-4769, CVSS 9.8) reachable without authentication during the boot window. And CISA KEV-listed the three-year-old KNX Connection Authorization lockout (CVE-2023-4346) as actively exploited — an attacker can permanently lock operators out of a building-automation installation with no software patch, only procedural hardening. None of the newly-disclosed items is reported exploited, but the KNX item confirms OT exposure is being actively used, and the interim controls (network isolation, boot-window segmentation, procedural lockout hygiene) matter as much as the firmware.
discovered_at: "2026-07-19T23:54:00Z"
event_date: 2026-07-18
run_id: 2026-07-19T2310Z-weekly
priority: notable
immediate_action: null
tags:
  - ot-ics
  - vulnerabilities
  - actively-exploited
  - cisa-kev
regions:
  - switzerland
  - europe
  - global
sectors:
  - energy
  - water
  - transport
  - public-sector
entities: []
cves: []
techniques:
  - T1190
affected_products:
  - "Rockwell Automation 1715-AENTR"
  - "Siemens RUGGEDCOM ROX II"
  - "WAGO I/O System Field"
  - "ABB T-MAC Plus"
sources:
  - url: "https://www.cisa.gov/news-events/ics-advisories/icsa-26-195-04"
    publisher: "CISA (ICSA-26-195-04, republishing Rockwell Automation PSIRT)"
    date: "2026-07-14"
    role: primary
  - url: "https://unit42.paloaltonetworks.com/siemens-rox-ii-zero-day-vulnerabilities/"
    publisher: "Palo Alto Networks Unit 42"
    date: "2026-07-17"
    role: primary
  - url: "https://www.certvde.com/en/advisories/VDE-2026-031/"
    publisher: "CERT@VDE"
    date: "2026-07-13"
    role: primary
  - url: "https://www.cisa.gov/news-events/alerts/2026/07/15/cisa-adds-two-known-exploited-vulnerabilities-catalog"
    publisher: "CISA"
    date: "2026-07-15"
    role: primary
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: "Every strand is a first-party advisory (CISA ICS, CERT@VDE, Siemens PSIRT via Unit 42) — Admiralty A; no exploitation is reported for the newly-disclosed items and the KNX exploitation is CISA-KEV-confirmed. cves: [] by design — each CVE is fully sourced in its referenced operational entry."
confidence: high
update_of: null
references:
  - 2026-07-15/cisa-ics-batch-rockwell-abb-energy-water-ot
  - 2026-07-18/siemens-ruggedcom-rox-ii-unit42-three-cve-chain
  - 2026-07-13/wago-io-system-field-cve-2026-4769-early-boot-backdoor
  - 2026-07-16/cve-2023-4346-knx-building-automation-lockout-dos-kev
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions: []
migrated_from: null
---

The week's OT/ICS advisories are worth reading as a set because they hit every sector the constituency defends and because the fixes are not uniformly "patch." The most severe newly-disclosed item is Rockwell's 1715-AENTR EtherNet/IP adapter (CVE-2026-10577, CVSS 10.0): a network-reachable debug port with no authentication lets an unauthenticated attacker read and delete files, stop tasks, modify memory and change I/O states on an adapter deployed in energy and water plants, with Rockwell fixing it in firmware 3.011 and naming network isolation as the interim control ([CISA ICSA-26-195-04, 2026-07-14](https://www.cisa.gov/news-events/ics-advisories/icsa-26-195-04)). The same CISA batch carried the ABB T-MAC Plus fuel/chemical terminal-management chain (led by CVE-2025-14771).

Siemens RUGGEDCOM ROX II — a routing/security boundary inside rail, utility, water and manufacturing networks across Europe — drew a full Unit 42 exploit chain: file disclosure via a root-privileged `xz` misuse (CVE-2025-40948), command injection in the feature-key signature-verification path (CVE-2025-40947), and task-scheduler command injection for persistent, reboot-surviving root (CVE-2025-40949), all fixed in firmware V2.17.1 ([Unit 42, 2026-07-17](https://unit42.paloaltonetworks.com/siemens-rox-ii-zero-day-vulnerabilities/)). WAGO's I/O System Field couplers exposed a hidden early-boot diagnostic interface reachable without authentication during the boot window (CVE-2026-4769, CVSS 9.8, [CERT@VDE VDE-2026-031, 2026-07-13](https://www.certvde.com/en/advisories/VDE-2026-031/)), fixed per-model in firmware.

The one confirmed-exploited item is the outlier that matters most operationally: CISA KEV-listed the KNX Connection Authorization Option-1 account-lockout flaw (CVE-2023-4346) three years after disclosure — an attacker with network or physical access to a KNX installation can purge unprotected devices and set a BCU key, permanently locking legitimate operators out **with no software patch**, only procedural hardening ([CISA, 2026-07-15](https://www.cisa.gov/news-events/alerts/2026/07/15/cisa-adds-two-known-exploited-vulnerabilities-catalog)). It is directly relevant to any Swiss/EU CI or public-sector estate running KNX for HVAC, lighting, access control or building management.

**Defender takeaway:** the week's OT signal is that CVSS-10-class exposure landed on exactly the profiled sectors, and the effective controls are network-architecture and procedure, not just firmware — segment the Rockwell debug port and the WAGO boot window off untrusted networks, apply the RUGGEDCOM V2.17.1 fix given the persistent-root outcome, and treat the KNX KEV listing as evidence that building-automation lockout is being used, so KNX Connection Authorization hardening is a now task, not a backlog item. Per-device firmware versions and the interim isolation steps are in the referenced operational entries.
