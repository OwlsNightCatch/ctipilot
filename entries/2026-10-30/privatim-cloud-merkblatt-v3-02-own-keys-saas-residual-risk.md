---
schema: 1
kind: policy
title: "privatim revises its cloud guidance for Swiss public bodies (Merkblatt v3.02, 2 October 2026): sensitive data stays under the body's own keys, standard SaaS from Microsoft, Google, AWS and SAP is in most cases inadmissible for secrecy-bound data, and top management signs the residual risk"
headline: "privatim cloud guidance v3.02: public bodies keep their own keys for sensitive data; big-vendor SaaS mostly out"
summary: >
  privatim, the conference of the Swiss data-protection authorities, revised its guidance on cloud-specific risks for public bodies on 2026-10-02 (version 3.02, replacing the version of 3 February 2022).
  For particularly sensitive personal data the public body must encrypt with keys only it can use, outsourcing such data or data under a statutory duty of confidentiality to standard SaaS from large international providers is in most cases inadmissible,
  and the body's top management is to confirm the residual risk in writing.
discovered_at: "2026-10-30T03:52:00Z"
updated_at: null
event_date: "2026-10-02"
run_id: 2026-10-30T0255Z-intel
priority: routine
immediate_action: null
tags: [policy, cloud]
regions: [switzerland]
sectors: [public-sector]
entities: ["report:privatim-cloud-merkblatt-v3-02-2026"]
techniques: []
affected_products: []
cves: []
sources:
  - url: "https://www.privatim.ch/wp-content/uploads/2026/10/privatim_Cloud-Merkblatt_v3_02_20261002_def_DE.pdf"
    publisher: "privatim (Konferenz der schweizerischen Datenschutzbeauftragten)"
    date: "2026-10-02"
    role: primary
  - url: "https://dcod.ch/2026/10/27/privatim-usage-du-cloud/"
    publisher: "DCOD"
    date: "2026-10-27"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Outsourcing personal data that is particularly sensitive or subject to a statutory duty of confidentiality to SaaS solutions of large international providers (such as Microsoft, Google, AWS and SAP) by public bodies is in most cases inadmissible because of the untenable risk. (translated from German)"
    original: "Eine Auslagerung von besonders schützenswerten oder einer gesetzlichen Geheimhaltungspflicht unterstehenden Personendaten in SaaS-Lösungen von grossen internationalen Anbietern (wie Microsoft, Google, AWS und SAP) durch öffentliche Organe ist in den meisten Fällen aufgrund des untragbaren Risikos unzulässig"
    publisher: "privatim"
    source_url: "https://www.privatim.ch/wp-content/uploads/2026/10/privatim_Cloud-Merkblatt_v3_02_20261002_def_DE.pdf"
verification: single-source
sourcing_note: >
  privatim publishes its own guidance and the German PDF is the source for every statement; DCOD, a Swiss trade outlet, summarises it and dates the previous version.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

privatim, the conference of the Swiss data-protection authorities, dates version 3.02 of its guidance "Cloud-specific risks and measures" to 2 October 2026 ([privatim, 2026-10-02](https://www.privatim.ch/wp-content/uploads/2026/10/privatim_Cloud-Merkblatt_v3_02_20261002_def_DE.pdf)); it replaces the version of 3 February 2022 ([DCOD, 2026-10-27](https://dcod.ch/2026/10/27/privatim-usage-du-cloud/)). For particularly sensitive personal data the public body must encrypt, the keys may be available only to it, and outsourcing such data, or data under a statutory duty of confidentiality, to SaaS from large international providers, with Microsoft, Google, AWS and SAP named, is in most cases inadmissible because of the untenable risk ([privatim, 2026-10-02](https://www.privatim.ch/wp-content/uploads/2026/10/privatim_Cloud-Merkblatt_v3_02_20261002_def_DE.pdf)). Keys may stay with the provider only where no untenable risk follows and the provider is bound by contract to use them only with the body's express consent and to log every access ([privatim, 2026-10-02](https://www.privatim.ch/wp-content/uploads/2026/10/privatim_Cloud-Merkblatt_v3_02_20261002_def_DE.pdf)).

The body, or its top management, is to confirm in writing that it has understood the risks and accepts the residual risk, and data the cloud services generate about their users, such as telemetry and logging data, is to be treated with the same care and contract terms as the content data ([privatim, 2026-10-02](https://www.privatim.ch/wp-content/uploads/2026/10/privatim_Cloud-Merkblatt_v3_02_20261002_def_DE.pdf)). The five risk areas are contract design, places of processing including foreign authority access, confidentiality with encryption and key management, user data, and sub-processors ([privatim, 2026-10-02](https://www.privatim.ch/wp-content/uploads/2026/10/privatim_Cloud-Merkblatt_v3_02_20261002_def_DE.pdf)).

**Defender takeaway:** the guidance addresses public bodies subject to Swiss data-protection law; a body that runs or plans standard SaaS from the named providers for sensitive or secrecy-bound data is advised to keep its own encryption keys, to have top management sign the residual risk, and to hold provider telemetry and logs about its users to the same contract terms.
