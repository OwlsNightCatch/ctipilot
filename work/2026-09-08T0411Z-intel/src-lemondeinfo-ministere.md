# extract: served via trafilatura-direct
---
title: Le ministère de la Transition écologique ciblé par une cyberattaque - Le Monde Informatique
author: Louise Costa
url: https://www.lemondeinformatique.fr/actualites/lire-le-ministere-de-la-transition-ecologique-cible-par-une-cyberattaque-100771.html
hostname: lemondeinformatique.fr
description: Un cybercriminel revendique l'exfiltration de plus de 22 000 enregistrements, après avoir exploité, selon ses dires, une mauvaise configuration d'API...
sitename: LeMondeInformatique
date: "2026-09-07"
---
La série d’attaques visant les institutions publiques françaises se poursuit. Le ministère de la Transition écologique a confirmé avoir été la cible d’une attaque informatique sophistiquée. L’incident intervient alors qu’un cybercriminel revendique sur un forum spécialisé l’exfiltration de données provenant de systèmes associés au domaine developpement-durable.gouv.fr.

Selon les informations publiées [par French Breaches,](https://frenchbreaches.com/alertes/minist-re-de-la-transition-cologique-mtk4bzvizh7z1fmgm7) le premier fichier, nommé controleurs.csv, contiendrait 14 656 enregistrements relatifs à des contrôleurs agréés. Les extraits présentés font apparaître des données telles que des noms, prénoms, dates de naissance, numéros d’agrément, informations administratives et coordonnées téléphoniques. Certains enregistrements seraient notamment associés à des organismes de contrôle comme APAVE Exploitation France. Le second fichier, all_users.json, regrouperait les informations de 8 166 utilisateurs. D’après l’analyse réalisée par French Breaches, cette base comprendrait 8 166 adresses électroniques uniques, 5 278 numéros de téléphone fixe, 3 642 numéros de téléphone mobile, 4 849 matricules professionnels ainsi que des utilisateurs rattachés à 942 unités ou directions différentes. Les échantillons publiés montrent la présence d’informations d’identité, de coordonnées professionnelles, de logins et de données issues d’un annuaire LDAP. Toutefois, le nombre d’enregistrements revendiqué ne correspond pas nécessairement au nombre de personnes effectivement concernées. L’authenticité et l’exhaustivité des données présentées n’ont pas été confirmées indépendamment.

## Une mauvaise configuration d’API et une faille IDOR évoquées

Sur le plan technique, l’attaquant affirme que l’accès initial aurait été obtenu via un service d’authentification mal configuré. Il revendique ensuite l’exploitation d’une vulnérabilité de type IDOR (Insecure Direct Object Reference)affectant l’OISO, l’Outil Informatique de Surveillance des Organismes. Une vulnérabilité IDOR permet généralement à un utilisateur authentifié d’accéder à des ressources auxquelles il ne devrait normalement pas avoir accès en manipulant simplement des identifiants ou des références dans les requêtes adressées à l’application.

À ce stade, aucun élément technique indépendant ne permet toutefois de confirmer le scénario décrit par le cybercriminel. French Breaches souligne d’ailleurs que la nature exacte de la mauvaise configuration invoquée, l’étendue réelle de la vulnérabilité et le périmètre des systèmes compromis restent à déterminer.

## **Des perturbations visibles sur plusieurs services**

L’incident ne s’est pas limité à une simple revendication de fuite de données. Plusieurs sites rattachés au ministère ont été temporairement rendus indisponibles pendant les opérations de sécurisation. Des messages de maintenance ont notamment été affichés sur la plateforme des consultations publiques environnementales ainsi que sur plusieurs sites d’administrations régionales. Selon les informations communiquées à l’AFP, l’attaque aurait ciblé des outils de messagerie du pôle ministériel. Le ministère a indiqué avoir mis en œuvre des mesures de protection renforcées et confirmé avoir effectué un signalement au parquet. De son côté, l’Anssi a précisé intervenir auprès des administrations concernées dans le cadre d’investigations liées à de possibles compromissions de comptes utilisateurs.

Cette attaque intervient dans un contexte de forte pression sur les systèmes d’information de l’administration française. Depuis plusieurs mois, plusieurs organismes publics ont fait l’objet de revendications ou de compromissions présumées, notamment la Direction générale des finances publiques et [l’Éducation nationale](https://www.lemondeinformatique.fr/actualites/lire-le-ministere-de-l-education-nationale-cible-par-une-attaque-100733.html) en juillet dernier. À ce stade, l’étendue exacte de la compromission du ministère de la Transition écologique reste à déterminer. Les investigations techniques doivent notamment permettre de confirmer la nature des données effectivement exfiltrées, le périmètre des systèmes compromis et le nombre réel de personnes potentiellement concernées.

## Commentaire
