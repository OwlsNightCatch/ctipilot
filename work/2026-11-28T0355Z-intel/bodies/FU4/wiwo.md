---
title: "Hackerangriff auf SAP: Warum der Vorfall auf GitHub alarmiert"
author: Thomas Kuhn
url: https://www.wiwo.de/unternehmen/it/hackerangriff-auf-sap-warum-der-vorfall-auf-github-alarmiert/100273346.html
hostname: wiwo.de
description: Wie genau Hacker den Day-Konzern attackierten, ist noch unklar. Doch allein, dass es so weit kommen konnte, alarmiert die Szene.
sitename: Wirtschaftswoche
date: "2026-11-27"
categories: ['Unternehmen']
fingerprint: "9e47be1e9aba23c9"
language: de
image: https://images.wiwo.de/QFph0V7V9mJl/cover/5568/3132/0/0/215/365/0.5/0.5/sap-headquarters-in-walldorf-im-rhein-neckar-kreis.-sap-headquarters-in-walldorf-in-the-rhine-ne.jpg
pagetype: article
filedate: "2026-11-28"
---
##  IT-Sicherheitsvorfall: Was die GitHub-Attacke für SAP so gefährlich macht 

Wenn Fremde in die Softwarewerkstatt eines Konzerns wie [SAP](https://www.wiwo.de/boerse/isin/DE0007164600) gelangen, [wie das der Walldorfer Konzern am Donnerstag bestätigt hat, geht es nicht mehr nur um SAP](https://www.wiwo.de/unternehmen/it/cyberangriff-auf-sap-was-zum-vorfall-bei-github-bekannt-ist/100273210.html). Es geht, speziell für die Kunden und Partner des Konzerns, um die Frage, ob in den Programmen, die Hunderttausende Unternehmen und Behörden regelmäßig einspielen, noch das steckt, was draufsteht. Ob sie den SAP-Anwendungen noch vertrauen können? Oder haben Unbekannte Programmcode kopiert, womöglich schon verändert? Sind digitale Siegel in falsche Hände geraten?

Antworten auf all diese Fragen gibt es bislang kaum. [SAP](https://www.wiwo.de/themen/sap) bestätigt nur „verdächtige Aktivitäten“ auf der Entwicklerplattform GitHub und betont, man habe „Schutzmaßnahmen ergriffen“. Intern läuft der Vorfall laut Medienberichten unter dem Codenamen „Project Granite“. 

Wann, wie und durch wen die „Aktivitäten“ erfolgten, ist offen. Von einem Hackerangriff spricht der Konzern nicht. Hinweise auf unbefugten Zugriff auf Kundendaten gebe es nach aktuellem Stand auch nicht, betont man in Walldorf. Doch so weit muss es gar nicht gekommen sein. Schon die Möglichkeit eines Einbruchs in die Softwareproduktion alarmiert Fachleute – unabhängig davon, was tatsächlich geschah.

Man muss sich SAP weniger als Verkäufer fertiger Programme vorstellen, denn als Großbäckerei für die Verwaltung der Wirtschaft. Nach SAP-Angaben nutzen weltweit gut 320.000 Unternehmen und Behörden die Software, in der Buchhaltung, Lohnabrechnung, Lieferketten und zahlreiche weitere Funktionen zusammenlaufen.

### Ist die Backstube noch sauber?

Wer diese Module – bleiben wir im Sprachbild, diese „Brote“ – regelmäßig frisch bezieht, als Updates und neue Programmversionen, prüft nicht jede Zutat nach. Er vertraut darauf, dass die Backstube sauber, SAPs Softwareentwicklung frei von Eindringlingen, von Viren, Würmern oder anderem Schadcode ist.

Genau dieses Vertrauen macht sie zum beliebten Ziel von Angreifern. Wer sich dort einnistet, muss nicht bei jedem Kunden einzeln einbrechen: Er mischt sein Gift in den Teig und die Kunden öffnen ihm beim Brotkauf selbst die Tür. [Fachleute nennen das einen Lieferkettenangriff.](https://www.wiwo.de/technologie/cybersecurity-hackerattacken-its-the-lieferkette-stupid/27794806.html)

Das [bekannteste Beispiel für solche Attacken ist SolarWinds:](https://www.wiwo.de/politik/ausland/cybersicherheit-hackerangriff-auf-us-regierungsnetzwerk-hat-erhebliche-auswirkungen/26726924.html) 2020 unterwanderten Angreifer, mutmaßlich im Auftrag russischer Geheimdienste (die Regierung in Moskau bestritt das), die Programmentwicklung des US-Anbieters und versteckten in der Software eigenen Schadcode, der ihnen später die Tür zu den IT-Systemen der Kunden öffnete. Rund 18.000 von etwa 33.000 Kunden der betroffenen Software installierten das von den Hackern präparierte Update, darunter US-Behörden.


### Schlüssel, Siegel, Bauplan

Drei Dinge machen den Zugriff auf eine Entwicklungsumgebung so heikel. Erstens der Quellcode, der Bauplan der Software selbst: Wer ihn im Detail lesen kann, findet womöglich Schwachstellen, die der Hersteller selbst bisher nicht kennt. Zweitens die Möglichkeit, ihn die Software zu verändern: Ein paar unscheinbare Zeilen genügen für eine Hintertür, die später unbemerkt mitgeliefert wird. Drittens die Signaturschlüssel, eine Art digitaler Notarstempel, mit dem ein Hersteller bescheinigt, dass ein Programm von ihm stammt. Wer ihn besitzt, kann Fälschungen beglaubigen – und kein Kunde würde es merken.

Genau diese Szenarien stehen nun im Raum. Nach Informationen des „Spiegel“, der als Erster über den Fall berichtete, sollen Angreifer Zugangsschlüssel von SAP-Mitarbeitern gestohlen und damit Code auf GitHub kopiert und verändert haben, womöglich mithilfe von KI‑Agenten. [Das „Handelsblatt“ berichtet aus Konzernkreisen](https://www.handelsblatt.com/technik/ki/sap-it-sicherheitsvorfall-kunden-fordern-lueckenlose-aufklaerung/100273138.html), SAP habe den GitHub-Zugriff eingeschränkt, automatisierte Entwicklungsabläufe gestoppt und Signaturschlüssel ausgetauscht – was ein vorsorgliches Umsiegeln mit neuen Notarstempeln nahelegt. Ein Beleg ist es nicht, SAP hat beides nicht bestätigt.

Als Eintrittskarte zur Entwicklungsplattform dienen in solchen Fällen sogenannte Token: eine Art digitale Zimmerkarten für die Entwickler, die ohne erneute Passworteingabe Zugang gewähren, je nach Rechten zum Anschauen des Programmcodes oder zum Umbauen.


Kriminelle könnten Quellcode als Druckmittel nutzen oder Schwachstellen verkaufen, staatsnahe Hacker auf stille, dauerhafte Hintertüren in Ministerien und Konzernen zielen, Hacktivisten ihre Opfer bloßstellen oder stören wollen. Hinzu kommt das Tempo: Wenn KI-Agenten Lücken schneller aufspüren, als Menschen sie schließen, schrumpft der Vorsprung der Verteidiger. Das Bundesamt für Sicherheit in der Informationstechnik hat bereits vor agentischen Angriffswerkzeugen gewarnt.

Dass ein Konzern wie SAP, den Außenstehende als eigenständiges Softwarehaus wahrnehmen, seine Software-Baupläne ausgerechnet beim Dienst der Microsoft-Tochter GitHub verwaltet, wirkt widersprüchlich. Praktisch ist das aber kaum anders möglich. Denn GitHub fungiert als gemeinsames Aktenarchiv samt Werkbank für Programmcode mit separierten Entwicklungsumgebungen, zu denen im Normalfall nur SAP-Kräfte Zugriff haben. Bei laut SAP rund 110.000 Beschäftigten – natürlich nicht alles Entwickler – in 157 Ländern ist das unverzichtbar: Jede Änderung wird festgehalten, von Kollegen geprüft und freigegeben. Zudem laufen dort automatische Prüf- und Fertigungsstraßen, die Programme testen, verpacken und veröffentlichen. SAP stellt außerdem Werkzeuge und Open-Source-Projekte öffentlich bereit.


[Microsoft kaufte GitHub 2018 für 7,5 Milliarden Dollar in Aktien](https://www.wiwo.de/unternehmen/it/software-entwicklungsplattform-microsoft-uebernimmt-github-fuer-7-5-milliarden-dollar/22641208.html); schon damals nutzten rund 28 Millionen Entwickler den Dienst. Ein Industrievertreter nannte ihn seinerzeit den „De-facto-Standard in der Softwareentwicklung“. Die Kehrseite: Wer sich auf einen Standard verlässt, macht ihn auch zum Angriffsziel. Sicherheitsexperten berichten, GitHub stehe seit Monaten im Fokus von Kriminellen, die immer wieder Tausende Projekte kaperten. Hinweise, dass GitHub im konkreten Fall selbst gehackt wurde, gibt es bislang nicht; die Berichte betreffen SAP-Konten.

SAPs Aussage zu Kundendaten ist wichtig. Doch sie beantwortet eine andere Frage als die nach der Unversehrtheit der Software. Ob manipulierter Code in Updates gelangte, hat der Konzern öffentlich nicht beantwortet; „BleepingComputer“ zitiert SAP mit der Aussage, bislang keine Belege für kompromittierte Kundensysteme zu haben. Ob Kunden aktiv werden müssen, ließ SAP bisher offen. Schon im April waren mehrere offizielle SAP-Softwarepakete mit Schadcode präpariert worden; ein Zusammenhang zum aktuellen Fall ist aber nicht belegt. 

Ob die Backstube sauber ist, muss sich erst zeigen. Die nächsten Tage entscheiden, ob aus „verdächtigen Aktivitäten“ eine Randnotiz oder ein Lehrstück wird.
