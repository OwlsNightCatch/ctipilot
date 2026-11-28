---
schema: 1
kind: research
title: "OP-512: China-linked cluster runs a cryptographically-unique, self-reporting IIS web-shell framework against legacy .NET servers"
headline: "OP-512: China-linked cluster runs a cryptographically-unique, self-reporting IIS web-shell framework against legacy .NET servers"
summary: "ReliaQuest documented OP-512, a previously-unreported China-linked espionage cluster targeting internet-facing Microsoft IIS servers running end-of-life .NET Framework 4.0 (ReliaQuest, 2026-06-05) [SINGLE-SOURCE — ReliaQuest original disclosure]."
discovered_at: "2026-06-06T05:00:05Z"
event_date: 2026-06-05
run_id: 2026-06-06-d01b95fe
priority: notable
immediate_action: null
tags:
  - espionage
  - nation-state
  - china-nexus
regions:
  - global
  - europe
sectors:
  - public-sector
entities:
  - "actor:op-512"
cves: []
sources:
  - url: "https://reliaquest.com/blog/threat-spotlight-reliaquests-agentic-ai-uncovers-new-china-linked-cluster-op-512"
    publisher: ReliaQuest — OP-512 threat spotlight
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
actions:
  - "**Hunt legacy IIS / .NET 4.0 servers for OP-512 behaviourally, not by timestamp** (. Look for `w3wp.exe` issuing long hex-string DNS subdomain queries and spawning `cmd`/`powershell`/`csc`; isolate or retire EOL .NET 4.0 hosts."
migrated_from: briefs/2026-06-06.md
---

ReliaQuest documented **OP-512**, a previously-unreported China-linked espionage cluster targeting internet-facing Microsoft IIS servers running end-of-life .NET Framework 4.0 ([ReliaQuest, 2026-06-05](https://reliaquest.com/blog/threat-spotlight-reliaquests-agentic-ai-uncovers-new-china-linked-cluster-op-512)) `[SINGLE-SOURCE — ReliaQuest original disclosure]`. The framework is a three-component web shell — one `.aspx` file manager plus two `.ashx` command handlers — that is **per-deployment cryptographically unique** (RSA signatures and RC4 keys differ per installation), defeating signature-based detection. It carries a timestomping module that matches shell file timestamps to surrounding legitimate IIS artefacts (`T1070.006` Timestomp), uses reflective .NET assembly loading to bypass static scanning (`T1620`), and implements a novel self-reporting beacon: the deployed shell's URL is hex-encoded into a DNS subdomain query issued from `w3wp.exe`, so the operator is notified of a live shell without actively scanning for it. ReliaQuest found initial access roughly **75 days** before the shell was deployed, consistent with patient espionage tradecraft, and notes overlap with the hex-encoded-DNS technique seen in CL-STA-0048 while assessing OP-512 as a separate cluster.

**Why it matters to us:** Many Swiss and EU public-sector estates still run legacy IIS/ASP.NET portals and intranet apps on .NET 4.0 — exactly OP-512's stated footprint. The detection lesson is concrete: filesystem timestamps are useless for triage here (timestomped), so hunt on behaviour instead — `w3wp.exe` issuing long hex-string DNS subdomain queries, `w3wp.exe` spawning `cmd.exe`/`powershell.exe`/`csc.exe` (Sysmon EID 1), reflective-assembly loads, and `.aspx`/`.ashx` writes into web roots (Windows Security EID 4663 on `inetsrv` paths). Hardening: isolate or retire .NET 4.0 servers and apply WDAC/AppLocker to block execution of unsigned web-root artefacts.
