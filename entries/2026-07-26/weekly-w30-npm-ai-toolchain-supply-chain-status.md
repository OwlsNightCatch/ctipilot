---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-long-running
title: "npm / AI-developer-toolchain supply-chain wave status: this week the front edge moved from poisoning packages to poisoning the AI coding assistant's own trust config, via rogue MCP tool-provider entries"
headline: "SANDWORM_MODE extends the tracked supply-chain wave into the AI coding assistant itself — rogue MCP server entries in AI-assistant configs"
summary: >
  Update to the tracked npm / developer-ecosystem supply-chain wave. Prior weeklies followed it from install-hook-evasion package compromises (jscrambler, injectivelabs) to abuse of the trust machinery around packages (AsyncAPI riding a legitimate CI/CD release workflow to ship provenance-attested malicious versions; DPRK Contagious Interview targeting developers directly). This week CrowdStrike documented SANDWORM_MODE, which moves the front edge one layer further in: rather than poisoning a package or a pipeline, the multi-stage npm worm writes rogue Model Context Protocol (MCP) tool-provider entries into AI coding-assistant configurations (Cursor, VS Code, Claude Desktop, Windsurf), injects global git-template hooks for persistence, and exfiltrates npm/AWS/SSH credentials plus multi-provider LLM API keys — delaying activation 48-96 hours to defeat install-versus-behaviour correlation. The transferable lesson is unchanged in direction but sharper in target: the developer's AI-assisted toolchain and its trust configuration are now the initial-access objective, and of 14 investigated behaviours CrowdStrike found only 2 met the bar for high-fidelity alerting because the worm's actions blend into legitimate developer and CI telemetry.
discovered_at: "2026-07-26T23:46:00Z"
event_date: 2026-07-21
run_id: 2026-07-26T2309Z-weekly
priority: notable
immediate_action: null
tags:
  - supply-chain
  - infostealer
  - ai-abuse
regions:
  - global
  - europe
sectors:
  - public-sector
  - technology
entities:
  - malware:sandworm-mode
cves: []
techniques:
  - T1195.002
  - T1552.001
  - T1546
  - T1071.004
  - T1497
affected_products: []
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
evidence: []
verification: multi-source
sourcing_note: "CrowdStrike is the primary first-party researcher; SecurityBrief corroborates the headline claim. This is a status delta on the tracked wave — the 48-96h activation delay, MCP-config poisoning and git-template persistence are the new facts, and are attributed to CrowdStrike's own analysis."
confidence: high
update_of: 2026-07-19/weekly-w29-npm-supply-chain-developer-targeting
references:
  - 2026-07-23/sandworm-mode-npm-ai-toolchain-supply-chain-worm-mcp
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

**UPDATE (originally covered 2026-07-19):** the npm / developer-ecosystem supply-chain wave this pipeline has tracked across prior weeklies added a distinct front this week, and the delta is the target layer.

Earlier stages of the wave moved from poisoning published packages with evasive install hooks (jscrambler, injectivelabs) to abusing the trust machinery around packages — the AsyncAPI compromise rode the org's own legitimate CI/CD release workflow so its trojanized versions carried cryptographically valid provenance attestations, and the DPRK-aligned Contagious Interview campaign targeted developers directly through fake job repos. This week's addition, CrowdStrike's SANDWORM_MODE, moves one layer further in: instead of poisoning a package or a pipeline, the multi-stage npm worm writes rogue Model Context Protocol (MCP) tool-provider entries into AI coding-assistant configurations — Cursor, VS Code, Claude Desktop and Windsurf — so the assistant itself loads and trusts an attacker-controlled tool provider, injects global git-template hooks for persistence, and exfiltrates npm, AWS and SSH credentials alongside multi-provider LLM API keys, delaying activation 48-96 hours on workstations to break the correlation between install time and malicious behaviour ([CrowdStrike, 2026-07-21](https://www.crowdstrike.com/en-us/blog/denying-the-worm-sandworm-mode-and-ai-toolchain-supply-chain-attacks/)).

**Defender takeaway:** the wave's direction is unchanged — the developer and the build/trust machinery are the initial-access target, not just the registry — but the newly-added surface is the AI coding assistant's own configuration, which most organisations do not yet monitor or baseline. CrowdStrike's own detection finding is the operative point for defenders building coverage: of 14 investigated behaviours only 2 met the bar for high-fidelity alerting, because the worm's file writes and network calls blend into legitimate developer and CI telemetry. That argues for treating AI-assistant MCP-server configuration files and global git-template hooks as monitored, change-controlled artifacts on developer endpoints, and for scoping developer-workstation credential exposure (npm tokens, cloud keys, LLM API keys) as a blast-radius question rather than assuming install-script scanning covers it. Mechanics are in the referenced operational entry.
