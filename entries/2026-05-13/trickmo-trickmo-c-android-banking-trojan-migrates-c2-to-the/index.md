---
schema: 1
kind: research
title: "TrickMo C: Android banking trojan moves its C2 onto The Open Network and turns infected phones into SOCKS5 and SSH network pivots"
headline: "New TrickMo variant hides its C2 in The Open Network and turns infected phones into network pivots"
summary: "ThreatFabric reported on 2026-05-11 a redesigned TrickMo Android banking trojan, tracked since January to February 2026 in campaigns against banking and wallet users in France, Italy and Austria, that routes its command-and-control traffic through an embedded TON proxy to .adnl endpoints, which blunts domain takedowns and network blocking. New operator commands run network reconnaissance from the phone and open SSH tunnels and an authenticated SOCKS5 proxy, giving attackers reach into the network the device is on and an exit node on the victim's IP."
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
techniques: [T1036.005, T1105, T1056.001, T1056.002, T1113, T1111, T1071.001, T1090, T1572, T1016, T1046]
affected_products: []
cves: []
sources:
  - url: "https://www.threatfabric.com/blogs/new-trickmo-variant-device-take-over-malware-targeting-banking-fintech-wallet-auth-app"
    publisher: "ThreatFabric"
    date: "2026-05-11"
    role: primary
  - url: "https://thehackernews.com/2026/05/new-trickmo-variant-uses-ton-c2-and.html"
    publisher: "The Hacker News"
    date: "2026-05-12"
    role: corroborating
  - url: "https://securityaffairs.com/192003/malware/android-banking-trojan-trickmo-evolves-using-ton-network-for-c2.html"
    publisher: "Security Affairs"
    date: "2026-05-12"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Traffic-pattern detection at the network edge sees only TON traffic, which is encrypted and indistinguishable from any other TON-enabled application's outbound flow."
    publisher: ThreatFabric
    source_url: "https://www.threatfabric.com/blogs/new-trickmo-variant-device-take-over-malware-targeting-banking-fintech-wallet-auth-app"
  - quote: "these dormant components suggest the operators are preparing the platform for future runtime-delivered features"
    publisher: ThreatFabric
    source_url: "https://www.threatfabric.com/blogs/new-trickmo-variant-device-take-over-malware-targeting-banking-fintech-wallet-auth-app"
  - quote: "Dropper apps containing the malware masquerade as adult-friendly versions of TikTok through Facebook"
    publisher: The Hacker News
    source_url: "https://thehackernews.com/2026/05/new-trickmo-variant-uses-ton-c2-and.html"
verification: multi-source
sourcing_note: "ThreatFabric is the only party that analysed the samples; The Hacker News and Security Affairs report its findings."
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-13.md
updated_at: null
updates:
  - at: "2026-10-21T20:19:00Z"
    run_id: 2026-10-21T1148Z-audit
    type: improvement
    summary: >
      ThreatFabric's point about TrickMo's TON transport is that edge traffic analysis cannot tell its
      encrypted C2 from other TON applications and that domain takedowns lose effect, not that TON shares
      standard internet routes. The bundled Pine framework and NFC permissions are unused and read as
      reserved for future runtime-delivered features rather than as contactless-payment interception in
      development, and the droppers are TikTok look-alikes delivered through Facebook campaigns, not ads.
    fields: [affected_products, body, classification, evidence, headline, sources, sourcing_note, summary, techniques, title]
---

ThreatFabric identified a new TrickMo variant between January and February 2026 that is progressively replacing its predecessor in campaigns against banking and wallet customers in France, Italy and Austria ([ThreatFabric, 2026-05-11](https://www.threatfabric.com/blogs/new-trickmo-variant-device-take-over-malware-targeting-banking-fintech-wallet-auth-app)). The on-device feature set is largely unchanged: once the user grants the accessibility-service permission the bot coerces, the operator gets overlay credential phishing, keylogging, screen recording and streaming, remote control, and SMS and notification interception that silently suppresses one-time-password messages, while the offensive code arrives as a module fetched from operator infrastructure at runtime ([ThreatFabric, 2026-05-11](https://www.threatfabric.com/blogs/new-trickmo-variant-device-take-over-malware-targeting-banking-fintech-wallet-auth-app)). Campaign tags point to TikTok-themed apps delivered over Facebook ([ThreatFabric, 2026-05-11](https://www.threatfabric.com/blogs/new-trickmo-variant-device-take-over-malware-targeting-banking-fintech-wallet-auth-app)); the droppers pose as adult-friendly versions of TikTok and the malware as Google Play Services ([The Hacker News, 2026-05-12](https://thehackernews.com/2026/05/new-trickmo-variant-uses-ton-c2-and.html)).

Command and control now runs over The Open Network: an embedded native TON proxy starts on a loopback port, the bot's HTTP client sends every request through it to `.adnl` hostnames resolved inside the TON overlay, and the few clearnet names it still needs are resolved over public DNS-over-HTTPS ([ThreatFabric, 2026-05-11](https://www.threatfabric.com/blogs/new-trickmo-variant-device-take-over-malware-targeting-banking-fintech-wallet-auth-app)). New operator commands run curl, DNS lookups, ping, multi-port TCP-connect probes and traceroute from the device's network position, open SSH local-forward and remote-forward tunnels, the latter reaching into the corporate or home LAN the phone is on, and start an authenticated SOCKS5 proxy whose traffic appears to come from the victim's IP and so defeats IP-based fraud checks ([ThreatFabric, 2026-05-11](https://www.threatfabric.com/blogs/new-trickmo-variant-device-take-over-malware-targeting-banking-fintech-wallet-auth-app)). The Pine hooking framework and a full set of NFC permissions are bundled but unused, which ThreatFabric reads as preparation for features delivered at runtime later ([ThreatFabric, 2026-05-11](https://www.threatfabric.com/blogs/new-trickmo-variant-device-take-over-malware-targeting-banking-fintech-wallet-auth-app)).

**Exposure:** Android users of banking, fintech, wallet and authenticator apps in France, Italy and Austria, by the campaign tags; any corporate or home network an infected phone joins is reachable to the operator through the remote-forward tunnel ([ThreatFabric, 2026-05-11](https://www.threatfabric.com/blogs/new-trickmo-variant-device-take-over-malware-targeting-banking-fintech-wallet-auth-app)).

**Detection:** network-edge traffic analysis sees only encrypted TON traffic that cannot be told apart from other TON applications, and takedowns of the C2 lose effect ([ThreatFabric, 2026-05-11](https://www.threatfabric.com/blogs/new-trickmo-variant-device-take-over-malware-targeting-banking-fintech-wallet-auth-app)), so the signals sit on the device and around it: in mobile-device inventories, an app presenting itself as Google Play Services that holds the accessibility-service permission ([The Hacker News, 2026-05-12](https://thehackernews.com/2026/05/new-trickmo-variant-uses-ton-c2-and.html)), and in internal network telemetry, TCP-connect sweeps, DNS lookups and traceroutes originating from a phone's address ([ThreatFabric, 2026-05-11](https://www.threatfabric.com/blogs/new-trickmo-variant-device-take-over-malware-targeting-banking-fintech-wallet-auth-app)).

**Defender takeaway:** ThreatFabric judges domain takedowns largely ineffective against this variant and network blocking less effective ([ThreatFabric, 2026-05-11](https://www.threatfabric.com/blogs/new-trickmo-variant-device-take-over-malware-targeting-banking-fintech-wallet-auth-app)), so the control point is the device: on managed Android devices, restrict app installs from outside the official store and accessibility-service grants, and handle an infected phone that has joined a corporate network as a foothold in that network as well as a fraud case. Security Affairs reports the same findings ([Security Affairs, 2026-05-12](https://securityaffairs.com/192003/malware/android-banking-trojan-trickmo-evolves-using-ton-network-for-c2.html)).

## Improvement — 2026-10-21T20:19:00Z

ThreatFabric's point about the TON transport is that traffic analysis at the network edge sees only encrypted TON traffic, indistinguishable from any other TON application's, and that domain takedowns lose effect because the endpoints live inside the overlay ([ThreatFabric, 2026-05-11](https://www.threatfabric.com/blogs/new-trickmo-variant-device-take-over-malware-targeting-banking-fintech-wallet-auth-app)); it does not say TON shares standard internet routes, and no source describes "unusual entitlements" as a signal. The Pine hooking framework and the NFC permissions are bundled but not exercised, which ThreatFabric reads as capability reserved for features delivered at runtime later, possibly NFC-targeted, not as contactless-payment interception in development ([ThreatFabric, 2026-05-11](https://www.threatfabric.com/blogs/new-trickmo-variant-device-take-over-malware-targeting-banking-fintech-wallet-auth-app)). The droppers are TikTok look-alikes delivered through Facebook campaigns ([ThreatFabric, 2026-05-11](https://www.threatfabric.com/blogs/new-trickmo-variant-device-take-over-malware-targeting-banking-fintech-wallet-auth-app); [The Hacker News, 2026-05-12](https://thehackernews.com/2026/05/new-trickmo-variant-uses-ton-c2-and.html)); no source says ads. The observable activity is on the device: accessibility-service grants to an app posing as Google Play Services, and network probes originating from a phone inside the LAN ([ThreatFabric, 2026-05-11](https://www.threatfabric.com/blogs/new-trickmo-variant-device-take-over-malware-targeting-banking-fintech-wallet-auth-app)).
