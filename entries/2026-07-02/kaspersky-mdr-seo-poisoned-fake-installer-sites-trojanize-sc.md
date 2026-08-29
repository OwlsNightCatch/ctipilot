---
schema: 1
kind: research
title: "Kaspersky MDR: SEO-poisoned fake-installer sites trojanize ScreenConnect to deploy AsyncRAT"
headline: "Kaspersky MDR: SEO-poisoned fake-installer sites trojanize ScreenConnect to deploy AsyncRAT"
summary: "Kaspersky's MDR team pivoted from a single flagged incident (suspicious PowerShell/VBS spawned by a ScreenConnect process) into a \"massive, multi-domain, multi-language\" campaign running since at least August 2025, using 90+ spoofed sites in ten languages — including German and French — impersonating free software …"
discovered_at: "2026-07-02T04:55:23Z"
event_date: 2026-07-01
run_id: 2026-07-02-6551f8c2
priority: notable
immediate_action: null
tags:
  - infostealer
  - phishing
  - supply-chain
regions:
  - global
sectors:
  - technology
entities:
  - "campaign:screenconnect-asyncrat-seo-poisoning"
cves: []
sources:
  - url: "https://securelist.com/tr/the-soc-files-screenconnect-campaign-with-asyncrat/120472/"
    publisher: Kaspersky Securelist
    role: primary
  - url: "https://thehackernews.com/2026/07/seo-poisoned-software-sites-abuse.html"
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
migrated_from: briefs/2026-07-02.md
---

Kaspersky's MDR team pivoted from a single flagged incident (suspicious PowerShell/VBS spawned by a ScreenConnect process) into a "massive, multi-domain, multi-language" campaign running since at least August 2025, using 90+ spoofed sites in ten languages — including German and French — impersonating free software such as OBS Studio, DNS Jumper and Bandicam ([Kaspersky Securelist, 2026-07-01](https://securelist.com/tr/the-soc-files-screenconnect-campaign-with-asyncrat/120472/)). Each malicious installer bundles a legitimate Microsoft-signed `install.exe` alongside a rogue `install.res.1033.dll` sideloaded via classic DLL search-order abuse; ScreenConnect deploys as an "Access-type" service, then a PowerShell script adds Defender path exclusions for all local drives and `C:\Users\Public`, disables the UAC consent prompt, and a chained VBScript reconstructs a .NET payload (XOR key `0xA7`) that reflectively loads and process-hollows (T1055.012) into a suspended `RegAsm.exe` acting as the AsyncRAT container, with a two-minute scheduled-task re-trigger for persistence ([The Hacker News, 2026-07-01](https://thehackernews.com/2026/07/seo-poisoned-software-sites-abuse.html)). **Detection/hardening:** flag ScreenConnect service creation with an explicit relay parameter where the deploying process is a freshly-downloaded installer; alert on Defender exclusions covering full drive roots or `C:\Users\Public` added via PowerShell rather than GPO/MDM; treat long-lived `RegAsm.exe` with active network connections as a process-hollowing tell; block DLL sideloading via WDAC/AppLocker on signed binaries' unsigned companion DLLs.
