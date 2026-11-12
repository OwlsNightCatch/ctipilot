---
title: "Korrektur: PowerFolder Server sind betroffen — bitte /wopi/ sofort sperren"
url: https://www.powerfolder.com/news/2026-11-07-korrektur-powerfolder-server-sind-betroffen-bitte-wopi-sofor.html
hostname: powerfolder.com
description: Bitte sperren Sie sofort alle Anfragen auf den Pfad /wopi/ einschließlich aller Unterpfade an Ihrem Reverse-Proxy bzw. Ihrer Firewall — auch für Ihren…
sitename: PowerFolder
date: "2026-11-07"
fingerprint: "27cd9f722da33bdf"
---
# Korrektur: PowerFolder Server sind betroffen — bitte /wopi/ sofort sperren

**Bitte sperren Sie sofort alle Anfragen auf den Pfad `/wopi/` einschließlich aller Unterpfade** an Ihrem Reverse-Proxy bzw. Ihrer Firewall — auch für Ihren Dokumentenserver. Im Zweifel nehmen Sie den Server vom Netz, bis das Sicherheitsupdate installiert ist.

**Korrektur unserer bisherigen Aussage:** Dass selbst betriebene Server nicht betroffen seien, trifft nach neuen Erkenntnissen **nicht zu**. Die Schwachstelle, über die der Angreifer in unsere Cloud eingedrungen ist, betrifft **alle PowerFolder Server und sämtliche Versionen**.

Das gilt auch dann, wenn die **Online-Dokumentbearbeitung nicht eingerichtet** oder in den Einstellungen **abgeschaltet** ist: **Das Abschalten in den Einstellungen schützt nicht.** Die Sperre muss vor dem Server greifen, also im Reverse-Proxy oder in der Firewall.

Betreiber erhalten die Details direkt von uns. Ein Sicherheitsupdate ist in Arbeit. Fragen bitte über [support.powerfolder.com](https://support.powerfolder.com).

Zum Hintergrund: [Update zum Sicherheitsvorfall vom 6. November 2026](https://www.powerfolder.com/news/2026-11-06-update-angriff-gestoppt-ihre-dateien-sind-sicher-wiederanlau.html)
