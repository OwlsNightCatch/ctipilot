---
title: Attacken auf Cisco UCS Central Software und Unified CM können bevorstehen
author: Heise Online; Dennis Schirrmacher
url: https://www.heise.de/news/Schadcode-Attacken-auf-Cisco-UCS-Central-Software-und-Unified-CM-moeglich-11515138.html
hostname: heise.de
description: Sicherheitsupdates schließen Lücken in Cisco UCS Central Software und Cisco Unified Communications Manager.
sitename: Heise Online
date: "2026-11-06"
categories: ['IT']
tags: ['Alert, Cisco Unified Communications Manager, IT, Patchday, Security, Sicherheitslücken, Updates']
fingerprint: f57466fb48a38796
---
# Attacken auf Cisco UCS Central Software und Unified CM können bevorstehen

Sicherheitsupdates schließen Lücken in Cisco UCS Central Software und Cisco Unified Communications Manager.

Sind Attacken auf Cisco UCS Central Software oder Cisco Unified Communications Manager erfolgreich, können Angreifer Schadcode ausführen. Sicherheitspatches stehen zum Download bereit. Bislang gibt es seitens des Netzwerkausrüsters keine Hinweise auf laufende Attacken.

Mit UCS Central Software verwalten Admins Ciscos Compute- und Storage-Plattform Unified Computing System (UCS). Unified Communications Manager steuert IP-Telefonie und Kommunikation.

### Softwareschwachstellen

[Wie aus einer Warnmeldung hervorgeht](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cucs-rce-LzHSFRDQ), ist die Lücke (CVE-2026-76506) in UCS Central Software mit dem Bedrohungsgrad „**hoch**“ eingestuft. Sie steckt konkret im Web-Management-Interface. Daran können der Beschreibung zufolge entfernte authentifizierte Angreifer mit manipulierten HTTP-Anfragen ansetzen. Diese kommen aufgrund von unzureichenden Überprüfungen durch. Im Anschluss können Angreifer eigene Kommandos ausführen, beliebige Dateien schreiben und sensible Informationen abgreifen. Einen Workaround gibt es nicht.

Die Entwickler geben an, das Sicherheitsproblem in der **Version 2.1(2c)** gelöst zu haben. Admins, die noch 2.0 oder ältere Versionen nutzen, müssen auf eine abgesicherte Version upgraden.

Die Lücke in Unified Communications Manager gilt als „**mittel**“ ([CVE-2026-76419](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cucm-xss-5mQn2U5z)). Sie betrifft das Web-Management-Interface von Unified CM und Unified CM SME. Entfernte Angreifer ohne Authentifizierung können Opfer dazu bringen, einen präparierten Link anzuklicken, und dann Skriptcode im Kontext des Interfaces ausführen. Hier schafft ein Update/Upgrade auf **15SU5** Abhilfe. Wer noch Version 14 nutzt, muss auf eine abgesicherte Version migrieren.

[Zuletzt attackierten Angreifer Ende Oktober](https://www.heise.de/news/Cisco-Firewalls-und-GitLab-Luecke-werden-angegriffen-11505669.html) Cisco-Firewalls.

([des](mailto:des@heise.de))
