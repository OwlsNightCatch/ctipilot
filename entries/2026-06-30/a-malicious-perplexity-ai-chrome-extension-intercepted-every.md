---
schema: 1
kind: research
horizon: operational
title: "A malicious \"Perplexity AI\" Chrome extension intercepted every address-bar keystroke via a search-suggest override"
headline: "A malicious \"Perplexity AI\" Chrome extension intercepted every address-bar keystroke via a search-suggest override"
summary: "Microsoft Defender researchers found a malicious Chrome extension (\"Search for perplexity ai\") that abused Chrome's search-settings override API — specifically the suggest_url parameter — to exfiltrate every character typed into the address bar in real time before redirecting to legitimate results (Microsoft …"
discovered_at: "2026-06-30T05:10:40Z"
event_date: 2026-06-30
run_id: 2026-06-30-9aaa1114
priority: notable
immediate_action: null
tags:
  - infostealer
  - identity
regions:
  - global
sectors:
  - technology
entities: []
cves: []
sources:
  - url: "https://www.microsoft.com/en-us/security/blog/2026/06/29/chromium-extension-uses-airelated-branding-redirect-browser-search/"
    publisher: Microsoft Security Blog
    role: primary
  - url: "https://thehackernews.com/2026/06/malicious-perplexity-chrome-extension.html"
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
migrated_from: briefs/2026-06-30.md
---

Microsoft Defender researchers found a malicious Chrome extension ("Search for perplexity ai") that abused Chrome's search-settings override API — specifically the `suggest_url` parameter — to exfiltrate every character typed into the address bar in real time before redirecting to legitimate results ([Microsoft Security Blog, 2026-06-29](https://www.microsoft.com/en-us/security/blog/2026/06/29/chromium-extension-uses-airelated-branding-redirect-browser-search/) · [The Hacker News, 2026-06-30](https://thehackernews.com/2026/06/malicious-perplexity-chrome-extension.html)). It used `declarativeNetRequest` rules for a two-hop redirect: the first hop shipped the query plus live autocomplete keystrokes to attacker infrastructure (server-side Node.js logging full headers, UA, and source IP), the second returned real results so the user noticed nothing. Google pulled the extension after disclosure. It is part of a broader AI-brand-impersonation trend Microsoft is tracking.

**Why it matters to us:** AI-brand impersonation is an easy lure for staff reaching for popular assistant tools. Enforce an enterprise extension allowlist via Group Policy / Intune, and monitor Chromium policy for unexpected changes to `DefaultSearchProviderSuggestURL` on endpoints with access to sensitive systems.
