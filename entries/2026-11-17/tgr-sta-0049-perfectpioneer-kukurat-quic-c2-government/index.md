---
schema: 1
kind: threat
title: "TGR-STA-0049: Unit 42 describes the PerfectPioneer and KUKURAT implants, which use HTTP/3 over QUIC for command and control against government networks entered through unpatched Exchange servers, then spread through domain logon scripts and grant FullAccess on every mailbox"
headline: "Unit 42: TGR-STA-0049 uses QUIC C2, logon-script spread and Exchange FullAccess loops against governments"
summary: >
  Unit 42 reports that TGR-STA-0049 (also tracked as REF7707, Earth Alux and Ink Dragon) has attacked Southeast Asian government entities since at least July 2025, entering through unpatched Exchange and web servers, and says the group's targeting also includes governments in South America and Europe. Its new PerfectPioneer and KUKURAT implants use HTTP/3 over QUIC as the main command channel in most variants, the operators spread KUKURAT through domain logon scripts after taking a domain controller, and on Exchange they grant a compromised account FullAccess on every mailbox.
discovered_at: "2026-11-17T04:40:30Z"
updated_at: null
event_date: "2026-11-16"
run_id: 2026-11-17T0355Z-intel
priority: notable
immediate_action: null
tags: [espionage, nation-state]
regions: [apac, europe, latam]
sectors: [public-sector]
entities: ["actor:jewelbug", "malware:perfectpioneer-rat", "malware:kukurat"]
techniques: [T1190, T1505.003, T1566, T1574.001, T1071.001, T1037.003, T1003.001, T1218.011, T1003.006, T1003.002, T1569.002, T1047, T1021.006, T1098.002, T1041, T1005]
affected_products: ["Microsoft Exchange Server"]
cves: []
sources:
  - url: "https://unit42.paloaltonetworks.com/custom-rats-target-southeast-asia-governments/"
    publisher: "Palo Alto Networks Unit 42"
    date: "2026-11-16"
    role: primary
closed_sources: []
evidence:
  - quote: "the exploitation of vulnerable, unpatched Microsoft Exchange servers and web servers to deploy web shells"
    publisher: "Palo Alto Networks Unit 42"
    source_url: "https://unit42.paloaltonetworks.com/custom-rats-target-southeast-asia-governments/"
  - quote: "PerfectPioneer RAT relies on HTTP/3 as its primary C2 communication mechanism, automatically falling back to HTTP/2 in the event of connection failure."
    publisher: "Palo Alto Networks Unit 42"
    source_url: "https://unit42.paloaltonetworks.com/custom-rats-target-southeast-asia-governments/"
  - quote: "Instead of calling the MiniDump function by name, the attackers invoked it via its ordinal hidden index number, #+000024."
    publisher: "Palo Alto Networks Unit 42"
    source_url: "https://unit42.paloaltonetworks.com/custom-rats-target-southeast-asia-governments/"
verification: single-source
sourcing_note: >
  Unit 42 holds the incident-response telemetry and is the only source; it names no victim organisation and no vulnerability identifier for the Exchange and web-server entry, and it does not mention Jewelbug, whose REF7707 and Earth Alux names Symantec's cluster shares with Unit 42's alias list.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

Unit 42 describes a campaign by TGR-STA-0049, also tracked as REF7707, Earth Alux and Ink Dragon, against Southeast Asian government entities since at least July 2025, and says the group's targeting also includes government organizations in South America and Europe ([Unit 42, 2026-11-16](https://unit42.paloaltonetworks.com/custom-rats-target-southeast-asia-governments/)). Server exploitation is the primary entry: unpatched Microsoft Exchange and web servers receive web shells, among them variants of ASPXSpy, Godzilla, Bysunue.aspx and Suo5, while phishing with decoy PDFs from lookalike government domains is secondary ([Unit 42, 2026-11-16](https://unit42.paloaltonetworks.com/custom-rats-target-southeast-asia-governments/)). The implants are two previously undocumented families: the Go-based PerfectPioneer RAT, active since July 2025 and run through DLL side-loading of a modified legitimate executable, decoy installers or phishing, and its modular C++ successor KUKURAT, deployed since March 2026, which loads at least 12 DLL modules from the command server into memory ([Unit 42, 2026-11-16](https://unit42.paloaltonetworks.com/custom-rats-target-southeast-asia-governments/)). Unit 42 says both families use HTTP/3 over QUIC as the primary command channel, with an automatic HTTP/2 fallback in the PerfectPioneer variant it analyzes, separate HTTP/2 and HTTP/3 builds of KUKURAT, and two PerfectPioneer variants, RatAAkk-tt and PerfectRat, that rely on HTTP/2 alone, and that some firewalls and inspection engines handle QUIC less well than TCP traffic ([Unit 42, 2026-11-16](https://unit42.paloaltonetworks.com/custom-rats-target-southeast-asia-governments/)). Two of the six PerfectPioneer variants, Pioneer and rat_http3_cc, carry a built-in blocklist that stops operators running noisy or destructive commands, and KUKURAT generates synthetic network, registry and file activity as camouflage ([Unit 42, 2026-11-16](https://unit42.paloaltonetworks.com/custom-rats-target-southeast-asia-governments/)).

After taking a domain controller, the operators installed malicious domain logon scripts, so each user's logon pulled KUKURAT; they also used PsExec, WMI and WinRM ([Unit 42, 2026-11-16](https://unit42.paloaltonetworks.com/custom-rats-target-southeast-asia-governments/)). Credentials came from LSASS dumps taken with rundll32 calling comsvcs.dll by ordinal rather than by the MiniDump name, from DCSync, and from Mimikatz, ProcDump, SharpDPAPI and SAM and SYSTEM hive dumps ([Unit 42, 2026-11-16](https://unit42.paloaltonetworks.com/custom-rats-target-southeast-asia-governments/)). On Exchange, the operators first listed accounts holding the ApplicationImpersonation role and, when none was found, ran a hidden PowerShell loop that granted a compromised account FullAccess on every mailbox ([Unit 42, 2026-11-16](https://unit42.paloaltonetworks.com/custom-rats-target-southeast-asia-governments/)). The exfiltration targeted pdf, docx, xlsx and png files whose names suggest international relations and internal political affairs ([Unit 42, 2026-11-16](https://unit42.paloaltonetworks.com/custom-rats-target-southeast-asia-governments/)).

**Exposure:** on-premises Exchange and other web servers that are unpatched and internet-facing, and Active Directory domains in which an attacker with domain controller access can edit logon scripts in SYSVOL or Group Policy.

**Detection:** egress telemetry for outbound UDP 443 (QUIC) from servers that do not browse, since Unit 42 advises logging or blocking it so traffic falls back to TCP, paired with proxy and TLS egress telemetry because the HTTP/2-only variants and the KUKURAT HTTP/2 build never use UDP 443; SYSVOL and Group Policy change audit plus endpoint alerts on an uncommon startup process running under a domain user SID at logon, which raised an alert in Unit 42's telemetry; process events for rundll32 loading comsvcs.dll with an ordinal argument; and Exchange audit of ApplicationImpersonation role holders and of Add-MailboxPermission loops that grant FullAccess across all mailboxes ([Unit 42, 2026-11-16](https://unit42.paloaltonetworks.com/custom-rats-target-southeast-asia-governments/)).

**Defender takeaway:** patch or isolate internet-facing Exchange and web servers first, then check domain logon scripts, ApplicationImpersonation holders and mailbox permissions, and decide whether servers need outbound UDP 443 at all.
