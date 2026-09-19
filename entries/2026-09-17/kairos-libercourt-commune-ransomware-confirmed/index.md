---
schema: 1
kind: incident
title: "A small French commune confirms a ransomware attack and data theft, days after the extortion actor Kairos claimed it on its leak site"
headline: "Ville de Libercourt confirms data exfiltration; Kairos claimed the commune on its leak site two weeks earlier"
summary: >
  The Ville de Libercourt (Pas-de-Calais, France) confirmed on 2026-09-15 a ransomware attack in
  late August 2026 with personal-data exfiltration. The data-theft-only extortion actor Kairos had
  listed the commune on its leak site on 2026-09-02; no party has attributed the confirmed
  intrusion to Kairos beyond that leak-site claim and its timing. The commune names no access
  vector, ransomware group or data scope; CNIL and ANSSI have been notified.
discovered_at: "2026-09-17T04:37:00Z"
updated_at: null
event_date: "2026-09-15"
run_id: 2026-09-17T0409Z-intel
priority: notable
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
  - url: "https://ayto-velilla.es/posible-exposicion-de-informacion-en-los-sistemas-del-ayuntamiento-de-velilla-de-san-antonio/"
    publisher: "Ayuntamiento de Velilla de San Antonio"
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
sourcing_note: "The commune's own public statement, relayed verbatim by FrenchBreaches, is the sole source for the confirmed ransomware attack and data exfiltration; no separate municipal press release URL or independent French mainstream press pickup was found. Ransomware.live's own listing corroborates only the leak-site claim's date and actor name, not the technical scope of the confirmed incident — it states no data volume and no access vector. This is an out-of-nexus small foreign commune; see body for the relevance basis."
confidence: medium
references: ["2026-08-22/kairos-velilla-san-antonio-second-madrid-municipality"]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

The Ville de Libercourt, a commune in France's Pas-de-Calais department, announced on 2026-09-15 that it suffered a ransomware attack in late August 2026 and confirmed that personal data was exfiltrated ([FrenchBreaches, 2026-09-16](https://frenchbreaches.com/alertes/ville-de-libercourt-mu3s726lzo8j6uv1ta)). The commune states it detected the threat quickly and had its external IT provider run technical checks, and has since deployed unspecified corrective measures to strengthen server-access security; it says municipal services were not operationally disrupted. It does not confirm the intrusion method, the responsible ransomware group, the categories or volume of exfiltrated data, or whether a ransom was demanded — all stated as still under investigation. The commune has notified France's CNIL and ANSSI, filed a criminal complaint, and is warning residents to watch for phishing attempts using any exfiltrated data ([FrenchBreaches, 2026-09-16](https://frenchbreaches.com/alertes/ville-de-libercourt-mu3s726lzo8j6uv1ta)).

An extortion actor tracked as Kairos listed the commune on its own leak site on 2026-09-02, thirteen days before the commune's confirmation ([Ransomware.live, 2026-09-02](https://www.ransomware.live/id/VmlsbGUgZGUgTGliZXJjb3VydEBrYWlyb3M=)); the listing states no data volume or access vector, and no party — not the commune, not any other source — attributes the confirmed intrusion to Kairos beyond that leak-site claim and its timing. That gap matters here specifically: Kairos's own tracked history is data-theft extortion with no ransomware encryptor ever linked to it, while the commune's statement names a genuine ransomware attack — a tension the sources do not resolve, and one more reason the Kairos link stays a claim, not an attribution. Kairos separately claimed the Madrid-region municipality of Velilla de San Antonio in August 2026; that municipality's own statement confirmed a security incident but was explicit that it could not yet confirm effective data access or extraction had occurred ([Ayuntamiento de Velilla de San Antonio, 2026-08-21](https://ayto-velilla.es/posible-exposicion-de-informacion-en-los-sistemas-del-ayuntamiento-de-velilla-de-san-antonio/)) — a narrower confirmation than Libercourt's, which names exfiltration outright. Taken together, this is now a second small European municipality where a Kairos leak-site claim coincides with a victim's own confirmation of at least a security incident, a pattern consistent with — though not proven to be — this actor opportunistically targeting small local-government administrations that typically run with limited in-house IT security staffing and externally contracted IT support, a profile shared by Swiss cantonal and communal administrations.

**Defender takeaway:** whether or not Kairos is confirmed as the intruder here, the operationally relevant pattern is the target profile — small municipal administrations relying on external IT providers — not a specific actor's tradecraft. A Swiss cantonal or communal IT team's actionable lesson is process: confirm your own externally-contracted IT provider has a documented, tested incident-detection and notification path, since that gap is what both confirmed cases share.
