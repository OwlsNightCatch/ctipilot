---
schema: 1
kind: research
title: npm v12 will disable install scripts by default — audit CI/CD pipelines before July
headline: npm v12 will disable install scripts by default — audit CI/CD pipelines before July
summary: "GitHub announced that npm v12 (expected July 2026) disables dependency lifecycle scripts (preinstall/install/postinstall, including implicit node-gyp builds) by default, requires npm approve-scripts for explicit opt-in, and blocks Git/remote-URL dependencies without --allow-git/--allow-remote (GitHub …"
discovered_at: "2026-06-12T05:00:09Z"
event_date: 2026-06-11
run_id: 2026-06-12-5ab9a319
priority: notable
immediate_action: null
tags:
  - supply-chain
regions:
  - global
sectors:
  - technology
entities:
  - "campaign:ironworm"
  - "actor:teampcp"
cves: []
sources:
  - url: "https://github.blog/changelog/2026-06-09-upcoming-breaking-changes-for-npm-v12/"
    publisher: GitHub Changelog
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/github-announces-npm-security-changes-to-tackle-supply-chain-attacks/"
    publisher: BleepingComputer
    role: corroborating
  - url: "https://thehackernews.com/2026/06/github-to-disable-npm-install-scripts.html"
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
migrated_from: briefs/2026-06-12.md
---

GitHub announced that npm v12 (expected July 2026) disables dependency lifecycle scripts (`preinstall`/`install`/`postinstall`, including implicit `node-gyp` builds) by default, requires `npm approve-scripts` for explicit opt-in, and blocks Git/remote-URL dependencies without `--allow-git`/`--allow-remote` ([GitHub Changelog, 2026-06-09](https://github.blog/changelog/2026-06-09-upcoming-breaking-changes-for-npm-v12/)). This is a structural response to the install-script abuse that powered this spring's npm worm wave (Shai-Hulud/Miasma, IronWorm, TeamPCP — coverage 2026-06-06 through 2026-06-10) and brings npm in line with other package managers that already block install scripts by default ([BleepingComputer, 2026-06-11](https://www.bleepingcomputer.com/news/security/github-announces-npm-security-changes-to-tackle-supply-chain-attacks/)). The warnings are live today in npm ≥ 11.16.0. Defender takeaway: this is a breaking change with a security upside — run `npm install` under 11.16.0 now to enumerate deprecation warnings, build the script allow-list before v12 ships, and treat any pipeline that must keep scripts enabled wholesale as a finding.
