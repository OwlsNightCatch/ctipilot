---
schema: 1
kind: vulnerability
title: "MiniPlasma: Chaotic Eclipse PoC turns the 2020 Windows Cloud Files driver flaw CVE-2020-17103 into a SYSTEM shell on patched Windows 11; June 2026 updates fix it"
headline: "MiniPlasma revived Windows Cloud Files flaw CVE-2020-17103 for a SYSTEM shell; Microsoft's June 2026 updates fix it"
summary: "The researcher Chaotic Eclipse (also Nightmare Eclipse) released MiniPlasma on 2026-05-17, an exploit for the HsmOsBlockPlaceholderAccess routine of the Windows Cloud Files Mini Filter Driver (cldflt.sys), the flaw Google Project Zero reported in 2020 as CVE-2020-17103, which opened a SYSTEM command prompt from a standard user on Windows 11 with the May 2026 updates; BleepingComputer and Will Dormann reproduced it. Microsoft re-released CVE-2020-17103 on 2026-06-09 and recommends the June 2026 Windows updates to address MiniPlasma; it scores the flaw CVSS 3.1 7.0 and lists it as not exploited."
discovered_at: "2026-05-19T05:00:09Z"
event_date: 2026-05-17
run_id: 2026-05-19-2505c918
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - zero-day
  - lpe
  - poc-public
  - patch-available
regions:
  - global
sectors:
  - technology
entities:
  - "campaign:nightmare-eclipse-microsoft-dcu-threat-greenplasma-miniplasmaaac"
  - "actor:nightmare-eclipse"
techniques: [T1068, T1112]
affected_products: ["Microsoft Windows"]
cves:
  - id: CVE-2020-17103
    cvss: "7.0 (CVSS 3.1, Microsoft)"
    epss: null
    type: lpe
    vector: local
    auth: post-auth
    status:
      - poc-public
      - patch-available
    affected: "Windows Cloud Files Mini Filter Driver (cldflt.sys) on Windows without the June 2026 updates; reproduced on Windows 11 with the May 2026 updates"
    fixed: "June 2026 Windows security updates (CVE-2020-17103 re-released on 2026-06-09)"
sources:
  - url: "https://www.bleepingcomputer.com/news/microsoft/new-windows-miniplasma-zero-day-exploit-gives-system-access-poc-released/"
    publisher: BleepingComputer
    date: "2026-05-17"
    role: primary
  - url: "https://thehackernews.com/2026/05/miniplasma-windows-0-day-enables-system.html"
    publisher: The Hacker News
    date: "2026-05-18"
    role: corroborating
  - url: "https://msrc.microsoft.com/update-guide/vulnerability/CVE-2020-17103"
    publisher: "Microsoft MSRC"
    date: "2026-06-09"
    role: primary
closed_sources: []
evidence:
  - quote: "BleepingComputer tested the exploit on a fully patched Windows 11 Pro system running the latest May 2026 Patch Tuesday updates."
    publisher: BleepingComputer
    source_url: "https://www.bleepingcomputer.com/news/microsoft/new-windows-miniplasma-zero-day-exploit-gives-system-access-poc-released/"
  - quote: "Forshaw's original report said that the flaw could allow arbitrary registry keys to be created in the .DEFAULT user hive without proper access checks, potentially enabling privilege escalation."
    publisher: BleepingComputer
    source_url: "https://www.bleepingcomputer.com/news/microsoft/new-windows-miniplasma-zero-day-exploit-gives-system-access-poc-released/"
  - quote: "To comprehensively address the vulnerability identified by CVE-2020-17103 and recently publicly referred to as \"Mini-Plasma\" Microsoft recommends installing the June 2026 updates for your Windows operating systems."
    publisher: Microsoft MSRC
    source_url: "https://msrc.microsoft.com/update-guide/vulnerability/CVE-2020-17103"
verification: multi-source
sourcing_note: >
  BleepingComputer tested the exploit itself and Will Dormann reproduced it independently, The Hacker News adds the researcher's own statements, and
  Microsoft's update guide is the vendor's record of the score and of the June 2026 fix.
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-19.md
updates:
  - at: "2026-10-21T20:37:19Z"
    run_id: 2026-10-21T1148Z-audit
    type: correction
    summary: >
      Microsoft scores CVE-2020-17103 CVSS 3.1 7.0, not 7.8, and re-released it on 2026-06-09 with the
      June 2026 Windows updates as the fix for MiniPlasma, so the flaw is patched rather than unpatched.
      BleepingComputer tested the exploit itself on Windows 11 Pro with the May 2026 updates, and Will
      Dormann separately confirmed it on the latest public Windows 11. MiniPlasma follows BlueHammer,
      RedSun, UnDefend, YellowKey and GreenPlasma in the researcher's 2026 series rather than being its
      third proof of concept, and the monitoring advice is ThreatLocker's two registry paths.
    fields: [affected_products, body, classification, cves, event_date, evidence, headline, sectors, sources, sourcing_note, summary, tags, techniques, title]
---

Chaotic Eclipse, also known as Nightmare Eclipse, released source code and a compiled exploit for MiniPlasma on GitHub, saying that the flaw James Forshaw of Google Project Zero reported in September 2020 in the HsmOsBlockPlaceholderAccess routine of the Cloud Filter driver cldflt.sys, assigned CVE-2020-17103 and reportedly fixed in December 2020, was still present and that Google's original proof of concept worked unchanged ([BleepingComputer, 2026-05-17](https://www.bleepingcomputer.com/news/microsoft/new-windows-miniplasma-zero-day-exploit-gives-system-access-poc-released/)). The exploit appears to abuse how the driver handles registry key creation through the undocumented CfAbortHydration API, which Forshaw's report said could create arbitrary registry keys in the .DEFAULT user hive without proper access checks ([BleepingComputer, 2026-05-17](https://www.bleepingcomputer.com/news/microsoft/new-windows-miniplasma-zero-day-exploit-gives-system-access-poc-released/)). BleepingComputer, using a standard user account on a fully patched Windows 11 Pro system with the May 2026 updates, got a command prompt with SYSTEM privileges, and Will Dormann confirmed the exploit on the latest public Windows 11 but not on the latest Insider Preview Canary build ([BleepingComputer, 2026-05-17](https://www.bleepingcomputer.com/news/microsoft/new-windows-miniplasma-zero-day-exploit-gives-system-access-poc-released/)); the researcher says success may vary because it is a race condition and that all Windows versions are likely affected ([The Hacker News, 2026-05-18](https://thehackernews.com/2026/05/miniplasma-windows-0-day-enables-system.html)).

Microsoft re-released CVE-2020-17103 on 2026-06-09 to comprehensively address the flaw "recently publicly referred to as 'Mini-Plasma'" and recommends installing the June 2026 Windows updates; it rates it Important with a CVSS 3.1 base score of 7.0 and lists it as not exploited ([Microsoft MSRC, CVE-2020-17103](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2020-17103)). MiniPlasma is the latest in a 2026 series from the same researcher after BlueHammer, RedSun and the UnDefend tool, all three of which were later seen exploited in attacks, and the YellowKey and GreenPlasma exploits ([BleepingComputer, 2026-05-17](https://www.bleepingcomputer.com/news/microsoft/new-windows-miniplasma-zero-day-exploit-gives-system-access-poc-released/)).

**Exposure:** Windows systems without the June 2026 updates on which an attacker can already run code as a standard user ([Microsoft MSRC, CVE-2020-17103](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2020-17103); [BleepingComputer, 2026-05-17](https://www.bleepingcomputer.com/news/microsoft/new-windows-miniplasma-zero-day-exploit-gives-system-access-poc-released/)).

**Detection:** in registry telemetry, creation or modification of keys under \Registry\User\Software\Policies\Microsoft\CloudFiles\BlockedApps and \Registry\User\.DEFAULT\Volatile Environment, the paths ThreatLocker advises monitoring for this exploit ([BleepingComputer, 2026-05-17](https://www.bleepingcomputer.com/news/microsoft/new-windows-miniplasma-zero-day-exploit-gives-system-access-poc-released/)), especially by a standard user's process that is followed by a SYSTEM command prompt.

**Defender takeaway:** install the June 2026 Windows updates, the fix Microsoft names for MiniPlasma ([Microsoft MSRC, CVE-2020-17103](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2020-17103)); on a host still without them, a standard-user foothold is one public exploit away from SYSTEM ([BleepingComputer, 2026-05-17](https://www.bleepingcomputer.com/news/microsoft/new-windows-miniplasma-zero-day-exploit-gives-system-access-poc-released/)).

## Correction — 2026-10-21T20:37:19Z

Microsoft rates CVE-2020-17103 at CVSS 3.1 7.0, not 7.8, and re-released it on 2026-06-09, recommending the June 2026 Windows updates to comprehensively address the flaw now called Mini-Plasma, so it is no longer unpatched ([Microsoft MSRC, CVE-2020-17103](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2020-17103)). The reproduction on fully patched Windows 11 Pro with the May 2026 updates was BleepingComputer's own test with a standard user account, and Will Dormann confirmed it separately on the latest public Windows 11 ([BleepingComputer, 2026-05-17](https://www.bleepingcomputer.com/news/microsoft/new-windows-miniplasma-zero-day-exploit-gives-system-access-poc-released/)). MiniPlasma is not the third proof of concept in the series: BlueHammer, RedSun and UnDefend came first, followed by YellowKey and GreenPlasma ([BleepingComputer, 2026-05-17](https://www.bleepingcomputer.com/news/microsoft/new-windows-miniplasma-zero-day-exploit-gives-system-access-poc-released/)). The monitoring the reporting gives is ThreatLocker's pair of registry paths; no source advises driver-load monitoring or says that disabling Cloud Files or OneDrive integration removes the attack surface ([BleepingComputer, 2026-05-17](https://www.bleepingcomputer.com/news/microsoft/new-windows-miniplasma-zero-day-exploit-gives-system-access-poc-released/)).
