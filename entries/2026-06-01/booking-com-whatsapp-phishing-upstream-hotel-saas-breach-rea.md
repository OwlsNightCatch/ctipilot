---
schema: 1
kind: incident
horizon: strategic
weekly_section: weekly-incidents-recap
title: "Booking.com WhatsApp phishing + upstream hotel SaaS breach: real reservation data weaponised, 100+ properties affected, Dutch DPA opens investigation"
headline: "Booking.com WhatsApp phishing + upstream hotel SaaS breach: real reservation data weaponised, 100+ properties affected, Dutch DPA opens investigation"
summary: "NCSC-CH's Week 22 report (4 June; daily 2026-06-04) documents two phishing variants exploiting real booking data leaked in the April 2026 Booking.com compromise: Variant 1 — fake WhatsApp refund lure → TWINT/Swiss-bank-portal credential harvest; Variant 2 — attackers using compromised hotel booking-system …"
discovered_at: "2026-06-01T05:00:14Z"
event_date: 2026-06-04
run_id: 2026-W23-9118e7bd
priority: notable
immediate_action: null
tags:
  - data-breach
  - phishing
  - supply-chain
regions:
  - europe
  - switzerland
sectors:
  - public-sector
  - finance
entities:
  - "incident:ncsc-ch-booking-hotel-phishing-2026"
cves: []
sources:
  - url: "https://www.ncsc.admin.ch/ncsc/en/home/aktuell/im-fokus/2026/wochenrueckblick_22.html"
    publisher: NCSC-CH Week 22 report
    role: primary
  - url: "https://www.dutchnews.nl/2026/06/mass-data-breach-on-over-100-dutch-hotels-hits-guests/"
    publisher: DutchNews.nl
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

NCSC-CH's Week 22 report (4 June; [daily 2026-06-04](/briefs/2026-06-04/)) documents two phishing variants exploiting real booking data leaked in the April 2026 Booking.com compromise: **Variant 1** — fake WhatsApp refund lure → TWINT/Swiss-bank-portal credential harvest; **Variant 2** — attackers using compromised hotel booking-system credentials to message guests *through the legitimate booking channel*, demanding urgent card re-verification. Variant 2 breaks user-awareness controls because the message originates from a trusted platform ([NCSC-CH](https://www.ncsc.admin.ch/ncsc/en/home/aktuell/im-fokus/2026/wochenrueckblick_22.html)). In the same window, a separate upstream booking/channel-management SaaS layer breach exposed guest reservation records (names, contacts, arrival/departure dates) for guests at more than 100 Dutch, Belgian and Irish hotels; criminals are already sending contextually accurate "confirm your reservation" phishing referencing real upcoming stays ([DutchNews.nl](https://www.dutchnews.nl/2026/06/mass-data-breach-on-over-100-dutch-hotels-hits-guests/)). The Dutch Data Protection Authority (Autoriteit Persoonsgegevens) has opened a GDPR investigation; Art. 33/34 notification clocks are running for each hotel as an independent controller.
