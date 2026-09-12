---
schema: 1
kind: threat
title: "\"Atomic Arch\" supply-chain attack hijacks 400+ AUR packages to drop a credential stealer and eBPF rootkit"
headline: "\"Atomic Arch\" supply-chain attack hijacks 400+ AUR packages to drop a credential stealer and eBPF rootkit"
summary: "\"Atomic Arch\" hijacked 400+ orphaned Arch Linux AUR packages to drop a Rust credential stealer and an eBPF rootkit that hides processes/files via pinned BPF maps; injection rides a malicious atomic-lockfile npm dependency added to PKGBUILD (Sonatype, 2026-06-11)."
discovered_at: "2026-06-13T05:00:01Z"
event_date: 2026-06-12
run_id: 2026-06-13-40b26572
priority: high
immediate_action: null
tags:
  - supply-chain
  - infostealer
  - organized-crime
regions:
  - global
sectors:
  - technology
entities:
  - "campaign:atomic-arch-aur-supply-chain-2026"
cves: []
sources:
  - url: "https://www.sonatype.com/blog/atomic-arch-npm-campaign-adds-malicious-dependency"
    publisher: Sonatype
    role: primary
  - url: "https://ioctl.fail/preliminary-analysis-of-aur-malware/"
    publisher: ioctl.fail
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/over-400-arch-linux-packages-compromised-to-push-rootkit-infostealer/"
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
migrated_from: briefs/2026-06-13.md
---

Attackers adopted roughly 400 orphaned Arch User Repository (AUR) packages through the AUR's standard disowned-package adoption mechanism, then rewrote their PKGBUILD build scripts to pull a malicious npm dependency, `atomic-lockfile`, during build ([Sonatype, 2026-06-11](https://www.sonatype.com/blog/atomic-arch-npm-campaign-adds-malicious-dependency)). On any machine that builds an affected package, the dependency fetches a Rust-compiled Linux ELF that harvests developer secrets — browser profiles, SSH keys, GitHub/npm/cloud and AI-service tokens, messaging session data, shell histories, Docker and VPN credentials. When it runs with root or `CAP_BPF`/`CAP_SYS_ADMIN`, an embedded eBPF component pins maps at `/sys/fs/bpf/hidden_pids`, `/sys/fs/bpf/hidden_names` and `/sys/fs/bpf/hidden_inodes` to hide its processes, files and socket inodes from `ps`, `ls`, `netstat` and live-response tooling ([ioctl.fail, 2026-06-11](https://ioctl.fail/preliminary-analysis-of-aur-malware/)). A second wave on 12 June added `js-digest`/`lockfile-js` delivery packages and a Bun-based path; Sonatype tracks it as Sonatype-2026-003775 (CVSS 8.7) and estimates the campaign may reach ~1,500 packages ([BleepingComputer, 2026-06-12](https://www.bleepingcomputer.com/news/security/over-400-arch-linux-packages-compromised-to-push-rootkit-infostealer/)). Maps to T1195.002 (Compromise Software Supply Chain) and T1059 (Command and Scripting Interpreter via PKGBUILD).

**Why it matters to us:** Developer workstations and CI runners that build AUR packages are the blast radius. Hunt for `npm install`/`bun install` spawned from `makepkg` (Sysmon for Linux EID 1, parent-image filter), enumerate `ls /sys/fs/bpf/hidden_*` across Linux developer hosts, and restrict AUR-helper use on privilege-holding CI runners.
