---
schema: 1
kind: threat
title: Mustang Panda abuses Zoho WorkDrive as a dead-drop C2 channel (ZOHOMURK) against government and energy targets
headline: Mustang Panda abuses Zoho WorkDrive as a dead-drop C2 channel (ZOHOMURK) against government and energy targets
summary: "Acronis Threat Research Unit documented two coordinated June 12–22 campaigns by China-aligned Mustang Panda (also tracked TA416 / HIVE0154 / BRONZE PRESIDENT) against Indian government bodies and hydropower-sector entities (Acronis TRU, 2026-06-29 · The Hacker News, 2026-06-29)."
discovered_at: "2026-06-30T05:10:34Z"
event_date: 2026-06-29
run_id: 2026-06-30-9aaa1114
priority: notable
immediate_action: null
tags:
  - espionage
  - nation-state
  - china-nexus
  - cloud
regions:
  - apac
  - europe
sectors:
  - public-sector
  - energy
entities: []
cves: []
sources:
  - url: "https://www.acronis.com/en/tru/posts/mustang-panda-targets-indias-government-and-energy-sectors/"
    publisher: Acronis Threat Research Unit
    role: primary
  - url: "https://thehackernews.com/2026/06/mustang-panda-uses-zoho-workdrive-as.html"
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

Acronis Threat Research Unit documented two coordinated June 12–22 campaigns by China-aligned Mustang Panda (also tracked TA416 / HIVE0154 / BRONZE PRESIDENT) against Indian government bodies and hydropower-sector entities ([Acronis TRU, 2026-06-29](https://www.acronis.com/en/tru/posts/mustang-panda-targets-indias-government-and-energy-sectors/) · [The Hacker News, 2026-06-29](https://thehackernews.com/2026/06/mustang-panda-uses-zoho-workdrive-as.html)). Initial access is spear-phishing with ZIP-delivered lures (a hydropower cooperation proposal; an India–Taiwan memorandum of understanding). The toolkit introduces SHARDLOADER (DLL side-loading through a legitimate Solid PDF Creator / Citrix Receiver binary, loading shellcode from fragmented files to defeat static scanning — `T1574.002`), MINIRECON (a reworked Toneshell variant beaconing over `wss://`), and ZOHOMURK, which carries hardcoded Zoho OAuth credentials to drive an attacker-controlled WorkDrive account as a dead-drop resolver (`T1102.001`) — reading operator commands from an "inbox" folder and writing exfiltrated output to an "outbox", blending all C2 with legitimate `workdrive.zoho.com` API traffic.

**Why it matters to us:** Abusing a legitimate SaaS platform's API for C2 defeats egress controls that allowlist well-known cloud providers — the traffic blends with sanctioned `workdrive.zoho.com` calls. EU public-sector SOCs should extend CASB/DLP allowlisting to less-obvious SaaS such as Zoho WorkDrive and alert on OAuth token grants for cloud apps that are not sanctioned business tools.
