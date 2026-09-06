# extract: served via trafilatura-direct
---
title: "Fuite de données : l’Association des maires de France touchée, 114 000..."
author: Seblatombe
url: https://frenchbreaches.com/alertes/association-des-maires-de-france-mtmsxq04rjndct88z4p
hostname: frenchbreaches.com
description: Une fuite de données visant l’Association des maires de France expose plus de 100 000 entrées liées aux élus et collectivités.
sitename: French Breaches
date: "2026-09-04"
categories: ['Secteur public']
---
## Fuite de données de l’Association des maires de France : plus de 100 000 entrées liées aux élus et collectivités exposées

## Mise à jour le 4/09 à 15h45

L’Association des maires de France (AMF) a confirmé avoir été victime de cette fuite de données. Plus de 100 000 entrées ont été dérobées, comprenant notamment des noms, prénoms, adresses e-mail, fonctions, identifiants internes et données liées aux élus et collectivités, ainsi que des mots de passe en clair. L’AMF indique être en train de délimiter l’étendue de la fuite et avoir saisi la CNIL. Les personnes potentiellement concernées seront contactées après la réalisation de l’audit.

Une importante

**fuite de données visant l’Association des maires de France et des présidents d’intercommunalité (AMF)**a été revendiquée le

**4 septembre 2026**sur un forum cybercriminel.

Un utilisateur utilisant le pseudonyme **Alduin** affirme avoir exploité une **injection SQL de type UNION** sur le site **amf.asso.fr** afin d’accéder à plusieurs tables de sa base de données.

La publication est présentée sous le chiffre de **114 000 entrées** et concerne notamment des données liées à des **maires, élus, agents territoriaux, collectivités et autres acteurs de l’administration publique française**.

L’analyse des éléments diffusés montre également la présence de données d’authentification dans certaines tables, dont des **hachages de mots de passe** et, dans un autre ensemble, des **mots de passe enregistrés en clair**.

## Plus de 100 000 entrées attribuées à l’AMF

La publication diffusée par Alduin est intitulée **« [FR] amf.asso.fr - 114K »**.

Le chiffre de 114 000 doit cependant être interprété avec prudence.

Plusieurs tables différentes auraient été extraites et une même personne peut apparaître dans plusieurs fichiers ou disposer de plusieurs enregistrements.

Il est donc plus précis de parler de **plus de 100 000 entrées ou profils exposés** plutôt que de 114 000 victimes uniques.

Parmi les fichiers présentés figure notamment une base consacrée aux abonnés de l’AMF.

La capture publiée indique pour l’un de ces fichiers :

- un format **JSONL** ;
- une taille d’environ **35 841 Ko** ;
- des informations relatives aux abonnés et organisations ;
- des fonctions professionnelles ;
- des adresses e-mail ;
- différentes informations liées aux abonnements.

## Quelles données apparaissent dans la fuite de l’Association des maires de France ?

Les données observées permettent d’associer des personnes à leur **fonction professionnelle et à leur organisation de rattachement**.

Parmi les champs présents figurent notamment :

- **noms et prénoms** ;
- **adresses e-mail** professionnelles ou personnelles ;
- **fonction occupée** ;
- commune, intercommunalité ou organisation ;
- identifiants internes ;
- type d’abonné ;
- dates de début et de fin d’abonnement ;
- informations de suivi associées au profil.

## Des maires, DGS, RH et agents territoriaux concernés

Cette **fuite de données de l’AMF** est particulièrement sensible en raison des fonctions des personnes présentes dans les fichiers.

Les données analysées font apparaître différents profils liés aux collectivités françaises, notamment des :

- **maires** ;
- adjoints et conseillers municipaux ;
- **directeurs généraux des services (DGS)** ;
- responsables des ressources humaines ;
- gestionnaires de paie ;
- juristes ;
- responsables administratifs ;
- responsables comptables ;
- chargés de mission ;
- agents territoriaux.

Cela ne signifie pas que les systèmes informatiques de ces administrations ont eux-mêmes été compromis. Leurs informations peuvent simplement être présentes parce qu’elles étaient enregistrées dans les bases utilisées par l’AMF.

## Une cartographie des collectivités et administrations locales

La fuite ne contient pas uniquement une liste d’adresses e-mail.

L’association entre **identité, fonction et collectivité** permet potentiellement de reconstituer une partie de l’organisation interne de certaines communes et intercommunalités.

Un acteur malveillant pourrait ainsi identifier plus facilement le maire d’une commune, son DGS, un responsable RH, un responsable financier ou différents agents administratifs.

Ces informations augmentent notamment les risques d’**ingénierie sociale et de phishing ciblé**.

## Une injection SQL revendiquée contre amf.asso.fr

Alduin affirme avoir identifié une **injection SQL de type UNION** sur le site de l’Association des maires de France.

Une telle vulnérabilité peut, selon sa configuration et les permissions accordées à l’application, permettre de manipuler une requête SQL afin d’accéder à des informations provenant d’autres tables de la base de données.

L’auteur affirme avoir utilisé cette faiblesse pour sélectionner puis extraire plusieurs tables qu’il considérait comme intéressantes.

À ce stade, **l’existence exacte de cette vulnérabilité et les circonstances techniques de son exploitation n’ont pas été confirmées publiquement par l’AMF**.

Il convient donc de présenter l’injection SQL comme une **méthode revendiquée par l’auteur de la fuite** et non comme une conclusion technique définitivement établie.

## Des hachages de mots de passe dans une autre table

Parmi les fichiers analysés figure également une table contenant des comptes utilisateurs avec leurs identifiants et un champ consacré au mot de passe.

Dans cet ensemble, les valeurs observées correspondent à des **hachages bcrypt**.

Il ne s’agit donc pas de mots de passe directement lisibles.

Bcrypt est une fonction de hachage conçue pour rendre plus coûteuses les tentatives visant à retrouver un mot de passe à partir de son empreinte.

La présence de ces hachages reste néanmoins sensible, particulièrement lorsque les utilisateurs ont choisi des mots de passe faibles ou réutilisés sur plusieurs services.

## Une table contiendrait également des mots de passe en clair

Plus préoccupant, une autre table analysée contient des **identifiants ou adresses e-mail associés à des mots de passe directement lisibles**.

Ces informations ne sont volontairement pas reproduites.

Les comptes concernés semblent notamment être associés à des **mairies, collectivités, associations et autres organisations**.

La présence de ces données dans la fuite ne permet toutefois pas d’affirmer que tous les identifiants sont encore actifs ou que les mots de passe sont toujours valides en septembre 2026.

Ils doivent néanmoins être considérés comme potentiellement compromis.

## Quels risques pour les maires et collectivités ?

Cette fuite de données pourrait être particulièrement intéressante pour des cybercriminels souhaitant cibler les collectivités territoriales.

Les informations exposées peuvent notamment faciliter :

- le **phishing ciblé** ;
- l’usurpation d’identité d’un maire ou d'un élu ;
- la **fraude au président** ;
- les faux ordres de virement ;
- l’usurpation d’un DGS ou d’un responsable administratif ;
- le ciblage des services RH et financiers ;
- les tentatives de compromission de messageries professionnelles ;
- l’exploitation de mots de passe réutilisés sur d’autres services.

## Un risque de réutilisation des mots de passe

La présence de données d’authentification représente également un risque dépassant potentiellement le seul environnement de l’AMF.

Lorsqu’un utilisateur réutilise le même mot de passe sur plusieurs services, l’exposition d’un ancien identifiant peut faciliter des tentatives d’accès à une **messagerie professionnelle, un extranet ou un autre service utilisé par une collectivité**.

Cela ne signifie toutefois pas que ces services ont été compromis.

Il s’agit d’un risque potentiel lié à la **réutilisation des identifiants et mots de passe**.

## 114 000 lignes ne signifient pas 114 000 maires touchés

Le titre de la publication peut facilement prêter à confusion.

Il ne faut pas interpréter les **114 000 entrées revendiquées** comme 114 000 maires victimes.

La France compte évidemment beaucoup moins de maires et les fichiers semblent réunir différentes catégories de personnes et d’organisations.

Une même personne peut également apparaître plusieurs fois dans les différentes tables.

Le chiffre correspond donc davantage au **volume global d’enregistrements revendiqués** qu'au nombre confirmé de personnes uniques concernées.

## L’AMF n’a pas encore confirmé publiquement l’incident

Au moment de la publication de ces informations, aucune confirmation publique de l’Association des maires de France concernant cette revendication n’a été identifiée.

Plusieurs éléments restent donc à déterminer :

- la date exacte de l’éventuelle intrusion ;
- la date d’extraction des bases ;
- le périmètre complet des données concernées ;
- le nombre de personnes uniques présentes ;
- la validité actuelle des comptes exposés ;
- la confirmation technique de l’injection SQL revendiquée.

## Conclusion

Une importante **fuite de données attribuée à l’Association des maires de France (AMF)** a été publiée le 4 septembre 2026 par un acteur utilisant le pseudonyme Alduin.

La publication est annoncée sous le chiffre de **114 000 entrées** et contient des informations associées à des **maires, élus, DGS, responsables RH, agents territoriaux, collectivités et autres organisations publiques**.

Les fichiers analysés comprennent notamment des **noms, adresses e-mail, fonctions professionnelles, organisations et informations d’abonnement**.

Certaines tables contiennent également des données d’authentification : des **hachages bcrypt** dans un fichier et des **mots de passe lisibles en clair** dans un autre.

L’auteur affirme avoir obtenu ces données grâce à une **injection SQL UNION visant amf.asso.fr**.

**Cette méthode d’intrusion reste cependant une revendication de l’auteur et n’a pas encore été confirmée publiquement par l’Association des maires de France.**

**Ressources utiles :**

[Annuaire fuite de données](https://frenchbreaches.com/)|

[Que faire après une fuite de données](https://frenchbreaches.com/que-faire)|

[Blog fuite de données](https://frenchbreaches.com/blog/)

## Alertes liées

### Autres fuites du secteur public

[Voir toutes les alertes du secteur public](https://frenchbreaches.com/secteur/secteur-public)

Si cet article vous a plu, n’hésitez pas à nous suivre sur **X** pour plus de contenus exclusifs.
