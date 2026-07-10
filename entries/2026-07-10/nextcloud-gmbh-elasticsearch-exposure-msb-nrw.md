---
schema: 1
kind: incident
horizon: operational
title: "Nextcloud GmbH's own hosting infrastructure exposed 367K internal records via a misconfigured public Elasticsearch cluster, including client setup scripts with hardcoded credentials"
headline: "Nextcloud GmbH exposed 367K internal records — client setup scripts with hardcoded DB credentials, a German ministry contact — via open Elasticsearch"
summary: >
  Cybernews found a publicly reachable, unauthenticated Elasticsearch cluster (~7.9 GB, ~367,000 records) belonging to Nextcloud GmbH's own corporate/hosting infrastructure — not the open-source Nextcloud software and no customer-operated servers. Exposed for roughly nine days in May 2026, it held invoices, contracts, internal/client email, and shell/Python client-setup scripts, some carrying hardcoded database credentials; named exposed parties include IONOS, STRATO and Germany's North Rhine-Westphalia Ministry of Schools and Education (MSB NRW). The risk to EU public-sector Nextcloud tenants is pretexting-grade material and a supplier-side secrets-hygiene lesson, not a confirmed downstream compromise.
discovered_at: "2026-07-10T04:36:19Z"
event_date: "2026-05-18"
run_id: 2026-07-10T0409Z-intel
priority: notable
immediate_action: null
tags: [data-breach, cloud, supply-chain, phishing]
regions: [europe, dach]
sectors: [public-sector, technology]
entities: [incident:nextcloud-gmbh-elasticsearch-exposure-2026]
techniques: [T1552.001, T1566]
affected_products: ["Elastic Elasticsearch"]
cves: []
sources:
  - url: "https://cybernews.com/security/nextcloud-cloud-provider-data-leak/"
    publisher: "Cybernews"
    date: "2026-07-08"
    role: primary
  - url: "https://www.heise.de/en/news/Open-database-Nextcloud-GmbH-fixes-potential-data-leak-11358446.html"
    publisher: "heise online"
    date: "2026-07-09"
    role: corroborating
closed_sources: []
evidence:
  - quote: "On May 18th, our research team discovered an exposed dataset containing 367,000 records. An investigation revealed that the cluster, with nearly 8GB of data, contained internal Nextcloud data."
    publisher: "Cybernews"
  - quote: "Some records include hardcoded database credentials."
    publisher: "Cybernews"
  - quote: "The issue was caused by a misconfiguration of our hosting infrastructure and is not related to the Nextcloud solution. No other Nextcloud servers belonging to our customers, partners or other users have been affected by this issue."
    publisher: "Cybernews"
verification: multi-source
sourcing_note: null
confidence: medium
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "If your organisation is a Nextcloud GmbH hosting/onboarding client, treat any credentials that appeared in vendor-supplied setup or management scripts as potentially exposed and rotate them, and review whether your deployment architecture was inferable from leaked material."
  - "Brief helpdesk and finance staff to scrutinise invoice- or contract-themed emails referencing Nextcloud or its hosting partners (IONOS, STRATO) in the near term — the leaked invoices/contracts are ready-made spearphishing pretext."
  - "Audit your own Elasticsearch/OpenSearch estate: bind clusters to internal-only interfaces or a VPC, enable the security/auth plugin (it is off by default on TCP 9200/9300), and add continuous external attack-surface scanning for unauthenticated data/management ports."
  - "Treat hardcoded credentials in infrastructure-as-code and setup scripts as a secrets-management finding to remediate regardless of whether the script is ever exposed."
migrated_from: null
---

Cybernews researchers discovered a publicly reachable, unauthenticated Elasticsearch cluster — about 7.92 GB across ~367,000 records — belonging to Nextcloud GmbH's own hosting and business infrastructure, not the Nextcloud open-source collaboration software and not any customer-operated Nextcloud server ([Cybernews, 2026-07-08](https://cybernews.com/security/nextcloud-cloud-provider-data-leak/)). The cluster was reachable from at least 18 May until Nextcloud closed it around 25-27 May 2026. Exposed, and in many cases unencrypted, records included client invoices and contracts (naming partnership terms and contact email addresses), internal and client email with headers and timestamps, beta-feature signup lists, and — the most operationally significant category — shell and Python scripts Nextcloud built to set up and manage its product for clients, some containing hardcoded database credentials (`T1552.001`). Named exposed parties in the contact data include hosting providers IONOS and STRATO and German government bodies such as North Rhine-Westphalia's Ministry of Schools and Education (MSB NRW). Nextcloud confirmed the root cause as a hosting-infrastructure misconfiguration, said no customer-operated Nextcloud servers were affected, reported the incident to its German data-protection supervisory authority, and states it found no evidence the data was accessed before closure — though an internet-reachable, unauthenticated Elasticsearch index is precisely the target continuously swept by automated internet-wide scanning, so prior undetected access cannot be excluded ([heise online, 2026-07-09](https://www.heise.de/en/news/Open-database-Nextcloud-GmbH-fixes-potential-data-leak-11358446.html)).

The relevance for this constituency is the supplier context: Nextcloud is actively adopted as a "Euro-Office" sovereign-cloud alternative to Microsoft 365/SharePoint across EU public administration, so vendor-side exposure of client-specific onboarding scripts and hardcoded credentials is a supply-chain-adjacent risk to any public-sector tenant whose material was in the leak. **Defender takeaway:** the concrete, transferable actions are secrets hygiene (never hardcode credentials in IaC/setup scripts, even ones that never leave internal storage) and external attack-surface monitoring for unauthenticated data stores — Elasticsearch/OpenSearch defaults to no authentication on 9200/9300 unless the security plugin is explicitly enabled, and this exposure was purely a network-reachability misconfiguration no host-based control would have caught. For Nextcloud clients specifically, the near-term threat is not a patch but pretexting: the leaked invoices and contracts are realistic phishing fodder (`T1566`), so raise scrutiny on unsolicited invoice/contract emails referencing Nextcloud or its hosting-partner ecosystem.
