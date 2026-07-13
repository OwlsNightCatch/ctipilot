---
schema: 1
kind: threat
horizon: operational
title: "France and the EU attribute the Turla intrusion set to FSB Centre 16, with French victimology, TTPs and EU/UK sanctions"
headline: "ANSSI publishes CERTFR-2026-CTI-005 on FSB Centre 16's Turla cluster as France and the EU formally attribute it and sanction AO AST and NPP Gamma"
summary: >
  On 2026-07-13 France (ANSSI/C4) and the EU High Representative formally attributed the Turla intrusion set
  to Russia's FSB 16th Centre, publishing CERT-FR report CERTFR-2026-CTI-005 with French victimology (defence,
  diplomatic, justice and technology entities since 2017) and its spearphishing/watering-hole TTPs; the EU
  sanctioned 9 individuals and 4 organisations (incl. AO AST, NPP Gamma) and the UK sanctioned 24. Companion
  to the morning's Static Tundra router-hijacking advisory — the sibling FSB Centre 16 espionage cluster.
discovered_at: "2026-07-13T20:35:00Z"
event_date: "2026-07-13"
run_id: 2026-07-13T2009Z-intel
priority: notable
immediate_action: null
tags: [nation-state, espionage, phishing, russia-nexus]
regions: [europe, switzerland]
sectors: [public-sector, defense]
entities: [actor:secretblizzard, actor:static-tundra, incident:france-eu-turla-fsb-attribution-2026-07]
techniques: [T1566, T1189, T1204.002, T1190, T1584.004]
affected_products: []
cves: []
sources:
  - url: "https://www.cert.ssi.gouv.fr/cti/CERTFR-2026-CTI-005/"
    publisher: "CERT-FR (ANSSI)"
    date: "2026-07-13"
    role: primary
  - url: "https://cyber.gouv.fr/actualites/ciblage-et-compromission-dentites-francaises-par-le-fsb/"
    publisher: "ANSSI (cyber.gouv.fr)"
    date: "2026-07-13"
    role: primary
  - url: "https://www.defense.gouv.fr/comcyber/actualites/ciblage-compromission-dentites-francaises-au-moyen-du-mode-du-mode-operatoire-dattaque-turla"
    publisher: "Ministère des Armées / COMCYBER"
    date: "2026-07-13"
    role: corroborating
  - url: "https://www.heise.de/en/news/EU-sanctions-Russia-for-serious-cyberattacks-and-sabotage-11363418.html"
    publisher: "heise online"
    date: "2026-07-13"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Members of the Cyber Crisis Coordination Centre (C4) have observed the targeting and compromise of French entities using the Turla intrusion set operated by the 16th Centre of the Federal Security Service of the Russian Federation (FSB)."
    publisher: "CERT-FR (ANSSI)"
  - quote: "Russian technology companies supporting the intelligence service are also affected. For example, Advanced System Technology (AST) and NPP Gamma will no longer be allowed to do business in the EU in the future."
    publisher: "heise online (citing EU Council statement)"
verification: multi-source
sourcing_note: "Primary attribution and French victimology from CERT-FR CERTFR-2026-CTI-005 and ANSSI's newsroom. COMCYBER's page is cited only for the Turla mode being an FSB 16th Centre intelligence MOA active since ≥2004 — it does NOT mention Berserk Bear/Static Tundra or Poland; the parent-unit framing (16th Centre spanning both Turla and the Static Tundra cluster) rests on the heise EU-sanctions coverage (16th Centre 'controls groups like Turla') and the morning Static Tundra advisory. EU sanctions detail (AO AST, NPP Gamma) is carried by heise citing the EU Council statement. heise's paraphrase also mentions 'hijacked Iranian servers', but the CERT-FR CERTFR-2026-CTI-005 PDF (the primary) does not state this, so that detail is deliberately NOT carried. The intermediary-victim range is taken from the CERT-FR PDF ('2019–2025'); ANSSI's newsroom page gives '2021' — the primary is used. The French MFA statement page was reachable but its body sat behind a consent wall and was not extracted."
confidence: high
update_of: 2026-07-13/fsb-centre-16-static-tundra-router-hijacking-advisory
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: null
---

**UPDATE (originally covered 2026-07-13):** The morning entry covered the 19-agency Static Tundra/Berserk Bear advisory (SNMP and Cisco Smart Install router hijacking) and the UK/EU attribution of the December 2025 Polish grid sabotage. This delta covers the **sibling FSB Centre 16 cluster** — Turla — which France and the EU formally attributed the same day. France's Cyber Crisis Coordination Centre (C4 — ANSSI, COMCYBER, DGA, DGSE, DGSI and the Ministry for Europe and Foreign Affairs) and the EU High Representative jointly attributed the Turla intrusion set to the FSB's 16th Centre on 2026-07-13, publishing CERT-FR's technical report CERTFR-2026-CTI-005 alongside formal French and EU attribution statements ([CERT-FR, 2026-07-13](https://www.cert.ssi.gouv.fr/cti/CERTFR-2026-CTI-005/); [ANSSI, 2026-07-13](https://cyber.gouv.fr/actualites/ciblage-et-compromission-dentites-francaises-par-le-fsb/)). France's COMCYBER describes Turla as an FSB 16th Centre attack mode (*mode opératoire*) used for intelligence-gathering since at least 2004 ([COMCYBER, 2026-07-13](https://www.defense.gouv.fr/comcyber/actualites/ciblage-compromission-dentites-francaises-au-moyen-du-mode-du-mode-operatoire-dattaque-turla)). The 16th Centre is the parent unit behind both this Turla/Secret Blizzard espionage set and the Static Tundra/Berserk Bear router-hijacking cluster covered this morning — the EU-sanctions reporting describes the 16th Centre as controlling groups including Turla ([heise online, 2026-07-13](https://www.heise.de/en/news/EU-sanctions-Russia-for-serious-cyberattacks-and-sabotage-11363418.html)).

ANSSI documents French Turla victims including Ministry of Armed Forces webmail accounts compromised since 2017, the network of the French Embassy in Moscow (2018), a justice-sector personnel-training host (2019) and an advanced-technology company (2025), plus opportunistic intermediary compromises across varied sectors between 2019 and 2025 used as relay infrastructure ([CERT-FR, 2026-07-13](https://www.cert.ssi.gouv.fr/cti/CERTFR-2026-CTI-005/)). The initial-access tradecraft combines spearphishing and watering-hole attacks that lure targets into downloading malicious files masquerading as legitimate software, plus exploitation of vulnerabilities in webmail/messaging services, browsers, business applications and web servers; the operators favour rented or previously-compromised infrastructure for camouflage ([ANSSI, 2026-07-13](https://cyber.gouv.fr/actualites/ciblage-et-compromission-dentites-francaises-par-le-fsb/)). In coordination, the EU sanctioned 9 individuals and 4 organisations (entry bans and asset freezes), including the enabler firms Advanced System Technology (AST) and NPP Gamma, and the UK sanctioned 24 individuals and organisations; the EU Council statement names Germany, Poland, Cyprus, the Netherlands, Austria, Slovakia, Romania and Finland among affected states ([heise online, 2026-07-13](https://www.heise.de/en/news/EU-sanctions-Russia-for-serious-cyberattacks-and-sabotage-11363418.html)).

**Defender takeaway:** the operational surface for EU/Swiss government, diplomatic and defence entities is Turla's *access* tradecraft, not the diplomacy — hunt for trojanised "legitimate software" delivered via spearphishing or watering-holes, and for exploitation of exposed webmail, browser and web-server surfaces, which is where this set gets in. The relay-through-compromised-third-parties pattern (opportunistic intermediary victims used as infrastructure) means a Swiss or EU organisation may surface as *staging infrastructure* for onward targeting rather than as the final objective — outbound connections from your estate to other victims' networks, and inbound access that pivots onward, are as much the signal as data leaving toward Russia.
