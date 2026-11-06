---
title: "Cyberattaque à l'INRAE : des bases de données et des accès sensibles..."
author: Seblatombe
url: https://frenchbreaches.com/alertes/cyberattaque-inrae-piratage-base-pcb-fuite-donnees-mw1bopq3536zduavp2g
hostname: frenchbreaches.com
description: Des hackers revendiquent le piratage d'un site de l'INRAE, avec 9 bases de données, des comptes utilisateurs et des fichiers internes potentiellement exposés.
sitename: French Breaches
date: "2026-11-04"
categories: ['Secteur public']
fingerprint: "6c24154955acd477"
---
## Cyberattaque : l'INRAE visé par un piratage, des données sensibles potentiellement volées

L'Institut national de recherche pour l'agriculture, l'alimentation et l'environnement (INRAE), l'un des principaux organismes publics de recherche français, serait victime d'une importante compromission informatique.

Selon les **informations exclusives de FrenchBreaches**, des pirates auraient accédé à un serveur lié à l'institut et récupéré des bases de données, des fichiers internes et des informations permettant potentiellement d'accéder à plusieurs services informatiques.

Le site **base-pcb.inrae.fr** est au cœur de cette affaire. Nos informations font également état d'une possible défiguration du site, une technique consistant à modifier une page internet sans autorisation.

FrenchBreaches a obtenu un inventaire détaillé des fichiers présentés comme dérobés, ainsi que plusieurs échantillons permettant d'examiner la nature des informations potentiellement compromises.

**Au total, les éléments recueillis font état de 9 bases de données, 781 tables, 7 archives serveur et près de 5 000 fichiers de code source.**

Les données revendiquées comprendraient notamment **des comptes de personnels et d'administrateurs, des adresses e-mail professionnelles, des mots de passe protégés par hachage, des identifiants de connexion et des fichiers techniques sensibles**.

L'authenticité de l'ensemble des fichiers et l'étendue exacte de la compromission restent toutefois à établir.

## Quelles données personnelles et sensibles auraient été exposées ?

C'est l'un des aspects les plus préoccupants de cette cyberattaque présumée.

Selon les informations exclusives obtenues par FrenchBreaches, les fichiers attribués à l'INRAE contiendraient plusieurs catégories de données concernant des personnels, des administrateurs et des utilisateurs de plateformes numériques.

Parmi les informations potentiellement compromises figureraient :

- **Des noms et identifiants de comptes utilisateurs**, permettant d'identifier des personnes inscrites sur certaines plateformes ;
- **Des adresses e-mail professionnelles**, notamment associées à des domaines institutionnels tels que `gouv.fr` et `irstea.fr` ;
- **Des comptes administrateurs**, disposant potentiellement de droits de gestion sur certaines applications ;
- **Des comptes de personnels et d'utilisateurs de plateformes de recherche**, notamment associés à l'environnement CESAB ;
- **Des comptes d'utilisateurs Moodle**, une plateforme de formation en ligne ;
- **Des mots de passe hachés**, protégés par différents mécanismes techniques, notamment MD5, Drupal et bcrypt selon les fichiers annoncés ;
- **Des identifiants de connexion à des bases de données**, susceptibles de permettre l'accès à certaines ressources informatiques ;
- **Une clé privée SSL**, un fichier particulièrement sensible utilisé pour sécuriser l'identité et les communications d'un serveur.

Ces informations proviendraient notamment de fichiers présentés sous les noms

`PII_admin_mdtb_users.txt`, `PII_irbasusers_CESAB.txt`, `PII_moodle_mdl_user.txt`, `mysql_user_table.txt` et `CREDENTIALS_ALL.txt`.
**FrenchBreaches a obtenu une archive d'échantillons contenant des fichiers correspondant à ces catégories**, sans que cela permette de confirmer l'intégralité des données revendiquées.

À ce stade, le nombre de comptes et de personnes distinctes potentiellement concernés n'a pas pu être établi.

## Des mots de passe et des accès informatiques : pourquoi est-ce préoccupant ?

La présence présumée de mots de passe et d'identifiants techniques représente un risque particulier.

Les mots de passe hachés ne sont pas nécessairement lisibles directement. Ils sont transformés par un procédé informatique destiné à empêcher leur récupération immédiate.

Cependant, certaines méthodes anciennes, comme **MD5**, peuvent être vulnérables à des tentatives de récupération, notamment lorsque les mots de passe sont faibles.

Les fichiers revendiqués feraient également apparaître des identifiants de connexion à des bases de données **MySQL et PostgreSQL**.

Contrairement à de simples informations de contact, ces identifiants pourraient, s'ils étaient toujours valides, faciliter des accès non autorisés à certains services.

Autre élément sensible : **une clé privée SSL attribuée à un ancien domaine lié à l'environnement informatique concerné** figurerait parmi les fichiers.

Une telle clé peut présenter un risque de sécurité selon son usage, son statut et les certificats auxquels elle est associée.

**Rien ne permet néanmoins d'affirmer que ces accès sont toujours actifs ou qu'ils ont été exploités après leur éventuelle extraction.**

## Neuf bases de données et des milliers de fichiers potentiellement compromis

Selon les informations exclusives obtenues par FrenchBreaches, les attaquants affirment avoir récupéré une sauvegarde regroupant **9 bases de données MySQL et 781 tables**.

L'archive représenterait **71,8 Mo compressés, soit environ 542 Mo une fois décompressée**.

Pour le grand public, une base de données peut être comparée à un ensemble de fichiers numériques organisés, permettant à un site internet ou à une application de stocker et de retrouver des informations.

Les éléments annoncés pourraient contenir des informations sur les utilisateurs, les applications et le fonctionnement de certains services.

Notre rédaction a également obtenu un inventaire faisant état de **7 archives provenant de serveurs**, représentant plus d'un gigaoctet de fichiers compressés.

Ces archives comprendraient notamment :

- **373 Mo de fichiers du site principal**, correspondant à l'application en fonctionnement ;
- **412 Mo d'archives d'un ancien site**, contenant potentiellement d'anciennes versions de fichiers ;
- **204 Mo d'archives techniques**, comprenant notamment des certificats, des dépôts de développement et des scripts ;
- **105 Mo de fichiers liés à Drupal et au CESAB**, dont des espaces de stockage privés et des jeux de données ;
- **48 Mo de fichiers Moodle**, associés à une plateforme de formation ;
- **1,7 Mo de fichiers de données Moodle**, potentiellement liés aux utilisateurs ;
- **5,85 Mo de fichiers associés à un outil d'accès à distance**, dont la présence et l'utilisation restent à expliquer.

Les pirates revendiquent par ailleurs

**4 956 fichiers de code source**, correspondant à des éléments utilisés pour développer et faire fonctionner certaines applications.

Ces informations ne permettent pas, à elles seules, d'affirmer que l'ensemble du réseau informatique de l'INRAE a été compromis.

## Des documents internes et des projets de recherche potentiellement concernés

Les informations recueillies ne se limiteraient pas aux données personnelles et aux comptes utilisateurs.

L'inventaire mentionne également des **fichiers de développement, des configurations informatiques, des scripts, des archives d'applications et des données associées à des environnements de recherche**.

Certains éléments seraient liés au **CESAB**, un environnement de recherche mentionné dans les archives, ainsi qu'à des plateformes utilisant Drupal.

D'autres concerneraient **Moodle**, un logiciel fréquemment utilisé pour proposer des formations en ligne.

Ces fichiers pourraient permettre de mieux comprendre le fonctionnement de certaines applications et, dans certains cas, faciliter la recherche de vulnérabilités informatiques.

Il reste toutefois impossible de déterminer précisément quels documents de recherche figureraient dans les archives revendiquées.

**Aucun élément disponible ne permet d'affirmer que l'ensemble des projets scientifiques ou des données confidentielles de l'INRAE ont été compromis.**

## Le site de l'INRAE aurait également été défiguré

Selon nos informations, les pirates auraient également procédé à une **défiguration du site base-pcb.inrae.fr**.

Cette pratique, appelée *defacement* dans le domaine de la cybersécurité, consiste à modifier sans autorisation l'apparence ou le contenu d'un site internet.

Les attaquants peuvent notamment remplacer une page par un message destiné à revendiquer leur intrusion.

Une telle modification peut témoigner d'un accès non autorisé à certains éléments du site, mais ne suffit pas à prouver que toutes les données annoncées ont effectivement été extraites.

Les circonstances techniques de cette possible intrusion restent inconnues.

## Quels risques pour les personnels et les utilisateurs ?

Si la fuite est confirmée, les conséquences pourraient dépasser la simple indisponibilité d'un site internet.

Les informations potentiellement compromises pourraient notamment être utilisées pour :

- **Des tentatives de phishing**, avec des e-mails frauduleux ciblant les personnels et utilisateurs ;
- **Des usurpations d'identité numérique**, à partir de comptes et d'adresses professionnelles ;
- **Des tentatives de récupération de mots de passe**, notamment lorsque des méthodes de hachage anciennes ont été utilisées ;
- **Des accès frauduleux à des applications**, si certains identifiants techniques sont toujours valides ;
- **De nouvelles cyberattaques**, facilitées par l'exposition de fichiers de configuration et de code source.

La divulgation de comptes professionnels pourrait également permettre à des cybercriminels de préparer des messages frauduleux particulièrement crédibles.

**À ce stade, le nombre de personnes potentiellement concernées reste inconnu.**

Il n'est pas non plus établi que des comptes aient été effectivement utilisés par les attaquants après l'extraction présumée des fichiers.

## FrenchBreaches a alerté l'INRAE

Compte tenu de la sensibilité des éléments recueillis, notamment la présence présumée d'identifiants techniques, de comptes administrateurs et d'une clé privée SSL, **FrenchBreaches a engagé une démarche de signalement auprès de l'INRAE**.

Notre rédaction cherche notamment à déterminer si l'organisme a connaissance de cette compromission, si des investigations sont en cours et si des mesures de sécurisation ont été prises.

L'INRAE n'a pas confirmé publiquement, dans les informations dont nous disposons, l'ampleur de la fuite revendiquée.

**FrenchBreaches poursuit ses vérifications afin de déterminer l'origine des fichiers, leur authenticité, le nombre de personnes potentiellement concernées et les conséquences éventuelles de cette cyberattaque présumée.**
