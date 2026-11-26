---
title: "1Password wurde gehackt (Nov. 2026)"
author: Tomas Jakobs
url: https://borncity.com/blog/2026/11/26/1password-wurde-gehackt-nov-2026/
hostname: borncity.com
description: Der in Toronto, Kanada, ansässige Passwortmanager-Anbieter 1Password hat einen Hack seiner internen Systeme bestätigt. Bei diesen Sicherheitsvorfall wurden einige Kundendaten abgegriffen.
sitename: Borns IT- und Windows-Blog
date: "2026-11-26"
categories: ['Allgemein']
fingerprint: "1f18fe9cdcb363c5"
language: de
image: https://borncity.com/blog/wp-content/uploads/2026/11/1Password-Hack.jpg
pagetype: article
filedate: "2026-11-26"
---
Der in Toronto, Kanada, ansässige Passwortmanager-Anbieter 1Password hat einen Hack seiner internen Systeme bestätigt. Bei diesen Sicherheitsvorfall wurden einige Kundendaten abgegriffen. Es soll jedoch kein Zugriff auf die Passwort-Tresore der Kunden und andere vertrauliche Daten erfolgt sein.


Die Meldung ist mir bereits zum 25. November 2026 in verschiedenen Tweets untergekommen, 1Password hat den Hack im Blog-Beitrag [Update on a security incident involving 1Password's backend systems. Customer vaults were not affected and all vault contents remain secure](https://1password.com/blog/update-on-nov-2026-security-incident) bestätigt. Die Kompaktform, was man wissen muss:

- Ein Angreifer hat sich Zugang zu einigen der 1Pasword Backend-Systeme verschafft.
- Am 19. November 2026 begann 1Password mit der Untersuchung von Hinweisen darauf, dass sich ein Angreifer Zugang zum GitHub-Konto eines Mitarbeiters verschafft hatte.
- Der Angreifer nutzte das Konto, um auf Quellcode zuzugreifen und Schadcode in Backend-Dienste einzuspielen.
- Durch den Schadcode wurden Verwaltungsdaten der Kunden vom Angreifer heruntergeladen. 1Password schreibt von "einer begrenzten Anzahl von Kundenkontodaten eines Teils der Kunden", die kopiert wurden.
- Abgeflossen sind unter anderem die Namen und E-Mail-Adressen, mit denen sich Kunden bei 1Password anmelden, sowie nicht vertrauliche interne Metadaten zum Konto.
- Zu keinem Zeitpunkt hatte der Angreifer Zugriff auf den Inhalt der Kunden-Vaults (Password-Tresore), noch standen diese Daten dem Angreifer zur Verfügung.
- Die Tresordaten, die darin enthaltenen Einträge und die Schlüssel, die diese schützen, sind sicher und waren nicht betroffen, schreibt der Anbieter. Denn 1Password hat keinen Zugriff auf das Passwort oder den geheimen Schlüssel des Tresors.

Der Anbieter hat Maßnahmen zur Eindämmung des Vorfalls ergriffen, saubere Versionen der betroffenen Dienste wiederhergestellt und eine Rotation der internen Zugangsdaten veranlasst. Nutzer müssen in ihrem 1Password-Konto keine Änderungen vornehmen. Der Anbieter warnt aber, bei Phishing-Versuchen in Form von unerwarteten E-Mails zu 1Password vorsichtig zu sein, beispielsweise bei Einladungen oder Anfragen zur Kontowiederherstellung, die nicht selbst veranlasst wurden.

Obiger Tweet thematisiert, dass Paul Moore auf so etwas gewartet hat, weil 1Password verstärkt auf AI setzt – obwohl obiger Vorfall nach öffentlichen Bekundungen nicht mit AI in Verbindung steht. Details sind dem Blog-Beitrag [Update on a security incident involving 1Password's backend systems. Customer vaults were not affected and all vault contents remain secure](https://1password.com/blog/update-on-nov-2026-security-incident) zu entnehmen.
