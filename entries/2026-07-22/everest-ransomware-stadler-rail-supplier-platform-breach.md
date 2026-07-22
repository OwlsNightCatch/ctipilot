---
schema: 1
kind: incident
horizon: operational
title: "Everest ransomware breaches a Stadler Rail supplier data-exchange platform, demands CHF 10 million — the Swiss rail manufacturer refuses to pay"
headline: "Everest reaches Stadler Rail through a supplier's data-exchange platform, not Stadler's own perimeter"
summary: >
  Stadler Rail, the Swiss rolling-stock manufacturer headquartered in Bussnang (Thurgau), disclosed on
  2026-07-21 that the Russian-speaking double-extortion group Everest compromised a data-exchange platform
  it shares with a supplier and demanded a CHF 10 million ransom. Stadler refused to pay, filed a criminal
  complaint, and states its own IT and worldwide production were unaffected and no security-relevant or
  personal data was stolen. It is another home-region breach reached through a trusted third-party channel
  rather than the primary victim's network.
discovered_at: "2026-07-22T04:34:31Z"
event_date: "2026-07-21"
run_id: 2026-07-22T0409Z-intel
priority: notable
immediate_action: null
tags: [ransomware, data-breach, supply-chain, organized-crime]
regions: [switzerland, europe]
sectors: [transport, manufacturing]
entities: [actor:everest-ransomware, incident:stadler-rail-everest-supplier-breach-2026]
techniques: [T1199]
affected_products: []
cves: []
sources:
  - url: "https://www.swissinfo.ch/ger/cyberkriminelle-greifen-thurgauer-zugbauer-stadler-rail-an/91776656"
    publisher: "swissinfo.ch"
    date: "2026-07-21"
    role: primary
  - url: "https://www.itmagazine.ch/artikel/87645/Ransomware-Attacke_Stadler_Rail_hat_nicht_gezahlt.html"
    publisher: "Swiss IT Magazine"
    date: "2026-07-21"
    role: corroborating
  - url: "https://www.halcyon.ai/threat-group/everest"
    publisher: "Halcyon"
    date: "2025-11-19"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Ein von der cyberkriminellen Everest Group gefordertes Lösegeld in Höhe von zehn Millionen Franken bezahlte die Firma laut Mitteilung nicht"
    publisher: "swissinfo.ch"
  - quote: "Die Produktion laufe aktuell weltweit normal weiter"
    publisher: "swissinfo.ch"
verification: multi-source
sourcing_note: "Incident facts are from Stadler's own public statement (Mitteilung) as relayed by swissinfo.ch (Swiss public broadcaster) and Swiss IT Magazine; the Everest attribution rests on the group's own claim as reported. Stadler did not name the supplier or the platform, and no intrusion-mechanism details were disclosed."
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

Stadler Rail disclosed on 2026-07-21 that unauthorised parties gained access, in mid-July, to a **data-exchange platform Stadler uses with an (unnamed) supplier**, and that the Everest ransomware/extortion group claimed the intrusion and demanded a **CHF 10 million** ransom ([swissinfo.ch, 2026-07-21](https://www.swissinfo.ch/ger/cyberkriminelle-greifen-thurgauer-zugbauer-stadler-rail-an/91776656)). Stadler states it does not pay ransoms under any circumstances, has filed a criminal complaint with Thurgau cantonal police, and reports that its own IT systems were unharmed, no security-relevant or personal data was stolen, and worldwide rail-vehicle production and in-service fleets are unaffected — the accessed information belonged to the supplier and is described as not security-relevant ([Swiss IT Magazine, 2026-07-21](https://www.itmagazine.ch/artikel/87645/Ransomware-Attacke_Stadler_Rail_hat_nicht_gezahlt.html)).

Everest is a Russian-speaking, closed-group double-extortion operation that emerged in December 2020, with a code-level connection to the BlackByte ransomware family; it has run hybrid Initial Access Broker services since November 2021 and a corporate-insider recruitment programme offering cash/profit-sharing since October 2023, and its documented infection vectors are internet-exposed RDP without MFA, vulnerable VPN endpoints, and credentials bought from other brokers ([Halcyon, 2025-11-19](https://www.halcyon.ai/threat-group/everest)). Per the same profile the group claimed, in October 2025, attacks on critical infrastructure including a European national electricity transmission operator, aviation systems affecting multiple European airports (Heathrow, Brussels and Berlin), and telecommunications networks — recurring targeting of the European critical-infrastructure and transport space, though those victim claims are the group's own leak-site assertions and are unconfirmed by the named organisations.

**Defender takeaway:** the operationally important fact for peers is the vector, not the victim — a well-resourced extortion actor reached a Swiss transport manufacturer's supplier-side data without touching Stadler's own network, by compromising a B2B data-exchange integration. This is the same trusted-relationship pattern (mapped as T1199) behind several recent home-region incidents. Treat supplier and partner data-exchange platforms as part of your own attack surface in third-party risk reviews, and note that Stadler's refusal-to-pay posture only holds because its own systems and backups were intact — the exposure that mattered here sat in a shared platform outside its direct control.
