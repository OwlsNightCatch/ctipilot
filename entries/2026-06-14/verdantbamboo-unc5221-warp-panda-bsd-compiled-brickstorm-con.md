---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-long-running
title: "VerdantBamboo (UNC5221 / WARP PANDA) — BSD-compiled BRICKSTORM confirmed on pfSense, plus a new PLENET backdoor"
headline: "VerdantBamboo (UNC5221 / WARP PANDA) — BSD-compiled BRICKSTORM confirmed on pfSense, plus a new PLENET backdoor"
summary: "key: actor:VerdantBamboo. The W23 weekly first carried Volexity's IR disclosure of this China-nexus operator; follow-up reporting this week fills in the technical chain."
discovered_at: "2026-06-14T23:57:35Z"
event_date: null
run_id: 2026-W24-bd5a7519
priority: notable
immediate_action: null
tags:
  - nation-state
  - espionage
  - china-nexus
regions:
  - global
sectors:
  - technology
  - public-sector
entities:
  - "actor:verdantbamboo"
cves: []
sources:
  - url: "https://www.volexity.com/blog/2026/06/04/verdantbamboo-just-another-brickstorm-in-the-firewall/"
    publisher: Volexity
    role: primary
  - url: "https://thehackernews.com/2026/06/verdantbamboo-deploys-bsd-variant-of.html"
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
migrated_from: briefs/weekly/2026-W24.md
---

`key: actor:VerdantBamboo`. The W23 weekly first carried Volexity's IR disclosure of this China-nexus operator; follow-up reporting this week fills in the technical chain. Volexity's case describes a BSD-compiled variant of the BRICKSTORM Golang backdoor on an MSP customer's pfSense firewall, reached after compromising an Egnyte Storage Sync appliance (local privilege escalation via default `egnyteservice` sudo permissions, fixed in Storage Sync v13.13), plus a previously-undocumented .NET Native AOT backdoor named **PLENET** on a Synology NAS and an AGENTPSD dropper ([Volexity](https://www.volexity.com/blog/2026/06/04/verdantbamboo-just-another-brickstorm-in-the-firewall/); [The Hacker News](https://thehackernews.com/2026/06/verdantbamboo-deploys-bsd-variant-of.html)). The BSD variant is the status-changing detail: it confirms VerdantBamboo can operate on FreeBSD-based appliances, beyond the Linux-only model where enterprise EDR is already blind. The intrusion ran ~18 months undetected and was used to proxy through the MSP into customer Microsoft 365 tenants via Conditional Access bypass. Outstanding question for defenders: edge appliances (firewalls, NAS, sync gateways) remain the EDR dead zone — the hunt has to move to network-flow anomalies and appliance-integrity baselining, not endpoint telemetry.
