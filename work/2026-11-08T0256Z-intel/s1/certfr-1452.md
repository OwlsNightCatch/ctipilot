---
title: Avis du CERT-FR
url: https://www.cert.cyber.gouv.fr/avis/CERTFR-2026-AVI-1452/
hostname: gouv.fr
sitename: cert.cyber.gouv.fr
date: "2024-04-08"
fingerprint: "3dc7a93fb7cc8337"
---
# Avis du CERT-FR

Objet : Multiples vulnérabilités dans Ruby on Rails

## Gestion du document

Une gestion de version détaillée se trouve à la fin de ce document.

## Risques

- Atteinte à l'intégrité des données
- Atteinte à la confidentialité des données
- Contournement de la politique de sécurité
- Déni de service à distance
- Exécution de code arbitraire à distance
- Injection de code indirecte à distance (XSS)

## Systèmes affectés

- Ruby on Rails versions 8.x antérieures à 8.1.4.1
- Ruby on Rails versions antérieures à 8.0.5.2

## Résumé

De multiples vulnérabilités ont été découvertes dans Ruby on Rails. Certaines d'entre elles permettent à un attaquant de provoquer une exécution de code arbitraire à distance, un déni de service à distance et une atteinte à la confidentialité des données.

## Solutions

Se référer au bulletin de sécurité de l'éditeur pour l'obtention des correctifs (cf. section Documentation).

## Documentation

- Bulletin de sécurité Ruby on Rails 91802 du 04 novembre 2026 [https://discuss.rubyonrails.org/t/rails-security-releases-8-0-5-2-and-8-1-4-1/91802](https://discuss.rubyonrails.org/t/rails-security-releases-8-0-5-2-and-8-1-4-1/91802)
