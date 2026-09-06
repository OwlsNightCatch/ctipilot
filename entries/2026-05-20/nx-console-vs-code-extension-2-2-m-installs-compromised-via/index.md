---
schema: 1
kind: threat
title: "Nx Console VS Code extension (2.2 M installs) compromised via stolen publisher credentials — 11-minute window 2026-05-18 12:36–12:47 UTC"
headline: "Nx Console VS Code extension (2.2 M installs) compromised via stolen publisher credentials — 11-minute window 2026-05-18 12:36–12:47 UTC"
summary: "On 2026-05-18 between 12:36 and 12:47 UTC, version 18.95.0 of the Nx Console VS Code extension (nrwl.angular-console, 2.2+ million installs) was pushed to the Visual Studio Marketplace using stolen publisher credentials."
discovered_at: "2026-05-20T05:00:04Z"
event_date: 2026-05-19
run_id: 2026-05-20-a0f7b07f
priority: notable
immediate_action: null
tags:
  - supply-chain
  - infostealer
  - identity
  - cloud
regions:
  - global
sectors:
  - technology
entities: []
cves: []
sources:
  - url: "https://cybersecuritynews.com/nx-console-vs-code-extension-compromised/"
    publisher: "CybersecurityNews, 2026-05-19"
    role: primary
  - url: "https://thehackernews.com/2026/05/compromised-nx-console-18950-targeted.html"
    publisher: "The Hacker News, 2026-05-19"
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
migrated_from: briefs/2026-05-20.md
---

On 2026-05-18 between 12:36 and 12:47 UTC, version **18.95.0** of the Nx Console VS Code extension (`nrwl.angular-console`, 2.2+ million installs) was pushed to the Visual Studio Marketplace using stolen publisher credentials. The malicious version activated on any workspace open, fetching a 498 KB obfuscated payload from a dangling orphan commit on the official `nrwl/nx` GitHub repository; the injected code amounted to 2,777 bytes inserted into the minified `main.js` ([CybersecurityNews, 2026-05-19](https://cybersecuritynews.com/nx-console-vs-code-extension-compromised/)). The payload is a multi-stage stealer harvesting tokens from GitHub, npm, AWS, HashiCorp Vault, Kubernetes kubeconfigs, and 1Password, exfiltrating over three independent channels: HTTPS, GitHub API as dead-drop, and DNS tunnelling. On macOS the loader installs a persistent Python backdoor using the GitHub Search API as command channel, with messages signed with a 4096-bit RSA key ([The Hacker News, 2026-05-19](https://thehackernews.com/2026/05/compromised-nx-console-18950-targeted.html)). Safe version: 18.100.0 or later.

**Why it matters to us:** Any developer who opened a workspace during the 11-minute window with Nx Console installed should treat every credential accessible from that machine as compromised — that includes corporate GitHub PATs that grant access to public-sector repos, cloud-deployment credentials, and any secret manager whose CLI ever ran on that host. The pattern — abuse of marketplace publisher credentials to push a transient malicious version, with the malicious binary itself short-lived enough to evade most retrospective scanning — generalises beyond Nx Console; expect imitators.
