---
title: Basler Datenschützerin stoppt Cloud-Pläne für das Kantonsnetz- wegen Prisma Access von Palo Alto Networks
author: Avongunten; Adrienne Fichter
url: https://dnip.ch/2026/11/25/basler-datenschuetzerin-stoppt-cloud-plaene-fuer-das-kantonsnetz-wegen-prisma-access-von-palo-alto-networks/
hostname: dnip.ch
description: Die Basler Datenschutzbeauftragte Danielle Kaufmann hat letzte Woche für einen Paukenschlag gesorgt. Per Medienmitteilung gab sie bekannt, dass sie eine
sitename: Das Netz ist politisch
date: "2026-11-25"
categories: ['Uncategorized']
fingerprint: "6cb439a1cabfbce"
license: CC BY 4.0
language: de
image: https://dnip.ch/wp-content/uploads/2026/11/danny144-map-4636843-1024x655.jpg
pagetype: article
filedate: "2026-11-27"
---
Die Basler Datenschutzbeauftragte Danielle Kaufmann [hat letzte Woche für einen Paukenschlag gesorgt. Per Medienmitteilung gab sie bekannt, dass sie eine verbindliche Weisung erlassen hat:](https://www.bs.ch/news/2026-weisung-zur-auslagerung-der-kantonalen-vpn-und-web-proxy-loesungen-die-cloud) Die geplante Cloud-Lösung für den Fernzugriff auf das kantonale Netz darf nicht eingesetzt werden. Betroffen ist damit der Dreh- und Angelpunkt zwischen dem internen Verwaltungsnetz, den Geräten der Angestellten und dem offenen Internet.

Dieser Knotenpunkt erfüllt zwei Funktionen. Die erste ist das «VPN» («Remote Access»): Darüber gelangen Geräte von ausserhalb in das Netzwerk des Kantons. Die zweite ist der «Web Proxy»: Über ihn erhalten die Kantonsangestellten Zugang zur Welt draussen, also zu externen Websites. Das gilt auch, wenn sie unterwegs oder im Homeoffice arbeiten. Dann verbinden sie sich zuerst per VPN mit der Infrastruktur der Kantonsverwaltung und surfen von dort aus über den Web Proxy ins Internet.

Warum also hat die Datenschützerin durchgegriffen?

In ihrer Mitteilung begründet sie das hiermit: *«Die Kantonsverwaltung plant, ihre bis jetzt lokal betriebenen IT-Lösungen für den sicheren Zugriff auf das kantonale Netzwerk, den ‹Remote Access› oder ‹VPN›, und die Steuerung des Internetzugriffs, den ‹Web Proxy›, in eine Cloud-Lösung eines US-amerikanischen Anbieters auszulagern. Das bedeutet, dass künftig ein Grossteil des Datenverkehrs über diesen Anbieter verlaufen würde. Es ist vorgesehen, dass der Anbieter die Verschlüsselung aufbricht.»*

Starker Tobak. Vor allem wenn man sieht um welche Daten der Basler Einwohner:innen es sich handeln würde:

„…einschliesslich besonderer Personendaten (z.B. Gesundheitsdaten) und Daten, die einer besonderer Geheimhaltungspflicht unterstehen (z.B. Steuerdaten). Betroffen wären etwa jegliche Word-Dateien, Verfahrensakten, Passwörter, staatssicherheitsrelevante Informationen etc.“

Natürlich stellt sich sofort die Frage: Um welchen Anbieter und welches Produkt geht es?

Die Datenschützerin war für eine Stellungnahme nicht erreichbar. Den Inhalt der Weisung beziehungsweise Verfügung habe ich deshalb nicht einsehen können. Auch das Finanzdepartement, dem die kantonale IT unterstellt ist, will die Frage nicht beantworten: «Wir prüfen die Einsprache der DSB inhaltlich und juristisch und bitten Sie um Verständnis, dass wir aufgrund des laufenden Verfahrens keine weiteren Informationen geben können.»

Auch in der Mediendatenbank findet sich nichts dazu. Einzig «[Inside IT» berichtete im September 2025](https://www.inside-it.ch/basel-stadt-loest-vpn-infrastruktur-fuer-11-millionen-ab-20250924), dass der IT-Dienstleister BNC mit Hauptsitz in Urtenen-Schönbühl bei Bern den Zuschlag für den Betrieb und die Ablösung der veralteten VPN-Infrastruktur des Kantons erhalten hat. In der Ausschreibung heisst es: «Aufgrund wachsender Bedrohungslagen, steigender Sicherheitsanforderungen und der Notwendigkeit einer flexibleren, standortunabhängigen Arbeitsweise soll nun eine Zero-Trust-Network-Access-Lösung (ZTNA) implementiert werden.» Um welche Technologie es sich handelt, wird nicht erwähnt.

Mehrere Quellen aus der kantonalen IT bestätigen nun: Es handelt sich um Palo Alto Networks, konkret um eine Lizenz für «Prisma Access» – einen Dienst, bei dem der Datenverkehr über die Cloud von Palo Alto läuft.

Der [Anwalt Martin Steiger hatte das bereits aus öffentlich zugänglichen Informationen hergeleitet.](https://steigerlegal.ch/2026/11/21/datenschutzbeauftragte-basel-stadt-auslegerung-cloud-dienst/) Der Auftrag an die BNC AG wurde wie folgt beschrieben:

*«Das Ziel des Projekts INFRA21+ / Remote Access / ZTNA ist, die bisherige VPN-basierte Remote Access Infrastruktur sowie den Secure Web Gateway durch eine **zukunftsfähige, hochsichere und flexible Zero Trust Network Access (ZTNA)-Lösung** abzulösen. Diese Lösung soll die Anforderungen der modernen Arbeitswelt abdecken, indem sie sichere und ortsunabhängige Zugänge zu den IT-Diensten und -Systemen ermöglicht*.»

Die damalige BNC AG, die inzwischen Axians BNC AG heisst, bezeichnete sich öffentlich als «Diamond Innovator Partner von Palo Alto Networks». Die Partnerschaft bestätigt Axians BNC auch auf der eigenen Website.

Und Palo Alto Networks [habe mit «Prisma Access» genau den passenden Cloud-Dienst im Angebot:](https://docs.paloaltonetworks.com/translated/german) Er umfasst unter anderem die ausgeschriebenen Funktionen «Zero Trust Network Access (ZTNA)» für den Zugriff auf interne Anwendungen sowie einen «Cloud Secure Web Gateway», der den Internetverkehr einschliesslich Inhaltsprüfung kontrolliert.

Diese Vermutung haben mehrere IT-Mitarbeitende bestätigt.

Inhalte

[Toggle](https://dnip.ch/2026/11/25/basler-datenschuetzerin-stoppt-cloud-plaene-fuer-das-kantonsnetz-wegen-prisma-access-von-palo-alto-networks/)

## Was ändert sich mit der Cloud-Lösung?

Heute läuft alles im eigenen Haus, «on premises», wie es im IT-Jargon heisst. VPN-Gateway und Web Proxy stehen als Geräte in den Rechenzentren des Kantons und werden von dessen IT-Leuten betrieben. Wer im Homeoffice arbeitet, baut einen verschlüsselten Tunnel direkt zur Kantonsverwaltung auf. Erst dort, auf kantonseigener Hardware, wird entschieden, welche Website aufgerufen werden darf und welche nicht. Der Datenverkehr verlässt die Infrastruktur des Kantons erst, wenn er ins offene Internet geht.

Mit Prisma Access dreht sich das um. Der Tunnel endet nicht mehr in Basel, sondern in einem Rechenzentrum von Palo Alto Networks. Dort sitzen die Funktionen, die heute im Keller der Verwaltung stehen: Zugangskontrolle, Firewall, Web-Filter. Die Angestellten merken davon kaum etwas. Für die Daten hingegen ändert sich viel. Jeder Klick und jeder Seitenaufruf von mehreren Hunderten Kantonsangestellten, und je nach Konfiguration auch der Zugriff auf interne Fachanwendungen, läuft künftig zuerst über die Plattform eines privaten US-Konzerns.

Palo Alto bietet zwar einen Standort in Zürich an. Betrieben werden diese Knoten nach Angaben des Herstellers aber auf der Infrastruktur grosser Cloud-Anbieter wie Google Cloud oder Amazon Web Services. Damit stecken gleich zwei US-Firmen in der Lieferkette. Ein Serverstandort in Zürich bedeutet ohnehin nicht, dass die Daten dem Zugriff aus den USA entzogen sind.

## Warum die Verschlüsselung aufgebrochen wird

Heute ist fast der gesamte Webverkehr verschlüsselt, erkennbar am «https» und am Schloss-Symbol im Browser. Das schützt vor neugierigen Blicken, aber eben auch vor dem Blick der eigenen Sicherheitssysteme. Eine Firewall sieht dann nur, dass jemand mit einem Server kommuniziert, aber nicht, was übertragen wird. Schadsoftware, die über eine verschlüsselte Verbindung hereinkommt, oder vertrauliche Dokumente, die hinausgehen, bleiben unsichtbar.

Deshalb setzen Sicherheitsanbieter auf «SSL-Inspection» oder «TLS-Decryption». Technisch ist das ein kontrollierter «Man in the Middle»: Das System gibt sich gegenüber dem Gerät der Angestellten als die angefragte Website aus und baut gleichzeitig eine eigene, zweite verschlüsselte Verbindung zur echten Website auf. Dazwischen liegt der Inhalt im Klartext vor. Er wird geprüft und danach wieder verschlüsselt weitergeschickt. Damit das funktioniert, installiert die IT auf allen Geräten ein Zertifikat, mit dem diese Zwischenstation als vertrauenswürdig gilt. Palo Alto beschreibt diese Funktion in seiner Dokumentation ausdrücklich auch für Prisma Access.

Das ist gängige Praxis und an sich kein Skandal. Bisher geschah es aber auf Geräten des Kantons. Neu würden die Inhalte genau an jenem Punkt lesbar, der ausserhalb der kantonalen Kontrolle liegt: in der Cloud eines US-Anbieters.

Welche Websites ein:e Mitarbeiter:in aufruft, was in ein Webformular eingetippt wird, welche Dokumente hoch- oder heruntergeladen werden – all das läge dort für einen Moment offen. Und es unterliegt potenziell US-Recht, etwa dem Cloud Act, der US-Behörden unter bestimmten Bedingungen Zugriff auf Daten bei US-Firmen erlaubt, unabhängig vom Serverstandort.

Man darf deshalb gespannt sein, was bei der Prüfung durch das Finanzdepartement herauskommt. Vor allem würde ich gerne wissen, ob dies auf Druck des Herstellers zurückgeht, der die On Prem/Gateway-Lösung nicht mehr unterstützt.

Die Basler Datenschützerin sagt dazu:

*„Es ist für die geplante Auslagerung keine besondere Dringlichkeit nachgewiesen worden. Die bestehende, lokal-betriebene Lösung kann verlängert werden. Soweit bekannt, setzen auch die anderen Kantone für ihre VPN und Web Proxys weiterhin auf klassische, lokale Lösungen. Dies deutet darauf hin, dass valable, datenschutzkonforme Alternativen für den Betrieb von VPN und Web Proxy durchaus vorhanden sind.*„

## Basel-Stadt und Microsoft 365

An dieser Stelle [verweise ich auf einen früheren Beitrag von mir auf dnip.ch.](https://dnip.ch/2025/05/21/der-microsoft-report-teil-1-wie-die-kantone-die-quadratur-des-kreises-verkaufen-und-sich-dem-tech-giganten-unterwerfen/#Kanton-Basel-Stadt) Denn Basel-Stadt ist auch auf den Microsoft-Express-Zug aufgesprungen – wegen des berühmten Cloud-Zwangs durch den IT-Konzern.

Brisant dabei: Auch Finanz-, Sozial- und Gesundheitsdaten der Baslerinnen und Basler dürften in der Microsoft-Cloud landen. Die Basler Grossrätin Anina Ineichen (Grüne) stellte deshalb in einer Interpellation kritische Fragen an die zuständige Regierungsrätin Tanja Soland (SP). Diese entgegnete, der Schritt sei wegen der Cloud-Strategie von Microsoft notwendig. Dabei bot Microsoft gerade Kunden aus der öffentlichen Verwaltung sogar an, noch länger ohne Cloud auszukommen.

Die Medienmitteilung des Kantons mutete anachronistisch an. Sie sagte im Wesentlichen, eine Alternative zu Microsoft werde als «nicht realistisch, zu risikoreich und teuer beurteilt». Anachronistisch deshalb, weil wir uns in geopolitisch turbulenten Zeiten befinden – und weil die Einschätzung «nicht realistisch» heute sicher nicht mehr zutrifft. Vor vielleicht sechs Jahren hätte sie noch gegolten.

Soland behauptete etwa, Open-Source-Alternativen hätten in den Kantonen nicht funktioniert. Dabei gibt es ein prominentes Gegenbeispiel einer wichtigen Behörde: das Bundesgericht in Lausanne. Es arbeitet seit fast 20 Jahren mit Linux, LibreOffice und weiterer offener Software. Die Akzeptanz beim Personal sei gut, bestätigt ein Sprecher auf Anfrage. Und auch das deutsche Bundesland Schleswig-Holstein geht inzwischen diesen souveränen Open-Source-Weg.

Warum Microsoft 365 als alternativlos gilt, bleibt ein Rätsel. Gemäss einem Bundesgerichtsurteil von 2023 müssen Verwaltungen bei einer freihändigen Vergabe eigentlich genau begründen, warum es keine Alternative gibt. Eine solche Begründung liefern die meisten Kantonsverwaltungen kaum – ausser dass Microsoft sie mit seiner Cloud-Strategie dazu zwinge.

## Wer hat den Schlüssel?

SP-Regierungsrätin Tanja Soland behauptete in der Sitzung des Grossen Rates zudem, die Verwaltung sei im Besitz der «Schlüssel» für die Daten, die in den Schweizer Rechenzentren von Microsoft liegen. Doch Microsoft selbst räumt ein, dass eine Verschlüsselung, bei der wirklich nur der Kunde den Schlüssel hat («Double Key Encryption»), die Cloud weitgehend unbrauchbar macht. Der Konzern empfiehlt, diese Form der Verschlüsselung nur für rund 5 Prozent der Dokumente einzusetzen. Andernfalls funktionieren die meisten Dienste nicht mehr. Auch der Kanton Bern verzichtet laut seinem Risikobericht deswegen auf eine eigene Verschlüsselung.

Was also meinte Soland mit der behaupteten Schlüsselhoheit?

Ich hatte damals beim Kanton Basel-Stadt nachgefragt. Regierungssprecher Marco Greiner antwortete, gemeint sei der sogenannte «Customer Key»:

*«Die Verschlüsselungsthematik umfasst verschiedene Massnahmen. Im Bereich der Customer Managed Key Lösung setzt Basel-Stadt (neben anderen Sicherheitsmassnahmen) auf folgende Funktion: Overview of Customer Key – Microsoft Purview | Microsoft Learn. ‹Microsoft Purview Customer Key› wird zusätzlich mit ‹Microsoft Customer Lockbox› ergänzt – diese Funktion verhindert den Zugriff von Microsoft Mitarbeitenden (z.B. Supportmitarbeitende) auf unsere Daten. Sollte dies in einem Supportfall dennoch nötig sein, was äusserst selten vorkommt, muss jeder Zugriff von uns über einen ‹Lockbox Request› genehmigt werden. Ohne unsere Freigabe kann der Zugriff nicht erfolgen.»*

Mit „Customer Key“ sei somit die Schlüsselhoheit gemeint. Diesen Schlüssel verwaltet zwar die IT-Abteilung des Kantons. Doch jeder Microsoft-Server, der mit den Dokumenten arbeiten muss, erhält ihn anstandslos, automatisiert und innert Sekundenbruchteilen. Denn ohne Schlüssel könnten die Microsoft-Server im Auftrag der Basler Mitarbeiter:innen weder nach Dokumenten suchen noch diese anzeigen oder zum Bearbeiten bereitstellen. (Zudem hält Microsoft beim Customer Key einen eigenen «Availability Key»/Notfallschlüssel, mit dem sich Daten wiederherstellen lassen, falls der Kunde seine Schlüssel verliert.)

Die Lockbox ist tatsächlich eine Massnahme, die den Zugriff durch Microsoft-Mitarbeitende erschwert. Dass sie einen Zugriff im Ernstfall nicht verhindert, schreibt Microsoft allerdings selbst.

Immerhin räumt Greiner ein, dass sich Cloud- und On-Premises-Daten im Büroalltag nicht dauerhaft trennen lassen. On-Premises-Daten sind solche, die lokal auf eigenen Servern, etwa im Rechenzentrum der Verwaltung, gespeichert und bearbeitet werden:

*«Daten mit einem erhöhten Schutzbedarf – wie beispielsweise Sozial-, Gesundheits- oder Finanzdaten – werden weiterhin hauptsächlich in den lokalen Fachanwendungen bearbeitet und gespeichert. Die Nutzung von M365 ist aber auch für diese Datenkategorie grundsätzlich möglich. E-Mail-Programme, Kollaborationswerkzeuge und Dateiablagen von M365 für diese Datenkategorie grundsätzlich nicht zu verwenden, wäre in der Praxis kaum umsetzbar.*»

## Die erste, die durchgreift

Die Datenschutzbeauftragten sämtlicher Kantone hadern mit dem Entscheid ihrer Regierungen für Microsoft 365. Das zeigt auch die [Resolution von Privatim, der Konferenz der schweizerischen Datenschutzbeauftragten, vom November 2025 zur Nutzung internationaler Cloud-Dienste durch Behörden.](https://www.privatim.ch/de/publikation-resolution-zur-auslagerung-von-datenbearbeitungen-in-die-cloud/) Darin halten sie fest, dass besonders schützenswerte Personendaten und Daten, die einer gesetzlichen Geheimhaltungspflicht unterliegen, in den meisten Fällen nicht in internationale Cloud-Anwendungen ausgelagert werden dürfen – ausser die Behörde verschlüsselt die Daten selbst und der Anbieter hat keinen Zugriff auf den Schlüssel.

Trotz dieser klaren Haltung hat bisher noch keine Datenschutzbehörde die Zusammenarbeit mit einem US-Hyperscaler gestoppt, wie Martin Steiger treffend festhält. Die Initiative ging bisher von IT-Fachleuten ([siehe den Fall Luzern](https://www.republik.ch/2025/06/16/microsoft-es-knallt-in-den-kantonen)) und von Politiker:innen in den Kantonsparlamenten aus.

Die Basler Datenschutzbeauftragte Danielle Kaufmann ist nun die erste, die durchgreift. Vermutlich auch weil mit der Cloud-Entschlüsselung durch einen amerikanischen VPN-Anbieter der Fall auch am offensichtlichsten ist, weil dieser den ganzen Datenverkehr im Klartext mitlesen kann. [Man kann sich dem Votum von Martin Steiger nur anschliessen:](https://steigerlegal.ch/2026/11/21/datenschutzbeauftragte-basel-stadt-auslegerung-cloud-dienst/)

*«Mit ihrer verbindlichen Weisung setzt die Datenschutzbeauftragte ein klares Zeichen für den Schutz der Grundrechte der Menschen im Kanton Basel-Stadt. Sie können nicht wählen, mit welcher IT-Infrastruktur die kantonale Verwaltung ihre Daten bearbeitet.*»
