---
title: "Netscaler-Admins aufgepasst: Zero-Day verursacht Crashes und Codeausführung"
author: Heise Online; Dr Christopher Kunz
url: https://www.heise.de/news/Netscaler-Admins-aufgepasst-Zero-Day-verursacht-Crashes-und-Codeausfuehrung-11474971.html
hostname: heise.de
description: Sicherheitsforscher und Administratoren melden massenhafte Spontanreboots betroffener Geräte. Diese waren auf dem neuesten Patchstand.
sitename: Heise Online
date: "2026-10-03"
categories: ['IT']
tags: ['Citrix, Citrix NetScaler ADC, Citrix Netscaler Gateway, Exploit, IT, Security']
---
# Netscaler-Admins aufgepasst: Zero-Day verursacht Crashes und Codeausführung

Sicherheitsforscher und Administratoren melden massenhafte Spontanreboots betroffener Geräte. Diese waren auf dem neuesten Patchstand.

Seit den Abendstunden des 2. Oktober 2026 kursiert offenbar ein Exploit für eine neue Sicherheitslücke auf Citrix-Netscaler-Geräten. Der Hersteller warnt in einem Blogartikel, Sicherheitsforscher wollen Schadsoftware auf ihren Testgeräten beobachtet haben. Patches sind zur Stunde noch nicht verfügbar.

Dem britischen Sicherheitsexperten Kevin Beaumont zufolge könnte es sich um eine Umgehung der Fehlerbehebung der letzte Woche bekannt gewordenen Lücke „Pitscaler“ (CVE-2026-88771 / CVE-2026-88772) handeln. Er schreibt: „Also auf einem meiner Honeypots läuft eine heruntergeladene (Malware-) Binärdatei. Beide [Honeypots, Anm. d.Red.] waren gepatcht, also neue Schwachstelle.“ Sie ist offenbar auf der kürzlich erschienenen neuesten Version des Netscaler-Betriebssystems ausnutzbar – ein Zero-Day.

Andere Fachleute sekundieren: „Das Team von watchTowr Labs hat die Schwachstelle nun erfolgreich reproduziert.“ Damit ist nur eine Woche nach der letzten fatalen Lücke wieder ein Exploit für Netscaler-Systeme im Umlauf, der zur Einschleusung von Malware und dem Angriff auf Firmennetze taugt. Der Exploit lässt sich wohl über den massenhaften Versand von SAML-Anfragen an ein verwundbares Gerät ausführen. Reddit-Nutzer diskutieren die Lücke und ihre Ausnutzung in einem [umfangreichen Diskussionsfaden](https://www.reddit.com/r/Citrix/comments/1wvwuno/vulnerability_scans_causing_netscaler_reboots/).

Videos by heise

### Citrix forscht – noch kein Patch

Der Hersteller äußerte sich ebenfalls überraschend zügig [in seinem Blog](https://community.citrix.com/techzone-blogs/110_security-updates/security-update-guidance-for-netscaler-saml-authentication-deployments/). Jedoch nennt er weder wirksame Gegenmaßnahmen noch stellt er eine Lösung mittels Patch bereit. Betroffene mögen den Kundendienst kontaktieren. Bis ein Patch für den Zero-Day verfügbar ist, hilft nur erhöhte Wachsamkeit am Feiertagswochenende. Wir werden diese Meldung kontinuierlich aktualisieren.

Erst vor wenigen Tagen versüßte ein [Zero-Day-Angriff auf Citrix-Appliances](https://www.heise.de/news/Sicherheitsforscher-warnen-Neue-Zero-Day-Exploits-in-Citrix-Netscaler-11467200.html) Admins und Sicherheitsforschern weltweit das Wochenende, davor im [August](https://www.heise.de/news/Citrix-stopft-kritische-Anmeldungsumgehung-in-Netscaler-ADC-und-Gateway-11420304.html).

([cku](mailto:cku@heise.de))
