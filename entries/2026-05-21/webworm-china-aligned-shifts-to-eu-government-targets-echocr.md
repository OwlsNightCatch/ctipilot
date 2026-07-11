---
schema: 1
kind: threat
horizon: operational
title: "Webworm (China-aligned) shifts to EU government targets — EchoCreep (Discord C2) and GraphWorm (Microsoft Graph / OneDrive C2) backdoors documented by ESET, with Belgian, Italian, Serbian, Polish and Spanish governmental victims"
headline: Webworm (China-aligned) shifts to EU government targets — EchoCreep (Discord C2) and GraphWorm (Microsoft Graph / OneDrive C2) backdoors documented by ESET
summary: "Webworm (China-aligned) targets Belgian, Italian, Serbian and Polish government organisations with two new custom backdoors — EchoCreep (Discord C2) and GraphWorm (Microsoft Graph / OneDrive C2). ESET also documents Spanish and Italian governmental documents exfiltrated to a compromised AWS S3 bucket (ESET Research, 2026-05-20)."
discovered_at: "2026-05-21T05:00:00Z"
event_date: 2026-05-20
run_id: 2026-05-21-77cdc4cd
priority: high
immediate_action: null
tags:
  - nation-state
  - espionage
  - identity
  - cloud
  - china-nexus
regions:
  - europe
sectors:
  - public-sector
  - education
entities:
  - "actor:webworm-fishmonger-aquatic-panda-eset-echocreep-graphworm-eu"
cves: []
sources:
  - url: "https://www.welivesecurity.com/en/eset-research/webworm-new-burrowing-techniques/"
    publisher: ESET WeLiveSecurity
    role: primary
  - url: "https://thehackernews.com/2026/05/webworm-deploys-echocreep-and-graphworm.html"
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
migrated_from: briefs/2026-05-21.md
---

ESET Research published a technical analysis on 2026-05-20 of Webworm — also tracked as FishMonger / Aquatic Panda / SixLittleMonkeys / Space Pirates — documenting a 2025 campaign pivot to European governmental organisations in Belgium, Italy, Serbia and Poland, plus a South African university; the group has abandoned its prior primary backdoors (Trochilus RAT, McRat / 9002 RAT) in favour of two new custom implants — EchoCreep (which ESET describes as written in Go) and GraphWorm ([ESET WeLiveSecurity, 2026-05-20](https://www.welivesecurity.com/en/eset-research/webworm-new-burrowing-techniques/)). **EchoCreep** uses Discord as a bidirectional C2 channel, encoding commands with base64 + AES-CBC-128; it creates per-victim Discord channels named after the victim IP (or IP+hostname), supports file upload/download and `cmd.exe` command execution, and ESET recovered 433 decrypted Discord messages dating back to 2024-03-21 from four unique victim channels (`T1102.002` Web Service: Bidirectional Communication, `T1059.003` Windows Command Shell). **GraphWorm** is more capable: an implant (implementation language not stated in the ESET write-up) that authenticates against the Microsoft Graph API and uses per-victim OneDrive directories for C2, with `/createUploadSession` for large-file exfiltration and AES-256-CBC + base64 encoding on uploaded data (`T1102.002`, `T1071.001` Application Layer Protocol — Web Protocols); it persists at logon and spawns `cmd.exe` sessions under the implant's process context. The custom proxy toolkit added in 2025 includes **WormFrp** (a modified `frp` that pulls its config from a compromised AWS S3 bucket `wamanharipethe.s3.ap-south-1.amazonaws.com`), **ChainWorm** (multi-hop chaining), **SmuxProxy**, and **WormSocket** (`socket.io`-based proxy); a **SharpSecretsdump** Impacket-look-alike credential dumper was uploaded to the same S3 bucket in October 2025 (`T1003.001` OS Credential Dumping: LSASS Memory) ([ESET, 2026-05-20](https://www.welivesecurity.com/en/eset-research/webworm-new-burrowing-techniques/); [The Hacker News, 2026-05-20](https://thehackernews.com/2026/05/webworm-deploys-echocreep-and-graphworm.html)). Files exfiltrated from victims and staged in the S3 bucket included virtual-machine snapshots from an Italian governmental entity and an mRemoteNG connection-configuration file plus a Microsoft Visio infrastructure diagram from a Spanish governmental entity — both documents that materially aid follow-on intrusion. Initial-access tradecraft documented against Serbian targets used CVE-2017-7692 (SquirrelMail post-auth RCE), implying credential theft preceded webmail exploitation. **Why it matters to us:** the cloud-API C2 design (Discord, Microsoft Graph) blends with legitimate enterprise traffic and defeats domain / URL block-lists. Detection concept — alert on Sysmon EID 3 outbound HTTPS to `discord.com/api/*` or `graph.microsoft.com` from process trees whose parent is not the expected first-party application (`Discord.exe`, `Teams.exe`, `OneDrive.exe`, Office); correlate Graph API non-interactive sign-ins in Entra ID for app registrations with no enterprise approval path; flag `cmd.exe` spawned by long-running services with no interactive user context. Hardening — Conditional Access for the Microsoft Graph application restricting non-managed device sign-ins; block `socket.io` and Discord WebSocket outbound at the SWG for server workloads that have no business reason; force first-party-only WebSocket egress on government-segment workstations.
