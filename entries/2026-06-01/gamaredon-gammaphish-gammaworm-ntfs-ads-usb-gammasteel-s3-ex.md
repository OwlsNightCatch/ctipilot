---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-multi-day
title: "Gamaredon: GammaPhish → GammaWorm (NTFS ADS + USB) → GammaSteel (S3 exfil) — the week's most complete intrusion kill-chain disclosure"
headline: "Gamaredon: GammaPhish → GammaWorm (NTFS ADS + USB) → GammaSteel (S3 exfil) — the week's most complete intrusion kill-chain disclosure"
summary: "Monday 2 June brought Sekoia's part-one Gamaredon series (Sekoia TDR, 2026-06-01), consolidating three capability clusters under unified naming: GammaPhish (the spearphishing-through-GammaLoad funnel), GammaWorm (the USB-and-network-propagation layer), and GammaSteel (the S3-exfiltration stealer confirmed …"
discovered_at: "2026-06-01T05:00:04Z"
event_date: 2026-06-03
run_id: 2026-W23-9118e7bd
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
entities: []
cves: []
sources:
  - url: "https://blog.sekoia.io/fsbs-matryoshka-1-3-gamaredons-gifts-that-keeps-unpacking-gammaphish-and-gammaworm/"
    publisher: Sekoia TDR — GammaPhish and GammaWorm
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
migrated_from: briefs/weekly/2026-W23.md
---

Monday 2 June brought Sekoia's part-one Gamaredon series ([Sekoia TDR, 2026-06-01](https://blog.sekoia.io/fsbs-matryoshka-1-3-gamaredons-gifts-that-keeps-unpacking-gammaphish-and-gammaworm/)), consolidating three capability clusters under unified naming: **GammaPhish** (the spearphishing-through-GammaLoad funnel), **GammaWorm** (the USB-and-network-propagation layer), and **GammaSteel** (the S3-exfiltration stealer confirmed in the same campaign arc via Sekoia TDR follow-up, [daily 2026-06-03](/briefs/2026-06-03/)).

**Initial access (GammaPhish):** weaponised xHTML files exploiting CVE-2025-8088 (the WinRAR path-traversal flaw, patched but widely unpatched) drop HTA payloads into Windows Startup directories via `mshta.exe`. **Propagation (GammaWorm):** a 20,000+-line obfuscated VBScript worm persists via scheduled tasks and `Run`/`RunOnce` registry keys, hides components in **NTFS Alternate Data Streams**, and spreads across USB drives and mapped network shares using Ukrainian-language lures (`T1025`, `T1091`). C2 resolves through dead-drop pages on Telegram, Telegra.ph, Teletype.in, Supabase and Cloudflare Workers — all platforms with high allow-list rates at enterprise egress proxies. **Exfiltration (GammaSteel):** the S3-exfiltration stealer stages and uploads collected data directly to attacker-controlled AWS S3 buckets.

The detection pattern across all three stages is highly transferable to non-Ukraine targets. Hunt for: `mshta.exe` spawning `wscript.exe`; large obfuscated VBScripts executing from `%APPDATA%`; scheduled tasks with randomised GUID names pointing into user-profile paths; NTFS ADS on `%TEMP%`/`%APPDATA%` files (`dir /r` or Sysmon EID 11 for streams); outbound HTTPS to Telegra.ph / Supabase / Workers from non-developer hosts; and anomalous S3-API calls from user endpoints.
