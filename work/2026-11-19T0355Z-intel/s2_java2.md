---
title: "Java4Shell: Kritische Schwachstelle in Java - Sicherheits-Updates sofort einspielen"
url: https://www.bacs.admin.ch/de/warnung-java-2-de
hostname: admin.ch
description: Die kritische Schwachstelle «Java4Shell» (CVE-2026-114938) ermöglicht Angreifern, über das Netzwerk Schadcode auf betroffenen Systemen auszuführen, teilweise ohne Anmeldung. Sicherheits-Updates sind verfügbar. Das BACS empfiehlt Betreiberinnen und Betreibern ihre Betroffenheit unverzüglich zu prüfen und betroffene Systeme zu aktualisieren.
sitename: bacs.admin.ch
date: "2026-11-18"
fingerprint: "8d0615f7ec2f5b96"
---
# Java4Shell: Kritische Schwachstelle in Java - Sicherheits-Updates sofort einspielen

**Die kritische Schwachstelle «Java4Shell» (CVE-2026-114938) ermöglicht Angreifern, über das Netzwerk Schadcode auf betroffenen Systemen auszuführen, teilweise ohne Anmeldung. Sicherheits-Updates sind verfügbar. Das BACS empfiehlt Betreiberinnen und Betreibern ihre Betroffenheit unverzüglich zu prüfen und betroffene Systeme zu aktualisieren.**

Java ist eine technische Grundlage vieler Anwendungen und kann auch in Software und Geräten enthalten sein, ohne dass dies den Nutzenden bekannt ist. Die Schwachstelle betrifft die Java-Laufzeit selbst, welche diese Programme ausführt. Beim Verarbeiten speziell präparierter Daten können Angreifer vertrauliche Informationen auslesen, Anwendungen manipulieren oder die Kontrolle über den betroffenen Prozess übernehmen.

## Weit verbreitete und geschäftskritische Anwendungen betroffen

Das Sicherheitsunternehmen Calif hat die Ausführung von Schadcode in verschiedenen Anwendungen demonstriert:

- **Ohne Anmeldung (Pre-Authentication-RCE):** 
Keycloak, Atlassian Jira, Atlassian Confluence, JFrog Artifactory, Jenkins und PingFederate.
- **Mit angemeldetem Zugriff (Post-Authentication-RCE):** 
Apache Kafka Broker, Apache Solr, Elasticsearch, Gerrit und Netflix Spinnaker.

Darunter sind zentrale Anmeldedienste sowie Plattformen für Software-Entwicklung und Software-Bereitstellung. Eine erfolgreiche Ausnutzung kann deshalb auch den Zugriff auf weitere Systeme und sensible Informationen erleichtern.

Die Aufzählung ist nicht abschliessend. Auch weitere Java-Anwendungen, beispielsweise Banken-Software und andere Branchenlösungen, können betroffen sein. Betreiber müssen dies mit ihren Software-Lieferanten klären.

## Welche Systeme müssen geprüft werden?

Die Schwachstelle betrifft bestimmte Java-Versionen auf bestimmten, weit verbreiteten Prozessortypen. Ob ein System angreifbar ist, hängt auch davon ab, wie die Anwendung Daten verarbeitet. Prüfen Sie die konkrete Betroffenheit anhand der Sicherheitsinformationen des jeweiligen Herstellers.

Die Prüfung muss auch Java-Komponenten innerhalb von Anwendungen, Geräten und Containern umfassen. Berücksichtigen Sie neben öffentlich erreichbaren Diensten auch interne Systeme. Laut Calif bestehen zudem Angriffswege gegen Java-Anwendungen, die selbst Verbindungen zu einem bösartigen Server aufbauen.

## Was Betreiberinnen und Betreiber jetzt tun sollten

Priorisieren Sie aus dem Internet erreichbare Anwendungen, zentrale Anmeldedienste und geschäftskritische Systeme.

- **Betroffene Systeme erfassen:** 
Ermitteln Sie, welche Anwendungen und Geräte Java verwenden. Klären Sie mit den Anbietern oder Ihrem IT-Dienstleister, welche davon betroffen sind.
- **Eigene Anwendungen aktualisieren:** 
Wenn Sie Java-Anwendungen selbst entwickeln und betreiben, aktualisieren Sie die dafür verwendete Java-Version unverzüglich.
- **Software und Geräte aktualisieren:** 
Installieren Sie bei eingesetzter Software und Geräten die Sicherheits-Updates des jeweiligen Anbieters. Klären Sie bei Bedarf mit dem Anbieter oder IT-Dienstleister, ob Java zusätzlich separat aktualisiert werden muss. Lassen Sie sich bei extern betriebenen Diensten die Behebung bestätigen.
- **Aktualisierung überprüfen:** 
Starten Sie betroffene Anwendungen und Java-Prozesse nach dem Update neu. Container müssen gegebenenfalls neu erstellt und bereitgestellt werden. Prüfen Sie, ob die laufenden Anwendungen tatsächlich die korrigierte Java-Version verwenden.
- **Falls ein Update noch nicht möglich ist:** 
Setzen Sie die dokumentierten Übergangsmassnahmen in Abstimmung mit dem Anbieter oder Ihrem IT-Dienstleister um. Beschränken Sie zusätzlich nicht benötigte Zugriffe.
- **Auf Auffälligkeiten prüfen:** 
Untersuchen Sie betroffene Systeme auf ungewöhnliche Abstürze, unerwartete Prozesse und verdächtige Aktivitäten. Ein Sicherheits-Update beseitigt keine bereits erfolgte Kompromittierung.

Die technischen Hinweise zu betroffenen Versionen, Updates und [Übergangsmassnahmen sind auf dem Cyber Security Hub](https://security-hub.ncsc.admin.ch/#/posts/13198) verfügbar. Übergangsmassnahmen ersetzen die Sicherheits-Updates nicht.

## Was Privatpersonen tun sollten

Installieren Sie verfügbare Sicherheits-Updates für Ihre Programme und Geräte zeitnah über die offiziellen Update-Funktionen. Enthaltene Java-Komponenten werden je nach Produkt über dessen Software- oder Geräte-Update aktualisiert.

Wer eigene Server oder Online-Dienste betreibt, sollte zusätzlich die Empfehlungen für Betreiberinnen und Betreiber beachten.

## Weitere Informationen

[BACS: Technische Informationen auf dem Cyber Security Hub](https://security-hub.ncsc.admin.ch/#/posts/13198)

[Oracle: Sicherheitsupdates vom November 2026](https://www.oracle.com/security-alerts/cspunov2026.html)
