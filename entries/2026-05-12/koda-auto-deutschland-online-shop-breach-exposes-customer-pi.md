---
schema: 1
kind: incident
title: "Škoda Auto Deutschland accessories-shop breach: attackers exploited the shop software, customer data and password hashes were accessible, logs cannot show what was copied"
headline: "Attackers exploited Škoda's German accessories-shop software; logs cannot show which customer data was copied"
summary: "Škoda Auto Deutschland disclosed in May 2026 that unauthorised parties exploited a vulnerability in the standard shop software of its German accessories shop and gained temporary access to the shop system, which stores names, addresses, contact details, orders and account credentials with hashed passwords. Its logs cannot show whether or how much data was copied; full card data is not stored in the shop, and other Škoda shops, the manufacturer's systems and Škoda Connect are not affected."
discovered_at: "2026-05-12T05:00:03Z"
event_date: 2026-05-11
run_id: 2026-05-12-cd1ab844
priority: notable
immediate_action: null
tags:
  - data-breach
  - vulnerabilities
regions:
  - dach
  - europe
sectors:
  - retail
  - manufacturing
entities:
  - "incident:skoda-shop-breach-2026"
techniques: [T1190]
affected_products: []
cves: []
sources:
  - url: "https://www.skoda-auto.de/unternehmen/sicherheitsvorfall-skoda-shop"
    publisher: "Škoda Auto Deutschland (Information zum IT-Sicherheitsvorfall im Škoda Online-Shop, information on the IT security incident in the Škoda online shop)"
    role: primary
  - url: "https://www.securityweek.com/skoda-data-breach-hits-online-shop-customers/"
    publisher: "SecurityWeek"
    date: "2026-05-11"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Our technical security monitoring established that unauthorised parties had exploited a vulnerability in the standard shop software in use. (translated from German)"
    original: "Im Rahmen unserer technischen Sicherheitsüberwachung wurde festgestellt, dass Unbefugte eine Schwachstelle in der eingesetzten Shop-Standardsoftware ausgenutzt haben."
    publisher: "Škoda Auto Deutschland"
    source_url: "https://www.skoda-auto.de/unternehmen/sicherheitsvorfall-skoda-shop"
  - quote: "Because of the nature of the available logs, however, it cannot be reconstructed in every detail after the fact whether and to what extent data was actually copied or retrieved. (translated from German)"
    original: "Aufgrund der Art der vorhandenen Protokolle lässt sich im Nachhinein jedoch nicht in allen Einzelheiten nachvollziehen, ob und in welchem Umfang Daten tatsächlich kopiert oder abgerufen wurden."
    publisher: "Škoda Auto Deutschland"
    source_url: "https://www.skoda-auto.de/unternehmen/sicherheitsvorfall-skoda-shop"
  - quote: "Access credentials consist of the email address and a password that is stored in encrypted form, that is, as a cryptographic hash. (translated from German)"
    original: "Zugangsdaten bestehen aus der E Mail-Adresse und einem Passwort, das in verschlüsselter Form, also als kryptografischer Hash, gespeichert wird."
    publisher: "Škoda Auto Deutschland"
    source_url: "https://www.skoda-auto.de/unternehmen/sicherheitsvorfall-skoda-shop"
  - quote: "The Škoda Connect portal is not affected by the security incident. (translated from German)"
    original: "Das Škoda Connect Portal ist vom Sicherheitsvorfall nicht betroffen."
    publisher: "Škoda Auto Deutschland"
    source_url: "https://www.skoda-auto.de/unternehmen/sicherheitsvorfall-skoda-shop"
  - quote: "The company has yet to disclose how many individuals were potentially affected."
    publisher: "SecurityWeek"
    source_url: "https://www.securityweek.com/skoda-data-breach-hits-online-shop-customers/"
verification: single-source-victim
sourcing_note: >
  Every fact comes from Škoda Auto Deutschland's own question-and-answer page; SecurityWeek restates it. Škoda says access to the
  stored data was possible, which SecurityWeek reports as data having been accessed.
confidence: medium
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
migrated_from: briefs/2026-05-12.md
updates:
  - at: "2026-10-21T20:44:49Z"
    run_id: 2026-10-21T1148Z-audit
    type: correction
    summary: >
      Škoda Auto Deutschland says access to the stored shop data was possible in principle but its logs
      cannot show whether or how much was copied, and it reported the incident to the data-protection
      authority without stating any 72-hour timing. Only the German accessories shop was affected, not
      other Škoda shops, the manufacturer's systems or Škoda Connect, and full card data is not stored in
      the shop; Škoda's advice to customers is to change reused passwords and watch for phishing that
      refers to their orders.
    fields: [affected_products, body, classification, confidence, entities, evidence, headline, sources, sourcing_note, summary, techniques, title, verification]
---

Škoda Auto Deutschland's security monitoring found that unauthorised parties had exploited a vulnerability in the standard shop software of its online accessories shop and gained temporary access to the shop system; the shop was taken offline, the vulnerability fixed, an external IT forensics firm engaged and the incident reported to the competent data-protection authority ([Škoda Auto Deutschland](https://www.skoda-auto.de/unternehmen/sicherheitsvorfall-skoda-shop)). The shop stores names and addresses, email addresses and sometimes telephone numbers, order information and customer-account credentials made up of the email address and a password kept as a cryptographic hash; full credit card data is processed only by the payment providers ([Škoda Auto Deutschland](https://www.skoda-auto.de/unternehmen/sicherheitsvorfall-skoda-shop)). Škoda's analysis found that access to the stored data was possible in principle, but the nature of its logs does not allow it to reconstruct whether and to what extent data was actually copied or retrieved, and it has no concrete indication of misuse ([Škoda Auto Deutschland](https://www.skoda-auto.de/unternehmen/sicherheitsvorfall-skoda-shop)). Only the accessories shop run by Škoda Auto Deutschland GmbH for customers in Germany was affected, not other Škoda online shops, the systems of the manufacturer Škoda Auto a.s. or the Škoda Connect portal ([Škoda Auto Deutschland](https://www.skoda-auto.de/unternehmen/sicherheitsvorfall-skoda-shop)). SecurityWeek reported the disclosure on 2026-05-11 and noted that the number of affected customers had not been disclosed ([SecurityWeek, 2026-05-11](https://www.securityweek.com/skoda-data-breach-hits-online-shop-customers/)).

**Exposure:** customers of the German Škoda accessories shop, above all those who reuse its password elsewhere: Škoda expects phishing that refers to earlier orders and login attempts with the known credentials, especially where the same password serves several services ([Škoda Auto Deutschland](https://www.skoda-auto.de/unternehmen/sicherheitsvorfall-skoda-shop)).

**Defender takeaway:** affected customers change any password they reused from the shop and treat messages about Škoda orders with suspicion, as Škoda advises ([Škoda Auto Deutschland](https://www.skoda-auto.de/unternehmen/sicherheitsvorfall-skoda-shop)); for other organisations the case changes no decision, since neither the shop software nor the vulnerability is named ([Škoda Auto Deutschland](https://www.skoda-auto.de/unternehmen/sicherheitsvorfall-skoda-shop)).

## Correction — 2026-10-21T20:44:49Z

Škoda Auto Deutschland reported the incident to the competent data-protection authority but does not say when, so no 72-hour timing can be stated ([Škoda Auto Deutschland](https://www.skoda-auto.de/unternehmen/sicherheitsvorfall-skoda-shop)). Its own words on the data are that access to the stored data was possible in principle and that, because of the nature of the available logs, it cannot reconstruct in every detail whether and to what extent data was actually copied or retrieved (translated from German); the shop concerned is only the German accessories shop, while other Škoda shops, the manufacturer's systems and Škoda Connect are unaffected and full card data is not stored there ([Škoda Auto Deutschland](https://www.skoda-auto.de/unternehmen/sicherheitsvorfall-skoda-shop)). The step Škoda gives customers is to change passwords reused from the shop and to watch for messages that refer to their Škoda orders ([Škoda Auto Deutschland](https://www.skoda-auto.de/unternehmen/sicherheitsvorfall-skoda-shop)).
