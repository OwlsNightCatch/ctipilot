---
schema: 1
kind: threat
title: 'ScreenConnect: commands pushed through Run Command to at least 288 managed endpoints at 48 Huntress customers within 90 minutes on 2026-11-11 installed a rogue second client and the SCKit toolkit; Huntress links the activity to the RMM+ extension, whose versions 1.0.31 and 1.0.32 accepted a blank access key'
headline: 'ScreenConnect SCKit: second wave hits on-prem; disable RMM+, update technician clients to 26.6.5+'
summary: Huntress saw an operator use access to several cloud-hosted ScreenConnect panels on 2026-11-11 to run Run Command as SYSTEM on groups of managed endpoints, installing an attacker-controlled second ScreenConnect client and the SCKit toolkit on at least 288 hosts at 48 organisations within 90 minutes; Sophos independently saw the same client deployments. Huntress later said the activity seems related to the third-party RMM+ extension, whose versions 1.0.31 and 1.0.32 accepted a blank access key; ConnectWise's CNA record CVE-2026-127063 (CVSS 4.0 9.3) says the extension uses a static API secret by default, names no fix and gives disabling as the mitigation, while a Huntress spokesperson says the panel-access vector is still unclear and Blackpoint calls the extensions' role unresolved. A second wave on 2026-11-13 hit 205 hosts at 41 organisations (Huntress) and appears to target on-premises instances with mitigations pending (Blackpoint); Microsoft describes a rogue client built to deliver a payload to the technician who connects, which ConnectWise says ScreenConnect clients 26.6.5 and later block.
discovered_at: '2026-11-12T04:07:00Z'
updated_at: "2026-11-14T03:57:58Z"
event_date: '2026-11-11'
run_id: 2026-11-12T0255Z-intel
priority: high
immediate_action: null
tags:
  - supply-chain
  - no-patch
regions:
  - global
sectors:
  - technology
entities:
  - incident:screenconnect-sckit-msp-compromise-2026-11
  - malware:sckit
techniques:
  - T1072
  - T1219.002
  - T1059.003
  - T1059.001
  - T1105
  - T1218.007
  - T1685
  - T1053.005
  - T1547.001
  - T1489
  - T1027
  - T1539
  - T1550.004
  - T1027.004
  - T1543.003
  - T1036.004
  - T1570
affected_products:
  - ConnectWise ScreenConnect
cves:
  - id: CVE-2026-127063
    cvss: 9.3 (CVSS 4.0, ConnectWise as CNA)
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status:
      - no-patch
      - mitigation-only
    affected: 'DataComm RMM+ extension for ConnectWise ScreenConnect, all versions that keep the default API secret (Huntress: versions 1.0.31 and 1.0.32 with a blank key); the ScreenConnect server and client are not affected'
    fixed: 'none announced; ConnectWise disabled and removed the extension from cloud-hosted instances; on-premises: disable it immediately, verify it stays disabled, do not re-enable or reinstall'
sources:
  - url: https://www.huntress.com/blog/sckit-worm-rogue-screenconnect
    publisher: Huntress
    date: '2026-11-11'
    role: primary
  - url: https://www.sophos.com/en-us/blog/malicious-screenconnect-deployments-observed
    publisher: Sophos
    date: '2026-11-11'
    role: corroborating
  - url: https://www.bleepingcomputer.com/news/security/active-screenconnect-attacks-breach-msps-impact-dozens-of-organizations/
    publisher: BleepingComputer
    date: '2026-11-11'
    role: corroborating
  - url: https://github.com/ConnectWise-Advisories/Disclosures/tree/main/CVE-2026-127063
    publisher: ConnectWise (CNA disclosure CVE-2026-127063)
    date: '2026-11-12'
    role: primary
  - url: https://therecord.media/connectwise-screenconnect-breaches-third-party-tool
    publisher: The Record
    date: '2026-11-12'
    role: corroborating
  - url: https://blackpointcyber.com/blog/screenconnect-attack-sckit/
    publisher: Blackpoint Cyber
    date: '2026-11-12'
    role: corroborating
  - url: https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-124597
    publisher: ENISA EUVD (EUVD-2026-124597)
    date: '2026-11-12'
    role: corroborating
  - url: https://www.microsoft.com/en-us/security/blog/2026/11/13/sckit-abuses-screenconnect-deploy-remote-access-target-technician-sessions/
    publisher: Microsoft Threat Intelligence
    date: '2026-11-13'
    role: corroborating
  - url: https://www.huntress.com/blog/sckit-worm-rogue-screenconnect
    publisher: Huntress (update of 2026-11-13)
    date: '2026-11-13'
    role: corroborating
  - url: https://blackpointcyber.com/blog/screenconnect-attack-sckit/
    publisher: Blackpoint Cyber (SITREP update of 2026-11-13)
    date: '2026-11-13'
    role: corroborating
closed_sources: []
evidence:
  - quote: On November 11, 2026, Huntress observed an operator using access to multiple cloud-hosted ScreenConnect panels to push commands to groups of managed endpoints.
    publisher: Huntress
    source_url: https://www.huntress.com/blog/sckit-worm-rogue-screenconnect
  - quote: The legitimate installation of ScreenConnect is then stopped, set to manual start, and the attacker controlled copy of ScreenConnect positioned to replace it.
    publisher: Huntress
    source_url: https://www.huntress.com/blog/sckit-worm-rogue-screenconnect
  - quote: Disabling these 3rd party extensions is a precautionary containment measure. It does not establish that unauthorized software, persistence mechanisms, or access already present on affected devices has been removed
    publisher: BleepingComputer (quoting the ConnectWise advisory)
    source_url: https://www.bleepingcomputer.com/news/security/active-screenconnect-attacks-breach-msps-impact-dozens-of-organizations/
  - quote: versions 1.0.31 and 1.0.32 contained a serious authentication flaw
    publisher: Huntress
    source_url: https://www.huntress.com/blog/sckit-worm-rogue-screenconnect
  - quote: The third-party RMM+ extension for ConnectWise ScreenConnect uses a static API secret by default.
    publisher: ConnectWise (CNA disclosure CVE-2026-127063)
    source_url: https://github.com/ConnectWise-Advisories/Disclosures/tree/main/CVE-2026-127063
  - quote: No fixed RMM+ version has been announced. Disabling the extension is the current mitigation.
    publisher: ConnectWise (CNA disclosure CVE-2026-127063)
    source_url: https://github.com/ConnectWise-Advisories/Disclosures/tree/main/CVE-2026-127063
  - quote: "ConnectWise states that ScreenConnect client 26.6.5 and later block the toolkit’s attempted endpoint-to-technician transfer technique."
    publisher: Microsoft Threat Intelligence
    source_url: https://www.microsoft.com/en-us/security/blog/2026/11/13/sckit-abuses-screenconnect-deploy-remote-access-target-technician-sessions/
  - quote: "Removing an unauthorized client alone does not remove the toolkit’s persistence or invalidate exposed web sessions."
    publisher: Microsoft Threat Intelligence
    source_url: https://www.microsoft.com/en-us/security/blog/2026/11/13/sckit-abuses-screenconnect-deploy-remote-access-target-technician-sessions/
verification: multi-source
sourcing_note: Huntress and Sophos report the activity from their own telemetry and the Sophos client identifiers match Huntress's; Huntress's update of 2026-11-11 at 11:34 pm ET names RMM+ and its blank-access-key flaw from its own analysis. ConnectWise's advisory was not readable, so its statements come from the sentences BleepingComputer quotes, written before that update, and from Huntress's account of it. No source names an actor or a victim; the technician-workstation stage is reconstructed from code and Huntress says it never saw it succeed. ConnectWise's CNA record and the statements The Record quotes now describe the extension's defect differently from Huntress (a static default secret in all versions and a passphrase set by the partner, against a blank key in two versions), and a Huntress spokesperson says it has seen no evidence of a new vulnerability; the sources are printed as they state it and not reconciled. Blackpoint ties part of the toolkit's behaviour to CVE-2026-84869, a flaw already covered, and says its test against a current release did not execute. The client-version statement is ConnectWise's as Microsoft and Huntress relay it, while the statement that a cloud-console update does not update technician clients is Microsoft's own, since ConnectWise's Trust Center pages could not be read, and ConnectWise's own record for CVE-2026-84869 names 26.6.5 as the fixed client; Microsoft's account of RelayTrap and the cookie routine is code analysis of designed behaviour, and no source observed a technician compromise. The second wave rests on Huntress's update and Blackpoint's situation report, which relay the vendor's updated advisory and describe a modified toolkit without a recovered sample.
confidence: high
references:
  - 2026-09-12/cve-2026-84869-connectwise-screenconnect-worm-file-transfer
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions:
  - On every ScreenConnect instance your organisation or its IT providers run, disable the RMM+ extension immediately, verify it stays disabled and do not re-enable or reinstall it (on-premises instances by hand; ConnectWise removed it from cloud-hosted ones), review Run Command and Toolbox history and the instance audit logs for executions nobody started, including before 2026-11-11, and check managed endpoints for a second ScreenConnect client service; open no interactive session to a suspect host, use EDR live response or WinRM, because a session can trigger the toolkit to spread to the technician's workstation; update every technician host client to ScreenConnect 26.6.5 or later, because a cloud-console update does not update them.
updates:
  - at: "2026-11-13T04:04:37Z"
    run_id: 2026-11-13T0256Z-intel
    type: update
    summary: >
      ConnectWise's CNA record CVE-2026-127063 (CVSS 4.0 9.3) says the RMM+ extension uses a static API
      secret by default, names no fix and gives disabling as the mitigation; Huntress's spokesperson and
      Blackpoint leave the panel-access vector unresolved, so the explanations differ and the action now
      names RMM+ specifically.
    fields: [headline, summary, tags, cves, sources, evidence, sourcing_note, actions, body]
  - at: "2026-11-14T03:57:58Z"
    run_id: 2026-11-14T0255Z-intel
    type: update
    summary: >
      Microsoft's analysis describes RelayTrap, a rogue client built on the endpoint to deliver a payload
      to the technician who connects, and browser-cookie routines designed to push tools through the
      Shared Toolbox; ConnectWise says clients 26.6.5 and later block the transfer, and a second wave on
      2026-11-13 hit 205 hosts at 41 organisations, one with a self-hosted RMM+, so every technician
      client now belongs on the action list.
    fields: [headline, summary, techniques, sources, evidence, sourcing_note, actions, body]
migrated_from: null
---

On 2026-11-11 Huntress observed an operator using access to several cloud-hosted ScreenConnect panels to run commands as SYSTEM on groups of managed endpoints through the Run Command feature, hitting at least 288 hosts at 48 organisations within 90 minutes ([Huntress, 2026-11-11](https://www.huntress.com/blog/sckit-worm-rogue-screenconnect)). Each host installed an attacker-controlled second client and fetched SCKit, a 16-file toolkit delivered encrypted that sets the legitimate client to manual start so the attacker's copy replaces it and runs a per-host executable from a scheduled task ([Huntress, 2026-11-11](https://www.huntress.com/blog/sckit-worm-rogue-screenconnect)). A second wave on 2026-11-13 hit 205 hosts at 41 organisations with no follow-on executions observed ([Huntress, 2026-11-13](https://www.huntress.com/blog/sckit-worm-rogue-screenconnect)), and Blackpoint says it appears to target on-premises instances where mitigations are still pending ([Blackpoint, 2026-11-13](https://blackpointcyber.com/blog/screenconnect-attack-sckit/)).

Huntress's later update says the activity seems related to RMM+, a third-party extension that bypasses ScreenConnect's accounts, roles and MFA: versions 1.0.31 and 1.0.32 accepted a blank access key when an administrator had never set one ([Huntress, 2026-11-11](https://www.huntress.com/blog/sckit-worm-rogue-screenconnect)). ConnectWise, as CNA, published CVE-2026-127063 (CVSS 4.0 9.3) saying the extension uses a static API secret by default; it names no fixed version, removed the extension from cloud-hosted instances and tells on-premises customers to disable it and not reinstall it ([ConnectWise, 2026-11-12](https://github.com/ConnectWise-Advisories/Disclosures/tree/main/CVE-2026-127063)).

Microsoft describes the technician stage: RelayTrap, a replacement client compiled on the endpoint with the .NET C# compiler and designed to deliver a payload to the technician who connects, and browser-access code that searches Chrome, Edge and Opera profiles for cookies named .ASPXAUTH, with a component designed to queue payloads through the console's Shared Toolbox ([Microsoft, 2026-11-13](https://www.microsoft.com/en-us/security/blog/2026/11/13/sckit-abuses-screenconnect-deploy-remote-access-target-technician-sessions/)). ConnectWise says clients 26.6.5 and later block the transfer, and Microsoft adds that a cloud-console update does not update technician clients ([Microsoft, 2026-11-13](https://www.microsoft.com/en-us/security/blog/2026/11/13/sckit-abuses-screenconnect-deploy-remote-access-target-technician-sessions/)); Huntress and Blackpoint saw no successful technician compromise ([Huntress, 2026-11-11](https://www.huntress.com/blog/sckit-worm-rogue-screenconnect); [Blackpoint, 2026-11-13](https://blackpointcyber.com/blog/screenconnect-attack-sckit/)).

**Exposure:** a ScreenConnect instance whose panel can run commands on managed endpoints, run by the organisation or an IT provider; an RMM+ extension at any version, since ConnectWise's record names a static default secret, with versions 1.0.31 and 1.0.32 and a blank key as the condition Huntress describes; a technician host client older than 26.6.5; an endpoint with a second client service pointing at a foreign relay.

**Detection:** ScreenConnect instance audit logs, Run Command and Toolbox history for mass executions nobody started and RMM+ requests with no matching login ([Huntress, 2026-11-11](https://www.huntress.com/blog/sckit-worm-rogue-screenconnect)), and file-transfer-and-run events (event ID 201, per Blackpoint) ([Blackpoint, 2026-11-13](https://blackpointcyber.com/blog/screenconnect-attack-sckit/)); process-creation telemetry with the ScreenConnect client service as parent of cmd, PowerShell or msiexec, curl or PowerShell downloads followed by a silent msiexec install (the Sophos pattern) ([Sophos, 2026-11-11](https://www.sophos.com/en-us/blog/malicious-screenconnect-deployments-observed)), a scheduled-task PowerShell watcher that compiles an executable with the .NET compiler ([Microsoft, 2026-11-13](https://www.microsoft.com/en-us/security/blog/2026/11/13/sckit-abuses-screenconnect-deploy-remote-access-target-technician-sessions/)), and a client service named like a Windows component ([Huntress, 2026-11-13](https://www.huntress.com/blog/sckit-worm-rogue-screenconnect)).

**Defender takeaway:** treat Run Command or Toolbox executions you did not start as a compromise; disable RMM+ and the four other extensions the first notice named, update every technician host client to 26.6.5 or later, rotate ScreenConnect credentials and revoke active sessions and the browser and identity-provider sessions the toolkit could steal, and keep hosts and technician workstations out of service until the rogue client and persistence are gone ([Huntress, 2026-11-11](https://www.huntress.com/blog/sckit-worm-rogue-screenconnect); [Microsoft, 2026-11-13](https://www.microsoft.com/en-us/security/blog/2026/11/13/sckit-abuses-screenconnect-deploy-remote-access-target-technician-sessions/)). Removing the rogue client alone leaves the persistence and the web sessions, and the cleanup script found in the kit must not be used ([Microsoft, 2026-11-13](https://www.microsoft.com/en-us/security/blog/2026/11/13/sckit-abuses-screenconnect-deploy-remote-access-target-technician-sessions/)).

## Update — 2026-11-13T04:04:37Z

ConnectWise, as CNA, published CVE-2026-127063 (CVSS 4.0 9.3) on 2026-11-12: the third-party RMM+ extension "uses a static API secret by default", no fixed version has been announced, disabling is the mitigation, and ConnectWise has removed the extension from cloud-hosted instances while on-premises customers must disable it and not reinstall it ([ConnectWise, 2026-11-12](https://github.com/ConnectWise-Advisories/Disclosures/tree/main/CVE-2026-127063)). This differs from Huntress's account of a blank key in versions 1.0.31 and 1.0.32, and a Huntress spokesperson told The Record that it has seen no evidence of a new vulnerability and that how the attacker got panel access is still unclear, while ConnectWise says the extension's API is protected by a passphrase the partner sets ([The Record, 2026-11-12](https://therecord.media/connectwise-screenconnect-breaches-third-party-tool)). Blackpoint reverse engineered the toolkit, saw unauthorised deployments through legitimate cloud-hosted instances but no successful propagation to a technician workstation, and calls the extensions' role in the first panel access unresolved ([Blackpoint, 2026-11-12](https://blackpointcyber.com/blog/screenconnect-attack-sckit/)).

## Update — 2026-11-14T03:57:58Z

Microsoft published on 2026-11-13 its analysis of SCKit, which includes RelayTrap, a malicious replacement for the ScreenConnect client on an affected customer endpoint that is designed to deliver a payload to a technician's workstation when they connect for support ([Microsoft, 2026-11-13](https://www.microsoft.com/en-us/security/blog/2026/11/13/sckit-abuses-screenconnect-deploy-remote-access-target-technician-sessions/)). A watcher on the endpoint enumerates the ScreenConnect client services and builds RelayTrap for each with the .NET C# compiler, and the toolkit's browser code searches Chrome, Edge, Opera and Opera GX profiles for cookies named .ASPXAUTH; a console-distribution component is designed to combine the cookie with the anti-forgery and access tokens, upload a payload, queue it through the Shared Toolbox and remove the uploaded item afterwards ([Microsoft, 2026-11-13](https://www.microsoft.com/en-us/security/blog/2026/11/13/sckit-abuses-screenconnect-deploy-remote-access-target-technician-sessions/)). Microsoft relays ConnectWise's statement that clients 26.6.5 and later block the transfer; in its own words the fix for CVE-2026-84869 was released on 2026-09-08 and a cloud-console update does not automatically update technician clients, and it advises live response or another out-of-band method instead of ScreenConnect on a suspected device, with connecting technician workstations in scope, invalidation of ScreenConnect web and identity-provider sessions, and no use of a cleanup script recovered from the kit ([Microsoft, 2026-11-13](https://www.microsoft.com/en-us/security/blog/2026/11/13/sckit-abuses-screenconnect-deploy-remote-access-target-technician-sessions/)). Blackpoint's own test found that a current Host client did not fetch or run the queued transfer, and it found no technical link between the extensions and RelayTrap or the browser routines ([Blackpoint, 2026-11-13](https://blackpointcyber.com/blog/screenconnect-attack-sckit/)).

Huntress's update of 2026-11-13 reports a second spike at 16:12 UTC that hit 205 hosts at 41 organisations with no follow-on executions observed, one incident at an organisation running a self-hosted RMM+, a rogue client persisting as a service called Windows Update Agent, and ConnectWise's updated advisory urging partners to verify that every technician client runs 26.6.5 or later ([Huntress, 2026-11-13](https://www.huntress.com/blog/sckit-worm-rogue-screenconnect)). Blackpoint's update says the second wave appears to target on-premises instances where mitigations remain pending ([Blackpoint, 2026-11-13](https://blackpointcyber.com/blog/screenconnect-attack-sckit/)).
