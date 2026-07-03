---
schema: 1
kind: incident
horizon: strategic
weekly_section: weekly-incidents-recap
title: "France's Tchap government messenger — account-takeover scrapes 73,467 civil servants' metadata"
headline: "France's Tchap government messenger — account-takeover scrapes 73,467 civil servants' metadata"
summary: "France's sovereign Tchap government messenger was breached — account-takeover scraped metadata on 73,467 civil servants, ANSSI detected it and DINUM disclosed; the largest public-sector incident of the week. (daily 06-10, DINUM)"
discovered_at: "2026-06-14T23:57:30Z"
event_date: null
run_id: 2026-W24-bd5a7519
priority: high
immediate_action: null
tags:
  - data-breach
  - identity
regions:
  - europe
sectors:
  - public-sector
entities: []
cves: []
sources:
  - url: "https://www.numerique.gouv.fr/sinformer/espace-presse/incident-tchap/"
    publisher: DINUM incident page
    role: primary
closed_sources: []
evidence: []
verification: single-source
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

The most consequential public-sector incident of the week. On 7 June ANSSI detected a compromise of Tchap, the French state's sovereign Matrix-based encrypted messenger used by ~825,000 civil servants across all ministries; DINUM published the disclosure ([DINUM](https://www.numerique.gouv.fr/sinformer/espace-presse/incident-tchap/); [daily 06-10](/briefs/2026-06-10/)). The attacker used account takeover to scrape directory metadata on 73,467 users; message content, protected by end-to-end encryption, was not exposed, and CNIL was notified. The defender takeaway is that "sovereign and E2E-encrypted" still leaves a metadata-harvesting surface at the account/identity layer — the directory is a target even when the message body is not.
