---
schema: 1
kind: threat
title: "CyberPower PowerPanel Business as a SYSTEM script channel on a domain controller: Symantec traces ntds.dit extraction with ntdsutil ifm and esentutl /vss and a side-loaded implant to scripts that the UPS-management service ppbed.exe runs as SYSTEM; Symantec does not say how the console was reached and no actor is named"
headline: "Symantec: attacker ran SYSTEM commands on a domain controller through CyberPower PowerPanel Business, then took ntds.dit"
summary: >
  Symantec analysed an intrusion in which the attacker used CyberPower PowerPanel Business, UPS-management software, as an execution channel on a Windows domain controller: scripts placed in the product's extcmd folder run through the ppbed.exe service as SYSTEM, and the operator iterated scripts until ntds.dit was exported with ntdsutil ifm and esentutl /vss, then side-loaded an implant. Symantec does not say how the attacker reached the console (public advisories or stolen administrator credentials could give that access) and names no actor.
discovered_at: "2026-11-19T05:20:00Z"
updated_at: null
event_date: "2026-11-18"
run_id: 2026-11-19T0355Z-intel
priority: notable
immediate_action: null
tags: [identity]
regions: [global]
sectors: [technology]
entities: ["incident:cyberpower-powerpanel-dc-intrusion-2026-11", "product:cyberpower-powerpanel-business"]
techniques: [T1072, T1059.003, T1059.001, T1105, T1140, T1620, T1003.003, T1574.001]
affected_products: ["CyberPower PowerPanel Business"]
cves: []
sources:
  - url: "https://www.security.com/threat-intelligence/power-management-software-attack-vector"
    publisher: "Symantec Threat Intelligence"
    date: "2026-11-18"
    role: primary
  - url: "https://www.cisa.gov/news-events/ics-advisories/icsa-24-123-01"
    publisher: "CISA (ICSA-24-123-01)"
    date: "2024-05-02"
    role: corroborating
  - url: "https://www.cyberpower.com/uk/en/product/series/powerpanel_business"
    publisher: "CyberPower (PowerPanel Business product page)"
    date: "2026-11-19"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The commands in this attack chain have ppbed.exe as their ancestor and run as SYSTEM."
    publisher: "Symantec Threat Intelligence"
    source_url: "https://www.security.com/threat-intelligence/power-management-software-attack-vector"
  - quote: "In process telemetry, the activity looks like a power-management product launching cmd.exe, which defenders may dismiss as a standard power-related recovery process without further investigation."
    publisher: "Symantec Threat Intelligence"
    source_url: "https://www.security.com/threat-intelligence/power-management-software-attack-vector"
  - quote: "Any of these, or stolen administrator credentials, could give an attacker the necessary console access to carry out the attack described in this blog."
    publisher: "Symantec Threat Intelligence"
    source_url: "https://www.security.com/threat-intelligence/power-management-software-attack-vector"
  - quote: "If you find them, assume Active Directory credentials are exposed and plan a krbtgt reset and wider credential rotation."
    publisher: "Symantec Threat Intelligence"
    source_url: "https://www.security.com/threat-intelligence/power-management-software-attack-vector"
verification: single-source
sourcing_note: >
  Symantec's analysis of one intrusion is the only source for the intrusion itself; it gives no date, victim sector, country or product version and attributes the activity to no actor. The second sources cover only the product: CISA's 2024 advisory on its weaknesses and CyberPower's own description of the command-execution feature. Symantec does not cite CISA's advisory, and the vendor and documentation pages carry no dateline, so their citations carry the retrieval date.
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "On every host that runs CyberPower PowerPanel Business, domain controllers first, compare the extcmd and temp\\profile\\extcmd folders with the product defaults and compare the extcmd folders and the console's event-to-command assignments with what administrators configured and treat unknown scripts as hostile; where the techniques Symantec lists are found (ntdsutil or esentutl on a domain controller, scripts staged under extcmd that no administrator configured, a side-loaded implant), assume Active Directory credentials are exposed and plan a krbtgt reset and wider credential rotation, because Symantec saw this channel used to export ntds.dit from a domain controller."
updates: []
migrated_from: null
---

Symantec analysed an intrusion in which the attacker used CyberPower PowerPanel Business (PPB), software that manages UPS devices, as the execution channel on a Windows domain controller ([Symantec, 2026-11-18](https://www.security.com/threat-intelligence/power-management-software-attack-vector)). Scripts placed in the product's extcmd folder and staged first under temp\profile\extcmd, are run by the PPB service ppbed.exe as SYSTEM, so the commands of the chain have ppbed.exe as their ancestor and the lineage runs ppbed.exe, cmd.exe, powershell.exe and then the implant ([Symantec, 2026-11-18](https://www.security.com/threat-intelligence/power-management-software-attack-vector)). The attacker pushed the scripts to the PPB web service endpoint /local/rest/v1/file/upload on TCP port 3052, worked hands-on, iterating scripts until ntds.dit was exported with ntdsutil ifm and esentutl /vss, and then side-loaded the implant, an old trusted executable paired with an unknown DLL in a user-profile path ([Symantec, 2026-11-18](https://www.security.com/threat-intelligence/power-management-software-attack-vector)). The channel is a documented product function: CyberPower describes user-programmable command executions for event actions ([CyberPower, 2026-11-19](https://www.cyberpower.com/uk/en/product/series/powerpanel_business)), and Symantec notes the attacker did not use power events to trigger them ([Symantec, 2026-11-18](https://www.security.com/threat-intelligence/power-management-software-attack-vector)).

Symantec does not say how the attacker reached the console; public advisories or stolen administrator credentials could give that access, and it names no actor, victim sector or product version ([Symantec, 2026-11-18](https://www.security.com/threat-intelligence/power-management-software-attack-vector)). CISA's 2024 advisory lists PowerPanel Business 4.9.0 and prior as affected by weaknesses fixed in version 4.10.1 or later, which Symantec does not cite ([CISA, 2024-05-02](https://www.cisa.gov/news-events/ics-advisories/icsa-24-123-01)).

**Exposure:** every host that runs PPB, a domain controller above all, whose web service on TCP 3052 a hostile network or a compromised administrator account can reach; Symantec says to audit the extcmd and temp\profile\extcmd paths of every PPB host against the product defaults ([Symantec, 2026-11-18](https://www.security.com/threat-intelligence/power-management-software-attack-vector)).

**Detection:** process-creation lineage with ppbed.exe as the ancestor of cmd.exe or powershell.exe, every script staged under extcmd, whatever its name, certutil downloads and decodes, curl downloads and powershell -ep bypass loading .NET code in memory, inbound requests to TCP 3052 from addresses that do not administer the UPS, and on a domain controller ntdsutil, esentutl and new shadow copies; an unexpected DLL next to a trusted binary in a user-profile path marks the side-loaded implant ([Symantec, 2026-11-18](https://www.security.com/threat-intelligence/power-management-software-attack-vector)).

**Triage:** the activity looks like a power-management product launching cmd.exe, which defenders may dismiss as a routine power-related recovery process; scripts or event-to-command assignments that no administrator configured, children that are not shutdown or notification routines (which follows from the mechanism) and the absence of a preceding power event separate it from benign use ([Symantec, 2026-11-18](https://www.security.com/threat-intelligence/power-management-software-attack-vector)).

**Defender takeaway:** treat PPB hosts as privileged execution surfaces: restrict TCP port 3052 to named administrator hosts, change the default administrator password and keep PPB patched, since CISA names 4.10.1 as the fixed build for its 2024 advisory ([Symantec, 2026-11-18](https://www.security.com/threat-intelligence/power-management-software-attack-vector); [CISA, 2024-05-02](https://www.cisa.gov/news-events/ics-advisories/icsa-24-123-01)); where the techniques Symantec lists are found, assume Active Directory credentials are exposed and plan a krbtgt reset and wider credential rotation ([Symantec, 2026-11-18](https://www.security.com/threat-intelligence/power-management-software-attack-vector)).
