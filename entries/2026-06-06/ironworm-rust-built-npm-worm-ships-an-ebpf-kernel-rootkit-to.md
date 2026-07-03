---
schema: 1
kind: threat
horizon: operational
title: "IronWorm: Rust-built npm worm ships an eBPF kernel rootkit, Tor C2 and a cloud/AI-credential sweep"
headline: "IronWorm: Rust-built npm worm ships an eBPF kernel rootkit, Tor C2 and a cloud/AI-credential sweep"
summary: "Two distinct self-propagating npm worms hit the JavaScript supply chain in the same window — the new Rust-built IronWorm (eBPF kernel rootkit + Tor C2, ~36 packages, cloud/AI-key sweep) (JFrog, 2026-06-03), and a fresh Miasma variant that reached 73 Microsoft GitHub repositories including the Azure Durable Task ecosystem (§ 4). Both abuse install-time scripts and stolen publishing credentials."
discovered_at: "2026-06-06T05:00:01Z"
event_date: 2026-06-04
run_id: 2026-06-06-d01b95fe
priority: high
immediate_action: null
tags:
  - supply-chain
  - infostealer
  - cloud
regions:
  - global
sectors:
  - technology
entities:
  - "campaign:ironworm"
cves: []
sources:
  - url: "https://research.jfrog.com/post/iron-worm-shai-hulud-rustier-cousin/"
    publisher: "JFrog Security Research — IronWorm: Shai-Hulud's rustier cousin"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/new-ironworm-malware-hits-36-packages-in-npm-supply-chain-attack/"
    publisher: "BleepingComputer, 2026-06-04"
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
actions:
  - "**Lock down npm build pipelines against IronWorm and Miasma** (. Enforce `npm install --ignore-scripts` in CI, pin lockfile integrity, rotate/scope npm publish (incl. Trusted Publishing) tokens, and rotate Azure managed-identity / `~/.azure` credentials on any runner that installed an affected `@azure/*` package. Add `bpf()`-syscall and Tor-bootstrap egress monitoring on build hosts."
migrated_from: briefs/2026-06-06.md
---

JFrog Security Research disclosed **IronWorm**, a self-propagating npm supply-chain worm distributed across roughly 36 packages from a compromised publisher account ([JFrog, 2026-06-03](https://research.jfrog.com/post/iron-worm-shai-hulud-rustier-cousin/); [BleepingComputer, 2026-06-04](https://www.bleepingcomputer.com/news/security/new-ironworm-malware-hits-36-packages-in-npm-supply-chain-attack/)). Unlike the JavaScript-stager Shai-Hulud lineage, IronWorm executes a Rust ELF payload through an install-time `preinstall` hook and carries an embedded eBPF object (`T1195.002` Compromise Software Supply Chain, `T1059.004` Unix Shell via lifecycle script). JFrog reports the eBPF component provides kernel-level process, socket and anti-debug concealment — hiding the implant from procfs-based enumeration and many EDR agents — while the command channel runs over Tor: the malware downloads the Tor expert bundle, writes its own `torrc`, and beacons to a hidden service. The stealer sweeps dozens of environment variables and credential paths spanning AWS, GCP, Azure, HashiCorp Vault, Kubernetes, Docker, GitHub and npm tokens, and the 2026 generation of AI-provider API keys (Anthropic, OpenAI, Gemini and others). Self-propagation reuses stolen npm credentials — including npm Trusted Publishing secrets — to publish trojanised versions of the victim's own packages.

**Why it matters to us:** The eBPF rootkit moves npm-worm tradecraft below the userland telemetry most pipelines rely on, so process-tree hunting on the build host is no longer sufficient. Detection concepts: alert on `node`/`npm`/`npx` parent processes spawning `sh`/`bash` during `preinstall`/`postinstall` (Sysmon-for-Linux EID 1), audit `bpf()` syscalls from non-privileged processes via `auditd`, and watch CI/CD egress for Tor bootstrap traffic. Hardening: run `npm install --ignore-scripts` in CI, pin lockfile integrity, and scope/rotate npm publish tokens — Trusted Publishing credentials are now an explicit propagation target.
