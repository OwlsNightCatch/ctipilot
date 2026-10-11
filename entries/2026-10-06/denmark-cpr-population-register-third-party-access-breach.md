---
schema: 1
kind: incident
title: "Denmark's CPR population register: unauthorised parties abused a small private company's lawful lookup access, where Politiken reports at least three accounts used the password 123456, and obtained names, addresses and CPR numbers of 8.8 million people"
headline: "A Danish company's register access, reportedly secured with the password 123456, was abused to obtain 8.8 million CPR numbers"
summary: >
  Denmark's CPR administration says unauthorised parties used a private Danish company's lawful right to search the Central
  Person Register to obtain names, addresses and CPR numbers of about 8.8 million of its roughly 11 million records (living,
  deceased and emigrated persons); the ministry says the access does not cover the names and addresses of people with
  name-and-address protection. The company, Pays ApS of Odense, confirmed to TV 2 that its lawful access was abused, and
  Politiken reports that at least three of its accounts, including the administrator account, used the password 123456; Ritzau
  puts the access at 21 days and 17 hours from 10 September, where the minister had described about ten days. An anonymous
  hacker told Politiken the access began with a leaked former employee's password, which is the hacker's claim, and Datatilsynet
  describes a very large number of automated lookups made to identify valid CPR numbers.
discovered_at: "2026-10-06T04:57:00Z"
updated_at: "2026-10-11T03:40:00Z"
event_date: "2026-10-02"
run_id: 2026-10-06T0405Z-intel
priority: notable
immediate_action: null
tags: [data-breach]
regions: [europe]
sectors: [public-sector]
entities: ["incident:denmark-cpr-register-third-party-access-2026-10"]
techniques: [T1199, T1078, T1213, T1119]
affected_products: []
cves: []
sources:
  - url: "https://via.ritzau.dk/pressemeddelelse/15205753/omfattende-uautoriseret-adgang-til-borgeres-cpr-oplysninger"
    publisher: "Danish Ministry of Research, Education and Digitalisation"
    date: "2026-10-05"
    role: primary
  - url: "https://fagligsenior.dk/2026/10/05/cpr-laek-i-ti-dage-minister-erkender-svigt-i-sikkerheden/"
    publisher: "Faglig Senior (Ritzau)"
    date: "2026-10-05"
    role: corroborating
  - url: "https://www.datatilsynet.dk/presse-og-nyheder/nyhedsarkiv/2026/okt/datatilsynet-er-opmaerksom-paa-sag-om-opslag-i-cpr"
    publisher: "Datatilsynet (Danish Data Protection Agency)"
    date: "2026-10-05"
    role: corroborating
  - url: "https://www.dr.dk/nyheder/indland/live-uvedkommende-har-haft-adgang-til-millioner-af-cpr-numre"
    publisher: "DR Nyheder"
    date: "2026-10-06"
    role: corroborating
  - url: "https://cphpost.dk/2026-10-10/news/round-up/123456-password-used-in-massive-danish-cpr-data-breach/"
    publisher: "The Copenhagen Post (Ritzau)"
    date: "2026-10-10"
    role: corroborating
  - url: "https://www.tv4.se/artikel/tt-261008-danmarkintrang1-2cc02852/hackare-sa-gick-danska-jatteintranget-till"
    publisher: "TV4 Nyheterna (TT)"
    date: "2026-10-08"
    role: corroborating
closed_sources: []
evidence:
  - quote: "By abusing a Danish company's lawful access to search for information in the CPR system, unauthorised parties have obtained names, addresses, CPR numbers and more on about 8.8 million registered citizens in the CPR system. (translated from Danish)"
    original: "Ved at misbruge en dansk virksomheds lovlige adgang til at søge oplysninger i CPR-systemet, har uvedkommende skaffet sig adgang til navne, adresser, CPR-numre mv. på ca. 8,8 millioner registrerede borgere i CPR-systemet."
    publisher: "Danish Ministry of Research, Education and Digitalisation"
    source_url: "https://via.ritzau.dk/pressemeddelelse/15205753/omfattende-uautoriseret-adgang-til-borgeres-cpr-oplysninger"
  - quote: "It is clear to me that the security measures around this company's access to CPR have not been good enough. (translated from Danish)"
    original: "Det er tydeligt for mig, at sikkerhedsforanstaltningerne omkring denne virksomheds adgang til CPR ikke har været gode nok"
    publisher: "Faglig Senior (Ritzau)"
    source_url: "https://fagligsenior.dk/2026/10/05/cpr-laek-i-ti-dage-minister-erkender-svigt-i-sikkerheden/"
  - quote: "The notification states that a very large number of automated lookups were made against the CPR system in order to identify valid CPR numbers. (translated from Danish)"
    original: "Det fremgår af anmeldelsen, at der er foretaget et meget stort antal automatiserede opslag mod CPR-systemet med henblik på at identificere gyldige CPR-numre."
    publisher: "Datatilsynet (Danish Data Protection Agency)"
    source_url: "https://www.datatilsynet.dk/presse-og-nyheder/nyhedsarkiv/2026/okt/datatilsynet-er-opmaerksom-paa-sag-om-opslag-i-cpr"
  - quote: "It was an expensive invoice that hinted a breach had happened, not systematic alarms. (translated from Danish)"
    original: "Det var en dyr faktura, der gav hint om, at der var sket et brud - ikke systematiske alamer."
    publisher: "DR Nyheder"
    source_url: "https://www.dr.dk/nyheder/indland/live-uvedkommende-har-haft-adgang-til-millioner-af-cpr-numre"
  - quote: "At least three accounts at the company linked to a major breach of Denmark’s CPR register reportedly used the password “123456”, including an administrator account."
    publisher: "The Copenhagen Post (Ritzau)"
    source_url: "https://cphpost.dk/2026-10-10/news/round-up/123456-password-used-in-massive-danish-cpr-data-breach/"
  - quote: "The hacker had access to the CPR register from 10 September for a total of 21 days and 17 hours."
    publisher: "The Copenhagen Post (Ritzau)"
    source_url: "https://cphpost.dk/2026-10-10/news/round-up/123456-password-used-in-massive-danish-cpr-data-breach/"
  - quote: "We can confirm that we are the company that has been subjected to an attack where our legal access to search for information in the CPR system has been abused"
    publisher: "The Copenhagen Post (Ritzau)"
    source_url: "https://cphpost.dk/2026-10-10/news/round-up/123456-password-used-in-massive-danish-cpr-data-breach/"
verification: single-source-victim
sourcing_note: >
  The Danish ministry and the CPR administration, which runs the register, disclose the incident themselves; Datatilsynet relays
  the register's notification and DR's live blog reports the authorities' press briefing of 2026-10-06. The company's name is its
  own confirmation to TV 2 as relayed by Ritzau, the password finding is Politiken's reporting as relayed by Ritzau, the 21-day
  access window is Ritzau's statement, and the account of how access began is an anonymous hacker's claim to Politiken.
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
  - at: "2026-10-07T04:51:00Z"
    run_id: 2026-10-07T0404Z-intel
    type: update
    summary: >
      Datatilsynet's notice says the register reported a very large number of automated lookups made to identify valid CPR
      numbers, and at the 2026-10-06 press briefing the authorities said a costly invoice rather than systematic alarms hinted at
      the breach, that police visited a smaller company in person and contacted foreign police, and that the CPR number can no
      longer be used to authenticate a person. Police are examining whether an algorithm or AI was used; the actor, the company
      and how the access was obtained are still not public.
    fields: [summary, techniques, sources, evidence, sourcing_note, body]
  - at: "2026-10-11T03:40:00Z"
    run_id: 2026-10-11T0256Z-intel
    type: update
    summary: >
      The abused company is Pays ApS of Odense, which confirmed it to TV 2; Politiken reports that at least three of its accounts,
      including the administrator account, used the password 123456, and an anonymous hacker says access began with a leaked
      former employee's password, a claim. Ritzau puts the access at 21 days and 17 hours from 10 September, where the minister
      had described about ten days.
    fields: [title, headline, summary, techniques, sources, evidence, sourcing_note, body]
migrated_from: null
---

Denmark's CPR administration noticed irregular behaviour in the register on the evening of Friday 2026-10-02, learned over the weekend that unauthorised parties had obtained names, addresses and CPR numbers of about 8.8 million registered persons, and says the access worked by misusing a Danish private company's lawful right to search the register, within the scope of data that private companies may access (translated from Danish) ([Danish Ministry of Research, Education and Digitalisation, 2026-10-05](https://via.ritzau.dk/pressemeddelelse/15205753/omfattende-uautoriseret-adgang-til-borgeres-cpr-oplysninger)). The register holds about 11 million records, covering living, deceased and emigrated persons, and the ministry says the unauthorised access does not cover the names and addresses of people registered with name-and-address protection; CPR stopped the company's access, reported the incident to the Danish data protection authority, and the police are investigating, with no statement yet on who is behind it ([Danish Ministry of Research, Education and Digitalisation, 2026-10-05](https://via.ritzau.dk/pressemeddelelse/15205753/omfattende-uautoriseret-adgang-til-borgeres-cpr-oplysninger)). Under section 38 of the CPR Act a private company with a legitimate interest may receive information on a larger delimited group of persons that it has identified individually in advance, by CPR number, date of birth and name, or by name and address ([Danish Ministry of Research, Education and Digitalisation, 2026-10-05](https://via.ritzau.dk/pressemeddelelse/15205753/omfattende-uautoriseret-adgang-til-borgeres-cpr-oplysninger)).

The digitalisation minister told Ritzau the access lasted about ten days in September and ran through a smaller Danish company, that an employee of the CPR administration spotted the unusual activity on 2 October, and that red lights should have lit when it went on for so long; she declined to say whether the investigation sees criminal intent at the company ([Faglig Senior (Ritzau), 2026-10-05](https://fagligsenior.dk/2026/10/05/cpr-laek-i-ti-dage-minister-erkender-svigt-i-sikkerheden/)). Ritzau later reported that the hacker had access from 10 September for a total of 21 days and 17 hours ([The Copenhagen Post (Ritzau), 2026-10-10](https://cphpost.dk/2026-10-10/news/round-up/123456-password-used-in-massive-danish-cpr-data-breach/)). Datatilsynet, the Danish data protection authority, says the register's notification describes a very large number of automated lookups made to identify valid CPR numbers (translated from Danish) ([Datatilsynet, 2026-10-05](https://www.datatilsynet.dk/presse-og-nyheder/nyhedsarkiv/2026/okt/datatilsynet-er-opmaerksom-paa-sag-om-opslag-i-cpr)). The company is Pays ApS of Odense, and Politiken reports that at least three of its accounts, including the administrator account, used the password 123456 ([The Copenhagen Post (Ritzau), 2026-10-10](https://cphpost.dk/2026-10-10/news/round-up/123456-password-used-in-massive-danish-cpr-data-breach/)); an anonymous hacker says the access began with a leaked password of a former employee of a small Danish company, which is the hacker's own account of events (see the update below).

**Exposure:** about 8.8 million of the register's roughly 11 million records (the ministry says the access does not cover the names and addresses of people with name-and-address protection); the ministry warns recipients never to hand out passwords or other confidential information in calls or emails, even when the caller knows their name, address and CPR number ([Danish Ministry of Research, Education and Digitalisation, 2026-10-05](https://via.ritzau.dk/pressemeddelelse/15205753/omfattende-uautoriseret-adgang-til-borgeres-cpr-oplysninger)). The same exposure exists for any register or portal that gives private parties lookup access: the third party's access path is what the attacker used, so a weakness there is a weakness in the register.

**Detection:** access and audit logs of the register's lookup interface, aggregated per authorised party (queries per day, distinct subjects looked up, breadth of fields returned, share of lookups that miss) and compared with that party's declared purpose. The sources describe an employee noticing irregular behaviour on 2 October, after access that the minister put at about ten days in September ([Faglig Senior (Ritzau), 2026-10-05](https://fagligsenior.dk/2026/10/05/cpr-laek-i-ti-dage-minister-erkender-svigt-i-sikkerheden/)) and Ritzau later at 21 days and 17 hours ([The Copenhagen Post (Ritzau), 2026-10-10](https://cphpost.dk/2026-10-10/news/round-up/123456-password-used-in-massive-danish-cpr-data-breach/)), and the minister acknowledging that red lights should have lit earlier ([Faglig Senior (Ritzau), 2026-10-05](https://fagligsenior.dk/2026/10/05/cpr-laek-i-ti-dage-minister-erkender-svigt-i-sikkerheden/)); DR reports that an expensive invoice, not systematic alarms, gave the first hint ([DR Nyheder, 2026-10-06](https://www.dr.dk/nyheder/indland/live-uvedkommende-har-haft-adgang-til-millioner-af-cpr-numre)).

**Defender takeaway:** registry operators and the companies that hold lookup access should treat each authorised third party's access path as an attack path, with per-party volume ceilings and an alert on departure from the declared scope; people and organisations that handle citizen data should expect the leaked identifiers to make impersonation calls and emails more convincing, and should not accept knowledge of a CPR number as proof of identity, which a Danish agency director now says it no longer is ([DR Nyheder, 2026-10-06](https://www.dr.dk/nyheder/indland/live-uvedkommende-har-haft-adgang-til-millioner-af-cpr-numre)). The reported use of 123456 on the company's administrator account shows that password quality on the accounts that hold register lookup access is part of the register's own exposure ([The Copenhagen Post (Ritzau), 2026-10-10](https://cphpost.dk/2026-10-10/news/round-up/123456-password-used-in-massive-danish-cpr-data-breach/)).

## Update — 2026-10-07T04:51:00Z

Datatilsynet said on 2026-10-05 that it received the register's notification on Sunday 2026-10-04 and that the notification describes a very large number of automated lookups against the CPR system to identify valid CPR numbers (translated from Danish) ([Datatilsynet, 2026-10-05](https://www.datatilsynet.dk/presse-og-nyheder/nyhedsarkiv/2026/okt/datatilsynet-er-opmaerksom-paa-sag-om-opslag-i-cpr)).

At the press briefing of 2026-10-06, DR reports, the authorities said an expensive invoice, not systematic alarms, hinted that a breach had happened, that police have been to a smaller company in person to collect traces, and that foreign police have been contacted in case foreign actors are behind it; the director of the agency for societal security (Styrelsen for Samfundssikkerhed) said the CPR number can no longer be used to authenticate a person (translated from Danish) ([DR Nyheder, 2026-10-06](https://www.dr.dk/nyheder/indland/live-uvedkommende-har-haft-adgang-til-millioner-af-cpr-numre)). A head of centre at the national police unit NSK said police are looking at whether an algorithm was used, as a hypothesis, because so many lookups were made in a short time, and could not say more ([DR Nyheder, 2026-10-06](https://www.dr.dk/nyheder/indland/live-uvedkommende-har-haft-adgang-til-millioner-af-cpr-numre)). The authorities did not say who is behind the breach, how it happened or whose access was misused ([DR Nyheder, 2026-10-06](https://www.dr.dk/nyheder/indland/live-uvedkommende-har-haft-adgang-til-millioner-af-cpr-numre)).

## Update — 2026-10-11T03:40:00Z

Pays ApS, a company in Odense that had two employees as of July 2026 according to Denmark's Central Business Register, confirmed to TV 2 on 2026-10-09 that it is the company whose lawful access to search the CPR system was abused ([The Copenhagen Post (Ritzau), 2026-10-10](https://cphpost.dk/2026-10-10/news/round-up/123456-password-used-in-massive-danish-cpr-data-breach/)). Politiken, which reviewed data from the breach that the hacker allegedly used, reports that at least three user accounts at Pays used the password 123456, one of them the administrator account, and an Aarhus University professor called the company's password security hopeless ([The Copenhagen Post (Ritzau), 2026-10-10](https://cphpost.dk/2026-10-10/news/round-up/123456-password-used-in-massive-danish-cpr-data-breach/)).

An anonymous hacker told Politiken that they were behind the attack and that access was first obtained with a leaked password belonging to a former employee of a small Danish company, after which they allegedly created two programs to retrieve information from the CPR system and store it externally; the article does not say that this was a Pays employee, and it is the hacker's account, not a finding ([The Copenhagen Post (Ritzau), 2026-10-10](https://cphpost.dk/2026-10-10/news/round-up/123456-password-used-in-massive-danish-cpr-data-breach/)). TT reports that the experts Politiken interviewed consider it likely that the hacker was involved in the breach (translated from Swedish) ([TV4 Nyheterna (TT), 2026-10-08](https://www.tv4.se/artikel/tt-261008-danmarkintrang1-2cc02852/hackare-sa-gick-danska-jatteintranget-till)). Ritzau reports that the hacker had access from 10 September for a total of 21 days and 17 hours, which differs from the minister's earlier description of about ten days ([The Copenhagen Post (Ritzau), 2026-10-10](https://cphpost.dk/2026-10-10/news/round-up/123456-password-used-in-massive-danish-cpr-data-breach/)).
