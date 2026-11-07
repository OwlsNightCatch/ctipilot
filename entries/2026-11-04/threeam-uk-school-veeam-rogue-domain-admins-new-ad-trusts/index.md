---
schema: 1
kind: incident
title: "3AM ransomware affiliate in a UK school estate: Bitdefender documents backup-credential theft, rogue domain admins and new two-way trusts between Active Directory domains, with a command-retry pattern it reads as a model-driven loop"
headline: "Bitdefender: a 3AM affiliate joined a school estate's AD domains with new trusts after stealing Veeam credentials"
summary: >
  Bitdefender MDR describes a September 2026 intrusion by a 3AM ransomware affiliate into a UK school estate that began as several unconnected Active Directory domains: a modified public Veeam script
  decrypted credentials stored on three backup servers, the attacker created two backdoor domain-administrator accounts, joined three domains with new two-way trusts within about three hours, tried to remove EDR agents (anti-tampering blocked it) and
  encrypted machines. Initial access is unknown, every attacker action Bitdefender saw came from an unmanaged internal host, and Bitdefender reads the 40 to 101 second retry cadence as a model-driven loop, flagged as its own interpretation;
  it says a new trust between domains is a rare change that is cheap to alert on.
discovered_at: "2026-11-04T03:55:00Z"
updated_at: null
event_date: "2026-11-03"
run_id: 2026-11-04T0256Z-intel
priority: notable
immediate_action: null
tags: [ransomware, ai-abuse]
regions: [uk]
sectors: [education, public-sector]
entities: ["malware:threeam", "incident:uk-school-estate-3am-hybrid-ai-intrusion-2026-09"]
techniques: [T1555, T1555.003, T1003.001, T1482, T1087, T1136.002, T1484.002, T1047, T1059.001, T1053.005, T1021.002, T1036, T1074, T1112, T1041, T1490, T1685, T1486]
affected_products: ["Veeam Backup & Replication"]
cves: []
sources:
  - url: "https://businessinsights.bitdefender.com/3am-ransomware-hybrid-ai-attack"
    publisher: "Bitdefender Business Insights"
    date: "2026-11-03"
    role: primary
closed_sources: []
evidence:
  - quote: "a new trust between domains is a rare change and cheap to alert on."
    publisher: "Bitdefender"
    source_url: "https://businessinsights.bitdefender.com/3am-ransomware-hybrid-ai-attack"
  - quote: "We were not able to access the machine the attacker worked from, so we cannot document anything about the language model itself"
    publisher: "Bitdefender"
    source_url: "https://businessinsights.bitdefender.com/3am-ransomware-hybrid-ai-attack"
verification: single-source
sourcing_note: >
  Bitdefender MDR's own investigation is the only source. It attributes the intrusion to a 3AM affiliate on the encryptor build and command-line pattern, says initial access is unknown, and presents the
  hybrid human-and-model reading as interpretation, not a finding, because the host the attacker worked from was unmanaged and outside its visibility.
confidence: medium
references: []
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

Bitdefender MDR attributes the intrusion to a 3AM (ThreeAM) ransomware affiliate on the encryptor build and its command-line pattern; the target was a school estate in the UK whose domains began as separate Active Directory environments, and initial access is unknown ([Bitdefender, 2026-11-03](https://businessinsights.bitdefender.com/3am-ransomware-hybrid-ai-attack)). In September 2026 the attacker first took credentials from the backup software: a modified copy of a public script read the credentials stored in Veeam's databases on three backup servers and decrypted them with the Windows Data Protection API, and a browser credential database was copied from a terminal server ([Bitdefender, 2026-11-03](https://businessinsights.bitdefender.com/3am-ransomware-hybrid-ai-attack)). It then worked with built-in tools (PowerShell, WMI, reg, netsh, rundll32) and a few public ones (an Impacket-like remote-execution tool that returns output over administrative shares, Mimikatz renamed to look like a monitoring binary), enumerated domain trusts from a domain controller, searched SYSVOL logon scripts for the names and subnets of other schools, created two backdoor domain-administrator accounts, joined three separate domains with two-way trusts within about three hours, tried to remove EDR agents, which anti-tampering controls blocked, deleted system-state backups and encrypted machines with a Rust-based encryptor ([Bitdefender, 2026-11-03](https://businessinsights.bitdefender.com/3am-ransomware-hybrid-ai-attack)).

Bitdefender's reading, which it calls interpretation and not a finding, is that a model drove part of the work: commands call the Veeam web interface on a port and with a login method that do not match the vendor documentation, output is self-labelled, scripts carry numbered revisions, and retries arrive 40 to 101 seconds apart whatever the size of the change, while a new task takes minutes. Every attacker action Bitdefender saw came from an unmanaged internal host with no agent, so the automation itself was never seen, and Bitdefender says it could not document anything about a language model ([Bitdefender, 2026-11-03](https://businessinsights.bitdefender.com/3am-ransomware-hybrid-ai-attack)).

**Exposure:** a Windows estate that runs Veeam Backup & Replication and has several Active Directory domains or a flat network that an unmanaged internal host can reach; the unmanaged host is the gap, because it ran no agent and sat outside Bitdefender's visibility.

**Detection:** in directory-service change events, new trust relationships between domains, which Bitdefender calls a rare change that is cheap to alert on, and new domain-administrator group members; in backup-server logs, Veeam web-interface calls and credential-store reads from hosts that are not backup administrators'; in endpoint telemetry, saves of the SECURITY, SYSTEM or SAM registry hives by any process that is not a known backup or administration job, LSASS access, a Windows Defender exclusion for the temporary directory, and the same command re-issued with small edits at a steady cadence; across hosts, file contents staged into registry values, which Bitdefender calls an unusual channel and a strong indicator to hunt for, and sent out by HTTP POST to an internal host, and probe or confirmation artifacts such as a scheduled task named for the probe left on production hosts; in authentication logs, unmanaged hosts authenticating to domain controllers ([Bitdefender, 2026-11-03](https://businessinsights.bitdefender.com/3am-ransomware-hybrid-ai-attack)).

**Defender takeaway:** alert on any new domain trust and on additions to the domain-administrator groups, alert on credential-reading access to backup-software databases and on saves of the SECURITY, SYSTEM or SAM hives outside known backup or administration jobs, put an endpoint agent on every machine because the staging host here was unmanaged, and limit remote execution and administrative shares to known management hosts ([Bitdefender, 2026-11-03](https://businessinsights.bitdefender.com/3am-ransomware-hybrid-ai-attack)).
