---
schema: 1
kind: threat
horizon: operational
title: "Shai-Hulud/Miasma supply-chain worm jumps to PyPI as \"Hades\" — 37 malicious wheels across 19 packages"
headline: "Shai-Hulud/Miasma supply-chain worm jumps to PyPI as \"Hades\" — 37 malicious wheels across 19 packages"
summary: "UPDATE (originally covered 2026-06-06): The Miasma/Mini-Shai-Hulud supply-chain lineage previously tracked across npm and GitHub has opened a PyPI front dubbed \"Hades\": Socket and others identified 37 malicious wheel artifacts across 19 packages abusing Python's .pth site-module startup mechanism to auto-execute …"
discovered_at: "2026-06-10T05:00:17Z"
event_date: 2026-06-09
run_id: 2026-06-10-c84347b2
priority: notable
immediate_action: null
tags:
  - supply-chain
  - infostealer
  - ai-abuse
  - cloud
regions:
  - global
sectors:
  - technology
  - education
entities: []
cves: []
sources:
  - url: "https://thehackernews.com/2026/06/hades-pypi-attack-19-packages-poisoned.html"
    publisher: "The Hacker News, 2026-06-09"
    role: primary
  - url: "https://socket.dev/blog/shai-hulud-descends-to-hades-miasma-pypi-wave"
    publisher: "Socket, 2026-06-07"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: 2026-06-06/miasma-supply-chain-worm-reaches-73-microsoft-github-reposit
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-10.md
---

**UPDATE (originally covered 2026-06-06):** The Miasma/Mini-Shai-Hulud supply-chain lineage previously tracked across npm and GitHub has opened a PyPI front dubbed "Hades": Socket and others identified 37 malicious wheel artifacts across 19 packages abusing Python's `.pth` site-module startup mechanism to auto-execute on interpreter start without an import ([The Hacker News, 2026-06-09](https://thehackernews.com/2026/06/hades-pypi-attack-19-packages-poisoned.html)). The payload downloads the Bun runtime from GitHub and runs triple-encrypted JavaScript that sweeps GitHub/CI tokens, npm/PyPI/cloud (AWS/GCP/Azure) keys, Kubernetes and Vault configs, SSH keys and AI-tool configs, and plants backdoor config in AI coding-assistant workspaces so future agent sessions execute attacker instructions ([Socket, 2026-06-07](https://socket.dev/blog/shai-hulud-descends-to-hades-miasma-pypi-wave)).

Affected packages spanned developer tooling and a bioinformatics cluster (relevant to university/research compute), all since removed. Hunt for `*-setup.pth` creation under `site-packages`, Bun binary downloads from `github.com/oven-sh/bun`, and the `$TMPDIR/.bun_ran` sentinel via Sysmon EID 1 with parent `python`/`pip` (T1547.013, T1059.007, T1555). Pin dependencies and install with `--ignore-scripts`; audit recently-installed PyPI packages on research endpoints.
