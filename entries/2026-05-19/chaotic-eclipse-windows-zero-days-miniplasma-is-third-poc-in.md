---
schema: 1
kind: vulnerability
title: "Chaotic Eclipse Windows zero-days — MiniPlasma is third PoC in series; cldflt.sys CfAbortHydration path, claimed re-exploitable CVE-2020-17103 regression"
headline: "Chaotic Eclipse Windows zero-days — MiniPlasma is third PoC in series; cldflt.sys CfAbortHydration path, claimed re-exploitable CVE-2020-17103 regression"
summary: "UPDATE (originally covered 2026-05-15): Researcher \"Chaotic Eclipse\" / \"Nightmare Eclipse\" released a third unpatched Windows LPE PoC on 2026-05-17 — MiniPlasma — extending the YellowKey and GreenPlasma series covered in the 2026-05-15 daily (BleepingComputer, 2026-05-17; The Hacker News, 2026-05-18)."
discovered_at: "2026-05-19T05:00:09Z"
event_date: 2026-05-18
run_id: 2026-05-19-2505c918
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
  - public-sector
entities:
  - "campaign:nightmare-eclipse-microsoft-dcu-threat-greenplasma-miniplasmaaac"
  - "actor:nightmare-eclipse"
cves:
  - id: CVE-2020-17103
    cvss: "7.8"
    epss: null
    type: lpe
    vector: local
    auth: post-auth
    status:
      - poc-public
      - no-patch
sources:
  - url: "https://www.bleepingcomputer.com/news/microsoft/new-windows-miniplasma-zero-day-exploit-gives-system-access-poc-released/"
    publisher: BleepingComputer
    role: primary
  - url: "https://thehackernews.com/2026/05/miniplasma-windows-0-day-enables-system.html"
    publisher: The Hacker News
    role: corroborating
closed_sources: []
evidence:
  - quote: researcher Will Dormann confirmed the exploit works reliably on Windows 11 Pro with the latest May 2026 Patch Tuesday updates
    publisher: BleepingComputer
  - quote: "the flaw impacts the 'cldflt.sys' Cloud Filter driver and its 'HsmOsBlockPlaceholderAccess' routine, which was originally reported to Microsoft by Google Project Zero researcher James Forshaw in September 2020"
    publisher: The Hacker News
verification: multi-source
sourcing_note: "migration: update target unresolved (originally covered 2026-05-15)"
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-19.md
---

**UPDATE (originally covered 2026-05-15):** Researcher "Chaotic Eclipse" / "Nightmare Eclipse" released a third unpatched Windows LPE PoC on 2026-05-17 — *MiniPlasma* — extending the YellowKey and GreenPlasma series covered in the 2026-05-15 daily ([BleepingComputer, 2026-05-17](https://www.bleepingcomputer.com/news/microsoft/new-windows-miniplasma-zero-day-exploit-gives-system-access-poc-released/); [The Hacker News, 2026-05-18](https://thehackernews.com/2026/05/miniplasma-windows-0-day-enables-system.html)). The material new technical detail: MiniPlasma targets the `cldflt.sys` Cloud Filter Mini Filter Driver — specifically the `HsmOsBlockPlaceholderAccess` routine — and abuses the undocumented `CfAbortHydration` API to create arbitrary registry keys in the `.DEFAULT` user hive without proper ACL checks, escalating from standard user to SYSTEM. The flaw was originally reported by Google Project Zero (James Forshaw) in September 2020 and nominally patched in December 2020 as CVE-2020-17103; Chaotic Eclipse asserts the exact same code path remains exploitable on fully-patched Windows 11 with May 2026 cumulative updates applied. Will Dormann independently confirmed the PoC opens a SYSTEM `cmd.exe` reliably on Windows 11 Pro fully patched. The exploit reportedly fails on the latest Insider Preview Canary builds, suggesting Microsoft has a fix in the pipeline but has not yet released an out-of-band patch. ThreatLocker published two registry-path hunt pivots: `\Registry\User\Software\Policies\Microsoft\CloudFiles\BlockedApps*` and `\Registry\User\.DEFAULT\Volatile Environment*`.

Defender takeaway: the proliferation of unpatched LPEs from one researcher signals an extended period of `SYSTEM`-shell availability for any attacker that lands user-level execution on Windows endpoints. Sysmon EID 13 (RegistryEvent / SetValue) on the `.DEFAULT` hive from non-`SYSTEM` processes is the primary hunt pivot; Sysmon EID 6 driver-load monitoring catches related driver-abuse paths. Hardening: BitLocker PIN mitigates the companion YellowKey BitLocker bypass; disabling Cloud Files / OneDrive integration removes the MiniPlasma attack surface but is not practical in most environments. MITRE T1068 (Exploitation for Privilege Escalation).
