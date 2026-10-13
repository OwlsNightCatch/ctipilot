---
schema: 1
kind: incident
title: "Danfoss AK-SM and AK-SC refrigeration controllers compromised, with forced defrost reported at hundreds of French supermarkets; CERT-FR advises disconnecting or filtering access"
headline: "CERT-FR reports numerous compromised Danfoss refrigeration controllers while French supermarkets lose stock"
summary: >
  Coopérative U, Intermarché and E. Leclerc confirmed to AFP a cyberattack on their refrigeration systems overnight on 11 to 12 October 2026, which BFMTV reports as a remotely forced defrost at hundreds of stores, and
  CERT-FR's alert of 2026-10-12 reports numerous compromises of Danfoss AK-SM and AK-SC series devices and advises disconnecting or filtering access. Danfoss says most affected units are legacy products that no longer receive
  security updates; no source names an actor, the flaw or how the attackers got in, and the Paris prosecutor is investigating.
discovered_at: "2026-10-13T03:41:00Z"
updated_at: null
event_date: "2026-10-12"
run_id: 2026-10-13T0256Z-intel
priority: high
immediate_action: null
tags: [ot-ics, actively-exploited]
regions: [europe]
sectors: [retail]
entities: ["incident:danfoss-ak-sm-ak-sc-french-supermarket-refrigeration-attack-2026-10", "product:danfoss-ak-sm-800", "product:danfoss-ak-sc-355"]
techniques: [T1190]
affected_products: ["Danfoss AK-SM 800", "Danfoss AK-SC 355"]
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
closed_sources: []
evidence:
  - quote: "CERT-FR is aware of numerous compromises of Danfoss AK-SM and AK-SC series devices. (translated from French)"
    original: "Le CERT-FR a connaissance de nombreuses compromissions de Danfoss série AK-SM et AK-SC."
    publisher: "CERT-FR (alert CERTFR-2026-ALE-012)"
    source_url: "https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/"
  - quote: "Disconnect or filter access to AK-SM and AK-SC instances. (translated from French)"
    original: "Déconnecter ou filtrer les accès aux instances AK-SM et AK-SC."
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
verification: multi-source
sourcing_note: >
  CERT-FR's alert is the national authority's own statement; the retailers' confirmations, Danfoss's statement and the Paris prosecutor's investigation come through AFP.
  The forced 50-degree defrost and the "older than version 4" scope are BFMTV's reporting and no other source reports them independently. Store counts moved during the day: AFP and BFMTV give 300 Intermarché or Netto shops, twice the first estimate of 150 that Infosecurity quotes,
  and AFP gives more than 100 Coopérative U outlets where Coopérative U told BFMTV fewer than 100. No source read names the flaw or states how the attackers got in.
confidence: high
references:
  - 2026-08-28/claroty-danfoss-ak-sm-800a-code-of-the-day-rce
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Find every Danfoss AK-SM and AK-SC refrigeration controller in facilities you own or that a contractor manages for you and take its management interface off the internet or filter it to the contractor's addresses now."
updates: []
migrated_from: null
---

Coopérative U, Intermarché and E. Leclerc confirmed to AFP a cyberattack on their refrigeration systems overnight on 11 to 12 October 2026; AFP reports from the retailers' statements at least 300 Intermarché or Netto shops and more than 100 Coopérative U outlets, and the Paris prosecutor opened an investigation ([AFP, 2026-10-12](https://www.afp.com/en/french-supermarket-chains-say-cyberattack-forced-refrigerator-shutdown)). BFMTV puts the Intermarché and Netto count at 300, twice the first estimate of 150 that Infosecurity quotes, and Coopérative U below 100 stores ([BFMTV, 2026-10-12](https://www.bfmtv.com/economie/consommation/la-temperature-est-montee-jusqu-a-50-degres-une-cyberattaque-contre-les-systemes-frigorifiques-provoque-la-destruction-de-produits-frais-dans-des-centaines-d-intermarche-et-de-super-u_AN-202610120327.html); [Infosecurity Magazine, 2026-10-12](https://www.infosecurity-magazine.com/news/french-supermarket-chains/)). BFMTV, writing in the conditional, reports that the attackers are said to have imposed a forced, continuous defrost with the setpoint at 50 degrees, on software older than version 4, heating the equipment for hours (translated from French) ([BFMTV, 2026-10-12](https://www.bfmtv.com/economie/consommation/la-temperature-est-montee-jusqu-a-50-degres-une-cyberattaque-contre-les-systemes-frigorifiques-provoque-la-destruction-de-produits-frais-dans-des-centaines-d-intermarche-et-de-super-u_AN-202610120327.html)). CERT-FR's alert says it knows of numerous compromises of Danfoss AK-SM and AK-SC series devices and that exposing a management interface to the internet is contrary to good practice ([CERT-FR, 2026-10-12](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/)). Danfoss told AFP that most affected units are legacy products that no longer receive software or security updates, naming the AK-SM800 and AK-SC355 regulators, and a person close to the Prime Minister said ANSSI had identified a vulnerability in software from a Danish company and that other countries may be affected ([AFP, 2026-10-12](https://www.afp.com/en/french-supermarket-chains-say-cyberattack-forced-refrigerator-shutdown)). Intermarché told BleepingComputer that the attack reportedly affected a service provider that manages refrigeration systems in stores ([BleepingComputer, 2026-10-12](https://www.bleepingcomputer.com/news/security/cyberattack-shuts-down-refrigerators-at-french-supermarkets/)), and E. Leclerc told AFP that a cyberattack affected one of its refrigeration equipment suppliers ([AFP, 2026-10-12](https://www.afp.com/en/french-supermarket-chains-say-cyberattack-forced-refrigerator-shutdown)). Infosecurity says the affected stores include those running vulnerable consoles with remote control and no adequately secured communication channel ([Infosecurity Magazine, 2026-10-12](https://www.infosecurity-magazine.com/news/french-supermarket-chains/)). No source names an actor or the flaw or states how the attackers got in, and none ties the attack to the 2025 AK-SM 8xxA vulnerabilities that Claroty found ([BleepingComputer, 2026-10-12](https://www.bleepingcomputer.com/news/security/cyberattack-shuts-down-refrigerators-at-french-supermarkets/)).

**Exposure:** a Danfoss AK-SM or AK-SC refrigeration controller whose management interface is reachable from the internet, above all legacy units. Infosecurity reports, without naming them, that supermarkets in Belgium and the Netherlands were also reportedly affected ([Infosecurity Magazine, 2026-10-12](https://www.infosecurity-magazine.com/news/french-supermarket-chains/)); no source names a Swiss deployment, so ask whoever manages your refrigeration and building services whether a controller sits in your estate.

**Detection:** on the controller, defrost, setpoint and account changes outside a maintenance window; in firewall, provider VPN or ISP logs, inbound connections to the management interface from addresses other than the refrigeration contractor's, the only access CERT-FR leaves open ([CERT-FR, 2026-10-12](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/)). For a controller that may have been taken over, CERT-FR lists a factory reset, all available security fixes, rotation of secrets, a review of accounts and a reconfiguration ([CERT-FR, 2026-10-12](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/)).

**Triage:** a defrost cycle is normal; BFMTV quotes sector professionals saying installations can be programmed for two hours of defrost per 24 hours, whereas the reported attack is said to be a continuous forced defrost at a 50-degree setpoint held for hours (translated from French) ([BFMTV, 2026-10-12](https://www.bfmtv.com/economie/consommation/la-temperature-est-montee-jusqu-a-50-degres-une-cyberattaque-contre-les-systemes-frigorifiques-provoque-la-destruction-de-produits-frais-dans-des-centaines-d-intermarche-et-de-super-u_AN-202610120327.html)).

**Defender takeaway:** take any Danfoss AK-SM or AK-SC management interface off the internet or filter it to the contractor's addresses now, as CERT-FR advises, and ask the contractor whether its own remote access was affected; for the AK-SM800 and AK-SC355, isolation or replacement is the lever, since Danfoss says it had long advised supermarkets to move off those models ([AFP, 2026-10-12](https://www.afp.com/en/french-supermarket-chains-say-cyberattack-forced-refrigerator-shutdown)), and a controller that may have been taken over needs CERT-FR's reset-and-rotate sequence, not only a patch.
