---
schema: 1
kind: vulnerability
horizon: operational
title: "Nightmare/Chaotic Eclipse zero-day wave — the Defender LPE now carries a CVE, a public PoC, and Microsoft's \"Exploitation More Likely\" rating, with no patch"
headline: "Nightmare/Chaotic Eclipse zero-day wave — the Defender LPE now carries a CVE, a public PoC, and Microsoft's \"Exploitation More Likely\" rating, with no patch"
summary: "ESET detailed GentleKiller, an operator-maintained EDR-killer framework run centrally by the Gentlemen RaaS gang — eight BYOVD driver variants against 400+ security processes across 48 product families, with confirmed Western-European targeting (ESET, 2026-06-18). Microsoft's Defender LPE zero-day from the Nightmare Eclipse wave now carries a CVE (CVE-2026-50656) with a public PoC and no patch."
discovered_at: "2026-06-19T05:21:00Z"
event_date: 2026-06-17
run_id: 2026-06-19-c306b105
priority: high
immediate_action: null
tags:
  - vulnerabilities
  - zero-day
  - lpe
  - priv-esc
  - poc-public
  - no-patch
regions:
  - global
sectors:
  - public-sector
entities:
  - "trend:nightmare-eclipse-rogueplanet-defender-toctou-lpe-2026-06"
  - "actor:nightmare-eclipse"
cves:
  - id: CVE-2026-50656
    cvss: "7.8"
    epss: null
    type: lpe
    vector: local
    auth: post-auth
    status:
      - poc-public
      - no-patch
sources:
  - url: "https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-50656"
    publisher: Microsoft MSRC
    role: primary
  - url: "https://www.helpnetsecurity.com/2026/06/17/rogueplanet-zero-day-cve-2026-50656/"
    publisher: Help Net Security
    role: corroborating
  - url: "https://thehackernews.com/2026/06/microsoft-confirms-rogueplanet-defender_02022423645.html"
    publisher: The Hacker News
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
actions:
  - "**Compensate for the unpatched Defender LPE (CVE-2026-50656)** (§ 4). No patch exists — monitor for `MsMpEng.exe` spawning `cmd.exe`/`powershell.exe` as SYSTEM (Sysmon EID 1 parent-image filter, WEL 4688) and constrain which low-privilege accounts can trigger on-demand scans."
migrated_from: briefs/2026-06-19.md
---

**UPDATE (originally covered in the 2026-W24 weekly summary):** The serialised Windows zero-day campaign tracked as Nightmare/Chaotic Eclipse has a new, formally-identified entry: *RoguePlanet*, the local elevation-of-privilege flaw in the Microsoft Malware Protection Engine (`mpengine.dll`, used by Defender on all supported Windows 10/11), is now assigned **CVE-2026-50656**, acknowledged by Microsoft, and rated *Exploitation More Likely* on the MSRC Exploitability Index ([Microsoft MSRC, 2026-06-16](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-50656); [Help Net Security, 2026-06-17](https://www.helpnetsecurity.com/2026/06/17/rogueplanet-zero-day-cve-2026-50656/)).

The exploit abuses a TOCTOU race: during a scan Defender resolves a file path and later reopens it for analysis, and the PoC swaps in a malicious file in that window to obtain a SYSTEM shell. It requires only local low-privilege access, needs no user interaction, and the researcher states it functions regardless of whether real-time protection is enabled — though the race makes it non-deterministic ("hit or miss") ([The Hacker News, 2026-06-17](https://thehackernews.com/2026/06/microsoft-confirms-rogueplanet-defender_02022423645.html)). As of 2026-06-18 Microsoft states a fix is in development with no timeline; the public PoC is the in-window delta.
