---
schema: 1
kind: threat
title: "LLMShare malvertising campaign: attackers embed fake outage pages in ChatGPT share links and serve infostealer downloads via Google Ads"
headline: "LLMShare malvertising campaign: attackers embed fake outage pages in ChatGPT share links and serve infostealer downloads via Google Ads"
summary: "Push Security documented LLMShare, a malvertising campaign in which attackers buy Google Ads targeting \"ChatGPT\" and \"ChatGPT download\" queries (Push Security, 2026-05-29; BleepingComputer, 2026-05-29)."
discovered_at: "2026-05-30T05:00:03Z"
event_date: 2026-05-29
run_id: 2026-05-30-aca445cc
priority: notable
immediate_action: null
tags:
  - infostealer
  - phishing
  - ai-abuse
regions:
  - global
sectors:
  - technology
entities:
  - "campaign:llmshare-malvertising-chatgpt-share-links-infostealer-google"
cves: []
sources:
  - url: "https://pushsecurity.com/blog/llmshare-malvertising-campaign"
    publisher: Push Security
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/chatgpt-share-links-abused-to-host-fake-outage-pages-to-deliver-malware/"
    publisher: BleepingComputer
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

Push Security documented LLMShare, a malvertising campaign in which attackers buy Google Ads targeting "ChatGPT" and "ChatGPT download" queries ([Push Security, 2026-05-29](https://pushsecurity.com/blog/llmshare-malvertising-campaign); [BleepingComputer, 2026-05-29](https://www.bleepingcomputer.com/news/security/chatgpt-share-links-abused-to-host-fake-outage-pages-to-deliver-malware/)). Victims clicking the ads land on legitimate `chatgpt.com/s/[unique-id]` share URLs that render attacker-controlled HTML — a fake high-traffic outage page with a "Download our desktop app to continue" button — directly from the OpenAI domain. Because `chatgpt.com` is trusted by enterprise web-filtering rules and firewalls, the landing page is not blocked. The download button redirects to an attacker-controlled domain impersonating OpenAI; the site uses cloaking (serves a benign page to scanners). Windows users receive an infostealer payload. The technique exploits the same ChatGPT Artifacts/sharing feature previously abused in the ACR Stealer campaign (covered 2026-05-26) and extends it to malvertising. Detection: monitor for browser-spawned executable downloads from chatgpt.com domains — legitimate ChatGPT desktop app downloads do not originate from that path; alert on unusual process launch from browser-extracted or browser-downloaded unsigned executables. MITRE ATT&CK: T1566.002, T1204.001, T1036, T1027.
