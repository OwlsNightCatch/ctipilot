---
schema: 1
kind: threat
title: "Longlegs (Storm-2603), the developer of Warlock ransomware, still enters through on-premises SharePoint: a water utility, a telecom, a regional government body and a university hit in two months"
headline: "Symantec: Warlock's operator steals SharePoint machine keys, forges signed payloads and ships ransomware via SYSVOL"
summary: >
  Symantec reports that Longlegs (also known as Storm-2603), the China-nexus developer of Warlock ransomware, attacked at
  least four organizations in two months, a water utility, a telecommunications provider, a regional government body and a
  university in Portuguese- and Spanish-speaking countries, and still gets in through on-premises SharePoint Server. In the
  intrusion Symantec walks through, a web shell harvested the farm's ASP.NET machine keys to forge signed payloads, a
  security-tool killer ran on at least 40 hosts in about two hours, and Warlock reached at least 33 hosts through SYSVOL
  replication.
discovered_at: "2026-10-03T04:41:00Z"
updated_at: null
event_date: "2026-10-01"
run_id: 2026-10-03T0404Z-intel
priority: high
immediate_action: null
tags: [ransomware, china-nexus]
regions: [europe, africa, latam]
sectors: [public-sector, water, telco, education]
entities: ["actor:warlock-storm-2603"]
techniques: [T1190, T1505.003, T1059.001, T1059.003, T1574.001, T1105, T1218.007, T1482, T1087.002, T1098, T1036.010, T1110.003, T1570, T1219.001, T1685, T1486]
affected_products: ["Microsoft SharePoint Server"]
cves: []
sources:
  - url: "https://www.security.com/threat-intelligence/warlock-ransomware-critical-infrastructure"
    publisher: "Symantec Threat Hunter Team / Carbon Black"
    date: "2026-10-01"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/warlock-ransomware-breach-sharepoint-in-water-telecom-operator-attacks/"
    publisher: "BleepingComputer"
    date: "2026-10-02"
    role: corroborating
  - url: "https://www.microsoft.com/en-us/security/blog/2025/07/22/disrupting-active-exploitation-of-on-premises-sharepoint-vulnerabilities/"
    publisher: "Microsoft Security Blog"
    date: "2025-07-22"
    role: corroborating
closed_sources: []
evidence:
  - quote: "In the past two months, Longlegs has attacked at least four organizations, including two critical infrastructure operators (a water utility and a telecommunications provider), a regional government body, and a university."
    publisher: "Symantec Threat Hunter Team / Carbon Black"
    source_url: "https://www.security.com/threat-intelligence/warlock-ransomware-critical-infrastructure"
  - quote: "The webshell's function is to harvest the SharePoint farm's ASP.NET machine keys, which the attackers then use to forge a validly signed payload that achieves remote code execution inside the SharePoint application pool."
    publisher: "Symantec Threat Hunter Team / Carbon Black"
    source_url: "https://www.security.com/threat-intelligence/warlock-ransomware-critical-infrastructure"
  - quote: "In one intrusion against a critical infrastructure operator, the attackers pushed a tool designed to disable security software to at least 40 hosts within about two hours, then deployed Warlock on at least 33 hosts by staging it in the domain's SYSVOL share, where ordinary domain replication delivered it to machines."
    publisher: "Symantec Threat Hunter Team / Carbon Black"
    source_url: "https://www.security.com/threat-intelligence/warlock-ransomware-critical-infrastructure"
verification: single-source
sourcing_note: >
  Symantec and Carbon Black are the only assessor; BleepingComputer relays their report. The equivalence of Longlegs and
  Storm-2603 and the four recent victims are Symantec's statements, and Symantec names no victim.
confidence: medium
references:
  - 2026-08-05/bit-foitt-swiss-federal-sharepoint-breach-200-accounts
  - 2026-08-06/canton-graubuenden-sharepoint-server-breach
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "On every on-premises SharePoint Server farm that was reachable from the internet while unpatched, patch it and then rotate the ASP.NET machine keys and restart IIS on all SharePoint servers, as Microsoft's ToolShell guidance says, and look for unexpected .aspx files in the LAYOUTS template directories of every installed SharePoint version and for domain accounts named like SharePoint setup accounts in local Administrators groups."
updates: []
migrated_from: null
---

Symantec reports that Longlegs, also known as Storm-2603, develops the Warlock ransomware and attacked at least four organizations in two months: a water utility, a telecommunications provider, a regional government body and a university, in Portuguese- and Spanish-speaking countries ([Symantec, 2026-10-01](https://www.security.com/threat-intelligence/warlock-ransomware-critical-infrastructure)). Symantec says the group typically enters through on-premises SharePoint Server, and that the 2025 ToolShell flaws (CVE-2025-49704, CVE-2025-49706, CVE-2025-53770 and CVE-2025-53771) likely remain in its arsenal alongside newer SharePoint flaws ([Symantec, 2026-10-01](https://www.security.com/threat-intelligence/warlock-ransomware-critical-infrastructure)); BleepingComputer relays the report ([BleepingComputer, 2026-10-02](https://www.bleepingcomputer.com/news/security/warlock-ransomware-breach-sharepoint-in-water-telecom-operator-attacks/)).

In the intrusion Symantec walks through, the likely entry was SharePoint exploitation, and on 2026-07-22 PowerShell wrote a web shell into the SharePoint LAYOUTS template directory ([Symantec, 2026-10-01](https://www.security.com/threat-intelligence/warlock-ransomware-critical-infrastructure)). The group drops one into the directories of several SharePoint versions at once; it harvests the farm's ASP.NET machine keys, which the attackers use to forge a validly signed payload that runs code in the SharePoint application pool ([Symantec, 2026-10-01](https://www.security.com/threat-intelligence/warlock-ransomware-critical-infrastructure)). From 2026-07-28 PowerShell commands loading the System.Workflow.ComponentModel assembly, the deserialization gadget behind the forged payload, ran at intervals ([Symantec, 2026-10-01](https://www.security.com/threat-intelligence/warlock-ransomware-critical-infrastructure)). The attackers also used DLL sideloading, fetched installers with msiexec from legitimate cloud file-sharing services, enumerated domain accounts and trusts, added a setup-lookalike domain account to local Administrators on three more hosts, installed Visual Studio Code Insiders as a tunnel service, and ran NetExec for enumeration, credential spraying and remote execution ([Symantec, 2026-10-01](https://www.security.com/threat-intelligence/warlock-ransomware-critical-infrastructure)).

On 2026-07-31 a security-tool killer, pushed with one-line commands that copied a tool set from an internal share, ran on at least 40 hosts in about two hours; its driver is unknown, but in other recent attacks the group used the signed K7RKScan driver (CVE-2025-1055) ([Symantec, 2026-10-01](https://www.security.com/threat-intelligence/warlock-ransomware-critical-infrastructure)). Warlock then ran on at least 33 hosts from the domain's SYSVOL scripts share, with the DFS Replication service (dfsrs.exe) as the parent on three hosts, so SYSVOL replication delivered the payload ([Symantec, 2026-10-01](https://www.security.com/threat-intelligence/warlock-ransomware-critical-infrastructure)).

**Exposure:** on-premises SharePoint Server farms reachable from the internet or from an attacker's foothold that were unpatched against the ToolShell and later flaws; Symantec gives no version table ([Symantec, 2026-10-01](https://www.security.com/threat-intelligence/warlock-ransomware-critical-infrastructure)). Because the web shell takes the machine keys, patching alone does not replace them; Microsoft's ToolShell guidance says it is critical to rotate the machine keys and restart IIS on all SharePoint servers ([Microsoft, 2025-07-22](https://www.microsoft.com/en-us/security/blog/2025/07/22/disrupting-active-exploitation-of-on-premises-sharepoint-vulnerabilities/)).

**Detection:** new .aspx files written by PowerShell in the SharePoint LAYOUTS directories; PowerShell on SharePoint hosts loading System.Workflow.ComponentModel at intervals; msiexec silent installs from cloud file-sharing URLs; outbound requests to out-of-band interaction hosts carrying the target's domain; a domain account added to local Administrators on several hosts; a service installed from code-insiders.exe with the tunnel option from the Windows debug folder; security-tool termination across dozens of hosts, then executables run from a SYSVOL scripts path with dfsrs.exe as parent ([Symantec, 2026-10-01](https://www.security.com/threat-intelligence/warlock-ransomware-critical-infrastructure)).

**Triage:** Visual Studio Code tunnels are ordinary on developer workstations; the observed pattern is a service installed from a system folder on a host in a domain already showing SharePoint exploitation or an unexpected administrator account ([Symantec, 2026-10-01](https://www.security.com/threat-intelligence/warlock-ransomware-critical-infrastructure)).

**Defender takeaway:** treat every on-premises SharePoint farm that was reachable while unpatched as a candidate for compromise assessment: look for the web shell and for setup-lookalike accounts in local Administrators ([Symantec, 2026-10-01](https://www.security.com/threat-intelligence/warlock-ransomware-critical-infrastructure)), and, once patched, rotate the machine keys and restart IIS on all SharePoint servers as Microsoft's ToolShell guidance says ([Microsoft, 2025-07-22](https://www.microsoft.com/en-us/security/blog/2025/07/22/disrupting-active-exploitation-of-on-premises-sharepoint-vulnerabilities/)); in Active Directory domains, watch SYSVOL scripts paths for executables ([Symantec, 2026-10-01](https://www.security.com/threat-intelligence/warlock-ransomware-critical-infrastructure)).
