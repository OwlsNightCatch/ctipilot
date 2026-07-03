---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-multi-day
title: "Mini Shai-Hulud / TrapDoor — the supply-chain worm goes cross-ecosystem, open-source and destructive"
headline: "Mini Shai-Hulud / TrapDoor — the supply-chain worm goes cross-ecosystem, open-source and destructive"
summary: "Supply-chain worm widens — Mini Shai-Hulud goes cross-ecosystem, open-source and destructive. TrapDoor spans npm/PyPI/crates, the framework was open-sourced with a wiper stage, and Maven Central poisoning via mvnpm is now confirmed — one of last week's two un-hit registries. (daily, Wiz)"
discovered_at: "2026-05-25T05:00:05Z"
event_date: 2026-05-26
run_id: 2026-W22-da77963d
priority: high
immediate_action: null
tags:
  - supply-chain
  - infostealer
  - wiper
  - ai-abuse
  - cryptocrime
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
  - url: "https://socket.dev/blog/trapdoor-crypto-stealer-npm-pypi-crates"
    publisher: Socket — TrapDoor
    role: primary
  - url: "https://isc.sans.edu/diary/33016"
    publisher: SANS ISC diary 33016 — Mini Shai-Hulud framework / Microsoft SDK
    role: corroborating
  - url: "https://thehackernews.com/2026/05/trapdoor-supply-chain-attack-spreads.html"
    publisher: "The Hacker News, 2026-05-25"
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

The npm-born self-propagating supply-chain worm widened on two axes this week. **TrapDoor** — a cross-ecosystem (npm / PyPI / crates) stealer campaign — was documented validating stolen tokens *before* exfiltration and poisoning AI-assistant configuration files to persist across developer sessions ([2026-05-26](/briefs/2026-05-26/)). In parallel, the **Mini Shai-Hulud / TeamPCP framework was open-sourced**, a trojanised Microsoft PyPI SDK was shipped with a **wiper stage**, and the operators forged Sigstore provenance badges to launder trust ([2026-05-26 update](/briefs/2026-05-26/)).

Read across the days, the trajectory is the story: the propagation primitive (OIDC-token reuse) is now commoditised, the blast radius spans three major registries, and the payload added a destructive option on top of credential theft. This connects directly to the W21 watch item flagging Cargo and Maven as the un-hit wave-6 candidate registries, and to the npm staged-publishing GA (§ 8) that is the first registry-level structural answer. Pre-stage Sigstore / provenance-anomaly hunts in Rust and Java dependency pipelines and gate internal publishing behind interactive promotion.
