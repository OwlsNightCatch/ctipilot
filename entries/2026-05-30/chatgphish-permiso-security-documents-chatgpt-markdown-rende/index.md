---
schema: 1
kind: research
title: "ChatGPhish: Permiso Security documents ChatGPT Markdown renderer trusting third-party image URLs and links — used for IP exfiltration and phishing via legitimate chatgpt.com"
headline: "ChatGPhish: Permiso Security documents ChatGPT Markdown renderer trusting third-party image URLs and links — used for IP exfiltration and phishing via"
summary: "Permiso Security's P0 Labs (researcher Andi Ahmeti) disclosed on 29 May 2026 that ChatGPT's web summarisation feature unconditionally trusts and renders Markdown image URLs and links extracted from third-party pages, executing them inside the trusted chatgpt.com UI (Permiso Security P0 Labs, 2026-05-29; The Hacker …"
discovered_at: "2026-05-30T05:00:09Z"
event_date: 2026-05-29
run_id: 2026-05-30-aca445cc
priority: notable
immediate_action: null
tags:
  - ai-abuse
  - phishing
  - info-disclosure
regions:
  - global
sectors:
  - technology
entities:
  - "campaign:chatgphish-chatgpt-markdown-rendering-flaw-permiso-security"
cves: []
sources:
  - url: "https://permiso.io/blog/chatgpt-markdown-rendering-vulnerability"
    publisher: Permiso Security P0 Labs
    role: primary
  - url: "https://thehackernews.com/2026/05/chatgphish-vulnerability-turns-chatgpt.html"
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

Permiso Security's P0 Labs (researcher Andi Ahmeti) disclosed on 29 May 2026 that ChatGPT's web summarisation feature unconditionally trusts and renders Markdown image URLs and links extracted from third-party pages, executing them inside the trusted `chatgpt.com` UI ([Permiso Security P0 Labs, 2026-05-29](https://permiso.io/blog/chatgpt-markdown-rendering-vulnerability); [The Hacker News, 2026-05-29](https://thehackernews.com/2026/05/chatgphish-vulnerability-turns-chatgpt.html)). An attacker embedding a small Markdown payload on any web page (GitHub README, SaaS dashboard, documentation portal) triggers the attack when a victim asks ChatGPT to summarise the page: the payload executes silently and can exfiltrate the victim's IP, User-Agent, and Referer via attacker-hosted image fetch; render malicious links styled as ChatGPT output; inject fake security alerts; and serve QR codes from attacker-controlled S3 buckets that bypass desktop URL filters by moving the click action to mobile. Permiso submitted to OpenAI via Bugcrowd on 29 April; after follow-up on 7 May, OpenAI marked it as not reproducible then as not applicable, without resolution. No CVE assigned. Defenders using ChatGPT for document summarisation in enterprise workflows should: restrict ChatGPT access to internal documentation portals; educate users that any AI-summarised third-party page can carry attacker instructions embedded in rendered output.
