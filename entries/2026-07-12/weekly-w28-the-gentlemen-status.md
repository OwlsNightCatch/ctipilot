---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-long-running
title: 'The Gentlemen (Storm-2697) status update — Unit 42''s full profile: 580 victims, a Qilin-affiliate lineage, and a suspected EDR-disable zero-day'
headline: The Gentlemen status update — Unit 42 profiles 580 victims/77 countries, ArmCorp/Qilin lineage, 90% affiliate cut, suspected EDR-disable zero-day
summary: 'Unit 42 published (2026-07-10) the first full technical profile of The Gentlemen RaaS (Microsoft: Storm-2697), which this pipeline has tracked since May. New this week: 580 claimed victims across 77 countries through 3 July (a ~6x H2-2025-to-H1-2026 increase), an assessed lineage from ''ArmCorp'' — an affiliate of Qilin — before the ~September 2025 rebrand to a 90%-payout RaaS, initial-access vectors now explicitly including Erlang/OTP SSH and Windows SMB flaws alongside the tracked FortiOS/FortiProxy path, and a third-party (Expel) report of a suspected zero-day used specifically to disable EDR, distinct from the previously-documented GentleKiller BYOVD framework.'
discovered_at: '2026-07-12T23:46:00Z'
event_date: 2026-07-10
run_id: 2026-07-12T2309Z-weekly
priority: notable
immediate_action: null
tags:
  - ransomware
regions:
  - global
  - europe
sectors:
  - public-sector
entities:
  - actor:thegentlemen
  - actor:qilin
cves: []
techniques:
  - T1190
  - T1685
  - T1486
affected_products:
  - Fortinet FortiOS
  - Fortinet FortiProxy
sources:
  - url: https://unit42.paloaltonetworks.com/the-gentlemen-ransomware/
    publisher: Palo Alto Networks Unit 42
    role: primary
closed_sources: []
evidence:
  - quote: The operators (roughly 20 of them) likely morphed from a private entity into a RaaS model on or about September 2025. While traditional RaaS models typically offer affiliates a 70% to 80% cut of paid ransoms, The Gentlemen offer an unprecedented 90% payout.
    publisher: Palo Alto Networks Unit 42
  - quote: When comparing the last six months of 2025 to the first six months of 2026, the number of victims claimed by The Gentlemen increased by slightly more than 6x.
    publisher: Palo Alto Networks Unit 42
verification: single-source
sourcing_note: Status delta rests on a single primary (Unit 42, 2026-07-10); WebSearch found only aggregator re-publications, no independent second source yet. Prior actor coverage (ESET, Kaspersky, Trend Micro, Microsoft) is referenced by Unit 42 but not re-verified this run. Reliability B, credibility 2 (single-source status update from a reliable research lab; the Expel EDR-disable zero-day is a cited third-party claim, not independently confirmed here).
confidence: medium
classification:
  reliability: B
  credibility: 2
update_of: 2026-06-29/the-gentlemen
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
---
**UPDATE (originally covered 2026-06-29):** Palo Alto Unit 42 published the first full technical profile of The Gentlemen (Microsoft: Storm-2697; also Phantom Mantis), consolidating and extending the picture this pipeline built from ESET's GentleKiller research and the FortiBleed nexus. The delta worth carrying: Unit 42 counts 580 claimed victims across 77 countries through 3 July 2026 (103 in manufacturing) and a "slightly more than 6x" victim increase from H2 2025 to H1 2026, and assesses the ~20 operators "likely morphed from a private entity into a RaaS model on or about September 2025," previously operating as "ArmCorp," an affiliate of Qilin, now offering an "unprecedented 90% payout" versus the typical 70-80% ([Unit 42, 2026-07-10](https://unit42.paloaltonetworks.com/the-gentlemen-ransomware/)). Two operationally relevant additions: the initial-access set now explicitly names Erlang/OTP SSH-server and Windows SMB-client flaws alongside the already-tracked FortiOS/FortiProxy edge path, and Unit 42 cites Expel describing a *suspected zero-day the group uses specifically to disable target EDR agents* — distinct from the BYOVD-based GentleKiller framework and not previously in this pipeline's coverage. The Go/C dual-language encryptor and Curve25519/XChaCha20 per-file key scheme are unchanged.

**Defender takeaway:** the actionable change since June is the broadened initial-access surface — organisations exposing Erlang/OTP SSH or reachable SMB now share the same entry-point risk previously framed mainly around FortiGate edge, so prioritise those alongside the Fortinet patch posture; the reported EDR-disable zero-day means tamper-protection and EDR-health monitoring (agent-stop/uninstall alerting) are worth confirming as a hunt, though the specific mechanism awaits Expel's own write-up.
