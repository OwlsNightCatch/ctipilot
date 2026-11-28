---
schema: 1
kind: annual-report
title: "Recorded Future's H1 2026 Malware and Vulnerability Trends: two clusters reuse an identical post-exploitation tool stack across thirteen and ten unrelated initial CVEs"
headline: "Insikt Group: the same six-tool stack followed thirteen unrelated CVEs into Exchange, SharePoint, FortiOS, Cisco IOS XE, F5 BIG-IP, GeoServer and Apache Shiro"
summary: >
  Recorded Future's Insikt Group published its H1 2026 Malware and Vulnerability Trends report on
  2026-09-03, tracking 215 actively exploited CVEs. Its most actionable defender-facing finding is
  that post-exploitation tool-stack reuse persists across otherwise-unrelated initial-access
  vulnerabilities: a cluster designated StrikeShark applied an identical six-tool stack across
  thirteen separate CVEs spanning multiple vendors, and Storm-1175 linked the same credential-theft
  and ransomware tooling across ten different initial CVEs.
discovered_at: "2026-09-07T04:43:00Z"
updated_at: null
event_date: "2026-09-03"
run_id: 2026-09-07T0411Z-intel
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - ransomware
  - organized-crime
regions:
  - global
sectors: []
entities:
  - "report:recordedfuture-h1-2026-malware-vulnerability-trends"
  - "campaign:strikeshark-sharkloader"
  - "actor:storm-1175"
  - "actor:shadow-earth-053"
techniques:
  - T1190
  - T1059.001
  - T1059.003
  - T1059.004
  - T1505.003
  - T1071.001
  - T1105
  - T1082
  - T1005
  - T1041
affected_products:
  - "Microsoft Exchange Server"
  - "Microsoft SharePoint"
  - "Fortinet FortiOS"
  - "Cisco IOS XE"
  - "F5 BIG-IP"
  - "GeoServer"
  - "Apache Shiro"
cves: []
sources:
  - url: "https://www.recordedfuture.com/research/h1-2026-malware-vulnerability-trends"
    publisher: "Recorded Future (Insikt Group)"
    date: "2026-09-03"
    role: primary
  - url: "https://securelist.com/strikeshark-campaign/120326/"
    publisher: "Kaspersky Securelist (GReAT)"
    date: "2026-06-24"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Threat actors reused post-exploitation playbooks across different initial vulnerabilities; StrikeShark applied the same six-tool stack across thirteen CVEs, while Storm-1175 linked credential theft, remote execution, data transfer, and ransomware tooling across ten."
    publisher: "Recorded Future (Insikt Group)"
  - quote: "In the StrikeShark campaign, SharkLoader, Cobalt Strike Beacon, FScan, Searchall, Pillager Stealer, and SharpGPOAbuse were linked to the same thirteen CVEs. Those vulnerabilities spanned 2016 through 2025 and affected Microsoft Exchange and SharePoint, Fortinet FortiOS, Cisco IOS XE, F5 BIG-IP, GeoServer, Apache Shiro, and other public-facing technologies."
    publisher: "Recorded Future (Insikt Group)"
  - quote: "50 of the 77 CVEs associated with the exploitation of public-facing applications were also linked to PowerShell, Windows Command Shell, or Unix Shell, and all 28 web-shell-associated CVEs also included T1190."
    publisher: "Recorded Future (Insikt Group)"
verification: single-source
sourcing_note: >
  Single vendor threat-intelligence report; no independent lab has separately corroborated the
  specific tool-stack-reuse figures. Recorded Future is a large, established threat-intelligence
  vendor with a consistent editorial and analytic track record.
confidence: medium
references:
  - "2026-06-27/kaspersky-great-strikeshark-loader-deploys-cobalt-strike-via"
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

Recorded Future's Insikt Group published its H1 2026 Malware and Vulnerability Trends report on 3 September 2026, tracking 215 actively exploited CVEs in the first half of 2026 — up 34% from 161 in H1 2025 ([Recorded Future, 2026-09-03](https://www.recordedfuture.com/research/h1-2026-malware-vulnerability-trends)). Of those, 176 (82%) were network-accessible and 146 (68%) could be exploited without prior authentication; 142 of those 146 combined both properties, and 60 of 82 remote-code-execution CVEs combined network reachability, no authentication requirement and code execution in a single package ([Recorded Future, 2026-09-03](https://www.recordedfuture.com/research/h1-2026-malware-vulnerability-trends)).

The report's most actionable finding for defenders is that post-exploitation tool-stack reuse persists across otherwise-unrelated initial-access vulnerabilities, regardless of vendor or product family ([Recorded Future, 2026-09-03](https://www.recordedfuture.com/research/h1-2026-malware-vulnerability-trends)). A cluster the report designates StrikeShark applied an identical six-tool post-exploitation stack — SharkLoader, Cobalt Strike Beacon, FScan, Searchall, Pillager Stealer and SharpGPOAbuse — across thirteen separate CVEs spanning 2016 through 2025, reaching Microsoft Exchange, Microsoft SharePoint, Fortinet FortiOS, Cisco IOS XE, F5 BIG-IP, GeoServer and Apache Shiro ([Recorded Future, 2026-09-03](https://www.recordedfuture.com/research/h1-2026-malware-vulnerability-trends)); SharkLoader itself was previously profiled by Kaspersky's GReAT, which found it deploying Cobalt Strike via "Perfect DLL Hijacking" in a campaign whose confirmed victims spanned government and diplomatic entities, software developers and organizations in several other sectors and regions ([Kaspersky Securelist, 2026-06-24](https://securelist.com/strikeshark-campaign/120326/)). Separately, Storm-1175 linked Mimikatz, Impacket, PsExec, Rclone and Medusa ransomware across ten different initial CVEs; a China-linked cluster the report designates SHADOW-EARTH-053 separately reused Mimikatz following exploitation of CVE-2021-26855 in Microsoft Exchange Server ([Recorded Future, 2026-09-03](https://www.recordedfuture.com/research/h1-2026-malware-vulnerability-trends)). Insikt Group mapped 114 of the 215 CVEs to MITRE ATT&CK: exploitation of a public-facing application was associated with 77 CVEs (68%), and 50 of those 77 also co-occurred with PowerShell, Windows Command Shell or Unix Shell execution; every one of the 28 web-shell-associated CVEs also carried the public-facing-application technique. The next most frequently associated post-exploitation behaviors across the mapped CVEs were system-information discovery, collection of data from the local system, transfer of further tooling into the compromised environment, and exfiltration over the command-and-control channel or web-protocol-based C2 traffic ([Recorded Future, 2026-09-03](https://www.recordedfuture.com/research/h1-2026-malware-vulnerability-trends)).

The report's own defender-facing conclusion is explicit: because the same limited tool stack recurs regardless of which vulnerability supplied the initial foothold, detection engineering should chain exploitation telemetry from public-facing systems through to the post-exploitation behaviors these clusters repeat — credential dumping, remote-service execution via native administration mechanisms, bulk outbound data transfer, and ransomware staging — rather than treating each CVE alert as an isolated, one-off event ([Recorded Future, 2026-09-03](https://www.recordedfuture.com/research/h1-2026-malware-vulnerability-trends)).

**Defender takeaway:** exposure and impact are more informative indicators of operational risk from a newly disclosed CVE than vendor ranking or CVSS score alone, because the tooling an attacker deploys after gaining a foothold is frequently recycled across unrelated products. A detection strategy built around a specific CVE's exploit signature misses this: chaining exploitation telemetry from any public-facing application to subsequent credential-access, remote-execution and bulk-transfer activity catches the repeated post-exploitation pattern regardless of which initial flaw was used.
