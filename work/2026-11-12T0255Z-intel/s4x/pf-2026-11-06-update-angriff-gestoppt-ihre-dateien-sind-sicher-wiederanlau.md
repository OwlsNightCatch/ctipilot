---
title: "Update: Angriff gestoppt – Ihre Dateien sind sicher – Wiederanlauf am Dienstag"
url: https://www.powerfolder.com/news/2026-11-06-update-angriff-gestoppt-ihre-dateien-sind-sicher-wiederanlau.html
hostname: powerfolder.com
description: Der Angriff ist gestoppt. Der Zugang des Angreifers ist seit dem 6. November 2026, gegen 14:30 Uhr, gesperrt. Ihre Dateien sind sicher. Sie sind weder…
sitename: PowerFolder
date: "2026-11-06"
fingerprint: fada4fdaa9f96bde
---
# Update: Angriff gestoppt – Ihre Dateien sind sicher – Wiederanlauf am Dienstag

- **Der Angriff ist gestoppt.** Der Zugang des Angreifers ist seit dem 6. November 2026, gegen 14:30 Uhr, gesperrt.
- **Ihre Dateien sind sicher.** Sie sind weder verloren gegangen noch beschädigt.
- **Die PowerFolder Cloud ist voraussichtlich ab Dienstag, 10. November 2026, wieder verfügbar.**

**Was ist passiert?** Ein Angreifer hatte unbefugten Zugang zu Teilen unserer Cloud-Systeme; die Kontrolle über die Server selbst hat er nicht erlangt. Möglich wurde das durch eine Verkettung mehrerer Ursachen in unserer eigenen Betriebsinfrastruktur. Dem Zugriff gingen vorbereitende Aktivitäten voraus; wann sie begonnen haben, ist Teil der laufenden Untersuchung. Erkannt haben wir die Auffälligkeiten am 6. November 2026 über unsere Überwachungssysteme und sofort reagiert: Cloud abgeschaltet, Zugang gegen 14:30 Uhr gesperrt, betroffene Zugangsdaten ausgetauscht. Wir haben Strafanzeige erstattet und die Datenschutzbehörde informiert.

**Eine Vorsichtsmaßnahme:** Nicht ausschließen können wir, dass Nutzerdaten (Name, E-Mail-Adresse) und Passwörter in verschlüsselter Form kopiert wurden. Vor der Freischaltung entwerten wir alle bisherigen Passwörter, Sitzungen und betroffenen Zugangstokens — mit einem alten Passwort kommt niemand mehr hinein. Deshalb vergeben Sie nach dem Wiederanlauf beim ersten Login ein neues Passwort; alle Geräte melden sich neu an. Wenn Sie Ihr PowerFolder-Passwort auch anderswo verwenden, ändern Sie es dort. Wir fragen nie per E-Mail nach Ihrem Passwort.

#### PowerFolder Server (On-Premise) — Korrektur, Stand 7. November 2026

Unsere frühere Aussage, selbst betriebene Server seien nicht betroffen, trifft nach neuen Erkenntnissen **nicht zu**. Die Schwachstelle, über die der Angreifer eingedrungen ist, betrifft **alle PowerFolder Server und sämtliche Versionen** — auch wenn die Online-Dokumentbearbeitung nicht eingerichtet oder in den Einstellungen abgeschaltet ist. **Das Abschalten in den Einstellungen schützt nicht.**

Bitte sperren Sie sofort alle Anfragen auf den Pfad `/wopi/` einschließlich aller Unterpfade an Ihrem Reverse-Proxy bzw. Ihrer Firewall — auch für Ihren Dokumentenserver. Im Zweifel nehmen Sie den Server vom Netz, bis das Sicherheitsupdate installiert ist. Betreiber erhalten die Details direkt von uns; Fragen bitte über [support.powerfolder.com](https://support.powerfolder.com).

Herzlichen Dank an unser Team, das sofort erkannt und gehandelt hat – und an Sie für Ihre Geduld.

Nächstes Update: Montag, 9. November 2026. Fragen: [support.powerfolder.com](https://support.powerfolder.com).

**Korrektur vom 9. November 2026:** Die ursprüngliche Aussage „der Angreifer hat keine Dateien heruntergeladen“ ist nach neuen Erkenntnissen nicht haltbar und wurde entfernt. Den aktuellen Stand finden Sie im [Update vom 8. November 2026](https://www.powerfolder.com/news/2026-11-08-update-so-laeuft-der-wiederanlauf-der-powerfolder-cloud-ab-s.html).
