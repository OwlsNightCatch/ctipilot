---
title: SAP räumt einen IT-Sicherheitsvorfall ein, laut Handelsblatt ist die Softwareentwicklung betroffen
author: Markus Seyfferth
url: https://www.drweb.de/sap-it-sicherheitsvorfall-github-entwicklung/
hostname: drweb.de
description: SAP räumt einen IT-Sicherheitsvorfall ein, laut Handelsblatt ist die Entwicklung betroffen. Was bekannt ist und was Kunden und Entwickler jetzt prüfen.
sitename: Dr. Web
date: "2026-11-27"
categories: ['Beste Software finden, Cybersecurity, News']
tags: ['Github', 'SAP']
fingerprint: "57e2dd25ec8963cf"
language: de
image: https://www.drweb.de/wp-content/uploads/2026/11/sap-raeumt-einen-it-sicherheitsvorfall-ein-laut-handelsblatt-ist-die-softwareentwicklung-betroffen-beitragsbild.jpg
pagetype: article
filedate: "2026-11-28"
---
SAP hat am Donnerstagabend, dem 26. November 2026, einen IT-Sicherheitsvorfall eingeräumt und erklärt, der Konzern habe „verdächtige Aktivitäten“ identifiziert und Gegenmaßnahmen ergriffen.<sup>[\[1\]](https://www.drweb.de/sap-it-sicherheitsvorfall-github-entwicklung/#quelle-1)</sup> Hinweise auf einen unbefugten Zugriff auf Geschäftsdaten von Kunden gibt es nach aktuellem Stand der Untersuchung nicht. Den Angriffsweg und mögliche Täter nannte SAP nicht.

[Ein Klick · kostenlosDr. Web bei Google bevorzugenMarkieren Sie drweb.de als bevorzugte Quelle. Dann sehen Sie unsere Artikel öfter unter den Top-Meldungen.Jetzt hinzufügen](https://www.google.com/preferences/source?q=drweb.de)

## Inhalt 3 Abschnitte

Nach Informationen des Handelsblatts aus Konzernkreisen ist die Softwareentwicklung betroffen, und der Spiegel berichtet unter Berufung auf einen Insider von gestohlenen Zugangsschlüsseln für die Plattform GitHub. Auf GitHub speichern Programmierer ihren Code und bearbeiten ihn gemeinsam, SAP stellt dort für viele Produkte und Open-Source-Projekte öffentlich zugänglichen Quellcode bereit.

### Das Wichtigste in Kürze

- SAP räumt „verdächtige Aktivitäten“ ein und hat Gegenmaßnahmen ergriffen, Hinweise auf einen unbefugten Zugriff auf Geschäftsdaten von Kunden gibt es bisher nicht.
- Laut Handelsblatt ist die Softwareentwicklung betroffen, SAP schränkte den GitHub-Zugriff ein, stoppte automatisierte Abläufe und tauschte Signaturschlüssel aus.
- Der Spiegel berichtet von gestohlenen Zugangsschlüsseln, mit denen Angreifer Quellcode kopiert und verändert haben sollen.
- Im April 2026 hatten Angreifer bereits vier offizielle SAP-Pakete auf der Plattform npm vergiftet.

## Was hat SAP bestätigt, und was berichten Medien?

SAP äußerte sich am Donnerstagabend, nachdem der Spiegel zuvor über einen **Hackerangriff** berichtet hatte.<sup>[\[1\]](https://www.drweb.de/sap-it-sicherheitsvorfall-github-entwicklung/#quelle-1)</sup> Nach aktuellem Stand der Untersuchung gebe es keine Hinweise auf einen unbefugten Zugriff auf die Geschäftsdaten von Kunden, teilte der Konzern mit.

Das Handelsblatt schreibt nach Informationen aus Konzernkreisen, der Vorfall laufe intern unter dem Namen **Project Granite** und betreffe zahlreiche Teams der Softwareentwicklung.<sup>[\[1\]](https://www.drweb.de/sap-it-sicherheitsvorfall-github-entwicklung/#quelle-1)</sup> SAP habe den Zugriff auf GitHub eingeschränkt, automatisierte Abläufe in der Entwicklung gestoppt und Signaturschlüssel ausgetauscht. Mit diesen Maßnahmen soll verhindert werden, dass Angreifer mit bereits erbeuteten Zugangsdaten weiter Zugriff auf Systeme und Quellcode haben.

Der Spiegel berichtet unter Berufung auf einen Insider, die Angreifer hätten **Authentifizierungs-Token** von SAP-Mitarbeitern für GitHub erbeutet.<sup>[\[1\]](https://www.drweb.de/sap-it-sicherheitsvorfall-github-entwicklung/#quelle-1)</sup> Ein Token ist ein digitaler Zugangsschlüssel, der einem Programm oder einem Menschen den Zugriff erlaubt, ohne dass bei jedem Zugriff ein Passwort nötig ist. Damit könnten Angreifer unter Umständen Quellcode lesen und verändern.

## Warum ist ein Angriff auf die Entwicklung heikel?

Quellcode ist der Bauplan jeder Software, und wer ihn unbemerkt ändern kann, kann im ungünstigen Fall **Schadcode in Produkte** einschleusen, die Kunden später installieren. Fachsprachlich heißt das Lieferkettenangriff. Ob veränderter Code in ausgelieferte SAP-Produkte gelangt ist, steht in den bisherigen Berichten nicht.

Im Oktober stahl das kompromittierte [LiteLLM 1.107.0 auf PyPI](https://www.drweb.de/litellm-kompromittiert-pypi-zugangsdaten/) Zugangsdaten und installierte eine Hintertür, bei [Zod 4.6.6](https://www.drweb.de/zod-4-6-6-schadcode-repository/) kam der Schadcode dagegen nur bis ins Repository.

SAP-Entwickler waren in diesem Jahr schon einmal das Ziel eines Angriffs. Am 29. April 2026 veröffentlichten Angreifer innerhalb von gut zwei Stunden vergiftete Versionen von **vier offiziellen SAP-Paketen** auf der Plattform npm, die Zugangsdaten von Entwicklern stehlen.<sup>[\[2\]](https://www.drweb.de/sap-it-sicherheitsvorfall-github-entwicklung/#quelle-2)</sup> Diese vier Pakete werden zusammen rund 572.000 Mal pro Woche heruntergeladen. Auf Fragen von The Register verwies SAP damals auf einen Sicherheitshinweis, der nur angemeldeten Kunden zugänglich ist. Ob zwischen beiden Vorfällen ein Zusammenhang besteht, ist nicht belegt.

## Was sollten SAP-Kunden und Entwickler jetzt tun?

In den vorliegenden Berichten steht keine Handlungsempfehlung für Kunden. Entscheider mit SAP-Landschaften sollten deshalb bei ihrem SAP-Ansprechpartner oder Partner nachfragen, ob Auswirkungen auf Produkte, Updates und deren Signaturen zu erwarten sind, und sich die Antwort schriftlich geben lassen.

Teams, die SAP-Pakete oder SAP-Open-Source-Projekte von GitHub oder npm einsetzen, sollten die verwendeten Versionen festschreiben und neue SAP-Releases erst nach einem Blick auf Änderungshistorie und Signatur übernehmen. Eigene GitHub- und npm-Token mit zu weiten Rechten oder ohne Ablaufdatum lassen sich bei dieser Gelegenheit gleich erneuern.
