---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-long-running
title: "Chaotic Eclipse / Nightmare Eclipse — MiniPlasma confirmed SYSTEM on a fully-patched Windows 11; sixth zero-day in six weeks"
headline: "Chaotic Eclipse / Nightmare Eclipse — MiniPlasma confirmed SYSTEM on a fully-patched Windows 11; sixth zero-day in six weeks"
summary: "The Windows zero-day cluster carried a material technical update beyond the 2026-05-30 daily. MiniPlasma — the sixth zero-day the \"Chaotic Eclipse\" researcher has dropped in six weeks — is a local privilege escalation in the Windows Cloud Filter driver (cldflt.sys) that reuses CVE-2020-17103, the researcher …"
discovered_at: "2026-05-25T05:00:23Z"
event_date: null
run_id: 2026-W22-da77963d
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - zero-day
  - lpe
  - no-patch
  - poc-public
regions:
  - global
sectors: []
entities:
  - "campaign:nightmare-eclipse-microsoft-dcu-threat-greenplasma-miniplasmaaac"
cves:
  - id: CVE-2020-17103
    cvss: n/a
    epss: null
    type: lpe
    vector: local
    auth: post-auth
    status:
      - poc-public
      - no-patch
sources:
  - url: "https://www.bleepingcomputer.com/news/microsoft/new-windows-miniplasma-zero-day-exploit-gives-system-access-poc-released/"
    publisher: BleepingComputer — MiniPlasma zero-day PoC
    role: primary
  - url: "https://www.threatlocker.com/blog/miniplasma-windows-privilege-escalation-zero-day-affects-fully-patched-systems"
    publisher: ThreatLocker — exploitation on fully-patched systems
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
migrated_from: briefs/weekly/2026-W22.md
---

The Windows zero-day cluster carried a material technical update beyond the 2026-05-30 daily. **MiniPlasma** — the sixth zero-day the "Chaotic Eclipse" researcher has dropped in six weeks — is a local privilege escalation in the Windows Cloud Filter driver (`cldflt.sys`) that reuses **CVE-2020-17103**, the researcher claiming the 2020 patch was incomplete or partially reverted. **ThreatLocker independently confirmed MiniPlasma achieves SYSTEM on a fully-patched Windows 11 running the May 2026 cumulative update** — i.e. there is no configuration that closes it today. Three earlier drops in the series (BlueHammer, RedSun, UnDefend) have been observed in real attacks. Microsoft's DCU has called the uncoordinated releases "never justifiable" but has shipped no out-of-band fix; **June 10 Patch Tuesday is the first fix opportunity** (. Until then, treat any `cldflt.sys`-adjacent LPE as live.
