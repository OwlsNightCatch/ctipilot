---
schema: 1
kind: incident
horizon: strategic
weekly_section: weekly-incidents-recap
title: "Asocks residential-proxy botnet — Dutch Police + NCSC dismantle ~17M-device infrastructure hosted in the Netherlands"
headline: "Asocks residential-proxy botnet — Dutch Police + NCSC dismantle ~17M-device infrastructure hosted in the Netherlands"
summary: "The Cybercrime Team of the Police Unit The Hague, with the Dutch NCSC, dismantled a large residential-proxy botnet — at least 17 million compromised consumer devices worldwide, run through ~200 servers all physically hosted in the Netherlands (2026-05-29); NL Times and other reporting identify the service as …"
discovered_at: "2026-05-25T05:00:17Z"
event_date: 2026-05-29
run_id: 2026-W22-da77963d
priority: notable
immediate_action: null
tags:
  - law-enforcement
  - botnet
  - organized-crime
  - eu-nexus
regions:
  - europe
  - global
sectors:
  - public-sector
  - finance
  - telco
entities: []
cves: []
sources:
  - url: "https://www.politie.nl/nieuws/2026/mei/28/06-politie-en-ncsc-halen-groot-botnetwerk-offline.html"
    publisher: Politie.nl — botnet takedown
    role: primary
  - url: "https://nltimes.nl/2026/05/28/ncsc-dutch-police-disrupt-global-botnet-controlled-via-netherlands-based-servers"
    publisher: NL Times
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
migrated_from: briefs/weekly/2026-W22.md
---

The Cybercrime Team of the Police Unit The Hague, with the Dutch NCSC, dismantled a large residential-proxy botnet — at least 17 million compromised consumer devices worldwide, run through ~200 servers all physically hosted in the Netherlands ([2026-05-29](/briefs/2026-05-29/)); NL Times and other reporting identify the service as **Asocks** (the politie.nl primary states the scale and the NL-hosted infrastructure but does not name it). The operationally relevant point is what was hit: residential-proxy services are the anonymisation plumbing that launders credential-stuffing, scraping and fraud traffic to look like ordinary consumer ISP connections, defeating IP-reputation controls. The takedown degrades that capability industry-wide for a period, but — consistent with the W21 takedown pattern — expect infrastructure churn rather than a durable drop; the demand for residential-proxy egress is undiminished.
