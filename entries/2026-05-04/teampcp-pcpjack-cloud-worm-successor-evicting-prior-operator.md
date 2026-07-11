---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-long-running
title: "TeamPCP → PCPJack — cloud-worm successor evicting prior operator artefacts"
headline: "TeamPCP → PCPJack — cloud-worm successor evicting prior operator artefacts"
summary: "Current state: SentinelLabs documented PCPJack on 2026-05-07 as a worm-class framework that evicts and deletes existing TeamPCP artefacts on compromise (giving the framework its name), then deploys six Python modules harvesting credentials from Docker, Kubernetes, Redis, MongoDB, RayML, and dozens of cloud / SaaS …"
discovered_at: "2026-05-04T05:00:37Z"
event_date: 2026-05-10
run_id: 2026-W19-a5788b22
priority: notable
immediate_action: null
tags:
  - organized-crime
  - cloud
  - vulnerabilities
  - actively-exploited
  - supply-chain
regions:
  - global
sectors:
  - technology
entities:
  - "campaign:mini-shai-hulud"
  - "tool:pcpjack-cloud-worm-2026"
  - "actor:teampcp"
cves: []
sources:
  - url: "https://www.sentinelone.com/labs/cloud-worm-evicts-teampcp-and-steals-credentials-at-scale/"
    publisher: SentinelLabs — Cloud worm evicts TeamPCP
    role: primary
  - url: "https://thehackernews.com/2026/05/pcpjack-credential-stealer-exploits-5.html"
    publisher: The Hacker News — PCPJack credential stealer
    role: corroborating
  - url: "https://www.securityweek.com/pcpjack-worm-removes-teampcp-infections-steals-credentials/"
    publisher: SecurityWeek — PCPJack worm
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
migrated_from: briefs/weekly/2026-W19.md
---

Current state: SentinelLabs documented **PCPJack** on 2026-05-07 as a worm-class framework that evicts and deletes existing TeamPCP artefacts on compromise (giving the framework its name), then deploys six Python modules harvesting credentials from Docker, Kubernetes, Redis, MongoDB, RayML, and dozens of cloud / SaaS services (AWS, Azure, GCP, GitHub, Slack, HashiCorp Vault, 1Password). Propagation targets are pulled from Common Crawl Parquet files rather than ad-hoc scanning — far broader curated attack surface than typical opportunistic worms. Weaponises five public CVEs simultaneously ([CVE-2025-29927](https://nvd.nist.gov/vuln/detail/CVE-2025-29927) Next.js, [CVE-2025-55182](https://nvd.nist.gov/vuln/detail/CVE-2025-55182) React2Shell, [CVE-2026-1357](https://nvd.nist.gov/vuln/detail/CVE-2026-1357) WPVivid, [CVE-2025-9501](https://nvd.nist.gov/vuln/detail/CVE-2025-9501) W3 Total Cache, [CVE-2025-48703](https://nvd.nist.gov/vuln/detail/CVE-2025-48703) CWP). The TeamPCP → PCPJack succession overlay is the operational specific worth tracking: SentinelLabs explicitly states there is no evidence yet of a direct operator-level connection, while the eviction logic implies operators familiar with TeamPCP's target population. Defenders running self-hosted Next.js, React-server-actions stacks, WordPress with WPVivid Backup or W3 Total Cache, or CentOS Web Panel with internet-reachable FileManager should treat all five CVEs as actively weaponised ([SentinelLabs, 2026-05-07](https://www.sentinelone.com/labs/cloud-worm-evicts-teampcp-and-steals-credentials-at-scale/) · [The Hacker News, 2026-05-07](https://thehackernews.com/2026/05/pcpjack-credential-stealer-exploits-5.html) · [SecurityWeek, 2026-05-08](https://www.securityweek.com/pcpjack-worm-removes-teampcp-infections-steals-credentials/) · [daily 2026-05-10](/briefs/2026-05-10/)). The earlier TeamPCP "Mini Shai-Hulud" SAP CAP npm worm (covered 2026-05-06) used Claude Code SessionStart hooks and VSCode tasks for propagation — that thread is separate from PCPJack's CVE-chain propagation but the same operator population is tracked.
