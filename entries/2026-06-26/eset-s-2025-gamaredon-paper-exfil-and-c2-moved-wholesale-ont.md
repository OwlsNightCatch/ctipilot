---
schema: 1
kind: annual-report
horizon: operational
title: "ESET's 2025 Gamaredon paper: exfil and C2 moved wholesale onto trusted cloud services (ANNUAL REPORT)"
headline: "ESET's 2025 Gamaredon paper: exfil and C2 moved wholesale onto trusted cloud services (ANNUAL REPORT)"
summary: "ESET's 2025 Gamaredon paper shows the FSB group's exfil and C2 moving entirely onto trusted cloud services — S3-compatible object storage (Wasabi/Tebi/Intercolo) via rclone and Cloudflare-tunnel/Workers/DevTunnel C2 that blends with legitimate egress; targeting stayed exclusively Ukrainian, but the tradecraft is the transferable part (ESET, 2026-06-25)."
discovered_at: "2026-06-26T04:54:41Z"
event_date: 2026-06-25
run_id: 2026-06-26-6bbe4619
priority: high
immediate_action: null
tags:
  - nation-state
  - espionage
  - russia-nexus
regions:
  - europe
sectors:
  - public-sector
  - defense
entities:
  - "actor:gamaredon"
cves: []
sources:
  - url: "https://www.welivesecurity.com/en/eset-research/gamaredon-2025-leveraging-tunnels-workers-dead-drops-new-alliances/"
    publisher: ESET WeLiveSecurity
    role: primary
  - url: "https://www.sekoia.com/blog/fsbs-matryoshka-3-3-gamaredons-gifts-that-keeps-unpacking-gammasteel"
    publisher: Sekoia
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
migrated_from: briefs/2026-06-26.md
---

ESET's annual Gamaredon paper documents the FSB-linked group's 2025 toolset — six new PowerShell tools (PteroDee, PteroCache, PteroDum, PteroOdd, PteroEffigy, PteroPaste) plus a resurrected PteroSetup VBScript weaponizer — and, more usefully for defenders elsewhere, a wholesale shift of infrastructure onto trusted services ([ESET, 2026-06-25](https://www.welivesecurity.com/en/eset-research/gamaredon-2025-leveraging-tunnels-workers-dead-drops-new-alliances/)). C2 now rides Cloudflare tunnels (`trycloudflare.com`), Cloudflare Workers (`workers.dev`), Microsoft DevTunnels (`devtunnels.ms`), Loophole, No-IP DDNS, Clever Cloud and Supabase; data is exfiltrated via `rclone` to S3-compatible object storage (Wasabi, Tebi, and Intercolo — which became the primary destination by December), and hostnames are brokered through dead-drop resolvers spread across Telegram, Telegra.ph, Dropbox, GoFile, Mastodon and a dozen paste services so no fixed IP or domain appears in the implant. ESET also confirms an early-2025 collaboration with Turla. Sekoia independently documented the same 2025 shift toward tunnel-service C2 and S3-compatible cloud-storage exfiltration in its parallel "FSB's Matryoshka" Gamaredon series ([Sekoia, 2026-06-04](https://www.sekoia.com/blog/fsbs-matryoshka-3-3-gamaredons-gifts-that-keeps-unpacking-gammasteel)). Targeting stayed **exclusively** Ukrainian government and military — the report names no EU targets — so the relevance here is the tradecraft, not the victimology.

**Why it matters to us:** the tunnel-and-cloud-storage model defeats domain/IP blocklists and blends with legitimate egress, and it is exactly the pattern any espionage operator can adopt. Detection concepts: alert on tunnel-service egress (`trycloudflare.com` / `workers.dev` / `devtunnels.ms`) initiated by Office or scripting processes; flag `rclone` or S3-API `PUT`/`POST` from hosts with no backup role; hunt PowerShell that reads paste-site domains and decodes base64 blobs.
