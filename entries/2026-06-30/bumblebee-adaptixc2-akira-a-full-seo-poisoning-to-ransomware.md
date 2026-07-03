---
schema: 1
kind: threat
horizon: operational
title: "Bumblebee → AdaptixC2 → Akira: a full SEO-poisoning-to-ransomware kill chain with a parallel Swiss intrusion"
headline: "Bumblebee → AdaptixC2 → Akira: a full SEO-poisoning-to-ransomware kill chain with a parallel Swiss intrusion"
summary: The DFIR Report published (2026-06-29) the full reconstruction of an intrusion that began with SEO poisoning and ended in Akira ransomware in under three days.
discovered_at: "2026-06-30T05:10:44Z"
event_date: 2026-06-29
run_id: 2026-06-30-9aaa1114
priority: notable
immediate_action: null
tags:
  - ransomware
  - organized-crime
  - infostealer
regions:
  - switzerland
  - global
sectors:
  - technology
  - manufacturing
entities:
  - "incident:dfir-bumblebee-adaptixc2-akira-seo-poisoning-killchain"
  - "actor:akira"
cves: []
sources:
  - url: "https://thedfirreport.com/2026/06/29/from-bing-search-to-ransomware-bumblebee-and-adaptixc2-deliver-akira-3/"
    publisher: The DFIR Report
    role: primary
closed_sources: []
evidence: []
verification: single-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: true
deep_dive_category: ransomware-affiliate
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-30.md
---

The DFIR Report published (2026-06-29) the full reconstruction of an intrusion that began with SEO poisoning and ended in Akira ransomware in under three days. The report notes the case was first shared in a 2025 threat brief and flash alert produced with Swisscom B2B CSIRT, which observed a parallel intrusion tied to the same campaign — a Swiss-nexus thread (from that 2025 collaboration) that makes the now-public full reconstruction worth the day's deep dive ([The DFIR Report, 2026-06-29](https://thedfirreport.com/2026/06/29/from-bing-search-to-ransomware-bumblebee-and-adaptixc2-deliver-akira-3/)). It also features the open-source **AdaptixC2** post-exploitation framework as the Cobalt-Strike-equivalent in an Akira chain. Akira itself was deep-dived on 2026-06-23 via the SonicWall vector; this is a distinct initial-access path against the same end-stage operator.

**Initial access and loader.** A poisoned Bing result for "ManageEngine OpManager" led to a trojanized MSI installer (`T1608.006` SEO poisoning → [`T1204.002` Malicious File](https://attack.mitre.org/techniques/T1204/002/)). The **Bumblebee** loader established first C2 via [DLL search-order hijacking (`T1574.001`)](https://attack.mitre.org/techniques/T1574/001/) — a legitimate signed binary loading a same-directory `msimg32.dll` through `consent.exe`. Within ~5 hours, AdaptixC2 shellcode was injected into a renamed legitimate Windows Address Book utility, giving persistent interactive C2.

**Escalation, discovery, lateral movement.** The actor created domain accounts with Enterprise Admin privileges using RSAT ([`T1136.002` Create Account: Domain Account](https://attack.mitre.org/techniques/T1136/002/)), enumerated the network with SoftPerfect Network Scanner, Zenmap, and RVTools (`T1046`), and moved laterally over [RDP (`T1021.001`)](https://attack.mitre.org/techniques/T1021/001/). A legitimate **RustDesk** remote-access tool was installed as a redundant access channel ([`T1219` Remote Access Software](https://attack.mitre.org/techniques/T1219/)).

**Credential access and collection.** Credentials were harvested by extracting [NTDS.dit via `wbadmin.exe` (`T1003.003`)](https://attack.mitre.org/techniques/T1003/003/) and by dumping the Veeam backup database — the latter a recurring Akira-affiliate move that doubles as recovery sabotage. Roughly 77 GB was staged and exfiltrated over ~44 hours via FileZilla/SFTP to an external server (`T1048`/`T1567`).

**Impact.** [Akira ransomware (`T1486`)](https://attack.mitre.org/techniques/T1486/) was deployed across root and child domains over [WMI (`T1047`)](https://attack.mitre.org/techniques/T1047/), with shadow copies deleted via `vssadmin` ([`T1490` Inhibit System Recovery](https://attack.mitre.org/techniques/T1490/)).

**Detection concepts (no IOCs).** Per stage: Sysmon EID 1 for a signed binary / `consent.exe` side-loading `msimg32.dll` from a user-writable path; EID 11 for new executables written into AppData; EID 4104 for PowerShell carrying credential-access tradecraft; EID 4663 on NTDS.dit handle access; WMI-driven remote process creation (EID 4648 plus network logon type 3) from non-admin hosts; EID 4698 scheduled-task creation from unusual parents; and DLP/file-server alerts on large outbound SFTP staging. Treat any RustDesk install you did not deploy as a finding.

**Hardening.** Category-block software-download SEO traps at the SWG and require signed, hash-verified installers for IT-admin tooling; constrain who can create domain accounts and alert on new Enterprise Admin members; protect NTDS.dit / enable Credential Guard; restrict remote WMI to tiered admin hosts; harden Veeam service-account credentials and isolate the backup plane; and alert on unsanctioned remote-access tools (RustDesk/AnyDesk) at the proxy and EDR.
