---
title: "SAP unter Druck: Cyberangriff „Project Granite“ zielt auf GitHub-Entwicklung"
author: IT-BOLTWISE Redaktion
url: https://www.it-boltwise.de/sap-unter-druck-cyberangriff-project-granite-zielt-auf-github-entwicklung.html
hostname: it-boltwise.de
description: "SAP meldet einen aktiven Sicherheitsvorfall in der Softwareentwicklung: Laut Berichten sollen GitHub-Tokens gestohlen und Code verändert worden sein. Pipelines pausiert."
sitename: IT BOLTWISE x Super Intelligence
date: "2026-11-27"
categories: ['Hacker News']
tags: ['AI', 'Artificial Intelligence', 'Ci Cd', 'Code Signing', 'Cybersecurity', 'Github', 'Hacker', 'incident response', 'IT-Sicherheit', 'KI', 'Künstliche Intelligenz', 'Netzwerksicherheit', 'SAP', 'software supply chain', 'tokens', 'Walldorf']
fingerprint: "2ee0fe9c5e33dd67"
language: de
image: https://www.it-boltwise.de/wp-content/uploads/2026/11/ai-sap-project-granite-github-tokens-code-signing.jpg
pagetype: article
filedate: "2026-11-28"
---
**WALDORF / LONDON (IT BOLTWISE) – SAP reagiert auf einen Cyberangriff im Umfeld der Softwareentwicklung. Berichten zufolge sollen Angreifer Authentifizierungstokens von Mitarbeitenden gestohlen und damit Code auf GitHub kopiert sowie verändert haben. Intern werde das Geschehen unter „Project Granite“ als aktiver Sicherheitsvorfall behandelt; zugleich hat SAP GitHub-Zugriffe eingeschränkt, Build- und Delivery-Pipelines pausiert und Code-Signing-Keys rotiert. Offen bleibt, ob manipulierte Artefakte in Auslieferungen oder Kunden-Builds gelangt sind.**

[🧠 KI & Robotik auf Google News abonnieren](https://www.google.com/preferences/source?q=https://www.it-boltwise.de)

Der Vorfall trifft SAP mitten im Kern seiner Wertschöpfung: Nicht die IT-Infrastruktur für Anwenderdaten steht als erstes im Fokus, sondern die Kette, über die Quellcode zu signierten Software-Bausteinen wird. Laut Berichten, die sich auf Informationen aus dem Umfeld der Entwicklung stützen, sollen Angreifer Authentifizierungstokens entwendet haben, die SAP-Mitarbeitende für den Zugriff auf Entwicklerumgebungen nutzten. Damit konnten sie demnach Code auf GitHub kopieren und verändern; SAP behandelt das Ganze intern als aktiven Sicherheitsvorfall unter dem Codenamen „Project Granite“. Dass SAP keine Detailfreigaben zu Eintrittsweg, Identität der Angreifer oder konkret betroffenen Repositories macht, ist in solchen Fällen typisch, signalisiert aber vor allem eins: Die Untersuchung läuft noch, und die Schadensauswirkung lässt sich derzeit nicht vollständig eingrenzen.

Technisch ist das Muster bemerkenswert, weil es an zwei Stellen gleichzeitig angreift: erstens beim Identitäts- und Token-Handling und zweitens bei der Integrität des Lieferpfads. Tokens sind in modernen CI/CD-Setups (Continuous Integration/Continuous Delivery) häufig der Schlüssel zu automatisierten Schritten wie Build, Test, Signierung und Veröffentlichung. Wenn Token kompromittiert sind, reicht schon ein begrenztes Zeitfenster, um Gehaltslisten aus Änderungen in Commit-Historien zu erzeugen oder Artefakte mit manipuliertem Inhalt in nachgelagerte Jobs zu drücken. Genau darauf zielt der Bericht über SAPs Reaktion: GitHub-Zugriffe wurden eingeschränkt, automatische Build- und Delivery-Pipelines wurden pausiert und Code-Signing-Keys wurden rotiert. Diese Kombination adressiert zwei Risikokategorien – missbräuchliche Authentifizierung und das Risiko, dass signierte Binärartefakte mit manipuliertem Quellcode entstehen.

Bemerkenswert ist zudem, wie schnell solche Reaktionen organisatorisch durchschlagen müssen. Wenn SAP „viele Entwicklungsteams“ betrifft, dann bedeutet das in der Praxis, dass Berechtigungen nicht nur zentral entzogen werden, sondern Teams parallel prüfen müssen, ob ihre lokalen Umgebungen, ihre temporären Credentials und ihre Arbeitskopien kompromittiert sein könnten. In der Meldung heißt es, Mitarbeitende seien aufgefordert worden, ihre Zugangsdaten zu überprüfen und zu ändern. Diese Schritte wirken zwar wie „Routine“, sind aber in einem Supply-Chain-Szenario entscheidend: Selbst wenn die zentrale Plattform gesperrt wird, kann ein kompromittierter Credential-Legacy-Schatten in einer lokalen Pipeline oder einem Runner weiterarbeiten. Rotierte Code-Signing-Keys sollen außerdem sicherstellen, dass später veröffentlichte Versionen künftig eindeutig nachvollziehbar signiert sind und keine kompromittierten Vertrauensanker mehr nutzen.

Die eigentliche Frage für Unternehmen, die SAP-Systeme nutzen, lautet jedoch nicht nur „Wie kam es dazu?“, sondern „Was ist daraus geworden?“. SAP hat nach eigener Darstellung keine Hinweise auf unautorisierte Zugriffe auf Kundendaten gefunden; gleichzeitig bleibt offen, ob veränderte Codebestandteile veröffentlicht wurden oder ob sie in Kunden-Builds beziehungsweise in spätere Auslieferungen gelangt sind. Das ist für die Bewertung der Risikoexposition entscheidend, weil sich Supply-Chain-Angriffe in der Wirkung stark unterscheiden: Vom reinen Löschen und Verwässern von Commits bis zum Einspeisen schädlicher Logik reicht die Bandbreite, und die Abgrenzung gelingt erst, wenn Integritätsnachweise, Build-Logs und veröffentlichte Artefakte ausgewertet sind. Interessant ist hier auch der zeitliche Kontext: Der Vorfall fällt auf dasselbe Datum, an dem über einen weiteren strategischen Umbau berichtet wurde, bei dem SAP laut Berichten über mögliche große Einsparmaßnahmen nachdenkt. In solchen Umbauphasen sind Entwicklungsprozesse und Kapazitäten zwar oft klarer getaktet, aber auch die Angriffsfläche kann steigen, wenn Teams parallel migrieren, neue Abläufe einführen oder Rollen wechseln.

Dass SAP bereits im April mit einer Kompromittierung offizieller Pakete rund um npm zu tun hatte, verstärkt die Relevanz des Musters. Einmal kompromittierte Supply-Chain-Komponenten sind selten „isolierte Ausrutscher“ – viel häufiger zeigt sich ein wiederkehrendes Risiko in der Kombination aus Abhängigkeiten, Authentifizierung und Release-Mechanik. Für die betroffenen Kunden bedeutet das: Sie sollten nicht nur auf die Incident-Kommunikation des Anbieters warten, sondern ihre eigenen Software-Builds und Update-Prozesse daraufhin prüfen, wie sie signierte Artefakte verifizieren, wie schnell sie auf Revisionen reagieren können und ob ihre SBOM-/Dependency-Strategien (Software Bill of Materials) die nötige Sichtbarkeit liefern. Gerade bei Finanz-, Lieferketten- und HR-Prozessen, in denen SAP-Systeme häufig als geschäftskritische Grundlage dienen, kann schon eine minimale Unklarheit darüber, welche Versionen aus einem Release-Train stammen, den Betriebsrisiko-Umgang dominieren.

Aus Branchenperspektive lohnt sich außerdem ein Blick auf die Rolle von KI in diesem Kontext – ohne dass SAP selbst das bestätigt. Laut Berichten wird erwähnt, dass Angreifer möglicherweise KI-gestützte Agenten genutzt haben könnten. Selbst falls das zutrifft, ändert es vor allem die Angriffsökonomie: KI kann helfen, relevantere Repository-Strukturen schneller zu finden, Änderungen konsistenter zu formulieren oder Sicherheitsprüfungen gezielter zu umgehen. Technisch bleibt aber der entscheidende Hebel derselbe: Tokens und Signierungsmechanismen sind die Vertrauensgrenze. Die Schritte, die SAP beschrieben hat – Pipeline-Stopps, Key-Rotation und Credential-Checks – sind deshalb nicht nur „Reaktion“, sondern ein Signal, dass man die Grundprinzipien von Zero Trust und Build-Integrity ernster nimmt. Für die nächsten Tage wird entscheidend sein, ob SAP den Umfang (betroffene Repositories, Zeitfenster, veröffentlichten Artefakte) sauber nachliefert und ob unabhängige Integritätsprüfungen in den Release-Ketten konsistent ausfallen.

**💳[Amazon-Kreditkarte mit 2.000 Euro Limit bestellen!](https://www.it-boltwise.de/freecard)**

**🔥[Heutige Hot Deals bei Amazon: Bis zu 80% Rabatte!](https://www.it-boltwise.de/sponsoreddeals)**

**🎉[Amazon Haul-Store für absolute Schnäppchenjäger!](https://www.amazon.de/-/en/haul/store?&linkCode=ll2&tag=boltwise-21&linkId=399013a5af0a4d143675bfd9301b35bc&language=en_GB&ref_=as_li_ss_tl&creatorsDisableRedirect=true)**

[Sense Robot Go KI-Go-Brett mit Roboterarm – Automatische Steinplatzierung, interaktives Lernen, Spielwiederholung – Intelligenter Weiqi-Trainer für Kinder & Erwachsene](https://www.amazon.de/dp/B0F2FHGYLX?tag=boltwise-21&linkCode=ogi&th=1&psc=1&creatorsDisableRedirect=true)

- ★ 23-stufiges KI-Go-Training – Für Spieler mit Grundkenntnissen der Regeln – Entwickelt als intelligenter Trainingspartner passt sich die KI Spielern von 18K bis 9D an. Ideal für alle, die die Grundregeln bereits beherrschen und ihr Spiel verbessern möchten.

[ENERGIZE LAB Eiliko Coral Pink - Ihr winziger KI-Charm-Roboter, der zu jedem täglichen Outfit passt, lustiges elektronisches Anhängerspielzeug, für Paare und beste Freunde](https://www.amazon.de/dp/B0FFGW349R?tag=boltwise-21&linkCode=ogi&th=1&psc=1&creatorsDisableRedirect=true)

- IHR EMOTIONALER AI-BEGLEITER: Eiliko ist mehr als nur ein Anhänger, es ist ein charismatischer KI-Freund. Mit einem dynamischen LED-Bildschirm, der eine Vielzahl von animierten Gesichtern und Ausdrucksformen anzeigt, reagiert er auf Ihre Interaktionen mit einzigartiger Persönlichkeit und Charme.

[Eilik – Interaktiver Desktop Roboter mit Persönlichkeit, lebendigen Animationen & Reaktionen, Touch-Steuerung, Mini-Spiele, emotionaler Roboter Freund und besonderes Geschenk für Kinder & Erwachsene](https://www.amazon.de/dp/B0C2C9LJNQ?tag=boltwise-21&linkCode=ogi&th=1&psc=1&creatorsDisableRedirect=true)

- 【MEHR LEBEN FÜR DEINEN SCHREIBTISCH】 Lerne Eilik kennen – deinen kleinen Roboter-Freund mit Persönlichkeit. Mit liebevollen Animationen, ausdrucksstarken Reaktionen und spielerischen Interaktionen bringt Eilik mehr Freude in deinen Alltag. Ob auf dem Schreibtisch, im Büro oder am Nachttisch – Eilik wird schnell zu einem vertrauten Begleiter für besondere Momente.

[Plantbot Upgraded Large Smart Flower Pot Pet Planter Robot with Artificial Intelligence, Time Temperature Display, and Numerous Expressive Animations Based, for Indoor Decoration, Gifts (White)](https://www.amazon.de/dp/B0FNRG2V5N?tag=boltwise-21&linkCode=ogi&th=1&psc=1&creatorsDisableRedirect=true)

- 【XL-Größe für gedeihende Pflanzen】Geben Sie Ihren Pflanzen den Raum, den sie verdienen! Unser verbessertes, großes 13,7 cm großes Design bietet Platz für Pflanzen mit einem Durchmesser von bis zu 8,9 cm und damit deutlich mehr Platz für Wurzelwachstum und Pflanzengesundheit im Vergleich zu kleineren, veralteten Modellen. Die Produktabmessungen betragen 13,6 x 13,6 x 13,2 cm und das Gerät wiegt nur 355 g.

[Loona KEYI Premium Haustier-Roboter mit Ladestation (Smarte AI ChatGPT-4o, Stimmen- & Gestensteuerung, Echtzeit-Interaktion, Heimüberwachung)](https://www.amazon.de/dp/B0DCF53PCH?tag=boltwise-21&linkCode=ogi&th=1&psc=1&creatorsDisableRedirect=true)

- V28 Update - JETZT MIT NEUEN FUNKTIONEN! Als Reaktion auf das Ladeproblem von Loona haben wir das automatische Aufladen 2.0 verbessert. Diese Optimierung hilft Loona, die Ladewege in verschiedenen Szenarien zu erkennen und anzupassen, um die Erfolgsquote beim automatischen Aufladen zu erhöhen. Mobile Hotspots können sich mit Loona verbinden und überwinden WLAN-Einschränkungen, sodass Sie jederzeit und überall mit Loona interagieren können.


[Künstliche Intelligenz: Dem Menschen überlegen – wie KI uns rettet und bedroht | Der Neurowissenschaftler, Psychiater und SPIEGEL-Bestsellerautor von »Digitale Demenz«](https://www.amazon.de/dp/3426448505?tag=boltwise-21&linkCode=ogi&th=1&psc=1&creatorsDisableRedirect=true)

*Ergänzungen und Infos bitte an die Redaktion per eMail an de-info\[at\]it-boltwise.de. Da wir bei KI-erzeugten News und Inhalten selten auftretende KI-Halluzinationen nicht ausschließen können, bitten wir Sie bei Falschangaben und Fehlinformationen uns via eMail zu kontaktieren und zu informieren. Bitte vergessen Sie nicht in der eMail die Artikel-Headline zu nennen:**"SAP unter Druck: Cyberangriff „Project Granite“ zielt auf GitHub-Entwicklung"**.*

Du hast einen wertvollen Beitrag oder Kommentar zum Artikel

**"[SAP unter Druck: Cyberangriff „Project Granite“ zielt auf GitHub-Entwicklung](https://www.it-boltwise.de/sap-unter-druck-cyberangriff-project-granite-zielt-auf-github-entwicklung.html)"**für unsere Leser?

 **Die aktuellen intelligenten Ringe, intelligenten Brillen, intelligenten Uhren oder KI-Smartphones auf Amazon entdecken!** (Sponsored) 


**Es werden alle Kommentare moderiert!**

Für eine offene Diskussion behalten wir uns vor, jeden Kommentar zu löschen, der nicht direkt auf das Thema abzielt oder nur den Zweck hat, Leser oder Autoren herabzuwürdigen. 

Wir möchten, dass respektvoll miteinander kommuniziert wird, so als ob die Diskussion mit real anwesenden Personen geführt wird. Dies machen wir für den Großteil unserer Leser, der sachlich und konstruktiv über ein Thema sprechen möchte. 

**Du willst nichts verpassen?**

Du möchtest über ähnliche News und Beiträge wie **"SAP unter Druck: Cyberangriff „Project Granite“ zielt auf GitHub-Entwicklung"** informiert werden? Neben der E-Mail-Benachrichtigung habt ihr auch die Möglichkeit, den Feed dieses Beitrags zu abonnieren. Wer natürlich alles lesen möchte, der sollte den RSS-Hauptfeed oder IT BOLTWISE® bei Google News wie auch bei Bing News abonnieren.

*Nutze die Google-Suchmaschine für eine weitere Themenrecherche: **»SAP unter Druck: Cyberangriff „Project Granite“ zielt auf GitHub-Entwicklung«** bei Google Deutschland suchen, bei Bing oder Google News!*
