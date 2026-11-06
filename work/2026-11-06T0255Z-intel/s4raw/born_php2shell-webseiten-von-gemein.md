---
title: "php2shell: Webseiten von Gemeinden als Sorgenkind?"
author: Markus
url: https://borncity.com/blog/2026/11/03/php2shell-webseiten-von-gemeinden-als-sorgenkind/
hostname: borncity.com
description: Seit dem 21. Oktober 2026 hat das PHP-Projekt ja Patches zum Schließen zweier kritischer, php2shell genannter, Schwachstellen in PHP veröffentlicht. Während große Provider zeitnah patchten und Kunden…
sitename: Borns IT- und Windows-Blog
date: "2026-11-03"
categories: ['Sicherheit', 'Software']
tags: ['Sicherheit', 'Software']
fingerprint: f003609bcd8d27ce
---
Seit dem 21. Oktober 2026 hat das PHP-Projekt ja Patches zum Schließen zweier kritischer, php2shell genannter, Schwachstellen in PHP veröffentlicht. Während große Provider zeitnah patchten und Kunden absicherten, sieht die Situation bei "Selbst-Hostern" möglicherweise nicht so gut aus. Speziell Webseiten von Kommunen sind Sorgenkind.


## php2shell hier im Blog

Seit dem 21. Oktober 2026 hat das Thema php2shell, bezeichnet zwei schwere Sicherheitslücken (CVE-2026-109618 und CVE-2026-109619) in der Programmiersprache PHP, IT-Mitarbeiter ziemlich in Atem gehalten. So um die 70 % der Webseiten stützen sich auf PHP – und Produkte wie Joomla, WordPress etc. verwenden diese Programmiersprache als Basis.

Ich hatte hier im Blog ja zeitnah über dieses Thema berichtet (siehe Artikellinks am Beitragsende). Im Beitrag [php2shell: PHP-Updates und Nachlese](https://borncity.com/blog/2026/10/22/php2shell-php-updates-und-nachlese/) sind die verfügbaren PHP-Updates genannt und ich verweise auf eine Mitigations-Lösung eines belgischen Hosters für ältere PHP-Versionen. Die Artikel [php2Shell: Webseiten, die das Thema monitoren](https://borncity.com/blog/2026/10/24/php2shell-webseiten-die-das-thema-monitoren/) und [php2shell: NAS-Laufwerke und Windows betroffen; Prüf-Scripte und Analysen](https://borncity.com/blog/2026/10/30/php2shell-nas-laufwerke-und-windows-betroffen-pruef-scripte-und-analysen/) geben zudem Hinweise, wo es Hilfestellung gibt.

## Analyse der php2shell-Situation Ende Oktober 2026

Das Team von ShiftPress hat die Entwicklung rund um php2shell seit Veröffentlichung der PHP-Patches verfolgt. Rund 33 Stunden nach dem PHP2Shell-Update wurden die Startseiten von 54.743 Websites in Deutschland, Österreich und der Schweiz abgerufen und seitdem täglich nachgemessen.

### Jede fünfte Gemeinde-Website zeigt eine PHP-Reihe ohne Support

Von den 1.071 Gemeinde-Websites, die ihre PHP-Version offen zeigen, meldeten 21 Prozent beim Scan die PHP Version 8.1 oder älter. Für diese Reihen liefert das PHP-Team keine neuen Versionen mehr. Ob sie gegen PHP2Shell geschützt sind, hängt allein davon ab, ob der Hoster den Fix selbst eingebaut hat.

Viele Hoster haben genau das getan, ohne die Versionsnummer zu ändern, etwa Hetzner, Mittwald, DomainFactory, netcup, Hostinger und Infomaniak. Eine alte Nummer bedeutet deshalb nicht, dass eine Website ungeschützt ist. Sie bedeutet aber, dass der Schutz bei dieser und jeder nächsten Lücke vom Hoster abhängt.

Bei Hochschulen und Schulen lag der Anteil bei 19 Prozent, bei bekannten Websites mit .de, .at und .ch bei 26 Prozent. 255 Websites, davon 31 von Gemeinden, meldeten sogar noch PHP 5, für das es seit Ende 2018 keine Updates mehr gibt.

### Die gute Nachricht: Die Hoster waren schnell

Wo die PHP-Version sichtbar ist, zeigt die Messung ein schnelles Patch-Tempo: 73 Prozent der Gemeinde-Websites meldeten gut einen Tag nach dem Update bereits eine Version mit Fix. Mindestens 57 Websites zeigten statt ihrer Startseite einen Hinweis, dass sie wegen der Lücke vorsorglich abgeschaltet wurden, darunter 17 Gemeinden und Städte sowie 9 Schulen und Hochschulen. Weitere 9 Websites hatten einzelne Dienste abgeschaltet. Am 27. Oktober, sechs Tage nach dem Update, waren 34 der 57 abgeschalteten Websites wieder online, 19 zeigten weiter ihren Hinweis.

### Nachzügler ziehen nach

ShiftPress prüft die Websites mit einer älteren Versionsnummer seit der ersten Messung täglich nach. Von den 307 Websites, die bei der ersten Messung noch eine ältere Nummer der unterstützten Reihen 8.2 bis 8.5 zeigten, meldeten am 27. Oktober 81 Prozent die neue Version mit Fix. An dieser Stelle lässt sich eine erste vorsichtige Entwarnung geben – viele Hoster haben sichergestellt, dass ihre Kunden vor php2shell geschützt sind. Offen ist, ob es speziell bei selbst gehosteten Webseiten, deren PHP-Version nicht durch den Hoster aktualisiert wird, ungepatchte Systeme gibt.

"Die gute Nachricht ist, dass die großen Hoster schnell reagiert haben. Die schlechte: Für die meisten Websites kann niemand von außen sagen, ob sie sicher sind, oft nicht einmal der Betreiber selbst. Wer auf einer PHP-Version ohne Support läuft, sollte seinen Hoster schriftlich fragen, ob der Fix installiert ist, und den Wechsel auf eine aktuelle Version jetzt planen. Für PHP 8.2 endet der Support schon am 31. Dezember", sagt Alexander Spahn von ShiftPress.

Die aktuellen Ergebnisse der Messungen, derzeit mit Stand 1. November 2026 lassen sich auf der [ShiftPress-Webseite](https://shiftpress.ai/de/research/php2shell-studie-dach-2026) nachlesen.

Schon beeindruckend, was da an heißer Luft produziert wird. Da wird also von vielen "Dienstleistern" ständig alles "überwacht". Also Traffic erzeugt und ausgewertet in einer Art und Weise, die komplett ohne Aussage ist. Man weiß, dass man nichts weiß, aber es könnte ja.

Wer kannte vorher ShiftPress? Ich glaube hier geht es nur noch darum auf der Welle mitzuschwimmen, um Bekanntheit zu generieren (ich meine nicht diese Seite hier).

Und ja, auch die ganzen "Bösen" scannen täglich alle IPs um Lücken zu suchen.

Aber die Leute, die bis jetzt nicht aufgewacht sind, werden jetzt auch durch solche Experten nicht mehr aufwachen.

Vielleicht sollten wir aber auch den Gedanken von Herrn Altman weiterdenken und selbst gehostete Webseiten einfach verbieten. ;)

Sorry, musste mal raus und schöne Woche :)

Also meine Erfahrung ist, dass die meisten Gemeinden einen Dienstleister für sowas haben. Meine Erwartungshaltung wäre an dieser Stelle, dass der entsprechend reagiert hat und den Fix installiert hat. Die paar Gemeinden die selbst hosten, sind natürlich selbst in der Verantwortung.

Ich sehe da aber nicht mehr oder weniger Risko als bei den Internetauftritten von z.B. Kleinstgewerbe, dem Handwerksmeister um die Ecke, die Kfz-Bude oder der lokale Bäcker. Bei denen wird die Situation ähnlich sein.

Ich kann berichten, dass im Bereich Nordrhein-Westfalen sehr flott gehandelt wurde. Es wurde als allererstes alles vom Internet getrennt, was http spricht (egal ob php oder nicht). Danach wurden die Systeme evaluiert und nicht betroffene Systeme wieder ans Netz geschlossen. Im Anschluss wurden PHP-Systeme entsprechend ihrer wichtigkeit gepatched (wichtig als erstes, unwichtig erstmal offline gelassen und später patchen).

Die Patches sind inzwischen bereits seit einiger Zeit (eigentlich) überall eingespielt.

Im großen und ganzen bin ich tatsächlich sehr positiv überrascht, wie schnell und gut die Kommunen das gehandelt haben. Die meisten Webseiten waren tagesgleich wieder verfügbar.

"Im großen und ganzen bin ich tatsächlich sehr positiv überrascht, wie schnell und gut die Kommunen das gehandelt haben. Die meisten Webseiten waren tagesgleich wieder verfügbar."

Wie wurde verifiziert, dass dies tatsächlich für alle Kommunen gilt? Gibt es einen Nachweis, dass jede Kommune das Update bereits erhalten bzw. verarbeitet hat?

Ich weis von mindestens einem großen kommunalen Dienstleister/Internetprovider, der die Ports nicht nach außen wieder freischaltet, bis das update nicht verifiziert wurde.

Danke

Viel mehr Sorgen mache ich mir um private und Vereins-Webseiten und Foren, dort ist oft entweder die Kompetenz nicht da, oder es sind wegen veralteter Software, die auf PHP basiert, Updates oft nicht sehr einfach möglich, ohne z.B. das darauf laufende Forum, CMS und ähnliches anzufassen, oftmals auch zu lange nicht aktualisiert. Sowas wurde mal installiert, man war froh, dass es überhaupt funktioniert und das Vereinsmitglied, dass das mal eingerichtet hat, ist längst ausgetreten und es gibt keinen Nachfolger mit den Kenntnissen. Dementsprechend ist da noch viel Verwundbarkeit vorhanden, oder die Seiten sind momentan leider/wenigstens komplett abgeschaltet. Man könnte sich jetzt fragen, welcher Schaden kann überhaupt bei solchen Seiten entstehen? Vielleicht für die regulären Besucher nicht, aber wenn ein Angreifer per Reverse-Shell erstmal drauf ist, kann der ja weisgott dort alles anstellen, Phishing-Portale für bekannte Marken nachbilden, irgendwelche DDOS- oder sonstwas-Angriffe auf andere Adressen durchführen, Spam-Mails drüber leiten, usw.

Alexander Spahn von ShiftPress hier, die Zahlen stammen von uns. Herr Born hat vorgeschlagen, die Ergänzungen direkt hier in den Kommentaren zu bringen.

Zur Frage, wer ShiftPress ist: Wir sind kein Sicherheitsteam, sondern eine Webagentur, die Websites ohne PHP betreibt. Wir haben also ein eigenes Interesse an dem Thema. Deshalb stehen Methode und Zahlen zum Nachprüfen offen auf der Studienseite.

Eine Korrektur zu unserer Mitteilung: „täglich nachgemessen" war zu ungenau. Alle 54.743 Startseiten haben wir zweimal abgerufen (23. und 29. Oktober), ohne Test- oder Angriffscode. Täglich nachgeprüft haben wir nur Websites mit älterer Versionsnummer und die abgeschalteten.

@TBR: Einen solchen Nachweis kann unsere Messung nicht liefern. Sie sieht nur die Versionsnummer, die der Server selbst meldet. Bei 85 % der Gemeinde-Websites mit PHP lässt sich von außen nicht belegen, ob der Fix läuft. Was @Pong aus NRW berichtet, würden wir also oft gar nicht sehen.

Neu aus der zweiten Messung vom 29. Oktober:

Von den 225 Gemeinde-Websites mit PHP 8.1 oder älter zeigten 90 % dieselbe Nummer wie eine Woche zuvor, 4 % waren auf einer unterstützten Version mit Fix. Das heißt nicht „ungepatcht", sondern dass der Schutz weiter am Hoster hängt.

Von den 307 Websites mit älterer Nummer der Reihen 8.2 bis 8.5 zeigten 83 % die Version mit Fix.

36 Websites waren wegen der Lücke offline, darunter 10 Gemeinden und 12 Schulen und Hochschulen. Von den ursprünglich 57 waren 40 wieder online und 17 weiter offline, 19 kamen neu dazu.

@LO, @Gänseblümchen: Gemessen haben wir Gemeinden, Hochschulen, Schulen und bekannte .de-, .at- und .ch-Domains. Über Handwerksbetriebe, Vereine und private Foren sagen unsere Zahlen kaum etwas.

Methode und Daten: https://shiftpress.ai/de/research/php2shell-studie-dach-2026#welle-2
