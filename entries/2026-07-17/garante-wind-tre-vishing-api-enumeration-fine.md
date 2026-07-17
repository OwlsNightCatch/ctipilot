---
schema: 1
kind: incident
horizon: operational
title: "Garante fines Wind Tre EUR 1.7M over a vishing-enabled API-enumeration breach that exposed 365,048 telco customers"
headline: "Italian DPA fines Wind Tre EUR 1.7M — retail-staff vishing led to enumeration of an unprotected secondary API (365,048 customers)"
summary: >
  Italy's Garante published (2026-07-16) its 14 May 2026 decision fining Wind Tre S.p.A. EUR 1,715,600 over two
  2025 breaches with an unusually complete technical account: attackers vished retail point-of-sale staff into
  granting remote access, harvested a stored client digital certificate and credentials, used them as valid
  MFA'd access to a customer web application, then pivoted from the protected primary search API to an
  unprotected secondary API and ran ~2,000,000 sequential customerId requests, exfiltrating data on 365,048
  customers (payment data for 41,359). The transferable lesson for any Swiss/EU telco, utility or public body
  with a POS/field-agent access model: an enumeration-reachable secondary endpoint that pentesting never
  exercised.
discovered_at: "2026-07-17T04:35:00Z"
event_date: "2026-07-16"
run_id: 2026-07-17T0409Z-intel
priority: notable
immediate_action: null
tags: [data-breach, phishing, identity]
regions: [europe]
sectors: [telco]
entities: ["incident:wind-tre-2026-vishing-api-enumeration-breach"]
techniques: [T1566.004, T1078, T1552, T1213]
affected_products: []
cves: []
sources:
  - url: "https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/10272004"
    publisher: "Garante per la protezione dei dati personali (Newsletter n.549)"
    date: "2026-07-16"
    role: primary
  - url: "https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/10263796"
    publisher: "Garante per la protezione dei dati personali (Provvedimento n.348, 14 May 2026)"
    date: "2026-07-16"
    role: primary
  - url: "https://www.ansa.it/english/news/business/2026/07/16/privacy-watchdog-fines-wind-tre-1.7-million_43961a24-11d7-4652-9659-f09f4cd78659.html"
    publisher: "ANSA (English)"
    date: "2026-07-16"
    role: corroborating
closed_sources: []
evidence:
  - quote: "gli hacker, fingendosi tecnici dell'assistenza, hanno convinto gli operatori di due punti vendita a consentire l'accesso ai sistemi aziendali"
    publisher: "Garante per la protezione dei dati personali (Newsletter n.549)"
  - quote: "gli attaccanti sono riusciti ad eseguire circa 2 milioni di richieste totali seguendo una logica di enumeration, ovvero andando ad aumentare progressivamente l'identificativo del codice cliente (c.d. \"customerId\") violando i dati personali di 365.048 clienti"
    publisher: "Garante per la protezione dei dati personali (Provvedimento n.348, 14 May 2026)"
verification: multi-source
sourcing_note: "Primary is the Garante's own newsletter and full decision text (Provvedimento n.348, Admiralty A1), corroborated by ANSA. The breaches occurred in 2025; the decision is dated 2026-05-14 and was published 2026-07-16 (the in-window event). No threat actor is named — the perpetrators remain unidentified. Italian source quotes are glossed in the body."
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions: []
migrated_from: null
---

The Garante's decision gives a rare, fully technical account of a telco breach. Initial access was voice social engineering: attackers phoned staff at two retail points of sale, posed as internal support technicians, and "convinced operators at two retail points of sale to allow access to company systems" ([Garante, 2026-07-16](https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/10272004)). That remote access yielded the point-of-sale device's installed client digital certificate plus login credentials — reportedly recoverable in cleartext from the desktop or browser rather than held in an OS certificate store — which the attackers then used as valid, MFA-satisfied access to a customer-facing web application. In the first incident that access ran 66 targeted lookups (~23 customers). In the second, days later, the attackers pivoted from the primary (protected) search API to an unprotected secondary API invoked by the same search function and "executed about 2 million total requests following an enumeration logic, i.e. progressively incrementing the customer code identifier ('customerId')," compromising 365,048 customers and, for 41,359 of them, payment-instrument data ([Garante, 2026-07-16](https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/10263796)). The Garante rejected Wind Tre's defense that its API design followed OWASP practice, finding the enumeration-reachable secondary endpoints were "reasonably identifiable" by a vulnerability assessment and penetration test scoped to the API surface — not just the primary documented interfaces.

**Defender takeaway:** the chain is entirely transferable to any organization with a retail/field-agent access model and a customer-lookup web application, and it turns on two failures a SOC can act on independent of Wind Tre. First, credential/certificate custody: client certificates and service credentials recoverable in cleartext from an endpoint are stealable via a single social-engineered remote-access session — they belong in an encrypted store, KMS or HSM. Second, the object-level-authorization gap on a secondary API that the primary UI silently calls: security testing that exercises only documented primary interfaces misses exactly the endpoint an attacker finds by observing the app's own client behaviour. **Triage:** benign customer-lookup traffic is bounded and non-sequential; the discriminator here is volume and sequence — a single authenticated session issuing hundreds of thousands to millions of requests that increment an object identifier monotonically, against an endpoint with no rate-limiting or CAPTCHA, is enumeration, not use.
