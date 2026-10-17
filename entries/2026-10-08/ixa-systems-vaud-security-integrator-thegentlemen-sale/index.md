---
schema: 1
kind: incident
title: "Ixa Systems, a Vaud security integrator serving police, prisons and banks: camera locations, plans and some passwords that TheGentlemen claimed to have stolen are reported on sale on the darknet"
headline: "Site plans, camera locations and some credentials of Vaud prisons and banks, and of police premises, reported for sale"
summary: >
  Le Temps reports, and the AWP news agency names the firm as Ixa Systems of Crissier (Vaud), that data stolen from
  a video-surveillance, alarm and access-control integrator is on sale on the darknet; the group TheGentlemen
  claimed the theft at the end of August. The loot reportedly includes camera locations, security-installation
  plans and, in some cases, usernames or passwords, for clients including police authorities, gendarmerie
  premises, prisons, hospitals, schools and banks; the reports do not state the access vector or list every affected site.
discovered_at: "2026-10-08T04:52:00Z"
updated_at: null
event_date: "2026-10-06"
run_id: 2026-10-08T0404Z-intel
priority: notable
immediate_action: null
tags: [ransomware, supply-chain, data-breach]
regions: [switzerland]
sectors: [public-sector, technology]
entities: ["actor:thegentlemen", "incident:ixa-systems-thegentlemen-2026-08"]
techniques: [T1657]
affected_products: []
cves: []
sources:
  - url: "https://www.letemps.ch/suisse/vaud/une-cyberattaque-fait-fuiter-des-informations-de-securite-de-prisons-vaudoises-de-banques-et-de-dizaines-de-societes"
    publisher: "Le Temps"
    date: "2026-10-06"
    role: primary
  - url: "https://www.ictjournal.ch/news/2026-10-07/une-cyberattaque-expose-des-donnees-de-securite-de-sites-vaudois"
    publisher: "ICTjournal"
    date: "2026-10-07"
    role: corroborating
  - url: "https://www.cash.ch/news/top-news/hacker-erbeuten-schweizer-sicherheitsdaten-von-gefangnissen-und-banken-974664"
    publisher: "AWP via cash.ch"
    date: "2026-10-07"
    role: corroborating
  - url: "https://www.inside-it.ch/daten-von-westschweizer-gefaengnissen-und-banken-im-darknet-20261007"
    publisher: "Inside IT"
    date: "2026-10-07"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: >
  Le Temps is paywalled; the detail on clients and statements comes from ICTjournal and the AWP wire, which both
  report its article. Inside IT
  reports the claim and the publication from its own sources. The firm's name rests on the AWP report; the
  outlets differ on whether the data was offered for sale on 25 September or published at the end of September.
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "If your organisation bought video-surveillance, alarm or access-control installation or maintenance from Ixa Systems, ask the firm in writing which of your sites and credentials are in the stolen data and rotate every camera, alarm, intercom and remote-maintenance credential it held."
updates: []
migrated_from: null
---

Le Temps reports that data stolen in a ransomware attack on a Vaud security-technology firm is now on sale on the darknet, and that the loot includes the locations of surveillance cameras, passwords and plans of security installations ([Le Temps, 2026-10-06](https://www.letemps.ch/suisse/vaud/une-cyberattaque-fait-fuiter-des-informations-de-securite-de-prisons-vaudoises-de-banques-et-de-dizaines-de-societes)). The AWP agency names the firm as Ixa Systems of Crissier, which specialises in video surveillance, access control and burglary protection and whose customers include police authorities, banks, hospitals, schools and prisons ([AWP via cash.ch, 2026-10-07](https://www.cash.ch/news/top-news/hacker-erbeuten-schweizer-sicherheitsdaten-von-gefangnissen-und-banken-974664)). ICTjournal lists the Établissements de la plaine de l'Orbe and other judicial entities, gendarmerie premises, several banks including the Banque cantonale vaudoise and several dozen companies among the organisations concerned, and says exposure varies: for some clients the documents are limited to tenders or consultations, for others they give the location of cameras or the layout of alert buttons ([ICTjournal, 2026-10-07](https://www.ictjournal.ch/news/2026-10-07/une-cyberattaque-expose-des-donnees-de-securite-de-sites-vaudois)).

Le Temps says the group TheGentlemen announced and claimed the theft on the darknet at the end of August ([Le Temps, 2026-10-06](https://www.letemps.ch/suisse/vaud/une-cyberattaque-fait-fuiter-des-informations-de-securite-de-prisons-vaudoises-de-banques-et-de-dizaines-de-societes)). Inside IT dates the claim to 28 August and says the group made good on its threat to publish the data at the end of September ([Inside IT, 2026-10-07](https://www.inside-it.ch/daten-von-westschweizer-gefaengnissen-und-banken-im-darknet-20261007)), while ICTjournal says the documents were put on sale on 25 September and that, according to an expert's analysis seen by Le Temps, some of the data has begun to circulate ([ICTjournal, 2026-10-07](https://www.ictjournal.ch/news/2026-10-07/une-cyberattaque-expose-des-donnees-de-securite-de-sites-vaudois)). The firm says it never lost use of its data, paid no ransom and that the attack gave no direct access to camera images; the canton's cybersecurity delegate says checks so far have found nothing that would compromise the security of the establishments concerned or give access to the State's IT environment, and that knowing a camera model is not enough to exploit it because the device must be reachable ([ICTjournal, 2026-10-07](https://www.ictjournal.ch/news/2026-10-07/une-cyberattaque-expose-des-donnees-de-securite-de-sites-vaudois)). None of the reports states how the attackers got in.

**Exposure:** organisations whose cameras, alarms or access control were installed or maintained by Ixa Systems; the reports name only a few clients (the Établissements de la plaine de l'Orbe and the Banque cantonale vaudoise among them) and otherwise describe client categories, and none says which credentials in the data are still valid ([ICTjournal, 2026-10-07](https://www.ictjournal.ch/news/2026-10-07/une-cyberattaque-expose-des-donnees-de-securite-de-sites-vaudois)).

**Detection:** because the data reportedly holds usernames, passwords and camera locations, the telemetry is the authentication log of video-management, alarm and access-control systems (logins from unfamiliar source networks or from the supplier's accounts) and the log of any remote-maintenance path the supplier used ([Le Temps, 2026-10-06](https://www.letemps.ch/suisse/vaud/une-cyberattaque-fait-fuiter-des-informations-de-securite-de-prisons-vaudoises-de-banques-et-de-dizaines-de-societes); [ICTjournal, 2026-10-07](https://www.ictjournal.ch/news/2026-10-07/une-cyberattaque-expose-des-donnees-de-securite-de-sites-vaudois)).

**Defender takeaway:** ask the supplier in writing whether your sites are in the data, treat every camera, alarm, intercom and remote-maintenance credential it held as exposed and rotate it, and confirm that the devices are not reachable from outside a segmented network, the point the canton's delegate makes ([ICTjournal, 2026-10-07](https://www.ictjournal.ch/news/2026-10-07/une-cyberattaque-expose-des-donnees-de-securite-de-sites-vaudois)).
