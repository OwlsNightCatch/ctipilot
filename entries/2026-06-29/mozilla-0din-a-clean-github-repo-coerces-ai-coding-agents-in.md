---
schema: 1
kind: research
horizon: operational
title: "Mozilla 0DIN: a \"clean\" GitHub repo coerces AI coding agents into a reverse shell via three-stage indirection"
headline: "Mozilla 0DIN: a \"clean\" GitHub repo coerces AI coding agents into a reverse shell via three-stage indirection"
summary: "A novel indirect prompt-injection class turns a \"clean\" GitHub repo into a reverse shell against AI coding agents. Mozilla's 0DIN shows a three-step indirection — repo instructions → a deliberately failing Python package → an init command that fetches and runs a DNS TXT record as a shell command — with no malicious code in the repo to flag on static analysis. Relevant to any environment where AI coding agents (Claude Code, Copilot Workspace, Cursor) have repository and shell access (Mozilla 0DIN, 2026-06-25; BleepingComputer, 2026-06-27)."
discovered_at: "2026-06-29T04:47:14Z"
event_date: 2026-06-27
run_id: 2026-06-29-6d39189a
priority: high
immediate_action: null
tags:
  - ai-abuse
  - supply-chain
  - phishing
regions:
  - global
sectors:
  - technology
  - public-sector
entities:
  - "campaign:0din-ai-coding-agent-indirect-pi-dns-txt"
cves: []
sources:
  - url: "https://0din.ai/blog/clone-this-repo-and-i-own-your-machine"
    publisher: Mozilla 0DIN
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/clean-github-repo-tricks-ai-coding-agents-into-running-malware/"
    publisher: BleepingComputer
    role: corroborating
closed_sources: []
evidence:
  - quote: Claude Code never decided to open a shell. It decided to fix an error. The reverse shell is three indirection steps away from anything Claude Code actually evaluated
    publisher: Mozilla 0DIN
  - quote: "a seemingly benign GitHub repository contains three components: clean setup instructions, a Python package that triggers an error message, and an initialization command that fetches and executes a DNS TXT record controlled by attackers"
    publisher: BleepingComputer
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
migrated_from: briefs/2026-06-29.md
---

Mozilla's Zero Day Investigative Network (0DIN) detailed an indirect prompt-injection class against AI coding agents in which no malicious code is present in the repository itself ([Mozilla 0DIN, 2026-06-25](https://0din.ai/blog/clone-this-repo-and-i-own-your-machine); reported [BleepingComputer, 2026-06-27](https://www.bleepingcomputer.com/news/security/clean-github-repo-tricks-ai-coding-agents-into-running-malware/)). The repository carries three cooperating components: (1) plausible setup instructions telling the user/agent to install a Python package; (2) the package, engineered to fail at runtime with an error message that instructs the runtime to run `python3 -m axiom init`; (3) the `axiom init` handler, which issues a DNS TXT lookup to an attacker-controlled domain and executes the returned record value as a shell command. The chain achieves three levels of indirection — error message → DNS resolution → shell execution — so the agent never "decides" to open a shell; it interprets each step as routine error recovery and autonomously runs the suggested remediation, side-stepping per-step user approval. No CVE is assigned: this is exploitation of agentic error-recovery autonomy plus out-of-band payload retrieval, not a single software bug. It is a distinct technique from the Amazon Q Developer MCP-config auto-load issue (CVE-2026-12957) covered on 2026-06-27 — that abused automatic config loading; this abuses error-recovery behaviour and DNS-TXT C2.

**Why it matters to us:** Any environment where AI coding agents (Claude Code, GitHub Copilot Workspace, Cursor) hold repository and shell access — developer workstations, CI/CD runners, increasingly common in public-sector DevOps — should treat agent-executed setup/init steps as an untrusted-input execution surface. The static-analysis-clean property means repo scanning will not catch it; the behavioural tells are network-dependent init steps and out-of-band command retrieval. Detection concepts (no IOCs): alert on DNS TXT-record queries originating from developer-tooling process trees (`node`, `python`, `pip`, `npx`) during repository setup; EDR parent-child chains where an agent process spawns an unexpected shell child; egress monitoring for DNS TXT lookups from developer workstations and build agents. Hardening: require human-in-the-loop approval for any external network call made by agent-executed init scripts, and treat an agent's DNS/network capability as a scope that needs explicit grant rather than a default. Mapped to [T1566](https://attack.mitre.org/techniques/T1566/) (delivery via a malicious repo link), [T1071.004](https://attack.mitre.org/techniques/T1071/004/) (DNS as C2 channel) and [T1059.004](https://attack.mitre.org/techniques/T1059/004/) (Unix shell execution).
