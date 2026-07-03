---
schema: 1
kind: threat
horizon: operational
title: GREYVIBE — newly documented Russia-nexus cluster deploys five parallel attack chains against Ukraine with AI-generated lures and two PowerShell RATs
headline: GREYVIBE — newly documented Russia-nexus cluster deploys five parallel attack chains against Ukraine with AI-generated lures and two PowerShell RATs
summary: "WithSecure Labs disclosed GREYVIBE on 28–29 May 2026, a previously-unnamed Russia-nexus threat cluster active since at least August 2025, targeting Ukrainian military, government, civilians, and businesses (WithSecure Labs, 2026-05-29; SecurityWeek, 2026-05-28)."
discovered_at: "2026-05-30T05:00:02Z"
event_date: 2026-05-29
run_id: 2026-05-30-aca445cc
priority: notable
immediate_action: null
tags:
  - nation-state
  - espionage
  - russia-nexus
  - ai-abuse
  - phishing
regions:
  - europe
  - global
sectors:
  - public-sector
  - defense
entities:
  - "actor:greyvibe-russia-nexus-ai-assisted-five-parallel-ukraine-attack"
cves: []
sources:
  - url: "https://labs.withsecure.com/publications/greyvibe"
    publisher: WithSecure Labs
    role: primary
  - url: "https://www.securityweek.com/russia-linked-greyvibe-attackers-use-ai-to-supercharge-cyberattacks/"
    publisher: SecurityWeek
    role: corroborating
  - url: "https://thehackernews.com/2026/05/new-russian-linked-greyvibe-targets.html"
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
migrated_from: briefs/2026-05-30.md
---

WithSecure Labs disclosed GREYVIBE on 28–29 May 2026, a previously-unnamed Russia-nexus threat cluster active since at least August 2025, targeting Ukrainian military, government, civilians, and businesses ([WithSecure Labs, 2026-05-29](https://labs.withsecure.com/publications/greyvibe); [SecurityWeek, 2026-05-28](https://www.securityweek.com/russia-linked-greyvibe-attackers-use-ai-to-supercharge-cyberattacks/)). Five parallel attack chains: PhantomMail (spear-phishing with ZIP/RAR archives via Google Drive and 4sync), PhantomClick (fake CAPTCHA/ClickFix pages impersonating Zoom and LAPAS), PrincessClub (fraudulent adult-club sites with WebRTC-based social engineering), DroneLink (counterfeit Ukrainian Armed Forces charity sites), and Nebo (fake Russian military login portals). Core malware: LegionRelay (PowerShell RAT with file theft, screenshots, credential harvesting, RDP access; RC4 C2 comms), PhantomRelay (PowerShell RAT with dynamic script loading and watchdog persistence), and FallSpy (Android spyware for contact, call log, and geolocation extraction). Four custom obfuscators — LOOKVALPS, LOOKVALJS, DAYLIGHT, TEASOUP — were assessed as LLM-assisted developments. Attribution evidence: Russian-language panels and code comments; C2 servers in UTC+3 (Moscow time); OPSEC failures including public scan-platform uploads. WithSecure identifies possible links to UAC-0098 (former TrickBot associates). MITRE ATT&CK: T1566.001/T1566.002, T1059.001, T1005, T1204.001, T1133. Detection: alert on PowerShell spawned from archive-extraction utility parent processes; hunt scheduled tasks created by PowerShell beaconing to dynamic DNS; Android MDM alerts on sideloaded APKs accessing mic/camera. Organisations supporting Ukrainian government or civil-society counterparts are within the targeting scope.
