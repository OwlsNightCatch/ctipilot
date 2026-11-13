---
schema: 1
kind: threat
title: 'ScreenConnect: commands pushed through Run Command to at least 288 managed endpoints at 48 Huntress customers within 90 minutes on 2026-11-11 installed a rogue second client and the SCKit toolkit; Huntress links the activity to the RMM+ extension, whose versions 1.0.31 and 1.0.32 accepted a blank access key'
headline: 'ScreenConnect: rogue clients on 288+ endpoints; RMM+ extension CVE-2026-127063 has no fix, disable it'
summary: Huntress saw an operator use access to several cloud-hosted ScreenConnect panels on 2026-11-11 to run Run Command as SYSTEM on groups of managed endpoints, installing an attacker-controlled second ScreenConnect client and the SCKit toolkit on at least 288 hosts at 48 organisations within 90 minutes; Sophos independently saw the same client deployments. Huntress later said the activity seems related to the third-party RMM+ extension, whose versions 1.0.31 and 1.0.32 accepted a blank access key; ConnectWise's CNA record CVE-2026-127063 (CVSS 4.0 9.3) says the extension uses a static API secret by default, names no fix and gives disabling as the mitigation, while a Huntress spokesperson says the panel-access vector is still unclear and Blackpoint calls the extensions' role unresolved.
discovered_at: '2026-11-12T04:07:00Z'
updated_at: "2026-11-13T04:04:37Z"
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
verification: multi-source
sourcing_note: Huntress and Sophos report the activity from their own telemetry and the Sophos client identifiers match Huntress's; Huntress's update of 2026-11-11 at 11:34 pm ET names RMM+ and its blank-access-key flaw from its own analysis. ConnectWise's advisory was not readable, so its statements come from the sentences BleepingComputer quotes, written before that update, and from Huntress's account of it. No source names an actor or a victim; the technician-workstation stage is reconstructed from code and Huntress says it never saw it succeed. ConnectWise's CNA record and the statements The Record quotes now describe the extension's defect differently from Huntress (a static default secret in all versions and a passphrase set by the partner, against a blank key in two versions), and a Huntress spokesperson says it has seen no evidence of a new vulnerability; the sources are printed as they state it and not reconciled. Blackpoint ties part of the toolkit's behaviour to CVE-2026-84869, a flaw already covered, and says its test against a current release did not execute.
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
  - On every ScreenConnect instance your organisation or its IT providers run, disable the RMM+ extension immediately, verify it stays disabled and do not re-enable or reinstall it (on-premises instances by hand; ConnectWise removed it from cloud-hosted ones), review Run Command and Toolbox history and the instance audit logs for executions nobody started, including before 2026-11-11, and check managed endpoints for a second ScreenConnect client service; open no interactive session to a suspect host, use EDR live response or WinRM, because a session can trigger the toolkit to spread to the technician's workstation.
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
migrated_from: null
---

On 2026-11-11 Huntress observed an operator using access to several cloud-hosted ScreenConnect panels to run commands as SYSTEM on groups of managed endpoints through the Run Command feature, hitting at least 288 hosts at 48 organisations that use Huntress within 90 minutes ([Huntress, 2026-11-11](https://www.huntress.com/blog/sckit-worm-rogue-screenconnect)). Each host checked for a ScreenConnect client, silently installed an attacker-controlled one, wrote a dropper and fetched SCKit, a 16-file toolkit delivered encrypted whose decryption values the server issues against the requesting machine's UUID ([Huntress, 2026-11-11](https://www.huntress.com/blog/sckit-worm-rogue-screenconnect)). The kit adds Defender exclusions, installs a second attacker-controlled client, sets the legitimate client to manual start so the attacker's copy replaces it, and runs a per-host executable from a scheduled task ([Huntress, 2026-11-11](https://www.huntress.com/blog/sckit-worm-rogue-screenconnect)).

Huntress's later update says the activity seems related to RMM+, a third-party extension that bypasses ScreenConnect's user accounts, roles and MFA and authenticates requests with an access key: versions 1.0.31 and 1.0.32 accepted a blank key when an administrator had never set one, and commands reached endpoints across several instances within minutes with no corresponding login activity ([Huntress, 2026-11-11](https://www.huntress.com/blog/sckit-worm-rogue-screenconnect)). ConnectWise, as CNA, published CVE-2026-127063 (CVSS 4.0 9.3) saying the extension uses a static API secret by default; it names no fixed version, gives disabling as the mitigation, removed the extension from cloud-hosted instances and tells on-premises customers to disable it, keep it disabled and not reinstall it ([ConnectWise, 2026-11-12](https://github.com/ConnectWise-Advisories/Disclosures/tree/main/CVE-2026-127063)). It told The Record that it found about 400 partner environments with an extension of the RMM+ family ([The Record, 2026-11-12](https://therecord.media/connectwise-screenconnect-breaches-third-party-tool)). Huntress told The Record it has seen no evidence of a new vulnerability and that how the attacker got panel access is unclear (compromised credentials or hijacked operator sessions are possible), and Blackpoint calls the extensions' role in that first access unresolved ([The Record, 2026-11-12](https://therecord.media/connectwise-screenconnect-breaches-third-party-tool); [Blackpoint, 2026-11-12](https://blackpointcyber.com/blog/screenconnect-attack-sckit/)). Huntress reconstructs a second stage meant to spread through the connecting technician's panel but saw no successful jump ([Huntress, 2026-11-11](https://www.huntress.com/blog/sckit-worm-rogue-screenconnect)), and says sequential attacker tags suggest other MSPs were compromised earlier ([BleepingComputer, 2026-11-11](https://www.bleepingcomputer.com/news/security/active-screenconnect-attacks-breach-msps-impact-dozens-of-organizations/)).

**Exposure:** a ScreenConnect instance whose panel can run commands on managed endpoints, run by the organisation or an IT provider; an RMM+ extension at any version, since ConnectWise's record names a static default secret, with versions 1.0.31 and 1.0.32 and a blank key as the condition Huntress describes, which the Extensions list shows; an endpoint with a second client service pointing at a foreign relay.

**Detection:** ScreenConnect instance audit logs, Run Command and Toolbox history for mass executions nobody started, and RMM+ requests with no matching login; process-creation telemetry with the ScreenConnect client service as parent of cmd, PowerShell or msiexec; curl or PowerShell downloads followed by a silent msiexec install, the pattern Sophos describes; the persistence changes described above ([Huntress, 2026-11-11](https://www.huntress.com/blog/sckit-worm-rogue-screenconnect); [Sophos, 2026-11-11](https://www.sophos.com/en-us/blog/malicious-screenconnect-deployments-observed)). Isolation does not remove the persistence; hosts reinfected afterwards ([Huntress, 2026-11-11](https://www.huntress.com/blog/sckit-worm-rogue-screenconnect)).

**Defender takeaway:** treat Run Command or Toolbox executions you did not start as a compromise, not a misconfiguration; remove or disable RMM+ and the four other extensions the first notice named, verify the legitimate client before removing anything, rotate ScreenConnect credentials and revoke active sessions from a clean device, revoke the browser and identity-provider sessions the toolkit could steal, and keep hosts out of service until the rogue client and persistence are gone ([Huntress, 2026-11-11](https://www.huntress.com/blog/sckit-worm-rogue-screenconnect)). Disabling the extensions is precautionary containment that removes nothing already installed ([BleepingComputer, 2026-11-11](https://www.bleepingcomputer.com/news/security/active-screenconnect-attacks-breach-msps-impact-dozens-of-organizations/)).

## Update — 2026-11-13T04:04:37Z

ConnectWise, as CNA, published CVE-2026-127063 (CVSS 4.0 9.3) on 2026-11-12: the third-party RMM+ extension "uses a static API secret by default", no fixed version has been announced, disabling is the mitigation, and ConnectWise has removed the extension from cloud-hosted instances while on-premises customers must disable it and not reinstall it ([ConnectWise, 2026-11-12](https://github.com/ConnectWise-Advisories/Disclosures/tree/main/CVE-2026-127063)). This differs from Huntress's account of a blank key in versions 1.0.31 and 1.0.32, and a Huntress spokesperson told The Record that it has seen no evidence of a new vulnerability and that how the attacker got panel access is still unclear, while ConnectWise says the extension's API is protected by a passphrase the partner sets ([The Record, 2026-11-12](https://therecord.media/connectwise-screenconnect-breaches-third-party-tool)). Blackpoint reverse engineered the toolkit, saw unauthorised deployments through legitimate cloud-hosted instances but no successful propagation to a technician workstation, and calls the extensions' role in the first panel access unresolved ([Blackpoint, 2026-11-12](https://blackpointcyber.com/blog/screenconnect-attack-sckit/)).
