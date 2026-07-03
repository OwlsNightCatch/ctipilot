---
schema: 1
kind: research
horizon: operational
title: "An autonomous AI agent finds 21 zero-days in FFmpeg for ~$1,000 — nine numbered (CVE-2026-39210 to -39218), parser bugs up to 23 years old"
headline: "An autonomous AI agent finds 21 zero-days in FFmpeg for ~$1,000 — nine numbered (CVE-2026-39210 to -39218), parser bugs up to 23 years old"
summary: "An autonomous AI agent found 21 zero-days in FFmpeg for roughly $1,000, nine already numbered (CVE-2026-39210–39218). The bugs are heap/stack overflows in parsers and demuxers — one dating to 2003 — and FFmpeg is embedded across government media, surveillance and conferencing stacks. PoCs exist; no in-the-wild exploitation (depthfirst, 2026-06-02)."
discovered_at: "2026-06-07T05:00:03Z"
event_date: 2026-06-06
run_id: 2026-06-07-0885f123
priority: high
immediate_action: null
tags:
  - vulnerabilities
  - ai-abuse
  - poc-public
  - patch-available
regions:
  - global
sectors:
  - technology
  - public-sector
entities: []
cves:
  - id: CVE-2026-39210
    cvss: n/a
    epss: null
    type: null
    vector: user-interaction
    auth: pre-auth
    status:
      - poc-public
      - patch-available
  - id: CVE-2026-39211
    cvss: n/a
    epss: null
    type: null
    vector: user-interaction
    auth: pre-auth
    status:
      - poc-public
      - patch-available
  - id: CVE-2026-39212
    cvss: n/a
    epss: null
    type: null
    vector: user-interaction
    auth: pre-auth
    status:
      - poc-public
      - patch-available
  - id: CVE-2026-39213
    cvss: n/a
    epss: null
    type: null
    vector: user-interaction
    auth: pre-auth
    status:
      - poc-public
      - patch-available
  - id: CVE-2026-39214
    cvss: n/a
    epss: null
    type: null
    vector: user-interaction
    auth: pre-auth
    status:
      - poc-public
      - patch-available
  - id: CVE-2026-39215
    cvss: n/a
    epss: null
    type: null
    vector: user-interaction
    auth: pre-auth
    status:
      - poc-public
      - patch-available
  - id: CVE-2026-39216
    cvss: n/a
    epss: null
    type: null
    vector: user-interaction
    auth: pre-auth
    status:
      - poc-public
      - patch-available
  - id: CVE-2026-39217
    cvss: n/a
    epss: null
    type: null
    vector: user-interaction
    auth: pre-auth
    status:
      - poc-public
      - patch-available
  - id: CVE-2026-39218
    cvss: n/a
    epss: null
    type: null
    vector: user-interaction
    auth: pre-auth
    status:
      - poc-public
      - patch-available
sources:
  - url: "https://depthfirst.com/research/21-zero-days-in-ffmpeg"
    publisher: depthfirst — 21 zero-days in FFmpeg
    role: primary
  - url: "https://thehackernews.com/2026/06/ai-agent-uncovers-21-zero-days-in.html"
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
migrated_from: briefs/2026-06-07.md
---

Security startup depthfirst ran an autonomous AI analysis agent over FFmpeg's ~1.5 million lines of C and produced 21 confirmed, reproducible zero-days — each with a proof-of-concept input — for an estimated compute cost of about $1,000 ([depthfirst, 2026-06-02](https://depthfirst.com/research/21-zero-days-in-ffmpeg); [The Hacker News, 2026-06-06](https://thehackernews.com/2026/06/ai-agent-uncovers-21-zero-days-in.html)). Nine carry CVE identifiers (`CVE-2026-39210` through `CVE-2026-39218`); twelve more are fixed but unnumbered. The classes are predominantly heap and stack overflows in parsers and demuxers — the TS (transport-stream) demuxer, VP9 decoder, and the AV1 RTP depacketizer — and several had been latent for 15–20 years, with one service-description-table stack overflow dating to 2003. The AV1-over-RTP overflow is the most operationally pointed because it is network-reachable without special flags, which matters for any service that ingests untrusted RTSP/RTP media. All bugs are fixed upstream; downstream and embedded copies vary.
**Why it matters to us:** Two things for defenders. First, FFmpeg is embedded far beyond the obvious media players — browser stacks, Electron apps, conferencing clients (Teams/Zoom), surveillance/VMS transcoders, and Python wheels — and many ship their own non-auto-updating build, so SBOM/runtime inventory of bundled `libavcodec`/`libavformat` is the most reliable way to find exposure. Prioritise hosts that parse externally-sourced media or accept RTP/RTSP streams, and isolate media-processing services from internal networks. The open verification step for each environment is twofold: confirm whether your distribution has shipped the FFmpeg release carrying the upstream fixes (the fixes are upstream; distro packaging lag varies), and establish whether the network-reachable AV1-over-RTP path is actually exercised by any service you run (for example a WebRTC or RTP media pipeline) rather than assuming the parser is dormant. Second, the $1,000-for-21-bugs cost ratio is a signal that parser-class discovery against widely-embedded C libraries (libpng, zlib, libxml2) is now cheap enough to expect more of — treat embedded-parser memory safety as an accelerating attack surface. Maps to `T1203` (Exploitation for Client Execution).
