---
schema: 1
kind: research
title: "SANS ISC: WeTransfer-delivered JavaScript stages a steganographic image loader (\"Evil MSI background\") on Cloudflare Workers and R2"
headline: "SANS ISC: WeTransfer-delivered JavaScript stages a steganographic image loader (\"Evil MSI background\") on Cloudflare Workers and R2"
summary: "SANS ISC handler Xavier Mertens documented a resurgence of an image-steganography delivery chain (SANS ISC, 2026-06-05)."
discovered_at: "2026-06-07T05:00:04Z"
event_date: 2026-06-05
run_id: 2026-06-07-0885f123
priority: notable
immediate_action: null
tags:
  - phishing
  - infostealer
regions:
  - global
sectors:
  - public-sector
  - technology
entities: []
cves: []
sources:
  - url: "https://isc.sans.edu/diary/rss/33054"
    publisher: SANS Internet Storm Center (Xavier Mertens)
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
migrated_from: briefs/2026-06-07.md
---

SANS ISC handler Xavier Mertens documented a resurgence of an image-steganography delivery chain ([SANS ISC, 2026-06-05](https://isc.sans.edu/diary/rss/33054)). A >2 MB JavaScript file ("Remittance Advice.js"), distributed via a legitimate WeTransfer link and padded with do-nothing junk loops, hides functional code that: decodes a ROT13-obfuscated payload into an environment variable; fetches an MSI-installer background image (a JPEG) from a Cloudflare Workers (`*.workers.dev`) subdomain that carries the next stage via steganography (Base64 with `A`→`#` substitution to evade naive scanners, delimited by `IN-`/`-in1`); loads a decoded .NET DLL that is a trojanised fork of the open-source `Microsoft.Win32.TaskScheduler` library to establish Scheduled Task persistence at logon; then pulls a further payload from a Cloudflare R2 (`*.r2.dev`) bucket. The final payload was still under analysis at publication. The infrastructure choice — Cloudflare Workers + R2 — leans on Cloudflare's reputation to bypass category-based web filtering. This is a single-source SANS ISC diary `[SINGLE-SOURCE]`; the chain (not a specific actor) is the takeaway. Maps to `T1027.003` (Steganography), `T1059.007` (JavaScript), `T1059.001` (PowerShell) and `T1053.005` (Scheduled Task).
**Why it matters to us:** Detection concepts: alert on `wscript.exe`/`cscript.exe` spawning PowerShell with environment-variable-expanded or Base64 payloads (Sysmon EID 1); flag first-seen `*.workers.dev` and `*.r2.dev` connections immediately following a WeTransfer download in proxy logs; hunt for scheduled tasks created by `wscript`/`mshta` parents; and EDR-rule on `.NET` assembly loads from a TaskScheduler-derived DLL outside the genuine Windows Task Scheduler path.
