---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-top-stories
title: "Windows BitLocker \"YellowKey\" + CTFMON \"GreenPlasma\" — public PoC, no patch, TPM-only BitLocker bypassed"
headline: "Windows BitLocker \"YellowKey\" + CTFMON \"GreenPlasma\" — public PoC, no patch, TPM-only BitLocker bypassed"
summary: "Windows BitLocker \"YellowKey\" and CTFMON \"GreenPlasma\" zero-days — public PoC, no patch, TPM-only BitLocker configurations bypassed. Microsoft May Patch Tuesday (120+ CVEs) did not address either; the BitLocker primitive defeats the most common laptop full-disk-encryption configuration in Swiss federal and cantonal estates. (daily 2026-05-15)"
discovered_at: "2026-05-11T05:00:03Z"
event_date: 2026-05-15
run_id: 2026-W20-71c96b25
priority: high
immediate_action: null
tags:
  - vulnerabilities
  - zero-day
  - lpe
  - no-patch
  - poc-public
regions:
  - global
sectors:
  - public-sector
entities: []
cves: []
sources:
  - url: "https://www.bleepingcomputer.com/news/security/windows-bitlocker-zero-day-gives-access-to-protected-drives-poc-released/"
    publisher: BleepingComputer — Windows BitLocker zero-day PoC
    role: primary
  - url: "https://security-hub.ncsc.admin.ch/#/posts/12574"
    publisher: "NCSC.ch Security Hub #12574"
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
migrated_from: briefs/weekly/2026-W20.md
---

**If you did nothing this week:** every Windows endpoint configured with TPM-only BitLocker (no PIN, no startup key — the most common laptop configuration in Swiss federal and cantonal estates) is bypassable by an attacker with brief physical access using the publicly-disclosed YellowKey PoC; every Windows endpoint with the CTFMON service (the default on Windows 10/11/Server 2022/2025) is locally elevation-of-privilege-vulnerable via the GreenPlasma primitive. Both zero-days were disclosed without coordinated vendor patching; Microsoft's May 2026 Patch Tuesday (120+ CVEs) did **not** address either, and no out-of-band advisory has been issued ([daily 2026-05-15](/briefs/2026-05-15/)).

The operational reality for Swiss public-sector defenders is that the laptop full-disk-encryption story is materially weakened until Microsoft ships a fix. The interim guidance is to enforce BitLocker PIN-or-startup-key on every endpoint where physical-access risk is non-trivial (mobile estates, off-site work, hotel travel) — the GPO toggle is `Computer Configuration → Administrative Templates → Windows Components → BitLocker Drive Encryption → Operating System Drives → Require additional authentication at startup`. For GreenPlasma the only available control is privileged-account-segregation discipline: workstations that handle administrative credentials should not also run unprivileged user workloads where the local-EOP can be staged.
