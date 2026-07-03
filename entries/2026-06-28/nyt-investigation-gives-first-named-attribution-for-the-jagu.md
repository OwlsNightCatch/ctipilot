---
schema: 1
kind: threat
horizon: operational
title: NYT investigation gives first named attribution for the Jaguar Land Rover ransomware attack — a Russian state-linked criminal group
headline: NYT investigation gives first named attribution for the Jaguar Land Rover ransomware attack — a Russian state-linked criminal group
summary: "A New York Times investigation provides the first named attribution for the August 2025 Jaguar Land Rover ransomware attack — a Russian state-linked criminal group — in an incident that halted JLR production for ~six weeks and is estimated at ~£1.9 bn / $2.5 bn in UK economic impact. Attribution is the investigators' assessment, not an official UK government statement (TechCrunch, 2026-06-26)."
discovered_at: "2026-06-28T05:05:37Z"
event_date: 2026-06-26
run_id: 2026-06-28-1b30612a
priority: high
immediate_action: null
tags:
  - ransomware
  - organized-crime
  - russia-nexus
regions:
  - uk
  - europe
sectors:
  - manufacturing
  - transport
entities: []
cves: []
sources:
  - url: "https://techcrunch.com/2026/06/26/russian-hackers-were-behind-2-5-billion-hack-of-jaguar-land-rover-report/"
    publisher: TechCrunch
    role: primary
  - url: "https://thenextweb.com/news/jaguar-land-rover-hack-russian-hackers-nyt-investigation"
    publisher: The Next Web
    role: corroborating
closed_sources: []
evidence:
  - quote: "investigators have not determined whether the hackers were working directly for Vladimir Putin's government, were independent criminals, or were operating with the government's tacit approval."
    publisher: "TechCrunch, citing NYT"
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

A New York Times investigation published 2026-06-26 provides the first named attribution for the August–October 2025 ransomware attack on Jaguar Land Rover (JLR): investigators including the FBI, the UK National Crime Agency, NCSC, Google Mandiant and Palo Alto Networks now attribute the core intrusion to a Russian state-linked criminal group (Microsoft is reported to have named the group to investigators) ([TechCrunch, 2026-06-26](https://techcrunch.com/2026/06/26/russian-hackers-were-behind-2-5-billion-hack-of-jaguar-land-rover-report/); [The Next Web, 2026-06-26](https://thenextweb.com/news/jaguar-land-rover-hack-russian-hackers-nyt-investigation)). The attribution is the investigators' assessment relayed through journalism — the UK government has not made it official, and investigators say they cannot establish whether the group acted on Kremlin orders, with tacit approval, or independently. The attack halted JLR manufacturing for roughly six weeks and disrupted 5,000+ supply-chain businesses, with UK economic damage estimated at ~£1.9 bn ($2.5 bn). Investigators also found a separate Jordanian actor ("Rey") independently inside JLR networks, illustrating multi-actor opportunistic access to the same under-segmented victim.

**Defender takeaway:** Per the fake-news guard, treat the Russian attribution as the investigators'/NYT's claim, not an established fact — but the pattern (state-adjacent criminal ransomware against a NATO-aligned manufacturer, possibly retaliatory for Ukraine support) is a relevant sector signal for EU/Swiss defence-industrial and automotive supply chains. The multi-actor finding reinforces that a partially-compromised perimeter invites additional opportunistic intrusion; prioritise segmentation, credential hygiene and tested clean-recovery for high-value manufacturing/OT estates.
