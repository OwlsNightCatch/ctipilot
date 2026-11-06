---
title: Hoster Mittwald Opfer eines Cyberangriffs (5.11.2026)
author: Markus
url: https://borncity.com/blog/2026/11/05/hoster-mittwald-opfer-eines-cyberangriffs-5-11-2026/
hostname: borncity.com
description: Der Hoster Mittwald hat am 5. November 2026 gegen 11:34 Uhr den Zugriff auf sein Kundenportal mStudio (Login und alle SSH-Verbindungen) aus Sicherheitsgründen deaktiviert. Inzwischen ist klar…
sitename: Borns IT- und Windows-Blog
date: "2026-11-05"
categories: ['Cloud', 'Internet', 'Sicherheit']
tags: ['Cloud', 'Internet', 'Sicherheit']
fingerprint: d2d3de8e8c395b86
---
Der Hoster Mittwald hat am 5. November 2026 gegen 11:34 Uhr den Zugriff auf sein Kundenportal mStudio (Login und alle SSH-Verbindungen) aus Sicherheitsgründen deaktiviert. Inzwischen ist klar, dass es einen Cyberangriff auf den MCP-Server des Hosters gegeben hat. Mittwald informiert inzwischen auf seiner Webseite.


## Ein Blick auf Mittwald

Mittwald ist ein deutscher Internetdienstleister und Hosting-Provider aus Espelkamp (Nordrhein-Westfalen) mit ca. 200 Mitarbeitern. Der Hoster wird gerne von Agenturen, Freelancern und Web-Professionals für Web-Projekte (Webhosting, Managed Server und Cloud-Lösungen für Content-Management-Systeme wie WordPress, TYPO3, Joomla! und Magento) gebucht. Kunden haben Zugriff auf ein mStudio genanntes Control-Panel. Dort können Agenturen Kundenprojekte, Containern (z. B. Docker/n8n) und KI-Hosting verwalten.

## Ein Leserhinweis auf Probleme

Blog-Leser Adrian hat mich zum heutigen 5. November 2026 gegen Abend per Mail kontaktiert und schrieb: "Ich möchte Sie als Mittwald-Kunde auf die aktuellen Vorfälle beim Hosting-Anbieter aufmerksam machen. Möglicherweise ist das Thema für Ihren Blog interessant."

Der Leser beklagte, dass der Zugang zum Kundenportal mStudio in den vergangenen 48 Stunden nach seiner Beobachtung mehrfach nicht möglich war. In der Nacht zum heutigen 5. November sei zudem die Mittwald-Webseite nicht erreichbar gewesen. Die [obige Mittwald-Statusseite](https://www.mittwald-status.de/incidents) scheint die Beobachtungen des Lesers indirekt zu bestätigen, obwohl es beim letzten Eintrag hieß, dass die Störung beseitigt sei. Auf allestoerungen.de ist nichts an Störungen zu finden. Der Leser schrieb noch: "Eine direkte Information zu den Hintergründen oder einer möglichen Betroffenheit habe ich als Kunde bislang nicht erhalten. "

## Es gab einen Cybervorfall

Falls wer als Mittwald-Kunde am heutigen 5. November 2026 und die Tage vorher solche Probleme beim Zugriff auf das Kundenportal mStudio oder die Webseite des Anbieters hatte, hier ist der Grund. Mittwald hat laut [dieser MCP-Seite](https://www.mittwald.de/lp/mcp-faq) Sicherheitsmaßnahmen ergriffen und den Zugang von Kunden aus dem Kundencenter, die den Mittwald AV Manager nutzen, vorübergehend gesperrt.

Solange die Sperre aktiv ist, kannst der Kunde sich nicht im Kundencenter einloggen und den AV-Manager nutzen. Die Projekte seien davon nicht betroffen. Alle Webseiten laufen ganz normal weiter. Unter "Vorfall – 05.11.2026 · 11:34 CET" erfährt man aber:

Wir haben uns dazu entschieden den mStudio Login zu deaktivieren und alle SSH-Verbindungen zu beenden & deaktivieren. Ebenfalls sind die mittwald-Extensions deaktiviert.


In einer Nachtrags-Mail schrieb der Leser, dass Mittwald ihn am späten Nachmittag per E-Mail über einen Sicherheitsvorfall informiert habe. Der Blog-Leser hat mir dazu den nachfolgenden Screenshot mitgeliefert, der die Situation erklärt.

Es gab also bereits am 27. Oktober 2026 einen unbefugten Zugriff auf den MCP-Server, der aber erst am 4. November 2026 festgestellt wurde. Inzwischen ist auf der [MCP-FAQ-Seite](https://www.mittwald.de/lp/mcp-faq) von Mittwald folgende Information zu finden.

Untersuchung – 05.11.2026 · 17:02 CET

Unsere Analysen haben einen ubefugten Zugriff auf das mStudio über unseren MCP-Server festgestellt. Wir arbeiten mit Hochdruck an der Analyse und daran, die Folgen des Vorfalls zu beheben.

Zu Deinem Schutz sind vorübergehend einige Funktionen deaktiviert:

MCP-Server

Login ins mStudio

SSH-Zugriff

mittwald Extensions

Bestellungen

Das ist eine reine Vorsichtsmaßnahme.


Bleibt nun abzuwarten, was die weiteren Untersuchungen von Mittwald ergeben.

Was ich nicht verstehe: Selbst, wenn man nicht betroffen ist, weil man den MCP-Server nicht genutzt hat, hat man seit heute Mittag keinen Zugriff mehr auf seinen gemieteten VServer. Von außen ist zwar alles abrufbar, aber kein SSH etc.

Das ist irgendwie inzwischen typisch Mittwald. Bei PHP2Shell hat der Patch bei Mittwald auch vergleichsweise lang gedauert, bis in die Nacht waren alle Projekte offline. Übrigens auch solche, die PHP nicht nutzen.

Ich habe inzwischen die mehrtägigen Ausfälle in 2024 verziehen, aber Mittwald macht es einem auch nicht leicht.

Haben die sieben Tage gebraucht um festzustellen das etwas nicht stimmt? Respekt! In was für einem Tempo vielen ihre gammelige IT um die Ohren fliegt ist sagenhaft. Vertrauen kann man dahingehend ja kaum noch haben.

Wir sind ebenfalls betroffen. Ausgerechnet über das Wochenende hat unser Dienstleister die Homepage von Typo3 v10 auf v13 umgestellt. Gestern sollten wir alle DNS Einstellungen anpassen und anschließend bestätigen. Haben wir gemacht, hat alles geklappt. Rückgängig ist also nicht.

Heute haben wir die Info erhalten, dass man Probleme bei der Migration hat und es ein Problem beim Hoster Mittwald gibt. Man soll bitte keine DNS Einstellungen anpassen.

Nun die Homepage läuft und funktioniert, aber der Dienstleister kommt aktuell nicht mehr dran.
