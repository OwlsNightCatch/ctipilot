---
schema: 1
kind: threat
horizon: operational
title: DragonForce abuses Microsoft Teams TURN relays for C2 and chains four vulnerable drivers (BYOVD)
headline: DragonForce abuses Microsoft Teams TURN relays for C2 and chains four vulnerable drivers (BYOVD)
summary: "DragonForce ransomware ran C2 through Microsoft Teams TURN relays — first in-the-wild abuse of Teams relay infrastructure to hide C2 in legitimate Microsoft traffic, plus a four-driver BYOVD chain; two-month dwell at a services firm (Deep Dive, § 5)."
discovered_at: "2026-06-17T05:14:36Z"
event_date: 2026-06-16
run_id: 2026-06-17-e102009c
priority: high
immediate_action: null
tags:
  - ransomware
  - organized-crime
  - identity
  - cloud
regions:
  - us
  - global
sectors:
  - technology
  - public-sector
entities:
  - "campaign:dragonforce-backdoor-turn-teams-relay-byovd"
  - "actor:dragonforce"
cves: []
sources:
  - url: "https://www.security.com/threat-intelligence/dragonforce-msteams-backdoor"
    publisher: "Symantec / Broadcom, 2026-06-16"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/ransomware-gang-abuses-microsoft-teams-relays-to-hide-malicious-traffic/"
    publisher: "BleepingComputer, 2026-06-16"
    role: corroborating
  - url: "https://www.helpnetsecurity.com/2026/06/16/dragonforce-microsoft-teams-malware-backdoor-turn/"
    publisher: "Help Net Security, 2026-06-16"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: true
deep_dive_category: ransomware-affiliate
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-17.md
---

**Background.** DragonForce is a ransomware-as-a-service operation that has been documented since 2023 and rebranded itself in 2024–2025 as a "cartel"-style affiliate model; it has been tied to attacks on retail and enterprise targets across multiple regions and has previously leaned on affiliate-supplied access and living-off-the-land tooling. This deep dive is not about the ransomware payload but about an intrusion Symantec disclosed on 2026-06-16 that introduces a genuinely novel command-and-control technique and an unusually deep bring-your-own-vulnerable-driver (BYOVD) chain ([Symantec / Broadcom, 2026-06-16](https://www.security.com/threat-intelligence/dragonforce-msteams-backdoor)).

**The intrusion.** Symantec investigated a DragonForce intrusion at an unnamed major U.S. services company that began in December 2025 — roughly two months of undetected dwell before discovery ([BleepingComputer, 2026-06-16](https://www.bleepingcomputer.com/news/security/ransomware-gang-abuses-microsoft-teams-relays-to-hide-malicious-traffic/)). Initial access was via an internet-facing MSSQL server (or purchased access) — a reminder that exposed database services remain a high-value entry point ([`T1190` Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/)). The actor then dropped a ZIP containing a legitimate, signed `DbgView64.exe` (or VirtualBox binary) alongside a malicious `vboxrt.dll`, executed via DLL side-loading ([`T1574.002`](https://attack.mitre.org/techniques/T1574/002/)). Persistence was established through a `LimitBlankPasswordUse` registry modification, creation of rogue local users/groups ([`T1136.001`](https://attack.mitre.org/techniques/T1136/001/)), and firewall-rule changes.

**Backdoor.Turn and the Teams TURN-relay C2 (the novel part).** Backdoor.Turn is a Go-based RAT injected into `DbgView64.exe`. It obtains an anonymous Microsoft Teams visitor token from Skype identity services, then establishes a TURN (Traversal Using Relays around NAT) relay session through Microsoft's own infrastructure and runs a QUIC tunnel to the actual attacker C2. Symantec assesses this is the first known malware to abuse Teams' TURN relay servers for C2 ([Symantec / Broadcom, 2026-06-16](https://www.security.com/threat-intelligence/dragonforce-msteams-backdoor)). The defensive consequence is severe: a defender inspecting network flows sees only outbound connections to legitimate Microsoft IP ranges — the technique is a high-trust proxy/relay abuse ([`T1090` Proxy](https://attack.mitre.org/techniques/T1090/)) that blends with the Teams traffic any Microsoft 365 tenant already generates.

**The four-driver BYOVD chain.** To disable defences, the actor loaded four signed-but-vulnerable kernel drivers ([`T1068` Exploitation for Privilege Escalation](https://attack.mitre.org/techniques/T1068/) used to reach kernel for [`T1562.001` Impair Defenses](https://attack.mitre.org/techniques/T1562/001/)): Huawei `HWAuidoOs2Ec.sys` (novel, no prior CVE), Topaz Antifraud `wsftprm.sys` (CVE-2023-52271), Tower of Fantasy `GameDriverx64.sys` (CVE-2025-61155), and K7 Security `K7RKScan.sys` (CVE-2025-1055). A custom malicious driver, ABYSSWORKER, masqueraded as a Palo Alto Networks driver to handle defence evasion. Follow-on activity included network scanning ([`T1046`](https://attack.mitre.org/techniques/T1046/)), AD/LDAP enumeration ([`T1018`](https://attack.mitre.org/techniques/T1018/)), TLS-certificate harvesting, browser credential theft ([`T1555.003`](https://attack.mitre.org/techniques/T1555/003/)), and credential-based lateral movement ([`T1021`](https://attack.mitre.org/techniques/T1021/)).

**Detection concepts (no IOCs).** (1) Hunt for `DbgView64.exe` or VirtualBox binaries initiating QUIC (UDP/443) sessions to Microsoft TURN-relay ranges with anomalous parent-child trees (`vboxrt.dll` → `DbgView64.exe`) — Sysmon EID 3 network-connection events filtered against expected Teams behaviour. (2) Alert on signed drivers from Huawei, Topaz, Tower of Fantasy or K7 Security loading on systems that are not gaming/AV hosts (Sysmon EID 6 driver-load). (3) Registry-value sets on `HKLM\SYSTEM\CurrentControlSet\Control\Lsa\LimitBlankPasswordUse` (Sysmon EID 13). (4) Rogue local user/group creation (Windows Security EID 4720 / 4732) ([Help Net Security, 2026-06-16](https://www.helpnetsecurity.com/2026/06/16/dragonforce-microsoft-teams-malware-backdoor-turn/)).

**Hardening.** Enforce kernel-driver allow-listing via WDAC/HVCI and keep the Microsoft vulnerable-driver blocklist current (it covers the LOLDrivers entries this chain abuses); constrain egress so UDP/443 (QUIC) to Microsoft service tags is the only permitted path and is itself monitored; and audit any internet-reachable MSSQL/SQL Server instances out of existence. Because Backdoor.Turn rides genuine Microsoft relay infrastructure, IP/domain blocking is ineffective — the leverage is process-lineage and driver-load telemetry, not network reputation.
