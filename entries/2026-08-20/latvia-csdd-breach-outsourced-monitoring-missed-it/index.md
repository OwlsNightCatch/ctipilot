---
schema: 1
kind: incident
title: "Latvia's vehicle-registration authority lost payment records on two-thirds of the country's population — and the provider contractually watching its infrastructure round the clock did not notice"
headline: "CSDD's own staff found the intrusion and stopped it in hours; the outsourced monitoring never raised it, and the supervisory board has resigned"
summary: >
  Latvia's Road Traffic Safety Directorate (CSDD), the national vehicle-registration and driver-licensing
  authority, states that between 8 and 10 August 2026 an attacker obtained payment-receipt data going back to
  2008 on 1.2 million individuals and 200,000 legal entities — roughly two-thirds of Latvia's population.
  Names, personal identity codes, payment amounts and dates, licence plates and registered addresses were
  taken; phone numbers, email addresses, usernames and passwords were not. CSDD's own staff discovered and
  stopped the intrusion within hours, while its outsourced IT provider, contracted for round-the-clock
  monitoring, neither detected it nor alerted the agency. CERT.LV assesses the attack was targeted and preceded
  by preparation; a second targeted attempt the following weekend was blocked. The supervisory board has
  resigned and the agency's chief intends to.
discovered_at: "2026-08-20T05:02:00Z"
event_date: "2026-08-18"
run_id: 2026-08-20T0409Z-intel
priority: high
immediate_action: null
tags: [data-breach, vulnerabilities]
regions: [europe]
sectors: [public-sector, transport]
entities: [incident:latvia-csdd-breach-2026]
techniques: [T1190]
affected_products: []
cves: []
sources:
  - url: "https://cert.lv/lv/2026/08/csdd-saskaries-ar-kiberdrosibas-incidentu"
    publisher: "CERT.LV"
    date: "2026-08-18"
    role: primary
  - url: "https://therecord.media/latvia-cyberattack-vehicle-data"
    publisher: "The Record (Recorded Future News)"
    date: "2026-08-19"
    role: corroborating
  - url: "https://news.inbox.eu/150n4c8-why-tet-did-not-warn-csdd-about-the-cyberattack-the-company-commented-on-the-situation-for-the-first-time"
    publisher: "inbox.eu"
    date: "2026-08-19"
    role: corroborating
closed_sources: []
evidence:
  - quote: "laika posmā no 2026. gada 8. līdz 10. augustam (ieskaitot) kiberuzbrucējs ir ieguvis informāciju par maksājumu kvītīs ietvertiem datiem laika periodā no 2008. gada. CSDD norāda, ka ietekmēti 1,2 miljonu fizisko personu un 200 tūkstošu juridisko personu dati."
    publisher: "CERT.LV"
  - quote: "He said Tet did not detect the intrusion or alert the agency. Instead, CSDD employees discovered the attack themselves and stopped it within several hours."
    publisher: "The Record (Recorded Future News)"
verification: multi-source
sourcing_note: >
  CERT.LV's bulletin mirrors CSDD's own statements of 13 and 18 August and is the authority for the intrusion
  window, the record counts and the data categories. The access path is not in CERT.LV's written bulletin: The
  Record attributes it to CERT.LV speaking to Latvian public broadcaster LSM, and that is the only basis for
  describing the entry point as an internet-exposed system, which is why the technique mapping rests on that
  attribution rather than on the advisory text. Two source discrepancies are carried rather than reconciled: the
  Latvian outlet inbox.eu dates the attack to the night of 7-8 August, a day earlier than the 8-10 August window
  CSDD and CERT.LV state, and it sequences the executive board's resignation before the supervisory board's,
  where The Record reports only the supervisory board's resignation as complete and the chief executive's as
  intended. No actor has been named by any party, and no CVE, product or vendor appears in any source.
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
actions:
  - "For every outsourced monitoring, SOC or MDR contract, establish on paper which systems and network segments the provider is actually obliged to watch, what it is obliged to alert on, and within what time — then test it with an authorised detection exercise inside a segment you believe is covered. The failure mode here was not an undetected technique but a boundary nobody had checked: the provider states its responsibility covered only certain parts of the infrastructure, not the whole network."
migrated_from: null
---

Latvia's Road Traffic Safety Directorate — CSDD, the state authority for vehicle registration and driver licensing — states that between 8 and 10 August 2026 inclusive an attacker obtained the data held in payment receipts going back to 2008, affecting 1.2 million natural persons and 200,000 legal entities ([CERT.LV, 2026-08-18](https://cert.lv/lv/2026/08/csdd-saskaries-ar-kiberdrosibas-incidentu)). Latvia's population is a little over 1.8 million, so that is roughly two-thirds of the country ([The Record, 2026-08-19](https://therecord.media/latvia-cyberattack-vehicle-data)). What was taken is the combination that makes downstream fraud convincing rather than generic: personal identity code or company registration number, name, payment amount and date, vehicle licence-plate number, and the address registered at the time of the transaction. CSDD is explicit about what was not taken — customer contact details, meaning phone numbers and email addresses, were unaffected, the recovered address data is incomplete in some cases, and its earlier statement records that customer usernames and passwords were not compromised ([CERT.LV, 2026-08-18](https://cert.lv/lv/2026/08/csdd-saskaries-ar-kiberdrosibas-incidentu)).

The detection story is the part with a transferable lesson, and it runs the opposite way to the one an outsourcing arrangement is bought to produce. CSDD's own employees found the intrusion and stopped it within several hours; the agency's outsourced IT provider, Tet, did not detect it and did not alert the agency ([The Record, 2026-08-19](https://therecord.media/latvia-cyberattack-vehicle-data)). The agency's chief describes the five-year contract as covering IT infrastructure maintenance and monitoring including some firewall and incident-monitoring functions ([The Record, 2026-08-19](https://therecord.media/latvia-cyberattack-vehicle-data)), and as stipulating round-the-clock monitoring of the infrastructure ([inbox.eu, 2026-08-19](https://news.inbox.eu/150n4c8-why-tet-did-not-warn-csdd-about-the-cyberattack-the-company-commented-on-the-situation-for-the-first-time)). Tet's own response is where the gap becomes legible: it says it is too early to draw conclusions about causes, states that its contractual responsibility extends only to certain parts of CSDD's IT infrastructure rather than the agency's whole network, has not disclosed how that scope was drawn, and confirms it engaged two subcontractors to fulfil the contract ([inbox.eu, 2026-08-19](https://news.inbox.eu/150n4c8-why-tet-did-not-warn-csdd-about-the-cyberattack-the-company-commented-on-the-situation-for-the-first-time)). Nobody disputes that monitoring was contracted; what nobody had established, before it mattered, was the boundary of what "monitored" covered.

CERT.LV's own assessment is that the attack was targeted and preceded by preparation, and that the attackers showed technical competence; the entry point, per CERT.LV speaking to Latvian public broadcaster LSM, was a vulnerability in a CSDD system exposed to the internet, on which several mandatory cybersecurity requirements had not been met ([The Record, 2026-08-19](https://therecord.media/latvia-cyberattack-vehicle-data)). No CVE, product or vendor has been named. CSDD also disclosed that it faced a further targeted attack the following weekend, which was blocked thanks to the security improvements made in the interim ([CERT.LV, 2026-08-18](https://cert.lv/lv/2026/08/csdd-saskaries-ar-kiberdrosibas-incidentu)) — a reminder that a disclosed public-sector breach draws follow-on attempts while remediation is still in flight. The institutional consequences have been fast: the supervisory board resigned on the Wednesday morning after calls to do so from the President and a member of parliament, and the agency's chief says he intends to resign once the investigation and its consequences are dealt with ([The Record, 2026-08-19](https://therecord.media/latvia-cyberattack-vehicle-data)).

**Defender takeaway:** two things carry across to any administration that outsources detection. First, a monitoring contract is only as good as the asset boundary written into it, and that boundary is worth reading before an incident rather than after — here the provider and the customer clearly held different pictures of it, and the disagreement only surfaced once something went unnoticed. Second, CERT.LV's guidance to citizens is the operationally useful half for anyone handling the fallout of a similar leak: because a national identity code doubles as the user identifier for national e-signature and mobile-authentication schemes, the realistic downstream attack is a well-tailored authentication push or a personalised phishing message built from the leaked identity, plate and payment history. CERT.LV tells affected people never to approve an authentication request they did not themselves initiate, advises those whose e-signature user number is their identity code to change it to a random number, and tells them to reach the agency by navigating to its official site rather than following a link ([CERT.LV, 2026-08-18](https://cert.lv/lv/2026/08/csdd-saskaries-ar-kiberdrosibas-incidentu)). That is the shape of the next wave for a public body that has just lost an authoritative citizen dataset, and it is worth having the messaging ready before it arrives.
