---
title: Cybervorfall bei Iperius (Backup, Remote-Software), Dienste offline (4.11.2026)
author: Markus
url: https://borncity.com/blog/2026/11/05/cybervorfall-bei-iperius-backup-remote-software-dienste-offline-4-11-2026/
hostname: borncity.com
description: Der Software-Anbieter Iperius hat einen Cybervorfall erlitten, wie ich gerade erfahren habe. Dadurch stehen diverse Dienste im Bereich Shop-Systeme derzeit nicht zur Verfügung. Dienste für Backup…
sitename: Borns IT- und Windows-Blog
date: "2026-11-05"
categories: ['Internet', 'Sicherheit', 'Software']
tags: ['Backup', 'Internet', 'Sicherheit', 'Software']
fingerprint: "1fd5db2bfadd6e6e"
---
Der Software-Anbieter Iperius hat einen Cybervorfall erlitten, wie ich gerade erfahren habe. Dadurch stehen diverse Dienste im Bereich Shop-Systeme derzeit nicht zur Verfügung. Dienste für Backup, Remote-Software etc., sind dagegen weiterhin für Kunden verfügbar.


## Wer oder was as ist Iperius?

[Iperius](https://www.iperiusbackup.de/iperius-remote-desktop.aspx) ist eine italienische IT-Software-Suite (entwickelt von Enter Srl), die sich auf Backup-Lösungen und Remote-Desktop-/Fernwartungs-Software spezialisiert hat. Es gibt verschiedene Produkte wie:

- Iperius Backup: Eine All-in-One-Software für Datensicherung und Disaster Recovery. Sie unterstützt unter anderem Server, virtuelle Maschinen (VMware ESXi, Hyper-V, Proxmox), Datenbanken (SQL, Oracle etc.), Microsoft 365 sowie Cloud-Speicher (Google Drive, Amazon S3, Azure).
- Iperius Remote: Eine Software für Fernzugriff, Remote-Desktop-Steuerung und technischen Support (als Alternative zu Tools wie TeamViewer oder AnyDesk) für Windows, Mac, Linux, iOS und Android.
- Iperius ONE: Eine kombinierte Plattform für MSPs (Managed Service Provider) mit RMM (Remote Monitoring and Management), Backup, Patch-Management und zentraler Verwaltung.

Die Software-Suite dürfte bei dem einen oder anderen Administrator aus der Leserschaft bekannt sein.

## Hinweis auf einen Cybervorfall

Ein ungenannt bleiben wollender Blog-Leser hat mich gerade über den Cybervorfall informiert, da er per E-Mail vom Anbieter informiert wurde. Versucht man die Webseiten des Anbieters aufzurufen, werden diese im Browser nicht angezeigt oder es kommt eine Störungsmeldung.

Die Webseite sei kurzzeitig nicht in Betrieb, sie werde gerade "aktualisiert". Der Leser hat mir aber eine E-Mail zur Kenntnis gegeben, dass die "Aktualisierung" durch einen Cyberangriff erforderlich wurde.

Obiger Ausriss aus einer Sicherheitswarnung bestätigt, dass der Anbieter Opfer eines Cyberangriffs war, in dessen Folge einige Dienste wie das Dashboard von Iberius Console, der Kundenbereich des Online-Shops und individuelle Clients eingeschränkt wurden und nicht verfügbar sind. Backup, Remote-Software, Storage etc. laufen weiter.

Es liegen diem Anbieter auch keine Hinweise auf unbefugte Zugriffe auf Daten in den Speichersystemen vor. Auch gibt es laut Sicherheitsmeldung des Anbieters keine Hinweise auf Risiken bei Kreditkartenzahlungen. Es sei jedoch möglich, dass einige E-Mail-Adressen kompromittiert wurden. Kunden mögen bitte Sie daher besonders auf

verdächtige Nachrichten, insbesondere auf Aufforderungen zur Passwortänderung achten, heißt es.

Das Sicherste ist halt mit Bordmitteln arbeiten.

Je mehr Software, desto mehr potentielle Sicherheitslücken.

Volle Zustimmung, aber oft ist es doch so, das Bordmittel nicht intuitiv sind. Oder nicht die Funktionalität hat, welche man benötigt.

Ein Beispiel, das Windowseigene "Backup" (System und Sicherheit > Sichern und Wiederherstellen (Windows 7). Da nehme ich doch lieber Veeam Agent Windows Free, oder Macrium Reflect Free. Beide nutze ich schon seit 10 Jahren +, für meine privaten Systeme. Auch das Recocery funktioniert einwandfrei. Das teste ich alle paar Wochen mal durch.

Ja das stimmt, wir nutzen Synology Active Backup. Das ist aber auch eine zielgerichtete Lösung von einem großen Hersteller und nicht so ein All-in-one Paket von einem Nischenhersteller wie es das bei Iperius zu sein scheint.

Bei solchen Sachen wie ESET bin ich mir auch nicht sicher wieviel Kollateralschäden da entstehen. Da setze ich lieber auf den Defender von Microsoft.
