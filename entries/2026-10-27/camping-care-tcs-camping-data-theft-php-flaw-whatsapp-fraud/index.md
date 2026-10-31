---
schema: 1
kind: incident
title: "Camping.Care booking system (TCS Camping): customer and booking data stolen in connection with the PHP flaws, with real reservation numbers already used in WhatsApp fraud and 15,000 guests warned as a precaution"
headline: "Camping.Care booking data stolen: TCS and a second campsite warn of WhatsApp fraud; PHP link not vendor-confirmed"
summary: >
  TCS Camping is warning about 15,000 guests after data was stolen at Camping.Care, the Dutch supplier of the booking system for all TCS
  campsites; TCS confirmed the theft to SRF on 2026-10-26, SRF reports it in connection with the PHP security hole and Blick says the
  attackers used the two critical PHP flaws, though no source names a CVE or the entry point. Names, telephone numbers and reservation
  numbers are already used in fraudulent WhatsApp messages; TCS says account and IBAN data were not affected and the hole is closed. A
  second customer, Campingplatz Hüttenberg in canton Thurgau, has warned its guests of the same fraud in a notice that says Camping.care
  is still investigating the cause and does not mention PHP.
discovered_at: "2026-10-27T03:53:00Z"
updated_at: "2026-10-28T03:43:52Z"
event_date: "2026-10-26"
run_id: 2026-10-27T0256Z-intel
priority: notable
immediate_action: null
tags: [data-breach, supply-chain, phishing]
regions: [switzerland, europe]
sectors: []
entities: ["incident:camping-care-tcs-camping-data-theft-2026-10", "tool:php2shell", "product:camping-care"]
techniques: [T1190, T1566.003]
affected_products: ["Camping.Care", "PHP"]
cves: []
sources:
  - url: "https://www.srf.ch/sendungen/kassensturz-espresso/espresso/php-sicherheitsluecke-betrugsversuche-nach-datenleck-im-buchungssystem-fuer-tcs-camping"
    publisher: "SRF (Espresso)"
    date: "2026-10-26"
    role: primary
  - url: "https://www.blick.ch/wirtschaft/hackerangriff-auf-tcs-camping-15000-kunden-gewarnt/nws2bcn"
    publisher: "Blick"
    date: "2026-10-26"
    role: corroborating
  - url: "https://www.cisa.gov/news-events/alerts/2026/10/21/critical-vulnerabilities-php-require-immediate-patching"
    publisher: "CISA (alert, updated 2026-10-26)"
    date: "2026-10-26"
    role: corroborating
  - url: "https://www.camping-huettenberg.ch/erreichbarkeit-ueber-die-herbst-und-winterzeit-2/"
    publisher: "Campingplatz Hüttenberg (guest notice, page date 2026-10-23)"
    date: "2026-10-23"
    role: corroborating
  - url: "https://www.netzwoche.ch/news/2026-10-27/nach-angriff-ueber-php-sicherheitsluecke-nehmen-betrueger-camper-ins-visier"
    publisher: "Netzwoche"
    date: "2026-10-27"
    role: corroborating
  - url: "https://www.watson.ch/schweiz/digital/154077128-tcs-camping-meldet-datenleck-nach-php-sicherheitsluecke"
    publisher: "watson.ch (Keystone-SDA dispatch)"
    date: "2026-10-26"
    role: corroborating
closed_sources: []
evidence:
  - quote: "As TCS confirms to the SRF consumer magazine Espresso, fraudsters were able to steal customer and booking information. (translated from German)"
    original: "Wie der TCS gegenüber dem SRF-Konsumentenmagazin «Espresso» bestätigt, konnten Betrüger Kunden- und Buchungsinformationen entwenden."
    publisher: "SRF (Espresso)"
    source_url: "https://www.srf.ch/sendungen/kassensturz-espresso/espresso/php-sicherheitsluecke-betrugsversuche-nach-datenleck-im-buchungssystem-fuer-tcs-camping"
  - quote: "The security hole has meanwhile been closed. (translated from German)"
    original: "Die Sicherheitslücke sei unterdessen geschlossen worden."
    publisher: "SRF (Espresso)"
    source_url: "https://www.srf.ch/sendungen/kassensturz-espresso/espresso/php-sicherheitsluecke-betrugsversuche-nach-datenleck-im-buchungssystem-fuer-tcs-camping"
  - quote: "The hackers used the critical security hole in the PHP programming language to steal customer and booking data (translated from German)"
    original: "Die Hacker nutzten die kritische Sicherheitslücke der Programmiersprache PHP, um Kunden- und Buchungsdaten zu stehlen"
    publisher: "Blick"
    source_url: "https://www.blick.ch/wirtschaft/hackerangriff-auf-tcs-camping-15000-kunden-gewarnt/nws2bcn"
  - quote: "Camping.care is currently investigating the cause of the incident. (translated from German)"
    original: "Camping.care untersucht derzeit die Ursache des Vorfalls."
    publisher: "Campingplatz Hüttenberg (guest notice, page date 2026-10-23)"
    source_url: "https://www.camping-huettenberg.ch/erreichbarkeit-ueber-die-herbst-und-winterzeit-2/"
  - quote: "As things stand, it must be assumed that booking data was used without authorisation. (translated from German)"
    original: "Nach aktuellem Stand ist davon auszugehen, dass Buchungsdaten unbefugt verwendet wurden."
    publisher: "Campingplatz Hüttenberg (guest notice, page date 2026-10-23)"
    source_url: "https://www.camping-huettenberg.ch/erreichbarkeit-ueber-die-herbst-und-winterzeit-2/"
  - quote: "Whether the attackers in the Camping.care incident actually exploited one of the PHP vulnerabilities is not apparent from the campsite's notice. (translated from German)"
    original: "Ob die Angreifer beim Vorfall bei Camping.care tatsächlich eine der PHP-Sicherheitslücken ausnutzten, geht aus der Mitteilung des Campingplatzes nicht hervor."
    publisher: "Netzwoche"
    source_url: "https://www.netzwoche.ch/news/2026-10-27/nach-angriff-ueber-php-sicherheitsluecke-nehmen-betrueger-camper-ins-visier"
  - quote: "Fraudsters were able to steal customer and booking information in connection with the international security hole in the PHP programming language, as a spokesperson of the Touring Club Schweiz (TCS) confirmed on Monday at the request of the news agency Keystone-SDA (translated from German)"
    original: "Betrüger konnten im Zusammenhang mit der internationalen Sicherheitslücke bei der Programmiersprache PHP Kundschafts- und Buchungsinformationen entwenden, wie ein Sprecher des Touring Club Schweiz (TCS) am Montag auf Anfrage der Nachrichtenagentur Keystone-SDA bestätigte"
    publisher: "watson.ch (Keystone-SDA dispatch)"
    source_url: "https://www.watson.ch/schweiz/digital/154077128-tcs-camping-meldet-datenleck-nach-php-sicherheitsluecke"
verification: single-source-victim
sourcing_note: >
  TCS's confirmation of the theft to SRF is the victim-side statement; Blick relays SRF. SRF links the case to the PHP security hole
  with the words "in connection with" and Blick states that the attackers used the two flaws, while neither names a CVE identifier, the
  entry point, the date of the intrusion or an actor. Camping.Care itself is not quoted: its position reaches us through a customer's notice
  (Campingplatz Hüttenberg), which says it is investigating the cause and does not mention PHP, and Netzwoche notes that the notice does not
  say whether the PHP flaws were used.
confidence: medium
references:
  - "2026-10-21/php-critical-release-pre-announced-cve-2026-109618-109619"
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates:
  - at: "2026-10-28T03:43:52Z"
    run_id: 2026-10-28T0256Z-intel
    type: update
    summary: >
      A second Swiss customer of Camping.Care, Campingplatz Hüttenberg in canton Thurgau, has warned its
      guests of the same WhatsApp fraud in a notice with the page date 2026-10-23; the notice says the
      supplier is investigating the cause and does not mention PHP, so the link to the PHP flaws rests on
      SRF, Blick and a TCS spokesperson's statement rather than on the supplier.
    fields: [headline, summary, sources, evidence, sourcing_note, body]
migrated_from: null
---

TCS Camping is warning about 15,000 guests as a precaution because the provider of its booking system, Camping.Care, suffered a data theft; TCS confirmed to the SRF consumer programme Espresso on 2026-10-26 that fraudsters could steal customer and booking information, and SRF reports the case in connection with the worldwide PHP security hole ([SRF, 2026-10-26](https://www.srf.ch/sendungen/kassensturz-espresso/espresso/php-sicherheitsluecke-betrugsversuche-nach-datenleck-im-buchungssystem-fuer-tcs-camping)). Blick describes Camping.Care as a Dutch company whose booking system handles reservations for all campsites of the Touring Club Schweiz, writes, citing SRF, that the hackers used the critical PHP flaw to steal customer and booking data and that Camping.Care is not the only software supplier hit ([Blick, 2026-10-26](https://www.blick.ch/wirtschaft/hackerangriff-auf-tcs-camping-15000-kunden-gewarnt/nws2bcn)). No source names the CVE identifiers, the entry point, the date of the intrusion or an actor, and TCS says the hole has since been closed ([SRF, 2026-10-26](https://www.srf.ch/sendungen/kassensturz-espresso/espresso/php-sicherheitsluecke-betrugsversuche-nach-datenleck-im-buchungssystem-fuer-tcs-camping)). The stolen data already in criminal use includes, among other data, names, telephone numbers and reservation numbers: guests received fraudulent WhatsApp messages that refer to existing reservations ([SRF, 2026-10-26](https://www.srf.ch/sendungen/kassensturz-espresso/espresso/php-sicherheitsluecke-betrugsversuche-nach-datenleck-im-buchungssystem-fuer-tcs-camping)). TCS says account details and IBANs were not affected and that credit card data is not stored in the booking system ([SRF, 2026-10-26](https://www.srf.ch/sendungen/kassensturz-espresso/espresso/php-sicherheitsluecke-betrugsversuche-nach-datenleck-im-buchungssystem-fuer-tcs-camping)). A second customer, Campingplatz Hüttenberg in canton Thurgau, told its guests in a notice (page date 2026-10-23) that Camping.care had informed it of WhatsApp messages to guests of several campsites that contain real booking information and a link, that Camping.care is investigating the cause and that booking data must be assumed to have been used without authorisation; the notice does not mention PHP, and Netzwoche points out that it does not say whether the attackers used one of the PHP flaws ([Campingplatz Hüttenberg, 2026-10-23](https://www.camping-huettenberg.ch/erreichbarkeit-ueber-die-herbst-und-winterzeit-2/); [Netzwoche, 2026-10-27](https://www.netzwoche.ch/news/2026-10-27/nach-angriff-ueber-php-sicherheitsluecke-nehmen-betrueger-camper-ins-visier)).

**Exposure:** the guests who booked through the TCS campsite booking system, about 15,000 of whom TCS has warned, and any other customer of the Camping.Care platform, one of which, Campingplatz Hüttenberg, has warned its own guests; Blick says Camping.Care is not the only software supplier hit ([Blick, 2026-10-26](https://www.blick.ch/wirtschaft/hackerangriff-auf-tcs-camping-15000-kunden-gewarnt/nws2bcn); [Netzwoche, 2026-10-27](https://www.netzwoche.ch/news/2026-10-27/nach-angriff-ueber-php-sicherheitsluecke-nehmen-betrueger-camper-ins-visier)).

**Detection:** the only signal the sources describe is on the recipient side, unsolicited WhatsApp messages that quote a real reservation with the correct name, telephone number and reservation number; no source gives intrusion telemetry from the supplier's systems ([SRF, 2026-10-26](https://www.srf.ch/sendungen/kassensturz-espresso/espresso/php-sicherheitsluecke-betrugsversuche-nach-datenleck-im-buchungssystem-fuer-tcs-camping)).

**Triage:** TCS Camping sends no automated booking details, payment requests or reservation links over WhatsApp, so a WhatsApp message of that kind that quotes a genuine reservation is the fraud, however accurate its details ([SRF, 2026-10-26](https://www.srf.ch/sendungen/kassensturz-espresso/espresso/php-sicherheitsluecke-betrugsversuche-nach-datenleck-im-buchungssystem-fuer-tcs-camping)).

**Defender takeaway:** for a booking, ticketing or citizen-portal application that a supplier runs on PHP, ask the supplier in writing whether its runtime was updated to 8.5.12, 8.4.27, 8.3.36 or 8.2.35 ([CISA, 2026-10-26](https://www.cisa.gov/news-events/alerts/2026/10/21/critical-vulnerabilities-php-require-immediate-patching)) and whether customer data was accessed before that, because SRF, Blick and a TCS spokesperson tie this theft to the PHP flaws ([SRF, 2026-10-26](https://www.srf.ch/sendungen/kassensturz-espresso/espresso/php-sicherheitsluecke-betrugsversuche-nach-datenleck-im-buchungssystem-fuer-tcs-camping); [Blick, 2026-10-26](https://www.blick.ch/wirtschaft/hackerangriff-auf-tcs-camping-15000-kunden-gewarnt/nws2bcn); [watson.ch, 2026-10-26](https://www.watson.ch/schweiz/digital/154077128-tcs-camping-meldet-datenleck-nach-php-sicherheitsluecke)), although a customer's notice says the supplier is still investigating the cause ([Campingplatz Hüttenberg, 2026-10-23](https://www.camping-huettenberg.ch/erreichbarkeit-ueber-die-herbst-und-winterzeit-2/)) and no source says how the intrusion happened; and tell the people whose data the supplier holds that a message quoting their real booking details is no proof that it comes from you.

## Update — 2026-10-28T03:43:52Z

Netzwoche reported on 2026-10-27 that a second Swiss Camping.Care customer, Campingplatz Hüttenberg in canton Thurgau, has warned its guests of WhatsApp messages about existing bookings that contain real booking information and a link; the campsite's notice carries the page date 2026-10-23 ([Netzwoche, 2026-10-27](https://www.netzwoche.ch/news/2026-10-27/nach-angriff-ueber-php-sicherheitsluecke-nehmen-betrueger-camper-ins-visier); [Campingplatz Hüttenberg, 2026-10-23](https://www.camping-huettenberg.ch/erreichbarkeit-ueber-die-herbst-und-winterzeit-2/)). The notice says Camping.care informed the campsite of the messages, that Camping.care is investigating the cause and that booking data must be assumed to have been used without authorisation; it does not mention PHP, and Netzwoche points out that it does not say whether the attackers used one of the PHP flaws. The link to the PHP flaws therefore rests on SRF, Blick and a TCS spokesperson's statement to Keystone-SDA ([watson.ch, 2026-10-26](https://www.watson.ch/schweiz/digital/154077128-tcs-camping-meldet-datenleck-nach-php-sicherheitsluecke)), not on the supplier.
