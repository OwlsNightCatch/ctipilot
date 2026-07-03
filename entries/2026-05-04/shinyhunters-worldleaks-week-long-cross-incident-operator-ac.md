---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-multi-day
title: "ShinyHunters / WorldLeaks — week-long cross-incident operator activity touching Inditex, Vimeo, ADT, and Instructure / Canvas"
headline: "ShinyHunters / WorldLeaks — week-long cross-incident operator activity touching Inditex, Vimeo, ADT, and Instructure / Canvas"
summary: "The cross-day pattern most visible in 2026-W19 is the ShinyHunters / WorldLeaks operator family's role in four parallel third-party / SaaS-tier compromises with European footprint, all riding the third-party-analytics → cloud-data-warehouse → tenant-data-exfiltration pivot rather than direct attack on the victim's …"
discovered_at: "2026-05-04T05:00:06Z"
event_date: 2026-05-09
run_id: 2026-W19-a5788b22
priority: notable
immediate_action: null
tags:
  - data-breach
  - organized-crime
  - supply-chain
  - cloud
  - identity
regions:
  - europe
  - us
  - global
sectors:
  - technology
  - retail
entities:
  - "incident:inditex-zara-breach-2026"
  - "actor:shinyhunters"
cves: []
sources:
  - url: "https://vimeo.com/blog/post/anodot-third-party-security-incident"
    publisher: Vimeo official blog — Anodot incident
    role: primary
  - url: "https://securityaffairs.com/191859/cyber-crime/zara-data-breach-197000-customers-exposed-in-third-party-security-incident.html"
    publisher: SecurityAffairs — Zara breach
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/video-service-vimeo-confirms-anodot-breach-exposed-user-data/"
    publisher: BleepingComputer — Vimeo Anodot
    role: corroborating
  - url: "https://newsroom.adt.com/corporate-news/adt-detects-cybersecurity-incident"
    publisher: ADT Newsroom
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
migrated_from: briefs/weekly/2026-W19.md
---

The cross-day pattern most visible in 2026-W19 is the ShinyHunters / WorldLeaks operator family's role in four parallel third-party / SaaS-tier compromises with European footprint, all riding the **third-party-analytics → cloud-data-warehouse → tenant-data-exfiltration** pivot rather than direct attack on the victim's infrastructure. The sequence: **Vimeo / Anodot** (first covered 2026-05-07) — Vimeo's official statement confirmed customer email addresses were affected via a third-party security incident involving Anodot, an analytics vendor integrated with Vimeo's infrastructure; the Snowflake-and-BigQuery cloud-data-warehouse pivot is attributed to ShinyHunters' extortion claim per BleepingComputer (not Vimeo's own confirmation); BleepingComputer reports approximately 119,000 email addresses exposed; ShinyHunters published the dataset after Vimeo declined extortion ([Vimeo official blog, 2026-04-27](https://vimeo.com/blog/post/anodot-third-party-security-incident) · [BleepingComputer, 2026-05-06](https://www.bleepingcomputer.com/news/security/video-service-vimeo-confirms-anodot-breach-exposed-user-data/) · [The Register, 2026-05-05](https://www.theregister.com/2026/05/05/shinyhunters_dump_puts_119k_vimeo/)). **Inditex (Zara)** (first covered 2026-05-09) — Have I Been Pwned confirmed 197,400 EU customer email addresses exposed via the same Anodot → BigQuery pivot; Inditex confirmed access to email, geographic location, order IDs, support ticket content; ShinyHunters dumped ~140 GB after Inditex declined ([SecurityAffairs, 2026-05-08](https://securityaffairs.com/191859/cyber-crime/zara-data-breach-197000-customers-exposed-in-third-party-security-incident.html) · [BleepingComputer, 2026-05-08](https://www.bleepingcomputer.com/news/security/zara-data-breach-exposed-personal-information-of-197-000-people/) · [daily 2026-05-09](/briefs/2026-05-09/)). **ADT Inc.** (first covered 2026-05-06) — SEC 8-K filed 2026-04-24 disclosed unauthorised access to certain cloud environments; ShinyHunters claimed the initial-access vector was vishing on an employee Okta SSO account followed by Salesforce data exfiltration (ADT did not confirm the vector) ([ADT Newsroom, 2026-04-24](https://newsroom.adt.com/corporate-news/adt-detects-cybersecurity-incident) · [daily 2026-05-06](/briefs/2026-05-06/)). **Instructure / Canvas** (first covered 2026-05-06; expanded each subsequent day — see separate H3 below).

The lesson under PD-11 (less is more) for Swiss / EU public-sector readers: third-party analytics, monitoring, evaluation, and observability integrations holding OAuth or service-account access to production data warehouses (Snowflake, BigQuery, Redshift) are a structural supply-chain attack surface that vendor-assessment checklists routinely miss. Audit delegated access grants for analytics tooling; enforce token scoping and expiry; require provider-side anomaly alerts; and treat any tenant-to-tenant credential propagation pattern (the four incidents above are all that pattern) as warranting a tabletop on revocation timing — Vimeo revoked privileged credentials and access tokens within hours of detection, which is the right reference performance.
