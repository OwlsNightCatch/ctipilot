---
schema: 1
kind: research
title: "Netcraft: Bluekit PhaaS uses Browser-in-the-Middle to defeat FIDO2 and Device Bound Session Credentials"
headline: "Netcraft: Bluekit PhaaS uses Browser-in-the-Middle to defeat FIDO2 and Device Bound Session Credentials"
summary: "Netcraft published a technical breakdown (2026-06-25) of Bluekit, a phishing-as-a-service platform first documented by Varonis Threat Labs (2026-04-29) and now seen by Netcraft at scale (~70 active hostnames in a single week) (Netcraft, 2026-06-25; Varonis, 2026-04-29)."
discovered_at: "2026-06-28T05:05:40Z"
event_date: 2026-06-25
run_id: 2026-06-28-1b30612a
priority: notable
immediate_action: null
tags:
  - phishing
  - identity
  - cloud
  - ai-abuse
regions:
  - global
  - europe
sectors:
  - public-sector
  - finance
entities:
  - "campaign:bluekit-phaas-browser-in-the-middle"
cves: []
sources:
  - url: "https://www.netcraft.com/blog/bluekit-phishing-as-a-service-threat"
    publisher: Netcraft
    role: primary
  - url: "https://www.varonis.com/blog/bluekit"
    publisher: Varonis Threat Labs
    role: corroborating
closed_sources: []
evidence:
  - quote: "The victim completes what appears to be a normal login flow but in reality, they have authenticated into the attacker's browser session on the attacker's browser."
    publisher: Netcraft
  - quote: Device Bound Session Credentials (DBSC) cannot protect against BitM attacks
    publisher: Netcraft
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
migrated_from: briefs/2026-06-28.md
---

Netcraft published a technical breakdown (2026-06-25) of **Bluekit**, a phishing-as-a-service platform first documented by Varonis Threat Labs (2026-04-29) and now seen by Netcraft at scale (~70 active hostnames in a single week) ([Netcraft, 2026-06-25](https://www.netcraft.com/blog/bluekit-phishing-as-a-service-threat); [Varonis, 2026-04-29](https://www.varonis.com/blog/bluekit)). Bluekit's distinguishing technique is Browser-in-the-Middle (BitM): instead of proxying the victim's HTTP traffic the way Evilginx/AiTM kits do (which leaves session-fingerprint mismatches), it runs a real automated browser on attacker infrastructure and streams its live DOM to the victim over WebSocket using the open-source `rrweb` DOM-serialisation library. The victim's keystrokes and clicks are relayed into the attacker's browser and executed against the genuine site, so the session is created in and owned by the attacker from the start — which is why Device Bound Session Credentials (DBSC, which bind tokens to the legitimate device's keys) provide no protection, and why FIDO2/WebAuthn is bypassed (the attacker's browser completes the relying-party challenge on the victim's behalf). Anti-analysis: per-load randomised CSS filter values to defeat screenshot pixel-hashing, >1 MB rotating obfuscated JS bundles, brand-impersonating CAPTCHA, and WebRTC IP-mismatch checks to spot analyst proxies. Detection concepts: `rrweb` presence outside legitimate analytics; WebSocket streams of binary/encrypted DOM diffs to unexpected origins; sub-second form-submission round-trip latency characteristic of BitM relay; randomised CSS filter rules on top-level HTML. Relevant because Microsoft 365 / Entra ID tenants — including Swiss and EU public-sector ones — are named targets, and BitM degrades the "phishing-resistant MFA solves this" assumption.
