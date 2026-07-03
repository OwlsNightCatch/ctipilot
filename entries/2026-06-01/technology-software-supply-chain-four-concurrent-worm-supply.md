---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-sector-patterns
title: Technology / software supply chain — four concurrent worm/supply-chain threats in one week
headline: Technology / software supply chain — four concurrent worm/supply-chain threats in one week
summary: "IronWorm: first eBPF-rootkit npm worm sweeps cloud/AI credentials from ~36 packages via Tor C2. Kernel-mode rootkit hides the implant from procfs and most EDR agents — user-space process hunting is insufficient. (daily, JFrog)"
discovered_at: "2026-06-01T05:00:11Z"
event_date: 2026-06-07
run_id: 2026-W23-9118e7bd
priority: high
immediate_action: null
tags:
  - supply-chain
  - infostealer
  - cloud
  - identity
regions:
  - global
sectors:
  - technology
entities:
  - "campaign:ironworm"
cves: []
sources:
  - url: "https://research.jfrog.com/post/iron-worm-shai-hulud-rustier-cousin/"
    publisher: JFrog — IronWorm
    role: primary
  - url: "https://flatt.tech/research/posts/poisoning-claude-code-one-github-issue-to-break-the-supply-chain/"
    publisher: GMO Flatt Security — claude-code-action
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/suspicious-polyfill-login-prompts-pop-up-on-toshiba-muji-websites/"
    publisher: BleepingComputer — Polyfill.io
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

Simultaneously active this week: Miasma npm credential collectors, IronWorm eBPF rootkit worm, two concurrent npm dependency confusion campaigns (Microsoft 45 packages + Sonatype 176 packages, [daily 2026-06-01](/briefs/2026-06-01/)), the claude-code-action GitHub Actions flaw (arbitrary code execution from a single malicious issue, fixed in v1.0.94; [daily 2026-06-05](/briefs/2026-06-05/)), and Polyfill.io domain reactivation surfacing native browser credential prompts on sites still loading the legacy CDN reference ([daily 2026-06-07](/briefs/2026-06-07/)). The combined picture is a meaningful escalation of the npm/GitHub Actions attack surface: credential theft, kernel-rootkit persistence, and CI/CD pipeline compromise are now simultaneous, not sequential, threats in the software supply chain.
