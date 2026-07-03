---
schema: 1
kind: threat
horizon: operational
title: "TeamPCP / Shai-Hulud — first copycat wave (Phantom Bot + SSH/cloud stealers), Checkmarx Jenkins plugin trojanised again, PCPJack rival worm hits exposed cloud services"
headline: "TeamPCP / Shai-Hulud — first copycat wave (Phantom Bot + SSH/cloud stealers), Checkmarx Jenkins plugin trojanised again, PCPJack rival worm hits exposed cloud"
summary: "TeamPCP/Shai-Hulud copycat wave begins — first imitator drops Phantom Bot DDoS and SSH/cloud-credential stealers in four typosquatted npm packages (OX Security, 2026-05-17). chalk-tempalte is a direct clone of the leaked Shai-Hulud worm source code that Datadog Security Labs analysed on 2026-05-13."
discovered_at: "2026-05-19T05:00:07Z"
event_date: 2026-05-18
run_id: 2026-05-19-2505c918
priority: high
immediate_action: null
tags:
  - supply-chain
  - ransomware
  - organized-crime
  - infostealer
  - botnet
regions:
  - global
  - europe
sectors:
  - technology
  - public-sector
entities:
  - "tool:pcpjack-cloud-worm-2026"
  - "actor:teampcp"
cves: []
sources:
  - url: "https://www.ox.security/blog/new-actors-deploy-shai-hulud-clones-teampcp-copycats-are-here/"
    publisher: OX Security
    role: primary
  - url: "https://thehackernews.com/2026/05/four-malicious-npm-packages-deliver.html"
    publisher: The Hacker News
    role: corroborating
  - url: "https://isc.sans.edu/diary/rss/32994"
    publisher: SANS Internet Storm Center
    role: corroborating
  - url: "https://checkmarx.com/blog/ongoing-security-updates/"
    publisher: Checkmarx
    role: corroborating
closed_sources: []
evidence:
  - quote: One of the packages (chalk-tempalte) is a direct clone of the Shai-Hulud worm open-sourced by TeamPCP with modified C2 infrastructure
    publisher: The Hacker News
  - quote: Checkmarx officially confirmed that a tampered plugin (version 2026.5.09) had been published to the Jenkins Marketplace ... This is the third TeamPCP compromise of Checkmarx in three months
    publisher: SANS Internet Storm Center
verification: multi-source
sourcing_note: null
confidence: high
update_of: 2026-05-13/mini-shai-hulud-teampcp-worm-hits-tanstack-uipath-mistral-ai
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-19.md
---

**UPDATE (originally covered 2026-05-13, 2026-05-15):** Three concurrent developments show the TeamPCP / Shai-Hulud campaign has entered an open-source-imitator phase following Datadog Security Labs' 2026-05-13 analysis of the leaked Shai-Hulud worm source code. First, OX Security disclosed on 2026-05-17 four malicious npm packages published by `deadcode09284814` — `chalk-tempalte`, `@deadcode09284814/axios-util`, `axois-utils`, and `color-style-utils` — combined weekly downloads ~3,000 ([OX Security, 2026-05-17](https://www.ox.security/blog/new-actors-deploy-shai-hulud-clones-teampcp-copycats-are-here/); [The Hacker News, 2026-05-18](https://thehackernews.com/2026/05/four-malicious-npm-packages-deliver.html)). `chalk-tempalte` is a near-unmodified clone of the leaked Shai-Hulud worm with a modified C2 server and a new attacker-controlled key embedded in the code — the two primary sources disagree on whether this is a public or private key (; `axois-utils` bundles "Phantom Bot," a Golang HTTP/TCP/UDP/Reset-flood DDoS tool with Windows Startup folder and Linux scheduled-task persistence that survives package removal; the other two harvest SSH keys, cloud-provider credentials (AWS/GCP/Azure), and cryptocurrency wallet data.

Second, SANS ISC synthesised a 2026-05-18 campaign update confirming that Checkmarx officially acknowledged on 2026-05-11 that its Jenkins AST Scanner plugin had been trojanised — version `2026.5.09`, compromise window 2026-05-09 01:25 UTC to 2026-05-10 08:47 UTC — making this TeamPCP's third confirmed Checkmarx intrusion in three months ([SANS Internet Storm Center, 2026-05-18](https://isc.sans.edu/diary/rss/32994); [Checkmarx, 2026-05-12](https://checkmarx.com/blog/ongoing-security-updates/)). Hundreds of Jenkins controllers installed the malicious plugin before removal; remediated builds `2.0.13-848` and `2.0.13-847` are safe. CxSAST on-premise was unaffected; the cloud-integrated `checkmarx/ast-github-action`, `checkmarx/kics-github-action`, and VS Code extensions were all trojaned.

Third, SentinelLabs disclosed on 2026-05-07 — also folded into the SANS ISC summary — "PCPJack," a rival cloud worm that scans for exposed Docker, Kubernetes, Redis, MongoDB and RayML services and chains five CVEs (CVE-2025-29927 Next.js middleware auth bypass; CVE-2025-55182 Next.js Server Actions deserialization; CVE-2026-1357 WPVivid arbitrary file upload; CVE-2025-9501 W3 Total Cache RCE; CVE-2025-48703 CentOS Web Panel command injection) for initial access, then explicitly kills TeamPCP processes and removes TeamPCP artefacts before harvesting credentials — assessed by SentinelLabs with moderate confidence as possibly a former TeamPCP affiliate. Defender takeaway for the Swiss/EU public-sector SOC: developer endpoints and CI/CD runners with installed Checkmarx plugin should be audited for plugin versions outside the known-safe SHA range during the 2026-05-09 → 2026-05-10 window; `npm audit` and SBOM scans should flag the `deadcode09284814` author/scope; egress from CI runners to `*.lhr.life` hostnames is a high-fidelity hunt pivot for the npm worm wave; Docker/Kubernetes/Redis/MongoDB endpoints exposed to the internet should be inventoried and removed from public exposure (PCPJack's scan list). MITRE T1195.002 (Supply Chain Compromise), T1552.001 (Credentials in Files), T1041 (Exfiltration over C2 Channel).
