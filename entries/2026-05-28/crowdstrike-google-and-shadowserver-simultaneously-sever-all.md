---
schema: 1
kind: threat
horizon: operational
title: "CrowdStrike, Google and Shadowserver simultaneously sever all four C2 channels of the GlassWorm developer-targeting botnet (not to be confused with the Nx Console / TanStack GitHub-publish chain in § 5) — Russia-attributed, active since early 2025"
headline: "CrowdStrike, Google and Shadowserver simultaneously sever all four C2 channels of the GlassWorm developer-targeting botnet (not to be confused with the Nx"
summary: "CrowdStrike, Google and Shadowserver simultaneously severed all four C2 channels of the GlassWorm developer-targeting botnet. The campaign — active since early 2025, attributed by CrowdStrike to likely Russia-based operators on the basis of CIS-locale exit checks — used Solana blockchain memo fields, BitTorrent DHT, Google Calendar event titles, and traditional VPS C2 in parallel for resilience; takedown required cutting all four at once. Infections persist on developer endpoints and post-compromise credential rotation is required (CrowdStrike, 2026-05-27; TechCrunch, 2026-05-27)."
discovered_at: "2026-05-28T05:00:02Z"
event_date: 2026-05-27
run_id: 2026-05-28-3e33200a
priority: high
immediate_action: null
tags:
  - supply-chain
  - botnet
  - organized-crime
  - russia-nexus
  - law-enforcement
regions:
  - global
  - europe
sectors:
  - technology
entities:
  - "campaign:glassworm-developer-botnet-takedown-crowdstrike-google-shadowserver-russia-attri"
cves: []
sources:
  - url: "https://www.crowdstrike.com/en-us/blog/inside-crowdstrike-takedown-of-a-developer-targeting-botnet/"
    publisher: CrowdStrike Counter Adversary Operations
    role: primary
  - url: "https://techcrunch.com/2026/05/27/crowdstrike-and-google-take-down-botnet-used-by-hackers-to-target-software-developers-in-supply-chain-attacks/"
    publisher: TechCrunch
    role: corroborating
  - url: "https://thehackernews.com/2026/05/glassworm-malware-takedown-disrupts.html"
    publisher: The Hacker News
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
migrated_from: briefs/2026-05-28.md
---

On 2026-05-26T14:00Z, CrowdStrike Counter Adversary Operations, Google, and the Shadowserver Foundation executed a simultaneous takedown of all four C2 channels operated by GlassWorm, a developer-targeting supply-chain campaign active since at least early 2025 ([CrowdStrike Counter Adversary Operations, 2026-05-27](https://www.crowdstrike.com/en-us/blog/inside-crowdstrike-takedown-of-a-developer-targeting-botnet/); [TechCrunch, 2026-05-27](https://techcrunch.com/2026/05/27/crowdstrike-and-google-take-down-botnet-used-by-hackers-to-target-software-developers-in-supply-chain-attacks/); [The Hacker News, 2026-05-27](https://thehackernews.com/2026/05/glassworm-malware-takedown-disrupts.html)). GlassWorm's C2 architecture was designed for resilience: (1) Solana blockchain — C2 server addresses encoded in transaction memo fields as an immutable public dead-drop; (2) BitTorrent DHT — `GlasswormRAT` queries the peer-to-peer network for configuration data stored against hardcoded public keys; (3) Google Calendar — event titles used as Base64-encoded path dead-drops; (4) traditional VPS-hosted C2 for final payload. Taking down any subset would have left the remainder operational.

The attack surface spanned VS Code Marketplace, Open VSX (reaching Forgejo/Gitea-based forks), npm, PyPI, and direct GitHub repository poisoning via stolen developer credentials — 300+ GitHub repositories poisoned across the campaign. Infected hosts were converted into covert infrastructure: SOCKS proxies, hidden VNC (HVNC) servers, and Node.js-based remote execution nodes via WebRTC. CrowdStrike attributes the operators to likely Russia-based actors on the basis of the malware's CIS-locale / language / timezone exit check.

**Defender takeaway:** the takedown sinkholes existing C2 but does not remediate the infected developer endpoints. Treat every workstation that installed an affected VS Code / Cursor / Windsurf extension between early 2025 and 2026-05-26 as potentially compromised; rotate every CI/CD secret, cloud credential, and GitHub PAT accessible from that host. Hunt: enumerate the org's installed VS Code extension inventory against the published `OpenVSX` extension allowlist; correlate with developer-endpoint outbound WebRTC connections from `node.exe` parents.
