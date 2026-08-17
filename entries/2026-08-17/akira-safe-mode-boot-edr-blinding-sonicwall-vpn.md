---
schema: 1
kind: threat
horizon: operational
title: "Akira blinds EDR by rebooting a victim host into Safe Mode with Networking — the operator's first observed use of the technique, and the stripped-down boot starved its own encryptor"
headline: "Akira reboots a SonicWall-VPN victim into Safe Mode to strip EDR — and starves its own encryptor"
summary: >
  Huntress documents the first Akira intrusion it has observed using a Safe Mode with Networking reboot to
  take endpoint defences offline. After a credential spray resolved into a successful login on a SonicWall
  SSL VPN with no multi-factor authentication, the operator wrote its own AnyDesk service into the Safe Mode
  service allow-list, forced a reboot through msconfig, and worked from 06:29 UTC until 08:10 UTC on a host
  where neither the EDR agent nor Microsoft Defender real-time protection could start. The encryptor then
  failed — Safe Mode's constrained virtual memory starved the process tree — but Active Directory dumps and
  archived file shares had already left, so the intrusion stayed extortion-viable, and Huntress is explicit
  that the failure was the attacker's own memory-budget mistake rather than a defence to rely on.
discovered_at: "2026-08-17T04:28:31Z"
event_date: "2026-08-12"
run_id: 2026-08-17T0413Z-intel
priority: high
immediate_action: null
tags: [ransomware, identity, data-breach]
regions: [global]
sectors: []
entities: [actor:akira]
techniques: [T1133, T1110.003, T1078, T1021.001, T1059.001, T1087.002, T1018, T1560.001, T1567.002, T1219, T1112, T1688, T1486]
affected_products: ["SonicWall SSL VPN", "Microsoft Windows"]
cves: []
sources:
  - url: "https://www.huntress.com/blog/akira-hits-safe-mode-ransomware-rebooting-around-edr"
    publisher: "Huntress"
    date: "2026-08-12"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/akira-hackers-disable-edr-with-safe-mode-steal-data-but-fail-to-encrypt/"
    publisher: "BleepingComputer"
    date: "2026-08-13"
    role: corroborating
  - url: "https://www.theregister.com/research/2026/08/12/akira-ransomware-scum-blocked-victims-security-tools-and-broke-their-own-encryptor/5286515"
    publisher: "The Register"
    date: "2026-08-12"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Ransomware families like Snatch and AvosLocker have abused Safe Mode for years, but this is the first reported tie to Akira that Huntress has observed."
    publisher: "Huntress"
  - quote: "For the entire Safe Mode window, the host had no working EDR, and AV was blinded."
    publisher: "Huntress"
  - quote: "Alert on boot-configuration changes and Safe Mode boots: msconfig.exe / bcdedit activity, Kernel-Boot EID 27 with a SAFEBOOT load option, Kernel-General EID 12 BootMode=2, and third-party security services stopping (System EID 7036)."
    publisher: "Huntress"
  - quote: "That's a lucky side effect of the attacker's own mistake in these circumstances, not a defence you can plan around."
    publisher: "Huntress"
verification: single-source
sourcing_note: >
  Huntress is the sole assessor — the incident-response telemetry, the timeline and the detection guidance
  are all its own. BleepingComputer and The Register are republishers of that same research rather than
  independent observers, so the entry claims one assessor with three publishers rather than corroboration.
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
  - "Sweep Windows event logs across servers and workstations for Kernel-Boot EID 27 carrying a SAFEBOOT load option and Kernel-General EID 12 with BootMode=2, and for writes under HKLM\\SYSTEM\\CurrentControlSet\\Control\\SafeBoot\\Minimal or \\Network that name a remote-access tool rather than a core OS driver; treat any hit with no change-ticket behind it as a live intrusion, because in Safe Mode the endpoint agent that would normally have told you was not running."
migrated_from: null
---

An Akira affiliate took a compromised Windows host into Safe Mode with Networking to strip its endpoint defences, which Huntress reports is the first time it has observed this operator using the technique — Snatch and AvosLocker have abused Safe Mode for years, but not Akira ([Huntress, 2026-08-12](https://www.huntress.com/blog/akira-hits-safe-mode-ransomware-rebooting-around-edr)). Everything around that step is the operator's familiar chain. From roughly 03:45 UTC on 4 August the SonicWall logged a burst of failed logins against multiple usernames from several external addresses, and about seven minutes later one succeeded against an SSL VPN with no multi-factor authentication in front of it; nearly two hours passed before any hands-on-keyboard activity ([Huntress, 2026-08-12](https://www.huntress.com/blog/akira-hits-safe-mode-ransomware-rebooting-around-edr)). The operator then reached the domain controller over RDP, spawned an elevated command shell, and ran full-property `Get-ADUser` and `Get-ADComputer` exports to files under `C:\ProgramData` — prefixed with `$formatenumerationlimit = -1` so PowerShell's default four-item truncation would not clip multi-valued attributes such as group membership. Collection followed on an application server: WinRAR was installed mid-intrusion and used to recursively archive mapped file shares with the same flag string Huntress has documented in earlier SonicWall-entry Akira cases, and the archives went out to cloud object storage.

The evasion itself is three cheap steps. AnyDesk was installed as a service to carry both hands-on control and payload delivery; because third-party services do not start in Safe Mode — including the attacker's own — the operator first wrote that service into the Safe Mode allow-list with a single `reg.exe add` against `HKLM\SYSTEM\CurrentControlSet\Control\SafeBoot\Network`, then ran `msconfig.exe` at 06:29:21 UTC and forced the reboot. The host came back with Kernel-Boot event 27 recording a `SAFEBOOT:NETWORK` load option and Kernel-General event 12 recording `BootMode = 2`. Windows Defender logged event 3002 seconds into the boot, and Huntress states plainly that "For the entire Safe Mode window, the host had no working EDR, and AV was blinded" ([Huntress, 2026-08-12](https://www.huntress.com/blog/akira-hits-safe-mode-ransomware-rebooting-around-edr)).

What the operator did not anticipate is that the same stripped-down environment starved the ransomware. The encryptor launched at 06:34:29 UTC, and within about two minutes the host logged System event 26 for virtual-memory exhaustion and a cascade of PowerShell stack failures; it never encrypted. A scheduled Defender scan identified the binary at 07:43:50 UTC but its cleanup routine failed repeatedly because real-time protection was down, and quarantine only succeeded at 08:12:28 UTC — after the attacker rebooted back to normal operation at 08:10:38 UTC and thereby restored the very protection they had removed ([Huntress, 2026-08-12](https://www.huntress.com/blog/akira-hits-safe-mode-ransomware-rebooting-around-edr)). Huntress calls that "a lucky side effect of the attacker's own mistake in these circumstances, not a defence you can plan around", and notes that a host with more memory or a larger page file, or a retooled encryptor with a lighter footprint, could carry the same play to completion ([Huntress, 2026-08-12](https://www.huntress.com/blog/akira-hits-safe-mode-ransomware-rebooting-around-edr)).

**Defender takeaway:** the whole chain from first VPN logon to attempted detonation ran in under five hours, and the data theft succeeded regardless of the encryption failure, so an environment that survives this on encryption alone has still lost its Active Directory inventory and its file shares. The detection weight sits on boot-configuration telemetry rather than on the endpoint agent, precisely because the agent is what the technique removes: Huntress recommends alerting on `msconfig.exe` and `bcdedit` activity, on Kernel-Boot event 27 with a SAFEBOOT load option, on Kernel-General event 12 with `BootMode=2`, on third-party security services stopping (System event 7036), and on tooling being added to the Safe Mode minimal-service registry list ([Huntress, 2026-08-12](https://www.huntress.com/blog/akira-hits-safe-mode-ransomware-rebooting-around-edr)). Those events survive the reboot in the local log and reach a SIEM if VPN and Windows logs are already being shipped, which is also what makes the two-hour gap between the successful spray and the first hands-on action usable. Coverage is the other half: Huntress records that in this environment "the agent was on a fraction of the machines the attacker enumerated; unmonitored hosts are where preparation happens undetected" ([Huntress, 2026-08-12](https://www.huntress.com/blog/akira-hits-safe-mode-ransomware-rebooting-around-edr)).

**Triage:** Safe Mode with Networking is a legitimate diagnostic boot mode, so a lone Safe Mode boot is not the signal and IT-driven troubleshooting will generate them. The discriminators are what surrounds it: a SafeBoot `Minimal` or `Network` registry write naming a remote-access tool rather than a core Windows driver, a boot-configuration change made from an interactive session that traces back to an external VPN logon minutes earlier, and third-party security services stopping without a corresponding maintenance window. A genuine support-driven Safe Mode boot carries none of those, and the registry write in particular has no benign reason to name a remote-support binary.
