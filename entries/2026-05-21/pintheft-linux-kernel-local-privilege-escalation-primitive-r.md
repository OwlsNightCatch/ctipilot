---
schema: 1
kind: research
horizon: operational
title: "PinTheft — Linux kernel local-privilege-escalation primitive (RDS zerocopy double-free + io_uring fixed-buffer page-cache overwrite), PoC public, Arch Linux default-loaded"
headline: "PinTheft — Linux kernel local-privilege-escalation primitive (RDS zerocopy double-free + io_uring fixed-buffer page-cache overwrite), PoC public, Arch Linux"
summary: "Aaron Esau (V12 Security) disclosed PinTheft on 2026-05-19 via the oss-security mailing list — a Linux kernel local privilege escalation that chains an RDS (Reliable Datagram Sockets) zerocopy double-free with io_uring fixed-buffer reference manipulation to overwrite the page cache of a SUID-root binary and gain …"
discovered_at: "2026-05-21T05:00:06Z"
event_date: 2026-05-20
run_id: 2026-05-21-77cdc4cd
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - lpe
  - poc-public
  - patch-available
regions:
  - global
sectors:
  - technology
entities:
  - "trend:pintheft-linux-kernel-rds-zerocopy-iouring-lpe-no-cve-arch-d"
cves: []
sources:
  - url: "https://www.openwall.com/lists/oss-security/2026/05/19/6"
    publisher: oss-security mailing list / V12 Security
    role: primary
  - url: "https://www.bleepingcomputer.com/news/linux/exploit-released-for-new-pintheft-arch-linux-root-escalation-flaw/"
    publisher: BleepingComputer
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-21.md
---

Aaron Esau (V12 Security) disclosed PinTheft on 2026-05-19 via the `oss-security` mailing list — a Linux kernel local privilege escalation that chains an RDS (Reliable Datagram Sockets) zerocopy double-free with `io_uring` fixed-buffer reference manipulation to overwrite the page cache of a SUID-root binary and gain root ([oss-security / V12 Security, 2026-05-19](https://www.openwall.com/lists/oss-security/2026/05/19/6); [BleepingComputer, 2026-05-20](https://www.bleepingcomputer.com/news/linux/exploit-released-for-new-pintheft-arch-linux-root-escalation-flaw/)). The bug lives in `rds_message_zcopy_from_user()` in the RDS send path: a partial page fault mid-scatter causes the error path to drop already-pinned pages while leaving the scatterlist bookkeeping live, so cleanup drops the pages a second time. The exploit registers an anonymous memory page as an `io_uring` fixed buffer (`FOLL_PIN` bias of 1024 references), drains all references via 1024 deliberately-failing RDS sends, then reuses the stale `io_uring` page pointer to overwrite the page cache of a SUID-root binary and redirect execution to attacker shellcode. Prerequisites: RDS kernel module loaded, `io_uring` enabled, a readable SUID-root binary, x86_64. **The RDS module is default-loaded only on Arch Linux** — not on Ubuntu, Fedora, Debian, RHEL or SUSE — narrowing the primary defender population to Arch CI/CD runners, developer workstations and AUR-based servers, plus any environment that explicitly `modprobe`'d `rds`. Upstream kernel patch landed before disclosure; **no CVE assigned at disclosure**. Technique class: `T1068` Exploitation for Privilege Escalation. Defender detection — auditd syscall events for `rds_sendmsg` / `io_uring_*` from unexpected binaries; Sysmon Linux EID 1 with process lineage showing a non-root process spawning a root shell without `sudo`/`su`. Hardening: `modprobe.d` blacklist `rds` if not in use; `sysctl kernel.io_uring_disabled=2` for untrusted workloads; apply upstream kernel patch when distributed via the distro's normal update channel.
