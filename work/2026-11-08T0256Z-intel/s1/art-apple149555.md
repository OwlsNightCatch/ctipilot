---
title: Informationen zu den kompromittierten Zwischenzertifizierungsstellen von eMudhra - Apple Support (DE)
url: https://support.apple.com/de-de/149555
hostname: apple.com
description: Apple blockiert die kompromittierten Zertifikate automatisch. Mac-Administratoren können für bestimmte Befehlszeilentools optional zusätzliche Maßnahmen ergreifen.
sitename: Apple Support
date: "2026-10-30"
fingerprint: ccbe90b592a3bd6
---
# Informationen zu den kompromittierten Zwischenzertifizierungsstellen von eMudhra

Apple blockiert die kompromittierten Zertifikate automatisch. Mac-Administratoren können für bestimmte Befehlszeilentools optional zusätzliche Maßnahmen ergreifen.

Seit dem 19. Oktober 2026 blockiert Apple die Zertifikate der kompromittierten Zwischenzertifizierungsstellen (CAs) von eMudhra, die TLS-Zertifikate ausstellen, und nimmt weitere Aktualisierungen an dieser Blockierung vor.

- Wenn du Terminal nicht im Rahmen deines Arbeitsablaufs verwendest, musst du nichts unternehmen. Deine Apple-Geräte blockieren diese Zertifikate jetzt automatisch in Safari, Mail und Apps, die die Netzwerk- und Sicherheitsframeworks von Apple verwenden.
- Wenn du Terminal im Rahmen deines Arbeitsablaufs verwendest (z. B. als Systemadministrator oder Entwickler), nutzt du möglicherweise Befehlszeilentools, die diese Zertifikate weiterhin akzeptieren können. Einige in macOS oder den Xcode-Befehlszeilentools enthaltene Tools – wie curl und git – überprüfen Zertifikate anhand von /etc/ssl/cert.pem und können diese Zertifikate bis zu einem zukünftigen Softwareupdate weiterhin akzeptieren. Damit diese Tools die Zertifikate schon vorher nicht mehr akzeptieren, kannst du die Stammzertifikate der Zertifizierungsstellen aus der Datei entfernen.

## Was ist passiert

Die privaten Schlüssel von acht Zwischenzertifizierungsstellen, die von eMudhra betrieben werden, wurden kompromittiert. Zwei dieser Zertifizierungsstellen stellen Codesignaturzertifikate aus, denen die Frameworks von Apple nicht vertrauen. Die anderen sechs stellen TLS-Zertifikate aus. Jemand, der über die Schlüssel dieser sechs Zertifizierungsstellen verfügt, könnte Zertifikate erstellen, die für jede beliebige Website gültig erscheinen. eMudhra und Sectigo haben die betroffenen Zertifikate widerrufen.

Jede der sechs TLS-Zwischenzertifizierungsstellen verfügt über zwei Zertifikate, insgesamt also zwölf:

- Ein von emSign Root TLS CA - G3 ausgestelltes Zertifikat, dessen Zertifikatskette zu emSign ECC Root CA - G3 führt
- Ein von Sectigo kreuzsigniertes Zertifikat, dessen Zertifikatskette zu AAA Certificate Services führt

[Eine Liste dieser 12 Zertifikate anzeigen](https://support.apple.com#blocked)

## Welche Maßnahmen Apple ergreift

Am 19. Oktober 2026 begann Apple damit, diese 12 Zertifikate auf Apple-Geräten zu blockieren. Aktualisierungen der Zertifikatskonfigurationsdaten werden bei Bedarf automatisch an die Geräte gesendet, sodass du kein Softwareupdate installieren musst, um diese Änderung zu erhalten. Apple nimmt weitere Aktualisierungen an dieser Blockierung vor, die ebenfalls automatisch bereitgestellt werden. Am 23. Oktober 2026 begann Apple außerdem damit, emSign ECC Root CA - G3 zu blockieren.

Apple nimmt weitere Änderungen vor, um diese Zertifikate auch an anderen Stellen auf dem Mac zu blockieren, an denen Software Zertifikate überprüft, beispielsweise in den in macOS enthaltenen Befehlszeilentools oder den Xcode-Befehlszeilentools, die /etc/ssl/cert.pem verwenden. Diese Änderungen werden mit einem zukünftigen Softwareupdate verfügbar sein, und du musst keine Dateien bearbeiten, um sie zu erhalten.

## Muss ich /etc/ssl/cert.pem bearbeiten?

Die meisten Benutzer müssen /etc/ssl/cert.pem nicht bearbeiten. Safari, Mail und Apps, die die Netzwerk- und Sicherheitsframeworks von Apple verwenden, nutzen diese Datei nicht, und deine Apple-Geräte blockieren diese Zertifikate darin automatisch.

Auf dem Mac überprüfen einige in macOS oder den Xcode-Befehlszeilentools enthaltene Befehlszeilentools (darunter curl, git, python3, ruby, perl und openssl) Zertifikate anhand von /etc/ssl/cert.pem. Bei Zertifikaten, deren Zertifikatskette zu einem Stammzertifikat einer Zertifizierungsstelle in dieser Datei führt, überprüfen diese Tools weder die Blockierung durch Apple noch, ob das Zertifikat widerrufen wurde. Diese Datei wird mit einem zukünftigen macOS-Update aktualisiert. Wenn du diese Tools verwendest und nicht auf das Update warten möchtest, kannst du die Stammzertifikate der Zertifizierungsstellen aus der Datei entfernen.

Einige Apps und Tools verfügen über eine eigene Liste von Stammzertifikaten der Zertifizierungsstellen und verwenden weder die Blockierung durch Apple noch /etc/ssl/cert.pem. Wende dich bei diesen Apps oder Tools [an den Entwickler](https://support.apple.com/102435).

### Stammzertifikate von Zertifizierungsstellen aus /etc/ssl/cert.pem entfernen

Anstatt auf das bevorstehende Softwareupdate zu warten, können Administratoren die Stammzertifikate der Zertifizierungsstellen, zu denen die Zertifikatsketten der blockierten Zertifikate führen, aus /etc/ssl/cert.pem entfernen.

- Diese Schritte wirken sich auf alle Tools aus, die /etc/ssl/cert.pem verwenden. Anschließend können Tools, die ausschließlich diese Datei verwenden, möglicherweise einige Websites nicht mehr verifizieren, deren Zertifikatsketten über nicht betroffene Zwischenzertifizierungsstellen zu diesen Stammzertifikaten führen.
- Ein macOS-Softwareupdate kann /etc/ssl/cert.pem durch die Version von Apple ersetzen. Führe nach jedem Softwareupdate den Befehl in Schritt 4 aus, bis du das Softwareupdate installiert hast, das die Änderungen von Apple enthält. Wenn dabei ein Stammzertifikat einer Zertifizierungsstelle aufgeführt wird, das du entfernt hast, wurde die Datei durch das Update ersetzt. Lösche das alte Backup mit `sudo rm /etc/ssl/cert.pem.orig`, und wiederhole anschließend diese Schritte. Nachdem du das Update mit den Änderungen von Apple installiert hast, musst du diese Schritte für die in macOS oder den Xcode-Befehlszeilentools enthaltenen Befehlszeilentools nicht wiederholen.
- Du benötigst einen Administratoraccount oder kannst die Befehle über deine Geräteverwaltungslösung bereitstellen. Kopiere jeden Befehl genau wie angegeben. Erfahre, was zu tun ist, wenn beim Einfügen des Befehls in Terminal [eine Warnmeldung zu möglicher Schadsoftware angezeigt wird](https://support.apple.com/de-de/127377).

So entfernst du Stammzertifikate von Zertifizierungsstellen aus /etc/ssl/cert.pem:

1. Erstelle eine Sicherungskopie der Datei. Wenn bereits eine Sicherungskopie vorhanden ist, bleibt sie bei diesem Befehl erhalten: 
  - `[ -e /etc/ssl/cert.pem.orig ] || sudo cp -p /etc/ssl/cert.pem /etc/ssl/cert.pem.orig`
2. Entferne emSign ECC Root CA - G3. Dieser Befehl erstellt eine Kopie der Datei ohne emSign ECC Root CA - G3, überprüft, ob die Kopie nicht leer ist, und ersetzt das Original. Bei erfolgreicher Ausführung wird nichts angezeigt: 
  - `t=$(mktemp) && awk -v s='=== /C=IN/OU=emSign PKI/O=eMudhra Technologies Limited/CN=emSign ECC Root CA - G3' '/^(===|###) /{skip=0} $0==s{skip=1} !skip' /etc/ssl/cert.pem > "$t" && [ -s "$t" ] && sudo install -m 0644 -o root -g wheel "$t" /etc/ssl/cert.pem; rm -f "$t"`
3. Optional: Durch das Entfernen von emSign ECC Root CA - G3 werden die sechs von Sectigo kreuzsignierten Zertifikate nicht blockiert, da diese Tools sie weiterhin über AAA Certificate Services verifizieren können. Damit diese Tools die sechs Zertifikate über die Datei nicht mehr akzeptieren, bis du das Softwareupdate von Apple installiert hast, kannst du auch AAA Certificate Services entfernen. Dieser Befehl funktioniert genauso wie der Befehl in Schritt 2: 
  - `t=$(mktemp) && awk -v s='=== /C=GB/ST=Greater Manchester/L=Salford/O=Comodo CA Limited/CN=AAA Certificate Services' '/^(===|###) /{skip=0} $0==s{skip=1} !skip' /etc/ssl/cert.pem > "$t" && [ -s "$t" ] && sudo install -m 0644 -o root -g wheel "$t" /etc/ssl/cert.pem; rm -f "$t"`
4. Überprüfe das Ergebnis. Dieser Befehl listet die beiden Stammzertifikate der Zertifizierungsstellen auf, sofern sie noch in der Datei vorhanden sind. Wenn du beide entfernt hast, wird nichts angezeigt. Wenn bei der Ausführung des Befehls ein Fehler angezeigt wird, stelle die Sicherungskopie aus Schritt 1 wieder her. 
  - `openssl crl2pkcs7 -nocrl -certfile /etc/ssl/cert.pem | openssl pkcs7 -print_certs -noout | grep -E 'emSign ECC Root CA - G3|AAA Certificate Services'`.

## Gesperrte Zertifikate

| **Zertifikat** | Ausgestellt von | SHA-256-Fingerabdruck | 
|---|---|---|
| EM EV TLS CA - G3B | emSign Root TLS CA - G3 | E7568FE6E12331F4FD7DE61DA4C7559D0F8EB192A218D4741A3BA75184333838 | 
| EM OV TLS CA - G3B | emSign Root TLS CA - G3 | 98B896625C0C230ADEEC3EB2CF6AAD5001ECF9156A68644E82374CE5833BC25B | 
| EM DV TLS CA - G3B | emSign Root TLS CA - G3 | 42C4ACCD12C4F59597925E1A08A7A90102608543809308D50EC427E118BA1493 | 
| EM EV TLS CA - G3C | emSign Root TLS CA - G3 | 432EC25F0D28DE9006D97BF752F17BBB2CD41F669933FCB072D9A1148D0261F3 | 
| EM OV TLS CA - G3C | emSign Root TLS CA - G3 | CB6E15165AC802E9B3F993F16C25D41F4E81C21EBDE71AE1B012AC00BF9C7C3F | 
| EM DV TLS CA - G3C | emSign Root TLS CA - G3 | 0164D7CEAE5BB909C272AF151FF44B1177AE9B47D9424B94F1D9558C30934D19 | 
| EM EV TLS CA - G3B | AAA Certificate Services | 579480AEA166290BD3C643589E795FC0D0E54E86505D180F1DFF99EFD3199512 | 
| EM OV TLS CA - G3B | AAA Certificate Services | 5F1DED4DD590AF74631290CF073B122A2AAC6A1FA479778A0BD43579BD832699 | 
| EM DV TLS CA - G3B | AAA Certificate Services | 45A883F349AEDFD5F3A649B5498FFB121712BA8B448F3F2A91DBC5A766FCDDBE | 
| EM EV TLS CA - G3C | AAA Certificate Services | FD9D5C2DBBD4995AB69B8D50C439D9527B00529199C2FD01B2174EB58F07021F | 
| EM OV TLS CA - G3C | AAA Certificate Services | 7485B51C0ED192878FA1D2F948FB529AE1842CC5086C4B67F7BE5B2039DE9489 | 
| EM DV TLS CA - G3C | AAA Certificate Services | 62B7F9868263F72F6911FC78CEAF72C1979158B7368BF648683BB2AA39B02E72 | 

Informationen zu nicht von Apple hergestellten Produkten oder nicht von Apple kontrollierten oder geprüften unabhängigen Websites stellen keine Empfehlung oder Billigung dar. Apple übernimmt keine Verantwortung für die Auswahl, Leistung oder Nutzung von Websites und Produkten Dritter. Apple gibt keine Zusicherungen bezüglich der Genauigkeit oder Zuverlässigkeit der Websites Dritter ab. [Kontaktiere den Anbieter](https://support.apple.com/de-de/103190), um zusätzliche Informationen zu erhalten.
