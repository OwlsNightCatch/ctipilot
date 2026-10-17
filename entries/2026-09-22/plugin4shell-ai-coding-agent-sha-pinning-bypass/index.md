---
schema: 1
kind: vulnerability
title: "Plugin4Shell: a zero-click design flaw breaks plugin SHA-pinning identically across Claude Code, OpenAI Codex, GitHub Copilot and Gemini CLI"
headline: "AI coding agents' plugin SHA-pinning is bypassable, mainly via plugins hosted on Bitbucket or self-hosted git, and only consumer Gemini CLI stays unfixed"
summary: >
  AIR Security disclosed Plugin4Shell (2026-09-17): a design flaw present in Claude Code, OpenAI
  Codex, GitHub Copilot and Gemini CLI, none of which verified after checkout that a plugin's
  working tree matches its marketplace-pinned commit hash, so a repository owner can swap malicious
  code into an installed, trusted plugin on its next update. The branch-name trick needs a git host
  that accepts hash-shaped branch names, such as Bitbucket or a self-hosted server (GitHub and GitLab
  reject them), and auto-update is on by default only for the agents' built-in GitHub-hosted
  marketplaces; Gemini CLI's variant is not clearly blocked on GitHub. OpenAI's own fix shipped in
  Codex 0.146.0, AIR says Claude Code 2.1.179 is fixed, heise online reports, citing GitHub support,
  that Copilot CLI 1.0.87 and the Copilot app 1.1.23 carry a fix, and Google is retiring consumer
  Gemini CLI instead of fixing it.
discovered_at: "2026-09-22T04:34:00Z"
updated_at: "2026-09-30T06:56:16Z"
event_date: "2026-09-17"
run_id: 2026-09-22T0410Z-intel
priority: notable
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
  - "Upgrade Codex to 0.146.0 or later (OpenAI's own fix), Claude Code to 2.1.179 or later (fixed according to AIR, though Anthropic's release notes do not mention it), and Copilot CLI to 1.0.87 or later and the Copilot app to 1.1.23 or later (fixed according to GitHub support, as reported by heise online). Consumer Gemini CLI gets no fix: on it, verify `git rev-parse HEAD` against a plugin's marketplace-pinned SHA before trusting any update, or migrate off it as AIR advises."
updates:
  - at: "2026-09-30T06:56:16Z"
    run_id: 2026-09-30T0639Z-audit
    type: update
    summary: >
      GitHub has fixed Copilot (Copilot CLI 1.0.87, Copilot app 1.1.23, according to GitHub support
      as reported by heise online), and heise now states that GitLab is not exploitable through the
      branch-name variant. The Claude Code fix is attributed to AIR, since Anthropic's release notes
      do not mention it, and the GitHub scope limit on the branch-name variant is stated up front.
      Priority moves from high to notable: developer-tooling research without in-the-wild
      exploitation. The 2026-08-04 confirmation of no fix for consumer Gemini CLI went to the
      researchers, not to Google's own researchers.
    fields: [priority, updated_at, headline, summary, actions, body]
migrated_from: null
---

Security firm AIR disclosed Plugin4Shell on 2026-09-17: a zero-click remote-code-execution design flaw present identically in four major AI coding agents: Claude Code, OpenAI Codex, GitHub Copilot and Gemini CLI. All four implement plugin-marketplace SHA-pinning, locking each install to a reviewed 40-hex commit hash, but none verifies after checkout that the resolved working tree actually matches that hash ([AIR Security, 2026-09-17](https://www.air.security/blog-posts/plugin4shell)). An attacker who controls or takes over a trusted plugin's upstream repository creates a branch named identically to the pinned SHA and sets it as the repository's default branch; Claude Code, Codex and Copilot run a plain `git clone` followed by a checkout of the pinned commit, and because git resolves an ambiguous ref-versus-object-id in favor of the ref, the checkout silently resolves to the attacker's branch while the agent reports the pinned commit installed ([AIR Security, 2026-09-17](https://www.air.security/blog-posts/plugin4shell)). Gemini CLI has a distinct but equally exploitable variant: it fetches the pinned commit into `FETCH_HEAD` then checks that out, which an attacker defeats by naming their malicious default branch literally "FETCH_HEAD" ([AIR Security, 2026-09-17](https://www.air.security/blog-posts/plugin4shell)).

Because background plugin auto-update is the default in Claude Code and Codex, an already-installed, already-reviewed plugin is silently swapped on the next update with no install step and no prompt: full zero-click compromise of the agent and "full access to every asset and every piece of data the agent can reach" ([AIR Security, 2026-09-17](https://www.air.security/blog-posts/plugin4shell)). AIR built a working test attack against all four agents in May 2026 and disclosed it to the vendors in June ([The Hacker News, 2026-09-18](https://thehackernews.com/2026/09/plugin4shell-lets-repository-owners.html)). OpenAI's own public fix for the same bug shipped in Codex 0.146.0, and AIR says Anthropic fixed it in Claude Code 2.1.179, which Anthropic's release notes do not mention ([The Hacker News, 2026-09-18](https://thehackernews.com/2026/09/plugin4shell-lets-repository-owners.html)). AIR wrote at disclosure that Microsoft had shipped no fix for Copilot ([AIR Security, 2026-09-17](https://www.air.security/blog-posts/plugin4shell)). By 2026-09-30 heise online had updated its article to report, citing GitHub support, that GitHub closed the flaw in Copilot CLI 1.0.87 and in the Copilot app 1.1.23, and that the fix checks whether the checked-out code matches the pinned commit (translated from German) ([heise online, 2026-09-21](https://www.heise.de/news/Kritische-Luecke-bei-Claude-Code-OpenAI-Codex-GitHub-Copilot-und-Gemini-CLI-11459862.html)). Consumer Gemini CLI is being deprecated rather than patched, so every existing install "stays vulnerable for good" ([AIR Security, 2026-09-17](https://www.air.security/blog-posts/plugin4shell)). On 2026-08-04 the researchers received Google's confirmation that consumer Gemini CLI is being discontinued and will get no fix ([heise online, 2026-09-21](https://www.heise.de/news/Kritische-Luecke-bei-Claude-Code-OpenAI-Codex-GitHub-Copilot-und-Gemini-CLI-11459862.html)). Enterprise access via Gemini Code Assist or Google Cloud is not affected by the discontinuation, and Google's replacement, Antigravity CLI, currently has no comparable SHA-pinning mechanism to bypass (translated from German) ([heise online, 2026-09-21](https://www.heise.de/news/Kritische-Luecke-bei-Claude-Code-OpenAI-Codex-GitHub-Copilot-und-Gemini-CLI-11459862.html)). Google says enterprise access to the Gemini CLI will continue with updates, and whether a fix for this flaw is among them is not clear ([The Hacker News, 2026-09-18](https://thehackernews.com/2026/09/plugin4shell-lets-repository-owners.html)).

The Hacker News independently checked the shipped plugin catalogs on 2026-09-18 and adds a material scope caveat: background auto-update is on by default only for each agent's own built-in, GitHub-hosted marketplace, and every plugin it checked in Anthropic's community catalog and the default Claude Code/Copilot catalogs points to a GitHub repository, which rejects SHA-shaped branch names outright, so the branch-hijack variant does not reach a user who installs only from an agent's default marketplace ([The Hacker News, 2026-09-18](https://thehackernews.com/2026/09/plugin4shell-lets-repository-owners.html)). The risk concentrates on externally-hosted marketplaces: AIR and The Hacker News name Bitbucket and self-hosted git servers ([The Hacker News, 2026-09-18](https://thehackernews.com/2026/09/plugin4shell-lets-repository-owners.html)), while heise online states that GitLab, like GitHub, rejects branch names in commit-hash format and is not exploitable this way (translated from German) ([heise online, 2026-09-21](https://www.heise.de/news/Kritische-Luecke-bei-Claude-Code-OpenAI-Codex-GitHub-Copilot-und-Gemini-CLI-11459862.html)). On those exposed hosts auto-update is off by default but can be enabled. Gemini CLI's `FETCH_HEAD`-named-branch variant is not clearly blocked by GitHub's hash-name restriction, so a GitHub-hosted Gemini plugin is not established as safe. As of 2026-09-18, no CVE identifier had been assigned and no source reported exploitation in the wild ([The Hacker News, 2026-09-18](https://thehackernews.com/2026/09/plugin4shell-lets-repository-owners.html)).

**Detection:** monitor the coding agent's plugin-manager child processes (process-creation events for the git binary spawned by the agent), and after a plugin install or update compare the commit actually checked out in the plugin directory (`git rev-parse HEAD`) with the marketplace-pinned SHA. AIR names this check of the resolved HEAD, rather than of the requested ref, as the assertion that closes both variants ([AIR Security, 2026-09-17](https://www.air.security/blog-posts/plugin4shell)). **Triage:** routine background plugin auto-update produces the same git clone and checkout telemetry as the attack, so a single update event is not itself suspicious. The discriminator is a resolved HEAD that differs from the pinned SHA, not the presence of an update.

**Defender takeaway:** update Codex, Claude Code and Copilot now, keeping in mind that the Claude Code fix rests on AIR's account and the Copilot fix on GitHub support's statement as reported by heise online. Consumer Gemini CLI will not be fixed ([AIR Security, 2026-09-17](https://www.air.security/blog-posts/plugin4shell)), and it is not established that installing its plugins only from GitHub avoids the flaw ([The Hacker News, 2026-09-18](https://thehackernews.com/2026/09/plugin4shell-lets-repository-owners.html)), so verify plugin commit hashes manually or move off it.

## Update — 2026-09-30T06:56:16Z

GitHub has closed the flaw in Copilot: according to GitHub support the fix is in Copilot CLI 1.0.87 and the Copilot app 1.1.23, and it checks whether the checked-out code matches the pinned commit (translated from German) ([heise online, 2026-09-21](https://www.heise.de/news/Kritische-Luecke-bei-Claude-Code-OpenAI-Codex-GitHub-Copilot-und-Gemini-CLI-11459862.html)). heise online also now states that GitLab, like GitHub, rejects branch names in commit-hash format and is not exploitable through the branch-name variant ([heise online, 2026-09-21](https://www.heise.de/news/Kritische-Luecke-bei-Claude-Code-OpenAI-Codex-GitHub-Copilot-und-Gemini-CLI-11459862.html)). The earlier statements that Copilot had no fix and that heise named GitLab as exposed are superseded.

The Claude Code fix rests on AIR's account alone: Anthropic's release notes for 2.1.179 do not mention it, whereas OpenAI's own public fix for the same bug shipped in Codex 0.146.0 ([The Hacker News, 2026-09-18](https://thehackernews.com/2026/09/plugin4shell-lets-repository-owners.html)). The branch-name variant also needs a git host that accepts hash-shaped branch names, which GitHub does not, so users who install plugins only from the agents' default GitHub-based marketplaces are not exposed to it ([The Hacker News, 2026-09-18](https://thehackernews.com/2026/09/plugin4shell-lets-repository-owners.html)). Google's 2026-08-04 confirmation that consumer Gemini CLI will get no fix was given to the researchers, not received by Google's own researchers ([heise online, 2026-09-21](https://www.heise.de/news/Kritische-Luecke-bei-Claude-Code-OpenAI-Codex-GitHub-Copilot-und-Gemini-CLI-11459862.html)).
