---
title: CLI von OVHcloud war am 19.10.2026 kompromittiert
author: Fritz
url: https://borncity.com/blog/2026/10/19/cli-von-ovhcloud-war-am-19-10-2026-kompromittiert/
hostname: borncity.com
description: Kurze Information und Warnung, falls ein Leser oder eine Leserin die CLI von OVHcloud verwendet und zufällig am 19. Oktober 2026 von den GitHub-Seiten der OVHcloud heruntergeladen hat.
sitename: Borns IT- und Windows-Blog
date: "2026-10-19"
categories: ['Sicherheit', 'Software']
tags: ['Sicherheit', 'Software']
fingerprint: "334518fd86b4787"
---
Kurze Information und Warnung, falls ein Leser oder eine Leserin die CLI von OVHcloud verwendet und zufällig am 19. Oktober 2026 von den GitHub-Seiten der OVHcloud heruntergeladen hat. Ich bin heute auf den Tweet von Octave Klaba (von OVHcloud) gestoßen, der schrieb, dass die CLI-Version von einem Hacker kompromittiert worden sei. OVHcloud hat es – nach Hinweisen von Kunden – gemerkt und die kompromittierten Versionen von GitHub entfernt.


Das Command Line Interface (CLI) der OVHcloud ist die Software, über die die OVHcloud-Dienste verwaltet werden. Um 18:52 Uhr informierte Octave Klaba über die Kompromittierung.

Falls Sie heute die neueste Version der CLI von OVHcloud heruntergeladen haben, danke, dass Sie sie sehr schnell erneut aktualisieren. Andernfalls löschen.


Es handelt sich um das offizielle OVHcloud CLI-Repo auf [dieser GitHub-Seite](https://github.com/ovh/ovhcloud-cli). Die CLI-Version von am 19. Oktober 2026, 14:47 Uhr CET, wurde von einem Hacker kompromittiert. OVHclout habt es um 16:21 Uhr erkannt und blockiert, nachdem Kunden, das Problem gemeldet haben.

Die kompromittierten Versionen sind v0.11.0 v0.12.0 v0.13.0 v0.14.0 v0.15.0. Die Version v0.10.0 und die kommende 0.16.0 sind sauber.

OVHclout habe gerade die ersten Überprüfungen abgeschlossen und kein anderes Repo ist betroffen, hieß es. Man habe den Vorfall auch zurückverfolgt. Der Hacker hat das GitHub-Konto eines der Entwickler genutzt und Binärcode hinzugefügt, dessen Aufgabe es ist, Geheimnisse von der Festplatte zu extrahieren. Die Qualität des Binärs ist mittelmäßig, aber es kann bis zum Ende durchlaufen.

Wer die kompromittierte CLI heruntergeladen und ausgeführt hat, sollte alle Passwörter, die auf der Festplatte gespeichert waren, vorsorglich ändern. OVHclout setzt die Untersuchungen am Binär fort und will bald zusätzliche Details veröffentlichen.

Die dunklen Wolken brauen sich immer mehr zusammen, Cyber Polygon läuft offenbar planmässig, bald wird das Internet, das wir kennenlernen durften, nicht mehr bestehen.
