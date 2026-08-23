---
schema: 1
kind: threat
horizon: operational
title: "SPECTRE unlinks EDR's kernel callbacks one at a time using a two-driver BYOVD toolkit and an offset table for thirteen Windows builds — and its Linux half hides through ftrace rather than the syscall table"
headline: "A cross-platform implant that blinds named endpoint products to process, thread and image-load events for the rest of the session"
summary: >
  Cisco Talos published an analysis on 2026-08-20 of SPECTRE, a cross-platform C backdoor deployed by
  a Chinese-speaking intrusion actor it tracks as UAT-10147 against compromised IIS and Linux web
  servers. The Windows variant loads one of two long-known vulnerable drivers as a transient kernel
  service, locates the kernel image through a documented information call, and uses a hardcoded
  per-build offset table covering thirteen Windows versions to unlink registered process-creation,
  thread-creation and image-load notification callbacks from their linked lists — blinding
  callback-dependent endpoint products, which Talos names as CrowdStrike Falcon, SentinelOne and
  Microsoft Defender, for the remainder of the session. Credential access deliberately avoids LSASS
  entirely, and the C2 configuration is held in an alternate data stream on the hosts file so it can be
  rotated without recompiling. The Linux variant persists as a systemd unit ordered ahead of security
  tooling and hides through the kernel's ftrace debugging interface rather than by patching the syscall
  table.
discovered_at: "2026-08-23T04:58:00Z"
event_date: "2026-08-20"
run_id: 2026-08-23T0409Z-intel
priority: high
immediate_action: null
tags: [organized-crime, infostealer, priv-esc]
regions: [global, europe]
sectors: [public-sector, telco, technology, education, media]
entities: [actor:uat-10147, malware:spectre-uat10147]
techniques: [T1190, T1068, T1055.012, T1055.004, T1134.001, T1014, T1685, T1027, T1003.002, T1555.003, T1071.001]
affected_products: ["Microsoft Windows", "Microsoft Internet Information Services", "Linux"]
cves:
  - id: CVE-2019-16098
    cvss: "7.8"
    epss: null
    type: priv-esc
    vector: local
    auth: post-auth
    status: [patch-available]
    affected: "MSI Afterburner RTCore64.sys (driver abused as a kernel read/write primitive; not a new flaw)"
    fixed: "long patched — carried here only as the vulnerable driver the implant brings with it"
  - id: CVE-2021-21551
    cvss: "8.8"
    epss: null
    type: priv-esc
    vector: local
    auth: post-auth
    status: [patch-available]
    affected: "Dell DBUtil_2_3.sys (driver abused as a kernel read/write primitive; not a new flaw)"
    fixed: "long patched — carried here only as the vulnerable driver the implant brings with it"
sources:
  - url: "https://blog.talosintelligence.com/uat-10147-deploys-spectre-a-cross-platform-implant-with-linux-rootkit-and-byovd-capabilities/"
    publisher: "Cisco Talos"
    date: "2026-08-20"
    role: primary
closed_sources: []
evidence:
  - quote: "By performing targeted kernel writes, the SPECTRE safely unlinks each registered EDR callback from its doubly-linked list"
    publisher: "Cisco Talos"
  - quote: "kernel-callback-dependent security products such as CrowdStrike Falcon, SentinelOne, Microsoft Defender"
    publisher: "Cisco Talos"
  - quote: "This strategy allows the threat actor to easily update the C2 configuration by modifying the ADS, thereby circumventing firewall blocklists without needing to recompile the binary."
    publisher: "Cisco Talos"
  - quote: "Talos investigated the source code of the Specter rootkit and assesses with medium confidence that UAT-10147 leveraged a combination of AI-assisted development and human expertise in the creation of this rootkit, which is designed to be invoked directly by SPECTRE."
    publisher: "Cisco Talos"
  - quote: "Signal 62 triggers process hiding by removing the target task_struct from the kernel PID list"
    publisher: "Cisco Talos"
verification: single-source
sourcing_note: >
  Cisco Talos is the sole assessor. The two CVEs recorded here are the long-patched third-party driver
  flaws the implant carries with it as its kernel read/write primitive, not new vulnerabilities in the
  targeted estate — they are listed so an asset owner can check whether either driver is permitted to
  load, and their status reflects that both were patched years ago. Neither score comes from Cisco Talos, which names both CVEs but publishes none, and the two have different provenance: the Dell flaw's score is its own CNA record's, while the MSI flaw's CNA record carries no metrics at all, so its score is the national vulnerability database's analyst assessment. Both vectors specify a local low-privileged account rather than administrative rights. The article's own coverage section
  lists vendor signature names and network rule identifiers, which this entry does not reproduce.
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
actions:
  - "Check whether RTCore64.sys and DBUtil_2_3.sys can load in your estate — Microsoft's vulnerable-driver blocklist covers both, and confirming it is enforced (rather than merely available) removes this implant's entire kernel-write path."
migrated_from: null
---

Cisco Talos published an analysis on 2026-08-20 of SPECTRE, a cross-platform C backdoor run by a Chinese-speaking intrusion actor it designates UAT-10147, which compromises internet-facing IIS and Linux web servers and monetises them through search-engine fraud ([Cisco Talos, 2026-08-20](https://blog.talosintelligence.com/uat-10147-deploys-spectre-a-cross-platform-implant-with-linux-rootkit-and-byovd-capabilities/)). The Windows build implements 45 commands, the Linux build 29. The interesting half is not the command set but how each variant makes itself unobservable, and both answers are instructive for tooling choices rather than for signature lists.

**Blinding the endpoint on Windows.** SPECTRE downloads one of two long-known vulnerable drivers from its command-and-control server — MSI's `RTCore64.sys` (CVE-2019-16098) or Dell's `DBUtil_2_3.sys` (CVE-2021-21551) — writes it to the temporary directory, installs it as a transient kernel service through the Service Control Manager, and opens a device handle to it. Neither is a new flaw; both are being reused as an arbitrary kernel read/write primitive. With that primitive it locates the kernel image in memory through a documented system-information call, then consults a hardcoded offset table covering thirteen Windows versions to compute where the notification-callback arrays live, and performs targeted writes: *"By performing targeted kernel writes, the SPECTRE safely unlinks each registered EDR callback from its doubly-linked list"*. The three callback classes it removes are process creation, thread creation and image load — the events most endpoint products depend on to see anything happen at all. Talos names the affected class as *"kernel-callback-dependent security products such as CrowdStrike Falcon, SentinelOne, Microsoft Defender"*, alongside other unnamed vendors. The blinding lasts for the remainder of the session, which matters for response scoping: it is not a permanent modification, and a reboot restores callback registration, but everything the implant does after that point produced no callback-derived telemetry.

**Execution, privilege and credentials.** Talos also documents the implant's injection tradecraft — standard process hollowing, targeting a common Windows service host by default, and an asynchronous-procedure-call injection variant executed early in a target process's lifetime. Escalation is named-pipe impersonation — the implant creates a pipe under a predictable per-thread name and acquires a SYSTEM token from a client that connects to it. Credential access is then deliberately built to avoid the one place defenders watch hardest: with SYSTEM in hand it saves the SAM, SYSTEM and SECURITY registry hives to disk for offline hash extraction, enumerates stored Windows credentials by capturing the output of the built-in credential-manager listing utility — Talos emphasises this happens without any LSASS access — and copies Chrome and Edge login-data and local-state files for offline DPAPI decryption with a named public post-exploitation tool. No process ever opens a handle to LSASS, so a detection strategy anchored on LSASS access sees none of it.

**Command-and-control that survives blocking.** The C2 configuration is stored in an alternate data stream on the Windows hosts file. Talos's framing of why: *"This strategy allows the threat actor to easily update the C2 configuration by modifying the ADS, thereby circumventing firewall blocklists without needing to recompile the binary."* The evasion value is specifically against static, hash-keyed and recompile-triggered detection rather than against telemetry that observes stream creation.

**The Linux half.** Persistence is a systemd unit presenting itself as a hardware performance monitor, and the detail worth carrying is its ordering directive: the unit is configured to start before the system initialisation target, which Talos states ensures the rootkit loads on every boot ahead of any security tooling. The kernel module masquerades as the legitimate ACPI processor power-management module. Hiding is implemented through ftrace with the instruction-pointer-modify flag, redirecting six entry points covering TCP socket enumeration for both IPv4 and IPv6, the three signal-delivery syscalls and directory enumeration. Talos's own explanation of why this choice matters: because ftrace is a legitimate kernel debugging interface, hooking through it produces minimal noise in kernel integrity checks — which is to say it specifically defeats tools that watch the syscall table for patching but do not watch ftrace registration state. Control is exercised by sending signals to a magic process id: one signal unlinks a task structure from the kernel process list so its `/proc` entry disappears, another unlinks the module itself from the kernel module list so it vanishes from module listings, a third rewrites the calling process's credential structure to grant it root, and a fourth serves as a module-load acknowledgement handshake.

**On the AI claim, at the source's own confidence.** Talos makes three separate and differently-hedged statements here, and they should not be collapsed. Scoped to the Linux rootkit's source code specifically, it states: *"Talos investigated the source code of the Specter rootkit and assesses with medium confidence that UAT-10147 leveraged a combination of AI-assisted development and human expertise in the creation of this rootkit, which is designed to be invoked directly by SPECTRE."* It rests that on four observations — an opening comment block that reads like a generated feature list narrating what the code is about to do, decorative separators of machine-like uniformity across more than ten sections, pedagogical inline comments explaining basic kernel concepts a developer would not explain to themselves, and three redundant implementations explicitly labelled as alternative methods where a human targeting one kernel would pick one. That last observation is the most portable: producing every known approach rather than selecting one is a completeness reflex, and it is a heuristic that works independently of this actor. Separately and without a confidence qualifier, Talos assesses the actor is gradually incorporating AI-assisted development more broadly, extending the suggestion to the SPECTRE backdoor itself without the same enumerated evidence. And separately again, build-path strings inside the actor's custom privilege-escalation tools reference an "AI" directory, which Talos describes only as strongly suggesting AI assistance in developing those tools — weaker wording, different tools, and not part of the medium-confidence rootkit assessment.

**Defender takeaway:** the two Windows-side dependencies are both removable in advance. The kernel-write primitive requires one of two specific third-party drivers to load, and Microsoft's vulnerable-driver blocklist covers both — so the question worth answering this week is not whether the blocklist exists but whether it is actually enforced on your servers, because if it is, the callback-unlinking step has no primitive to build on. On Linux, integrity checking that inspects only the syscall table is not sufficient against this implant; ftrace registration state and the kernel module list need to be compared against a known-good baseline, and a systemd unit ordered ahead of system initialisation is worth inventorying on its own. **Triage:** loading a signed third-party driver as a transient service is something legitimate vendor tooling and hardware utilities also do, and both drivers here are genuine signed products — the discriminators are the driver being written to a temporary directory rather than a vendor install path, the service existing only briefly around the load, and endpoint telemetry from that host going quiet for process and image-load events while the host demonstrably stays up and serving traffic. That last one inverts the usual reasoning: a sudden absence of routine callback-derived events from a busy server is itself the signal.
