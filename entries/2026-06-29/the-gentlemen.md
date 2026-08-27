---
schema: 1
kind: synthesis
horizon: strategic
title: The Gentlemen
headline: The Gentlemen
summary: >
  The Gentlemen ransomware makes Switzerland the second-most-targeted European country, claims 478
  victims and adds worm propagation — ESET's leaked-data deep-dive shows victims are chosen on
  FortiGate misconfiguration, tying the pipeline to FortiBleed reconnaissance. (daily 06-27,
  inside-it.ch)
discovered_at: "2026-06-29T00:21:21Z"
updated_at: "2026-07-19T23:36:00Z"
event_date: null
run_id: 2026-W26-b78503e7
priority: high
immediate_action: null
tags:
  - ransomware
  - organized-crime
  - russia-nexus
  - actively-exploited
regions:
  - switzerland
  - dach
  - europe
  - global
sectors:
  - manufacturing
  - healthcare
  - energy
  - public-sector
  - transport
entities:
  - "actor:thegentlemen"
  - "incident:fortibleed-fortigate-credential-exposure"
  - "actor:qilin"
techniques:
  - T1190
  - T1685
  - T1486
  - T1587.001
affected_products:
  - Fortinet FortiOS
  - Fortinet FortiProxy
cves: []
sources:
  - url: "https://www.inside-it.ch/aufstrebende-ransomware-bande-findet-mehr-schweizer-opfer-20260626"
    publisher: inside-it.ch
    role: primary
  - url: "https://www.welivesecurity.com/en/eset-research/killing-me-gently-inside-gentlemens-edr-killer-framework/"
    publisher: ESET WeLiveSecurity
    role: corroborating
  - url: "https://unit42.paloaltonetworks.com/the-gentlemen-ransomware/"
    publisher: Palo Alto Networks Unit 42
    role: primary
  - url: "https://reliaquest.com/blog/threat-spotlight-ransomware-and-cyber-extortion-in-q2-2026"
    publisher: ReliaQuest
    date: 2026-07-16
    role: primary
  - url: "https://www.infosecurity-magazine.com/news/the-gentlemen-most-prolific/"
    publisher: Infosecurity Magazine
    date: 2026-07-17
    role: corroborating
  - url: "https://www.cybersecuritydive.com/news/ransomware-concentrated-ai-guidepoint/824828/"
    publisher: Cybersecurity Dive (on GuidePoint GRIT Q2 2026)
    date: 2026-07-09
    role: corroborating
closed_sources: []
evidence:
  - quote: "The operators (roughly 20 of them) likely morphed from a private entity into a RaaS model on or about September 2025. While traditional RaaS models typically offer affiliates a 70% to 80% cut of paid ransoms, The Gentlemen offer an unprecedented 90% payout."
    publisher: Palo Alto Networks Unit 42
  - quote: "When comparing the last six months of 2025 to the first six months of 2026, the number of victims claimed by The Gentlemen increased by slightly more than 6x."
    publisher: Palo Alto Networks Unit 42
  - quote: "The Gentlemen became the most-active group, powered by aggressive affiliate recruitment and a well-packaged intrusion kit"
    publisher: ReliaQuest
verification: multi-source
sourcing_note: null
confidence: high
references:
  - 2026-07-18/metro-mondego-thegentlemen-ransomware-portugal-transit
weekly_section: weekly-long-running
deep_dive: false
deep_dive_category: null
org_triage: null
classification: null
watchlist_hit: false
actions: []
updates:
  - at: "2026-07-12T23:46:00Z"
    run_id: 2026-07-12T2309Z-weekly
    type: update
    summary: >
      Unit 42 published (2026-07-10) the first full technical profile of The Gentlemen RaaS
      (Microsoft: Storm-2697), which this pipeline has tracked since May. New this week: 580 claimed
      victims across 77 countries through 3 July (a ~6x H2-2025-to-H1-2026 increase), an assessed
      lineage from 'ArmCorp' — an affiliate of Qilin — before the ~September 2025 rebrand to a
      90%-payout RaaS, initial-access vectors now explicitly including Erlang/OTP SSH and Windows SMB
      flaws alongside the tracked FortiOS/FortiProxy path, and a third-party (Expel) report of a
      suspected zero-day used specifically to disable EDR, distinct from the previously-documented
      GentleKiller BYOVD framework.
    fields:
      - affected_products
      - entities
      - evidence
      - regions
      - sectors
      - sources
      - techniques
      - body
    merged_from: 2026-07-12/weekly-w28-the-gentlemen-status
  - at: "2026-07-19T23:36:00Z"
    run_id: 2026-07-19T2310Z-weekly
    type: update
    summary: >
      Update to the prior weekly's The Gentlemen (Storm-2697) profile. ReliaQuest's Q2 2026
      threat-spotlight (2026-07-16) reports The Gentlemen posted 300 victims in the quarter versus
      Qilin's 289, ending Qilin's leaderboard dominance, and attributes the pace to aggressive
      affiliate recruitment plus a well-packaged intrusion kit (pre-compromised victim lists, custom
      EDR killers, GPO-based deployment tooling) and a "likely AI-accelerated iteration layer" for
      tool refresh — with Infosecurity Magazine independently corroborating the 300-vs-289 figures. A
      GuidePoint GRIT review (pre-window) frames the same concentration as a "four-headed monster"
      (Qilin, The Gentlemen, Akira, DragonForce), with the five most prolific Q2 groups collectively
      claiming over 40% of recorded attacks. Operationally, the group's reach touched the constituency
      this week: Portugal's Metro Mondego confirmed a 6 July ransomware attack claimed by The
      Gentlemen, contained to internal systems. No new initial-access CVE or vector is disclosed — the
      delta is the quantitative leaderboard reversal, the AI-tooling-cadence explanation, and the
      fresh European public-transport victim.
    fields:
      - evidence
      - references
      - sectors
      - sources
      - tags
      - techniques
      - body
    merged_from: 2026-07-19/weekly-w29-thegentlemen-storm2697-status
migrated_from: briefs/weekly/2026-W26.md
---

The W25 multi-day item now has primary-evidence depth (the ESET deep-dive, § 7) and a sharp Swiss angle: Check Point data, reported by Swiss tech press, makes [Switzerland the second-most-targeted European country](https://www.inside-it.ch/aufstrebende-ransomware-bande-findet-mehr-schweizer-opfer-20260626) for the operation, which now claims 478 victims and has added worm propagation. The operationally important link is that victim selection runs on FortiGate misconfiguration scanning — so a Swiss organisation's FortiBleed exposure (above) is also its Gentlemen-victim-selection exposure. Outstanding for defenders: the same FortiGate hardening that closes FortiBleed reduces Gentlemen targeting, and EDR-tamper-protection plus driver-blocklist enforcement is the GentleKiller counter.

## Update — 2026-07-12T23:46:00Z

Palo Alto Unit 42 published the first full technical profile of The Gentlemen (Microsoft: Storm-2697; also Phantom Mantis), consolidating and extending the picture this pipeline built from ESET's GentleKiller research and the FortiBleed nexus. The delta worth carrying: Unit 42 counts 580 claimed victims across 77 countries through 3 July 2026 (103 in manufacturing) and a "slightly more than 6x" victim increase from H2 2025 to H1 2026, and assesses the ~20 operators "likely morphed from a private entity into a RaaS model on or about September 2025," previously operating as "ArmCorp," an affiliate of Qilin, now offering an "unprecedented 90% payout" versus the typical 70-80% ([Unit 42, 2026-07-10](https://unit42.paloaltonetworks.com/the-gentlemen-ransomware/)). Two operationally relevant additions: the initial-access set now explicitly names Erlang/OTP SSH-server and Windows SMB-client flaws alongside the already-tracked FortiOS/FortiProxy edge path, and Unit 42 cites Expel describing a *suspected zero-day the group uses specifically to disable target EDR agents* — distinct from the BYOVD-based GentleKiller framework and not previously in this pipeline's coverage. The Go/C dual-language encryptor and Curve25519/XChaCha20 per-file key scheme are unchanged.

**Defender takeaway:** the actionable change since June is the broadened initial-access surface — organisations exposing Erlang/OTP SSH or reachable SMB now share the same entry-point risk previously framed mainly around FortiGate edge, so prioritise those alongside the Fortinet patch posture; the reported EDR-disable zero-day means tamper-protection and EDR-health monitoring (agent-stop/uninstall alerting) are worth confirming as a hunt, though the specific mechanism awaits Expel's own write-up.

## Update — 2026-07-19T23:36:00Z

The prior weekly carried Unit 42's full profile of The Gentlemen (Storm-2697) — 580 claimed victims, a Qilin-affiliate lineage, a 90% affiliate payout and a suspected EDR-disable zero-day. This week the status change is quantitative and reaches the constituency. ReliaQuest's Q2 2026 threat-spotlight reports The Gentlemen "became the most-active group, powered by aggressive affiliate recruitment and a well-packaged intrusion kit" — 300 victims in Q2 against Qilin's 289 — with affiliates receiving pre-compromised victim lists, custom EDR killers and GPO-based deployment tooling, and a "likely AI-accelerated iteration layer" letting the operators refresh tooling faster than human-developer rivals ([ReliaQuest, 2026-07-16](https://reliaquest.com/blog/threat-spotlight-ransomware-and-cyber-extortion-in-q2-2026)); Infosecurity Magazine independently corroborates the 300-vs-289 figures ([Infosecurity Magazine, 2026-07-17](https://www.infosecurity-magazine.com/news/the-gentlemen-most-prolific/)). GuidePoint GRIT's pre-window Q2 review sets the same concentration in context — its "four-headed monster" is Qilin, The Gentlemen, Akira and DragonForce, and it reports the five most prolific groups collectively claimed over 40% of recorded Q2 attacks ([Cybersecurity Dive on GuidePoint GRIT, 2026-07-09](https://www.cybersecuritydive.com/news/ransomware-concentrated-ai-guidepoint/824828/)). Operationally, the group's claimed 6 July attack on Portugal's Metro Mondego — contained to internal systems, transport unaffected — is the fresh European public-sector datapoint. The initial-access funnel (the tracked FortiOS path and opportunistic edge exploitation) is unchanged; the practical takeaway for the constituency is that the most-active RaaS operator of the quarter is one already on its radar, now recruiting and tooling harder, so the FortiOS/edge and EDR-killer hunt posture the earlier coverage set remains the right one.
