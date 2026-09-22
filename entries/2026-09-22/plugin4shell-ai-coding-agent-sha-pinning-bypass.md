---
schema: 1
kind: vulnerability
title: "Plugin4Shell: a zero-click design flaw breaks plugin SHA-pinning identically across Claude Code, OpenAI Codex, GitHub Copilot and Gemini CLI"
headline: "Two of four major AI coding agents remain unpatched against a zero-click plugin-marketplace takeover technique"
summary: >
  AIR Security disclosed Plugin4Shell (2026-09-17): a zero-click remote-code-execution
  design flaw present identically in Claude Code, OpenAI Codex, GitHub Copilot and
  Gemini CLI — none of the four verifies, after checkout, that a plugin's working tree
  actually matches its marketplace-pinned commit hash, letting a repository owner
  silently swap in malicious code on an already-installed, already-trusted plugin's
  next background auto-update. Anthropic and OpenAI have patched; Microsoft has shipped
  no fix for Copilot and Google is deprecating Gemini CLI instead of fixing it.
discovered_at: "2026-09-22T04:34:00Z"
updated_at: null
event_date: "2026-09-17"
run_id: 2026-09-22T0410Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, supply-chain, rce, zero-click]
regions: [global]
sectors: [public-sector]
entities: []
techniques: [T1195.002]
affected_products: ["Anthropic Claude Code", "OpenAI Codex", "GitHub Copilot", "Google Gemini CLI"]
cves: []
sources:
  - url: "https://www.air.security/blog-posts/plugin4shell"
    publisher: "AIR Security"
    date: "2026-09-17"
    role: primary
  - url: "https://thehackernews.com/2026/09/plugin4shell-lets-repository-owners.html"
    publisher: "The Hacker News"
    date: "2026-09-18"
    role: corroborating
  - url: "https://www.helpnetsecurity.com/2026/09/18/plugin4shell-ai-coding-agents-vulnerability/"
    publisher: "Help Net Security"
    date: "2026-09-18"
    role: corroborating
  - url: "https://www.heise.de/news/Kritische-Luecke-bei-Claude-Code-OpenAI-Codex-GitHub-Copilot-und-Gemini-CLI-11459862.html"
    publisher: "heise online (Manuel Masiero)"
    date: "2026-09-21"
    role: corroborating
closed_sources: []
evidence:
  - quote: "It is a plugin SHA-pinning bypass: the agent checks out the exact commit the marketplace pinned but never verifies it landed there, so an attacker who controls the plugin's repo makes the checkout resolve to malicious code while the pin still looks honored. The result is zero-click remote code execution across Claude Code, Codex, GitHub Copilot, and Gemini CLI."
    publisher: "AIR Security"
  - quote: "Google has deprecated the Gemini CLI and will not patch it, so every install stays vulnerable for good; those users should migrate to Antigravity, which this attack does not reach"
    publisher: "AIR Security"
verification: multi-source
sourcing_note: null
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions:
  - "Apply the vendor patch now: upgrade Claude Code to ≥2.1.179 and Codex to ≥0.146.0. GitHub Copilot and consumer Gemini CLI have no fix; on those two, manually verify `git rev-parse HEAD` against a plugin's marketplace-pinned SHA before trusting any auto-update, and restrict Copilot plugin installs to the built-in GitHub-hosted marketplace until Microsoft ships a fix."
updates: []
migrated_from: null
---

Security firm AIR disclosed Plugin4Shell on 2026-09-17: a zero-click remote-code-execution design flaw present identically in four major AI coding agents — Claude Code, OpenAI Codex, GitHub Copilot and Gemini CLI. All four implement plugin-marketplace SHA-pinning, locking each install to a reviewed 40-hex commit hash, but none verifies after checkout that the resolved working tree actually matches that hash ([AIR Security, 2026-09-17](https://www.air.security/blog-posts/plugin4shell)). An attacker who controls or takes over a trusted plugin's upstream repository creates a branch named identically to the pinned SHA and sets it as the repository's default branch; Claude Code, Codex and Copilot run a plain `git clone` followed by a checkout of the pinned commit, and because git resolves an ambiguous ref-versus-object-id in favor of the ref, the checkout silently resolves to the attacker's branch while the agent reports the pinned commit installed ([AIR Security, 2026-09-17](https://www.air.security/blog-posts/plugin4shell)). Gemini CLI has a distinct but equally exploitable variant: it fetches the pinned commit into `FETCH_HEAD` then checks that out, which an attacker defeats by naming their malicious default branch literally "FETCH_HEAD" ([AIR Security, 2026-09-17](https://www.air.security/blog-posts/plugin4shell)).

Because background plugin auto-update is the default in Claude Code and Codex, an already-installed, already-reviewed plugin is silently swapped on the next update with no install step and no prompt — full zero-click compromise of the agent and "full access to every asset and every piece of data the agent can reach" ([AIR Security, 2026-09-17](https://www.air.security/blog-posts/plugin4shell)). AIR built a working test attack against all four agents in May 2026 and disclosed it to the vendors in June ([The Hacker News, 2026-09-18](https://thehackernews.com/2026/09/plugin4shell-lets-repository-owners.html)); Anthropic patched in Claude Code 2.1.179 and OpenAI in Codex 0.146.0, Microsoft has shipped no fix for Copilot, and consumer Gemini CLI is being deprecated rather than patched, so every existing install "stays vulnerable for good" ([AIR Security, 2026-09-17](https://www.air.security/blog-posts/plugin4shell)). Google's security researchers received confirmation of this on 2026-08-04; enterprise access via Gemini Code Assist or Google Cloud remains unaffected, and Google's replacement, Antigravity CLI, currently has no comparable SHA-pinning mechanism to bypass (translated from German) ([heise online, 2026-09-21](https://www.heise.de/news/Kritische-Luecke-bei-Claude-Code-OpenAI-Codex-GitHub-Copilot-und-Gemini-CLI-11459862.html)).

The Hacker News independently checked the shipped plugin catalogs on 2026-09-18 and adds a material scope caveat: background auto-update is on by default only for each agent's own built-in, GitHub-hosted marketplace, and every plugin it checked in Anthropic's community catalog and the default Claude Code/Copilot catalogs points to a GitHub repository, which rejects SHA-shaped branch names outright — so the branch-hijack variant does not reach a user who installs only from an agent's default marketplace ([The Hacker News, 2026-09-18](https://thehackernews.com/2026/09/plugin4shell-lets-repository-owners.html)). The risk concentrates on externally-hosted marketplaces — AIR and The Hacker News name Bitbucket and self-hosted git servers, and heise online additionally names GitLab (translated from German) ([The Hacker News, 2026-09-18](https://thehackernews.com/2026/09/plugin4shell-lets-repository-owners.html); [heise online, 2026-09-21](https://www.heise.de/news/Kritische-Luecke-bei-Claude-Code-OpenAI-Codex-GitHub-Copilot-und-Gemini-CLI-11459862.html)) — where auto-update is off by default but can be enabled; Gemini CLI's `FETCH_HEAD`-named-branch variant is not clearly blocked by GitHub's hash-name restriction, so a GitHub-hosted Gemini plugin is not established as safe. As of 2026-09-18, no CVE identifier had been assigned and no source reported exploitation in the wild ([The Hacker News, 2026-09-18](https://thehackernews.com/2026/09/plugin4shell-lets-repository-owners.html)).

**Detection:** monitor the coding agent's plugin-manager child processes (process-creation events for the git binary spawned by the agent) for a plugin directory whose `.git` HEAD resolves to a symbolic ref (a branch) rather than a detached commit matching the marketplace-pinned SHA — that mismatch is the only reliable discriminator AIR names. **Triage:** routine background plugin auto-update produces identical git clone/checkout telemetry to the attack, so a single benign-looking update event is not itself suspicious; the discriminator is the HEAD-resolves-to-a-branch condition, not the presence of an update.

**Defender takeaway:** patch Claude Code and Codex immediately; for Copilot and consumer Gemini CLI, where no fix exists, verify plugin commit hashes manually and restrict installs to marketplaces that reject SHA-shaped branch names until the vendors ship a fix.
