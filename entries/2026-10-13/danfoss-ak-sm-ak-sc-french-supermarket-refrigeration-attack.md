---
schema: 1
kind: incident
title: "Danfoss AK-SM and AK-SC, Copeland xweb and Dixell xweb refrigeration controllers compromised, with forced defrost at hundreds of French supermarkets, refrigeration failures at more than 115 shops in at least six more countries and first cases in Germany, and on 2026-11-02 altered settings in the cold rooms of the French blood service through a refrigeration supplier, and on 2026-11-05 the first publicly known cases in Switzerland; France attributes the 11 to 12 October campaign to the IRGC unit Shahid Kaveh; ENISA and Europol call for immediate action"
headline: "France blames Iran's IRGC for the October refrigeration attacks; Swiss cases (Köniz, Volg) are not attributed"
summary: >
  Coopérative U, Intermarché and E. Leclerc confirmed to AFP a cyberattack on their refrigeration systems overnight on 11 to 12 October 2026, a remotely forced defrost at hundreds of French stores, and on 2026-11-09 France's foreign ministry and the C4 crisis cell attributed that campaign to the Iranian unit Shahid Kaveh, affiliated with the Revolutionary Guard's electronic and cyber centre, CERT-FR calling its case a bundle of indicators. The French documents cover that campaign only: more than 115 stores in at least six more countries and the first German shops followed on 2026-11-02, the French blood service reported altered cold-room settings at three sites the same day, and SRF reported on 2026-11-05 the first publicly known Swiss cases, a Köniz butcher and three Volg stores. CERT-FR reports numerous compromises of Danfoss AK-SM and AK-SC controllers and of Copeland xweb and Dixell xweb; NCSC Switzerland rates the activity actively exploited but says the public information does not establish a common attack method or confirm exploitation of the Danfoss CVEs it lists, and ANSSI says controllers directly on the internet and weak passwords were exploited. CISA, FBI, HHS, USDA and DOT published a joint warning on refrigeration and cold-chain controllers that names no vendor. BACS repeated its warning publicly on 2026-11-10 and says security updates fixing the known flaws exist for the Danfoss AK-SM 800A and 8xxA family. ENISA, the European Commission, Europol and the CSIRTs Network advised immediate action on 2026-11-04, and Ransom-ISAC's log of one Copeland XWEB Pro compromise shows 743 parameter writes in two administrator sessions.
discovered_at: "2026-10-13T03:41:00Z"
updated_at: "2026-11-11T03:52:45Z"
event_date: "2026-10-12"
run_id: 2026-10-13T0256Z-intel
priority: high
immediate_action: null
tags: [ot-ics, actively-exploited, nation-state]
regions: [europe, switzerland]
sectors: [retail, healthcare]
entities: ["incident:danfoss-ak-sm-ak-sc-french-supermarket-refrigeration-attack-2026-10", "actor:shahid-kaveh", "actor:cyberav3ngers", "product:danfoss-ak-sm-800", "product:danfoss-ak-sc-355", "product:danfoss-ak-sm-800a", "product:copeland-xweb", "product:dixell-xweb"]
techniques: [T1190, T1133, T1078, T1595.001, T1596.005]
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
  - url: "https://www.heise.de/news/Cyberangriffe-auf-Kuehlschraenke-Erste-deutsche-Faelle-in-Bayern-und-NRW-11508922.html"
    publisher: "heise online"
    date: "2026-11-03"
    role: corroborating
  - url: "https://www1.wdr.de/nrw/cyberangriffe-supermarkt-kuehltruhen-nrw-100.html"
    publisher: "WDR"
    date: "2026-11-03"
    role: corroborating
  - url: "https://www.sentinelone.com/labs/defrost-and-disrupt-an-assessment-of-europe-s-refrigeration-attacks/"
    publisher: "SentinelLABS"
    date: "2026-11-03"
    role: corroborating
  - url: "https://www.lecanardenchaine.fr/police-justice/55332-les-hackers-ont-du-sang-sur-les-mains"
    publisher: "Le Canard enchaîné"
    date: "2026-11-03"
    role: corroborating
  - url: "https://presse.efs.sante.fr/actualites/l-efs-confirme-l-incident-de-cybersecurite-impactant-un-de-ces-prestataires-d-equipement-frigorifique-2c07c-08a0a.html"
    publisher: "Établissement français du sang (press release, in French)"
    date: "2026-11-03"
    role: primary
  - url: "https://www.coolworld-rentals.com/news/cybersecurity-update"
    publisher: "Coolworld International (statement)"
    date: "2026-11-04"
    role: corroborating
  - url: "https://www.enisa.europa.eu/news/joint-statement-on-cyber-incidents-in-refrigeration-systems-across-the-eu"
    publisher: "ENISA (joint statement)"
    date: "2026-11-04"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/cyberattack-disrupts-blood-storage-refrigeration-systems-in-france/"
    publisher: "BleepingComputer (blood-storage refrigeration)"
    date: "2026-11-04"
    role: corroborating
  - url: "https://www.heise.de/news/Nach-Gefriertruhen-Attacken-Jetzt-Blutbank-Kuehlung-im-Visier-11511444.html"
    publisher: "heise online (blood-bank cooling)"
    date: "2026-11-04"
    role: corroborating
  - url: "https://www.srf.ch/news/international/hintergruende-unklar-hackerangriff-auf-kuehlsysteme-blutbanken-in-frankreich-betroffen"
    publisher: "SRF"
    date: "2026-11-04"
    role: corroborating
  - url: "https://www.franceinfo.fr/internet/securite-sur-internet/cyberattaques/cyberattaques-des-frigos-pirates-les-stocks-de-l-etablissement-francais-du-sang-vises_8268404.html"
    publisher: "franceinfo"
    date: "2026-11-04"
    role: corroborating
  - url: "https://www.acn.gov.it/portale/w/sicurezza-dei-sistemi-a-supporto-della-catena-del-freddo-e-interfacce-di-management-di-sistemi-connessi-richiamo-urgente-alle-misure-di-verifica-e-mitigazione"
    publisher: "CSIRT Italia (bulletin BL02/261104/CSIRT-ITA)"
    date: "2026-11-04"
    role: corroborating
  - url: "https://www.acn.gov.it/portale/w/misure-urgenti-di-verifica-e-mitigazione-per-operatori-della-distribuzione-alimentare-e-della-filiera-del-freddo"
    publisher: "CSIRT Italia (bulletin BL01/261013/CSIRT-ITA, version of 2026-11-04)"
    date: "2026-11-04"
    role: corroborating
  - url: "https://www.srf.ch/news/schweiz/kuehlanlage-manipuliert-berner-metzgerei-opfer-von-hackerangriff-auch-volg-betroffen"
    publisher: "SRF"
    date: "2026-11-05"
    role: corroborating
  - url: "https://www.swissinfo.ch/ger/metzgerei-in-k%c3%b6niz-muss-nach-cyberangriff-vor%c3%bcbergehend-schliessen/92334848"
    publisher: "Keystone-SDA via swissinfo.ch (Köniz butcher)"
    date: "2026-11-05"
    role: corroborating
  - url: "https://www.swissinfo.ch/ger/hackerattacken-auf-gewerbe%3a-bund-begr%c3%bcsst-freiwillige-meldungen/92335202"
    publisher: "Keystone-SDA via swissinfo.ch (BACS statement)"
    date: "2026-11-05"
    role: corroborating
  - url: "https://www.cisa.gov/resources-tools/resources/us-government-partners-urge-hardening-industrial-refrigeration-and-cold-chain-monitoring-systems"
    publisher: "CISA, FBI, HHS, USDA and DOT (joint fact sheet)"
    date: "2026-11-05"
    role: corroborating
  - url: "https://ransom-isac.org/blog/the-copeland-incident/"
    publisher: "Ransom-ISAC"
    date: "2026-11-06"
    role: corroborating
  - url: "https://unit42.paloaltonetworks.com/europes-refrigeration-systems-attacks/"
    publisher: "Unit 42 (Palo Alto Networks)"
    date: "2026-11-06"
    role: corroborating
  - url: "https://www.diplomatie.gouv.fr/fr/presse-et-ressources/decouvrir-et-informer/actualites/declaration-d-attribution-a-l-iran-de-cyberattaques-visant-la-france"
    publisher: "French Ministry for Europe and Foreign Affairs (attribution statement)"
    date: "2026-11-09"
    role: corroborating
  - url: "https://www.cert.ssi.gouv.fr/uploads/CERTFR-2026-CTI-009.pdf"
    publisher: "CERT-FR (CERTFR-2026-CTI-009, report of the C4 crisis cell)"
    date: "2026-11-09"
    role: corroborating
  - url: "https://www.sekoia.com/blog/the-cold-chain-on-fire-unpatched-danfoss-controllers-exploited"
    publisher: "Sekoia"
    date: "2026-11-10"
    role: corroborating
  - url: "https://www.nbcnews.com/world/france/france-supermarket-cyberattacks-iran-revolutionary-guard-corps-accused-rcna608354"
    publisher: "Reuters (via NBC News)"
    date: "2026-11-09"
    role: corroborating
  - url: "https://www.bacs.admin.ch/de/warnung-kuehlanlagen-de"
    publisher: "BACS / NCSC.ch (public warning on cold-chain controllers)"
    date: "2026-11-10"
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
  - quote: "Responsibility for the European incidents has not been publicly established."
    publisher: "SentinelLABS"
    source_url: "https://www.sentinelone.com/labs/defrost-and-disrupt-an-assessment-of-europe-s-refrigeration-attacks/"
  - quote: "In a supermarket in Reisbach in Lower Bavaria, the cooling systems were heated to 50 degrees Celsius overnight into Monday. (translated from German)"
    original: "In einem Supermarkt im niederbayerischen Reisbach sind die Kühlanlagen in der Nacht zu Montag auf 50 Grad Celsius hochgeheizt worden."
    publisher: "heise online"
    source_url: "https://www.heise.de/news/Cyberangriffe-auf-Kuehlschraenke-Erste-deutsche-Faelle-in-Bayern-und-NRW-11508922.html"
  - quote: "There is zero operational consequence, because the situation was spotted. (translated from French)"
    original: "Il y a zéro conséquence opératoire, car la situation a été repérée."
    publisher: "Le Canard enchaîné (quoting the French Health Ministry)"
    source_url: "https://www.lecanardenchaine.fr/police-justice/55332-les-hackers-ont-du-sang-sur-les-mains"
  - quote: "On 2 November 2026, a refrigeration-equipment supplier of the Établissement français du sang (EFS) suffered a cybersecurity incident. The supervision and control installations of cold rooms deployed at three EFS sites were affected. (translated from French)"
    original: "Le 2 novembre 2026, un prestataire d’équipement frigorifique de l’Établissement français du sang (EFS) a été victime d'un incident de cybersécurité. Les installations de supervision et de pilotage de chambres froides déployées sur trois sites de l'EFS ont été touchées."
    publisher: "Établissement français du sang"
    source_url: "https://presse.efs.sante.fr/actualites/l-efs-confirme-l-incident-de-cybersecurite-impactant-un-de-ces-prestataires-d-equipement-frigorifique-2c07c-08a0a.html"
  - quote: "No health impact has been identified and no loss of blood products is to be reported. (translated from French)"
    original: "Aucun impact sanitaire n’a été identifié et aucune perte de produits sanguins n’est à déclarer."
    publisher: "Établissement français du sang"
    source_url: "https://presse.efs.sante.fr/actualites/l-efs-confirme-l-incident-de-cybersecurite-impactant-un-de-ces-prestataires-d-equipement-frigorifique-2c07c-08a0a.html"
  - quote: "Following a new wave of incidents having occurred on 1-2 November, ENISA, the European Commission (DG CNECT), Europol’s European Cybercrime Centre (EC3), the Network of the EU national computer security incident response teams (EU CSIRTs Network) and the European cyber crisis liaison organisation Network (EU- CyCLONe), advise organisations to take immediate action to mitigate exposure in the affected systems."
    publisher: "ENISA (joint statement)"
    source_url: "https://www.enisa.europa.eu/news/joint-statement-on-cyber-incidents-in-refrigeration-systems-across-the-eu"
  - quote: "The vulnerability currently being reported in the media relates to a component from a third-party supplier and was outside Coolworld’s direct control."
    publisher: "Coolworld International"
    source_url: "https://www.coolworld-rentals.com/news/cybersecurity-update"
  - quote: "It is the first publicly known attack of this kind in Switzerland. (translated from German)"
    original: "Es ist der erste öffentlich gewordene Angriff dieser Art in der Schweiz."
    publisher: "SRF"
    source_url: "https://www.srf.ch/news/schweiz/kuehlanlage-manipuliert-berner-metzgerei-opfer-von-hackerangriff-auch-volg-betroffen"
  - quote: "Three of the stores noticed that parameters in the cooling shelves had been changed, according to the company on request. (translated from German)"
    original: "Drei der Filialen bemerkten, dass Parameter in den Kühlregalen verstellt wurden, wie es auf Anfrage heisst."
    publisher: "SRF"
    source_url: "https://www.srf.ch/news/schweiz/kuehlanlage-manipuliert-berner-metzgerei-opfer-von-hackerangriff-auch-volg-betroffen"
  - quote: "In total, one reportable notification about a cyberattack on commercial refrigeration systems has been received so far. (translated from German)"
    original: "Insgesamt sei bislang eine meldepflichtige Meldung zu einem Cyberangriff auf gewerbliche Kühlanlagen eingegangen."
    publisher: "Keystone-SDA via swissinfo.ch"
    source_url: "https://www.swissinfo.ch/ger/hackerattacken-auf-gewerbe%3a-bund-begr%c3%bcsst-freiwillige-meldungen/92335202"
  - quote: "The actors may exploit vulnerabilities or weaknesses in unpatched or internet-accessible controllers to remotely alter settings and force units into continuous heating and defrost cycles"
    publisher: "CISA, FBI, HHS, USDA and DOT"
    source_url: "https://www.cisa.gov/resources-tools/resources/us-government-partners-urge-hardening-industrial-refrigeration-and-cold-chain-monitoring-systems"
  - quote: "Do not expose control system devices and/or systems, particularly controller panels, to the internet"
    publisher: "CISA, FBI, HHS, USDA and DOT"
    source_url: "https://www.cisa.gov/resources-tools/resources/us-government-partners-urge-hardening-industrial-refrigeration-and-cold-chain-monitoring-systems"
  - quote: "The public information reviewed does not establish a common attack method across these incidents or confirm exploitation of the specific Danfoss CVEs listed above."
    publisher: "NCSC Switzerland"
    source_url: "https://security-hub.ncsc.admin.ch/#/posts/13054"
  - quote: "In total, the log records 743 parameter writes affecting 31 devices."
    publisher: "Ransom-ISAC"
    source_url: "https://ransom-isac.org/blog/the-copeland-incident/"
  - quote: "France is able to attribute to Iran these destructive actions, carried out by the cyber-offensive unit SHAHID KAVEH, affiliated with the electronic and cyber centre of the Islamic Revolutionary Guard Corps of Iran. (translated from French)"
    original: "la France est en mesure d’attribuer à l’Iran ces actions destructrices, mises en œuvre par à l’unité cyberoffensive SHAHID KAVEH, affiliée au centre électronique et cyber du Corps des Gardiens de la Révolution Islamique d’Iran"
    publisher: "French Ministry for Europe and Foreign Affairs"
    source_url: "https://www.diplomatie.gouv.fr/fr/presse-et-ressources/decouvrir-et-informer/actualites/declaration-d-attribution-a-l-iran-de-cyberattaques-visant-la-france"
  - quote: "Available evidence shows similarities in the timing, the infrastructure, the targeting and observed tradecraft across the October and November waves"
    publisher: "Sekoia"
    source_url: "https://www.sekoia.com/blog/the-cold-chain-on-fire-unpatched-danfoss-controllers-exploited"
  - quote: "security updates that fix the known vulnerabilities are available (translated from German)"
    original: "stehen Sicherheitsupdates zur Verfügung, welche die bekannten Schwachstellen beheben"
    publisher: "BACS"
    source_url: "https://www.bacs.admin.ch/de/warnung-kuehlanlagen-de"
  - quote: "Newer firmware versions also activate additional protection mechanisms and enforce encrypted communication over HTTPS. (translated from German)"
    original: "Neuere Firmware-Versionen aktivieren zudem zusätzliche Schutzmechanismen und erzwingen die verschlüsselte Kommunikation über HTTPS."
    publisher: "BACS"
    source_url: "https://www.bacs.admin.ch/de/warnung-kuehlanlagen-de"
verification: multi-source
sourcing_note: >
  CERT-FR's alert is the national authority's own statement, in its revision of 2026-10-16 (its page does not show which sentences changed), while NCSC Switzerland adds the exploitation rating and relays an older CERT-FR remediation sequence, and the retailers' confirmations, Danfoss's statement and the Paris prosecutor's investigation come through AFP. The forced 50-degree defrost and the "older than version 4" scope are BFMTV's reporting alone, store counts differ between AFP, BFMTV and Infosecurity, and ANSSI's account of the cause is its director general's testimony as Public Sénat and Le Monde Informatique report it, with no transcript read, while Forescout says the access vector, exploited vulnerabilities and actors remain unconfirmed and Censys points to three patched 2025 AK-SM 800A flaws and says Danfoss has not confirmed the vector.
  The Dixell France PDF opens with Copeland's bulletin dated 14 October 2026, and the file at that address was replaced on 2026-10-18. The second wave of 2026-11-02 rests on company statements and press: the claim that the attacker used the same vulnerability as in France is Sabcobel's as BleepingComputer reports it, and CyberInsider states that the manufacturer, controller models and initial access method of the new wave are unknown. The German cases rest on heise and WDR reporting, with the cause unconfirmed by the police, the maintenance-firm account the operator's own and heise adding that the BSI knows of cases at individual supermarkets; SentinelLABS' assessment is its own reading of public reporting; and the blood-service case rests on EFS's own press release and Coolworld's statement, relayed by franceinfo, BleepingComputer, heise and SRF: neither EFS nor Coolworld names the other, that link is the outlets', and Coolworld's statement does not say attackers exploited the component. ENISA's joint statement names no product, actor or count.
  The Swiss cases of 2026-11-05 rest on SRF's reporting, the owner's and Volg's own statements as SRF and Keystone-SDA relay them, and BACS's reply to Keystone-SDA; no authority finding, controller make or access route is stated, and the joint CISA, FBI, HHS, USDA and DOT fact sheet names no vendor, victim or actor.
  The Ransom-ISAC log is a supplied event log of unstated origin; its statement that the controller was still on default credentials rests on evidence it does not publish, and it says the log cannot show how the attackers got in. Unit 42's exposure counts are one vendor's scan counts and do not show vulnerable versions.
  The attribution of 2026-11-09 is the French government's own: the foreign ministry states it, and CERT-FR's report for the C4 crisis cell words it as a bundle of indicators naming the Revolutionary Guard as sponsor and Shahid Kaveh as executing unit, for the campaign of 11 to 12 October only; Reuters, as relayed by NBC News, says it could not establish how the French reached the determination, and Iran routinely denies such operations. Sekoia's honeypot observations are its own telemetry, and its view that the October and November waves may share an actor is a hypothesis, not a finding of the French documents.
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
  - "Find every Danfoss AK-SM and AK-SC, Copeland xweb and Dixell xweb refrigeration controller, and any other refrigeration controller with a remote management interface because not every second-wave site's vendor is confirmed, in facilities you own or that a contractor manages for you and take its management interface off the internet now, restoring access only through a secure VPN or protected network (filtering to the contractor's source addresses is an emergency stop-gap, and CERT-FR asks you to check your insurance conditions before cutting the contractor's data uplink); an end-of-life unit that gets no fixes needs replacing, because a factory reset leaves it vulnerable and probably compromised again."
  - "On every such controller that was reachable from the internet, check the whole configuration, defrost ranges, alarm thresholds and notification recipients included, against the intended one, verify the actual temperatures and test that alarms reach staff; for a Danfoss unit that may have been taken over, restart it or otherwise factory-reset it, restore access only through a secure VPN or protected network and reconfigure it for service, then update its firmware, set the security level to Strict and replace the default and any weak passwords, and on every Copeland or Dixell XWEB unit confirm the factory Admin password was changed and give each contractor a named account with an expiry date."
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
  - at: "2026-11-04T03:30:36Z"
    run_id: 2026-11-04T0256Z-intel
    type: update
    summary: >
      The attacks reached Germany: heise reports an Edeka market in Reisbach whose cooling systems were
      heated to 50 degrees overnight into 2 November, WDR quotes a CAP supermarket manager saying the
      attack hit the firm that maintains the cooling plants remotely and reports that Rewe's head office
      confirmed an attack aimed at Danfoss; SentinelLABS says responsibility has not been publicly
      established; and Le Canard enchaîné reports that cold rooms of a contractor of the French blood
      service were programmed to 110 degrees overnight on 1 to 2 November, with no source tying that case
      to these controllers.
    fields: [title, headline, summary, sources, evidence, sourcing_note, body, actions]
  - at: "2026-11-05T04:02:44Z"
    run_id: 2026-11-05T0255Z-intel
    type: update
    summary: >
      The French blood service EFS confirmed that an incident at its refrigeration supplier on 2 November
      altered the temperature and defrost thresholds of cold rooms at three of its sites, caught by its
      own alarms with no loss of blood products, so the case no longer rests on Le Canard enchaîné alone;
      ENISA, the European Commission, Europol and the CSIRTs Network advised organisations on 2026-11-04
      to take immediate action, CSIRT Italia issued cold-chain measures, and no source ties the
      blood-service case to the Danfoss, Copeland or Dixell controllers.
    fields: [title, headline, summary, sectors, sources, evidence, sourcing_note, body]
  - at: "2026-11-06T03:44:30Z"
    run_id: 2026-11-06T0255Z-intel
    type: update
    summary: >
      SRF reported on 2026-11-05 the first publicly known cases of the refrigeration attacks in Switzerland, a butcher in Köniz whose freezer reached 50 to 70 degrees and three Volg stores with changed cooling parameters; BACS has received one reportable notification about an attack on commercial refrigeration, and CISA, FBI, HHS, USDA and DOT published a joint fact sheet on refrigeration and cold-chain controllers that names no vendor, CVE or actor. No source names the controller make or the access route in the Swiss cases.
    fields: [title, headline, summary, sources, evidence, sourcing_note, body]
  - at: "2026-11-07T03:53:29Z"
    run_id: 2026-11-07T0256Z-intel
    type: update
    summary: >
      NCSC Switzerland updated its advisory on 2026-11-06 with the Swiss incidents, Copeland and Dixell
      XWEB and healthcare, a four-point checklist for refrigeration management systems across all relevant
      operations, supplier-managed equipment included, and the statement that the public information does
      not establish a common attack method or confirm exploitation of the Danfoss CVEs it lists.
      Ransom-ISAC published the event log of one internet-reachable Copeland XWEB Pro compromise (743
      parameter writes in two administrator sessions, default credentials claimed without published
      evidence), and Unit 42 counts over 5,000 exposed devices across countries on 5 and 6 November and a
      falling count in France since October.
    fields: [summary, actions, sources, evidence, sourcing_note]
  - at: "2026-11-10T03:42:41Z"
    run_id: 2026-11-10T0255Z-intel
    type: update
    summary: >
      France's foreign ministry and the C4 crisis cell attributed the 11 to 12 October
      refrigeration-controller campaign to Iran on 2026-11-09, naming the Revolutionary Guard unit Shahid
      Kaveh, and the Paris prosecutor requested arrest warrants against its leader and two deputies; the
      French documents cover that campaign only, and the later waves and the Swiss cases are not
      attributed in them.
    fields: [title, headline, summary, tags, entities, techniques, sources, evidence, sourcing_note, body]
  - at: "2026-11-11T03:52:45Z"
    run_id: 2026-11-11T0256Z-intel
    type: update
    summary: >
      BACS published its own public warning on 2026-11-10: it says Switzerland is affected and that the
      controllers also run in butchers, restaurants, pharmacies, doctors' practices, laboratories,
      logistics, industry and farms, many of whose operators do not know their plants are reachable from
      the internet, and it repeats that security updates for the AK-SM 800A and 8xxA family exist and that
      newer firmware enforces HTTPS.
    fields: [summary, sources, evidence, body]
migrated_from: null
---

Coopérative U, Intermarché and E. Leclerc confirmed to AFP a cyberattack on their refrigeration systems overnight on 11 to 12 October 2026, at hundreds of stores ([AFP, 2026-10-12](https://www.khaleejtimes.com/world/europe/french-supermarkets-refrigerator-shutdown-cyberattack)). CERT-FR knows of numerous compromises of Danfoss AK-SM and AK-SC controllers and of Copeland xweb and Dixell xweb, and says exposing a management interface to the internet is contrary to good practice ([CERT-FR, 2026-10-16](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/)); NCSC Switzerland rates the activity actively exploited ([NCSC Switzerland, 2026-10-13](https://security-hub.ncsc.admin.ch/#/posts/13054)), and BACS repeated its warning publicly on 2026-11-10, saying that Switzerland is affected too ([BACS, 2026-11-10](https://www.bacs.admin.ch/de/warnung-kuehlanlagen-de)). On 2026-11-09 France's foreign ministry attributed the 11 to 12 October campaign to the Iranian unit Shahid Kaveh, affiliated with the Revolutionary Guard's electronic and cyber centre ([French Ministry for Europe and Foreign Affairs, 2026-11-09](https://www.diplomatie.gouv.fr/fr/presse-et-ressources/decouvrir-et-informer/actualites/declaration-d-attribution-a-l-iran-de-cyberattaques-visant-la-france)), and CERT-FR's report words this as a bundle of indicators ([CERT-FR, 2026-11-09](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2026-CTI-009.pdf)); it covers the French campaign only, and Sekoia says the evidence suggests the October and November waves may share an actor ([Sekoia, 2026-11-10](https://www.sekoia.com/blog/the-cold-chain-on-fire-unpatched-danfoss-controllers-exploited)).

On 2026-11-02 retailers in Belgium, Luxembourg, the Netherlands, Sweden, Ireland, Estonia and, per The Guardian, Finland reported refrigeration failures, more than 115 stores according to BleepingComputer, and the first German cases followed ([BleepingComputer, 2026-11-02](https://www.bleepingcomputer.com/news/security/hackers-disrupt-refrigeration-systems-at-european-supermarkets/); [The Guardian, 2026-11-02](https://www.theguardian.com/world/2026/nov/02/supermarket-freezers-across-europe-hit-by-second-suspected-cyber-attack); [heise, 2026-11-03](https://www.heise.de/news/Cyberangriffe-auf-Kuehlschraenke-Erste-deutsche-Faelle-in-Bayern-und-NRW-11508922.html)). SRF reported on 2026-11-05 the first publicly known Swiss cases, at a butcher in Köniz and at three Volg stores ([SRF, 2026-11-05](https://www.srf.ch/news/schweiz/kuehlanlage-manipuliert-berner-metzgerei-opfer-von-hackerangriff-auch-volg-betroffen)).

A separate incident reached healthcare cold storage. The French blood service EFS confirmed that on 2026-11-02 a refrigeration-equipment supplier suffered a cybersecurity incident that affected the supervision and control installations of cold rooms at three EFS sites and raised their temperature and defrost thresholds to very high values (translated from French) ([EFS, 2026-11-03](https://presse.efs.sante.fr/actualites/l-efs-confirme-l-incident-de-cybersecurite-impactant-un-de-ces-prestataires-d-equipement-frigorifique-2c07c-08a0a.html)). BleepingComputer, heise and SRF name the supplier as Coolworld, SRF adding that the attackers reportedly came in through its remote maintenance, and Coolworld says the incident involved remote monitoring software ([BleepingComputer, 2026-11-04](https://www.bleepingcomputer.com/news/security/cyberattack-disrupts-blood-storage-refrigeration-systems-in-france/); [heise, 2026-11-04](https://www.heise.de/news/Nach-Gefriertruhen-Attacken-Jetzt-Blutbank-Kuehlung-im-Visier-11511444.html); [SRF, 2026-11-04](https://www.srf.ch/news/international/hintergruende-unklar-hackerangriff-auf-kuehlsysteme-blutbanken-in-frankreich-betroffen); [Coolworld, 2026-11-04](https://www.coolworld-rentals.com/news/cybersecurity-update)). None of these sources names Danfoss, Copeland or Dixell equipment for the blood-service case.

ENISA, the European Commission, Europol and the EU CSIRTs Network advise organisations to take immediate action to mitigate exposure after the new wave of 1 to 2 November ([ENISA, 2026-11-04](https://www.enisa.europa.eu/news/joint-statement-on-cyber-incidents-in-refrigeration-systems-across-the-eu)).

**Exposure:** a Danfoss AK-SM or AK-SC refrigeration controller, or a Copeland or Dixell xweb unit, whose management interface is reachable from the internet, above all legacy units: Danfoss told AFP that most affected units no longer receive updates ([AFP, 2026-10-12](https://www.khaleejtimes.com/world/europe/french-supermarkets-refrigerator-shutdown-cyberattack)). A second class is cold rooms supervised through a contractor's solution: EFS was not itself targeted, yet its cold-room settings were altered through its supplier ([EFS, 2026-11-03](https://presse.efs.sante.fr/actualites/l-efs-confirme-l-incident-de-cybersecurite-impactant-un-de-ces-prestataires-d-equipement-frigorifique-2c07c-08a0a.html)). BACS adds that they also run in butchers, restaurants, pharmacies, doctors' practices, laboratories, logistics, industry and farms, and that many operators do not know their plants are reachable from the internet (translated from German) ([BACS, 2026-11-10](https://www.bacs.admin.ch/de/warnung-kuehlanlagen-de)).

**Detection:** on the controller, defrost, setpoint and account changes outside a maintenance window, and defrost duration, which Le Monde reports the attackers lengthened from one hour to eight so that alarms trigger late (translated from French) ([Le Monde, 2026-10-12](https://www.lemonde.fr/economie/article/2026/10/12/journee-noire-dans-les-supermarches-francais-apres-une-cyberattaque-massive_6792763_3234.html)); in firewall, provider VPN or ISP logs, inbound connections to the management interface from addresses other than the contractor's. EFS's own monitoring and alarm systems caught the altered thresholds ([EFS, 2026-11-03](https://presse.efs.sante.fr/actualites/l-efs-confirme-l-incident-de-cybersecurite-impactant-un-de-ces-prestataires-d-equipement-frigorifique-2c07c-08a0a.html)), and CSIRT Italia says to check actual temperatures and alarm function with instruments independent of the supervision platform ([CSIRT Italia, 2026-11-04](https://www.acn.gov.it/portale/w/misure-urgenti-di-verifica-e-mitigazione-per-operatori-della-distribuzione-alimentare-e-della-filiera-del-freddo)).

**Triage:** a defrost cycle is normal; BFMTV reports that installations can be programmed for two hours of defrost per 24 hours, whereas the reported attack is a continuous forced defrost at a 50-degree setpoint (translated from French) ([BFMTV, 2026-10-12](https://www.bfmtv.com/economie/consommation/la-temperature-est-montee-jusqu-a-50-degres-une-cyberattaque-contre-les-systemes-frigorifiques-provoque-la-destruction-de-produits-frais-dans-des-centaines-d-intermarche-et-de-super-u_AN-202610120327.html)).

**Defender takeaway:** take any Danfoss AK-SM or AK-SC, Copeland xweb or Dixell xweb management interface off the internet now and restore access only through a secure VPN or protected network, as CERT-FR advises ([CERT-FR, 2026-10-13](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/)), and ask the contractor whether its own remote access or monitoring platform was affected. For the AK-SM800 and AK-SC355, replacement is the lever: no fix exists for them according to NCSC Switzerland ([NCSC Switzerland, 2026-10-13](https://security-hub.ncsc.admin.ch/#/posts/13054)), and CERT-FR says a factory reset of an unpatched end-of-life unit leaves it vulnerable and almost certainly compromised again ([CERT-FR, 2026-10-13](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/)). For the current AK-SM 800A and 8xxA family BACS says security updates fixing the known flaws exist and newer firmware enforces HTTPS ([BACS, 2026-11-10](https://www.bacs.admin.ch/de/warnung-kuehlanlagen-de)).

## Update — 2026-10-14T03:44:00Z

CERT-FR revised its alert on 2026-10-13: the list of compromised remote controllers now includes Copeland xweb and Dixell xweb besides Danfoss AK-SM and AK-SC, campaigns against these devices are probably still ongoing, and an unpatched end-of-life unit kept on the internet is very likely to be compromised, so a factory reset alone is insufficient ([CERT-FR, 2026-10-13](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/)). NCSC Switzerland published advisory 13054 on 2026-10-13 with the exploitation status Actively Exploited. It lists the Danfoss AK-SM 800 (end of life, no longer patched), the AK-SC 355 (phased out, no longer patched) and the current AK-SM 800A series when it runs outdated firmware, says no fixes exist for the two older models and that Danfoss urges replacing them, and says the attack could affect other sectors, such as healthcare for specialized cooling equipment, so organisations should check whether affected devices are in use ([NCSC Switzerland, 2026-10-13](https://security-hub.ncsc.admin.ch/#/posts/13054)). Danfoss told Cooling Post that the AK-SM800 was declared end of life in 2021, that the AK-SC355 was phased out in 2016, and that the affected AK-SM800A systems ran outdated firmware ([Cooling Post, 2026-10-12](https://www.coolingpost.com/world-news/danfoss-moves-to-mitigate-cyberattack/)). Blick reports that Migros uses the same Danfoss refrigeration systems in a limited number of Swiss stores and sees no sign they were targeted, and that Aldi, Lidl and Coop say they are not affected ([Blick, 2026-10-13](https://www.blick.ch/fr/suisse/cyberattaque-les-frigos-de-migros-et-coop-sont-ils-proteges/79vpc6q)); as of 2026-10-14 no source reported a Swiss victim. The advisory relays a six-step CERT-FR sequence (limit access to trusted addresses, factory reset, apply all fixes, rotate passwords and secrets, review accounts, reconfigure) and lists filtering to trusted addresses as a temporary measure ([NCSC Switzerland, 2026-10-13](https://security-hub.ncsc.admin.ch/#/posts/13054)), whereas the revised CERT-FR page puts removal of internet exposure first, accepts source-address filtering only as an emergency stop-gap and lists no secret rotation or account review ([CERT-FR, 2026-10-13](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/)).

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

## Update — 2026-11-04T03:30:36Z

The first German cases followed on 2026-11-02: heise reports that the cooling systems of an Edeka market in Reisbach, Lower Bavaria, were heated to 50 degrees overnight into Monday and that the police have not confirmed a cyberattack as the cause, and WDR quotes a division manager at a CAP supermarket in North Rhine-Westphalia saying the actual attack hit the firm that maintains the cooling plants remotely, which is the operator's statement and not an authority finding, and Rewe's head office confirmed to WDR a cyberattack aimed specifically at the cooling-system supplier Danfoss, whose technology only a few regional Rewe stores use (translated from German) ([heise, 2026-11-03](https://www.heise.de/news/Cyberangriffe-auf-Kuehlschraenke-Erste-deutsche-Faelle-in-Bayern-und-NRW-11508922.html); [WDR, 2026-11-03](https://www1.wdr.de/nrw/cyberangriffe-supermarkt-kuehltruhen-nrw-100.html)). SentinelLABS' assessment of 2026-11-03 says responsibility for the European incidents has not been publicly established, calls Russian-aligned disruptive groups one credible hypothesis based on precedent, and says shared maintenance access deserves scrutiny ([SentinelLABS, 2026-11-03](https://www.sentinelone.com/labs/defrost-and-disrupt-an-assessment-of-europe-s-refrigeration-attacks/)). Le Canard enchaîné reports that Coolworld, a company that maintains refrigerated storage containers for the French blood service, was hacked overnight on 1 to 2 November and that cold rooms held at minus 30 degrees were programmed to reach 110 degrees; the blood service says an on-duty technician saw the temperature rise and acknowledges that frozen plasma intended for transfusion was among the products, and the Health Ministry says there was zero operational consequence because the situation was spotted (translated from French) ([Le Canard enchaîné, 2026-11-03](https://www.lecanardenchaine.fr/police-justice/55332-les-hackers-ont-du-sang-sur-les-mains)). The 110 degrees is the programmed set-point and not a measured temperature, and no source names the equipment, the vendor or the access method, or ties this case to the Danfoss and Copeland controllers.

## Update — 2026-11-05T04:02:44Z

The French blood service EFS confirmed on 2026-11-03 that on 2 November a refrigeration-equipment supplier suffered a cybersecurity incident that affected the supervision and control installations of cold rooms at three EFS sites, with temperature and defrost thresholds raised to very high values (translated from French) ([EFS, 2026-11-03](https://presse.efs.sante.fr/actualites/l-efs-confirme-l-incident-de-cybersecurite-impactant-un-de-ces-prestataires-d-equipement-frigorifique-2c07c-08a0a.html)). EFS says its own monitoring and alarm systems identified the anomalies quickly, the affected equipment was brought under control without impact on the products or neutralised, the products stored in those cold rooms were transferred preventively to other installations, and no health impact or loss of blood products is to be reported; it names no supplier and gives no temperature figure (translated from French) ([EFS, 2026-11-03](https://presse.efs.sante.fr/actualites/l-efs-confirme-l-incident-de-cybersecurite-impactant-un-de-ces-prestataires-d-equipement-frigorifique-2c07c-08a0a.html)).

BleepingComputer, heise and SRF identify the supplier as Coolworld, and SRF reports that the attackers reportedly entered through its remote maintenance ([BleepingComputer, 2026-11-04](https://www.bleepingcomputer.com/news/security/cyberattack-disrupts-blood-storage-refrigeration-systems-in-france/); [heise, 2026-11-04](https://www.heise.de/news/Nach-Gefriertruhen-Attacken-Jetzt-Blutbank-Kuehlung-im-Visier-11511444.html); [SRF, 2026-11-04](https://www.srf.ch/news/international/hintergruende-unklar-hackerangriff-auf-kuehlsysteme-blutbanken-in-frankreich-betroffen)). Coolworld's statement of 2026-11-04 says the incident involved remote monitoring software, that the vulnerability reported in the media relates to a component from a third-party supplier outside its control and that a limited number of its units were affected; it does not say that attackers exploited that component ([Coolworld, 2026-11-04](https://www.coolworld-rentals.com/news/cybersecurity-update)). BleepingComputer's account reads it the other way, saying Coolworld says the attackers exploited a vulnerability in a third-party component, which the statement does not state ([BleepingComputer, 2026-11-04](https://www.bleepingcomputer.com/news/security/cyberattack-disrupts-blood-storage-refrigeration-systems-in-france/)). No source names Danfoss, Copeland or Dixell equipment for this case.

ENISA, the European Commission (DG CNECT), Europol's EC3, the EU CSIRTs Network and EU-CyCLONe issued a joint statement on 2026-11-04: since 11 October 2026 several commercial refrigeration systems and similar devices have been hit in a number of EU Member States, a new wave occurred on 1 to 2 November, affected Member States are investigating and issuing guidance, and organisations are advised to take immediate action to mitigate exposure in the affected systems; it names no product, actor or count and does not mention Switzerland ([ENISA, 2026-11-04](https://www.enisa.europa.eu/news/joint-statement-on-cyber-incidents-in-refrigeration-systems-across-the-eu)). CSIRT Italia's bulletin of 2026-11-04 extends its call to every operator of cold-chain technology, whatever the sector, to apply its earlier measures urgently, removing direct internet exposure of administrative and control interfaces and verifying that operating parameters and alarms are intact first ([CSIRT Italia, 2026-11-04](https://www.acn.gov.it/portale/w/sicurezza-dei-sistemi-a-supporto-della-catena-del-freddo-e-interfacce-di-management-di-sistemi-connessi-richiamo-urgente-alle-misure-di-verifica-e-mitigazione)). Its bulletin of 2026-10-13, re-issued on 2026-11-04 as version 1.2, asks operators to limit supplier access to authorised resources and periods, to require multi-factor authentication on remote access, applied on the mediating system when the device cannot do it, and to check actual temperatures and alarms with instruments independent of the supervision platform ([CSIRT Italia, 2026-11-04](https://www.acn.gov.it/portale/w/misure-urgenti-di-verifica-e-mitigazione-per-operatori-della-distribuzione-alimentare-e-della-filiera-del-freddo)). The BSI had urged operators of networked freezer controllers to disconnect them from the internet or at least secure and patch them ([heise, 2026-11-04](https://www.heise.de/news/Nach-Gefriertruhen-Attacken-Jetzt-Blutbank-Kuehlung-im-Visier-11511444.html)).

## Update — 2026-11-06T03:44:30Z

SRF reported on 2026-11-05 the first publicly known attack of this kind in Switzerland: the butcher Lüthis Fleischwaren in Köniz, canton Bern, told customers that manipulation of the electronic control of its cooling and freezer systems caused considerable temperature deviations, the owner told SRF he found 50 to 70 degrees in the freezer, and the firm disconnected the installation from the network and closed the branch (translated from German) ([SRF, 2026-11-05](https://www.srf.ch/news/schweiz/kuehlanlage-manipuliert-berner-metzgerei-opfer-von-hackerangriff-auch-volg-betroffen)). Keystone-SDA adds that the shop can probably only reopen on 20 November and that the Bern cantonal police were briefly informed on Monday and had received no complaint yet ([Keystone-SDA via swissinfo.ch, 2026-11-05](https://www.swissinfo.ch/ger/metzgerei-in-k%c3%b6niz-muss-nach-cyberangriff-vor%c3%bcbergehend-schliessen/92334848)). Volg says three of its stores noticed that parameters in the cooling shelves had been changed ([SRF, 2026-11-05](https://www.srf.ch/news/schweiz/kuehlanlage-manipuliert-berner-metzgerei-opfer-von-hackerangriff-auch-volg-betroffen)). No source names the controller make, the access route or a maintenance provider in the Swiss cases; Keystone-SDA notes that operators can supervise cooling plants centrally over the internet and that the butcher apparently has such an installation, which is the agency's inference and not the owner's statement ([Keystone-SDA via swissinfo.ch, 2026-11-05](https://www.swissinfo.ch/ger/metzgerei-in-k%c3%b6niz-muss-nach-cyberangriff-vor%c3%bcbergehend-schliessen/92334848)). BACS told Keystone-SDA that it does not comment on specific incidents and has received one reportable notification about a cyberattack on commercial refrigeration so far, and it stressed that voluntary reports are welcome at any time ([Keystone-SDA via swissinfo.ch, 2026-11-05](https://www.swissinfo.ch/ger/hackerattacken-auf-gewerbe%3a-bund-begr%c3%bcsst-freiwillige-meldungen/92335202)). Blutspende SRK Schweiz told Keystone-SDA that no attacks on Swiss blood-donation services are known to date ([SRF, 2026-11-05](https://www.srf.ch/news/schweiz/kuehlanlage-manipuliert-berner-metzgerei-opfer-von-hackerangriff-auch-volg-betroffen)).

On the same day CISA, the FBI, HHS, USDA and DOT published a joint fact sheet on malicious cyber activity against industrial refrigeration and cold-chain monitoring systems worldwide: the actors may exploit vulnerabilities or weaknesses in unpatched or internet-accessible controllers to remotely alter settings and force units into continuous heating and defrost cycles, through authentication bypass, arbitrary code injection or weak configurations, with loss of visibility into current temperatures as a further effect ([CISA, 2026-11-05](https://www.cisa.gov/resources-tools/resources/us-government-partners-urge-hardening-industrial-refrigeration-and-cold-chain-monitoring-systems)). It names no vendor, CVE, victim or actor; its mitigations include keeping controller panels off the internet, allowlisting the devices and IP addresses that may change settings, defining reasonable setpoint limits for downstream devices with alerting on deviations, and collecting network traffic between OT assets where logs are not available ([CISA, 2026-11-05](https://www.cisa.gov/resources-tools/resources/us-government-partners-urge-hardening-industrial-refrigeration-and-cold-chain-monitoring-systems)).

## Update — 2026-11-07T03:53:29Z

NCSC Switzerland edited its advisory on 2026-11-06 with the reason "added Swiss incidents, Copeland/Dixell XWEB and healthcare attacks" and states that "The public information reviewed does not establish a common attack method across these incidents or confirm exploitation of the specific Danfoss CVEs listed above"; it lists CVE-2025-41451, CVE-2025-41450 and CVE-2025-41452 as "alleged as potentially related" ([NCSC Switzerland, 2026-10-13](https://security-hub.ncsc.admin.ch/#/posts/13054)). Its checklist asks operators to review refrigeration management systems across all relevant operations, "including equipment managed by external service providers"; to remove direct internet access to management interfaces and provide remote access through a secure VPN; to check temperature settings, defrost schedules, alarm thresholds, notification recipients and user accounts, verify actual temperatures and test alarm delivery; and to apply current firmware and plan to replace equipment that no longer gets security updates ([NCSC Switzerland, 2026-10-13](https://security-hub.ncsc.admin.ch/#/posts/13054)). For a suspected compromise it says "A factory reset alone is insufficient if the system remains vulnerable and directly accessible from the internet" ([NCSC Switzerland, 2026-10-13](https://security-hub.ncsc.admin.ch/#/posts/13054)).

Ransom-ISAC published the event log of a Copeland XWEB Pro controller, reportedly on firmware 1.9.0 and reachable through a public address, compromised on 2 November: two Administrator sessions from different external addresses read parameters across 31 devices, then made 588 writes across 26 devices in about six minutes, which Ransom-ISAC reads as scripted or bulk programming rather than manual edits, and 155 further writes across five cold rooms, moving setpoints to 110 and 150 degrees C and recording keypad-lock, alarm-mute and defrost commands ([Ransom-ISAC, 2026-11-06](https://ransom-isac.org/blog/the-copeland-incident/)). The post says the controller still used its default Administrator credentials, publishes no evidence for that statement, says the log cannot show how the attackers got in or what temperatures were reached, and says it has no evidence linking the case to NoName057(16), Z-Pentest Alliance or the French attacks ([Ransom-ISAC, 2026-11-06](https://ransom-isac.org/blog/the-copeland-incident/)). Its suggested alerts are more than about 20 parameter-write events a minute from one account, writes to more than three devices within five minutes, and keypad-lock, alarm-mute or defrost commands that do not come from the scheduler ([Ransom-ISAC, 2026-11-06](https://ransom-isac.org/blog/the-copeland-incident/)).

Unit 42 counts over 5,000 internet-exposed devices across countries from the manufacturers CERT-FR names on 5 and 6 November, and for France alone 1,853 in the first half of October, 558 in the second half and 316 in the first six days of November, and says the claims of NoName057(16) and Z-Pentest Alliance remain unverified ([Unit 42, 2026-11-06](https://unit42.paloaltonetworks.com/europes-refrigeration-systems-attacks/)). The counts do not show which versions are vulnerable.

## Update — 2026-11-10T03:42:41Z

France's foreign ministry said on 2026-11-09 that, following the investigation, France is able to attribute the destructive actions of the night of 11 to 12 October to Iran, carried out by the cyber-offensive unit Shahid Kaveh, affiliated with the electronic and cyber centre of the Islamic Revolutionary Guard Corps, and calls it the first cyber-offensive campaign run purely for sabotage on French soil (translated from French) ([French Ministry for Europe and Foreign Affairs, 2026-11-09](https://www.diplomatie.gouv.fr/fr/presse-et-ressources/decouvrir-et-informer/actualites/declaration-d-attribution-a-l-iran-de-cyberattaques-visant-la-france)). The report of the C4 crisis cell, which CERT-FR published, words the case as a bundle of indicators that names the Revolutionary Guard as sponsor and Shahid Kaveh as executing unit (translated from French) ([CERT-FR, 2026-11-09](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2026-CTI-009.pdf)). The indicators it lists are attack infrastructure also used in the same period to reconnoitre Schneider Electric equipment, use of the FOFA scan tool, which it says the unit habitually uses, relay of the attack on the unit's CyberbanNews outlet from 13 October, and traces of Farsi in the attack infrastructure ([CERT-FR, 2026-11-09](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2026-CTI-009.pdf)).

The same report says the unit is known mainly through hacktivist personas, CyberAveng3rs among them, and the CyberbanNews outlet, and that it has held scripts since at least June 2024 to scan, access and control Schneider Electric, Siemens and Rockwell industrial equipment; in April 2026 it was seen using Modbus on TCP port 502 for mass reconnaissance of Schneider Electric systems, including in France ([CERT-FR, 2026-11-09](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2026-CTI-009.pdf)). The C4 links to the same attack the concurrent targeting of Schneider Electric equipment at small hydroelectric installations in France, with moderate effects on the targeted equipment ([CERT-FR, 2026-11-09](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2026-CTI-009.pdf)). Industrial controllers of that class, reachable on Modbus, belong in the same internet-exposure check as the refrigeration controllers.

The attribution covers the French campaign of 11 to 12 October. Sekoia's honeypots recorded unauthenticated requests to the controllers' xml.cgi endpoint from 26 addresses, password spraying of the Supervisor and admin accounts and, on 2026-11-01, an attempt to use a non-public flaw that renames an account by its numerical identifier; Sekoia says the evidence shows similarities between the October and November waves that suggest they may share an actor, and that it assesses the NoName057(16) and Z-Pentest Alliance claim with doubts ([Sekoia, 2026-11-10](https://www.sekoia.com/blog/the-cold-chain-on-fire-unpatched-danfoss-controllers-exploited)). Reuters reports that the Paris prosecutor's office said it had requested international arrest warrants against the leader of Shahid Kaveh and his two deputies, and that it could not establish exactly how the French made their determination ([Reuters via NBC News, 2026-11-09](https://www.nbcnews.com/world/france/france-supermarket-cyberattacks-iran-revolutionary-guard-corps-accused-rcna608354)). NCSC Switzerland's advisory still says the public information does not establish a common attack method across the incidents ([NCSC Switzerland, 2026-10-13](https://security-hub.ncsc.admin.ch/#/posts/13054)).

## Update — 2026-11-11T03:52:45Z

BACS published a public warning on 2026-11-10, which repeats the earlier warning of the Cyber Security Hub advisory cited above; it says the attacks of recent weeks show that Switzerland is affected too and that it is repeating its warning because the systems are widespread among small and medium-sized businesses (translated from German) ([BACS, 2026-11-10](https://www.bacs.admin.ch/de/warnung-kuehlanlagen-de)). Per BACS, attackers reach management interfaces that are directly reachable from the internet and then change temperatures, defrost cycles, alarm thresholds or notification settings remotely, which can spoil food, medicines and other temperature-sensitive goods; it names the end-of-life AK-SM 800 and AK-SC 355, the current AK-SM 800A and 8xxA family when it runs outdated firmware, and Copeland and Dixell XWEB.

What is new is the wider population: BACS lists butchers and food producers, restaurants and hotels, pharmacies, doctors' practices and laboratories, logistics and warehouses, industry and farms among the users, many of which do not know their cooling plants are reachable from the internet or run by an external provider, and it repeats what the Hub advisory already said, that security updates fixing the known flaws are available for the AK-SM 800A and 8xxA family and that newer firmware activates additional protections and enforces encrypted HTTPS communication (translated from German) ([BACS, 2026-11-10](https://www.bacs.admin.ch/de/warnung-kuehlanlagen-de)). It recommends identifying the controllers, those run by contractors included, installing vendor updates, restricting unsupported systems to trusted networks or a VPN, reaching them remotely only through one centrally managed access point with default passwords replaced, and replacing end-of-life products; it names no attacker, no exploited CVE and no count of Swiss victims.
