---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-multi-day
title: TeamPCP / Mini Shai-Hulud npm supply-chain worm — wave 4 + framework source leak
headline: TeamPCP / Mini Shai-Hulud npm supply-chain worm — wave 4 + framework source leak
summary: "TeamPCP Mini Shai-Hulud wave 4 compromised 170+ npm packages / 400+ malicious versions per daily-brief tracking (TanStack, UiPath, Mistral AI, OpenSearch, OpenAI named); Datadog static analysis of the leaked Shai-Hulud framework source (2026-05-12 leak) surfaces previously-undocumented IDE-persistence hooks targeting .claude/settings.json and .vscode/tasks.json, plus OIDC token extraction from /proc/<pid>/mem to forge Sigstore provenance attestations. Provenance-only verification no longer separates malicious from legitimate publications. (Datadog Security Labs · Wiz Blog · daily 2026-05-13 UPDATE · daily 2026-05-15 UPDATE)"
discovered_at: "2026-05-11T05:00:05Z"
event_date: 2026-05-15
run_id: 2026-W20-71c96b25
priority: high
immediate_action: null
tags:
  - supply-chain
  - ai-abuse
  - actively-exploited
regions:
  - global
sectors:
  - technology
entities:
  - "campaign:mini-shai-hulud"
  - "actor:shinyhunters"
  - "tool:pcpjack-cloud-worm-2026"
  - "actor:teampcp"
cves: []
sources:
  - url: "https://securitylabs.datadoghq.com/articles/shai-hulud-open-source-framework-static-analysis/"
    publisher: Datadog Security Labs
    role: primary
  - url: "https://www.wiz.io/blog/mini-shai-hulud-strikes-again-tanstack-more-npm-packages-compromised"
    publisher: Wiz Blog
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
migrated_from: briefs/weekly/2026-W20.md
---

The TeamPCP / Mini Shai-Hulud story spans every working day of 2026-W20 and the daily briefs add a piece each day. **Tuesday 2026-05-12:** an attacker briefly published what appears to be the complete Shai-Hulud framework source (TypeScript / Bun) to a public GitHub repository attributed to TeamPCP, taken down within hours but mirrored widely; the public source disclosure inverts the threat model — every IDE, EDR, and PR-review vendor now has access to the same artefact the operator was using but defenders must assume new variants will appear with one to two days' lead-time on signatures ([Datadog Security Labs static analysis, 2026-05-13](https://securitylabs.datadoghq.com/articles/shai-hulud-open-source-framework-static-analysis/); [daily 2026-05-15 UPDATE](/briefs/2026-05-15/)). **Wednesday 2026-05-13:** Wave 4 hits — 170+ packages / 400+ malicious versions compromised per daily-brief tracking across `@tanstack` (including `react-router`, ~12M weekly downloads), `@uipath`, `@mistralai`, `@opensearch-project`, and `@guardrails-ai`; the Wiz writeup confirms the same TeamPCP / UNC6780 / PCPJack attribution as prior waves ([Wiz Blog, 2026-05-11](https://www.wiz.io/blog/mini-shai-hulud-strikes-again-tanstack-more-npm-packages-compromised); [daily 2026-05-13 UPDATE](/briefs/2026-05-13/)). **Friday 2026-05-15:** OpenAI named as a victim; the company enforces code-signing certificate rotation across all macOS apps as remediation ([daily 2026-05-15 UPDATE](/briefs/2026-05-15/)).

What W1 horizon research surfaced that the dailies could not yet see: Datadog's static analysis of the leaked source reveals two new capability classes that change the defender posture. First, **IDE persistence** via hook entries in `.claude/settings.json` (Claude Code) and `.vscode/tasks.json` — allowing arbitrary command execution on developer-workspace events; this is not a build-time supply-chain primitive but a developer-workstation persistence mechanism that survives `npm install` cleanup and outlives the malicious-package removal. Second, **OIDC token extraction directly from `/proc/<pid>/mem` on GitHub Actions runners**, used to forge Sigstore provenance attestations — meaning malicious packages can be published that are indistinguishable from legitimate ones by **provenance verification alone**. The W19 weekly already flagged ShinyHunters / WorldLeaks as a long-running operator-family pattern; the TeamPCP / Mini Shai-Hulud progression confirms a parallel ecosystem maturing on the npm registry side, now with publication-provenance forgery in the toolset. The leaked framework source materially elevates the risk of secondary operators applying Shai-Hulud-style techniques against other package registries (PyPI, Cargo, Maven Central) in 2026-W21 ([Datadog Security Labs](https://securitylabs.datadoghq.com/articles/shai-hulud-open-source-framework-static-analysis/)).

The defender pivot is two-fold: (1) for DevOps pipelines, **provenance verification is necessary but no longer sufficient** — supplement with publisher-pinning, two-factor publish enforcement, and post-install hash-pinning; (2) for developer workstations, treat `.claude/settings.json` / `.vscode/tasks.json` / equivalent IDE hook files as security-relevant configuration and add them to file-integrity-monitoring scope. The Datadog filesystem indicators (`gh-token-monitor` daemon process, `claude@users.noreply.github.com` commits in unexpected repositories, exfil-repo names matching "Shai-Hulud: Here We Go Again") are the right hunt seeds.
