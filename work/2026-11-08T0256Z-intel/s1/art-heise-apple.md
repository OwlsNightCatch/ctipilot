---
title: "macOS 27.3: Apple behebt letztes eMudhra-Leck – aber es wird dauern"
author: Heise Online; Ben Schwan
url: https://www.heise.de/news/macOS-27-3-Apple-behebt-letztes-eMudhra-Leck-aber-es-wird-dauern-11513443.html
hostname: heise.de
description: Safari und andere Browser auf dem Mac sind vor dem schweren TLS-Sicherheitsproblem zwar sicher, das Terminal aber nur mit Handarbeit. Apple hilft verspätet.
sitename: Heise Online
date: "2026-11-06"
categories: ['IT']
tags: ['Apple, IT, Mobiles, Security, TLS, eMudhra, macOS, macOS 27.3']
fingerprint: ef90699c7a2ff35b
---
# macOS 27.3: Apple behebt letztes eMudhra-Leck – aber es wird dauern

Safari und andere Browser auf dem Mac sind vor dem schweren TLS-Sicherheitsproblem zwar sicher, das Terminal aber nur mit Handarbeit. Apple hilft verspätet.

Nach wie vor muss man händisch tätig werden, will man seinen Mac vollständig gegen einen [massiven Sicherheitsvorfall bei der indisch-europäischen Zertifizierungsstelle eMudhra](https://www.heise.de/news/Vorfall-bei-Zertifizierungsstelle-eMudhra-Acht-CA-Zertifikate-kompromittiert-11494412.html) abdichten. Und das dürfte noch eine ganze Weile so bleiben: Erst mit macOS 27.3, das in dieser Woche in den Betatest durch Entwickler gegangen ist, wird das Problem abgestellt. Wieso Apple hier so langsam vorgeht, bleibt unklar.

### Fix verschwindet gegebenenfalls wieder

Der Konzern [liefert zwar eine Anleitung](https://www.heise.de/news/eMudhra-TLS-Leck-Apple-laesst-Problem-auf-macOS-Kommandozeile-zunaechst-bestehen-11500945.html), wie sich Nutzer vorab behelfen können, doch wurde die Wirksamkeit dieses Workarounds erstaunlicherweise durch das Aufspielen des [macOS-27.2-Updates](https://www.heise.de/news/Sicherheit-Apple-stopft-wieder-viele-Loecher-auch-fuer-aeltere-Betriebssysteme-11501091.html) (das selbst keinen Fix mitbrachte) wieder entfernt. Heißt: Wer Apples Methodik vor der Aktualisierung auf macOS 27.2 angewendet hat, muss sie wiederholen. Oder er oder sie warten bis macOS 27.3, doch das braucht mit Sicherheit noch mindestens bis Dezember.

Die eMudhra-Lücke erlaubt es, auf ungepatchten Maschinen gefälschte TLS-Zertifikate zu nutzen, da bei der Firma CA-Zertifikate samt privater Schlüssel kompromittiert worden waren. Die Zertifizierungsstelle hatte extrem schlechte Sicherheitspraxis walten lassen, Schlüssel bestanden zum Teil nur aus einer einzigen Zahl. Während Browser-Hersteller inklusive Apple mit Safari das Problem über Updates ihrer CA-Listen behoben (prüfbar [etwa hier](https://emudhra.we-have-a-problem.com/)), gilt das für macOS-Terminal-Werkzeuge nicht. Nutzer von beliebten Tools wie `git`, `curl`, `python3` oder `openssl` nutzen bis heute eine veraltete Version von `/etc/ssl/cert.pem`, die die Angriffe weiter zulässt. So kann nicht sichergestellt werden, ob man etwa mit `curl` Code von einer bösen Website herunterlädt.

### Es könnte Wochen dauern

Wie Nutzer der macOS-27.3-Developer-Beta nun melden, hat Apple `/etc/ssl/cert.pem` mit dem Update endlich getauscht. Schwierig ist nun, dass der Konzern offenbar nicht vorhat, diesen sehr simplen Patch vor Veröffentlichung der Finalversion von macOS 27.2 herauszubringen. Dabei gibt es genau hierfür Mechanismen, mit denen Apple für macOS sogenannte Security Responses schnell verteilen und installieren kann.

Offenbar nimmt das Unternehmen an, dass es vergleichsweise wenig Betroffene gibt. Allerdings setzt [der Trend zu Vibe-Coding](https://www.heise.de/ratgeber/Vibe-Coding-am-Mac-So-legen-Sie-los-11475065.html) und lokaler KI stark auf die Kommandozeile – wo man dann genau in diese Sicherheitslücke rennt. Die Anleitung von Apple, wie man das Problem selbst beheben kann – die entsprechenden Zertifizierungsstellen werden aus `cert.pem` gelöscht – findet sich inzwischen [auch in deutscher Sprache](https://support.apple.com/de-de/149555) hier.

## Empfohlener redaktioneller Inhalt

Mit Ihrer Zustimmung wird hier ein externer Preisvergleich (heise Preisvergleich) geladen.

Ich bin damit einverstanden, dass mir externe Inhalte angezeigt werden.
    Damit können personenbezogene Daten an Drittplattformen (heise Preisvergleich) übermittelt werden.
    Mehr dazu in unserer
    [Datenschutzerklärung](https://www.heise.de/Datenschutzerklaerung-der-Heise-Medien-GmbH-Co-KG-4860.html).

([bsc](mailto:bsc@heise.de))
