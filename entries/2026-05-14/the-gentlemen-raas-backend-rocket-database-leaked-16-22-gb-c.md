---
schema: 1
kind: threat
title: "The Gentlemen RaaS: leaked internal chats show Fortinet and Cisco edge access, NTLM relay, ADCS abuse and EDR-kill tooling, mapped by Check Point Research"
headline: "Leaked chats of The Gentlemen ransomware group show its edge-device access, NTLM relay and EDR-kill toolkit"
summary: "The Gentlemen ransomware-as-a-service administrator acknowledged on 2026-05-04 that the group's internal Rocket backend had leaked, and Check Point Research analysed a 44.4 MB part of a leak a seller's screenshot put at about 16.22 GB. The chats show access through Fortinet and Cisco edge devices by brute force, known vulnerabilities and bought access, NTLM relay and certificate-services abuse, tools that block EDR at start-up, ZeroPulse and Velociraptor for remote access and Cloudflare tunnels for persistence; Check Point counts about 332 leak-site victims in the first five months of 2026. A free decryptor released in April recovers files only from a memory image of the ransomware process captured while it was running."
discovered_at: "2026-05-14T05:00:04Z"
event_date: 2026-05-13
run_id: 2026-05-14-e05c6e6e
priority: high
immediate_action: null
tags:
  - ransomware
  - organized-crime
  - identity
regions:
  - europe
  - global
sectors:
  - technology
entities:
  - "actor:thegentlemen"
techniques: [T1190, T1110, T1078, T1557.001, T1649, T1685, T1003.001, T1539, T1135, T1484.001, T1572, T1219, T1490, T1486, T1657]
affected_products: []
cves: []
sources:
  - url: "https://research.checkpoint.com/2026/thus-spoke-the-gentlemen/"
    publisher: "Check Point Research"
    date: "2026-05-13"
    role: primary
  - url: "https://www.bankinfosecurity.com/tables-turned-gentlemen-ransomware-group-suffers-data-leak-a-31654"
    publisher: "BankInfoSecurity"
    date: "2026-05-11"
    role: corroborating
  - url: "https://github.com/Bedrock-Safeguard/gentlemen-decryptor"
    publisher: "Bedrock Safeguard (gentlemen-decryptor)"
    date: "2026-04-21"
    role: corroborating
closed_sources: []
evidence:
  - quote: "While the chats do not show detailed exploitation steps, the presence of this CVE alongside their FortiGate targeting suggests it is part of the set of vulnerabilities they track for potential use against exposed management interfaces."
    publisher: Check Point Research
    source_url: "https://research.checkpoint.com/2026/thus-spoke-the-gentlemen/"
  - quote: "In that case, the affiliate used SystemBC, and the associated command-and-control (C&C) server revealed more than 1,570 victims."
    publisher: Check Point Research
    source_url: "https://research.checkpoint.com/2026/thus-spoke-the-gentlemen/"
  - quote: "The compromised communications included 8,200 lines of text from an internal chat tool"
    publisher: BankInfoSecurity
    source_url: "https://www.bankinfosecurity.com/tables-turned-gentlemen-ransomware-group-suffers-data-leak-a-31654"
  - quote: "There is no master or skeleton key."
    publisher: Bedrock Safeguard
    source_url: "https://github.com/Bedrock-Safeguard/gentlemen-decryptor"
  - quote: "The keys are lost soon after the process exits."
    publisher: Bedrock Safeguard
    source_url: "https://github.com/Bedrock-Safeguard/gentlemen-decryptor"
verification: multi-source
sourcing_note: >
  Check Point Research analysed a partial copy of the leak and is the primary for the workflow, the tools and the victim
  counts; DynaRisk's analyst, quoted by BankInfoSecurity, read the leak independently and describes the same broad
  workflow; the decryptor's scope comes from Bedrock Safeguard's own repository.
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
migrated_from: briefs/2026-05-14.md
updated_at: null
updates:
  - at: "2026-10-21T20:30:42Z"
    run_id: 2026-10-21T1148Z-audit
    type: correction
    summary: >
      The free Gentlemen decryptor released in April 2026 recovers files only from a memory image of the
      ransomware process captured while it ran, has no master key and predates the leak, so trying
      decryption before negotiating does not help most victims; capturing the running locker's memory
      does. The 1,570 figure is victims of one affiliate's SystemBC server from an earlier Check Point
      investigation, not hidden ransomware victims, and the group tracks CVE-2024-55591 among other CVEs
      without the chats showing exploitation. Initial access usually runs through Fortinet and Cisco edge
      devices by brute force, known vulnerabilities and bought access, the ETW and NTDLL tampering belongs
      to the locker, and the 8,200 chat lines are DynaRisk's count.
    fields: [affected_products, body, classification, entities, evidence, headline, sources, sourcing_note, summary, techniques, title]
---

On 2026-05-04 the administrator of The Gentlemen ransomware-as-a-service programme acknowledged on underground forums that the group's internal backend database, Rocket, had leaked; a seller offered the data for 10,000 USD, and Check Point Research obtained a 44.4 MB partial copy of the internal chats while the seller's screenshot showed about 16.22 GB in total ([Check Point Research, 2026-05-13](https://research.checkpoint.com/2026/thus-spoke-the-gentlemen/)). DynaRisk's analyst counted 8,200 lines of internal chat text with timestamps largely matching Moscow working hours ([BankInfoSecurity, 2026-05-11](https://www.bankinfosecurity.com/tables-turned-gentlemen-ransomware-group-suffers-data-leak-a-31654)).

The chats describe initial access usually through exposed edge devices, with a focus on Fortinet FortiGate and Cisco, by brute-forcing web and VPN panels, exploiting known vulnerabilities and buying access; the group tracks CVE-2024-55591 in the FortiOS management interface without the chats showing exploitation steps, evaluates a proof of concept for CVE-2025-32433 in Erlang SSH, and scans domains for NTLM relay paths including CVE-2025-33073 to feed relay tooling ([Check Point Research, 2026-05-13](https://research.checkpoint.com/2026/thus-spoke-the-gentlemen/)). After access the operators seek domain administrator rights through Active Directory discovery, certificate-services abuse (enumerating ADCS misconfigurations ESC1 to ESC17) and local privilege escalation, dump LSASS and browser sessions, tamper with EDR using tools that block or delay security processes at start-up and bring-your-own-vulnerable-driver techniques, keep access through Cloudflare tunnels and the ZeroPulse and Velociraptor remote-access frameworks, and exfiltrate from NAS, backup and virtualisation systems; the administrator also announced locker upgrades that unhook NTDLL and patch ETW ([Check Point Research, 2026-05-13](https://research.checkpoint.com/2026/thus-spoke-the-gentlemen/)). DynaRisk adds that the group modified Group Policy Objects after reaching domain admin and targeted NAS, Exchange, storage and backup systems to prevent recovery ([BankInfoSecurity, 2026-05-11](https://www.bankinfosecurity.com/tables-turned-gentlemen-ransomware-group-suffers-data-leak-a-31654)).

Check Point counts about 332 victims published on the leak site in the first five months of 2026 and 412 in total, and links 29 campaigns to 8 affiliate contact IDs, including the administrator's, who also carries out infections himself; a separate, earlier Check Point investigation of one affiliate's intrusion found a SystemBC command-and-control server holding more than 1,570 victims ([Check Point Research, 2026-05-13](https://research.checkpoint.com/2026/thus-spoke-the-gentlemen/)).

**Exposure:** internet-facing Fortinet FortiGate and Cisco VPN and management interfaces, Active Directory domains where NTLM relay is possible, and certificate services with misconfigured templates are the paths the chats describe ([Check Point Research, 2026-05-13](https://research.checkpoint.com/2026/thus-spoke-the-gentlemen/)).

**Detection:** in endpoint telemetry, processes that stop EDR services from starting and user processes that patch ETW or unhook NTDLL; in directory telemetry, enumeration of ADCS templates and NTLM relay scanning; in network and host inventory, remote-access agents and Cloudflare tunnel clients IT did not deploy ([Check Point Research, 2026-05-13](https://research.checkpoint.com/2026/thus-spoke-the-gentlemen/)); in change logs, Group Policy modifications after a domain-admin compromise, and discovery sweeps of hypervisors, NAS and backup servers before encryption ([BankInfoSecurity, 2026-05-11](https://www.bankinfosecurity.com/tables-turned-gentlemen-ransomware-group-suffers-data-leak-a-31654)).

**Defender takeaway:** during an active Gentlemen incident, capture the memory of the running ransomware process (an EDR memory capture, a process dump or a full RAM image) before killing it or rebooting: the free decryptor Bedrock Safeguard released in April 2026 recovers per-file keys only from such an image, is best-effort and has no master key ([Bedrock Safeguard, 2026-04-21](https://github.com/Bedrock-Safeguard/gentlemen-decryptor)), and the group shipped a same-day patch after its release ([BankInfoSecurity, 2026-05-11](https://www.bankinfosecurity.com/tables-turned-gentlemen-ransomware-group-suffers-data-leak-a-31654)).

## Correction — 2026-10-21T20:30:42Z

The decryptor Bedrock Safeguard released in April 2026 does not let victims recover without payment in general: it extracts per-file keys from a memory image of the ransomware process captured while it was running, is best-effort and may be partial, and without such an image cannot recover files, because there is no master key ([Bedrock Safeguard, 2026-04-21](https://github.com/Bedrock-Safeguard/gentlemen-decryptor)); the group issued a same-day patch ([BankInfoSecurity, 2026-05-11](https://www.bankinfosecurity.com/tables-turned-gentlemen-ransomware-group-suffers-data-leak-a-31654)). The 1,570 figure is the victim count on one affiliate's SystemBC command-and-control server from an earlier Check Point investigation, and Check Point draws no under-reporting conclusion from it ([Check Point Research, 2026-05-13](https://research.checkpoint.com/2026/thus-spoke-the-gentlemen/)).

The chats describe initial access usually, not almost exclusively, through edge devices, by brute force, known vulnerabilities and bought access; CVE-2024-55591 is one of the CVEs the group tracks for potential use without the chats showing exploitation, no CWMP or TR-069 vector appears, ETW patching and NTDLL unhooking are locker upgrades rather than functions of the EDR-blocking tools, and the certificate-services enumeration runs through NetExec rather than certutil ([Check Point Research, 2026-05-13](https://research.checkpoint.com/2026/thus-spoke-the-gentlemen/)). The 8,200 chat lines are DynaRisk's count ([BankInfoSecurity, 2026-05-11](https://www.bankinfosecurity.com/tables-turned-gentlemen-ransomware-group-suffers-data-leak-a-31654)), and Check Point lists ZeroPulse as a remote-access framework the group uses without describing its internals ([Check Point Research, 2026-05-13](https://research.checkpoint.com/2026/thus-spoke-the-gentlemen/)).
