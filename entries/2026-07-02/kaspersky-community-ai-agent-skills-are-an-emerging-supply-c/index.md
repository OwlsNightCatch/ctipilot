---
schema: 1
kind: research
title: "Kaspersky: community AI-agent \"skills\" are an emerging supply-chain surface — OpenClaw marketplace still distributing malicious skills"
headline: "Kaspersky: community AI-agent \"skills\" are an emerging supply-chain surface — OpenClaw marketplace still distributing malicious skills"
summary: "Kaspersky published fresh detection telemetry (through mid-June 2026) on OpenClaw, an AI-agent framework whose agents load \"skills\" — plaintext SKILL.md natural-language instruction files, some with embedded code — from a community marketplace (\"ClawHub\"), typically running with file-system access and the …"
discovered_at: "2026-07-02T04:55:24Z"
event_date: 2026-07-01
run_id: 2026-07-02-6551f8c2
priority: notable
immediate_action: null
tags:
  - ai-abuse
  - supply-chain
  - identity
regions:
  - global
sectors:
  - technology
entities: []
cves: []
sources:
  - url: "https://securelist.com/openclaw-security/120484/"
    publisher: Kaspersky Securelist
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
migrated_from: briefs/2026-07-02.md
---

Kaspersky published fresh detection telemetry (through mid-June 2026) on OpenClaw, an AI-agent framework whose agents load "skills" — plaintext `SKILL.md` natural-language instruction files, some with embedded code — from a community marketplace ("ClawHub"), typically running with file-system access and the tokens/keys of the systems each skill touches ([Kaspersky Securelist, 2026-07-01](https://securelist.com/openclaw-security/120484/)). Because building a malicious skill needs no custom-malware development, Kaspersky frames skill distribution as a supply-chain-attack analogue with an even lower bar than package-repository attacks: prior to 7 February 2026 no skills underwent any security check, and an April scan of the hub found 24 accounts distributing 600+ malicious skills, with OSINT indicating 1,100+ malicious accounts created since January. Although the marketplace has since added pre-publication scanning, Kaspersky's June detection statistics show malicious-skill activity continuing on customer endpoints. **Defender takeaway:** treat `SKILL.md` ingestion as an untrusted-code-execution surface — log and alert on file-system access and outbound network calls from AI-agent processes to non-allow-listed hosts, watch for plaintext credential/token files co-located with agent skill directories, require pre-execution scanning plus least-privilege sandboxing before any community skill runs against production credentials, and set an explicit enterprise AI-usage policy barring unreviewed third-party skill installation. Single-source (Kaspersky); no independent corroboration located this run.
