---
schema: 1
kind: threat
title: "Kaspersky GERT: two ESXi and Proxmox ransomware cases in which a monitoring server's reused root password and plaintext administrator notes, not a VM escape, gave the attackers the hypervisor"
headline: "Kaspersky: ESXi and Proxmox ransomware ran on a monitoring server's root password and admin notes, no VM escape"
summary: >
  Kaspersky's Global Emergency Response Team describes two ransomware cases in virtualised estates. In the BlackNevas case a PRTG Network Monitor held ESXi root access and the same root password was reused across hosts, so the attacker connected over SSH, disabled the execInstalledOnly policy with esxcli, ran the encryptor and deleted logs; in the case attributed to The Gentlemen the actor found Proxmox root credentials in plaintext notes on an administrator workstation and used the VNC web socket to encrypt the cluster. Kaspersky stresses that no VM escape was needed.
discovered_at: "2026-11-07T04:00:00Z"
updated_at: null
event_date: "2026-11-06"
run_id: 2026-11-07T0256Z-intel
priority: notable
immediate_action: null
tags: [ransomware]
regions: [global]
sectors: []
entities: ["actor:blacknevas", "actor:thegentlemen", "product:proxmox-ve", "product:paessler-prtg-network-monitor"]
techniques: [T1078.003, T1021.004, T1021.005, T1552.001, T1685, T1685.006, T1486, T1219]
affected_products: ["VMware ESXi", "Proxmox VE", "Paessler PRTG Network Monitor"]
cves: []
sources:
  - url: "https://securelist.com/virtualization-security-esxi-and-proxmox-ransomware-cases/121819/"
    publisher: "Kaspersky Global Emergency Response Team (Securelist)"
    date: "2026-11-06"
    role: primary
closed_sources: []
evidence:
  - quote: "A monitoring system that could reach the virtualization layer also exposed a reusable root credential."
    publisher: "Kaspersky Global Emergency Response Team (Securelist)"
    source_url: "https://securelist.com/virtualization-security-esxi-and-proxmox-ransomware-cases/121819/"
  - quote: "No VM escape was required."
    publisher: "Kaspersky Global Emergency Response Team (Securelist)"
    source_url: "https://securelist.com/virtualization-security-esxi-and-proxmox-ransomware-cases/121819/"
  - quote: "Password reuse converted one recovered secret into farm-wide access."
    publisher: "Kaspersky Global Emergency Response Team (Securelist)"
    source_url: "https://securelist.com/virtualization-security-esxi-and-proxmox-ransomware-cases/121819/"
verification: single-source
sourcing_note: >
  Kaspersky's incident-response team is the only source and describes its own investigations; neither case states how the attacker first got in or how long the dwell time lasted, the first case is dated 2025-10-18 and 2025-10-19, and the second case's log timestamps do not show whether the day or the month comes first. One of Kaspersky's seven recommendations is a pitch for its own product and is not used here.
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
  - "List every monitoring server, script, scheduled task and connection manager that stores an ESXi, vCenter or Proxmox root password, replace each with a least-privilege monitoring account, and rotate the root passwords that were stored or reused across hosts."
updates: []
migrated_from: null
---

In the first case, Kaspersky's investigation began with BlackNevas ransomware activity on a Windows system in a virtualised domain-controller segment, where the execution of the AnyDesk remote tool and the GMER binary was recorded ([Kaspersky GERT, 2026-11-06](https://securelist.com/virtualization-security-esxi-and-proxmox-ransomware-cases/121819/)). The environment used PRTG Network Monitor, whose deployment had broad access to the ESXi hosts, and the same root password was reused across several nodes; after obtaining access to the monitoring environment the attacker used the ESXi credential to connect over SSH to the hosts that shared the password ([Kaspersky GERT, 2026-11-06](https://securelist.com/virtualization-security-esxi-and-proxmox-ransomware-cases/121819/)). On the first host, a file was uploaded during a root SSH session and its first execution failed with "Execution of non-installed file prevented"; the actor then disabled the execInstalledOnly policy with esxcli and ran it, while on a second host in another subnet with the same password the binary ran and the logs were cleared ([Kaspersky GERT, 2026-11-06](https://securelist.com/virtualization-security-esxi-and-proxmox-ransomware-cases/121819/)).

In the second case, a ransomware incident by The Gentlemen, the actor used information it had collected between initial access and visible impact: on a compromised system administrator's workstation it found Proxmox root credentials and access details in plain-text notes and logged in as root ([Kaspersky GERT, 2026-11-06](https://securelist.com/virtualization-security-esxi-and-proxmox-ransomware-cases/121819/)). It then activated the VNC web socket through the root account, which gave it control of the Proxmox environment, and used that access to download and run the ransomware in the cluster, encrypting the whole virtual environment ([Kaspersky GERT, 2026-11-06](https://securelist.com/virtualization-security-esxi-and-proxmox-ransomware-cases/121819/)). Kaspersky says a fully patched hypervisor can still be compromised through a shared password, an overprivileged monitoring account, an open SSH path or an administrator interface reachable from a general server network ([Kaspersky GERT, 2026-11-06](https://securelist.com/virtualization-security-esxi-and-proxmox-ransomware-cases/121819/)).

**Exposure:** a virtualisation estate where a monitoring, backup or management server stores or can use hypervisor root credentials, where one root password is shared across hosts, where SSH to ESXi is reachable from general server networks, or where administrators keep Proxmox or ESXi credentials in plain-text notes; PRTG, which supports storing VMware credentials at device or group level, is the product Kaspersky names ([Kaspersky GERT, 2026-11-06](https://securelist.com/virtualization-security-esxi-and-proxmox-ransomware-cases/121819/)).

**Detection:** on ESXi, root SSH logins from addresses that do not normally administer the hosts, a file upload followed by a failed execution of a non-installed file, a change to the execInstalledOnly setting and cleared logs; on Proxmox, root@pam requests to the VNC web socket used to reach other hosts, as the log records Kaspersky shows ([Kaspersky GERT, 2026-11-06](https://securelist.com/virtualization-security-esxi-and-proxmox-ransomware-cases/121819/)). Kaspersky advises alerting when execInstalledOnly, Secure Boot enforcement, Lockdown Mode, SSH, local accounts or remote logging settings change ([Kaspersky GERT, 2026-11-06](https://securelist.com/virtualization-security-esxi-and-proxmox-ransomware-cases/121819/)).

**Defender takeaway:** give each monitoring platform its own least-privilege identity instead of ESXi root, replace stored root passwords with vault retrieval or limited tokens, administer ESXi through vCenter with Lockdown Mode and SSH stopped by default, and keep logs off the hosts so a compromised administrator cannot erase them ([Kaspersky GERT, 2026-11-06](https://securelist.com/virtualization-security-esxi-and-proxmox-ransomware-cases/121819/)).
