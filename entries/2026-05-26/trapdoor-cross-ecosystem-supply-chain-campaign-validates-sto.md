---
schema: 1
kind: threat
horizon: operational
title: "\"TrapDoor\" cross-ecosystem supply-chain campaign validates stolen tokens before exfil and poisons AI-assistant config files"
headline: "\"TrapDoor\" cross-ecosystem supply-chain campaign validates stolen tokens before exfil and poisons AI-assistant config files"
summary: "\"TrapDoor\" is a coordinated cross-ecosystem supply-chain campaign (34+ packages, 384+ versions across npm, PyPI and Crates.io) that validates stolen AWS/GitHub tokens before exfiltrating and poisons AI coding-assistant config files — npm postinstall harvester, PyPI import-time execution, Rust build.rs wallet-keystore theft; novel vector writes hidden prompt-injection into .cursorrules and CLAUDE.md using zero-width Unicode so a human sees clean text while the AI tool parses attacker instructions (Socket, 2026-05-24)."
discovered_at: "2026-05-26T05:00:00Z"
event_date: 2026-05-25
run_id: 2026-05-26-ae9d0d4b
priority: high
immediate_action: null
tags:
  - supply-chain
  - infostealer
  - ai-abuse
  - cryptocrime
regions:
  - global
  - europe
sectors:
  - technology
  - finance
  - public-sector
entities:
  - "campaign:trapdoor"
cves: []
sources:
  - url: "https://socket.dev/blog/trapdoor-crypto-stealer-npm-pypi-crates"
    publisher: "Socket, 2026-05-24"
    role: primary
  - url: "https://thehackernews.com/2026/05/trapdoor-supply-chain-attack-spreads.html"
    publisher: "The Hacker News, 2026-05-25"
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
migrated_from: briefs/2026-05-26.md
---

Socket disclosed **TrapDoor**, a coordinated supply-chain campaign spanning 34+ malicious packages across 384+ versions published to npm, PyPI and Crates.io, with earliest activity on 2026-05-22 ~20:20 UTC; Socket reports a median detection latency of under six minutes after publish ([Socket, 2026-05-24](https://socket.dev/blog/trapdoor-crypto-stealer-npm-pypi-crates); [The Hacker News, 2026-05-25](https://thehackernews.com/2026/05/trapdoor-supply-chain-attack-spreads.html)). Each registry carries a distinct execution path: npm packages run a JavaScript credential harvester via a `postinstall` lifecycle hook ([`T1195.001`](https://attack.mitre.org/techniques/T1195/001/), [`T1059.004`](https://attack.mitre.org/techniques/T1059/004/)); PyPI packages execute on import and pull a remote payload via `node -e`; Rust crates use `build.rs` scripts that XOR-encrypt local Sui/Solana/Aptos wallet keystores and exfiltrate them to GitHub Gists. The npm harvester validates stolen **AWS and GitHub tokens against live APIs before flagging them** — only working credentials are exfiltrated ([`T1552.001`](https://attack.mitre.org/techniques/T1552/001/)) — and establishes persistence via cron, systemd units, Git hooks and SSH-based lateral movement ([`T1053.003`](https://attack.mitre.org/techniques/T1053/003/), [`T1021.004`](https://attack.mitre.org/techniques/T1021/004/)). The defining novelty is an AI-assistant targeting vector: the packages write hidden instructions into `.cursorrules` and `CLAUDE.md` using zero-width Unicode characters (U+200B family), so a developer reviewing the file sees clean text while Cursor or Claude Code parses an attacker "security scan" directive that triggers data exfiltration ([`T1195.002`](https://attack.mitre.org/techniques/T1195/002/)).

**Why it matters to us:** the targeting (crypto/DeFi/AI developer communities) is narrow, but the execution model is not — any CH/EU public-sector DevOps pipeline that installs from these registries is exposed, and the AI-config-poisoning vector is a fresh class of persistence that survives a clean-looking code review. Hunt for `node`/`python`/`cargo` build processes spawning `sh`/`bash`/`node -e`, package-manager process trees writing to `~/.cursorrules` or `CLAUDE.md` (especially with zero-width code points U+200B/U+200C/U+FEFF present), unexpected `systemd` unit or `crontab` writes from build runners, and GitHub Gist `POST` from CI. Pin exact versions, verify lockfile hashes, and run installs with `--ignore-scripts` where feasible.
