---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-long-running
title: "Chaotic Eclipse / Nightmare Eclipse zero-day wave — RoguePlanet (CVE-2026-50656) still unpatched, PoC works on June builds"
headline: "Chaotic Eclipse / Nightmare Eclipse zero-day wave — RoguePlanet (CVE-2026-50656) still unpatched, PoC works on June builds"
summary: "key: item:nightmare-chaotic-eclipse-zero-day-wave-the-defender-lpe-now. The serialised Windows zero-day campaign the W24 weekly consolidated has a worsening status."
discovered_at: "2026-06-22T00:15:04Z"
event_date: 2026-06-17
run_id: 2026-W25-0aacfe65
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - zero-day
  - lpe
  - poc-public
  - no-patch
regions:
  - global
sectors:
  - technology
entities:
  - "campaign:nightmare-eclipse-microsoft-dcu-threat-greenplasma-miniplasmaaac"
  - "trend:nightmare-eclipse-rogueplanet-defender-toctou-lpe-2026-06"
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
  - url: "https://www.helpnetsecurity.com/2026/06/17/rogueplanet-zero-day-cve-2026-50656/"
    publisher: Help Net Security
    role: primary
  - url: "https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-50656"
    publisher: Microsoft MSRC
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
migrated_from: briefs/weekly/2026-W25.md
---

`key: item:nightmare-chaotic-eclipse-zero-day-wave-the-defender-lpe-now`. The serialised Windows zero-day campaign the W24 weekly consolidated has a worsening status. As of 2026-06-21, **CVE-2026-50656 (RoguePlanet) remains unpatched.** The exploit abuses a Time-of-Check-to-Time-of-Use race in Microsoft Defender's file-processing workflow (CWE-59): Defender checks a file path under SYSTEM, then reopens it, and the exploit swaps the file in the gap to get SYSTEM-level execution ([Help Net Security, 2026-06-17](https://www.helpnetsecurity.com/2026/06/17/rogueplanet-zero-day-cve-2026-50656/); [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-50656); [daily 06-19](/briefs/2026-06-19/)). The PoC is validated against fully-patched Windows 10 and 11 including the June 2026 Patch Tuesday build, Real-Time Protection status is irrelevant, and the researcher states small PoC changes defeat mitigations — "the only thing you can realistically do is wait for a patch." Microsoft confirms a fix is in development with no timeline. This is post-initial-access privilege escalation (local auth required), so it compounds rather than initiates a breach; until a patch ships, the realistic controls are application allowlisting to constrain post-exploitation and hunting for `MsMpEng.exe` spawning unexpected children or temp-directory symlink manipulation timed to scans. Outstanding question to watch: whether Microsoft ships an out-of-band fix or holds it to July Patch Tuesday.
