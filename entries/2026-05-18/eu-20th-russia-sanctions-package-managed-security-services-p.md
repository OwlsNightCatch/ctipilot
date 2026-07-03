---
schema: 1
kind: policy
horizon: strategic
weekly_section: weekly-policy
title: "EU 20th Russia sanctions package — managed-security-services prohibition effective 25 May; Switzerland adopted most measures 22 May"
headline: "EU 20th Russia sanctions package — managed-security-services prohibition effective 25 May; Switzerland adopted most measures 22 May"
summary: "EU 20th Russia sanctions package prohibits \"managed security services\" from 25 May; Switzerland adopted most measures 22 May — EU/CH MSSP, IR and pentest providers with Russian-entity clients must have wound those engagements down. (Greenberg Traurig; Swiss EAER)"
discovered_at: "2026-05-18T05:00:36Z"
event_date: null
run_id: 2026-W21-473d6fa5
priority: high
immediate_action: null
tags:
  - law-enforcement
  - russia-nexus
  - eu-nexus
regions:
  - europe
  - switzerland
sectors: []
entities:
  - "policy:eu-20th-russia-sanctions-mss-prohibition-2026"
cves: []
sources:
  - url: "https://www.gtlaw.com/en/insights/2026/5/eus-20th-russia-sanctions-package-key-changes-and-compliance-implications"
    publisher: Greenberg Traurig — EU 20th sanctions package analysis
    role: primary
  - url: "https://www.wbf.admin.ch/en/newnsb/Byvj7-WGL93MiOgIL-f2p"
    publisher: "Swiss EAER press release, 2026-05-22"
    role: corroborating
  - url: "https://www.squirepattonboggs.com/insights/publications/the-20th-eu-sanctions-package-against-russia-scope-entry-into-force-and-compliance-implications-for-operators"
    publisher: Squire Patton Boggs
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
migrated_from: briefs/weekly/2026-W21.md
---

The single most defender-relevant regulatory change of the window. Council Regulation (EU) 2026/506 introduces a prohibition on providing **"managed security services"** — defined to include incident handling, penetration testing, security audits and security consulting/technical-support advice — to the Government of Russia and to entities legally established in Russia, effective **25 May 2026**. The prohibition reaches EU-incorporated MSSPs supplying Russian subsidiaries absent a national-competent-authority licence; no European Commission interpretive guidance on scope had been published as of 24 May, so law-firm analyses advise a conservative reading. **Switzerland's EAER adopted most of the 20th-package measures effective 22 May** (115 individuals/entities asset-frozen, 20 Russian banks and 7 third-country intermediaries under transaction ban, RUBx / digital-ruble transactions prohibited from 26 May), deferring some energy/trade provisions; whether the Swiss transposition includes the managed-security-services prohibition specifically requires SECO confirmation. **What defenders must do differently:** any EU or Swiss SOC, IR firm, or pentest provider with a Russian-law-entity client must have wound those engagements down by 25 May, and should verify no security tooling (EDR agents, SIEM forwarders, ticketing/connector integrations) is being operated or serviced under a contract with a Russian-established entity.
