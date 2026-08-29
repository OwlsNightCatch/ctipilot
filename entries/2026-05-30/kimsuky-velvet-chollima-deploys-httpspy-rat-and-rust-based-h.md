---
schema: 1
kind: research
title: Kimsuky (Velvet Chollima) deploys HTTPSpy RAT and Rust-based HelloDoor via VS Code Remote Tunnel and Cloudflare Quick Tunnel C2
headline: Kimsuky (Velvet Chollima) deploys HTTPSpy RAT and Rust-based HelloDoor via VS Code Remote Tunnel and Cloudflare Quick Tunnel C2
summary: "ENKI WhiteHat and The Hacker News documented Kimsuky campaigns in March and April 2026 targeting South Korean military personnel and corporate entities with two malware chains (The Hacker News, 2026-05-29; ENKI WhiteHat, 2026-05-27)."
discovered_at: "2026-05-30T05:00:07Z"
event_date: 2026-05-29
run_id: 2026-05-30-aca445cc
priority: notable
immediate_action: null
tags:
  - nation-state
  - espionage
  - north-korea-nexus
  - phishing
regions:
  - apac
  - europe
  - global
sectors:
  - defense
  - public-sector
entities:
  - "actor:kimsuky"
cves: []
sources:
  - url: "https://thehackernews.com/2026/05/kimsuky-deploys-httpspy-expands-arsenal.html"
    publisher: The Hacker News
    role: primary
  - url: "https://www.enki.co.kr/en/media-center/blog/kimsuky-s-advanced-attack-techniques-jsonping-webex-spoofing-and-a-new-httpspy-variant"
    publisher: ENKI WhiteHat
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
migrated_from: briefs/2026-05-30.md
---

ENKI WhiteHat and The Hacker News documented Kimsuky campaigns in March and April 2026 targeting South Korean military personnel and corporate entities with two malware chains ([The Hacker News, 2026-05-29](https://thehackernews.com/2026/05/kimsuky-deploys-httpspy-expands-arsenal.html); [ENKI WhiteHat, 2026-05-27](https://www.enki.co.kr/en/media-center/blog/kimsuky-s-advanced-attack-techniques-jsonping-webex-spoofing-and-a-new-httpspy-variant)). March chain: masquerade installers for nProtect Online Security and AhnLab Safe Transaction launch MemLoader.dll via `regsvcs.exe`, which downloads HTTPSpy. April chain: fake Webex meeting page delivers encrypted JavaScript (`.jse` extension) which stages a PowerShell downloader, ultimately installing HTTPSpy. HTTPSpy is a full-capability RAT (first observed 2022; previously used against a German defence manufacturer May–September 2024): RC4-encrypted C2, shell execution, file upload/download, screenshot capture, process injection, self-deletion. HelloDoor is a Rust-based PebbleDash variant (assessed LLM-assisted per ENKI): configurable sleep, command execution, directory traversal. C2 evasion: Kimsuky now abuses Visual Studio Code Remote Tunneling (authenticated via GitHub OAuth, registered via `code --tunnel --name <name>`) and Cloudflare Quick Tunnels (`cloudflared.exe`) — neither can be blocked by IP or domain without blocking Microsoft and Cloudflare respectively. JSONPing confirms active infections via a locally-running HTTP server, reducing exposure of attacker infrastructure. MITRE ATT&CK: T1036 (Masquerading), T1059.001 (PowerShell), T1059.007 (JavaScript), T1071 (Application Layer Protocol). Detection: hunt for `regsvcs.exe` as a parent of DLL loads in non-.NET-Framework contexts; alert on VS Code CLI processes with `--tunnel` argument from non-developer endpoints; audit GitHub OAuth app grants for unrecognised VS Code tunnel registrations; monitor `cloudflared.exe` on managed endpoints without prior baseline.
