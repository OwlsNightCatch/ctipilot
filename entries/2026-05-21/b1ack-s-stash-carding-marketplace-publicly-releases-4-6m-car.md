---
schema: 1
kind: incident
horizon: operational
title: "B1ack's Stash carding marketplace publicly releases 4.6M card records — SOCRadar attributes collection to e-skimming and phishing; not confirmed by issuing banks"
headline: "B1ack's Stash carding marketplace publicly releases 4.6M card records — SOCRadar attributes collection to e-skimming and phishing; not confirmed by issuing"
summary: "The dark-web carding marketplace B1ack's Stash — operational since at least 2023, with prior free-release waves of 1M cards in April 2024 and 4M in February 2025 — announced the free release of approximately 4.6 million stolen credit and debit card records on 2026-05-18 as a punitive action against vendors that …"
discovered_at: "2026-05-21T05:00:02Z"
event_date: 2026-05-20
run_id: 2026-05-21-77cdc4cd
priority: notable
immediate_action: null
tags:
  - cryptocrime
  - data-breach
  - phishing
  - organized-crime
regions:
  - us
  - europe
  - apac
sectors:
  - finance
  - retail
entities: []
cves: []
sources:
  - url: "https://socradar.io/blog/b1acks-stash-4-6-million-stolen-credit-cards-free/"
    publisher: SOCRadar
    role: primary
  - url: "https://securityaffairs.com/192415/cyber-crime/carding-site-b1acks-stash-dumps-4-6-million-stolen-cards-for-free.html"
    publisher: Security Affairs
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
migrated_from: briefs/2026-05-21.md
---

The dark-web carding marketplace B1ack's Stash — operational since at least 2023, with prior free-release waves of 1M cards in April 2024 and 4M in February 2025 — announced the free release of approximately 4.6 million stolen credit and debit card records on 2026-05-18 as a punitive action against vendors that cross-listed cards on competing shops ([SOCRadar, 2026-05-18](https://socradar.io/blog/b1acks-stash-4-6-million-stolen-credit-cards-free/); [Security Affairs, 2026-05-20](https://securityaffairs.com/192415/cyber-crime/carding-site-b1acks-stash-dumps-4-6-million-stolen-cards-for-free.html)). Each record carries the full primary account number, expiration date, CVV2, cardholder name, billing address, email, phone number and source IP — sufficient detail for card-not-present (CNP) fraud. SOCRadar's analysis estimates ~4.3 million records are net-new after de-duplication and expired-card filtering; geographic distribution is approximately 70 % US-issued, with Canada, UK, France, Malaysia, Hong Kong, Singapore and Thailand as secondary sources. SOCRadar attributes the collection methodology to e-skimming and phishing based on capture completeness. This is a dark-web marketplace claim — B1ack's Stash listed the dump for free, but no individual issuing bank has confirmed that specific cards originated from their systems. **Defender takeaway:** Swiss and European card-fraud teams should query their compromise feeds (FS-ISAC, card-network compromise files) for matching BIN ranges and review e-skimming exposure on legacy WooCommerce / Magento storefronts in the customer-facing estate; the consistent collection-method finding across multiple B1ack's Stash waves points at front-end JavaScript skimmer infections as the upstream root cause that still goes undetected in many low-volume merchant configurations.
