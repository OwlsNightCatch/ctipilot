---
schema: 1
kind: research
title: "Symantec and Carbon Black: the fast16 sabotage framework corrupted LS-DYNA and AUTODYN nuclear-detonation simulations; Kim Zetter argues it was contemporaneous with Stuxnet"
headline: "Symantec: fast16 corrupted LS-DYNA and AUTODYN simulations of uranium compression in nuclear detonations"
summary: "Broadcom's Symantec and Carbon Black teams reported on 2026-05-16 that fast16, the circa-2005 sabotage framework SentinelOne first analyzed in April 2026, hooks LS-DYNA and AUTODYN through a boot-start filesystem driver and scales down simulation outputs only in high-explosive runs once the simulated material passes 30 g/cm³, a density uranium reaches only in an implosion device. It spreads only inside its own network and avoids hosts with endpoint-security products; Kim Zetter argues that, if it targeted Iran, it was contemporaneous with Stuxnet rather than a predecessor, while Broadcom still calls it pre-Stuxnet."
discovered_at: "2026-05-19T05:00:06Z"
event_date: 2026-05-16
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
techniques: [T1059, T1014, T1565.003, T1543.003, T1546.012, T1070.006, T1518.001, T1135, T1021.002, T1570, T1569.002]
affected_products: []
cves: []
sources:
  - url: "https://www.security.com/blog-post/fast16-nuclear-sabotage"
    publisher: Broadcom Security
    date: "2026-05-16"
    role: primary
  - url: "https://thehackernews.com/2026/05/pre-stuxnet-fast16-malware-tampered.html"
    publisher: The Hacker News
    date: "2026-05-18"
    role: corroborating
  - url: "https://www.zetter-zeroday.com/experts-confirm-the-fast16-malware-was-sabotaging-nuclear-weapons-tests-likely-in-iran/"
    publisher: Kim Zetter / ZERO DAY
    date: "2026-05-16"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The malware checks for the density of the material being simulated and only acts when that value passes 30 g/cm³, the threshold uranium can only reach under the shock compression of an implosion device."
    publisher: Broadcom Security
    source_url: "https://www.security.com/blog-post/fast16-nuclear-sabotage"
  - quote: "Fast16 didn't predate Stuxnet but was contemporaneous with it. It also wasn't aimed at altering nuclear weapons but was simply feeding false data to engineers about the nuclear detonation tests they were conducting, in order to trick them into believing the tests were failing."
    publisher: Kim Zetter / ZERO DAY
    source_url: "https://www.zetter-zeroday.com/experts-confirm-the-fast16-malware-was-sabotaging-nuclear-weapons-tests-likely-in-iran/"
  - quote: "Organizations concerned about similar threats capable of sabotage should iterate regularly across their endpoints to inventory loaded drivers, flagging any that are unsigned or unfamiliar."
    publisher: Broadcom Security
    source_url: "https://www.security.com/blog-post/fast16-nuclear-sabotage"
verification: multi-source
sourcing_note: >
  Symantec and Carbon Black reverse-engineered the hook engine and confirm the applications SentinelOne had identified, so two research teams agree on the
  technical core; Kim Zetter's framing rests on interviews with Symantec researchers and nuclear experts, and The Hacker News restates Broadcom.
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-19.md
updates:
  - at: "2026-10-21T20:42:29Z"
    run_id: 2026-10-21T1148Z-audit
    type: correction
    summary: >
      SentinelOne published the first public analysis of fast16 in April 2026 and dated its oldest
      components to around 2005, about two years before Stuxnet became active; no source places that
      disclosure at LABScon or describes earlier speculation about centrifuges. Broadcom's analysis
      appeared on 2026-05-16 and still calls fast16 pre-Stuxnet, while Kim Zetter argues it was
      contemporaneous with Stuxnet if it targeted Iran. LS-DYNA and AUTODYN are general explicit-dynamics
      simulation programs that are also used for explosive simulation.
    fields: [affected_products, body, classification, event_date, evidence, headline, sources, sourcing_note, summary, techniques, title]
---

Broadcom's Symantec and Carbon Black teams published on 2026-05-16 an analysis of fast16, the sabotage framework that SentinelOne first analyzed in April 2026 and whose oldest components date from around 2005, and confirm that its hook engine targets LS-DYNA and AUTODYN, applications used to simulate problems such as vehicle crashworthiness, material modelling and explosive simulation ([Broadcom Security, 2026-05-16](https://www.security.com/blog-post/fast16-nuclear-sabotage); [The Hacker News, 2026-05-18](https://thehackernews.com/2026/05/pre-stuxnet-fast16-malware-tampered.html)). The framework combines a service binary that embeds a Lua 5.0 virtual machine, a boot-start filesystem filter driver that patches Intel-compiled executables on the fly as they are read from disk, and 101 byte-pattern rules in nine or ten groups for different builds of the two programs ([Broadcom Security, 2026-05-16](https://www.security.com/blog-post/fast16-nuclear-sabotage)). Its hooks act only in high-explosive simulations and scale down outputs such as pressure or stress once the simulated material density passes 30 g/cm³, the threshold Broadcom says uranium reaches only under the shock compression of an implosion device, which it reads as sabotage of nuclear weapons research ([Broadcom Security, 2026-05-16](https://www.security.com/blog-post/fast16-nuclear-sabotage)).

Before installing, fast16 checks for 18 endpoint-security registry keys and refuses to spread if any is present; it then registers itself as a service whose file takes the creation dates and permissions of a system binary, loads its driver as a SCSI-class filter at the next boot, and persists by hijacking a chosen application through the Image File Execution Options Debugger value ([Broadcom Security, 2026-05-16](https://www.security.com/blog-post/fast16-nuclear-sabotage)). It spreads only inside its own network, enumerating domains, servers and shares and, for hosts in local address ranges, copying itself to their admin share under the logged-on user's credentials and creating a remote service ([Broadcom Security, 2026-05-16](https://www.security.com/blog-post/fast16-nuclear-sabotage)). Kim Zetter, citing Symantec researchers and nuclear experts, argues that if fast16 targeted Iran in 2005 it was contemporaneous with Stuxnet rather than its predecessor, and that it fed false simulation data to engineers rather than altering weapons ([Kim Zetter / ZERO DAY, 2026-05-16](https://www.zetter-zeroday.com/experts-confirm-the-fast16-malware-was-sabotaging-nuclear-weapons-tests-likely-in-iran/)); Broadcom still calls it a pre-Stuxnet tool ([Broadcom Security, 2026-05-16](https://www.security.com/blog-post/fast16-nuclear-sabotage)).

**Exposure:** Windows hosts that run Intel-compiled simulation software, specifically builds of LS-DYNA and AUTODYN from that era; the framework does not spread to hosts carrying any of the endpoint-security products it checks for ([Broadcom Security, 2026-05-16](https://www.security.com/blog-post/fast16-nuclear-sabotage)).

**Detection:** in driver inventory telemetry, a boot-start filter driver registered under the SCSI class that is unsigned or unfamiliar; in registry telemetry, an Image File Execution Options Debugger value that launches a non-debugger binary and is deleted and re-added around each launch of the target application; in file and service telemetry, a new service binary whose timestamps match a system file; in network telemetry, one host copying an executable to the admin shares of same-subnet hosts and starting remote services ([Broadcom Security, 2026-05-16](https://www.security.com/blog-post/fast16-nuclear-sabotage)).

**Defender takeaway:** Broadcom does not know whether a modern version of fast16 exists; operators of simulation and research-computing estates concerned about similar sabotage should inventory loaded drivers regularly, flagging unsigned or unfamiliar ones, and run tightly tuned application control ([Broadcom Security, 2026-05-16](https://www.security.com/blog-post/fast16-nuclear-sabotage)). Other organizations have no decision to make.

## Correction — 2026-10-21T20:42:29Z

SentinelOne's first public analysis of fast16 appeared in April 2026 and dated its oldest components to around 2005, about two years before Stuxnet first became active ([Broadcom Security, 2026-05-16](https://www.security.com/blog-post/fast16-nuclear-sabotage)); no source places that disclosure at LABScon or reports earlier speculation that fast16 attacked centrifuges. The two framings are not settled: Kim Zetter argues that if fast16 targeted Iran in 2005 it was contemporaneous with Stuxnet rather than its predecessor ([Kim Zetter / ZERO DAY, 2026-05-16](https://www.zetter-zeroday.com/experts-confirm-the-fast16-malware-was-sabotaging-nuclear-weapons-tests-likely-in-iran/)), while Broadcom's analysis, published on 2026-05-16 rather than 2026-05-18, still calls it a pre-Stuxnet tool ([Broadcom Security, 2026-05-16](https://www.security.com/blog-post/fast16-nuclear-sabotage)). LS-DYNA and AUTODYN are applications for simulating problems such as vehicle crashworthiness, material modelling and explosive simulation, not weapons-design codes as such, and Broadcom does not claim the hook engine is the first documented technique of its kind; the detection it supports rests on the install artifacts it documents and on inventorying unsigned or unfamiliar drivers ([Broadcom Security, 2026-05-16](https://www.security.com/blog-post/fast16-nuclear-sabotage)).
