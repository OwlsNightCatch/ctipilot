---
schema: 1
kind: research
horizon: operational
title: "Sekoia consolidates Gamaredon tooling under GammaPhish / GammaWorm, details an NTFS-ADS USB+network worm"
headline: "Sekoia consolidates Gamaredon tooling under GammaPhish / GammaWorm, details an NTFS-ADS USB+network worm"
summary: "Sekoia's Threat Detection & Research team published part one of a Gamaredon (UAC-0010 / ACTINIUM, attributed to Russia's FSB) series describing a January 2026 campaign against Ukrainian government and military targets, introducing unified naming for two capability clusters: GammaPhish (the funnel from …"
discovered_at: "2026-06-02T05:00:07Z"
event_date: 2026-06-01
run_id: 2026-06-02-8af85d01
priority: notable
immediate_action: null
tags:
  - nation-state
  - espionage
  - russia-nexus
  - botnet
regions:
  - europe
sectors:
  - public-sector
  - defense
entities:
  - "actor:gamaredon"
cves: []
sources:
  - url: "https://blog.sekoia.io/fsbs-matryoshka-1-3-gamaredons-gifts-that-keeps-unpacking-gammaphish-and-gammaworm/"
    publisher: Sekoia TDR
    role: primary
  - url: "https://www.infosecurity-magazine.com/news/gamaredon-worm-ntfs-data-streams/"
    publisher: Infosecurity Magazine
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
migrated_from: briefs/2026-06-02.md
---

Sekoia's Threat Detection & Research team published part one of a Gamaredon (UAC-0010 / ACTINIUM, attributed to Russia's FSB) series describing a January 2026 campaign against Ukrainian government and military targets, introducing unified naming for two capability clusters: **GammaPhish** (the funnel from spearphishing through GammaLoad deployment) and **GammaWorm** (the propagation layer, subsuming the tooling previously tracked as LitterDrifter / PteroLNK) ([Sekoia TDR, 2026-06-01](https://blog.sekoia.io/fsbs-matryoshka-1-3-gamaredons-gifts-that-keeps-unpacking-gammaphish-and-gammaworm/) · [Infosecurity Magazine, 2026-06-01](https://www.infosecurity-magazine.com/news/gamaredon-worm-ntfs-data-streams/)). The chain begins with weaponised xHTML files exploiting CVE-2025-8088 (the WinRAR path-traversal flaw) to drop HTA payloads into Windows Startup directories via `mshta.exe`. GammaWorm itself is a 20,000+-line obfuscated VBScript worm that persists via scheduled tasks and `RunOnce`/`Run` registry keys, hides components in NTFS Alternate Data Streams, propagates across USB and mapped network drives using Ukrainian-language lures, and resolves C2 through dead-drop resolvers on Telegram, Telegra.ph, Teletype.in, Supabase and Cloudflare Workers.

**Why it matters to us:** The ADS-hiding + removable-media propagation + legitimate-service dead-drop pattern is highly transferable to any EU public-sector estate. Hunt for `mshta.exe` spawning `wscript.exe`, large obfuscated VBScripts executing from `%APPDATA%`, scheduled tasks with randomised GUID names pointing into user-profile paths, ADS on `%TEMP%`/`%APPDATA%` files, and outbound HTTPS to Telegra.ph / Supabase / Workers endpoints from non-developer hosts.
