---
schema: 1
kind: policy
horizon: strategic
weekly_section: weekly-policy
title: "NCSC-CH — fake Swiss Post \"Avis de passage\" QR-code phishing in French-speaking Switzerland"
headline: "NCSC-CH — fake Swiss Post \"Avis de passage\" QR-code phishing in French-speaking Switzerland"
summary: "NCSC-CH's Week 24 Wochenrückblick flagged a hybrid physical-plus-digital social-engineering campaign in French-speaking Switzerland: attackers drop fake Swiss Post collection-notice (\"Avis de passage\") letters into letterboxes, closely mimicking official branding, with a QR code leading to a phishing site that …"
discovered_at: "2026-06-22T00:15:11Z"
event_date: 2026-06-16
run_id: 2026-W25-0aacfe65
priority: notable
immediate_action: null
tags:
  - phishing
regions:
  - switzerland
sectors:
  - public-sector
entities:
  - "incident:ncsc-ch-booking-hotel-phishing-2026"
cves: []
sources:
  - url: "https://www.ncsc.admin.ch/ncsc/en/home/aktuell/im-fokus/2026/wochenrueckblick_24.html"
    publisher: "NCSC-CH Week 24 Wochenrückblick"
    role: primary
closed_sources: []
evidence: []
verification: single-source-national-cert
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/weekly/2026-W25.md
---

NCSC-CH's Week 24 Wochenrückblick flagged a hybrid physical-plus-digital social-engineering campaign in French-speaking Switzerland: attackers drop fake Swiss Post collection-notice ("Avis de passage") letters into letterboxes, closely mimicking official branding, with a QR code leading to a phishing site that harvests identity and credit-card data ([NCSC-CH, 2026-06-16](https://www.ncsc.admin.ch/ncsc/en/home/aktuell/im-fokus/2026/wochenrueckblick_24.html)). The physical-delivery vector defeats email-gateway controls entirely. Public-sector organisations in French-speaking cantons should brief staff on the physical-QR lure, since the Swiss Post brand is frequently abused and a letterbox-delivered QR bypasses every email-based phishing control.
