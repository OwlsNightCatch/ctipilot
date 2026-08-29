---
schema: 1
kind: research
title: >
  Sekoia consolidates Gamaredon tooling under GammaPhish / GammaWorm, details an NTFS-ADS
  USB+network worm
headline: >
  Sekoia consolidates Gamaredon tooling under GammaPhish / GammaWorm, details an NTFS-ADS
  USB+network worm
summary: >
  Sekoia's Threat Detection & Research team published part one of a Gamaredon (UAC-0010 /
  ACTINIUM, attributed to Russia's FSB) series describing a January 2026 campaign against
  Ukrainian government and military targets, introducing unified naming for two capability
  clusters: GammaPhish (the funnel from …
discovered_at: "2026-06-02T05:00:07Z"
updated_at: "2026-06-03T05:00:08Z"
event_date: 2026-06-01
run_id: 2026-06-02-8af85d01
priority: notable
immediate_action: null
tags:
  - nation-state
  - espionage
  - russia-nexus
  - botnet
  - infostealer
  - vulnerabilities
  - actively-exploited
  - patch-available
regions:
  - europe
  - russia-cis
sectors:
  - public-sector
  - defense
entities:
  - "actor:gamaredon"
techniques: []
affected_products: []
cves:
  - id: CVE-2025-8088
    cvss: n/a
    epss: null
    type: null
    vector: user-interaction
    auth: pre-auth
    status:
      - exploited
      - patch-available
sources:
  - url: "https://blog.sekoia.io/fsbs-matryoshka-1-3-gamaredons-gifts-that-keeps-unpacking-gammaphish-and-gammaworm/"
    publisher: Sekoia TDR
    role: primary
  - url: "https://www.infosecurity-magazine.com/news/gamaredon-worm-ntfs-data-streams/"
    publisher: Infosecurity Magazine
    role: corroborating
  - url: "https://thehackernews.com/2026/06/gamaredon-exploits-winrar-to-deliver.html"
    publisher: The Hacker News
    role: corroborating
closed_sources: []
evidence:
  - quote: "UPDATE (originally covered 2026-06-02): Sekoia TDR's \"FSB's Matryoshka\" series adds material technical detail to the Gamaredon (UAC-0010 / ACTINIUM) tooling consolidation covered yesterday: the group is exploiting the WinRAR path-traversal flaw CVE-2025-8088 as an initial-access vector, using the …"
    publisher: ctipilot v2 brief (migrated)
verification: multi-source
sourcing_note: null
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification: null
watchlist_hit: false
actions:
  - "**Inventory WinRAR to ≥ 7.13 and hunt Startup-folder writes** to close the Gamaredon CVE-2025-8088 entry vector (§ 4); alert on archive utilities writing `.exe`/`.vbs` into `Programs\Startup`."
updates:
  - at: "2026-06-03T05:00:08Z"
    run_id: 2026-06-03-ee0eae61
    type: update
    summary: >
      UPDATE (originally covered 2026-06-02): Sekoia TDR's "FSB's Matryoshka" series adds material
      technical detail to the Gamaredon (UAC-0010 / ACTINIUM) tooling consolidation covered yesterday:
      the group is exploiting the WinRAR path-traversal flaw CVE-2025-8088 as an initial-access
      vector, using the traversal to …
    fields:
      - actions
      - cves
      - evidence
      - regions
      - sources
      - tags
      - body
    merged_from: 2026-06-03/gamaredon-weaponises-winrar-cve-2025-8088-and-adds-the-gamma
migrated_from: briefs/2026-06-02.md
---

Sekoia's Threat Detection & Research team published part one of a Gamaredon (UAC-0010 / ACTINIUM, attributed to Russia's FSB) series describing a January 2026 campaign against Ukrainian government and military targets, introducing unified naming for two capability clusters: **GammaPhish** (the funnel from spearphishing through GammaLoad deployment) and **GammaWorm** (the propagation layer, subsuming the tooling previously tracked as LitterDrifter / PteroLNK) ([Sekoia TDR, 2026-06-01](https://blog.sekoia.io/fsbs-matryoshka-1-3-gamaredons-gifts-that-keeps-unpacking-gammaphish-and-gammaworm/) · [Infosecurity Magazine, 2026-06-01](https://www.infosecurity-magazine.com/news/gamaredon-worm-ntfs-data-streams/)). The chain begins with weaponised xHTML files exploiting CVE-2025-8088 (the WinRAR path-traversal flaw) to drop HTA payloads into Windows Startup directories via `mshta.exe`. GammaWorm itself is a 20,000+-line obfuscated VBScript worm that persists via scheduled tasks and `RunOnce`/`Run` registry keys, hides components in NTFS Alternate Data Streams, propagates across USB and mapped network drives using Ukrainian-language lures, and resolves C2 through dead-drop resolvers on Telegram, Telegra.ph, Teletype.in, Supabase and Cloudflare Workers.

**Why it matters to us:** The ADS-hiding + removable-media propagation + legitimate-service dead-drop pattern is highly transferable to any EU public-sector estate. Hunt for `mshta.exe` spawning `wscript.exe`, large obfuscated VBScripts executing from `%APPDATA%`, scheduled tasks with randomised GUID names pointing into user-profile paths, ADS on `%TEMP%`/`%APPDATA%` files, and outbound HTTPS to Telegra.ph / Supabase / Workers endpoints from non-developer hosts.

## Update — 2026-06-03T05:00:08Z

Sekoia TDR's "FSB's Matryoshka" series adds material technical detail to the Gamaredon (UAC-0010 / ACTINIUM) tooling consolidation covered yesterday: the group is exploiting the WinRAR path-traversal flaw **CVE-2025-8088** as an initial-access vector, using the traversal to write payloads directly into `%APPDATA%\…\Start Menu\Programs\Startup\` for persistence without a Registry or Scheduled-Task artefact ([Sekoia TDR, 2026-06-01](https://blog.sekoia.io/fsbs-matryoshka-1-3-gamaredons-gifts-that-keeps-unpacking-gammaphish-and-gammaworm/)).

The series also names **GammaSteel**, a modular file-stealer (consolidating prior QuietSieve/HarvesterX-class modules) that captures files by extension and — newly — exfiltrates to attacker-controlled S3-compatible cloud storage in addition to Gamaredon's previously documented HTTP/Telegram channels ([The Hacker News, 2026-06-02](https://thehackernews.com/2026/06/gamaredon-exploits-winrar-to-deliver.html)). The full chain runs WinRAR archive → GammaPhish (HTA) → GammaLoad (VBScript downloader) → GammaWorm/GammaSteel.

Delta for defenders: CVE-2025-8088 is fixed in WinRAR 7.13 (August 2025), so the entry vector is closed by patching — inventory WinRAR versions across the estate. Hunt for archive utilities writing executables or `.vbs` into `Programs\Startup` paths (Sysmon EID 11 on target path containing `Programs\Startup`), WinRAR spawning `wscript.exe`/`mshta.exe`, and VBScript processes making outbound requests to S3 endpoints inconsistent with normal business traffic. The targeting is Ukraine-centric, but the WinRAR vector reaches any organisation that opens archive-format lures.
