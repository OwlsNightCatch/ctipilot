---
title: "1Password: Kundendaten entfleucht"
author: Heise Online; Daniel AJ Sokolov
url: https://www.heise.de/news/1Password-Kundendaten-entfleucht-11538455.html
hostname: heise.de
description: Warum die Datenbank hacken, wenn man das Backend umschreiben kann? Kundendaten 1Passwords sind in unbefugte Hände gelangt. Obacht vor Phishing!
sitename: Heise Online
date: "2026-11-26"
categories: ['IT']
tags: ['1Password', 'Agile Bits', 'Datensicherheit', 'IT', 'Lieferkette', 'Passwörter', 'Security']
fingerprint: "3ef15c9fd51b38c4"
language: de
image: https://heise.cloudimg.io/v7/_www-heise-de_/imgs/18/5/2/0/8/3/4/4/shutterstock_2839481119-eb3763d22c93a997.jpg?func=bound&height=1200&org_if_sml=1&q=85&width=1200
pagetype: website
filedate: "2026-11-28"
---
# 1Password: Kundendaten entfleucht

Warum die Datenbank hacken, wenn man das Backend umschreiben kann? Kundendaten 1Passwords sind in unbefugte Hände gelangt. Obacht vor Phishing!

Angreifer haben bei 1Password Kundendaten erbeutet. Namen, E-Mail-Adressen, Kundenkontonummern, öffentliche Schlüssel, Passwortparamenter, „interne Metadaten“ sowie in einigen Fällen Identifizierungstoken sind in falsche Hände gelangt, teilt der Passwortsafebetreiber Agilebits mit. Nicht betroffen seien die Passwörter zur Öffnung der Passwortsafes und die darin gespeicherten [Passwörter](https://www.heise.de/news/1Password-draengt-Nutzer-der-Legacy-Version-ohne-Cloud-zum-Wechsel-11536995.html). Kunden sind nicht zu Sicherheitsupdates aufgerufen.

Einfallstor war [laut Mitteilung](https://1password.com/blog/update-on-nov-2026-security-incident) keine Sicherheitslücke der Datenbank, sondern das Github-Konto eines Mitarbeiters Agilebits'. Der oder die Täter verschafften sich demnach Zugang zu dort gespeichertem Source Code und schafften es auf diesem Weg, Malware in die 1Password-Systeme zu schieben. Diese lieferten dem Angreifer dann die Kundendaten – eine Spielart der Angriffe auf Lieferketten.

Agilebits verständigt nur jene kleine Zahl an Kunden, deren Identifizierungstoken abgegriffen wurden, direkt. Das sind Token, die in bestimmten, per E-Mail verschickten Hyperlinks mit Einladungen zu bestimmten administrativen Tätigkeiten enthalten sind. Diese Token alleine sollen noch keinen Zugriff auf 1Password-Konten ermöglichen.

Wann die Angreifer die Malware eingeschleust haben, sagt das Unternehmen nicht. Aufgefallen ist die Sache den Angaben zufolge am Donnerstag voriger Woche. Eine naheliegende Verwendungsmöglichkeit für die erbeuteten Daten ist Phishing: Die Täter könnten versuchen, sich als 1Password-Mitarbeiter auszugeben; das mag nun besonders überzeugend wirken, weil sie anhand der Daten wahre Angaben zur Identität des Kunden und Details seines Kontos machen können. Daher empfiehlt Agilebits seinen 1Password-Kunden, besonders aufzupassen.

### Kunden ohne Online-Konto unerwünscht

Unabhängig davon möchte Agilebits Bestandskunden, die noch keine laufenden Abonnementgebühren für 1Password entrichten, loswerden. Das betrifft insbesondere Nutzer der 1Password-Version 7. Denn dieses Programm kann man nutzen, ohne auf 1Password-Server angewiesen zu sein.

Das ist Agilebits ein Dorn im Auge, weil es diese Nutzer nicht zu kostenpflichtigen Abonnements zwingen kann. Daher beschneidet Agilebits die Funktionen von 1Password 7 schrittweise, [droht mit der Einstellung technischer Unterstützung](https://www.heise.de/news/1Password-draengt-Nutzer-der-Legacy-Version-ohne-Cloud-zum-Wechsel-11536995.html) und unterbreitet manchen Anwendern vermeintliche Sonderangebote.

([ds](mailto:ds@ct.de))
