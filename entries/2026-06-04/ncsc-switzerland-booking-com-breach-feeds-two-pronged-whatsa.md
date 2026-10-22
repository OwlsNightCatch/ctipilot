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
techniques: [T1566.003, T1078.004, T1684.001]
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
  - at: "2026-10-11T14:02:54Z"
    run_id: 2026-10-11T1307Z-audit
    type: correction
    internal: true
    summary: >
      Relabels the closing line as the Defender takeaway, the label the rest of the store uses; its text is unchanged.
    fields: [body]
  - at: "2026-10-21T08:21:35Z"
    run_id: 2026-10-21T0800Z-audit
    type: improvement
    summary: >
      The analysis gains Exposure, Detection and Triage lines from NCSC's report: the two exposed groups,
      booking-system logins and guest messaging plus visits to TWINT and bank look-alike pages as the
      telemetry, and NCSC's tell that a refund never asks for login details or a QR-code scan. The
      takeaway now rests on NCSC's out-of-band verification advice instead of an unsourced detection
      claim, and the impersonation of Booking.com and hotel customer service is mapped.
    fields: [body, techniques]
migrated_from: briefs/2026-06-04.md
---

NCSC Switzerland's Week 22 report notes an uptick in fraudulent WhatsApp messages about hotel bookings, in two variants ([NCSC-CH, 2026-06-02](https://www.bacs.admin.ch/en/26w22-en)). Variant 1 draws on real booking data (dates of stay, hotel names, guest names) from the April 2026 Booking.com data leak and sends a fake refund lure on WhatsApp that leads to a phishing page imitating TWINT and then to a second one posing as a bank, where the victim enters card data. Variant 2, which NCSC calls long-known, uses hotel booking-system credentials stolen by phishing or malware to message guests through the platform's official messaging, or by email or WhatsApp, demanding urgent card verification or an advance payment. In analyst judgement the second is the harder one to spot, since the message carries the trust of the real platform and defeats the usual "is this sender legitimate?" check. NCSC speaks of victims generally and names no sector.

**Exposure:** guests whose bookings were in the April 2026 Booking.com data leak, who receive the refund lure, and hotels whose booking-system logins are phished or stolen by malware, whose existing and future guests are then contacted through the platform's own messaging ([NCSC-CH, 2026-06-02](https://www.bacs.admin.ch/en/26w22-en)). Staff who book travel through these platforms fall in the same exposed population (analyst inference).

**Detection:** for a hotel, booking-system login records and the messages its account sends to guests, since the takeover variant logs in with stolen credentials and messages guests with urgent card-verification or advance-payment demands; for any organisation, web-proxy or DNS records of visits to pages imitating TWINT or a bank, the path the refund variant uses to collect card data ([NCSC-CH, 2026-06-02](https://www.bacs.admin.ch/en/26w22-en)).

**Triage:** correct booking details and a seemingly authentic sender do not make a message genuine; NCSC's tell is the request, an unsolicited refund or an urgent card verification to be completed through a link, and a refund never asks for login details or a QR-code scan ([NCSC-CH, 2026-06-02](https://www.bacs.admin.ch/en/26w22-en)).

**Defender takeaway:** because the takeover lure comes from the hotel's real booking account, a sender check does not catch it (analyst judgement); NCSC's lever is out-of-band verification, opening the booking through the official app or website or calling the hotel on a number looked up independently, never through the message's link, and having the card blocked at once if its details were entered ([NCSC-CH, 2026-06-02](https://www.bacs.admin.ch/en/26w22-en)).

## Correction — 2026-09-30T06:43:01Z

NCSC Switzerland ties only the first variant, the WhatsApp refund scam, to the April 2026 Booking.com data leak. It calls the second, the takeover of hotel booking-system accounts, long-known, and it does not rank the two ([NCSC-CH, 2026-06-02](https://www.bacs.admin.ch/en/26w22-en)). The title, summary and analysis now say so, and the view that the second is the harder one to spot is marked as analyst judgement. The phishing pages imitate TWINT and a bank, and NCSC speaks of victims generally without narrowing them to Switzerland or to a sector, so the entry's priority is notable rather than high. The citation now points at the page's new address on bacs.admin.ch, after the old ncsc.admin.ch page went dead.

## Improvement — 2026-10-21T08:21:35Z

Correct booking details and a seemingly authentic sender do not make a message genuine: the tell is an unsolicited refund or urgent card verification to be completed through a link, and a refund never asks for login details or a QR-code scan. Verification belongs out of band, through the official app or website or a call to the hotel on an independently looked-up number, and a card whose details were entered should be blocked at once ([NCSC-CH, 2026-06-02](https://www.bacs.admin.ch/en/26w22-en)).
