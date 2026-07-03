---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-multi-day
title: npm supply-chain worms — a sustained wave across the week
headline: npm supply-chain worms — a sustained wave across the week
summary: "Three separate npm-ecosystem supply-chain events were in play across the window, and the pattern is the story. Microsoft attributed the Mastra scope compromise (140+ @mastra packages, postinstall dropper) to North Korea's Sapphire Sleet (covered in the daily on 06-21)."
discovered_at: "2026-06-29T00:20:57Z"
event_date: null
run_id: 2026-W26-b78503e7
priority: notable
immediate_action: null
tags:
  - supply-chain
  - infostealer
  - north-korea-nexus
  - organized-crime
regions:
  - global
sectors:
  - technology
entities:
  - "campaign:mini-shai-hulud"
cves: []
sources:
  - url: "https://socket.dev/blog/miasma-mini-shai-hulud-hits-leoplatform-npm-packages-go-ecosystem"
    publisher: Socket Security — Miasma
    role: primary
  - url: "https://research.jfrog.com/post/from-postcss-typosquat-to-windows-rat/"
    publisher: JFrog — PostCSS RAT
    role: corroborating
  - url: "https://www.microsoft.com/en-us/security/blog/2026/06/17/postinstall-payload-inside-mastra-npm-supply-chain-compromise/"
    publisher: Microsoft — Mastra
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
migrated_from: briefs/weekly/2026-W26.md
---

Three separate npm-ecosystem supply-chain events were in play across the window, and the pattern is the story. Microsoft attributed the [Mastra scope compromise](https://www.bleepingcomputer.com/news/security/microsoft-links-mastra-ai-supply-chain-attack-to-north-korean-hackers/) (140+ `@mastra` packages, `postinstall` dropper) to North Korea's Sapphire Sleet (covered in the daily on 06-21). JFrog documented [PostCSS typosquats](https://research.jfrog.com/post/from-postcss-typosquat-to-windows-rat/) from the `abdrizak` account delivering a Nuitka-compiled Python RAT with Chrome DPAPI credential theft. And on 2026-06-25 Socket reported a [fresh Miasma / "Mini Shai-Hulud" worm wave](https://socket.dev/blog/miasma-mini-shai-hulud-hits-leoplatform-npm-packages-go-ecosystem) across LeoPlatform/RStreams packages (carried in the daily 06-27), the self-propagating supply-chain worm last seen backdooring `@redhat-cloud-services`.

The synthesis: the npm registry is under continuous, parallel pressure from a state actor (DPRK), commodity typosquat crews and a self-replicating worm — three different operators, one ecosystem. The common control is the same one npm v12 is about to enforce by default: disable install scripts (`--ignore-scripts`), pin and review dependencies, and treat CI build-time package resolution as an attack surface. ([daily 06-21](/briefs/2026-06-21/), [daily 06-24](/briefs/2026-06-24/), [daily 06-27](/briefs/2026-06-27/))
