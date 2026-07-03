---
schema: 1
kind: threat
horizon: operational
title: Calypso/Red Lamassu (Bronze Medley) deploys Showboat (Linux) and JFMBackdoor (Windows) against telecoms — new implant pair disclosed by Lumen Black Lotus Labs and PwC Threat Intelligence
headline: Calypso/Red Lamassu (Bronze Medley) deploys Showboat (Linux) and JFMBackdoor (Windows) against telecoms — new implant pair disclosed by Lumen Black Lotus Labs
summary: "Calypso/Red Lamassu deploys Showboat (Linux) + JFMBackdoor (Windows) against telecoms — multi-year Chinese espionage campaign targeting ISPs in Middle East, Central Asia; kworker-masquerading ELF implant with SOCKS5 proxy and Pastebin dead-drop rootkit loader; Lumen Black Lotus Labs + PwC joint disclosure (BleepingComputer, 2026-05-21)."
discovered_at: "2026-05-22T05:00:01Z"
event_date: 2026-05-21
run_id: 2026-05-22-5b90d5a1
priority: high
immediate_action: null
tags:
  - nation-state
  - espionage
  - china-nexus
regions:
  - europe
  - middle-east
  - apac
sectors:
  - telco
entities:
  - "campaign:calypso-red-lamassu-showboat-jfmbackdoor-linux-windows-telco"
cves: []
sources:
  - url: "https://www.lumen.com/blog/en-us/introducing-showboat-a-new-malware-family-taunts-defenses-and-targets-international-telecom-firms"
    publisher: "Lumen Black Lotus Labs, 2026-05-21"
    role: primary
  - url: "https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/red-lamassu-open-season.html"
    publisher: "PwC Threat Intelligence, 2026-05-21"
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/chinese-hackers-target-telcos-with-new-linux-windows-malware/"
    publisher: "BleepingComputer, 2026-05-21"
    role: corroborating
  - url: "https://thehackernews.com/2026/05/showboat-linux-malware-hits-middle-east.html"
    publisher: "The Hacker News, 2026-05-21"
    role: corroborating
closed_sources: []
evidence: []
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
migrated_from: briefs/2026-05-22.md
---

Lumen's Black Lotus Labs and PwC Threat Intelligence disclosed on 2026-05-21 two purpose-built implants used by the China-aligned espionage cluster Calypso (also tracked as Red Lamassu, Bronze Medley — active since at least mid-2022 based on binary upload and victim telemetry) in a multi-year campaign against telecommunications providers ([Lumen Black Lotus Labs, 2026-05-21](https://www.lumen.com/blog/en-us/introducing-showboat-a-new-malware-family-taunts-defenses-and-targets-international-telecom-firms) · [PwC Threat Intelligence, 2026-05-21](https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/red-lamassu-open-season.html)). Confirmed victims include a Middle East ISP, an Afghanistan ISP, and entities in Azerbaijan, the US, and Ukraine; European telecoms are within the actor's documented targeting pattern. Showboat is a modular ELF binary masquerading as a Linux kernel worker thread (`kworker` — `T1036.005 Masquerade: Match Legitimate Name`) providing remote shell (`T1059.004`), bidirectional file transfer, SOCKS5 proxy to internal network segments (`T1090.001 Internal Proxy`), and a `hide` command that fetches a rootkit payload from Pastebin at runtime (`T1102.001 Dead Drop Resolver`) — the C2 payload is exfiltrated base64-encoded inside PNG image fields to blend with web traffic ([Lumen Black Lotus Labs, 2026-05-21](https://www.lumen.com/blog/en-us/introducing-showboat-a-new-malware-family-taunts-defenses-and-targets-international-telecom-firms)). JFMBackdoor, the Windows counterpart, is delivered via DLL sideloading (`T1574.002`): a batch script drops a legitimate signed executable that loads the malicious DLL, providing remote shell, file operations, SOCKS5 proxy, and self-removal ([PwC Threat Intelligence, 2026-05-21](https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/red-lamassu-open-season.html)). C2 infrastructure clusters to Chengdu, Sichuan-geolocated IP ranges; X.509 certificate SAN/CN patterns link the victim set ([Lumen Black Lotus Labs, 2026-05-21](https://www.lumen.com/blog/en-us/introducing-showboat-a-new-malware-family-taunts-defenses-and-targets-international-telecom-firms)). Detection: hunt for `kworker` ELF processes whose parent is not `kthreadd` (PID 2) on Linux telecom servers (auditd EXECVE or Sysmon for Linux EID 1 parent-pid check); alert on unsigned DLLs loaded by vendor-signed executables (Sysmon EID 7: signed process, unsigned module); flag egress DNS queries or HTTP GET to pastebin.com from daemon-context processes.
