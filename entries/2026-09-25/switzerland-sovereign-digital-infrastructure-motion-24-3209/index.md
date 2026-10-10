---
schema: 1
kind: policy
title: "Switzerland's parliament refers a motion ordering a sovereign government cloud and independent data-exchange platform to the Federal Council, over the Federal Council's own recommendation to reject it"
headline: "Swiss parliament sends a sovereign-cloud mandate to the Federal Council despite its own recommendation to reject it"
summary: >
  Switzerland's Federal Assembly referred motion 24.3209 to the Federal Council on 2026-09-23 after
  the National Council adopted it by 126 votes to 66, following the Council of States' 31:11 vote in
  March 2026. The motion instructs the Federal Council to submit a legal revision enabling a
  federally co-financed sovereign cloud service and an independent data-exchange platform to host
  administration, industry and critical-infrastructure data inside Switzerland, over the Federal
  Council's own recommendation to reject it. No operational obligation exists yet; the Federal
  Council must still draft the requested legislation.
discovered_at: "2026-09-25T04:27:00Z"
updated_at: null
event_date: "2026-09-23"
run_id: 2026-09-25T0404Z-intel
priority: notable
immediate_action: null
tags: [policy]
regions: [switzerland]
sectors: [public-sector]
entities: ["policy:switzerland-sovereign-digital-infrastructure-motion-2026"]
techniques: []
affected_products: []
cves: []
sources:
  - url: "https://ws.parlament.ch/odata.svc/Business(ID=20243209,Language='DE')/BusinessStates?$format=json"
    publisher: "Swiss Federal Assembly — Curia Vista OData service (motion 24.3209 status record)"
    date: "2026-09-23"
    role: primary
  - url: "https://www.lauxlawyers.ch/it-recht-in-der-herbstsession-2026/"
    publisher: "Laux Lawyers AG"
    date: "2026-09"
    role: corroborating
  - url: "https://www.netzwoche.ch/news/2026-03-23/staenderat-sagt-ja-zu-souveraener-ki-infrastruktur"
    publisher: "Netzwoche (report of 2026-03-23, updated 2026-09-25)"
    date: "2026-09-25"
    role: corroborating
closed_sources: []
evidence:
  - quote: "\"BusinessStatusId\": 209, \"BusinessStatusName\": \"Überwiesen an den Bundesrat\", \"BusinessStatusDate\": \"/Date(1790187732000)/\""
    publisher: "Swiss Federal Assembly — Curia Vista OData service (motion 24.3209 status record)"
    source_url: "https://ws.parlament.ch/odata.svc/Business(ID=20243209,Language='DE')/BusinessStates?$format=json"
  - quote: "The motion demands a legal revision so that the federal government, together with cantons, research institutions and the private sector, can advance, co-finance, steer and monitor the build-out of a sovereign digital infrastructure. In particular, an independent cloud service and an independent exchange platform are envisaged, to host data from companies, administration and critical infrastructure inside Switzerland where possible."
    original: "Die Motion verlangt eine Gesetzesrevision, damit der Bund gemeinsam mit Kantonen, Forschungsinstitutionen und Privatwirtschaft den Aufbau einer souveränen digitalen Infrastruktur vorantreiben, mitfinanzieren, steuern und überwachen kann. Vorgesehen sind insbesondere ein eigenständiger Cloud-Dienst sowie eine unabhängige Austauschplattform, um Daten von Unternehmen, Verwaltung und kritischen Infrastrukturen möglichst in der Schweiz zu hosten."
    publisher: "Laux Lawyers AG (translated from German)"
    source_url: "https://www.lauxlawyers.ch/it-recht-in-der-herbstsession-2026/"
verification: multi-source
sourcing_note: null
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions: []
updates:
  - at: "2026-09-30T07:02:46Z"
    run_id: 2026-09-30T0639Z-audit
    type: correction
    summary: >
      The Laux Lawyers quote is now given in English, as its translation label said, and a reference to the readers now names Swiss federal, cantonal and communal organizations. The
      Federal Council's reasoning is narrowed to what Netzwoche reports: a Swiss solo effort is
      unworkable and the request is partly met by EMBAG Article 11 and the digital-sovereignty
      postulate. The National Council's 126 to 66 adoption, with the committee minority's view that
      the existing legal bases suffice, is added. Netzwoche is cited as its report of 2026-03-23
      reads after the update of 2026-09-25, which holds the National Council vote.
    fields: [body, summary, sources]
migrated_from: null
---

Switzerland's Federal Assembly's own Curia Vista record for motion 24.3209, "Für eine souveräne digitale Infrastruktur in der Schweiz im Zeitalter der künstlichen Intelligenz" (for a sovereign digital infrastructure in Switzerland in the age of artificial intelligence), shows its status moved to "Überwiesen an den Bundesrat" (referred to the Federal Council) on 2026-09-23, with the National Council's own committee deliberation on the motion recorded as concluded shortly before ([Swiss Federal Assembly, Curia Vista, 2026-09-23](https://ws.parlament.ch/odata.svc/Business(ID=20243209,Language='DE')/BusinessStates?$format=json)). The Council of States adopted the motion first, in March 2026, by a 31:11 vote ([Netzwoche, 2026-09-25](https://www.netzwoche.ch/news/2026-03-23/staenderat-sagt-ja-zu-souveraener-ki-infrastruktur)); Netzwoche's update of 2026-09-25 reports that the National Council followed by 126 votes to 66, after its committee backed the motion 13 to 12 and a committee minority argued that "the existing legal bases suffice" (translated from German) ([Netzwoche, 2026-09-25](https://www.netzwoche.ch/news/2026-03-23/staenderat-sagt-ja-zu-souveraener-ki-infrastruktur)). Both chambers thus adopted it despite the Federal Council formally recommending rejection. The motion instructs the Federal Council to submit a legal revision letting the federal government, cantons, research institutions and the private sector jointly advance, co-finance, steer and monitor a sovereign digital infrastructure, specifically an independent cloud service and an independent data-exchange platform intended to host administration, industry and critical-infrastructure data inside Switzerland ("The motion requires a legal revision so that the federal government, together with the cantons, research institutions and the private sector, can advance, co-finance, steer and monitor the build-out of a sovereign digital infrastructure," translated from German, [Laux Lawyers AG, 2026-09](https://www.lauxlawyers.ch/it-recht-in-der-herbstsession-2026/)). The Federal Council's recommendation to reject called a Swiss solo effort unworkable and held the request partly met already, citing Article 11 of the EMBAG federal e-government act and parliament's adoption of a postulate for a digital-sovereignty strategy ([Netzwoche, 2026-09-25](https://www.netzwoche.ch/news/2026-03-23/staenderat-sagt-ja-zu-souveraener-ki-infrastruktur)).

This is a directional, strategic-level signal rather than an immediate operational obligation: the Federal Council must still draft and pass the legislation before any sovereign-cloud or exchange-platform requirement takes effect. It is nonetheless the trigger event for a legislative process that will determine where and by whom federal, cantonal and critical-infrastructure workloads may legally be hosted, with downstream implications for data-residency and supply-chain risk assessments across Swiss federal, cantonal and communal organizations. Public-sector IT and procurement teams tracking Swiss Government Cloud planning should treat this motion as the point at which a domestic-hosting requirement moved from proposal to a parliamentary mandate the Federal Council cannot simply decline.

## Correction — 2026-09-30T07:02:46Z

The National Council adopted the motion by 126 votes to 66, following a 13 to 12 majority in its committee; the committee minority held that the existing legal bases suffice (translated from German) ([Netzwoche, 2026-09-25](https://www.netzwoche.ch/news/2026-03-23/staenderat-sagt-ja-zu-souveraener-ki-infrastruktur)). The Federal Council's case for rejection was narrower than the earlier text said: it called a Swiss solo effort unworkable and considered the request only partly met by Article 11 of the EMBAG and the digital-sovereignty postulate ([Netzwoche, 2026-09-25](https://www.netzwoche.ch/news/2026-03-23/staenderat-sagt-ja-zu-souveraener-ki-infrastruktur)).
