---
schema: 1
kind: threat
title: "Showboat Linux post-exploitation framework and JFMBackdoor for Windows used against telecom providers; PwC attributes the operation to Red Lamassu (Calypso)"
headline: "Lumen and PwC detail Showboat, a Linux implant that hides and proxies inside telcos, and Red Lamassu's JFMBackdoor"
summary: >
  Lumen's Black Lotus Labs (2026-05-20) and PwC Threat Intelligence (2026-05-21) documented Showboat, a
  modular Linux post-exploitation framework that PwC calls kworker, which spawns shells, moves files,
  hides its own process and acts as a SOCKS5 proxy, and JFMBackdoor, a Windows backdoor delivered by DLL
  side-loading. Lumen confirms an Afghanistan-based ISP and an entity in Azerbaijan as victims and ties
  Showboat to at least one and likely several PRC-aligned clusters; PwC attributes the JFMBackdoor
  operation to Red Lamassu (Calypso), which it has tracked since 2019 against telecom providers in Asia.
discovered_at: "2026-05-22T05:00:01Z"
event_date: 2026-05-20
run_id: 2026-05-22-5b90d5a1
priority: high
immediate_action: null
tags:
  - nation-state
  - espionage
  - china-nexus
regions:
  - middle-east
  - apac
sectors:
  - telco
entities:
  - "campaign:calypso-red-lamassu-showboat-jfmbackdoor-linux-windows-telco"
techniques: [T1059.004, T1090.001, T1105, T1543.002, T1564, T1132.001, T1574.001, T1140, T1620, T1113, T1070.006]
cves: []
sources:
  - url: "https://www.lumen.com/blog/en-us/introducing-showboat-a-new-malware-family-taunts-defenses-and-targets-international-telecom-firms"
    publisher: "Lumen Black Lotus Labs"
    date: "2026-05-20"
    role: primary
  - url: "https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/red-lamassu-open-season.html"
    publisher: "PwC Threat Intelligence"
    date: "2026-05-21"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/chinese-hackers-target-telcos-with-new-linux-windows-malware/"
    publisher: "BleepingComputer"
    date: "2026-05-21"
    role: corroborating
  - url: "https://thehackernews.com/2026/05/showboat-linux-malware-hits-middle-east.html"
    publisher: "The Hacker News"
    date: "2026-05-21"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Showboat is a modular post-exploitation framework designed for Linux systems, capable of spawning a remote shell, transferring files and functioning as a Socks5 proxy."
    publisher: "Lumen Black Lotus Labs"
    source_url: "https://www.lumen.com/blog/en-us/introducing-showboat-a-new-malware-family-taunts-defenses-and-targets-international-telecom-firms"
  - quote: "As the malware was not directly observed on any live systems, we are unable to comment on the initial access vector or exploit."
    publisher: "Lumen Black Lotus Labs"
    source_url: "https://www.lumen.com/blog/en-us/introducing-showboat-a-new-malware-family-taunts-defenses-and-targets-international-telecom-firms"
  - quote: "Red Lamassu is our name for a China-based threat actor likely operating out of Sichuan Province, associated with the targeting of telecommunications organisations based in Asia, predominantly Kazakhstan, Afghanistan, and India."
    publisher: "PwC Threat Intelligence"
    source_url: "https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/red-lamassu-open-season.html"
verification: multi-source
sourcing_note: >
  Lumen Black Lotus Labs and PwC Threat Intelligence analysed the tooling independently and published in
  tandem; PwC makes the Red Lamassu attribution, while Lumen attributes Showboat only to PRC-aligned
  clusters. BleepingComputer and The Hacker News restate both.
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-22.md
updates:
  - at: "2026-10-21T20:43:20Z"
    run_id: 2026-10-21T1148Z-audit
    type: correction
    summary: >
      Lumen confirms an Afghanistan-based ISP and an entity in Azerbaijan as Showboat victims, calls the
      US cases potential and ties the Ukrainian traffic to a separate cluster, and no source places
      European telecoms in the targeting. Showboat is not shown masquerading as a kernel worker (kworker
      is PwC's name for it), the campaign dates from mid-2022 while PwC has tracked Red Lamassu since
      2019, and JFMBackdoor's capabilities, the certificate clustering and the side-loading mapping are
      stated as the sources give them, with exposure, detection and takeaway guidance added.
    fields: [body, classification, event_date, evidence, headline, regions, sources, sourcing_note, summary, techniques, title]
---

Lumen's Black Lotus Labs published Showboat on 2026-05-20: a modular Linux post-exploitation framework, used since at least mid-2022, that spawns a remote shell, uploads and downloads files, acts as a SOCKS5 proxy and port mapper into internal hosts, can persist as a service and swap C2 nodes, and has a "hide" command that conceals its process with code fetched from Pastebin or online forums used as a dead drop ([Lumen, 2026-05-20](https://www.lumen.com/blog/en-us/introducing-showboat-a-new-malware-family-taunts-defenses-and-targets-international-telecom-firms)). It reports the host data it gathers in a PNG field as an encrypted, base64-encoded string, and Lumen found it on VirusTotal rather than on a live system, so the initial access vector is unknown ([Lumen, 2026-05-20](https://www.lumen.com/blog/en-us/introducing-showboat-a-new-malware-family-taunts-defenses-and-targets-international-telecom-firms)). PwC, publishing in tandem on 2026-05-21, found a Showboat sample, which it calls kworker, in an open directory active from July to October 2025 next to JFMBackdoor: a batch script downloads the files into the victim's temp directory and runs the legitimate `fltMC.exe`, which side-loads a malicious `FLTLIB.dll` that decrypts its configuration and loads the backdoor in memory through a shellcode stub; JFMBackdoor then offers a remote shell, full file operations including timestomping, TCP proxying and screenshots it base64-encodes and XOR-encrypts for exfiltration ([PwC, 2026-05-21](https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/red-lamassu-open-season.html)). Lumen's telemetry confirms two victims, an Afghanistan-based ISP whose Outlook server talked to a C2 node from 2025-12-01 to 2026-02-03 and an entity in Azerbaijan, finds two potential compromises in the United States, and links C2 traffic with the Donbas region, with moderate confidence, to a separate cluster sharing the tooling; the C2 nodes cluster on a shared self-signed certificate ([Lumen, 2026-05-20](https://www.lumen.com/blog/en-us/introducing-showboat-a-new-malware-family-taunts-defenses-and-targets-international-telecom-firms)). PwC ties the open directory to a telecommunications provider in Afghanistan and attributes it to Red Lamassu (also known as Calypso), a China-based actor likely operating from Sichuan Province that it has tracked since 2019 against telecom organizations in Asia ([PwC, 2026-05-21](https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/red-lamassu-open-season.html)), while Lumen attributes Showboat only to at least one and likely several PRC-aligned clusters ([Lumen, 2026-05-20](https://www.lumen.com/blog/en-us/introducing-showboat-a-new-malware-family-taunts-defenses-and-targets-international-telecom-firms)).

**Exposure:** telecommunications providers, chiefly in Asia and the Middle East ([PwC, 2026-05-21](https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/red-lamassu-open-season.html)) ([Lumen, 2026-05-20](https://www.lumen.com/blog/en-us/introducing-showboat-a-new-malware-family-taunts-defenses-and-targets-international-telecom-firms)), and in particular their Linux servers and routers, which Lumen notes typically run no EDR ([Lumen, 2026-05-20](https://www.lumen.com/blog/en-us/introducing-showboat-a-new-malware-family-taunts-defenses-and-targets-international-telecom-firms)).

**Detection:** network and host telemetry on Linux servers: east-west traffic from servers that does not map to a business process, which Lumen recommends monitoring, and, from Showboat's functions, a server process fetching Pastebin or forum content, a SOCKS5 listener or port mapper on a server, and a new service persisting an unfamiliar binary ([Lumen, 2026-05-20](https://www.lumen.com/blog/en-us/introducing-showboat-a-new-malware-family-taunts-defenses-and-targets-international-telecom-firms)). On Windows, a legitimate binary such as `fltMC.exe` launched from the temp directory next to a `FLTLIB.dll` is the side-loading pattern PwC describes ([PwC, 2026-05-21](https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/red-lamassu-open-season.html)).

**Defender takeaway:** telecom operators hunt their Linux server and router estate for these behaviors rather than waiting for EDR alerts; Lumen calls the presence of such implants an early warning sign of broader compromise ([Lumen, 2026-05-20](https://www.lumen.com/blog/en-us/introducing-showboat-a-new-malware-family-taunts-defenses-and-targets-international-telecom-firms)).

## Correction — 2026-10-21T20:43:20Z

The confirmed victims are an Afghanistan-based ISP and an entity in Azerbaijan; Lumen calls the US cases potential compromises, links the traffic from Ukraine's Donbas region with moderate confidence to a separate cluster sharing the tooling, and neither source places European telecoms in the targeting ([Lumen, 2026-05-20](https://www.lumen.com/blog/en-us/introducing-showboat-a-new-malware-family-taunts-defenses-and-targets-international-telecom-firms)). Showboat is not described as masquerading as a kernel worker thread: kworker is PwC's name for the malware and the sample PwC found was named systemd-ac-update ([PwC, 2026-05-21](https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/red-lamassu-open-season.html)), while Lumen documents process hiding and service persistence ([Lumen, 2026-05-20](https://www.lumen.com/blog/en-us/introducing-showboat-a-new-malware-family-taunts-defenses-and-targets-international-telecom-firms)).

The campaign dates from at least mid-2022, whereas PwC has tracked Red Lamassu since 2019; JFMBackdoor offers TCP proxying and screenshots rather than SOCKS5 and self-removal ([PwC, 2026-05-21](https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/red-lamassu-open-season.html)); and the self-signed certificate clusters the C2 nodes rather than linking the victims ([Lumen, 2026-05-20](https://www.lumen.com/blog/en-us/introducing-showboat-a-new-malware-family-taunts-defenses-and-targets-international-telecom-firms)).
