---
schema: 1
kind: incident
title: "B1ack's Stash carding marketplace releases about 4.6 million stolen payment card records for free"
headline: "Carding shop B1ack's Stash dumps 4.6M stolen card records, about 70% US-issued, to punish its own sellers"
summary: >
  SOCRadar reported on 2026-05-18 that the dark-web carding marketplace B1ack's Stash suspended about
  8 million stolen CVV2 records after sellers resold its cards on competing shops, and released about
  4.6 million of them for free. The records carry full card numbers, CVV2, cardholder identity, billing
  address, e-mail, phone and IP address, about 70% of them from US cardholders; SOCRadar assesses that the
  data likely comes from e-commerce skimming or phishing.
discovered_at: "2026-05-21T05:00:02Z"
event_date: 2026-05-18
run_id: 2026-05-21-77cdc4cd
priority: notable
immediate_action: null
tags:
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
entities:
  - "campaign:b1ack-stash-46m-card-dump-may-2026-third-free-release-wave"
techniques: [T1657]
cves: []
sources:
  - url: "https://socradar.io/blog/b1acks-stash-4-6-million-stolen-credit-cards-free/"
    publisher: "SOCRadar"
    date: "2026-05-18"
    role: primary
  - url: "https://securityaffairs.com/192415/cyber-crime/carding-site-b1acks-stash-dumps-4-6-million-stolen-cards-for-free.html"
    publisher: "Security Affairs"
    date: "2026-05-20"
    role: corroborating
closed_sources: []
evidence:
  - quote: "making American cardholders by far the most heavily represented victims"
    publisher: "SOCRadar"
    source_url: "https://socradar.io/blog/b1acks-stash-4-6-million-stolen-credit-cards-free/"
  - quote: "The most immediate threat is card-not-present (CNP) fraud."
    publisher: "SOCRadar"
    source_url: "https://socradar.io/blog/b1acks-stash-4-6-million-stolen-credit-cards-free/"
  - quote: "After filtering, roughly 4.3 million records appear to be fresh and potentially usable."
    publisher: "Security Affairs"
    source_url: "https://securityaffairs.com/192415/cyber-crime/carding-site-b1acks-stash-dumps-4-6-million-stolen-cards-for-free.html"
verification: single-source
sourcing_note: >
  SOCRadar analysed the released dataset and is the only assessor; the release itself is the marketplace's
  own announcement, and Security Affairs restates SOCRadar.
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-21.md
updates:
  - at: "2026-10-21T20:28:19Z"
    run_id: 2026-10-21T1148Z-audit
    type: improvement
    summary: >
      B1ack's Stash's release was reported on 2026-05-18 and is part of about 8 million suspended CVV2
      records, and the roughly 4.3 million fresh records come from Security Affairs' account of SOCRadar's
      filtering. SOCRadar only assesses the source as likely e-commerce skimming or phishing, so the
      unsourced storefront and cross-release root-cause claims are dropped, with exposure, detection and
      takeaway guidance added.
    fields: [body, classification, entities, event_date, evidence, headline, sources, sourcing_note, summary, tags, techniques, title, verification]
---

SOCRadar reported on 2026-05-18 that B1ack's Stash, a dark-web carding marketplace operating since at least 2023, suspended about 8 million stolen CVV2 records from its inventory because sellers had resold its cards in competing shops, and released about 4.6 million of them as a free download ([SOCRadar, 2026-05-18](https://socradar.io/blog/b1acks-stash-4-6-million-stolen-credit-cards-free/)). Each record holds the full card number, expiry date, CVV2, cardholder name, billing address, e-mail, phone number and IP address; SOCRadar assesses that the data likely comes from e-commerce skimming or phishing operations, and about 70% of the records belong to US cardholders, followed by Canada, the United Kingdom, France and Malaysia ([SOCRadar, 2026-05-18](https://socradar.io/blog/b1acks-stash-4-6-million-stolen-credit-cards-free/)). After SOCRadar filtered out expired and duplicate records, roughly 4.3 million appear fresh and usable, and the marketplace has used free releases as marketing before, one million cards in April 2024 and over four million records in February 2025 ([Security Affairs, 2026-05-20](https://securityaffairs.com/192415/cyber-crime/carding-site-b1acks-stash-dumps-4-6-million-stolen-cards-for-free.html)).

**Exposure:** card issuers and merchants whose cardholders appear in the dump, overwhelmingly in the US; Europe appears mainly through UK and French cards ([SOCRadar, 2026-05-18](https://socradar.io/blog/b1acks-stash-4-6-million-stolen-credit-cards-free/)).

**Detection:** payment fraud telemetry: SOCRadar expects card-not-present fraud to accelerate in the weeks after the release, and complete billing addresses make address verification easy to pass ([SOCRadar, 2026-05-18](https://socradar.io/blog/b1acks-stash-4-6-million-stolen-credit-cards-free/)).

**Defender takeaway:** for card-fraud teams the decision is SOCRadar's recommendation to review card-not-present fraud thresholds for transactions whose billing details match the dataset's patterns ([SOCRadar, 2026-05-18](https://socradar.io/blog/b1acks-stash-4-6-million-stolen-credit-cards-free/)); organizations without a card portfolio or merchant estate have no decision to make.

## Improvement — 2026-10-21T20:28:19Z

The release was reported on 2026-05-18 and is part of about 8 million CVV2 records the marketplace suspended ([SOCRadar, 2026-05-18](https://socradar.io/blog/b1acks-stash-4-6-million-stolen-credit-cards-free/)); the estimate of roughly 4.3 million fresh records is Security Affairs' account of SOCRadar's filtering ([Security Affairs, 2026-05-20](https://securityaffairs.com/192415/cyber-crime/carding-site-b1acks-stash-dumps-4-6-million-stolen-cards-for-free.html)). SOCRadar assesses only that the data likely comes from e-commerce skimming or phishing ([SOCRadar, 2026-05-18](https://socradar.io/blog/b1acks-stash-4-6-million-stolen-credit-cards-free/)); no source names WooCommerce or Magento storefronts or a root cause shared across the marketplace's releases.
