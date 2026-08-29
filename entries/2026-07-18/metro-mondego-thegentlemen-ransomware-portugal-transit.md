---
schema: 1
kind: incident
title: "TheGentlemen ransomware hits Portugal's Metro Mondego (Coimbra light-rail); operator confirms attack, notifies CNCS and CNPD"
headline: "Metro Mondego confirms a 6 July ransomware attack on internal systems — transport operation unaffected; TheGentlemen claims data theft"
summary: >
  Metro Mondego, the public operator of the Metrobus light-rail service between Lousã and Coimbra
  (Portugal), confirmed on 2026-07-17 that a ransomware attack on 6 July affected part of its internal
  systems without compromising transport operation. The RaaS group TheGentlemen (Microsoft: Storm-2697)
  claimed the attack and data theft on its leak site. Metro Mondego activated incident response with
  external experts and notified Portugal's national cyber authority (CNCS), the data-protection
  authority (CNPD) and criminal investigators; it cannot yet confirm whether personal data was copied,
  but says passenger payment data was not affected. A clean EU public-transport incident showing IT/OT
  segmentation holding.
discovered_at: "2026-07-18T04:35:00Z"
event_date: "2026-07-17"
run_id: 2026-07-18T0409Z-intel
priority: notable
immediate_action: null
tags: [ransomware, data-breach, organized-crime]
regions: [europe]
sectors: [transport, public-sector]
entities: ["actor:thegentlemen"]
techniques: [T1486, T1567]
affected_products: []
cves: []
sources:
  - url: "https://www.campeaoprovincias.pt/2026/07/17/metro-mondego-foi-alvo-de-ataque-informatico-que-afectou-sistemas-internos/"
    publisher: "Campeão das Províncias (relaying Metro Mondego's statement)"
    date: "2026-07-17"
    role: primary
  - url: "https://tugatech.com.pt/t87569-metro-mondego-e-alvo-de-alegado-ataque-informatico-com-roubo-de-dados"
    publisher: "TugaTech"
    date: "2026-07-16"
    role: corroborating
closed_sources: []
evidence:
  - quote: "A Metro Mondego anunciou esta sexta-feira que foi alvo de um ataque informático a 6 de Julho que afectou “parte dos seus sistemas internos”, mas sem comprometer a operação do serviço de transporte."
    publisher: "Campeão das Províncias"
  - quote: "A ação foi reivindicada pelo grupo de cibercriminosos Thegentlemen, que afirma ter conseguido extrair documentação confidencial"
    publisher: "TugaTech"
verification: multi-source
sourcing_note: "Multi-source: Metro Mondego's own public statement (victim-own disclosure, relayed by Campeão das Províncias) confirms the ransomware attack, the notifications and the impact scope; the TheGentlemen (Storm-2697) attribution and the data-theft claim are reported by TugaTech from the group's leak-site listing. TheGentlemen is registry-tracked; the actor's exfiltration claim is not yet independently confirmed."
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

Metro Mondego — the public operator of the Metrobus light-rail line between Lousã and Coimbra, Portugal — announced on 2026-07-17 that it was hit by a ransomware attack on 6 July that affected "part of its internal systems" without compromising the transport service ("um ataque informático a 6 de Julho que afectou 'parte dos seus sistemas internos', mas sem comprometer a operação do serviço de transporte") ([Campeão das Províncias, 2026-07-17](https://www.campeaoprovincias.pt/2026/07/17/metro-mondego-foi-alvo-de-ataque-informatico-que-afectou-sistemas-internos/)). The operator confirms it activated incident-response procedures with external cybersecurity experts and notified the competent authorities — Portugal's National Cybersecurity Centre (CNCS), the National Data Protection Commission (CNPD) and criminal-investigation authorities — and that its investigation is examining whether the attackers copied data from the affected internal systems; it cannot yet determine whether any personal data of passengers, employees or suppliers is involved, but states passenger payment data was not affected ([Campeão das Províncias, 2026-07-17](https://www.campeaoprovincias.pt/2026/07/17/metro-mondego-foi-alvo-de-ataque-informatico-que-afectou-sistemas-internos/)). The attack was claimed by the ransomware-and-extortion group **TheGentlemen** (Microsoft: Storm-2697; registry-tracked), which posted that it extracted confidential documentation and threatened to publish absent payment ([TugaTech, 2026-07-16](https://tugatech.com.pt/t87569-metro-mondego-e-alvo-de-alegado-ataque-informatico-com-roubo-de-dados)).

**Defender takeaway:** the operationally useful detail for CH/EU public-transport operators is that Metro Mondego is explicit its transport service was not compromised while corporate "internal systems" were — evidence that segmentation between the back-office/IT estate and the operational transport environment held, which is exactly the boundary a transit operator's ransomware playbook depends on. The disclosure also models the correct sequence: precautionary containment, national-CSIRT (CNCS) plus DPA (CNPD) notification, and staged public disclosure as the investigation progresses. **Triage:** the operator is also warning passengers to watch for follow-on fraud in its name — suspicious messages or calls claiming to be Metro Mondego, or requests for payment, bank-detail changes, codes or passwords — a reminder that a back-office ransomware event routinely spawns downstream social-engineering against the victim's customers regardless of whether personal data is confirmed exfiltrated.
