---
title: "Objet: Multiples vulnérabilités dans les produits Cisco"
url: https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-1197/
hostname: gouv.fr
sitename: cert.ssi.gouv.fr
date: "2026-09-17"
---
## Risques

- Atteinte à l'intégrité des données
- Atteinte à la confidentialité des données
- Contournement de la politique de sécurité
- Déni de service à distance
- Exécution de code arbitraire à distance
- Injection SQL (SQLi)
- Non spécifié par l'éditeur
- Élévation de privilèges

## Systèmes affectés

- Adaptive Security Appliance (ASA), se référer au bulletin de sécurité de l'éditeur pour la liste des systèmes affectés (cf. section Documentation)
- Firewall Management Center (FMC), se référer au bulletin de sécurité de l'éditeur pour la liste des systèmes affectés (cf. section Documentation)
- Firewall Threat Defense (FTD), se référer au bulletin de sécurité de l'éditeur pour la liste des systèmes affectés (cf. section Documentation)
- ISE ou ISE-PIC versions 3.4 antérieures à 3.4 Patch 7
- ISE versions 3.2 antérieures à 3.2 Patch 11
- ISE versions 3.5 antérieures à 3.5 Patch 4
- ISE versions antérieures à 3.1 Patch 12
- ISE versions antérieures à 3.3 Patch 12

Cisco indique que les versions 3.2 et 3.1 de Identity Services Engine (ISE) ne seront plus supportées à partir du 30 novembre 2027 et n'ont pas reçu de correctif pour les vulnérabilités CVE-2026-20247, CVE-2026-20282, CVE-2026-20300, CVE-2026-76424, CVE-2026-76425, CVE-2026-76426, CVE-2026-76427 et CVE-2026-76428.

La branche 3.0 ne l'est plus depuis le 13 juillet 2025.

Concernant ISE-PIC, l'éditeur indique que ce produit n'est plus commercialisé et que la version 3.4 est la dernière encore maintenue.

## Résumé

De multiples vulnérabilités ont été découvertes dans les produits Cisco. Certaines d'entre elles permettent à un attaquant de provoquer une exécution de code arbitraire à distance, une élévation de privilèges et un déni de service à distance.

Cisco indique que la vulnérabilité CVE-2026-76460 est activement exploitée.

## Solutions

Se référer au bulletin de sécurité de l'éditeur pour l'obtention des correctifs (cf. section Documentation).

## Documentation

- Bulletin de sécurité Cisco cisco-sa-asa-ftd-logging-dos-ZXXNesfN du 16 septembre 2026
- Bulletin de sécurité Cisco cisco-sa-asaftd-dtls-dos-Kp57HkyO du 16 septembre 2026
- Bulletin de sécurité Cisco cisco-sa-asaftd-eigrp-dos-GOhNejSj du 16 septembre 2026
- Bulletin de sécurité Cisco cisco-sa-asaftd-ikev2cert-dos-uWyc2xtv du 16 septembre 2026
- Bulletin de sécurité Cisco cisco-sa-fmc-javarce-y2NypXwk du 16 septembre 2026
- Bulletin de sécurité Cisco cisco-sa-fmc-mulivulns-4PsnFwvx du 16 septembre 2026
- Bulletin de sécurité Cisco cisco-sa-fmc-sftunn-codex-c3O4Jft2 du 16 septembre 2026
- Bulletin de sécurité Cisco cisco-sa-fmc2-multivulns-HXgcqRG du 16 septembre 2026
- Bulletin de sécurité Cisco cisco-sa-fmcftd-sftun-multivulns-WGVHOrN3 du 16 septembre 2026
- Bulletin de sécurité Cisco cisco-sa-ftd-tls1 du 16 septembre 2026
- Bulletin de sécurité Cisco cisco-sa-hardening-asaftdfmc-uvpPROhN du 16 septembre 2026
- Bulletin de sécurité Cisco cisco-sa-hardening-ise-XU5EwX5T du 16 septembre 2026
- Bulletin de sécurité Cisco cisco-sa-hardening-ndw1-psFvnrg du 16 septembre 2026
- Bulletin de sécurité Cisco cisco-sa-ISE-ABP-VNSW7Tn5 du 16 septembre 2026
- Bulletin de sécurité Cisco cisco-sa-ise-cmd-inj-e2CuZCYZ du 16 septembre 2026
- Bulletin de sécurité Cisco cisco-sa-ise-mult-vul-ymSsTLCc du 16 septembre 2026
- Bulletin de sécurité Cisco cisco-sa-ise-multi-hrP9jQSQ du 16 septembre 2026
- Bulletin de sécurité Cisco cisco-sa-ise-RADIUS-dos-wR3hYPMw du 16 septembre 2026
- Bulletin de sécurité Cisco cisco-sa-ise-rce-se7bYU57 du 16 septembre 2026
- Bulletin de sécurité Cisco cisco-sa-ise-sql-inj-3QTKR947 du 16 septembre 2026
- Support ISE Cisco
- Référence CVE CVE-2026-20130
- Référence CVE CVE-2026-20135
- Référence CVE CVE-2026-20154
- Référence CVE CVE-2026-20176
- Référence CVE CVE-2026-20192
- Référence CVE CVE-2026-20194
- Référence CVE CVE-2026-20211
- Référence CVE CVE-2026-20222
- Référence CVE CVE-2026-20234
- Référence CVE CVE-2026-20237
- Référence CVE CVE-2026-20242
- Référence CVE CVE-2026-20247
- Référence CVE CVE-2026-20249
- Référence CVE CVE-2026-20250
- Référence CVE CVE-2026-20282
- Référence CVE CVE-2026-20283
- Référence CVE CVE-2026-20284
- Référence CVE CVE-2026-20287
- Référence CVE CVE-2026-20295
- Référence CVE CVE-2026-20300
- Référence CVE CVE-2026-20305
- Référence CVE CVE-2026-20306
- Référence CVE CVE-2026-20307
- Référence CVE CVE-2026-20322
- Référence CVE CVE-2026-20323
- Référence CVE CVE-2026-20324
- Référence CVE CVE-2026-20325
- Référence CVE CVE-2026-20326
- Référence CVE CVE-2026-20329
- Référence CVE CVE-2026-20330
- Référence CVE CVE-2026-20331
- Référence CVE CVE-2026-20332
- Référence CVE CVE-2026-20333
- Référence CVE CVE-2026-20334
- Référence CVE CVE-2026-20335
- Référence CVE CVE-2026-20336
- Référence CVE CVE-2026-20340
- Référence CVE CVE-2026-20341
- Référence CVE CVE-2026-20342
- Référence CVE CVE-2026-20343
- Référence CVE CVE-2026-20344
- Référence CVE CVE-2026-20352
- Référence CVE CVE-2026-20360
- Référence CVE CVE-2026-20361
- Référence CVE CVE-2026-76409
- Référence CVE CVE-2026-76412
- Référence CVE CVE-2026-76413
- Référence CVE CVE-2026-76420
- Référence CVE CVE-2026-76423
- Référence CVE CVE-2026-76424
- Référence CVE CVE-2026-76425
- Référence CVE CVE-2026-76426
- Référence CVE CVE-2026-76427
- Référence CVE CVE-2026-76428
- Référence CVE CVE-2026-76460

[https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asa-ftd-logging-dos-ZXXNesfN](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asa-ftd-logging-dos-ZXXNesfN)

[https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-dtls-dos-Kp57HkyO](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-dtls-dos-Kp57HkyO)

[https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-eigrp-dos-GOhNejSj](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-eigrp-dos-GOhNejSj)

[https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-ikev2cert-dos-uWyc2xtv](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-ikev2cert-dos-uWyc2xtv)

[https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-fmc-javarce-y2NypXwk](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-fmc-javarce-y2NypXwk)

[https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-fmc-mulivulns-4PsnFwvx](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-fmc-mulivulns-4PsnFwvx)

[https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-fmc-sftunn-codex-c3O4Jft2](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-fmc-sftunn-codex-c3O4Jft2)

[https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-fmc2-multivulns-HXgcqRG](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-fmc2-multivulns-HXgcqRG)

[https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-fmcftd-sftun-multivulns-WGVHOrN3](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-fmcftd-sftun-multivulns-WGVHOrN3)

[https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ftd-tls1.3-dos-dLxwFWgF](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ftd-tls1.3-dos-dLxwFWgF)

[https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-asaftdfmc-uvpPROhN](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-asaftdfmc-uvpPROhN)

[https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-ise-XU5EwX5T](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-ise-XU5EwX5T)

[https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-ndw1-psFvnrg](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-ndw1-psFvnrg)

[https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ISE-ABP-VNSW7Tn5](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ISE-ABP-VNSW7Tn5)

[https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ise-cmd-inj-e2CuZCYZ](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ise-cmd-inj-e2CuZCYZ)

[https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ise-mult-vul-ymSsTLCc](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ise-mult-vul-ymSsTLCc)

[https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ise-multi-hrP9jQSQ](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ise-multi-hrP9jQSQ)

[https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ise-RADIUS-dos-wR3hYPMw](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ise-RADIUS-dos-wR3hYPMw)

[https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ise-rce-se7bYU57](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ise-rce-se7bYU57)

[https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ise-sql-inj-3QTKR947](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ise-sql-inj-3QTKR947)

[https://www.cisco.com/c/en/us/support/security/identity-services-engine/series.html](https://www.cisco.com/c/en/us/support/security/identity-services-engine/series.html)

[https://www.cve.org/CVERecord?id=CVE-2026-20130](https://www.cve.org/CVERecord?id=CVE-2026-20130)

[https://www.cve.org/CVERecord?id=CVE-2026-20135](https://www.cve.org/CVERecord?id=CVE-2026-20135)

[https://www.cve.org/CVERecord?id=CVE-2026-20154](https://www.cve.org/CVERecord?id=CVE-2026-20154)

[https://www.cve.org/CVERecord?id=CVE-2026-20176](https://www.cve.org/CVERecord?id=CVE-2026-20176)

[https://www.cve.org/CVERecord?id=CVE-2026-20192](https://www.cve.org/CVERecord?id=CVE-2026-20192)

[https://www.cve.org/CVERecord?id=CVE-2026-20194](https://www.cve.org/CVERecord?id=CVE-2026-20194)

[https://www.cve.org/CVERecord?id=CVE-2026-20211](https://www.cve.org/CVERecord?id=CVE-2026-20211)

[https://www.cve.org/CVERecord?id=CVE-2026-20222](https://www.cve.org/CVERecord?id=CVE-2026-20222)

[https://www.cve.org/CVERecord?id=CVE-2026-20234](https://www.cve.org/CVERecord?id=CVE-2026-20234)

[https://www.cve.org/CVERecord?id=CVE-2026-20237](https://www.cve.org/CVERecord?id=CVE-2026-20237)

[https://www.cve.org/CVERecord?id=CVE-2026-20242](https://www.cve.org/CVERecord?id=CVE-2026-20242)

[https://www.cve.org/CVERecord?id=CVE-2026-20247](https://www.cve.org/CVERecord?id=CVE-2026-20247)

[https://www.cve.org/CVERecord?id=CVE-2026-20249](https://www.cve.org/CVERecord?id=CVE-2026-20249)

[https://www.cve.org/CVERecord?id=CVE-2026-20250](https://www.cve.org/CVERecord?id=CVE-2026-20250)

[https://www.cve.org/CVERecord?id=CVE-2026-20282](https://www.cve.org/CVERecord?id=CVE-2026-20282)

[https://www.cve.org/CVERecord?id=CVE-2026-20283](https://www.cve.org/CVERecord?id=CVE-2026-20283)

[https://www.cve.org/CVERecord?id=CVE-2026-20284](https://www.cve.org/CVERecord?id=CVE-2026-20284)

[https://www.cve.org/CVERecord?id=CVE-2026-20287](https://www.cve.org/CVERecord?id=CVE-2026-20287)

[https://www.cve.org/CVERecord?id=CVE-2026-20295](https://www.cve.org/CVERecord?id=CVE-2026-20295)

[https://www.cve.org/CVERecord?id=CVE-2026-20300](https://www.cve.org/CVERecord?id=CVE-2026-20300)

[https://www.cve.org/CVERecord?id=CVE-2026-20305](https://www.cve.org/CVERecord?id=CVE-2026-20305)

[https://www.cve.org/CVERecord?id=CVE-2026-20306](https://www.cve.org/CVERecord?id=CVE-2026-20306)

[https://www.cve.org/CVERecord?id=CVE-2026-20307](https://www.cve.org/CVERecord?id=CVE-2026-20307)

[https://www.cve.org/CVERecord?id=CVE-2026-20322](https://www.cve.org/CVERecord?id=CVE-2026-20322)

[https://www.cve.org/CVERecord?id=CVE-2026-20323](https://www.cve.org/CVERecord?id=CVE-2026-20323)

[https://www.cve.org/CVERecord?id=CVE-2026-20324](https://www.cve.org/CVERecord?id=CVE-2026-20324)

[https://www.cve.org/CVERecord?id=CVE-2026-20325](https://www.cve.org/CVERecord?id=CVE-2026-20325)

[https://www.cve.org/CVERecord?id=CVE-2026-20326](https://www.cve.org/CVERecord?id=CVE-2026-20326)

[https://www.cve.org/CVERecord?id=CVE-2026-20329](https://www.cve.org/CVERecord?id=CVE-2026-20329)

[https://www.cve.org/CVERecord?id=CVE-2026-20330](https://www.cve.org/CVERecord?id=CVE-2026-20330)

[https://www.cve.org/CVERecord?id=CVE-2026-20331](https://www.cve.org/CVERecord?id=CVE-2026-20331)

[https://www.cve.org/CVERecord?id=CVE-2026-20332](https://www.cve.org/CVERecord?id=CVE-2026-20332)

[https://www.cve.org/CVERecord?id=CVE-2026-20333](https://www.cve.org/CVERecord?id=CVE-2026-20333)

[https://www.cve.org/CVERecord?id=CVE-2026-20334](https://www.cve.org/CVERecord?id=CVE-2026-20334)

[https://www.cve.org/CVERecord?id=CVE-2026-20335](https://www.cve.org/CVERecord?id=CVE-2026-20335)

[https://www.cve.org/CVERecord?id=CVE-2026-20336](https://www.cve.org/CVERecord?id=CVE-2026-20336)

[https://www.cve.org/CVERecord?id=CVE-2026-20340](https://www.cve.org/CVERecord?id=CVE-2026-20340)

[https://www.cve.org/CVERecord?id=CVE-2026-20341](https://www.cve.org/CVERecord?id=CVE-2026-20341)

[https://www.cve.org/CVERecord?id=CVE-2026-20342](https://www.cve.org/CVERecord?id=CVE-2026-20342)

[https://www.cve.org/CVERecord?id=CVE-2026-20343](https://www.cve.org/CVERecord?id=CVE-2026-20343)

[https://www.cve.org/CVERecord?id=CVE-2026-20344](https://www.cve.org/CVERecord?id=CVE-2026-20344)

[https://www.cve.org/CVERecord?id=CVE-2026-20352](https://www.cve.org/CVERecord?id=CVE-2026-20352)

[https://www.cve.org/CVERecord?id=CVE-2026-20360](https://www.cve.org/CVERecord?id=CVE-2026-20360)

[https://www.cve.org/CVERecord?id=CVE-2026-20361](https://www.cve.org/CVERecord?id=CVE-2026-20361)

[https://www.cve.org/CVERecord?id=CVE-2026-76409](https://www.cve.org/CVERecord?id=CVE-2026-76409)

[https://www.cve.org/CVERecord?id=CVE-2026-76412](https://www.cve.org/CVERecord?id=CVE-2026-76412)

[https://www.cve.org/CVERecord?id=CVE-2026-76413](https://www.cve.org/CVERecord?id=CVE-2026-76413)

[https://www.cve.org/CVERecord?id=CVE-2026-76420](https://www.cve.org/CVERecord?id=CVE-2026-76420)

[https://www.cve.org/CVERecord?id=CVE-2026-76423](https://www.cve.org/CVERecord?id=CVE-2026-76423)

[https://www.cve.org/CVERecord?id=CVE-2026-76424](https://www.cve.org/CVERecord?id=CVE-2026-76424)

[https://www.cve.org/CVERecord?id=CVE-2026-76425](https://www.cve.org/CVERecord?id=CVE-2026-76425)

[https://www.cve.org/CVERecord?id=CVE-2026-76426](https://www.cve.org/CVERecord?id=CVE-2026-76426)

[https://www.cve.org/CVERecord?id=CVE-2026-76427](https://www.cve.org/CVERecord?id=CVE-2026-76427)

[https://www.cve.org/CVERecord?id=CVE-2026-76428](https://www.cve.org/CVERecord?id=CVE-2026-76428)

[https://www.cve.org/CVERecord?id=CVE-2026-76460](https://www.cve.org/CVERecord?id=CVE-2026-76460)
