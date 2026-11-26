---
title: Unauthenticated remote code execution vulnerability in GeoServer
author: Niels Teusink
url: https://labs.eye.security/unauthenticated-remote-code-execution-vulnerability-in-geoserver/
hostname: eye.security
description: In our efforts to identify security vulnerabilities in products commonly used by our customers, we investigated GeoServer. GeoServer…
sitename: Eye Research
date: "2026-11-24"
categories: ['Tech blog']
tags: ['cve', 'geoserver', 'security vulnerability']
fingerprint: bdfb0e95889342e3
language: en
image: https://labs.eye.security/wp-content/uploads/image-8-1-1024x683.png
pagetype: article
filedate: "2026-11-26"
---
[← Return to overview](https://labs.eye.security/unauthenticated-remote-code-execution-vulnerability-in-geoserver/)


Nov 24, 2026

In our efforts to identify security vulnerabilities in products commonly used by our customers, we investigated GeoServer. GeoServer is an open-source, Java-based server for sharing geospatial data, such as maps. It is commonly used by government institutions to publish open data, and its GitHub repository has approximately 4,500 stars. We identified over 3,000 internet-accessible GeoServer instances.

In August, a SQL injection vulnerability in GeoServer was [exploited in the wild](https://thehackernews.com/2026/08/unpatched-geoserver-zero-day-targeted.html) before a patch was available. In 2025, an unnamed US government agency [was hacked](https://www.securityweek.com/geoserver-flaw-exploited-in-us-federal-agency-hack/) using a GeoServer vulnerability.

We discovered vulnerabilities in all supported versions of GeoServer (3.0.1 and 2.28.5). This blog post focuses on vulnerabilities in the 3.0.1 (stable) version of GeoServer. These vulnerabilities can be exploited without any authentication and lead to remote code execution. They require no special settings and work on the default configuration.

We worked with GeoServer to make this process go as smoothly as possible. On October 19th GeoServer released the fixed versions. They included this notice:

*“This release addresses security vulnerabilities and is an important upgrade for production systems. Details about the fixes will be provided at the start of November.”*

By then we had found out some of the vulnerabilities had also been reported by another researcher. For a GeoServer user, the impact was not immediately clear and we had to make a decision: do we go public or wait for GeoServer to publish details? We used AI to discover these bugs and so could a determined malicious attacker.

We decided to wait for the official announcement, but it wasn’t an easy decision. We used AI to find these bugs, and a determined attacker with good models could do the same, especially with the official patch to diff against. That makes the gap between releasing a fix and publishing details riskier than it used to be.

We did try to encourage users to upgrade. We posted a message on private channels encouraging people to upgrade, without sharing details. Later, we also [posted on LinkedIn](https://www.linkedin.com/feed/update/urn:li:activity:7521580168436445186). We hope this encouraged defenders to patch without tipping off attackers.

It took a while for CVEs to be assigned, as this process is heavily overloaded with the many vulnerabilities that are being discovered. GeoServer published the details on November 23rd.

GeoServer has a rich API, including an implementation of the Web Feature Service 2.0 (WFS 2.0) standard. One stored query, ‘GetFeatureById’ allows an API client to retrieve a specific map feature, like a road or building, by its identifier.

The supplied identifier is used in a query template without adequate escaping. This allows an attacker to inject additional XML elements, including XInclude elements. We used this to exploit an [XInclude](https://portswigger.net/web-security/xxe/lab-xinclude-attack)-based file read.

The vulnerability can expose files on the filesystem accessible to the GeoServer process. The content must be compatible with the XML processing involved, so arbitrary binary files may not be readable. We were able to access users.xml, which contains GeoServer usernames and password hashes.

GeoServer uses a salted password hash with 100,000 iterations of SHA256, which is reasonably good and should make strong passwords hard to crack.

There is, however, a pass-the-hash option. GeoServer has a ‘rememberme’ function. This functionality requires a password hash and a rememberme key. This rememberme key can also be extracted using the file read vulnerability, but is usually set to the static value ‘geoserver’. This gives us a cookie that can be used to authenticate to the application and get a valid JSESSIONID.

An authenticated administrator can change a number of GeoServer settings, including registering a JDBC connection. In our testing, we used a SQLite connection and its load\_extension() functionality to execute code from an uploaded native library. We verified this works on both Linux and Windows versions of GeoServer.

We reported the vulnerabilities to GeoServer on September 29<sup>th</sup> 2026. The reported vulnerabilities were fixed in versions [3.0.2](https://geoserver.org/announcements/vulnerability/2026/10/19/geoserver-3-0-2-released.html) (stable), [2.28.6](https://geoserver.org/announcements/vulnerability/2026/10/19/geoserver-2-28-6-released.html) (maintenance), which have been available since October 19th. We recommend upgrading to a fixed release. Note there is also a fix available for the [2.27.x](https://geoserver.org/announcements/vulnerability/2026/10/19/geoserver-2-27-7-released.html) series, but that isn’t officially supported anymore.

The new versions also harden the ‘rememberbe’ functionality, making it a lot harder for an attacker to forge these cookies.

To check your version, log in to the GeoServer web interface and open the “About GeoServer” page; the version is listed under Build Information.

Three vulnerabilities combine to create the unauthenticated remote code execution chain:

- [CVE-2026-120705](https://github.com/geoserver/geoserver/security/advisories/GHSA-39mw-5chv-jh47) allows an attacker to read users.xml and security configuration.
- [CVE-2026-129245](https://github.com/geoserver/geoserver/security/advisories/GHSA-hgm3-wq4h-8vvq) is a predictable remember-me signing key. Combined with the stored password representation, it allows an attacker to forge administrator authentication.
- [CVE-2026-120704](https://github.com/geoserver/geoserver/security/advisories/GHSA-wc3v-48j7-xf57) is administrator-controlled SQLite JDBC extension loading, which provides native code execution.

Chained together, these vulnerabilities allow an unauthenticated attacker to progress from file access to administrator authentication and then to remote code execution. These vulnerabilities were also reported by other researchers, which is increasingly common in this age of AI vulnerability research.

Other researchers that found these and other bugs have created blog posts on them as well:

- [https://cryptocat.me/blog/research/analysis/geoserver\_preauth\_rce/](https://cryptocat.me/blog/research/analysis/geoserver_preauth_rce/)
- [https://wallesonmoura.com.br/2026/11/23/geoserver-unauth-xxe-to-rce.html](https://wallesonmoura.com.br/2026/11/23/geoserver-unauth-xxe-to-rce.html)

An AI-driven attack framework was a the center of one of our incident response cases, and machine speed stopped being a buzzword. What the agents did, how fast they adapted, and how we fought back with agents of our own.

You are a defender and spot an M365 user that was phished. The first thing you want to…

The PHP2Shell vulnerabilities are two of the most serious bugs of 2026. They can be used to exploit…

Between November 2025 and March 2026, Eye Research actively disabled the vulnerable update mechanism used by the popular…

Manage Consent

To provide the best experiences, we use technologies like cookies to store and/or access device information. Consenting to these technologies will allow us to process data such as browsing behavior or unique IDs on this site. Not consenting or withdrawing consent, may adversely affect certain features and functions.

Functional
					
						
							
							
						
						Always active

The technical storage or access is strictly necessary for the legitimate purpose of enabling the use of a specific service explicitly requested by the subscriber or user, or for the sole purpose of carrying out the transmission of a communication over an electronic communications network.

Preferences

The technical storage or access is necessary for the legitimate purpose of storing preferences that are not requested by the subscriber or user.

Statistics

The technical storage or access that is used exclusively for statistical purposes.
					The technical storage or access that is used exclusively for anonymous statistical purposes. Without a subpoena, voluntary compliance on the part of your Internet Service Provider, or additional records from a third party, information stored or retrieved for this purpose alone cannot usually be used to identify you.

Marketing

The technical storage or access is required to create user profiles to send advertising, or to track the user on a website or across several websites for similar marketing purposes.
