---
schema: 1
kind: threat
title: "DPRK UNK_DeadDrop weaponises VS Code / Cursor auto-run to hit developers, including EU targets"
headline: "DPRK UNK_DeadDrop weaponises VS Code / Cursor auto-run to hit developers, including EU targets"
summary: "Proofpoint details UNK_DeadDrop, a North-Korea-aligned cluster (related to but distinct from Contagious Interview / Famous Chollima) that sent 250+ recruitment-themed phishing emails to ~100 finance, crypto, education and technology organisations over April–May 2026 (Proofpoint, 2026-06-15); the targeted …"
discovered_at: "2026-06-16T05:08:55Z"
event_date: 2026-06-16
run_id: 2026-06-16-38d638e1
priority: notable
immediate_action: null
tags:
  - nation-state
  - supply-chain
  - infostealer
  - north-korea-nexus
regions:
  - global
  - europe
sectors:
  - finance
  - technology
  - education
entities:
  - "campaign:unk-deaddrop-2026"
cves: []
sources:
  - url: "https://www.proofpoint.com/us/blog/threat-insight/dont-fear-repo-unkdeaddrop-phishing-campaign-targets-developers-steal"
    publisher: Proofpoint
    role: primary
  - url: "https://thehackernews.com/2026/06/north-korean-hackers-are-turning.html"
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
migrated_from: briefs/2026-06-16.md
---

Proofpoint details **UNK_DeadDrop**, a North-Korea-aligned cluster (related to but distinct from Contagious Interview / Famous Chollima) that sent 250+ recruitment-themed phishing emails to ~100 finance, crypto, education and technology organisations over April–May 2026 ([Proofpoint, 2026-06-15](https://www.proofpoint.com/us/blog/threat-insight/dont-fear-repo-unkdeaddrop-phishing-campaign-targets-developers-steal)); the targeted geographies are a US majority followed by the UK, Australia, **France, Germany and the Netherlands**, among others ([The Hacker News, 2026-06-16](https://thehackernews.com/2026/06/north-korean-hackers-are-turning.html)). The lure links to attacker-controlled GitHub/GitLab repositories carrying a `.vscode/tasks.json` with `runOn: folderOpen`; VS Code shows a workspace-trust prompt, but **Cursor IDE executes the task silently with no prompt**, dropping the open-source **Overlord** Go C2 that steals browser credentials and crypto wallets ([The Hacker News, 2026-06-16](https://thehackernews.com/2026/06/north-korean-hackers-are-turning.html)). Mapped to `T1566.002`, `T1195.001`, `T1059.004` and `T1555.003`.

**Why it matters to us:** public-sector and fintech development teams that have adopted Cursor are exposed to silent execution on repository open. Hunt for editor processes (`code`, `cursor`) spawning shell/script interpreters outside build directories (Sysmon EID 1 parent-image filter); enforce workspace-trust policy and restrict VSIX installation to an approved-publisher allowlist via enterprise policy.
