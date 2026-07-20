---
schema: 1
kind: threat
horizon: operational
title: "CERT-UA: Sandworm subcluster UAC-0145 pairs ClickFix fake-CAPTCHA with Ethereum-smart-contract C2 resolution and a Signal-delivered Android backdoor"
headline: "GRU's Sandworm adopts ClickFix, blockchain-hidden C2 (EtherHiding) and a Signal-lured Android backdoor — transferable tradecraft for EU CI defenders"
summary: >
  CERT-UA reports UAC-0145, a subcluster of Sandworm (APT44 / Seashell Blizzard, GRU),
  compromised at least 10 legitimate websites in June–July 2026 to serve a fake CAPTCHA
  that coerces visitors into pasting a PowerShell command (ClickFix), staging VBS
  persistence and Python backdoors. The injected CAPTCHA resolves its content domain via
  an Ethereum smart-contract call (EtherHiding) to survive takedowns, and the group
  separately distributes a full-featured Android backdoor (COWARDDUCK) via Signal disguised
  as security software. Primary targeting is Ukraine, but Sandworm is a standing threat to
  European CI/government and the technique stack is directly transferable.
discovered_at: "2026-07-20T04:30:00Z"
event_date: "2026-07-19"
run_id: 2026-07-20T0409Z-intel
priority: notable
immediate_action: null
tags: [nation-state, espionage, phishing, mobile]
regions: [europe, russia-cis]
sectors: [public-sector, defense]
nexus: [russia-nexus]
entities: [actor:uac-0145, actor:sandworm]
techniques: [T1189, T1204.004, T1059.001, T1547.001, T1102, T1568]
affected_products: []
cves: []
sources:
  - url: "https://cert.gov.ua/article/6318437"
    publisher: "CERT-UA"
    date: "2026-07-19"
    role: primary
  - url: "https://thehackernews.com/2026/07/uac-0145-uses-clickfix-captchas-to.html"
    publisher: "The Hacker News"
    date: "2026-07-19"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The CAPTCHA content to be injected into the web page employs the EtherHiding technique to retrieve the domain name of the remote resource from an Ethereum smart contract using an address specified in the source code."
    publisher: "The Hacker News"
  - quote: "The malware embedded in the APK file is a full-featured backdoor codenamed COWARDDUCK that can clandestinely collect the following details"
    publisher: "The Hacker News"
verification: single-source-national-cert
sourcing_note: "CERT-UA is the primary disclosing authority for its own jurisdiction (national-CERT carve-out); The Hacker News (2026-07-19) provides English-language corroboration but its facts derive from the same CERT-UA advisory, so this is effectively single-origin. The CERT-UA page's 'Published Time' metadata reads 2026-03-10, which contradicts the article's own June–July 2026 activity dates — treated as a site-metadata artefact, with the in-window reporting date anchored to the 2026-07-19 disclosure. No attacker-controlled indicators are reproduced (no-IOC policy); abused legitimate platforms are named only as technique."
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: null
---

CERT-UA reports that UAC-0145 — a subcluster of UAC-0002 / Sandworm (APT44, Seashell Blizzard), the GRU-linked destructive-actor family — compromised at least 10 legitimate websites between June and July 2026 to serve a fake CAPTCHA that instructs visitors to paste and run a PowerShell command in the ClickFix pattern ([The Hacker News, 2026-07-19](https://thehackernews.com/2026/07/uac-0145-uses-clickfix-captchas-to.html)). The PowerShell one-liner drops a VBS persistence stub into the Startup folder — "one of the variants of such a program was called GHETTOVIBE," per CERT-UA — which stages a PowerShell reconnaissance script (SCOUTCURL) that profiles the host, while two loaders, FLUIDLEECH (masquerading as software for removing computer viruses) and LOADLOOP, fetch a Python backdoor, FREAKYPOLL ([The Hacker News, 2026-07-19](https://thehackernews.com/2026/07/uac-0145-uses-clickfix-captchas-to.html)). The compromised-site injection uses a bespoke tool, SMARTAXE, layered on the commodity Cloaking.House traffic-filtering service to serve different content by visitor; the injected CAPTCHA "content to be injected into the web page employs the EtherHiding technique to retrieve the domain name of the remote resource from an Ethereum smart contract" ([The Hacker News, 2026-07-19](https://thehackernews.com/2026/07/uac-0145-uses-clickfix-captchas-to.html)) — a `eth_call`-style read that replaces a hardcoded C2 domain and survives takedowns because the resolution layer lives on-chain.

Separately, UAC-0145 distributes a full-featured Android backdoor, COWARDDUCK, via Signal disguised as security software; it collects contacts, files matching targeted extensions, and real-time geolocation, uploading via the Dropbox API and pulling C2 tasking from content hosted on legitimate services (e.g. Steam Community) proxied through a public search-engine proxy — both chosen to blend into normal outbound traffic ([CERT-UA, 2026-07-19](https://cert.gov.ua/article/6318437)). CERT-UA frames this as a continuation of its multi-year UAC-0145 tracking; the group's earlier tradecraft (trojanized torrent installers, Signal "antivirus" lures) is background — the in-window delta is the ClickFix vector, the EtherHiding C2-resolution layer, and the COWARDDUCK mobile backdoor. The ClickFix pivot marks a departure from Sandworm's prior reliance on trojanized Windows/Office installers ([The Hacker News, 2026-07-19](https://thehackernews.com/2026/07/uac-0145-uses-clickfix-captchas-to.html)).

**Defender takeaway:** Sandworm is a standing threat to European critical infrastructure and government, so this technique stack matters to EU/Swiss defenders even though the current victims are in Ukraine. Hunt on the desktop chain: a Startup-folder VBS created around the time a browser presents a "CAPTCHA" asking the user to open Win+R or a terminal and paste text; PowerShell child processes of `explorer.exe` or a browser with no prior parent-child history (process-creation telemetry with lineage — Sysmon EID 1, EDR process events); and, for the EtherHiding tell, outbound `eth_call`-style JSON-RPC traffic to public Ethereum nodes originating from endpoints rather than developer tooling. For mobile fleets, treat Signal-delivered APKs claiming to be AV/security tools as hostile, and watch BYOD/MDM egress for the Dropbox-API-plus-legitimate-platform C2 pattern. **Triage:** developer and IT-admin hosts legitimately spawn PowerShell from many parents and legitimately query blockchain nodes — the discriminators are (1) the PowerShell instance being a child of a browser/`explorer` immediately after a web CAPTCHA prompt, paired with a new Startup-folder VBS, and (2) `eth_call` traffic from a general-purpose endpoint with no Web3 developer role; either alone is weak, the sequence is the signal.
