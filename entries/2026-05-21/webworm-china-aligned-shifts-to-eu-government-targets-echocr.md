---
schema: 1
kind: threat
title: "Webworm (China-aligned) turns to European government targets with the EchoCreep (Discord) and GraphWorm (Microsoft Graph and OneDrive) backdoors, ESET reports"
headline: "ESET: China-aligned Webworm targeted governments in Belgium, Italy, Serbia and Poland with Discord and OneDrive implants"
summary: >
  ESET reported on 2026-05-20 that the China-aligned group Webworm targeted governmental organizations in
  Belgium, Italy, Serbia and Poland, and a South African university, in 2025 with two new backdoors:
  EchoCreep, written in Go, which takes commands through Discord, and GraphWorm, which uses Microsoft Graph
  and OneDrive for command and control. A compromised third-party Amazon S3 bucket held its proxy
  configurations and files taken from Italian and Spanish governmental entities; ESET could not find the
  entry point, but the group scanned victims' web servers and ran a public SquirrelMail exploit
  (CVE-2017-7692) against a Serbian webmail target.
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
techniques: [T1595.002, T1595.003, T1588.006, T1583.003, T1583.004, T1584.006, T1608.002, T1059.003, T1053.005, T1547.001, T1112, T1070.004, T1070.006, T1027.013, T1550.001, T1078.004, T1021.007, T1005, T1074.001, T1074.002, T1105, T1071.001, T1132.001, T1573.002, T1090.001, T1090.002, T1090.003, T1102.002, T1041, T1567.002]
cves:
  - id: CVE-2017-7692
    cvss: "n/a"
    epss: null
    type: rce
    vector: zero-click
    auth: post-auth
    status:
      - poc-public
    affected: "SquirrelMail webmail (versions not given by ESET)"
    fixed: null
sources:
  - url: "https://www.welivesecurity.com/en/eset-research/webworm-new-burrowing-techniques/"
    publisher: "ESET Research (WeLiveSecurity)"
    date: "2026-05-20"
    role: primary
  - url: "https://thehackernews.com/2026/05/webworm-deploys-echocreep-and-graphworm.html"
    publisher: "The Hacker News"
    date: "2026-05-20"
    role: corroborating
closed_sources: []
evidence:
  - quote: "This trend continued in 2025, with the attacks we observed targeting governmental organizations in Belgium, Italy, Serbia, and Poland."
    publisher: "ESET Research (WeLiveSecurity)"
    source_url: "https://www.welivesecurity.com/en/eset-research/webworm-new-burrowing-techniques/"
  - quote: "Upon EchoCreep’s first execution, it does not attempt to create a new channel, but sends a message saying Up Success to a channel that already exists"
    publisher: "ESET Research (WeLiveSecurity)"
    source_url: "https://www.welivesecurity.com/en/eset-research/webworm-new-burrowing-techniques/"
  - quote: "In the case of GraphWorm, which uses Microsoft Graph API for C&C communication, we discovered that it uses OneDrive endpoints exclusively, specifically to get new jobs and to upload victim information."
    publisher: "ESET Research (WeLiveSecurity)"
    source_url: "https://www.welivesecurity.com/en/eset-research/webworm-new-burrowing-techniques/"
  - quote: "ESET told The Hacker News that Webworm's links to Space Pirates is tenuous at best, citing the use of open-source RATs and a lack of concrete evidence tying the two clusters."
    publisher: "The Hacker News"
    source_url: "https://thehackernews.com/2026/05/webworm-deploys-echocreep-and-graphworm.html"
verification: single-source
sourcing_note: >
  ESET Research is the only assessor, from its own telemetry and decrypted command traffic, and the
  attribution to Webworm is ESET's; The Hacker News restates it with ESET's comments on related clusters.
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
migrated_from: briefs/2026-05-21.md
updates:
  - at: "2026-10-21T20:41:34Z"
    run_id: 2026-10-21T1148Z-audit
    type: correction
    summary: >
      ESET links Webworm to SixLittleMonkeys and FishMonger as related groups and calls a Space Pirates
      link tenuous, so none of them are names for Webworm; EchoCreep reports to Discord channels the
      operators created in advance rather than creating them. The S3 bucket was a compromised third-party
      bucket, since taken down, SharpSecretsdump was only uploaded to it, and the ATT&CK mapping follows
      ESET's own table.
    fields: [body, classification, cves, evidence, headline, sources, sourcing_note, summary, techniques, title, verification]
---

ESET Research published its analysis of Webworm, a China-aligned group active since at least 2022 that it links to SixLittleMonkeys and FishMonger, on 2026-05-20: in 2025 the group moved from Asia to governmental organizations in Belgium, Italy, Serbia and Poland, compromised a South African university, and replaced its Trochilus and McRat backdoors with two new ones, EchoCreep and GraphWorm ([ESET, 2026-05-20](https://www.welivesecurity.com/en/eset-research/webworm-new-burrowing-techniques/)). ESET told The Hacker News that a link to Space Pirates is tenuous at best ([The Hacker News, 2026-05-20](https://thehackernews.com/2026/05/webworm-deploys-echocreep-and-graphworm.html)). ESET could not find the entry point, but an operator server showed nuclei and dirsearch scans of 56 targets in countries including Spain, Hungary, Belgium, Nigeria, Czechia and Serbia, and a public exploit for the SquirrelMail post-authentication RCE CVE-2017-7692 run against a Serbian webmail target, which suggests the group held that victim's credentials ([ESET, 2026-05-20](https://www.welivesecurity.com/en/eset-research/webworm-new-burrowing-techniques/)).

**EchoCreep and GraphWorm.** EchoCreep, written in Go, sends all its traffic through Discord API endpoints, decodes commands with base64 and AES-CBC-128, runs them through `cmd.exe` and uploads files as attachments; it reports to per-victim channels, named after the victim's IP address or IP address and hostname, that the operators created before it first ran, and it runs under a custom scheduled task and carries a modified timestamp ([ESET, 2026-05-20](https://www.welivesecurity.com/en/eset-research/webworm-new-burrowing-techniques/)). ESET decrypted 433 messages going back to 2024-03-21 across four victim channels; the first real compromise came on 2025-04-09, followed by curl downloads ([ESET, 2026-05-20](https://www.welivesecurity.com/en/eset-research/webworm-new-burrowing-techniques/)). GraphWorm runs at every user logon through registry Run keys and talks only to OneDrive endpoints of Microsoft Graph, with a valid cloud account and API tokens, fetching jobs from and uploading results to a per-victim folder; it encrypts traffic with AES-256-CBC and base64, stages command output in a local file that it deletes after upload, and likely uses Graph's upload-session endpoint for large files ([ESET, 2026-05-20](https://www.welivesecurity.com/en/eset-research/webworm-new-burrowing-techniques/)).

**Proxies, staging and stolen data.** The proxy tools WormFrp, a modified frp that reads AES-encrypted configurations from a compromised third-party Amazon S3 bucket, ChainWorm, SmuxProxy and WormSocket build internal, external and multi-hop proxies through rented servers and VPS hosts, the group staged tools in a GitHub repository, and both the repository and the S3 bucket have been taken down ([ESET, 2026-05-20](https://www.welivesecurity.com/en/eset-research/webworm-new-burrowing-techniques/)). The S3 bucket held virtual-machine snapshots, one with the state of an Italian governmental machine, and from December 2025 to January 2026 an mRemoteNG connection-configuration file and a Visio infrastructure diagram taken from a Spanish governmental entity; in October 2025 the operators also uploaded SharpSecretsdump, a tool that mimics Impacket's secretsdump ([ESET, 2026-05-20](https://www.welivesecurity.com/en/eset-research/webworm-new-burrowing-techniques/)).

**Exposure:** governmental organizations in Europe, Webworm's focus since 2025, and in particular internet-facing web servers and webmail, which the group scans and probes ([ESET, 2026-05-20](https://www.welivesecurity.com/en/eset-research/webworm-new-burrowing-techniques/)).

**Detection:** egress and endpoint telemetry: Discord API traffic from hosts or processes with no business use of Discord, Microsoft Graph OneDrive calls from an unexpected process, new scheduled tasks and Run-key entries starting unfamiliar binaries, and frp-style reverse and SOCKS5 proxies opening outbound connections ([ESET, 2026-05-20](https://www.welivesecurity.com/en/eset-research/webworm-new-burrowing-techniques/)). Because ESET reads the SquirrelMail exploit as run with the victim's own credentials, a webmail account it touched needs a new password after clean-up.

**Defender takeaway:** European government networks hunt for the Discord and OneDrive command channels and the proxy tooling described above, and review webmail and web servers for the scanning and the SquirrelMail exploitation ESET found ([ESET, 2026-05-20](https://www.welivesecurity.com/en/eset-research/webworm-new-burrowing-techniques/)).

## Correction — 2026-10-21T20:41:34Z

FishMonger (which The Hacker News also calls Aquatic Panda ([The Hacker News, 2026-05-20](https://thehackernews.com/2026/05/webworm-deploys-echocreep-and-graphworm.html))), SixLittleMonkeys and Space Pirates are not other names for Webworm: ESET links Webworm to SixLittleMonkeys and FishMonger as related China-aligned groups ([ESET, 2026-05-20](https://www.welivesecurity.com/en/eset-research/webworm-new-burrowing-techniques/)) and calls the Space Pirates link tenuous at best ([The Hacker News, 2026-05-20](https://thehackernews.com/2026/05/webworm-deploys-echocreep-and-graphworm.html)). EchoCreep does not create its Discord channels: it reports to channels the operators made before it first ran, which suggests they knew their targets or had gathered the details after initial access ([ESET, 2026-05-20](https://www.welivesecurity.com/en/eset-research/webworm-new-burrowing-techniques/)). The S3 bucket was a compromised third-party bucket that has since been taken down, and SharpSecretsdump, which mimics Impacket's secretsdump rather than dumping LSASS memory, was only seen uploaded to it ([ESET, 2026-05-20](https://www.welivesecurity.com/en/eset-research/webworm-new-burrowing-techniques/)).
