---
schema: 1
kind: incident
title: "Danfoss AK-SM and AK-SC, Copeland xweb and Dixell xweb refrigeration controllers compromised, with forced defrost reported at hundreds of French supermarkets; CERT-FR and NCSC Switzerland say to remove internet exposure"
headline: "CERT-FR adds Copeland and Dixell xweb to the hijacked refrigeration controllers; NCSC.ch rates the attacks exploited"
summary: >
  Coopérative U, Intermarché and E. Leclerc confirmed to AFP a cyberattack on their refrigeration systems overnight on 11 to 12 October 2026, which BFMTV reports as a remotely forced defrost at hundreds of stores. CERT-FR's alert, last revised on 2026-10-16, reports numerous compromises of Danfoss AK-SM and AK-SC controllers and of Copeland xweb and Dixell xweb, says campaigns are probably still running and that a factory reset alone does not protect an unpatched end-of-life unit, and in its current text tells owners to check the whole configuration, defrost ranges included, and to restart or otherwise factory-reset a compromised Danfoss unit. NCSC Switzerland rates the activity actively exploited, and Dixell France's operator guide, which CERT-FR links, says any XWEB PRO on firmware 1.12.1 or earlier must be updated without delay. Danfoss says most affected units are legacy products or current AK-SM800A units on outdated firmware; no source names an actor, the flaw or how the attackers got in, and the Paris prosecutor is investigating.
discovered_at: "2026-10-13T03:41:00Z"
updated_at: "2026-10-18T03:33:00Z"
event_date: "2026-10-12"
run_id: 2026-10-13T0256Z-intel
priority: high
immediate_action: null
tags: [ot-ics, actively-exploited]
regions: [europe, switzerland]
sectors: [retail]
entities: ["incident:danfoss-ak-sm-ak-sc-french-supermarket-refrigeration-attack-2026-10", "product:danfoss-ak-sm-800", "product:danfoss-ak-sc-355", "product:danfoss-ak-sm-800a", "product:copeland-xweb", "product:dixell-xweb"]
techniques: [T1190]
affected_products: ["Danfoss AK-SM 800", "Danfoss AK-SC 355", "Danfoss AK-SM 800A", "Copeland xweb", "Dixell xweb"]
cves: []
sources:
  - url: "https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/"
    publisher: "CERT-FR (alert CERTFR-2026-ALE-012)"
    date: "2026-10-12"
    role: primary
  - url: "https://www.afp.com/en/french-supermarket-chains-say-cyberattack-forced-refrigerator-shutdown"
    publisher: "AFP"
    date: "2026-10-12"
    role: corroborating
  - url: "https://www.bfmtv.com/economie/consommation/la-temperature-est-montee-jusqu-a-50-degres-une-cyberattaque-contre-les-systemes-frigorifiques-provoque-la-destruction-de-produits-frais-dans-des-centaines-d-intermarche-et-de-super-u_AN-202610120327.html"
    publisher: "BFMTV"
    date: "2026-10-12"
    role: corroborating
  - url: "https://www.infosecurity-magazine.com/news/french-supermarket-chains/"
    publisher: "Infosecurity Magazine"
    date: "2026-10-12"
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/cyberattack-shuts-down-refrigerators-at-french-supermarkets/"
    publisher: "BleepingComputer"
    date: "2026-10-12"
    role: corroborating
  - url: "https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/"
    publisher: "CERT-FR (alert CERTFR-2026-ALE-012, revised version)"
    date: "2026-10-13"
    role: primary
  - url: "https://security-hub.ncsc.admin.ch/#/posts/13054"
    publisher: "NCSC Switzerland (Security Hub advisory 13054)"
    date: "2026-10-13"
    role: corroborating
  - url: "https://www.coolingpost.com/world-news/danfoss-moves-to-mitigate-cyberattack/"
    publisher: "Cooling Post"
    date: "2026-10-12"
    role: corroborating
  - url: "https://www.blick.ch/fr/suisse/cyberattaque-les-frigos-de-migros-et-coop-sont-ils-proteges/79vpc6q"
    publisher: "Blick"
    date: "2026-10-13"
    role: corroborating
  - url: "https://censys.com/blog/frostbitten-in-france-a-danfoss-storeview-internet-exposure-report/"
    publisher: "Censys"
    date: "2026-10-14"
    role: corroborating
  - url: "https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/"
    publisher: "CERT-FR (alert CERTFR-2026-ALE-012, third version)"
    date: "2026-10-16"
    role: primary
  - url: "https://dixell.fr/wp-content/uploads/2026/10/Recommandations-pour-une-utilisation-securisee-des-superviseurs-XWEB-v1.0.pdf"
    publisher: "Dixell France (Copeland)"
    date: "2026-10-13"
    role: corroborating
closed_sources: []
evidence:
  - quote: "CERT-FR is aware of numerous compromises of the remote refrigeration-installation controllers Danfoss AK-SM and AK-SC series as well as Copeland xweb and Dixell xweb. (translated from French)"
    original: "Le CERT-FR a connaissance de nombreuses compromissions des controleurs à distance d'installation de réfrigération Danfoss série AK-SM, AK-SC ainsi que Copeland xweb et Dixell xweb."
    publisher: "CERT-FR (alert CERTFR-2026-ALE-012)"
    source_url: "https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/"
  - quote: "In an emergency, simply filtering the source IPs of the refrigeration contractors on a firewall is possible, but this solution must not be considered lasting. (translated from French)"
    original: "Dans l'urgence, un simple filtrage des IP sources des prestataires frigoristes sur un pare-feu est possible, mais cette solution ne doit pas être considérée comme pérenne."
    publisher: "CERT-FR (alert CERTFR-2026-ALE-012)"
    source_url: "https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/"
  - quote: "the persistence of a compromised instance will be removed but the equipment will remain vulnerable and will certainly be compromised again. (translated from French)"
    original: "les persistances d'une instance compromise seront supprimées mais l'équipement restera vulnérable et sera certainement de nouveau compromis."
    publisher: "CERT-FR (alert CERTFR-2026-ALE-012)"
    source_url: "https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/"
  - quote: "most of the affected equipment was \"legacy\" products which \"no longer receive software or security updates\""
    publisher: "AFP"
    source_url: "https://www.afp.com/en/french-supermarket-chains-say-cyberattack-forced-refrigerator-shutdown"
  - quote: "the hackers would have hijacked this function by imposing a forced and continuous defrost, with a temperature setpoint fixed at 50 degrees (translated from French)"
    original: "les pirates auraient détourné cette fonction en imposant un dégivrage forcé et continu, avec une consigne de température fixée à 50 degrés"
    publisher: "BFMTV"
    source_url: "https://www.bfmtv.com/economie/consommation/la-temperature-est-montee-jusqu-a-50-degres-une-cyberattaque-contre-les-systemes-frigorifiques-provoque-la-destruction-de-produits-frais-dans-des-centaines-d-intermarche-et-de-super-u_AN-202610120327.html"
  - quote: "Affected stores include those operating vulnerable Danfoss consoles with remote-control capabilities that lacked an adequately secured communication channel."
    publisher: "Infosecurity Magazine"
    source_url: "https://www.infosecurity-magazine.com/news/french-supermarket-chains/"
  - quote: "the majority of units affected were legacy products or current products running outdated firmware"
    publisher: "Cooling Post"
    source_url: "https://www.coolingpost.com/world-news/danfoss-moves-to-mitigate-cyberattack/"
  - quote: "While Danfoss has not confirmed the exact initial access vector, it says most affected controllers were either older models that no longer received security updates or newer models running outdated firmware."
    publisher: "Censys"
    source_url: "https://censys.com/blog/frostbitten-in-france-a-danfoss-storeview-internet-exposure-report/"
  - quote: "Verify the entire configuration, notably the defrost ranges. (translated from French)"
    original: "Vérifier l’intégralité de la configuration, notamment les plages de dégivrage."
    publisher: "CERT-FR (alert CERTFR-2026-ALE-012, third version)"
    source_url: "https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/"
  - quote: "Restart the Danfoss equipment, otherwise restore the equipment (Reset Factory). (translated from French)"
    original: "Redémarrer l'équipement Danfoss, sinon restaurer l'équipement (Reset Factory)."
    publisher: "CERT-FR (alert CERTFR-2026-ALE-012, third version)"
    source_url: "https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/"
  - quote: "Any XWEB PRO whose firmware is version 1.12.1 or earlier must be updated without delay. (translated from French)"
    original: "Tout XWEB PRO dont le firmware est en version 1.12.1 ou antérieure doit être mis à jour sans délai."
    publisher: "Dixell France (Copeland)"
    source_url: "https://dixell.fr/wp-content/uploads/2026/10/Recommandations-pour-une-utilisation-securisee-des-superviseurs-XWEB-v1.0.pdf"
verification: multi-source
sourcing_note: >
  CERT-FR's alert is the national authority's own statement, in its revision of 2026-10-16 (its page does not show which sentences changed), while NCSC Switzerland adds the exploitation rating and relays an older CERT-FR remediation sequence, and the retailers' confirmations, Danfoss's statement and the Paris prosecutor's investigation come through AFP. The forced 50-degree defrost and the "older than version 4" scope are BFMTV's reporting alone, store counts differ between AFP, BFMTV and Infosecurity, and no source read names the flaw or how the attackers got in (Censys points to three patched 2025 AK-SM 800A flaws and says Danfoss has not confirmed the vector).
  Dixell France's guide is undated, so the date given for it is the file's last modification on the vendor's server.
confidence: high
references:
  - 2026-08-28/claroty-danfoss-ak-sm-800a-code-of-the-day-rce
  - 2026-08-28/claroty-copeland-xweb-pro-refrigeration-unauth-root-rce
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Find every Danfoss AK-SM and AK-SC, Copeland xweb and Dixell xweb refrigeration controller in facilities you own or that a contractor manages for you and take its management interface off the internet now, restoring access only through a secure VPN or protected network (filtering to the contractor's source addresses is an emergency stop-gap, and CERT-FR asks you to check your insurance conditions before cutting the contractor's data uplink); an end-of-life unit that gets no fixes needs replacing, because a factory reset leaves it vulnerable and probably compromised again."
  - "On every such controller that was reachable from the internet, check the whole configuration, defrost ranges included, against the intended one; for a Danfoss unit that may have been taken over, restart it or otherwise factory-reset it, restore access only through a secure VPN or protected network and reconfigure it for service, then update its firmware, set the security level to Strict and change the default passwords, and on every Copeland or Dixell XWEB unit confirm the factory Admin password was changed and give each contractor a named account with an expiry date."
updates:
  - at: "2026-10-14T03:44:00Z"
    run_id: 2026-10-14T0255Z-intel
    type: update
    summary: >
      CERT-FR revised its alert on 2026-10-13 to add Copeland xweb and Dixell xweb to the compromised controllers, says campaigns are probably still running, and says a factory reset alone is insufficient on an unpatched end-of-life unit. NCSC Switzerland published an advisory rating the activity actively exploited and naming the current AK-SM 800A on outdated firmware, and Danfoss says that is the case for the affected current units. Blick reports that Migros uses the same Danfoss systems in a limited number of Swiss stores and sees no sign they were targeted.
    fields: [title, headline, summary, regions, entities, affected_products, sources, evidence, sourcing_note, references, actions, body]
  - at: "2026-10-15T03:49:00Z"
    run_id: 2026-10-15T0256Z-intel
    type: improvement
    summary: >
      Censys's exposure report of 2026-10-14 points to three published 2025 AK-SM 800A flaws that Danfoss patched more than a year earlier and gives their firmware boundaries (4.3.1 or later fixes all three; Danfoss has not confirmed the vector), and shows exposed French controllers falling about 71 percent in three days with patched and unpatched builds leaving at the same rate, which Censys reads as operators taking units offline rather than patching.
    fields: [sources, evidence, sourcing_note, body]
  - at: "2026-10-18T03:33:00Z"
    run_id: 2026-10-18T0256Z-intel
    type: update
    summary: >
      CERT-FR's alert has a third version dated 2026-10-16 whose guidance differs for compromised and uncompromised units: the whole configuration, defrost ranges included, is to be checked, and a compromised Danfoss unit is to be restarted or otherwise factory-reset and reconfigured, with a caution to check insurance conditions before cutting the contractor's data uplink. The Dixell France operator guide that the alert links says any XWEB PRO on firmware 1.12.1 or earlier must be updated without delay, that XWEB units ship with a factory Admin account, and that remote access must go through an encrypted VPN; neither document names an entry vector.
    fields: [summary, actions, sources, evidence, sourcing_note, body]
migrated_from: null
---

Coopérative U, Intermarché and E. Leclerc confirmed to AFP a cyberattack on their refrigeration systems overnight on 11 to 12 October 2026; AFP reports from the retailers' statements at least 300 Intermarché or Netto shops and more than 100 Coopérative U outlets, and the Paris prosecutor opened an investigation ([AFP, 2026-10-12](https://www.afp.com/en/french-supermarket-chains-say-cyberattack-forced-refrigerator-shutdown)). BFMTV puts the Intermarché and Netto count at 300, which it says is twice the first estimates of 150 points of sale, and Coopérative U below 100 stores, while Infosecurity quotes 150 Intermarché and 30 Netto stores ([BFMTV, 2026-10-12](https://www.bfmtv.com/economie/consommation/la-temperature-est-montee-jusqu-a-50-degres-une-cyberattaque-contre-les-systemes-frigorifiques-provoque-la-destruction-de-produits-frais-dans-des-centaines-d-intermarche-et-de-super-u_AN-202610120327.html); [Infosecurity Magazine, 2026-10-12](https://www.infosecurity-magazine.com/news/french-supermarket-chains/)). BFMTV, writing in the conditional, reports that the attackers are said to have imposed a forced, continuous defrost with the setpoint at 50 degrees, on software older than version 4, heating the equipment for hours (translated from French) ([BFMTV, 2026-10-12](https://www.bfmtv.com/economie/consommation/la-temperature-est-montee-jusqu-a-50-degres-une-cyberattaque-contre-les-systemes-frigorifiques-provoque-la-destruction-de-produits-frais-dans-des-centaines-d-intermarche-et-de-super-u_AN-202610120327.html)). CERT-FR's alert, in its revision of 2026-10-13, says it knows of numerous compromises of the remote refrigeration controllers Danfoss AK-SM and AK-SC series as well as Copeland xweb and Dixell xweb, and that exposing a management interface to the internet is contrary to good practice ([CERT-FR, 2026-10-13](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/)). Danfoss told AFP that most affected units are legacy products that no longer receive software or security updates, naming the AK-SM800 and AK-SC355 regulators, and a person close to the Prime Minister said ANSSI had identified a vulnerability in software from a Danish company and that other countries may be affected ([AFP, 2026-10-12](https://www.afp.com/en/french-supermarket-chains-say-cyberattack-forced-refrigerator-shutdown)). Intermarché told BleepingComputer that the attack reportedly affected a service provider that manages refrigeration systems in stores ([BleepingComputer, 2026-10-12](https://www.bleepingcomputer.com/news/security/cyberattack-shuts-down-refrigerators-at-french-supermarkets/)), and E. Leclerc told AFP that a cyberattack affected one of its refrigeration equipment suppliers ([AFP, 2026-10-12](https://www.afp.com/en/french-supermarket-chains-say-cyberattack-forced-refrigerator-shutdown)). Infosecurity says the affected stores include those running vulnerable consoles with remote control and no adequately secured communication channel ([Infosecurity Magazine, 2026-10-12](https://www.infosecurity-magazine.com/news/french-supermarket-chains/)). No source names an actor or the flaw or states how the attackers got in, and none confirms a tie to the 2025 AK-SM 8xxA vulnerabilities that Claroty found: BleepingComputer reports no tie ([BleepingComputer, 2026-10-12](https://www.bleepingcomputer.com/news/security/cyberattack-shuts-down-refrigerators-at-french-supermarkets/)) and NCSC Switzerland lists three of them only as alleged to be potentially related ([NCSC Switzerland, 2026-10-13](https://security-hub.ncsc.admin.ch/#/posts/13054)); Censys names the same three as flaws that Danfoss patched more than a year earlier and says Danfoss has not confirmed the initial access vector ([Censys, 2026-10-14](https://censys.com/blog/frostbitten-in-france-a-danfoss-storeview-internet-exposure-report/)).

**Exposure:** a Danfoss AK-SM or AK-SC refrigeration controller, or a Copeland or Dixell xweb unit, whose management interface is reachable from the internet, above all legacy units; Danfoss says the current AK-SM800A units that were affected ran outdated firmware ([Cooling Post, 2026-10-12](https://www.coolingpost.com/world-news/danfoss-moves-to-mitigate-cyberattack/)), and CERT-FR names no models, flaw or entry vector for the Copeland and Dixell units ([CERT-FR, 2026-10-13](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/)). Infosecurity reports, without naming them, that supermarkets in Belgium and the Netherlands were also reportedly affected ([Infosecurity Magazine, 2026-10-12](https://www.infosecurity-magazine.com/news/french-supermarket-chains/)); Blick reports that Migros confirms using, in a limited number of its Swiss stores, the same Danfoss refrigeration systems that were targeted and says nothing indicates an attack on them, while Aldi and Lidl say they are not concerned and Coop says it was not affected and declines to say whether it uses Danfoss ([Blick, 2026-10-13](https://www.blick.ch/fr/suisse/cyberattaque-les-frigos-de-migros-et-coop-sont-ils-proteges/79vpc6q)); no source reports a Swiss victim, so ask whoever manages your refrigeration and building services whether a controller sits in your estate. For an AK-SM 800A, Censys maps the firmware to the published flaws: a build below 4.2 carries all three, 4.2.4 fixes only the date-based login and so still carries the two later ones, and 4.3.1 or later fixes all three, with 5.3.2 the current build it lists ([Censys, 2026-10-14](https://censys.com/blog/frostbitten-in-france-a-danfoss-storeview-internet-exposure-report/)). For the Copeland and Dixell units, CERT-FR links an operator guide from Dixell France ([CERT-FR, 2026-10-16](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/)), which says any XWEB PRO on firmware 1.12.1 or earlier must be updated without delay and that XWEB PRO and EVO ship with the same factory Admin account ([Dixell France, 2026-10-13](https://dixell.fr/wp-content/uploads/2026/10/Recommandations-pour-une-utilisation-securisee-des-superviseurs-XWEB-v1.0.pdf)).

**Detection:** on the controller, defrost, setpoint and account changes outside a maintenance window; in firewall, provider VPN or ISP logs, inbound connections to the management interface from addresses other than the refrigeration contractor's; CERT-FR accepts filtering to the contractors' source addresses only as an emergency measure and wants access restored through a secure VPN or protected network ([CERT-FR, 2026-10-13](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/)). For a controller that may have been taken over, CERT-FR's current text is to remove the internet exposure, restart the Danfoss unit or otherwise restore it with a factory reset, restore access only through a secure VPN or protected network, reconfigure it and apply the maker's practices, which for Danfoss means updating the firmware, setting the security level to Strict and confirming the default passwords were changed ([CERT-FR, 2026-10-16](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/)); for a unit not known to be compromised it asks to check the whole configuration, notably the defrost ranges ([CERT-FR, 2026-10-16](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/)).

**Triage:** a defrost cycle is normal; BFMTV quotes sector professionals saying installations can be programmed for two hours of defrost per 24 hours, whereas the reported attack is said to be a continuous forced defrost at a 50-degree setpoint held for hours (translated from French) ([BFMTV, 2026-10-12](https://www.bfmtv.com/economie/consommation/la-temperature-est-montee-jusqu-a-50-degres-une-cyberattaque-contre-les-systemes-frigorifiques-provoque-la-destruction-de-produits-frais-dans-des-centaines-d-intermarche-et-de-super-u_AN-202610120327.html)).

**Defender takeaway:** take any Danfoss AK-SM or AK-SC, Copeland xweb or Dixell xweb management interface off the internet now and restore access only through a secure VPN or protected network, as CERT-FR advises ([CERT-FR, 2026-10-13](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/)), and ask the contractor whether its own remote access was affected; for the AK-SM800 and AK-SC355, replacement is the lever, since Danfoss says it had long advised supermarkets to move off those models ([AFP, 2026-10-12](https://www.afp.com/en/french-supermarket-chains-say-cyberattack-forced-refrigerator-shutdown)), no fix exists for them according to NCSC Switzerland ([NCSC Switzerland, 2026-10-13](https://security-hub.ncsc.admin.ch/#/posts/13054)), and CERT-FR says a factory reset on an unpatched end-of-life unit removes the implant but leaves the device vulnerable and almost certainly compromised again ([CERT-FR, 2026-10-13](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/)).

## Update — 2026-10-14T03:44:00Z

CERT-FR revised its alert on 2026-10-13: the list of compromised remote controllers now includes Copeland xweb and Dixell xweb besides Danfoss AK-SM and AK-SC, campaigns against these devices are probably still ongoing, and an unpatched end-of-life unit kept on the internet is very likely to be compromised, so a factory reset alone is insufficient ([CERT-FR, 2026-10-13](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/)). NCSC Switzerland published advisory 13054 on 2026-10-13 with the exploitation status Actively Exploited. It lists the Danfoss AK-SM 800 (end of life, no longer patched), the AK-SC 355 (phased out, no longer patched) and the current AK-SM 800A series when it runs outdated firmware, says no fixes exist for the two older models and that Danfoss urges replacing them, and says the attack could affect other sectors, such as healthcare for specialized cooling equipment, so organisations should check whether affected devices are in use ([NCSC Switzerland, 2026-10-13](https://security-hub.ncsc.admin.ch/#/posts/13054)). Danfoss told Cooling Post that the AK-SM800 was declared end of life in 2021, that the AK-SC355 was phased out in 2016, and that the affected AK-SM800A systems ran outdated firmware ([Cooling Post, 2026-10-12](https://www.coolingpost.com/world-news/danfoss-moves-to-mitigate-cyberattack/)). Blick reports that Migros uses the same Danfoss refrigeration systems in a limited number of Swiss stores and sees no sign they were targeted, and that Aldi, Lidl and Coop say they are not affected ([Blick, 2026-10-13](https://www.blick.ch/fr/suisse/cyberattaque-les-frigos-de-migros-et-coop-sont-ils-proteges/79vpc6q)); no source reports a Swiss victim. The advisory relays a six-step CERT-FR sequence (limit access to trusted addresses, factory reset, apply all fixes, rotate passwords and secrets, review accounts, reconfigure) and lists filtering to trusted addresses as a temporary measure ([NCSC Switzerland, 2026-10-13](https://security-hub.ncsc.admin.ch/#/posts/13054)), whereas the revised CERT-FR page puts removal of internet exposure first, accepts source-address filtering only as an emergency stop-gap and lists no secret rotation or account review ([CERT-FR, 2026-10-13](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/)).

## Improvement — 2026-10-15T03:49:00Z

Censys, which scans for Danfoss StoreView control panels, says Danfoss has not confirmed the initial access vector and points to three AK-SM 800A flaws that Danfoss patched more than a year earlier: CVE-2025-41450 (March 2025), which Censys describes as letting an unauthenticated actor log in as an administrator with a code computed from the current calendar date, and CVE-2025-41451 and CVE-2025-41452 (August 2025), which it says let authenticated users run commands and disrupt the management interface ([Censys, 2026-10-14](https://censys.com/blog/frostbitten-in-france-a-danfoss-storeview-internet-exposure-report/)). Censys maps the firmware by build: below 4.2 carries all three, 4.2.4 fixes only the date-based login and still carries the two later ones, and 4.3.1 or later fixes all three ([Censys, 2026-10-14](https://censys.com/blog/frostbitten-in-france-a-danfoss-storeview-internet-exposure-report/)). Its scan counted 1,825 exposed StoreView panels in France on 2026-10-11 and 537 on 2026-10-14, a fall of 71 percent, with builds below 4.2, build 4.2.4 and builds from 4.3.1 leaving at about the same rate, which it reads as operators taking controllers off the internet rather than patching them ([Censys, 2026-10-14](https://censys.com/blog/frostbitten-in-france-a-danfoss-storeview-internet-exposure-report/)). Outside France the count fell from 1,166 to 966, and in ten of the twelve countries with the most exposed hosts more than 60 percent of the hosts run a build below 4.3.1, led by Poland at 81 percent and Romania at 80 percent ([Censys, 2026-10-14](https://censys.com/blog/frostbitten-in-france-a-danfoss-storeview-internet-exposure-report/)).

## Update — 2026-10-18T03:33:00Z

CERT-FR's alert now has a third version, dated 2026-10-16 and listed on the page as an update of the recommendations; the page does not show which sentences changed ([CERT-FR, 2026-10-16](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/)). Its current text separates the two cases. For every unit it asks to remove the internet exposure of the affected units and of any unit on a public IP address, and to check the insurance contract conditions before cutting the data uplink to the refrigeration contractor ([CERT-FR, 2026-10-16](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/)). For a unit not known to be compromised it then asks to check the whole configuration, notably the defrost ranges; for a compromised Danfoss unit it says to restart the equipment or otherwise restore it with a factory reset, and then to reconfigure it for service ([CERT-FR, 2026-10-16](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/)). In both cases access returns only through a secure VPN or protected network, with source-address filtering for the contractors an emergency measure and not a lasting one, and the maker's practices apply ([CERT-FR, 2026-10-16](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/)). The alert still says campaigns are probably ongoing, still names no flaw or entry vector, and gives the risk as not specified by the vendor ([CERT-FR, 2026-10-16](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/)).

The alert's documentation section links an operator guide from Dixell France (Copeland) ([CERT-FR, 2026-10-16](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/)); the guide is undated, and its file was last modified on 2026-10-13 ([Dixell France, 2026-10-13](https://dixell.fr/wp-content/uploads/2026/10/Recommandations-pour-une-utilisation-securisee-des-superviseurs-XWEB-v1.0.pdf)). It repeats Copeland's March 2024 bulletin, which says never to expose the XWEB to the public internet, and adds three operational recommendations ([Dixell France, 2026-10-13](https://dixell.fr/wp-content/uploads/2026/10/Recommandations-pour-une-utilisation-securisee-des-superviseurs-XWEB-v1.0.pdf)). First, any XWEB PRO on firmware 1.12.1 or earlier must be updated without delay; the guide cites CISA's February 2026 advisory ICSA-26-057-10 on several critical XWEB PRO vulnerabilities up to that version, says Copeland has published a fix and advises backing up the configuration first ([Dixell France, 2026-10-13](https://dixell.fr/wp-content/uploads/2026/10/Recommandations-pour-une-utilisation-securisee-des-superviseurs-XWEB-v1.0.pdf)). Second, XWEB PRO and EVO ship with the same factory account, Admin with the password Admin, so any unit whose password was never changed or is simple must be corrected, with one account per technician and an expiry date on external-contractor accounts ([Dixell France, 2026-10-13](https://dixell.fr/wp-content/uploads/2026/10/Recommandations-pour-une-utilisation-securisee-des-superviseurs-XWEB-v1.0.pdf)). Third, remote access must go through an encrypted VPN tunnel, with a port forward limited to one trusted source address acceptable only as a temporary, degraded stop-gap, no DMZ or port forward open to all addresses, and no remote-control software such as AnyDesk or TeamViewer on a site PC that stays on ([Dixell France, 2026-10-13](https://dixell.fr/wp-content/uploads/2026/10/Recommandations-pour-une-utilisation-securisee-des-superviseurs-XWEB-v1.0.pdf)). Neither document says how the attackers got in, and no source ties the attacks to the XWEB PRO flaws the guide cites.
