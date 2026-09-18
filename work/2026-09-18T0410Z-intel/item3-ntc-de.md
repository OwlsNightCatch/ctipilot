---
title: Cybersicherheit von Photovoltaikanlagen
author: Team NTC
url: https://www.ntc.swiss/aktuelles/cybersicherheit-von-photovoltaikanlagen
hostname: ntc.swiss
description: Die Cybersicherheit von Photovoltaikanlagen in der Schweiz ist gefährdet. Eine Analyse zeigt kritische Schwachstellen und Energiemanagementsystemen.
sitename: Nationales Testinstitut für Cybersicherheit | NTC
date: "2026-09-17"
---
# Cybersicherheit von Photovoltaikanlagen

Systemrelevante Photovoltaikanlagen: Umfassende Cybersicherheitsanalyse mit konkreten Empfehlungen

Eine umfassende Analyse des Nationalen Testinstituts für Cybersicherheit NTC zeigt, dass die wachsende Photovoltaik-Flotte der Schweiz eine unterschätzte Angriffsfläche für das Stromnetz darstellt. Geprüft wurden sieben Wechselrichter und vier Energiemanagementsysteme von acht Herstellern – Geräte, wie sie in Tausenden Schweizer Häusern verbaut sind. Dabei konnten über 50 Befunde identifiziert werden, darunter sieben kritische und sechs hohe. Die Befunde wurden den Herstellern vertraulich gemeldet. Die meisten reagierten rasch, während die Behebung der Schwachstellen bei einigen Produkten noch im Gange ist.

Wie konkret dieses Risiko ist, zeigt ein reales Muster aus der Untersuchung: Bei nahezu allen geprüften Wechselrichtern lässt sich über die lokale Steuerschnittstelle ohne Anmeldung verändern, wie viel Leistung die Anlage einspeist – bis hinunter auf null. Für sich genommen betrifft das nur eine einzelne Anlage. Kontrolliert ein Angreifer jedoch die Cloud eines Herstellers, kann er dieselbe Manipulation gleichzeitig bei Tausenden angebundenen Anlagen auslösen. Die einzelne Solaranlage auf dem Hausdach ist für das Netz bedeutungslos – der Bestand als Ganzes ist kritische Infrastruktur.

So entsteht eine gefährliche Verschiebung: Was früher physischen Zugang zu einem Kraftwerk erforderte, ist heute über einen zentralen Fernzugang möglich. Das grösste Risiko lässt sich nicht durch bessere Produktsicherheit allein beheben – es entsteht aus der Anbindung Tausender Anlagen an wenige Herstellerclouds.

Ergebnisse der Sicherheitsanalyse und zentrale Risikomuster

Um das Sicherheitsniveau der in der Schweiz verbreiteten Photovoltaik-Technik zu beurteilen, hat das NTC über rund ein Jahr elf digitale Produkte von acht Herstellern einer umfassenden technischen Sicherheitsanalyse unterzogen: sieben Wechselrichter und vier Energiemanagementsysteme.

Insgesamt ergaben die Prüfungen über 50 Befunde, sieben davon kritisch und sechs hoch. Fünf der elf Produkte wiesen mindestens einen hohen oder kritischen Befund auf, bei vier Produkten erlangte das NTC die vollständige Kontrolle über das Gerät. Der öffentliche Bericht verzichtet bewusst auf Produktnamen und technische Details. Stattdessen beschreibt er typische Risikomuster:

- Mängel bei Authentifizierung und Zugriffskontrolle, etwa Standardpasswörter

- unsichere Wartungszugänge, etwa mit identischen Zugangsdaten für die ganze Geräteflotte

- fehlende oder schwache Verschlüsselung der Kommunikation über lokale Schnittstellen

- Schnittstellen, die sich nicht deaktivieren lassen

Das Sicherheitsniveau der einzelnen Produkte unterscheidet sich dabei nicht wesentlich von dem anderer weitverbreiteter vernetzter Geräte. Das eigentliche Risiko für das Schweizer Stromnetz liegt nicht im einzelnen Gerät, sondern in der Abhängigkeit von wenigen Herstellern: Über deren Cloud-Infrastruktur werden die Anlagen gesteuert und mit Firmware versorgt, und die meisten Hersteller behalten einen privilegierten Wartungszugang zum gesamten Gerätebestand.


Empfehlungen zur Risikominimierung

Der Bericht leitet daraus Empfehlungen für fünf Adressatengruppen ab:

Eine einfache und vollständige Lösung gibt es nicht; alle Ansätze haben Vor- und Nachteile, und Restrisiken bleiben. Der Bericht versteht sich dabei nicht als Argument gegen die Photovoltaik, sondern als Grundlage für ihren sicheren Ausbau.

Die Untersuchung erfolgte aus eigener Initiative des Nationalen Testinstituts für Cybersicherheit NTC, das dafür das Prüfteam stellte und einen wesentlichen Teil der Mittel trug. Unterstützt wurde sie von mehreren Organisationen, mehrheitlich aus der Energiebranche, sowie von EnergieSchweiz – das NTC dankt ihnen für ihren Beitrag. Um die Unabhängigkeit der Resultate zu gewährleisten, waren die Hersteller der geprüften Produkte weder an der Auswahl noch an der Durchführung der Tests beteiligt und wurden erst im Rahmen der vertraulichen Schwachstellenmeldung kontaktiert.

###### *Der summarischer Bericht ist in Deutsch, Französisch, Italienisch und Englisch verfügbar.*

              
            
              
                ###### Medienbeobachtung


Die Veröffentlichung des Berichts zur Cybersicherheit von Photovoltaikanlagen wurde in den Medien aufgegriffen. Nachfolgend eine nicht abschliessende Auflistung einiger Artikel:

              
            
              
                - **SRF, 16. September 2026:** Sicherheitsexperten: Blackout-Risiko wegen Solaranlagen[Zum SRF Artikel](https://www.srf.ch/news/schweiz/risiko-cyberangriffe-sicherheitsexperten-blackout-risiko-wegen-solaranlagen)
