---
schema: 1
kind: vulnerability
title: "PinTheft: Linux kernel RDS zerocopy double-free (CVE-2026-43494) turned into a root exploit through io_uring fixed buffers, public PoC; RDS loads by default only on Arch Linux"
headline: "PinTheft gives a local user root through an RDS zerocopy double-free, wherever the RDS kernel module is loaded"
summary: >
  V12 Security released PinTheft and a working exploit on 2026-05-19, relayed to oss-security by Gentoo's
  Sam James: a double-free in the Linux kernel's RDS zerocopy send path, rds_message_zcopy_from_user(),
  that the exploit turns into a page-cache overwrite of a SUID-root binary through io_uring fixed buffers
  for a root shell. The bug was patched upstream earlier in May and the kernel fix was published as
  CVE-2026-43494 (CVSS 7.8) on 2026-05-21; exploitation needs the RDS modules, which V12 found loaded by
  default only on Arch Linux among common distributions.
discovered_at: "2026-05-21T05:00:06Z"
event_date: 2026-05-19
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
techniques: [T1068]
affected_products:
  - "Linux kernel"
cves:
  - id: CVE-2026-43494
    cvss: "7.8"
    epss: null
    type: lpe
    vector: local
    auth: post-auth
    status:
      - poc-public
      - patch-available
    affected: "Linux kernel RDS zerocopy send path before the upstream fix of May 2026"
    fixed: "upstream fix net/rds: reset op_nents when zerocopy page pin fails"
sources:
  - url: "https://www.openwall.com/lists/oss-security/2026/05/19/6"
    publisher: "oss-security (Sam James, relaying V12 Security)"
    date: "2026-05-19"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/linux/exploit-released-for-new-pintheft-arch-linux-root-escalation-flaw/"
    publisher: "BleepingComputer"
    date: "2026-05-20"
    role: corroborating
  - url: "https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-31267"
    publisher: "ENISA EUVD-2026-31267"
    date: "2026-05-21"
    role: corroborating
closed_sources: []
evidence:
  - quote: "PinTheft is a Linux local privilege escalation exploit for an RDS"
    publisher: "oss-security (Sam James, relaying V12 Security)"
    source_url: "https://www.openwall.com/lists/oss-security/2026/05/19/6"
  - quote: "Sadly, the RDS kernel module this requires is only default on Arch Linux among the common distributions we tested"
    publisher: "BleepingComputer"
    source_url: "https://www.bleepingcomputer.com/news/linux/exploit-released-for-new-pintheft-arch-linux-root-escalation-flaw/"
  - quote: "Linux users on affected distros are advised to install the latest kernel updates as soon as possible."
    publisher: "BleepingComputer"
    source_url: "https://www.bleepingcomputer.com/news/linux/exploit-released-for-new-pintheft-arch-linux-root-escalation-flaw/"
verification: single-source
sourcing_note: >
  V12 Security's write-up, relayed to oss-security with its proof of concept, is the only analysis of the
  exploit; BleepingComputer restates it, and the kernel CNA's CVE record, read through ENISA's EUVD,
  describes the same rds_message_zcopy_from_user() fix.
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-21.md
updates:
  - at: "2026-10-21T20:35:19Z"
    run_id: 2026-10-21T1148Z-audit
    type: improvement
    summary: >
      V12 found the RDS module enabled by default only on Arch Linux among the common distributions it
      tested, a narrower finding than a statement about every distribution; Aaron Esau of V12 found
      PinTheft and Gentoo's Sam James relayed it to oss-security. The kernel fix was published as
      CVE-2026-43494 (CVSS 7.8) on 2026-05-21, the finding is recast as a vulnerability with that CVE
      record, and unsourced auditd and Sysmon hunts give way to the exploit's own syscall sequence and the
      module-blocking mitigation.
    fields: [affected_products, body, classification, cves, event_date, evidence, headline, kind, sources, sourcing_note, summary, techniques, title, verification]
---

V12 Security released PinTheft with a proof-of-concept exploit on 2026-05-19, and Gentoo's Sam James relayed it to the oss-security list the same day; Aaron Esau of the V12 team found the bug ([oss-security, 2026-05-19](https://www.openwall.com/lists/oss-security/2026/05/19/6)). In the RDS zerocopy send path, `rds_message_zcopy_from_user()` pins user pages one at a time; when a later page faults, the error path drops the pages already pinned while the scatterlist entries stay live, so message cleanup drops them again and each failed send steals a reference from the first page ([oss-security, 2026-05-19](https://www.openwall.com/lists/oss-security/2026/05/19/6)). The exploit registers an anonymous page as an `io_uring` fixed buffer, which gives it a FOLL_PIN bias of 1024 references, steals those references with failing RDS zerocopy sends, lets the page be reclaimed as page cache of a SUID-root binary and overwrites it through the stale fixed-buffer pointer with a small ELF payload, so running the binary drops into a root shell ([oss-security, 2026-05-19](https://www.openwall.com/lists/oss-security/2026/05/19/6)). It needs the RDS modules, io_uring enabled, a readable SUID-root binary and x86_64 for the included payload ([BleepingComputer, 2026-05-20](https://www.bleepingcomputer.com/news/linux/exploit-released-for-new-pintheft-arch-linux-root-escalation-flaw/)). The bug was patched upstream earlier in May ([BleepingComputer, 2026-05-20](https://www.bleepingcomputer.com/news/linux/exploit-released-for-new-pintheft-arch-linux-root-escalation-flaw/)), and the kernel CNA published that fix, which resets `op_nents` in `rds_message_zcopy_from_user()`, as CVE-2026-43494 (CVSS 7.8) on 2026-05-21 ([ENISA EUVD-2026-31267](https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-31267)).

**Exposure:** Linux hosts that load the RDS modules (`CONFIG_RDS` with `CONFIG_RDS_TCP`), which V12 found enabled by default only on Arch Linux among the common distributions it tested ([oss-security, 2026-05-19](https://www.openwall.com/lists/oss-security/2026/05/19/6)), and that have the io_uring I/O API enabled ([BleepingComputer, 2026-05-20](https://www.bleepingcomputer.com/news/linux/exploit-released-for-new-pintheft-arch-linux-root-escalation-flaw/)).

**Detection:** process and syscall telemetry: an unprivileged process that opens RDS sockets, registers an io_uring fixed buffer and issues a burst of failing RDS zerocopy sends, then executes a SUID-root binary that yields a root shell, is the exploit's sequence ([oss-security, 2026-05-19](https://www.openwall.com/lists/oss-security/2026/05/19/6)).

**Defender takeaway:** install the fixed kernel; where that cannot happen at once, unload `rds_tcp` and `rds` and block both from loading through modprobe configuration, the mitigation BleepingComputer gives ([BleepingComputer, 2026-05-20](https://www.bleepingcomputer.com/news/linux/exploit-released-for-new-pintheft-arch-linux-root-escalation-flaw/)); hosts that never load RDS are not reachable by this exploit.

## Improvement — 2026-10-21T20:35:19Z

V12 found the RDS module (`CONFIG_RDS` with `CONFIG_RDS_TCP`) enabled by default only on Arch Linux among the common distributions it tested; it did not establish that the module is off on every other distribution ([oss-security, 2026-05-19](https://www.openwall.com/lists/oss-security/2026/05/19/6)). Aaron Esau of V12 found the bug and V12 released the exploit, which Gentoo's Sam James relayed to oss-security ([oss-security, 2026-05-19](https://www.openwall.com/lists/oss-security/2026/05/19/6)). The kernel fix was published as CVE-2026-43494 (CVSS 7.8) on 2026-05-21 ([ENISA EUVD-2026-31267](https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-31267)), and the mitigation for hosts that cannot take the fixed kernel yet is to unload and block the `rds_tcp` and `rds` modules ([BleepingComputer, 2026-05-20](https://www.bleepingcomputer.com/news/linux/exploit-released-for-new-pintheft-arch-linux-root-escalation-flaw/)).
