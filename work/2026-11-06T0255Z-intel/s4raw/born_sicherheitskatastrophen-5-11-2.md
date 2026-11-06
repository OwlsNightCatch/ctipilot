---
title: "Sicherheitskatastrophen 5.11.2026: Digicert, Fake RVTools, Barracuda 0-Day und mehr"
author: Markus
url: https://borncity.com/blog/2026/11/05/sicherheitskatastrophen-5-11-2026-digicert/
hostname: borncity.com
description: "Alles abschalten: Die Sicherheitskatastrophen und -Vorfälle stellen langsam alles in den Schatten, was wir bisher erlebt haben. Zertifikataussteller Digicert wurde gehackt und Nutzerdaten (auch…"
sitename: Borns IT- und Windows-Blog
date: "2026-11-05"
categories: ['Sicherheit']
tags: ['Sicherheit']
fingerprint: f0d8fc9d5b94b69
---
Alles abschalten: Die Sicherheitskatastrophen und -Vorfälle stellen langsam alles in den Schatten, was wir bisher erlebt haben. Zertifikataussteller Digicert wurde gehackt und Nutzerdaten (auch Ausweiskopien etc.) sind abgeflossen. Es gibt 0-Click-Angriffe auf iOS- und Android-Geräte. Sega wurde gehackt. Node.js will zum 11.11.2026 neue Versionen mit Sicherheitskorrekturen veröffentlichen. Gefälschte Kopien von Dells RVTools erlauben Angreifern den Remote-Zugriff auf PCs, und so weiter. Hier eine Sammlung an Meldungen rund um diese Themen.


Dass es wieder einen Sicherheitsvorfall bei einer Buchungsplattform für Hotel gab, hatte ich im Beitrag [Cybervorfall bei vioma (Hotellerie / Tourismus) mit Abfluss von Buchungsdaten](https://borncity.com/blog/2026/11/05/cybervorfall-bei-vioma-hotellerie-tourismus-mit-abfluss-von-buchungsdaten/) angesprochen. Auch Iperius musste Dienste nach einem Angriff abschalten (siehe [Cybervorfall bei Iperius (Backup, Remote-Software), Dienste offline (4.11.2026)](https://borncity.com/blog/2026/11/05/cybervorfall-bei-iperius-backup-remote-software-dienste-offline-4-11-2026/)). Aber über diese Vorfälle hinaus gab es weitere Cybervorfälle, von denen ich einige nachfolgend kurz ansprechen.

## Datenabfluss bei Digicert

Digicert gilt als führender US-amerikanischer Anbieter von digitalen Zertifikaten, Public-Key-Infrastrukturen (PKI) und Digital-Trust-Lösungen. Und das Unternehmen ist Opfer eines Cyberangriffs geworden.

Die Nacht ist mir in einem Anfall seniler Bettflucht obiger [Tweet](https://x.com/troyhunt/status/2118064905391935681) von Troy Hunt untergekommen. Habe aber beschlossen, einige Stunden zu schlafen, dann zu frühstücken noch zum Donnerstag Frühsport zu gehen, und dann den "Weltuntergang" zu verkünden. Troy Hunt (Have I been pwnd) hat eine Benachrichtigung von Digicert bekommen, in der er von einem Abfluss seiner persönlichen Daten (Name, Telefonnummern, und Adressen) informiert wurde. Aber auch Dokumente zur Identifikation, wie Ausweiskopien, Führerscheine etc. scheinen beim Cybervorfall abgeflossen zu sein. Digitcert hat den Vorfall, der sich zum 18. Juni 2026 ereignete, in [diesem Post](https://bugzilla.mozilla.org/show_bug.cgi?id=2084460#c2) bestätigt – bei Cyber Security News wurde es [hier](https://cybersecuritynews.com/digicert-confirms-data-breach/) etwas lesefreundlicher aufbereitet.

## Spielehersteller Sega gehackt

Sega ist ein traditionsreiches japanisches Unternehmen für Videospiele und ehemaliger Hersteller von Spielkonsolen mit Sitz in Shinagawa, Tokio. In [einer Mitteilung](https://www.segafave.co.jp/news/261102_1/) vom 2.11.2026 hat Sega den Zugriff von unbefugten Dritten auf bestimmte Server des Unternehmens eingeräumt.

Betroffen waren Server im Zusammenhang mit den Arcade-Spiel-Netzwerkdiensten ALL.Net und Aime. Seit der Aufdeckung des Vorfalls wird derzeit untersucht, ob Daten abgeflossen sind und wie groß der Umfang der Auswirkungen ist. Zur Durchführung der Untersuchungen und zur Überprüfung der Sicherheit hat man wir seit Sonntag, dem 1. November, um 15:00 Uhr verschiedene Dienste im Zusammenhang mit ALL.Net und Aime eingestellt. Dadurch sind "Mario Kart" und "Taiko no Tatsujin"-Spielautomaten in Japan im Offline-Modus.

## Fake Dell VMware tool RVTools erlauben Remote-Zugriff

RVTools ist ein kostenloses Windows-Verwaltungs- und Analyse-Tool für VMware-vSphere-Umgebungen (vCenter und ESXi-Hosts), das ursprünglich von Robware entwickelt und 2023 von Dell übernommen wurde. RVTools verbindet sich über das VMware vSphere Management SDK (VI SDK) direkt mit einem vCenter-Server oder ESXi-Host und liest eine Vielzahl von Informationen über die virtuelle Infrastruktur aus.

Obiger [Tweet](https://x.com/IntCyberDigest/status/2117888075208831347) warnt, dass eine gefälschte GitHub-Kopie von Dells VMware-Tool "RVTools"  kursiert, die Angreifern unbemerkt die vollständige Fernsteuerung über den PC verschafft. Das Installationsprogramm "Dell Setup" installiert einen echten, signierten Action1-Fernzugriffs-Agenten, der mit dem eigenen Konto des Angreifers verknüpft ist. Viele Antivirenprogramme erkennen dies angeblich nicht. Dieser [reddit.com-Post](https://www.reddit.com/r/sysadmin/comments/1xmdpuf/psa_fake_rvtools_on_github_rvsphexrvtools/) nennt das entsprechende GitHub-Repository und weitere Details.

## 0-Click-Angriffe auf Android und iOS

Gerade wurde ein groß angelegter "Watering-Hole"-Angriff gegen Nutzer von Android und iOS bekannt. Der russischen Hackern zugeschriebene Angriff  erfolgte über kompromittierte Websites. Es reichte der Besuch der betreffenden Seiten, um kompromittiert zu werden. Die Kollegen von Bleeping Computer haben einige Details in [diesem Beitrag](https://www.bleepingcomputer.com/news/security/hackers-use-n-day-exploits-in-zero-click-attacks-on-ios-android-devices/) aufbereitet.

## Ivanti Connect Secure 0-Day-Exploit

In der SSL-VPN- und Zero-Trust-Zugriffslösung für Unternehmen, Ivanti Connect Secure, gibt es wohl Schwachstellen, die zum Diebstahl von Active-Directory-Anmeldedaten ausgenutzt werden. Cyber Security News berichtet in [diesem Artikel](https://cybersecuritynews.com/ivanti-connect-secure/), dass Angreifer  dazu drei Zero-Day-Schwachstellen in Ivanti Connect Secure VPN-Geräten kombiniert haben, um sich ohne Anmeldung Root-Zugriff zu verschaffen, und suchten anschließend nach Anmeldedaten und sensiblen Active-Directory-Daten. Die Angriffe begannen am 3. Oktober 2026, und richteten sich gegen ein vollständig gepatchtes Gerät mit der Version 22.8R2.4. Dies wurde bei der Untersuchung verdächtiger Aktivitäten bei einem Kunden entdeckt.

## Microsoft Entra ID and Azure DevOps-Hacks

Hacker haben gestohlene Anmeldedaten für Microsoft Entra ID und Azure DevOps genutzt, um Zugriff auf 27 Organisationen zu erlangen, wird in [diesem Tweet](https://x.com/The_Cyber_News/status/2117857721747919211) berichtet. Die seit dem 1. November 2026 andauernde Kampagne richtet sich gegen Managed-Service-Provider (MSPs) und deren Kunden. Der Angreifer hatte es auf etwa 45 App-Registrierungen bei rund 18 Organisationen abgesehen. Bei mehr als 33 App-Registrierungen waren die Angreifer erfolgreich bei der Authentifizierung. Details finden sich in [diesem Artikel](https://cybersecuritynews.com/stolen-entra-id-and-azure-credentials/) von Cyber Security News.

## Neue Node.js-Releases zum 11.11.2026

Das Node.js-Projekt, welches im Oktober 2026 durch die node2shell-Schwachstelle aufgefallen ist, [kündigt ein neues Release](https://nodejs.org/en/blog/vulnerability/november-2026-security-releases) zum 11. November 2026 an. Es soll neue Versionen für die Zweige 22, 25 und 26 geben, die dann Schwachstellen adressieren.

## SonicWall-Schwachstellen bestätigt

Der Anbieter SonicWall hat bestätigt, dass zwei Sicherheitslücken in der nicht mehr unterstützten Version GMS 9.5.2 und früheren Versionen nicht behoben werden.

• CVE-2026-109593: Unauthentifiziertes Lesen von Dateien

• CVE-2026-109594: Authentifizierte SQL-Injection

Die Version GMS 9.5.2 sei End-of-Live und es wird der Umstieg auf SonicWall NSM empfohlen. Details finden sich bei [The Hacker News](https://thehackernews.com/2026/11/sonicwall-wont-patch-eol-gms-flaws-that.html).

## Xen-Hypervisor mit Schwachstellen

Anthropics "Claude" hat zwei Schwachstellen im Xen-Hypervisor entdeckt. Diese ermöglichen es einer böswilligen Gast-VM, auf den Speicher anderer VMs zuzugreifen und dort Daten zu schreiben, darunter auch auf den Speicher der privilegierten dom0.

- Xen 4.6+ ist betroffen
- Patches für 4.17+, keine für 4.6–4.16
- Qubes OS und XCP-ng sind betroffen

The Hacker News hat die betreffenden Details in [diesem Beitrag](https://thehackernews.com/2026/11/xen-hypervisor-flaws-let-one-malicious.html) zusammen gefasst.

## Debian APT-Schwachstelle

Debians APT-Mechanismus ist von einem Man-in-the-Middle-Angriff betroffen, der die Ausführung von beliebigem Code als Root ermöglicht. Der Angreifer muss sich aber im Netzwerk der Debian Maschinen befinden und dann dann Pakete manipulieren. Phoronix hat die Details in [diesem Beitrag](https://www.phoronix.com/news/Debian-APT-MITM-RCE) aufgegriffen.

## Schwachstelle bedroht Barracuda Secure Gateway

Sofern jemand das Barracuda Secure Gateway einsetzt, sollte er sich dringend nach Updates umsehen. Angreifer können sich bei Barracuda Email Security Gateway u.u. Root-Rechte verschaffen. heise hat dies in [diesem Beitrag](https://www.heise.de/news/Barracuda-Root-Sicherheitsluecke-bedroht-unter-anderem-Email-Security-Gateway-11511074.html?wt_mc=sm.red.ho.mastodon.mastodon.md_beitraege.md_beitraege) aufgegriffen und Details zur Ausnutzung genannt.

## Schwachstelle in FME-Software Safe

Andreas hat mich im Nachgang informiert, dass die Software FME des Anbieters Safe Sicherheitsupdates für die Plattformen FME FLow (Server) und FME Form (Desktop) erhalten hat. Bei Andreas wird die Software bei uns eingesetzt um Geodaten, Vektordaten, Rasterdaten sowie nicht-räumliche Daten aus verschiedenen Formaten zu lesen, umzuwandeln, zu prüfen und in andere Systeme zu überführen. Betroffen von dem Sicherheitsupdate sind alle FME-Versionen vor 2026.3.1. Aktuell sind 35 Schwachstellen vorhanden:

- Kritisch: 12
- Hoch: 21
- Mittel: 1
- Niedrig: 1

Details lassen sich im Beitrag [FME November 2026 Security Updates](https://support.safe.com/hc/en-us/articles/46792031942029-FME-November-2026-Security-Updates) nachlesen (danke an den Leser für den Hinweis).

## Eichstädt massiv von Cyberangriff betroffen

Anfang Oktober 2026 hatte ich im Beitrag [Welle von Cyberangriffen: Fehmarn-Belt-Kontaktor, Dixell-Frankreich, Egide, Citrix Workspace App etc.](https://borncity.com/blog/2026/10/13/welle-von-cyberangriffen-fehmarn-belt-kontaktor-dixell-frankreich-egide-etc/) berichtet, dass die Verwaltung von Eichstädt durch einen Cyberangriff lahm gelegt wurde. Sämtliche Dienste der Stadt in Bayern seien lahmgelegt, hieß es am 13.10.2026. Es gab auch Gerüchte über einen Datenabfluss. Nun hat mich ein Leser per Mail kontaktiert, weil er wohl von dem Angriff betroffen ist. Der Leser schrieb:

"Inzwischen sind erste Erkenntnisse erreicht, welche auch [offiziell bestätigt](https://www.eichstaett.de/cyberangriff/) wurden. Es wurde bestätigt, dass die Angreifer 1,4 TB an Daten (rund 1/4 aller Daten) entwendet haben. Auch sensible personenbezogene Daten können dabei sein. 400GB können nicht bewertet werden, um welche Daten es sich handelt. Es wird vor Fake-Rechnungen, Anschreiben etc gewarnt. Ebenso wurde die Datenschutzbehörde eingeschaltet. Unter den Bürgern der Stadt und auch bei mir persönlich als Betroffener ist die Frage offen, was vorallem mit den Ausweisdaten (inkl. Bild und Biometrische Daten) passiert ist und ob diese auch entwendet wurden."


## Was sonst noch wichtig wäre

Angreifer scannen laut [diesem Tweet](https://x.com/IntCyberDigest/status/2117992765216997476), der sich auf Marcus Hutchins bezieht, das Internet nach Linux-Servern, die von der kritischen Kernel-Sicherheitslücke CVE-2026-98432 betroffen sind. Zu dieser Schwachstelle hatte ich mehrere Blog-Beiträge (siehe [hier](https://borncity.com/blog/2026/10/30/sicherheits-meldungen-schwachstellen-und-angriffe-30-10-2026/), [hier](https://borncity.com/blog/2026/10/31/securepoint-zur-ipv4-tcp-schwachstelle-cve-2026-98432-in-linux/) und [hier](https://borncity.com/blog/2026/11/04/ubuntu-patch-fuer-ipv4-tcp-schwachstelle-cve-2026-98432/)). Es wurden bei Scans 2,1 Millionen Server gefunden, die diese Sicherheitslücke aufweisen.

In WordPress wird die Schwachstelle CVE-2026-119977 aktiv ausgenutzt. Ich hatte im Beitrag [WordPress 7.1.4 verfügbar (28. Oktober 2026)](https://borncity.com/blog/2026/10/28/wordpress-7-1-4-verfuegbar-28-oktober-2026/) über eine verfügbare, gepatchte Version berichtet.

Zum Binance-Hack (siehe [Cybervorfälle: Telekolumbus Netz GmbH (Pyur); iPhone-Hack, Binance und mehr](https://borncity.com/blog/2026/11/02/cybervorfaelle-telekolumbus-netz-gmbh-pyur-bianance-und-mehr/)) werden mehr und mehr Details bekannt. Scheint eine länger vorbereitete Operation gewesen zu sein. Arstechnica hat einige Details in [diesem Artikel](https://arstechnica.com/information-technology/2026/11/binance-says-hackers-who-stole-billions-in-crypto-spent-months-planning-heist/) dazu veröffentlicht.

In Norwegen gibt es die Entwicklungshilfeagentur Norad. Hacker sind in das System eingedrungen und haben dabei Informationen über jeden einzelnen registrierten Nutzer ihres Förderportals gestohlen. Norad teilte mit, dass bei 20.614 registrierten Personen Namen und E-Mail-Adressen gestohlen wurden und dass Informationen aus den Anträgen von mindestens drei Organisationen "umgeleitet" wurden. The Register hat die Details in [diesem Beitrag](https://www.theregister.com/cyber-crime/2026/11/05/norways-aid-agency-pwned-and-all-users-data-is-stolen/5307765) veröffentlicht.

Und Browser-Anbieter Brave hat Zoff mit der New York Times. Die Zeitung und weitere US-Medien verklagen Brave, weil dieser Paywalls im Browser umgehe und die von den Benutzern besuchten Webseiten bzw. Daten mit KI-Anbietern teilt. "Brave ist der Anbieter, Händler und Vertreiber gestohlener urheberrechtlich geschützter Inhalte für seine eigenen Nutzer und viele der bekanntesten GenAI-Unternehmen, darunter Anthropic, Perplexity, Mistral, xAI und Cohere", heißt es in der Klageschrift, aus der Arstechnica in [diesem Beitrag](https://arstechnica.com/tech-policy/2026/11/nyt-demands-brave-shut-down-its-paywall-blocker-and-end-deals-with-ai-firms/) zitiert.

Uff, vielleicht wäre es doch besser, wieder auf Steintafeln zu meißeln.

Papier reicht.

Und das gute alte Faxgerät wieder aus dem Keller holen.

Wieder mehr analog arbeiten und leben, das will ich wieder lernen. Eine Herausforderung.

Und dann kommt eine DDos Attacke und dein Papier ist leer.

Mit der sich rasch entwickelnden KI wird es zu immer mehr Exploitausnutzungen kommen, da selbst Otto-Normalos sich mittlerweile mithilfe von KI Wissen und die nötigen Ressourcen aneignen können, um solche Angriffe zu tätigen bzw. Exploits ausfindig zu machen.

Das wird in ein paar Jahren in einen Kampf zwischen KIs ausarten. Frei nach dem Motto: Welche KI kann die Exploits früher entdecken und ggf. patchen als eine andere diese ausnutzen kann?

Dann sollte man ja annehmen, dass die Hersteller diese Tools auch zur Prüfung Ihrer eigenen Produkte verwenden könnten.

Ja! Sofort abschalten ! Es ist ungeheuerlich wie erbärmlich schlecht so ziemlich alles programmiert ist was mit Datensicherheit in und um das Internet zusammenhängt. Hacks in Berlin und anderen Städten mit Datenabflüssen ungeahnten Ausmaßes, Webseiten unsicher ( php ), Onlinebanking unsicher, Clouds angehackt und und und…

Wir sind eben noch nicht so weit. Wir sollten eben nochmal einen Schritt zurückgehen und tatsächlich eine Zeit lang auf Fax, Papier usw. zurückgreifen BIS wir so weit sind augereifte System anzubieten. Auch Betriebssysteme abzuspecken, denn jedes neue Feature schafft neue Einfallstore.

Ich möchte wetten dass wenn Mikkisoft und Apfeltech Alternativversionen von Windows und OSX wieder anbieten würden, mit übreüften Code auf Sicherheit, dass eine große Anzahl zurückgreifen würde auf die alten Systeme mit aktualisierten Code.

Man stelle sich vor: Windows 7 auf heutiges Sicherheitsniveau gebracht, Snow Leopard von Apple auf heutiges Sicherheitsniveau gebracht, alles ohne den bunten überflüssigen Bloatware-Kram… Wundervoll. Schlanke, schnelle Systeme und wer mehr will soll sich optinional eben selber dazuinstallieren. Doch das beträfe nur die Systeme.

Was mit den den ganzen hochgefährlichen Katastrophen in Internet, Verwaltung, Services – Online Dienste ? Abschalten, abspecken, neu starten und zurück an das Reißbrett!

Jetzt brachten die im Radio die neueste Neuigkeit (Kot) : Bundesweit online Wohnortwechsel an Meldebehörde nun möglich. Ich garantiere: Es wird nicht so lange dauern, da werden auch dort branntgefährliche Hacks stattfinden.

Es ist ein Trauerspiel und die Verantwortlichen in Politik und IT tun nichts, lassen es darauf ankommen; Hauptsache Digitalisierung, weil es so schick klingt und so modern und so up to date!

Pfui Teufel!

Du weißt nicht, welche Lücken noch in den alten Windows und MacOS Versionen drin stecken. Auch Linux, ganz frisch:

https://www.golem.de/news/mit-ki-agenten-openai-will-in-linux-system-fast-1-000-root-luecken-gefunden-haben-2611-214884.html

Da wird einem schlecht…

Ein wichtiger Satz im OpenAI-Artikel:

"exploits that could give unprivileged local users root access."

\*https://openai.com/index/a-thousand-fewer-paths-to-root/

Das heißt, der Angreifer muss bereits lokal mit einem user-account eingeloggt sein, damit diese Angriffe funktionieren.

Für einen Angreifer von außen gelten alle diese Exploits nicht, es ist also kein Remote-Code-Execution (RCE), sondern nur local-privilege-escalation (LPE).

Das ist also wesentlich weniger schlimm als es zuerst klingt.

Ein Angreifer von außen kommt normalerweise nichtmal über den Router hinaus auf den eigentlich anzugreifenden Computer.

Naja, viele Probleme werden gar nicht durch die Software selbst verursacht, sondern durch schlampige Konfiguration. Und dafür sind oft gar nicht die Systemadmins schuld, sondern deren Vorgesetzen, die Anforderungen stellen, die große Sicherheitslöcher reißen oder verhindern, das man vorhandene Sicherheitseinstellungen auch aktivieren kann.

Oft sind die Vorgesetzten auch sehr stur und lassen sich von den Experten im eigenen Haus nicht von ihren fatalen Forderungen abbringen.

Das fängt schon bei so etwas wie Zugriffsrechten an.

In gar nicht so wenigen Firmen und Behörden stehen die Berechtigungen auf "Jeder".

Weitere Konfigurationsfehler:

Benutzer können sich von beliebigen PCs aus anmelden und zu beliebigen Uhrzeiten.

Netzwerke sind nicht segementiert.

Benutzer haben auf ihren Arbeitsstationen lokale Adminrechte.

Dienste und Verwaltungsschnittstellen sind unnötigerweise aus dem Internet erreichbar.

Patches werden nicht zeitnah eingespielt.

Software wird nicht aktuell gehalten.

Ereignisprotokolle werden nicht regelmäßig gelesen.

Backups werden nicht regelmäßig kontrolliert, ob auch der Restore fehlerfrei funktioniert.

etc. etc.

Die IT-Systeme werden sehr oft nur als lästige Notwendigkeit, die nur Geld kostet, angesehen.

Das von der Sicherheit der IT-Systeme die Zukunft des Unternehmens abhängt, wird oft nicht gesehen.

Vor längerer Zeit wurde eine Firma in Bayern von Ransomware befallen.

Die hatten ihr Backup nicht im Griff, so das die verschlüsselten Daten nicht wieder hergestellt werden konnten.

Die Firma war damit arbeitsunfähig und musste Insolvenz anmelden.

Die Firma gibt es nicht mehr.

Die Auswirkungen der meisten Sicherheitslücken wären extrem viel kleiner, wenn man die Netzwerke vernünftig konfiguriert.

Und Konfiguration und Administration eines Netzwerks ist nichts, was man einmal macht und dann vergisst, sondern es ist ein Job, der tägliche Aufmerksamkeit und Arbeit verlangt.

Die Guten werden es überstehen, die Schlechten werden untergehen… who cares? Kann einem doch eigentlich nur recht sein, wenn da mal ordentlich durchgesiebt wird.

\> "Es ist ein Trauerspiel und die Verantwortlichen in Politik und IT tun nichts"

To be fair: 1. Schlimm genug, dass die Politik überhaupt Gesetze erlassen muss, dass Firmen keinen Müll verkaufen bzw. bei ihrem eigenen Laden nicht alle Türen unverschlossen für jeden offen stehen zu lassen. Das ist NICHT deren Job!

2\. Jede Politik ist für die Geschwindigkeit in der sich IT weiterentwickelt viel zu langsam. Das ist auch wichtig, denn wenn man ein Gesetz zu schnell raushaut, hat man ein Problem. Abgesehen davon: DSGVO, KRITIS, NIS2 etc. gibt es ja alles.

Ihr wisst aber, dass Faxe in der heutigen Zeit nur noch digital übertragen werden?

Da nutzt endlich wieder Brieftauben die sind umweltfreundlich.

Umweltfreundlich ?

Du vergißt den gefährlichen und ätzenden Vogelkot.

:-)

Puh schockier mich doch nicht so

Digicert + Alles Abschalten hat ja mal so geklungen als hätten die nen CA PK verloren

Du hast https://sshhole.com/ übersehen, ein wunderbares Paradebeispiel für "technische Schulden" — Entwickler waren zu blöde, den Rückgabewert NULL korrekt zu behandeln, und Frickler haben statt dessen die "unmögliche" Zeichenkette \* zurückgegeben…

FAIL EARLY, FAIL OFTEN!

Zur FME (auch bei uns im Einsatz):

Das Sicherheitsupdate auf die Version 2026.3.1.1 wurde bereits am 29.10.2026 veröffentlicht, siehe:

https://fme.safe.com/downloads/

Für das zeitnahe Einspielen der Updates empfehle ich daher für alle Admins ein "Website monitoring" der entsprechenden Seiten um die Updates zeitnah einzuspielen.

Zu RVtools (auch bei uns im Einsatz):

Warum ein Download über GitHub und nicht direkt über DELL?

https://www.dell.com/support/kbdoc/de-de/000325532/rvtools-installationsprogramm-4-8-2-installationsprogramm

Hallo @Felix

"To be fair: 1. Schlimm genug, dass die Politik überhaupt Gesetze erlassen muss, dass Firmen keinen Müll verkaufen bzw. bei ihrem eigenen Laden nicht alle Türen unverschlossen für jeden offen stehen zu lassen. Das ist NICHT deren Job!"

Du hast Recht, es ist nicht der Politiker Job für die Sicherheit von Code zu sorgen, aber es ist deren Job nicht alles zeitlich zu erzwingen was nicht sicher ist. Wenn die Politik sagt : "Können wir noch nicht implementieren, weil noch icht sicher" – ist es jedoch deren Verantwortung höchstsensible Datenbanken / Portale / digitale Dienste noch zu verbieten.

—–

"2. Jede Politik ist für die Geschwindigkeit in der sich IT weiterentwickelt viel zu langsam. Das ist auch wichtig, denn wenn man ein Gesetz zu schnell raushaut, hat man ein Problem. Abgesehen davon: DSGVO, KRITIS, NIS2 etc. gibt es ja alles."

Das stimmt mitunter, jedoch ist es dann erst recht so, dass die Verantwortung für die Einführung hochsensibler Dienste noch ausgeschlossen werden – per Gesetz.

Zudem gehören bereits bestehende Dienste / Gesetze auf den Prüfstand, insbesondere was Entschädigungen betrifft bei Verletzungen von sensiblen Daten.

Beispiel: Der Berlin-Hack. Alle personenbezogen, sensible Daten die einfach so abgreifbar waren, alle betroffenen Personen sollte eine hochschmerzhafte Entschädigung zustehen. Denn das, was da für die Hacker vorzufinden war auf den Servern war teilweise schon sträflich ungeschützt.

Ich bin mal gespannt, wann wirklich (und ob überhaupt) das vollmundige Versprechen der Politiker und des Senats etc… greift. Wie hieß es doch so schön ? Es wird geforscht welche Daten , vom wem, rausgingen….

Man hört so gar nichts mehr davon… jaja…..
