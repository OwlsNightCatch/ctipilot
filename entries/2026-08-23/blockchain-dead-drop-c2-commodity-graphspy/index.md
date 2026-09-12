---
schema: 1
kind: research
title: "Dead-drop command-and-control went commodity: three of four new entrants on Red Canary's monthly list resolve their C2 from a dead drop, two of them from a public blockchain, and the fourth is a GUI for Entra ID device-code phishing"
headline: "Dead-drop C2 moved from novelty to routine, and the control is an egress baseline rather than a blocklist"
summary: >
  Red Canary's monthly threat round-up, published 2026-08-20 on July 2026 telemetry, records four new
  entrants to its most-prevalent list — GraphSpy, Phexia, CastleRAT and EtherRAT — of which three
  resolve their command-and-control address from a dead drop rather than from a hardcoded domain, and
  two of those three read it from a public blockchain smart contract. The technique defeats domain and IP blocking because the operator rewrites the
  contract value and every installation picks up the change. The fourth, GraphSpy, is an open-source
  Entra ID and Microsoft 365 attack tool with a browser GUI that centralises device-code phishing,
  primary refresh token theft, Windows Hello for Business key registration and MFA method
  manipulation — the third device-code phishing tool to reach that list in 2026.
discovered_at: "2026-08-23T04:46:00Z"
event_date: "2026-08-20"
run_id: 2026-08-23T0409Z-intel
priority: notable
immediate_action: null
tags: [infostealer, identity, cloud, phishing]
regions: [global, europe]
sectors: [public-sector, finance, telco]
entities: [tool:graphspy, malware:phexia, malware:castlerat, malware:etherrat]
techniques: [T1102.001, T1204.004, T1528, T1556.006, T1543.001]
affected_products: ["Microsoft Entra ID", "Microsoft 365"]
cves: []
sources:
  - url: "https://redcanary.com/blog/threat-intelligence/intelligence-insights-august-2026/"
    publisher: "Red Canary"
    date: "2026-08-20"
    role: primary
closed_sources: []
evidence:
  - quote: "GraphSpy runs a local web server that presents a browser-based GUI, which enables less technical adversaries to engage in Entra ID attacks."
    publisher: "Red Canary"
  - quote: "The technique makes traditional C2 blocking challenging, since the URL can be updated dynamically by adversaries"
    publisher: "Red Canary"
  - quote: "the public blockchain RPC endpoints highlighted on chainlist.org are a good place to start, as adversaries are more likely to leverage widely-used URLs instead of standing up their own infrastructure"
    publisher: "Red Canary"
verification: single-source
sourcing_note: >
  Red Canary is the sole assessor for the prevalence observations and for the July 2026 telemetry
  behind them; this entry carries the technique descriptions and the mitigation guidance, which are
  the source's own, and does not restate its ranking positions, which are vendor-internal
  measurements rather than defender-actionable facts.
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
actions:
  - "Establish which users, systems and applications in your estate legitimately make HTTPS calls to public blockchain RPC endpoints — for most public-sector estates the honest answer is none — and alert on anything outside that set; chainlist.org enumerates the widely-used endpoints adversaries prefer."
migrated_from: null
---

Red Canary's monthly threat round-up, published 2026-08-20 against July 2026 telemetry, is useful here not for its rankings but for what the new arrivals have in common: three of the four resolve their command-and-control address from a dead drop rather than from a hardcoded domain or IP, and two of those read that dead drop off a public blockchain ([Red Canary, 2026-08-20](https://redcanary.com/blog/threat-intelligence/intelligence-insights-august-2026/)). The technique — querying a smart contract whose stored value is the current C2 URL, which Red Canary calls EtherHiding and dates to first reporting in 2023 — has been documented for a while; what this round-up records is its arrival in commodity tooling — Red Canary counts three of its top ten using it this month, two of them new arrivals.

The mechanics are worth stating precisely because they determine what a defender can and cannot block. **Phexia**, a macOS remote-access tool and stealer delivered through malicious copy-and-paste lures, queries public Polygon RPC endpoints for a smart contract's value, decodes the ABI-encoded response to extract a URL, posts to it and pipes the reply into `osascript`; it keeps Telegram and Steam profiles as redundant dead-drop channels and persists with a LaunchAgent that sets both `KeepAlive` and `RunAtLoad`. **EtherRAT** is *"a Node.js-based remote access trojan observed targeting Windows workstations via social engineering and Linux servers via exploitation of server-side vulnerabilities"*, polling one or more public Ethereum RPC endpoints for a C2 URL held at a predefined contract address, with modules for credential theft, lateral movement and web-server hijacking. **CastleRAT** resolves its dead drop through `steamcommunity.com` or adversary-controlled domains. Red Canary's own summary of why this matters operationally: *"The technique makes traditional C2 blocking challenging, since the URL can be updated dynamically by adversaries"* — the operator rewrites one contract value and the change propagates to every installation without redistributing the malware.

The fourth entrant is a different problem. **GraphSpy** is an open-source initial-access and post-exploitation tool for Entra ID and Microsoft 365 that, in Red Canary's words, *"runs a local web server that presents a browser-based GUI, which enables less technical adversaries to engage in Entra ID attacks"*. It centralises device-code phishing, primary refresh token theft and abuse, Windows Hello for Business key registration, MFA method manipulation, and exfiltration from SharePoint, OneDrive, Outlook and Teams. Red Canary notes it is the third device-code phishing tool to reach its top ten in 2026, after GraphRunner in May and Kali365 in June — three separate toolkits in four months packaging the same identity attack behind progressively lower skill requirements.

Detection concepts, telemetry class first. For the dead-drop families the signal is in **egress telemetry**: an outbound HTTPS session from an endpoint or server to a public blockchain RPC endpoint, made by a process that has no business speaking to one — the request itself is ordinary-looking JSON-RPC to a widely used, reputable host, so the discriminator is the process and the host role, not the destination's reputation. On macOS, correlate it with **process-lineage telemetry** showing `osascript` executing content received from a network read, and with **persistence artifacts** — a newly written LaunchAgent whose program arguments carry an encoded payload. For GraphSpy the surface is **identity telemetry** rather than endpoint: device-code authentication events for users and locations that have no workflow requiring that flow, primary refresh token issuance followed by access from an unfamiliar device, and new Windows Hello for Business key or MFA method registration on an account that did not request it. Red Canary's own mitigation for the device-code half is to revoke the affected user's refresh tokens and active sessions, reset credentials, force re-authentication, and restrict the device-code flow through Conditional Access policies *"for users and locations that do not require it"*.

**Defender takeaway:** for the blockchain channel the control is an egress baseline, not a blocklist — the endpoints are legitimate infrastructure that cannot be reputation-blocked, so the question to answer in advance is which of your systems have any legitimate reason to query a public chain. For most public-sector and critical-infrastructure estates that set is empty, which turns a hard detection problem into a simple one. **Triage:** developer workstations and any wallet, blockchain-analytics or Web3 tooling produce genuine RPC traffic to the same endpoints; the separators are whether the querying process is a browser or developer toolchain versus a script interpreter or service binary, whether the same host subsequently contacts an address it learned rather than one it was configured with, and whether the query pattern is interactive or a steady poll.
