---
schema: 1
kind: incident
title: "Danfoss AK-SM and AK-SC, Copeland xweb and Dixell xweb refrigeration controllers compromised, with forced defrost at hundreds of French supermarkets and, on 2026-11-02, refrigeration failures at more than 115 shops in at least six more countries; CERT-FR and NCSC Switzerland say to remove internet exposure"
headline: "Refrigeration attacks hit at least six more countries on 2 Nov; Coop CH: attempts failed; ANSSI blames exposure"
summary: >
  Coopérative U, Intermarché and E. Leclerc confirmed to AFP a cyberattack on their refrigeration systems overnight on 11 to 12 October 2026, a remotely forced defrost at hundreds of French stores. On 2026-11-02 BleepingComputer counts more than 115 stores in Belgium, Luxembourg, the Netherlands, Sweden, Ireland and Estonia with refrigeration failures, in some cases remotely changed settings, and says it is unclear whether they were hit in a coordinated attack; Belgian contractor Sabcobel says its sites were hit through the same vulnerability as in France, Euronews names Danfoss as the software supplier in both incidents, CyberInsider says the manufacturer and access method of the new wave remain unknown, and Coop Switzerland says attempts against it failed. CERT-FR reports numerous compromises of Danfoss AK-SM and AK-SC controllers and of Copeland xweb and Dixell xweb, NCSC Switzerland rates the activity actively exploited, and ANSSI says elementary flaws were exploited, controllers directly on the internet and weak passwords, not published vulnerabilities. No actor is named on the record; Reuters and Nextgov report that the Pentagon treats freezer failures at US military commissaries as a suspected hack.
discovered_at: "2026-10-13T03:41:00Z"
updated_at: "2026-11-03T03:45:49Z"
event_date: "2026-10-12"
run_id: 2026-10-13T0256Z-intel
priority: high
immediate_action: null
tags: [ot-ics, actively-exploited]
regions: [europe, switzerland]
sectors: [retail]
entities: ["incident:danfoss-ak-sm-ak-sc-french-supermarket-refrigeration-attack-2026-10", "product:danfoss-ak-sm-800", "product:danfoss-ak-sc-355", "product:danfoss-ak-sm-800a", "product:copeland-xweb", "product:dixell-xweb"]
techniques: [T1190, T1133, T1078]
affected_products: ["Danfoss AK-SM 800", "Danfoss AK-SC 355", "Danfoss AK-SM 800A", "Copeland xweb", "Dixell xweb"]
cves: []
sources:
  - url: "https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/"
    publisher: "CERT-FR (alert CERTFR-2026-ALE-012)"
    date: "2026-10-12"
    role: primary
  - url: "https://www.khaleejtimes.com/world/europe/french-supermarkets-refrigerator-shutdown-cyberattack"
    publisher: "AFP (via Khaleej Times)"
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
    date: "2026-10-14"
    role: corroborating
  - url: "https://www.lemonde.fr/economie/article/2026/10/12/journee-noire-dans-les-supermarches-francais-apres-une-cyberattaque-massive_6792763_3234.html"
    publisher: "Le Monde"
    date: "2026-10-12"
    role: corroborating
  - url: "https://www.securityweek.com/supermarket-refrigeration-attack-widens-to-copeland-dixell-controllers/"
    publisher: "SecurityWeek"
    date: "2026-10-15"
    role: corroborating
  - url: "https://www.cybersecuritydive.com/news/thousands-refrigerator-devices-exposed-french-cyberattack/833117/"
    publisher: "Cybersecurity Dive"
    date: "2026-10-15"
    role: corroborating
  - url: "https://www.publicsenat.fr/actualites/politique/des-defauts-de-securisation-elementaire-et-des-mots-de-passe-faibles-ont-permis-la-cyberattaque-contre-les-frigos-de-supermarches"
    publisher: "Public Sénat"
    date: "2026-10-21"
    role: corroborating
  - url: "https://www.lemondeinformatique.fr/actualites/lire-frigos-de-supermarches-pirates-l-anssi-pointe-des-failles-de-securite-elementaires-100864.html"
    publisher: "Le Monde Informatique"
    date: "2026-10-22"
    role: corroborating
  - url: "https://www.forescout.com/blog/cold-chain-open-control-exposed-refrigeration-systems-reveal-global-risk/"
    publisher: "Forescout Research (Vedere Labs)"
    date: "2026-10-22"
    role: corroborating
  - url: "https://www.internazionale.it/ultime-notizie-reuters/2026/10/29/exclusive-pentagon-treating-military-base-freezer-malfunctions-as-suspected-cyberattack-officials-say"
    publisher: "Reuters (republished by Internazionale)"
    date: "2026-10-29"
    role: corroborating
  - url: "https://www.nextgov.com/cybersecurity/2026/10/officials-suspect-iran-series-cyberattacks-military-base-freezers/416934/"
    publisher: "Nextgov"
    date: "2026-10-30"
    role: corroborating
  - url: "https://www.theguardian.com/world/2026/nov/02/supermarket-freezers-across-europe-hit-by-second-suspected-cyber-attack"
    publisher: "The Guardian"
    date: "2026-11-02"
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/hackers-disrupt-refrigeration-systems-at-european-supermarkets/"
    publisher: "BleepingComputer"
    date: "2026-11-02"
    role: corroborating
  - url: "https://www.euronews.com/2026/11/02/cyberattack-hits-belgian-supermarket-fridges-and-freezers"
    publisher: "Euronews"
    date: "2026-11-02"
    role: corroborating
  - url: "https://www.tagesschau.de/wirtschaft/technologie/cyberangriff-supermaerkte-100.html"
    publisher: "Tagesschau (ARD)"
    date: "2026-11-02"
    role: corroborating
  - url: "https://cyberinsider.com/supermarket-refrigeration-cyberattacks-belgium-sweden/"
    publisher: "CyberInsider"
    date: "2026-11-02"
    role: corroborating
  - url: "https://www.20min.ch/story/seit-mitte-oktober-mysterioese-hacking-welle-trifft-europaeische-supermaerkte-103660687"
    publisher: "20 Minuten"
    date: "2026-11-02"
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
    publisher: "AFP (via Khaleej Times)"
    source_url: "https://www.khaleejtimes.com/world/europe/french-supermarkets-refrigerator-shutdown-cyberattack"
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
  - quote: "We acknowledge the existence of the vulnerability identified on a generation of XWEB EVO controllers that is no longer marketed and has reached end of life. (translated from French)"
    original: "Nous reconnaissons l’existence de la vulnérabilité identifiée sur une génération de contrôleurs XWEB EVO dont la commercialisation est arrêtée et qui est parvenue en fin de vie."
    publisher: "Dixell France (Copeland)"
    source_url: "https://dixell.fr/wp-content/uploads/2026/10/Recommandations-pour-une-utilisation-securisee-des-superviseurs-XWEB-v1.0.pdf"
  - quote: "Immediately remove all XWEB EVO units from the public internet, then look for any suspicious activity from the local network and restore the devices if necessary. (translated from French)"
    original: "Retirez immédiatement toutes les unités XWEB EVO de l’Internet public, puis recherchez toute activité suspecte depuis le réseau local et restaurez les appareils si nécessaire."
    publisher: "Dixell France (Copeland)"
    source_url: "https://dixell.fr/wp-content/uploads/2026/10/Recommandations-pour-une-utilisation-securisee-des-superviseurs-XWEB-v1.0.pdf"
  - quote: "the hackers had raised the duration of the operation from one hour to eight hours so that the alarms trigger late (translated from French)"
    original: "les pirates avaient porté de une heure à huit heures la durée de l’opération afin que les alarmes se déclenchent tardivement"
    publisher: "Le Monde"
    source_url: "https://www.lemonde.fr/economie/article/2026/10/12/journee-noire-dans-les-supermarches-francais-apres-une-cyberattaque-massive_6792763_3234.html"
  - quote: "A spokesperson for Copeland confirmed that a vulnerability was found in discontinued end-of-life controllers."
    publisher: "Cybersecurity Dive"
    source_url: "https://www.cybersecuritydive.com/news/thousands-refrigerator-devices-exposed-french-cyberattack/833117/"
  - quote: "but it has since acknowledged a vulnerability"
    publisher: "SecurityWeek"
    source_url: "https://www.securityweek.com/supermarket-refrigeration-attack-widens-to-copeland-dixell-controllers/"
  - quote: "it is elementary security flaws that were exploited, starting with the direct exposure of refrigeration equipment on the internet and its administration without particular protection, weak passwords, that kind of thing (translated from French)"
    original: "ce sont des défauts de sécurisation élémentaire qui ont été exploités, à commencer par l’exposition directe sur Internet d’équipements frigorifiques et leur administration sans sécurisation particulière, des mots de passe faibles, ce genre de choses"
    publisher: "Public Sénat"
    source_url: "https://www.publicsenat.fr/actualites/politique/des-defauts-de-securisation-elementaire-et-des-mots-de-passe-faibles-ont-permis-la-cyberattaque-contre-les-frigos-de-supermarches"
  - quote: "without a firewall or network segmentation, and their administration interface was protected only by weak passwords (translated from French)"
    original: "sans pare-feu ni segmentation réseau, et leur interface d’administration n’était protégée que par des mots de passe faibles"
    publisher: "Le Monde Informatique"
    source_url: "https://www.lemondeinformatique.fr/actualites/lire-frigos-de-supermarches-pirates-l-anssi-pointe-des-failles-de-securite-elementaires-100864.html"
  - quote: "Initial access methods, exploited vulnerabilities, attacker infrastructure, persistence mechanism, and responsible actors in those incidents remain unconfirmed"
    publisher: "Forescout Research (Vedere Labs)"
    source_url: "https://www.forescout.com/blog/cold-chain-open-control-exposed-refrigeration-systems-reveal-global-risk/"
  - quote: "Since January 2026, our tracking of hacktivist groups identified over 20 claimed attacks against refrigeration systems."
    publisher: "Forescout Research (Vedere Labs)"
    source_url: "https://www.forescout.com/blog/cold-chain-open-control-exposed-refrigeration-systems-reveal-global-risk/"
  - quote: "The Pentagon is treating the spate of mysterious freezer malfunctions that spoiled food at military bases across the United States in August as a suspected hack, according to four officials familiar with the matter."
    publisher: "Reuters (republished by Internazionale)"
    source_url: "https://www.internazionale.it/ultime-notizie-reuters/2026/10/29/exclusive-pentagon-treating-military-base-freezer-malfunctions-as-suspected-cyberattack-officials-say"
  - quote: "Reuters could not establish whether Danfoss or any other brand of freezer controller were in use at the affected US bases."
    publisher: "Reuters (republished by Internazionale)"
    source_url: "https://www.internazionale.it/ultime-notizie-reuters/2026/10/29/exclusive-pentagon-treating-military-base-freezer-malfunctions-as-suspected-cyberattack-officials-say"
  - quote: "U.S. officials suspect Iran-linked hackers are behind a series of cyberattacks that have targeted freezers at military bases around the country and caused them to malfunction, according to two people familiar with the matter."
    publisher: "Nextgov"
    source_url: "https://www.nextgov.com/cybersecurity/2026/10/officials-suspect-iran-series-cyberattacks-military-base-freezers/416934/"
  - quote: "More than 115 stores in Belgium, the Netherlands, Sweden, Luxembourg, Ireland, and Estonia have been affected."
    publisher: "BleepingComputer"
    source_url: "https://www.bleepingcomputer.com/news/security/hackers-disrupt-refrigeration-systems-at-european-supermarkets/"
  - quote: "According to Sabcobel's director, Stephan Moelans, the attacker leveraged the same vulnerability"
    publisher: "BleepingComputer"
    source_url: "https://www.bleepingcomputer.com/news/security/hackers-disrupt-refrigeration-systems-at-european-supermarkets/"
  - quote: "Danfoss, the company that supplied the software for the refrigeration systems affected in both the latest incident and the one in France in October, said customers who had not updated their software were affected."
    publisher: "Euronews"
    source_url: "https://www.euronews.com/2026/11/02/cyberattack-hits-belgian-supermarket-fridges-and-freezers"
  - quote: "The manufacturer, controller models, and initial access method involved in the latest incidents remain unknown."
    publisher: "CyberInsider"
    source_url: "https://cyberinsider.com/supermarket-refrigeration-cyberattacks-belgium-sweden/"
  - quote: "In Switzerland, too, corresponding attempts were registered at Coop - but without success, a spokeswoman for the retailer confirmed on request. (translated from German)"
    original: "Auch in der Schweiz wurden bei Coop entsprechende Versuche registriert – allerdings ohne Erfolg, wie eine Sprecherin des Detailhändlers auf Anfrage bestätigt."
    publisher: "20 Minuten"
    source_url: "https://www.20min.ch/story/seit-mitte-oktober-mysterioese-hacking-welle-trifft-europaeische-supermaerkte-103660687"
verification: multi-source
sourcing_note: >
  CERT-FR's alert is the national authority's own statement, in its revision of 2026-10-16 (its page does not show which sentences changed), while NCSC Switzerland adds the exploitation rating and relays an older CERT-FR remediation sequence, and the retailers' confirmations, Danfoss's statement and the Paris prosecutor's investigation come through AFP. The forced 50-degree defrost and the "older than version 4" scope are BFMTV's reporting alone, store counts differ between AFP, BFMTV and Infosecurity, and ANSSI's account of the cause is its director general's testimony as Public Sénat and Le Monde Informatique report it, with no transcript read, while Forescout says the access vector, exploited vulnerabilities and actors remain unconfirmed and Censys points to three patched 2025 AK-SM 800A flaws and says Danfoss has not confirmed the vector.
  The Dixell France PDF opens with Copeland's bulletin dated 14 October 2026, and the file at that address was replaced on 2026-10-18. The second wave of 2026-11-02 rests on company statements and press: the claim that the attacker used the same vulnerability as in France is Sabcobel's as BleepingComputer reports it, and CyberInsider states that the manufacturer, controller models and initial access method of the new wave are unknown.
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
  - "Find every Danfoss AK-SM and AK-SC, Copeland xweb and Dixell xweb refrigeration controller, and any other refrigeration controller with a remote management interface because the vendor of the second wave is unconfirmed, in facilities you own or that a contractor manages for you and take its management interface off the internet now, restoring access only through a secure VPN or protected network (filtering to the contractor's source addresses is an emergency stop-gap, and CERT-FR asks you to check your insurance conditions before cutting the contractor's data uplink); an end-of-life unit that gets no fixes needs replacing, because a factory reset leaves it vulnerable and probably compromised again."
  - "On every such controller that was reachable from the internet, check the whole configuration, defrost ranges included, against the intended one; for a Danfoss unit that may have been taken over, restart it or otherwise factory-reset it, restore access only through a secure VPN or protected network and reconfigure it for service, then update its firmware, set the security level to Strict and replace the default and any weak passwords, and on every Copeland or Dixell XWEB unit confirm the factory Admin password was changed and give each contractor a named account with an expiry date."
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
  - at: "2026-10-19T04:06:00Z"
    run_id: 2026-10-19T0256Z-intel
    type: correction
    summary: >
      The Dixell France guide that CERT-FR links was replaced on 2026-10-18 and now carries Copeland's own bulletin of 14 October 2026, which acknowledges the vulnerability on a discontinued, end-of-life generation of XWEB EVO controllers, says to remove every XWEB EVO from the public internet at once, gives a restore procedure and says to check product temperatures in the cabinets directly; the earlier statements about XWEB PRO firmware 1.12.1, a CISA advisory and a March 2024 bulletin are no longer on that page and are removed. Le Monde's report that the defrost operation was lengthened from one hour to eight so that alarms trigger late, and SecurityWeek's figure of about 700 supermarkets, the prosecutor's report of fires and the absence of a claim or ransom demand, are added, with Cybersecurity Dive's report that Copeland confirmed the flaw was found in discontinued controllers.
    fields: [summary, sources, evidence, sourcing_note, body]
  - at: "2026-10-19T21:00:14Z"
    run_id: 2026-10-18T1307Z-audit
    type: correction
    internal: true
    summary: >
      The Defender takeaway says, as CERT-FR does, that a factory reset removes the compromised instance's
      persistence, instead of 'the implant'.
    fields: [body]
  - at: "2026-10-25T03:37:30Z"
    run_id: 2026-10-25T0256Z-intel
    type: update
    summary: >
      ANSSI's director general told the French Senate on 2026-10-21 that elementary flaws were exploited,
      starting with controllers directly on the internet, administered without particular protection, and
      weak passwords, not vulnerabilities researchers had published, so a firmware update alone does not
      close the exposure. Forescout, on 2026-10-22, counts 12,976 exposed service observations in 99
      countries, 3,762 exposed Danfoss StoreView observations on AK-SM 800A units, 80 percent of the 4,697 StoreView observations, on firmware older than 4.3.1, and over 20
      hacktivist-claimed refrigeration attacks since January 2026, and says the French access vector
      remains unconfirmed.
    fields: [headline, summary, techniques, sources, evidence, sourcing_note, actions, body]
  - at: "2026-10-25T13:39:27Z"
    run_id: 2026-10-25T1308Z-audit
    type: correction
    internal: true
    summary: >
      The 2026-10-25 section said Forescout's 20-plus claimed refrigeration attacks were mostly by
      Z-Pentest Alliance and NoName057(16); Forescout calls them the most active groups, and the sentence
      now says so.
    fields: [body]
  - at: "2026-11-02T03:47:57Z"
    run_id: 2026-11-02T0256Z-intel
    type: update
    summary: >
      Reuters reports that the Pentagon treats late-August freezer failures at at least six US military
      commissaries as a suspected hack, with Cyber Command and Army investigators in touch with their
      French counterparts, and Nextgov adds that two people familiar with the matter say US officials
      suspect Iran-linked hackers; neither says how the intruders got in, and no official has attributed
      the activity on the record.
    fields: [summary, sources, evidence, body]
  - at: "2026-11-03T03:45:49Z"
    run_id: 2026-11-03T0256Z-intel
    type: update
    summary: >
      The attacks returned on 2026-11-02 across Belgium, Luxembourg, the Netherlands, Sweden, Ireland and
      Estonia, and Finland per The Guardian: BleepingComputer counts more than 115 stores and says it is
      unclear whether the attacks were coordinated, Sabcobel says its sites were hit through the same
      vulnerability as in France, Euronews names Danfoss as the software supplier in both incidents while
      CyberInsider says the manufacturer and access method of the new wave remain unknown, and Coop
      Switzerland says attempts against it failed.
    fields: [title, headline, summary, sources, evidence, sourcing_note, actions, body]
migrated_from: null
---

Coopérative U, Intermarché and E. Leclerc confirmed to AFP a cyberattack on their refrigeration systems overnight on 11 to 12 October 2026, at hundreds of stores, and Paris prosecutors confirmed the attack ([AFP, 2026-10-12](https://www.khaleejtimes.com/world/europe/french-supermarkets-refrigerator-shutdown-cyberattack)). CERT-FR knows of numerous compromises of Danfoss AK-SM and AK-SC controllers and of Copeland xweb and Dixell xweb, says campaigns are probably still running and that exposing a management interface to the internet is contrary to good practice ([CERT-FR, 2026-10-16](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/)); NCSC Switzerland rates the activity actively exploited ([NCSC Switzerland, 2026-10-13](https://security-hub.ncsc.admin.ch/#/posts/13054)). ANSSI's director general told the French Senate on 2026-10-21 that elementary flaws were exploited, above all equipment directly on the internet without particular protection, plus weak passwords, rather than vulnerabilities researchers had published ([Public Sénat, 2026-10-21](https://www.publicsenat.fr/actualites/politique/des-defauts-de-securisation-elementaire-et-des-mots-de-passe-faibles-ont-permis-la-cyberattaque-contre-les-frigos-de-supermarches)). No actor is named on the record.

On 2026-11-02 retailers in Belgium, Luxembourg, the Netherlands, Sweden, Ireland, Estonia and, per The Guardian, Finland reported refrigeration failures; BleepingComputer counts more than 115 affected stores from company statements and says it is unclear whether they were hit in a coordinated attack ([BleepingComputer, 2026-11-02](https://www.bleepingcomputer.com/news/security/hackers-disrupt-refrigeration-systems-at-european-supermarkets/)), and several companies confirmed they had been hacked ([The Guardian, 2026-11-02](https://www.theguardian.com/world/2026/nov/02/supermarket-freezers-across-europe-hit-by-second-suspected-cyber-attack)). Sabcobel, the refrigeration contractor behind several Belgian sites, attributed the disruption to remotely activated defrost functions and, per BleepingComputer, said the attacker used the same vulnerability as in France ([BleepingComputer, 2026-11-02](https://www.bleepingcomputer.com/news/security/hackers-disrupt-refrigeration-systems-at-european-supermarkets/)). Euronews names Danfoss as the software supplier of the affected systems in both incidents, quotes it saying customers who had not updated their software were affected, and quotes a refrigeration executive saying a software update alone is not enough ([Euronews, 2026-11-02](https://www.euronews.com/2026/11/02/cyberattack-hits-belgian-supermarket-fridges-and-freezers)); in Estonia, attackers reached the control computer of an older Danfoss system with outdated software (translated from German) ([Tagesschau, 2026-11-02](https://www.tagesschau.de/wirtschaft/technologie/cyberangriff-supermaerkte-100.html)). CyberInsider nonetheless states that the manufacturer, controller models and initial access method of the new wave remain unknown ([CyberInsider, 2026-11-02](https://cyberinsider.com/supermarket-refrigeration-cyberattacks-belgium-sweden/)), so the vendor of the Belgian and Swedish sites is not independently confirmed. Coop Switzerland told 20 Minuten that corresponding attempts were registered without success and declined to name its refrigeration equipment, and Migros reports no indication of an attack ([20 Minuten, 2026-11-02](https://www.20min.ch/story/seit-mitte-oktober-mysterioese-hacking-welle-trifft-europaeische-supermaerkte-103660687)); Blick reported that Migros uses the same Danfoss systems in a limited number of Swiss stores ([Blick, 2026-10-13](https://www.blick.ch/fr/suisse/cyberattaque-les-frigos-de-migros-et-coop-sont-ils-proteges/79vpc6q)).

**Exposure:** a Danfoss AK-SM or AK-SC refrigeration controller, or a Copeland or Dixell xweb unit, whose management interface is reachable from the internet, above all legacy units: Danfoss told AFP that most affected units no longer receive updates ([AFP, 2026-10-12](https://www.khaleejtimes.com/world/europe/french-supermarkets-refrigerator-shutdown-cyberattack)) and that the AK-SM800A units hit ran outdated firmware ([Cooling Post, 2026-10-12](https://www.coolingpost.com/world-news/danfoss-moves-to-mitigate-cyberattack/)). Copeland's bulletin of 14 October acknowledges a vulnerability in a discontinued, end-of-life generation of XWEB EVO controllers and says to remove every XWEB EVO from the public internet immediately ([Dixell France, 2026-10-14](https://dixell.fr/wp-content/uploads/2026/10/Recommandations-pour-une-utilisation-securisee-des-superviseurs-XWEB-v1.0.pdf)). For an AK-SM 800A, Censys maps firmware below 4.2 to all three published 2025 flaws and 4.3.1 or later to none ([Censys, 2026-10-14](https://censys.com/blog/frostbitten-in-france-a-danfoss-storeview-internet-exposure-report/)). Ask whoever manages your refrigeration and building services whether such a controller sits in your estate.

**Detection:** on the controller, defrost, setpoint and account changes outside a maintenance window, and defrost duration, which Le Monde reports the attackers lengthened from one hour to eight so that alarms trigger late (translated from French) ([Le Monde, 2026-10-12](https://www.lemonde.fr/economie/article/2026/10/12/journee-noire-dans-les-supermarches-francais-apres-une-cyberattaque-massive_6792763_3234.html)); in firewall, provider VPN or ISP logs, inbound connections to the management interface from addresses other than the contractor's. Forescout advises correlating remote-access sessions with changes to defrost schedules, alarms, setpoints and users, because the abused functions are legitimate ([Forescout, 2026-10-22](https://www.forescout.com/blog/cold-chain-open-control-exposed-refrigeration-systems-reveal-global-risk/)). For a unit not known to be compromised, CERT-FR asks to check the whole configuration, notably the defrost ranges ([CERT-FR, 2026-10-16](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/)).

**Triage:** a defrost cycle is normal; BFMTV reports, citing sector professionals, that installations can be programmed for two hours of defrost per 24 hours, whereas the reported attack is said to be a continuous forced defrost at a 50-degree setpoint held for hours (translated from French) ([BFMTV, 2026-10-12](https://www.bfmtv.com/economie/consommation/la-temperature-est-montee-jusqu-a-50-degres-une-cyberattaque-contre-les-systemes-frigorifiques-provoque-la-destruction-de-produits-frais-dans-des-centaines-d-intermarche-et-de-super-u_AN-202610120327.html)).

**Defender takeaway:** take any Danfoss AK-SM or AK-SC, Copeland xweb or Dixell xweb management interface off the internet now and restore access only through a secure VPN or protected network, as CERT-FR advises ([CERT-FR, 2026-10-13](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/)), and ask the contractor whether its own remote access was affected. For the AK-SM800 and AK-SC355, replacement is the lever: no fix exists for them according to NCSC Switzerland ([NCSC Switzerland, 2026-10-13](https://security-hub.ncsc.admin.ch/#/posts/13054)), and CERT-FR says a factory reset of an unpatched end-of-life unit leaves it vulnerable and almost certainly compromised again ([CERT-FR, 2026-10-13](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/)). A firmware update alone does not close the hole, because ANSSI puts the cause at exposure and weak passwords ([Public Sénat, 2026-10-21](https://www.publicsenat.fr/actualites/politique/des-defauts-de-securisation-elementaire-et-des-mots-de-passe-faibles-ont-permis-la-cyberattaque-contre-les-frigos-de-supermarches)).

## Update — 2026-10-14T03:44:00Z

CERT-FR revised its alert on 2026-10-13: the list of compromised remote controllers now includes Copeland xweb and Dixell xweb besides Danfoss AK-SM and AK-SC, campaigns against these devices are probably still ongoing, and an unpatched end-of-life unit kept on the internet is very likely to be compromised, so a factory reset alone is insufficient ([CERT-FR, 2026-10-13](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/)). NCSC Switzerland published advisory 13054 on 2026-10-13 with the exploitation status Actively Exploited. It lists the Danfoss AK-SM 800 (end of life, no longer patched), the AK-SC 355 (phased out, no longer patched) and the current AK-SM 800A series when it runs outdated firmware, says no fixes exist for the two older models and that Danfoss urges replacing them, and says the attack could affect other sectors, such as healthcare for specialized cooling equipment, so organisations should check whether affected devices are in use ([NCSC Switzerland, 2026-10-13](https://security-hub.ncsc.admin.ch/#/posts/13054)). Danfoss told Cooling Post that the AK-SM800 was declared end of life in 2021, that the AK-SC355 was phased out in 2016, and that the affected AK-SM800A systems ran outdated firmware ([Cooling Post, 2026-10-12](https://www.coolingpost.com/world-news/danfoss-moves-to-mitigate-cyberattack/)). Blick reports that Migros uses the same Danfoss refrigeration systems in a limited number of Swiss stores and sees no sign they were targeted, and that Aldi, Lidl and Coop say they are not affected ([Blick, 2026-10-13](https://www.blick.ch/fr/suisse/cyberattaque-les-frigos-de-migros-et-coop-sont-ils-proteges/79vpc6q)); no source reports a Swiss victim. The advisory relays a six-step CERT-FR sequence (limit access to trusted addresses, factory reset, apply all fixes, rotate passwords and secrets, review accounts, reconfigure) and lists filtering to trusted addresses as a temporary measure ([NCSC Switzerland, 2026-10-13](https://security-hub.ncsc.admin.ch/#/posts/13054)), whereas the revised CERT-FR page puts removal of internet exposure first, accepts source-address filtering only as an emergency stop-gap and lists no secret rotation or account review ([CERT-FR, 2026-10-13](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/)).

## Improvement — 2026-10-15T03:49:00Z

Censys, which scans for Danfoss StoreView control panels, says Danfoss has not confirmed the initial access vector and points to three AK-SM 800A flaws that Danfoss patched more than a year earlier: CVE-2025-41450 (March 2025), which Censys describes as letting an unauthenticated actor log in as an administrator with a code computed from the current calendar date, and CVE-2025-41451 and CVE-2025-41452 (August 2025), which it says let authenticated users run commands and disrupt the management interface ([Censys, 2026-10-14](https://censys.com/blog/frostbitten-in-france-a-danfoss-storeview-internet-exposure-report/)). Censys maps the firmware by build: below 4.2 carries all three, 4.2.4 fixes only the date-based login and still carries the two later ones, and 4.3.1 or later fixes all three ([Censys, 2026-10-14](https://censys.com/blog/frostbitten-in-france-a-danfoss-storeview-internet-exposure-report/)). Its scan counted 1,825 exposed StoreView panels in France on 2026-10-11 and 537 on 2026-10-14, a fall of 71 percent, with builds below 4.2, build 4.2.4 and builds from 4.3.1 leaving at about the same rate, which it reads as operators taking controllers off the internet rather than patching them ([Censys, 2026-10-14](https://censys.com/blog/frostbitten-in-france-a-danfoss-storeview-internet-exposure-report/)). Outside France the count fell from 1,166 to 966, and in ten of the twelve countries with the most exposed hosts more than 60 percent of the hosts run a build below 4.3.1, led by Poland at 81 percent and Romania at 80 percent ([Censys, 2026-10-14](https://censys.com/blog/frostbitten-in-france-a-danfoss-storeview-internet-exposure-report/)).

## Update — 2026-10-18T03:33:00Z

CERT-FR's alert now has a third version, dated 2026-10-16 and listed on the page as an update of the recommendations; the page does not show which sentences changed ([CERT-FR, 2026-10-16](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/)). Its current text separates the two cases. For every unit it asks to remove the internet exposure of the affected units and of any unit on a public IP address, and to check the insurance contract conditions before cutting the data uplink to the refrigeration contractor ([CERT-FR, 2026-10-16](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/)). For a unit not known to be compromised it then asks to check the whole configuration, notably the defrost ranges; for a compromised Danfoss unit it says to restart the equipment or otherwise restore it with a factory reset, and then to reconfigure it for service ([CERT-FR, 2026-10-16](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/)). In both cases access returns only through a secure VPN or protected network, with source-address filtering for the contractors an emergency measure and not a lasting one, and the maker's practices apply ([CERT-FR, 2026-10-16](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/)). The alert still says campaigns are probably ongoing, still names no flaw or entry vector, and gives the risk as not specified by the vendor ([CERT-FR, 2026-10-16](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/)).

The alert's documentation section links an operator guide from Dixell France (Copeland) ([CERT-FR, 2026-10-16](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/)). The file at that address was replaced on 2026-10-18; its current text, described in the correction of 2026-10-19T04:06:00Z, is Copeland's bulletin of 14 October 2026 followed by Dixell France's own complement ([Dixell France, 2026-10-14](https://dixell.fr/wp-content/uploads/2026/10/Recommandations-pour-une-utilisation-securisee-des-superviseurs-XWEB-v1.0.pdf)). That complement says XWEB PRO and EVO ship with the same factory account, Admin with the password Admin, advises keeping the original Admin password sealed or in a password manager and not using it daily, gives each user a named account with an expiry date for an external contractor's account, and requires remote access through an encrypted VPN, with no port forward or DMZ and no remote-control software such as AnyDesk or TeamViewer on a site PC that stays on ([Dixell France, 2026-10-14](https://dixell.fr/wp-content/uploads/2026/10/Recommandations-pour-une-utilisation-securisee-des-superviseurs-XWEB-v1.0.pdf)). CERT-FR does not say how the attackers got in, and SecurityWeek writes that neither Danfoss nor French authorities have tied the attack to the flaws Claroty disclosed ([CERT-FR, 2026-10-16](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/); [SecurityWeek, 2026-10-15](https://www.securityweek.com/supermarket-refrigeration-attack-widens-to-copeland-dixell-controllers/)).

## Correction — 2026-10-19T04:06:00Z

The Dixell France guide that CERT-FR links was replaced on 2026-10-18, the file's date on the vendor's server, and now opens with Copeland's own security bulletin dated 14 October 2026 ([Dixell France, 2026-10-14](https://dixell.fr/wp-content/uploads/2026/10/Recommandations-pour-une-utilisation-securisee-des-superviseurs-XWEB-v1.0.pdf)). The earlier update section's statements about XWEB PRO firmware 1.12.1, a CISA advisory and a March 2024 bulletin are no longer on that page and are removed from the summary and the body. The bulletin acknowledges the vulnerability on a generation of XWEB EVO controllers that is no longer marketed and has reached end of life, says to remove every XWEB EVO from the public internet immediately and then look for suspicious activity from the local network, and says XWEB EVO no longer receives security patches, while XWEB PRO is the supported platform and must not be exposed to the internet either ([Dixell France, 2026-10-14](https://dixell.fr/wp-content/uploads/2026/10/Recommandations-pour-une-utilisation-securisee-des-superviseurs-XWEB-v1.0.pdf)). For an XWEB EVO that may have been accessed it gives a procedure: isolate the unit, restore the latest backup made before the access or otherwise check the users and profiles, set new passwords, check the alarm categories and recipients with a test alarm, and restore the device parameters from backup files or, without one, read each device's parameters and check setpoints, alarm thresholds and defrost parameters; it also says to check the product temperatures in the cabinets directly, since altered setpoints or alarm thresholds can compromise food safety ([Dixell France, 2026-10-14](https://dixell.fr/wp-content/uploads/2026/10/Recommandations-pour-une-utilisation-securisee-des-superviseurs-XWEB-v1.0.pdf)).

Le Monde reports that besides raising the defrost temperature to 50 degrees the attackers lengthened the defrost operation from one hour to eight so that alarms trigger late, which delayed interventions and amplified the damage (translated from French) ([Le Monde, 2026-10-12](https://www.lemonde.fr/economie/article/2026/10/12/journee-noire-dans-les-supermarches-francais-apres-une-cyberattaque-massive_6792763_3234.html)). SecurityWeek relays that detail and adds that the Paris prosecutor's office said the attack caused fires as well as food losses, that the Finance Minister put the number of affected supermarkets at about 700 of roughly 10,000, and that investigators are reportedly puzzled by the lack of a claim of responsibility or a ransom demand, citing Reuters ([SecurityWeek, 2026-10-15](https://www.securityweek.com/supermarket-refrigeration-attack-widens-to-copeland-dixell-controllers/)). Cybersecurity Dive had already reported that a Copeland spokesperson confirmed the vulnerability was found in discontinued end-of-life controllers ([Cybersecurity Dive, 2026-10-15](https://www.cybersecuritydive.com/news/thousands-refrigerator-devices-exposed-french-cyberattack/833117/)).

## Update — 2026-10-25T03:37:30Z

ANSSI's director general, Vincent Strubel, told the French Senate foreign-affairs committee on 2026-10-21 that the attack rested on elementary security flaws, starting with refrigeration equipment directly on the internet and administered without particular protection, and weak passwords, and he dismissed analyses that tied it to vulnerabilities researchers had published over the previous two years ([Public Sénat, 2026-10-21](https://www.publicsenat.fr/actualites/politique/des-defauts-de-securisation-elementaire-et-des-mots-de-passe-faibles-ont-permis-la-cyberattaque-contre-les-frigos-de-supermarches)). Le Monde Informatique reports the same hearing and adds that the systems were reachable without a firewall or network segmentation and that the management interface was protected only by weak passwords ([Le Monde Informatique, 2026-10-22](https://www.lemondeinformatique.fr/actualites/lire-frigos-de-supermarches-pirates-l-anssi-pointe-des-failles-de-securite-elementaires-100864.html)). Neither outlet reports evidence beyond the testimony, and ANSSI names no actor; the account sits against Copeland's acknowledgment of a vulnerability in its end-of-life XWEB EVO controllers and the earlier report that ANSSI had identified a vulnerability in a Danish company's software, and no source reconciles them; the two outlets also differ on the date and the count, Public Sénat giving the night of 12 to 13 October and more than 700 supermarkets, Le Monde Informatique the night of 11 to 12 October and at least 300 Intermarché and Netto shops. Le Monde Informatique adds that ANSSI can alert and advise but has no means to impose connection rules on retailers ([Le Monde Informatique, 2026-10-22](https://www.lemondeinformatique.fr/actualites/lire-frigos-de-supermarches-pirates-l-anssi-pointe-des-failles-de-securite-elementaires-100864.html)), and Public Sénat reports that ANSSI ran a rapid check with health-sector players because laboratories and pharmacies that store vaccines use the same kind of refrigeration equipment ([Public Sénat, 2026-10-21](https://www.publicsenat.fr/actualites/politique/des-defauts-de-securisation-elementaire-et-des-mots-de-passe-faibles-ont-permis-la-cyberattaque-contre-les-frigos-de-supermarches)).

Forescout's Vedere Labs says on 2026-10-22 that the access vector, exploited vulnerabilities, attacker infrastructure, persistence and responsible actors in the French incidents remain unconfirmed, and that the reported changes, made in rapid succession, used ordinary supervisory functions ([Forescout, 2026-10-22](https://www.forescout.com/blog/cold-chain-open-control-exposed-refrigeration-systems-reveal-global-risk/)). Its tracking of hacktivist groups counts over 20 claimed attacks on refrigeration systems since January 2026, the most active being the pro-Russian groups Z-Pentest Alliance and NoName057(16) through internet-exposed human-machine interfaces, and its count of exposed services is 12,976 observations on 6,017 public addresses in 99 countries, with 3,762 exposed Danfoss StoreView observations on AK-SM 800A units, 80 percent of the 4,697 StoreView observations, on firmware older than 4.3.1 ([Forescout, 2026-10-22](https://www.forescout.com/blog/cold-chain-open-control-exposed-refrigeration-systems-reveal-global-risk/)). Forescout adds that the manufacturers' documentation presents internet remote maintenance through port forwarding as a supported option, so the exposure is not only an accident of configuration ([Forescout, 2026-10-22](https://www.forescout.com/blog/cold-chain-open-control-exposed-refrigeration-systems-reveal-global-risk/)).

## Update — 2026-11-02T03:47:57Z

Reuters reported on 2026-10-29, citing four officials, that the Pentagon is treating the late-August freezer failures at military bases across the United States as a suspected hack ([Reuters, 2026-10-29](https://www.internazionale.it/ultime-notizie-reuters/2026/10/29/exclusive-pentagon-treating-military-base-freezer-malfunctions-as-suspected-cyberattack-officials-say)). On Reuters' own review of the bases' social-media posts at least six commissaries were hit, and in at least one case the cooling units' temperatures were raised overnight instead of the units stopping; Fort Huachuca said its freezer "went into defrost mode where it heated up all the food" ([Reuters, 2026-10-29](https://www.internazionale.it/ultime-notizie-reuters/2026/10/29/exclusive-pentagon-treating-military-base-freezer-malfunctions-as-suspected-cyberattack-officials-say)). A Cyber Command unit and the Army Criminal Investigation Division's Cyber Field Office are involved, and one official said the investigators are in touch with their French counterparts about the French attack; Reuters could not establish whether Danfoss or any other controller brand was in use at the bases, nor how far the investigation had got or who might be responsible ([Reuters, 2026-10-29](https://www.internazionale.it/ultime-notizie-reuters/2026/10/29/exclusive-pentagon-treating-military-base-freezer-malfunctions-as-suspected-cyberattack-officials-say)).

Nextgov reported on 2026-10-30, citing two people familiar with the matter, that US officials suspect Iran-linked hackers, that the intrusions began around late August, that how the intruders got in is not clear and that the assessment may change ([Nextgov, 2026-10-30](https://www.nextgov.com/cybersecurity/2026/10/officials-suspect-iran-series-cyberattacks-military-base-freezers/416934/)). No official has attributed the activity on the record, and the sources give no technical evidence for the suspicion. The only stated link between the two cases is the investigators' contact, and Reuters notes that the French attack, like the Fort Huachuca failure, raised temperatures instead of switching units off ([Reuters, 2026-10-29](https://www.internazionale.it/ultime-notizie-reuters/2026/10/29/exclusive-pentagon-treating-military-base-freezer-malfunctions-as-suspected-cyberattack-officials-say)).

## Update — 2026-11-03T03:45:49Z

On 2026-11-02 refrigeration failures struck stores in Belgium, Luxembourg, the Netherlands, Sweden, Ireland and Estonia, and Finland according to The Guardian; BleepingComputer counts more than 115 affected stores from company statements and says it is unclear whether they were hit in a coordinated attack, and several companies confirmed they had been hacked ([BleepingComputer, 2026-11-02](https://www.bleepingcomputer.com/news/security/hackers-disrupt-refrigeration-systems-at-european-supermarkets/); [The Guardian, 2026-11-02](https://www.theguardian.com/world/2026/nov/02/supermarket-freezers-across-europe-hit-by-second-suspected-cyber-attack)). Sabcobel's chief executive says the units' evaporators were switched to defrost mode ([The Guardian, 2026-11-02](https://www.theguardian.com/world/2026/nov/02/supermarket-freezers-across-europe-hit-by-second-suspected-cyber-attack)) and, per BleepingComputer, that the attacker used the same vulnerability as in France ([BleepingComputer, 2026-11-02](https://www.bleepingcomputer.com/news/security/hackers-disrupt-refrigeration-systems-at-european-supermarkets/)); Euronews names Danfoss as the software supplier in both incidents and quotes it saying customers who had not updated their software were affected ([Euronews, 2026-11-02](https://www.euronews.com/2026/11/02/cyberattack-hits-belgian-supermarket-fridges-and-freezers)), and in Estonia attackers reached the control computer of an older Danfoss system with outdated software (translated from German) ([Tagesschau, 2026-11-02](https://www.tagesschau.de/wirtschaft/technologie/cyberangriff-supermaerkte-100.html)). CyberInsider nonetheless states that the manufacturer, controller models and initial access method of the new wave remain unknown ([CyberInsider, 2026-11-02](https://cyberinsider.com/supermarket-refrigeration-cyberattacks-belgium-sweden/)), so the vendor of the Belgian and Swedish sites is not independently confirmed. Coop Switzerland told 20 Minuten that corresponding attempts were registered without success, and Migros reports no indication of an attack ([20 Minuten, 2026-11-02](https://www.20min.ch/story/seit-mitte-oktober-mysterioese-hacking-welle-trifft-europaeische-supermaerkte-103660687)). The head of Sweden's national cybersecurity centre says it is working on incidents around the country and that Sweden has quite a lot of exposed operational technology devices ([The Guardian, 2026-11-02](https://www.theguardian.com/world/2026/nov/02/supermarket-freezers-across-europe-hit-by-second-suspected-cyber-attack)).
