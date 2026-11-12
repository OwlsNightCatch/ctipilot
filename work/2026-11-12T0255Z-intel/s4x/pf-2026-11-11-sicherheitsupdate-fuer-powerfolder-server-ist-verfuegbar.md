---
title: Sicherheitsupdate für PowerFolder Server ist verfügbar
url: https://www.powerfolder.com/news/2026-11-11-sicherheitsupdate-fuer-powerfolder-server-ist-verfuegbar.html
hostname: powerfolder.com
description: "Das Sicherheitsupdate für PowerFolder Server ist verfügbar. Bitte installieren Sie es zeitnah: 28.2.100 für die Linie 28.2, 26.4.100 für die Linie 26.4…"
sitename: PowerFolder
date: "2026-11-11"
fingerprint: d499997add9113b7
---
# Sicherheitsupdate für PowerFolder Server ist verfügbar

- **Das Sicherheitsupdate für PowerFolder Server ist verfügbar.** Bitte installieren Sie es zeitnah: **28.2.100** für die Linie 28.2, **26.4.100** für die Linie 26.4.
- **Nach der Installation können Sie die Sperre auf `/wopi/` wieder aufheben.** Bis dahin bleibt sie bestehen — auch für Ihren Dokumentenserver.
- **PowerFolder Cloud:** läuft bereits auf diesem Stand. Für Cloud-Kunden ist nichts zu tun.
- **Release Candidate im Einsatz?** Bitte trotzdem auf .100 aktualisieren: sie enthält gegenüber dem letzten RC eine weitere Korrektur.

#### Download

- **28.2.100 · Linux, vollständiges Paket:** [PowerFolder-Server\_v28.2.100.tar.gz](https://www.powerfolder.com/downloads/server/28.2.100/07f02803a9c86023/PowerFolder-Server_v28.2.100.tar.gz) — SHA-256 `165b1363648e948735d3fdba54b64bcb00826c4f9ee84c6d373db3b4f39913d0`
- **28.2.100 · Windows, Installer:** [PowerFolder-Server\_v28.2.100\_Installer.exe](https://www.powerfolder.com/downloads/server/28.2.100/07f02803a9c86023/PowerFolder-Server_v28.2.100_Installer.exe) — SHA-256 `e53cede884fd6cda1d0934f48b31f6dcf1928177c30b77ac7ca92e072e9c9e31`
- **26.4.100 · Linux, vollständiges Paket:** [PowerFolder-Server\_v26.4.100.tar.gz](https://www.powerfolder.com/downloads/server/26.4.100/99caef6ed9e14167/PowerFolder-Server_v26.4.100.tar.gz) — SHA-256 `d1147dc7e82d7f9b9da3b948b675b637a3b53224aa4381a1c6a507f64477819a`
- **26.4.100 · Windows, Installer:** [PowerFolder-Server\_v26.4.100\_Installer.exe](https://www.powerfolder.com/downloads/server/26.4.100/99caef6ed9e14167/PowerFolder-Server_v26.4.100_Installer.exe) — SHA-256 `d954e456bfd3a5fffd5c9c854615e6ebdf1324ed2b259ab25dc3ab929d84de5c`

Prüfen Sie die Datei vor der Installation mit `certutil -hashfile <Datei> SHA256` (Windows) bzw. `sha256sum <Datei>` (Linux).

#### Installation

- **Windows:** den Installer ausführen. Er richtet den Server neu ein oder aktualisiert eine vorhandene Installation.
- **Linux, neue Installation:** das `.tar.gz` entpacken und als systemd-Dienst einrichten — die Schritte stehen in `README-systemd.txt` im Archiv. Das Paket bringt seine eigene Java-Laufzeitumgebung mit.
- **Linux, bestehende Installation:** Archiv in ein temporäres Verzeichnis entpacken, Dienst stoppen (`systemctl stop powerfolder`), dann `PowerFolder-Server.jar`, `PowerFolder-Server.sh`, `jre64/` und `fonts/` über das Installationsverzeichnis kopieren, Dienst starten. **`libs/` dabei behalten** — dort liegt Ihr Datenbanktreiber, das Archiv bringt keinen mit. Wurde `PowerFolder-Server.sh` lokal angepasst (Speicher, Pfade), übernehmen Sie die Einstellungen; Speicherwerte gehören ab dieser Version nach `/etc/default/powerfolder-server`.

Ihre Daten liegen außerhalb des Installationsverzeichnisses und bleiben unberührt: Konfiguration, interne Datenbank, Schlüssel und Protokolle in `~/.PowerFolder`, die Ordner in `~/PowerFolders` des Kontos, unter dem der Server läuft. Sichern Sie `~/.PowerFolder` bzw. Ihre Datenbank trotzdem vor dem Update. Planen Sie außerdem ein, dass Server-Administratoren sich danach einmalig für die Zwei-Faktor-Anmeldung einrichten.

#### Was das Update enthält

Das Update schließt die beim Angriff ausgenutzten Schwachstellen. Bereits geplante Sicherheitskorrekturen haben wir vorgezogen; zusätzliche Schwachstellen, die wir bei der umfassenden Prüfung unseres Codes gefunden haben, sind ebenfalls geschlossen. Dazu kommen neue Schutzfunktionen: verpflichtende Zwei-Faktor-Anmeldung für Server-Administratoren, kürzere Gültigkeitsdauern für Anmeldetokens sowie eine Protokollierung von Administrator-Anmeldungen und Konfigurationsänderungen. Details zu den einzelnen Schwachstellen veröffentlichen wir erst, wenn Betreiber genug Zeit zum Aktualisieren hatten.

Fragen bitte über [support.powerfolder.com](https://support.powerfolder.com).
