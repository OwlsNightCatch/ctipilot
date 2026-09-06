---
schema: 1
kind: incident
title: "BKA and ZIT dismantle relaunched Crimenetwork darknet marketplace; German operator arrested in Mallorca on European Arrest Warrant"
headline: "BKA and ZIT dismantle relaunched Crimenetwork darknet marketplace; German operator arrested in Mallorca on European Arrest Warrant"
summary: "BKA + ZIT dismantle relaunched Crimenetwork darknet marketplace; German operator arrested in Mallorca. Operator arrested on a European Arrest Warrant on 2026-05-08; the rebooted platform had reached ~22,000 users and 100+ vendors with ~€3.6 M cumulative commissions before being seized (BKA — Deutscher Betreiber von \"Crimenetwork\" auf Mallorca verhaftet, 2026-05-08). Second BKA/ZIT/Spanish-Police takedown of the same brand inside 18 months."
discovered_at: "2026-05-12T05:00:01Z"
event_date: 2026-05-11
run_id: 2026-05-12-cd1ab844
priority: high
immediate_action: null
tags:
  - organized-crime
  - law-enforcement
  - cryptocrime
  - data-breach
regions:
  - dach
  - europe
sectors:
  - legal-services
  - public-sector
entities: []
cves: []
sources:
  - url: "https://www.bka.de/SharedDocs/Pressemitteilungen/DE/Presse_2026/pm260508_Crimenetwork.pdf?__blob=publicationFile&v=3"
    publisher: "Bundeskriminalamt — Deutscher Betreiber von \"Crimenetwork\" auf Mallorca verhaftet (en. \"German operator of 'Crimenetwork' arrested in Mallorca\"), 2026-05-08"
    role: primary
  - url: "https://www.helpnetsecurity.com/2026/05/11/germany-crimenetwork-marketplace-shut-down/"
    publisher: "Help Net Security, 2026-05-11"
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
migrated_from: briefs/2026-05-12.md
---

The German Bundeskriminalamt (BKA) and Frankfurt's Central Office for Combating Internet Crime (ZIT), with Spanish National Police support, arrested a 35-year-old German national at his residence in Mallorca on a European Arrest Warrant on **2026-05-08** and shut down the relaunched Crimenetwork ([Bundeskriminalamt press release — Deutscher Betreiber von "Crimenetwork" auf Mallorca verhaftet, 2026-05-08](https://www.bka.de/SharedDocs/Pressemitteilungen/DE/Presse_2026/pm260508_Crimenetwork.pdf?__blob=publicationFile&v=3); [Help Net Security, 2026-05-11](https://www.helpnetsecurity.com/2026/05/11/germany-crimenetwork-marketplace-shut-down/)). Crimenetwork was the dominant German-language darknet marketplace; the platform was originally taken down in December 2024, and a new operator rebuilt the infrastructure under the same branding shortly afterwards. The rebooted platform reached ~22,000 users and 100+ vendors and brokered stolen data, narcotics, forged documents and illegal services in BTC / LTC / XMR for an estimated **€3.6 million** in commissions and vendor fees before being seized. Investigators recovered approximately **€194,000** in assets and substantial user/transaction data, which the BKA states will drive a wave of follow-on prosecutions — the press release explicitly frames the seized infrastructure data as the operational value, not the headline arrest.

**Defender takeaway:** The DACH-region credential / payment-card / forged-document inventory cycle on Crimenetwork is now a known-historical artefact for the next 12–24 months — the seized vendor and buyer ledgers will resurface in attribution reports and breach-notification timelines. For Swiss / German / Austrian SOCs running credential-monitoring services, expect a downstream wave of leaked-credential validations once the BKA dataset reaches partner CERTs. The case also reinforces a structural point for German-speaking-market threat models: when an EU-wide darknet platform is dismantled, the replacement is typically a same-branding relaunch on residual customer trust rather than a forum migration — the rebrand interval has now compressed to weeks.
