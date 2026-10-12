---
title: "Sicherheitslücke bei Bricksforge: Angreifer nutzen kritische Upload-Lücke ohne Login aus - Dr. Web"
author: Michael Dobler
url: https://www.drweb.de/bricksforge-sicherheitsluecke-upload-aktiv-ausgenutzt/
hostname: drweb.de
description: "Bricksforge bis 3.1.8.9: Angreifer laden ohne Login PHP-Code über Pro Forms hoch. So schließen Sie die Lücke auf Ihrer WordPress-Website."
sitename: Dr. Web
date: "2026-10-09"
categories: ['Cybersecurity, News, WordPress']
tags: ['Bricksforge', 'Patchstack']
fingerprint: "3af45a1817915ce"
---
Seit Mittwochnacht schleusen Angreifer über das Formularmodul der WordPress-Erweiterung Bricksforge eigenen PHP-Code auf fremde Server. Die Lücke CVE-2026-85097 erreicht einen CVSS-Wert von 9,8 und lässt sich ohne Anmeldung ausnutzen. Die Korrektur steckt in den Versionen 3.1.8.10 und 4.0.1.

[drweb.de als bevorzugte Quelle auf Google hinzufügenQualitätsgeprüfte Inhalte direkt in Google News & DiscoverJetzt hinzufügen](https://www.google.com/preferences/source?q=drweb.de)

Die Sicherheitsfirma Patchstack registrierte den ersten Angriff am 7. Oktober um 23:47 Uhr deutscher Zeit, am selben Tag, an dem die Lücke in ihrer Datenbank erschienen war.<sup>[\[1\]](https://www.drweb.de#quelle-1)</sup> Bricksforge ergänzt den Page-Builder Bricks um Formulare, Animationen und eigene Backend-Seiten; Patchstack zählt rund 6.000 aktive Installationen. Für die Erweiterung ist CVE-2026-85097 die dritte schwere Lücke binnen fünf Wochen.

### Das Wichtigste in Kürze

- Bricksforge bis 3.1.8.9 übernimmt beim Absenden eines Formulars ungeprüfte Dateiangaben aus dem Browser (CVE-2026-85097, CVSS 3.1: 9,8, vergeben von Wordfence; Patchstack vergibt 10,0).
- Angreifer ohne Konto legen so PHP-Dateien auf dem Server ab und übernehmen damit die ganze Website.
- Patchstack beobachtet seit dem 7. Oktober automatisierte Angriffe von 63 verschiedenen IP-Adressen.
- Die Lücke schließen Version 3.1.8.10 in der älteren Reihe und Version 4.0.1 vom 8. Oktober.

## Wie wird aus einem geprüften Bild eine PHP-Datei?

Das **Formularmodul** Pro Forms prüft eine hochgeladene Datei zunächst korrekt auf ihren Dateityp und legt sie in einem temporären Ordner ab. Beim späteren Absenden des Formulars übernimmt Bricksforge jedoch die Dateiangaben, die der Browser mitschickt, ohne erneute Kontrolle.<sup>[\[1\]](https://www.drweb.de#quelle-1)</sup> Angreifer laden deshalb eine Polyglott-Datei hoch, ein gültiges GIF-Bild mit eingebettetem PHP-Code. Als Ziel nennen die Angreifer beim Absenden eine Datei mit PHP-Endung. Bricksforge kopiert den Bildinhalt genau dorthin.

Ein einziger Aufruf dieser Datei genügt, damit der Server den Code ausführt. Die nötige **Sicherheitsmarke** (Nonce) gibt das Plugin auch an Besucher ohne Konto aus. Laut WordPress-Entwicklerhandbuch schützen Nonces ohnehin nur vor untergeschobenen Anfragen und ersetzen keine Rechteprüfung.<sup>[\[2\]](https://www.drweb.de#quelle-2)</sup> Im Changelog schreibt Bricksforge, der Fehler betreffe jede Website mit aktivem Pro Forms, auch ohne Upload-Feld im Formular.[\[3\]](https://www.drweb.de#quelle-3)

Die Lücke steht damit auf der **Stufe** „aktive Ausnutzung beobachtet“. In 95 Prozent der von Patchstack erfassten Anfragen tarnte sich die Schadcode-Datei als GIF oder PNG. Von drei IP-Adressen aus testeten Angreifer 25 Schreibweisen der Dateiendung, um Filter auszutricksen. Im Katalog der US-Behörde CISA für aktiv ausgenutzte Lücken fehlt der Eintrag bislang.

## Warum häufen sich bei Bricksforge die schweren Lücken?

Am 16. August meldete ein Forscher eine **Rechteausweitung**, über die Abonnenten zu Administratoren aufsteigen konnten (CVE-2026-84814, CVSS 9,8). Version 3.1.8.9 behob den Fehler Ende August, Patchstack veröffentlichte den Eintrag am 2. September.<sup>[\[4\]](https://www.drweb.de#quelle-4)</sup> Am 18. September folgte CVE-2026-18030: Über Pro Forms ließen sich ohne Anmeldung fremde Passwörter zurücksetzen (CVSS 8,1, behoben in 3.1.8.8). Passwort- und Upload-Lücke stecken beide im Formularmodul.

Das **Muster** aus geprüftem Upload und ungeprüfter Weiterverarbeitung kennen WordPress-Betreiber aus dem September. Bei der [Upload-Lücke in Gravity Forms](https://www.drweb.de/gravity-forms-kritische-upload-luecke/) umging ein verstecktes Upload-Feld die Prüfung der Dateiendung. Formular-Plugins nehmen Dateien von anonymen Besuchern an und bieten damit die kürzeste Strecke zur Codeausführung. Wie hartnäckig automatisierte Scanner nach einer Offenlegung suchen, zeigte bereits die [Lücke in King Addons for Elementor](https://www.drweb.de/48-400-blockierte-angriffe-king-addons-luecke-wird-aktiv-ausgenutzt/), gegen die Wordfence über 48.400 Angriffsversuche blockierte.

Entwickelt wird Bricksforge in **Saarbrücken**.<sup>[\[5\]](https://www.drweb.de#quelle-5)</sup> Seit dem 11. September 2026 verpflichtet der Cyber Resilience Act der EU Hersteller von Produkten mit digitalen Elementen, eine aktiv ausgenutzte Lücke binnen 24 Stunden als Frühwarnung und binnen 72 Stunden ausführlich zu melden.<sup>[\[6\]](https://www.drweb.de#quelle-6)</sup> Zuständig ist die Stelle im Land der Hauptniederlassung, für Bricksforge also das BSI.

### Drei schwere Lücken in fünf Wochen

## Was sollten Betreiber von Bricksforge jetzt tun?

Bricksforge steht nicht im Plugin-Verzeichnis von wordpress.org, eine öffentliche Versionsstatistik fehlt deshalb. Plugin-Updates gehören bei Bricksforge zur **Jahreslizenz**.<sup>[\[7\]](https://www.drweb.de#quelle-7)</sup> Bei ausgelaufener Lizenz kommt die Korrektur womöglich gar nicht an. Diese Schritte schließen die Lücke und begrenzen den Schaden:

- **Aktualisieren:** Spielen Sie Version 4.0.1 ein, in der älteren Reihe mindestens 3.1.8.10. Version 3.1.8.10 nennt Patchstack als Korrektur, der öffentliche Changelog führt bisher nur 4.0.1.
- **Abschalten:** Klappt das Update nicht sofort, deaktivieren Sie Pro Forms oder die ganze Erweiterung.
- **PHP sperren:** Untersagen Sie per Serverkonfiguration die Ausführung von PHP-Dateien im Upload-Ordner. Eine eingeschleuste Datei bleibt dann wirkungslos.
- **Spuren suchen:** Durchsuchen Sie den Upload-Ordner samt temporärem Bricksforge-Unterordner nach PHP-Dateien, besonders nach Namen mit dem Anfang login\_admin. Prüfen Sie unter Benutzer, ob unbekannte Admin-Konten existieren. Wie Angreifer solche Konten verstecken, zeigen die [Angriffe auf Ninja Forms](https://www.drweb.de/ninja-forms-angriffe-versteckter-admin/).
- **Neu aufsetzen:** Finden Sie Schadcode, spielen Sie eine Sicherung aus der Zeit vor dem 7. Oktober ein und ändern Sie alle Passwörter. Passende Werkzeuge listet der Vergleich der [Backup-Plugins für WordPress](https://www.drweb.de/backup-plugins-fuer-wordpress-vergleich/).

Pro Forms speichert Namen, E-Mail-Adressen und Anfragen von Besuchern. Hatte ein Angreifer Zugriff auf den Server, greift deshalb die **Meldepflicht** nach Art. 33 DSGVO: Birgt der Vorfall ein Risiko für Betroffene, muss die Meldung binnen 72 Stunden bei der Aufsichtsbehörde eingehen.<sup>[\[8\]](https://www.drweb.de#quelle-8)</sup> Für Agenturen mit vielen Bricks-Kundensites beginnt damit wieder das bekannte [Update-Rennen](https://www.drweb.de/90-plugin-luecken-im-mai-wordpress-agenturen-verlieren-das-update-rennen/). Ein Hoster mit eigener Web Application Firewall kann solche Upload-Muster abfangen, bevor das Plugin-Update ankommt. Tarife dieser Art vergleicht der [WordPress-Hosting-Vergleich](https://www.drweb.de/wordpress-hosting-vergleich/), Grundregeln bündelt der Ratgeber zur [WordPress-Sicherheit](https://www.drweb.de/wordpress-sicherheit/).

## FAQ: Bricksforge: Angreifer nutzen kritische Upload-Lücke ohne Login aus

### Was ist Bricksforge?

Bricksforge ist eine kostenpflichtige Erweiterung für den WordPress-Page-Builder Bricks. Das Plugin ergänzt unter anderem Formulare (Pro Forms), Animationen, einen E-Mail-Designer und eigene Backend-Seiten. Entwickelt wird Bricksforge in Saarbrücken, Patchstack zählt rund 6.000 aktive Installationen.

### Welche Bricksforge-Versionen sind von CVE-2026-85097 betroffen?

Anfällig sind alle Versionen bis einschließlich 3.1.8.9. Patchstack nennt 3.1.8.10 als korrigierte Fassung, im Changelog des Herstellers steht die Reparatur des Datei-Uploads unter Version 4.0.1 vom 8. Oktober 2026. Betreiber sollten auf 4.0.1 aktualisieren.

### Was ist eine Polyglott-Datei?

Eine Polyglott-Datei ist zugleich in zwei Formaten gültig, etwa als GIF-Bild und als PHP-Skript. Eine Prüfung des Dateityps erkennt nur das Bild und lässt die Datei passieren. Landet der Inhalt später unter einer PHP-Endung auf dem Server, führt PHP den eingebetteten Code aus.

### Wie verhindert man die Ausführung von PHP im Upload-Ordner?

Auf Apache-Servern sperrt eine passende .htaccess-Datei im Ordner wp-content/uploads den Aufruf von PHP-Dateien. Nginx wertet .htaccess nicht aus, dort übernimmt eine Regel in der Serverkonfiguration diese Aufgabe. Bilder, PDFs und andere Medien bleiben weiterhin abrufbar.

### Woran erkenne ich, ob meine Website angegriffen wurde?

Verdächtig sind PHP-Dateien im Upload-Ordner, besonders im temporären Bricksforge-Verzeichnis oder mit Namen ab login\_admin, sowie unbekannte Administratorkonten. Patchstack rät außerdem, die Server-Logs auf auffällige Formular-Übermittlungen seit dem 7. Oktober 2026 zu prüfen.

### Quellen

## 8 Quellen anzeigenQuellen ausblenden

1. Patchstack[Critical Unauthenticated Arbitrary File Upload Vulnerability Exploited in Bricksforge Plugin](https://patchstack.com/articles/critical-unauthenticated-arbitrary-file-upload-vulnerability-exploited-in-bricksforge-plugin/)
2. WordPress Developer Resources[Nonces](https://developer.wordpress.org/apis/security/nonces/)
3. Bricksforge[Changelog, Version 4.0.1 vom 8. Oktober 2026](https://bricksforge.io/version-changelog/)
4. Patchstack[Bricksforge, Verlauf der Sicherheitslücken](https://patchstack.com/database/wordpress/plugin/bricksforge)
5. Bricksforge[Impressum](https://bricksforge.io/legal-notice/)
6. EUR-Lex[Verordnung (EU) 2024/2847 (Cyber Resilience Act), Art. 14](https://eur-lex.europa.eu/eli/reg/2024/2847/oj)
7. Bricksforge[Preise und Lizenzen](https://bricksforge.io/pricing/)
8. EUR-Lex[Verordnung (EU) 2016/679 (DSGVO), Art. 33](https://eur-lex.europa.eu/eli/reg/2016/679/oj?locale=de)
