---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-sector-patterns
title: WordPress retail / e-commerce
headline: WordPress retail / e-commerce
summary: "FunnelKit \"Funnel Builder for WooCommerce\" actively exploited as a Magecart skimmer on 40,000+ WordPress stores (daily 2026-05-17), no CVE assigned."
discovered_at: "2026-05-11T05:00:20Z"
event_date: null
run_id: 2026-W20-71c96b25
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - actively-exploited
  - data-breach
  - supply-chain
regions:
  - global
sectors:
  - retail
entities: []
cves: []
sources:
  - url: "https://sansec.io/research/funnelkit-woocommerce-vulnerability-exploited"
    publisher: Sansec research
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/funnel-builder-wordpress-plugin-bug-exploited-to-steal-credit-cards/"
    publisher: BleepingComputer — Funnel Builder skimmer
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
migrated_from: briefs/weekly/2026-W20.md
---

**FunnelKit "Funnel Builder for WooCommerce"** actively exploited as a Magecart skimmer on 40,000+ WordPress stores (daily 2026-05-17), no CVE assigned. The operational pattern (Magecart abuse of a popular WooCommerce plugin) is portable across the WordPress + WooCommerce e-commerce ecosystem used by Swiss / EU SMB retailers; SOC managers serving SMB or municipal e-commerce estates should sweep deployed WooCommerce plugin inventories for the affected FunnelKit version and audit checkout-page DOM for injected payment-form-skimming scripts.
