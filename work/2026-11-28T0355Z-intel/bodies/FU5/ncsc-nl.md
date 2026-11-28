---
title: Security Advisories
url: https://advisories.ncsc.nl/2026/ncsc-2026-0506.html
hostname: ncsc.nl
description: NCSC NL | Security Advisories
sitename: advisories.ncsc.nl
date: "2026-11-18"
tags: ['ncsc', 'advisory', 'Security Advisories', 'beveiligingsadvies', 'nl', 'cve', 'kwetsbaarheid', 'index']
fingerprint: "245a4e9166b6611d"
language: nl
filedate: "2026-11-28"
---
## Download

## Security Advisory; NCSC-2026-0506 \[1.0.0\]

- Security Advisory
  NCSC-2026-0506 \[1.0.0\]
- Publicatie
  18-11-2026 17:07 (Europe/Amsterdam)
- Prioriteit
  Hoog
- Betreft
  Kwetsbaarheden verholpen in NGINX door F5 Networks

### Kenmerken

- Integer Underflow (Wrap or Wraparound)
- Use After Free
- NULL Pointer Dereference
- Out-of-bounds Write
- Loop with Unreachable Exit Condition
- Improper Validation of Unsafe Equivalence in Input

### Omschrijving

F5 Networks heeft meerdere kwetsbaarheden verholpen in NGINX Plus en NGINX Open Source.

De kwetsbaarheden betreffen verschillende onderdelen en configuraties van NGINX. De belangrijkste kwetsbaarheid met kenmerk CVE-2026-123007 stelt kwaadwillenden in staat om willekeurige code uit te voeren op het onderliggende systeem.

Het NCSC verwacht dat er op korte termijn proof of concept code beschikbaar komt, waarna exploitatie op grote schaal verwacht wordt.

### Oplossingen

F5 Networks heeft updates uitgebracht voor NGINX Plus en NGINX Open Source om deze kwetsbaarheden te verhelpen. Zie bijgevoegde referenties voor meer informatie.

### Referenties

### CVE's

- [CVE-2026-113425](https://vulnerabilities.ncsc.nl/vulnerability.html?id=2026/cve-2026-113425) - CVSS (v4) 9.2
- [CVE-2026-118899](https://vulnerabilities.ncsc.nl/vulnerability.html?id=2026/cve-2026-118899) - CVSS (v4) 8.7
- [CVE-2026-120967](https://vulnerabilities.ncsc.nl/vulnerability.html?id=2026/cve-2026-120967) - CVSS (v4) 6.3
- [CVE-2026-120993](https://vulnerabilities.ncsc.nl/vulnerability.html?id=2026/cve-2026-120993) - CVSS (v4) 6.9
- [CVE-2026-121810](https://vulnerabilities.ncsc.nl/vulnerability.html?id=2026/cve-2026-121810) - CVSS (v4) 9.2
- [CVE-2026-123007](https://vulnerabilities.ncsc.nl/vulnerability.html?id=2026/cve-2026-123007) - CVSS (v4) 9.2
- [CVE-2026-123633](https://vulnerabilities.ncsc.nl/vulnerability.html?id=2026/cve-2026-123633) - CVSS (v4) 9.2
- [CVE-2026-123634](https://vulnerabilities.ncsc.nl/vulnerability.html?id=2026/cve-2026-123634) - CVSS (v4) 9.2
- [CVE-2026-123640](https://vulnerabilities.ncsc.nl/vulnerability.html?id=2026/cve-2026-123640) - CVSS (v4) 6.9
- [CVE-2026-125283](https://vulnerabilities.ncsc.nl/vulnerability.html?id=2026/cve-2026-125283) - CVSS (v4) 6.9

### Producten

## **F5**

### Disclaimer

The Netherlands Cyber Security Center (henceforth: NCSC-NL) maintains this page to enhance access to its information and security advisories. The use of this security advisory is subject to the following terms and conditions: NCSC-NL makes every reasonable effort to ensure that the content of this page is kept up to date, and that it is accurate and complete. Nevertheless, NCSC-NL cannot entirely rule out the possibility of errors, and therefore cannot give any warranty in respect of its completeness, accuracy or continuous keeping up-to-date. The information contained in this security advisory is intended solely for the purpose of providing general information to professional users. No rights can be derived from the information provided therein. NCSC-NL and the Kingdom of the Netherlands assume no legal liability or responsibility for any damage resulting from either the use or inability of use of this security advisory. This includes damage resulting from the inaccuracy of incompleteness of the information contained in the advisory. This security advisory is subject to Dutch law. All disputes related to or arising from the use of this advisory will be submitted to the competent court in The Hague. This choice of means also applies to the court in summary proceedings.
