---
schema: 1
kind: vulnerability
horizon: operational
title: "Nightmare Eclipse / Chaotic Eclipse — Microsoft's Digital Crimes Unit threatens criminal action; GreenPlasma and MiniPlasma (cldflt.sys SYSTEM escalation) remain unpatched; researcher announces July 14 drop"
headline: "Nightmare Eclipse / Chaotic Eclipse — Microsoft's Digital Crimes Unit threatens criminal action; GreenPlasma and MiniPlasma (cldflt.sys SYSTEM escalation)"
summary: "UPDATE (originally covered 2026-W21): Microsoft's Digital Crimes Unit issued a formal public statement on 28–29 May 2026 calling uncoordinated zero-day releases \"never justifiable\" and warning its DCU would \"continue bringing cases against these actors and those that enable their criminal activity\" (The Record …"
discovered_at: "2026-05-30T05:00:11Z"
event_date: 2026-05-29
run_id: 2026-05-30-aca445cc
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - zero-day
  - lpe
  - no-patch
regions:
  - global
sectors: []
entities:
  - "campaign:nightmare-eclipse-microsoft-dcu-threat-greenplasma-miniplasmaaac"
  - "actor:nightmare-eclipse"
cves:
  - id: CVE-2026-45585
    cvss: n/a
    epss: null
    type: lpe
    vector: local
    auth: post-auth
    status:
      - poc-public
      - no-patch
sources:
  - url: "https://therecord.media/microsoft-calls-zero-day-releases-never-justifiable-as-researcher-threatens-more"
    publisher: The Record
    role: primary
  - url: "https://www.heise.de/en/news/Too-many-zero-days-Microsoft-threatens-legal-action-11310736.html"
    publisher: heise Security
    role: corroborating
  - url: "https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45585"
    publisher: Microsoft MSRC
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
migrated_from: briefs/2026-05-30.md
---

**UPDATE (originally covered 2026-W21):** Microsoft's Digital Crimes Unit issued a formal public statement on 28–29 May 2026 calling uncoordinated zero-day releases "never justifiable" and warning its DCU would "continue bringing cases against these actors and those that enable their criminal activity" ([The Record, 2026-05-29](https://therecord.media/microsoft-calls-zero-day-releases-never-justifiable-as-researcher-threatens-more)). The pseudonymous researcher Nightmare Eclipse / Chaotic Eclipse responded by threatening a new vulnerability release on 14 July 2026 (the next Patch Tuesday).

Of the six Windows vulnerabilities the researcher has released since early April: BlueHammer (CVE-2026-33825), UnDefend (CVE-2026-45498), and RedSun (CVE-2026-41091) are patched and saw confirmed in-the-wild exploitation following PoC publication. YellowKey (CVE-2026-45585 — BitLocker bypass via Windows Recovery Environment, requiring physical access), GreenPlasma (LPE class), and MiniPlasma remain unpatched as of 30 May 2026. MiniPlasma specifically abuses the Windows Cloud Files Mini Filter Driver (`cldflt.sys`) to achieve a SYSTEM shell from a standard user session on fully-patched Windows 11; the root cause is assessed as an incomplete remediation of CVE-2020-17103 (no CVE yet assigned to MiniPlasma itself).

The July 14 release deadline should be treated as a hard date for resolving any outstanding Windows LPE chain gaps. Defenders on Windows 11 estates should monitor for `cldflt.sys`-related anomalies and consider AppLocker/WDAC policies blocking unsigned executables from low-privileged user sessions while patches are pending. Next Patch Tuesday: 10 June 2026.
