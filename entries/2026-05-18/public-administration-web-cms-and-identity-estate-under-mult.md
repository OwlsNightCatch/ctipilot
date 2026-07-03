---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-sector-patterns
title: Public administration — web-CMS and identity estate under multi-vector pressure
headline: Public administration — web-CMS and identity estate under multi-vector pressure
summary: "Public-sector web and identity infrastructure took hits from several directions this week: the actively-exploited Drupal pre-auth SQLi (§ 1), ANSSI/CERT-FR's CERTFR-2026-AVI-0635 on SPIP < 4.4.15 (the dominant French public-administration CMS), the unpatched Sparx Enterprise Architect chain and the Keycloak IAM …"
discovered_at: "2026-05-18T05:00:15Z"
event_date: 2026-05-19
run_id: 2026-W21-473d6fa5
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - nation-state
  - data-breach
regions:
  - europe
  - switzerland
sectors:
  - public-sector
entities: []
cves: []
sources:
  - url: "https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0635/"
    publisher: ANSSI / CERT-FR — CERTFR-2026-AVI-0635 (SPIP)
    role: primary
  - url: "https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/"
    publisher: Krebs on Security — CISA GovCloud keys
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

Public-sector web and identity infrastructure took hits from several directions this week: the actively-exploited Drupal pre-auth SQLi (§ 1), ANSSI/CERT-FR's CERTFR-2026-AVI-0635 on **SPIP < 4.4.15** (the dominant French public-administration CMS), the unpatched Sparx Enterprise Architect chain and the Keycloak IAM cluster (§ 3), and Webworm's pivot to EU government targets (§ 7). Add the Krebs-reported CISA-contractor exposure of AWS GovCloud admin keys in a public GitHub repo for ~6 months ([daily 2026-05-19](/briefs/2026-05-19/)) and the Rhysida Stuttgart claim (§ 5), and the week's signal is that the public-administration estate's CMS, IAM and cloud-credential surfaces are all live targets simultaneously. Prioritise the CMS/IAM patch SLAs and audit cloud-credential hygiene in contractor repositories.
