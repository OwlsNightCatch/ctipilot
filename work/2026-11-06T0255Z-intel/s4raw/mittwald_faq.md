---
title: "MCP-Server: Was du jetzt wissen musst | mittwald"
url: https://www.mittwald.de/lp/mcp-faq
hostname: mittwald.de
description: "Unbefugter Zugriff auf unseren MCP-Server: Wir beantworten deine Fragen zu betroffenen Tokens, deinen Projekten und den nächsten Schritten."
sitename: Mittwald - Webtechnologie Für Agenturen
date: "2026-11-05"
fingerprint: b49bcf0e8d99c786
---
## Informationen zu unserem 

MCP-Server

## Updates

Stand 05.11.2026 – 21:00 Uhr

#### Update – 05.11.2026 · 21:00 CET

Wir arbeiten weiter mit Hochdruck an der Analyse. Unsere Scans und Maßnahmen laufen und wir kommen gut voran. Neue Erkenntnisse gibt es im Moment noch nicht. Sobald sich etwas Wesentliches tut, informieren wir dich hier sofort.

**Für Agenturen:** Für deine Kunden haben wir ein Formulierungshilfen mit den wichtigsten Infos vorbereitet. Du kannst es direkt weiterleiten und sparst dir so viele Einzelanfragen.

### Historie

Wir haben im Zuge der Sicherheitsmaßnahmen den Zugang von Kunden aus dem Kundencenter, die unseren AV Manager nutzen, vorübergehend gesperrt.

Solange die Sperre aktiv ist, kannst Du Dich nicht im Kundencenter einloggen und den AV-Manager nicht nutzen.

Wichtig: Deine Projekte sind davon **nicht** betroffen. Die Sperre gilt nur für Deinen Zugang. Alle Deine Webseiten laufen ganz normal weiter.

Unsere Analysen haben einen ubefugten Zugriff auf das mStudio über unseren MCP-Server festgestellt. Wir arbeiten mit Hochdruck an der Analyse und daran, die Folgen des Vorfalls zu beheben.

Zu Deinem Schutz sind vorübergehend einige Funktionen deaktiviert:

- MCP-Server
- Login ins mStudio
- SSH-Zugriff
- mittwald Extensions
- Bestellungen

Das ist eine reine Vorsichtsmaßnahme. Sobald alles wieder läuft, geben wir Dir Bescheid.

Wir haben im Zuge unserer Vorsichtsmaßnahmen einen geringen Teil der Projekte deaktiviert.

Solltest du davon betroffen sein, hast du von uns eine Mail erhalten.

Wir haben uns dazu entschieden, den mStudio Login, SSH-Verbindungen sowie alle mittwald Extensions zu deaktivieren.

Dies ist eine vorsorgliche Sicherheitsmaßnahme, da wir zum aktuellen Zeitpunkt nicht ausschließen können, dass noch ein unberechtigter Zugriff auf unsere Systeme möglich ist.

Wir haben bereits alle notwendigen Überprüfungen eingeleitet und ergreifen situationsabhängig alle Maßnahmen, um die Sicherheit der bei uns gehosteten Projekte sicherzustellen.

Die bei uns gehosteten Projekte und E-Mails sind derzeit erreichbar.

Wir informieren an dieser Stelle so regelmäßig wie möglich über Neuigkeiten.

Wir haben uns dazu entschieden den mStudio Login zu deaktivieren und alle SSH-Verbindungen zu beenden & deaktivieren.

Ebenfalls sind die mittwald-Extensions deaktiviert.

## Für alle Kunden

Am 04.11.2026 haben wir durch eigene Analysen festgestellt, dass es am 27.10.2026 einen unbefugten Zugriff auf unseren MCP-Server gab. Der MCP-Server ist eine Schnittstelle, über die Kunden ihr mStudio mit KI-Assistenten verbinden konnten. Dabei wurden Zugangsdaten (Tokens) von Nutzern dieser Schnittstelle ausgelesen.

Nur, wenn du den MCP-Server genutzt hast. Alle Betroffenen erhalten eine persönliche E-Mail von uns. Wenn du keine E-Mail bekommen hast und den MCP-Server nie eingerichtet hast, bist du nach aktuellem Stand nicht betroffen.

Nein. Dein mStudio-Zugang, deine Projekte und deine Daten sind nach aktuellem Stand nicht betroffen. Wir empfehlen unabhängig davon, Zwei-Faktor-Authentifizierung zu aktivieren.

Nein. Es wurden keine Passwörter ausgelesen, sondern Sitzungs-Tokens. Diese Tokens wurden alle widerrufen und sind nicht mehr gültig.

Wir haben keine Hinweise darauf. Eine Prüfung einschlägiger Plattformen hat keine veröffentlichten Daten ergeben. Wir prüfen das weiterhin.

Nein. Der MCP-Server ist abgeschaltet und bleibt bis auf Weiteres offline. Ob und in welcher Form wir die Schnittstelle wieder anbieten, entscheiden wir nach Abschluss der Untersuchung. Das mittwald CLI kann alternativ genutzt werden.

Unsere Prüfungen laufen noch. Deshalb können wir dir aktuell keinen verlässlichen Zeitpunkt nennen, ab dem das mStudio und deine Webprojekte wieder verfügbar sind. Sobald wir mehr wissen, informieren wir dich auf unserer Statusseite und per E-Mail.

Nein, ein Umzug ist im Moment leider nicht möglich. Dafür bitten wir dich um Verständnis. Auch Sonderlösungen für einzelne Projekte können wir gerade nicht anbieten. Unsere oberste Priorität ist, alle Projekte so schnell und so sicher wie möglich wieder freizuschalten.

Der Angreifer hat seine Vorbereitungen gezielt getarnt. Er hat dafür Aktionen genutzt, die wie ganz normales Nutzerverhalten aussahen. Als wir die verdächtigen Aktivitäten erkannt haben, haben wir sofort reagiert und Gegenmaßnahmen eingeleitet.

Ja, die SSH-Sperre bleibt vorerst aktiv. Wir heben sie auf, sobald unsere Prüfungen und Scans abgeschlossen sind und wir alle nötigen Maßnahmen umgesetzt haben. Den Zeitpunkt geben wir auf unserer Statusseite bekannt und informieren dich zusätzlich per E-Mail.

Nach aktuellem Stand nicht. Wir kümmern uns um alle nötigen Schritte, damit deine Projekte sicher sind. Falls wir dir doch konkrete Maßnahmen empfehlen, melden wir uns direkt bei dir.

Wir schalten jedes Projekt einzeln frei, sobald der Sicherheitsscan dafür abgeschlossen ist. So stellen wir sicher, dass jedes Projekt mit der gleichen Sorgfalt geprüft wird.

Wenn wir Hinweise darauf haben, dass Daten aus deinen Projekten abgerufen wurden, informieren wir dich persönlich und direkt. Hast du keine solche Nachricht von uns erhalten, liegen uns für deine Projekte aktuell keine Hinweise auf einen Zugriff vor.

Die Lücke lag in unserem MCP-Server. Sobald wir davon wussten, haben wir den Server vom Netz genommen, den Vorfall vollständig analysiert und die Lücke geschlossen. Die Prüfung aller Projekte läuft aber weiterhin.

Intern halten wir unsere Learnings bereits fest. Da unsere Analysen und Maßnahmen noch laufen, werden weitere dazukommen. Sobald wir ein vollständiges Bild haben, teilen wir unsere Learnings offen und transparent mit dir.

## Für betroffene MCP-Nutzer

Am 04.11.2026 haben wir durch eigene Analysen festgestellt, dass es am 27.10.2026 einen unbefugten Zugriff auf unseren MCP-Server gab. Der MCP-Server ist eine Schnittstelle, über die Kunden ihr mStudio mit KI-Assistenten verbinden konnten. Dabei wurden Zugangsdaten (Tokens) von Nutzern dieser Schnittstelle ausgelesen.

Das Token erlaubte Zugriff auf dein mStudio mit deinen Rechten. Der Angreifer konnte damit auf Projekte zugreifen, auf die du Zugriff hattest. Wir prüfen aktuell jedes betroffene Projekt einzeln.

Wir scannen alle Projekte, auf die mit entwendeten Tokens zugegriffen werden konnte, auf Spuren des Angreifers. Projekte mit Spuren stellen wir vorübergehend ab. Du bekommst von uns Bescheid.

1. Passwort in mStudio ändern.
2. Zwei-Faktor-Authentifizierung aktivieren.
3. API-Keys, Project Tokens und SSH-Keys in deinen Projekten prüfen und unbekannte Einträge löschen. Achte auf SSH-User, die du nicht angelegt hast.
4. Zugangsdaten von Drittdiensten, die du in deinen Projekten hinterlegt hast (Datenbanken, Mail, externe APIs), erneuern.
5. Deine Nutzer im Projekt informieren.

Wir melden uns bei dir sollten wir Auffälligkeiten in den Scans feststellen. Verdächtig sind SSH-User, die du nicht kennst, unbekannte Dateien im Projektverzeichnis und API-Keys, die du nicht angelegt hast. Wenn dir etwas auffällt, wende dich an unseren Kundenservice.

Wenn wir ein Backup einspielen, besprechen wir mit dir, welche Änderungen seit dem 27.10. du übernehmen willst. Nichts passiert ohne Rücksprache.

Der Server war ab dem 27.10. übernommen. Jede Nutzung danach gilt als potenziell kompromittiert. Bitte führe alle Schritte unter „Was muss ich jetzt tun?“ durch.

Im Zuge der ersten Gegenmaßnahmen haben wir vorsorglich API-Keys gesperrt.
