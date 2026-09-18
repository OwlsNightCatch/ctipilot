---
title: "Objet: Vulnérabilité dans les produits Check Point"
url: https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-1193/
hostname: gouv.fr
sitename: cert.ssi.gouv.fr
date: "2026-09-17"
---
## Risque

- Exécution de code arbitraire à distance

## Systèmes affectés

- Log Server versions antérieures à R81.20 take 28
- Log Server versions R82 antérieures à R82 take 28
- Log Server versions R82.10 antérieures à R82.10 take 28
- Log Server versions R82.20 antérieures à R82.20 take29
- Multi-Domain Log Server versions antérieures à R81.20 take 28
- Multi-Domain Log Server versions R82 antérieures à R82 take 28
- Multi-Domain Log Server versions R82.10 antérieures à R82.10 take 28
- Multi-Domain Log Server versions R82.20 antérieures à R82.20 take29
- Multi-Domain Security Management Server versions antérieures à R81.20 take 28
- Multi-Domain Security Management Server versions R82 antérieures à R82 take 28
- Multi-Domain Security Management Server versions R82.10 antérieures à R82.10 take 28
- Multi-Domain Security Management Server versions R82.20 antérieures à R82.20 take29
- Security Management Server versions antérieures à R81.20 take 28
- Security Management Server versions R82 antérieures à R82 take 28
- Security Management Server versions R82.10 antérieures à R82.10 take 28
- Security Management Server versions R82.20 antérieures à R82.20 take29

## Résumé

Une vulnérabilité a été découverte dans les produits Check Point. Elle permet à un attaquant de provoquer une exécution de code arbitraire à distance.

## Indicateurs de compromission

Checkpoint recommande de rechercher, via la *SmartConsole*, le motif **"Administrator failed to log in: Username too long"** dans les journaux *Audit* et *Admin login*.

## Solutions

Se référer au bulletin de sécurité de l'éditeur pour l'obtention des correctifs (cf. section Documentation).

## Documentation

- Bulletin de sécurité Check Point sk1000155 du 16 septembre 2026
- Référence CVE CVE-2026-91843

[https://support.checkpoint.com/results/sk/sk1000155](https://support.checkpoint.com/results/sk/sk1000155)

[https://www.cve.org/CVERecord?id=CVE-2026-91843](https://www.cve.org/CVERecord?id=CVE-2026-91843)
