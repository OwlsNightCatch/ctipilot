---
schema: 1
kind: research
title: "Island: \"BadBlocker\" — an 11M-user Chrome ad-blocker is one server config change away from arbitrary JavaScript on any site"
headline: "Island: \"BadBlocker\" — an 11M-user Chrome ad-blocker is one server config change away from arbitrary JavaScript on any site"
summary: "Island researchers documented (2026-06-25) a dormant but architecturally complete arbitrary-JavaScript-execution capability in \"Adblock for YouTube\" (11M+ installs) (Island, 2026-06-25; The Hacker News, 2026-06-25)."
discovered_at: "2026-06-28T05:05:43Z"
event_date: 2026-06-25
run_id: 2026-06-28-1b30612a
priority: notable
immediate_action: null
tags:
  - supply-chain
  - data-breach
  - identity
regions:
  - global
  - europe
sectors:
  - finance
  - public-sector
entities:
  - "campaign:island-badblocker-adblock-youtube-extension"
cves: []
sources:
  - url: "https://www.island.io/blog/badblocker-11-million-users-one-server-call-away-from-compromise"
    publisher: Island
    role: primary
  - url: "https://thehackernews.com/2026/06/chrome-ad-blocker-with-10m-installs.html"
    publisher: The Hacker News
    role: corroborating
closed_sources: []
evidence:
  - quote: "The extension contains the architectural ingredients for arbitrary JavaScript execution on any website, activated by a single server-side configuration change, without an extension update, without a store review, and without any visible sign that something has changed."
    publisher: Island
  - quote: "If server passes 'script' as element type with JavaScript content, code runs in page context with access to sensitive data"
    publisher: Island
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
migrated_from: briefs/2026-06-28.md
---

Island researchers documented (2026-06-25) a dormant but architecturally complete arbitrary-JavaScript-execution capability in "Adblock for YouTube" (11M+ installs) ([Island, 2026-06-25](https://www.island.io/blog/badblocker-11-million-users-one-server-call-away-from-compromise); [The Hacker News, 2026-06-25](https://thehackernews.com/2026/06/chrome-ad-blocker-with-10m-installs.html)). The extension fetches config every 24 hours; a server-controlled `scriptletsRules` field can activate a "create-element" scriptlet that appends an externally-sourced `<script>` to the DOM via a TrustedTypes policy that bypasses the browser's own script-injection guard. Because the extension declares `<all_urls>` host permissions but only checks whether the string `youtube.com` appears *anywhere* in the URL (not as the hostname), a lure such as `https://bank.example.com/search?q=youtube.com` passes the check — so an injected script could run in authenticated banking, admin-panel or enterprise-SaaS sessions with full DOM and credential access (`T1176` Browser Extensions; `T1056` Input Capture). Island demonstrated a Salesforce-data-exfiltration PoC; no malicious payload was live at analysis time, but sister extensions were previously removed by Google for actual malware. Defender concepts: flag browser extensions making config-fetch HTTPS requests outside their declared purpose; audit `<all_urls>` extensions against business need; enforce extension allowlisting via browser management policy.
