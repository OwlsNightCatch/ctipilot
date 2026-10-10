---
schema: 1
kind: incident
title: "NCSC Switzerland: WhatsApp hotel-booking phishing in two variants, one fed by the April Booking.com data leak"
headline: "NCSC Switzerland: WhatsApp hotel-booking phishing in two variants, one fed by the April Booking.com data leak"
summary: "NCSC Switzerland warns of two hotel-booking phishing variants: a WhatsApp refund scam that uses booking data from the April 2026 Booking.com data leak and leads through TWINT and bank phishing pages to card theft, and a long-known takeover of hotel booking-system accounts that contacts guests through the platform's own messaging (NCSC-CH, 2026-06-02)."
discovered_at: "2026-06-04T05:00:00Z"
event_date: 2026-06-02
run_id: 2026-06-04-51b23ffa
priority: notable
immediate_action: null
tags:
  - phishing
  - identity
  - data-breach
regions:
  - switzerland
  - europe
sectors: []
entities:
  - "incident:ncsc-ch-booking-hotel-phishing-2026"
techniques: [T1566.003, T1078.004]
cves: []
sources:
  - url: "https://www.bacs.admin.ch/en/26w22-en"
    publisher: "NCSC Switzerland, Week 22 report"
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
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
updates:
  - at: "2026-09-30T06:43:01Z"
    run_id: 2026-09-30T0634Z-audit
    type: correction
    summary: >
      NCSC ties only the refund variant to the April 2026 Booking.com data leak and does not rank the
      two variants, so the entry now says so, marks the ranking as analyst judgement and moves from
      high to notable priority. The citation follows the page to its new address on bacs.admin.ch.
    fields: [sources, techniques, classification, title, headline, summary, priority, sectors, body]
migrated_from: briefs/2026-06-04.md
---

NCSC Switzerland's Week 22 report notes an uptick in fraudulent WhatsApp messages about hotel bookings, in two variants ([NCSC-CH, 2026-06-02](https://www.bacs.admin.ch/en/26w22-en)). Variant 1 draws on real booking data (dates of stay, hotel names, guest names) from the April 2026 Booking.com data leak and sends a fake refund lure on WhatsApp that leads to a phishing page imitating TWINT and then to a second one posing as a bank, where the victim enters card data. Variant 2, which NCSC calls long-known, uses hotel booking-system credentials stolen by phishing or malware to message guests through the platform's official messaging, or by email or WhatsApp, demanding urgent card verification or an advance payment. In analyst judgement the second is the harder one to spot, since the message carries the trust of the real platform and defeats the usual "is this sender legitimate?" check. NCSC speaks of victims generally and names no sector. Staff who book travel through these platforms fall in the same exposed population (analyst inference).

**Why it matters to us:** the account-takeover variant breaks user-awareness controls because the lure originates from a trusted booking system, not a spoofed sender, so detection has to move to anomalous outbound messaging from booking-platform accounts and to card-data entry on TWINT/bank look-alike domains.

## Correction — 2026-09-30T06:43:01Z

NCSC Switzerland ties only the first variant, the WhatsApp refund scam, to the April 2026 Booking.com data leak. It calls the second, the takeover of hotel booking-system accounts, long-known, and it does not rank the two ([NCSC-CH, 2026-06-02](https://www.bacs.admin.ch/en/26w22-en)). The title, summary and analysis now say so, and the view that the second is the harder one to spot is marked as analyst judgement. The phishing pages imitate TWINT and a bank, and NCSC speaks of victims generally without narrowing them to Switzerland or to a sector, so the entry's priority is notable rather than high. The citation now points at the page's new address on bacs.admin.ch, after the old ncsc.admin.ch page went dead.
