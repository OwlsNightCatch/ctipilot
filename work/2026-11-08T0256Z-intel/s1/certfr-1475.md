---
title: Avis du CERT-FR
url: https://www.cert.cyber.gouv.fr/avis/CERTFR-2026-AVI-1475/
hostname: gouv.fr
sitename: cert.cyber.gouv.fr
date: "2024-04-08"
fingerprint: "6903c59ee6ec838b"
---
# Avis du CERT-FR

Objet : Multiples vulnérabilités dans les produits Splunk

## Gestion du document

Une gestion de version détaillée se trouve à la fin de ce document.

## Risques

- Atteinte à l'intégrité des données
- Atteinte à la confidentialité des données
- Contournement de la politique de sécurité
- Exécution de code arbitraire à distance
- Non spécifié par l'éditeur

## Systèmes affectés

- AppDynamics On-Premises
- AppDynamics SaaS
- Observability OpenTelemetry Collector versions antérieures à 0.163.1
- Python for Scientific Computing
- Smartlook
- Splunk Attack Analyzer
- Splunk Enterprise version 10.0 antérieures à 10.2
- Splunk Observability Cloud
- Splunk SOAR Automation Broker
- Splunk UBA
- Splunk Visual Exporter

Splunk recommande de désactiver ou de désinstaller l'application Visual Exporter

## Résumé

De multiples vulnérabilités ont été découvertes dans les produits Splunk. Certaines d'entre elles permettent à un attaquant de provoquer une exécution de code arbitraire à distance, une atteinte à la confidentialité des données et une atteinte à l'intégrité des données.

## Solutions

Se référer au bulletin de sécurité de l'éditeur pour l'obtention des correctifs (cf. section Documentation).

## Documentation

- Bulletin de sécurité Splunk SVD-2026-1014 du 27 octobre 2026 [https://advisory.splunk.com/advisories/SVD-2026-1014](https://advisory.splunk.com/advisories/SVD-2026-1014)
- Bulletin de sécurité Splunk SVD-2026-1015 du 28 octobre 2026 [https://advisory.splunk.com/advisories/SVD-2026-1015](https://advisory.splunk.com/advisories/SVD-2026-1015)
- Référence CVE CVE-2026-105482 [https://www.cve.org/CVERecord?id=CVE-2026-105482](https://www.cve.org/CVERecord?id=CVE-2026-105482)
- Référence CVE CVE-2026-105483 [https://www.cve.org/CVERecord?id=CVE-2026-105483](https://www.cve.org/CVERecord?id=CVE-2026-105483)
- Référence CVE CVE-2026-106069 [https://www.cve.org/CVERecord?id=CVE-2026-106069](https://www.cve.org/CVERecord?id=CVE-2026-106069)
- Référence CVE CVE-2026-111497 [https://www.cve.org/CVERecord?id=CVE-2026-111497](https://www.cve.org/CVERecord?id=CVE-2026-111497)
