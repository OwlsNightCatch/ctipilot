---
schema: 1
kind: threat
title: "Seqrite: reverse engineering of two Qilin builds shows the October 2026 variant adding a vCenter and ESXi spreading engine, Restart Manager lock release, a Safe Mode reboot loop and ransom notes printed to office printers"
headline: "Qilin's October build spreads through vCenter and ESXi, reboots into Safe Mode and prints notes on office printers"
summary: >
  Seqrite compares a March 2026 and an October 2026 Qilin (Agenda) sample and reports that the newer build embeds a PowerShell engine that logs in to vCenter, disables HA and DRS and
  pushes Linux payloads to ESXi hosts over SSH, shuts down the processes that lock files through the Windows Restart Manager instead of brute-force termination, sets a Safe Mode reboot so EDR drivers do not load,
  and sends ransom notes to TCP 9100 on local subnets. It is a vendor analysis of two samples with no incident confirmation.
discovered_at: "2026-11-06T03:50:00Z"
updated_at: null
event_date: "2026-11-03"
run_id: 2026-11-06T0255Z-intel
priority: notable
immediate_action: null
tags: [ransomware]
regions: [global]
sectors: [healthcare, education]
entities: ["actor:qilin", "product:vmware-vcenter-server", "product:vmware-esxi"]
techniques: [T1486, T1490, T1489, T1688, T1021.002, T1569.002, T1018, T1059.001, T1021.004, T1570, T1036.001]
affected_products: ["VMware vCenter Server", "VMware ESXi"]
cves: []
sources:
  - url: "https://www.seqrite.com/blog/the-evolution-of-qilin-agenda-a-comparative-reverse-engineering-analysis-of-qilin-agenda-ransomware-across-2026/"
    publisher: "Seqrite Labs"
    date: "2026-11-03"
    role: primary
closed_sources: []
evidence:
  - quote: "the evolved binary contains a modular 20.8 KB PowerShell automation suite (–spread-vcenter). It authenticates to VMware vCenter servers, disables High Availability (HA) and Distributed Resource Scheduler (DRS), extracts ESXi hypervisor IP addresses, and establishes SSH/SCP sessions."
    publisher: "Seqrite Labs"
    source_url: "https://www.seqrite.com/blog/the-evolution-of-qilin-agenda-a-comparative-reverse-engineering-analysis-of-qilin-agenda-ransomware-across-2026/"
  - quote: "Detection of both Qilin strains is possible using static and behavior-based signatures, such as bcdedit Safe Mode modification and rstrtmgr.dll process termination."
    publisher: "Seqrite Labs"
    source_url: "https://www.seqrite.com/blog/the-evolution-of-qilin-agenda-a-comparative-reverse-engineering-analysis-of-qilin-agenda-ransomware-across-2026/"
verification: single-source
sourcing_note: >
  Seqrite is the only source: a vendor comparison of one March 2026 and one October 2026 sample that names no victim, no initial-access route and no incident in which the October build ran. The capabilities are what the reverse engineering found in the binary; how often affiliates use them is not stated.
confidence: medium
references:
  - 2026-09-21/qilin-ai-generated-wiper-locker-scripts-forensic-markers
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 3
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

Seqrite's reverse engineering of a March 2026 and an October 2026 Qilin (Agenda) sample finds that the Rust code was reworked into a modular workspace of 22 internal crates, that the command line grew from 6 to 42 switches, and that the October build carries subsystems the baseline lacked ([Seqrite Labs, 2026-11-03](https://www.seqrite.com/blog/the-evolution-of-qilin-agenda-a-comparative-reverse-engineering-analysis-of-qilin-agenda-ransomware-across-2026/)). It uses the Windows Restart Manager API to shut down the processes that lock SQL Server, Exchange and virtual-machine disk files, instead of the brute-force process termination of the March sample, so that the files can be encrypted ([Seqrite Labs, 2026-11-03](https://www.seqrite.com/blog/the-evolution-of-qilin-agenda-a-comparative-reverse-engineering-analysis-of-qilin-agenda-ransomware-across-2026/)). An embedded PowerShell engine, started with `--spread-vcenter`, authenticates to vCenter, disables HA and DRS, extracts the ESXi host addresses, opens SSH and SCP sessions, uploads Linux ransomware payloads to /tmp on the hosts and runs esxcli to power off virtual machines and encrypt .vmdk volumes ([Seqrite Labs, 2026-11-03](https://www.seqrite.com/blog/the-evolution-of-qilin-agenda-a-comparative-reverse-engineering-analysis-of-qilin-agenda-ransomware-across-2026/)).

The build also installs the RSAT Active Directory module itself with DISM before enumerating computers, embeds 32-bit and 64-bit PsExec to spread over the ADMIN$ and C$ shares with harvested credentials, and sets a Safe Mode boot with bcdedit plus an AutoAdminLogon registry value so that it reboots into Safe Mode, where EDR drivers do not load ([Seqrite Labs, 2026-11-03](https://www.seqrite.com/blog/the-evolution-of-qilin-agenda-a-comparative-reverse-engineering-analysis-of-qilin-agenda-ransomware-across-2026/)). A raw-printing module scans local subnets for TCP port 9100 and sends cleartext ransom notes to office printers, and the October binary masquerades as resmon.exe with a forged Microsoft code-signing overlay ([Seqrite Labs, 2026-11-03](https://www.seqrite.com/blog/the-evolution-of-qilin-agenda-a-comparative-reverse-engineering-analysis-of-qilin-agenda-ransomware-across-2026/)). Seqrite lists healthcare, manufacturing, education and technology as the victim sectors in its telemetry ([Seqrite Labs, 2026-11-03](https://www.seqrite.com/blog/the-evolution-of-qilin-agenda-a-comparative-reverse-engineering-analysis-of-qilin-agenda-ransomware-across-2026/)).

**Exposure:** Windows estates with a vCenter and ESXi hosts that a domain-joined host can reach over the network and SSH, since the spreading engine needs a vCenter login and SSH to the hosts; Seqrite names no initial-access route.

**Detection:** in vCenter audit events, HA or DRS being disabled on a cluster followed by SSH sessions to ESXi hosts and esxcli activity; in process-creation and registry telemetry, bcdedit setting a Safe Mode boot and a Winlogon AutoAdminLogon change outside a change window, DISM installing the RSAT Active Directory component on a host that never had it, and rstrtmgr.dll loaded by a process that is not an installer; in network telemetry, one host sending to TCP 9100 on many hosts of a subnet; and an executable named resmon.exe outside System32 ([Seqrite Labs, 2026-11-03](https://www.seqrite.com/blog/the-evolution-of-qilin-agenda-a-comparative-reverse-engineering-analysis-of-qilin-agenda-ransomware-across-2026/)).

**Triage:** the Restart Manager and a DISM-installed RSAT component are normal in patching and administration, so each is weak alone; the combination with the print fan-out, the Safe Mode change and the vCenter actions is the signal.

**Defender takeaway:** treat HA or DRS being turned off in vCenter, followed by SSH sessions to ESXi hosts, as an incident, and alert on a Safe Mode boot configured by bcdedit outside change windows, which Seqrite names as a detection point ([Seqrite Labs, 2026-11-03](https://www.seqrite.com/blog/the-evolution-of-qilin-agenda-a-comparative-reverse-engineering-analysis-of-qilin-agenda-ransomware-across-2026/)).
