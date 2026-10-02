---
title: "Sécurité : le premier point de situation REACTIV de l’ANSSI illustre l’ampleur du problème"
author: Vincent Hermann
url: https://next.ink/259353/securite-le-premier-point-de-situation-reactiv-de-lanssi-illustre-lampleur-du-probleme/
hostname: next.ink
description: L’ANSSI a publié le premier point de situation de son dispositif REACTIV. Le rapport est sobre et direct, alignant les causes des différents incidents…
sitename: Next
date: "2026-10-01"
categories: ['Sécurité']
---
# Sécurité : le premier point de situation REACTIV de l’ANSSI illustre l’ampleur du problème

Il y a du travail

Le 01 octobre à 15h55

**L’ANSSI a publié le premier point de situation de son dispositif REACTIV. Le rapport est sobre et direct, alignant les causes des différents incidents cyber des deux derniers mois contre les ministères, avec des chiffres éloquents.**

# Sécurité : le premier point de situation REACTIV de l’ANSSI illustre l’ampleur du problème

## Il y a du travail

**L’ANSSI a publié le premier point de situation de son dispositif REACTIV. Le rapport est sobre et direct, alignant les causes des différents incidents cyber des deux derniers mois contre les ministères, avec des chiffres éloquents.**

Sécurité

Sécurité

6 min

Le dispositif REACTIV (pour REponse & ACTion Interministérielle face aux Violations de données) a été créé par l’ANSSI (Agence nationale de la sécurité des systèmes d’information) à la demande du Premier ministre Sébastien Lecornu. Annoncée publiquement le 7 septembre, elle constitue une réorientation des moyens opérationnels de l’ANSSI vers deux tâches : le traitement des comptes utilisateurs compromis et l’analyse des violations de données.

[Cybersécurité : l’ANSSI lance son mécanisme REACTIV dédié aux services de l’État – Next↗](https://next.ink/brief-article/cybersecurite-lanssi-lance-son-mecanisme-reactiv-dedie-aux-services-de-letat/)

Comme nous [l’indiquions au moment de l’annonce](https://next.ink/brief-article/cybersecurite-lanssi-lance-son-mecanisme-reactiv-dedie-aux-services-de-letat/), l’agence obtient deux pouvoirs nouveaux. D’abord, elle centralise la communication technique de crise. Ensuite, et surtout, l’ANSSI peut imposer aux ministères des mesures de protection immédiates dans des délais contraints. Vincent Strubel, directeur de l’agence, avait bien précisé lors de l’annonce que l’effort était temporaire et qu’il se faisait au détriment d’autres pans de la menace.

La situation exigeait une forme d’urgence. Il n’aura fallu que trois semaines pour que l’ANSSI publie un [premier point d’étape](https://www.cert.ssi.gouv.fr/cti/CERTFR-2026-CTI-006/), faisant le bilan des attaques des deux derniers mois contre plusieurs ministères.

- 
    
        [L’Éducation nationale s’est encore fait pirater, un nombre important d’agents concernés](https://next.ink/brief-article/leducation-nationale-sest-encore-faite-pirater-un-nombre-important-dagents-concernes/)    
- 
    
        [Le piratage du ministère de l’Intérieur : un coup de bol opportuniste, et même pas ciblé](https://next.ink/252664/le-piratage-du-ministere-de-linterieur-un-coup-de-bol-opportuniste-et-meme-pas-cible/)    
- 
    
        [Troisième fuite confirmée aux impôts, Bercy détaille sa réponse aux attaques](https://next.ink/252117/troisieme-fuite-confirmee-aux-impots-bercy-detaille-sa-reponse-aux-attaques/)    

### Des brèches en pagaille

Depuis le 1ᵉʳ août 2026, 99 violations de données ont été signalées à l’ANSSI, dont 67 sont confirmées et 32 sont en cours de traitement par l’agence.

Parmi les incidents, [la faille CVE-2026-72898](https://nvd.nist.gov/vuln/detail/cve-2026-72898) (score CVSS 10) dans Metabase (une plateforme open source dédiée à l’intelligence économique) et son exploitation sont en bonne place. L’ANSSI évoque neuf instances ministérielles compromises depuis début août. « *Cette vulnérabilité, de type injection SQL, permet l’accès à la base de données de l’application Metabase pour un utilisateur non authentifié et l’obtention des droits administrateurs de l’instance* », indique le rapport.

Lorsque la faille a été découverte le 3 août [par Metabase](https://www.metabase.com/blog/security-update-6-aug-2026), elle était déjà exploitée. Le correctif a été publié le 6 août. Pour les ministères français en revanche, il ne s’agissait probablement déjà plus d’une faille 0-day, l’attaque contre France VAE étant par exemple survenue le 8 août. L’exploitation de cette faille a servi également contre Zéro Logement Vacant, Qualicharge et probablement Docurba, même si l’enquête n’est pas terminée.

Mais cette faille a aussi servi contre le propre Laboratoire d’innovation de l’ANSSI et contre la Direction interministérielle du numérique (DINUM), deux agences relevant du Premier ministre. Dans le premier cas, l’ANSSI pointe « *la compromission de 118 comptes utilisateurs Metabase dont une trentaine de comptes d’utilisateurs externes (données statistiques d’utilisation, identifiants, courriels et mots de passe hachés)* ». Les instances vulnérables ont été mises à jour, les mots de passe ont été renouvelés pour l’ensemble des comptes et les comptes inutilisés depuis plus de trois mois ont été désactivés.

Dans le cas de la DINUM, deux instances Metabase ont été compromises, ProConnect et Nuage-Public. « *Les données exfiltrées portent sur des informations administratives d’organismes publics (SIREN, SIRET, budgets, effectifs), des métadonnées de contributions à des projets logiciels open source, et des historiques de connexions anonymisés* », indique l’ANSSI. L’agence ajoute que ces données étaient cependant déjà publiques. Là encore, les vulnérabilités ont été colmatées, les secrets réinitialisés et les comptes créés par l’attaquant supprimés.

Le rapport n’indique pas toutefois dans quelle mesure ces instances Metabase étaient exposées à internet. Dans tous les cas, l’information tombe mal pour l’ANSSI, qui doit montrer l’exemple, notamment en matière de réactivité sur les correctifs sortant régulièrement. Il s’est écoulé au moins plusieurs jours entre la publication du correctif de Metabase et les premiers signes d’attaque contre la faille au sein des ministères, témoignant d’un retard dans l’application. Dans le cas de l’agence, même s’il s’agit uniquement de son Laboratoire d’innovation, le signal renvoyé n’est pas glorieux.

On peut noter également que l’avis du CERT-FR sur plusieurs failles Metabase a [été publié le 24 août](https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-1075/), alors que trois des quatre failles (dont CVE-2026-72898) étaient [connues depuis le 6](https://github.com/metabase/metabase/security/advisories/GHSA-vwf4-m7j8-wcjf) et la dernière le 11.

### Des défauts de sécurisation classiques

Les autres incidents relèvent malheureusement de défauts de sécurité classiques. Par exemple, des identifiants volés par des infostealers sur des postes personnels ou de partenaires, puis utilisés contre des services exposés sans double authentification. C’est le cas pour le PIGP (Portail de la Gestion Publique de la DGFIP), le cadastre et l’AEFE (Agence pour l’enseignement français à l’étranger).

L’absence de double authentification ressort justement dans le rapport, ou un deuxième facteur par simple e-mail, cette méthode n’étant plus considérée comme robuste depuis longtemps. Le point de situation évoque également la compromission de sous-traitants, dont un de TRACFIN, et le serveur d’échange avec les prestataires de la DGDDI.

On note aussi que plusieurs incidents sont en cours de qualification. Par exemple, pour Signal Logement (identification de logements insalubres) et le BCPR (Bureau des courriers parlementaires et réservés), duquel des e-mails auraient été exfiltrés, sans que l’ANSSI en soit certaine pour l’instant.

En outre, si la mission de REACTIV est surtout de pouvoir imposer des mesures concrètes dans des délais contraints, on ne sait rien des éventuels changements mis en place pour faire évoluer la culture de la cybersécurité chez l’ensemble des personnes concernées. Si l’exploitation de failles peut souvent être combattue par une application stricte des correctifs de sécurité, les attaques passant par des comptes compromis doivent interpeler les utilisateurs impliqués et leur hygiène numérique, dont la gestion de leurs mots de passe.

Une utilisation sérieuse de la double authentification ne semble pas toujours la règle non plus, le mécanisme relevant des ministères et de leurs services informatiques. À ce sujet, la position de l’ANSSI est d’ailleurs claire : « *facteur clé de nombreux incidents analysés par l’ANSSI, l’absence de MFA, ou l’utilisation d’un second facteur faible (e-mail), a facilité les intrusions puisqu’un mot de passe faible ou une fuite de mot de passe suffisait à l’attaquant pour s’octroyer a minima un accès utilisateur* ».

## Commentaires (2)

Abonnez-vous pour prendre part au débat

Déjà abonné ou lecteur ? Se connecter

## Cet article est en accès libre, mais il est le produit d'une rédaction qui ne travaille que pour ses lecteurs, sur un média sans pub et sans tracker. Soutenez le journalisme tech de qualité en vous abonnant.

Accédez en illimité aux articles d'un média expert

Profitez d'au moins 1 To de stockage pour vos sauvegardes

Intégrez la communauté et prenez part aux débats

Partagez des articles premium à vos contacts

Abonnez-vous
Hier à 21h31

Il suffit que la/les personnes en charge de l'application du patch n'aient pas étés mise au courant avant le WE, ou qu'elles n'aient pas pu l'appliquer ce même jour et PAF !

N'oublions pas que l'application de patch n'est pas forcément automatique et que les équipes peuvent ne pas être dimensionnées pour faire ces actions assez rapidement.

Et que dire du shadow IT...

Aujourd'hui à 00h42

Ce genre d’application c'est plutôt orienté interne, donc de base on évite de l'exposer publiquement si ce n'est pas nécessaire (et pour les presta et les itinérant on passe par un VPN c'est des pratiques plus que généralisé).

Ensuite qu'une injection SQL passe ça laisse supposer l'absence de WAF qui reste assez efficace pour bloquer ce genre de requête malveillante, d'autant plus quand il a des mises à jour auto avec de règles dédié à éviter l'exploitation des CVE à la mode.

Et puis plus particulièrement les outils de reporting/analytiques connecté à des grosses sources de donnée c'est un peu un running gag de la sécurité tellement on voit régulièrement des fuites qui sont lié à ce type d'usage (parce que bien souvent ça provient de demande "urgente" de la direction/marketing/... d'avoir de jolie rapport qui n'ont que peu d’intérêt pour le métier donc on fait bricoler ça vite fait par des gens pas forcément qualifié/concerné puis ça reste en place et on l'oublie vite car au final personne ne l'utilise).

Bref ça reste pas de bol mais ça fait un peu amateur pour l'ANSSI de s'être pris les pieds dans le tapis de cette façon (malheureusement la sécu ça pardonne pas trop).

## Signaler un commentaire

Voulez-vous vraiment signaler ce commentaire ?
