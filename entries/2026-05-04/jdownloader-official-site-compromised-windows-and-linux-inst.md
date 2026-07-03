---
schema: 1
kind: incident
horizon: strategic
weekly_section: weekly-incidents-recap
title: "JDownloader official site compromised — Windows and Linux installers swapped for ~48 hours"
headline: "JDownloader official site compromised — Windows and Linux installers swapped for ~48 hours"
summary: "The official download page of JDownloader (German-developed AppWork GmbH, Java-based download manager popular across European user bases) was compromised between approximately 2026-05-06 and 2026-05-08; attackers exploited an unpatched access-control flaw in the site's CMS layer to replace Windows and Linux installer …"
discovered_at: "2026-05-04T05:00:22Z"
event_date: 2026-05-10
run_id: 2026-W19-a5788b22
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
    publisher: PiunikaWeb — JDownloader compromised
    role: primary
  - url: "https://www.cyberkendra.com/2026/05/jdownloader-website-hacked-malicious.html"
    publisher: CyberKendra — JDownloader malicious installers
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
migrated_from: briefs/weekly/2026-W19.md
---

The official download page of JDownloader (German-developed AppWork GmbH, Java-based download manager popular across European user bases) was compromised between approximately 2026-05-06 and 2026-05-08; attackers exploited an unpatched access-control flaw in the site's CMS layer to replace Windows and Linux installer download links without altering the main JAR, the in-app updater, the macOS bundle, or the package-manager distributions (Winget, Flatpak, Snap). Trojanised Windows executables bore forged publisher names — "Zipline LLC", "The Water Team", "Peace Team" — triggering Windows SmartScreen warnings that helped some users detect the substitution. The substituted installers carry a Python-based remote-access payload; a more specific capability description has not been corroborated by a named research lab in available reporting. The JDownloader team confirmed and asked users to verify file hashes against the project's published SHA-256 manifest ([PiunikaWeb, 2026-05-08](https://piunikaweb.com/2026/05/08/jdownloader-website-hacked-malware/) · [CyberKendra, 2026-05-07](https://www.cyberkendra.com/2026/05/jdownloader-website-hacked-malicious.html) · [daily 2026-05-10](/briefs/2026-05-10/)). **Defender takeaway:** audit developer / power-user / multimedia-engineering workstations across DACH for JDownloader installers downloaded between 2026-05-06 and 2026-05-08 from the official site or "Alternative Installer" link; hunt for unsigned / non-AppWork-signed `JDownloader*.exe`, unexpected Python interpreters in user-profile paths, and Python child processes spawned from JDownloader parent images.
