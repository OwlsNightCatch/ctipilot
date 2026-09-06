---
schema: 1
kind: threat
title: "\"The Gentlemen\" ransomware claims 478 victims and adds worm propagation — Switzerland the second-most-targeted European country"
headline: "\"The Gentlemen\" ransomware claims 478 victims and adds worm propagation — Switzerland the second-most-targeted European country"
summary: "\"The Gentlemen\" ransomware: Switzerland is the second-most-targeted European country (Check Point data via Swiss press), against a group profile of 478 claimed victims and an SMB --spread worm capability (inside-it.ch, 2026-06-26)."
discovered_at: "2026-06-27T05:17:50Z"
event_date: 2026-06-26
run_id: 2026-06-27-40e791d4
priority: high
immediate_action: null
tags:
  - ransomware
  - organized-crime
regions:
  - switzerland
  - dach
  - europe
sectors: []
entities:
  - "actor:thegentlemen"
cves: []
sources:
  - url: "https://www.inside-it.ch/aufstrebende-ransomware-bande-findet-mehr-schweizer-opfer-20260626"
    publisher: inside-it.ch
    role: primary
  - url: "https://thehackernews.com/2026/06/the-gentlemen-ransomware-claims-478.html"
    publisher: The Hacker News
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: "migration: update target unresolved (no originally-covered date in v2 body)"
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-27.md
---

**UPDATE (originally covered in the 2026-W25 weekly):** The fresh in-window signal on The Gentlemen ransomware operation is geographic: Swiss tech press, citing Check Point Research, reports Switzerland as the second-most-targeted European country (after Germany) for the group ([inside-it.ch, 2026-06-26](https://www.inside-it.ch/aufstrebende-ransomware-bande-findet-mehr-schweizer-opfer-20260626)).

The group's established profile — detailed earlier this month — is 478 claimed victims and a `--spread` command-line argument enabling self-propagation across Windows networks via SMB share enumeration and credential reuse ([The Hacker News, 2026-06-11](https://thehackernews.com/2026/06/the-gentlemen-ransomware-claims-478.html)). Combined with the previously reported GentleKiller BYOVD EDR-killer, the Swiss-targeting signal means a foothold in one Swiss organisation can spread laterally without further operator action; defenders should enforce SMB signing, restrict admin shares, apply the Microsoft vulnerable-driver blocklist, and alert on a `--spread` argument in ransomware process trees.
