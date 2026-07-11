---
schema: 1
kind: research
horizon: operational
title: "Symantec / Carbon Black document Fast16 hook engine targeting LS-DYNA/AUTODYN nuclear-simulation codes; Kim Zetter corrects \"pre-Stuxnet\" framing to contemporaneous-and-simulation-sabotage"
headline: "Symantec / Carbon Black document Fast16 hook engine targeting LS-DYNA/AUTODYN nuclear-simulation codes; Kim Zetter corrects \"pre-Stuxnet\" framing to"
summary: Background. Fast16 — a Lua-based sabotage framework — was first disclosed by SentinelOne at LABScon 2026 in April 2026 and originally framed as a Stuxnet predecessor by approximately two years. Earlier reporting also speculated that the malware operated against physical centrifuge equipment.
discovered_at: "2026-05-19T05:00:06Z"
event_date: 2026-05-18
run_id: 2026-05-19-2505c918
priority: notable
immediate_action: null
tags:
  - nation-state
  - espionage
  - ot-ics
  - iran-nexus
regions:
  - middle-east
  - global
sectors:
  - defense
  - energy
entities:
  - "campaign:fast16-symantec-carbon-black-contemporaneous-stuxnet-nuclea"
cves: []
sources:
  - url: "https://www.security.com/blog-post/fast16-nuclear-sabotage"
    publisher: Broadcom Security
    role: primary
  - url: "https://thehackernews.com/2026/05/pre-stuxnet-fast16-malware-tampered.html"
    publisher: The Hacker News
    role: corroborating
  - url: "https://www.zetter-zeroday.com/experts-confirm-the-fast16-malware-was-sabotaging-nuclear-weapons-tests-likely-in-iran/"
    publisher: Kim Zetter / ZERO DAY
    role: corroborating
closed_sources: []
evidence:
  - quote: "Fast16's hook engine is selectively interested in high-explosive simulations inside LS-DYNA and AUTODYN, and the malware checks for the density of the material being simulated and only acts when that value passes 30 g/cm³, the threshold uranium can only be reached under the shock compression of an implosion device"
    publisher: Broadcom Security
  - quote: "Fast16 didn't predate Stuxnet but was contemporaneous with it. It also wasn't aimed at altering nuclear weapons but was simply feeding false data to engineers about the nuclear detonation tests they were conducting, in order to trick them into believing the tests were failing"
    publisher: Kim Zetter / ZERO DAY
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
migrated_from: briefs/2026-05-19.md
---

**Background.** Fast16 — a Lua-based sabotage framework — was first disclosed by SentinelOne at LABScon 2026 in April 2026 and originally framed as a Stuxnet predecessor by approximately two years. Earlier reporting also speculated that the malware operated against physical centrifuge equipment. Both framings now appear incorrect on closer expert review.

Broadcom's Symantec and Carbon Black teams published a technical analysis on 2026-05-18 documenting the framework's operating envelope and target selection ([Broadcom Security, 2026-05-18](https://www.security.com/blog-post/fast16-nuclear-sabotage); [The Hacker News, 2026-05-18](https://thehackernews.com/2026/05/pre-stuxnet-fast16-malware-tampered.html)). The architecture: a service binary embedding an early Lua 5.0 VM; a boot-start filesystem driver intercepting executable code as it is read from disk; and a rule-driven hook engine rewriting specific instruction sequences inside narrowly targeted simulation applications. The hook engine selectively intercepts execution inside LS-DYNA and AUTODYN — the canonical high-explosive simulation codes used for weapons design — and activates only when the simulated material density exceeds 30 g/cm³, the threshold reachable only under implosion shock-compression conditions relevant to weapons-grade uranium. Kim Zetter's investigative analysis on 2026-05-16 separately corrected the historical framing of the campaign ([Kim Zetter / ZERO DAY, 2026-05-16](https://www.zetter-zeroday.com/experts-confirm-the-fast16-malware-was-sabotaging-nuclear-weapons-tests-likely-in-iran/)): Fast16 was contemporaneous with Stuxnet, not a predecessor, and was engineered to feed false output to weapons engineers rather than to physically alter nuclear infrastructure. Defender relevance is narrow but specific: Broadcom appears to describe the first publicly-documented use of a filesystem-driver-level instruction-rewriting hook engine to corrupt scientific-simulation output — a sabotage technique class distinct from data exfiltration, ransomware, or DoS. Operators of national-laboratory research-computing environments, defence-related HPC clusters, and reactor-physics-modelling labs should add filesystem-driver-load monitoring (Sysmon EID 6, Windows boot-start driver enumeration) and integrity checking of long-running simulation binaries to their threat models.
