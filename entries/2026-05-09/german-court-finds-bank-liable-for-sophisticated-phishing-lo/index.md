---
schema: 1
kind: incident
title: "Berlin court orders Apobank to refund EUR 218,000 lost to a letter, QR-code and phone scam that enrolled the attackers' own device"
headline: "A German court found a phishing victim not grossly negligent after a bank-branded letter, a cloned portal and a call led her to enrol the attackers' device"
summary: >
  Landgericht Berlin II ruled on 2026-04-22 (38 O 293/25, not yet final) that Apobank must refund about
  EUR 218,000 because its customer was not grossly negligent: a bank-branded letter with a QR code led to a
  cloned banking portal, a caller posing as the bank guided her, and photographing a QR code enrolled the
  attackers' own device.
discovered_at: "2026-05-09T05:00:10Z"
event_date: "2026-04-22"
run_id: 2026-05-09-migrated
priority: routine
immediate_action: null
tags:
  - phishing
  - identity
regions:
  - dach
sectors:
  - finance
entities: []
cves: []
sources:
  - url: "https://www.heise.de/news/Urteil-gegen-die-Apobank-Finanzinstitut-haftet-fuer-Phishing-Schaden-11288231.html"
    publisher: "heise online"
    date: "2026-05-08"
    role: primary
  - url: "https://borncity.com/news/landgericht-berlin-ii-verurteilt-apobank-zu-218-000-euro-rueckzahlung/"
    publisher: "Borncity"
    date: "2026-05-09"
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
techniques: [T1566.002, T1566.004, T1098.005]
classification:
  reliability: B
  credibility: 2
migrated_from: briefs/2026-05-09.md
updates:
  - at: "2026-10-11T14:33:17Z"
    run_id: 2026-10-11T1307Z-audit
    type: correction
    summary: >
      The court did not impose a PSD2 duty to run IP analytics or trigger strong authentication; it held the customer not grossly negligent and remarked, beyond the holding, that the bank could have blocked the device registration given the IP and provider mismatch. No appeal is reported, only that the judgment is not yet final; the Swiss and public-sector generalisation and the law-enforcement tag had no basis, and the unreadable law-firm source is replaced by Borncity. The QR-code device-enrolment step is added, with a rating, an ATT&CK mapping and priority routine. A contradiction line records that heise has the customer reaching the fake prompt through her usual login rather than a QR code.
    fields: [kind, title, headline, summary, event_date, priority, tags, regions, sectors, techniques, sources, classification, body]
---

Landgericht Berlin II ruled on 2026-04-22 (38 O 293/25) that Apobank may not refuse to refund about EUR 218,000 on grounds of gross negligence: a bank-branded letter asked the customer to register a new security procedure, its QR code led to a cloned banking portal, a caller posing as the bank guided her through the process, and photographing a QR code let the attackers enrol their own device; the judgment is not yet final and the customer bears only the EUR 50 statutory share ([Borncity, 2026-05-09](https://borncity.com/news/landgericht-berlin-ii-verurteilt-apobank-zu-218-000-euro-rueckzahlung/)). Beyond the holding, the chamber remarked that the login and the attackers' new-device registration came from entirely different IP addresses and providers and that the bank did not block this discrepancy automatically ([heise online, 2026-05-08](https://www.heise.de/news/Urteil-gegen-die-Apobank-Finanzinstitut-haftet-fuer-Phishing-Schaden-11288231.html)).

**Contradiction:** Borncity has a QR code in the letter leading to the manipulated page ([Borncity, 2026-05-09](https://borncity.com/news/landgericht-berlin-ii-verurteilt-apobank-zu-218-000-euro-rueckzahlung/)), while heise reports that the customer was asked to set up two-factor authentication during her usual login through her browser's favourites bar ([heise online, 2026-05-08](https://www.heise.de/news/Urteil-gegen-die-Apobank-Finanzinstitut-haftet-fuer-Phishing-Schaden-11288231.html)).

**Defender takeaway:** the attack's decisive step was a device enrolment authorised by the victim, so the control point is the enrolment itself: a new authenticator registered from a network or provider different from the session that requested it deserves a hold and an out-of-band confirmation ([heise online, 2026-05-08](https://www.heise.de/news/Urteil-gegen-die-Apobank-Finanzinstitut-haftet-fuer-Phishing-Schaden-11288231.html)).

## Correction — 2026-10-11T14:33:17Z

The court's holding is that the customer was not grossly negligent, so the bank must refund the loss ([Borncity, 2026-05-09](https://borncity.com/news/landgericht-berlin-ii-verurteilt-apobank-zu-218-000-euro-rueckzahlung/)); its comments on the IP and provider mismatch were remarks beyond the decision, which the claimant's lawyer called technically still amateurish ([heise online, 2026-05-08](https://www.heise.de/news/Urteil-gegen-die-Apobank-Finanzinstitut-haftet-fuer-Phishing-Schaden-11288231.html)). No cited source mentions PSD2 or a duty to trigger strong customer authentication, and the judgment is described as not yet final rather than under appeal.
