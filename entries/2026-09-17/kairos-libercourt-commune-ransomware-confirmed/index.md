---
schema: 1
kind: incident
title: "A small French commune confirms a ransomware attack and data theft, days after the extortion actor Kairos claimed it on its leak site"
headline: "Ville de Libercourt confirms data exfiltration; Kairos claimed the commune on its leak site two weeks earlier"
summary: >
  The Ville de Libercourt (Pas-de-Calais, France) confirmed on 2026-09-15 a ransomware attack in
  late August 2026 with personal-data exfiltration. The Kairos ransomware group had listed the commune on its leak site on 2026-09-02, and no party has attributed the confirmed
  intrusion to Kairos beyond that leak-site claim and its timing. The commune names no access
  vector, ransomware group or data scope; CNIL and ANSSI have been notified.
discovered_at: "2026-09-17T04:37:00Z"
updated_at: null
event_date: "2026-09-15"
run_id: 2026-09-17T0409Z-intel
priority: routine
immediate_action: null
tags: [ransomware, data-breach, organized-crime]
regions: [europe]
sectors: [public-sector]
entities: ["incident:libercourt-kairos-ransomware-breach-2026-08", "actor:kairos-extortion", "incident:velilla-san-antonio-kairos-breach-2026-08"]
techniques: [T1486]
affected_products: []
cves: []
sources:
  - url: "https://frenchbreaches.com/alertes/ville-de-libercourt-mu3s726lzo8j6uv1ta"
    publisher: "FrenchBreaches"
    date: "2026-09-16"
    role: primary
  - url: "https://www.ransomware.live/id/VmlsbGUgZGUgTGliZXJjb3VydEBrYWlyb3M="
    publisher: "Ransomware.live"
    date: "2026-09-02"
    role: corroborating
  - url: "https://www.escudodigital.com/ciberseguridad/kairos-asegura-haber-robado-776-gb-de-datos-del-ayuntamiento-de-velilla-de-san-antonio.html"
    publisher: "Escudo Digital"
    date: "2026-08-21"
    role: corroborating
closed_sources: []
evidence:
  - quote: "It is confirmed that personal data was exfiltrated. (translated from French)"
    original: "Il est confirmé que des données personnelles ont été exfiltrées."
    publisher: "Ville de Libercourt (relayed by FrenchBreaches)"
  - quote: "Ransomware.live discovered on 2026-09-02 that Ville de Libercourt has been claimed by Kairos ransomware group"
    publisher: "Ransomware.live"
verification: single-source
sourcing_note: "The commune's statement, relayed by FrenchBreaches, is the sole source for the confirmed attack and exfiltration. Ransomware.live corroborates only the leak-site listing's date and actor, and Escudo Digital reports Kairos's earlier municipal claims."
confidence: medium
references: ["2026-08-22/kairos-velilla-san-antonio-second-madrid-municipality"]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: C
  credibility: 2
watchlist_hit: false
actions: []
updates:
  - at: "2026-09-30T06:56:03Z"
    run_id: 2026-09-30T0639Z-audit
    type: correction
    summary: >
      Priority recalibrated from notable to routine: a French commune ransomware confirmation with
      no vector, actor tradecraft or behaviour defenders can act on. The body is cut to the
      confirmed facts: no source identifies a shared IT-provider gap or ties the Libercourt
      intrusion to Kairos beyond its listing, the summary no longer calls Kairos a data-theft-only
      actor, the takeaway leads with the decision it supports, and the source reliability matches
      FrenchBreaches' standing as an aggregator.
    fields: [priority, body, classification, sources, sourcing_note, summary]
migrated_from: null
---

The Ville de Libercourt (Pas-de-Calais, France) announced on 2026-09-15 a ransomware attack in late August 2026 with confirmed exfiltration of personal data, naming no access vector, group or data scope; it notified CNIL and ANSSI and says its IT provider ran the technical checks ([FrenchBreaches, 2026-09-16](https://frenchbreaches.com/alertes/ville-de-libercourt-mu3s726lzo8j6uv1ta)). The extortion actor Kairos had listed the commune on its leak site on 2026-09-02 ([Ransomware.live, 2026-09-02](https://www.ransomware.live/id/VmlsbGUgZGUgTGliZXJjb3VydEBrYWlyb3M=)), after claiming the Madrid-region municipalities of Valdemoro in May and Velilla de San Antonio in August ([Escudo Digital, 2026-08-21](https://www.escudodigital.com/ciberseguridad/kairos-asegura-haber-robado-776-gb-de-datos-del-ayuntamiento-de-velilla-de-san-antonio.html)), but no source attributes the Libercourt intrusion to Kairos beyond that listing.

**Defender takeaway:** treat a leak-site listing that names your organization as an incident trigger: here the listing came thirteen days before the commune's own confirmation. Kairos has now listed three small municipal administrations in France and Spain, the same victim class as Swiss communes, and with no vector published there is nothing to hunt.

## Correction — 2026-09-30T06:56:03Z

Neither municipal case identifies a gap in an IT provider's detection or notification: Libercourt says its provider ran the technical checks ([FrenchBreaches, 2026-09-16](https://frenchbreaches.com/alertes/ville-de-libercourt-mu3s726lzo8j6uv1ta)), and Velilla de San Antonio said it had activated its security protocols and was still establishing what happened ([Escudo Digital, 2026-08-21](https://www.escudodigital.com/ciberseguridad/kairos-asegura-haber-robado-776-gb-de-datos-del-ayuntamiento-de-velilla-de-san-antonio.html)). The earlier takeaway's claim that both cases share such a gap, and its reference to limited in-house IT staffing, had no source and are withdrawn.
