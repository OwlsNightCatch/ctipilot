---
schema: 1
kind: threat
horizon: operational
title: "Unit 42 Operation FlutterBridge: notarized macOS backdoor hides its logic in a remote WebView and exfiltrates documents through an \"AI summarise\" feature"
headline: "Unit 42 Operation FlutterBridge: notarized macOS backdoor hides its logic in a remote WebView and exfiltrates documents through an \"AI summarise\" feature"
summary: "Unit 42 details Operation FlutterBridge, the evolution of cluster CL-CRI-1089 (active since August 2025), which distributes macOS backdoors disguised as productivity apps (PodcastsLounge, PDF-Brain, PDF-Ninja) via hundreds of Google Ads bought through verified shell companies (Unit 42, 2026-06-02; The Hacker News …"
discovered_at: "2026-06-05T05:00:02Z"
event_date: 2026-06-04
run_id: 2026-06-05-2c6574c4
priority: notable
immediate_action: null
tags:
  - organized-crime
  - infostealer
  - phishing
regions:
  - global
  - europe
sectors:
  - technology
entities: []
cves: []
sources:
  - url: "https://unit42.paloaltonetworks.com/flutterbridge-new-fluttershell-backdoor/"
    publisher: "Unit 42, 2026-06-02"
    role: primary
  - url: "https://thehackernews.com/2026/06/fluttershell-backdoor-spreads-to-macos.html"
    publisher: "The Hacker News, 2026-06-04"
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
migrated_from: briefs/2026-06-05.md
---

Unit 42 details **Operation FlutterBridge**, the evolution of cluster CL-CRI-1089 (active since August 2025), which distributes macOS backdoors disguised as productivity apps (PodcastsLounge, PDF-Brain, PDF-Ninja) via hundreds of Google Ads bought through verified shell companies ([Unit 42, 2026-06-02](https://unit42.paloaltonetworks.com/flutterbridge-new-fluttershell-backdoor/); [The Hacker News, 2026-06-04](https://thehackernews.com/2026/06/fluttershell-backdoor-spreads-to-macos.html)). Every sample was signed with a valid Apple Developer ID and **passed notarization**, with zero VirusTotal detections at analysis time — Gatekeeper does not catch these. The **FlutterShell** payload keeps its malicious logic on an attacker-controlled website and uses a Flutter JavaScript-to-native bridge to translate JSON commands into native macOS calls, so capability changes need no new binary. Confirmed behaviour: arbitrary shell execution, file read/write, environment-variable theft, Chrome hijacking via the "Secure Preferences" file, and document exfiltration routed through the attacker's server under the guise of an AI document-summarisation feature. Targeting is global with explicit emphasis on Western Europe, including **France and Germany**.

**Why it matters to us:** notarization-bypassed, Developer-ID-signed macOS malware defeats the controls most teams lean on for Mac fleets. The reliable detection layer is behavioural: macOS endpoint telemetry for apps that instantiate a `WKWebView` with a custom JS message handler that then spawns shell processes, non-browser writes to Chrome's Secure Preferences, and outbound connections from "productivity" apps to CDN-fronted infrastructure.
