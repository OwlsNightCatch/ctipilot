---
schema: 1
kind: threat
horizon: operational
title: "Grandoreiro's loader decides it is in a sandbox when it finds seven ordinary desktop shortcuts — an inverted environment check, behind a two-hop DLL sideload"
headline: "The evasion logic is backwards on purpose: a clean, well-stocked desktop is what makes this malware quit"
summary: >
  Acronis's Threat Research Unit analysed a Grandoreiro banking-trojan wave delivered as a renamed copy of the
  legitimate Duplicate Files Finder utility, which loads its genuine dependency and is in turn used to sideload a
  malicious library under the ordinary-looking name of a MinGW runtime component. Before any command-and-control
  attempt the loader runs a staged environment gate whose standout check is inverted: if desktop shortcuts for
  all seven of a named set of mainstream consumer applications are present at once, it concludes it is in an
  analysis image and terminates. Acronis's telemetry places the largest share of samples in Mexico, with Spain
  and several Latin American countries forming a secondary cluster and European presence described as limited
  but notable. The command-and-control server was offline during analysis, so the protocol detail is static
  analysis rather than observed traffic.
discovered_at: "2026-08-20T04:56:00Z"
event_date: "2026-08-19"
run_id: 2026-08-20T0409Z-intel
priority: notable
immediate_action: null
tags: [organized-crime, phishing]
regions: [latam, europe]
sectors: [finance]
entities: [malware:grandoreiro]
techniques: [T1574.001, T1036.005, T1564.003, T1497.001, T1082, T1016, T1614, T1057, T1140, T1071.001]
affected_products: []
cves: []
sources:
  - url: "https://www.acronis.com/en/tru/posts/grandoreiro-goes-north-from-brazil-to-mexico-with-a-new-dll-sideloading-campaign/"
    publisher: "Acronis Threat Research Unit"
    date: "2026-08-19"
    role: primary
closed_sources: []
evidence:
  - quote: "In this campaign, the authors use the legitimate Duplicate Files Finder application but rename it to a randomly generated filename to obscure its purpose. When executed, it first loads another legitimate dependency, dupfdll.dll. This DLL then attempts to load its next dependency, mingwm10.dll, which is not legitimate. In this case, it is a malicious replacement version."
    publisher: "Acronis Threat Research Unit"
  - quote: "Interestingly, the presence of all of these applications is treated as an indicator of an analysis environment rather than a legitimate user system. If shortcuts for all seven applications are present on the desktop, the malware classifies the system as a sandbox environment and terminates execution."
    publisher: "Acronis Threat Research Unit"
  - quote: "Unfortunately, the server was offline at the time of our analysis, preventing direct interaction with the C2 infrastructure."
    publisher: "Acronis Threat Research Unit"
verification: single-source
sourcing_note: >
  One publisher, and no corroborating analysis of this wave was located this run, so the entry is carried as
  single-source and its claims are Acronis's throughout. Three limits in the source are load-bearing and are
  stated in the body rather than smoothed over: the initial delivery vector could not be conclusively confirmed
  and spam delivery is Acronis's own moderate-confidence assessment; the command-and-control server was offline
  during analysis, so everything about the protocol comes from static analysis of the binary and not from
  observed traffic; and Acronis marks its own DNS-over-HTTPS technique mapping as provisional pending
  substantiation, which is why that mapping is not carried in this entry's frontmatter. Acronis attributes the
  wave to no named actor or cluster and links it to no specific prior report. The geographic distribution is
  described in the article's summary as drawn from the last 30 days of June 2026, so it is not a
  current-as-of-publication picture. Acronis's own mapping table cites a DLL side-loading technique identifier
  that has since been revoked and merged upstream; this entry uses the surviving identifier.
confidence: medium
update_of: null
references: [2026-05-29/watchguard-documents-grandoreiro-s-delphi-dll-side-loading-w]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: null
---

Acronis's Threat Research Unit has published a teardown of a Grandoreiro wave whose loader chain is worth reading even for defenders with no Latin American exposure, because the evasion logic runs opposite to the assumption most sandbox-detection countermeasures are built on. Delivery is an archive carrying a renamed copy of Duplicate Files Finder, a legitimate Windows utility. On execution that binary loads its own genuine dependency, and the genuine dependency in turn attempts to load a further library — and it is that second-hop dependency, carrying the ordinary filename of a MinGW runtime component, which has been replaced with the malicious payload ([Acronis TRU, 2026-08-19](https://www.acronis.com/en/tru/posts/grandoreiro-goes-north-from-brazil-to-mexico-with-a-new-dll-sideloading-campaign/)). The camouflage works because a defender or an endpoint product inspecting loaded modules sees a runtime library name with no obvious reason for suspicion, two hops away from the executable that was actually launched. Acronis notes the compile timestamps disagree — the parent utility carries a 2008 timestamp against the implant's 2026 one — while caveating that PE timestamps are trivially forgeable and are corroboration rather than proof. Because the host utility is a windowed application, the implant's first action is to hide the window it would otherwise show.

The environment gate that follows is staged, and one stage is the interesting one. The loader checks that the machine has been up for at least three minutes, profiles memory, processor count, free disk, screen resolution and recently-opened-document history, looks for virtualization driver files and BIOS registry strings, walks a 49-entry blacklist of debuggers, disassemblers and network-analysis processes, performs an IP-geolocation lookup against a short country blacklist, and compares the username and hostname against known default sandbox identifiers. Sitting inside that sequence is a check that inverts the usual reasoning: the loader looks for desktop shortcuts to seven named mainstream applications — a browser set, a cleanup utility, an FTP client, a PDF reader and a messaging client — and if *all seven* are present simultaneously, it treats the machine as an analysis environment and stops, on the assessment (Acronis's, at moderate confidence) that this exact software bundle fingerprints a particular automated sandbox image rather than a real user's desktop ([Acronis TRU, 2026-08-19](https://www.acronis.com/en/tru/posts/grandoreiro-goes-north-from-brazil-to-mexico-with-a-new-dll-sideloading-campaign/)). A machine that fails the gate is shown a Spanish-language error dialog instead of the payload. Only a host that passes every stage sees the malware resolve its command-and-control address through a public DNS-over-HTTPS resolver rather than the operating system's own resolver, and fetch its next stage over an HTTP request to TCP port 6432 — behaviour Acronis reconstructed from the binary, because the server was offline when it looked.

The hunting value is in the sequence rather than in any single artefact. Acronis's own leads are a renamed copy of that utility loading the runtime-library name from its own directory, and a graphical process that suppresses its own window and then, within moments of launch, queries a public IP-geolocation service and reads the BIOS description keys out of the registry. **Triage:** the individual actions are all things ordinary software does — installers read hardware information, updaters check geography, plenty of applications ship MinGW runtimes — so no one of them separates malicious from benign. What does is the ordering and the compression: a windowed application that never draws its window, followed inside a few seconds by hardware profiling, a geolocation call and a BIOS registry read, is not doing what the utility whose name it wears is for. The inverted shortcut check is also a warning about analysis tooling itself: a standard, well-stocked analysis image is exactly the fingerprint this family quits on, so a silent non-execution in a sandbox is a result to interpret rather than a clean verdict.

**Defender takeaway:** this is a banking trojan aimed primarily at Latin America — Acronis's telemetry puts the largest share of samples in Mexico, with Spain and several Latin American countries as a secondary cluster and European presence characterised as limited but notable, mostly Spain — and it reports no targets at all in Brazil or Portugal despite the malware's Portuguese-speaking authorship ([Acronis TRU, 2026-08-19](https://www.acronis.com/en/tru/posts/grandoreiro-goes-north-from-brazil-to-mexico-with-a-new-dll-sideloading-campaign/)). For European defenders the transferable content is the tradecraft rather than the targeting: a two-hop sideload that puts the malicious module behind a legitimate intermediate dependency, and an environment gate that reasons about the *absence* of a too-perfect software set. Both are portable to any family, and the second one quietly degrades the confidence a team can place in a negative sandbox result.
