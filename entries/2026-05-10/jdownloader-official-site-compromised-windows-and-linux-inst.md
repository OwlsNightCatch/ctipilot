---
schema: 1
kind: threat
horizon: operational
title: "JDownloader official site compromised — Windows and Linux installers swapped for a Python RAT for ~48 hours"
headline: "JDownloader official site compromised — Windows and Linux installers swapped for a Python RAT for ~48 hours"
summary: "The official download page of JDownloader, a German-developed (AppWork GmbH) Java-based download manager popular across European user bases, was compromised between approximately 2026-05-06 and 2026-05-08; attackers replaced the Windows and Linux installers with malicious counterparts (PiunikaWeb, 2026-05-08 · …"
discovered_at: "2026-05-10T05:00:02Z"
event_date: 2026-05-08
run_id: 2026-05-10-001
priority: notable
immediate_action: null
tags:
  - supply-chain
  - infostealer
regions:
  - europe
  - dach
  - global
sectors:
  - technology
entities:
  - "incident:jdownloader-supply-chain-2026"
cves: []
sources:
  - url: "https://piunikaweb.com/2026/05/08/jdownloader-website-hacked-malware/"
    publisher: "PiunikaWeb, 2026-05-08"
    role: primary
  - url: "https://www.cyberkendra.com/2026/05/jdownloader-website-hacked-malicious.html"
    publisher: "CyberKendra, 2026-05-07"
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
migrated_from: briefs/2026-05-10.md
---

The official download page of JDownloader, a German-developed (AppWork GmbH) Java-based download manager popular across European user bases, was compromised between approximately 2026-05-06 and 2026-05-08; attackers replaced the Windows and Linux installers with malicious counterparts ([PiunikaWeb, 2026-05-08](https://piunikaweb.com/2026/05/08/jdownloader-website-hacked-malware/) · [CyberKendra, 2026-05-07](https://www.cyberkendra.com/2026/05/jdownloader-website-hacked-malicious.html)). The intrusion exploited an unpatched access-control flaw in the site's content-management layer, allowing unauthenticated modification of download-link targets without altering the main JAR, the in-app updater, the macOS bundle, or the package-manager distributions (Winget, Flatpak, Snap). Trojanised Windows executables bore forged publisher names — "Zipline LLC", "The Water Team", "Peace Team" — instead of the legitimate AppWork GmbH signature, triggering Windows SmartScreen warnings that helped some users detect the substitution before execution. The substituted installers are described in available reporting as carrying a Python-based remote-access payload; the precise capability description has not been corroborated by a named research lab in this run's window (. The JDownloader team confirmed the breach and have asked users to verify file hashes against the project's published SHA-256 manifest.

ATT&CK mapping: [T1195.002 Supply Chain Compromise: Software Supply Chain](https://attack.mitre.org/techniques/T1195/002/), [T1036.005 Match Legitimate Name](https://attack.mitre.org/techniques/T1036/005/) (forged AppWork-adjacent publisher names), [T1059.006 Python](https://attack.mitre.org/techniques/T1059/006/) for the RAT runtime.

**Defender takeaway:** Audit endpoints — particularly developer / power-user / multimedia-engineering workstations across DACH — for JDownloader installers downloaded between 2026-05-06 and 2026-05-08 from the official site. Hunt for unsigned or non-AppWork-signed `JDownloader*.exe` and unexpected Python interpreters in user-profile paths; alert on Python child processes spawned from `JDownloader*` parent images (Sysmon EID 1 + parent-image filter). Inventory installations are uncertain via Winget / Flatpak / Snap (those distributions were not poisoned in this window) — the trojanised path was specifically the project's web-hosted installer and "Alternative Installer" download links.
