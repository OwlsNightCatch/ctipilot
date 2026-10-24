---
schema: 1
kind: threat
title: "PhantomRaven: CrowdStrike attributes an LLM-generated npm infostealer, hidden from registry scanners via a remote-URL dependency trick, to a self-described bug-bounty hunter"
headline: "A bug-bounty hunter builds their own npm infostealer to manufacture the compromises they then report for a payout"
summary: >
  CrowdStrike identifies a financially motivated actor — a self-described bug-bounty hunter active
  since 2022 — as the developer of PhantomRaven, an npm information stealer CrowdStrike assesses
  is almost certainly LLM-generated. The malware ships inside typosquatted packages that contain
  only trivial code, with the real payload fetched at install time via a raw-HTTP-URL dependency
  that bypasses the npm registry's own scanning surface, then harvests CI/CD environment
  variables and tokens from GitHub Actions, GitLab CI, Jenkins and CircleCI. The actor reportedly
  uses resulting compromises to submit bug-bounty disclosures for payouts.
discovered_at: "2026-09-17T04:48:00Z"
updated_at: null
event_date: "2026-09-16"
run_id: 2026-09-17T0409Z-intel
priority: notable
immediate_action: null
tags: [supply-chain, infostealer, ai-abuse]
regions: [global]
sectors: [technology, public-sector]
entities: ["malware:phantomraven"]
techniques: [T1195.001, T1552.001, T1552.007, T1071.001, T1016.001, T1082, T1036.005, T1072, T1027.009, T1587.001, T1041, T1005, T1083, T1104]
affected_products: ["npm (Node Package Manager)", "GitHub Actions", "GitLab CI", "Jenkins", "CircleCI"]
cves: []
sources:
  - url: "https://www.crowdstrike.com/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/"
    publisher: "CrowdStrike Counter Adversary Operations"
    date: "2026-09-16"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/new-phantomraven-npm-attack-wave-steals-dev-data-via-88-packages/"
    publisher: "BleepingComputer, citing Endor Labs research"
    date: "2026-03-11"
    role: corroborating
  - url: "https://www.endorlabs.com/learn/return-of-phantomraven"
    publisher: "Endor Labs"
    date: "2026-03-10"
    role: corroborating
closed_sources: []
evidence:
  - quote: "PhantomRaven is a simple JS information stealer that exfiltrates system information and continuous integration/continuous deployment (CI/CD)-related environment variables, likely in an attempt to collect account credentials. The code was almost certainly LLM-generated, and the author's technical sophistication is likely low."
    publisher: "CrowdStrike Counter Adversary Operations"
  - quote: "In npm version 12 or later, if a developer attempts to install a dependency package with a preinstall script, they receive a warning message indicating that the script has been blocked and will not automatically execute."
    publisher: "CrowdStrike Counter Adversary Operations"
verification: single-source
sourcing_note: "The September 2026 attribution to a single operator and the LLM-generation assessment rest solely on CrowdStrike's own cross-platform identity correlation. The underlying malware family, its Remote Dynamic Dependency technique and prior campaign waves are independently documented by Koi Security and Endor Labs (via BleepingComputer), so the technique itself is well-corroborated even though the September 2026 attribution angle is CrowdStrike-exclusive."
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

CrowdStrike Counter Adversary Operations attributes PhantomRaven, an npm information stealer, to a single financially motivated actor who publicly describes themself as a bug-bounty hunter and has been active since November 2022 ([CrowdStrike, 2026-09-16](https://www.crowdstrike.com/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/)). CrowdStrike assesses with high confidence that the malware's code is LLM-generated, based on verbose per-symbol comments explaining the obvious, placeholder code, and statistical token-analysis patterns consistent with an LLM token stream ([CrowdStrike, 2026-09-16](https://www.crowdstrike.com/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/)). The actor distributes the stealer through typosquatted npm packages whose visible code is trivial and non-malicious, but whose `package.json` specifies a dependency via a raw HTTP URL rather than a normal registry reference — a Remote Dynamic Dependency that npm fetches silently at install time from attacker-controlled infrastructure, so the real payload never appears in the registry's own web interface or most automated scanners. The fetched payload registers as a `preinstall` script that auto-executes on `npm install`; CrowdStrike credits npm 12's June 2026 default block on unapproved preinstall scripts with narrowing this vector going forward ([CrowdStrike, 2026-09-16](https://www.crowdstrike.com/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/)).

Once running, the stealer harvests host/OS information, local and external IP addresses, Node.js version, the current working directory and process ID, Git- and npm-configured usernames and emails, and CI/CD environment variables covering GitHub Actions, GitLab CI, Jenkins and CircleCI — tokens, project IDs and build URLs consistent with harvesting CI/CD account credentials rather than end-user secrets. Exfiltration goes out over both HTTP GET and POST to the same command-and-control domains, and the code also carries an incomplete fallback WebSocket exfiltration path CrowdStrike reads as unfinished, redundant infrastructure rather than a live channel. CrowdStrike correlated npm usernames, an X account, a HackerOne-referencing alias, a GitHub account and a rejected 2025 PyPI submission back to the same operator, who publicly claims via their own X profile to have collected bounties from at least nine organizations across tech, retail and hospitality via Bugcrowd, Intigriti, YesWeHack, HackenProof and HackerOne — using compromises their own malware enabled as leverage for disclosure submissions ([CrowdStrike, 2026-09-16](https://www.crowdstrike.com/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/)). The malware family itself and its Remote Dynamic Dependency technique were first documented by Koi Security, whose original wave affected 126+ packages with over 86,000 downloads ([Endor Labs, 2026-03-10](https://www.endorlabs.com/learn/return-of-phantomraven), citing Koi Security); Endor Labs' own follow-up research identified three further waves totalling 88 more packages between November 2025 and February 2026 ([Endor Labs, 2026-03-10](https://www.endorlabs.com/learn/return-of-phantomraven)). CrowdStrike's new contribution is the actor-identification and monetization-motive finding.

**Defender takeaway:** hunt for `preinstall`/`postinstall` npm lifecycle-script execution spawning outbound HTTP connections to non-registry hosts immediately after `npm install`, and for CI/CD runner processes making outbound connections to IP-lookup services (e.g. `ipify.org`-style APIs) followed by GET/POST exfiltration traffic. Ensure CI/CD pipelines run on a current npm major version so unapproved preinstall scripts are blocked by default, and treat any `package.json` dependency specified via a raw URL rather than a registry reference as a hard stop in code review.

**Triage:** a legitimate build tool's own telemetry or update-check call is the benign lookalike; the discriminators are the absence of any corresponding, expected package purpose for the network call and a destination domain pattern that is freshly registered or "artifact"/"registry"-themed rather than a known vendor telemetry endpoint.
