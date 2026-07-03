---
schema: 1
kind: threat
horizon: operational
title: "TeamPCP / Mini Shai-Hulud — framework open-sourced, Microsoft PyPI SDK trojanised with a wiper stage, forged Sigstore badges"
headline: "TeamPCP / Mini Shai-Hulud — framework open-sourced, Microsoft PyPI SDK trojanised with a wiper stage, forged Sigstore badges"
summary: "UPDATE (originally covered 2026-05-21, consolidated weekly update): SANS ISC handler Kenneth Hartman documents three material escalations in the TeamPCP / Mini Shai-Hulud supply-chain campaign through 2026-05-24 (SANS Internet Storm Center, 2026-05-25)."
discovered_at: "2026-05-26T05:00:05Z"
event_date: 2026-05-25
run_id: 2026-05-26-ae9d0d4b
priority: notable
immediate_action: null
tags:
  - supply-chain
  - infostealer
  - wiper
  - ai-abuse
regions:
  - global
  - europe
sectors:
  - technology
  - public-sector
entities:
  - "campaign:mini-shai-hulud"
  - "actor:teampcp"
cves: []
sources:
  - url: "https://isc.sans.edu/diary/33016"
    publisher: "SANS Internet Storm Center, 2026-05-25"
    role: primary
  - url: "https://thehackernews.com/2026/05/mini-shai-hulud-pushes-malicious-antv.html"
    publisher: "The Hacker News, 2026-05-19"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: 2026-05-21/teampcp-mini-shai-hulud-campaign-github-itself-breached-3-80
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-26.md
---

**UPDATE (originally covered 2026-05-21, consolidated weekly update):** SANS ISC handler Kenneth Hartman documents three material escalations in the TeamPCP / Mini Shai-Hulud supply-chain campaign through 2026-05-24 ([SANS Internet Storm Center, 2026-05-25](https://isc.sans.edu/diary/33016)). First, the complete TeamPCP framework was published to a public GitHub repository on/around 2026-05-22 — Datadog Security Labs' static analysis (reported by ISC) describes a modular TypeScript/Bun toolkit for credential harvesting, supply-chain poisoning and encrypted exfiltration whose README carries the strings "Love - TeamPCP" and "Change keys and C2 as needed" — and operational copycat forks appeared within hours, commoditising the kit and injecting attribution noise.

Second, an `@antv` npm wave pushed 639 malicious versions across 323 packages, including high-traffic libraries such as `echarts-for-react` (~1.1M weekly downloads) and `size-sensor` (~4.2M weekly downloads); 42 of the packages displayed **forged Sigstore verification badges in the npm UI** ([The Hacker News, 2026-05-19](https://thehackernews.com/2026/05/mini-shai-hulud-pushes-malicious-antv.html)). Read against the campaign's earlier abuse of genuine SLSA Build Level 3 attestations produced by hijacked pipelines, package provenance is now under attack from both directions at once — real attestations from compromised CI and fake badges rendered by the registry UI. Third, three versions of `durabletask` (1.4.1–1.4.3) on PyPI — Microsoft's official Azure Durable Functions SDK — were trojanised, and ISC reports the second-stage payload includes a **Linux disk wiper** ([`T1485`](https://attack.mitre.org/techniques/T1485/)), expanding the campaign's capability from credential theft to data destruction.

Defender takeaway: treat any `echarts-for-react` / `size-sensor` build pulled in the affected window as compromised; **stop treating an npm Sigstore badge or a displayed SLSA attestation as an install-time safety signal** — verify provenance out-of-band against a known-good pipeline. `durabletask` consumers should audit build-runner logs for unexpected outbound connections and destructive disk operations (Sysmon EID 11 for anomalous file-deletion patterns, EID 3 for unexpected `node`/`python` egress from CI workers). Pin exact versions and verify lockfile hashes. The open-sourcing means PBKDF2-salt and dead-drop-string lineage will now also fire on unrelated copycats — behavioural detection on the install-time execution chain is more durable than any static artefact.
