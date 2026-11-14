---
schema: 1
kind: threat
title: "Kaspersky GERT BlackNevas case: credentials from systems outside the virtualisation layer reach both vCenter appliances, a remote-access agent and a VMware-lookalike tunnel service persist, vCenter Host Profile remediation switches SSH on across the ESXi hosts, backups are destroyed first and a wipe of the datastores detonates over ten days, with no vulnerability exploited"
headline: "Kaspersky: BlackNevas used vCenter Host Profiles to enable SSH on ESXi, destroyed backups first, then wiped datastores"
summary: "Kaspersky GERT describes a ten-day engagement in which an adversary, identified as BlackNevas from its ransom notes, used credentials taken from systems outside the virtualisation layer to reach both vCenter appliances, persisted on one with a remote-access agent and a tunnel installed as a VMware-lookalike systemd service, then used vCenter Host Profile remediation to switch SSH on across four ESXi hosts, destroyed the backup environment first and detonated a wiper-capable locker that took every virtual machine. Kaspersky states no initial access vector, victim sector or country, and no virtualisation-layer vulnerability was exploited."
discovered_at: "2026-11-14T04:20:00Z"
updated_at: null
event_date: "2026-11-13"
run_id: 2026-11-14T0255Z-intel
priority: notable
immediate_action: null
tags: [ransomware]
regions: [global]
sectors: []
entities: ["actor:blacknevas"]
techniques: [T1078, T1021.004, T1219, T1543.002, T1036.005, T1572, T1105, T1685, T1489, T1490, T1486, T1485]
affected_products: ["VMware vCenter Server", "VMware ESXi"]
cves: []
sources:
  - url: "https://securelist.com/esxi-ransomware/121959/"
    publisher: "Kaspersky GERT (Securelist)"
    date: "2026-11-13"
    role: primary
closed_sources: []
evidence:
  - quote: "recently investigated an engagement in which an adversary destroyed an organization’s virtualization estate over a 10-day period."
    publisher: "Kaspersky GERT"
    source_url: "https://securelist.com/esxi-ransomware/121959/"
  - quote: "Subsequently, direct SSH access to the target ESXi hosts originated from the vCenter appliance IP, a source that would normally be considered highly trusted on the management network."
    publisher: "Kaspersky GERT"
    source_url: "https://securelist.com/esxi-ransomware/121959/"
  - quote: "In this incident, backup infrastructure was not collateral damage."
    publisher: "Kaspersky GERT"
    source_url: "https://securelist.com/esxi-ransomware/121959/"
verification: single-source
sourcing_note: "Kaspersky GERT is the only source and reports one engagement it investigated; it names no victim, sector, country or incident dates and does not state the initial access vector. The attribution to BlackNevas rests on ransom notes and on the encryptor's argument style resembling the Trigona and BlackNevas command-line family, which Kaspersky says strengthens attribution but does not replace a binary match, and no hashes were available. Kaspersky's indicator table also names an installed service and a remote-management agent, which are deliberately not carried. This is a different engagement from the BlackNevas case in Kaspersky's earlier report: the access path and the management-plane technique differ."
confidence: medium
references:
  - 2026-11-07/kaspersky-esxi-proxmox-ransomware-monitoring-root-password
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

Kaspersky GERT describes an engagement in which an adversary destroyed an organisation's virtualisation estate over ten days: four ESXi hosts, every virtual machine on them, both vCenter Server Appliances and all connected backup infrastructure ([Kaspersky GERT, 2026-11-13](https://securelist.com/esxi-ransomware/121959/)). No virtualisation-layer vulnerability was exploited: credentials obtained from non-virtualisation systems inside the perimeter reached the appliances, and every action against ESXi ran through legitimate VMware management interfaces ([Kaspersky GERT, 2026-11-13](https://securelist.com/esxi-ransomware/121959/)). The activity is attributed to BlackNevas through the ransom notes ([Kaspersky GERT, 2026-11-13](https://securelist.com/esxi-ransomware/121959/)).

The attackers logged in as root over SSH to the vCenter appliance that manages virtualisation disaster recovery, fetched and deployed MeshAgent with a shell script 43 seconds later, and about four hours later returned through MeshAgent to install the Ligolo-ng tunnel as a persistent systemd unit whose name, description and Restart=always imitate appliance housekeeping ([Kaspersky GERT, 2026-11-13](https://securelist.com/esxi-ransomware/121959/)). They then used vCenter Host Profiles to change the TSM-SSH service state: eleven minutes after the first configuration read SSH was enabled on the target ESXi hosts, and direct SSH to the hosts then came from the vCenter appliance address ([Kaspersky GERT, 2026-11-13](https://securelist.com/esxi-ransomware/121959/)). Payloads went to ESXi over SFTP, a self-test of the executable ran about three hours before the final detonation, and about the first 2 KB of the virtual disk files were overwritten ([Kaspersky GERT, 2026-11-13](https://securelist.com/esxi-ransomware/121959/)). The backup environment fell first: the attacker extracted stored credentials after gaining administrative execution on the backup infrastructure, disabled antivirus there days earlier, then stopped backup services and encrypted the recovery infrastructure, all before ESXi detonation ([Kaspersky GERT, 2026-11-13](https://securelist.com/esxi-ransomware/121959/)).

**Exposure:** a vCenter and ESXi estate where accounts from systems outside the virtualisation layer can reach the vCenter appliances and where Host Profile remediation can change the SSH service state; the article names no version ([Kaspersky GERT, 2026-11-13](https://securelist.com/esxi-ransomware/121959/)).

**Detection:** in vCenter events and tasks and in vpxa.log and vobd.log, Host Profile remediation that changes TSM or TSM-SSH from policy-disabled to running outside an approved change window, which Kaspersky rates critical when an SSH session from vCenter or another management appliance to the same host follows within 15 minutes; on the vCenter appliance, a new VMware-looking systemd unit absent from the organisation's list of trusted services; in ESXi shell logs, execution of a newly staged executable under /tmp followed by access to /vmfs; and preserved hostprofiletrace.log ([Kaspersky GERT, 2026-11-13](https://securelist.com/esxi-ransomware/121959/)). ESXi logs sit in a ramdisk that is cleared at reboot, so Kaspersky says not to begin by rebooting a host ([Kaspersky GERT, 2026-11-13](https://securelist.com/esxi-ransomware/121959/)).

**Triage:** each Host Profile step is legitimate alone, so the distinguishing context is authorisation, timing, source account, change window and whether the desired state weakens security; a VMware-looking service is not malicious by default, since custom integrations exist, but one absent from the trusted list is a high-confidence anomaly, and chmod +x is ambiguous alone while execution of a newly staged executable from /tmp is itself a strong indicator ([Kaspersky GERT, 2026-11-13](https://securelist.com/esxi-ransomware/121959/)).

**Defender takeaway:** treat the vCenter appliances as the control plane to protect: alert on Host Profile changes to TSM-SSH outside change windows and on SSH from vCenter to ESXi that follows them, review VMware-looking services on the appliances against a trusted list, and keep backup-platform credentials and administration separate from the systems that can reach vCenter, because the backup environment was destroyed before the hosts ([Kaspersky GERT, 2026-11-13](https://securelist.com/esxi-ransomware/121959/)).
