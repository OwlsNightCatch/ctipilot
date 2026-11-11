---
title: "Kühl- und Kältesteuerungen: Systeme identifizieren, aktualisieren und schützen"
url: https://www.bacs.admin.ch/de/warnung-kuehlanlagen-de
hostname: admin.ch
description: Die in den vergangenen Wochen bekannt gewordenen Angriffe auf Kühlsteuerungen zeigen, dass auch die Schweiz von dieser Bedrohung betroffen ist. Mehrere Vorfälle in Europa und der Schweiz verdeutlichen, dass verwundbare Kühl- und Kältesteuerungen weiterhin erfolgreich angegriffen werden können und die empfohlenen Schutzmassnahmen nicht überall umgesetzt wurden.
sitename: bacs.admin.ch
date: "2026-11-10"
fingerprint: "1693173f0dbdcb0d"
---
# Kühl- und Kältesteuerungen: Systeme identifizieren, aktualisieren und schützen

**Die in den vergangenen Wochen bekannt gewordenen Angriffe auf Kühlsteuerungen zeigen, dass auch die Schweiz von dieser Bedrohung betroffen ist. Mehrere Vorfälle in Europa und der Schweiz verdeutlichen, dass verwundbare Kühl- und Kältesteuerungen weiterhin erfolgreich angegriffen werden können und die empfohlenen Schutzmassnahmen nicht überall umgesetzt wurden.**

Das BACS hat die Betreiberinnen von kritischen Infrastrukturen bereits nach den Vorfällen in Frankreich über die Fachplattform [Cyber Security Hub (CSH)](https://security-hub.ncsc.admin.ch/#/posts/13054) gewarnt. Da die betroffenen Systeme auch bei kleinen und mittleren Unternehmen (KMU) weit verbreitet sind, weist das BACS erneut auf die Risiken hin. Organisationen wird empfohlen, ihre eingesetzten Kühl- und Kältesteuerungen zu identifizieren, deren Erreichbarkeit aus dem Internet zu überprüfen und die empfohlenen Schutzmassnahmen umzusetzen.

## Worum geht es?

In den vergangenen Wochen wurden in mehreren europäischen Ländern, darunter auch in der Schweiz, Angriffe auf Kühlsteuerungen bekannt. Zunächst standen drei Steuerungssysteme von Danfoss im Fokus: die End-of-Life-Produkte **AK-SM 800 System Manager** und **AK-SC 355** sowie die aktuelle Produktfamilie **AK-SM 800A / AK-SM 8xxA**, sofern diese mit veralteter Firmware betrieben werden.

In der Folge wurden auch Kühlmanagementsysteme der Produktfamilie **Copeland/Dixell XWEB** als potenziell betroffen identifiziert. Insbesondere für ältere, nicht mehr unterstützte Systeme wurden [Schutz- und Migrationsmassnahmen empfohlen](https://cert.cyber.gouv.fr/alerte/CERTFR-2026-ALE-012).

Den bisherigen Erkenntnissen zufolge verschaffen sich Angreifer Zugriff auf Managementschnittstellen, die direkt aus dem Internet erreichbar sind. Nach einer erfolgreichen Kompromittierung können sie Einstellungen von Kühlanlagen aus der Ferne verändern, beispielsweise Temperaturen, Abtauzyklen, Alarmgrenzwerte oder Benachrichtigungseinstellungen. Manipulierte Kühlanlagen können zum Verderb von Lebensmitteln, Medikamenten oder anderen temperatursensitiven Gütern führen und dadurch finanzielle Schäden sowie Betriebsunterbrüche verursachen. Neben Vorfällen im Lebensmittelsektor wurden im Ausland auch Vorfälle im Gesundheitswesen bekannt.

Die bislang bekannten Fälle zeigen, dass weiterhin verwundbare oder unzureichend geschützte Systeme betrieben werden. Organisationen sollten deshalb prüfen, ob die genannten Steuerungssysteme eingesetzt werden und ob diese direkt oder indirekt aus dem Internet erreichbar sind.

## Wer ist betroffen?

Die Problematik betrifft nicht nur den Lebensmittelhandel. Kühl- und Kältesteuerungen werden ausserdem unter anderem eingesetzt in:

- Metzgereien und Lebensmittelproduktionsbetrieben;
- Restaurants und Hotels;
- Apotheken;
- Arztpraxen und Laboratorien;
- Logistik- und Lagerbetrieben;
- Industrie- und Produktionsanlagen;
- Landwirtschaftlichen Betrieben.

Vielen Unternehmen ist nicht bewusst, dass ihre Kälteanlagen direkt oder indirekt aus dem Internet erreichbar sind oder von externen Dienstleistern betrieben werden.

## Empfehlungen

Das BACS empfiehlt, die folgenden Massnahmen zeitnah umzusetzen:

- **Prüfen Sie, ob Kühl- oder Kältesteuerungen in Ihrem Unternehmen eingesetzt werden**
Berücksichtigen Sie dabei auch Systeme, die durch externe Dienstleister gewartet oder betrieben werden.
- **Installieren Sie verfügbare Sicherheits- und Firmware-Updates**
Folgen Sie den Empfehlungen des Herstellers. Für die Produktfamilie**AK-SM 800A / AK-SM 8xxA** stehen Sicherheitsupdates zur Verfügung, welche die bekannten Schwachstellen beheben. Neuere Firmware-Versionen aktivieren zudem zusätzliche Schutzmechanismen und erzwingen die verschlüsselte Kommunikation über HTTPS.
- **Treffen Sie besondere Schutzmassnahmen für nicht mehr unterstützte Systeme**
Ältere Systeme, die keine Sicherheitsupdates mehr erhalten, sollten nicht direkt aus dem Internet erreichbar sein. Falls ein Betrieb weiterhin erforderlich ist, sollte der Zugriff konsequent auf vertrauenswürdige Netze oder VPN-Zugänge beschränkt werden.
- **Beschränken Sie den Fernzugriff auf Kühl- und Kältesteuerungen**
Managementschnittstellen sollten nicht direkt aus dem Internet erreichbar sein. Wenn möglich, sind die Systeme vom Internet zu trennen oder der Zugriff auf vertrauenswürdige IP-Adressen beziehungsweise einen geschützten VPN-Zugang zu beschränken. Der Fernzugriff sollte über einen zentral verwalteten Zugangspunkt erfolgen. Standardpasswörter sollten unverzüglich geändert und durch sichere, individuelle Passwörter ersetzt werden.
- **Ersetzen Sie Systeme, die keine Sicherheitsupdates mehr erhalten**
End-of-Life-Produkte stellen ein erhöhtes Risiko dar und sollten möglichst rasch durch unterstützte Systeme ersetzt werden.

## Weiterführende Informationen

[Massnahmen zum Schutz von IoT Geräten](https://www.bacs.admin.ch/de/massnahmen-zum-schutz-von-iot-geraeten)

[Cyber Security Hub (CSH)](https://security-hub.ncsc.admin.ch/#/posts/13054) (Englisch)

[CERT-FR](https://cert.cyber.gouv.fr/alerte/CERTFR-2026-ALE-012/) (Französisch)

[BSI](https://www.allianz-fuer-cybersicherheit.de/SharedDocs/Downloads/Webs/ACS/DE/BSI-CS/BSI-CS_154.html)
