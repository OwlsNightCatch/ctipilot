---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-sector-patterns
title: Finance / payments — Stripe-abusing Magecart and OFAC Iran sanctions
headline: Finance / payments — Stripe-abusing Magecart and OFAC Iran sanctions
summary: "A Magecart variant delivering its skimmer through Stripe customer metadata and exfiltrating stolen card data back through api.stripe.com as fake customer records was documented by Sansec this week (Sansec, 2026-06-04; daily 2026-06-07)."
discovered_at: "2026-06-01T05:00:10Z"
event_date: 2026-06-07
run_id: 2026-W23-9118e7bd
priority: notable
immediate_action: null
tags:
  - organized-crime
  - supply-chain
  - data-breach
  - law-enforcement
  - iran-nexus
  - cryptocrime
regions:
  - global
  - us
sectors:
  - finance
  - retail
entities: []
cves: []
sources:
  - url: "https://sansec.io/research/stripe-api-skimmer-infrastructure"
    publisher: Sansec — Stripe API skimmer
    role: primary
  - url: "https://home.treasury.gov/news/press-releases/sb0519"
    publisher: US Treasury OFAC
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
migrated_from: briefs/weekly/2026-W23.md
---

A Magecart variant delivering its skimmer through Stripe customer metadata and exfiltrating stolen card data back through `api.stripe.com` as fake customer records was documented by Sansec this week ([Sansec, 2026-06-04](https://sansec.io/research/stripe-api-skimmer-infrastructure); [daily 2026-06-07](/briefs/2026-06-07/)). Because both payload delivery and exfiltration transit a universally allow-listed domain, CSP `connect-src` controls and WAF egress rules built around blocking unknown domains are blind to this variant. Detection must move server-side: audit GTM container IDs, monitor Stripe customer-creation events for non-order-matched calls, and inspect customer-metadata fields for encoded JavaScript. Separately, OFAC designated Nobitex and three Iranian exchanges for IRGC-affiliated ransomware proceeds — confirmed wallet clusters now carry an OFAC sanctions-nexus consideration for any EU institution with US correspondent relationships.
