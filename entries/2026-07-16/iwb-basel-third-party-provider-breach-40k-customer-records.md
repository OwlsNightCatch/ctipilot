---
schema: 1
kind: incident
title: "Basel utility IWB: ~40,000 customer records exfiltrated in a breach of a third-party service provider"
headline: "Swiss municipal energy/water/telecom utility IWB discloses a third-party-provider breach exposing ~40,000 customer meter records"
summary: >
  Industrielle Werke Basel (IWB) — the canton-owned Basel utility supplying electricity, gas,
  water and telecom — disclosed on 2026-07-15 that an external service provider was compromised
  and roughly 40,000 customer records (names, addresses, meter numbers and installation
  characteristics) were exfiltrated. Email addresses, phone numbers, consumption data and
  payment details were not exposed, IWB's own systems and supply were unaffected, and the
  Basel-Stadt data protection officer assessed the misuse risk as low. No provider name, actor
  or initial-access vector has been disclosed.
discovered_at: "2026-07-16T04:38:00Z"
event_date: "2026-07-15"
run_id: 2026-07-16T0409Z-intel
priority: notable
immediate_action: null
tags: [data-breach, supply-chain]
regions: [switzerland]
sectors: [energy, water, telco, public-sector]
entities: [incident:iwb-basel-service-provider-breach-2026-07]
techniques: [T1199]
affected_products: []
cves: []
sources:
  - url: "https://www.netzwoche.ch/news/2026-07-15/cyberangriff-auf-dienstleister-trifft-industrielle-werke-basel"
    publisher: "Netzwoche"
    date: "2026-07-15"
    role: primary
  - url: "https://www.swisscybersecurity.net/news/2026-07-15/cyberangriff-auf-dienstleister-trifft-industrielle-werke-basel"
    publisher: "SwissCybersecurity.net"
    date: "2026-07-15"
    role: corroborating
  - url: "https://www.watson.ch/schweiz/digital/404373086-kundendaten-der-industriellen-werke-basel-entwendet"
    publisher: "Watson.ch"
    date: "2026-07-15"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Bei einem Cyberangriff auf einen Dienstleister der Industriellen Werke Basel (IWB) haben Cyberkriminelle rund 40'000 Datensätze von Kundinnen und Kunden des Energieversorgers entwendet."
    publisher: "Netzwoche"
  - quote: "Die IWB-Systeme blieben unversehrt, wie das Unternehmen mitteilt. Auch die Energieversorgung sei nicht beeinträchtigt gewesen."
    publisher: "Netzwoche"
verification: multi-source
sourcing_note: "Three Swiss outlets (Netzwoche and its sister title SwissCybersecurity.net; the independent Watson.ch) report consistent facts, all tracing to IWB's own disclosure — no independent forensic confirmation beyond the utility's statement. Named data fields and the low-risk assessment are cited to IWB via the Basel-Stadt data protection officer."
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
migrated_from: null
---

Industrielle Werke Basel (IWB) — the canton-owned Basel multi-utility supplying electricity, gas, water, district heating and telecom/fibre — disclosed on 15 July 2026 that an external service provider it uses was compromised and roughly **40,000 customer records** were exfiltrated from the provider's environment ([Netzwoche, 2026-07-15](https://www.netzwoche.ch/news/2026-07-15/cyberangriff-auf-dienstleister-trifft-industrielle-werke-basel)). The stolen data comprises customer names and addresses plus technical smart-meter attributes (meter serial numbers and installation characteristics); IWB states that email addresses, phone numbers, energy-consumption data and billing/payment data were **not** part of the exposure, so no consumption-pattern inference is possible from what was taken ([SwissCybersecurity.net, 2026-07-15](https://www.swisscybersecurity.net/news/2026-07-15/cyberangriff-auf-dienstleister-trifft-industrielle-werke-basel)). IWB's own IT and OT/grid systems were unaffected and energy/water supply continuity was not disrupted — the compromise is scoped to the provider's systems and the customer-data feed IWB shares with it ([Netzwoche, 2026-07-15](https://www.netzwoche.ch/news/2026-07-15/cyberangriff-auf-dienstleister-trifft-industrielle-werke-basel)). The provider detected and notified IWB, which audited access, reviewed logs and pre-emptively restricted its data exchange with the affected provider; the Basel-Stadt cantonal data protection officer assessed the misuse risk as low ([Watson.ch, 2026-07-15](https://www.watson.ch/schweiz/digital/404373086-kundendaten-der-industriellen-werke-basel-entwendet)). No provider name, threat-actor claim or initial-access vector has been disclosed, and no matching leak-site listing was found for Switzerland in-window.

**Defender takeaway:** this is a textbook trusted-relationship exposure — a home-region critical-infrastructure operator's customer data reached attackers through a compromised external processor the utility's own SOC has no telemetry into. For any utility or public-sector body outsourcing metering/billing data, the load-bearing controls are contractual data-minimisation (share only the fields the processor needs), a right to breach notification and log access, and periodic review of what customer data actually sits outside the perimeter. The exposed name+address+meter-number combination is exactly the material for convincing pretext contact, so affected customers should be warned to treat unsolicited approaches referencing their address or meter number — especially demands for money or data under time pressure — with suspicion.
