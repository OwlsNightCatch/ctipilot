---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-multi-day
title: "Windows \"Chaotic Eclipse\" zero-day proliferation — YellowKey, GreenPlasma, MiniPlasma"
headline: "Windows \"Chaotic Eclipse\" zero-day proliferation — YellowKey, GreenPlasma, MiniPlasma"
summary: "The researcher cluster \"Chaotic Eclipse\" / \"Nightmare Eclipse\" continued releasing unpatched Windows LPE/bypass PoCs across the window. On 2026-05-19 a third PoC — MiniPlasma — landed, targeting the cldflt.sys CfAbortHydration path and claiming a re-exploitable regression of the 2020-era CVE-2020-17103."
discovered_at: "2026-05-18T05:00:06Z"
event_date: 2026-05-20
run_id: 2026-W21-473d6fa5
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - lpe
  - priv-esc
  - poc-public
  - no-patch
regions:
  - global
sectors:
  - public-sector
entities:
  - "campaign:nightmare-eclipse-microsoft-dcu-threat-greenplasma-miniplasmaaac"
  - "actor:nightmare-eclipse"
cves:
  - id: CVE-2026-45585
    cvss: n
    epss: null
    type: lpe
    vector: local
    auth: post-auth
    status:
      - poc-public
      - no-patch
  - id: CVE-2020-17103
    cvss: a
    epss: null
    type: lpe
    vector: local
    auth: post-auth
    status:
      - poc-public
      - no-patch
sources:
  - url: "https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-45585"
    publisher: MSRC — CVE-2026-45585
    role: primary
  - url: "https://www.bleepingcomputer.com/news/microsoft/new-windows-miniplasma-zero-day-exploit-gives-system-access-poc-released/"
    publisher: BleepingComputer — MiniPlasma PoC
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
migrated_from: briefs/weekly/2026-W21.md
---

The researcher cluster "Chaotic Eclipse" / "Nightmare Eclipse" continued releasing unpatched Windows LPE/bypass PoCs across the window. On [2026-05-19](/briefs/2026-05-19/) a third PoC — *MiniPlasma* — landed, targeting the `cldflt.sys` `CfAbortHydration` path and claiming a re-exploitable regression of the 2020-era CVE-2020-17103. On [2026-05-20](/briefs/2026-05-20/) Microsoft formally assigned **CVE-2026-45585** to the BitLocker/WinRE bypass (*YellowKey*) disclosed on 2026-05-12 and published a WinRE mitigation — but confirmed there is still no security update for the cluster; the earliest fix window remains the June 2026 Patch Tuesday. Three public PoCs (YellowKey, GreenPlasma, MiniPlasma) now exist against the Windows-centric desktop estates standard in CH/EU federal and cantonal administrations. Until a patch ships, enforce BitLocker PIN/Network-Unlock GPOs and AppLocker/WDAC rules on `ctfmon.exe` injection paths, and segregate privileged accounts from the workstation tier.
