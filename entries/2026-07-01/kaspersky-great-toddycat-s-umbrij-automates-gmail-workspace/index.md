---
schema: 1
kind: research
title: "Kaspersky GReAT: ToddyCat's \"Umbrij\" automates Gmail/Workspace OAuth-token theft via Chromium remote-debugging abuse"
headline: "Kaspersky GReAT: ToddyCat's \"Umbrij\" automates Gmail/Workspace OAuth-token theft via Chromium remote-debugging abuse"
summary: "Kaspersky GReAT documented Umbrij, a .NET tool used by the ToddyCat APT that automates theft of Google Workspace OAuth tokens through a technique GReAT calls Shadow Token via Remote Debug (STRD) (Kaspersky Securelist, 2026-06-30)."
discovered_at: "2026-07-01T04:41:18Z"
event_date: 2026-06-30
run_id: 2026-07-01-af9e697d
priority: notable
immediate_action: null
tags:
  - espionage
  - identity
  - cloud
  - china-nexus
regions:
  - global
sectors:
  - public-sector
  - defense
entities:
  - "tool:toddycat-umbrij-oauth-token-theft-strd"
cves: []
sources:
  - url: "https://securelist.com/toddycat-apt-umbrij-tool-and-oauth/120251/"
    publisher: Kaspersky Securelist / GReAT
    role: primary
closed_sources: []
evidence: []
verification: single-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-07-01.md
---

Kaspersky GReAT documented **Umbrij**, a .NET tool used by the ToddyCat APT that automates theft of Google Workspace OAuth tokens through a technique GReAT calls **Shadow Token via Remote Debug (STRD)** ([Kaspersky Securelist, 2026-06-30](https://securelist.com/toddycat-apt-umbrij-tool-and-oauth/120251/)). Umbrij copies the victim's existing Chromium profile (cached credentials, session cookies), relaunches the browser headless with the DevTools remote-debugging port enabled, and drives it via Puppeteer Sharp to silently replay a legitimate OAuth authorization-code flow against Google APIs — extracting the authorization code with no user interaction, then exchanging it server-side for access/refresh tokens. The requested scopes include `https://mail.google.com/` and `https://www.googleapis.com/auth/gmail.insert`. Prerequisites are on-host code execution plus an already-authenticated Gmail/Workspace browser session; no separate phishing step. Umbrij loads via DLL search-order hijacking (`T1574.001`) through signed legitimate binaries — `BDSubWiz.exe` (a Bitdefender ConnectAgent component, loading `log.dll`), `VSTestVideoRecorder.exe` (a Visual Studio testing tool), and the discontinued `GoogleDesktop.exe` (loading `GoogleServices.dll`). Because it operates inside a standard browser-automation framework rather than touching credential stores directly, it evades detection tuned to credential-store access; Securelist maps the access-token stages to `T1550.001` (Use Application Access Token) and `T1134.003` (Access Token Manipulation: Make and Impersonate Token). **[SINGLE-SOURCE]** — Kaspersky is the sole publisher. Detection concepts: alert on Chromium/Edge launched with `--remote-debugging-port` (and `--headless`) from non-browser parents such as `BDSubWiz.exe`, `VSTestVideoRecorder.exe` or `GoogleDesktop.exe`; watch Workspace admin logs for OAuth token issuance to unexpected client IDs. Hardening: enforce Chrome Enterprise `DeveloperToolsAvailability=Disabled` where remote debugging isn't needed, and review OAuth app grants.
