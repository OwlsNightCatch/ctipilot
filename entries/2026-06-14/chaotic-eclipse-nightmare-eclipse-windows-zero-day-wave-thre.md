---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-multi-day
title: "Chaotic Eclipse / Nightmare Eclipse Windows zero-day wave — three long-tracked bugs patched, a fourth still open"
headline: "Chaotic Eclipse / Nightmare Eclipse Windows zero-day wave — three long-tracked bugs patched, a fourth still open"
summary: "June Patch Tuesday was the largest ever (198 CVEs) and finally closed the long-tracked Chaotic Eclipse zero-days (YellowKey, GreenPlasma, MiniPlasma) — but a fourth, GreatXML, remains unpatched, and an HTTP.sys pre-auth RCE (CVE-2026-47291, CVSS 9.8) headlines the release. (daily 06-10, daily 06-12, BleepingComputer)"
discovered_at: "2026-06-14T23:57:20Z"
event_date: null
run_id: 2026-W24-bd5a7519
priority: high
immediate_action: null
tags:
  - vulnerabilities
  - zero-day
  - lpe
  - poc-public
regions:
  - global
sectors: []
entities:
  - "campaign:nightmare-eclipse-microsoft-dcu-threat-greenplasma-miniplasmaaac"
  - "trend:nightmare-eclipse-rogueplanet-defender-toctou-lpe-2026-06"
  - "trend:greatxml-bitlocker-bypass-2026"
  - "actor:nightmare-eclipse"
cves: []
sources:
  - url: "https://www.bleepingcomputer.com/news/microsoft/microsoft-june-2026-patch-tuesday-fixes-6-zero-days-200-flaws/"
    publisher: BleepingComputer — June Patch Tuesday
    role: primary
  - url: "https://www.securityweek.com/greatxml-zero-day-exploit-bypasses-bitlocker/"
    publisher: SecurityWeek — GreatXML
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: "migration: CVE fields incomplete in v2 footer (CVE-2026-45585, CVE-2026-45586, CVE-2020-17103)"
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/weekly/2026-W24.md
---

This researcher's serialised zero-day disclosures have run across four weekly cycles, and this week brought both resolution and a fresh open wound. June Patch Tuesday (9 June) finally closed the three bugs the W20–W22 weeklies tracked as "expected fix in June": **YellowKey** (CVE-2026-45585, BitLocker bypass via the Windows Recovery Environment, physical access required), **GreenPlasma** (CVE-2026-45586, CTFMON elevation to SYSTEM), and **MiniPlasma** (a re-opened regression of CVE-2020-17103 in the Cloud Filter driver `cldflt.sys`), per the patch-day round-ups ([BleepingComputer](https://www.bleepingcomputer.com/news/microsoft/microsoft-june-2026-patch-tuesday-fixes-6-zero-days-200-flaws/); [Tenable](https://www.tenable.com/blog/microsofts-june-2026-patch-tuesday-addresses-198-cves-cve-2026-49160-cve-2026-50507)).

But the cadence continued the same day. On 9 June the researcher published **RoguePlanet**, a TOCTOU race in the Microsoft Defender scan engine yielding a SYSTEM shell — hours after the patches landed, with no CVE and no fix ([BleepingComputer](https://www.bleepingcomputer.com/news/microsoft/microsoft-defender-rogueplanet-zero-day-grants-system-privileges/); [daily 06-11](/briefs/2026-06-11/)). Two days later came **GreatXML**, a BitLocker bypass via crafted XML on the recovery partition — PoC public, practical severity contested, still unpatched ([SecurityWeek](https://www.securityweek.com/greatxml-zero-day-exploit-bypasses-bitlocker/); [daily 06-12](/briefs/2026-06-12/)). The trajectory: deploy the June cumulative update to close the three patched bugs, retain BitLocker PIN/TPM policy regardless, and keep monitoring MSRC — the fourth disclosure is the pattern, not the exception.
