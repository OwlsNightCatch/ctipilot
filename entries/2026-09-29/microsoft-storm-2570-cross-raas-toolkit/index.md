---
schema: 1
kind: threat
title: "Storm-2570: a ransomware affiliate reuses a consistent commodity RMM/tunnelling/credential-theft toolkit across four separate RaaS brands, with government agencies among its confirmed victims"
headline: "Microsoft: the same toolkit rides into victims regardless of which ransomware brand signs the note"
summary: >
  Microsoft Threat Intelligence profiles Storm-2570, a ransomware affiliate active since April 2025 that
  deploys Qilin, DragonForce, Anubis and BERT payloads interchangeably while reusing a consistent
  MeshAgent/RMM-tunnelling/NTDS.dit-theft toolchain regardless of the final brand. Confirmed victims span
  healthcare, education, government agencies and services, financial services, energy, retail, IT and
  food/agriculture across the US, Canada, UK, Spain, Netherlands and Puerto Rico.
discovered_at: "2026-09-29T04:55:00Z"
updated_at: null
event_date: "2026-09-24"
run_id: 2026-09-29T0405Z-intel
priority: high
immediate_action: null
tags: [ransomware, organized-crime]
regions: [global, us, europe]
sectors: [public-sector, healthcare, education, energy, finance, retail]
entities: ["actor:storm-2570", "actor:qilin", "actor:dragonforce", "actor:anubis-raas", "actor:bert-raas"]
techniques: [T1219, T1572, T1046, T1003.003, T1003.001, T1555, T1685, T1021.001, T1570, T1569.002, T1567.002]
affected_products: []
cves: []
sources:
  - url: "https://www.microsoft.com/en-us/security/blog/2026/09/24/beyond-ransomware-tracking-storm-2570-consistent-tradecraft-across-deployments/"
    publisher: "Microsoft Security Blog / Microsoft Threat Intelligence"
    date: "2026-09-24"
    role: primary
closed_sources: []
evidence:
  - quote: "Microsoft Threat Intelligence has observed Storm-2570 in multiple investigated intrusions affecting organizations in United States, Canada, United Kingdom, Spain, Netherlands, and Puerto Rico, including healthcare and public health, education, government agencies and services, financial services, energy, consumer retail, Information technology (IT), food and agriculture, consumer services, commercial facilities, non-government organization (NGO), chemicals, critical manufacturing, and transportation."
    publisher: "Microsoft Security Blog / Microsoft Threat Intelligence"
    source_url: "https://www.microsoft.com/en-us/security/blog/2026/09/24/beyond-ransomware-tracking-storm-2570-consistent-tradecraft-across-deployments/"
verification: single-source
sourcing_note: >
  Single-sourced to Microsoft's own XDR-telemetry-based threat-intelligence blog (Admiralty B, original
  vendor research). Microsoft is the party positioned to correlate this cross-RaaS affiliate behavior from
  its own endpoint telemetry; no independent second source describing the identical cross-brand correlation
  was found.
confidence: high
references: ["2026-09-21/qilin-ai-generated-wiper-locker-scripts-forensic-markers"]
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

Microsoft Threat Intelligence profiles Storm-2570, a ransomware affiliate it has tracked since April 2025 that operates across multiple ransomware-as-a-service ecosystems rather than committing to one brand, deploying Qilin, DragonForce, Anubis and BERT payloads interchangeably against victims in healthcare, education, government agencies and services, financial services, energy, retail, IT and food/agriculture across the US, Canada, UK, Spain, the Netherlands and Puerto Rico ([Microsoft Security Blog, 2026-09-24](https://www.microsoft.com/en-us/security/blog/2026/09/24/beyond-ransomware-tracking-storm-2570-consistent-tradecraft-across-deployments/)). Post-compromise, the affiliate routinely conducts internal network discovery using NetScan, SoftPerfect Network Scanner Portable and Nmap alongside native discovery commands and file-searching activity, to identify reachable hosts and services, map internal networks and locate systems, shares and files of interest ahead of credential access or encryption. Regardless of the final ransomware brand, Microsoft describes a recurring commodity toolchain across deployments: MeshAgent/MeshCentral, frequently renamed per-victim (for example `meshagent64-[org].exe`) and one of the affiliate's most frequently observed tools, as the operational bridge from initial access into account manipulation and credential access; Atera plus Splashtop, ScreenConnect, NinjaRMM, and, in one intrusion, a persistent LocalSystem-service `Cloudflared.exe` tunnel, and ngrok exposing RDP for redundant remote access; `ntdsutil`-driven Install-From-Media dumps of `ntds.dit` for offline domain-credential extraction; Mimikatz, LaZagne and pypykatz for credential harvesting; systematic Windows Defender tampering (disabling real-time monitoring, adding `C:\PerfLogs` exclusions, direct `WinDefend` registry edits) ahead of deployment; PsExec-driven lateral movement using `@ip.txt` host lists, including an `rdp.bat` script that force-enables RDP, alongside Impacket and NetExec over SMB; and s5cmd- or Rclone-based exfiltration to attacker-controlled S3 buckets ahead of double-extortion.

Because the toolkit, not the ransomware brand, is what recurs, defenders who alert only on a known ransomware binary or a specific RaaS brand's indicators will miss the affiliate entirely on its next engagement under a different payload. The consistent tradecraft gives a detection surface that survives a brand switch: a renamed MeshAgent binary establishing outbound C2, an `ntdsutil` IFM snapshot followed by offline credential extraction, a persistent-service `Cloudflared.exe` process, discovery-scanner activity (NetScan/Nmap) ahead of lateral movement, and s5cmd/Rclone processes initiating outbound transfers to cloud object storage are the behaviors Microsoft's reporting keys on across Storm-2570 engagements, independent of which ransomware note appears at the end. Microsoft's own post closes with a Defender XDR detection and mitigation mapping tied to each of these behaviors.

**Triage:** MeshAgent, Atera, ScreenConnect and NinjaRMM are legitimate tools many organizations already run for IT support; the discriminator is not the tool's presence but its provenance and configuration: a renamed executable (`meshagent64-[org].exe` rather than the vendor's own binary name), an RMM agent installed outside a change-managed deployment window, or a `Cloudflared.exe` process registered as a persistent LocalSystem service rather than invoked interactively are the signals Microsoft's own telemetry keys on.

**Defender takeaway:** hunt for the toolkit, not the brand. A government agency estate should specifically watch for `ntdsutil` invoking Install-From-Media snapshots outside a scheduled backup window, unregistered or renamed RMM agents establishing outbound connections, and `Cloudflared.exe` or `ngrok` running as a persistent service on a domain-joined host; any one of these on a host with no legitimate business reason to run it is worth a compromise assessment regardless of which ransomware family, if any, is ultimately deployed.
