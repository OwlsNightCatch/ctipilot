---
title: "Cyberattaque : des pirates ont réglé des congélateurs de plasma à 110 °C"
author: Florian BURNEL
url: https://www.it-connect.fr/cyberattaque-efs-coolworld-congelateurs-plasma/
hostname: it-connect.fr
description: Un prestataire de l'EFS piraté, des congélateurs de plasma réglés à 110 °C au lieu de -30 °C. Ce que l'on sait de l'attaque qui touche le secteur de la santé.
sitename: IT-Connect
date: "2026-11-04"
categories: ['Actu Cybersécurité']
tags: ['cybersécurité,actu cybersécurité,non classé']
fingerprint: b9e9fb51962ecf2
---
# Cyberattaque contre un prestataire de l’EFS : des congélateurs de plasma réglés à 110 °C

**Des congélateurs normalement maintenus autour de -30 °C, reprogrammés pour atteindre 110 °C. À l'intérieur, des échantillons de donneurs, mais aussi du plasma destiné aux transfusions. C'est le résultat d'une cyberattaque visant Coolworld, un prestataire de l'Établissement français du sang (EFS). Voici ce que l'on sait.**

Certains cybercriminels n'ont aucune pitié au point de jouer avec la vie des citoyens. Cette nouvelle cyberattaque a été [révélée le 3 novembre 2026 par Le Canard enchaîné](https://www.lecanardenchaine.fr/police-justice/55332-les-hackers-ont-du-sang-sur-les-mains) : dans la nuit du dimanche 1er au lundi 2 novembre 2026, des attaquants s'en sont pris à Coolworld. Cette entreprise est un spécialiste des solutions frigorifiques et de leur maintenance, notamment pour le secteur médical. C'est un technicien d'astreinte qui aurait repéré une remontée anormale des températures pendant la nuit.

Dans un premier temps, l'EFS a d'abord évoqué des échantillons de donneurs, conservés pour la surveillance de la sécurité transfusionnelle. Puis, dans un second temps, l'EFS a précisé au Canard enchaîné que du plasma congelé destiné à être transfusé à des patients était aussi concerné. Quand on sait que les réserves de plasma et de sang sont régulièrement dans le rouge, ce type d'incidents montre que les individus à l'origine de ces actes sont sans scrupules.

À ce jour, ni le nombre d'installations touchées, ni la durée de l'incident, ni la méthode d'intrusion n'ont été rendus publics. Toutefois, les installations touchées se trouveraient notamment en Bourgogne-Franche-Comté.

## 110 °C : une consigne, pas une température atteinte

Dans le cadre de cette attaque, les attaquants auraient modifié la consigne, c'est-à-dire la valeur demandée au régulateur. Cela ne signifie pas que les poches de plasma ont atteint 110 °C, mais elle agit sur le comportement de l'équipement. Par exemple, une telle consigne peut couper la production de froid, voire activer des résistances de chauffe comme celles utilisées pour le dégivrage.

Dans les deux cas, la température remonte progressivement, et quand il s'agit du plasma, c'est forcément un problème. Je ne suis pas un spécialiste, mais d'après ce que j'ai pu lire, le plasma frais congelé doit être conservé à -25 °C ou moins : au-delà, et trop longtemps, les produits sortent du circuit transfusionnel. Le temps de réaction est donc décisif, et la réaction du technicien a peut-être permis d'éviter la destruction de plasma (aucune information à ce sujet pour le moment).

## Le même mode opératoire que dans les supermarchés ?

Difficile de ne pas faire le rapprochement. Dans la nuit du 11 au 12 octobre 2026, des centaines de supermarchés français ont vu leurs frigos chauffer. J'ai publié un article à propos de [cette cyberattaque contre les systèmes de froid Danfoss qui a frappé des magasins U et Intermarché](https://www.it-connect.fr/cyberattaque-supermarches-froid-danfoss/), où les pirates avaient détourné la fonction de dégivrage.

Dans la foulée, le CERT-FR avait publié un [bulletin d'alerte](https://cert.cyber.gouv.fr/alerte/CERTFR-2026-ALE-012/) à propos des contrôleurs à distance Danfoss des séries AK-SM et AK-SC, ainsi que des superviseurs Copeland xweb et Dixell xweb. Et puis, le 21 octobre 2026, auditionné au Sénat, Vincent Strubel, directeur général de l'ANSSI, a attribué l'attaque des supermarchés à des défauts de sécurité élémentaires (équipements exposés sur Internet, mots de passe faibles) et a étendu le constat au secteur de la santé, qui utilise ce type d'installations *"pour stocker des vaccins ou des choses dangereuses"*, a-t-il alerté, comme le rapporte [Public Sénat](https://www.publicsenat.fr/actualites/politique/des-defauts-de-securisation-elementaire-et-des-mots-de-passe-faibles-ont-permis-la-cyberattaque-contre-les-frigos-de-supermarches).

Alors, rien ne permet d'affirmer que les équipements gérés par Coolworld font partie des modèles visés par l'alerte du CERT-FR, ni que les auteurs sont les mêmes. Mais, cet incident fait partie de la même vague d'attaques, et celle-ci s'est d'ailleurs étendue en dehors de la France. En effet, des cybercriminels ont fait [chauffer les frigos de supermarchés ailleurs en Europe, notamment en Belgique et en Suède](https://www.it-connect.fr/cyberattaque-frigos-supermarches-belgique-suede/).
