---
title: "Actief misbruik van zeroday-kwetsbaarheden in Zammad: update nu | NCSC"
url: https://www.ncsc.nl/alerts/actief-misbruik-van-zeroday-kwetsbaarheden-in-zammad-update-nu
hostname: ncsc.nl
description: Zammad-kwetsbaarheden worden actief misbruikt. Update direct en neem maatregelen om je systemen te beschermen tegen mogelijke aanvallen.
sitename: NCSC
date: "2025-10-14"
---
# Actief misbruik van zeroday-kwetsbaarheden in Zammad: update nu

- Alert
- 30 september 2026

Er zijn twee zeroday-kwetsbaarheden ontdekt in Zammad, een softwareproduct voor klantenservice. De kwetsbaarheden hebben de kenmerken CVE-2026-102489 en CVE-2026-102490. Beide kwetsbaarheden worden actief misbruikt en de kans op misbruik en de mogelijke schade zijn hoog.

## Wat voor soort product is het?

Zammad is een softwarepakket dat bedrijven helpt bij het beheren van klantvragen en ondersteuning. Het wordt gebruikt om communicatie met klanten te organiseren en te volgen.

## Hoe kan de kwetsbaarheid misbruikt worden?

Er zijn twee ernstige kwetsbaarheden met actief misbruik.

- De kwetsbaarheid, met kenmerk CVE-2026-102489, maakt het mogelijk dat een aanvaller zonder in te loggen op afstand schadelijke code kan uitvoeren, ook wel Remote Code Execution (RCE) genoemd.
- De kwetsbaarheid, met kenmerk CVE-2026-102490, stelt een aanvaller met beperkte toegang in staat om de hoogste beheerdersrechten (rootrechten) op het systeem te krijgen. Dit betekent dat de aanvaller volledige controle over het systeem kan krijgen.

## Wat kan het gevolg zijn van de kwetsbaarheid?

De kwetsbaarheden stellen een aanvaller in staat om schadelijke code uit te voeren en rechten te verhogen. Hierdoor kan een aanvaller het systeem overnemen, gegevens bekijken, aanpassen of verwijderen en het systeem gebruiken voor verdere aanvallen. De eerste kwetsbaarheid met het kenmerk CVE-2026-102489 is al verholpen met het kenmerk. 

De tweede kwetsbaarheid met het kenmerk CVE-2026-102490 is nog niet verholpen.

Beide kwetsbaarheden worden sinds 21 september 2026 actief misbruikt.

## Welke versies zijn kwetsbaar?

De kwetsbaarheid met kenmerk CVE-2026-102489 is aanwezig in versies 6.3.0 tot en met 6.5.4. 

De kwetsbaarheid met kenmerk CVE-2026-102490 is nog niet verholpen en is in alle gangbare versies van Zammad aanwezig.       

## Wat kun je doen?

Maak voor het installeren van de update een kopie van de applicatie- en netwerklogs. Mocht er meer informatie over het misbruik van de tweede kwetsbaarheid, dan kunnen deze logs je in de toekomst helpen om te controleren of jouw systeem is aangevallen.

Zammad heeft een beveiligingsupdate uitgebracht voor de eerste kwetsbaarheid (CVE-2026-102489). Het NCSC adviseert om deze update zo snel mogelijk te installeren.

De tweede kwetsbaarheid (CVE-2026-102490) is nog niet opgelost. Neem contact op met je leverancier als je hierover vragen hebt. Als je niet zeker weet of je Zammad gebruikt of welke versie, neem dan contact op met je IT-dienstverlener.

Resultaten laden...

[Alles binnen alerts](https://www.ncsc.nl/alerts)
