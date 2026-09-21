# extract: served via trafilatura-direct
---
title: "AFPA : près de 2 millions de dossiers revendiqués après 2 cyberattaques"
author: Thomas Lazzaroni
url: https://www.cyberattaque.org/afpa-pres-dun-million-de-dossiers-revendiques-apres-une-cyberattaque/
hostname: cyberattaque.org
description: L’AFPA, l’Agence nationale pour la formation professionnelle des adultes, a confirmé avoir identifié une potentielle extraction de données après deux
sitename: Cyberattaque.org
date: "2026-09-15"
categories: ['Attaque']
---
L’**AFPA**, l’Agence nationale pour la formation professionnelle des adultes, a confirmé avoir identifié une **potentielle extraction de données** après deux revendications publiées à quelques heures d’intervalle. L’organisme évoque désormais **jusqu’à 1,7 million de personnes potentiellement concernées**.

La seconde revendication avait été publiée par un hacker utilisant le pseudonyme **Cybernox**, qui affirme disposer de **1 732 811 lignes** liées à l’organisme. Elle intervenait 24 heures après la mise en vente de 971 420 enregistrements par un autre acteur, xMetah.

Cybernox n’est pas inconnu dans ce dossier. Il s’agit du **même hacker qui avait déjà révélé, un mois plus tôt, la compromission de comptes liés à l’AFPA**, avec notamment [101 comptes exposés et la publication d’un accès administrateur](https://www.cyberattaque.org/afpa-pirate-101-comptes-exposes-et-un-acces-administrateur-publie/).

Dans sa nouvelle annonce publiée le 16 septembre 2026, Cybernox affirme que les données auraient été obtenues en exploitant une **vulnérabilité de type IDOR**. L’AFPA ne confirme pas précisément ce scénario technique, mais indique avoir identifié lors de ses premières investigations une **potentielle extraction liée à une faille sur un outil utilisé pour gérer les hébergements**.

## L’AFPA au cœur de la formation professionnelle en France

L’**AFPA** est l’un des principaux acteurs français de la formation professionnelle des adultes. Elle accompagne notamment des demandeurs d’emploi, salariés et personnes en reconversion dans l’acquisition de nouvelles compétences et l’accès à l’emploi.

Son activité implique le traitement d’un volume important d’informations sur les personnes accompagnées, leurs parcours, leurs inscriptions et les organismes partenaires.

## Jusqu’à 1,7 million de personnes potentiellement concernées

Le 16 septembre, Cybernox a publié une nouvelle annonce dans laquelle il affirme vendre des données concernant l’AFPA. Le hacker avance précisément le chiffre de **1 732 811 lignes**.

Dans son message, il présente ce volume comme correspondant à des utilisateurs de l’AFPA et indique que l’accès aurait été obtenu grâce à une **faille IDOR**.

Une vulnérabilité IDOR, pour **Insecure Direct Object Reference**, peut permettre à un utilisateur d’accéder à des ressources ou à des dossiers qui ne devraient normalement pas lui être accessibles en modifiant un identifiant transmis à une application, lorsque les contrôles d’autorisation sont insuffisants.

L’AFPA confirme désormais qu’une extraction de données a potentiellement eu lieu et indique que l’incident pourrait concerner **jusqu’à 1,7 million de personnes**. L’organisme poursuit toutefois ses investigations afin de déterminer précisément l’étendue des données et le nombre de personnes concernées.

Le chiffre exact de **1 732 811 lignes avancé par Cybernox** et la méthode IDOR revendiquée par le hacker n’ont, eux, pas été confirmés précisément par l’AFPA.

## Une faille sur un outil de gestion des hébergements

L’AFPA apporte surtout un élément nouveau sur l’origine possible de la fuite. Selon les premières investigations menées par l’organisme, l’extraction serait liée à une **faille affectant l’outil utilisé pour gérer les hébergements**.

Cet outil est **hébergé chez un éditeur tiers et externe au système d’information de l’AFPA**. L’organisme indique ainsi qu’il n’y aurait, à ce stade, pas eu d’impact sur ses services ni sur son système d’information interne.

Cette précision permet de mieux circonscrire l’incident sans toutefois établir à ce stade si les deux bases revendiquées par Cybernox et xMetah proviennent exactement du même environnement.

## Le même hacker avait déjà publié un accès administrateur

Cette nouvelle revendication intervient environ un mois après une première alerte impliquant directement Cybernox. Le hacker avait alors revendiqué l’accès à plusieurs comptes liés à l’AFPA.

Cyberattaque.org avait révélé que 101 comptes étaient exposés et qu’un accès administrateur avait notamment été publié.

La nouvelle annonce du 16 septembre donne donc une dimension particulière à cette précédente compromission. Rien ne permet cependant d’établir que les données aujourd’hui revendiquées ont été obtenues depuis ces comptes ou depuis l’accès administrateur précédemment diffusé, l’AFPA orientant actuellement ses investigations vers un outil externe dédié aux hébergements.

## Une première base de 971 420 lignes revendiquée 24 heures plus tôt

Cette nouvelle publication intervient seulement **24 heures après une première revendication**. Un autre acteur utilisant le pseudonyme **xMetah** avait affirmé disposer d’un fichier contenant précisément **971 420 enregistrements** associés à l’AFPA.

Contrairement à certaines fuites directement rendues publiques, cette première base était **proposée à la vente**.

xMetah ne précisait ni la date de l’extraction, ni la méthode utilisée pour obtenir les informations, ni le système depuis lequel elles auraient été récupérées.

Les déclarations de l’AFPA permettent désormais d’établir qu’une extraction potentielle a bien été repérée sur un outil externe. Il reste cependant impossible de déterminer si les **971 420 lignes revendiquées par xMetah** correspondent intégralement à cette extraction ou si elles n’en constituent qu’une partie.

## Noms dates de naissance adresses et téléphones dans les premiers échantillons

**Cyberattaque.org s’est procuré les échantillons diffusés avec la première annonce de xMetah.** Les enregistrements observés contiennent plusieurs catégories de données permettant d’identifier directement les personnes :

- **civilité, nom et prénom** ;
- **date de naissance** ;
- adresse postale complète ;
- **code postal et ville** ;
- pays ;
- **numéro de téléphone** ;
- identifiant interne ;
- informations relatives à un partenaire associé au dossier.

La structure comporte également des champs prévus pour des adresses e-mail, des seconds numéros de téléphone ou d’autres coordonnées. Dans les échantillons observés, plusieurs de ces champs sont cependant vides.

De son côté, l’AFPA indique que les données présentes dans l’application concernée seraient principalement des **noms, des adresses et éventuellement des numéros de téléphone**. À ce stade, l’organisme n’a pas identifié de données bancaires ou de numéros de Sécurité sociale dans l’outil touché.

## Des données provenant de toute la France

Les exemples diffusés avec la première revendication montrent des personnes domiciliées dans de nombreuses régions françaises, y compris en **Guadeloupe, Martinique, La Réunion, Hauts-de-France, Nouvelle-Aquitaine et Pays de la Loire**.

Cette dispersion géographique est cohérente avec la dimension nationale de l’AFPA et avec le nombre potentiellement très important de personnes désormais évoqué par l’organisme.

## La mention d’un partenaire apparaît dans les premiers exemples

Un élément mérite une attention particulière dans les données revendiquées par xMetah : les échantillons communiqués comportent un champ **« partenaire »**. Dans les lignes observées, celui-ci contient notamment la valeur **LHEA**.

Cette structure pouvait déjà laisser penser que les données provenaient d’un **flux partenaire, d’une application intermédiaire ou d’un environnement connecté à l’AFPA**. La confirmation par l’organisme de l’implication probable d’un outil externe hébergé chez un éditeur tiers renforce la nécessité de distinguer cette fuite d’une compromission directe du système d’information principal de l’AFPA.

Il n’est toutefois pas possible d’établir, à partir des seuls échantillons, le rôle exact du partenaire mentionné dans les données ni son éventuel lien avec l’application aujourd’hui identifiée par l’AFPA.

## Des identifiants internes permettent de relier les dossiers

Les premiers fichiers contiennent également plusieurs champs techniques, dont un **contextId** et un **identifiantAB**. Ces valeurs semblent servir à relier chaque personne à un dossier ou à un contexte applicatif spécifique.

Pris isolément, ces identifiants n’ont pas nécessairement de valeur pour un fraudeur. Mais associés à une identité complète, une adresse et une date de naissance, ils peuvent aider à construire un profil beaucoup plus précis de la personne concernée.

## Les deux revendications concernent-elles les mêmes données ?

La proximité entre les deux annonces pose toujours une question importante : les **971 420 lignes revendiquées par xMetah** et les **1 732 811 lignes annoncées par Cybernox** proviennent-elles du même environnement ou correspondent-elles à deux extractions différentes ?

L’AFPA reconnaît avoir été confrontée aux revendications des deux hackers et avoir identifié dans le même temps une potentielle extraction de données. L’organisme n’a toutefois pas établi publiquement si les deux jeux de données correspondent à une seule et même extraction.

Les volumes sont différents et les deux hackers ne décrivent pas leur accès de la même manière. Les deux ensembles pourraient être distincts, partiellement se chevaucher ou correspondre à différentes extractions issues du même environnement. Une comparaison des bases complètes serait nécessaire pour mesurer précisément leur éventuel recoupement.

## Le nombre exact de victimes reste à déterminer

Le chiffre précis de **1 732 811 lignes** revendiqué par Cybernox ne signifie pas automatiquement qu’autant de personnes distinctes figurent dans la base. Une même personne peut apparaître plusieurs fois, disposer de différents dossiers ou être enregistrée dans plusieurs contextes.

L’AFPA estime néanmoins que l’incident pourrait potentiellement concerner **jusqu’à 1,7 million de personnes**. L’organisme poursuit actuellement ses investigations pour déterminer l’étendue réelle de l’extraction et identifier les personnes devant être informées.

## Un risque important d’usurpation et de phishing ciblé

Les informations visibles dans les premiers échantillons peuvent présenter un intérêt important pour des cybercriminels. Un **nom complet associé à une date de naissance, une adresse et un numéro de téléphone** fournit déjà de nombreux éléments permettant de préparer des tentatives d’usurpation ou de phishing particulièrement crédibles.

Les personnes concernées pourraient notamment recevoir de faux appels ou messages prétendant provenir de l’AFPA, d’un organisme de formation, de France Travail ou d’un autre acteur lié à leur parcours professionnel.

Un attaquant peut également exploiter ces informations pour tenter d’obtenir des données supplémentaires sous prétexte de **mettre à jour un dossier, confirmer une inscription ou compléter une démarche administrative**.

## Les dates de naissance augmentent la sensibilité des données

La présence des **dates de naissance complètes** dans les premiers échantillons constitue l’un des principaux points sensibles. Cette information est encore régulièrement utilisée pour vérifier l’identité d’une personne lors d’un échange avec un service client ou une administration.

Associée au téléphone et à l’adresse postale, elle peut faciliter certaines attaques d’**ingénierie sociale et d’usurpation d’identité**.

## Trois alertes autour de l’AFPA en un mois

En l’espace d’environ un mois, l’AFPA s’est ainsi retrouvée associée à **trois alertes successives** : la publication de comptes et d’un accès administrateur par Cybernox, une base de 971 420 lignes revendiquée par xMetah, puis une seconde annonce de Cybernox portant sur 1 732 811 lignes.

La confirmation apportée par l’AFPA permet désormais d’établir qu’une **potentielle extraction de données a effectivement été détectée** dans le contexte des deux dernières revendications. En revanche, aucun élément ne permet encore de relier cette extraction à la compromission des comptes révélée un mois auparavant.

## L’AFPA confirme une extraction potentielle sur un outil tiers

L’incident ne repose donc plus uniquement sur les déclarations des hackers. Après de premières investigations, l’AFPA confirme avoir identifié une **potentielle extraction de données liée à une faille affectant son outil de gestion des hébergements**.

L’application concernée est hébergée chez un **éditeur tiers et reste extérieure au système d’information de l’AFPA**. L’organisme indique qu’il n’y aurait ainsi, à ce stade, pas eu d’impact sur ses services ou son infrastructure informatique interne.

L’AFPA poursuit désormais ses investigations pour déterminer précisément les données et les personnes concernées avant de procéder à leur information. L’organisme estime que **jusqu’à 1,7 million de personnes** pourraient potentiellement être concernées.

Restent désormais à établir le nombre exact de personnes touchées, le degré de recoupement entre les données revendiquées par xMetah et Cybernox ainsi que le scénario technique précis ayant permis leur extraction.
