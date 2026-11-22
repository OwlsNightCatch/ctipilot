---
schema: 1
kind: threat
title: "Symantec: a September 2026 intrusion at a US retailer shows attackers switching to AI-generated PowerShell and, about ten minutes after first querying SolarWinds Orion, using the RabbitMQ Erlang cookie bundled with it to run a command on a second server"
headline: "Symantec: AI-assisted retailer intrusion pivots through SolarWinds Orion's bundled RabbitMQ Erlang cookie"
summary: >
  Symantec reports that after hand-typed commands against a US retailer's web server were blocked, the attackers switched overnight to long, error-free PowerShell scripts and, about ten minutes after first querying SolarWinds Orion, read the Erlang cookie of the RabbitMQ broker bundled with it and ran Orion's own erl.exe to execute a command on a second web server. Symantec assesses AI assistance with high confidence and says no technique was new: the AI supplied speed, while the chain ran through SQL Server command execution, web shells, side-loaded security-vendor executables and domain credential theft.
discovered_at: "2026-11-17T04:39:30Z"
updated_at: null
event_date: "2026-09-23"
run_id: 2026-11-17T0355Z-intel
priority: notable
immediate_action: null
tags: [ai-abuse]
regions: [us]
sectors: [retail]
entities: ["tool:breakchain", "product:microsoft-sql-server"]
techniques: [T1505.003, T1505.001, T1059.001, T1574.001, T1068, T1003.002, T1003.004, T1003.003, T1552.001, T1021, T1572, T1090, T1110.003, T1047, T1036.005, T1105]
affected_products: ["Microsoft SQL Server", "Microsoft IIS", "SolarWinds Orion"]
cves: []
sources:
  - url: "https://www.security.com/threat-intelligence/ai-assisted-attack-us-retailer"
    publisher: "Symantec Threat Hunter Team (Broadcom)"
    date: "2026-11-12"
    role: primary
closed_sources: []
evidence:
  - quote: "This is one of dozens of AI-assisted attacks that Symantec has investigated since May 2026."
    publisher: "Symantec Threat Hunter Team (Broadcom)"
    source_url: "https://www.security.com/threat-intelligence/ai-assisted-attack-us-retailer"
  - quote: "About 10 minutes after first querying the victim's SolarWinds Orion monitoring software, the attackers had used a component bundled with it to run commands on a second server."
    publisher: "Symantec Threat Hunter Team (Broadcom)"
    source_url: "https://www.security.com/threat-intelligence/ai-assisted-attack-us-retailer"
  - quote: "Symantec assesses the AI assistance with high confidence and the operator-in-the-loop model with moderate confidence."
    publisher: "Symantec Threat Hunter Team (Broadcom)"
    source_url: "https://www.security.com/threat-intelligence/ai-assisted-attack-us-retailer"
verification: single-source
sourcing_note: >
  Symantec holds the incident telemetry and is the only source; the initial access method, the AI model or service and the victim are not stated, and no data theft or encryption was observed.
confidence: medium
references: ["2026-09-23/gambit-ai-agent-retail-skimmer-campaign-strix-cairn-hermes"]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates:
  - at: "2026-11-22T14:58:22Z"
    run_id: 2026-11-22T1407Z-audit
    type: correction
    summary: >
      Symantec does not say the side-loaded DLLs are unsigned, and it notes that one of the executable and
      DLL pairings is used by several threat actors, so the pairing alone identifies neither the malware
      nor the actor.
    fields: [body]
migrated_from: null
---

Symantec's Threat Hunter Team describes a September 2026 intrusion at a US retail organization in which the attackers first worked by hand on a compromised web server, with typing errors and every staged payload terminated by security software, and then, the next day, submitted about 50 long, error-free PowerShell scripts over roughly two hours, with labelled output sections and comments that read as a model's reasoning ([Symantec, 2026-11-12](https://www.security.com/threat-intelligence/ai-assisted-attack-us-retailer)). Symantec assesses AI assistance with high confidence and an operator relaying output to an AI tool, not an autonomous agent, with moderate confidence; it could not identify the model ([Symantec, 2026-11-12](https://www.security.com/threat-intelligence/ai-assisted-attack-us-retailer)). The initial infection vector is unknown ([Symantec, 2026-11-12](https://www.security.com/threat-intelligence/ai-assisted-attack-us-retailer)).

The earliest activity, on 2026-09-18, ran cmd.exe directly under sqlservr.exe on three SQL Servers, which Symantec reads as commands issued through the database service, most likely xp_cmdshell; on one host the attackers compiled the public EfsPotato exploit with csc.exe from base64 text decoded by certutil and saved the SAM, SYSTEM and SECURITY hives ([Symantec, 2026-11-12](https://www.security.com/threat-intelligence/ai-assisted-attack-us-retailer)). On a web server compromised through w3wp.exe they side-loaded malicious DLLs with a legitimate Bitdefender executable and a G DATA executable placed in ProgramData, used a utility called BreakChain to relaunch them so they no longer appeared as children of w3wp.exe, copied one to a file named w3wp.exe, and planted ASP web shells in the application's images folder ([Symantec, 2026-11-12](https://www.security.com/threat-intelligence/ai-assisted-attack-us-retailer)). The AI-style scripts then harvested credentials from connection strings, FileZilla, WinSCP and PuTTY settings, saved RDP files and IIS configuration, read the Erlang cookie file of the RabbitMQ broker that ships with Orion; running Orion's bundled erl.exe with that cookie, they called the broker on a second web server to run an encoded operating system command ([Symantec, 2026-11-12](https://www.security.com/threat-intelligence/ai-assisted-attack-us-retailer)). Later activity searched a probable domain controller for NTDS.dit, SYSVOL cpassword values and LAPS passwords and ran a Chisel tunnelling tool and a password sprayer ([Symantec, 2026-11-12](https://www.security.com/threat-intelligence/ai-assisted-attack-us-retailer)).

Symantec says no second-phase technique was new and suggests a possible link, through a shared address and the retail focus, to the operation Gambit Security described on 2026-09-22 ([Symantec, 2026-11-12](https://www.security.com/threat-intelligence/ai-assisted-attack-us-retailer)). No Swiss or public-sector victim is named; the case matters for the transferable chain and its AI-assisted tempo.

**Exposure:** Windows estates running SolarWinds Orion with its bundled RabbitMQ broker alongside SQL Server hosts and IIS web applications; the Erlang cookie file on the Orion host is the pivot.

**Detection:** process-creation telemetry with parent lineage for cmd.exe or PowerShell started under sqlservr.exe or w3wp.exe, csc.exe started by PowerShell on a server, certutil decoding a text file in ProgramData, a vendor-signed security executable running from ProgramData and loading a DLL beside it, an executable named w3wp.exe outside the IIS directory, and erl.exe started from the Orion directory with a cookie argument and a remote broker call; registry hive save events for SAM, SYSTEM and SECURITY.

**Triage:** long, labelled PowerShell is not the signal on its own, because administrators write such scripts too; a parent of sqlservr.exe or w3wp.exe rather than an administrator session, credential-store targets and a blocked loader returning rebuilt are.

**Defender takeaway:** hunt SQL Server and IIS hosts for this lineage, treat an Orion server as a lateral-movement bridge to every host that runs its RabbitMQ node, and alert on behavior rather than file names, since the tools were renamed and rebuilt after each block.

## Correction — 2026-11-22T14:58:22Z

Symantec describes the side-loading as a legitimate Bitdefender executable and a G DATA signed executable each loading a malicious DLL; it does not say the DLLs are unsigned, and it notes that one of the executable and DLL pairings has been used by several threat actors, so the pairing alone identifies neither the malware nor the actor ([Symantec, 2026-11-12](https://www.security.com/threat-intelligence/ai-assisted-attack-us-retailer)).
