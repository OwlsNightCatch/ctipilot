# extract: served via trafilatura-direct
---
title: "Carrefour : des données clients exposées après la cyberattaque de son prestataire"
author: Thomas Lazzaroni
url: https://www.cyberattaque.org/carrefour-des-donnees-clients-exposees-apres-la-cyberattaque-de-son-prestataire/
hostname: cyberattaque.org
description: Carrefour a informé début septembre certains de ses clients qu’une partie de leurs données personnelles a été exposée à la suite d’un incident de sécurité
sitename: Cyberattaque.org
date: "2026-09-26"
categories: ['Attaque']
fingerprint: "75baad140f1813f2"
---
**Carrefour** a informé début septembre certains de ses clients qu’une partie de leurs données personnelles a été exposée à la suite d’un incident de sécurité ayant touché l’un de ses prestataires. Les informations concernées comprennent les **noms, prénoms, adresses e-mail et numéros de téléphone**.

Le groupe ne nomme pas directement le prestataire dans la communication consultée par **Cyberattaque.org**. Plusieurs éléments permettent cependant d’identifier **[Shipup](https://www.cyberattaque.org/tag/shipup/)**, la plateforme de suivi des livraisons déjà impliquée ces dernières semaines dans plusieurs fuites touchant de grandes enseignes françaises.

## Carrefour confirme une fuite chez un prestataire

Dans une communication adressée à ses clients dont Cyberattaque.org s’est procuré une copie, Carrefour explique qu’« un de ses prestataires » a subi un incident de sécurité au sein de son système d’information.

Les données personnelles susceptibles d’avoir été compromises sont limitées, selon l’enseigne, aux **prénom, nom, adresse e-mail et numéro de téléphone**.

Carrefour précise qu’**aucune donnée bancaire ni aucun mot de passe** n’a été compromis dans le cadre de cet incident. L’enseigne invite néanmoins ses clients à se méfier des e-mails, SMS et autres communications suspectes pouvant exploiter les informations dérobées.

## Le prestataire concerné est Shipup

Si Carrefour ne cite pas le nom de son sous-traitant dans son message, les éléments recoupés par Cyberattaque.org permettent de rapprocher cette notification de la [cyberattaque contre Shipup](https://www.cyberattaque.org/cyberattaque-shipup/).

Shipup est une société française spécialisée dans le **suivi des colis et les communications post-achat**. Sa plateforme permet notamment aux sites e-commerce d’envoyer des notifications de livraison par e-mail ou SMS et de proposer des pages de suivi personnalisées.

Carrefour faisait déjà partie des enseignes publiquement identifiées comme utilisatrices de Shipup. Les catégories de données annoncées par Carrefour correspondent également à celles exposées chez les autres clients touchés : **nom, prénom, e-mail et numéro de téléphone**.

## Une faille Metabase à l’origine de l’incident

La compromission de Shipup est liée à une importante campagne de cyberattaques ayant ciblé **Metabase**, un logiciel d’analyse et de visualisation de données utilisé en interne par de nombreuses entreprises.

Une vulnérabilité critique, référencée **CVE-2026-72898**, permettait notamment à un attaquant distant non authentifié de compromettre une instance vulnérable et d’accéder potentiellement aux données accessibles depuis celle-ci.

Dans les précédents dossiers liés à Shipup documentés par Cyberattaque.org, des accès non autorisés avaient été possibles entre le **31 juillet et le 17 août 2026**. Carrefour ne précise toutefois pas cette période dans le message actuellement adressé à ses clients.

## Micromania et Easypara déjà concernés

Carrefour vient allonger la liste des enseignes touchées indirectement par cette même compromission. Cyberattaque.org avait notamment révélé que [Micromania](https://www.cyberattaque.org/micromania-ses-donnees-clients-exposees-apres-une-cyberattaque-chez-shipup/) avait exposé les mêmes catégories de données après l’incident chez Shipup.

**[Easypara](https://www.cyberattaque.org/easypara-une-faille-metabase-chez-son-prestataire-expose-les-coordonnees-de-certains-clients/)** avait également informé ses clients d’un accès non autorisé chez son prestataire de suivi des livraisons. Là encore, les données concernées comprenaient les noms, prénoms, adresses e-mail et numéros de téléphone lorsqu’ils avaient été renseignés.

Ces différents cas sont détaillés dans notre dossier consacré à [Shipup](https://www.cyberattaque.org/cyberattaque-shipup/), qui avait déjà identifié Carrefour parmi les grandes enseignes utilisant le service avant même la confirmation de son exposition.

## Une cyberattaque avec un effet domino

L’incident illustre surtout le risque représenté par les prestataires communs à de nombreuses grandes entreprises. Shipup accompagne **plus de 700 marques** : une seule compromission de son infrastructure peut donc avoir des conséquences chez plusieurs clients sans que leurs propres systèmes aient été directement piratés.

Dans le cas de Carrefour, rien dans la communication consultée ne laisse penser que le site, les comptes clients ou les systèmes internes du groupe aient été compromis. L’exposition provient des données confiées au prestataire dans le cadre de ses services.

## Le principal risque reste le phishing

Les informations exposées ne permettent pas directement d’effectuer un paiement ou de se connecter à un compte Carrefour. Elles peuvent en revanche servir à rendre des **campagnes de phishing beaucoup plus crédibles**.

Un fraudeur disposant du véritable nom, de l’adresse e-mail et du téléphone d’un client peut notamment se faire passer pour Carrefour ou un transporteur en évoquant une livraison, une commande, un remboursement ou un colis nécessitant une action urgente.

Carrefour indique que les mesures nécessaires ont été prises par son prestataire pour traiter l’incident. Le groupe ne communique en revanche pas, à ce stade, le **nombre de clients concernés**.
