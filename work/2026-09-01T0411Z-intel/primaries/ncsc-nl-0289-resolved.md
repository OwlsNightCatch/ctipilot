# extract: served via trafilatura-direct
---
title: Security Advisories
url: https://advisories.ncsc.nl/2026/ncsc-2026-0289.html
hostname: ncsc.nl
description: NCSC NL | Security Advisories
sitename: advisories.ncsc.nl
date: "2026-08-12"
tags: ['ncsc, advisory, Security Advisories, beveiligingsadvies, nl, cve, kwetsbaarheid, index']
---
## Download

## Security Advisory; NCSC-2026-0289 [1.0.1]

- Security Advisory
- NCSC-2026-0289 [1.0.1]
- Publicatie
- 28-08-2026 13:33 (Europe/Amsterdam)
- Prioriteit
- Hoog
- Betreft
- Kwetsbaarheden verholpen in Microsoft Exchange server

### Revisies

| Versie | Datum | Opmerking |  | 
|---|---|---|---|
| 1.0.1 | 28-08-2026 11:33 | Voor de kwetsbaarheid met kenmerk CVE-2026-62911 is proof-of-concept-code online verschenen. Deze informatie is aan dit beveiligingsadvies toegevoegd. De aanschaling is bijgesteld van MEDIUM/HIGH naar HIGH/HIGH. |  | 
| 1.0.0 | 12-08-2026 05:43 | Initiele versie | [Bekijken](https://advisories.ncsc.nl/ncsc-2026-0289-0.html) | 

### Kenmerken

- Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')
- Improper Control of Resource Identifiers ('Resource Injection')
- Heap-based Buffer Overflow
- Authentication Bypass by Capture-replay
- Deserialization of Untrusted Data
- Missing Authorization
- Server-Side Request Forgery (SSRF)

### Omschrijving

Microsoft heeft kwetsbaarheden verholpen in Exchange Server.

Een kwaadwillende kan de kwetsbaarheden misbruiken om een Denial-of-Service uit te voeren, zich voor te doen als andere gebruiker, zich verhoogde rechten toe te kennen, willekeurige code uit te voeren en/of toegang te krijgen tot gevoelige gegevens.

**Update**: Voor de kwetsbaarheid met kenmerk CVE-2026-62911 is proof-of-concept-code gepubliceerd. Deze kwetsbaarheid stelt een ongeauthenticeerde kwaadwillende in staat om willekeurige code uit te voeren. Zodoende krijgt de kwaadwillende bijvoorbeeld toegang tot mailboxen van Exchange-gebruikers, en kan de kwetsbaarheid worden misbruikt voor het uitvoeren van verdere aanvallen op het netwerk van het slachtoffer.

### Oplossingen

Microsoft heeft updates beschikbaar gesteld waarmee de beschreven kwetsbaarheden worden verholpen. We raden u aan om deze updates te installeren. Meer informatie over de kwetsbaarheden, de installatie van de updates en eventuele work-arounds vindt u op:

https://portal.msrc.microsoft.com/en-us/security-guidance

Houd er rekening mee dat Exchange Server 2016 en 2019 end-of-life zijn en enkel via het ESU-programma nog beveiligingsupdates ontvangen. Het NCSC adviseert met klem om Exchange Servers die geen ESU-ondersteuning ontvangen, alleen vanaf interne netwerken benaderbaar te maken en waar mogelijk uit te faseren.

### Referenties

### CVE's

- [CVE-2026-62910](https://vulnerabilities.ncsc.nl/vulnerability.html?id=2026/cve-2026-62910) - CVSS (v3) 7.2
- [CVE-2026-62912](https://vulnerabilities.ncsc.nl/vulnerability.html?id=2026/cve-2026-62912) - CVSS (v3) 6.5
- [CVE-2026-62913](https://vulnerabilities.ncsc.nl/vulnerability.html?id=2026/cve-2026-62913) - CVSS (v3) 8.8
- [CVE-2026-62914](https://vulnerabilities.ncsc.nl/vulnerability.html?id=2026/cve-2026-62914) - CVSS (v3) 7.3
- [CVE-2026-62915](https://vulnerabilities.ncsc.nl/vulnerability.html?id=2026/cve-2026-62915) - CVSS (v3) 6.5
- [CVE-2026-65813](https://vulnerabilities.ncsc.nl/vulnerability.html?id=2026/cve-2026-65813) - CVSS (v3) 6.5
- [CVE-2026-62911](https://vulnerabilities.ncsc.nl/vulnerability.html?id=2026/cve-2026-62911) - CVSS (v3) 8.0

### Producten

## **Microsoft**

                      ### Disclaimer

The Netherlands Cyber Security Center (henceforth: NCSC-NL) maintains this page to enhance access to its information and security advisories. The use of this security advisory is subject to the following terms and conditions: NCSC-NL makes every reasonable effort to ensure that the content of this page is kept up to date, and that it is accurate and complete. Nevertheless, NCSC-NL cannot entirely rule out the possibility of errors, and therefore cannot give any warranty in respect of its completeness, accuracy or continuous keeping up-to-date. The information contained in this security advisory is intended solely for the purpose of providing general information to professional users. No rights can be derived from the information provided therein. NCSC-NL and the Kingdom of the Netherlands assume no legal liability or responsibility for any damage resulting from either the use or inability of use of this security advisory. This includes damage resulting from the inaccuracy of incompleteness of the information contained in the advisory. This security advisory is subject to Dutch law. All disputes related to or arising from the use of this advisory will be submitted to the competent court in The Hague. This choice of means also applies to the court in summary proceedings.
