# extract: served via trafilatura-direct
---
title: "Aveyron : les données de plus de 20 000 personnes exposées"
author: Seblatombe
url: https://frenchbreaches.com/alertes/aveyron-mtp0hyfwss6ietkec1q
hostname: frenchbreaches.com
description: Plus de 20 000 personnes sont concernées par une fuite de données en Aveyron. Des coordonnées personnelles et près de 1 500 documents sont revendiqués.
sitename: French Breaches
date: "2026-09-06"
categories: ['Secteur public']
---
## Fuite de données en Aveyron : plus de 20 000 personnes et près de 1 500 documents concernés

## Mise à jour à 01h45

**Selon nos informations, la fuite aurait été rendue possible par la compromission d’un compte client dépourvu de double authentification, combinée à une faille IDOR donnant accès à une base de données Odoo mal configurée. Aucune détection de l’activité malveillante n’aurait eu lieu à ce jour.**

**Une importante fuite de données touche OnRecrute.enAveyron.fr, la plateforme dédiée à l’emploi du Département de l’Aveyron. Le pirate ChimeraZ revendique les données de 20 316 personnes ainsi que près de 1 500 documents PDF, dont des CV contenant de nombreuses informations personnelles et professionnelles.**

Le service concerné, **OnRecrute.enAveyron.fr**, est un dispositif du Département de l’Aveyron animé par l’**Agence Départementale de l’Attractivité et du Tourisme (ADAT)**. La plateforme permet notamment de consulter des offres d’emploi, de candidater et de déposer un CV dans une CVthèque destinée aux employeurs.

Le **5 septembre 2026**, ChimeraZ publie sur un forum cybercriminel des données qu’il attribue à cette plateforme. L’ensemble revendiqué représente environ **465 Mo**, avec **23 381 enregistrements concernant 20 316 personnes**.

Les échantillons que nous avons analysés contiennent des données personnelles issues de profils et de candidatures, tandis que **1 499 documents PDF**, représentant environ 451 Mo, sont également annoncés.

## Quelles données personnelles sont exposées ?

Les échantillons analysés montrent la présence de plusieurs catégories de données permettant d’identifier directement les utilisateurs de la plateforme.

Parmi les informations observées figurent notamment :

- les **noms et prénoms** ;
- les **adresses e-mail** ;
- les **numéros de téléphone** ;
- les **codes postaux et communes** ;
- des identifiants internes ;
- différentes informations associées aux profils et candidatures.

La fuite est néanmoins particulièrement sensible en raison de la présence de documents associés aux utilisateurs, qui contiennent beaucoup plus d’informations qu’une simple base de coordonnées.

Pour des raisons de confidentialité, nous ne reproduisons aucune donnée personnelle issue des échantillons.

## Près de 1 500 documents PDF, dont des CV

Le pirate revendique également **1 499 documents PDF**, représentant environ **451 Mo**.

Un fichier intitulé **`1.5K_documents_avec_texte.json`** contient du texte extrait ou indexé à partir de ces documents. Les éléments que nous avons pu analyser montrent notamment la présence de **curriculum vitae**.

Ces CV peuvent contenir des informations personnelles et professionnelles particulièrement détaillées :

- coordonnées personnelles ;
- **date de naissance** ;
- diplômes et formations ;
- expériences professionnelles ;
- anciens employeurs ;
- périodes d’emploi ;
- qualifications et compétences ;
- permis de conduire ;
- informations relatives aux langues.

**parcours professionnel d’un candidat**, bien au-delà de son identité et de ses coordonnées.

## Des candidatures et profils professionnels concernés

Les données comprennent également des enregistrements liés à des **candidatures et profils professionnels**.

L’un des éléments analysés contient notamment l’identité d’un candidat, un intitulé de profil, des informations relatives aux formations et activités, des dates de création et de disponibilité ainsi qu’une référence vers une pièce jointe.

Cette structure est cohérente avec l’activité de **OnRecrute.enAveyron.fr**, qui permet aux candidats de déposer leur CV et de présenter leur profil aux employeurs.

Elle explique également la diversité des informations retrouvées dans la fuite : comptes utilisateurs, candidatures, profils professionnels et documents peuvent être associés à une même personne.

## Comment le piratage aurait-il eu lieu ?

**Selon nos informations, la compromission aurait débuté par l’accès à un compte client sans double authentification (MFA).**Une

**faille IDOR**aurait ensuite permis d’accéder à des ressources non autorisées, puis à une

**base de données Odoo mal configurée**depuis laquelle les données auraient été extraites.

**L’activité malveillante n’aurait, à ce jour, pas été détectée.**Ces éléments n’ont pas encore fait l’objet d’une confirmation officielle.

## Une faille IDOR au cœur de la compromission

L’exploitation présumée d’une faille IDOR est un élément important pour comprendre l’incident.

Contrairement à une vulnérabilité permettant nécessairement de prendre le contrôle complet d’un serveur, une IDOR exploite généralement une faiblesse dans la manière dont une application vérifie les autorisations d’un utilisateur.

Un compte parfaitement valide peut ainsi, dans certaines configurations vulnérables, demander l’accès à des ressources appartenant à d’autres utilisateurs ou à des objets auxquels il ne devrait pas avoir accès.

Dans ce cas précis, la compromission initiale d’un compte client aurait donc constitué **le point d’entrée**, tandis que le défaut de contrôle d’accès aurait permis d’aller plus loin dans le système.

La configuration de l’environnement Odoo aurait ensuite joué un rôle dans l’accès aux données.

## Le Département de l’Aveyron est-il directement concerné ?

La fuite concerne **OnRecrute.enAveyron.fr**, une plateforme emploi rattachée au Département de l’Aveyron et animée par l’Agence Départementale de l’Attractivité et du Tourisme.

Il convient toutefois de distinguer la compromission de ce service de celle de **l’ensemble du système d’information du Département**.

Les éléments dont nous disposons concernent la plateforme emploi et son environnement technique.

Ils ne permettent pas d’affirmer que d’autres services, applications ou infrastructures informatiques du Département de l’Aveyron ont également été compromis.

La portée de l’incident doit donc être limitée, à ce stade, au **service OnRecrute et aux systèmes concernés par cette fuite**.

## Pourquoi cette fuite est particulièrement sensible

La sensibilité de l’incident ne repose pas uniquement sur les **20 316 personnes** revendiquées.

Les informations contenues dans les CV et les candidatures offrent un niveau de détail important sur les personnes concernées.

Un acteur malveillant peut potentiellement disposer simultanément de l’identité d’un candidat, de ses coordonnées, de sa localisation et d’une partie de son parcours professionnel.

Les anciens employeurs, formations, qualifications ou compétences constituent également des informations qui peuvent rester valables pendant plusieurs années.

Cette combinaison facilite la création de scénarios de **phishing ciblé, d’usurpation d’identité et d’ingénierie sociale** particulièrement crédibles.

## Quels risques pour les personnes concernées ?

Les informations exposées pourraient notamment être utilisées pour construire de faux messages en lien avec une candidature ou une recherche d’emploi.

Un attaquant pourrait se faire passer pour :

- un **recruteur** ;
- un employeur ;
- le Département de l’Aveyron ;
- un organisme de formation ;
- un service lié à l’emploi ;
- ou un acteur local connu de la victime.

Les personnes potentiellement concernées doivent donc être particulièrement vigilantes face aux communications inattendues faisant référence à leur **CV, leur recherche d’emploi, leurs expériences professionnelles ou leurs candidatures**.

## Ce que l’on sait à ce stade

La publication attribuée à ChimeraZ revendique **23 381 enregistrements concernant 20 316 personnes**, pour un volume total d’environ **465 Mo**.

Les échantillons analysés contiennent des **noms, prénoms, adresses e-mail, numéros de téléphone, codes postaux, communes et informations liées à des profils ou candidatures**.

La fuite comprend également **1 499 documents PDF**, dont certains sont des CV contenant des informations personnelles et professionnelles détaillées.

**Selon nos informations, l’accès aurait été obtenu à partir d’un compte client sans MFA, avant l’exploitation d’une faille IDOR permettant d’atteindre une base Odoo mal configurée. L’activité malveillante n’aurait pas été détectée à ce jour.**

Ces informations permettent de mieux comprendre la méthodologie présumée utilisée lors de la compromission. Elles restent toutefois distinctes des éléments publiquement confirmés et devront être confrontées à d’éventuelles conclusions techniques ou communications officielles.

## Conclusion

**La fuite de données touchant OnRecrute.enAveyron.fr expose potentiellement les informations de plus de 20 000 personnes et près de 1 500 documents, dont des CV particulièrement détaillés.**

L’incident est d’autant plus sensible que les données ne se limitent pas à des coordonnées : des candidatures, formations, expériences professionnelles, qualifications et autres informations contenues dans les CV figurent également dans les éléments revendiqués.

Selon nos informations, la compromission aurait débuté par **un compte client dépourvu de MFA**, avant l’exploitation d’une **faille IDOR** donnant accès à une **base de données Odoo mal configurée**. L’activité malveillante n’aurait, à ce jour, fait l’objet d’aucune détection.

Cette chaîne de compromission devra encore être confirmée par une analyse technique ou une communication officielle.

En attendant, les personnes potentiellement concernées doivent être particulièrement attentives aux tentatives de **phishing et d’usurpation d’identité utilisant leur parcours professionnel ou leurs candidatures comme moyen de crédibilisation**.

**Ressources utiles :**

[Annuaire fuite de données](https://frenchbreaches.com/)|

[Que faire après une fuite de données](https://frenchbreaches.com/que-faire)|

[Blog fuite de données](https://frenchbreaches.com/blog/)

## Alertes liées

### Autres fuites du secteur public

[Voir toutes les alertes du secteur public](https://frenchbreaches.com/secteur/secteur-public)

Si cet article vous a plu, n’hésitez pas à nous suivre sur **X** pour plus de contenus exclusifs.
