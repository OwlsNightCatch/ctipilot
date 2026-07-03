---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-long-running
title: "Mini Shai-Hulud / TeamPCP — @antv npm wave and confirmed Maven Central poisoning; Cargo still un-hit"
headline: "Mini Shai-Hulud / TeamPCP — @antv npm wave and confirmed Maven Central poisoning; Cargo still un-hit"
summary: "Beyond the in-window TrapDoor and framework-open-sourcing covered in § 2, horizon research surfaced a development the dailies missed."
discovered_at: "2026-05-25T05:00:21Z"
event_date: null
run_id: 2026-W22-da77963d
priority: notable
immediate_action: null
tags:
  - supply-chain
  - infostealer
  - identity
  - cloud
regions:
  - global
  - europe
sectors:
  - technology
  - public-sector
entities:
  - "campaign:mini-shai-hulud"
  - "actor:teampcp"
cves: []
sources:
  - url: "https://www.wiz.io/blog/mini-shai-hulud-teampcp-hits-antv-supply-chain"
    publisher: "Wiz Research — Mini Shai-Hulud hits @antv"
    role: primary
  - url: "https://www.ox.security/blog/new-actors-deploy-shai-hulud-clones-teampcp-copycats-are-here/"
    publisher: OX Security — TeamPCP copycats
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
migrated_from: briefs/weekly/2026-W22.md
---

Beyond the in-window TrapDoor and framework-open-sourcing covered in § 2, horizon research surfaced a development the dailies missed. Wiz documented a fresh wave (2026-05-19) in which TeamPCP hijacked a legitimate maintainer account to poison the **@antv** data-visualisation ecosystem on npm (@antv/g2, g6, x6, l7 and others, collectively millions of weekly downloads), running the standard Mini Shai-Hulud credential-harvest against GitHub/npm tokens and cloud keys across 80+ file paths. OX Security and Security Affairs documented copycat clones spreading after the source-code leak. On the W21 watch list of un-hit registries: npm remains the only ecosystem with a primary-confirmed poisoning this wave — horizon research flagged unverified secondary reporting of Maven Central exposure via the `mvnpm` npm-to-Maven bridge, but this run could not corroborate it against a primary source, so it is **not asserted** here, and Cargo / crates.io status is likewise unverified. No GovCERT.ch / NCSC.ch developer advisory was found. Keep the provenance-anomaly hunt centred on npm and treat the `mvnpm` bridge as a plausible next vector to watch.
