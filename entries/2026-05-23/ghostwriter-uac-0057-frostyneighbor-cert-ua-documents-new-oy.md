---
schema: 1
kind: threat
horizon: operational
title: "Ghostwriter / UAC-0057 / FrostyNeighbor — CERT-UA documents new OYSTERFRESH → OYSTERBLUES → OYSTERSHUCK implant chain via Prometheus learning-platform lures"
headline: "Ghostwriter / UAC-0057 / FrostyNeighbor — CERT-UA documents new OYSTERFRESH → OYSTERBLUES → OYSTERSHUCK implant chain via Prometheus learning-platform lures"
summary: "UPDATE (originally covered weekly 2026-W21): CERT-UA published a bulletin (surfaced 2026-05-22) on a spring-2026 phishing campaign by Ghostwriter (a.k.a."
discovered_at: "2026-05-23T05:00:11Z"
event_date: 2026-05-22
run_id: 2026-05-23-852c21c8
priority: notable
immediate_action: null
tags:
  - nation-state
  - espionage
  - phishing
  - russia-nexus
regions:
  - europe
sectors:
  - public-sector
  - defense
  - education
entities: []
cves: []
sources:
  - url: "https://thehackernews.com/2026/05/ghostwriter-targets-ukraine-government.html"
    publisher: The Hacker News
    role: primary
  - url: "https://www.scworld.com/brief/belarus-linked-ghostwriter-group-targets-ukraine-using-prometheus-learning-platform-lures"
    publisher: SC World
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: "migration: update target unresolved (no originally-covered date in v2 body)"
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-23.md
---

**UPDATE (originally covered weekly 2026-W21):** CERT-UA published a bulletin (surfaced 2026-05-22) on a spring-2026 phishing campaign by **Ghostwriter** (a.k.a. UAC-0057, UNC1151, FrostyNeighbor) targeting Ukrainian government entities through lures themed on the Prometheus online-learning platform ([The Hacker News, 2026-05-22](https://thehackernews.com/2026/05/ghostwriter-targets-ukraine-government.html) · [SC World, 2026-05-22](https://www.scworld.com/brief/belarus-linked-ghostwriter-group-targets-ukraine-using-prometheus-learning-platform-lures)). The material delta from this week's weekly long-running coverage of FrostyNeighbor / Ghostwriter activity is a **new three-stage implant trio** distinct from the prior PicassoLoader toolset.

Chain: phishing email from a compromised account → PDF attachment with a link to a ZIP archive → ZIP carrying a JavaScript file (**OYSTERFRESH**). OYSTERFRESH renders a decoy document as cover while writing an obfuscated, RC4-encrypted **OYSTERBLUES** payload to the Windows Registry and launching **OYSTERSHUCK**. OYSTERSHUCK decodes OYSTERBLUES (executed via JavaScript) which then collects computer name, user account, OS version, last boot time and running process list, exfiltrates via HTTP POST to C2, and executes dynamically received JavaScript via `eval()`. The final payload is assessed as Cobalt Strike. *(MITRE ATT&CK overlay added by this brief, not by the CERT-UA narrative as carried by The Hacker News: T1027 Obfuscated Files/Information on the OYSTERFRESH stage, T1547.001 Registry Run Keys on the OYSTERBLUES persistence, T1059.007 JavaScript on OYSTERSHUCK execution, T1219 Remote Access Software on the Cobalt Strike final.)*

Defender vantage: CERT-UA's own recommendation is to **block `wscript.exe` execution for standard user accounts** — a high-yield control because the OYSTER* trio relies on script-host execution from user context. EDR signal: `wscript.exe` spawning `powershell.exe` or a base64-encoded command; registry monitoring for new `HKCU\Software` Run-key values containing binary blobs or script paths; hunt for Cobalt Strike beacon signatures in HTTP POST egress to non-corporate domains. The EU/CH relevance is direct: Ghostwriter historically targets Belgium, Germany, Poland, Lithuania, Latvia and other NATO members alongside Ukraine, and the OYSTER* implant chain is a toolset upgrade defenders should expect to see surfaced in EU government tenants and Eastern-Europe-focused think tanks.
