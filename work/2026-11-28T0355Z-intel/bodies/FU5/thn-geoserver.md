---
title: Hackers Exploit Two GeoServer Flaws as Researchers Warn of Unauthenticated RCE Chains
author: The Hacker News
url: https://thehackernews.com/2026/11/hackers-exploit-two-geoserver-flaws-as.html
hostname: thehackernews.com
description: Attackers are exploiting two newly patched GeoServer flaws that could enable file disclosure and authorization bypass without authentication.
sitename: The Hacker News
date: "2026-11-25"
categories: ['Article']
tags: ['Arbitrary File Read', 'Authorization Bypass', 'cyber attacks', 'Open Source', 'remote code execution', 'Vulnerability']
fingerprint: "253aec108d17c2ef"
language: en
image: https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhi8jBS9UW1bUouUo2cLun5A5rtqPOFJoVQctV4ZsoX9uuMottAxM0HLjLZrvTVGU1GtrewszjOwVMBkvHgyFIBsOndc049nwMidNiVnnoKCOePOhy-XDsjiVjxFvubbxn-Z6ca8VJAxxgLmyQ9KGYBRMWV5GP2et02dmXzcG3jKJw1p_njPdaPuJAaxAz1/s1700-nu-rw-lo-l85-e365/geoserver.png
pagetype: article
filedate: "2026-11-28"
---
Threat actors are actively exploiting two newly patched security flaws in GeoServer, according to [watchTowr](https://x.com/watchtowrcyber/status/2125547398021693623).

The vulnerabilities in question are CVE-2026-120705 and CVE-2026-129243, details of which are below -

- **[CVE-2026-120705](https://github.com/geoserver/geoserver/security/advisories/GHSA-39mw-5chv-jh47)** (CVSS score: 8.6) - An arbitrary file read vulnerability that could enable an attacker to access local text files readable by the GeoServer process or fetch adversary-selected HTTP or HTTPS URLs by means of a single unauthenticated Web Feature Service (WFS) request.
- **[CVE-2026-129243](https://github.com/geoserver/geoserver/security/advisories/GHSA-rv5g-g2r9-58rj)** (CVSS score: 8.8) - An incorrect authorization vulnerability that could allow an unauthenticated attacker to invoke [OWS](https://docs.geoserver.org/main/en/developer/programming-guide/ows-services/) operations that are otherwise protected by service security rules.

Advisories for both the flaws were published on November 24, 2026, in the following versions -

- CVE-2026-120705: org.geoserver:gs-wfs-core - 3.0.2, 2.28.6, and 2.27.7
- CVE-2026-120705: org.geotools:gt-metadata - 35.2, 34.6, and 33.7
- CVE-2026-129243: org.geoserver:gs-ows - 3.0.2, 2.28.6, and 2.27.7

"Attackers sent error-based exploit probes to validate that the server is vulnerable by creating and invoking stored queries," the preemptive exposure management firm said in an X post today.

Yordan Ganchev, principal threat intelligence specialist at watchTowr, said the vulnerabilities can allow attackers to bypass security restrictions, interact with internal services, retrieve stored secrets, forge authentication credentials, and deserialize and run code on affected systems.

"On November 25, we observed in-the-wild exploitation against our global honeypot network in the early morning hours leveraging CVE-2026-120705 and CVE-2026-129244," Ganchev said. "Threat actors from multiple IP addresses were observed validating vulnerable systems on the internet by creating stored queries on GeoServer machines, checking whether they were created, and deleting them immediately afterward."

Eye Security, which [discovered and reported](https://labs.eye.security/unauthenticated-remote-code-execution-vulnerability-in-geoserver/) CVE-2026-120705, said the flaw can be combined with two other vulnerabilities in the same product to create an unauthenticated remote code execution chain -


- **[CVE-2026-129245](https://github.com/geoserver/geoserver/security/advisories/GHSA-hgm3-wq4h-8vvq)** (CVSS score: 9.2) - A use of a hard-coded signing key ("geoserver") vulnerability in the "remember me" functionality that could be exploited to forge administrator authentication. (Fixed in org.geoserver:gs-main versions 3.0.2, 2.28.6, and 2.27.7)
- **[CVE-2026-120704](https://github.com/geoserver/geoserver/security/advisories/GHSA-wc3v-48j7-xf57)** (CVSS score: 7.2) - An improper control of the generation of code vulnerability that could allow an administrator, or anyone with access to an administrator session, to execute arbitrary code as the user running GeoServer. (Fixed in org.geoserver.security:gs-sec-jdbc versions 3.0.2, 2.28.6, and 2.27.7)

In a hypothetical attack chain, a bad actor can follow the steps below -

- Exploit CVE-2026-120705 to access "users.xml," a file containing GeoServer usernames and password hashes, and obtain the password representation along with the static signing key extracted from the security configuration ("security/config.xml").
- Exploit CVE-2026-129245 to forge a valid administrator authentication cookie by using the predictable signing key and the stored password representation without having to know the administrator password.
- Exploit CVE-2026-120704 to abuse an administrator-controlled JDBC configuration to execute code from an uploaded native library on both Linux and Windows versions of GeoServer.

According to the project maintainers, CVE-2026-129245 is also part of a five-step unauthenticated remote command execution chain that involves -

- **[CVE-2026-129244](https://github.com/geoserver/geoserver/security/advisories/GHSA-4v26-c537-jvxc)** (CVSS score: 6.9) - WFS stored query exception discloses data directory path
- **CVE-2026-129243** (CVSS score: 8.8) - Service security rules bypassed with a prefixed service name such as x/WFS
- **CVE-2026-120705** (CVSS score: 8.6) - Unauthenticated WFS GetFeatureById XML injection
- **CVE-2026-129245** (CVSS score: 9.2) - Predictable "remember me" key allows administrator session forgery
- **[CVE-2026-129242](https://github.com/geoserver/geoserver/security/advisories/GHSA-9wf2-fcgq-vxhq)** (CVSS score: 8.6) - Deserialization in JDBC user and role services allows administrator code execution

"An attacker who obtains an administrator password digest, through any file disclosure or a copy of the data directory, can log in as that administrator," GeoServer maintainers said. "Changing the key in security/config.xml does not help when the same file disclosure also reveals the key."

Jonah Burgess, a Senior Security Researcher at Rapid7, who goes by the online alias **CryptoCat** has been acknowledged for independently discovering and reporting the five-step unauthenticated remote command execution chain on August 2, 2026.

"Prefixing the Web Feature Service (WFS) name, as in x/WFS, slips past the admin-only rule for stored queries. GeoServer turns escaped text in a saved query into live xi:include elements, which leaks the files holding the remember-me key and the admin password digest," the researcher [said](https://cryptocat.me/blog/research/analysis/geoserver_preauth_rce/).

"Those two values forge an administrator cookie without cracking the password. As admin, the attacker points a JDBC user service at an uploaded HSQLDB database, and the bundled driver deserialises a stored value that runs commands."

In light of active exploitation of two of the flaws, users are advised to update to GeoServer versions [2.27.7](https://github.com/geoserver/geoserver/releases/tag/2.27.7), [2.28.6](https://github.com/geoserver/geoserver/releases/tag/2.28.6), and [3.0.2](https://github.com/geoserver/geoserver/releases/tag/3.0.2) released over the past month as soon as possible.

The development comes a little over three months after another critical flaw in GeoServer ([CVE-2026-76904](https://thehackernews.com/2026/08/unpatched-geoserver-zero-day-targeted.html), CVSS score: 9.8) witnessed active exploitation efforts as a zero-day.

"Organizations running publicly exposed GeoServer instances should prioritize patching them as soon as possible," Ganchev said. "Any exposed systems should be audited for signs of credentials leaking, unauthorized access and code execution on the host. Where patching is not immediately possible, restrict access to the host."

*(The story has been updated after publication to include more details of the flaws and emphasize that advisories for the issues were released on November 24, 2026. The patches were originally released in October and early November 2026.)*

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ),
