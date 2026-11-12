---
schema: 1
kind: threat
title: "ScreenConnect: commands pushed through Run Command to at least 288 managed endpoints at 48 Huntress customers within 90 minutes on 2026-11-11 installed a rogue second client and the SCKit toolkit; Huntress links the activity to the RMM+ extension, whose versions 1.0.31 and 1.0.32 accepted a blank access key"
headline: "ScreenConnect: rogue clients pushed to 288+ endpoints; Huntress ties it to RMM+ extension with blank access key"
summary: >
  Huntress saw an operator use access to several cloud-hosted ScreenConnect panels on 2026-11-11 to run Run Command as SYSTEM on groups of managed endpoints, installing an attacker-controlled second ScreenConnect client and the SCKit toolkit on at least 288 hosts at 48 organisations within 90 minutes; Sophos independently saw the same client deployments. Huntress later said the activity seems related to the third-party RMM+ extension, whose versions 1.0.31 and 1.0.32 accepted a blank access key and bypass ScreenConnect's accounts and MFA, while ConnectWise had not identified an initial access vector and disabled five third-party extensions in about 400 partner environments, a containment step that removes nothing already installed.
discovered_at: "2026-11-12T04:07:00Z"
updated_at: null
event_date: "2026-11-11"
run_id: 2026-11-12T0255Z-intel
priority: high
immediate_action: null
tags: [supply-chain]
regions: [global]
sectors: [technology]
entities: ["incident:screenconnect-sckit-msp-compromise-2026-11", "malware:sckit"]
techniques: [T1072, T1219.002, T1059.003, T1059.001, T1105, T1218.007, T1685, T1053.005, T1547.001, T1489, T1027, T1539, T1550.004]
affected_products: ["ConnectWise ScreenConnect"]
cves: []
sources:
  - url: "https://www.huntress.com/blog/sckit-worm-rogue-screenconnect"
    publisher: "Huntress"
    date: "2026-11-11"
    role: primary
  - url: "https://www.sophos.com/en-us/blog/malicious-screenconnect-deployments-observed"
    publisher: "Sophos"
    date: "2026-11-11"
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/active-screenconnect-attacks-breach-msps-impact-dozens-of-organizations/"
    publisher: "BleepingComputer"
    date: "2026-11-11"
    role: corroborating
closed_sources: []
evidence:
  - quote: "On November 11, 2026, Huntress observed an operator using access to multiple cloud-hosted ScreenConnect panels to push commands to groups of managed endpoints."
    publisher: "Huntress"
    source_url: "https://www.huntress.com/blog/sckit-worm-rogue-screenconnect"
  - quote: "The legitimate installation of ScreenConnect is then stopped, set to manual start, and the attacker controlled copy of ScreenConnect positioned to replace it."
    publisher: "Huntress"
    source_url: "https://www.huntress.com/blog/sckit-worm-rogue-screenconnect"
  - quote: "Disabling these 3rd party extensions is a precautionary containment measure. It does not establish that unauthorized software, persistence mechanisms, or access already present on affected devices has been removed"
    publisher: "BleepingComputer (quoting the ConnectWise advisory)"
    source_url: "https://www.bleepingcomputer.com/news/security/active-screenconnect-attacks-breach-msps-impact-dozens-of-organizations/"
  - quote: "versions 1.0.31 and 1.0.32 contained a serious authentication flaw"
    publisher: "Huntress"
    source_url: "https://www.huntress.com/blog/sckit-worm-rogue-screenconnect"
verification: multi-source
sourcing_note: "Huntress and Sophos report the activity from their own telemetry and the Sophos client identifiers match Huntress's; Huntress's update of 2026-11-11 at 11:34 pm ET names RMM+ and its blank-access-key flaw from its own analysis. ConnectWise's advisory was not readable, so its statements come from the sentences BleepingComputer quotes, written before that update, and from Huntress's account of it. No source names an actor or a victim; the technician-workstation stage is reconstructed from code and Huntress says it never saw it succeed."
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
  - "On every ScreenConnect instance your organisation or its IT providers run, review Run Command and Toolbox history and the instance audit logs for executions nobody started, including before 2026-11-11, check managed endpoints for a second ScreenConnect client service, and disable the five named extensions (on-premises instances by hand), RMM+ versions 1.0.31 and 1.0.32 first because they accept a blank access key; open no interactive session to a suspect host, use EDR live response or WinRM, because a session can trigger the toolkit to spread to the technician's workstation."
updates: []
migrated_from: null
---

On 2026-11-11 Huntress observed an operator using access to several cloud-hosted ScreenConnect panels to run commands as SYSTEM on groups of managed endpoints through the Run Command feature, hitting at least 288 hosts at 48 organisations that use Huntress within 90 minutes ([Huntress, 2026-11-11](https://www.huntress.com/blog/sckit-worm-rogue-screenconnect)). Each host checked for a ScreenConnect client, silently installed an attacker-controlled one, wrote a dropper and fetched SCKit, a 16-file toolkit delivered encrypted whose decryption values the server issues against the requesting machine's UUID ([Huntress, 2026-11-11](https://www.huntress.com/blog/sckit-worm-rogue-screenconnect)). The kit adds Defender exclusions, installs a second attacker-controlled client, sets the legitimate client to manual start so the attacker's copy replaces it, and runs a per-host executable from a scheduled task ([Huntress, 2026-11-11](https://www.huntress.com/blog/sckit-worm-rogue-screenconnect)).

Huntress's later update says the activity seems related to RMM+, a third-party extension that bypasses ScreenConnect's user accounts, roles and MFA and authenticates requests with a shared access key: versions 1.0.31 and 1.0.32 accepted a blank key when an administrator had never set one, commands reached endpoints across several instances within minutes with no corresponding login activity and were linked in the logs to RMM+; most RMM+ installations it saw were legitimate ([Huntress, 2026-11-11](https://www.huntress.com/blog/sckit-worm-rogue-screenconnect)). ConnectWise suspects the actor used independent third-party extensions that partners may have added, and disabled five (Labtech Plus, RMM Plus, RMM+, RMM Plus Password Link and RMM+ Password Link) in about 400 partner environments; on-premises customers must disable them by hand ([BleepingComputer, 2026-11-11](https://www.bleepingcomputer.com/news/security/active-screenconnect-attacks-breach-msps-impact-dozens-of-organizations/)); Huntress says ConnectWise had not yet identified an initial access vector or the full scope ([Huntress, 2026-11-11](https://www.huntress.com/blog/sckit-worm-rogue-screenconnect)). Huntress reconstructs a second stage meant to spread through the connecting technician's panel but saw no successful jump ([Huntress, 2026-11-11](https://www.huntress.com/blog/sckit-worm-rogue-screenconnect)). Huntress says sequential attacker tags suggest other MSPs were compromised earlier; BleepingComputer found a batch script first uploaded on 2026-07-25 that references one of Huntress's rogue client IDs, its link to this campaign unclear ([BleepingComputer, 2026-11-11](https://www.bleepingcomputer.com/news/security/active-screenconnect-attacks-breach-msps-impact-dozens-of-organizations/)).

**Exposure:** a ScreenConnect instance whose panel can run commands on managed endpoints, run by the organisation or an IT provider; an RMM+ extension at version 1.0.31 or 1.0.32 with RMMPlus.AccessKey left blank is the condition Huntress describes, and the Extensions list shows which of the five named extensions are installed; an endpoint shows a second ScreenConnect client service pointing at a relay that is not your own.

**Detection:** ScreenConnect instance audit logs, Run Command and Toolbox history for mass executions nobody started, and RMM+ requests with no matching login; process-creation telemetry with the ScreenConnect client service as parent of cmd, PowerShell or msiexec; curl or PowerShell downloads followed by a silent msiexec install, the pattern Sophos describes; a second client service installed, Defender exclusions added, the legitimate client's start type changed to manual, and a new scheduled task running as SYSTEM ([Huntress, 2026-11-11](https://www.huntress.com/blog/sckit-worm-rogue-screenconnect); [Sophos, 2026-11-11](https://www.sophos.com/en-us/blog/malicious-screenconnect-deployments-observed)). Isolation does not remove the persistence; hosts reinfected afterwards ([Huntress, 2026-11-11](https://www.huntress.com/blog/sckit-worm-rogue-screenconnect)).

**Defender takeaway:** treat Run Command or Toolbox executions you did not start as a compromise, not a misconfiguration; remove or disable RMM+ and the other four extensions, verify the legitimate client before removing anything, rotate ScreenConnect credentials and revoke active sessions from a clean device, revoke the browser and identity-provider sessions the toolkit could steal, and keep hosts out of service until the rogue client and persistence are gone ([Huntress, 2026-11-11](https://www.huntress.com/blog/sckit-worm-rogue-screenconnect)). Disabling the five extensions is precautionary containment that removes nothing already installed ([BleepingComputer, 2026-11-11](https://www.bleepingcomputer.com/news/security/active-screenconnect-attacks-breach-msps-impact-dozens-of-organizations/)).
