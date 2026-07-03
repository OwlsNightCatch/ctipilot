---
schema: 1
kind: policy
horizon: strategic
weekly_section: weekly-policy
title: "npm ships 2FA-gated \"staged publishing\" GA — platform-governance response to the worm waves"
headline: "npm ships 2FA-gated \"staged publishing\" GA — platform-governance response to the worm waves"
summary: "GitHub announced on 2026-05-22 that npm staged publishing is now Generally Available: a maintainer runs npm stage publish to create a staged release that must be explicitly promoted under 2FA before it becomes installable, alongside new install-time controls."
discovered_at: "2026-05-18T05:00:37Z"
event_date: 2026-05-22
run_id: 2026-W21-473d6fa5
priority: notable
immediate_action: null
tags:
  - supply-chain
  - identity
regions:
  - global
sectors:
  - technology
entities: []
cves: []
sources:
  - url: "https://github.blog/changelog/2026-05-22-staged-publishing-and-new-install-time-controls-for-npm/"
    publisher: GitHub Changelog — staged publishing GA
    role: primary
closed_sources: []
evidence: []
verification: single-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/weekly/2026-W21.md
---

GitHub announced on [2026-05-22](/briefs/2026-05-24/) that npm **staged publishing** is now Generally Available: a maintainer runs `npm stage publish` to create a staged release that must be explicitly promoted under 2FA before it becomes installable, alongside new install-time controls. This is the registry-level governance answer to the Shai-Hulud/Megalodon waves (§ 2) — the OIDC-token-reuse propagation primitive that made those worms self-spreading is blunted when an automated `npm publish` cannot reach end users without an interactive 2FA promotion step. Defender takeaway: where you operate internal npm publishing pipelines, adopt staged publishing and require the 2FA promotion gate; it does not retroactively clean compromised packages but it raises the cost of the next worm's propagation step.
