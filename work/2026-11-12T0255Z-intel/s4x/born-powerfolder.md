---
title: Sicherheitsvorfall beim Anbieter PowerFolder Drive
author: Christian Krause
url: https://borncity.com/blog/2026/11/09/sicherheitsvorfall-beim-anbieter-powerfolder-drive/
hostname: borncity.com
description: Ein Blog-Leser hat mich zum 9. November 2026 darüber informiert, dass es einen Sicherheitsvorfall beim Anbieter PowerFolder Drive gegeben habe. Er wurde als Kunde informiert, und der Cloud-Anbieter…
sitename: Borns IT- und Windows-Blog
date: "2026-11-09"
categories: ['Cloud', 'Sicherheit']
tags: ['Cloud', 'Sicherheit']
fingerprint: "7580df2f6fffcadd"
---
Ein Blog-Leser hat mich zum 9. November 2026 darüber informiert, dass es einen Sicherheitsvorfall beim Anbieter PowerFolder Drive gegeben habe. Er wurde als Kunde informiert, und der Cloud-Anbieter hat zum 6. November 2026 seine Cloud-Dienste deaktiviert. Hier einige Informationen, was bekannt ist.


## Wer ist PowerFolder Drive?

Mir sagte der Namen nichts, aber im Internet habe ich die Information gefunden, dass [PowerFolder Drive](https://www.powerfolder.com/) eine unternehmensorientierte Cloud- und File-Sync-&-Share-Lösung für Datenaustausch, Synchronisation und Backup aus Deutschland sei. Hinter dem Dienst stehe die dal33t GmbH (ursprünglich 2010 in Düsseldorf gegründet, heute mit Sitz in Monheim am Rhein).

Im September 2022 hat PowerFolder die frühere Cloud-Lösung TERRA Drive von der Wortmann AG übernommen und firmierte diese zum heutigen PowerFolder Drive um. Der Anbieter wirbt damit, 100 % DSGVO-konform, ISO 27001- und BSI IT-Grundschutz-zertifiziert sowie frei vom US CLOUD Act. zu sein. Das Hosting erfolgt in Deutschland (u. a. über Rechenzentren der Wortmann TERRA-Cloud).

## Der Sicherheitsvorfall vom 6.11.2026

Blog-Leser Mario H. hat mich zum 9. November 2026 darüber informiert, dass er per E-Mail über einen Cybervorfall bei PowerFolder Drive in Kenntnis gesetzt wurde (danke dafür). Zum 6. November 2026, also an einem Freitag, hat sich der Worst-Case für diesen Anbieter ergeben. Ein externer Angreifer hat laut [einer Mitteilung](https://mailchi.mp/6b5918655086/powerfolder-281-ki-fr-ihre-dokumente-mehr-die-news-im-oktober-16588680) am 6. November 2026 mehrere bis dahin unbekannte Schwachstellen in der Software dieses Anbieters ausgenutzt.

Das Unternehmen gibt an, den Angriff noch am selben Tag erkannt und alle betroffenen Systeme innerhalb von rund 30 Minuten vom Netz genommen zu haben. Seitdem sind die Cloud-Dienste außer Betrieb, heißt es in der betreffenden Mitteilung.

Der Angreifer hatte es gezielt auf einzelne Systemdateien der Server (Konfiguration) abgesehen, heißt es in der Mitteilung. Für einen Zugriff auf die gespeicherten Dateien und Ordner haben die Leute des Anbieters keine Anhaltspunkte gefunden.

Alle Passwörter speichere man nur als Hash. Vorsorglich behandelt der Anbieter aber alle Cloud-Konten als betroffen: Beim Neustart muss jede Nutzerin und jeder Nutzer ein neues Passwort zur Anmeldung vergeben.

Laut Anbieter wurden keine Daten verschlüsselt und es habe auch keine Lösegeldforderung gegeben. Die Abschaltung der Cloud-Dienste sei zur Beweissicherung und forensische Auswertung erfolgt.

Der Anbieter hat eine Meldung an die Datenschutzaufsicht (LDI NRW) und das BSI geschickt, sowie Strafanzeige gestellt. Derzeit werden wohl Sicherheitsupdate vorbereitet, alle Systeme neu aufgebaut und sämtliche Zugangsdaten und Schlüssel ausgetauscht.

## Was passiert, was wird empfohlen?

PowerFolder Drive geht erst wieder online, schreibt der Anbieter, wenn alle Tests bestanden sind. Nach aktuellem Stand steht PowerFolder Drive voraussichtlich im Laufe des 10. November 2026 wieder zur Verfügung. Eine Schritt-für-Schritt-Anleitung für Nutzer will man rechtzeitig vorab bereitstellen (aktuelle Informationen auf der [News-Seite](https://www.powerfolder.com/news)).

Für Kunden wird empfohlen, falls das PowerFolder-Passwort auch anderswo verwendet wurde, dies dort jetzt ändern. Zudem sollen Kunden auf Phishing achten (PowerFolder fragt niemals per E-Mail nach Passwörtern). Und PowerFolder-Clients sollen bis zum Neustart nicht deinstalliert und lokale Ordner nicht gelöscht werden.

Mehrere Dinge:

\> "Ein externer Angreifer hat am 6. November 2026 mehrere bis dahin unbekannte Schwachstellen in unserer Software ausgenutzt"

Ja, der Satz ist aber Bullshit wenn die Lösung weiter unten aus …

\> "Sicherheitsupdate, Neuaufbau aller Systeme, Austausch sämtlicher Zugangsdaten und Schlüssel."

.. bestand. Dann waren das mitnichten "unbekannte Schwachstellen". Dann ist Euer Patch-Management kacke!

\> "Der Angreifer hatte es gezielt auf einzelne Systemdateien…"

Ja das machen Angreifer zur Persistenzerlangung oder lateralen Fortbewegung und für andere Dinge weiter unten. Das ist weder gezielt noch sonderlich bemerkenswert sondern solides Hackerhandwerk.

\> "Alle Passwörter speichere man nur als Hash"

Was der größte Bullshit ist! Dann hätte man in Zeiten von leistungsstarken GPUs und Rainbow Tables diese gleich auch als Klartext in der Datenbank belassen können, wenn da nur mit SHA und einem statischen Passwort aus einer Systemdatei (!?!) was gehasht wurde. Stand der Technik (seit 15 Jahren) sind zusätzliche Salts, die an jedem Datensatz entweder als Feld mithängen bzw. aus festen Feldwerten eines Datensatzes (z.B. dem Index oder einem Erstelldatum) generiert werden (und somit kein extra Feld benötigen).

\> "Beim Neustart muss jede Nutzerin und jeder Nutzer ein neues Passwort zur Anmeldung vergeben."

Ja weil Hashes alleine Murcks sind! Das wissen die selbst. Warum dann diese geframten Geschichten?

\> "Die Abschaltung der Cloud-Dienste sei zur Beweissicherung und forensische Auswertung erfolgt."

Dazu reichen Logs und Snapshots der ohnehin in der Terra-Cloud virtualisierten Systeme. Die gepatchten Systeme selbst können nach kurzer Zeit weiterlaufen. Wenn nach Tagen immer noch ausgeschaltete Systeme vorliegen, ist diese Behauptung entweder nicht glaubhaft, deren Lösung handwerklich schlecht (nicht hinreichend automatisiert) betrieben oder es wurde nicht nur gepatched sondern auch was Neues angeflansht, was die Aussage mit den Tests bestätigen könnte. Vermutlich eine Kombination aus allen drei Dingen.

Das wirft gleich Folgefragen wie deren Notfalpläne, Change-Management und generell das Verständnis nach Informationssicherheit aussieht.

Und wieder ein Unternehmen, das nicht vollumfänglich und nicht offen mit seinen Sicherheitsvorfällen kommuniziert und seine Kundschaft und Sicherheit nicht für Ernst nimmt.

Hallo,

zum Thema Hashes hier etwas aufbereitet:

https://www.msxfaq.de/windows/sicherheit/hashwertsicherheit.htm

Grüße 🙋♂️

Hallo,

zum Thema Hashes hier etwas aufbereitet:

https://www.msxfaq.de/windows/sicherheit/hashwertsicherheit.htm

Grüße 🙋♂️

Die scheinen keinen terraXaler zu haben.

Oder der terraXaler ist nicht so gut wie von Wortmann propagiert. ;)

Terra macht auch nur das, was ein Kunde sich wünscht…

Muss beim Betrachten der terraXaler Website trotzdem schmunzeln:

"hochverfügbar" und "Windows 2025" sollte man besser nicht in einem Satz nennen, selbst dann, wenn man es nach Lehrbuch mit HyperV redundant auslegt.

2 Nodes sind noch kein Cluster… der Spaß beginnt ab 3 Nodes und CEPHs aufwärts…
