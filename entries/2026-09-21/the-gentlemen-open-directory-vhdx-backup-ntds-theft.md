---
schema: 1
kind: threat
title: "The Gentlemen's open-directory attack toolchain: mounting a victim's own VHDX backup files to pull ntds.dit and SAM offline, then chunked-rclone exfil to Wasabi"
headline: "Cisco Talos maps The Gentlemen's AD attack chain, including credential theft from a mounted backup image rather than the live domain controller"
summary: >
  Cisco Talos reconstructed a six-phase Active Directory attack chain used by an operator associated
  with the ransomware-as-a-service brand The Gentlemen, recovered from an exposed open directory's own
  command history. The chain tunnels through Chisel/Ligolo-ng, enumerates AD via RustHound/BloodHound
  and NetExec, exploits a public-facing GLPI SQL injection and attempts Zerologon/MS17-010 for lateral
  movement, then extracts ntds.dit and SAM not from the live domain controller but from a CIFS-mounted
  VHDX backup image, exfiltrating the results in 256MiB chunks to Wasabi cloud storage via rclone.
discovered_at: "2026-09-21T04:40:00Z"
updated_at: null
event_date: "2026-09-17"
run_id: 2026-09-21T0410Z-intel
priority: high
immediate_action: null
tags:
  - ransomware
  - organized-crime
  - vulnerabilities
  - identity
regions:
  - global
sectors: []
entities:
  - "actor:thegentlemen"
techniques:
  - T1595
  - T1572
  - T1018
  - T1087.002
  - T1069.002
  - T1482
  - T1190
  - T1557.001
  - T1210
  - T1021.001
  - T1021.002
  - T1021.006
  - T1039
  - T1003.002
  - T1003.003
  - T1567.002
affected_products: ["GLPI"]
cves:
  - id: CVE-2025-24799
    cvss: "7.5"
    epss: null
    type: sqli
    vector: zero-click
    auth: pre-auth
    status: [poc-public]
    affected: ">= 10.0.0, < 10.0.18"
    fixed: "10.0.18"
sources:
  - url: "https://blog.talosintelligence.com/ransomware-incidents-in-japan-in-the-first-half-of-2026/"
    publisher: "Cisco Talos"
    date: "2026-09-17"
    role: primary
closed_sources: []
evidence:
  - quote: "Talos identified open directory infrastructure believed to have been used by a threat actor associated with The Gentlemen. During our investigation, we observed numerous tools used to support ransomware operations."
    publisher: "Cisco Talos"
    source_url: "https://blog.talosintelligence.com/ransomware-incidents-in-japan-in-the-first-half-of-2026/"
  - quote: "In Phase 6, involving information collection and exfiltration, the threat actor mounted a backup share via CIFS at /mnt/Backup and inspected the Windows file system within VHDX backups. The command history records the installation of libguestfs-tools, qemu-utils, and nbd-client, the creation of directories such as /mnt/vhdx, and the copying of ntds.dit, SAM, and SYSTEM. The actor then used Impacket's secretsdump.py to extract credentials and password hashes from the collected ntds.dit and SAM files, saving the results as \"ntds.txt\" and \"SAM.txt\"."
    publisher: "Cisco Talos"
    source_url: "https://blog.talosintelligence.com/ransomware-incidents-in-japan-in-the-first-half-of-2026/"
verification: single-source
sourcing_note: >
  Cisco Talos is the sole publisher of this open-directory forensic analysis; no independent lab has
  corroborated the specific command-history reconstruction. Talos itself frames the actor link as
  "believed to have been used" (a confidence qualifier, not a firm attribution), carried through in this
  entry's own wording. The article's tool-inventory paragraph separately names "exploit code targeting
  CVE-2025-2479, a SQL injection vulnerability" among tools found in the directory; that CVE resolves on
  MITRE to an unrelated WordPress plugin reflected-XSS flaw, not a SQL injection, so this entry omits it
  and cites only CVE-2025-24799 (the GLPI SQL injection Talos's own Phase 3 narrative describes the actor
  exploiting), which the CNA record confirms as a SQL injection.
confidence: high
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

Cisco Talos recovered an exposed open directory believed to belong to an operator associated with the ransomware-as-a-service brand The Gentlemen, and reconstructed a six-phase attack chain from the directory's own shell command history ([Cisco Talos, 2026-09-17](https://blog.talosintelligence.com/ransomware-incidents-in-japan-in-the-first-half-of-2026/)). The operator first built a pivot platform using Chisel, Ligolo-ng and SSH tunnels, then ran nmap and masscan against externally exposed hosts and internal services once inside, then used NetExec to enumerate SMB shares, host information, LDAP and computer information in Active Directory; Talos assesses the operator may also have used RustHound/BloodHound-related tools (a Rust BloodHound collector) to collect domain users, groups, computers, administrative privileges and trust relationships for attack-path analysis. For initial footholds against public-facing applications, the actor ran a PoC and sqlmap against CVE-2025-24799, an unauthenticated SQL injection in GLPI's inventory endpoint (fixed in GLPI 10.0.18), and separately downloaded and ran a cPanel/WHM authentication-bypass PoC. Toward the domain controller, the command history shows attempted exploitation of CVE-2020-1472 (Zerologon) and the MS17-010 vulnerabilities alongside NTLM-relay tooling via Responder. Separately, for lateral movement once inside the network, the operator used NetExec and Impacket to attempt authentication against SMB, LDAP, RDP and WinRM across multiple hosts.

The credential-theft step is the chain's most distinctive detail: rather than dumping credentials from a live, monitored domain controller, the operator mounted a backup share over CIFS, installed `libguestfs-tools`, `qemu-utils` and `nbd-client` to inspect the Windows filesystem inside VHDX backup images, copied out `ntds.dit`, `SAM` and `SYSTEM`, and ran Impacket's `secretsdump.py` offline against the extracted files ([Cisco Talos, 2026-09-17](https://blog.talosintelligence.com/ransomware-incidents-in-japan-in-the-first-half-of-2026/)). The VHDX backup files themselves — not just the small credential-dump output — were compressed with `zstd`, split into 256MiB chunks and uploaded concurrently (up to 16 files at a time) to Wasabi cloud storage via `rclone`, with the operator visibly reconfiguring transfer settings mid-exfiltration to improve speed and reliability. Command and control ran on the open-source AdaptixC2 post-exploitation framework, and Russian-language script comments plus Cyrillic-keymap mistyping in the operator's own bash history (`whoami`, `ls`, `ip a`, `clear`, `exit` typed on a Russian keyboard layout) support Talos's existing assessment that The Gentlemen is Russian-speaking-operator-led.

**Defender takeaway:** backup infrastructure is a credential-theft target in its own right, not only a ransomware-destruction target — any process that mounts, loop-attaches or NBD-attaches a VHDX/VHD backup image and then reads `ntds.dit`, `SAM` or `SYSTEM` out of it is functionally equivalent to a live NTDS dump and should alert identically. Monitor for `libguestfs-tools`/`qemu-utils`/`nbd-client` installation and CIFS mounts of backup shares on hosts that are not the designated backup-management server, and treat `rclone` (or any bulk-upload tool) process creation with a cloud-storage destination immediately following such a mount as a high-confidence exfiltration signal. GLPI deployments should confirm they are on 10.0.18 or later.

**Triage:** legitimate backup-verification and disaster-recovery testing also mount VHDX images and inspect their contents, so the mount event alone is not the signal — the discriminator is the immediate follow-on: `secretsdump.py` or an equivalent credential-extraction tool run against files copied from that mount, on a host or account that has no operational reason to be doing backup verification.
