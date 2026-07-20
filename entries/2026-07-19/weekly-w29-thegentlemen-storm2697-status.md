---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-long-running
title: "The Gentlemen (Storm-2697) status: ReliaQuest's Q2 2026 numbers put it ahead of Qilin on the ransomware leaderboard, and a European public-transport victim (Metro Mondego) landed this week"
headline: "The Gentlemen status — ReliaQuest ranks it Q2's most-active operator (300 vs Qilin's 289) on an AI-accelerated affiliate kit; it hit Metro Mondego (Portugal)"
summary: >
  Update to the prior weekly's The Gentlemen (Storm-2697) profile. ReliaQuest's Q2 2026 threat-spotlight (2026-07-16) reports The Gentlemen posted 300 victims in the quarter versus Qilin's 289, ending Qilin's leaderboard dominance, and attributes the pace to aggressive affiliate recruitment plus a well-packaged intrusion kit (pre-compromised victim lists, custom EDR killers, GPO-based deployment tooling) and a "likely AI-accelerated iteration layer" for tool refresh — with Infosecurity Magazine independently corroborating the 300-vs-289 figures. A GuidePoint GRIT review (pre-window) frames the same concentration as a "four-headed monster" (Qilin, The Gentlemen, Akira, DragonForce), with the five most prolific Q2 groups collectively claiming over 40% of recorded attacks. Operationally, the group's reach touched the constituency this week: Portugal's Metro Mondego confirmed a 6 July ransomware attack claimed by The Gentlemen, contained to internal systems. No new initial-access CVE or vector is disclosed — the delta is the quantitative leaderboard reversal, the AI-tooling-cadence explanation, and the fresh European public-transport victim.
discovered_at: "2026-07-19T23:36:00Z"
event_date: 2026-07-16
run_id: 2026-07-19T2310Z-weekly
priority: notable
immediate_action: null
tags:
  - ransomware
  - actively-exploited
regions:
  - europe
  - global
sectors:
  - public-sector
  - transport
entities:
  - actor:thegentlemen
  - actor:qilin
cves: []
techniques:
  - T1190
  - T1486
  - T1587.001
affected_products: []
sources:
  - url: "https://reliaquest.com/blog/threat-spotlight-ransomware-and-cyber-extortion-in-q2-2026"
    publisher: "ReliaQuest"
    date: "2026-07-16"
    role: primary
  - url: "https://www.infosecurity-magazine.com/news/the-gentlemen-most-prolific/"
    publisher: "Infosecurity Magazine"
    date: "2026-07-17"
    role: corroborating
  - url: "https://www.cybersecuritydive.com/news/ransomware-concentrated-ai-guidepoint/824828/"
    publisher: "Cybersecurity Dive (on GuidePoint GRIT Q2 2026)"
    date: "2026-07-09"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The Gentlemen became the most-active group, powered by aggressive affiliate recruitment and a well-packaged intrusion kit"
    publisher: "ReliaQuest"
verification: multi-source
sourcing_note: "The 300-vs-289 leaderboard figure is corroborated (ReliaQuest + Infosecurity Magazine); the 'AI-accelerated iteration layer' is ReliaQuest's own assessment, not independently confirmed, and is stated as such. The GuidePoint GRIT framing (2026-07-09) is pre-window background. Reliability B (research labs), credibility 2 (assessment-level tooling claim)."
confidence: medium
update_of: 2026-07-12/weekly-w28-the-gentlemen-status
references:
  - 2026-07-18/metro-mondego-thegentlemen-ransomware-portugal-transit
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: null
---

**UPDATE (originally covered 2026-07-12):** The prior weekly carried Unit 42's full profile of The Gentlemen (Storm-2697) — 580 claimed victims, a Qilin-affiliate lineage, a 90% affiliate payout and a suspected EDR-disable zero-day. This week the status change is quantitative and reaches the constituency. ReliaQuest's Q2 2026 threat-spotlight reports The Gentlemen "became the most-active group, powered by aggressive affiliate recruitment and a well-packaged intrusion kit" — 300 victims in Q2 against Qilin's 289 — with affiliates receiving pre-compromised victim lists, custom EDR killers and GPO-based deployment tooling, and a "likely AI-accelerated iteration layer" letting the operators refresh tooling faster than human-developer rivals ([ReliaQuest, 2026-07-16](https://reliaquest.com/blog/threat-spotlight-ransomware-and-cyber-extortion-in-q2-2026)); Infosecurity Magazine independently corroborates the 300-vs-289 figures ([Infosecurity Magazine, 2026-07-17](https://www.infosecurity-magazine.com/news/the-gentlemen-most-prolific/)). GuidePoint GRIT's pre-window Q2 review sets the same concentration in context — its "four-headed monster" is Qilin, The Gentlemen, Akira and DragonForce, and it reports the five most prolific groups collectively claimed over 40% of recorded Q2 attacks ([Cybersecurity Dive on GuidePoint GRIT, 2026-07-09](https://www.cybersecuritydive.com/news/ransomware-concentrated-ai-guidepoint/824828/)). Operationally, the group's claimed 6 July attack on Portugal's Metro Mondego — contained to internal systems, transport unaffected — is the fresh European public-sector datapoint. The initial-access funnel (the tracked FortiOS path and opportunistic edge exploitation) is unchanged; the practical takeaway for the constituency is that the most-active RaaS operator of the quarter is one already on its radar, now recruiting and tooling harder, so the FortiOS/edge and EDR-killer hunt posture the earlier coverage set remains the right one.
