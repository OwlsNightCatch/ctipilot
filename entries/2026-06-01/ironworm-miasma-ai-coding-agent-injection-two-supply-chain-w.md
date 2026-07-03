---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-top-stories
title: "IronWorm + Miasma AI coding-agent injection: two supply-chain worms target cloud credentials and developer toolchains simultaneously"
headline: "IronWorm + Miasma AI coding-agent injection: two supply-chain worms target cloud credentials and developer toolchains simultaneously"
summary: "Miasma worm pivots to AI coding-agent config injection — 73 Microsoft GitHub repositories disabled in 105 seconds. Malicious commits wire execution to Claude Code / Cursor / Gemini CLI / VS Code workspace-config files, detonating on repo open rather than npm install; azure-functions-action CI/CD globally disrupted. (daily, StepSecurity)"
discovered_at: "2026-06-01T05:00:02Z"
event_date: 2026-06-06
run_id: 2026-W23-9118e7bd
priority: high
immediate_action: null
tags:
  - supply-chain
  - infostealer
  - cloud
  - actively-exploited
regions:
  - global
sectors:
  - technology
  - public-sector
entities:
  - "campaign:ironworm"
cves: []
sources:
  - url: "https://research.jfrog.com/post/iron-worm-shai-hulud-rustier-cousin/"
    publisher: JFrog Security Research — IronWorm
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/new-ironworm-malware-hits-36-packages-in-npm-supply-chain-attack/"
    publisher: BleepingComputer — IronWorm
    role: corroborating
  - url: "https://www.stepsecurity.io/blog/miasma-worm-hits-microsoft-again-azure-functions-action-and-72-other-repositories-disabled-after-supply-chain-attack-targeting-ai-coding-agents"
    publisher: StepSecurity — Miasma AI coding agent injection
    role: corroborating
  - url: "https://thehackernews.com/2026/06/miasma-worm-hits-73-microsoft-github.html"
    publisher: The Hacker News
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
migrated_from: briefs/weekly/2026-W23.md
---

**If you did nothing this week:** any developer who cloned one of the 73 disabled Microsoft GitHub repositories and opened it in Claude Code, Cursor, Gemini CLI, or VS Code with AI extensions may have triggered malicious payload execution. Any CI/CD pipeline consuming azure-functions-action in the exposure window may have run attacker-controlled code. Any developer machine running npm packages from the affected @redhat-cloud-services or IronWorm-infected namespaces should be treated as credential-compromised.

**IronWorm** (disclosed by JFrog on 2026-06-03; [daily 2026-06-06](/briefs/2026-06-06/)) is a self-propagating npm worm distributed across ~36 packages from a compromised publisher account ([JFrog, 2026-06-03](https://research.jfrog.com/post/iron-worm-shai-hulud-rustier-cousin/)). Unlike the JavaScript-stager Shai-Hulud lineage, IronWorm executes a Rust ELF payload through a `preinstall` lifecycle hook (`T1195.002`), then deploys an eBPF object providing kernel-level process, socket and anti-debug concealment — hiding the implant from procfs-based enumeration and most EDR agents that rely on user-space telemetry. The command channel runs over Tor. The credential sweep targets AWS, GCP, Azure, HashiCorp Vault, Kubernetes, Docker, GitHub and npm tokens, plus the 2026 generation of AI-provider API keys (Anthropic, OpenAI, Gemini). Self-propagation reuses stolen npm Trusted Publishing credentials. Detection: alert on `node`/`npm`/`npx` spawning `sh`/`bash` during `preinstall`/`postinstall`; audit `bpf()` syscalls from non-privileged processes via `auditd`; watch CI/CD egress for Tor bootstrap traffic. Hardening: run `npm install --ignore-scripts` in CI, pin lockfile integrity, scope/rotate npm publish tokens.

**Miasma's AI coding-agent injection** (2026-06-05–06; [daily 2026-06-06](/briefs/2026-06-06/)) planted a ~4.6 MB payload runner (4,643,745 bytes) in 73 Microsoft and Microsoft-adjacent GitHub repositories, wiring execution to workspace-config files — CLAUDE.md, `.claude/commands/`, `.gemini/`, `.cursor/rules`, `.vscode/settings.json` — so the trigger is a developer **opening the repository in an AI-assisted IDE**, not an `npm install` ([StepSecurity](https://www.stepsecurity.io/blog/miasma-worm-hits-microsoft-again-azure-functions-action-and-72-other-repositories-disabled-after-supply-chain-attack-targeting-ai-coding-agents); [The Hacker News](https://thehackernews.com/2026/06/miasma-worm-hits-73-microsoft-github.html)). GitHub disabled the affected repositories by June 6. StepSecurity forensics trace the entry-point account to the same contributor credentials compromised in the May 19 PyPI attack; full revocation was not confirmed (three hypotheses; non-revocation is the most parsimonious). Detection: treat workspace-config files from cloned repositories as untrusted data, not code, in CI/CD environments; monitor `.claude/commands/`, `.gemini/`, `.cursor/rules` for unexpected writes or outbound HTTP triggers; audit azure-functions-action workflows for execution in the exposure window.
