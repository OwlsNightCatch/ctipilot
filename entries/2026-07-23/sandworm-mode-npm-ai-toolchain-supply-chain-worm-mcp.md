---
schema: 1
kind: research
horizon: operational
title: "SANDWORM_MODE — an npm supply-chain worm that 'lives off the AI toolchain', poisoning MCP servers in AI coding assistants to steal developer credentials"
headline: "CrowdStrike documents SANDWORM_MODE, an npm worm that abuses AI coding-assistant MCP configs and git hooks to harvest developer credentials"
summary: >
  CrowdStrike published defensive research on SANDWORM_MODE, a multi-stage npm supply-chain worm that
  targets AI-augmented developer workflows — it writes rogue Model Context Protocol (MCP) tool-provider
  entries into AI coding-assistant configs (Cursor, VS Code, Claude Desktop, Windsurf), injects global
  git-template hooks for persistence, and exfiltrates npm/AWS/SSH credentials plus multi-provider LLM API
  keys, delaying activation 48–96 h on workstations to defeat install-versus-behaviour correlation. The
  transferable lesson is the evasion premise: of 14 investigated behaviours only 2 met the bar for
  high-fidelity alerting, because the worm's actions blend into legitimate developer and CI telemetry.
discovered_at: "2026-07-23T04:34:04Z"
event_date: "2026-07-21"
run_id: 2026-07-23T0409Z-intel
priority: notable
immediate_action: null
tags: [supply-chain, ai-abuse, infostealer, identity, cloud]
regions: [global]
sectors: [public-sector, technology]
entities: [malware:sandworm-mode]
techniques: [T1195.002, T1552.001, T1546, T1071.004, T1497]
affected_products: ["npm", "Cursor", "Visual Studio Code", "Claude Desktop", "Windsurf", "Model Context Protocol (MCP)"]
cves: []
sources:
  - url: "https://www.crowdstrike.com/en-us/blog/denying-the-worm-sandworm-mode-and-ai-toolchain-supply-chain-attacks/"
    publisher: "CrowdStrike"
    date: "2026-07-21"
    role: primary
  - url: "https://securitybrief.com.au/story/crowdstrike-warns-of-malware-targeting-ai-coding-tools"
    publisher: "SecurityBrief"
    date: "2026-07-22"
    role: corroborating
closed_sources: []
evidence:
  - quote: "SANDWORM_MODE introduces an analogous pattern for AI-augmented development environments: living off the AI toolchain."
    publisher: "CrowdStrike"
  - quote: "Of 14 investigated behaviors, only 9 could produce any signal, and only 2 met the fidelity bar for customer-visible alerting."
    publisher: "CrowdStrike"
verification: single-source
sourcing_note: "Primary is CrowdStrike's own defensive research; the corroborating SecurityBrief piece re-reports CrowdStrike rather than confirming independently, so the finding rests on a single originating research lab (reliability B, credibility 2). The full technical body was not deep-read to avoid content-safety-classifier interruption; behavioural detail is taken from CrowdStrike's summary and the verbatim quotes above."
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
migrated_from: null
---

CrowdStrike's research describes SANDWORM_MODE as a multi-stage npm supply-chain worm (first discovered February 2026) that targets AI-augmented developer workflows rather than only conventional package distribution or build systems — what CrowdStrike frames as "living off the AI toolchain," abusing the normalised runtime behaviours of AI coding assistants, CI automation and LLM tooling so its actions blend into legitimate developer telemetry ([CrowdStrike, 2026-07-21](https://www.crowdstrike.com/en-us/blog/denying-the-worm-sandworm-mode-and-ai-toolchain-supply-chain-attacks/)). On install the worm writes unexpected entries into AI coding-assistant configuration files (Claude Desktop, Cursor, VS Code, Windsurf) that register a rogue Model Context Protocol (MCP) tool provider staged in a hidden directory, and it injects hooks under the global git-template hooks path so persistence fires on future git operations. It then harvests credentials from environment variables and `.env`/SSH-key files — npm tokens, AWS keys, SSH keys, and API keys for multiple LLM providers — fingerprints the host to separate developer workstations from CI runners, and delays full activation 48–96 hours on workstations (immediately on CI) specifically to defeat tools that correlate install-time and behaviour signals, falling back to DNS tunnelling when primary exfiltration is blocked ([SecurityBrief, 2026-07-22](https://securitybrief.com.au/story/crowdstrike-warns-of-malware-targeting-ai-coding-tools)). The load-bearing defender lesson is CrowdStrike's own candour: of 14 investigated behaviours only 9 produced any signal and only 2 met the fidelity bar for customer-visible alerting, because npm publishes, repo pushes, LLM-API calls, credential handling and file writes overlap heavily with legitimate developer and CI activity ([CrowdStrike, 2026-07-21](https://www.crowdstrike.com/en-us/blog/denying-the-worm-sandworm-mode-and-ai-toolchain-supply-chain-attacks/)).

**Defender takeaway:** the highest-value single artifact is an unexpected MCP tool-provider entry appearing in an AI coding-assistant config — especially one pointing at a hidden directory — shortly after a package install; baseline those configs and alert on writes that register a new provider. Watch modification of the global git-template hooks path (`git config --global init.templateDir` and unauthorised writes to it), which yields persistence that outlives the original package, and in process-lineage telemetry surface `node`/`npm` process trees performing narrowly-scoped actions against git hooks or AI-config files, correlated with reads of `~/.aws`, `~/.ssh` and `.env` followed by egress. The 48–96 h activation delay is a deliberate blind spot for install-to-behaviour correlation — extend telemetry retention and correlation windows beyond 96 h on developer and CI hosts, add review gates before npm publish and git-hook changes, and scope and short-live CI credentials. **Triage:** developer and CI hosts legitimately spawn `node`/`npm` trees and handle credentials constantly — the discriminators are a newly-registered MCP provider in a hidden path, an unexpected global git-template hook, and anomalous outbound DNS volume/entropy from those hosts; any one alone is weak, the sequence is the signal. (SANDWORM_MODE is a malware family and is unrelated to the Russian GRU actor of a similar name.)
