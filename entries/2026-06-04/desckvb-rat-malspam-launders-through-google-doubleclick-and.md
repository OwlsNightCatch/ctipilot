---
schema: 1
kind: threat
horizon: operational
title: "DesckVB RAT malspam launders through Google DoubleClick and blinds AMSI/ETW, with German-language lures aimed at DACH"
headline: "DesckVB RAT malspam launders through Google DoubleClick and blinds AMSI/ETW, with German-language lures aimed at DACH"
summary: "Huntress documented a DesckVB RAT chain from a May 2026 IR engagement that abuses Google DoubleClick Campaign Manager click-tracking for reputation laundering: a German-named HTML attachment (Bestellung_2026.html — \"order\") does a zero-second meta-refresh to a high-reputation ad.doubleclick.net URL that …"
discovered_at: "2026-06-04T05:00:04Z"
event_date: 2026-06-03
run_id: 2026-06-04-51b23ffa
priority: notable
immediate_action: null
tags:
  - phishing
  - infostealer
regions:
  - dach
sectors:
  - manufacturing
  - finance
entities: []
cves: []
sources:
  - url: "https://www.huntress.com/blog/malspam-to-deskcvb-rat-delivery-chain-analysis"
    publisher: Huntress Labs
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
migrated_from: briefs/2026-06-04.md
---

Huntress documented a DesckVB RAT chain from a May 2026 IR engagement that abuses Google DoubleClick Campaign Manager click-tracking for reputation laundering: a German-named HTML attachment (`Bestellung_2026.html` — "order") does a zero-second meta-refresh to a high-reputation `ad.doubleclick.net` URL that allowlist-based mail/web filters pass transparently, then steers to a "Download PDF" landing page delivering a JavaScript loader ([Huntress, 2026-06-03](https://www.huntress.com/blog/malspam-to-deskcvb-rat-delivery-chain-analysis)). The loader runs a .NET assembly via process hollowing (`T1055.012`) after patching AMSI and ETW at the native-API level (`T1562.001`) to blind Windows telemetry; persistence is set before C2 over raw TCP. German-language purchase-order lures point at DACH enterprises.
**Why it matters to us:** the DoubleClick hop defeats domain-reputation allowlisting at the gateway — flag HTML email attachments containing meta-refresh to ad-network domains, and watch for runtime patching of `AmsiScanBuffer` / ETW from `node`/script-spawned process trees rather than relying on the redirect domain.
