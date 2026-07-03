---
schema: 1
kind: research
horizon: operational
title: "TrickMo \"TrickMo C\" — Android banking trojan migrates C2 to The Open Network blockchain, adds SOCKS5 / SSH device-as-pivot"
headline: "TrickMo \"TrickMo C\" — Android banking trojan migrates C2 to The Open Network blockchain, adds SOCKS5 / SSH device-as-pivot"
summary: "ThreatFabric's 2026-05-11 research identifies a substantially redesigned TrickMo variant active across January–February 2026 in campaigns against banking and fintech users in France, Italy and Austria (ThreatFabric, 2026-05-11; The Hacker News, 2026-05-12; Security Affairs, 2026-05-12)."
discovered_at: "2026-05-13T05:00:09Z"
event_date: 2026-05-12
run_id: 2026-05-13-c148b9a5
priority: notable
immediate_action: null
tags:
  - phishing
  - mobile
  - organized-crime
regions:
  - europe
sectors:
  - finance
entities:
  - "tool:trickmo-c-2026"
cves: []
sources:
  - url: "https://www.threatfabric.com/blogs/new-trickmo-variant-device-take-over-malware-targeting-banking-fintech-wallet-auth-app"
    publisher: "ThreatFabric, 2026-05-11"
    role: primary
  - url: "https://thehackernews.com/2026/05/new-trickmo-variant-uses-ton-c2-and.html"
    publisher: "The Hacker News, 2026-05-12"
    role: corroborating
  - url: "https://securityaffairs.com/192003/malware/android-banking-trojan-trickmo-evolves-using-ton-network-for-c2.html"
    publisher: "Security Affairs, 2026-05-12"
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
migrated_from: briefs/2026-05-13.md
---

ThreatFabric's 2026-05-11 research identifies a substantially redesigned TrickMo variant active across January–February 2026 in campaigns against banking and fintech users in France, Italy and Austria ([ThreatFabric, 2026-05-11](https://www.threatfabric.com/blogs/new-trickmo-variant-device-take-over-malware-targeting-banking-fintech-wallet-auth-app); [The Hacker News, 2026-05-12](https://thehackernews.com/2026/05/new-trickmo-variant-uses-ton-c2-and.html); [Security Affairs, 2026-05-12](https://securityaffairs.com/192003/malware/android-banking-trojan-trickmo-evolves-using-ton-network-for-c2.html)). The C2 architecture has migrated off conventional DNS / IP infrastructure: the host APK embeds a native TON (The Open Network) proxy that starts on a loopback port at process launch, and all C2 HTTP requests address `.adnl` hostnames resolved inside the TON decentralised overlay. That design defeats traditional domain-takedown and DNS-based blocklisting — operator endpoints exist as TON identities inside a permissionless overlay rather than at a controllable DNS or IP. Beyond the banking-trojan core (accessibility-service device takeover, fake overlay login pages, SMS / OTP interception, mapped to `T1517 Access Notifications`), TrickMo C adds a network-reconnaissance subsystem via five operator commands (`curl`, `dnslookup`, `ping`, `telnet`, `traceroute`) and an SSH tunnel + authenticated SOCKS5 proxy — turning infected Android devices into programmable network pivots so operators can route abuse traffic from the victim's IP space and defeat IP-reputation fraud detection on banking and crypto-exchange platforms. Mapped to `T1090.001 Proxy: Internal Proxy` for the SOCKS5 mode. Droppers masquerade as TikTok variants distributed via Facebook ads; the final payload impersonates Google Play Services. Dormant code includes the Pine hooking framework and NFC permissions, suggesting contactless-payment interception is in development.

**Defender takeaway:** The relevant change for an EU defender is the C2 transport: blocking TON traffic at the corporate gateway is non-trivial because TON shares the standard internet routes; behaviour-side, detect Android devices that initiate the TON loopback proxy and that issue outbound to non-corporate SOCKS5 / SSH ports under unusual entitlements. Public-sector implication: government-issued Android or BYOD devices that access banking, tax, or e-government services should be scoped under MDM policies that block sideloaded APKs from social-media link-outs and forbid sideloaded TikTok-look-alikes. Mapped to `T1422 System Network Configuration Discovery` and `T1437.001 Application Layer Protocol: Web Protocols`.
