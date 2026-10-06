---
schema: 1
kind: incident
title: "Denmark's CPR population register: unauthorised parties abused one private company's lawful lookup access for about ten days and obtained names, addresses and CPR numbers of 8.8 million people"
headline: "A Danish company's legitimate register access, abused, exposed 8.8 million people's names, addresses and CPR numbers"
summary: >
  Denmark's CPR administration says unauthorised parties used a private Danish company's lawful right to search the Central
  Person Register to obtain names, addresses and CPR numbers of about 8.8 million of its roughly 11 million records (living,
  deceased and emigrated persons); the ministry says the access does not cover the names and addresses of people with name-and-address protection. The minister told Ritzau the access
  lasted about ten days in September through a smaller company whose security around that access had not been good enough,
  in her words; the actor, the company and the method are not public.
discovered_at: "2026-10-06T04:57:00Z"
updated_at: null
event_date: "2026-10-02"
run_id: 2026-10-06T0405Z-intel
priority: notable
immediate_action: null
tags: [data-breach]
regions: [europe]
sectors: [public-sector]
entities: ["incident:denmark-cpr-register-third-party-access-2026-10"]
techniques: [T1199, T1213]
affected_products: []
cves: []
sources:
  - url: "https://ufm.dk/aktuelt/pressemeddelelser/2026/oktober/omfattende-uautoriseret-adgang-til-borgeres-cpr-oplysninger/"
    publisher: "Danish Ministry of Research, Education and Digitalisation"
    date: "2026-10-05"
    role: primary
  - url: "https://fagligsenior.dk/2026/10/05/cpr-laek-i-ti-dage-minister-erkender-svigt-i-sikkerheden/"
    publisher: "Faglig Senior (Ritzau)"
    date: "2026-10-05"
    role: corroborating
closed_sources: []
evidence:
  - quote: "By abusing a Danish company's lawful access to search for information in the CPR system, unauthorised parties have obtained names, addresses, CPR numbers and more on about 8.8 million registered citizens in the CPR system. (translated from Danish)"
    original: "Ved at misbruge en dansk virksomheds lovlige adgang til at søge oplysninger i CPR-systemet, har uvedkommende skaffet sig adgang til navne, adresser, CPR-numre mv. på ca. 8,8 millioner registrerede borgere i CPR-systemet."
    publisher: "Danish Ministry of Research, Education and Digitalisation"
    source_url: "https://ufm.dk/aktuelt/pressemeddelelser/2026/oktober/omfattende-uautoriseret-adgang-til-borgeres-cpr-oplysninger/"
  - quote: "It is clear to me that the security measures around this company's access to CPR have not been good enough. (translated from Danish)"
    original: "Det er tydeligt for mig, at sikkerhedsforanstaltningerne omkring denne virksomheds adgang til CPR ikke har været gode nok"
    publisher: "Faglig Senior (Ritzau)"
    source_url: "https://fagligsenior.dk/2026/10/05/cpr-laek-i-ti-dage-minister-erkender-svigt-i-sikkerheden/"
verification: single-source-victim
sourcing_note: >
  The Danish ministry and the CPR administration, the party that runs the register, disclose the incident themselves, and the
  minister's Ritzau interview adds the duration and the company's size; both are the same authority speaking. The investigation
  is at an early stage and the ministry says the details may change as the sequence of events is mapped.
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
updates: []
migrated_from: null
---

Denmark's CPR administration noticed irregular behaviour in the register on the evening of Friday 2026-10-02, learned over the weekend that unauthorised parties had obtained names, addresses and CPR numbers of about 8.8 million registered persons, and says the access worked by misusing a Danish private company's lawful right to search the register, within the scope of data that private companies may access (translated from Danish) ([Danish Ministry of Research, Education and Digitalisation, 2026-10-05](https://ufm.dk/aktuelt/pressemeddelelser/2026/oktober/omfattende-uautoriseret-adgang-til-borgeres-cpr-oplysninger/)). The register holds about 11 million records, covering living, deceased and emigrated persons, and the ministry says the unauthorised access does not cover the names and addresses of people registered with name-and-address protection; CPR stopped the company's access, reported the incident to the Danish data protection authority, and the police are investigating, with no statement yet on who is behind it ([Danish Ministry of Research, Education and Digitalisation, 2026-10-05](https://ufm.dk/aktuelt/pressemeddelelser/2026/oktober/omfattende-uautoriseret-adgang-til-borgeres-cpr-oplysninger/)). Under section 38 of the CPR Act a private company with a legitimate interest may receive information on a larger delimited group of persons that it has identified individually in advance, by CPR number, date of birth and name, or by name and address ([Danish Ministry of Research, Education and Digitalisation, 2026-10-05](https://ufm.dk/aktuelt/pressemeddelelser/2026/oktober/omfattende-uautoriseret-adgang-til-borgeres-cpr-oplysninger/)).

The digitalisation minister told Ritzau the access lasted about ten days in September and ran through a smaller Danish company, that an employee of the CPR administration spotted the unusual activity on 2 October, and that red lights should have lit when it went on for so long; she declined to say whether the investigation sees criminal intent at the company ([Faglig Senior (Ritzau), 2026-10-05](https://fagligsenior.dk/2026/10/05/cpr-laek-i-ti-dage-minister-erkender-svigt-i-sikkerheden/)). No source names the company, says how the access was taken over, or says how many queries were made.

**Exposure:** about 8.8 million of the register's roughly 11 million records (the ministry says the access does not cover the names and addresses of people with name-and-address protection); the ministry warns recipients never to hand out passwords or other confidential information in calls or emails, even when the caller knows their name, address and CPR number ([Danish Ministry of Research, Education and Digitalisation, 2026-10-05](https://ufm.dk/aktuelt/pressemeddelelser/2026/oktober/omfattende-uautoriseret-adgang-til-borgeres-cpr-oplysninger/)). The same exposure exists for any register or portal that gives private parties lookup access: the third party's access path is what the attacker used, so a weakness there is a weakness in the register.

**Detection:** access and audit logs of the register's lookup interface, aggregated per authorised party (queries per day, distinct subjects looked up, breadth of fields returned) and compared with that party's declared purpose. The sources describe an employee noticing irregular behaviour on 2 October, after access that had run for about ten days in September, and the minister acknowledging that red lights should have lit earlier ([Faglig Senior (Ritzau), 2026-10-05](https://fagligsenior.dk/2026/10/05/cpr-laek-i-ti-dage-minister-erkender-svigt-i-sikkerheden/)).

**Defender takeaway:** registry operators and the companies that hold lookup access should treat each authorised third party's access path as an attack path, with per-party volume ceilings and an alert on departure from the declared scope; people and organisations that handle citizen data should expect the leaked identifiers to make impersonation calls and emails more convincing.
