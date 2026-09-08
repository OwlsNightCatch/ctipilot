# extract: served via trafilatura-direct
---
title: "Cyberattaque au ministère de la Transition écologique : des milliers de..."
author: Seblatombe
url: https://frenchbreaches.com/alertes/minist-re-de-la-transition-cologique-mtk4bzvizh7z1fmgm7
hostname: frenchbreaches.com
description: "Un pirate revendique deux bases liées au ministère de la Transition écologique : 8 166 utilisateurs et 14 656 enregistrements de contrôleurs."
sitename: French Breaches
date: "2026-09-02"
categories: ['Secteur public']
---
## Cyberattaque au ministère de la Transition écologique : les données de milliers d’utilisateurs et contrôleurs revendiquées

## Mise à jour à 20h40

Le ministère de la Transition écologique confirme avoir subi une « attaque informatique sophistiquée » la semaine dernière. Plusieurs sites sont indisponibles. L’ANSSI intervient et un signalement au parquet a été effectué.

Un cybercriminel revendique le piratage de systèmes liés au ministère de la Transition écologique et au domaine developpement-durable.gouv.fr. Deux ensembles de données auraient été récupérés, comprenant les informations de 8 166 utilisateurs ainsi que 14 656 enregistrements relatifs à des contrôleurs.

Dans une publication diffusée le **2 septembre 2026** sur un forum cybercriminel, un utilisateur sous le pseudonyme **« mondial »** affirme avoir extrait deux bases de données provenant de systèmes associés à **developpement-durable.gouv.fr**, domaine lié aux services du ministère de la Transition écologique.

Le pirate affirme que l’accès aurait notamment été rendu possible par une **mauvaise configuration d’API**. Il revendique également l’exploitation d’une vulnérabilité de type **IDOR** concernant **OISO (Outil Informatique de Surveillance des Organismes)**.

## Deux ensembles de données récupérés selon le pirate

La revendication fait apparaître deux ensembles distincts.

Le premier fichier, intitulé **controleurs.csv**, est annoncé comme contenant **14 656 enregistrements relatifs à des contrôleurs**.

Le second, **all_users.json**, contiendrait les informations de **8 166 utilisateurs**.

Des extraits des deux ensembles sont directement publiés sur le forum afin de montrer la nature des informations auxquelles le cybercriminel affirme avoir eu accès.

## 14 656 enregistrements relatifs à des contrôleurs

Le fichier **controleurs.csv** constitue l’un des éléments les plus importants de la fuite revendiquée.

Le pirate annonce précisément **14 656 enregistrements**.

L’échantillon visible dans sa publication contient de nombreux champs, parmi lesquels :

- un **identifiant** ;
- le **nom** ;
- le **prénom** ;
- la **date de naissance** ;
- un numéro d’agrément ;
- un numéro interne ;
- le métier ou la fonction ;
- différentes dates administratives ;
- l’**organisme de rattachement** ;
- des informations relatives à l’activité ;
- un **numéro de téléphone portable** .

**données personnelles nominatives**.

Le chiffre de 14 656 correspond toutefois à un nombre d’enregistrements et ne permet pas, à lui seul, d’affirmer que **14 656 personnes distinctes** sont concernées.

## Les informations de 8 166 utilisateurs également revendiquées

La seconde base, intitulée **all_users.json**, contiendrait les informations de **8 166 utilisateurs**.

L’analyse des données communiquées fait apparaître :

- **8 166 utilisateurs** ;
- **8 166 adresses e-mail uniques** ;
- **5 278 numéros de téléphone fixe** ;
- **3 642 numéros de téléphone mobile** ;
- **4 849 matricules** ;
- **942 unités ou directions différentes** .

## Noms, e-mails, téléphones, matricules et logins

Les exemples provenant de **all_users.json** contiennent de nombreux champs permettant d’identifier les utilisateurs et leur environnement professionnel.

Parmi les informations observées figurent notamment :

- le **nom** ;
- le **prénom** ;
- la civilité ;
- l’**adresse e-mail professionnelle** ;
- le numéro de téléphone fixe ;
- le numéro de téléphone mobile pour certains utilisateurs ;
- l’adresse professionnelle ;
- le code postal ;
- la ville ;
- le bureau ;
- l’**unité ou la direction de rattachement** ;
- le pays ;
- le **matricule professionnel** ;
- un identifiant utilisateur ;
- un **login de connexion** ;
- différentes informations provenant de l’annuaire LDAP.

**CGDD (Commissariat général au développement durable)**et localisés à

**La Défense**.

## 942 unités ou directions différentes apparaissent dans les données

La base revendiquée comprend des utilisateurs associés à **942 unités ou directions distinctes**.

Ce chiffre suggère un périmètre organisationnel particulièrement large et indique que les données ne semblent pas se limiter à quelques comptes appartenant à une seule unité.

Les échantillons observés montrent notamment des comptes associés au **CGDD**, une administration liée au ministère chargé de la Transition écologique.

L’identification précise des 942 unités serait toutefois nécessaire pour déterminer l’ensemble des services effectivement représentés dans les données.

## Près de 5 000 matricules professionnels

Parmi les **8 166 utilisateurs**, les données comprennent également **4 849 matricules**.

Ces informations sont accompagnées, selon les comptes, de différents identifiants techniques tels que :

- UID ;
- USERID ;
- login ;
- unité de rattachement ;
- informations LDAP.

## Des informations issues de l’annuaire LDAP

Plusieurs champs contenus dans les données semblent provenir d’un **annuaire LDAP**.

LDAP est notamment utilisé au sein des organisations pour centraliser les informations relatives aux utilisateurs, comptes et structures organisationnelles.

Les informations observées comprennent notamment :

- l’organisation LDAP ;
- l’unité organisationnelle ;
- le **Distinguished Name (DN)** ;
- le login ;
- l’identifiant utilisateur ;
- l’unité administrative de rattachement.

## Une mauvaise configuration d’API revendiquée

Le cybercriminel affirme que l’une des compromissions aurait été rendue possible par une **mauvaise configuration d’une API** associée à un service d’authentification.

Une API permet à différents services informatiques de communiquer et d’interroger automatiquement des données.

Une mauvaise configuration des contrôles d’accès peut, selon sa nature, permettre à un utilisateur de récupérer des informations auxquelles il ne devrait normalement pas avoir accès.

Le pirate ne fournit toutefois pas suffisamment de détails dans sa publication pour déterminer précisément la configuration concernée ou reproduire indépendamment son scénario.

## Une vulnérabilité IDOR sur OISO également revendiquée

La publication mentionne également une vulnérabilité **IDOR** concernant **OISO (Outil Informatique de Surveillance des Organismes)**.

Une vulnérabilité **IDOR (Insecure Direct Object Reference)** correspond à un défaut de contrôle des autorisations.

Elle peut permettre à un utilisateur d’accéder à une ressource qui ne lui est normalement pas destinée lorsque le serveur ne vérifie pas correctement les droits associés à l’identifiant demandé.

L’existence et l’étendue exacte de la vulnérabilité revendiquée restent cependant à confirmer indépendamment.

## Un risque de phishing particulièrement ciblé

La combinaison des données revendiquées pourrait faciliter des opérations de **phishing ciblé** contre les personnes concernées.

Selon les enregistrements, un attaquant pourrait disposer simultanément :

- de l’identité de la personne ;
- de son adresse e-mail professionnelle ;
- de ses numéros de téléphone ;
- de son matricule ;
- de son login ;
- de son unité ou de sa direction ;
- de son adresse et de son bureau professionnels ;
- de différentes informations relatives à son compte LDAP.

## Les données proposées au téléchargement

Dans sa publication, le cybercriminel indique mettre les données revendiquées à disposition des utilisateurs du forum.

Une section **« Download »** est visible, mais son contenu est masqué et nécessite une interaction avec la publication.

Le pirate affiche également une chaîne présentée comme une **« Session »**.

La seule capture ne permet toutefois pas de déterminer la nature exacte de cette chaîne, sa validité ou les éventuels privilèges auxquels elle pourrait donner accès.

## Ce qui apparaît dans la revendication

✅ Un cybercriminel **revendique une compromission de systèmes associés à developpement-durable.gouv.fr**.

✅ Les systèmes et données concernés sont liés à l’environnement du **ministère de la Transition écologique**.

✅ Deux ensembles de données sont revendiqués.

✅ **controleurs.csv** est annoncé avec **14 656 enregistrements relatifs à des contrôleurs**.

✅ Des **noms et prénoms** apparaissent dans les données concernant les contrôleurs.

✅ Des **dates de naissance** sont également visibles.

✅ Des numéros de téléphone et différentes informations administratives et professionnelles apparaissent dans cet ensemble.

✅ **all_users.json** contiendrait **8 166 utilisateurs**.

✅ La base comprend **8 166 adresses e-mail uniques**.

✅ **5 278 numéros de téléphone fixe** sont recensés.

✅ **3 642 numéros de téléphone mobile** apparaissent également.

✅ Les données comprennent **4 849 matricules**.

✅ **942 unités ou directions différentes** sont représentées.

✅ Des **logins et identifiants utilisateurs** apparaissent dans les données.

✅ Plusieurs informations provenant d’un **annuaire LDAP** sont présentes.

✅ Le pirate revendique une **mauvaise configuration d’API**.

✅ Une vulnérabilité **IDOR affectant OISO** est également revendiquée.

## Ce qui reste à confirmer

⚠️ L’authenticité et l’origine de l’intégralité des données doivent être confirmées indépendamment.

⚠️ Les **14 656 enregistrements de contrôleurs** ne correspondent pas nécessairement à 14 656 personnes distinctes.

⚠️ Il reste également à déterminer si les **8 166 utilisateurs** correspondent tous à des personnes distinctes et à des comptes actuellement actifs.

⚠️ L’étendue exacte des systèmes compromis n’est pas connue.

⚠️ Il n’est pas établi que l’intégralité de l’infrastructure du ministère ait été compromise.

⚠️ La nature précise de la **mauvaise configuration de l’API** n’est pas détaillée.

⚠️ L’étendue réelle de la vulnérabilité **IDOR** revendiquée sur OISO reste à déterminer.

⚠️ Aucun **mot de passe** n’apparaît dans les éléments présentés.

⚠️ La nature et la validité de la chaîne présentée comme une **session** ne sont pas établies.

⚠️ La date exacte de l’intrusion initiale n’est pas précisée.

⚠️ La durée pendant laquelle le cybercriminel aurait eu accès aux systèmes reste inconnue.

## Conclusion

**Un cybercriminel revendique une importante fuite de données provenant de systèmes liés au ministère de la Transition écologique et au domaine developpement-durable.gouv.fr.**

Deux ensembles sont concernés : un fichier comprenant **14 656 enregistrements relatifs à des contrôleurs** et une seconde base contenant les informations de **8 166 utilisateurs**.

Cette dernière comprendrait notamment **8 166 adresses e-mail uniques, 5 278 téléphones fixes, 3 642 mobiles, 4 849 matricules et des informations associées à 942 unités ou directions**.

Les données revendiquées comprennent également des **identités, coordonnées, logins, informations professionnelles et données issues d’un annuaire LDAP**.

Selon le pirate, l’extraction aurait notamment été rendue possible par une **mauvaise configuration d’API**, tandis qu’une vulnérabilité **IDOR affectant l’outil OISO** est également revendiquée.

L’étendue exacte de la compromission, le nombre définitif de personnes concernées et les circonstances techniques de l’intrusion restent à confirmer indépendamment.

**Ressources utiles :**

[Annuaire fuite de données](https://frenchbreaches.com/)|

[Que faire après une fuite de données](https://frenchbreaches.com/que-faire)|

[Blog fuite de données](https://frenchbreaches.com/blog/)

## Alertes liées

### Autres fuites du secteur public

[Voir toutes les alertes du secteur public](https://frenchbreaches.com/secteur/secteur-public)

Si cet article vous a plu, n’hésitez pas à nous suivre sur **X** pour plus de contenus exclusifs.
