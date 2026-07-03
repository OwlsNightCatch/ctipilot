---
schema: 1
kind: threat
horizon: operational
title: "npm ships 2FA-gated \"staged publishing\" GA in response to the 2026 supply-chain worm waves"
headline: "npm ships 2FA-gated \"staged publishing\" GA in response to the 2026 supply-chain worm waves"
summary: "UPDATE (supply-chain worm wave, originally covered 2026-05-23): GitHub announced on 2026-05-22 that npm staged publishing is now Generally Available — a maintainer must run npm stage publish (npm CLI 11.15.0+), which uploads the version to a consumer-invisible staging queue, then pass a separate 2FA …"
discovered_at: "2026-05-24T05:00:05Z"
event_date: 2026-05-23
run_id: 2026-05-24-f1fd8070
priority: notable
immediate_action: null
tags:
  - supply-chain
  - identity
regions:
  - global
sectors:
  - technology
  - public-sector
entities:
  - "actor:teampcp"
cves: []
sources:
  - url: "https://github.blog/changelog/2026-05-22-staged-publishing-and-new-install-time-controls-for-npm/"
    publisher: "GitHub Changelog, 2026-05-22"
    role: primary
  - url: "https://thehackernews.com/2026/05/npm-adds-2fa-gated-publishing-and.html"
    publisher: "The Hacker News, 2026-05-23"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: "migration: update target unresolved (originally covered 2026-05-23)"
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-24.md
---

**UPDATE (supply-chain worm wave, originally covered 2026-05-23):** GitHub announced on 2026-05-22 that npm **staged publishing** is now Generally Available — a maintainer must run `npm stage publish` (npm CLI 11.15.0+), which uploads the version to a consumer-invisible staging queue, then pass a separate 2FA challenge to approve the release before it becomes installable ([GitHub Changelog, 2026-05-22](https://github.blog/changelog/2026-05-22-staged-publishing-and-new-install-time-controls-for-npm/)). This directly targets the automated mass-publish pattern behind the Megalodon GitHub-repo campaign (covered 2026-05-23) and the earlier mini-shai-hulud / TeamPCP npm waves, where many malicious versions were pushed in seconds via compromised maintainer sessions — a human-in-the-loop 2FA gate would have broken that tempo.

The same release adds three install-source restriction flags — `--allow-file`, `--allow-remote` and `--allow-directory` (each `all` | `none`) — letting CI/CD pipelines forbid installs from remote URLs or local paths, the vectors abused in several 2026 dependency-confusion and supply-chain campaigns ([The Hacker News, 2026-05-23](https://thehackernews.com/2026/05/npm-adds-2fa-gated-publishing-and.html)). For CH/EU public-sector development teams, the operational action is to enable staged publishing on org-owned packages and set `--allow-remote none` / `--allow-directory none` in production CI.
