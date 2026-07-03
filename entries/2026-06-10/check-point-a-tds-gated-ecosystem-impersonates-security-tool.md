---
schema: 1
kind: research
horizon: operational
title: "Check Point: a TDS-gated ecosystem impersonates security tools (Ghidra, dnSpy, ILSpy) to deliver SessionGate, RemusStealer and a clipboard hijacker"
headline: "Check Point: a TDS-gated ecosystem impersonates security tools (Ghidra, dnSpy, ILSpy) to deliver SessionGate, RemusStealer and a clipboard hijacker"
summary: "Check Point Research details a malware-distribution operation that impersonates open-source reversing tools using CloudFront-hosted JavaScript to hijack download clicks and route victims through a Traffic Distribution System enforcing geo/device/VPN/frequency filtering before delivering one of three payloads (Check …"
discovered_at: "2026-06-10T05:00:15Z"
event_date: 2026-06-03
run_id: 2026-06-10-c84347b2
priority: notable
immediate_action: null
tags:
  - infostealer
  - phishing
  - cryptocrime
regions:
  - global
sectors:
  - technology
entities:
  - "campaign:tds-security-tool-impersonation-checkpoint"
cves: []
sources:
  - url: "https://research.checkpoint.com/2026/impersonation-click-hijacking-and-tds-inside-a-malware-distribution-ecosystem/"
    publisher: "Check Point Research, 2026-06-03"
    role: primary
closed_sources: []
evidence: []
verification: single-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-10.md
---

Check Point Research details a malware-distribution operation that impersonates open-source reversing tools using CloudFront-hosted JavaScript to hijack download clicks and route victims through a Traffic Distribution System enforcing geo/device/VPN/frequency filtering before delivering one of three payloads ([Check Point Research, 2026-06-03](https://research.checkpoint.com/2026/impersonation-click-hijacking-and-tds-inside-a-malware-distribution-ecosystem/)). The payloads are SessionGate (a per-session multi-stage loader with AES-encrypted modules), RemusStealer (targeting 20+ browsers, 220+ wallet extensions, 77 password-manager extensions and 18 2FA tools), and AnimateClipper (a clipboard hijacker with on-chain C2). The targeting is notable for this audience: it goes after security researchers and developers searching for trusted tools, bypassing standard phishing-awareness training (T1566, T1204, T1555, T1111). Hunt for `ghidra`/`dnspy`/`ilspy` download-then-execute chains under browser child processes and clipboard-API access from unexpected processes. [SINGLE-SOURCE] (Check Point primary research).
