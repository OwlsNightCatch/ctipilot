---
schema: 1
kind: research
title: "NTC finds default passwords, fleet-wide shared credentials and unauthenticated grid-feed shutoff across Swiss solar inverters, with a named cantonal procurement gap"
headline: "Switzerland's national cybersecurity test institute finds most tested solar inverters let an unauthenticated user zero out grid feed-in"
summary: >
  Switzerland's National Test Institute for Cybersecurity (NTC) published a year-long assessment
  (2026-09-17) of seven inverters and four energy-management systems from eight manufacturers,
  finding 50+ vulnerabilities (7 critical, 6 high) including unauthenticated local-interface
  power-output control down to zero on nearly all tested devices; canton Bern's own procurement
  admits cybersecurity is barely anchored in its tender process for a cantonal school's PV
  installation.
discovered_at: "2026-09-18T04:54:00Z"
updated_at: null
event_date: "2026-09-17"
run_id: 2026-09-18T0410Z-intel
priority: high
immediate_action: null
tags: [ot-ics, vulnerabilities, default-config]
regions: [switzerland]
sectors: [energy, public-sector]
entities: ["report:ntc-photovoltaic-cybersecurity-2026"]
techniques: [T1078.001]
affected_products: []
cves: []
sources:
  - url: "https://en.ntc.swiss/news/cybersecurity-of-photovoltaic-systems"
    publisher: "National Test Institute for Cybersecurity (NTC), Switzerland"
    date: "2026-09-17"
    role: primary
  - url: "https://www.srf.ch/news/schweiz/risiko-cyberangriffe-sicherheitsexperten-blackout-risiko-wegen-solaranlagen"
    publisher: "SRF (Rundschau)"
    date: "2026-09-16"
    role: corroborating
  - url: "https://www.cash.ch/news/studie-findet-kritische-cyberlucken-bei-schweizer-solaranlagen-969350"
    publisher: "cash.ch (AWP)"
    date: "2026-09-17"
    role: corroborating
closed_sources: []
evidence:
  - quote: "In total, the assessments produced more than 50 findings, seven of them critical and a further six rated high."
    publisher: "National Test Institute for Cybersecurity (NTC)"
    source_url: "https://en.ntc.swiss/news/cybersecurity-of-photovoltaic-systems"
  - quote: "On almost every inverter tested, the local control interface makes it possible — without any login — to change how much power the installation feeds into the grid, all the way down to zero."
    publisher: "National Test Institute for Cybersecurity (NTC)"
    source_url: "https://en.ntc.swiss/news/cybersecurity-of-photovoltaic-systems"
  - quote: "on four products, the NTC gained complete control over the device"
    publisher: "National Test Institute for Cybersecurity (NTC)"
    source_url: "https://en.ntc.swiss/news/cybersecurity-of-photovoltaic-systems"
  - quote: "If the Chinese manufacturers were to simultaneously switch off all their devices at full power, a collapse of the Swiss power grid would threaten. (translated from German)"
    original: "Würden die chinesischen Hersteller alle ihre Geräte bei voller Leistung gleichzeitig abschalten, drohe ein Zusammenbruch des Stromnetzes in der Schweiz."
    publisher: "SRF (Rundschau)"
    source_url: "https://www.srf.ch/news/schweiz/risiko-cyberangriffe-sicherheitsexperten-blackout-risiko-wegen-solaranlagen"
  - quote: "Asked about this, the Baudirektion writes that it did not specify the manufacturer. It does concede, however, that cybersecurity is \"still barely anchored\" in tenders. (translated from German)"
    original: "Auf Anfrage schreibt die Baudirektion, man habe den Hersteller nicht vorgegeben. Sie räumt aber ein, Cybersicherheit sei bei Ausschreibungen «noch wenig verankert»."
    publisher: "SRF (Rundschau)"
    source_url: "https://www.srf.ch/news/schweiz/risiko-cyberangriffe-sicherheitsexperten-blackout-risiko-wegen-solaranlagen"
verification: multi-source
sourcing_note: >
  The findings originate in a single assessment: the National Test Institute for Cybersecurity ran
  the tests and published the report. SRF and cash.ch report on that study rather than testing the
  devices themselves, and the Federal Office of Energy endorsed the analysis rather than conducting
  its own, so the corroboration is editorial rather than a second assessment.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
updates:
  - at: "2026-09-20T13:29:09Z"
    run_id: 2026-09-20T1308Z-audit
    type: correction
    summary: >
      Credibility was rated 1 (corroborated by independent sources). Every cited source traces to the
      National Test Institute for Cybersecurity's own study: SRF and cash.ch report on it and the Federal
      Office of Energy endorsed it, and none of them re-tested the inverters. That is one assessor with
      several publishers, which rates 2. A sourcing note now records the provenance. The findings
      themselves were re-verified against the institute's own publication and are unchanged.
    fields: [classification, sourcing_note]
migrated_from: null
---

Switzerland's National Test Institute for Cybersecurity (NTC) published a year-long technical security assessment (2026-09-17) of seven solar inverters and four energy-management systems from eight manufacturers, of the kind installed in thousands of Swiss homes ([NTC, 2026-09-17](https://en.ntc.swiss/news/cybersecurity-of-photovoltaic-systems)) among Switzerland's roughly 338,000 grid-connected photovoltaic installations ([cash.ch, 2026-09-17](https://www.cash.ch/news/studie-findet-kritische-cyberlucken-bei-schweizer-solaranlagen-969350)). Testing produced more than 50 findings, seven critical and six high, with full device takeover on four of the eleven products ([NTC, 2026-09-17](https://en.ntc.swiss/news/cybersecurity-of-photovoltaic-systems)). The recurring weaknesses: default passwords, maintenance access using identical credentials across an entire device fleet, weak or missing encryption on local-interface communication, and interfaces that cannot be disabled. On almost every inverter tested, the local control interface let an unauthenticated actor change how much power the installation feeds into the grid, down to zero, with no login required ([NTC, 2026-09-17](https://en.ntc.swiss/news/cybersecurity-of-photovoltaic-systems)); NTC found no evidence of intentionally built-in backdoors, per its own statement, framing the risk instead as manufacturer-cloud concentration ([cash.ch, 2026-09-17](https://www.cash.ch/news/studie-findet-kritische-cyberlucken-bei-schweizer-solaranlagen-969350)) — because most inverters stay permanently connected to a handful of manufacturer clouds for remote management, compromising one manufacturer's cloud could let an attacker trigger the same unauthenticated shutdown across every connected installation simultaneously, turning a fleet of individually low-value consumer devices into de facto critical grid infrastructure. NTC founder Raphael Reischuk states that if the Chinese manufacturers were to simultaneously switch off all their devices at full power, a collapse of the Swiss power grid would threaten (translated from German) ([Raphael Reischuk, NTC, via SRF, 2026-09-16](https://www.srf.ch/news/schweiz/risiko-cyberangriffe-sicherheitsexperten-blackout-risiko-wegen-solaranlagen)), and Switzerland's Federal Office of Energy independently confirms NTC's risk assessment, per SRF ([SRF, 2026-09-16](https://www.srf.ch/news/schweiz/risiko-cyberangriffe-sicherheitsexperten-blackout-risiko-wegen-solaranlagen)).

The market-concentration and procurement angle is directly relevant to Swiss public-sector buyers: Huawei and Sungrow together hold over 60% of the Swiss inverter market, Switzerland's Federal Intelligence Service (NDB) warns the country risks becoming a preferred target if it protects critical infrastructure less than the EU, and canton Bern's own cantonal building authority admits that a public tender for a cantonal vocational school's rooftop solar installation was structured such that only a Huawei inverter could qualify, conceding that cybersecurity is still barely anchored in tenders (translated from German) ([Kanton Bern Baudirektion, via SRF, 2026-09-16](https://www.srf.ch/news/schweiz/risiko-cyberangriffe-sicherheitsexperten-blackout-risiko-wegen-solaranlagen)). The EU has withdrawn subsidy eligibility for Chinese-inverter projects and the US has declared a grid emergency that can force removal of already-installed sanctioned-country inverters ([SRF, 2026-09-16](https://www.srf.ch/news/schweiz/risiko-cyberangriffe-sicherheitsexperten-blackout-risiko-wegen-solaranlagen)). NTC deliberately withheld product names and technical exploit detail, reporting findings confidentially to manufacturers, and states most manufacturers responded quickly to the disclosure while work to fix the vulnerabilities remains under way for some products ([NTC, 2026-09-17](https://en.ntc.swiss/news/cybersecurity-of-photovoltaic-systems)); cash.ch separately reports manufacturers have already closed the gaps (translated from German) ([cash.ch, 2026-09-17](https://www.cash.ch/news/studie-findet-kritische-cyberlucken-bei-schweizer-solaranlagen-969350)). No CVEs were assigned to any of the findings, and neither NTC nor cash.ch names one ([NTC, 2026-09-17](https://en.ntc.swiss/news/cybersecurity-of-photovoltaic-systems); [cash.ch, 2026-09-17](https://www.cash.ch/news/studie-findet-kritische-cyberlucken-bei-schweizer-solaranlagen-969350)).

**Defender takeaway:** any cantonal or communal procurement of solar, PV or building-management technology should now require a documented minimum device-security standard in the tender specification, and disable or network-isolate local maintenance interfaces on installed inverters — the exact gap canton Bern's own Baudirektion admits it lacked.

## Correction — 2026-09-20T13:29:09Z

The corroboration behind this entry is editorial rather than independent, and its credibility rating now says so. The National Test Institute for Cybersecurity ran the tests and published the findings; SRF and cash.ch report on that study rather than testing the devices themselves, and the Federal Office of Energy endorsed the institute's analysis rather than conducting its own. That is one assessor with several publishers, so the rating moves from confirmed to probably true. Every figure in the entry was re-checked against the institute's own publication and none of them changes ([National Test Institute for Cybersecurity, 2026-09-17](https://en.ntc.swiss/news/cybersecurity-of-photovoltaic-systems)).
