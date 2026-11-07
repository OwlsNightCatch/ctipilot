---
schema: 1
kind: research
title: "'Friendly Fire': prompt injection hijacks AI coding agents' defensive auto-review into remote code execution"
headline: "AI Now Institute PoC turns an untrusted library's own files into RCE when Claude Code or Codex CLI review it in auto-mode — no hooks or config needed"
summary: >
  AI Now Institute published a proof-of-concept (2026-07-08) achieving RCE against Claude Code CLI
  (auto-mode) and OpenAI Codex CLI (auto-review) simply by having the agent security-review an
  untrusted repository. A two-layer prompt injection — a decoy Go source paired with a malicious
  binary, plus a README that steers the agent to run a bundled script — executes attacker code with
  no hooks, plugins, MCP servers or config files. It is the third distinct AI-coding-agent
  prompt-injection RCE class reported in under two weeks; relevant to any team adopting agentic AI
  code review over third-party or open-source code.
discovered_at: "2026-07-11T04:30:43Z"
event_date: "2026-07-08"
run_id: 2026-07-11T0409Z-intel
priority: notable
immediate_action: null
tags: [ai-abuse, supply-chain, rce]
regions: [global]
sectors: [technology, public-sector]
entities: [campaign:friendly-fire-ai-agent-defensive-hijack]
techniques: [T1204.002, T1059.004, T1195.001]
affected_products: ["Anthropic Claude Code CLI", "OpenAI Codex CLI"]
cves: []
sources:
  - url: "https://ainowinstitute.org/publications/friendly-fire-exploit-brief"
    publisher: "AI Now Institute"
    date: "2026-07-08"
    role: primary
  - url: "https://www.infosecurity-magazine.com/news/anthropic-openai-report-exploit/"
    publisher: "Infosecurity Magazine"
    date: "2026-07-10"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Our attack only requires an out-of-the-box configuration of Claude Code in “auto-mode” or Codex in “auto-review” and leverages prompt injections disseminated across a library’s source code that target AI-enabled cyber defense without the need for hooks, skills, plugins, MCP servers, or configuration files as an injection vector."
    publisher: "AI Now Institute"
  - quote: "When Claude Code or Codex proceed to analyze the source code, the prompt injections steer each respective agent to presume that the malicious binary is necessary to perform the security review, thereby executing the binary and failing to detect it as harmful."
    publisher: "AI Now Institute"
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: [2026-06-29/mozilla-0din-a-clean-github-repo-coerces-ai-coding-agents-in, 2026-07-09/ghostapproval-ai-coding-assistant-symlink-trust-boundary]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Do not point an agentic coding assistant with command-execution ability (Claude Code auto-mode, Codex auto-review, or equivalents) at untrusted third-party or open-source code, including automated dependency-update review in CI/CD — treat the reviewed repository as attacker-controlled input, not trusted data."
  - "Where such agents are used, run them in isolated, credential-minimised environments and do not treat sandboxing as sufficient: the researchers show an in-sandbox RCE can be chained to escape (citing CVE-2026-39861 and CVE-2026-25725 against Claude Code's own sandbox)."
  - "Hunt on developer/CI hosts for coding-agent processes spawning a Unix shell or executing a repository-supplied binary/script (e.g. a `security.sh` or similar) during a review task, and for outbound network or credential access from such child processes."
migrated_from: null
---

AI Now Institute researchers Boyan Milanov and Heidy Khlaaf published a proof-of-concept, "Friendly Fire," that achieves remote code execution against Anthropic's Claude Code CLI (auto-mode, with Sonnet 4.6, Sonnet 5 or Opus 4.8) and OpenAI's Codex CLI (auto-review, with GPT-5.5) when either is used for its advertised defensive purpose — reviewing the security of an untrusted open-source or third-party library ([AI Now Institute, 2026-07-08](https://ainowinstitute.org/publications/friendly-fire-exploit-brief)). The attack needs only an out-of-the-box configuration: no custom hooks, skills, plugins, MCP servers, or machine-configuration files as an injection vector. The chain is two layers of prompt injection carried entirely inside the reviewed repository's own files. The first layer makes a malicious binary look safe: alongside the binary (`code_policies`) the attacker ships a decoy Go source file (`code_policies.go`) implementing a legitimate-looking static checker, and embeds matching string constants in the binary so the agent's own disassembly-inspection step associates the two and clears it. The second layer, placed in `README.md` — deliberately, because README is not an enforceable machine-config file and needs no user approval — references a bundled `security.sh` "security checker" in innocuous language, leading the agent to run the script, which launches the binary ([AI Now Institute, 2026-07-08](https://ainowinstitute.org/publications/friendly-fire-exploit-brief); [Infosecurity Magazine, 2026-07-10](https://www.infosecurity-magazine.com/news/anthropic-openai-report-exploit/)).

The researchers demonstrated the technique against a modified copy of the `geopy` Python library and report it transfers to other libraries and to Codex without modification, mapping it onto two realistic threat models: malicious library maintainers embedding instructions in their own code, and supply-chain compromise of upstream packages (they cite recent GitHub-repo-poisoning and PyTorch Lightning incidents), the latter especially dangerous where CI/CD auto-updates dependencies and then hands them to a defensive agent to review. They explicitly reject sandboxing as a sufficient mitigation, arguing an in-sandbox RCE can be used to attempt escape and citing sandbox-escape CVEs against Claude Code itself. **Defender takeaway:** this is the third distinct AI-coding-agent prompt-injection RCE mechanism to surface in under two weeks — after Mozilla 0DIN's clean-repo coercion ([covered 2026-06-29](../2026-06-29/mozilla-0din-a-clean-github-repo-coerces-ai-coding-agents-in.md)) and Wiz GhostApproval's symlink/confirmation-UI bypass ([covered 2026-07-09](../2026-07-09/ghostapproval-ai-coding-assistant-symlink-trust-boundary.md)) — and while each mechanism differs, the pattern is consistent: an agent with execution capability cannot reliably separate untrusted reviewed content from trusted instructions. **Triage:** legitimate review tasks rarely require the agent to execute a repository-supplied binary or shell script, so a coding-agent process spawning a Unix shell or running a bundled executable during a review — particularly with subsequent outbound network or credential access — is the discriminating behaviour to hunt on developer and CI hosts.
