---
schema: 1
kind: threat
title: "Acronis TRU on BOSSAI: one operator's mesh of 12 AI agents took patient-care records and dispatch case data from Taiwanese emergency services through a legacy open port, a public API and default root credentials, and failed wherever authentication was enforced"
headline: "BOSSAI AI agents took emergency-services data through open ports, public APIs and default credentials"
summary: >
  Acronis TRU describes BOSSAI, an agentic campaign it attributes with high confidence to one operator in Taiwan: a mesh of 12 AI agents, nine active, that over 12 observed days targeted government emergency services, banks, universities and military systems in 11 countries, with confirmed data exfiltration or system access at roughly ten targets in three countries. The confirmed emergency-services harm was patient-care records of a Taipei fire department and dispatch case records of a city 119 system; TRU says the agents failed where authentication was enforced and endpoints were filtered.
discovered_at: "2026-11-07T03:59:00Z"
updated_at: null
event_date: "2026-11-04"
run_id: 2026-11-07T0256Z-intel
priority: notable
immediate_action: null
tags: [ai-abuse, data-breach]
regions: [apac, global]
sectors: [public-sector, healthcare]
entities: ["campaign:bossai-ai-attack-mesh-taiwan-2026-11", "tool:hermes-ai-agent"]
techniques: [T1595.002, T1190, T1078.001, T1110, T1119]
affected_products: []
cves: []
sources:
  - url: "https://www.acronis.com/en/tru/posts/bossai-inside-the-ai-attack-mesh-that-targeted-taiwans-emergency-services/"
    publisher: "Acronis Threat Research Unit"
    date: "2026-11-04"
    role: primary
closed_sources: []
evidence:
  - quote: "TRU assesses with high confidence that the infrastructure and activity were operated by a single individual based in Hualien City, Taiwan."
    publisher: "Acronis Threat Research Unit"
    source_url: "https://www.acronis.com/en/tru/posts/bossai-inside-the-ai-attack-mesh-that-targeted-taiwans-emergency-services/"
  - quote: "Confirmed data exfiltration or system access occurred at roughly 10 distinct targets across three countries."
    publisher: "Acronis Threat Research Unit"
    source_url: "https://www.acronis.com/en/tru/posts/bossai-inside-the-ai-attack-mesh-that-targeted-taiwans-emergency-services/"
  - quote: "The agents failed where authentication was enforced, where paywalls required valid sessions and where endpoints were properly filtered."
    publisher: "Acronis Threat Research Unit"
    source_url: "https://www.acronis.com/en/tru/posts/bossai-inside-the-ai-attack-mesh-that-targeted-taiwans-emergency-services/"
verification: single-source
sourcing_note: >
  Acronis TRU is the only source and the findings come from the operator's workstation it recovered; the post gives "hundreds" of organisations in its introduction and "dozens" in a later section, so only its confirmed counts are used here, and it publishes no defender recommendations of its own.
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 3
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

Acronis TRU found an open attack workstation holding more than 90,000 files and describes BOSSAI as a mesh of 12 AI agents, nine active, driven by a changing roster of language models, with the operator acting as the bridge between agents and typing commands in Traditional Chinese ([Acronis TRU, 2026-11-04](https://www.acronis.com/en/tru/posts/bossai-inside-the-ai-attack-mesh-that-targeted-taiwans-emergency-services/)). The agents that executed attacks ran almost exclusively on abliterated open-weight models run locally, after commercial models repeatedly refused offensive requests ([Acronis TRU, 2026-11-04](https://www.acronis.com/en/tru/posts/bossai-inside-the-ai-attack-mesh-that-targeted-taiwans-emergency-services/)). In the 12 days TRU observed, the operator targeted government emergency services, banks and lenders, universities and military systems in 11 countries, with confirmed exfiltration or system access at roughly ten targets in three countries and about fifteen more attacked without confirmed compromise ([Acronis TRU, 2026-11-04](https://www.acronis.com/en/tru/posts/bossai-inside-the-ai-attack-mesh-that-targeted-taiwans-emergency-services/)).

The confirmed emergency-services harm is the part that matters here. A Taipei fire-department patient-care records platform exposed ECG readings, ambulance video and vital signs from 2018, accessible without credentials; a city's 119 dispatch system yielded case records with incident times, response types, status fields and street-level locations across seven districts from the system's API; and a fire-dispatch vendor's database administration panel opened with default root credentials, exposing 18 or more tables ([Acronis TRU, 2026-11-04](https://www.acronis.com/en/tru/posts/bossai-inside-the-ai-attack-mesh-that-targeted-taiwans-emergency-services/)). In an emergency-management system the agents found a hardcoded AES-256 key in front-end JavaScript that exposed session-cookie contents, an administrator identity among them, and a partial server-side request forgery path, without confirming a full compromise ([Acronis TRU, 2026-11-04](https://www.acronis.com/en/tru/posts/bossai-inside-the-ai-attack-mesh-that-targeted-taiwans-emergency-services/)). A brute-force run against a national fire agency's single sign-on portal gave no confirmed access, and the critical Apache flaw that the operator's vulnerability platform reported at a disaster-response centre was fabricated, because the port was filtered ([Acronis TRU, 2026-11-04](https://www.acronis.com/en/tru/posts/bossai-inside-the-ai-attack-mesh-that-targeted-taiwans-emergency-services/)). TRU says the agents failed where authentication was enforced, where paywalls required valid sessions and where endpoints were properly filtered, and that obscurity no longer protects a system from agents that investigate hundreds of targets at once ([Acronis TRU, 2026-11-04](https://www.acronis.com/en/tru/posts/bossai-inside-the-ai-attack-mesh-that-targeted-taiwans-emergency-services/)).

**Exposure:** emergency-service, dispatch and public-safety systems that expose a record API or a legacy data port without authentication, leave default administrator credentials on a vendor's database panel, or ship secrets in front-end JavaScript; those are the weaknesses the agents turned into data, and TRU reports the patient-care and dispatch records as the gravest confirmed harm.

**Detection:** TRU names sqlmap, nmap and nikto among the most-used tools, so the traffic is ordinary scanner traffic in web access and authentication logs (an inference from the tool list): bursts of SQL-injection probing, repeated sign-in attempts against a single sign-on portal from one source, and logins to a database administration panel with a default account.

**Defender takeaway:** Swiss dispatch, patient-care and records systems of emergency services are the same target class, so check them for unauthenticated APIs and legacy ports, default root or administrator credentials on vendor panels, and keys or tokens in front-end code; the agents failed wherever authentication was enforced, so closing those gaps is what stops this tooling.
