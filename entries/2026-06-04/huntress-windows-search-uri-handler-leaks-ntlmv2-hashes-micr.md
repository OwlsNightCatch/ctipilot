---
schema: 1
kind: research
horizon: operational
title: "Huntress: Windows search: URI handler leaks NTLMv2 hashes — Microsoft declines to patch"
headline: "Huntress: Windows search: URI handler leaks NTLMv2 hashes — Microsoft declines to patch"
summary: "Huntress detailed an unpatched NTLMv2-leak in the Windows search: protocol handler: a crafted link with a crumb=location: parameter pointing at an attacker UNC path makes Windows open an outbound SMB (TCP 445) connection and expose the user's Net-NTLMv2 challenge-response for offline cracking or relay (Huntress …"
discovered_at: "2026-06-04T05:00:09Z"
event_date: 2026-06-03
run_id: 2026-06-04-51b23ffa
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - identity
  - no-patch
regions:
  - global
sectors:
  - public-sector
entities: []
cves: []
sources:
  - url: "https://www.huntress.com/blog/unpatched-ntlm-leak-windows-search-uri-handler"
    publisher: Huntress Labs
    role: primary
  - url: "https://thehackernews.com/2026/06/unpatched-windows-search-uri.html"
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
migrated_from: briefs/2026-06-04.md
---

Huntress detailed an unpatched NTLMv2-leak in the Windows `search:` protocol handler: a crafted link with a `crumb=location:` parameter pointing at an attacker UNC path makes Windows open an outbound SMB (TCP 445) connection and expose the user's Net-NTLMv2 challenge-response for offline cracking or relay ([Huntress, 2026-06-03](https://www.huntress.com/blog/unpatched-ntlm-leak-windows-search-uri-handler) · [The Hacker News, 2026-06-03](https://thehackernews.com/2026/06/unpatched-windows-search-uri.html)). The bug class is structurally identical to the Snipping Tool `ms-screensketch:` handler leak (CVE-2026-33829) patched in April; Huntress reported the `search:` variant a day later but Microsoft declined a CVE or fix, assessing it as Moderate severity — below the Important/Critical threshold of its servicing bar. Forced-authentication mapping is `T1187`. The single highest-value control neutralises the whole URI-handler leak class: block outbound SMB (TCP 445/139) at host firewall and perimeter for endpoints that don't need external shares, and enable EPA on NTLM-accepting services.
