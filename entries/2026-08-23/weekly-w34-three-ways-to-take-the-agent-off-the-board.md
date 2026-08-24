---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-top-stories
title: "Three unrelated disclosures this week removed the endpoint agent by three different mechanisms — a boot mode, a borrowed kernel driver, and Defender's own signed remediation driver — and the vulnerable-driver blocklist answers exactly one of them"
headline: "The agent was taken off the board three ways this week, and only the middle one has a blocklist"
summary: >
  Between 17 and 23 August 2026 three separate publications documented an operator removing the
  endpoint agent's ability to run rather than evading its rules. Huntress recorded an Akira affiliate
  rebooting a SonicWall-VPN victim into Safe Mode with Networking after writing its own remote-access
  service into the Safe Mode allow-list, leaving the host with no working EDR for the whole window.
  Cisco Talos documented SPECTRE loading one of two long-known vulnerable drivers and unlinking the
  registered process, thread and image-load notification callbacks, naming CrowdStrike Falcon,
  SentinelOne and Microsoft Defender as the affected class. Check Point Research showed that BTR.sys,
  the Microsoft-signed Boot Time Removal Tool driver Windows Defender extracts from MpEngine.dll,
  exposes an arbitrary kernel file and registry write to anyone who understands its transaction
  format — with no vulnerability, no memory corruption and, because the driver is a required Defender
  component pulled from the local machine's own DLL, nothing for a blocklist to key on. Microsoft's
  response centre declined to service it. A prior weekly covered rootkits that falsify what Windows
  reports; this week the target is whether the agent runs and whether it is told at all.
discovered_at: "2026-08-23T23:51:00Z"
event_date: "2026-08-20"
run_id: 2026-08-23T2311Z-weekly
priority: high
immediate_action: null
tags: [ransomware, espionage, lpe, zero-day, actively-exploited, no-patch]
regions: [global, europe]
sectors: [public-sector, technology, manufacturing, healthcare]
entities:
  - actor:akira
  - actor:uat-10147
  - malware:spectre-uat10147
  - tool:btr-sys-loldriver-primitive
techniques: [T1685, T1543.003, T1112, T1014, T1547.001]
affected_products: ["Microsoft Windows", "Microsoft Defender Antivirus"]
cves: []
sources:
  - url: "https://www.huntress.com/blog/akira-hits-safe-mode-ransomware-rebooting-around-edr"
    publisher: "Huntress"
    date: "2026-08-12"
    role: primary
  - url: "https://blog.talosintelligence.com/uat-10147-deploys-spectre-a-cross-platform-implant-with-linux-rootkit-and-byovd-capabilities/"
    publisher: "Cisco Talos"
    date: "2026-08-20"
    role: primary
  - url: "https://research.checkpoint.com/2026/btr-reforged-weaponizing-defenders-remediation-driver-as-a-kernel-operation-primitive/"
    publisher: "Check Point Research"
    date: "2026-08-20"
    role: primary
closed_sources: []
evidence:
  - quote: "For the entire Safe Mode window, the host had no working EDR, and AV was blinded"
    publisher: "Huntress"
  - quote: "By performing targeted kernel writes, the SPECTRE safely unlinks each registered EDR callback from its doubly-linked list"
    publisher: "Cisco Talos"
  - quote: "Recognize that the Microsoft Vulnerable Driver Blocklist (WDAC) does not protect against the abuse of functionally intended drivers like BTR.sys."
    publisher: "Check Point Research"
verification: multi-source
sourcing_note: >
  Three independent first-hand publishers, each reporting its own case or its own reverse engineering:
  Huntress from a incident-response engagement, Cisco Talos from a tracked intrusion set, Check Point
  Research from a driver analysis that began in an unrelated incident response. No cited source links
  the three, and this entry asserts no connection between the operators; the pattern claimed is a
  shared objective and three different answers to it.
confidence: high
update_of: null
references:
  - 2026-08-17/akira-safe-mode-boot-edr-blinding-sonicwall-vpn
  - 2026-08-23/spectre-uat-10147-byovd-edr-callback-unlink
  - 2026-08-23/btr-sys-defender-remediation-driver-kernel-primitive
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions: []
migrated_from: null
---

**If you did nothing this week:** the vulnerable-driver blocklist you may be relying on as the answer to kernel-level defence tampering covers one of the three techniques published this week, and the other two are answered by boot-configuration telemetry and by privilege reduction respectively. Whether the blocklist is actually *enforced* on your servers is the one question of the three that has a same-week answer.

A prior weekly covered two espionage toolsets shipping kernel rootkits whose job was to change the answers Windows gives to the tools that ask it — a telemetry teardown suite, and a driver hooking the network stack so operator-registered addresses were filtered out of what user mode saw. This week's three cases attack something one layer earlier: not the truthfulness of the report, but whether the agent runs at all and whether the kernel ever calls it. They arrive from three unrelated publishers, and the useful thing about seeing them together is that each one dies to a different control.

The cheapest is Akira's, and it involves no kernel code whatsoever. Huntress documents an affiliate that reached a domain controller through a SonicWall SSL VPN with no multi-factor authentication, installed AnyDesk as a service, and then — because third-party services do not start in Safe Mode, the attacker's own included — wrote that service into the Safe Mode allow-list with a single registry add before forcing the reboot through `msconfig.exe`. Huntress's summary of the result is unambiguous: "For the entire Safe Mode window, the host had no working EDR, and AV was blinded" ([Huntress, 2026-08-12](https://www.huntress.com/blog/akira-hits-safe-mode-ransomware-rebooting-around-edr)). There is no malicious binary to blocklist and no signature to write; the technique is a supported diagnostic boot mode plus a registry value. What survives it is boot-configuration telemetry — the Kernel-Boot and Kernel-General events recording the load option and boot mode persist in the local log across the reboot and reach a collector if Windows logs are already being shipped.

The middle case is the one a blocklist does answer, and it is worth being precise about why. Cisco Talos's SPECTRE analysis describes the implant downloading one of two long-known vulnerable drivers — MSI's `RTCore64.sys` or Dell's `DBUtil_2_3.sys` — installing it as a transient kernel service to obtain an arbitrary kernel read/write primitive, locating the kernel image through a documented information call, and then using a hardcoded offset table covering thirteen Windows versions to reach the notification-callback arrays: "By performing targeted kernel writes, the SPECTRE safely unlinks each registered EDR callback from its doubly-linked list" ([Cisco Talos, 2026-08-20](https://blog.talosintelligence.com/uat-10147-deploys-spectre-a-cross-platform-implant-with-linux-rootkit-and-byovd-capabilities/)). The three classes removed are process creation, thread creation and image load — the events most endpoint products depend on to observe anything — and Talos names CrowdStrike Falcon, SentinelOne and Microsoft Defender as the affected class alongside other unnamed vendors. Both drivers are third-party, both are known, and Microsoft's vulnerable-driver blocklist covers them, so the entire chain has no primitive to build on where that blocklist is enforced. On a fleet where it is configured but not verified, it has one.

Check Point's BTR.sys work is the case that has no such answer, and it is the reason to read the three together. `BTR.sys` — the "Boot Time Removal Tool" — is a genuine Microsoft-signed kernel driver embedded as a resource inside `MpEngine.dll`, which Defender extracts to `System32\drivers` under a randomised name when a remediation action needs a reboot to complete. Check Point's opening question is the finding: "What if a signed Microsoft remediation driver could be instructed to execute arbitrary file and registry operations from Ring 0 – without exploits, vulnerabilities, or memory corruption?" ([Check Point Research, 2026-08-20](https://research.checkpoint.com/2026/btr-reforged-weaponizing-defenders-remediation-driver-as-a-kernel-operation-primitive/)). The driver exposes no device interface; it reads an RC4-encrypted job list from an NTFS alternate data stream on its own file and executes six action types, two of which amount to arbitrary file write and arbitrary registry write. Check Point states the control implication directly: "Recognize that the Microsoft Vulnerable Driver Blocklist (WDAC) does not protect against the abuse of functionally intended drivers like BTR.sys." Adding it to the blocklist would disable Defender's own boot-time remediation on every Windows install, and because the tool is extracted from the local machine's `MpEngine.dll` each time, there is no external binary or hash for a blocklist to key on at all. Microsoft's response centre declined to service the finding on the grounds that the technique presupposes administrative privilege — a disposition that leaves the behaviour in place rather than assigning it a vulnerability identifier. Check Point reports no evidence of real-world abuse.

**Defender takeaway:** three techniques, three different controls, and only one of them is a list. Where the blocklist applies — the SPECTRE case — the question worth answering this week is enforcement rather than existence, because a policy configured on workstations and not on the servers running IIS is exactly the gap the implant was found in. Where it does not apply, the detection weight has to move off the agent, because the agent is what is being removed: boot-configuration telemetry for the Safe Mode case (a SafeBoot registry write naming a remote-access tool, a boot-mode event with no maintenance window), and for the BTR.sys class the privilege that gates it — audit and reduce holdings of the driver-load privilege — plus behavioural rules that treat a security vendor's own driver loading outside that vendor's expected process lineage as suspicious regardless of its signature. A fourth observation follows from the mechanics of all three rather than from any one source, and it is the one worth acting on: each technique works by stopping the flow of callback-derived events, so a busy host going quiet for process and image-load events while it demonstrably stays up and serving traffic is itself the signal. An alert on the *absence* of routine endpoint telemetry is the only detection that fires for all three of this week's techniques, because producing that absence is what all three are for.

**Triage:** every one of these produces artefacts that legitimate operations also produce. Safe Mode with Networking is a supported diagnostic boot and IT troubleshooting will generate them, so the discriminator is the surrounding sequence — a SafeBoot allow-list write naming a remote-support binary rather than a core Windows driver, traced back to an external VPN logon minutes earlier. Loading a signed third-party driver as a transient service is what hardware utilities and vendor tooling do, so the discriminators there are the driver being written to a temporary directory rather than a vendor install path and the service existing only briefly around the load. And BTR.sys is the hardest, because every artefact the technique produces is also produced by Defender doing its job: Check Point's own separators are the process lineage behind the driver load, the absence of a service-installation record alongside a service key created directly, and where the driver's feedback report is written — Defender's legitimate usage directs it to a standalone file under a protected path.
