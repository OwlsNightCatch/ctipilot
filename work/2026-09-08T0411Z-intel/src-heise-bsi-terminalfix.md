# extract: served via trafilatura-direct
---
title: BSI erklärt ersten Angriffsvektor auf Berliner Behörden
author: Heise Online; Nico Ernst
url: https://www.heise.de/news/BSI-erklaert-ersten-Angriffsvektor-auf-Berliner-Behoerden-11444072.html
hostname: heise.de
description: Erst Phishing, dann ein Fake-Captcha und ein Terminal-Befehl – so einfach lief nach ersten Analysen die Cyberattacke auf Berlin ab.
sitename: Heise Online
date: "2026-09-07"
categories: ['IT']
tags: ['Berlin, Cybercrime, IT, Journal, PowerShell, Ransomware, Rhysida, Security, Windows Terminal']
---
# BSI erklärt ersten Angriffsvektor auf Berliner Behörden

Erst Phishing, dann ein Fake-Captcha und ein Terminal-Befehl – so einfach lief nach ersten Analysen die Cyberattacke auf Berlin ab.

Das Bundesamt für Sicherheit in der Informationstechnik (BSI) warnt vor einer neuen Angriffskampagne namens „TerminalFix“. Die Behörde bezieht sich dabei auf eine Analyse von Microsoft. Brisant: TerminalFix war wohl für Cyberkriminelle die Eintrittskarte zu Netzen des Berliner Senats. Der Mitte August bekannt gewordene Angriff führte zu [einem massiven Datenabfluss](https://www.heise.de/news/Berliner-Senat-zahlt-nicht-sensible-Daten-jetzt-im-Darknet-11442286.html) mit [teils kritischen Informationen](https://www.heise.de/news/Cyberangriff-Berlin-mit-Steuerungseinheit-will-Betroffene-kontaktieren-11442896.html).

Dass es sich bei der Methode TerminalFix um den von der Cyberbande Rhysida genutzten Angriffsvektor handelt, hat das BSI in einem [Beitrag bei Mastodon](https://social.bund.de/@bsi/117212729947889443) bestätigt. Diese Information findet sich zwar nicht in [der BSI-Sicherheitsmitteilung](https://www.bsi.bund.de/SharedDocs/Cybersicherheitswarnungen/DE/2026/2026-287419-1032.pdf) (BITS) des Amtes ([PDF](https://www.bsi.bund.de/SharedDocs/Cybersicherheitswarnungen/DE/2026/2026-287419-1032.pdf?__blob=publicationFile)). Auf Mastodon verweist das BSI jedoch direkt auf diese Mitteilung. Damit steht fest: Die Senatsverwaltungen für Bauen und Verkehr wurden per TerminalFix attackiert.

- **7. bis 12. August 2026** : Bei den beiden Senatsverwaltungen für Stadtentwicklung, Bauen und Wohnen sowie für Mobilität, Verkehr, Umwelt und Klimaschutz[werden Daten durch Unbekannte ausgeleitet](https://www.heise.de/news/Berlin-Cyberangriff-auf-Verwaltung-begann-lange-vor-der-Entdeckung-11432414.html) . Der Angriff begann lange vor diesem Zeitpunkt.
- **14. August 2026:** Die beiden Senatsverwaltungen werden[vom Landesnetz isoliert](https://www.heise.de/news/Cyberattacke-auf-Berliner-Verwaltung-Ermittlungen-laufen-11416539.html) .
- **17. August 2026:** Die Senatskanzlei informiert per Pressemitteilung über[einen „IKT-Vorfall im Landesnetz Berlin](https://www.heise.de/news/Cyberattacke-auf-Berliner-Verwaltung-Ermittlungen-laufen-11416539.html) “. Es wird ein Notfallkrisenstab eingerichtet, BKA und LKA ermitteln, das BSI ist informiert.
- **21. August 2026** : Die beiden Behörden sind weiterhin vom Landesnetz abgeschnitten. Es kommt[zu Problemen bei Transferleistungen](https://www.heise.de/news/Berliner-Verwaltungen-nach-Cyberangriff-weiter-vom-Netz-getrennt-11421320.html) , unter anderem kann an 50.000 berechtigte Haushalten in Berlin kein Wohngeld ausgezahlt werden.
- **24. August 2026** : Alle Teile der Senatsverwaltung[sind wieder am Netz](https://www.heise.de/news/Nach-Cyberangriff-Senatsverwaltungen-wieder-am-Netz-11423077.html) und laut des Regierernden Bürgermeisters Kai Wegner „grundsätzlich arbeitsfähig“.
- **27. August 2026:** Florian Hauer, Berliner[Staatssekretär für Digitalisierung erklärt](https://www.heise.de/news/Sensible-Daten-bei-Cyberangriff-womoeglich-doch-betroffen-11427279.html) : „Derzeit gehen wir davon aus, dass der Angriff eingedämmt werden konnte“. Er kann nicht ausschließen, dass „auch personenbezogene oder sonstige nicht-öffentliche Daten betroffen sind“.
- **28. August 2026:** Sicherheitsbehörden treffen sich mit Vertretern des Landes Berlin[zu einer Krisensitzung](https://www.heise.de/news/30-Bitcoin-oder-Leak-Ransomware-Bande-erpresst-Berlin-11434325.html) . Die Angreifer haben Daten erbeutet und stellen eine Lösegeldforderung. Der Regierende Bürgermeister Kai Wegner erklärt: „Das Land Berlin lässt sich nicht erpressen.“ Angaben zu Umfang und Inhalt der Daten gibt es nicht. Am Abend berichtet der Spiegel, dass die bekannte Ransomware-Bande „Rhysida“ dahinter stecken soll. Auf deren Darknet-Webseite gibt es nachvollziehbar eine Forderung nach 30 Bitcoin (rund 2 Millionen Euro), mitsamt angeblichen Auszügen aus den Daten. Die Kriminellen versprechen unter anderem Listen mit Passwörtern im Klartext, Justizunterlagen und über 46.500 Verträge des Landes.
- **30. August 2026:** Der CCC-Sprecher Joachim Selzer warnt vor möglichem[Identitätsdiebstahl und anderen Betrugsversuchen](https://www.heise.de/news/Cyberangriff-auf-Berlin-Was-mit-den-Daten-passieren-koennte-11434581.html) . Bürger, von denen persönliche Angaben in dem vermeintlichen Datensatz enthalten sein könnten, würden zudem leicht Opfer von Erpressungsversuchen.
- **1. September 2026:** Auf einer Pressekonferenz bestätigt die Senatsverwaltung, dass[auch Passwörter abgeflossen sind](https://www.heise.de/news/Berlin-Passwoerter-abgeflossen-12-000-Systeme-werden-gescannt-11436809.html) . Die Mitarbeiter der beiden Verwaltungen könnten daher derzeit nicht aus dem Home Office arbeiten. Alle 12.000 Systeme des Landes Berlin würden derzeit „rund um die Uhr“ überprüft.
- **4. September 2026:** Die Kriminellen veröffentlichen[rund 1,44 Millionen Dateien im Darknet](https://www.heise.de/news/Berliner-Senat-zahlt-nicht-sensible-Daten-jetzt-im-Darknet-11442286.html) . Darunter sind auch Personalunterlagen, Angaben zu Disziplinarverfahren, Finanzunterlagen sowie Details zur Kritischen Infrastruktur des Landes Berlin.
- **5. September 2026:** Das BSI warnt vor einer „[erhöhten Bedrohungslage](https://www.heise.de/news/BSI-warnt-nach-Daten-Leak-vor-erhoehter-Cyber-Bedrohung-11442510.html) “ für die Gesellschaft.
- **6. September 2026:** Das Land Berlin[richtet eine „Steuerungseinheit“ ein](https://www.heise.de/news/Cyberangriff-Berlin-mit-Steuerungseinheit-will-Betroffene-kontaktieren-11442896.html) . Vom Leak Betroffene sollen per E-Mail und Brief kontaktiert werden. Politiker und IT-Experten zeigen sich schockiert von Umfang und Inhalt der veröffentlichten Daten.

Dabei handelt es sich um eine Variante der Malware-Kampagne „ClickFix“, vor der Microsoft schon im Februar 2026 gewarnt hat. Wie [bereits ausführlich beschrieben](https://www.heise.de/news/Nutzer-starten-Malware-ClickFix-Angriffskampagne-setzt-auf-Windows-Terminal-11202023.html), werden Nutzer mit ClickFix trickreich dazu gebracht, das Windows-Terminal auszuführen. Dort ist die PowerShell verfügbar, über die dem Betriebssystem Befehle etwa zum Kopieren von Dateien oder zum Ausführen von Programmen gegeben werden können.

TerminalFix unterscheidet sich von ClickFix vor allem dadurch, dass nicht das direkte Ausführen von Befehlen per **[Windows]** + **[R]** (wie „run“), sondern das Windows-Terminal durch **[Windows]** + **[X]** mit einem anschließenden Druck auf die Taste **[I]** für direkten Zugang zur PowerShell genutzt wird.

### Ein gefaktes Captcha verleitet zu Shell-Befehlen

Über die PowerShell wird dann ein bösartiger Befehl ausgeführt, welchen der Nutzer aus der Zwischenablage einfügen muss. Dort befindet er sich, weil er von einer manipulierten Webseite vor diesen Aktionen per JavaScript dorthin kopiert wurde. Diese Webseiten spiegeln, [so Microsoft](https://www.microsoft.com/en-us/security/blog/2026/08/28/terminalfix-campaign-deploys-reverse-tunnel-through-multistage-intrusion/), ein gefälschtes Captcha von Cloudflare vor. Hier liegt dann auch ein wenig Social Engineering vor, denn: Die echten Captchas von Cloudflare müssen, um effektiv zu sein, immer ein wenig anders aussehen und vom Nutzer verschiedene Dinge verlangen. Dass man dann auch mal ein paar Tasten drücken und nicht nur etwas anklicken muss, fällt unbedarften Benutzern vielleicht nicht sofort auf.

Der Befehl, der in der PowerShell landet, lädt per Skript im Hintergrund die erste Malware der Angreifer von deren Systemen herunter. Im Vordergrund fordert die manipulierte Webseite mit dem Fake-Captcha zu weiteren Aktionen auf. Der Nutzer ist also abgelenkt, während sein PC infiziert wird. Das Skript ruft unter anderem die signierte und gutartige Windows-Datei „LockScreenContentServer.exe“ auf, über die per Sideloading dann ein Teil der Malware als „dui70.dll“ installiert wird. Der Code darin lädt PNG-Bilddateien von den Angreifern herunter, in denen per Steganografie weitere Programme und DLLs versteckt sind.

### Persistente Malware und Proxy

Anschließend nistet sich das Paket an Schadsoftware persistent, also dauerhaft, per Registry-Keys auf dem angegriffenen System ein. Alle 60 Minuten prüft die Malware, ob sie noch läuft, und lauscht nach neuen Befehlen der Angreifer. Diese richten auch einen SOCKS-Proxy ein, haben also durch einen Tunnel Zugriff auf das Netz der attackierten Organisation. Was der Nutzer dort tut, kann also überwacht und abgefangen werden, sofern nicht alles sinnvoll verschlüsselt ist. Wie bei professionellen Angriffen üblich, werden all diese Aktionen verschleiert, unter anderem, indem die Dateien und Verzeichnisse vor bloßem Anzeigen im Windows-Explorer versteckt werden.

Videos by heise

In der Folge hören die Angreifer also mit und haben mindestens Zugriff auf die lokalen Dateien des Nutzers und auf die Verzeichnisse, die er abrufen kann. Von dort aus können sie sich weiterhangeln. Da bei den Berliner Behörden – wie bereits bestätigt wurde – auch [Passwortlisten im Klartext geführt wurden](https://www.heise.de/news/Berlin-Passwoerter-abgeflossen-12-000-Systeme-werden-gescannt-11436809.html), hatte Rhysida wohl relativ leichtes Spiel. Wie es dazu kam, dass die Kriminellen auch Zugriff auf offenbar die gesamten Daten der beiden Senatsverwaltungen hatten, ist noch ungeklärt.

### Öffentliche Verwaltungen sind ein leichtes Ziel

Damit all das klappen kann, muss die erste Zielperson nur zum Aufrufen einer entsprechend manipulierten Webseite verleitet werden und die dann wie beschrieben bedienen. Das kann etwa durch eine Phishing-Mail erfolgen oder durch einen Link per Social Media, in Foren oder auf Webseiten. Derlei Angriffe werden auch „Water-Holing“ genannt, da sie auf Webseiten platziert werden, an denen sich die Opfer regelmäßig einfinden – ähnlich einer Wasserstelle, die in der Savanne Tierherden anlockt.

Da die Namen und Mailadressen sowie Personalstrukturen von Behörden in der Regel mindestens teilweise öffentlich sind, ist Social Engineering leicht zu bewerkstelligen. Und selbst wenn das erst im vielleicht zwanzigsten Versuch erfolgreich ist: Für die [geforderten rund 2 Millionen Euro in Bitcoin](https://www.heise.de/news/30-Bitcoin-oder-Leak-Ransomware-Bande-erpresst-Berlin-11434325.html) lohnt sich der Aufwand.

Drohungen von Banden wie Rhysida sind im Übrigen sehr ernst zu nehmen. Wie das BSI unter Berufung auf einen nicht genannten externen Dienstleister berichtet, erfolgt in 92 Prozent der Fälle, in denen die Kriminellen mit einer Veröffentlichung drohen, diese auch. Rhysida konzentriert sich demnach vor allem auf den Gesundheits- und Bildungssektor – öffentliche Verwaltungen finden sich immerhin noch unter den fünf meistgenannten Zieltypen.

([nie](mailto:nie@heise.de))
