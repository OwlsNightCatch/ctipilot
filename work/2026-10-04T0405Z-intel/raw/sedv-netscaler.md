---
title: "Citrix NetScaler: Abstürze trotz Patch, SAML-Problem…"
author: Marcel Schönfelder
url: https://s-edv.com/news/citrix-netscaler-saml-abstuerze-nach-notfall-patch
hostname: s-edv.com
description: Gepatchte NetScaler-Appliances mit SAML stürzen unter Angriffen ab. Citrix untersucht, Patch fehlt. Wer betroffen ist und was Admins jetzt prüfen sollten.
sitename: Schönfelder EDV News
date: "2026-10-04"
categories: ['Sicherheit & Datenschutz']
tags: ['Citrix', 'NetScaler', 'SAML', 'Zero-Day', 'Gateway', 'Sicherheitslücke']
---
[← Alle News](https://s-edv.com/news)

# Citrix NetScaler: Abstürze trotz Notfall-Patch, Citrix untersucht SAML-Problem

Eine Woche nach dem Notfall-Update vom 27.09.2026 melden Admins und Forscher Abstürze und Neustarts voll gepatchter NetScaler ADC und Gateway-Instanzen. Citrix untersucht ein neues Problem bei der SAML-Authentifizierung kundenverwalteter Installationen und nennt zwei Konfigurationsbefehle als Prüfmerkmal. Einen Patch gibt es noch nicht.

Eine Woche nach dem Notfall-Patch für NetScaler ADC und NetScaler Gateway gibt es neue Probleme: Administratoren und Sicherheitsforscher melden seit dem Abend des 2. Oktober 2026 wiederholte Abstürze und erzwungene Neustarts von Appliances, die bereits auf dem neuesten Stand 14.1-73.37 beziehungsweise 13.1 waren. Citrix bestätigt in einem Blogbeitrag vom 2. Oktober, dass die Entwicklungs- und Supportteams ein neu festgestelltes Problem bei der SAML-Authentifizierung in kundenverwalteten NetScaler-Instanzen untersuchen. Ein Patch ist bislang nicht verfügbar. Hintergrund zum Patch vom 27.09.2026 liefert unser Beitrag zu den [Zero-Days CVE-2026-88771 und CVE-2026-88772](https://s-edv.com/news/citrix-netscaler-zero-days-cve-2026-88771-88772-aktiv-ausgenutzt).

Betroffen sind nach Herstellerangaben nur Installationen, die SAML-Authentifizierung zusammen mit Gateway- oder AAA-Funktionen nutzen. NetScaler-Instanzen ohne SAML-Konfiguration sind nach derzeitigem Stand nicht betroffen. Citrix spricht ausdrücklich von kundenverwalteten Bereitstellungen. Wer extern erreichbare Gateways mit SAML betreibt, sollte die Konfiguration noch heute prüfen und die Geräte eng überwachen. Auf ein Wartungsfenster zu warten, ist nicht angemessen.

## Was ist passiert?

Laut heise kursiert seit den Abendstunden des 2. Oktober offenbar ein Exploit für eine neue Schwachstelle in NetScaler. Sicherheitsforscher Kevin Beaumont berichtet, dass seine gepatchten Honeypots mit Firmware 13.1 und 14.1 abstürzen und die Auslöser von mehreren Quell-IP-Adressen kommen. Auf einem Honeypot sei eine heruntergeladene Binärdatei ausgeführt worden. Beaumont hält eine neue Lücke oder eine Umgehung der Fehlerbehebung für CVE-2026-88771 und CVE-2026-88772 für wahrscheinlich, schreibt aber selbst, dass dies noch zu bestätigen sei. Nach Angaben von heise hat das Team von watchTowr Labs die Schwachstelle inzwischen reproduziert.

Ein IT-Dienstleister berichtet laut Borns IT-Blog auf Reddit, dass mehrere Kunden ihre externen Appliances auf 14.1-73.37 wiederholt neu starten müssten. Born gibt zudem einen Bericht von The Hacker News wieder, wonach die Ausfälle mit manipulierten SAML-Authentifizierungsdaten zusammenhängen, die den Dienst `nsaaad` zum Absturz bringen. heise zufolge lässt sich der Exploit wohl über den massenhaften Versand von SAML-Anfragen auslösen.

Citrix hat am 2. Oktober den Beitrag „Security Update: Guidance for NetScaler SAML Authentication Deployments“ veröffentlicht. Laut heise nennt der Hersteller darin weder Gegenmaßnahmen noch einen Patch, Betroffene sollen sich an den Support wenden. Ein Sicherheitshinweis und eine Fehlerbehebung sollen folgen. Eine CVE-Nummer für das neue Problem ist bislang nicht bekannt. Die Herstellerseite war bei unserer Prüfung hinter einer Bot-Schutzseite nicht abrufbar, die Angaben stammen aus den Wiedergaben von heise und Borns IT-Blog.

## Wer ist betroffen?

Nach den bisher vorliegenden Informationen ist das Problem konfigurationsabhängig. Laut Citrix betrifft es kundenverwaltete NetScaler-Instanzen, die als virtueller Gateway- oder AAA-Server mit SAML-Authentifizierung arbeiten. Eine Appliance gilt als betroffen, wenn mindestens einer dieser Befehle in der Konfiguration steht:

- `add authentication samlAction` , also NetScaler als SAML-Service-Provider gegenüber einem externen Identity Provider
- `add authentication samlIdPProfile` , also NetScaler selbst als SAML-Identity-Provider

Die Absturzberichte betreffen Geräte mit installiertem Notfall-Update vom 27.09.2026, der Patchstand allein schützt also nicht. Eine Liste betroffener Builds hat Citrix noch nicht veröffentlicht.

## Wie kritisch ist das?

Gesichert ist bisher ein Ausfallrisiko: Gepatchte Appliances mit SAML stürzen nach übereinstimmenden Berichten unter gezielten Anfragen ab und starten neu. Deutlich ernster ist der Hinweis auf Codeausführung. Er stützt sich auf eine Honeypot-Beobachtung und die Reproduktion durch watchTowr, eine Bestätigung durch Citrix steht aus. Weil die Angriffe laut Beaumont breit gestreut erfolgen, sind alle aus dem Internet erreichbaren SAML-Gateways potenziell im Visier.

Die Einordnung lautet daher: Nur relevant für NetScaler-Instanzen mit SAML-Authentifizierung, dort aber akut kritisch und mit Priorität vor dem nächsten Arbeitstag zu behandeln.

## Was sollten Admins jetzt tun?

- Alle NetScaler ADC und Gateway-Instanzen inventarisieren, Build-Stand notieren und in der laufenden Konfiguration nach `add authentication samlAction` und`add authentication samlIdPProfile` suchen. Fundstellen bedeuten Betroffenheit nach Citrix-Kriterium.
- Prüfen, ob das Notfall-Update vom 27.09.2026 auf allen Knoten installiert ist. Es bleibt Pflicht.
- Uptime, Neustartzeitpunkte und Absturzmeldungen der Appliances auswerten. Unerwartete Reboots seit dem 2. Oktober sind ein Warnsignal.
- Bei Auffälligkeiten sofort einen Fall beim Citrix-Support eröffnen, so wie es der Hersteller empfiehlt, und auf den angekündigten Sicherheitshinweis achten.
- Kompromittierung nicht ausschließen: unbekannte Dateien, Prozesse und ausgehende Verbindungen der Appliance sowie Anmeldungen der vergangenen Tage prüfen.
- Für den Ernstfall abwägen, ob SAML-Anmeldung oder der externe Zugang vorübergehend eingeschränkt werden kann. Das ist eine eigene Risikoabwägung, keine Empfehlung von Citrix.

## Einordnung für Unternehmen

Für viele kleine und mittlere Unternehmen ist NetScaler Gateway der zentrale Zugang ins Firmennetz, oft mit SAML-Anbindung an einen Identity Provider. Auf einen Notfall-Patch folgt erneut rasch eine Angriffswelle, während der Hersteller noch untersucht. Wer Gateways von einem Dienstleister betreuen lässt, sollte dort aktiv nach SAML-Status und Neustartprotokollen fragen.

Langfristig gehören Neustarts, Konfigurationsänderungen und ausgehende Verbindungen von Edge-Geräten ins zentrale Monitoring, dazu ein Plan, wie der Remote-Zugang bei Abschaltung des Gateways weiterläuft.

## Passende Anleitungen auf S-EDV

- [Citrix NetScaler: Zwei Zero-Days CVE-2026-88771 und CVE-2026-88772 aktiv ausgenutzt](https://s-edv.com/news/citrix-netscaler-zero-days-cve-2026-88771-88772-aktiv-ausgenutzt) : Notfall-Patch vom 27.09.2026.
- [NetScaler CVE-2026-8451: SAML-Speicherleck nach CitrixBleed-Muster](https://s-edv.com/news/citrix-netscaler-cve-2026-8451-saml-memory-overread-citrixbleed) : frühere SAML-Lücke.
- [CISA-Warnung zu Cisco, Citrix und Fortinet](https://s-edv.com/news/cisa-dreierwarnung-cisco-citrix-fortinet-edge-priorisierung) : Edge-Patches priorisieren.
