---
schema: 1
kind: threat
horizon: operational
title: "UAT-10147's SPECTRE implant unlinks EDR's kernel callbacks with two long-known vulnerable drivers, and on Linux persists as a systemd unit ordered to start before any security tooling"
headline: "After the unlinking step the endpoint agent still reports healthy and stops witnessing anything — the silence is the detection"
summary: >
  Cisco Talos published two companion analyses of UAT-10147, a Chinese-speaking intrusion actor monetising
  compromised web servers through search-ranking fraud and data theft, with confirmed victims in
  government, universities, media, technology and gaming across Brazil, Bolivia, China, Canada and
  Vietnam. Two techniques transfer regardless of the actor. On Windows, its SPECTRE backdoor fetches one
  of two long-known vulnerable third-party drivers, installs it as a transient kernel service, and uses
  the arbitrary kernel access it grants to unlink the process, thread and image-load notification
  callbacks that endpoint sensors depend on — Talos states the affected products are rendered completely
  blind for the rest of the session. On Linux, its rootkit persists through a systemd unit ordered to run
  before system initialisation, which Talos states puts it ahead of any security tooling on every boot.
  Talos separately assesses, at medium confidence, that the rootkit component's source reflects a
  combination of AI-assisted development and human expertise.
discovered_at: "2026-08-22T05:11:00Z"
event_date: "2026-08-20"
run_id: 2026-08-22T0410Z-intel
priority: notable
immediate_action: null
tags: [organized-crime, ai-abuse, actively-exploited]
regions: [global]
sectors: [public-sector, education, media, technology]
entities: [actor:uat-10147, malware:spectre-implant]
techniques: [T1190, T1505.003, T1505.004, T1068, T1134.001, T1685, T1543.003, T1547.006, T1014, T1543.002, T1055.012, T1055.004, T1027.007, T1027.013, T1497.001, T1564.004, T1071.001, T1053.005, T1136.001, T1021.001, T1105, T1588.002]
affected_products: ["Microsoft IIS", "Microsoft Windows", "Linux"]
cves:
  - id: CVE-2019-16098
    cvss: null
    epss: null
    type: priv-esc
    vector: local
    auth: admin-required
    status: [patch-available]
    affected: "the MSI graphics-utility kernel driver the implant fetches and loads; the driver is brought by the attacker rather than present on the victim"
    fixed: "not applicable — the defensive control is driver blocklisting, not patching a victim-side component"
  - id: CVE-2021-21551
    cvss: null
    epss: null
    type: priv-esc
    vector: local
    auth: admin-required
    status: [patch-available]
    affected: "the Dell firmware-utility kernel driver the implant fetches and loads; brought by the attacker rather than present on the victim"
    fixed: "not applicable — the defensive control is driver blocklisting, not patching a victim-side component"
sources:
  - url: "https://blog.talosintelligence.com/uat-10147-deploys-spectre-a-cross-platform-implant-with-linux-rootkit-and-byovd-capabilities/"
    publisher: "Cisco Talos"
    date: "2026-08-20"
    role: primary
  - url: "https://blog.talosintelligence.com/uat-10147-chinese-speaking-adversary-integrates-agentic-ai-into-post-compromise-operations/"
    publisher: "Cisco Talos"
    date: "2026-08-20"
    role: primary
closed_sources: []
evidence:
  - quote: "kernel-callback-dependent security products such as CrowdStrike Falcon, SentinelOne, Microsoft Defender, and other well-known EDR vendors are rendered completely blind to new process creations, thread creations, and image load events for the remainder of the session, successfully neutralizing EDR visibility on the target machine."
    publisher: "Cisco Talos"
  - quote: "is configured with “Before=sysinit.target”, ensuring the rootkit executes on every system boot prior to the initialization of any security tooling."
    publisher: "Cisco Talos"
verification: single-source
sourcing_note: >
  One originating lab publishing its own investigation across two same-day posts, so reliability is B and
  credibility stays at 2 with no second assessor. The two CVE records here are unusual and are included
  because an automated consumer needs them: they identify the vulnerable third-party drivers the implant
  *brings with it*, not flaws in anything the victim runs, and the `fixed` field says so — the control is
  blocklisting, not patching. Neither Talos post publishes an ATT&CK mapping, so the frontmatter mapping
  is this pipeline's, each identifier tied to a behaviour the posts describe. Two hedges are preserved.
  The AI-assisted-authorship finding is Talos's own medium-confidence assessment of a combination of
  machine and human work on the rootkit component, not a claim that the implant was machine-written, and
  the body carries both qualifiers. And the actor-naming overlap Talos reports is carried in the body at
  Talos's own medium confidence rather than recorded as a registry alias, because an alias would harden an
  assessment into an identity. No European or Swiss victim is named; the
  relevance is the sector match — government and universities are among the confirmed victim sectors — the
  exposure class of internet-facing web servers, and the actor-agnostic transferability of the two
  defence-impairment techniques. Talos ships detection content and an indicator file; neither is
  reproduced here.
confidence: high
update_of: null
references: []
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

Cisco Talos published two companion analyses on 2026-08-20 of UAT-10147, which it characterises as a highly capable Chinese-speaking intrusion actor operating a multi-platform post-exploitation ecosystem against internet-facing web servers. The business model is ordinary crime — Talos states the group engages in multiple criminal activities including search-engine-optimisation fraud and data theft — run at scale from compromised servers, with a target list of roughly 170,000 URLs recovered from an open directory on the actor's own infrastructure ([Cisco Talos, 2026-08-20](https://blog.talosintelligence.com/uat-10147-chinese-speaking-adversary-integrates-agentic-ai-into-post-compromise-operations/)). Confirmed victims sit in government, universities, media, technology and gaming, on servers in Brazil, Bolivia, China, Canada and Vietnam ([Cisco Talos, 2026-08-20](https://blog.talosintelligence.com/uat-10147-chinese-speaking-adversary-integrates-agentic-ai-into-post-compromise-operations/)). No European victim is named. Two of the techniques, however, have nothing to do with who this actor targets.

The first is the Windows defence-impairment step, and it is the reason this entry exists. Talos states SPECTRE retrieves one of two long-known vulnerable third-party drivers from its command-and-control server — a graphics-card utility driver associated with CVE-2019-16098 or a Dell firmware utility driver associated with CVE-2021-21551 — writes it to a temporary location and installs it as a transient kernel service ([Cisco Talos, 2026-08-20](https://blog.talosintelligence.com/uat-10147-deploys-spectre-a-cross-platform-implant-with-linux-rootkit-and-byovd-capabilities/)). Using the arbitrary kernel access those drivers expose, the implant locates the kernel image and, from a per-build offset table Talos says covers thirteen Windows versions, resolves the three notification callback routines for process creation, thread creation and image load, then unlinks each registered security-product callback. Talos's description of the result is unambiguous: kernel-callback-dependent security products including named major endpoint agents are rendered completely blind to new process creations, thread creations and image-load events for the remainder of the session ([Cisco Talos, 2026-08-20](https://blog.talosintelligence.com/uat-10147-deploys-spectre-a-cross-platform-implant-with-linux-rootkit-and-byovd-capabilities/)). The consequence for an investigation is that everything after this step happened without a witness — and the agent does not fail, crash or report degraded, it simply stops seeing.

The second is the Linux persistence, which expresses the same idea through a different mechanism. The rootkit component loads as a kernel module named after a legitimate processor-power-management module, and its persistence is a fraudulent systemd unit presented as a hardware performance monitor. What makes it durable is one ordering directive: Talos states the unit is configured with `Before=sysinit.target`, ensuring the rootkit executes on every system boot prior to the initialisation of any security tooling ([Cisco Talos, 2026-08-20](https://blog.talosintelligence.com/uat-10147-deploys-spectre-a-cross-platform-implant-with-linux-rootkit-and-byovd-capabilities/)). Rather than patching the syscall table it hooks a handful of syscall handlers through the kernel's own tracing framework, can hide processes by removing a task from the kernel's process list so the corresponding entry under `/proc` vanishes, and can hide itself from module listings by unlinking its own entry from the kernel module list. The companion post covers the actor's use of agentic AI tooling in exploitation, reconnaissance, payload generation, validation and persistence workflows; Talos separately assesses with medium confidence that the rootkit component's source reflects a combination of AI-assisted development and human expertise — an assessment from code characteristics, at its own stated confidence, and not a claim that the code was machine-written outright. Talos separately assesses, again at medium confidence, that several search-ranking-fraud components used in this campaign are associated with a handle it renders as x神 — an association scoped to those components, on the basis of development artifacts embedded in them, and not extended to the actor as a whole.

**Defender takeaway:** the hardening lever here is one that did *not* apply to the other driver-abuse research published the same week: because these are third-party drivers with assigned CVEs rather than a built-in Windows component, vulnerable-driver blocklisting — the Microsoft blocklist, hypervisor-protected code integrity, or an application-control policy — is exactly the control this case exists for, and it has to be in place before the unlinking step rather than after. On Windows, the detectable moment is the driver install and load, because it is the last thing the sensor sees. That means driver-load telemetry with process lineage and load context is the primary control — a signed but contextually absurd driver, a graphics-card overclocking utility or a workstation firmware tool, loading on a production web server is the anomaly, and the file appearing in a user-writable temporary path alongside a short-lived kernel service is the supporting sequence. After that step the durable detection is the silence itself, and it lives in telemetry most SOCs collect and few alert on: an endpoint agent that continues to report healthy and check in while emitting no process-creation, thread-creation or image-load events for a host that is demonstrably still serving traffic. Event-rate-per-host and sensor-health monitoring are ordinary operational metrics; here they are the only remaining witness. On Linux the equivalents are module-load audit records — a module named for a legitimate kernel component but loading from an unexpected path, unsigned, or at a moment no firmware or power event explains — and systemd unit-file creation or enablement, with a non-security unit carrying an ordering directive that places it before system initialisation as the specific thing to alert on. Because the rootkit hides by unlinking rather than by patching, inconsistency hunting works: a process visible to one enumeration path and absent from `/proc`, or a loaded module absent from the module listing, is the tell.

**Triage:** vulnerable drivers load legitimately all the time on the endpoints they belong to — a graphics utility driver on a workstation with that vendor's hardware is unremarkable, which is exactly why the discriminator is the host role rather than the driver. On a server there is no benign reason for either of these. The sensor-silence signal needs the same care in the other direction: an agent legitimately goes quiet when a host is idle, shut down or in maintenance, so the correlation that matters is silence in the process and image-load channels while other evidence — network flow, application logs, authentication records — shows the host is working. On Linux, a unit ordered before system initialisation is normal for storage, network and firmware units and abnormal for anything describing itself as a monitor or helper.
