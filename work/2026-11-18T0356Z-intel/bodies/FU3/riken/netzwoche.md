---
title: "Update: Auch EPFL und Uni Basel von Cyberattacke betroffen"
author: Uhr; René Jaun; Steve Wagner
url: https://www.netzwoche.ch/news/2020-05-18/supercomputer-unter-cyberbeschuss
hostname: netzwoche.ch
description: Mehrere Supercomputer sind im Mai in ganz Europa wegen kompromittierter SSH-Verbindungen gehackt worden. In der Schweiz waren neben der ETH Zürich und dem Swiss National Supercomputing Centre (CSCS) auch die EPFL und die Universität Basel betroffen.
sitename: netzwoche.ch
date: "2020-05-18"
fingerprint: "7ed5cb9ecdabd18d"
---
# Update: Auch EPFL und Uni Basel von Cyberattacke betroffen

Mehrere Supercomputer sind im Mai in ganz Europa wegen kompromittierter SSH-Verbindungen gehackt worden. In der Schweiz waren neben der ETH Zürich und dem Swiss National Supercomputing Centre (CSCS) auch die EPFL und die Universität Basel betroffen.

*Update vom 3. Juni 2020: Vor zwei Wochen sind mehrere Forschungseinrichtungen in Europa einer Reihe von Cyberangriffen auf ihre Supercomputer zum Opfer gefallen. In der Schweiz wurden die ETH Zürich und das Swiss National Supercomputing Centre (CSCS) in Lugano über kompromittierte SSH-Zugangsdaten attackiert. Aber auch die ETH Lausanne und die Universität Basel wurden angegriffen, berichtet RTS. Der Vorfall sei um den 14. und 15. Mai entdeckt worden, habe aber keinen Schaden angerichtet.*

*Die ETH Lausanne sagte auf Anfrage, dass sie trotz der Fälle von Angriffen, die auf mehreren europäischen Websites gemeldet wurden, nicht über "Beweise für ein wirkliches Eindringen" verfüge. Ausserdem sei kein Datendiebstahl festgestellt worden. Als Vorsichtsmassnahme würden jedoch alle Maschinen des Rechenclusters neu installiert, so eine EPFL-Sprecherin. "Es ist ein Standardverfahren, wenn man mit dieser Art von Risiko konfrontiert wird." Die Benutzer müssten auch ihre Passwörter und Zugangsschlüssel ändern.*

*Die Universität Basel bestätigte gegenüber der Redaktion, dass sie keine Hinweise auf Datenverlust oder andere Schäden an Systemen habe. Professor Torsten Schwede sagte, dass der Angriff dem gleichen Muster gefolgt sei wie anderswo in Europa: "Der anfängliche Zugriff auf die Systeme basierte auf kompromittierten SSH-Schlüsseln von Benutzerkonten, die von anderen HPC-Zentren bezogen wurden, gefolgt von einer Erweiterung der Zugriffsrechte nach der regulären Anmeldung am System." Seither, so die Universität Basel, wurden alle Benutzer-Credentials widerrufen, das HPC-Betriebssystem aktualisiert und der Zugriff auf die Systeme neu konfiguriert, um künftig Angriffe dieser Art zu verhindern. Das HPC-System wurde am 26. Mai wieder für Wissenschaftler geöffnet.*

*Der Vorfall wird zur Zeit von der Melde- und Analysestelle Informationssicherung (Melani) untersucht. Bis heute hat keine der angegriffenen Institutionen Einzelheiten über die Täter oder ihre Motive genannt. In der Zwischenzeit haben die Universität Basel und die ETH Zürich laut RTS bei ihren jeweiligen Staatsanwaltschaften eine Anzeige gegen unbekannt wegen unbefugten Eindringens in ein Datenverarbeitungssystem eingereicht.*

**Originalmeldung "Supercomputer unter Cyberbeschuss" vom 18. Mai 2020:** Eine Reihe von Cyberangriffen sorgt derzeit für viel Hektik unter Betreibern von Supercomputern. Seit Montag, 13. Mai, vermelden Forschungsinstitutionen aus ganz Europa Vorfälle, schalten die Systeme ab oder sperren zumindest den Benutzerzugriff darauf, schreibt "[ZDNet](https://www.zdnet.com/article/supercomputers-hacked-across-europe-to-mine-cryptocurrency/)". Bestätigte Angriffe meldeten demnach Einrichtungen im Vereinigten Königreich, Deutschland und der Schweiz. Gerüchteweise kommt noch ein weiterer Fall in Spanien dazu.

### "Fragen Sie uns nicht, wann die Cluster wieder zugänglich sind"

In der Schweiz vermelden die ETH und das nationale Hochleistungsrechenzentrum (CSCS) im Tessin Vorfälle, wie der "[Tagesanzeiger](https://www.tagesanzeiger.ch/eth-supercomputer-gehackt-370887112689)" berichtet. Bei der ETH seien die Supercomputer Euler und Leonhard betroffen. Da der Angriff über kompromitierte SSH-Zugänge erfolgt sei, wurde der Zugriff für Benutzer mittlerweile gesperrt, heisst es auf einer [Status-Seite](<https://scicomp.ethz.ch/wiki/Clusters_temporarily_closed_for_security_reasons_(14_May_2020)>).

"Die Cluster bleiben so lange geschlossen, bis wir wissen, wie der Angriff stattgefunden hat und wie wir unsere Systeme davor schützen können", heisst es dort. Und weiter: "Bitte kontaktieren Sie uns nicht, um zu fragen, wann sie wieder zugänglich sind." Man habe zum jetzigen Zeitpunkt nicht genügend Informationen, dies zu beantworten.

Auch das [CSCS](https://www.cscs.ch/publications/news/2020/shutdown-after-cyber-incident/) hat den externen Zugriff auf seine Systeme vorübergehend abgeschaltet. Beide Schweizer Institutionen betonen, dass die Supercomputer an sich weiter arbeiten. Die Wettervorhersagen von Meteoswiss, die am CSCS berechnet würden, seien durch den Angriff nicht beeinträchtigt, sagt Direktor Michele De Lorenzi gegenüber dem Tagesanzeiger.

### Cryptominer oder Datendiebe

Keine der angegriffenen Institutionen machte bislang weitere Angaben zu den Tätern oder ihren Motiven, allerdings veröffentlichte das Europäische Computer Security Incident Response Team (CSIRT) Teile des Malware-Codes, der für die Attacke genutzt wurde. Laut des US-amerikanischen Unternehmens Cado Security gehe daraus hervor, dass die Hacker versucht haben sollen, eine Software zum Schürfen der Kryptowährung Monero auf den Supercomputern zu installieren, wie Zdnet schreibt.

Aus den USA wurden Anfang vergangener Woche Beschuldigungen des FBI und des Ministeriums für Innere Sicherheit laut, dass China Institutionen und Forscher hacken lasse, die am Coronavirus und dessen Bekämpfung arbeiteten, schreibt "[Der Spiegel](https://www.spiegel.de/netzwelt/web/supercomputer-in-europa-gehackt-mindestens-neun-in-deutschland-betroffen-a-7d9403b9-c7ea-4f84-a9d7-17bbdff3a954)".

Es scheine jedoch eher unwahrscheinlich, dass die Angriffe auf die Supercomputer damit zusammenhängen. Denn zum Einen seien einige Systeme bereits im Januar angegriffen worden, während zum anderen auf manchen Maschinen auch heute gar keine Coronaforschung betrieben werde. Schliesslich habe keine der betroffenen Institutionen einen entsprechenden Datenabfluss feststellen können.

Der Supercomputer Piz Daint des CSCS gehört zu den schnellsten Maschinen der Welt. In einem [Ranking im vergangenen November](https://www.netzwoche.ch/news/2019-11-19/weniger-schweizer-mehr-chinesische-supercomputer) schaffte er es auf Platz 6. Da Dell und Eni inzwischen einen [noch schnelleren Rechner ans Netz genommen](https://www.netzwoche.ch/news/2020-02-18/dell-und-eni-bauen-fuenftschnellsten-supercomputer-der-welt) haben, fällt die Schweiz einen Platz zurück.
