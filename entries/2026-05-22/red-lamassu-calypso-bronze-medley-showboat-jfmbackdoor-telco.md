---
schema: 1
kind: threat
horizon: operational
title: "Red Lamassu (Calypso/Bronze Medley): Showboat + JFMBackdoor telco espionage implant pair"
headline: "Red Lamassu (Calypso/Bronze Medley): Showboat + JFMBackdoor telco espionage implant pair"
summary: "Background. Calypso (also tracked as Red Lamassu and Bronze Medley) is a China-aligned espionage cluster active since at least mid-2022 based on Lumen's binary upload and victim telemetry — the Showboat/JFMBackdoor campaign dates to this period."
discovered_at: "2026-05-22T05:00:09Z"
event_date: 2026-05-21
run_id: 2026-05-22-5b90d5a1
priority: notable
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
entities: []
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
deep_dive: true
deep_dive_category: other
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-22.md
---

**Background.** Calypso (also tracked as Red Lamassu and Bronze Medley) is a China-aligned espionage cluster active since at least mid-2022 based on Lumen's binary upload and victim telemetry — the Showboat/JFMBackdoor campaign dates to this period. The group has previously been linked to intrusions against government entities, energy companies, and telecommunications operators in Central Asia, South Asia, and the Middle East using commodity and bespoke tooling including PlugX and ShadowPad variants. Lumen Black Lotus Labs and PwC Threat Intelligence disclosed the Showboat/JFMBackdoor toolset on 2026-05-21 based on infrastructure analysis, binary upload telemetry, and victim telemetry ([Lumen Black Lotus Labs, 2026-05-21](https://www.lumen.com/blog/en-us/introducing-showboat-a-new-malware-family-taunts-defenses-and-targets-international-telecom-firms) · [PwC Threat Intelligence, 2026-05-21](https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/red-lamassu-open-season.html)).

**Linux implant: Showboat.** Showboat is a modular post-exploitation ELF binary. On disk, the process name is `kworker`, directly impersonating Linux kernel worker threads to evade basic process-list inspection (`T1036.005 Masquerade: Match Legitimate Name or Location`). The implant contacts its C2 server, collects basic system information, and encodes the beacon data as Base64 inside PNG image field bytes — blending C2 beaconing with image-format traffic (`T1001.002 Steganography`). Functional modules provide: (1) **remote shell** (`T1059.004 Unix Shell`); (2) **bidirectional file transfer**; (3) **SOCKS5 proxy and port-forwarding** (`T1090.001 Internal Proxy`) — enabling the attacker to tunnel through the compromised telecom server into internal network segments without direct external access to those targets; (4) a `hide` command that fetches a rootkit payload from a Pastebin or forum-style dead-drop at runtime (`T1102.001 Dead Drop Resolver`), pulling additional capability after initial deployment rather than shipping it on disk. C2 infrastructure is geolocated to Chengdu, Sichuan province, consistent with prior Calypso campaigns. X.509 certificate SAN/CN clustering links the campaign's confirmed victim set.

**Windows implant: JFMBackdoor.** JFMBackdoor is delivered via DLL sideloading (`T1574.002 Hijack Execution Flow: DLL Side-Loading`): a batch script drops a legitimate vendor-signed executable alongside a malicious DLL in a writable path; the signed binary loads the DLL, providing the attacker with remote shell, file operations, SOCKS5 proxy, screenshot capture, and self-removal capability. The use of a vendor-signed loader binary defeats application allowlisting based on signing alone.

**Kill-chain pattern.** Initial access vector is not publicly confirmed; the long-running nature (mid-2022 to 2026) and focus on network-exposed telecom infrastructure suggest exploitation of public-facing services (`T1190`) or credential-based entry. Post-access, Showboat provides the persistent Linux bridgehead; from there SOCKS5 tunnels are used for lateral movement into internal segments (`T1090.001`). Data collection via `T1560 Archive Collected Data` and exfiltration via the C2 covert channel completes the chain.

**Detection for EU/telco SOCs.** (1) Linux: `kworker` processes whose parent is not `kthreadd` (PID 2) are anomalous — legitimate kernel workers are exclusively children of `kthreadd`; any `kworker`-named process with a user-space parent (e.g., bash, sshd, any application binary) is high-confidence suspicious. Enumerate via auditd EXECVE rules or Sysmon for Linux EID 1 with parent-pid cross-check. (2) Linux: SOCKS5 connection establishment from application-layer daemon processes (not expected proxy services) to non-standard ports is a lateral-movement pivot indicator. (3) Linux: DNS queries or HTTP GET to `pastebin.com` from processes running as root or as non-web-facing service accounts are anomalous — no production daemon should be fetching Pastebin content. (4) Windows: Sysmon EID 7 (ImageLoad) showing a signed process binary loading an unsigned DLL from a writable user-controlled path (e.g., AppData, Temp, or any path not under `%SystemRoot%`) warrants investigation. (5) Network: X.509 certificate attribute hunting against the Chengdu IP ranges described by Lumen Black Lotus Labs; if your threat-intel platform supports cert-fingerprint or SAN searches, use the campaign's known certificate clustering pattern as a pivot.

**Hardening.** On Linux telecom servers: (a) enforce process-name uniqueness checks via auditd rules that alert on EXECVE where `comm` matches `kworker` but `ppid` != 2; (b) egress-filter server processes to block outbound connections to hosting services (Pastebin, paste sites, general code-hosting) from root-context processes. On Windows: (c) require DLL signature enforcement via Windows Defender Application Control (WDAC) `RequireSignedCode` policy; (d) restrict writable paths in the DLL search order through AppLocker or WDAC deny-list rules on `AppData\Roaming`, `Temp`, and user-writable directories. Across the estate: (e) enforce strict outbound firewall rules on telecom infrastructure servers limiting egress to known management and update destinations.
