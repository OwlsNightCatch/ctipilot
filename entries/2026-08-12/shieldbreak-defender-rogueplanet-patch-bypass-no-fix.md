---
schema: 1
kind: vulnerability
horizon: operational
title: "ShieldBreak — a public proof-of-concept defeats Microsoft's July fix for the RoguePlanet Defender flaw, claims 100% reliability where the original was a coin flip, and now covers Windows Server 2025"
headline: "Nightmare Eclipse drops a Defender privilege-escalation patch bypass on Patch Tuesday itself, with no fix available"
summary: >
  Researcher Nightmare Eclipse published ShieldBreak on 2026-08-11/12, a proof-of-concept the
  researcher describes as a full bypass of the patch Microsoft shipped in July for RoguePlanet
  (CVE-2026-50656), the Microsoft Malware Protection Engine privilege-escalation flaw that yields a
  SYSTEM shell on fully updated Windows. Two properties make it worse than what it replaces: it is
  listed with a 100 percent success rate where RoguePlanet was an unreliable race, and it is listed
  as tested on Windows Server 2025 alongside Windows 11 25H2, where the June exploit did not run.
  No patch exists, no vendor has publicly reproduced it, and Microsoft had not commented at
  publication.
discovered_at: "2026-08-12T04:47:00Z"
event_date: "2026-08-12"
run_id: 2026-08-12T0411Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, priv-esc, lpe, poc-public, no-patch, zero-day]
regions: [global, europe]
sectors: [public-sector, energy, healthcare, finance, telco, technology]
entities:
  - actor:nightmare-eclipse
  - trend:shieldbreak-defender-rogueplanet-patch-bypass-2026-08
  - trend:nightmare-eclipse-rogueplanet-defender-toctou-lpe-2026-06
techniques: [T1068, T1548, T1036.005]
affected_products: ["Microsoft Defender Antivirus", "Microsoft Windows 11", "Microsoft Windows Server 2025"]
cves:
  - id: CVE-2026-50656
    cvss: "7.8"
    epss: null
    type: priv-esc
    vector: local
    auth: post-auth
    status: [poc-public, patch-available]
    affected: "Microsoft Malware Protection Engine builds before 1.1.26060.3008 (RoguePlanet, the flaw ShieldBreak is described as bypassing)"
    fixed: "Engine build 1.1.26060.3008, shipped 2026-07-09 — reported as bypassed by ShieldBreak"
sources:
  - url: "https://www.cyberkendra.com/2026/08/shieldbreak-poc-bypasses-microsofts.html"
    publisher: "Cyber Kendra"
    date: "2026-08-12"
    role: primary
  - url: "https://www.rapid7.com/blog/post/em-patch-tuesday-august-2026/"
    publisher: "Rapid7"
    date: "2026-08-11"
    role: corroborating
closed_sources: []
evidence:
  - quote: "ShieldBreak is listed with a 100 percent success rate."
    publisher: "Cyber Kendra"
  - quote: "No patch exists for ShieldBreak, and no vendor has reproduced it publicly yet."
    publisher: "Cyber Kendra"
verification: multi-source
sourcing_note: >
  Both sources report the researcher's own claims about ShieldBreak rather than independent
  reproduction — Cyber Kendra states explicitly that no vendor has reproduced it publicly, and
  Rapid7 reports the release as part of its Patch Tuesday round-up. The reliability rating reflects
  Rapid7 as the higher-reliability of the two; the credibility number reflects that the technical
  claims (100% success rate, Server 2025 coverage) trace to the researcher and are so far
  uncorroborated by any vendor or independent analysis.
confidence: medium
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
  - "Confirm application allowlisting is in enforcement — not audit — mode on Windows endpoints where standard users can write executables: ThreatLocker found allowlisting blocked RoguePlanet by default, and the source calls it the strongest control available for this bug class, and no patch exists."
migrated_from: null
---

The pseudonymous researcher Nightmare Eclipse published ShieldBreak, a proof-of-concept described as defeating the patch Microsoft shipped five weeks earlier for a Windows Defender privilege-escalation flaw ([Cyber Kendra, 2026-08-12](https://www.cyberkendra.com/2026/08/shieldbreak-poc-bypasses-microsofts.html)). Rapid7 places the drop late on Patch Tuesday itself, continuing what it describes as a pattern of the past few months ([Rapid7, 2026-08-11](https://www.rapid7.com/blog/post/em-patch-tuesday-august-2026/)). Rapid7, covering the same release in its Patch Tuesday analysis, records the researcher describing ShieldBreak as a full patch bypass for RoguePlanet — the entry in the same series that Microsoft patched as CVE-2026-50656 in July, a month after its public disclosure — and notes that both are elevation-of-privilege-to-SYSTEM vulnerabilities in Defender ([Rapid7, 2026-08-11](https://www.rapid7.com/blog/post/em-patch-tuesday-august-2026/)).

Two claims are what make this worth acting on rather than filing. RoguePlanet was a race condition whose reliability varied sharply between machines — the researcher called it hit or miss in June — while "ShieldBreak is listed with a 100 percent success rate". And where the June exploit did not run on Windows Server because standard users cannot mount ISO images there, ShieldBreak is listed as tested on Windows Server 2025 alongside Windows 11 25H2 and the Canary channel ([Cyber Kendra, 2026-08-12](https://www.cyberkendra.com/2026/08/shieldbreak-poc-bypasses-microsofts.html)). Both of those are the researcher's own claims: Cyber Kendra states that "No patch exists for ShieldBreak, and no vendor has reproduced it publicly yet", and that Microsoft had not commented at publication. Treat the reliability figure and the server coverage as unverified until someone reproduces them — but treat the existence of working exploit code as established, because that is what the release consists of.

The target is the Microsoft Malware Protection Engine, the scanner behind Defender, which runs as SYSTEM; RoguePlanet abused improper link resolution before file access to spawn a SYSTEM shell on fully updated machines, was rated Important at CVSS 7.8, and was fixed in engine build 1.1.26060.3008 on 2026-07-09. Analysts who dissected RoguePlanet in June described an attack chain built on NTFS junctions, opportunistic locks and the Windows Error Reporting `QueueReporting` scheduled task, which Cyber Kendra reads as suggesting ShieldBreak reworks the same plumbing rather than opening a new front ([Cyber Kendra, 2026-08-12](https://www.cyberkendra.com/2026/08/shieldbreak-poc-bypasses-microsofts.html)) — that is an inference in the reporting, not a stated finding, and no technical analysis of ShieldBreak itself has been published.

The reason a local privilege-escalation PoC from this particular persona deserves more than a backlog ticket is the track record the same reporting sets out: of the previously disclosed flaws in the series, three — BlueHammer (CVE-2026-33825), RedSun (CVE-2026-41091) and UnDefend (CVE-2026-45498) — were exploited in real-world intrusions before fixes landed and all three ended up in CISA's Known Exploited Vulnerabilities catalog ([Cyber Kendra, 2026-08-12](https://www.cyberkendra.com/2026/08/shieldbreak-poc-bypasses-microsofts.html)). This is also the second time a fix in this class has fallen: Microsoft hardened Defender's internal file-handling APIs in mid-May and RoguePlanet was rewritten to defeat that.

Compensating controls, not patching, are the available lever. The one the reporting names as strongest for this bug class is application allowlisting — ThreatLocker found it blocked RoguePlanet by default ([Cyber Kendra, 2026-08-12](https://www.cyberkendra.com/2026/08/shieldbreak-poc-bypasses-microsofts.html)). Detection concepts follow the RoguePlanet chain rather than ShieldBreak's unpublished internals, so they are hypotheses to hunt with rather than confirmed signatures for this variant: in filesystem and process telemetry, reparse-point or junction creation by a standard-user process inside a path the Defender engine subsequently touches, and unexpected execution lineage from the Windows Error Reporting scheduled task, are the observable steps that chain described. Because the escalation ends in a SYSTEM process spawned by an engine that legitimately runs as SYSTEM all day, the parent-process shape alone will not separate this from routine scanning activity — the preceding filesystem manipulation by an unprivileged account is where the discriminator lives.
