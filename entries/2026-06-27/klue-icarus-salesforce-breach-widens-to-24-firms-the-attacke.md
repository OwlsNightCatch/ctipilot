---
schema: 1
kind: incident
horizon: operational
title: "Klue/Icarus Salesforce breach widens to ~24 firms; the attacker is itself hacked and a second extortion actor emerges"
headline: "Klue/Icarus Salesforce breach widens to ~24 firms; the attacker is itself hacked and a second extortion actor emerges"
summary: "Klue/Icarus Salesforce breach widens to ~24 firms — newly named EU victims include Germany's Lucanet and Link11; the attacker was itself hacked and a second extortion actor has emerged (SecurityWeek, 2026-06-26)."
discovered_at: "2026-06-27T05:17:49Z"
event_date: 2026-06-26
run_id: 2026-06-27-40e791d4
priority: high
immediate_action: null
tags:
  - data-breach
  - supply-chain
  - identity
  - cloud
  - organized-crime
regions:
  - global
  - europe
sectors:
  - technology
  - finance
entities: []
cves: []
sources:
  - url: "https://www.securityweek.com/more-klue-breach-victims-identified-as-hackers-get-hacked/"
    publisher: SecurityWeek
    role: primary
  - url: "https://techcrunch.com/2026/06/25/hacked-klue-says-criminals-are-deleting-stolen-customer-data-but-now-other-hackers-are-making-threats/"
    publisher: TechCrunch
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: 2026-06-25/klue-icarus-salesforce-oauth-breach-beyondtrust-and-lastpass
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-27.md
---

**UPDATE (originally covered 2026-06-25):** Roughly two dozen companies have now publicly notified customers of the Klue–Salesforce OAuth-integration breach, up from eleven on June 25, with newly named EU-domiciled victims including Germany's Lucanet and Link11 alongside Blackbaud, Deel, Camunda and Tines ([SecurityWeek, 2026-06-26](https://www.securityweek.com/more-klue-breach-victims-identified-as-hackers-get-hacked/)).

Klue reportedly told customers that the attacker ("Icarus") was itself compromised and that the stolen dataset is now in the hands of a second, unnamed actor running an independent extortion campaign; Icarus's Tor leak site went offline ([TechCrunch, 2026-06-25](https://techcrunch.com/2026/06/25/hacked-klue-says-criminals-are-deleting-stolen-customer-data-but-now-other-hackers-are-making-threats/)). The root cause is unchanged — a single over-privileged legacy OAuth integration credential granting bulk Salesforce access across ~195 customer orgs — reinforcing the standing action: audit and revoke dormant Connected Apps with export scopes, and alert on anomalous bulk `ReportExport`/API activity from integration service accounts.
