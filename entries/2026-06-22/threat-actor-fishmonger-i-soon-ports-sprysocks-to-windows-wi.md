---
schema: 1
kind: research
horizon: strategic
weekly_section: weekly-research
title: "Threat actor: FishMonger (I-SOON) ports SprySOCKS to Windows with a kernel-mode rootkit"
headline: "Threat actor: FishMonger (I-SOON) ports SprySOCKS to Windows with a kernel-mode rootkit"
summary: "ESET's full research paper detailed two previously undocumented Windows variants of the SprySOCKS backdoor attributed to FishMonger (Earth Lusca / Aquatic Panda — the Winnti-contractor tracked as I-SOON), centred on a RawWNPF.sys kernel driver that hides processes (NtQuerySystemInformation hook), network …"
discovered_at: "2026-06-22T00:14:59Z"
event_date: 2026-06-16
run_id: 2026-W25-0aacfe65
priority: notable
immediate_action: null
tags:
  - nation-state
  - espionage
  - china-nexus
regions:
  - global
  - europe
sectors:
  - defense
entities:
  - "actor:webworm-fishmonger-aquatic-panda-eset-echocreep-graphworm-eu"
cves: []
sources:
  - url: "https://www.welivesecurity.com/en/eset-research/fishmongers-arsenal-upgraded-sprysocks-windows/"
    publisher: ESET WeLiveSecurity
    role: primary
  - url: "https://thehackernews.com/2026/06/china-linked-sprysocks-backdoor-expands.html"
    publisher: The Hacker News
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

ESET's full research paper detailed two previously undocumented Windows variants of the SprySOCKS backdoor attributed to **FishMonger** (Earth Lusca / Aquatic Panda — the Winnti-contractor tracked as I-SOON), centred on a `RawWNPF.sys` kernel driver that hides processes (`NtQuerySystemInformation` hook), network connections (`nsiproxy.sys` IOCTL interception), files (minifilter callbacks) and persistence registry keys, and redirects crafted TCP packets to a hidden backdoor port via the Windows Filtering Platform ([ESET, 2026-06-16](https://www.welivesecurity.com/en/eset-research/fishmongers-arsenal-upgraded-sprysocks-windows/); [daily 06-17](/briefs/2026-06-17/)). **Background:** FishMonger has been publicly tracked since the 2024 I-SOON contractor-leak exposed its government-espionage-for-hire model; ESET's earlier work documented the Linux SprySOCKS lineage, and this report extends the toolkit to a Windows kernel rootkit with a possible UEFI-bootkit component (leveraging the patched BlackLotus Secure Boot bypass, CVE-2023-24932). Confirmed victims are government organisations in Honduras, Taiwan, Thailand and Pakistan; the targeting class — government and defence — keeps EU government networks in scope. Enable the vulnerable-driver blocklist, hunt for the named driver and for process/network-hiding behaviours, and verify Secure Boot is at current patch level.
