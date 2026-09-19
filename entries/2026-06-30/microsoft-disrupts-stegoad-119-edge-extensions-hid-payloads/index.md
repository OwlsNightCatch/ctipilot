---
schema: 1
kind: research
title: Microsoft disrupts StegoAd — 119 Edge extensions hid payloads in image and font files via steganography
headline: Microsoft disrupts StegoAd — 119 Edge extensions hid payloads in image and font files via steganography
summary: "Microsoft's Edge security team detailed and disrupted StegoAd, 119 malicious extensions across 90+ developer accounts with a combined ~2.6M installs, masquerading as ad blockers, VPNs, translators, and downloaders (Microsoft Edge Security, 2026-06-16 · Risky Biz News, 2026-06-29)."
discovered_at: "2026-06-30T05:10:39Z"
event_date: 2026-06-29
run_id: 2026-06-30-9aaa1114
priority: notable
immediate_action: null
tags:
  - china-nexus
  - infostealer
  - supply-chain
regions:
  - global
sectors:
  - technology
entities:
  - "campaign:stegoad-darkspectre-119-edge-extensions-steganography"
cves: []
sources:
  - url: "https://microsoftedge.github.io/edgevr/posts/Inside-StegoAd-How-We-Disrupted-a-Massive-Malicious-Extension-Campaign/"
    publisher: Microsoft Edge Security
    role: primary
  - url: "https://thehackernews.com/2026/06/microsoft-removes-119-edge-extensions.html"
    publisher: The Hacker News
    role: corroborating
  - url: "https://news.risky.biz/risky-bulletin-microsoft-disrupts-stegoad-operation/"
    publisher: Risky Biz News
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
migrated_from: briefs/2026-06-30.md
---

Microsoft's Edge security team detailed and disrupted StegoAd, 119 malicious extensions across 90+ developer accounts with a combined ~2.6M installs, masquerading as ad blockers, VPNs, translators, and downloaders ([Microsoft Edge Security, 2026-06-16](https://microsoftedge.github.io/edgevr/posts/Inside-StegoAd-How-We-Disrupted-a-Massive-Malicious-Extension-Campaign/) · [Risky Biz News, 2026-06-29](https://news.risky.biz/risky-bulletin-microsoft-disrupts-stegoad-operation/)). The core trick hides executable payloads after the IEND marker of PNG icon files (later WebP images and WOFF2 fonts), passing standard scanner analysis; extensions stay dormant 3–5 days, detect DevTools, and validate requests server-side to dodge sandboxes. Payloads ranged from Google/WordPress credential theft and cookie collection to affiliate-commission hijack, ad fraud, and an RCE backdoor, with failover C2 across 10+ domains fronted by Cloudflare Workers and Google Analytics properties used as a covert channel. The Hacker News reports overlap with the China-linked DarkSpectre operation (prior ShadyPanda / GhostPoster extension campaigns) ([The Hacker News, 2026-06-29](https://thehackernews.com/2026/06/microsoft-removes-119-edge-extensions.html)); the Microsoft Edge write-up itself does not name DarkSpectre. Hunt: extensions with multi-day activation delays; data after IEND in PNGs or at unusual WOFF2 offsets; browser-process requests to Cloudflare Workers domains not matching the installed manifest origin.
