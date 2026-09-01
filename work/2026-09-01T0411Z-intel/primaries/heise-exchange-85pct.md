# extract: served via trafilatura-direct
---
title: "Exchange-Sicherheitslücke: 85 Prozent der On-Prem-Server in Deutschland anfällig"
author: Heise Online; Dirk Knop
url: https://www.heise.de/news/Exchange-Sicherheitsluecke-85-Prozent-der-On-Prem-Server-in-Deutschland-anfaellig-11434785.html
hostname: heise.de
description: Ein Proof-of-Concept-Exploit für eine hochriskante Exchange-Lücke ist öffentlich. 85 Prozent der On-Premises-Server sind anfällig.
sitename: Heise Online
date: "2026-08-31"
categories: ['IT']
tags: ['BSI, IT, Microsoft Exchange, On-Premises, Proof of concept, Security, Warnung']
---
# Exchange-Sicherheitslücke: 85 Prozent der On-Prem-Server in Deutschland anfällig

Ein Proof-of-Concept-Exploit für eine hochriskante Exchange-Lücke ist öffentlich. 85 Prozent der On-Premises-Server sind anfällig.

Kurz vor dem vergangenen Wochenende wurde ein [Proof-of-Concept-Exploit (PoC) gegen eine hochriskante Sicherheitslücke in Exchange-Servern](https://www.heise.de/news/Angriffe-erwartbar-Proof-of-Concept-fuer-Exchange-Luecke-veroeffentlicht-11431561.html) veröffentlicht. Als Teil einer Schwachstellenverkettung hilft er Angreifern, verwundbare Server zu übernehmen – durch den PoC sind Angriffe jetzt jederzeit zu erwarten. Das CERT-Bund des Bundesamts für Sicherheit in der Informationstechnik (BSI) hat nach unserer Anfrage Zahlen veröffentlicht: Der Großteil der On-Premises-Exchange-Server in Deutschland war am Freitag noch anfällig.

Das hat die IT-Sicherheitsbehörde auf [Mastodon bekanntgegeben](https://social.bund.de/@certbund/117171896801475447). Das BSI schreibt dort, dass der PoC-Exploit für die Sicherheitslücke CVE-2026-62911, die Microsoft am August-Patchday mit einem Softwareflicken gestopft hat, die Übernahme der Systeme aus dem Internet ohne vorherige Authentifizierung ermöglicht. „Aktuell sind jedoch noch rund 85 Prozent der on-premises Exchange-Server in Deutschland für diese Schwachstelle verwundbar“, erklärt das CERT-Bund des BSI dort. Seit dem 14. August benachrichtigt das BSI demnach deutsche Netzbetreiber bereits über die noch verwundbaren Systeme in ihren Netzen.

### Unbedingt Patches anwenden

Auch das BSI weist darauf hin, dass Betreiber von Exchange-Servern die bereitstehenden Aktualisierungen umgehend anwenden sollen. Für Exchange SE steht etwa das Sicherheitsupdate KB5121573 bereit. Für Exchange 2016 und 2019 lief der reguläre Support im Oktober 2025 aus, einen Patch können nur Teilnehmer am kostenpflichtigen Extended-Security-Updates-Programm (ESU) erhalten. „Aktuell sind uns in Deutschland jedoch nur 9 Exchange-Server 2016/2019 bekannt, auf denen im Rahmen von ESU herausgegebene Patches installiert sind“, weist das BSI eine konkrete Zahl aus. Wie viele alte Exchange-Server derzeit noch laufen, schreibt das BSI jedoch nicht. Die letzte Zahl stammt vom [Ende Oktober 2025, wo 92 Prozent der rund 33.000 On-Premises-Exchange-Server](https://www.bsi.bund.de/SharedDocs/Cybersicherheitswarnungen/DE/2025/2025-287772-1032_bits.html) in Deutschland noch mit den zu dem Zeitpunkt aus dem Support gefallenen Versionen liefen und aus dem Netz erreichbare OWA-Instanzen betrieben.

Videos by heise

Aktuell gibt das BSI daher auch den Tipp, Zugriffe auf Exchange nach Möglichkeit zu beschränken: „Das BSI empfiehlt grundsätzlich, den Zugriff aus dem Internet auf webbasierte Dienste eines Exchange-Servers auf vertrauenswürdige Quell-IPs zu beschränken oder über ein VPN abzusichern.“

([dmk](mailto:dmk@heise.de))
