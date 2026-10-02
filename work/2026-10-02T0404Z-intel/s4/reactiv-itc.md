---
title: "Faille Metabase : l'ANSSI et la DINUM victimes d'une fuite de données"
author: Florian BURNEL
url: https://www.it-connect.fr/anssi-dinum-fuite-donnees-metabase/
hostname: it-connect.fr
description: Une faille Metabase a permis de compromettre 118 comptes du laboratoire d'innovation de l'ANSSI et deux instances de la DINUM. Voici ce que l'on sait.
sitename: IT-Connect
date: "2026-10-01"
categories: ['Actu Cybersécurité']
tags: ['anssi,cybersécurité,actu cybersécurité']
---
# Faille Metabase : l’ANSSI et la DINUM victimes d’une fuite de données

**118 comptes compromis dans le laboratoire d'innovation de l'ANSSI, deux instances piratées à la DINUM : l'agence nationale de cybersécurité apparaît elle-même dans son propre bilan des fuites de données de l'État. En cause, une faille critique dans Metabase. Voici ce que l'on sait.**

Pour rappel, le Premier ministre a demandé le 1er septembre 2026 à l'ANSSI de lancer l'opération REACTIV, pour *"REponse & ACTion Interministérielle face aux Violations de données"*. J'avais d'ailleurs publié un article à propos de [ce dispositif qui permet à l'ANSSI d'imposer des mesures d'urgence aux ministères après les fuites de données](https://www.it-connect.fr/anssi-reactiv-violations-donnees-services-etat/). Le 30 septembre 2026, l'agence française a publié [le premier point de situation de l'opération REACTIV](https://www.cert.ssi.gouv.fr/cti/CERTFR-2026-CTI-006). On y apprend que 99 violations de données lui ont été signalées depuis le 1er août 2026, dont 67 sont confirmées.

Ce document arrive au lendemain du rapport d'incident de l'ANSSI à propos des cyberattaques qui ont ciblé la DGFiP (voir [mon article sur la cyberattaque de la DGFiP](https://www.it-connect.fr/rapport-anssi-cyberattaque-dgfip/)). Sauf que cette fois, l'ANSSI balaie aussi devant sa porte, en toute transparence. Son propre laboratoire d'innovation a été victime d'une fuite de données, et il y en a également une à déclarer du côté de la DINUM (direction interministérielle du numérique).

## ANSSI et DINUM : ce qui a été compromis

Le point commun entre ces deux incidents porte un nom : Metabase, une plateforme open source de visualisation de données utilisée pour construire des tableaux de bord. Un outil populaire que vous connaissez probablement. La lecture de ce rapport nous apprend ce qui suit :

- **Laboratoire d'innovation de l'ANSSI** : l'exploitation d'une vulnérabilité Metabase a entraîné la compromission de 118 comptes utilisateurs Metabase, dont une trentaine de comptes externes. Les données concernées sont des statistiques d'utilisation, des identifiants, des adresses e-mail et des hash de mots de passe. Suite à cette intrusion, l'ANSSI a mis à jour les instances vulnérables, renouvelé les mots de passe de tous les comptes et désactivé ceux inutilisés depuis plus de trois mois.
- **DINUM** : deux instances Metabase, associées à ProConnect et à Nuage-Public, ont été compromises. Les données exfiltrées portent sur des informations administratives d'organismes publics (SIREN, SIRET, budgets, effectifs), des métadonnées de contributions à des projets open source et des historiques de connexion anonymisés.

Côté DINUM, le rapport se veut rassurant sur la nature des informations dérobées : *"Ces données sont déjà publiques"*, peut-on lire. Effectivement, c'est bien de le préciser compte tenu de leur nature.

Il faut aussi remettre l'incident à sa juste place. Il s'agit des comptes d'une plateforme Metabase utilisée par le laboratoire d'innovation de l'ANSSI, et non du système d'information de l'agence dans son ensemble. Rien dans le document n'évoque une intrusion plus large.

## Metabase, la porte d'entrée qui revient en boucle

La vulnérabilité en question, associée à la référence CVE-2026-72898, est une injection SQL exploitable sans authentification. Elle permet d'accéder à la base de données de l'application Metabase et d'obtenir les droits administrateur de l'instance. Une faille de sécurité critique corrigée par Metabase via un correctif publié le 6 août 2026, et qui a d'ailleurs fait l'objet d'[une alerte par le CERT-FR le 10 septembre 2026](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-010/).

Quelque chose m'interpelle : la faille de sécurité a été corrigée le 6 août 2026. Le bulletin d'alerte du CERT-FR date du 10 septembre 2026, soit un mois plus tard. Et si ce bulletin d'alerte avait été publié suite à l'intrusion sur les instances de l'ANSSI et de la DINUM ? C'est une hypothèse, mais cela donnerait une piste quant au timing de cette intrusion. *"Le CERT-FR a connaissance de nombreuses compromissions de Metabase vulnérables."*, peut-on lire.

De son côté, l'ANSSI évoque dans son rapport avoir observé une exploitation massive de cette faille depuis début août 2026. Elle recense neuf instances compromises au sein des ministères, notamment :

- **France VAE** : le portail a été compromis via la vulnérabilité Metabase le 8 août 2026, soit 2 jours après la publication du patch. L'attaquant a obtenu un accès privilégié et exfiltré l'intégralité des données utilisateurs.
- **Qualicharge** : 102 000 sessions de recharge et une centaine de comptes techniques ont été exfiltrés depuis l'application de gestion des infrastructures de recharge pour véhicules électriques.
- **Zéro Logement Vacant** : le point d'entrée serait une instance Metabase, pour une violation qui concernerait 48 millions de propriétaires.

Si vous hébergez une instance Metabase et qu'elle n'a pas été mise à jour depuis un petit moment, il est temps de s'y coller. À défaut, Metabase conseille de bloquer l'accès public au chemin `/api/session/reset_password`.
