---
schema: 1
kind: incident
horizon: operational
title: "Novo Nordisk — FulcrumSec claims authorship, $25M demand refused, data offered for private sale"
headline: "Novo Nordisk — FulcrumSec claims authorship, $25M demand refused, data offered for private sale"
summary: "UPDATE (originally covered 2026-06-13): The cloud data-extortion group FulcrumSec has publicly claimed the Novo Nordisk breach, saying it spent more than two months inside the networks and exfiltrated roughly 1.3 TB (~700,000 files) including source code, drug-pipeline data, ~11,500 pseudonymised clinical-trial …"
discovered_at: "2026-06-17T05:14:35Z"
event_date: 2026-06-16
run_id: 2026-06-17-e102009c
priority: notable
immediate_action: null
tags:
  - data-breach
  - organized-crime
  - cloud
  - identity
regions:
  - europe
  - global
sectors:
  - healthcare
entities: []
cves: []
sources:
  - url: "https://www.globalbankingandfinance.com/hacking-group-claims-major-hack-novo-nordisk-attempted-25/"
    publisher: "Global Banking & Finance Review, 2026-06-16"
    role: primary
  - url: "https://www.insurancebusinessmag.com/us/news/cyber/ozempic-maker-novo-nordisk-hit-with-25-million-ransom-demand-after-claimed-data-breach-579161.aspx"
    publisher: "Insurance Business Magazine, 2026-06-16"
    role: corroborating
  - url: "https://www.moxfive.com/blog/who-is-fulcrumsec-inside-the-cloud-extortion-group-behind-21-victims-and-counting"
    publisher: "MOXFIVE actor profile, 2026-06-10"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: 2026-06-13/novo-nordisk-discloses-theft-of-clinical-trial-and-healthcar
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-17.md
---

**UPDATE (originally covered 2026-06-13):** The cloud data-extortion group FulcrumSec has publicly claimed the Novo Nordisk breach, saying it spent more than two months inside the networks and exfiltrated roughly 1.3 TB (~700,000 files) including source code, drug-pipeline data, ~11,500 pseudonymised clinical-trial records and internal AI artefacts; it demanded $25M, was refused, and is now exploring private sale of the data ([Global Banking & Finance Review, 2026-06-16](https://www.globalbankingandfinance.com/hacking-group-claims-major-hack-novo-nordisk-attempted-25/)).

FulcrumSec is a data-theft-only (non-ransomware) group active since late 2025 with 21+ prior claimed victims; an actor profile characterises its access vectors as unpatched public-facing apps, dormant/embedded credentials and API keys, absent MFA and misconfigured cloud storage ([MOXFIVE, 2026-06-10](https://www.moxfive.com/blog/who-is-fulcrumsec-inside-the-cloud-extortion-group-behind-21-victims-and-counting)). Novo Nordisk has confirmed unauthorised access to a limited number of internal systems and pseudonymised clinical-trial data exposure but has not validated FulcrumSec's scope claims ([Insurance Business Magazine, 2026-06-16](https://www.insurancebusinessmag.com/us/news/cyber/ozempic-maker-novo-nordisk-hit-with-25-million-ransom-demand-after-claimed-data-breach-579161.aspx)). Detection focus for FulcrumSec-style actors: large outbound transfers (DLP), cloud-storage access logs, OAuth grants to unfamiliar apps, and long-dwell reuse of stale service-account credentials. Enforce MFA on all privileged cloud identities and rotate dormant credentials.
