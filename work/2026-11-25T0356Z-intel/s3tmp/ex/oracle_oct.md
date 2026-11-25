---
title: Oracle Critical Patch Update Advisory - October 2026
url: https://www.oracle.com/security-alerts/cpuoct2026.html
hostname: oracle.com
description: Oracle Critical Patch Update Advisory - October 2026
sitename: oracle.com
date: "2026-10-15"
tags: ['CPU', 'Critical Patch Update', 'Security', 'Security Advisory', 'October 2026']
fingerprint: "77597e33c5b2b13a"
language: en
filedate: "2026-11-25"
---
A Critical Patch Update is a collection of patches for multiple security vulnerabilities.  These patches address vulnerabilities in Oracle code and in third party components included in Oracle products.  These patches are usually cumulative, but each advisory describes only the security patches added since the previous Critical Patch Update Advisory. Thus, prior Critical Patch Update advisories should be reviewed for information regarding earlier published security patches.  Refer to [Critical Patch Updates, Critical Security Patch Updates, Security Alerts and Bulletins](https://www.oracle.com/security-alerts/) for information about Oracle Security advisories.

**Oracle continues to periodically receive reports of attempts to maliciously exploit vulnerabilities for which Oracle has already released security patches. In some instances, it has been reported that attackers have been successful because targeted customers had failed to apply available Oracle patches. Oracle therefore strongly recommends that customers remain on actively-supported versions and apply security patches without delay.**

This Critical Patch Update contains 1295 new security patches across the product families listed below. Please note that a My Oracle Support (MOS) note summarizing the content of this Critical Patch Update and other Oracle Software Security Assurance activities is located at  [October 2026 Critical Patch Update: Executive Summary and Analysis](https://support.oracle.com/support/?documentId=CPU289).

Security vulnerabilities addressed by this Critical Patch Update affect the products listed below.

**Please click on the links in the Patch Availability Document column below to access the documentation for patch availability information and installation instructions.** 

Risk matrices list only security vulnerabilities that are newly addressed by the patches associated with this advisory. Risk matrices for previous security patches can be found in [previous Critical Patch Update advisories, Critical Security Patch Update advisories and Alerts](https://www.oracle.com/security-alerts). An English text version of the risk matrices provided in this document is  [here](https://www.oracle.com/security-alerts/cpuoct2026verbose.html).

Several vulnerabilities addressed in this Critical Patch Update affect multiple products. Each vulnerability is identified by a [CVE ID](https://cve.org). A vulnerability that affects multiple products will appear with the same CVE ID in all risk matrices.

Security vulnerabilities are scored using CVSS version 3.1 (see [Oracle CVSS Scoring](https://www.oracle.com/security-alerts/cvssscoringsystem.html) for an explanation of how Oracle applies CVSS version 3.1).

Oracle conducts an analysis of each security vulnerability addressed by a Critical Patch Update. Oracle does not disclose detailed information about this security analysis to customers, but the resulting Risk Matrix and associated documentation provide information about conditions required to exploit the vulnerability and the potential impact of a successful exploit. Oracle provides this information so that customers may conduct their own risk analysis based on the particulars of their product usage. For more information, see [Oracle vulnerability disclosure policies](https://www.oracle.com/corporate/security-practices/assurance/vulnerability/disclosure/).

Third party component vulnerabilities that are deemed not exploitable in the context of their inclusion in an Oracle product are listed, with [VEX](https://www.oracle.com/security-alerts/cpufaq.html#vex) justifications, below the respective Oracle product's risk matrix.

The protocol in the risk matrix implies that all of its secure variants are affected as well. For example, if HTTP is listed as an affected protocol, it implies that HTTPS is also affected. The secure variant of a protocol is listed in the risk matrix only if it is the *only* variant affected.

**Due to the threat posed by a successful attack, Oracle strongly recommends that customers apply Critical Patch Update security patches as soon as possible**. Until you apply the Critical Patch Update patches, it may be possible to reduce the risk of successful attack by blocking network protocols required by an attack. For attacks that require certain privileges or access to certain packages, removing the privileges or the ability to access the packages from users that do not need the privileges may help reduce the risk of successful attack. Both approaches may break application functionality, so Oracle strongly recommends that customers test changes on non-production systems. Neither approach should be considered a long-term solution as neither corrects the underlying problem.

Oracle strongly recommends that customers apply security patches as soon as possible. For customers that have skipped one or more security patches and are concerned about products that do not have security patches announced in this Critical Patch Update, please review [previous Critical Patch Update and Critical Security Patch Update advisories](https://www.oracle.com/security-alerts) to determine appropriate actions.

Patches released through the Critical Patch Update program are provided only for product versions that are covered under the Premier Support or Extended Support phases of the  [Lifetime Support Policy](https://www.oracle.com/us/support/lifetime-support/index.html?ssSourceSiteId=otnen). Oracle recommends that customers plan product upgrades to ensure that patches released through the Critical Patch Update program are available for the versions they are currently running.

Product releases that are not under Premier Support or Extended Support are not tested for the presence of vulnerabilities addressed by this Critical Patch Update. However, it is likely that earlier versions of affected releases are also affected by these vulnerabilities. As a result, Oracle recommends that customers upgrade to supported versions.

The following people or organizations reported security vulnerabilities addressed by this Critical Patch Update to Oracle:

- 4ra1n, pyn3rd and unam4: CVE-2026-101725, CVE-2026-101726, CVE-2026-101727, CVE-2026-101728, CVE-2026-101729, CVE-2026-101768, CVE-2026-83395, CVE-2026-87367, CVE-2026-91394
- Acol7542: CVE-2026-83395, CVE-2026-91400
- Alexander Dezhinov, Stanislav Dukhin, Nikita Kozlov: CVE-2026-83387, CVE-2026-87367, CVE-2026-91379
- Alexandre Cornet: CVE-2026-101735
- Alexey Bakhtin: CVE-2026-91418
- Amitay Shahar: CVE-2026-101512
- Anas Cherni of Calif.io: CVE-2026-101624
- Arthur Chan of ADAlogics: CVE-2026-87294
- Avicii: CVE-2026-91415
- Binbin Xu of Tencent YUNDING LAB CodeBuddy Security: CVE-2026-101794, CVE-2026-101795, CVE-2026-101796, CVE-2026-101797, CVE-2026-101798, CVE-2026-101799, CVE-2026-83395
- Brandon Peterson of Horizon3.ai: CVE-2026-101767
- Bruce Dang of Calif.io: CVE-2026-83378
- Cheonwoong Park: CVE-2026-101781
- Co-tang X: CVE-2026-101499, CVE-2026-91215, CVE-2026-91231, CVE-2026-91609, CVE-2026-91610
- Dat Hoang Thanh: CVE-2026-101593, CVE-2026-101595
- David Korczynski of ADA Logics: CVE-2026-101769, CVE-2026-101770, CVE-2026-101771, CVE-2026-101772, CVE-2026-101773, CVE-2026-101774, CVE-2026-101775
- Dhanush Arvind: CVE-2026-101810, CVE-2026-87322
- Doria Tang: CVE-2026-83374
- Equixly: CVE-2026-101598, CVE-2026-101598
- Feng Xue: CVE-2026-101787, CVE-2026-101788, CVE-2026-101789
- Greencrow1234: CVE-2026-83376
- h1ei1: CVE-2026-101803
- Haogang Mao of SKLCCSE Lab at Beihang University: CVE-2026-101620, CVE-2026-101730, CVE-2026-101731, CVE-2026-101732, CVE-2026-101756
- Jens Frieß of Goethe University Frankfurt: CVE-2026-83400
- Jie Liang of SKLCCSE Lab at Beihang University: CVE-2026-101730, CVE-2026-101731, CVE-2026-101732
- Jimi Sebree of Horizon3.ai: CVE-2026-101767
- Le Viet Hoang: CVE-2026-101596
- Lukasz Plonka: CVE-2026-101490
- Mat Powell of TrendAI Zero Day Initiative: CVE-2026-91457, CVE-2026-91458, CVE-2026-91459, CVE-2026-91460, CVE-2026-91483
- Mrraul124: CVE-2026-101785
- Muhammad Daffa: CVE-2026-101802
- Muntadher Hasan (Dark River): CVE-2026-101783
- Nguyen Dang Minh of Viettel Cybersecurity: CVE-2026-101591, CVE-2026-101592, CVE-2026-101594
- Noah King of Horizon3.ai: CVE-2026-101767
- Omkhar Arasaratnam of Linkedin: CVE-2026-101766
- Omri Dar of Remedio: CVE-2026-101796
- Quang Vũ from Viettel Cyber Security: CVE-2026-101602
- Safa S. Karakuş of Secunnix Siber Teknoloji Hizmetleri Ltd. Sti.: CVE-2026-87413
- Sergey Bylokhov of AWS Security: CVE-2026-91415
- Siddharth Shubham Pal: CVE-2026-101800
- Suraj Theekshana (株式会社CyberCrew): CVE-2026-101804
- Thien Ta Duc: CVE-2026-91409
- Tristan Madani of Talence Security: CVE-2026-87301, CVE-2026-87303, CVE-2026-87311
- Vulcanix: CVE-2026-101500
- Weber Leon: CVE-2026-91415
- Xiang Chen: CVE-2026-101510, CVE-2026-91479, CVE-2026-91499
- Yoggydev: CVE-2026-83404
- Yuelin Wang of Violin0613: CVE-2026-101721, CVE-2026-101722, CVE-2026-101761, CVE-2026-101762, CVE-2026-101776, CVE-2026-101777, CVE-2026-101778, CVE-2026-101779, CVE-2026-101780
- Yuval Fradkin: CVE-2026-101677, CVE-2026-101678
- Zheng Yu of depthfirst: CVE-2026-101786, CVE-2026-91609
- Ziad Salah: CVE-2026-101599
- Zorta Zenith: CVE-2026-91542, CVE-2026-91552

Oracle acknowledges people who have contributed to our Security-In-Depth program (see [FAQ](https://www.oracle.com/security-alerts/cpufaq.html)). People are acknowledged for Security-In-Depth contributions if they provide information, observations or suggestions pertaining to security vulnerability issues that result in significant modification of Oracle code or documentation in future releases, but are not of such a critical nature that they are distributed in Critical Patch Updates.

In this Critical Patch Update, Oracle recognizes the following for contributions to Oracle's Security-In-Depth program:

- Alexander Dezhinov, Stanislav Dukhin, Nikita Kozlov
- Bruce Dang of Calif.io
- Yaxin Kuang (Lya0), Hao Zheng (qi4L)

Oracle acknowledges people who have contributed to our On-Line Presence Security program (see [FAQ](https://www.oracle.com/security-alerts/cpufaq.html)). People are acknowledged for contributions relating to Oracle's on-line presence if they provide information, observations or suggestions pertaining to security-related issues that result in significant modification to Oracle's on-line external-facing systems.

For this quarter, Oracle recognizes the following for contributions to Oracle's On-Line Presence Security program:

- Aakil Mirza

Security patches are released on the third Tuesday of each month. The next four dates are:

- 17 November 2026 (CSPU)
- 15 December 2026 (CSPU)
- 19 January 2027 (CPU)
- 16 February 2027 (CSPU)

| Date | Note | 
|---|---|
| 2026-November-4 | Rev 3. Added credit for CVE-2026-101796 | 
| 2026-October-26 | Rev 2. Updated credit name for Nguyen Dang Minh, Updated Siebel CRM versions, Updated credit for CVE-2026-101725 and CVE-2026-101768 | 
| 2026-October-20 | Rev 1. Initial Release. | 


This Critical Patch Update contains 126 new security patches for Oracle Database Products divided as follows:

- 14 new security patches for Oracle Database Products
- 2 new security patches for Oracle APEX
- 5 new security patches for Oracle Autonomous Health Framework
- 38 new security patches for Oracle Essbase
- 1 new security patch for Oracle Global Lifecycle Management
- 11 new security patches for Oracle GoldenGate
- No new security patches for Oracle Graph Server and Client, but third party patches are provided
- 1 new security patch for Oracle NoSQL Database
- 35 new security patches for Oracle REST Data Services
- 6 new security patches for Oracle Secure Backup
- 1 new security patch for Oracle SQL Developer
- 4 new security patches for Oracle TimesTen In-Memory Database
- 8 new security patches for Oracle Trusted Answer Search


This Critical Patch Update contains 14 new security patches, plus additional third party patches noted below, for Oracle Database Products.  4 of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  2 of these patches are applicable to client-only installations, i.e., installations that do not have the Oracle Database Server installed. The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cpuoct2026verbose.html#DB)

| CVE ID | Component | Package and/or Privilege Required | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-75803 | RDBMS (OpenSSL) | None | TLS | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 19.3-19.32, 23.4.0-23.26.3 |  | 
| CVE-2026-91563 | Oracle OLAP | DBMS\_AW | Oracle Net | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 19.3-19.32, 21.3-21.23, 23.4.0-23.26.3 |  | 
| CVE-2026-91499 | RDBMS | DBMS\_VECTOR | Oracle Net | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 23.4.0-23.26.3 |  | 
| CVE-2026-93569 | RDBMS (Micronaut) | None | HTTP | Yes | 8.2 | Network | Low | None | None | Un- changed | Low | High | None | 19.3-19.32, 23.4.0-23.26.3 |  | 
| CVE-2026-91503 | VPD | Create Table | Oracle Net | No | 8.1 | Network | Low | Low | None | Un- changed | High | High | None | 19.3-19.32, 21.3-21.23, 23.4.0-23.26.3 |  | 
| CVE-2026-91568 | RDBMS | Create Session | Oracle Net | No | 7.7 | Network | Low | Low | None | Changed | High | None | None | 23.4.0-23.26.3 |  | 
| CVE-2026-101512 | RDBMS | None | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 23.4.0-23.26.3 |  | 
| CVE-2026-91479 | RDBMS | None | UDP | Yes | 6.5 | Adjacent Network | Low | None | None | Un- changed | None | None | High | 23.4.0-23.26.3 |  | 
| CVE-2026-91615 | Java VM | None | SOCKS5 | No | 6.3 | Network | High | Low | None | Changed | None | High | None | 19.3-19.32, 21.3-21.23, 23.4.0-23.26.3 |  | 
| CVE-2026-59889 | RDBMS (jackson-databind) | None | None | No | 6.2 | Local | Low | None | None | Un- changed | None | High | None | 19.3-19.32, 21.3-21.23, 23.4.0-23.26.3 |  | 
| CVE-2026-75803 | RDBMS (Python) | None | None | No | 6.2 | Local | Low | None | None | Un- changed | None | High | None | 21.3-21.23, 23.4.0-23.26.3 |  | 
| CVE-2026-101510 | Oracle Net Services | None | None | No | 4.4 | Local | Low | High | None | Un- changed | None | None | High | 19.3-19.32, 21.3-21.23, 23.4.0-23.26.3 |  | 
| CVE-2026-54399 | Oracle SQLcl (Apache HttpComponents) | None | HTTP | Yes | 3.1 | Network | High | None | Required | Un- changed | None | None | Low | 19.3-19.32, 21.3-21.23, 23.4.0-23.26.3 |  | 
| CVE-2026-73964 | RDBMS | Query Optimizer | Oracle Net | No | 2.7 | Network | Low | High | None | Un- changed | Low | None | None | 19.3-19.32, 21.3-21.23 |  | 

- The patch for CVE-2026-75803 also addresses CVE-2026-14456, CVE-2026-14457, CVE-2026-18798, CVE-2026-54874, CVE-2026-63072, CVE-2026-63074, CVE-2026-63075, and CVE-2026-63076.
- The patch for CVE-2026-54399 also addresses CVE-2025-27820, CVE-2026-40542, and CVE-2026-54428.
- The patch for CVE-2026-59889 also addresses CVE-2026-54515.
- The patch for CVE-2026-93569 also addresses CVE-2026-89044, CVE-2026-93492, CVE-2026-93493, CVE-2026-93494, CVE-2026-93560, CVE-2026-93561, CVE-2026-93563, CVE-2026-93564, CVE-2026-93565, CVE-2026-93566, CVE-2026-93567, CVE-2026-93568, CVE-2026-93572, CVE-2026-93573, CVE-2026-93574, CVE-2026-93575, CVE-2026-93576, CVE-2026-93578, and CVE-2026-93579.

- Clusterware (Apache MINA SSHD): CVE-2026-56624, CVE-2026-56452, CVE-2026-56623 and CVE-2026-58624 \[VEX Justification: vulnerable\_code\_not\_in\_execute\_path\].
- Oracle Spatial and Graph (gdal): CVE-2026-11824, CVE-2025-6965, CVE-2025-70873 and CVE-2026-11822 \[VEX Justification: vulnerable\_code\_not\_in\_execute\_path\].
- RDBMS (Apache Log4j): CVE-2026-49844 \[VEX Justification: vulnerable\_code\_cannot\_be\_controlled\_by\_adversary\].
- RDBMS (Apache Tomcat): CVE-2026-87022, CVE-2026-65182, CVE-2026-65183, CVE-2026-65637, CVE-2026-65905, CVE-2026-65927, CVE-2026-66422, CVE-2026-68525, CVE-2026-68569, CVE-2026-68763, CVE-2026-73180, CVE-2026-73581, CVE-2026-75973, CVE-2026-76183, CVE-2026-77756, CVE-2026-77762, CVE-2026-77791, CVE-2026-78383, CVE-2026-78437, CVE-2026-79677, CVE-2026-86248 and CVE-2026-86350 \[VEX Justification: vulnerable\_code\_not\_in\_execute\_path\].
- RDBMS (DBI): CVE-2026-78030 \[VEX Justification: vulnerable\_code\_cannot\_be\_controlled\_by\_adversary\].
- RDBMS (jline): CVE-2026-56741 \[VEX Justification: vulnerable\_code\_not\_in\_execute\_path\].
- RDBMS (jsoup): CVE-2026-71497 \[VEX Justification: vulnerable\_code\_not\_in\_execute\_path\].

- The following Oracle Database Server vulnerabilities included in this Critical Patch Update affect client-only installations: CVE-2026-75803 and CVE-2026-54399.

This Critical Patch Update contains 2 new security patches for Oracle APEX.  Both of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cpuoct2026verbose.html#APEX)

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-101521 | Oracle APEX | General | HTTPS | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 24.1.0-24.1.21, 24.2.0-24.2.20, 26.1.0-26.1.4 |  | 
| CVE-2026-66010 | Oracle APEX | General (DOMPurify) | HTTP | Yes | 6.1 | Network | Low | None | Required | Changed | Low | Low | None | 24.1.0-24.1.19, 24.2.0-24.2.18, 26.1.0-26.1.2 |  | 

This Critical Patch Update contains 5 new security patches, plus additional third party patches noted below, for Oracle Autonomous Health Framework.  1 of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cpuoct2026verbose.html#AHTF)

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-75803 | Oracle Autonomous Health Framework | AHFCOMMON (OpenSSL) | HTTPS | Yes | 9.1 | Network | Low | None | None | Un- changed | High | High | None | 26.3-26.8 |  | 
| CVE-2026-101452 | Oracle Autonomous Health Framework | AHF Instant Diagnostic Replay | None | No | 7.8 | Local | Low | Low | None | Un- changed | High | High | High | 26.3-26.8 |  | 
| CVE-2026-101477 | Oracle Autonomous Health Framework | Trace File Analyzer | None | No | 7.8 | Local | Low | Low | None | Un- changed | High | High | High | 26.3-26.8 |  | 
| CVE-2026-101478 | Oracle Autonomous Health Framework | Trace File Analyzer | None | No | 7.8 | Local | Low | Low | None | Un- changed | High | High | High | 26.3-26.8 |  | 
| CVE-2026-101485 | Oracle Autonomous Health Framework | Trace File Analyzer | None | No | 6.5 | Local | Low | Low | None | Changed | High | None | None | 26.3-26.8 |  | 

- The patch for CVE-2026-75803 also addresses CVE-2026-2673, CVE-2026-28389, CVE-2026-31789, CVE-2026-31790, and CVE-2026-63073.

- Oracle Autonomous Health Framework
  - Trace File Analyzer (Apache Log4j): CVE-2026-49844 \[VEX Justification: vulnerable\_code\_not\_in\_execute\_path\].

This Critical Patch Update contains 38 new security patches for Oracle Essbase.  14 of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cpuoct2026verbose.html#ESSB)

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-91637 | Oracle Essbase | Security | HTTP | No | 9.9 | Network | Low | Low | None | Changed | High | High | High | 21.8.3.0.0 |  | 
| CVE-2026-91638 | Oracle Essbase | Security | HTTP | No | 9.9 | Network | Low | Low | None | Changed | High | High | High | 21.8.3.0.0 |  | 
| CVE-2026-91658 | Oracle Essbase | Security | HTTP | No | 9.9 | Network | Low | Low | None | Changed | High | High | High | 21.8.3.0.0 |  | 
| CVE-2026-91663 | Oracle Essbase | Security | T3, IIOP | No | 9.9 | Network | Low | Low | None | Changed | High | High | High | 21.8.3.0.0 |  | 
| CVE-2026-91665 | Oracle Essbase | Security | TCP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 21.8.3.0.0 |  | 
| CVE-2026-91644 | Oracle Essbase | Security | HTTP | Yes | 9.3 | Network | Low | None | None | Changed | High | Low | None | 21.8.3.0.0 |  | 
| CVE-2026-91656 | Oracle Essbase | Federated Partitions | HTTP | No | 9.1 | Network | Low | Low | None | Changed | High | Low | Low | 21.8.3.0.0 |  | 
| CVE-2026-91655 | Oracle Essbase | Security | HTTP | No | 9.1 | Network | Low | Low | None | Changed | High | Low | Low | 21.8.3.0.0 |  | 
| CVE-2026-91651 | Oracle Essbase | Essbase Web Platform | HTTP | No | 8.5 | Network | High | Low | None | Changed | High | High | High | 21.8.3.0.0 |  | 
| CVE-2026-91653 | Oracle Essbase | Essbase Web Platform | HTTP | No | 8.5 | Network | Low | Low | None | Changed | High | Low | None | 21.8.3.0.0 |  | 
| CVE-2026-91635 | Oracle Essbase | Security | T3, IIOP | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 21.8.3.0.0 |  | 
| CVE-2026-91647 | Oracle Essbase | Security | TCP | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 21.8.3.0.0 |  | 
| CVE-2026-91659 | Oracle Essbase | Build | HTTP | No | 7.7 | Network | Low | Low | None | Changed | High | None | None | 21.8.3.0.0 |  | 
| CVE-2026-91632 | Oracle Essbase | Security | HTTP | No | 7.7 | Network | Low | Low | None | Changed | High | None | None | 21.8.3.0.0 |  | 
| CVE-2026-91636 | Oracle Essbase | Security | HTTP | No | 7.7 | Network | Low | Low | None | Changed | High | None | None | 21.8.3.0.0 |  | 
| CVE-2026-91639 | Oracle Essbase | Security | HTTP | No | 7.7 | Network | Low | Low | None | Changed | High | None | None | 21.8.3.0.0 |  | 
| CVE-2026-91661 | Oracle Essbase | Security | HTTP | No | 7.7 | Network | Low | Low | None | Changed | High | None | None | 21.8.3.0.0 |  | 
| CVE-2026-54428 | Oracle Essbase | Infrastructure (Apache HttpComponents) | HTTP/2 | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 21.8.3.0.0 |  | 
| CVE-2026-91664 | Oracle Essbase | Security | TCP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 21.8.3.0.0 |  | 
| CVE-2026-91642 | Oracle Essbase | Security | HTTP | Yes | 7.3 | Network | Low | None | None | Un- changed | Low | Low | Low | 21.8.3.0.0 |  | 
| CVE-2026-91630 | Oracle Essbase | Security | HTTP | No | 6.8 | Network | Low | High | None | Changed | High | None | None | 21.8.3.0.0 |  | 
| CVE-2026-91662 | Oracle Essbase | Java Based Agent | None | No | 6.4 | Local | High | Low | None | Changed | High | Low | None | 21.8.3.0.0 |  | 
| CVE-2026-91654 | Oracle Essbase | Security | HTTP | No | 6.3 | Network | Low | Low | None | Un- changed | Low | Low | Low | 21.8.3.0.0 |  | 
| CVE-2026-91649 | Oracle Essbase | Java Based Agent | None | No | 6.0 | Local | Low | High | None | Changed | High | None | None | 21.8.3.0.0 |  | 
| CVE-2026-91633 | Oracle Essbase | Security | None | No | 6.0 | Local | Low | High | None | Changed | High | None | None | 21.8.3.0.0 |  | 
| CVE-2026-91646 | Oracle Essbase | Security | T3, IIOP | Yes | 5.6 | Network | High | None | None | Un- changed | Low | Low | Low | 21.8.3.0.0 |  | 
| CVE-2025-48924 | Oracle Essbase | Infrastructure (Apache Commons Lang) | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | None | None | Low | 21.8.3.0.0 |  | 
| CVE-2026-91643 | Oracle Essbase | Java Based Agent | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | Low | None | None | 21.8.3.0.0 |  | 
| CVE-2026-91645 | Oracle Essbase | Security | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | Low | None | None | 21.8.3.0.0 |  | 
| CVE-2026-91634 | Oracle Essbase | Security | T3, IIOP | Yes | 5.3 | Network | Low | None | None | Un- changed | Low | None | None | 21.8.3.0.0 |  | 
| CVE-2026-91648 | Oracle Essbase | Java Based Agent | TCP | Yes | 5.3 | Network | Low | None | None | Un- changed | Low | None | None | 21.8.3.0.0 |  | 
| CVE-2026-91631 | Oracle Essbase | Security | HTTP | No | 5.0 | Network | Low | Low | None | Changed | Low | None | None | 21.8.3.0.0 |  | 
| CVE-2026-91640 | Oracle Essbase | Security | HTTP | No | 5.0 | Network | Low | Low | None | Changed | Low | None | None | 21.8.3.0.0 |  | 
| CVE-2026-91641 | Oracle Essbase | Security | HTTP | No | 5.0 | Network | Low | Low | None | Changed | Low | None | None | 21.8.3.0.0 |  | 
| CVE-2026-91652 | Oracle Essbase | Security | HTTP | No | 5.0 | Network | Low | Low | None | Changed | Low | None | None | 21.8.3.0.0 |  | 
| CVE-2026-91657 | Oracle Essbase | Security | HTTP | No | 4.3 | Network | Low | Low | None | Un- changed | Low | None | None | 21.8.3.0.0 |  | 
| CVE-2026-91660 | Oracle Essbase | Security | HTTP | No | 4.3 | Network | Low | Low | None | Un- changed | None | None | Low | 21.8.3.0.0 |  | 
| CVE-2026-91650 | Oracle Essbase | Java Based Agent | HTTP | Yes | 3.7 | Network | High | None | None | Un- changed | Low | None | None | 21.8.3.0.0 |  | 

- The patch for CVE-2026-54428 also addresses CVE-2026-54399.

This Critical Patch Update contains 1 new security patch, plus additional third party patches noted below, for Oracle Global Lifecycle Management.  This vulnerability is not remotely exploitable without authentication, i.e., may not be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cpuoct2026verbose.html#GLM)

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-101500 | Oracle Global Lifecycle Management OPatchAuto | Database extensions | None | No | 6.5 | Local | Low | High | Required | Un- changed | High | High | High | 12.2.0.1.16-12.2.0.1.52 |  | 

- Oracle Global Lifecycle Management OPatch
  - Patch Installer: CVE-2026-61308, CVE-2026-60589, CVE-2026-62574 and CVE-2026-70907 \[VEX Justification: vulnerable\_code\_cannot\_be\_controlled\_by\_adversary\].

This Critical Patch Update contains 11 new security patches, plus additional third party patches noted below, for Oracle GoldenGate.  3 of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cpuoct2026verbose.html#GG)

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-87351 | Oracle GoldenGate | Admin Server Executable | HTTPS | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 19.1.0.0.0-19.32.0.0, 21.3-21.23, 23.4-23.26.3.0.0 |  | 
| CVE-2026-91517 | Oracle Management Pack for Oracle GoldenGate | EM Plugin | HTTP | Yes | 8.0 | Adjacent Network | Low | None | Required | Un- changed | High | High | High | 13.4.1.0.1-13.5.2.0.6 |  | 
| CVE-2025-67030 | Oracle GoldenGate Big Data and Application Adapters | Java Delivery (Plexus Utils) | HTTP | Yes | 7.5 | Network | High | None | Required | Un- changed | High | High | High | 21.3-21.20, 23.4-23.26.1 |  | 
| CVE-2026-0636 | Oracle GoldenGate Stream Analytics | Security (Bouncy Castle Java Library) | HTTPS | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 19.1.0.0.0-19.1.0.0.16 |  | 
| CVE-2026-45416 | Oracle GoldenGate Stream Analytics | Security (Netty) | TLS | No | 6.5 | Network | Low | Low | None | Un- changed | None | None | High | 19.1.0.0.0-19.1.0.0.16 |  | 
| CVE-2026-91547 | Oracle GoldenGate | Vendor Access Module | None | No | 5.5 | Local | Low | Low | None | Un- changed | High | None | None | 19.1.0.0.0-19.32.0.0, 21.3-21.23, 23.4-23.26.3.0.0 |  | 
| CVE-2026-101601 | Oracle GoldenGate | Vendor Access Module | None | No | 5.5 | Local | Low | Low | None | Un- changed | High | None | None | 21.3-21.23 |  | 
| CVE-2026-2332 | Oracle GoldenGate Stream Analytics | Security (Eclipse Jetty) | HTTP | Yes | 5.4 | Network | High | None | None | Changed | Low | Low | None | 26.1.0.0.0-26.2.0.0.1 |  | 
| CVE-2025-67721 | Oracle GoldenGate Stream Analytics | General Issues (Aircompressor) | HTTP | No | 5.3 | Network | High | Low | None | Un- changed | High | None | None | 19.1.0.0.0-19.1.0.0.16 |  | 
| CVE-2026-91530 | Oracle GoldenGate | Admin Client Executable | HTTP | No | 4.4 | Network | High | High | None | Un- changed | High | None | None | 23.4-23.26.2.0.0 |  | 
| CVE-2026-54513 | Oracle GoldenGate Stream Analytics | Security (jackson-databind) | None | No | 2.9 | Local | High | None | None | Un- changed | None | Low | None | 26.1.0.0.0-26.2.0.0.1 |  | 

- The patch for CVE-2026-2332 also addresses CVE-2024-6763 and CVE-2025-11143.
- The patch for CVE-2026-45416 also addresses CVE-2025-25193, CVE-2026-33870, CVE-2026-42583, and CVE-2026-42587.

- Oracle GoldenGate Stream Analytics
  - Security (Apache ActiveMQ): CVE-2026-33227 and CVE-2026-39304 \[VEX Justification: vulnerable\_code\_not\_in\_execute\_path\].
  - Security (Apache Ignite): CVE-2025-48977 \[VEX Justification: vulnerable\_code\_not\_in\_execute\_path\].
  - Security (Apache Log4j): CVE-2026-34481, CVE-2025-68161, CVE-2026-34477, CVE-2026-34478, CVE-2026-34479 and CVE-2026-34480 \[VEX Justification: vulnerable\_code\_not\_in\_execute\_path\].
  - Security (Bouncy Castle Java Library): CVE-2026-5588 and CVE-2025-14813 \[VEX Justification: vulnerable\_code\_not\_in\_execute\_path\].
  - Security (Apache Commons Configuration): CVE-2026-45205 \[VEX Justification: vulnerable\_code\_cannot\_be\_controlled\_by\_adversary\].
  - Security (Netty): CVE-2026-42578, CVE-2026-42579, CVE-2026-44249, CVE-2026-44892, CVE-2026-45536, CVE-2026-47244, CVE-2026-47691 and CVE-2026-50009 \[VEX Justification: vulnerable\_code\_not\_in\_execute\_path\].
  - Security (Eclipse Jersey): CVE-2025-12383 \[VEX Justification: vulnerable\_code\_not\_in\_execute\_path\].
  - Security (Vert.x-Web): CVE-2026-6860 \[VEX Justification: vulnerable\_code\_not\_in\_execute\_path\].

This Critical Patch Update contains no new security patches for exploitable vulnerabilities but does include third party patches, noted below, for the following non-exploitable third party CVEs for Oracle Graph Server and Client.  Please refer to previous Critical Patch Update Advisories if the last Critical Patch Update was not applied for the Oracle Graph Server and Client.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cpuoct2026verbose.html#GSC)

- Oracle Graph Server and Client
  - Packaging/install issues (Apache Tomcat): CVE-2026-55956, CVE-2026-50229, CVE-2026-53404, CVE-2026-53434, CVE-2026-55276 and CVE-2026-55955 \[VEX Justification: vulnerable\_code\_not\_in\_execute\_path\].

This Critical Patch Update contains 1 new security patch, plus additional third party patches noted below, for Oracle NoSQL Database.  This vulnerability is remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cpuoct2026verbose.html#NSQL)

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-42587 | Oracle NoSQL Database | Administration (Netty) | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 23.3.41, 24.4.14, 25.3.24 |  | 

- The patch for CVE-2026-42587 also addresses CVE-2026-41417, CVE-2026-42578, CVE-2026-42579, CVE-2026-42580, CVE-2026-42581, CVE-2026-42583, CVE-2026-42584, CVE-2026-42585, CVE-2026-42586, and CVE-2026-44248.

- Oracle NoSQL Database
  - Administration (Aircompressor): CVE-2025-67721 \[VEX Justification: vulnerable\_code\_cannot\_be\_controlled\_by\_adversary\].

This Critical Patch Update contains 35 new security patches for Oracle REST Data Services.  11 of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cpuoct2026verbose.html#REST)

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-91610 | Oracle REST Data Services | General | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 24.2.0-26.2.2 |  | 
| CVE-2026-33941 | Oracle REST Data Services | Database Actions (handlebars) | None | No | 8.2 | Local | Low | Low | Required | Changed | High | High | High | 24.2.0-26.2.1 |  | 
| CVE-2026-9753 | Oracle REST Data Services | General (mongodb) | HTTP | No | 8.1 | Network | Low | Low | None | Un- changed | High | None | High | 24.2.0-26.2.1 |  | 
| CVE-2026-101494 | Oracle REST Data Services | Core | HTTP | No | 7.7 | Network | Low | Low | None | Changed | High | None | None | 24.2.0-26.2.2 |  | 
| CVE-2026-101362 | Oracle REST Data Services | Core | HTTP | Yes | 6.9 | Network | High | None | Required | Changed | Low | High | None | 24.2.0-26.1.0 |  | 
| CVE-2026-91609 | Oracle REST Data Services | Graph QL | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 24.2.0-26.2.1 |  | 
| CVE-2026-101375 | Oracle REST Data Services | Database Actions | HTTP | No | 6.3 | Network | Low | Low | None | Un- changed | Low | Low | Low | 24.2.0-26.1.0 |  | 
| CVE-2026-101369 | Oracle REST Data Services | Backend-as-a-Service | HTTP | Yes | 6.1 | Network | Low | None | Required | Changed | Low | Low | None | 24.2.0-26.1.0 |  | 
| CVE-2026-101374 | Oracle REST Data Services | Backend-as-a-Service | HTTP | Yes | 5.9 | Network | High | None | None | Un- changed | None | High | None | 24.2.0-26.1.0 |  | 
| CVE-2026-101367 | Oracle REST Data Services | ADP | HTTP | No | 5.4 | Network | Low | Low | None | Un- changed | Low | Low | None | 24.2.0-26.1.0 |  | 
| CVE-2026-101380 | Oracle REST Data Services | ADP | HTTP | No | 5.4 | Network | Low | Low | Required | Changed | Low | Low | None | 24.2.0-26.1.0 |  | 
| CVE-2026-101381 | Oracle REST Data Services | ADP | HTTP | No | 5.4 | Network | Low | Low | None | Un- changed | Low | Low | None | 24.2.0-26.1.0 |  | 
| CVE-2026-101368 | Oracle REST Data Services | Backend-as-a-Service | HTTP | Yes | 5.4 | Network | Low | None | Required | Un- changed | Low | Low | None | 24.2.0-26.1.0 |  | 
| CVE-2026-101360 | Oracle REST Data Services | Core | HTTP | No | 5.4 | Network | Low | Low | None | Un- changed | Low | Low | None | 24.2.0-26.1.0 |  | 
| CVE-2026-101383 | Oracle REST Data Services | Core | HTTP | Yes | 5.4 | Network | Low | None | Required | Un- changed | Low | Low | None | 24.2.0-26.1.0 |  | 
| CVE-2026-101493 | Oracle REST Data Services | Core | HTTP | No | 5.4 | Network | Low | Low | None | Un- changed | Low | Low | None | 24.2.0-26.2.1 |  | 
| CVE-2026-101364 | Oracle REST Data Services | Database Actions | HTTP | No | 5.4 | Network | Low | Low | Required | Changed | Low | Low | None | 24.2.0-26.1.0 |  | 
| CVE-2026-101379 | Oracle REST Data Services | ADP | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | Low | None | None | 24.2.0-26.1.0 |  | 
| CVE-2026-101359 | Oracle REST Data Services | Core | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | None | Low | None | 24.2.0-26.1.0 |  | 
| CVE-2026-54515 | Oracle REST Data Services | General (jackson-databind) | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | None | Low | None | 24.2.0-26.2.1 |  | 
| CVE-2026-101363 | Oracle REST Data Services | Graph QL | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | Low | None | None | 24.2.0-26.1.0 |  | 
| CVE-2026-101384 | Oracle REST Data Services | Core | HTTP | No | 5.0 | Network | Low | Low | None | Changed | Low | None | None | 24.2.0-26.1.0 |  | 
| CVE-2026-101385 | Oracle REST Data Services | Core | HTTP | No | 4.9 | Network | Low | High | None | Un- changed | None | High | None | 24.2.0-26.1.0 |  | 
| CVE-2026-101365 | Oracle REST Data Services | Database Actions | HTTP | No | 4.7 | Network | Low | High | None | Un- changed | Low | Low | Low | 24.2.0-26.1.0 |  | 
| CVE-2026-101376 | Oracle REST Data Services | Database Actions | HTTP | No | 4.7 | Network | Low | High | None | Un- changed | Low | Low | Low | 24.2.0-26.1.0 |  | 
| CVE-2026-101366 | Oracle REST Data Services | ADP | HTTP | No | 4.3 | Network | Low | Low | None | Un- changed | Low | None | None | 24.2.0-26.1.0 |  | 
| CVE-2026-101378 | Oracle REST Data Services | ADP | HTTP | No | 4.3 | Network | Low | Low | None | Un- changed | None | Low | None | 24.2.0-26.1.0 |  | 
| CVE-2026-101361 | Oracle REST Data Services | Core | HTTP | No | 4.2 | Network | High | Low | None | Un- changed | Low | Low | None | 24.2.0-26.1.0 |  | 
| CVE-2026-101382 | Oracle REST Data Services | Core | HTTP | No | 4.2 | Network | High | Low | None | Un- changed | Low | Low | None | 24.2.0-26.1.0 |  | 
| CVE-2026-101386 | Oracle REST Data Services | Core | HTTP | No | 4.2 | Network | High | Low | None | Un- changed | Low | Low | None | 24.2.0-26.1.0 |  | 
| CVE-2026-101372 | Oracle REST Data Services | Core | HTTP | Yes | 3.7 | Network | High | None | None | Un- changed | Low | None | None | 24.2.0-26.1.0 |  | 
| CVE-2026-101370 | Oracle REST Data Services | Core | HTTP | Yes | 3.1 | Network | High | None | Required | Un- changed | Low | None | None | 24.2.0-26.1.0 |  | 
| CVE-2026-101371 | Oracle REST Data Services | Core | HTTP | No | 3.1 | Network | High | High | Required | Un- changed | Low | Low | None | 24.2.0-26.1.0 |  | 
| CVE-2026-101377 | Oracle REST Data Services | Database Actions | HTTP | No | 2.7 | Network | Low | High | None | Un- changed | None | None | Low | 24.2.0-26.1.0 |  | 
| CVE-2026-101373 | Oracle REST Data Services | Core | HTTP | No | 2.4 | Network | Low | High | Required | Un- changed | None | Low | None | 24.2.0-26.1.0 |  | 

- The patch for CVE-2026-33941 also addresses CVE-2026-33937, CVE-2026-33938, CVE-2026-33939, and CVE-2026-33940.
- The patch for CVE-2026-54515 also addresses CVE-2026-54512, CVE-2026-54513, and CVE-2026-54514.

This Critical Patch Update contains 6 new security patches, plus additional third party patches noted below, for Oracle Secure Backup.  3 of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cpuoct2026verbose.html#OSB)

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-101484 | Oracle Secure Backup | Backup and Restore | TCP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 19.1.0.0.0, 19.1.0.1.0 |  | 
| CVE-2026-101481 | Oracle Secure Backup | Device Management and Support | None | No | 8.8 | Local | Low | Low | None | Changed | High | High | High | 19.1.0.0.0, 19.1.0.1.0 |  | 
| CVE-2026-101479 | Oracle Secure Backup | Backup and Restore | TCP | Yes | 8.6 | Network | Low | None | None | Changed | None | None | High | 19.1.0.0.0, 19.1.0.1.0 |  | 
| CVE-2026-101482 | Oracle Secure Backup | Device Management and Support | None | No | 7.8 | Local | Low | Low | None | Un- changed | High | High | High | 19.1.0.0.0, 19.1.0.1.0 |  | 
| CVE-2026-101483 | Oracle Secure Backup | Device Management and Support | None | No | 6.5 | Local | Low | Low | None | Changed | None | None | High | 19.1.0.0.0, 19.1.0.1.0 |  | 
| CVE-2026-101480 | Oracle Secure Backup | NDMP daemon | TCP | Yes | 5.3 | Network | Low | None | None | Un- changed | Low | None | None | 19.1.0.0.0, 19.1.0.1.0 |  | 

- Oracle Secure Backup
  - Secure Backup (Apache HTTP Server): CVE-2026-29167, CVE-2026-29170, CVE-2026-34355, CVE-2026-34356, CVE-2026-42535, CVE-2026-42536, CVE-2026-43951, CVE-2026-44119, CVE-2026-44185, CVE-2026-44186, CVE-2026-44631, CVE-2026-48913 and CVE-2026-49975 \[VEX Justification: vulnerable\_code\_not\_in\_execute\_path\].

This Critical Patch Update contains 1 new security patch, plus additional third party patches noted below, for Oracle SQL Developer.  This vulnerability is remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cpuoct2026verbose.html#SQLD)

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2025-4949 | Oracle SQL Developer | Infrastructure (Eclipse JGit) | HTTP | Yes | 5.3 | Network | High | None | Required | Un- changed | None | None | High | 23.1.1-26.1.0 |  | 

- Oracle SQL Developer
  - Installation (Apache Log4j): CVE-2026-34481, CVE-2025-68161, CVE-2026-34477, CVE-2026-34478, CVE-2026-34479 and CVE-2026-34480 \[VEX Justification: vulnerable\_code\_not\_in\_execute\_path\].

This Critical Patch Update contains 4 new security patches for Oracle TimesTen In-Memory Database.  None of these vulnerabilities may be remotely exploitable without authentication, i.e., none may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cpuoct2026verbose.html#XTEN)

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-39822 | Oracle TimesTen In-Memory Database | EM TimesTen plug-in (Golang Go) | None | No | 7.8 | Local | Low | Low | None | Un- changed | High | High | High | 26.1-26.1.1.3.0, 22.1-22.1.1.41.0 |  | 
| CVE-2026-101522 | Oracle TimesTen In-Memory Database | TimesTen IMDB | None | No | 5.5 | Local | Low | Low | None | Un- changed | High | None | None | 22.1-22.1.1.43.0 |  | 
| CVE-2026-87354 | Oracle TimesTen In-Memory Database | Kubernetes Operator | HTTPS | No | 4.3 | Network | Low | Low | None | Un- changed | Low | None | None | 22.1-22.1.40.0, 26.1-26.1.1.2.0 |  | 
| CVE-2026-101600 | Oracle TimesTen In-Memory Database | TimesTen IMDB | None | No | 3.6 | Local | High | Low | None | Un- changed | Low | Low | None | 26.1-26.1.1.3.0 |  | 

- The patch for CVE-2026-39822 also addresses CVE-2026-42505.

This Critical Patch Update contains 8 new security patches for Oracle Trusted Answer Search.  1 of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cpuoct2026verbose.html#TAS)

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-101501 | Oracle Trusted Answer Search | PLSQL package | Oracle Net | No | 9.9 | Network | Low | Low | None | Changed | Low | High | High | 26.1 |  | 
| CVE-2026-101503 | Oracle Trusted Answer Search | PLSQL package | Oracle Net | No | 9.9 | Network | Low | Low | None | Changed | High | High | High | 26.1 |  | 
| CVE-2026-101505 | Oracle Trusted Answer Search | Application expert UI | HTTP | No | 8.7 | Network | Low | Low | Required | Changed | High | High | None | 26.1 |  | 
| CVE-2026-101498 | Oracle Trusted Answer Search | PLSQL package | Oracle Net | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 26.1 |  | 
| CVE-2026-101506 | Oracle Trusted Answer Search | Application expert UI | HTTP | No | 7.7 | Network | Low | Low | None | Changed | High | None | None | 26.1 |  | 
| CVE-2026-101504 | Oracle Trusted Answer Search | Application expert UI | HTTP | No | 7.6 | Network | Low | Low | Required | Changed | High | Low | None | 26.1 |  | 
| CVE-2026-101507 | Oracle Trusted Answer Search | PLSQL package | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 26.1 |  | 
| CVE-2026-101502 | Oracle Trusted Answer Search | PLSQL package | None | No | 5.0 | Local | High | Low | Required | Changed | Low | Low | Low | 26.1 |  | 

This Critical Patch Update contains 2 new security patches for Oracle Application Testing Suite.  Neither of these vulnerabilities may be remotely exploitable without authentication, i.e., neither may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cpuoct2026verbose.html#OATS)

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-101549 | Oracle Application Testing Suite | OpenScript | None | No | 7.8 | Local | Low | Low | None | Un- changed | High | High | High | 13.3.0.1 |  | 
| CVE-2026-101548 | Oracle Application Testing Suite | OpenScript | None | No | 7.0 | Local | High | Low | None | Un- changed | High | High | High | 13.3.0.1 |  | 

This Critical Patch Update contains 3 new security patches, plus additional third party patches noted below, for Oracle Commerce.  2 of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cpuoct2026verbose.html#OCOM)

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-101560 | Oracle Commerce Platform | Dynamo Commerce Server | HTTP | No | 7.1 | Network | Low | Low | None | Un- changed | Low | High | None | 11.4.0 |  | 
| CVE-2026-49844 | Oracle Commerce Platform | Dynamo Application Framework (Apache Log4j) | HTTP | Yes | 5.9 | Network | High | None | None | Un- changed | None | High | None | 11.4.0 |  | 
| CVE-2026-54515 | Oracle Commerce Platform | Dynamo Application Framework (jackson-databind) | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | None | Low | None | 11.4.0 |  | 

- The patch for CVE-2026-49844 also addresses CVE-2026-34481.
- The patch for CVE-2026-54515 also addresses CVE-2026-54512, CVE-2026-54513, and CVE-2026-54514.

- Oracle Commerce Platform
  - Dynamo Application Framework (Spring Framework): CVE-2026-41855, CVE-2026-22737, CVE-2026-22740, CVE-2026-41853, CVE-2026-47884, CVE-2026-47886, CVE-2026-47887, CVE-2026-47888, CVE-2026-47891, CVE-2026-47892, CVE-2026-47893, CVE-2026-59280, CVE-2026-59281, CVE-2026-59282, CVE-2026-59283, CVE-2026-59313 and CVE-2026-59314 \[VEX Justification: component\_not\_present\].

This Critical Patch Update contains 110 new security patches for Oracle Communications.  77 of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cpuoct2026verbose.html#CGBU)

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-101763 | Oracle Communications BRM - Elastic Charging Engine | Cloud native deployment | RMI | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 15.0.0.0.0, 15.0.1.0.0, 15.1.0.0.0, 15.2.0.0.0 |  | 
| CVE-2026-5450 | Oracle Communications Cloud Native Core Binding Support Function | Configuration (glibc) | HTTPS | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 25.2.201 |  | 
| CVE-2026-6653 | Oracle Communications Cloud Native Core Certificate Management | Configuration (libxml2) | HTTP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 26.1.200 |  | 
| CVE-2026-6653 | Oracle Communications Cloud Native Core Console | Console (libxml2) | HTTP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 25.2.202,26.1.200 |  | 
| CVE-2026-29167 | Oracle Communications Cloud Native Core Security Edge Protection Proxy | Automated Test Suite Framework (Apache HTTP Server) | HTTP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 25.2.200, 26.1.200 |  | 
| CVE-2026-29167 | Oracle Communications Policy Management | CMP (Apache HTTP Server) | HTTP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 15.0.0.0.0, 15.1.0.0.0 |  | 
| CVE-2026-64193 | Oracle Communications Unified Assurance | Core (Net::DNS) | DNS | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 6.1.1-7.0.0 |  | 
| CVE-2026-86219 | Oracle Communications Unified Assurance | Core (Authen::SASL) | HTTP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 6.1.1-7.0.0 |  | 
| CVE-2026-78030 | Oracle Communications Unified Assurance | Core (DBI) | HTTP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 6.1.1-7.0.0 |  | 
| CVE-2026-54906 | Oracle Communications Unified Assurance | Core (Ruby) | HTTP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 6.1.1-7.0.0 |  | 
| CVE-2026-39892 | Oracle Communications Unified Assurance | Microservices (pyca-cryptography) | HTTP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 6.1.1-7.0.0 |  | 
| CVE-2026-75596 | Oracle Communications Unified Assurance | Core (Netty) | TLS | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 6.1.1-7.0.0 |  | 
| CVE-2026-101765 | Oracle Communications Billing and Revenue Management | BRM Server | HTTP | Yes | 9.1 | Network | Low | None | None | Un- changed | High | High | None | 15.0.0.0.0, 15.0.1.0.0, 15.1.0.0.0, 15.2.0.0.0 |  | 
| CVE-2026-28369 | Oracle Communications Cloud Native Core Binding Support Function | Install/Upgrade (Undertow) | HTTP | Yes | 9.1 | Network | Low | None | None | Un- changed | High | High | None | 25.2.200 |  | 
| CVE-2026-58016 | Oracle Communications Cloud Native Core Certificate Management | Configuration (glib) | HTTP | Yes | 9.1 | Network | Low | None | None | Un- changed | High | None | High | 26.1.200 |  | 
| CVE-2026-84939 | Oracle Communications Cloud Native Core Console | CNC Console (class) | HTTP | Yes | 9.1 | Network | Low | None | None | Un- changed | High | High | None | 25.2.202, 26.1.200 |  | 
| CVE-2026-58016 | Oracle Communications Cloud Native Core Console | Console (glib) | HTTP | Yes | 9.1 | Network | Low | None | None | Un- changed | High | None | High | 25.2.202,26.1.200 |  | 
| CVE-2026-28369 | Oracle Communications Cloud Native Core Policy | Alarms, KPI, and Measurements (Undertow) | HTTP | Yes | 9.1 | Network | Low | None | None | Un- changed | High | High | None | 25.2.200 |  | 
| CVE-2026-8763 | Oracle Communications Cloud Native Core Security Edge Protection Proxy | Signaling (Bouncy Castle Java Library) | HTTPS | Yes | 9.1 | Network | Low | None | None | Un- changed | High | High | None | 25.2.200, 26.1.200 |  | 
| CVE-2026-8763 | Oracle Communications Cloud Native Core Unified Data Repository | Configuration (Bouncy Castle Java Library) | HTTPS | Yes | 9.1 | Network | Low | None | None | Un- changed | High | High | None | 25.2.200,26.1.200 |  | 
| CVE-2026-75595 | Oracle Communications Cloud Native Core Unified Data Repository | Configuration (Netty) | TLS | Yes | 9.1 | Network | Low | None | None | Un- changed | High | High | None | 25.2.200,26.1.200 |  | 
| CVE-2026-75595 | Oracle Communications Service Catalog and Design | Third Party (Netty) | TLS | Yes | 9.1 | Network | Low | None | None | Un- changed | High | High | None | 8.0-8.1 |  | 
| CVE-2026-84939 | Oracle Communications Unified Assurance | Core (Apache FreeMarker) | HTTP | Yes | 9.1 | Network | Low | None | None | Un- changed | High | High | None | 6.1.1-7.0.0 |  | 
| CVE-2026-32327 | Oracle Communications Unified Assurance | Core (Apache Portable Runtime) | HTTP | Yes | 9.1 | Network | Low | None | None | Un- changed | High | None | High | 6.1.1-7.0.0 |  | 
| CVE-2026-56130 | Oracle Communications Unified Assurance | Core (Apache Shiro) | HTTP | Yes | 9.1 | Network | Low | None | None | Un- changed | High | High | None | 6.1.1-7.0.0 |  | 
| CVE-2026-58389 | Oracle Communications Unified Assurance | Core (Apache Thrift) | HTTP | Yes | 9.1 | Network | Low | None | None | Un- changed | High | None | High | 6.1.1-7.0.0 |  | 
| CVE-2026-10050 | Oracle Communications Unified Assurance | Core (Eclipse Jetty) | HTTP | Yes | 9.1 | Network | Low | None | None | Un- changed | High | None | High | 7.0.0 |  | 
| CVE-2026-13221 | Oracle Communications Unified Assurance | Core (Perl) | HTTP | Yes | 9.1 | Network | Low | None | None | Un- changed | None | High | High | 6.1.1-7.0.0 |  | 
| CVE-2026-68525 | Oracle Communications Unified Assurance | Microservices (Apache Tomcat) | HTTP | Yes | 9.1 | Network | Low | None | None | Un- changed | High | High | None | 7.0.0 |  | 
| CVE-2026-61674 | Oracle Communications Unified Assurance | Core (fluentbit) | TCP | Yes | 9.1 | Network | Low | None | None | Un- changed | High | High | None | 6.1.1-7.0.0 |  | 
| CVE-2025-48734 | Oracle Communications EAGLE Element Management System | Security (Apache Commons BeanUtils) | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 47.0.0.2.0 |  | 
| CVE-2026-63639 | Oracle Communications Unified Assurance | Core (valkey) | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 7.0.0 |  | 
| CVE-2026-13321 | Oracle Communications Cloud Native Core Console | Console (BIND) | DNS | Yes | 8.6 | Network | Low | None | None | Changed | None | High | None | 25.2.202, 26.1.200 |  | 
| CVE-2026-13321 | Oracle Communications Cloud Native Core Security Edge Protection Proxy | Install (BIND) | DNS | Yes | 8.6 | Network | Low | None | None | Changed | None | High | None | 25.2.200, 26.1.200 |  | 
| CVE-2026-63388 | Oracle Communications Cloud Native Core Security Edge Protection Proxy | Install (libevent) | None | No | 8.4 | Local | Low | None | None | Un- changed | High | High | High | 25.2.200, 26.1.200 |  | 
| CVE-2026-21716 | Oracle Communications Unified Assurance | Core (Node.js) | None | No | 8.4 | Local | Low | Low | None | Changed | High | High | None | 6.1.1-7.0.0 |  | 
| CVE-2026-101758 | Oracle Communications Billing and Revenue Management | BRM Server | HTTP | Yes | 8.2 | Network | Low | None | None | Un- changed | High | Low | None | 15.0.0.0.0, 15.0.1.0.0, 15.1.0.0.0, 15.2.0.0.0 |  | 
| CVE-2026-101791 | Oracle Communications BRM - Elastic Charging Engine | Security | TLS | No | 8.1 | Network | Low | Low | None | Un- changed | High | High | None | 15.2.0.0.0 |  | 
| CVE-2026-41855 | Oracle Communications Unified Assurance | Core (Spring Framework) | HTTP | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 6.1.1-7.0.0 |  | 
| CVE-2026-91627 | Oracle Communications Billing and Revenue Management | Platform | None | No | 7.8 | Local | Low | Low | None | Un- changed | High | High | High | 15.0.0.0.0, 15.0.1.0.0, 15.1.0.0.0, 15.2.0.0.0 |  | 
| CVE-2026-101759 | Oracle Communications Billing and Revenue Management | BRM Server | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | High | None | None | 15.0.0.0.0, 15.0.1.0.0, 15.1.0.0.0, 15.2.0.0.0 |  | 
| CVE-2026-54399 | Oracle Communications Billing and Revenue Management | BRM Server (Apache HttpClient) | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 15.0.0.0.0, 15.0.1.0.0, 15.1.0.0.0, 15.2.0.0.0 |  | 
| CVE-2026-56740 | Oracle Communications Billing and Revenue Management | BRM Server (jline) | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 15.0.0.0.0, 15.0.1.0.0, 15.1.0.0.0, 15.2.0.0.0 |  | 
| CVE-2026-54874 | Oracle Communications Cloud Native Core Certificate Management | Configuration (OpenSSL) | HTTPS | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 25.2.201, 26.1.200 |  | 
| CVE-2025-13151 | Oracle Communications Cloud Native Core Network Repository Function | Install (Libtasn1) | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 25.2.202,26.1.202 |  | 
| CVE-2026-21441 | Oracle Communications Cloud Native Core Network Slice Selection Function | Install (urllib3) | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 25.2.200 |  | 
| CVE-2026-5928 | Oracle Communications Cloud Native Core Security Edge Protection Proxy | Install (glibc) | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 25.2.200, 26.1.200 |  | 
| CVE-2026-55831 | Oracle Communications Cloud Native Core Security Edge Protection Proxy | Signaling (Netty) | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 25.2.200, 26.1.200 |  | 
| CVE-2025-13151 | Oracle Communications Cloud Native Core Service Communication Proxy | Install (Libtasn1) | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 25.1.100, 25.1.200, 25.2.100, 25.2.200 |  | 
| CVE-2026-68494 | Oracle Communications Cloud Native Core Unified Data Repository | Configuration (jackson-core) | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 25.2.200,26.1.200 |  | 
| CVE-2026-68497 | Oracle Communications Cloud Native Core Unified Data Repository | Configuration (jackson-databind) | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 25.2.200,26.1.200 |  | 
| CVE-2026-34481 | Oracle Communications EAGLE Element Management System | Security (Apache Log4j) | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | High | None | 47.0.0.2.0 |  | 
| CVE-2026-34487 | Oracle Communications EAGLE Element Management System | Security (Apache Tomcat) | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | High | None | None | 47.0.0.2.0 |  | 
| CVE-2024-47072 | Oracle Communications EAGLE Element Management System | Security (XStream) | HTTPS | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 47.0.0.2.0 |  | 
| CVE-2025-13151 | Oracle Communications EAGLE LNP Application Processor | Platform (Libtasn1) | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 11.0 |  | 
| CVE-2025-13151 | Oracle Communications LSMS | Platform (Libtasn1) | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 14.0 |  | 
| CVE-2025-13151 | Oracle Communications Policy Management | CMP (Libtasn1) | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 15.0.0.0.0, 15.1.0.0.0 |  | 
| CVE-2026-69247 | Oracle Communications Unified Assurance | Core (Cryptography) | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 6.1.1-7.0.0 |  | 
| CVE-2026-60075 | Oracle Communications Unified Assurance | Core (Date::Manip) | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 6.1.1-7.0.0 |  | 
| CVE-2026-55971 | Oracle Communications Unified Assurance | Core (Erlang/OTP) | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 7.0.0 |  | 
| CVE-2026-101603 | Oracle Communications Unified Inventory Management | Security | HTTP | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 7.5.0,7.5.1,7.6.0,7.7.0,7.8.0,8.0.1 |  | 
| CVE-2026-101604 | Oracle Communications Unified Inventory Management | Security | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | High | None | None | 7.5.0,7.5.1,7.6.0,7.7.0,7.8.0,8.0.1 |  | 
| CVE-2026-101680 | Oracle Communications Billing and Revenue Management | Platform | TLS | Yes | 7.4 | Network | High | None | None | Un- changed | High | High | None | 15.0.0.0.0, 15.0.1.0.0, 15.1.0.0.0, 15.2.0.0.0 |  | 
| CVE-2026-5795 | Oracle Communications EAGLE Element Management System | Security (Eclipse Jetty) | HTTP | Yes | 7.4 | Network | High | None | None | Un- changed | High | High | None | 47.0.0.2.0 |  | 
| CVE-2021-42576 | Oracle Communications Unified Assurance | Core (bluemonday) | HTTP | No | 6.8 | Network | Low | High | Required | Un- changed | High | High | High | 7.0.0 |  | 
| CVE-2026-83406 | Oracle Communications Billing and Revenue Management | Platform | None | No | 6.7 | Local | Low | High | None | Un- changed | High | High | High | 15.0.0.0.0, 15.0.1.0.0, 15.1.0.0.0, 15.2.0.0.0 |  | 
| CVE-2026-87297 | Oracle Communications Billing and Revenue Management | Platform | None | No | 6.7 | Local | Low | High | None | Un- changed | High | High | High | 15.0.0.0.0, 15.0.1.0.0, 15.1.0.0.0, 15.2.0.0.0 |  | 
| CVE-2026-41989 | Oracle Communications Cloud Native Core Network Repository Function | Install (libgcrypt) | None | No | 6.7 | Local | High | None | None | Un- changed | None | High | High | 25.2.202,26.1.202 |  | 
| CVE-2026-41989 | Oracle Communications Cloud Native Core Security Edge Protection Proxy | Signaling (libgcrypt) | None | No | 6.7 | Local | High | None | None | Un- changed | None | High | High | 25.2.200, 26.1.200 |  | 
| CVE-2026-41989 | Oracle Communications Cloud Native Core Service Communication Proxy | Install (libgcrypt) | None | No | 6.7 | Local | High | None | None | Un- changed | None | High | High | 25.2.200, 26.1.200 |  | 
| CVE-2026-41989 | Oracle Communications EAGLE LNP Application Processor | Platform (libgcrypt) | None | No | 6.7 | Local | High | None | None | Un- changed | None | High | High | 11.0 |  | 
| CVE-2026-41989 | Oracle Communications LSMS | Platform (libgcrypt) | None | No | 6.7 | Local | High | None | None | Un- changed | None | High | High | 14.0 |  | 
| CVE-2026-41989 | Oracle Communications Network Analytics Data Director | Third Party (libgcrypt) | None | No | 6.7 | Local | High | None | None | Un- changed | None | High | High | 25.1.200, 25.2.100, 25.2.200 |  | 
| CVE-2026-54512 | Oracle Communications Network Analytics Data Director | Third Party (jackson-databind) | HTTP | No | 6.6 | Network | High | High | None | Un- changed | High | High | High | 25.1.200, 25.2.100, 25.2.200 |  | 
| CVE-2026-59889 | Oracle Communications Billing and Revenue Management | BRM Server (jackson-databind) | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | None | High | None | 15.1.0.0.0, 15.2.0.0.0 |  | 
| CVE-2026-101606 | Oracle Communications Billing and Revenue Management | BRM Server | TLS | Yes | 6.5 | Network | Low | None | None | Un- changed | Low | Low | None | 15.0.0.0.0, 15.0.1.0.0, 15.1.0.0.0, 15.2.0.0.0 |  | 
| CVE-2026-59949 | Oracle Communications BRM - Elastic Charging Engine | Third Party (lz4-java) | HTTP | Yes | 6.5 | Network | High | None | None | Un- changed | Low | None | High | 15.0.0.0.0, 15.0.1.0.0, 15.1.0.0.0, 15.2.0.0.0 |  | 
| CVE-2026-55956 | Oracle Communications Cloud Native Core Policy | Alarms, KPI, and Measurements (Apache Tomcat) | HTTP | Yes | 6.5 | Network | Low | None | None | Un- changed | Low | Low | None | 25.2.200 |  | 
| CVE-2026-55956 | Oracle Communications EAGLE Element Management System | Platform (Apache Tomcat) | HTTP | Yes | 6.5 | Network | Low | None | None | Un- changed | Low | Low | None | 47.0.0.2.0 |  | 
| CVE-2026-55956 | Oracle Communications Policy Management | CMP (Apache Tomcat) | HTTP | Yes | 6.5 | Network | Low | None | None | Un- changed | Low | Low | None | 15.0.0.0.0, 15.1.0.0.0 |  | 
| CVE-2026-59889 | Oracle Communications Service Catalog and Design | Third Party (jackson-databind) | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | None | High | None | 8.0-8.3 |  | 
| CVE-2026-4800 | Oracle Communications Unified Assurance | Core (Lodash) | HTTP | No | 6.4 | Network | High | High | Required | Un- changed | High | High | High | 7.0.0 |  | 
| CVE-2026-54369 | Oracle Communications Network Analytics Data Director | Third Party (libacl) | None | No | 6.3 | Local | High | Low | None | Un- changed | High | High | None | 25.1.200, 25.2.100, 25.2.200 |  | 
| CVE-2024-38356 | Oracle Communications EAGLE Element Management System | Platform (TinyMCE) | HTTPS | Yes | 6.1 | Network | Low | None | Required | Changed | Low | Low | None | 47.0.0.2.0 |  | 
| CVE-2026-49844 | Oracle Communications Billing and Revenue Management | Platform (Apache Log4j) | HTTP | Yes | 5.9 | Network | High | None | None | Un- changed | None | High | None | 15.0.0.0.0, 15.0.1.0.0, 15.1.0.0.0, 15.2.0.0.0 |  | 
| CVE-2026-101792 | Oracle Communications BRM - Elastic Charging Engine | Security | Radius | Yes | 5.9 | Adjacent Network | High | None | None | Un- changed | Low | High | None | 15.0.0.0.0, 15.0.1.0.0, 15.1.0.0.0, 15.2.0.0.0 |  | 
| CVE-2026-55858 | Oracle Communications Cloud Native Core Console | Configuration (JDBC) | MySQL Protocol | Yes | 5.9 | Network | High | None | None | Un- changed | None | High | None | 25.2.202, 26.1.200 |  | 
| CVE-2026-54291 | Oracle Communications Cloud Native Core Console | Console (PostgreSQL JDBC Driver) | TLS | Yes | 5.9 | Network | High | None | None | Un- changed | None | High | None | 25.2.202, 26.1.200 |  | 
| CVE-2026-59901 | Oracle Communications Network Analytics Data Director | Third Party (Netty) | HTTP | Yes | 5.9 | Network | High | None | None | Un- changed | None | None | High | 25.1.200, 25.2.100, 25.2.200 |  | 
| CVE-2026-27601 | Oracle Communications Operations Monitor | Front-end (underscore) | HTTPS | Yes | 5.9 | Network | High | None | None | Un- changed | None | None | High | 6.0, 6.1 |  | 
| CVE-2026-58014 | Oracle Communications Network Analytics Data Director | Third Party (glib) | HTTP | Yes | 5.6 | Network | High | None | None | Un- changed | Low | Low | Low | 25.1.200, 25.2.100, 25.2.200 |  | 
| CVE-2026-91628 | Oracle Communications Billing and Revenue Management | BRM Server | None | No | 5.5 | Local | Low | Low | None | Un- changed | High | None | None | 15.0.0.0.0, 15.0.1.0.0, 15.1.0.0.0, 15.2.0.0.0 |  | 
| CVE-2026-101764 | Oracle Communications Billing and Revenue Management | BRM Server | None | No | 5.5 | Local | Low | Low | None | Un- changed | High | None | None | 15.0.0.0.0, 15.0.1.0.0, 15.1.0.0.0, 15.2.0.0.0 |  | 
| CVE-2026-101793 | Oracle Communications BRM - Elastic Charging Engine | Core | None | No | 5.5 | Local | Low | Low | None | Un- changed | High | None | None | 15.0.0.0.0, 15.0.1.0.0, 15.1.0.0.0, 15.2.0.0.0 |  | 
| CVE-2024-6763 | Oracle Communications Cloud Native Core Policy | Alarms, KPI, and Measurements (Eclipse Jetty) | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | None | Low | None | 24.2.4-25.2.000 |  | 
| CVE-2025-48924 | Oracle Communications Cloud Native Core Security Edge Protection Proxy | Automated Test Suite Framework (Apache Commons Lang) | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | None | None | Low | 25.2.201, 26.1.200 |  | 
| CVE-2025-48924 | Oracle Communications Cloud Native Core Service Communication Proxy | Install (Apache Commons Lang) | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | None | None | Low | 25.1.200, 25.2.100, 25.2.200 |  | 
| CVE-2026-45292 | Oracle Communications Cloud Native Core Unified Data Repository | Install (OpenTelemetry-Go) | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | None | None | Low | 25.2.200,26.1.200 |  | 
| CVE-2025-48924 | Oracle Communications Cloud Native Core Unified Data Repository | Signaling (Apache Commons Lang) | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | None | None | Low | 25.1.200 |  | 
| CVE-2026-7168 | Oracle Communications Unified Assurance | Core (libcurl) | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | Low | None | None | 6.1.1-7.0.0 |  | 
| CVE-2026-41001 | Oracle Communications Unified Assurance | Core (Spring Boot) | None | No | 5.3 | Local | Low | Low | None | Un- changed | Low | Low | Low | 6.1.1-7.0.0 |  | 
| CVE-2026-8643 | Oracle Communications Billing and Revenue Management | BRM Server (pip) | None | No | 5.0 | Local | Low | Low | Required | Un- changed | None | High | None | 15.0.1.0.0, 15.1.0.0.0, 15.2.0.0.0 |  | 
| CVE-2026-5704 | Oracle Communications Cloud Native Core Console | Configuration (node-tar) | None | No | 5.0 | Local | Low | Low | Required | Un- changed | None | High | None | 25.2.202, 26.1.200 |  | 
| CVE-2026-22702 | Oracle Communications Unified Assurance | Core (virtualenv) | None | No | 4.9 | Local | High | None | None | Un- changed | Low | Low | Low | 6.1.1-7.0.0 |  | 
| CVE-2026-101807 | Oracle Communications Billing and Revenue Management | BRM Server | HTTP | Yes | 4.8 | Network | High | None | None | Un- changed | Low | Low | None | 15.0.0.0.0, 15.0.1.0.0, 15.1.0.0.0, 15.2.0.0.0 |  | 
| CVE-2026-91629 | Oracle Communications Billing and Revenue Management | Platform | None | No | 4.7 | Local | High | Low | None | Un- changed | High | None | None | 15.0.0.0.0, 15.0.1.0.0, 15.1.0.0.0, 15.2.0.0.0 |  | 
| CVE-2026-101790 | Oracle Communications BRM - Elastic Charging Engine | Security | None | No | 3.3 | Local | Low | Low | None | Un- changed | Low | None | None | 15.0.0.0.0, 15.0.1.0.0, 15.1.0.0.0, 15.2.0.0.0 |  | 
| CVE-2026-91612 | Oracle Communications Unified Inventory Management | Security | None | No | 3.3 | Local | Low | Low | None | Un- changed | Low | None | None | 7.5.0,7.5.1,7.6.0,7.7.0,7.8.0,8.0.1 |  | 
| CVE-2026-91613 | Oracle Communications Unified Inventory Management | Security | None | No | 3.3 | Local | Low | Low | None | Un- changed | Low | None | None | 7.5.0,7.5.1,7.6.0,7.7.0,7.8.0,8.0.1 |  | 
| CVE-2026-91614 | Oracle Communications Unified Inventory Management | Security | None | No | 3.3 | Local | Low | Low | None | Un- changed | Low | None | None | 7.5.0,7.5.1,7.6.0,7.7.0,7.8.0,8.0.1 |  | 

- The patch for CVE-2026-39892 also addresses CVE-2026-34073, CVE-2026-34180, CVE-2026-69247, CVE-2026-69248, and CVE-2026-69249.
- The patch for CVE-2026-8643 also addresses CVE-2026-1703, CVE-2026-3219, and CVE-2026-6357.
- The patch for CVE-2026-55956 also addresses CVE-2026-50229, CVE-2026-53404, CVE-2026-53434, CVE-2026-55276, and CVE-2026-55955.
- The patch for CVE-2026-56130 also addresses CVE-2026-43827, CVE-2026-43828, CVE-2026-44598, CVE-2026-48589, CVE-2026-49268, and CVE-2026-56091.
- The patch for CVE-2026-13321 also addresses CVE-2026-10723, CVE-2026-11331, CVE-2026-11622, CVE-2026-11721, and CVE-2026-13204.
- The patch for CVE-2026-58389 also addresses CVE-2025-48431, CVE-2026-41602, CVE-2026-41604, CVE-2026-41605, CVE-2026-41606, CVE-2026-41607, CVE-2026-41608, CVE-2026-41636, CVE-2026-43868, CVE-2026-43869, CVE-2026-43870, CVE-2026-43871, CVE-2026-48144, CVE-2026-48145, CVE-2026-48586, CVE-2026-49158, CVE-2026-55968, CVE-2026-55969, CVE-2026-55970, CVE-2026-55971, and CVE-2026-58023.
- The patch for CVE-2026-29167 also addresses CVE-2026-29170, CVE-2026-34355, CVE-2026-34356, CVE-2026-42535, CVE-2026-42536, CVE-2026-43951, CVE-2026-44119, CVE-2026-44185, CVE-2026-44186, CVE-2026-44631, CVE-2026-48913, and CVE-2026-49975.
- The patch for CVE-2026-60075 also addresses CVE-2026-60074.
- The patch for CVE-2026-13221 also addresses CVE-2026-4176, CVE-2026-57432, and CVE-2026-8376.
- The patch for CVE-2026-55971 also addresses CVE-2026-42792, CVE-2026-47078, CVE-2026-54890, CVE-2026-55737, CVE-2026-55953, CVE-2026-58227, CVE-2026-59250, CVE-2026-59251, CVE-2026-59696, CVE-2026-66357, CVE-2026-73812, CVE-2026-74835, and CVE-2026-74994.
- The patch for CVE-2026-75596 also addresses CVE-2026-44891, CVE-2026-55831, CVE-2026-55833, CVE-2026-55851, CVE-2026-56745, CVE-2026-56746, CVE-2026-56816, CVE-2026-56817, CVE-2026-56819, CVE-2026-56820, CVE-2026-56821, CVE-2026-56822, CVE-2026-59898, CVE-2026-59899, CVE-2026-59900, CVE-2026-59901, CVE-2026-59902, CVE-2026-59903, CVE-2026-59919, CVE-2026-59920, CVE-2026-59921, CVE-2026-62380, CVE-2026-73507, CVE-2026-73508, and CVE-2026-75595.
- The patch for CVE-2026-21716 also addresses CVE-2024-36137, CVE-2026-21710, CVE-2026-21712, CVE-2026-21713, CVE-2026-21714, CVE-2026-21715, CVE-2026-21717, CVE-2026-48615, CVE-2026-48617, CVE-2026-48618, CVE-2026-48619, CVE-2026-48928, CVE-2026-48930, CVE-2026-48931, CVE-2026-48933, CVE-2026-48934, CVE-2026-48935, CVE-2026-48937, CVE-2026-56846, CVE-2026-56847, CVE-2026-56848, CVE-2026-56850, CVE-2026-58039, CVE-2026-58041, CVE-2026-58042, CVE-2026-58043, CVE-2026-58044, and CVE-2026-58045.
- The patch for CVE-2026-34487 also addresses CVE-2026-34483, CVE-2026-34486, and CVE-2026-34500.
- The patch for CVE-2026-64193 also addresses CVE-2026-64194.
- The patch for CVE-2026-54512 also addresses CVE-2026-54513, CVE-2026-54514, CVE-2026-54515, CVE-2026-54516, and CVE-2026-54518.
- The patch for CVE-2026-54874 also addresses CVE-2026-14456, CVE-2026-14457, CVE-2026-18798, CVE-2026-54876, CVE-2026-63072, CVE-2026-63073, CVE-2026-63074, CVE-2026-63075, and CVE-2026-63076.
- The patch for CVE-2026-28369 also addresses CVE-2026-28367 and CVE-2026-28368.
- The patch for CVE-2026-6653 also addresses CVE-2026-11979, CVE-2026-74860, CVE-2026-86138, CVE-2026-86140, CVE-2026-86142, CVE-2026-86143, and CVE-2026-86144.
- The patch for CVE-2026-22702 also addresses CVE-2024-53899 and CVE-2026-20060.
- The patch for CVE-2026-4800 also addresses CVE-2026-2950.
- The patch for CVE-2026-69247 also addresses CVE-2026-69248 and CVE-2026-69249.
- The patch for CVE-2026-8763 also addresses CVE-2026-13506.
- The patch for CVE-2026-59889 also addresses CVE-2026-54512, CVE-2026-54513, CVE-2026-54514, CVE-2026-54515, CVE-2026-54516, CVE-2026-54517, CVE-2026-54518, and CVE-2026-59888.
- The patch for CVE-2026-34481 also addresses CVE-2025-68161, CVE-2026-34477, CVE-2026-34478, CVE-2026-34479, and CVE-2026-34480.
- The patch for CVE-2024-38356 also addresses CVE-2024-38357.
- The patch for CVE-2026-54906 also addresses CVE-2026-54904 and CVE-2026-54905.
- The patch for CVE-2026-63388 also addresses CVE-2026-63382, CVE-2026-63385, and CVE-2026-63387.
- The patch for CVE-2026-41001 also addresses CVE-2026-40992.
- The patch for CVE-2026-41855 also addresses CVE-2026-41838, CVE-2026-41839, CVE-2026-41840, CVE-2026-41841, CVE-2026-41842, CVE-2026-41843, CVE-2026-41844, CVE-2026-41845, CVE-2026-41846, CVE-2026-41848, CVE-2026-41850, CVE-2026-41851, CVE-2026-41852, CVE-2026-41853, and CVE-2026-41854.
- The patch for CVE-2026-54399 also addresses CVE-2026-54428 and CVE-2026-64607.
- The patch for CVE-2026-32327 also addresses CVE-2022-25147, CVE-2022-28331, CVE-2023-49582, CVE-2025-49506, and CVE-2026-34502.
- The patch for CVE-2026-63639 also addresses CVE-2026-56684.
- The patch for CVE-2026-68525 also addresses CVE-2022-23181, CVE-2024-52316, CVE-2025-24813, CVE-2026-24733, CVE-2026-24880, CVE-2026-41284, CVE-2026-42498, CVE-2026-43512, CVE-2026-43513, CVE-2026-43514, CVE-2026-43515, CVE-2026-50229, CVE-2026-55276, CVE-2026-55955, CVE-2026-55956, CVE-2026-55957, CVE-2026-59083, CVE-2026-65182, CVE-2026-65905, and CVE-2026-68569.
- The patch for CVE-2026-7168 also addresses CVE-2022-43552, CVE-2023-23916, CVE-2023-27535, CVE-2023-27536, CVE-2023-28321, CVE-2023-28322, CVE-2023-38546, CVE-2023-46218, CVE-2024-2398, and CVE-2026-8286.
- The patch for CVE-2026-56740 also addresses CVE-2026-56741.
- The patch for CVE-2026-5704 also addresses CVE-2026-18477 and CVE-2026-18508.
- The patch for CVE-2026-41989 also addresses CVE-2026-41990.
- The patch for CVE-2026-10050 also addresses CVE-2022-2047, CVE-2022-2048, CVE-2023-26048, CVE-2023-26049, CVE-2023-44487, CVE-2024-6763, CVE-2026-10051, CVE-2026-6790, and CVE-2026-8384.
- The patch for CVE-2026-68494 also addresses CVE-2026-89407 and CVE-2026-89425.
- The patch for CVE-2026-55831 also addresses CVE-2026-55833, CVE-2026-56745, CVE-2026-56746, CVE-2026-56819, CVE-2026-59898, CVE-2026-59899, CVE-2026-59900, CVE-2026-59901, and CVE-2026-59921.
- The patch for CVE-2026-68497 also addresses CVE-2026-91776 and CVE-2026-91777.
- The patch for CVE-2026-5450 also addresses CVE-2026-33701, CVE-2026-42496, and CVE-2026-58016.

This Critical Patch Update contains 13 new security patches for Oracle Construction and Engineering.  7 of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cpuoct2026verbose.html#PVA)

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-41855 | Primavera Gateway | Admin (Spring Framework) | HTTP | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 21.12.0-21.12.18 |  | 
| CVE-2026-68497 | Primavera Unifier | Platform (jackson-databind) | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 21.12.0-21.12.17, 22.12.0-22.12.15, 23.12.0-23.12.16, 24.12.0-24.12.16, 25.12.0-25.12.9 |  | 
| CVE-2026-75140 | Primavera Unifier | Platform (jsoup) | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 21.12.0-21.12.17, 22.12.0-22.12.15, 23.12.0-23.12.16, 24.12.0-24.12.16, 25.12.0-25.12.9 |  | 
| CVE-2026-101736 | Primavera Unifier | Core | HTTP | Yes | 7.4 | Network | High | None | None | Un- changed | High | High | None | 21.12.0-21.12.17 |  | 
| CVE-2026-101735 | Primavera Unifier | Project Control | HTTP | No | 7.1 | Network | Low | Low | None | Un- changed | Low | High | None | 23.12.0-23.12.16 |  | 
| CVE-2026-91376 | Primavera P6 Enterprise Project Portfolio Management | Web Access | HTTP | No | 6.5 | Network | High | Low | Required | Changed | High | Low | None | 21.12.0.0-21.12.21.9,22.12.0.0-22.12.21.4,23.12.0-23.12.20,24.12.0-24.12.16,25.12.0-25.12.8 |  | 
| CVE-2026-101475 | Primavera Unifier | Logging | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 21.12.0-21.12.17, 22.12.0-22.12.15, 23.12.0-23.12.16, 24.12.0-24.12.16, 25.12.0-25.12.9 |  | 
| CVE-2026-66144 | Primavera Unifier | Platform (Apache Neethi) | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | None | None | High | 21.12.0-21.12.17, 22.12.0-22.12.15, 23.12.0-23.12.16, 24.12.0-24.12.16, 25.12.0-25.12.9 |  | 
| CVE-2026-49844 | Primavera Unifier | Platform (Apache Log4j) | HTTP | Yes | 5.9 | Network | High | None | None | Un- changed | None | High | None | 21.12.0-21.12.17, 22.12.0-22.12.15, 23.12.0-23.12.16, 24.12.0-24.12.16, 25.12.0-25.12.9 |  | 
| CVE-2026-84501 | Primavera Unifier | Platform (Apache ZooKeeper) | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | None | Low | None | 21.12.0-21.12.17, 22.12.0-22.12.15, 23.12.0-23.12.16, 24.12.0-24.12.16, 25.12.0-25.12.9 |  | 
| CVE-2026-41855 | Primavera Unifier | Document Management (Spring Framework) | HTTP | Yes | 4.8 | Network | High | None | None | Un- changed | None | Low | Low | 22.12.0-22.12.15, 23.12.0-23.12.16, 24.12.0-24.12.16, 25.12.0-25.12.9 |  | 
| CVE-2026-91399 | Primavera P6 Enterprise Project Portfolio Management | Web Access | HTTP | No | 4.3 | Network | Low | Low | None | Un- changed | None | Low | None | 21.12.0.0-21.12.21.9,22.12.0.0-22.12.21.4,23.12.0-23.12.20,24.12.0-24.12.16,25.12.0-25.12.8 |  | 
| CVE-2026-78254 | Primavera Unifier | Platform (Apache Ant) | Multiple | No | 4.2 | Network | High | Low | None | Un- changed | Low | Low | None | 21.12.0-21.12.17, 22.12.0-22.12.15, 23.12.0-23.12.16, 24.12.0-24.12.16, 25.12.0-25.12.9 |  | 

- The patch for CVE-2026-68497 also addresses CVE-2026-19032, CVE-2026-54515, CVE-2026-59889, CVE-2026-91776, and CVE-2026-91777.
- The patch for CVE-2026-84501 also addresses CVE-2026-59739, CVE-2026-59969, CVE-2026-79993, and CVE-2026-84439.
- The patch for CVE-2026-66144 also addresses CVE-2026-66142, CVE-2026-66143, and CVE-2026-91863.
- The patch for CVE-2026-75140 also addresses CVE-2026-71497.
- The patch for CVE-2026-41855 also addresses CVE-2026-22735, CVE-2026-22737, CVE-2026-22740, CVE-2026-22741, CVE-2026-22745, CVE-2026-41838, CVE-2026-41839, CVE-2026-41840, CVE-2026-41841, CVE-2026-41842, CVE-2026-41843, CVE-2026-41844, CVE-2026-41845, CVE-2026-41846, CVE-2026-41848, CVE-2026-41850, CVE-2026-41851, CVE-2026-41852, CVE-2026-41853, CVE-2026-41854, CVE-2026-47891, CVE-2026-47892, CVE-2026-47893, CVE-2026-59280, CVE-2026-59281, CVE-2026-59282, CVE-2026-59283, CVE-2026-59313, and CVE-2026-59314.

This Critical Patch Update contains 194 new security patches for Oracle E-Business Suite.  31 of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cpuoct2026verbose.html#EBS)

Oracle E-Business Suite products include Oracle Database and Oracle Fusion Middleware components that are affected by the vulnerabilities listed in the Oracle Database and Oracle Fusion Middleware sections. The exposure of Oracle E-Business Suite products is dependent on the Oracle Database and Oracle Fusion Middleware versions being used. Oracle Database and Oracle Fusion Middleware security updates are not listed in the Oracle E-Business Suite risk matrix. However, since vulnerabilities affecting Oracle Database and Oracle Fusion Middleware versions may affect Oracle E-Business Suite products, Oracle recommends that customers apply the October 2026 Critical Patch Update to the Oracle Database and Oracle Fusion Middleware components of Oracle E-Business Suite. For information on what patches need to be applied to your environments, refer to Oracle E-Business Suite Release 12 Critical Patch Update Knowledge Document (October 2026), [My Oracle Support Note KA923](https://support.oracle.com/support/?documentId=KA923).

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-101809 | Workflow | Workflow Notification Mailer | HTTP | Yes | 10.0 | Network | Low | None | None | Changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101767 | Oracle Application Object Library | Core | HTTP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101634 | Oracle Mobile Field Service | Internal Operations | HTTP | Yes | 9.1 | Network | Low | None | None | Un- changed | High | None | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101808 | Oracle Product Workbench | WebUI | HTTP | Yes | 9.1 | Network | Low | None | None | Un- changed | High | High | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101742 | Oracle Applications Manager | Diagnostics | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-91532 | Oracle Applications Manager | Internal Operations | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101542 | Oracle Capacity | Internal Operations | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-83363 | Oracle Contract Lifecycle Management for Public Sector | Award/PO | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101567 | Oracle Cost Management | Cost Planning | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101685 | Oracle E-Business Suite Integrated SOA Gateway | SOA Provider | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101686 | Oracle E-Business Suite Integrated SOA Gateway | SOA Provider | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101813 | Oracle Engineering | Change Management | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101692 | Oracle Mobile Field Service | Admin UI | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101635 | Oracle Mobile Field Service | Internal Operations | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101655 | Oracle Mobile Field Service | Internal Operations | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101664 | Oracle Mobile Field Service | Internal Operations | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101653 | Oracle Mobile Field Service | Internal Operations | HTTPS | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101654 | Oracle Mobile Field Service | Internal Operations | HTTPS | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101656 | Oracle Mobile Field Service | Internal Operations | HTTPS | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101852 | Oracle Product Hub | Internal Operations | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101853 | Oracle Product Hub | Internal Operations | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101854 | Oracle Product Hub | Internal Operations | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101557 | Oracle Purchasing | Internal Operations | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101842 | Strategic Network Optimization | Installation of SNO | HTTP | Yes | 8.8 | Network | Low | None | Required | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101824 | Document Management and Collaboration | Attachments | HTTP | No | 8.7 | Network | Low | Low | Required | Changed | High | High | None | 12.2.3-12.2.15 |  | 
| CVE-2026-87408 | Oracle Applications Framework | Personalization | HTTP | No | 8.7 | Network | Low | Low | Required | Changed | High | High | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101688 | Oracle E-Business Suite Integrated SOA Gateway | SOA Provider | HTTP | Yes | 8.6 | Network | Low | None | None | Changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-91347 | iSupport | Service Requests | HTTP | No | 8.5 | Network | Low | Low | None | Changed | None | High | Low | 12.2.3-12.2.15 |  | 
| CVE-2026-101534 | Oracle EDI Gateway | EDI | HTTP | No | 8.5 | Network | Low | Low | None | Changed | High | Low | None | 12.2.3-12.2.15 |  | 
| CVE-2026-83393 | Oracle Product Hub | Internal Operations | HTTP | No | 8.5 | Network | High | Low | None | Changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101648 | Oracle Partner Management | Internal Operations | HTTP | No | 8.4 | Network | High | Low | None | Changed | High | High | Low | 12.2.3-12.2.15 |  | 
| CVE-2026-101684 | Oracle E-Business Suite Integrated SOA Gateway | Internal Operations | HTTP | No | 8.3 | Network | Low | Low | None | Un- changed | High | High | Low | 12.2.3-12.2.15 |  | 
| CVE-2026-101841 | Global Order Promising | Web Service | HTTP | No | 8.2 | Network | High | Low | None | Changed | High | High | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101704 | Oracle Concurrent Processing | Other | None | No | 8.2 | Local | Low | High | None | Changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101690 | Oracle E-Business Suite Integrated SOA Gateway | SOA Provider | HTTP | Yes | 8.2 | Network | Low | None | None | Un- changed | High | Low | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101640 | Oracle Marketing | Audience | HTTP | Yes | 8.2 | Network | Low | None | None | Un- changed | High | Low | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101700 | Oracle Application Object Library | Core | HTTP | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101672 | Oracle Call Center Technology | Internal Operations | RMI | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-83361 | Oracle Contract Lifecycle Management for Public Sector | Award/PO | HTTP | No | 8.1 | Network | Low | Low | None | Un- changed | High | High | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101665 | Oracle Mobile Field Service | Admin UI | HTTP | No | 8.1 | Network | Low | Low | None | Un- changed | High | High | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101831 | Oracle Quality | Internal Operations | HTTP | No | 8.1 | Network | Low | Low | None | Un- changed | High | High | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101834 | Oracle Shipping Execution | Workflow Events | HTTP | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-91506 | Workflow | Workflow Notification Mailer | HTTP | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101682 | Applications DBA | AD Utilities | None | No | 7.8 | Local | Low | None | Required | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-87356 | Applications Platform Engineering | Valid Session | None | No | 7.8 | Local | Low | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101566 | Oracle Application Object Library | DB Privileges | None | No | 7.8 | Local | Low | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101757 | Oracle Application Object Library | DB Privileges | None | No | 7.8 | Local | Low | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101676 | Oracle Concurrent Processing | Other Issues | None | No | 7.8 | Local | Low | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101540 | Oracle Capacity | Internal Operations | HTTP | No | 7.7 | Network | Low | Low | None | Changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101541 | Oracle Capacity | Internal Operations | HTTP | No | 7.7 | Network | Low | Low | None | Changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101705 | Oracle Common Applications | Role Summary | HTTP | No | 7.7 | Network | High | High | None | Changed | High | High | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101689 | Oracle E-Business Suite Integrated SOA Gateway | SOA Provider | HTTP | No | 7.7 | Network | Low | Low | None | Changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101818 | Oracle Product Hub | Item Catalog | HTTP | No | 7.7 | Network | High | Low | None | Changed | High | Low | Low | 12.2.3-12.2.15 |  | 
| CVE-2026-101830 | Oracle Project Contracts | Internal Operations | HTTP | No | 7.7 | Network | Low | Low | None | Changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101837 | Oracle Shipping Execution | Workflow Events | HTTP | No | 7.7 | Network | High | Low | None | Changed | Low | Low | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101815 | Assets | Internal Operations | HTTP | No | 7.6 | Network | Low | Low | None | Un- changed | Low | Low | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101849 | Installed Base | Create Item Instance | HTTP | No | 7.6 | Network | Low | Low | Required | Changed | High | Low | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101387 | Oracle Capacity | Internal Operations | HTTP | No | 7.6 | Network | Low | Low | None | Un- changed | High | Low | Low | 12.2.3-12.2.15 |  | 
| CVE-2026-101398 | Oracle Capacity | Internal Operations | HTTP | No | 7.6 | Network | Low | Low | None | Un- changed | High | Low | Low | 12.2.3-12.2.15 |  | 
| CVE-2026-101641 | Oracle Report Manager | Internal Operations | HTTPS | No | 7.6 | Network | Low | Low | None | Un- changed | High | Low | Low | 12.2.3-12.2.15 |  | 
| CVE-2026-101833 | Oracle Shipping Execution | Internal Operations | HTTP | No | 7.6 | Network | Low | Low | None | Un- changed | High | Low | Low | 12.2.3-12.2.15 |  | 
| CVE-2026-91321 | iProcurement | Requisition Management | HTTP | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101552 | Oracle Application Object Library | Flexfields | HTTP | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101551 | Oracle Applications Manager | Oracle Diagnostics Interfaces | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101823 | Oracle Bills of Material | Internal Operations | HTTP | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101847 | Oracle Bills of Material | Internal Operations | HTTP | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101543 | Oracle Capacity | Internal Operations | HTTP | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101536 | Oracle Cost Management | Cost Maintenance | HTTP | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101687 | Oracle E-Business Suite Integrated SOA Gateway | SOA Provider | HTTP | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101820 | Oracle General Ledger | ADADMIN | HTTP | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101825 | Oracle HCM Common Architecture | Internal Operations | HTTP | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101826 | Oracle HCM Common Architecture | Internal Operations | HTTP | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101645 | Oracle iSetup | General Ledger Update Transform, Reports | HTTP | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101647 | Oracle iSetup | General Ledger Update Transform, Reports | HTTP | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101546 | Oracle Materials Requirement Planning | Internal Operations | HTTP | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101660 | Oracle Mobile Field Service | Admin UI | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101699 | Oracle One-to-One Fulfillment | Documents | HTTP | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101698 | Oracle One-to-One Fulfillment | Java Server Issues | HTTP | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101708 | Oracle Payroll | Internal Operations | HTTP | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101554 | Oracle Payroll | Internal Operations | HTTP | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-87363 | Oracle Payroll | Internal Operations | HTTP | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101555 | Oracle Payroll | Internal Operations | HTTP | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101556 | Oracle Payroll | Internal Operations | HTTP | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101712 | Oracle Payroll | Internal Operations | HTTP | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101535 | Oracle Sales Foundation | Security API | HTTP | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101835 | Oracle Shipping Execution | Workflow Events | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101703 | Pasta | Internal Operations | HTTP | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-87404 | Pasta | Printing Engine | HTTP | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-83370 | Sourcing | Auctions | HTTP | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-91496 | Workflow | Workflow Notification Mailer | HTTP | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-91337 | iProcurement | Internal operations | HTTPS | Yes | 7.4 | Network | High | None | None | Un- changed | High | High | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101707 | Oracle Concurrent Processing | Other Issues | HTTP | Yes | 7.4 | Network | High | None | None | Un- changed | High | High | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101829 | Oracle Mobile Application Server | MWA Terminal Server | HTTP | Yes | 7.4 | Network | High | None | None | Un- changed | High | High | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101636 | Oracle Mobile Field Service | Admin UI | HTTP | Yes | 7.4 | Network | High | None | None | Un- changed | High | High | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101658 | Oracle Mobile Field Service | Admin UI | HTTP | Yes | 7.4 | Network | High | None | None | Un- changed | High | High | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101661 | Oracle Mobile Field Service | Admin UI | HTTP | Yes | 7.4 | Network | High | None | None | Un- changed | High | High | None | 12.2.3-12.2.15 |  | 
| CVE-2026-83366 | Oracle Shipping Execution | Workflow Events | HTTP | Yes | 7.4 | Network | High | None | None | Un- changed | High | High | None | 12.2.3-12.2.15 |  | 
| CVE-2026-83367 | Oracle Shipping Execution | Workflow Events | Oracle Net | Yes | 7.4 | Network | High | None | None | Un- changed | High | High | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101638 | Applications DBA | AD Utilities | None | No | 7.3 | Local | Low | Low | Required | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-87402 | Applications DBA | AD Utilities | None | No | 7.3 | Local | Low | Low | Required | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-91260 | iProcurement | E-Content Manager Catalog | HTTP | No | 7.2 | Network | Low | High | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-91316 | iProcurement | E-Content Manager Catalog | HTTPS | No | 7.2 | Network | Low | High | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101822 | Oracle Bills of Material | Internal Operations | HTTP | No | 7.2 | Network | High | High | None | Changed | Low | High | Low | 12.2.3-12.2.15 |  | 
| CVE-2026-101840 | Oracle Contract Lifecycle Management for Public Sector | Award/PO | HTTP | No | 7.2 | Network | Low | High | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101466 | Oracle EDI Gateway | All Miscellaneous EDI Issues | HTTP | No | 7.2 | Network | Low | High | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101519 | Oracle EDI Gateway | All Miscellaneous EDI Issues | HTTP | No | 7.2 | Network | Low | High | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101532 | Oracle EDI Gateway | All Miscellaneous EDI Issues | HTTP | No | 7.2 | Network | Low | High | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101646 | Oracle iSetup | General Ledger Update Transform, Reports | HTTP | No | 7.2 | Network | Low | High | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101694 | Oracle Mobile Field Service | Admin UI | HTTPS | No | 7.2 | Network | Low | High | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101816 | Oracle Product Hub | Internal Operations | HTTP | No | 7.2 | Network | Low | High | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-87357 | Order Capture | Internal Operations | HTTP | No | 7.2 | Network | Low | High | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-87403 | Applications DBA | AD Utilities | None | No | 7.1 | Local | Low | Low | None | Un- changed | High | High | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101851 | Installed Base | Data Provider UI | HTTP | No | 7.1 | Network | Low | Low | None | Un- changed | High | Low | None | 12.2.3-12.2.15 |  | 
| CVE-2026-91338 | iSupport | Internal operations | HTTP | No | 7.1 | Network | Low | Low | None | Un- changed | Low | High | None | 12.2.3-12.2.15 |  | 
| CVE-2026-87358 | Oracle General Ledger | Internal Operations | HTTP | No | 7.1 | Network | High | Low | None | Un- changed | Low | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101827 | Oracle HCM Common Architecture | Internal Operations | HTTP | No | 7.1 | Network | High | Low | None | Un- changed | High | High | Low | 12.2.3-12.2.15 |  | 
| CVE-2026-101662 | Oracle Mobile Field Service | Admin UI | HTTP | No | 7.1 | Network | Low | Low | None | Un- changed | Low | High | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101650 | Oracle Partner Management | Internal Operations | HTTP | No | 7.1 | Network | Low | Low | None | Un- changed | None | High | Low | 12.2.3-12.2.15 |  | 
| CVE-2026-101649 | Oracle Partner Management | Internal Operations | HTTPS | No | 7.1 | Network | Low | Low | None | Un- changed | None | High | Low | 12.2.3-12.2.15 |  | 
| CVE-2026-91511 | Oracle Purchasing | Internal Operations | HTTP | No | 7.1 | Network | High | Low | None | Changed | High | Low | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101642 | Oracle Report Manager | Internal Operations | HTTPS | No | 7.1 | Network | Low | Low | None | Un- changed | High | None | Low | 12.2.3-12.2.15 |  | 
| CVE-2026-101643 | Oracle Sales Online | Internal Operations | HTTP | No | 7.1 | Network | Low | Low | None | Un- changed | Low | High | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101681 | Applications DBA | AD Utilities | None | No | 7.0 | Local | High | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101683 | Applications DBA | AD Utilities | None | No | 7.0 | Local | High | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101545 | Oracle Inventory Management | Internal Operations | None | No | 7.0 | Local | High | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101544 | Oracle Payroll | Internal Operations | None | No | 7.0 | Local | High | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101696 | Oracle Application Object Library | Core | HTTP | Yes | 6.8 | Network | High | None | Required | Un- changed | High | High | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101812 | Oracle Complex Maintenance, Repair and Overhaul | LOV | HTTP | No | 6.8 | Network | High | Low | None | Un- changed | High | High | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101695 | Oracle One-to-One Fulfillment | Documents | HTTP | No | 6.8 | Network | High | Low | None | Un- changed | None | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101710 | Oracle Payroll | Internal Operations | HTTP | No | 6.8 | Network | High | Low | None | Un- changed | High | High | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101669 | Oracle Public Sector Human Resources | Regression Testing | HTTP | No | 6.8 | Network | High | Low | None | Un- changed | High | High | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101674 | Oracle Mobile Field Service | Internal Operations | None | No | 6.7 | Local | Low | High | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101675 | Oracle Mobile Field Service | Internal Operations | None | No | 6.7 | Local | Low | High | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101533 | Oracle EDI Gateway | All Miscellaneous EDI Issues | HTTP | No | 6.6 | Network | High | High | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101644 | Oracle Mobile Field Service | Internal Operations | HTTP | No | 6.6 | Network | High | High | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101711 | Oracle Payroll | Payroll | HTTP | No | 6.6 | Network | High | High | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-87335 | Applications DBA | Internal Operations | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101836 | iSupplier Portal | Internal Operations | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-91257 | iSupport | Service Requests | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-91339 | iSupport | Service Requests | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-87407 | Oracle Applications Framework | Security | HTTP | Yes | 6.5 | Network | Low | None | Required | Un- changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101782 | Oracle Applications Manager | Oracle Diagnostics Interfaces | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101670 | Oracle Email Center | Message Component | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101819 | Oracle General Ledger | Internal Operations | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-83359 | Oracle HRMS (India) | Indian Payroll | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-87295 | Oracle HRMS (India) | Indian Payroll | None | No | 6.5 | Local | Low | Low | None | Changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-83358 | Oracle HRMS (Norway) | Internal Operations | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-83360 | Oracle HRMS (Republic of Korea) | Korean Payroll | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-83383 | Oracle HRMS (US) | Internal Operations | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-83384 | Oracle HRMS (US) | Internal Operations | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-83385 | Oracle HRMS (US) | Internal Operations | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-83386 | Oracle HRMS (US) | Internal Operations | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101828 | Oracle Mobile Application Server | MWA Terminal Server | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101706 | Oracle One-to-One Fulfillment | Documents | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101538 | Oracle Order Management | Product Diagnostic Tools | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101832 | Oracle Order Management | Product Diagnostic Tools | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101856 | Oracle Order Management | Product Diagnostic Tools | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101857 | Oracle Order Management | Product Diagnostic Tools | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-83139 | Oracle Order Management | Product Diagnostic Tools | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101651 | Oracle Partner Management | Internal Operations | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101553 | Oracle Payroll | Element Types, Links, Entries | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | None | High | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101539 | Oracle Payroll | Internal Operations | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101855 | Oracle Product Hub | Internal Operations | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101559 | Oracle Purchasing | PO View Document | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101673 | Oracle US Federal Human Resources | Internal Operations | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101850 | Installed Base | HTML UI | HTTP | Yes | 6.1 | Network | Low | None | Required | Changed | Low | Low | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101668 | Oracle Customer Care | Internal Operations | HTTP | Yes | 6.1 | Network | Low | None | Required | Changed | Low | Low | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101671 | Oracle Email Center | Message Component | HTTP | Yes | 6.1 | Network | Low | None | Required | Changed | Low | Low | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101697 | Oracle One-to-One Fulfillment | Admin Console UI | HTTP | Yes | 6.1 | Network | Low | None | Required | Changed | Low | Low | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101558 | Oracle Purchasing | Approvals | HTTP | Yes | 6.1 | Network | Low | None | Required | Changed | Low | Low | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101701 | Oracle Concurrent Processing | Request Submission and Scheduling | None | No | 6.0 | Local | Low | High | None | Changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-60746 | Oracle Order Management | Product Diagnostic Tools | HTTP | No | 5.9 | Network | High | Low | None | Un- changed | High | Low | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101630 | Oracle Advanced Outbound Telephony | Internal Operations | HTTP | No | 5.4 | Network | Low | Low | Required | Changed | Low | Low | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101821 | Oracle Compensation Workbench | Total Compensation Statement | HTTP | No | 5.4 | Network | Low | Low | Required | Changed | Low | Low | None | 12.2.3-12.2.15 |  | 
| CVE-2026-83371 | Oracle HRMS (UK) | Internal Operations | HTTP | No | 5.4 | Network | Low | Low | Required | Changed | Low | Low | None | 12.2.3-12.2.15 |  | 
| CVE-2026-83389 | Oracle HRMS (UK) | Internal Operations | HTTP | No | 5.4 | Network | Low | Low | Required | Changed | Low | Low | None | 12.2.3-12.2.15 |  | 
| CVE-2026-83377 | Oracle HRMS (US) | Mobile Applications | HTTP | No | 5.4 | Network | Low | Low | Required | Changed | Low | Low | None | 12.2.3-12.2.15 |  | 
| CVE-2026-83391 | Oracle HRMS (US) | US Payroll Year End | HTTP | No | 5.4 | Network | Low | Low | Required | Changed | Low | Low | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101639 | Oracle Marketing | Audience | HTTP | No | 5.4 | Network | Low | Low | Required | Changed | Low | Low | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101709 | Oracle Payroll | Internal Operations | HTTP | No | 5.4 | Network | Low | Low | Required | Changed | Low | Low | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101666 | Oracle Trade Management | Claim LOV | HTTP | No | 5.4 | Network | Low | Low | Required | Changed | Low | Low | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101667 | Oracle Trade Management | Claim LOV | HTTP | No | 5.4 | Network | Low | Low | Required | Changed | Low | Low | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101814 | Oracle Engineering | Change Management | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | Low | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-91357 | Oracle Order Management | Transaction Entry | HTTP | No | 5.3 | Network | High | Low | None | Un- changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-87366 | Oracle Applications Framework | Web Utilities | HTTP | No | 4.9 | Network | Low | High | None | Un- changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101843 | Production Scheduling | Internal Operations | None | No | 4.5 | Local | High | Low | None | Un- changed | Low | Low | Low | 12.2.3-12.2.15 |  | 
| CVE-2026-83382 | Oracle Report Manager | Internal Operations | HTTPS | No | 4.3 | Network | Low | Low | None | Un- changed | Low | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-83390 | Oracle Applications Manager | Diagnostics | HTTP | No | 4.2 | Network | High | Low | None | Un- changed | Low | None | Low | 12.2.3-12.2.15 |  | 
| CVE-2026-101846 | Oracle Purchasing | Internal Operations | HTTP | No | 3.5 | Network | Low | Low | Required | Un- changed | None | Low | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101805 | Oracle Applications Manager | Diagnostics | HTTP | No | 3.3 | Network | High | High | None | Un- changed | Low | None | Low | 12.2.3-12.2.15 |  | 
| CVE-2026-83392 | Oracle Applications Manager | Diagnostics | HTTP | No | 3.1 | Network | High | Low | None | Un- changed | Low | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101844 | Oracle Concurrent Processing | Concurrent Requests | HTTP | No | 3.1 | Network | High | Low | None | Un- changed | Low | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101845 | Oracle Purchasing | Internal Operations | HTTP | No | 3.1 | Network | High | Low | None | Un- changed | None | Low | None | 12.2.3-12.2.15 |  | 
| CVE-2026-83388 | Oracle Applications Manager | Diagnostics | HTTP | No | 2.2 | Network | High | High | None | Un- changed | Low | None | None | 12.2.3-12.2.15 |  | 

This Critical Patch Update contains 12 new security patches for Oracle Enterprise Manager.  2 of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  None of these patches are applicable to client-only installations, i.e., installations that do not have Oracle Enterprise Manager installed. The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cpuoct2026verbose.html#EM)

Oracle Enterprise Manager products include Oracle Database and Oracle Fusion Middleware components that are affected by the vulnerabilities listed in the Oracle Database and Oracle Fusion Middleware sections. The exposure of Oracle Enterprise Manager products is dependent on the Oracle Database and Oracle Fusion Middleware versions being used. Oracle Database and Oracle Fusion Middleware security updates are not listed in the Oracle Enterprise Manager risk matrix. However, since vulnerabilities affecting Oracle Database and Oracle Fusion Middleware versions may affect Oracle Enterprise Manager products, Oracle recommends that customers apply the October 2026 Critical Patch Update to the Oracle Database and Oracle Fusion Middleware components of Enterprise Manager. For information on what patches need to be applied to your environments, refer to Critical Patch Update October 2026 Patch Availability Document for Oracle Products, [My Oracle Support Note CPU391](https://support.oracle.com/support/?documentId=CPU391).

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-101528 | Oracle Enterprise Manager for Oracle Database | Data Guard Management | HTTP | No | 9.9 | Network | Low | Low | None | Changed | High | High | High | 13.5, 24.1 |  | 
| CVE-2026-101529 | Oracle Enterprise Manager for Oracle Database | Data Guard Management | HTTP | No | 9.9 | Network | Low | Low | None | Changed | High | High | High | 13.5, 24.1 |  | 
| CVE-2026-101518 | Oracle Enterprise Manager Base Platform | Agent Next Gen | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 13.5, 24.1 |  | 
| CVE-2025-48734 | Oracle Enterprise Manager Base Platform | Oracle Management Service (Apache Commons BeanUtils) | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 13.5, 24.1 |  | 
| CVE-2026-101525 | Oracle Enterprise Manager for Siebel | Configuration Management | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 13.5, 24.1 |  | 
| CVE-2026-101526 | Oracle Enterprise Manager for Siebel | Configuration Management | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 13.5, 24.1 |  | 
| CVE-2025-48734 | Oracle Enterprise Manager for Virtualization | Generic Virtualization (Apache Commons BeanUtils) | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 13.5 |  | 
| CVE-2026-54512 | Oracle Enterprise Manager Base Platform | Security Framework (jackson-databind) | HTTP | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 13.5, 24.1 |  | 
| CVE-2026-101527 | Oracle Enterprise Manager Base Platform | Enterprise Manager Install | None | No | 7.8 | Local | Low | Low | None | Un- changed | High | High | High | 13.5, 24.1 |  | 
| CVE-2026-101524 | Oracle Enterprise Manager Base Platform | Security Framework | HTTP | Yes | 5.6 | Network | High | None | None | Un- changed | Low | Low | Low | 13.5, 24.1 |  | 
| CVE-2026-101511 | Oracle Enterprise Manager Base Platform | Metadata Plugin | HTTP | No | 4.3 | Network | Low | Low | None | Un- changed | Low | None | None | 13.5, 24.1 |  | 
| CVE-2026-1225 | Oracle Enterprise Manager Base Platform | API Gateway (jackson-core) | None | No | 1.9 | Local | High | High | None | Un- changed | None | Low | None | 24.1 |  | 

- The patch for CVE-2026-54512 also addresses CVE-2026-54513, CVE-2026-54514, CVE-2026-54515, and CVE-2026-59889.

This Critical Patch Update contains 5 new security patches for Oracle Financial Services Applications.  All of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cpuoct2026verbose.html#IFLX)

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-41855 | Oracle Financial Services Analytical Applications Infrastructure | Others (Spring Framework) | HTTP | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 8.0.7.9, 8.0.8.7, 8.1.2.5, 8.1.2.6 |  | 
| CVE-2026-41855 | Oracle Financial Services Behavior Detection Platform | Third Party (Spring Framework) | HTTP | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 8.0.8.1, 8.1.2.11, 8.1.2.12 |  | 
| CVE-2026-41855 | Oracle Financial Services Trade-Based Anti Money Laundering Enterprise Edition | User Interface (Spring Framework) | HTTP | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 8.0.8.0 |  | 
| CVE-2026-68497 | Oracle Financial Services Analytical Applications Infrastructure | Infrastructure | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 8.0.7.9, 8.0.8.7, 8.1.2.5, 8.1.2.6 |  | 
| CVE-2026-49844 | Oracle Financial Services Analytical Applications Infrastructure | Platform (Apache Log4j) | HTTP | Yes | 5.9 | Network | High | None | None | Un- changed | None | High | None | 8.0.7.9, 8.0.8.7, 8.1.2.5, 8.1.2.6 |  | 

This Critical Patch Update contains 206 new security patches for Oracle Fusion Middleware.  134 of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cpuoct2026verbose.html#FMW)

To get the full list of current and previously released Critical Security Patch Update and Critical Patch Update patches for Oracle Fusion Middleware products, refer to [My Oracle Support Doc ID KA1182](https://support.oracle.com/support/?documentId=KA1182).

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-87337 | Oracle Access Manager | Authentication Engine | HTTP | Yes | 10.0 | Network | Low | None | None | Changed | High | High | None | 12.2.1.4.0, 14.1.2.1.0 |  | 
| CVE-2026-91231 | Oracle SOA Suite | Adapters | HTTP | Yes | 10.0 | Network | Low | None | None | Changed | High | High | High | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91216 | Oracle SOA Suite | Fabric Layer | T3, IIOP | Yes | 10.0 | Network | Low | None | None | Changed | High | High | High | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91221 | Oracle SOA Suite | Fabric Layer | T3, IIOP | Yes | 10.0 | Network | Low | None | None | Changed | High | High | High | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91222 | Oracle Business Process Management Suite | Human Workflow (11g+) | SOAP | No | 9.9 | Network | Low | Low | None | Changed | High | High | High | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91354 | Oracle Outside In Technology | Outside In Clean Content SDK | HTTP | No | 9.9 | Network | Low | Low | None | Changed | High | High | High | 8.5.8 |  | 
| CVE-2026-91251 | Oracle SOA Suite | Adapters | HTTP | No | 9.9 | Network | Low | Low | None | Changed | High | High | High | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91224 | Oracle SOA Suite | Fabric Layer | HTTP | No | 9.9 | Network | Low | Low | None | Changed | High | High | High | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91232 | Oracle SOA Suite | Fabric Layer | HTTP | No | 9.9 | Network | Low | Low | None | Changed | High | High | High | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91250 | Oracle SOA Suite | Adapters | Multiple | No | 9.9 | Network | Low | Low | None | Changed | High | High | High | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-87251 | Oracle Access Manager | Authentication Engine | SAML | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 12.2.1.4.0, 14.1.2.1.0 |  | 
| CVE-2026-91220 | Oracle Business Process Management Suite | Human Workflow | HTTP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-47065 | Oracle Business Process Management Suite | Human workflow 11g+ (Apache Mina) | HTTP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-83397 | Oracle Data Integrator | Console / Repository Explorer | HTTP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-83396 | Oracle Data Integrator | Console / Repository Explorer | RMI | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-4176 | Oracle Fusion Middleware | Centralized Thirdparty Jars (Perl) | HTTP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91408 | Oracle Identity Manager | End User Self Service | T3, IIOP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 12.2.1.4.0, 14.1.2.1.0 |  | 
| CVE-2026-91491 | Oracle Identity Manager Connector | LDAP Gateway | LDAP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 12.2.1.4.0, 14.1.2.1.0 |  | 
| CVE-2026-42779 | Oracle Managed File Transfer | MFT Runtime Server (Apache Mina) | HTTP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 14.1.2.0.0 |  | 
| CVE-2026-41635 | Oracle Managed File Transfer | MFT Runtime Server (Apache Mina) | HTTP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 12.2.1.4.0 |  | 
| CVE-2026-47065 | Oracle Middleware Common Libraries and Tools | Third Party (Apache Mina) | HTTP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91214 | Oracle SOA Suite | Fabric Layer | HTTP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91234 | Oracle SOA Suite | Fabric Layer | HTTP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91235 | Oracle SOA Suite | Fabric Layer | HTTP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91236 | Oracle SOA Suite | Fabric Layer | HTTP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91233 | Oracle SOA Suite | Enterprise Scheduling System | SOAP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91495 | Oracle WebCenter Content | Content Server | HTTP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-101499 | Oracle WebCenter Sites | WebCenter Sites | HTTP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91323 | Oracle WebLogic Server | Core | HTTP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0, 15.1.1.0.0 |  | 
| CVE-2026-83399 | Oracle WebLogic Server | Core | T3, IIOP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0, 15.1.1.0.0 |  | 
| CVE-2026-91243 | Oracle Business Process Management Suite | Fabric Layer | HTTP | No | 9.6 | Network | Low | Low | None | Changed | High | High | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-87347 | Oracle HTTP Server | OSSL Module | HTTP | No | 9.6 | Network | Low | Low | None | Changed | High | High | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91218 | Oracle SOA Suite | Fabric Layer | HTTP | No | 9.6 | Network | Low | Low | None | Changed | High | High | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91230 | Oracle SOA Suite | Fabric Layer | HTTP | Yes | 9.3 | Network | Low | None | None | Changed | High | Low | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-101590 | Helidon | helidon-microprofile-security | HTTP | Yes | 9.1 | Network | Low | None | None | Un- changed | High | High | None | 4.0.0-4.5.5 |  | 
| CVE-2026-8763 | Oracle Global Lifecycle Management NextGen OUI Framework | NextGen Installer (Bouncy Castle Java Library) | HTTPS | Yes | 9.1 | Network | Low | None | None | Un- changed | High | High | None | 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0, 14.1.2.1.0, 15.1.1.0.0 |  | 
| CVE-2026-91490 | Oracle Identity Manager Connector | LDAP Gateway | LDAP | Yes | 9.1 | Network | Low | None | None | Un- changed | High | High | None | 12.2.1.4.0, 14.1.2.1.0 |  | 
| CVE-2026-91341 | Oracle Outside In Technology | Outside In Clean Content SDK | HTTP | Yes | 9.1 | Network | Low | None | None | Un- changed | None | High | High | 8.5.8 |  | 
| CVE-2026-91225 | Oracle SOA Suite | Adapters | HTTP | Yes | 9.1 | Network | Low | None | None | Un- changed | None | High | High | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-87302 | Oracle WebLogic Server | Core | HTTP | Yes | 9.1 | Network | Low | None | None | Un- changed | High | High | None | 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0, 15.1.1.0.0 |  | 
| CVE-2026-91213 | Oracle Business Process Management Suite | BPM Composer | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91668 | Oracle Data Integrator | Dictionary Repository | SQL | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-83403 | Oracle Identity Manager | OIM Legacy UI | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 12.2.1.4.0, 14.1.2.1.0 |  | 
| CVE-2026-91259 | Oracle Identity Manager | OIM Legacy UI | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 12.2.1.4.0, 14.1.2.1.0 |  | 
| CVE-2026-91407 | Oracle Identity Manager | REST WebServices | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 12.2.1.4.0, 14.1.2.1.0 |  | 
| CVE-2026-83402 | Oracle Identity Manager | OIM Legacy UI | HTTPS | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 12.2.1.4.0, 14.1.2.1.0 |  | 
| CVE-2026-91340 | Oracle Outside In Technology | Outside In Clean Content SDK | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 8.5.8 |  | 
| CVE-2026-87397 | Oracle Outside In Technology | Outside In Core | HTTP | Yes | 8.8 | Network | Low | None | Required | Un- changed | High | High | High | 8.5.8 |  | 
| CVE-2026-87359 | Oracle Service Bus | Core | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-87364 | Oracle Service Bus | Core | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-87419 | Oracle Service Bus | Core | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-87420 | Oracle Service Bus | Core | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 14.1.2.0.0 |  | 
| CVE-2026-91215 | Oracle SOA Suite | Fabric Layer | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91223 | Oracle SOA Suite | Fabric Layer | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91239 | Oracle SOA Suite | Fabric Layer | Multiple | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-83426 | Oracle Access Manager | Authentication Engine | HTTP | Yes | 8.7 | Network | High | None | None | Changed | High | High | None | 12.2.1.4.0, 14.1.2.1.0 |  | 
| CVE-2026-87346 | Oracle HTTP Server | Oracle Weblogic Server Proxy Plug-in for Oracle HTTP Server | HTTP | Yes | 8.7 | Network | High | None | None | Changed | High | High | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91492 | Oracle Identity Manager Connector | SAP ERP+ | HTTP | Yes | 8.7 | Network | High | None | None | Changed | High | High | None | 12.2.1.4.0, 14.1.2.1.0 |  | 
| CVE-2026-91211 | Oracle Identity Manager Connector | Connectors and Connector Server | SOAP | No | 8.7 | Network | Low | High | None | Changed | High | High | None | 12.2.1.4.0, 14.1.2.1.0 |  | 
| CVE-2026-83379 | Oracle Weblogic Server Proxy Plug-in | WebLogic Server Proxy Plug-In for Third-Party Web Servers | HTTP | Yes | 8.7 | Network | High | None | None | Changed | High | High | None | 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0 |  | 
| CVE-2026-87300 | Oracle Weblogic Server Proxy Plug-in | WebLogic Server Proxy Plug-In for Third-Party Web Servers | HTTP | Yes | 8.7 | Network | High | None | None | Changed | High | High | None | 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0 |  | 
| CVE-2026-83407 | Oracle Access Manager | Authentication Engine | HTTP | Yes | 8.6 | Network | Low | None | None | Un- changed | High | Low | Low | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91212 | Oracle Identity Manager Connector | Generic REST | HTTP | Yes | 8.6 | Network | Low | None | None | Changed | High | None | None | 12.2.1.4.0, 14.1.2.1.0 |  | 
| CVE-2026-91343 | Oracle Outside In Technology | Outside In Clean Content SDK | HTTP | Yes | 8.6 | Network | Low | None | None | Changed | None | High | None | 8.5.8 |  | 
| CVE-2026-91353 | Oracle Outside In Technology | Outside In Clean Content SDK | HTTP | Yes | 8.6 | Network | Low | None | None | Changed | High | None | None | 8.5.8 |  | 
| CVE-2026-87304 | Oracle Outside In Technology | Outside In Core | HTTP | Yes | 8.6 | Network | Low | None | None | Changed | High | None | None | 8.5.8 |  | 
| CVE-2026-91217 | Oracle SOA Suite | Fabric Layer | HTTP | Yes | 8.6 | Network | Low | None | None | Changed | High | None | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91219 | Oracle SOA Suite | Fabric Layer | HTTP | Yes | 8.6 | Network | Low | None | None | Changed | High | None | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-12817 | Oracle WebLogic Server | Centralized Thirdparty Jars (Bouncy Castle Java Library) | HTTPS | Yes | 8.6 | Network | Low | None | None | Un- changed | Low | Low | High | 12.2.1.4.0, 14.1.1.0.0 |  | 
| CVE-2026-91355 | Oracle Outside In Technology | Outside In Clean Content SDK | None | No | 8.4 | Local | Low | None | None | Un- changed | High | High | High | 8.5.8 |  | 
| CVE-2026-91358 | Oracle Business Process Management Suite | Case management Service (11g+) | HTTP | Yes | 8.2 | Network | Low | None | None | Un- changed | High | Low | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-83398 | Oracle Data Integrator | Data Transforms | HTTP | Yes | 8.2 | Network | Low | None | None | Un- changed | High | Low | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91342 | Oracle Outside In Technology | Outside In Clean Content SDK | HTTP | Yes | 8.2 | Network | Low | None | Required | Changed | Low | High | None | 8.5.8 |  | 
| CVE-2026-91346 | Oracle Outside In Technology | Outside In Clean Content SDK | HTTP | Yes | 8.2 | Network | Low | None | Required | Changed | High | Low | None | 8.5.8 |  | 
| CVE-2026-87394 | Oracle Outside In Technology | Outside In Core | HTTP | Yes | 8.2 | Network | Low | None | None | Un- changed | High | None | Low | 8.5.8 |  | 
| CVE-2026-83409 | Oracle Access Manager | Authentication Engine | SAML | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-41855 | Oracle Identity Manager | Installer (Spring Framework) | HTTP | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 12.2.1.4.0 |  | 
| CVE-2026-54513 | Oracle Identity Manager | Third Party (jackson-databind) | HTTP | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 12.2.1.4.0, 14.1.2.1.0 |  | 
| CVE-2026-41855 | Oracle Middleware Common Libraries and Tools | Thirdparty Patch (Spring Framework) | HTTP | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-54513 | Oracle SOA Suite | Rest Converters (jackson-databind) | HTTP | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-54513 | Oracle Web Services Manager | Third Party (jackson-databind) | HTTP | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 14.1.2.0.0 |  | 
| CVE-2026-54513 | Oracle Web Services Manager | Third Party (jackson-databind) | HTTP | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 14.1.2.0.0 |  | 
| CVE-2026-41855 | Oracle WebLogic Server | Core (Spring Framework) | HTTP | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0, 15.1.1.0.0 |  | 
| CVE-2022-1471 | Oracle Data Integrator | Repository (SnakeYAML) | None | No | 7.8 | Local | Low | Low | None | Un- changed | High | High | High | 14.1.2.0.0 |  | 
| CVE-2026-91419 | Oracle HTTP Server | OSSL Module | None | No | 7.8 | Local | Low | Low | None | Un- changed | High | High | High | 12.2.1.4.0 |  | 
| CVE-2026-91473 | Oracle HTTP Server | Web Listener | None | No | 7.8 | Local | Low | Low | None | Un- changed | High | High | High | 12.2.1.4.0 |  | 
| CVE-2026-91458 | Oracle Outside In Technology | Outside In Core | None | No | 7.8 | Local | Low | None | Required | Un- changed | High | High | High | 8.5.8 |  | 
| CVE-2026-91483 | Oracle Outside In Technology | Outside In Core | None | No | 7.8 | Local | Low | None | Required | Un- changed | High | High | High | 8.5.8 |  | 
| CVE-2026-91457 | Oracle Outside In Technology | Outside In Image Export SDK | None | No | 7.8 | Local | Low | None | Required | Un- changed | High | High | High | 8.5.8 |  | 
| CVE-2026-91459 | Oracle Outside In Technology | Outside In Image Export SDK | None | No | 7.8 | Local | Low | None | Required | Un- changed | High | High | High | 8.5.8 |  | 
| CVE-2026-91460 | Oracle Outside In Technology | Outside In Image Export SDK | None | No | 7.8 | Local | Low | None | Required | Un- changed | High | High | High | 8.5.8 |  | 
| CVE-2026-101572 | Helidon | helidon-webclient-http2 | HTTP/2 | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 4.0.0-4.5.5,27.0.0 |  | 
| CVE-2026-87296 | Oracle Access Manager | Authentication Engine | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | High | None | None | 12.2.1.4.0, 14.1.2.1.0 |  | 
| CVE-2026-54399 | Oracle Access Manager | Authentication Engine (Apache HttpComponents) | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 14.1.2.1.0 |  | 
| CVE-2026-54399 | Oracle Access Manager | Third Party (Apache HttpComponents) | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 14.1.2.1.0 |  | 
| CVE-2026-54428 | Oracle Business Process Management Suite | Composer (Apache HttpComponents) | HTTP/2 | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-56741 | Oracle Coherence | Centralized Thirdparty Jars (jline) | TCP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 12.2.1.4.0, 14.1.1.0.0 |  | 
| CVE-2026-101520 | Oracle Global Lifecycle Management NextGen OUI Framework | NextGen Installer | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0, 14.1.2.1.0, 15.1.1.0.0 |  | 
| CVE-2026-91776 | Oracle Global Lifecycle Management NextGen OUI Framework | NextGen Installer (jackson-databind) | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0, 14.1.2.1.0, 15.1.1.0.0 |  | 
| CVE-2026-91493 | Oracle Identity Manager Connector | LDAP Gateway | LDAP | Yes | 7.5 | Network | Low | None | None | Un- changed | High | None | None | 12.2.1.4.0, 14.1.2.1.0 |  | 
| CVE-2026-54399 | Oracle Middleware Common Libraries and Tools | Third Party (Apache HttpComponents) | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 14.1.2.0.0 |  | 
| CVE-2026-59649 | Oracle Middleware Common Libraries and Tools | Third Party (Bouncy Castle Java Library) | HTTPS | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 14.1.2.0.0 |  | 
| CVE-2026-91344 | Oracle Outside In Technology | Outside In Clean Content SDK | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 8.5.8 |  | 
| CVE-2026-91345 | Oracle Outside In Technology | Outside In Clean Content SDK | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 8.5.8 |  | 
| CVE-2026-91349 | Oracle Outside In Technology | Outside In Clean Content SDK | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 8.5.8 |  | 
| CVE-2026-91350 | Oracle Outside In Technology | Outside In Clean Content SDK | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 8.5.8 |  | 
| CVE-2026-87395 | Oracle Outside In Technology | Outside In Core | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 8.5.8 |  | 
| CVE-2026-87398 | Oracle Outside In Technology | Outside In Core | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 8.5.8 |  | 
| CVE-2026-91405 | Oracle Outside In Technology | Outside In PDF Export SDK | HTTP | Yes | 7.5 | Network | High | None | Required | Un- changed | High | High | High | 8.5.8 |  | 
| CVE-2026-91406 | Oracle Outside In Technology | Outside In PDF Export SDK | HTTP | Yes | 7.5 | Network | High | None | Required | Un- changed | High | High | High | 8.5.8 |  | 
| CVE-2026-87369 | Oracle Service Bus | Core | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91226 | Oracle SOA Suite | Fabric Layer | HTTP | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91227 | Oracle SOA Suite | Fabric Layer | HTTP | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91229 | Oracle SOA Suite | Fabric Layer | HTTP | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91237 | Oracle SOA Suite | Fabric Layer | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | High | None | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-5598 | Oracle SOA Suite | Rest Converters (Bouncy Castle Java Library) | HTTPS | Yes | 7.5 | Network | Low | None | None | Un- changed | High | None | None | 12.2.1.4.0 |  | 
| CVE-2026-91504 | Oracle WebCenter Content | Content Portal Suite | HTTP | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91542 | Oracle WebCenter Sites | WebCenter Sites | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | High | None | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91552 | Oracle WebCenter Sites | WebCenter Sites | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | High | None | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-9563 | Oracle WebLogic Server | Centralized Thirdparty Jars (Eclipse Parsson) | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 15.1.1.0.0 |  | 
| CVE-2023-43622 | Oracle WebLogic Server | Core (Apache HTTP Server) | HTTP/2 | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 14.1.1.0.0, 14.1.2.0.0, 15.1.1.0.0 |  | 
| CVE-2025-7962 | Oracle WebLogic Server | Centralized Thirdparty Jars (Jakarta Mail) | SMTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | High | None | 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0 |  | 
| CVE-2026-91494 | Oracle Identity Manager Connector | LDAP Gateway | TCP | Yes | 7.4 | Network | High | None | None | Un- changed | High | High | None | 12.2.1.4.0, 14.1.2.1.0 |  | 
| CVE-2026-91502 | Oracle WebLogic Server | Core | TLS | Yes | 7.3 | Network | Low | None | None | Un- changed | Low | Low | Low | 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0, 15.1.1.0.0 |  | 
| CVE-2026-101585 | Helidon | helidon-cors | HTTP | Yes | 7.2 | Network | Low | None | None | Changed | Low | Low | None | 3.0.0-3.2.21 |  | 
| CVE-2026-101579 | Helidon | helidon-grpc-server | HTTP/2 | Yes | 7.2 | Network | Low | None | None | Changed | Low | Low | None | 3.0.0-3.2.21 |  | 
| CVE-2026-42404 | Oracle SOA Suite | Centralized Thirdparty Jars (Apache Neethi) | Multiple | Yes | 7.2 | Network | Low | None | None | Changed | Low | Low | None | 12.2.1.4.0 |  | 
| CVE-2026-91488 | Oracle Identity Manager Connector | Generic REST | None | No | 7.1 | Local | Low | Low | None | Un- changed | High | High | None | 12.2.1.4.0, 14.1.2.1.0 |  | 
| CVE-2026-91489 | Oracle Identity Manager Connector | LDAP Gateway | None | No | 7.1 | Local | Low | Low | None | Un- changed | High | High | None | 12.2.1.4.0, 14.1.2.1.0 |  | 
| CVE-2026-91228 | Oracle SOA Suite | Fabric Layer | HTTP | No | 7.1 | Network | Low | Low | None | Un- changed | High | Low | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91238 | Oracle SOA Suite | Fabric Layer | HTTP | No | 7.1 | Network | Low | Low | None | Un- changed | None | High | Low | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-101583 | Helidon | helidon-common-mapper | HTTP | Yes | 7.0 | Network | High | None | None | Un- changed | Low | High | Low | 4.0.0-4.5.5,27.0.0 |  | 
| CVE-2026-101574 | Helidon | OIDC | HTTP | Yes | 6.9 | Network | High | None | Required | Changed | High | Low | None | 4.0.0-4.5.5,27.0.0 |  | 
| CVE-2026-87400 | Oracle WebCenter Content | Content Server | HTTP | Yes | 6.9 | Network | High | None | Required | Changed | High | Low | None | 14.1.2.0.0 |  | 
| CVE-2026-101573 | Helidon | helidon-security-providers-http-auth | HTTP | Yes | 6.8 | Network | High | None | None | Changed | High | None | None | 3.0.0-3.2.21,4.0.0-4.5.5,27.0.0 |  | 
| CVE-2026-87374 | Oracle WebCenter Content | Content Server | HTTP | No | 6.8 | Network | High | Low | None | Un- changed | High | High | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-87371 | Oracle WebCenter Content | Content Server | TCP/IP | Yes | 6.8 | Adjacent Network | High | None | None | Un- changed | High | High | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-87376 | WebCenter Content: Imaging | Core | HTTP | No | 6.8 | Network | High | Low | None | Un- changed | High | High | None | 14.1.2.0.0 |  | 
| CVE-2026-87377 | WebCenter Content: Imaging | Core | SOAP | No | 6.8 | Network | High | Low | None | Un- changed | High | High | None | 14.1.2.0.0 |  | 
| CVE-2026-91467 | Oracle Fusion Middleware Control | Framework | None | No | 6.6 | Physical | Low | None | Required | Un- changed | High | High | High | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91475 | Oracle Outside In Technology | Outside In Clean Content SDK | None | No | 6.6 | Local | Low | Low | None | Un- changed | Low | High | Low | 8.5.8 |  | 
| CVE-2026-101581 | Helidon | helidon-webclient-dns-resolver-round-robin | DNS | Yes | 6.5 | Network | Low | None | None | Un- changed | None | Low | Low | 4.0.0-4.5.5,27.0.0 |  | 
| CVE-2026-101575 | Helidon | LRA | HTTP | Yes | 6.5 | Network | High | None | None | Changed | Low | Low | Low | 4.0.0-4.5.5 |  | 
| CVE-2026-101569 | Helidon | helidon-common-concurrency-limits | HTTP | Yes | 6.5 | Network | Low | None | None | Un- changed | None | Low | Low | 4.0.0-4.5.5,27.0.0 |  | 
| CVE-2026-101584 | Helidon | helidon-webclient-websocket | HTTP | Yes | 6.5 | Network | Low | None | None | Un- changed | Low | None | Low | 4.0.0-4.5.5,27.0.0 |  | 
| CVE-2026-59889 | Oracle Global Lifecycle Management NextGen OUI Framework | NextGen Installer (jackson-databind) | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | None | High | None | 15.1.1.0.0 |  | 
| CVE-2026-59889 | Oracle Global Lifecycle Management NextGen OUI Framework | NextGen Installer (jackson-databind) | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | None | High | None | 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0, 14.1.2.1.0 |  | 
| CVE-2026-91318 | Oracle JDeveloper | Security Framework | HTTP | Yes | 6.5 | Network | Low | None | Required | Un- changed | High | None | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-87393 | Oracle Outside In Technology | Outside In Core | HTTP | Yes | 6.5 | Network | Low | None | Required | Un- changed | None | None | High | 8.5.8 |  | 
| CVE-2026-87396 | Oracle Outside In Technology | Outside In Core | HTTP | Yes | 6.5 | Network | Low | None | Required | Un- changed | High | None | None | 8.5.8 |  | 
| CVE-2024-41311 | Oracle Outside In Technology | Outside In Search Export SDK (libheif) | HTTP | Yes | 6.5 | Network | Low | None | Required | Un- changed | None | None | High | 8.5.8 |  | 
| CVE-2026-87298 | Oracle WebCenter Content | Content Server | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-87365 | Oracle WebCenter Content | Content Server | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | None | None | High | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-87370 | Oracle WebCenter Content | Content Server | HTTP | No | 6.5 | Network | High | Low | Required | Changed | High | Low | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-87373 | Oracle WebCenter Content | Content Server | HTTP | Yes | 6.5 | Network | High | None | None | Un- changed | High | Low | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91210 | Oracle WebCenter Content | Content Server | HTTP | No | 6.5 | Network | High | Low | Required | Changed | High | Low | None | 14.1.2.0.0 |  | 
| CVE-2026-87372 | Oracle WebCenter Content | Content Server | None | No | 6.5 | Local | Low | Low | None | Changed | High | None | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91245 | Oracle WebCenter Portal | Runtime Tools | HTTP | Yes | 6.5 | Network | Low | None | Required | Un- changed | High | None | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-87375 | WebCenter Content: Imaging | Core | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-87378 | WebCenter Content: Imaging | Core | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-87392 | WebCenter Content: Imaging | Core | SOAP | No | 6.5 | Network | Low | Low | None | Un- changed | None | High | None | 14.1.2.0.0 |  | 
| CVE-2026-87399 | Oracle WebCenter Content | Content Server | HTTP | No | 6.3 | Network | Low | Low | Required | Un- changed | Low | High | None | 14.1.2.0.0 |  | 
| CVE-2026-83401 | Oracle Identity Manager | OIM Legacy UI | HTTP | Yes | 6.1 | Network | Low | None | Required | Changed | Low | Low | None | 12.2.1.4.0, 14.1.2.1.0 |  | 
| CVE-2026-91351 | Oracle Outside In Technology | Outside In Clean Content SDK | None | No | 6.1 | Local | Low | Low | None | Un- changed | None | High | Low | 8.5.8 |  | 
| CVE-2026-87299 | Oracle WebCenter Content | Content Server | HTTP | Yes | 6.1 | Network | Low | None | Required | Changed | Low | Low | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91246 | Oracle WebCenter Portal | Runtime Tools | HTTP | Yes | 6.1 | Network | Low | None | Required | Changed | Low | Low | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91319 | Oracle JDeveloper | Java Business Objects | HTTP | Yes | 5.9 | Network | High | None | None | Un- changed | None | High | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91317 | Oracle JDeveloper | ADF Databinding | SOAP | No | 5.9 | Network | High | Low | None | Un- changed | High | None | Low | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-49844 | Oracle Middleware Common Libraries and Tools | Third Party (Apache Log4j) | HTTP | Yes | 5.9 | Network | High | None | None | Un- changed | None | High | None | 14.1.2.0.0 |  | 
| CVE-2026-49844 | Oracle Middleware Common Libraries and Tools | Third Party (Apache Log4j) | HTTP | Yes | 5.9 | Network | High | None | None | Un- changed | None | High | None | 12.2.1.4.0 |  | 
| CVE-2026-91247 | Oracle WebCenter Portal | Runtime Tools | HTTP | Yes | 5.9 | Network | High | None | Required | Un- changed | None | High | Low | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91240 | Oracle WebCenter Sites | WebCenter Sites | HTTP | Yes | 5.9 | Network | High | None | None | Un- changed | High | None | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-34477 | Oracle WebCenter Sites | WebCenter Sites (Apache Log4j) | Multiple | Yes | 5.9 | Network | High | None | None | Un- changed | None | High | None | 12.2.1.4.0 |  | 
| CVE-2026-101515 | Oracle WebLogic Server | Centralized Thirdparty Jars | HTTP | Yes | 5.9 | Network | High | None | None | Un- changed | High | None | None | 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0, 15.1.1.0.0 |  | 
| CVE-2026-49844 | Oracle WebLogic Server | Centralized Thirdparty Jars (Apache Log4j) | HTTP | Yes | 5.9 | Network | High | None | None | Un- changed | None | High | None | 12.2.1.4.0 |  | 
| CVE-2026-101582 | Helidon | helidon-integrations-vault | HTTP | Yes | 5.8 | Network | Low | None | None | Changed | Low | None | None | 4.0.0-4.5.5 |  | 
| CVE-2026-101580 | Helidon | helidon-security-providers-jwt | HTTP | Yes | 5.8 | Network | Low | None | None | Changed | Low | None | None | 4.0.0-4.5.5,27.0.0 |  | 
| CVE-2026-91320 | Oracle JDeveloper | Oracle JDeveloper | None | No | 5.7 | Local | High | High | None | Un- changed | None | High | High | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-101571 | Helidon | helidon-security-providers-idcs-mapper | None | No | 5.6 | Local | High | Low | None | Changed | High | None | None | 3.0.0-3.2.21,4.0.0-4.5.5 |  | 
| CVE-2026-91501 | Oracle Identity Manager | Installer | None | No | 5.5 | Local | Low | Low | None | Un- changed | High | None | None | 12.2.1.4.0, 14.1.2.1.0 |  | 
| CVE-2026-87334 | Oracle JDeveloper | ADF Faces | None | No | 5.5 | Local | Low | Low | None | Un- changed | High | None | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91617 | Oracle Middleware Common Libraries and Tools | Remote Diagnostic Agent | None | No | 5.5 | Local | Low | Low | None | Un- changed | High | None | None | 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0, 15.1.1.0.0 |  | 
| CVE-2026-87391 | WebCenter Content: Imaging | Core | None | No | 5.5 | Local | Low | High | Required | Changed | High | None | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-87390 | Oracle WebCenter Content | Content Server | HTTP | Yes | 5.4 | Network | Low | None | Required | Un- changed | None | Low | Low | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91262 | Oracle WebCenter Content | Content Server | HTTP | Yes | 5.4 | Network | Low | None | Required | Un- changed | Low | Low | None | 14.1.2.0.0 |  | 
| CVE-2026-101588 | Helidon | WebSocket | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | Low | None | None | 4.0.0-4.5.5,27.0.0 |  | 
| CVE-2026-101568 | Helidon | helidon-health | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | Low | None | None | 3.0.0-3.2.21,4.0.0-4.5.5,27.0.0 |  | 
| CVE-2026-101578 | Helidon | helidon-security-providers-google-login | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | Low | None | None | 4.0.0-4.5.5 |  | 
| CVE-2026-101586 | Helidon | helidon-webclient | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | Low | None | None | 4.0.0-4.5.5,27.0.0 |  | 
| CVE-2026-101587 | Helidon | helidon-webclient-http1 | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | None | None | Low | 4.0.0-4.5.5,27.0.0 |  | 
| CVE-2026-64607 | Oracle Access Manager | Authentication Engine (Apache HttpClient) | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | None | None | Low | 14.1.2.0.0 |  | 
| CVE-2026-64607 | Oracle Middleware Common Libraries and Tools | Third Party (Apache HttpClient) | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | None | None | Low | 14.1.2.0.0 |  | 
| CVE-2026-91352 | Oracle Outside In Technology | Outside In Clean Content SDK | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | None | None | Low | 8.5.8 |  | 
| CVE-2026-87360 | Oracle WebCenter Content | Content Server | HTTP | Yes | 5.3 | Network | High | None | Required | Un- changed | High | None | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91248 | Oracle WebCenter Portal | Runtime Tools | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | Low | None | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91536 | Oracle SOA Suite | Fabric Layer | HTTPS | No | 5.0 | Network | High | Low | None | Un- changed | Low | Low | Low | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-101497 | Oracle Identity Manager | Connector Framework | HTTP | No | 4.3 | Network | Low | Low | None | Un- changed | None | None | Low | 12.2.1.4.0, 14.1.2.1.0 |  | 
| CVE-2026-87361 | Oracle WebCenter Content | Content Server | HTTP | No | 4.3 | Network | Low | Low | None | Un- changed | None | Low | None | 12.2.1.4.0 |  | 
| CVE-2026-87379 | WebCenter Content: Imaging | Core | SOAP | No | 4.3 | Network | Low | Low | None | Un- changed | Low | None | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91404 | Oracle Outside In Technology | Outside In PDF Export SDK | None | No | 4.0 | Local | Low | None | None | Un- changed | Low | None | None | 8.5.8 |  | 
| CVE-2026-101576 | Helidon | LRA | HTTP | Yes | 3.7 | Network | High | None | None | Un- changed | Low | None | None | 4.0.0-4.5.5 |  | 
| CVE-2026-101570 | Helidon | helidon-webserver-http2 | HTTP/2 | Yes | 3.7 | Network | High | None | None | Un- changed | None | None | Low | 4.0.0-4.5.5 |  | 
| CVE-2026-91616 | Oracle Middleware Common Libraries and Tools | Remote Diagnostic Agent | HTTP | Yes | 3.7 | Network | High | None | None | Un- changed | Low | None | None | 12.2.1.4.0, 14.1.1.0.0 |  | 
| CVE-2026-91322 | Oracle JDeveloper | Oracle JDeveloper | None | No | 3.3 | Local | Low | Low | None | Un- changed | Low | None | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-101577 | Helidon | helidon-cors | HTTP | Yes | 3.1 | Network | High | None | Required | Un- changed | None | Low | None | 4.0.0-4.5.5 |  | 
| CVE-2026-91261 | Oracle WebCenter Content | Content Server | HTTP | No | 3.1 | Network | High | Low | None | Un- changed | Low | None | None | 14.1.2.0.0 |  | 

- The patch for CVE-2026-4176 also addresses CVE-2026-27171 and CVE-2026-3381.
- The patch for CVE-2026-59889 also addresses CVE-2026-54515, CVE-2026-54517, and CVE-2026-54518.
- The patch for CVE-2026-91668 also addresses CVE-2022-41853.
- The patch for CVE-2026-41855 also addresses CVE-2026-22740, CVE-2026-22741, CVE-2026-22745, CVE-2026-41838, CVE-2026-41839, CVE-2026-41840, CVE-2026-41841, CVE-2026-41842, CVE-2026-41843, CVE-2026-41844, CVE-2026-41845, CVE-2026-41846, CVE-2026-41847, CVE-2026-41848, CVE-2026-41849, CVE-2026-41850, CVE-2026-41851, CVE-2026-41852, CVE-2026-41853, and CVE-2026-41854.
- The patch for CVE-2026-56741 also addresses CVE-2026-56740, CVE-2026-77420, CVE-2026-77421, and CVE-2026-77422.
- The patch for CVE-2026-34477 also addresses CVE-2025-68161.
- The patch for CVE-2024-41311 also addresses CVE-2024-38949 and CVE-2024-38950.
- The patch for CVE-2026-12817 also addresses CVE-2026-59645.
- The patch for CVE-2026-41635 also addresses CVE-2026-41409 and CVE-2026-47065.
- The patch for CVE-2026-54513 also addresses CVE-2026-54512.
- The patch for CVE-2026-42404 also addresses CVE-2026-42402 and CVE-2026-42403.
- The patch for CVE-2026-59649 also addresses CVE-2026-12185, CVE-2026-12802, CVE-2026-12803, CVE-2026-12816, CVE-2026-12817, CVE-2026-12860, CVE-2026-13506, CVE-2026-13586, CVE-2026-14682, CVE-2026-15055, CVE-2026-58059, CVE-2026-58060, CVE-2026-58061, CVE-2026-58062, CVE-2026-58063, CVE-2026-59639, CVE-2026-59642, CVE-2026-59645, CVE-2026-59647, CVE-2026-59650, CVE-2026-59651, CVE-2026-59652, and CVE-2026-8763.
- The patch for CVE-2026-91776 also addresses CVE-2026-89407, CVE-2026-89425, and CVE-2026-91777.
- The patch for CVE-2026-42779 also addresses CVE-2026-42778.
- The patch for CVE-2026-8763 also addresses CVE-2025-14813, CVE-2026-12185, CVE-2026-12803, CVE-2026-12816, CVE-2026-12860, CVE-2026-13506, CVE-2026-13586, CVE-2026-14682, CVE-2026-58059, CVE-2026-58060, CVE-2026-58061, CVE-2026-58062, CVE-2026-58063, CVE-2026-59650, CVE-2026-59651, and CVE-2026-59652.

This Critical Patch Update contains 33 new security patches, plus additional third party patches noted below, for Oracle Analytics.  14 of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cpuoct2026verbose.html#ANLY)

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-91241 | Oracle Business Intelligence Enterprise Edition | Analytics Web Administration | HTTP | No | 9.1 | Network | Low | High | None | Changed | High | High | High | 8.2.0.0.0, 12.2.1.4.0, 26.01.0.0.0 |  | 
| CVE-2026-75803 | Oracle Business Intelligence Enterprise Edition | Platform Security (OpenSSL) | HTTPS | Yes | 9.1 | Network | Low | None | None | Un- changed | High | High | None | 8.2.0.0.0, 26.01.0.0.0 |  | 
| CVE-2026-91579 | Oracle BI Publisher | BI Platform Security | HTTP | Yes | 8.8 | Network | Low | None | Required | Un- changed | High | High | High | 8.2.0.0.0, 12.2.1.4.0, 26.01.0.0.0 |  | 
| CVE-2026-87263 | Oracle Business Intelligence Enterprise Edition | Analytics Server | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 8.2.0.0.0, 26.01.0.0.0 |  | 
| CVE-2026-91535 | Oracle Business Intelligence Enterprise Edition | BI Search | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 8.2.0.0.0, 12.2.1.4.0, 26.01.0.0.0 |  | 
| CVE-2026-91534 | Oracle Business Intelligence Enterprise Edition | Analytics Web General | HTTP | Yes | 8.6 | Network | Low | None | None | Un- changed | Low | Low | High | 8.2.0.0.0, 12.2.1.4.0, 26.01.0.0.0 |  | 
| CVE-2026-91597 | Oracle Business Intelligence Enterprise Edition | Platform Security | TLS | Yes | 8.3 | Adjacent Network | High | None | None | Changed | High | High | High | 8.2.0.0.0, 26.01.0.0.0 |  | 
| CVE-2026-91546 | Oracle Business Intelligence Enterprise Edition | BI Foundation | HTTP | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 12.2.1.4.0 |  | 
| CVE-2026-28387 | Oracle Business Intelligence Enterprise Edition | Foundation (OpenSSL) | HTTPS | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 8.2.0.0.0, 26.01.0.0.0 |  | 
| CVE-2026-91549 | Oracle Business Intelligence Enterprise Edition | Analytics Server | None | No | 7.8 | Local | Low | None | Required | Un- changed | High | High | High | 8.2.0.0.0, 12.2.1.4.0 |  | 
| CVE-2026-91545 | Oracle Business Intelligence Enterprise Edition | Platform Security | None | No | 7.8 | Local | Low | None | Required | Un- changed | High | High | High | 8.2.0.0.0, 12.2.1.4.0 |  | 
| CVE-2026-91539 | Oracle Business Intelligence Enterprise Edition | Presentation Services | None | No | 7.8 | Local | Low | Low | None | Un- changed | High | High | High | 12.2.1.4.0 |  | 
| CVE-2026-91608 | Oracle BI Publisher | Web Server | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | High | None | None | 8.2.0.0.0, 12.2.1.4.0, 26.01.0.0.0 |  | 
| CVE-2026-101531 | Oracle Business Intelligence Enterprise Edition | Analytics Server | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | High | None | None | 8.2.0.0.0, 26.01.0.0.0 |  | 
| CVE-2026-31790 | Oracle Business Intelligence Enterprise Edition | Visual Analyzer (OpenSSL) | HTTPS | Yes | 7.5 | Network | Low | None | None | Un- changed | High | None | None | 8.2.0.0.0, 26.01.0.0.0 |  | 
| CVE-2026-91557 | Oracle Business Intelligence Enterprise Edition | BI Foundation | None | No | 7.0 | Local | High | Low | None | Un- changed | High | High | High | 12.2.1.4.0 |  | 
| CVE-2026-91574 | Oracle BI Publisher | BI Publisher Security | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 8.2.0.0.0, 12.2.1.4.0, 26.01.0.0.0 |  | 
| CVE-2026-91514 | Oracle BI Publisher | Web Server | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 8.2.0.0.0, 12.2.1.4.0, 26.01.0.0.0 |  | 
| CVE-2026-91554 | Oracle BI Publisher | Web Server | HTTP | Yes | 6.5 | Network | Low | None | None | Un- changed | Low | Low | None | 12.2.1.4.0 |  | 
| CVE-2026-91576 | Oracle Business Intelligence Enterprise Edition | Analytics Server | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 12.2.1.4.0 |  | 
| CVE-2026-91588 | Oracle Business Intelligence Enterprise Edition | BI Search | HTTP | Yes | 6.5 | Network | Low | None | Required | Un- changed | None | High | None | 8.2.0.0.0, 12.2.1.4.0 |  | 
| CVE-2026-91577 | Oracle Business Intelligence Enterprise Edition | BI Platform Security | HTTP | No | 6.4 | Network | Low | Low | None | Changed | Low | Low | None | 12.2.1.4.0 |  | 
| CVE-2026-91555 | Oracle BI Publisher | Web Server | HTTP | Yes | 6.1 | Network | Low | None | Required | Changed | Low | Low | None | 8.2.0.0.0, 12.2.1.4.0, 26.01.0.0.0 |  | 
| CVE-2026-91518 | Oracle BI Publisher | BI Publisher Security | HTTP | No | 5.4 | Network | Low | Low | None | Un- changed | Low | Low | None | 8.2.0.0.0, 12.2.1.4.0, 26.01.0.0.0 |  | 
| CVE-2026-91590 | Oracle BI Publisher | Web Service API | HTTP | No | 5.4 | Network | Low | Low | Required | Changed | Low | Low | None | 8.2.0.0.0, 26.01.0.0.0 |  | 
| CVE-2026-91523 | Oracle Business Intelligence Enterprise Edition | Analytics Web General | HTTP | No | 5.4 | Network | Low | Low | Required | Changed | Low | Low | None | 8.2.0.0.0, 12.2.1.4.0, 26.01.0.0.0 |  | 
| CVE-2026-91526 | Oracle BI Publisher | Web Server | HTTP | Yes | 4.7 | Network | High | None | Required | Changed | Low | Low | None | 8.2.0.0.0, 12.2.1.4.0, 26.01.0.0.0 |  | 
| CVE-2026-91528 | Oracle BI Publisher | BI Platform Security | HTTPS | No | 4.3 | Network | Low | Low | None | Un- changed | Low | None | None | 12.2.1.4.0 |  | 
| CVE-2026-91607 | Oracle Business Intelligence Enterprise Edition | Analytics Server | HTTP | No | 4.3 | Network | Low | Low | None | Un- changed | Low | None | None | 8.2.0.0.0, 26.01.0.0.0 |  | 
| CVE-2026-91524 | Oracle Business Intelligence Enterprise Edition | BI Foundation | HTTP | No | 4.3 | Network | Low | Low | None | Un- changed | None | None | Low | 12.2.1.4.0 |  | 
| CVE-2026-91598 | Oracle Business Intelligence Enterprise Edition | Majel Mobile Service | HTTP | No | 4.3 | Network | Low | Low | None | Un- changed | Low | None | None | 8.2.0.0.0, 26.01.0.0.0 |  | 
| CVE-2026-91600 | Oracle Business Intelligence Enterprise Edition | Visual Analyzer | HTTP | No | 4.3 | Network | Low | Low | None | Un- changed | Low | None | None | 26.01.0.0.0 |  | 
| CVE-2026-91582 | Oracle Business Intelligence Enterprise Edition | BI Search | HTTP | Yes | 3.7 | Network | High | None | None | Un- changed | None | None | Low | 12.2.1.4.0 |  | 

- The patch for CVE-2026-101531 also addresses CVE-2026-5598.
- The patch for CVE-2026-31790 also addresses CVE-2026-28387, CVE-2026-28388, CVE-2026-28389, CVE-2026-28390, and CVE-2026-31789.
- The patch for CVE-2026-75803 also addresses CVE-2026-28387, CVE-2026-54874, CVE-2026-63072, CVE-2026-63074, and CVE-2026-63076.

- Oracle BI Publisher
  - Administration: CVE-2026-91584.

This Critical Patch Update contains 4 new security patches for Oracle HealthCare Applications.  All of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cpuoct2026verbose.html#HC)

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-42779 | Oracle Health Sciences Information Manager | Record Locator (Apache Mina) | HTTP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 4.0.0-4.0.3 |  | 
| CVE-2026-42779 | Oracle Healthcare Master Person Index | Core (Apache Mina) | HTTP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 5.0.0.0-5.0.9.7 |  | 
| CVE-2026-41855 | Oracle Healthcare Data Repository | FHIR Server (Spring Framework) | HTTP | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 8.2.0.0-8.2.0.8 |  | 
| CVE-2026-41855 | Oracle Healthcare Master Person Index | Master Index Data Manager (Spring Framework) | HTTP | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 5.0.0.0-5.0.9.7 |  | 

- The patch for CVE-2026-41855 also addresses CVE-2026-41838, CVE-2026-41839, CVE-2026-41840, CVE-2026-41841, CVE-2026-41842, CVE-2026-41843, CVE-2026-41844, CVE-2026-41845, CVE-2026-41846, CVE-2026-41848, CVE-2026-41850, CVE-2026-41851, CVE-2026-41852, CVE-2026-41853, and CVE-2026-41854.
- The patch for CVE-2026-42779 also addresses CVE-2026-42778.

This Critical Patch Update contains 4 new security patches for Oracle Hospitality Applications.  All of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cpuoct2026verbose.html#HOSP)

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-34481 | Oracle Hospitality OPERA 5 Property Services | OPERA Login (Apache Log4j) | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | High | None | 5.6.28.2 |  | 
| CVE-2025-64775 | Oracle Hospitality OPERA 5 Property Services | OPERA Login (Apache Struts) | HTTPS | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 5.6.28.2 |  | 
| CVE-2026-55956 | Oracle Hospitality Cruise Shipboard Property Management (SPMS) | Next-Gen SPMS (Apache Tomcat) | HTTP | Yes | 6.5 | Network | Low | None | None | Un- changed | Low | Low | None | 23.1, 23.2, 23.3 |  | 
| CVE-2024-47554 | Oracle Hospitality OPERA 5 Property Services | OPERA Login (Apache Commons IO) | HTTP | Yes | 4.3 | Network | Low | None | Required | Un- changed | None | None | Low | 5.6.28.0 |  | 

- The patch for CVE-2026-34481 also addresses CVE-2025-68161, CVE-2026-34477, CVE-2026-34478, CVE-2026-34479, and CVE-2026-34480.
- The patch for CVE-2026-55956 also addresses CVE-2026-50229, CVE-2026-53404, CVE-2026-53434, CVE-2026-55276, and CVE-2026-55955.

This Critical Patch Update contains 55 new security patches for Oracle Java SE.  49 of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cpuoct2026verbose.html#JAVA)

The CVSS scores below assume that a user running a Java applet or Java Web Start application has administrator privileges (typical on Windows). When the user does not run with administrator privileges (typical on Solaris and Linux), the corresponding CVSS impact scores for Confidentiality, Integrity, and Availability are "Low" instead of "High", lowering the CVSS Base Score. For example, a Base Score of 9.6 becomes 7.1.


Java Management Service, available to all users, can help you find vulnerable Java versions in your systems. Java SE Subscribers and customers running in Oracle Cloud can use Java Management Service to update Java Runtimes and to do further security reviews like identifying potentially vulnerable third party libraries used by your Java programs. Existing Java Management Service user [click here](https://cloud.oracle.com/jms/overview) to log in to your dashboard. [The Java Management Service Documentation](https://docs.oracle.com/en-us/iaas/jms/index.html) provides a list of features available to everyone and those available only to customers. [Learn more about using Java Management Service](https://www.oracle.com/java/jms/) to monitor and secure your Java Installations.

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-91484 | Oracle Java SE | Java plugin | None | No | 7.5 | Local | High | Low | None | Changed | High | High | None | Oracle Java SE: 8u503, 8u503-perf | See Note 1 | 
| CVE-2026-43660 | Oracle Java SE, Oracle JavaFX | JavaFX (WebKitGTK) | Multiple | Yes | 7.5 | Network | High | None | Required | Un- changed | High | High | High | Oracle Java SE: 8u503; Oracle JavaFX: 21.0.12, 25.0.4, 27 | See Note 1 | 
| CVE-2026-91415 | Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition | 2D | Multiple | Yes | 7.0 | Network | High | None | None | Un- changed | Low | Low | High | Oracle Java SE: 8u503, 8u503-perf, 11.0.32.1, 17.0.20.1, 21.0.12.1, 25.0.4.1, 27; Oracle GraalVM for JDK: 17.0.20.1, 21.0.12.1; Oracle GraalVM Enterprise Edition: 21.3.19.1.1 | See Note 2 | 
| CVE-2026-91398 | Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition | Networking | SOCKS5 | Yes | 6.8 | Network | High | None | None | Changed | None | High | None | Oracle Java SE: 8u503, 8u503-perf, 11.0.32.1, 17.0.20.1, 21.0.12.1, 25.0.4.1, 27; Oracle GraalVM for JDK: 17.0.20.1, 21.0.12.1; Oracle GraalVM Enterprise Edition: 21.3.19.1.1 | See Note 2 | 
| CVE-2026-91382 | Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition | 2D | Multiple | Yes | 6.5 | Network | High | None | None | Un- changed | None | High | Low | Oracle Java SE: 8u503, 8u503-perf, 11.0.32.1, 17.0.20.1; Oracle GraalVM for JDK: 17.0.20.1, 21.0.12.1; Oracle GraalVM Enterprise Edition: 21.3.19.1.1 | See Note 2 | 
| CVE-2026-91411 | Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition | JGSS | Multiple | Yes | 6.5 | Network | High | None | None | Un- changed | None | Low | High | Oracle Java SE: 8u503, 8u503-perf, 11.0.32.1; Oracle GraalVM for JDK: 17.0.20.1, 21.0.12.1; Oracle GraalVM Enterprise Edition: 21.3.19.1.1 | See Note 2 | 
| CVE-2026-101516 | Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition | Libraries | Multiple | Yes | 6.5 | Network | Low | None | None | Un- changed | Low | Low | None | Oracle Java SE: 8u503, 8u503-perf, 11.0.32.1, 17.0.20.1, 21.0.12.1, 25.0.4.1, 27; Oracle GraalVM for JDK: 17.0.20.1, 21.0.12.1; Oracle GraalVM Enterprise Edition: 21.3.19.1.1 | See Note 2 | 
| CVE-2026-83395 | Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition | Networking | Multiple | Yes | 6.5 | Network | Low | None | None | Un- changed | None | Low | Low | Oracle Java SE: 8u503, 8u503-perf, 11.0.32.1, 17.0.20.1, 21.0.12.1, 25.0.4.1, 27; Oracle GraalVM for JDK: 17.0.20.1, 21.0.12.1; Oracle GraalVM Enterprise Edition: 21.3.19.1.1 | See Note 2 | 
| CVE-2026-87294 | Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition | Security | Multiple | Yes | 6.5 | Network | Low | None | None | Un- changed | Low | Low | None | Oracle Java SE: 8u503, 8u503-perf, 11.0.32.1, 17.0.20.1, 21.0.12.1, 25.0.4.1, 27; Oracle GraalVM for JDK: 17.0.20.1, 21.0.12.1; Oracle GraalVM Enterprise Edition: 21.3.19.1.1 | See Note 2 | 
| CVE-2026-91395 | Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition | Utility | Multiple | Yes | 6.5 | Network | Low | None | None | Un- changed | None | Low | Low | Oracle Java SE: 8u503, 8u503-perf, 11.0.32.1; Oracle GraalVM for JDK: 17.0.20.1, 21.0.12.1; Oracle GraalVM Enterprise Edition: 21.3.19.1.1 | See Note 2 | 
| CVE-2026-91396 | Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition | Utility | Multiple | Yes | 6.5 | Network | Low | None | None | Un- changed | None | Low | Low | Oracle Java SE: 8u503, 8u503-perf, 11.0.32.1; Oracle GraalVM for JDK: 17.0.20.1, 21.0.12.1; Oracle GraalVM Enterprise Edition: 21.3.19.1.1 | See Note 2 | 
| CVE-2026-101737 | Oracle Java SE | Compiler | Multiple | Yes | 5.9 | Network | High | None | None | Un- changed | None | None | High | Oracle Java SE: 26.0.2 | See Note 3 | 
| CVE-2026-91394 | Oracle Java SE, Oracle GraalVM for JDK | Networking | Multiple | Yes | 5.9 | Network | High | None | None | Un- changed | High | None | None | Oracle Java SE: 11.0.32.1, 17.0.20.1, 21.0.12.1, 25.0.4.1, 27; Oracle GraalVM for JDK: 17.0.20.1, 21.0.12.1 | See Note 2 | 
| CVE-2026-87290 | Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition | JAXP | Multiple | Yes | 5.9 | Network | High | None | None | Un- changed | High | None | None | Oracle Java SE: 8u503, 8u503-perf, 11.0.32.1, 17.0.20.1, 21.0.12.1, 25.0.4.1, 27; Oracle GraalVM for JDK: 17.0.20.1, 21.0.12.1; Oracle GraalVM Enterprise Edition: 21.3.19.1.1 | See Note 2 | 
| CVE-2026-83387 | Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition | JDBC | Multiple | Yes | 5.9 | Network | High | None | None | Un- changed | High | None | None | Oracle Java SE: 8u503, 8u503-perf, 11.0.32.1, 17.0.20.1, 21.0.12.1, 25.0.4.1, 27; Oracle GraalVM for JDK: 17.0.20.1, 21.0.12.1; Oracle GraalVM Enterprise Edition: 21.3.19.1.1 | See Note 2 | 
| CVE-2026-91462 | Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition | JGSS | Multiple | Yes | 5.9 | Network | High | None | None | Un- changed | None | High | None | Oracle Java SE: 8u503, 8u503-perf, 11.0.32.1, 17.0.20.1, 21.0.12.1, 25.0.4.1, 27; Oracle GraalVM for JDK: 17.0.20.1, 21.0.12.1; Oracle GraalVM Enterprise Edition: 21.3.19.1.1 | See Note 3 | 
| CVE-2026-83374 | Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition | Security | Multiple | Yes | 5.9 | Network | High | None | None | Un- changed | None | High | None | Oracle Java SE: 8u503, 8u503-perf, 11.0.32.1, 17.0.20.1, 21.0.12.1, 25.0.4.1, 27; Oracle GraalVM for JDK: 17.0.20.1, 21.0.12.1; Oracle GraalVM Enterprise Edition: 21.3.19.1.1 | See Note 2 | 
| CVE-2026-6732 | Oracle Java SE, Oracle JavaFX, Oracle GraalVM Enterprise Edition | JavaFX (WebKitGTK) | Multiple | Yes | 5.9 | Network | High | None | None | Un- changed | None | None | High | Oracle Java SE: 8u503; Oracle JavaFX: 21.0.12, 25.0.4, 27;Oracle GraalVM Enterprise Edition: 21.3.19.1.1 | See Note 1 | 
| CVE-2026-87293 | Oracle Java SE | RMI | Multiple | Yes | 5.4 | Network | High | None | None | Changed | Low | Low | None | Oracle Java SE: 8u503, 8u503-perf; Oracle GraalVM Enterprise Edition: 21.3.19.1.1 | See Note 3 | 
| CVE-2026-91385 | Oracle Java SE, Oracle JavaFX, Oracle GraalVM Enterprise Edition | JavaFX | Multiple | Yes | 5.4 | Network | Low | None | Required | Un- changed | Low | Low | None | Oracle Java SE: 8u503; Oracle JavaFX: 21.0.12, 25.0.4, 27; Oracle GraalVM Enterprise Edition: 21.3.19.1.1 | See Note 1 | 
| CVE-2026-91410 | Oracle Java SE | Libraries | Multiple | Yes | 5.3 | Network | Low | None | None | Un- changed | None | None | Low | Oracle Java SE: 8u503, 8u503-perf, 11.0.32.1, 17.0.20.1, 21.0.12.1, 25.0.4.1; Oracle GraalVM for JDK: 17.0.20.1, 21.0.12.1; Oracle GraalVM Enterprise Edition: 21.3.19.1.1 | See Note 2 | 
| CVE-2026-87291 | Oracle Java SE | Networking | Multiple | Yes | 5.3 | Network | Low | None | None | Un- changed | Low | None | None | Oracle Java SE: 21.0.12.1, 25.0.4.1, 27 | See Note 3 | 
| CVE-2026-91332 | Oracle Java SE | Networking | Multiple | Yes | 5.3 | Network | Low | None | None | Un- changed | None | Low | None | Oracle Java SE: 8u503-perf, 11.0.32.1, 17.0.20.1, 21.0.12.1, 25.0.4.1, 27; Oracle GraalVM for JDK: 17.0.20.1, 21.0.12.1; Oracle GraalVM Enterprise Edition: 21.3.19.1.1 | See Note 2 | 
| CVE-2026-91451 | Oracle Java SE | Networking | Multiple | Yes | 5.3 | Network | Low | None | None | Un- changed | None | Low | None | Oracle Java SE: 8u503, 8u503-perf, 11.0.32.1, 17.0.20.1, 21.0.12.1, 25.0.4.1; Oracle GraalVM for JDK: 17.0.20.1, 21.0.12.1; Oracle GraalVM Enterprise Edition: 21.3.19.1.1 | See Note 3 | 
| CVE-2026-91373 | Oracle Java SE | JSSE | TLS | Yes | 5.3 | Network | Low | None | None | Un- changed | None | None | Low | Oracle Java SE: 8u503, 8u503-perf, 11.0.32.1, 17.0.20.1, 21.0.12.1, 25.0.4.1; Oracle GraalVM for JDK: 17.0.20.1, 21.0.12.1; Oracle GraalVM Enterprise Edition: 21.3.19.1.1 | See Note 2 | 
| CVE-2026-91417 | Oracle Java SE, Oracle GraalVM Enterprise Edition | CORBA | Multiple | Yes | 5.3 | Network | Low | None | None | Un- changed | None | None | Low | Oracle Java SE: 8u503, 8u503-perf; Oracle GraalVM Enterprise Edition: 21.3.19.1.1 | See Note 3 | 
| CVE-2026-83380 | Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition | JAAS | Multiple | Yes | 5.3 | Network | Low | None | None | Un- changed | Low | None | None | Oracle Java SE: 8u503, 8u503-perf, 11.0.32.1, 17.0.20.1, 21.0.12.1, 25.0.4.1, 27; Oracle GraalVM for JDK: 17.0.20.1, 21.0.12.1; Oracle GraalVM Enterprise Edition: 21.3.19.1.1 | See Note 2 | 
| CVE-2026-83400 | Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition | JAXP | Multiple | Yes | 5.3 | Network | Low | None | None | Un- changed | None | None | Low | Oracle Java SE: 8u503, 8u503-perf, 11.0.32.1, 17.0.20.1, 21.0.12.1, 25.0.4.1, 27; Oracle GraalVM for JDK: 17.0.20.1, 21.0.12.1; Oracle GraalVM Enterprise Edition: 21.3.19.1.1 | See Note 2 | 
| CVE-2026-91463 | Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition | JGSS | Multiple | Yes | 5.3 | Network | High | None | Required | Un- changed | High | None | None | Oracle Java SE: 8u503, 8u503-perf, 11.0.32.1, 17.0.20.1, 21.0.12.1, 25.0.4.1, 27; Oracle GraalVM for JDK: 17.0.20.1, 21.0.12.1; Oracle GraalVM Enterprise Edition: 21.3.19.1.1 | See Note 1 | 
| CVE-2026-91464 | Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition | JGSS | Multiple | Yes | 5.3 | Network | High | None | Required | Un- changed | High | None | None | Oracle Java SE: 8u503, 8u503-perf, 11.0.32.1, 17.0.20.1, 21.0.12.1, 25.0.4.1, 27; Oracle GraalVM for JDK: 17.0.20.1, 21.0.12.1; Oracle GraalVM Enterprise Edition: 21.3.19.1.1 | See Note 1 | 
| CVE-2026-91453 | Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition | Lightweight HTTP Server | Multiple | Yes | 5.3 | Network | Low | None | None | Un- changed | None | Low | None | Oracle Java SE: 8u503, 8u503-perf, 11.0.32.1, 17.0.20.1, 21.0.12.1, 25.0.4.1, 27; Oracle GraalVM for JDK: 17.0.20.1, 21.0.12.1; Oracle GraalVM Enterprise Edition: 21.3.19.1.1 | See Note 3 | 
| CVE-2026-91452 | Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition | Networking | Multiple | Yes | 5.3 | Network | Low | None | None | Un- changed | None | Low | None | Oracle Java SE: 8u503, 8u503-perf, 11.0.32.1, 17.0.20.1, 21.0.12.1, 25.0.4.1, 27; Oracle GraalVM for JDK: 17.0.20.1, 21.0.12.1; Oracle GraalVM Enterprise Edition: 21.3.19.1.1 | See Note 3 | 
| CVE-2026-91418 | Oracle Java SE, Oracle JavaFX, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition | ImageIO | Multiple | Yes | 5.3 | Network | Low | None | None | Un- changed | None | None | Low | Oracle Java SE: 8u503, 8u503-perf, 11.0.32.1, 17.0.20.1, 21.0.12.1, 25.0.4.1, 27; Oracle JavaFX: 21.0.12, 25.0.4, 27; Oracle GraalVM for JDK: 17.0.20.1, 21.0.12.1; Oracle GraalVM Enterprise Edition: 21.3.19.1.1 | See Note 2 | 
| CVE-2026-83378 | Oracle Java SE | Compiler | Multiple | Yes | 4.8 | Network | High | None | None | Un- changed | Low | Low | None | Oracle Java SE: 21.0.12.1, 25.0.4.1, 27 | See Note 3 | 
| CVE-2026-91487 | Oracle Java SE | Compiler | Multiple | Yes | 4.8 | Network | High | None | None | Un- changed | Low | Low | None | Oracle Java SE: 8u503-perf, 11.0.32.1, 17.0.20.1, 21.0.12.1, 25.0.4.1, 27; Oracle GraalVM for JDK: 17.0.20.1, 21.0.12.1; Oracle GraalVM Enterprise Edition: 21.3.19.1.1 | See Note 3 | 
| CVE-2026-83381 | Oracle Java SE | Security | Multiple | Yes | 4.8 | Network | High | None | None | Un- changed | Low | Low | None | Oracle Java SE: 8u503, 8u503-perf, 11.0.32.1, 17.0.20.1, 21.0.12.1, 25.0.4.1, 27; Oracle GraalVM for JDK: 17.0.20.1, 21.0.12.1; Oracle GraalVM Enterprise Edition: 21.3.19.1.1 | See Note 2 | 
| CVE-2026-91374 | Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition | Serviceability | Multiple | Yes | 4.8 | Network | High | None | None | Un- changed | Low | Low | None | Oracle Java SE: 8u503, 8u503-perf, 11.0.32.1, 17.0.20.1, 21.0.12.1, 25.0.4.1, 27; Oracle GraalVM for JDK: 17.0.20.1, 21.0.12.1; Oracle GraalVM Enterprise Edition: 21.3.19.1.1 | See Note 2 | 
| CVE-2026-91375 | Oracle Java SE | Libraries | None | No | 4.7 | Local | High | None | Required | Un- changed | None | High | None | Oracle Java SE: 8u503-perf, 11.0.32.1, 17.0.20.1, 21.0.12.1, 25.0.4.1, 27; Oracle GraalVM for JDK: 17.0.20.1, 21.0.12.1; Oracle GraalVM Enterprise Edition: 21.3.19.1.1 | See Note 2 | 
| CVE-2026-91379 | Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition | JDK tools | None | No | 4.7 | Local | High | None | Required | Un- changed | None | High | None | Oracle Java SE: 8u503-perf, 11.0.32.1, 17.0.20.1, 21.0.12.1, 25.0.4.1, 27; Oracle GraalVM for JDK: 17.0.20.1, 21.0.12.1; Oracle GraalVM Enterprise Edition: 21.3.19.1.1 | See Note 1 | 
| CVE-2026-46470 | Oracle Java SE, Oracle JavaFX | JavaFX (gstreamer) | Multiple | Yes | 4.2 | Network | High | None | Required | Un- changed | Low | None | Low | Oracle Java SE: 8u503; Oracle JavaFX: 21.0.12, 25.0.4, 27 | See Note 1 | 
| CVE-2026-91380 | Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition | Utility | None | No | 4.0 | Local | High | None | None | Un- changed | Low | Low | None | Oracle Java SE: 8u503, 8u503-perf, 11.0.32.1, 17.0.20.1, 21.0.12.1, 25.0.4.1, 27; Oracle GraalVM for JDK: 17.0.20.1, 21.0.12.1; Oracle GraalVM Enterprise Edition: 21.3.19.1.1 | See Note 2 | 
| CVE-2026-87255 | Oracle Java SE | Compiler | Multiple | Yes | 3.7 | Network | High | None | None | Un- changed | Low | None | None | Oracle Java SE: 25.0.4.1, 27 | See Note 3 | 
| CVE-2026-91409 | Oracle Java SE | Networking | Multiple | Yes | 3.7 | Network | High | None | None | Un- changed | None | None | Low | Oracle Java SE: 27 | See Note 2 | 
| CVE-2026-91333 | Oracle Java SE | Security | Multiple | Yes | 3.7 | Network | High | None | None | Un- changed | None | Low | None | Oracle Java SE: 21.0.12.1, 25.0.4.1, 27 | See Note 2 | 
| CVE-2026-91381 | Oracle Java SE, Oracle GraalVM Enterprise Edition | 2D | Multiple | Yes | 3.7 | Network | High | None | None | Un- changed | None | Low | None | Oracle Java SE: 8u503, 8u503-perf; Oracle GraalVM Enterprise Edition: 21.3.19.1.1 | See Note 2 | 
| CVE-2026-91334 | Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition | ImageIO | Multiple | Yes | 3.7 | Network | High | None | None | Un- changed | Low | None | None | Oracle Java SE: 8u503, 8u503-perf, 11.0.32.1, 17.0.20.1, 21.0.12.1, 25.0.4.1, 27; Oracle GraalVM for JDK: 17.0.20.1, 21.0.12.1; Oracle GraalVM Enterprise Edition: 21.3.19.1.1 | See Note 2 | 
| CVE-2026-87367 | Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition | JAXP | Multiple | Yes | 3.7 | Network | High | None | None | Un- changed | None | Low | None | Oracle Java SE: 8u503, 8u503-perf, 11.0.32.1, 17.0.20.1, 21.0.12.1, 25.0.4.1, 27; Oracle GraalVM for JDK: 17.0.20.1, 21.0.12.1; Oracle GraalVM Enterprise Edition: 21.3.19.1.1 | See Note 2 | 
| CVE-2026-87292 | Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition | Networking | Multiple | Yes | 3.7 | Network | High | None | None | Un- changed | None | Low | None | Oracle Java SE: 8u503, 8u503-perf, 11.0.32.1, 17.0.20.1, 21.0.12.1, 25.0.4.1, 27; Oracle GraalVM for JDK: 17.0.20.1, 21.0.12.1; Oracle GraalVM Enterprise Edition: 21.3.19.1.1 | See Note 2 | 
| CVE-2026-83376 | Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition | JSSE | TLS | Yes | 3.7 | Network | High | None | None | Un- changed | None | Low | None | Oracle Java SE: 8u503, 8u503-perf, 11.0.32.1, 17.0.20.1, 21.0.12.1, 25.0.4.1, 27; Oracle GraalVM for JDK: 17.0.20.1, 21.0.12.1; Oracle GraalVM Enterprise Edition: 21.3.19.1.1 | See Note 2 | 
| CVE-2026-91461 | Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition | JSSE | TLS | Yes | 3.7 | Network | High | None | None | Un- changed | None | Low | None | Oracle Java SE: 8u503, 8u503-perf, 11.0.32.1, 17.0.20.1, 21.0.12.1, 25.0.4.1, 27; Oracle GraalVM for JDK: 17.0.20.1, 21.0.12.1; Oracle GraalVM Enterprise Edition: 21.3.19.1.1 | See Note 3 | 
| CVE-2026-91397 | Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition | Serviceability | None | No | 3.6 | Local | High | None | Required | Un- changed | None | Low | Low | Oracle Java SE: 8u503, 8u503-perf, 11.0.32.1, 17.0.20.1, 21.0.12.1, 25.0.4.1, 27; Oracle GraalVM for JDK: 17.0.20.1, 21.0.12.1; Oracle GraalVM Enterprise Edition: 21.3.19.1.1 | See Note 2 | 
| CVE-2026-91400 | Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition | Sound | Multiple | Yes | 3.1 | Network | High | None | Required | Un- changed | None | None | Low | Oracle Java SE: 8u503, 8u503-perf, 11.0.32.1, 17.0.20.1, 21.0.12.1, 25.0.4.1, 27; Oracle GraalVM for JDK: 17.0.20.1, 21.0.12.1; Oracle GraalVM Enterprise Edition: 21.3.19.1.1 | See Note 1 | 
| CVE-2026-91402 | Oracle Java SE, Oracle JavaFX, Oracle GraalVM Enterprise Edition | JavaFX | Multiple | Yes | 3.1 | Network | High | None | Required | Un- changed | Low | None | None | Oracle Java SE: 8u503; Oracle JavaFX: 21.0.12, 25.0.4, 27; Oracle GraalVM Enterprise Edition: 21.3.19.1.1 | See Note 1 | 
| CVE-2026-91477 | Oracle JavaFX | JavaFX | Multiple | Yes | 3.1 | Network | High | None | Required | Un- changed | Low | None | None | Oracle JavaFX: 25.0.4, 27 | See Note 1 | 
| CVE-2026-91335 | Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition | AWT | Multiple | No | 2.6 | Network | High | Low | Required | Un- changed | Low | None | None | Oracle Java SE: 8u503, 8u503-perf, 11.0.32.1, 17.0.20.1, 21.0.12.1, 25.0.4.1, 27; Oracle GraalVM for JDK: 17.0.20.1, 21.0.12.1; Oracle GraalVM Enterprise Edition: 21.3.19.1.1 | See Note 1 | 

1. This vulnerability applies to Java deployments, typically in clients running sandboxed Java Web Start applications or sandboxed Java applets, that load and run untrusted code (e.g., code that comes from the internet) and rely on the Java sandbox for security. This vulnerability does not apply to Java deployments, typically in servers, that load and run only trusted code (e.g., code installed by an administrator).
2. This vulnerability can be exploited by using APIs in the specified Component, e.g., through a web service which supplies data to the APIs. This vulnerability also applies to Java deployments, typically in clients running sandboxed Java Web Start applications or sandboxed Java applets, that load and run untrusted code (e.g., code that comes from the internet) and rely on the Java sandbox for security.
3. This vulnerability can only be exploited by supplying data to APIs in the specified Component without using Untrusted Java Web Start applications or Untrusted Java applets, such as through a web service.

- The patch for CVE-2026-46470 also addresses CVE-2024-47778, CVE-2026-1940, CVE-2026-2921, CVE-2026-39044, and CVE-2026-46469.
- The patch for CVE-2026-43660 also addresses CVE-2024-4367, CVE-2026-20643, CVE-2026-20664, CVE-2026-20665, CVE-2026-20691, CVE-2026-28847, CVE-2026-28857, CVE-2026-28859, CVE-2026-28861, CVE-2026-28871, CVE-2026-28883, CVE-2026-28901, CVE-2026-28902, CVE-2026-28903, CVE-2026-28904, CVE-2026-28905, CVE-2026-28907, CVE-2026-28942, CVE-2026-28946, CVE-2026-28947, CVE-2026-28953, CVE-2026-28955, CVE-2026-28958, CVE-2026-28984, CVE-2026-39872, CVE-2026-43658, CVE-2026-43663, CVE-2026-43676, CVE-2026-43699, CVE-2026-43701, CVE-2026-43705, CVE-2026-43707, CVE-2026-43712, CVE-2026-43713, CVE-2026-43715, CVE-2026-43716, CVE-2026-43720, CVE-2026-43721, CVE-2026-43725, CVE-2026-43726, CVE-2026-43727, CVE-2026-43731, CVE-2026-43732, CVE-2026-43734, CVE-2026-43740, CVE-2026-43742, CVE-2026-43745, CVE-2026-43804, CVE-2026-64713, CVE-2026-64719, CVE-2026-64728, CVE-2026-64730, CVE-2026-64757, CVE-2026-64783, and CVE-2026-64787.

This Critical Patch Update contains 102 new security patches for Oracle JD Edwards.  44 of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cpuoct2026verbose.html#JDE)

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-91299 | JD Edwards EnterpriseOne Orchestrator | E1 IOT Orchestrator Security | HTTP | Yes | 10.0 | Network | Low | None | None | Changed | High | High | High | 9.2.0.0-9.2.26.5 |  | 
| CVE-2025-15467 | JD Edwards EnterpriseOne Tools | Enterprise Infrastructure SEC (OpenSSL) | HTTPS | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 9.2.0.0-9.2.26.5 |  | 
| CVE-2022-45378 | JD Edwards EnterpriseOne Tools | Web Runtime SEC (Apache SOAP) | SOAP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91265 | JD Edwards EnterpriseOne Tools | Enterprise Infrastructure SEC | HTTP | Yes | 9.1 | Network | Low | None | None | Un- changed | High | High | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91305 | JD Edwards EnterpriseOne Tools | Installation Security | HTTPS | Yes | 9.1 | Network | Low | None | None | Un- changed | High | High | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91295 | JD Edwards EnterpriseOne Tools | Enterprise Infrastructure SEC | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91296 | JD Edwards EnterpriseOne Tools | Enterprise Infrastructure SEC | HTTP | Yes | 8.8 | Network | Low | None | Required | Un- changed | High | High | High | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91303 | JD Edwards EnterpriseOne Tools | Installation Security | HTTP | Yes | 8.8 | Network | Low | None | Required | Un- changed | High | High | High | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91270 | JD Edwards EnterpriseOne Tools | Monitoring and Diagnostics SEC | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91268 | JD Edwards EnterpriseOne Tools | Web Runtime SEC | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91326 | JD Edwards EnterpriseOne Tools | Installation Security | HTTPS | Yes | 8.8 | Adjacent Network | Low | None | Required | Changed | High | High | High | 9.2.0.0-9.2.26.4 |  | 
| CVE-2026-87310 | JD Edwards EnterpriseOne Tools | Database and Comm SEC | JDENET | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91310 | JD Edwards EnterpriseOne Tools | Installation SEC | JDENET | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-87313 | JD Edwards EnterpriseOne Tools | Interoperability SEC | JDENET | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91273 | JD Edwards EnterpriseOne Tools | Object and Env Tech SEC | HTTP | Yes | 8.6 | Network | Low | None | None | Changed | High | None | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91267 | JD Edwards EnterpriseOne Tools | Interoperability SEC | SOAP | Yes | 8.6 | Network | Low | None | None | Changed | High | None | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91266 | JD Edwards EnterpriseOne Tools | Monitoring and Diagnostics SEC | None | No | 8.4 | Local | Low | Low | None | Changed | High | High | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91286 | JD Edwards EnterpriseOne Tools | Monitoring and Diagnostics SEC | HTTPS | Yes | 8.2 | Adjacent Network | Low | None | None | Changed | High | Low | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91269 | JD Edwards EnterpriseOne Tools | Enterprise Infrastructure SEC | HTTP | No | 8.1 | Network | Low | Low | None | Un- changed | High | High | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91313 | JD Edwards EnterpriseOne Tools | Installation Security | HTTP | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 9.2.0.0-9.2.26.4 |  | 
| CVE-2026-91271 | JD Edwards EnterpriseOne Tools | Monitoring and Diagnostics SEC | HTTP | No | 8.1 | Network | Low | Low | None | Un- changed | High | High | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-87309 | JD Edwards EnterpriseOne Tools | Package Build SEC | HTTP | No | 8.1 | Network | Low | Low | None | Un- changed | None | High | High | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91287 | JD Edwards EnterpriseOne Tools | Enterprise Infrastructure SEC | JDENET | Yes | 8.1 | Adjacent Network | Low | None | None | Un- changed | High | High | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-87306 | JD Edwards EnterpriseOne Tools | Interoperability SEC | JDENET | No | 8.1 | Network | Low | Low | None | Un- changed | High | High | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-87305 | JD Edwards EnterpriseOne Tools | Enterprise Infrastructure SEC | SMTP | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91328 | JD Edwards EnterpriseOne Tools | Deployment SEC | None | No | 7.8 | Local | Low | None | Required | Un- changed | High | High | High | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-87316 | JD Edwards EnterpriseOne Tools | Enterprise Infrastructure SEC | None | No | 7.8 | Local | Low | Low | None | Un- changed | High | High | High | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91304 | JD Edwards EnterpriseOne Tools | Installation Security | None | No | 7.8 | Local | Low | None | Required | Un- changed | High | High | High | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91306 | JD Edwards EnterpriseOne Tools | Installation Security | None | No | 7.8 | Local | Low | Low | None | Un- changed | High | High | High | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91311 | JD Edwards EnterpriseOne Tools | Installation Security | None | No | 7.8 | Local | Low | Low | None | Un- changed | High | High | High | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91314 | JD Edwards EnterpriseOne Tools | Installation Security | None | No | 7.8 | Local | Low | None | Required | Un- changed | High | High | High | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91315 | JD Edwards EnterpriseOne Tools | Installation Security | None | No | 7.8 | Local | Low | None | Required | Un- changed | High | High | High | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-87315 | JD Edwards EnterpriseOne Tools | Enterprise Infrastructure SEC | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | High | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91325 | JD Edwards EnterpriseOne Tools | Installation Security | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | High | None | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-87312 | JD Edwards EnterpriseOne Tools | Enterprise Infrastructure SEC | JDENET | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91307 | JD Edwards EnterpriseOne Tools | Installation Security | Oracle Net | Yes | 7.5 | Network | Low | None | None | Un- changed | High | None | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91308 | JD Edwards EnterpriseOne Tools | Installation Security | Oracle Net | Yes | 7.5 | Network | Low | None | None | Un- changed | High | None | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91327 | JD Edwards EnterpriseOne Tools | Installation Security | TLS | Yes | 7.5 | Adjacent Network | High | None | None | Un- changed | High | High | High | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91272 | JD Edwards EnterpriseOne Tools | Interoperability SEC | HTTPS | Yes | 7.4 | Network | High | None | None | Un- changed | High | High | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91288 | JD Edwards EnterpriseOne Tools | Interoperability SEC | JDENET | Yes | 7.4 | Network | High | None | None | Un- changed | High | High | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-87314 | JD Edwards EnterpriseOne Tools | Interoperability SEC | TLS | Yes | 7.4 | Network | High | None | None | Un- changed | High | High | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-87307 | JD Edwards EnterpriseOne Tools | Interoperability SEC | HTTP | No | 7.1 | Network | Low | Low | None | Un- changed | High | None | Low | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-87308 | JD Edwards EnterpriseOne Tools | Enterprise Infrastructure SEC | None | No | 7.1 | Local | Low | Low | None | Un- changed | High | High | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91386 | JD Edwards EnterpriseOne Orchestrator | E1 IOT Orchestrator Security | TLS | Yes | 6.8 | Adjacent Network | High | None | None | Un- changed | High | High | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-87320 | JD Edwards EnterpriseOne Tools | E1 Dev Platform Tech - UNIX | None | No | 6.7 | Local | High | Low | Required | Un- changed | High | High | High | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-87383 | JD Edwards EnterpriseOne Tools | Package Build SEC | None | No | 6.7 | Local | Low | High | None | Un- changed | High | High | High | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91383 | JD Edwards EnterpriseOne Tools | Monitoring and Diagnostics SEC | HTTP | No | 6.6 | Network | High | High | None | Changed | High | Low | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91275 | JD Edwards EnterpriseOne Tools | Monitoring and Diagnostics SEC | SQL | No | 6.6 | Network | High | High | None | Changed | High | Low | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-87387 | JD Edwards EnterpriseOne Homebuilder | Homebuilder Management | JDENET | No | 6.5 | Network | Low | Low | None | Un- changed | None | High | None | 9.2 |  | 
| CVE-2026-87382 | JD Edwards EnterpriseOne Operational Sourcing | Operational Sourcing | SMTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 9.2 |  | 
| CVE-2026-91285 | JD Edwards EnterpriseOne Orchestrator | E1 IOT Orchestrator Security | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-87380 | JD Edwards EnterpriseOne Sales Order Entry | Sales Order Entry | JDENET | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 9.2 |  | 
| CVE-2026-91274 | JD Edwards EnterpriseOne Tools | Monitoring and Diagnostics SEC | HTTP | Yes | 6.5 | Network | High | None | None | Un- changed | High | Low | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91284 | JD Edwards EnterpriseOne Tools | E1 Dev Platform Tech - UNIX | JDENET | No | 6.5 | Network | Low | Low | None | Un- changed | None | None | High | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91384 | JD Edwards EnterpriseOne Tools | Web Runtime SEC | JDENET | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-87329 | JD Edwards EnterpriseOne Tools | Enterprise Infrastructure SEC | None | No | 6.5 | Local | High | Low | None | Un- changed | Low | High | High | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91312 | JD Edwards EnterpriseOne Tools | Installation Security | None | No | 6.5 | Local | Low | Low | None | Changed | High | None | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91329 | JD Edwards EnterpriseOne Tools | Installation Security | None | No | 6.5 | Local | High | None | Required | Un- changed | Low | High | High | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-87324 | JD Edwards EnterpriseOne Tools | Enterprise Infrastructure SEC | JDENET | No | 6.4 | Network | High | Low | None | Un- changed | Low | Low | High | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-87325 | JD Edwards EnterpriseOne Tools | Enterprise Infrastructure SEC | JDENET | No | 6.4 | Network | High | Low | None | Un- changed | Low | Low | High | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-87321 | JD Edwards EnterpriseOne Tools | Package Build SEC | None | No | 6.4 | Local | High | High | None | Un- changed | High | High | High | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-87318 | JD Edwards EnterpriseOne Tools | Enterprise Infrastructure SEC | None | No | 6.3 | Local | High | Low | None | Un- changed | High | High | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-87319 | JD Edwards EnterpriseOne Tools | Enterprise Infrastructure SEC | None | No | 6.3 | Local | High | Low | None | Un- changed | High | High | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91281 | JD Edwards EnterpriseOne Tools | Enterprise Infrastructure SEC | HTTP | Yes | 6.1 | Network | Low | None | Required | Changed | Low | Low | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91297 | JD Edwards EnterpriseOne Tools | Monitoring and Diagnostics SEC | HTTP | Yes | 6.1 | Network | Low | None | Required | Changed | Low | Low | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91279 | JD Edwards EnterpriseOne Tools | Web Runtime SEC | HTTP | Yes | 6.1 | Network | Low | None | Required | Changed | Low | Low | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91280 | JD Edwards EnterpriseOne Tools | Web Runtime SEC | HTTP | Yes | 6.1 | Network | Low | None | Required | Changed | Low | Low | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-87326 | JD Edwards EnterpriseOne Tools | Enterprise Infrastructure SEC | HTTP | Yes | 5.9 | Network | High | None | None | Un- changed | High | None | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91282 | JD Edwards EnterpriseOne Tools | Portal SEC | HTTP | Yes | 5.9 | Network | High | None | None | Un- changed | High | None | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91309 | JD Edwards EnterpriseOne Tools | Interoperability SEC | HTTPS | Yes | 5.9 | Network | High | None | None | Un- changed | High | None | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-87328 | JD Edwards EnterpriseOne Tools | Enterprise Infrastructure SEC | JDENET | Yes | 5.9 | Network | High | None | None | Un- changed | High | None | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-87327 | JD Edwards EnterpriseOne Tools | Enterprise Infrastructure SEC | SMTP | Yes | 5.9 | Adjacent Network | High | None | None | Un- changed | High | Low | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2025-53864 | JD Edwards EnterpriseOne Orchestrator | E1 IOT Orchestrator Security (Nimbus JOSE+JWT) | HTTP | Yes | 5.8 | Network | Low | None | None | Changed | None | None | Low | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-87323 | JD Edwards EnterpriseOne Tools | Installation Security | None | No | 5.5 | Local | Low | Low | None | Un- changed | High | None | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91278 | JD Edwards EnterpriseOne Tools | Monitoring and Diagnostics SEC | None | No | 5.5 | Local | Low | Low | None | Un- changed | High | None | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91290 | JD Edwards EnterpriseOne Tools | Web Runtime SEC | None | No | 5.5 | Local | Low | Low | None | Un- changed | High | None | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-87384 | JD Edwards EnterpriseOne Human Resources Management | Human Resources | JDENET | No | 5.4 | Network | Low | Low | None | Un- changed | None | Low | Low | 9.2 |  | 
| CVE-2026-91292 | JD Edwards EnterpriseOne Localizations | LATAM | JDENET | No | 5.4 | Network | Low | Low | None | Un- changed | Low | None | Low | 9.2 |  | 
| CVE-2026-91455 | JD Edwards EnterpriseOne Tools | E1 Dev Platform Tech - UNIX | HTTP | Yes | 5.4 | Network | Low | None | Required | Un- changed | Low | Low | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91298 | JD Edwards EnterpriseOne Tools | Web Runtime SEC | HTTP | No | 5.4 | Network | Low | Low | Required | Changed | Low | Low | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-87381 | JD Edwards EnterpriseOne Tools | Business Logic Infra SEC | JDENET | No | 5.4 | Network | Low | Low | None | Un- changed | Low | Low | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91293 | JD Edwards EnterpriseOne Tools | Business Logic Infra SEC | JDENET | No | 5.4 | Network | Low | Low | None | Un- changed | Low | None | Low | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-87388 | JD Edwards EnterpriseOne Configurator | Configuration Management | HTTP | No | 5.3 | Network | High | Low | None | Un- changed | None | High | None | 9.2 |  | 
| CVE-2026-87386 | JD Edwards EnterpriseOne General Ledger | E1 Foundation | JDENET | No | 5.3 | Network | High | Low | None | Un- changed | None | None | High | 9.2 |  | 
| CVE-2026-91276 | JD Edwards EnterpriseOne Orchestrator | E1 IOT Orchestrator Security | HTTP | Yes | 5.3 | Network | High | None | Required | Un- changed | High | None | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91277 | JD Edwards EnterpriseOne Orchestrator | E1 IOT Orchestrator Security | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | Low | None | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91289 | JD Edwards EnterpriseOne Tools | Monitoring and Diagnostics SEC | TLS | Yes | 5.3 | Adjacent Network | High | None | None | Un- changed | High | None | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-87385 | JD Edwards EnterpriseOne Human Resources Management | Human Resources | JDENET | Yes | 4.8 | Network | High | None | None | Un- changed | Low | Low | None | 9.2 |  | 
| CVE-2025-68161 | JD Edwards EnterpriseOne Tools | Web Runtime SEC (Apache Log4j) | HTTP | Yes | 4.8 | Network | High | None | None | Un- changed | Low | Low | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-87317 | JD Edwards EnterpriseOne Tools | Enterprise Infrastructure SEC | SMTP | Yes | 4.8 | Network | High | None | None | Un- changed | None | Low | Low | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91283 | JD Edwards EnterpriseOne Tools | Web Runtime SEC | HTTP | Yes | 4.3 | Network | Low | None | Required | Un- changed | Low | None | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91294 | JD Edwards EnterpriseOne Tools | Business Logic Infra SEC | JDENET | No | 4.3 | Network | Low | Low | None | Un- changed | None | None | Low | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-87330 | JD Edwards EnterpriseOne Tools | E1 Dev Platform Tech - UNIX | None | No | 4.2 | Local | Low | High | None | Un- changed | Low | Low | Low | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-87389 | JD Edwards EnterpriseOne Human Resources Management | Human Resources | HTTP | Yes | 3.7 | Network | High | None | None | Un- changed | None | Low | None | 9.2 |  | 
| CVE-2026-91291 | JD Edwards EnterpriseOne Tools | Business Logic Infra SEC | None | No | 3.6 | Local | High | Low | None | Un- changed | Low | Low | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-87333 | JD Edwards EnterpriseOne Tools | Enterprise Infrastructure SEC | None | No | 3.6 | Local | High | Low | None | Un- changed | Low | Low | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91301 | JD Edwards EnterpriseOne Tools | Monitoring and Diagnostics SEC | None | No | 3.6 | Local | High | Low | None | Un- changed | None | Low | Low | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-87331 | JD Edwards EnterpriseOne Tools | E1 Dev Platform Tech - UNIX | None | No | 3.4 | Local | Low | High | None | Un- changed | None | Low | Low | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91302 | JD Edwards EnterpriseOne Tools | Enterprise Infrastructure SEC | None | No | 3.3 | Local | Low | None | Required | Un- changed | None | None | Low | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91330 | JD Edwards EnterpriseOne Tools | Installation Security | None | No | 3.3 | Local | Low | Low | None | Un- changed | None | None | Low | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-91300 | JD Edwards EnterpriseOne Tools | Web Runtime SEC | HTTP | Yes | 3.1 | Network | High | None | Required | Un- changed | None | Low | None | 9.2.0.0-9.2.26.5 |  | 
| CVE-2026-87332 | JD Edwards EnterpriseOne Tools | E1 Dev Platform Tech - Cloud | None | No | 3.0 | Local | High | High | None | Un- changed | None | Low | Low | 9.2.0.0-9.2.26.5 |  | 

- The patch for CVE-2025-53864 also addresses CVE-2023-52428.
- The patch for CVE-2025-15467 also addresses CVE-2025-68160, CVE-2025-69418, CVE-2025-69419, CVE-2025-69420, CVE-2025-69421, CVE-2025-9230, CVE-2026-22795, and CVE-2026-22796.

This Critical Patch Update contains 98 new security patches for Oracle MySQL.  29 of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cpuoct2026verbose.html#MSQL)

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-9547 | MySQL Enterprise Backup | Enterprise Backup (curl) | HTTPS | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0 |  | 
| CVE-2025-15467 | MySQL Enterprise Backup | Enterprise Backup (OpenSSL) | TLS | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0 |  | 
| CVE-2026-9547 | MySQL Server, MySQL Cluster | Server: Compiling (curl) | HTTPS | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2025-15467 | MySQL Server, MySQL Cluster | Server: Compiling (OpenSSL) | MySQL Protocol | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101781 | MySQL Server, MySQL Cluster | Server: Group Replication GCS | MySQL Protocol | Yes | 8.8 | Adjacent Network | Low | None | None | Un- changed | High | High | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101785 | MySQL Server, MySQL Cluster | Server: JSON | MySQL Protocol | No | 8.3 | Network | Low | Low | None | Un- changed | Low | High | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101768 | MySQL Connectors | Connector/J | HTTP | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 26.7.0 |  | 
| CVE-2026-101770 | MySQL Server, MySQL Cluster | Client programs | MySQL Protocol | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101771 | MySQL Server, MySQL Cluster | Client programs | MySQL Protocol | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101772 | MySQL Server, MySQL Cluster | Client programs | MySQL Protocol | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-83404 | MySQL Connectors | Connector/Python | MySQL Protocol | Yes | 7.5 | Network | Low | None | None | Un- changed | High | None | None | 26.7.0 |  | 
| CVE-2026-101810 | MySQL Router | Router: General | MySQL Protocol | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 26.7.0 |  | 
| CVE-2026-101679 | MySQL Server, MySQL Cluster | Client programs | MySQL Protocol | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101797 | MySQL Server, MySQL Cluster | Client: mysqldump | MySQL Protocol | Yes | 7.5 | Network | High | None | Required | Un- changed | High | High | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101796 | MySQL Server, MySQL Cluster | Server: Replication | MySQL Protocol | Yes | 7.5 | Network | High | None | Required | Un- changed | High | High | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101783 | MySQL Router | Router: General | HTTPS | Yes | 7.4 | Network | High | None | None | Un- changed | High | High | None | 26.7.0 |  | 
| CVE-2026-101775 | MySQL Server, MySQL Cluster | Server: Replication | MySQL Protocol | Yes | 7.4 | Network | High | None | None | Un- changed | None | High | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101786 | MySQL Server, MySQL Cluster | Server: Optimizer | MySQL Protocol | No | 7.2 | Network | Low | High | None | Un- changed | High | High | High | MySQL Server: 26.7.0-26.7.1; MySQL Cluster: 26.7.0-26.7.1 |  | 
| CVE-2026-101773 | MySQL Server, MySQL Cluster | Server: Group Replication Plugin | MySQL Protocol | Yes | 7.1 | Adjacent Network | Low | None | None | Un- changed | None | Low | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101769 | MySQL Cluster | Cluster: General | TCP | Yes | 7.0 | Network | High | None | None | Un- changed | Low | Low | High | 26.7.0-26.7.1 |  | 
| CVE-2026-101806 | MySQL Connectors | Connector/ODBC | MySQL Protocol | No | 6.8 | Network | High | Low | None | Un- changed | High | High | None | 26.7.1 |  | 
| CVE-2026-101631 | MySQL Router | Router: General | HTTPS | Yes | 6.8 | Network | High | None | Required | Un- changed | High | High | None | 26.7.0 |  | 
| CVE-2026-101800 | MySQL Server, MySQL Cluster | Server: Security: Privileges | MySQL Protocol | No | 6.8 | Network | High | Low | None | Un- changed | High | High | None | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101795 | MySQL Server, MySQL Cluster | Server: Components Services | MySQL Protocol | No | 6.7 | Local | Low | High | None | Un- changed | High | High | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101628 | MySQL Cluster | Cluster: NDB Operator | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | None | None | High | 9.7.3 |  | 
| CVE-2026-101725 | MySQL Server, MySQL Cluster | C API | MySQL Protocol | No | 6.5 | Network | Low | Low | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101726 | MySQL Server, MySQL Cluster | C API | MySQL Protocol | No | 6.5 | Network | Low | Low | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101747 | MySQL Server, MySQL Cluster | InnoDB | MySQL Protocol | No | 6.5 | Network | Low | Low | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101778 | MySQL Server, MySQL Cluster | Server: Components Services | MySQL Protocol | No | 6.5 | Network | Low | Low | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101743 | MySQL Server, MySQL Cluster | Server: GIS | MySQL Protocol | No | 6.5 | Network | Low | Low | None | Un- changed | None | None | High | MySQL Server: 26.7.0-26.7.1; MySQL Cluster: 26.7.0-26.7.1 |  | 
| CVE-2026-101799 | MySQL Server, MySQL Cluster | Server: Group Replication GCS | MySQL Protocol | Yes | 6.5 | Adjacent Network | Low | None | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101616 | MySQL Server, MySQL Cluster | Server: JSON | MySQL Protocol | No | 6.5 | Network | Low | Low | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101733 | MySQL Server, MySQL Cluster | Server: JSON | MySQL Protocol | No | 6.5 | Network | Low | Low | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101608 | MySQL Server, MySQL Cluster | Server: Optimizer | MySQL Protocol | No | 6.5 | Network | Low | Low | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101620 | MySQL Server, MySQL Cluster | Server: Optimizer | MySQL Protocol | No | 6.5 | Network | Low | Low | None | Un- changed | None | None | High | MySQL Server: 9.7.0-9.7.3; MySQL Cluster: 9.7.0-9.7.3 |  | 
| CVE-2026-101789 | MySQL Server, MySQL Cluster | Server: Optimizer | MySQL Protocol | No | 6.5 | Network | Low | Low | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101802 | MySQL Server, MySQL Cluster | Server: Parser | MySQL Protocol | No | 6.5 | Network | Low | Low | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101728 | MySQL Server, MySQL Cluster | Server: Pluggable Auth | MySQL Protocol | No | 6.5 | Network | Low | Low | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101774 | MySQL Server, MySQL Cluster | Server: Pluggable Auth | MySQL Protocol | Yes | 6.5 | Network | High | None | None | Un- changed | None | Low | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101748 | MySQL Server, MySQL Cluster | Server: Security: Audit | MySQL Protocol | No | 6.5 | Network | Low | Low | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101780 | MySQL Server, MySQL Cluster | Server: X Plugin | MySQL Protocol | No | 6.5 | Network | Low | Low | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101794 | MySQL Server, MySQL Cluster | Server: XML | MySQL Protocol | No | 6.5 | Network | Low | Low | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101803 | MySQL Server, MySQL Cluster | Server: XML | MySQL Protocol | No | 6.5 | Network | Low | High | None | Un- changed | None | High | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101626 | MySQL Connectors | Connector/Net | MySQL Protocol | Yes | 5.9 | Network | High | None | None | Un- changed | High | None | None | 26.7.0 |  | 
| CVE-2026-101788 | MySQL Server, MySQL Cluster | Server: Components Services | MySQL Protocol | Yes | 5.9 | Network | High | None | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101761 | MySQL Server, MySQL Cluster | Server: Security: Encryption | MySQL Protocol | Yes | 5.9 | Network | High | None | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101637 | MySQL Server, MySQL Cluster | InnoDB | MySQL Protocol | No | 5.5 | Network | Low | High | None | Un- changed | None | Low | High | MySQL Server: 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101777 | MySQL Server, MySQL Cluster | Server: Security: Encryption | MySQL Protocol | No | 5.5 | Network | Low | High | None | Un- changed | Low | None | High | MySQL Server: 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101755 | MySQL Server, MySQL Cluster | Client programs | MySQL Protocol | No | 5.3 | Network | High | Low | None | Un- changed | None | None | High | MySQL Server: 26.7.0-26.7.1; MySQL Cluster: 26.7.0-26.7.1 |  | 
| CVE-2026-101720 | MySQL Server, MySQL Cluster | Server: Connection Handling | MySQL Protocol | Yes | 5.3 | Network | Low | None | None | Un- changed | None | Low | None | MySQL Server: 26.7.0-26.7.1; MySQL Cluster: 26.7.0-26.7.1 |  | 
| CVE-2026-101762 | MySQL Server, MySQL Cluster | Server: Security: Encryption | MySQL Protocol | No | 5.3 | Network | High | Low | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101614 | MySQL Server, MySQL Cluster | InnoDB | MySQL Protocol | No | 4.9 | Network | Low | High | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101617 | MySQL Server, MySQL Cluster | InnoDB | MySQL Protocol | No | 4.9 | Network | Low | High | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101618 | MySQL Server, MySQL Cluster | InnoDB | MySQL Protocol | No | 4.9 | Network | Low | High | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101619 | MySQL Server, MySQL Cluster | InnoDB | MySQL Protocol | No | 4.9 | Network | Low | High | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101621 | MySQL Server, MySQL Cluster | InnoDB | MySQL Protocol | No | 4.9 | Network | Low | High | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101622 | MySQL Server, MySQL Cluster | InnoDB | MySQL Protocol | No | 4.9 | Network | Low | High | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101624 | MySQL Server, MySQL Cluster | InnoDB | MySQL Protocol | No | 4.9 | Network | Low | High | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101629 | MySQL Server, MySQL Cluster | InnoDB | MySQL Protocol | No | 4.9 | Network | Low | High | None | Un- changed | None | None | High | MySQL Server: 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101724 | MySQL Server, MySQL Cluster | InnoDB | MySQL Protocol | No | 4.9 | Network | Low | High | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101760 | MySQL Server, MySQL Cluster | InnoDB | MySQL Protocol | No | 4.9 | Network | Low | High | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101750 | MySQL Server, MySQL Cluster | Server: Clone Plugin | MySQL Protocol | No | 4.9 | Network | Low | High | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101721 | MySQL Server, MySQL Cluster | Server: Components Services | MySQL Protocol | No | 4.9 | Network | Low | High | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101613 | MySQL Server, MySQL Cluster | Server: DDL | MySQL Protocol | No | 4.9 | Network | Low | High | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101756 | MySQL Server, MySQL Cluster | Server: GIS | MySQL Protocol | No | 4.9 | Network | Low | High | None | Un- changed | None | None | High | MySQL Server: 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101751 | MySQL Server, MySQL Cluster | Server: Group Replication GCS | MySQL Protocol | No | 4.9 | Network | Low | High | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101776 | MySQL Server, MySQL Cluster | Server: Group Replication Plugin | MySQL Protocol | No | 4.9 | Network | Low | High | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101607 | MySQL Server, MySQL Cluster | Server: Optimizer | MySQL Protocol | No | 4.9 | Network | Low | High | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101610 | MySQL Server, MySQL Cluster | Server: Optimizer | MySQL Protocol | No | 4.9 | Network | Low | High | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101623 | MySQL Server, MySQL Cluster | Server: Optimizer | MySQL Protocol | No | 4.9 | Network | Low | High | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101730 | MySQL Server, MySQL Cluster | Server: Optimizer | MySQL Protocol | No | 4.9 | Network | Low | High | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101731 | MySQL Server, MySQL Cluster | Server: Optimizer | MySQL Protocol | No | 4.9 | Network | Low | High | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101732 | MySQL Server, MySQL Cluster | Server: Optimizer | MySQL Protocol | No | 4.9 | Network | Low | High | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101784 | MySQL Server, MySQL Cluster | Server: Optimizer | MySQL Protocol | No | 4.9 | Network | Low | High | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101787 | MySQL Server, MySQL Cluster | Server: Optimizer | MySQL Protocol | No | 4.9 | Network | Low | High | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101798 | MySQL Server, MySQL Cluster | Server: Optimizer | MySQL Protocol | No | 4.9 | Network | Low | High | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101801 | MySQL Server, MySQL Cluster | Server: Optimizer | MySQL Protocol | No | 4.9 | Network | Low | High | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101727 | MySQL Server, MySQL Cluster | Server: Replication | MySQL Protocol | No | 4.9 | Network | Low | High | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101729 | MySQL Server, MySQL Cluster | Server: Replication | MySQL Protocol | No | 4.9 | Network | Low | High | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101749 | MySQL Server, MySQL Cluster | Server: Security: Encryption | MySQL Protocol | No | 4.9 | Network | Low | High | None | Un- changed | None | None | High | MySQL Server: 26.7.0-26.7.1; MySQL Cluster: 26.7.0-26.7.1 |  | 
| CVE-2026-101754 | MySQL Server, MySQL Cluster | Client programs | MySQL Protocol | No | 4.4 | Network | High | High | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101609 | MySQL Server, MySQL Cluster | InnoDB | MySQL Protocol | No | 4.4 | Network | High | High | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101611 | MySQL Server, MySQL Cluster | InnoDB | MySQL Protocol | No | 4.4 | Network | High | High | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101615 | MySQL Server, MySQL Cluster | InnoDB | MySQL Protocol | No | 4.4 | Local | Low | High | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101627 | MySQL Server, MySQL Cluster | InnoDB | MySQL Protocol | No | 4.4 | Network | High | High | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101752 | MySQL Server, MySQL Cluster | Server: Components Services | MySQL Protocol | No | 4.4 | Network | High | High | None | Un- changed | None | None | High | MySQL Server: 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101753 | MySQL Server, MySQL Cluster | Server: RAPID | MySQL Protocol | No | 4.4 | Network | High | High | None | Un- changed | None | None | High | MySQL Server: 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101766 | MySQL Server, MySQL Cluster | Server: Replication | MySQL Protocol | No | 4.4 | Network | High | High | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101677 | MySQL Connectors | Connector/J | MySQL Protocol | Yes | 4.3 | Network | Low | None | Required | Un- changed | None | Low | None | 26.7.0 |  | 
| CVE-2026-101678 | MySQL Connectors | Connector/J | MySQL Protocol | Yes | 4.3 | Network | Low | None | Required | Un- changed | None | None | Low | 26.7.0 |  | 
| CVE-2026-101625 | MySQL Connectors | Connector/Net | MySQL Protocol | Yes | 4.3 | Network | Low | None | Required | Un- changed | Low | None | None | 26.7.0 |  | 
| CVE-2026-101632 | MySQL Router | Router: General | HTTPS | Yes | 4.3 | Network | Low | None | Required | Un- changed | Low | None | None | 26.7.0 |  | 
| CVE-2026-101633 | MySQL Router | Router: General | HTTPS | No | 4.3 | Network | Low | Low | None | Un- changed | Low | None | None | 26.7.0 |  | 
| CVE-2026-101722 | MySQL Server, MySQL Cluster | Server: Connection Handling | MySQL Protocol | No | 4.3 | Network | Low | Low | None | Un- changed | Low | None | None | MySQL Server: 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101612 | MySQL Server, MySQL Cluster | InnoDB | None | No | 4.0 | Local | High | High | Required | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.0.0-8.0.49, 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101513 | MySQL Cluster | InnoDB | None | No | 3.8 | Physical | High | High | None | Un- changed | None | None | High | 8.0.0-8.0.37 |  | 
| CVE-2026-101779 | MySQL Server, MySQL Cluster | Server: Telemetry | MySQL Protocol | No | 2.7 | Network | Low | High | None | Un- changed | None | None | Low | MySQL Server: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1; MySQL Cluster: 8.4.0-8.4.12, 9.7.0-9.7.3, 26.7.0-26.7.1 |  | 
| CVE-2026-101804 | MySQL Connectors | Connector/ODBC | None | No | 2.5 | Local | High | None | Required | Un- changed | None | None | Low | 26.7.1 |  | 

- The patch for CVE-2026-9547 also addresses CVE-2025-10148, CVE-2025-10966, CVE-2025-13034, CVE-2025-14017, CVE-2025-14524, CVE-2025-14819, CVE-2025-15079, CVE-2025-15224, CVE-2025-9086, CVE-2026-10536, CVE-2026-11856, CVE-2026-12064, CVE-2026-13608, CVE-2026-18924, CVE-2026-1965, CVE-2026-19931, CVE-2026-3783, CVE-2026-3784, CVE-2026-3805, CVE-2026-4873, CVE-2026-5545, CVE-2026-5773, CVE-2026-6253, CVE-2026-6276, CVE-2026-6429, CVE-2026-7168, CVE-2026-8286, CVE-2026-8458, CVE-2026-8924, CVE-2026-8926, CVE-2026-8927, CVE-2026-8932, CVE-2026-9079, CVE-2026-9080, and CVE-2026-9545.
- The patch for CVE-2025-15467 also addresses CVE-2025-68160, CVE-2025-69418, CVE-2025-69419, CVE-2025-69420, CVE-2025-69421, CVE-2025-9230, CVE-2025-9232, CVE-2026-22795, CVE-2026-22796, CVE-2026-28387, CVE-2026-28388, CVE-2026-28389, CVE-2026-28390, CVE-2026-31790, CVE-2026-34180, CVE-2026-34182, CVE-2026-42766, CVE-2026-42767, CVE-2026-42770, CVE-2026-45445, CVE-2026-45446, CVE-2026-45447, CVE-2026-54874, CVE-2026-63072, CVE-2026-63074, CVE-2026-63076, CVE-2026-7383, CVE-2026-75803, and CVE-2026-9076.

This Critical Patch Update contains 109 new security patches, plus additional third party patches noted below, for Oracle PeopleSoft.  41 of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cpuoct2026verbose.html#PS)

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-33466 | PeopleSoft Enterprise PeopleTools | Logstash (Logstash) | HTTP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 8.61-8.63 |  | 
| CVE-2026-101420 | PeopleSoft Enterprise PeopleTools | SQR | HTTP | No | 9.6 | Network | Low | Low | None | Changed | High | High | None | 8.61-8.63 |  | 
| CVE-2026-91478 | PeopleSoft Enterprise SCM Strategic Sourcing | Strategic Sourcing | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 9.2 |  | 
| CVE-2026-101431 | PeopleSoft Enterprise PeopleTools | Test Framework | HTTP | No | 8.7 | Network | Low | Low | Required | Changed | High | High | None | 8.61-8.63 |  | 
| CVE-2026-55200 | PeopleSoft Enterprise PeopleTools | File Processing (libssh2) | HTTP | Yes | 8.3 | Network | Low | None | Required | Un- changed | High | High | Low | 8.61-8.63 |  | 
| CVE-2026-101390 | PeopleSoft Enterprise PeopleTools | Business Interlink | HTTP | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 8.61-8.63 |  | 
| CVE-2026-101411 | PeopleSoft Enterprise PeopleTools | Business Interlink | HTTP | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 8.61-8.63 |  | 
| CVE-2026-101422 | PeopleSoft Enterprise PeopleTools | Report Distribution | HTTP | No | 8.1 | Network | Low | Low | None | Un- changed | None | High | High | 8.61-8.63 |  | 
| CVE-2026-101427 | PeopleSoft Enterprise PeopleTools | Report Distribution | HTTP | Yes | 8.1 | Network | Low | None | Required | Un- changed | None | High | High | 8.61-8.63 |  | 
| CVE-2026-101434 | PeopleSoft Enterprise PeopleTools | Database Server | HTTP | Yes | 7.6 | Network | Low | None | Required | Un- changed | Low | Low | High | 8.61-8.63 |  | 
| CVE-2026-91465 | PeopleSoft Enterprise FIN Common Objects Argentina | Integration | Oracle Net | Yes | 7.5 | Network | Low | None | None | Un- changed | High | None | None | 9.1 |  | 
| CVE-2026-101410 | PeopleSoft Enterprise PeopleTools | Business Interlink | HTTP | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 8.61-8.63 |  | 
| CVE-2026-101409 | PeopleSoft Enterprise PeopleTools | Report Distribution | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | High | None | None | 8.61-8.63 |  | 
| CVE-2026-101421 | PeopleSoft Enterprise PeopleTools | SQR | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | High | None | None | 8.61-8.63 |  | 
| CVE-2026-101428 | PeopleSoft Enterprise PeopleTools | SQR | HTTP | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 8.61-8.63 |  | 
| CVE-2026-9563 | PeopleSoft Enterprise PeopleTools | Security (Eclipse Parsson) | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 8.61-8.63 |  | 
| CVE-2026-9076 | PeopleSoft Enterprise PeopleTools | Security (OpenSSL) | HTTPS | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 8.61-8.63 |  | 
| CVE-2026-101416 | PeopleSoft Enterprise PeopleTools | PsAdmin | RMI | Yes | 7.5 | Adjacent Network | High | None | None | Un- changed | High | High | High | 8.61-8.63 |  | 
| CVE-2026-101450 | PeopleSoft Enterprise PeopleTools | Integration Broker | HTTP | Yes | 7.1 | Network | Low | None | Required | Un- changed | High | Low | None | 8.61-8.63 |  | 
| CVE-2026-101388 | PeopleSoft Enterprise PeopleTools | Portal | HTTP | No | 7.1 | Network | Low | Low | None | Un- changed | High | None | Low | 8.61-8.63 |  | 
| CVE-2026-101429 | PeopleSoft Enterprise PeopleTools | SQR | None | No | 7.0 | Local | High | None | Required | Un- changed | High | High | High | 8.61-8.63 |  | 
| CVE-2026-101426 | PeopleSoft Enterprise PeopleTools | SQR | None | No | 6.9 | Local | High | High | Required | Changed | None | High | High | 8.61-8.63 |  | 
| CVE-2026-60869 | PeopleSoft Enterprise PeopleTools | Application Data Sets | HTTP | No | 6.8 | Network | High | Low | None | Un- changed | None | High | High | 8.61-8.63 |  | 
| CVE-2026-60885 | PeopleSoft Enterprise PeopleTools | Push Notifications | HTTP | No | 6.8 | Adjacent Network | Low | High | None | Un- changed | High | High | High | 8.61, 8.62 |  | 
| CVE-2026-87410 | PeopleSoft Enterprise PeopleTools | Report Distribution | HTTP | Yes | 6.8 | Network | High | None | None | Changed | High | None | None | 8.61-8.63 |  | 
| CVE-2026-83427 | PeopleSoft Enterprise PeopleTools | Multichannel Framework | HTTP | No | 6.6 | Network | High | High | None | Un- changed | High | High | High | 8.61-8.63 |  | 
| CVE-2026-101435 | PeopleSoft Enterprise PeopleTools | Porting | None | No | 6.6 | Local | Low | Low | None | Un- changed | Low | Low | High | 8.61-8.63 |  | 
| CVE-2026-91541 | PeopleSoft Enterprise FIN Common Objects Brazil | Common Objects | HTTP | Yes | 6.5 | Network | Low | None | None | Un- changed | None | Low | Low | 9.1 |  | 
| CVE-2026-101488 | PeopleSoft Enterprise PeopleTools | Business Interlink | HTTP | Yes | 6.5 | Network | Low | None | None | Un- changed | Low | None | Low | 8.61-8.63 |  | 
| CVE-2026-87344 | PeopleSoft Enterprise PeopleTools | LDAP | HTTP | Yes | 6.5 | Network | Low | None | None | Un- changed | Low | Low | None | 8.61-8.63 |  | 
| CVE-2026-60881 | PeopleSoft Enterprise PeopleTools | Meta Data | HTTP | No | 6.5 | Network | Low | High | None | Un- changed | High | None | High | 8.61-8.63 |  | 
| CVE-2026-91468 | PeopleSoft Enterprise PeopleTools | QAS | HTTP | Yes | 6.5 | Network | Low | None | None | Un- changed | None | Low | Low | 8.61-8.63 |  | 
| CVE-2026-101418 | PeopleSoft Enterprise PeopleTools | Report Distribution | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 8.61-8.63 |  | 
| CVE-2026-91519 | PeopleSoft Enterprise PeopleTools | Report Distribution | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 8.61-8.63 |  | 
| CVE-2026-101419 | PeopleSoft Enterprise PeopleTools | SQR | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 8.61-8.63 |  | 
| CVE-2026-87342 | PeopleSoft Enterprise PeopleTools | Security | HTTP | Yes | 6.5 | Network | High | None | None | Un- changed | High | Low | None | 8.61-8.63 |  | 
| CVE-2026-87409 | PeopleSoft Enterprise PeopleTools | nVision | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 8.61-8.63 |  | 
| CVE-2026-87349 | PeopleSoft Enterprise PeopleTools | Security | None | No | 6.5 | Local | Low | High | Required | Un- changed | High | High | High | 8.61-8.63 |  | 
| CVE-2026-60743 | PeopleSoft Enterprise PeopleTools | Weblogic | TLS | Yes | 6.5 | Network | High | None | None | Un- changed | High | Low | None | 8.61-8.63 |  | 
| CVE-2026-91482 | PeopleSoft Enterprise SCM Strategic Sourcing | Bidder Registration | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 9.2 |  | 
| CVE-2026-91480 | PeopleSoft Enterprise SCM Strategic Sourcing | Strategic Sourcing | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 9.2 |  | 
| CVE-2026-91466 | PeopleSoft Enterprise FIN Common Objects Argentina | Asset Management | HTTP | No | 6.4 | Network | Low | High | Required | Un- changed | High | High | Low | 9.1 |  | 
| CVE-2026-101430 | PeopleSoft Enterprise PeopleTools | Test Framework | None | No | 6.2 | Local | Low | None | None | Un- changed | High | None | None | 8.61-8.63 |  | 
| CVE-2026-91474 | PeopleSoft Enterprise FIN Common Objects Brazil | eProcurement | HTTPS | No | 6.1 | Adjacent Network | Low | High | None | Un- changed | High | High | None | 9.1 |  | 
| CVE-2026-87345 | PeopleSoft Enterprise PeopleTools | Business Interlink | HTTP | Yes | 6.1 | Network | Low | None | Required | Changed | Low | Low | None | 8.61-8.63 |  | 
| CVE-2026-101490 | PeopleSoft Enterprise PeopleTools | Fluid Core | HTTP | Yes | 6.1 | Network | Low | None | Required | Changed | Low | Low | None | 8.61-8.63 |  | 
| CVE-2026-83375 | PeopleSoft Enterprise HCM Human Resources | Administer Workforce | HTTP | No | 6.0 | Network | High | High | Required | Un- changed | Low | High | High | 9.2 |  | 
| CVE-2026-91505 | PeopleSoft Enterprise PeopleTools | Porting | None | No | 6.0 | Local | Low | High | None | Un- changed | High | High | None | 8.61,8.62 |  | 
| CVE-2026-60968 | PeopleSoft Enterprise PeopleTools | Updates Environment Mgmt | None | No | 6.0 | Local | Low | High | None | Un- changed | None | High | High | 8.61-8.63 |  | 
| CVE-2026-70860 | PeopleSoft Enterprise FIN Common Objects Argentina | eProcurement | HTTP | No | 5.9 | Network | High | Low | None | Un- changed | Low | High | None | 9.1 |  | 
| CVE-2026-101389 | PeopleSoft Enterprise PeopleTools | Business Interlink | HTTP | Yes | 5.9 | Network | High | None | None | Un- changed | None | None | High | 8.61-8.63 |  | 
| CVE-2026-101424 | PeopleSoft Enterprise PeopleTools | Report Distribution | HTTP | No | 5.8 | Network | High | High | None | Changed | High | None | None | 8.61-8.63 |  | 
| CVE-2026-60500 | PeopleSoft Enterprise PeopleTools | Web Server | HTTP | Yes | 5.8 | Network | Low | None | None | Changed | Low | None | None | 8.61-8.63 |  | 
| CVE-2026-101412 | PeopleSoft Enterprise PeopleTools | Analytic Server | None | No | 5.8 | Local | High | Low | None | Un- changed | Low | High | Low | 8.61-8.63 |  | 
| CVE-2026-60839 | PeopleSoft Enterprise PeopleTools | Query | HTTP | No | 5.5 | Network | High | High | None | Un- changed | Low | Low | High | 8.61, 8.62 |  | 
| CVE-2026-101407 | PeopleSoft Enterprise PeopleTools | Updates Change Assistant | HTTP | No | 5.5 | Network | Low | High | None | Un- changed | High | None | Low | 8.61-8.63 |  | 
| CVE-2026-101486 | PeopleSoft Enterprise PeopleTools | Fluid Core | HTTP | No | 5.4 | Network | Low | Low | Required | Changed | Low | Low | None | 8.61-8.63 |  | 
| CVE-2026-83372 | PeopleSoft Enterprise PeopleTools | Portal | HTTP | No | 5.4 | Network | Low | Low | Required | Changed | Low | Low | None | 8.61-8.63 |  | 
| CVE-2026-101487 | PeopleSoft Enterprise PeopleTools | Portal | HTTP | No | 5.4 | Network | Low | Low | Required | Changed | Low | Low | None | 8.61-8.63 |  | 
| CVE-2026-91481 | PeopleSoft Enterprise SCM Purchasing | Supplier Registration | HTTP | No | 5.4 | Network | Low | Low | Required | Changed | Low | Low | None | 9.2 |  | 
| CVE-2026-91476 | PeopleSoft Enterprise FIN Common Objects Brazil | eProcurement | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | Low | None | None | 9.1 |  | 
| CVE-2026-101413 | PeopleSoft Enterprise PeopleTools | Analytic Server | HTTP | No | 5.3 | Network | High | Low | None | Un- changed | None | None | High | 8.61-8.63 |  | 
| CVE-2026-87336 | PeopleSoft Enterprise PeopleTools | Portal | HTTP | No | 5.3 | Network | High | Low | None | Un- changed | High | None | None | 8.61-8.63 |  | 
| CVE-2026-87415 | PeopleSoft Enterprise PeopleTools | Report Distribution | HTTP | Yes | 5.3 | Network | High | None | Required | Un- changed | High | None | None | 8.61-8.63 |  | 
| CVE-2026-101433 | PeopleSoft Enterprise PeopleTools | Test Framework | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | Low | None | None | 8.61-8.63 |  | 
| CVE-2026-91497 | PeopleSoft Enterprise PeopleTools | Updates Environment Mgmt | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | None | Low | None | 8.61-8.63 |  | 
| CVE-2026-60882 | PeopleSoft Enterprise PeopleTools | Search Framework | HTTPS | Yes | 5.3 | Adjacent Network | High | None | None | Un- changed | High | None | None | 8.61, 8.62 |  | 
| CVE-2026-12816 | PeopleSoft Enterprise PeopleTools | Security (Bouncy Castle Java Library) | HTTPS | Yes | 5.3 | Network | Low | None | None | Un- changed | None | Low | None | 8.61-8.63 |  | 
| CVE-2026-101432 | PeopleSoft Enterprise PeopleTools | Test Framework | None | No | 5.3 | Local | Low | Low | None | Un- changed | Low | Low | Low | 8.61-8.63 |  | 
| CVE-2026-101491 | PeopleSoft Enterprise PeopleTools | Query | HTTP | No | 5.0 | Network | Low | Low | None | Changed | Low | None | None | 8.61-8.63 |  | 
| CVE-2026-91263 | PeopleSoft Enterprise PeopleTools | Notification Configuration | HTTP | No | 4.9 | Network | High | Low | None | Changed | Low | Low | None | 8.61-8.63 |  | 
| CVE-2026-87343 | PeopleSoft Enterprise PeopleTools | Portal | HTTP | Yes | 4.8 | Network | High | None | None | Un- changed | Low | Low | None | 8.61-8.63 |  | 
| CVE-2026-70869 | PeopleSoft Enterprise PeopleTools | Integration Broker | HTTP | Yes | 4.7 | Network | High | None | Required | Changed | Low | Low | None | 8.61-8.63 |  | 
| CVE-2026-87353 | PeopleSoft Enterprise PeopleTools | Porting | None | No | 4.5 | Local | High | None | Required | Un- changed | Low | Low | Low | 8.61-8.63 |  | 
| CVE-2026-87350 | PeopleSoft Enterprise PeopleTools | Security | None | No | 4.5 | Local | High | Low | None | Un- changed | Low | Low | Low | 8.61-8.63 |  | 
| CVE-2026-91486 | PeopleSoft Enterprise FIN General Ledger Brazil | General Ledger | None | No | 4.4 | Local | Low | Low | None | Un- changed | None | Low | Low | 9.1 |  | 
| CVE-2026-91562 | PeopleSoft Enterprise FIN Inventory Brazil | Inventory | None | No | 4.4 | Local | Low | Low | None | Un- changed | None | Low | Low | 9.1 |  | 
| CVE-2026-91559 | PeopleSoft Enterprise FIN Manufacturing Brazil | Integration | None | No | 4.4 | Local | Low | Low | None | Un- changed | None | Low | Low | 9.1 |  | 
| CVE-2026-91553 | PeopleSoft Enterprise FIN Product Configurator Brazil | Product Configurator | None | No | 4.4 | Local | Low | Low | None | Un- changed | None | Low | Low | 9.1 |  | 
| CVE-2026-87355 | PeopleSoft Enterprise PeopleTools | Panel Processor | HTTP | No | 4.4 | Network | High | Low | Required | Changed | Low | Low | None | 8.61-8.63 |  | 
| CVE-2026-60878 | PeopleSoft Enterprise PeopleTools | Process Scheduler | HTTP | No | 4.4 | Network | High | Low | Required | Changed | Low | Low | None | 8.61, 8.62 |  | 
| CVE-2026-60745 | PeopleSoft Enterprise PeopleTools | Application Server - JRE | None | No | 4.4 | Local | Low | High | None | Un- changed | High | None | None | 8.61-8.63 |  | 
| CVE-2026-87352 | PeopleSoft Enterprise PeopleTools | LDAP | None | No | 4.4 | Local | Low | Low | None | Un- changed | Low | Low | None | 8.61-8.63 |  | 
| CVE-2026-101489 | PeopleSoft Enterprise PeopleTools | Portal | HTTP | No | 4.3 | Network | Low | Low | None | Un- changed | Low | None | None | 8.61-8.63 |  | 
| CVE-2026-101423 | PeopleSoft Enterprise PeopleTools | Report Distribution | HTTP | No | 4.3 | Network | Low | Low | None | Un- changed | Low | None | None | 8.61-8.63 |  | 
| CVE-2026-91356 | PeopleSoft Enterprise HCM Global Payroll Switzerland | Global Payroll for Switzerland | None | No | 4.2 | Local | Low | High | None | Un- changed | Low | Low | Low | 9.2 |  | 
| CVE-2026-60874 | PeopleSoft Enterprise PeopleTools | Portal | HTTP | No | 4.2 | Network | High | Low | None | Un- changed | Low | None | Low | 8.61, 8.62 |  | 
| CVE-2026-60876 | PeopleSoft Enterprise PeopleTools | Search Framework | HTTP | Yes | 4.2 | Network | High | None | Required | Un- changed | Low | Low | None | 8.62 |  | 
| CVE-2026-60809 | PeopleSoft Enterprise PeopleTools | Weblogic | HTTPS | Yes | 4.2 | Adjacent Network | High | None | None | Un- changed | Low | Low | None | 8.61-8.63 |  | 
| CVE-2026-87348 | PeopleSoft Enterprise PeopleTools | Updates Environment Mgmt | None | No | 4.2 | Local | Low | High | None | Un- changed | Low | Low | Low | 8.61-8.63 |  | 
| CVE-2026-60814 | PeopleSoft Enterprise PeopleTools | Business Interlink | None | No | 3.9 | Local | High | High | None | Un- changed | Low | Low | Low | 8.61-8.63 |  | 
| CVE-2026-91331 | PeopleSoft Enterprise CC Common Application Objects | Common Application Objects | HTTP | No | 3.8 | Network | Low | High | None | Un- changed | Low | Low | None | 9.2 |  | 
| CVE-2026-91485 | PeopleSoft Enterprise FIN Cash Management | Cash Management | None | No | 3.8 | Local | High | High | Required | Un- changed | Low | Low | Low | 9.2 |  | 
| CVE-2026-60887 | PeopleSoft Enterprise PeopleTools | Data Mover | None | No | 3.8 | Local | High | High | Required | Un- changed | Low | Low | Low | 8.61-8.63 |  | 
| CVE-2026-91471 | PeopleSoft Enterprise CC Common Application Objects | BAM Framework | HTTP | Yes | 3.7 | Network | High | None | None | Un- changed | None | Low | None | 9.2 |  | 
| CVE-2026-87340 | PeopleSoft Enterprise PeopleTools | Portal | HTTP | Yes | 3.7 | Network | High | None | None | Un- changed | None | Low | None | 8.61-8.63 |  | 
| CVE-2026-87416 | PeopleSoft Enterprise PeopleTools | Report Distribution | HTTP | Yes | 3.7 | Network | High | None | None | Un- changed | Low | None | None | 8.61-8.63 |  | 
| CVE-2026-101417 | PeopleSoft Enterprise PeopleTools | Tuxedo | HTTP | Yes | 3.7 | Network | High | None | None | Un- changed | Low | None | None | 8.61-8.63 |  | 
| CVE-2026-60819 | PeopleSoft Enterprise PeopleTools | Application Server - JRE | SSH | Yes | 3.7 | Network | High | None | None | Un- changed | None | Low | None | 8.61-8.63 |  | 
| CVE-2026-91264 | PeopleSoft Enterprise SCM Manufacturing | Security | HTTP | Yes | 3.7 | Network | High | None | None | Un- changed | None | Low | None | 9.2 |  | 
| CVE-2026-87401 | PeopleSoft Enterprise PeopleTools | XML Publisher | None | No | 3.3 | Local | Low | Low | None | Un- changed | Low | None | None | 8.61-8.63 |  | 
| CVE-2026-101415 | PeopleSoft Enterprise PeopleTools | Analytic Server | HTTP | No | 3.1 | Network | High | Low | None | Un- changed | None | None | Low | 8.61-8.63 |  | 
| CVE-2024-20925 | PeopleSoft Enterprise PeopleTools | Updates Change Assistant | HTTP | Yes | 3.1 | Network | High | None | Required | Un- changed | None | Low | None | 8.61 |  | 
| CVE-2026-83373 | PeopleSoft Enterprise PeopleTools | Portal | HTTP | No | 3.0 | Network | High | Low | Required | Changed | Low | None | None | 8.61-8.63 |  | 
| CVE-2026-101414 | PeopleSoft Enterprise PeopleTools | Porting | None | No | 2.9 | Local | High | None | None | Un- changed | None | Low | None | 8.61-8.63 |  | 
| CVE-2026-87412 | PeopleSoft Enterprise PeopleTools | Report Distribution | HTTP | No | 2.7 | Network | Low | High | None | Un- changed | Low | None | None | 8.61-8.63 |  | 
| CVE-2026-101425 | PeopleSoft Enterprise PeopleTools | SQR | None | No | 2.5 | Local | High | Low | None | Un- changed | Low | None | None | 8.61-8.63 |  | 
| CVE-2026-87418 | PeopleSoft Enterprise PeopleTools | Updates Environment Mgmt | None | No | 2.5 | Local | High | Low | None | Un- changed | Low | None | None | 8.61-8.63 |  | 
| CVE-2026-60964 | PeopleSoft Enterprise PeopleTools | Open Query | None | No | 1.9 | Local | High | High | None | Un- changed | Low | None | None | 8.61, 8.62 |  | 

- The patch for CVE-2026-33466 also addresses CVE-2024-12798, CVE-2025-43857, CVE-2025-61772, CVE-2025-61780, CVE-2025-61919, CVE-2026-22860, CVE-2026-25500, CVE-2026-26961, CVE-2026-32762, CVE-2026-34230, CVE-2026-34763, CVE-2026-34785, CVE-2026-34786, CVE-2026-34826, CVE-2026-34827, CVE-2026-34829, CVE-2026-34830, CVE-2026-34831, CVE-2026-34835, CVE-2026-42257, CVE-2026-57234, CVE-2026-57235, CVE-2026-57236, CVE-2026-57435, CVE-2026-57436, CVE-2026-57437, CVE-2026-57438, CVE-2026-79769, CVE-2026-79770, CVE-2026-79771, and CVE-2026-79772.
- The patch for CVE-2026-55200 also addresses CVE-2025-15661, CVE-2026-55199, CVE-2026-58050, CVE-2026-58051, and CVE-2026-7598.
- The patch for CVE-2026-9076 also addresses CVE-2026-34180, CVE-2026-34181, CVE-2026-34182, CVE-2026-34183, CVE-2026-42764, CVE-2026-42766, CVE-2026-42767, CVE-2026-42768, CVE-2026-42769, CVE-2026-42770, CVE-2026-45445, CVE-2026-45446, CVE-2026-45447, and CVE-2026-7383.

- PeopleSoft Enterprise PeopleTools
  - PUM Automated Updates: CVE-2026-87341.
  - SQR: CVE-2026-87405.

This Critical Patch Update contains 5 new security patches for Oracle Retail Applications.  All of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cpuoct2026verbose.html#RAPP)

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-41855 | Oracle Retail Predictive Application Server | RPAS Server (Spring Framework) | HTTP | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 15.0.3.190, 16.0.3.350 |  | 
| CVE-2026-34481 | Oracle Retail Merchandise Financial Planning | Application Core (Apache Log4j) | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | High | None | 15.0, 16.0 |  | 
| CVE-2026-34481 | Oracle Retail Merchandising System | Security (Apache Log4j) | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | High | None | 19.0.1.044 |  | 
| CVE-2026-59901 | Oracle Retail Xstore Point of Service | Xenvironment (Netty) | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 22.0.3, 23.0.3, 24.0.2 |  | 
| CVE-2026-55956 | Oracle Retail Xstore Point of Service | Xenvironment (Apache Tomcat) | HTTP | Yes | 6.5 | Network | Low | None | None | Un- changed | Low | Low | None | 21.0.5, 22.0.3, 23.0.3, 24.0.2, 25.0.1, 26.0.0 |  | 

- The patch for CVE-2026-59901 also addresses CVE-2026-55831 and CVE-2026-56819.
- The patch for CVE-2026-34481 also addresses CVE-2025-68161, CVE-2026-34477, CVE-2026-34478, CVE-2026-34479, and CVE-2026-34480.
- The patch for CVE-2026-55956 also addresses CVE-2026-50229, CVE-2026-53404, CVE-2026-53434, CVE-2026-55276, and CVE-2026-55955.
- The patch for CVE-2026-41855 also addresses CVE-2026-41838, CVE-2026-41839, CVE-2026-41840, CVE-2026-41841, CVE-2026-41842, CVE-2026-41843, CVE-2026-41844, CVE-2026-41845, CVE-2026-41846, CVE-2026-41848, CVE-2026-41850, CVE-2026-41851, CVE-2026-41852, CVE-2026-41853, and CVE-2026-41854.

This Critical Patch Update contains 122 new security patches for Oracle Siebel CRM.  66 of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cpuoct2026verbose.html#SECR)

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-101446 | Siebel CRM Cloud Applications | Siebel Cloud Manager | HTTP | No | 9.9 | Network | Low | Low | None | Changed | High | High | High | 17.0-26.8 |  | 
| CVE-2026-54906 | Siebel CRM End User | Open UI (Ruby) | HTTP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 17.0-26.8 |  | 
| CVE-2026-59083 | Siebel CRM Deployment | Application Interface (Apache Tomcat) | HTTP | Yes | 9.1 | Network | Low | None | None | Un- changed | High | High | None | 17.0-26.8 |  | 
| CVE-2026-101457 | Siebel Apps - Life Sciences | eDetailing | SQL | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 17.0-26.8 |  | 
| CVE-2026-91442 | Siebel CRM Deployment | Server Infrastructure | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 17.0-26.8 |  | 
| CVE-2026-101495 | Siebel CRM Development | Siebel Approval Manager | HTTP | Yes | 8.8 | Network | Low | None | Required | Un- changed | High | High | High | 17.0-26.8 |  | 
| CVE-2026-91437 | Siebel CRM Deployment | Server Infrastructure | HTTP | No | 8.7 | Network | Low | High | None | Changed | High | High | None | 17.0-26.8 |  | 
| CVE-2026-101451 | Siebel Life Sciences | Web UI | HTTP | No | 8.7 | Network | Low | Low | Required | Changed | High | High | None | 17.0-26.8 |  | 
| CVE-2026-101459 | Siebel CRM Deployment | Server Infrastructure | HTTP | No | 8.3 | Network | Low | Low | None | Un- changed | High | High | Low | 17.0-26.8 |  | 
| CVE-2026-101458 | Siebel CRM Deployment | Server Infrastructure | HTTP | Yes | 8.2 | Network | Low | None | None | Un- changed | High | Low | None | 17.0-26.8 |  | 
| CVE-2026-91445 | Siebel CRM End User | Communications Panel/Dashboard | HTTP | Yes | 8.2 | Network | Low | None | None | Un- changed | High | Low | None | 17.0-26.8 |  | 
| CVE-2026-54513 | Siebel CRM Deployment | Application Interface (jackson-databind) | HTTP | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 17.0-26.8 |  | 
| CVE-2026-54513 | Siebel CRM Deployment | Server Infrastructure (jackson-databind) | HTTP | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 17.0-26.8 |  | 
| CVE-2026-54512 | Siebel CRM Development | Siebel Approval Manager (jackson-databind) | HTTP | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 17.0-26.8 |  | 
| CVE-2026-101438 | Siebel CRM Cloud Applications | Siebel Cloud Manager | SSH | Yes | 8.0 | Adjacent Network | High | None | None | Changed | High | High | None | 22.3-26.8 |  | 
| CVE-2026-11332 | Siebel CRM Cloud Applications | Siebel Cloud Manager (Ansible) | None | No | 7.8 | Local | Low | None | Required | Un- changed | High | High | High | 22.3-26.8 |  | 
| CVE-2026-101468 | Siebel CRM Deployment | Cloud Gateway | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | High | None | None | 17.0-26.8 |  | 
| CVE-2026-101461 | Siebel CRM Deployment | Server Infrastructure | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | High | None | None | 17.0-26.8 |  | 
| CVE-2026-91447 | Siebel CRM Deployment | Server Infrastructure | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | High | None | None | 17.0-26.8 |  | 
| CVE-2026-91448 | Siebel CRM Deployment | Server Infrastructure | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | High | None | None | 17.0-26.8 |  | 
| CVE-2026-50010 | Siebel CRM Deployment | Server Infrastructure (Netty) | HTTPS | Yes | 7.5 | Network | Low | None | None | Un- changed | High | None | None | 17.0-26.8 |  | 
| CVE-2026-101460 | Siebel CRM Deployment | Server Infrastructure | TLS | Yes | 7.5 | Network | Low | None | None | Un- changed | High | None | None | 17.0-26.8 |  | 
| CVE-2026-34480 | Siebel CRM Development | Siebel Approval Manager (Apache Log4j) | SYSLOG | Yes | 7.5 | Network | Low | None | None | Un- changed | None | High | None | 17.0-26.8 |  | 
| CVE-2026-101463 | Siebel CRM End User | UIF Open UI | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | High | None | None | 17.0-26.8 |  | 
| CVE-2026-101508 | Siebel CRM Integration | EAI | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 17.0-26.8 |  | 
| CVE-2026-91377 | Siebel CRM Integration | Open Integration | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | High | None | None | 25.12-26.8 |  | 
| CVE-2026-91449 | Siebel CRM Deployment | Server Infrastructure | HTTP | Yes | 7.4 | Network | High | None | None | Un- changed | High | High | None | 17.0-26.8 |  | 
| CVE-2026-91450 | Siebel CRM Deployment | Server Infrastructure | HTTP | Yes | 7.4 | Network | High | None | None | Un- changed | High | High | None | 17.0-26.8 |  | 
| CVE-2026-101467 | Siebel CRM End User | Portal Framework | HTTPS | Yes | 7.4 | Network | High | None | None | Un- changed | High | High | None | 17.0-26.8 |  | 
| CVE-2026-40542 | Siebel CRM Deployment | Server Infrastructure (Apache HttpClient) | HTTP | Yes | 7.3 | Network | Low | None | None | Un- changed | Low | Low | Low | 17.0-26.8 |  | 
| CVE-2026-91433 | Siebel Apps - Field Service | Smart Answer | HTTP | No | 7.2 | Network | Low | High | None | Un- changed | High | High | High | 17.0-26.8 |  | 
| CVE-2026-44161 | Siebel CRM Cloud Applications | Siebel Cloud Manager (Fluentd) | HTTP | Yes | 7.2 | Network | Low | None | None | Changed | Low | None | Low | 22.3-26.8 |  | 
| CVE-2026-91438 | Siebel CRM Deployment | Server Infrastructure | HTTP | No | 7.1 | Network | Low | Low | None | Un- changed | High | Low | None | 17.0-26.8 |  | 
| CVE-2026-101464 | Siebel CRM Deployment | Server Infrastructure | None | No | 7.1 | Local | Low | Low | None | Un- changed | High | High | None | 17.0-26.8 |  | 
| CVE-2026-101447 | Siebel CRM Development | Workflow | HTTP | No | 7.1 | Network | High | Low | Required | Un- changed | High | High | High | 25.12-26.8 |  | 
| CVE-2026-87338 | Siebel CRM Integration | EAI | HTTP | Yes | 6.9 | Network | High | None | Required | Changed | High | Low | None | 17.0-26.8 |  | 
| CVE-2026-91364 | Siebel CRM Cloud Applications | Siebel Cloud Manager | TLS | Yes | 6.8 | Adjacent Network | High | None | None | Un- changed | High | High | None | 22.3-26.8 |  | 
| CVE-2026-101453 | Siebel CRM Deployment | Server Infrastructure | None | No | 6.7 | Local | Low | High | None | Un- changed | High | High | High | 17.0-26.8 |  | 
| CVE-2026-91434 | Siebel CRM Deployment | Server Infrastructure | None | No | 6.7 | Local | Low | High | None | Un- changed | High | High | High | 17.0-26.8 |  | 
| CVE-2026-91444 | Siebel CRM Deployment | Server Infrastructure | None | No | 6.7 | Local | Low | High | None | Un- changed | High | High | High | 17.0-26.8 |  | 
| CVE-2026-91446 | Siebel CRM Deployment | Server Infrastructure | None | No | 6.7 | Local | Low | High | None | Un- changed | High | High | High | 17.0-26.8 |  | 
| CVE-2026-101437 | Siebel CRM Cloud Applications | Siebel Cloud Manager | HTTP | No | 6.6 | Network | High | High | None | Changed | Low | High | None | 22.3-26.8 |  | 
| CVE-2026-91441 | Siebel Apps - Customer Order Management | Order Management | HTTP | No | 6.5 | Network | Low | Low | Required | Changed | Low | Low | Low | 17.0-26.8 |  | 
| CVE-2026-91430 | Siebel Apps - Financial Services | Financial Accounts | HTTP | Yes | 6.5 | Network | High | None | None | Un- changed | High | Low | None | 17.0-26.8 |  | 
| CVE-2026-59889 | Siebel CRM Administration | Data Archival (jackson-databind) | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | None | High | None | 25.12-26.8 |  | 
| CVE-2026-91360 | Siebel CRM Cloud Applications | Siebel Cloud Manager | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 22.3-26.8 |  | 
| CVE-2025-61728 | Siebel CRM Cloud Applications | Siebel Cloud Manager (Golang Go) | HTTP | Yes | 6.5 | Network | Low | None | Required | Un- changed | None | None | High | 22.3-26.8 |  | 
| CVE-2026-101443 | Siebel CRM Cloud Applications | Siebel Cloud Manager | LDAP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 22.3-26.8 |  | 
| CVE-2026-91367 | Siebel CRM Cloud Applications | Siebel Cloud Manager | None | No | 6.5 | Local | Low | Low | None | Changed | High | None | None | 22.3-26.8 |  | 
| CVE-2026-91420 | Siebel CRM Deployment | Server Infrastructure | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | None | High | None | 17.0-26.8 |  | 
| CVE-2026-91429 | Siebel CRM Deployment | Server Infrastructure | HTTP | Yes | 6.5 | Network | High | None | None | Un- changed | High | Low | None | 17.0-26.8 |  | 
| CVE-2026-91435 | Siebel CRM Deployment | Server Infrastructure | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | None | None | High | 17.0-26.8 |  | 
| CVE-2026-91440 | Siebel CRM Deployment | Server Infrastructure | HTTP | Yes | 6.5 | Network | Low | None | None | Un- changed | Low | Low | None | 17.0-26.8 |  | 
| CVE-2026-91443 | Siebel CRM Deployment | Server Infrastructure | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 17.0-26.8 |  | 
| CVE-2026-91412 | Siebel CRM End User | Open UI | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 17.0-26.8 |  | 
| CVE-2026-91432 | Siebel CRM End User | Open UI | HTTP | Yes | 6.5 | Network | Low | None | None | Un- changed | Low | Low | None | 17.0-26.8 |  | 
| CVE-2026-91424 | Siebel CRM Deployment | Server Infrastructure | HTTP | No | 6.4 | Network | High | Low | None | Un- changed | Low | Low | High | 17.0-26.8 |  | 
| CVE-2026-101465 | Siebel CRM Deployment | Server Infrastructure | None | No | 6.3 | Local | High | Low | None | Un- changed | High | High | None | 17.0-26.8 |  | 
| CVE-2026-101455 | Siebel CRM Development | Integration - Scripting | None | No | 6.3 | Local | High | Low | None | Un- changed | High | High | None | 17.0-26.8 |  | 
| CVE-2026-101408 | Siebel Apps - Marketing | Email Marketing | HTTP | Yes | 6.1 | Network | Low | None | Required | Changed | Low | Low | None | 17.0-26.8 |  | 
| CVE-2026-101391 | Siebel Apps - Marketing | Marketing | HTTP | Yes | 6.1 | Network | Low | None | Required | Changed | Low | Low | None | 17.0-26.8 |  | 
| CVE-2026-101395 | Siebel Apps - Marketing | Marketing | HTTP | Yes | 6.1 | Network | Low | None | Required | Changed | Low | Low | None | 17.0-26.8 |  | 
| CVE-2026-101454 | Siebel CRM Development | Configuration Tools | None | No | 6.1 | Local | Low | Low | None | Un- changed | Low | High | None | 17.0-26.8 |  | 
| CVE-2026-91378 | Siebel CRM Integration | Open Integration | HTTP | Yes | 6.1 | Network | Low | None | Required | Changed | Low | Low | None | 25.12-26.8 |  | 
| CVE-2026-91423 | Siebel CRM Deployment | Server Infrastructure | None | No | 6.0 | Local | Low | High | None | Un- changed | High | High | None | 17.0-26.8 |  | 
| CVE-2026-91413 | Siebel CRM Development | Integration - Scripting | CORBA | No | 6.0 | Network | Low | High | None | Un- changed | Low | Low | High | 17.0-26.8 |  | 
| CVE-2026-101456 | Siebel CRM Development | Configuration Tools | None | No | 6.0 | Local | Low | High | None | Un- changed | High | High | None | 17.0-26.8 |  | 
| CVE-2026-101403 | Siebel Apps - Marketing | Email Marketing | HTTP | Yes | 5.9 | Network | High | None | Required | Un- changed | High | Low | None | 17.0-26.8 |  | 
| CVE-2026-91365 | Siebel CRM Cloud Applications | Siebel Cloud Manager | HTTPS | Yes | 5.9 | Adjacent Network | High | None | None | Un- changed | High | Low | None | 22.3-26.8 |  | 
| CVE-2026-101439 | Siebel CRM Cloud Applications | Siebel Cloud Manager | LDAP | Yes | 5.9 | Network | High | None | None | Un- changed | High | None | None | 22.3-26.8 |  | 
| CVE-2026-101440 | Siebel CRM Cloud Applications | Siebel Cloud Manager | LDAP | Yes | 5.9 | Adjacent Network | High | None | None | Un- changed | High | Low | None | 22.3-26.8 |  | 
| CVE-2026-91421 | Siebel CRM Deployment | Server Infrastructure | HTTP | Yes | 5.9 | Network | High | None | None | Un- changed | None | None | High | 17.0-26.8 |  | 
| CVE-2026-91371 | Siebel CRM Cloud Applications | Siebel Cloud Manager | HTTP | Yes | 5.8 | Network | Low | None | None | Changed | Low | None | None | 22.3-26.8 |  | 
| CVE-2026-101392 | Siebel Apps - Marketing | Marketing | None | No | 5.5 | Local | Low | Low | None | Un- changed | High | None | None | 17.0-26.8 |  | 
| CVE-2026-101444 | Siebel CRM Cloud Applications | Siebel Cloud Manager | None | No | 5.5 | Local | Low | Low | None | Un- changed | High | None | None | 22.3-26.8 |  | 
| CVE-2026-91426 | Siebel CRM Deployment | Server Infrastructure | None | No | 5.5 | Local | Low | Low | None | Un- changed | High | None | None | 17.0-26.8 |  | 
| CVE-2026-91439 | Siebel CRM Deployment | Server Infrastructure | None | No | 5.5 | Local | Low | Low | None | Un- changed | High | None | None | 17.0-26.8 |  | 
| CVE-2026-101462 | Siebel CRM Deployment | Server Infrastructure | None | No | 5.5 | Local | Low | Low | None | Un- changed | High | None | None | 17.0-26.8 |  | 
| CVE-2026-91431 | Siebel CRM End User | Open UI | None | No | 5.5 | Local | Low | Low | None | Un- changed | High | None | None | 17.0-26.8 |  | 
| CVE-2026-91387 | Siebel CRM End User | Open UI | HTTP | No | 5.4 | Network | Low | Low | None | Un- changed | Low | Low | None | 17.0-26.8 |  | 
| CVE-2026-91389 | Siebel CRM End User | Open UI | HTTP | No | 5.4 | Network | Low | Low | Required | Changed | Low | Low | None | 17.0-26.8 |  | 
| CVE-2026-91390 | Siebel CRM End User | Open UI | HTTP | No | 5.4 | Network | Low | Low | Required | Changed | Low | Low | None | 17.0-26.8 |  | 
| CVE-2026-101394 | Siebel Apps - Marketing | Marketing | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | None | Low | None | 17.0-26.8 |  | 
| CVE-2026-101399 | Siebel Apps - Marketing | Marketing | SMTP | Yes | 5.3 | Network | Low | None | None | Un- changed | None | None | Low | 17.0-26.8 |  | 
| CVE-2026-91359 | Siebel CRM Cloud Applications | Siebel Cloud Manager | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | Low | None | None | 22.3-26.8 |  | 
| CVE-2026-91361 | Siebel CRM Cloud Applications | Siebel Cloud Manager | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | None | Low | None | 22.3-26.8 |  | 
| CVE-2026-91362 | Siebel CRM Cloud Applications | Siebel Cloud Manager | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | Low | None | None | 22.3-26.8 |  | 
| CVE-2026-91369 | Siebel CRM Cloud Applications | Siebel Cloud Manager | HTTP | No | 5.3 | Network | High | Low | None | Un- changed | None | High | None | 22.3-26.8 |  | 
| CVE-2026-91370 | Siebel CRM Cloud Applications | Siebel Cloud Manager | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | Low | None | None | 22.3-26.8 |  | 
| CVE-2026-101441 | Siebel CRM Cloud Applications | Siebel Cloud Manager | TLS | Yes | 5.3 | Adjacent Network | High | None | None | Un- changed | High | None | None | 22.3-26.8 |  | 
| CVE-2026-91414 | Siebel CRM Deployment | Server Infrastructure | HTTP | Yes | 5.3 | Network | High | None | Required | Un- changed | High | None | None | 17.0-26.8 |  | 
| CVE-2026-91422 | Siebel CRM Deployment | Server Infrastructure | HTTP | No | 5.3 | Network | High | Low | None | Un- changed | None | High | None | 17.0-26.8 |  | 
| CVE-2026-101448 | Siebel CRM Deployment | Siebel Management Console | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | Low | None | None | 17.0-26.8 |  | 
| CVE-2026-41853 | Siebel CRM Development | Siebel Approval Manager (Spring Framework) | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | None | Low | None | 17.0-26.8 |  | 
| CVE-2026-8384 | Siebel CRM End User | Desktop Integration Siebel Agent (Eclipse Jetty) | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | None | Low | None | 17.0-26.8 |  | 
| CVE-2026-101405 | Siebel Apps - Marketing | Marketing | HTTPS | Yes | 4.8 | Network | High | None | None | Un- changed | Low | Low | None | 17.0-26.8 |  | 
| CVE-2026-101396 | Siebel Apps - Marketing | Marketing | None | No | 4.7 | Local | High | Low | None | Un- changed | None | High | None | 17.0-26.8 |  | 
| CVE-2026-91366 | Siebel CRM Cloud Applications | Siebel Cloud Manager | HTTPS | Yes | 4.7 | Adjacent Network | High | None | None | Changed | Low | Low | None | 22.3-26.8 |  | 
| CVE-2026-91388 | Siebel CRM End User | Open UI | HTTP | Yes | 4.7 | Network | High | None | Required | Changed | Low | Low | None | 17.0-26.8 |  | 
| CVE-2026-101492 | Siebel CRM Integration | Open Integration | HTTP | Yes | 4.7 | Network | High | None | Required | Changed | Low | Low | None | 25.12-26.8 |  | 
| CVE-2026-101393 | Siebel Apps - Marketing | Marketing | HTTP | Yes | 4.3 | Network | Low | None | Required | Un- changed | None | Low | None | 17.0-26.8 |  | 
| CVE-2026-101476 | Siebel Apps - Marketing | Marketing | HTTP | Yes | 4.3 | Network | Low | None | Required | Un- changed | None | Low | None | 17.0-26.8 |  | 
| CVE-2026-91428 | Siebel CRM End User | Open UI | HTTP | Yes | 4.3 | Network | Low | None | Required | Un- changed | None | Low | None | 17.0-26.8 |  | 
| CVE-2026-101436 | Siebel CRM Cloud Applications | Siebel Cloud Manager | None | No | 4.1 | Local | High | High | None | Un- changed | High | None | None | 22.3-26.8 |  | 
| CVE-2026-91368 | Siebel CRM Cloud Applications | Siebel Cloud Manager | None | No | 4.1 | Local | High | High | None | Un- changed | High | None | None | 22.3-26.8 |  | 
| CVE-2026-101404 | Siebel Apps - Marketing | Marketing | None | No | 3.9 | Local | High | High | None | Un- changed | Low | Low | Low | 17.0-26.8 |  | 
| CVE-2026-91436 | Siebel CRM Deployment | Server Infrastructure | None | No | 3.9 | Local | High | High | None | Un- changed | Low | Low | Low | 17.0-26.8 |  | 
| CVE-2026-101402 | Siebel Apps - Marketing | Email Marketing | HTTP | Yes | 3.7 | Network | High | None | None | Un- changed | None | None | Low | 17.0-26.8 |  | 
| CVE-2026-101406 | Siebel Apps - Marketing | Marketing | HTTP | Yes | 3.7 | Network | High | None | None | Un- changed | Low | None | None | 17.0-26.8 |  | 
| CVE-2026-91363 | Siebel CRM Cloud Applications | Siebel Cloud Manager | HTTP | Yes | 3.7 | Network | High | None | None | Un- changed | Low | None | None | 22.3-26.8 |  | 
| CVE-2026-91391 | Siebel CRM End User | Open UI | HTTP | Yes | 3.7 | Network | High | None | None | Un- changed | Low | None | None | 17.0-26.8 |  | 
| CVE-2026-91392 | Siebel CRM End User | Open UI | HTTP | Yes | 3.7 | Network | High | None | None | Un- changed | None | Low | None | 17.0-26.8 |  | 
| CVE-2026-101445 | Siebel CRM Cloud Applications | Siebel Cloud Manager | None | No | 3.6 | Local | High | Low | None | Un- changed | Low | Low | None | 22.3-26.8 |  | 
| CVE-2026-91372 | Siebel CRM Cloud Applications | Siebel Cloud Manager | None | No | 3.3 | Local | Low | Low | None | Un- changed | Low | None | None | 22.3-26.8 |  | 
| CVE-2026-101442 | Siebel CRM Cloud Applications | Siebel Cloud Manager | HTTP | No | 3.1 | Network | High | Low | None | Un- changed | Low | None | None | 22.3-26.8 |  | 
| CVE-2026-91393 | Siebel CRM End User | Open UI | HTTP | Yes | 3.1 | Network | High | None | Required | Un- changed | None | Low | None | 17.0-26.8 |  | 
| CVE-2026-87339 | Siebel CRM Integration | REST | HTTP | Yes | 3.1 | Network | High | None | Required | Un- changed | Low | None | None | 17.0-26.8 |  | 
| CVE-2026-101400 | Siebel Apps - Marketing | Marketing | None | No | 2.9 | Local | High | None | None | Un- changed | None | None | Low | 17.0-26.8 |  | 
| CVE-2026-101401 | Siebel Apps - Marketing | Marketing | None | No | 2.9 | Local | High | None | None | Un- changed | None | None | Low | 17.0-26.8 |  | 
| CVE-2026-101449 | Siebel CRM Deployment | Siebel Management Console | None | No | 2.4 | Physical | Low | None | None | Un- changed | Low | None | None | 17.0-26.8 |  | 
| CVE-2026-91427 | Siebel CRM Deployment | Server Infrastructure | None | No | 2.3 | Local | Low | High | None | Un- changed | None | None | Low | 17.0-26.8 |  | 
| CVE-2026-101397 | Siebel Apps - Marketing | Marketing | HTTP | No | 2.2 | Network | High | High | None | Un- changed | Low | None | None | 17.0-26.8 |  | 

- The patch for CVE-2026-54513 also addresses CVE-2023-35116, CVE-2024-6763, CVE-2026-2332, and CVE-2026-54512.
- The patch for CVE-2026-59889 also addresses CVE-2026-54512, CVE-2026-54513, CVE-2026-54514, CVE-2026-54515, CVE-2026-54516, CVE-2026-54517, CVE-2026-54518, and CVE-2026-59888.
- The patch for CVE-2026-34480 also addresses CVE-2026-34477 and CVE-2026-34478.
- The patch for CVE-2026-101508 also addresses CVE-2026-71497 and CVE-2026-75140.
- The patch for CVE-2026-50010 also addresses CVE-2026-42583, CVE-2026-44249, and CVE-2026-45416.
- The patch for CVE-2026-41853 also addresses CVE-2026-22746 and CVE-2026-22751.
- The patch for CVE-2026-8384 also addresses CVE-2026-10051, CVE-2026-54512, CVE-2026-54513, and CVE-2026-6790.
- The patch for CVE-2026-59083 also addresses CVE-2026-24733, CVE-2026-34477, CVE-2026-34480, CVE-2026-41284, CVE-2026-43513, CVE-2026-43515, CVE-2026-50229, and CVE-2026-55276.

This Critical Patch Update contains 50 new security patches, plus additional third party patches noted below, for Oracle Supply Chain.  19 of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cpuoct2026verbose.html#SCP)

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-91622 | Oracle Agile Product Lifecycle Management for Process | Product Quality Management | HTTP | Yes | 9.3 | Network | Low | None | Required | Changed | High | High | None | 6.2.4 |  | 
| CVE-2026-91624 | Oracle Agile Product Lifecycle Management for Process | Product Quality Management | HTTP | Yes | 9.1 | Network | Low | None | None | Un- changed | High | High | None | 6.2.4 |  | 
| CVE-2026-91520 | Oracle Agile Product Lifecycle Management for Process | Product Quality Management | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 6.2.4 |  | 
| CVE-2026-91521 | Oracle Agile Product Lifecycle Management for Process | Product Quality Management | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 6.2.4 |  | 
| CVE-2026-91550 | Oracle Agile Product Lifecycle Management for Process | Product Quality Management | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 6.2.4 |  | 
| CVE-2026-101594 | Oracle Agile Product Lifecycle Management for Process | Product Quality Management | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 6.2.4 |  | 
| CVE-2026-101596 | Oracle Agile Product Lifecycle Management for Process | Product Quality Management | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 6.2.4 |  | 
| CVE-2026-101744 | Oracle Agile Engineering Data Management | Engineering Communication Interface | HTTP | No | 8.4 | Network | High | Low | None | Changed | High | High | Low | 6.2.1 |  | 
| CVE-2026-101593 | Oracle Agile Product Lifecycle Management for Process | Product Quality Management | HTTP | No | 8.3 | Network | Low | Low | None | Un- changed | High | High | Low | 6.2.4 |  | 
| CVE-2026-91573 | Oracle Agile Product Lifecycle Management for Process | Product Quality Management | HTTP | Yes | 8.2 | Network | Low | None | None | Un- changed | High | Low | None | 6.2.4 |  | 
| CVE-2026-91625 | Oracle Agile Product Lifecycle Management for Process | Product Quality Management | HTTP | Yes | 8.2 | Network | Low | None | None | Un- changed | High | Low | None | 6.2.4 |  | 
| CVE-2026-54512 | Oracle Agile PLM | Application Server (jackson-databind) | HTTP | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 9.3.6 |  | 
| CVE-2026-68569 | Oracle Agile PLM | Folders & Files Attachment (Apache Tomcat) | HTTP | No | 8.1 | Network | Low | Low | None | Un- changed | High | High | None | 9.3.6 |  | 
| CVE-2026-101473 | Oracle Agile Product Lifecycle Management for Process | Product Quality Management | HTTP | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 6.2.4 |  | 
| CVE-2026-101602 | Oracle Agile Product Lifecycle Management for Process | Product Quality Management | HTTP | No | 8.0 | Network | Low | Low | Required | Un- changed | High | High | High | 6.2.4 |  | 
| CVE-2026-101562 | Oracle Agile PLM | Acollect | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | High | None | None | 2.6 |  | 
| CVE-2026-101719 | Oracle Agile PLM | Application Server | HTTP | Yes | 7.5 | Network | High | None | Required | Un- changed | High | High | High | 9.3.6 |  | 
| CVE-2026-91515 | Oracle Agile Product Lifecycle Management for Process | Product Quality Management | HTTP | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 6.2.4 |  | 
| CVE-2026-91604 | Oracle Agile Product Lifecycle Management for Process | Product Quality Management | HTTP | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 6.2.4 |  | 
| CVE-2022-34169 | Oracle Product Lifecycle Analytics | Installation Issues (Apache Xalan-Java) | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | High | None | 3.6.1 |  | 
| CVE-2026-101469 | Oracle Product Lifecycle Analytics | Installation Issues | SQL | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 3.6.1 |  | 
| CVE-2026-91623 | Oracle Agile Product Lifecycle Management for Process | Product Quality Management | HTTP | Yes | 7.4 | Network | High | None | None | Un- changed | High | High | None | 6.2.4 |  | 
| CVE-2026-101746 | Oracle Agile Engineering Data Management | Install | TCP/IP | Yes | 7.3 | Adjacent Network | Low | None | Required | Un- changed | High | High | None | 6.2.1 |  | 
| CVE-2026-91512 | Oracle Agile Product Lifecycle Management for Process | Product Quality Management | HTTP | No | 7.2 | Network | Low | High | None | Un- changed | High | High | High | 6.2.4 |  | 
| CVE-2026-101739 | Oracle Agile Engineering Data Management | Engineering Communication Interface | None | No | 7.0 | Local | High | Low | None | Un- changed | High | High | High | 6.2.1 |  | 
| CVE-2026-83394 | Oracle Demand Planning | Internal Operations | HTTP | No | 6.8 | Network | Low | Low | Required | Changed | High | None | None | 12.1, 12.2 |  | 
| CVE-2026-101723 | Oracle Agile PLM MCAD Connector | CAX Client | None | No | 6.7 | Local | High | Low | Required | Un- changed | High | High | High | 3.6 |  | 
| CVE-2026-101715 | Oracle Agile PLM | Application Server | HTTP | Yes | 6.5 | Network | High | None | None | Un- changed | High | Low | None | 9.3.6 |  | 
| CVE-2026-87362 | Oracle Agile PLM | Folders, Files & Attachments | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 9.3.6 |  | 
| CVE-2026-101718 | Oracle Agile PLM | Application Server | TLS | Yes | 6.5 | Network | High | None | None | Un- changed | High | Low | None | 9.3.6 |  | 
| CVE-2026-101717 | Oracle Agile PLM | Security | None | No | 6.4 | Local | High | Low | None | Changed | High | Low | None | 9.3.6 |  | 
| CVE-2026-91565 | Oracle Agile Product Lifecycle Management for Process | Product Quality Management | HTTP | No | 6.4 | Network | High | Low | None | Un- changed | High | Low | Low | 6.2.4 |  | 
| CVE-2026-101565 | Oracle Agile PLM | Import | None | No | 6.2 | Local | Low | None | None | Un- changed | High | None | None | 9.3.6 |  | 
| CVE-2026-101714 | Oracle Agile PLM | Web Client | HTTP | Yes | 6.1 | Network | Low | None | Required | Changed | Low | Low | None | 9.3.6 |  | 
| CVE-2026-101547 | Oracle Demand Planning | Internal Operations | HTTP | Yes | 6.1 | Network | Low | None | Required | Changed | Low | Low | None | 12.1, 12.2 |  | 
| CVE-2026-101471 | Oracle Product Lifecycle Analytics | Installation Issues | None | No | 6.1 | Local | Low | Low | None | Un- changed | High | None | Low | 3.6.1 |  | 
| CVE-2026-101470 | Oracle Product Lifecycle Analytics | Installation Issues | None | No | 6.0 | Local | Low | High | None | Un- changed | High | High | None | 3.6.1 |  | 
| CVE-2026-101564 | Oracle Agile PLM | Acollect | TLS | Yes | 5.9 | Network | High | None | None | Un- changed | High | None | None | 2.6 |  | 
| CVE-2026-101474 | Oracle Agile Product Lifecycle Management for Process | Product Quality Management | HTTP | No | 5.9 | Network | High | Low | None | Un- changed | High | None | Low | 6.2.4 |  | 
| CVE-2026-101472 | Oracle Product Lifecycle Analytics | Installation Issues | None | No | 5.5 | Local | Low | Low | None | Un- changed | High | None | None | 3.6.1 |  | 
| CVE-2026-101713 | Oracle Agile PLM | Application Server | HTTP | No | 5.4 | Network | Low | Low | Required | Changed | Low | Low | None | 9.3.6 |  | 
| CVE-2026-101592 | Oracle Agile Product Lifecycle Management for Process | Product Quality Management | HTTP | No | 5.4 | Network | Low | Low | Required | Changed | Low | Low | None | 6.2.4 |  | 
| CVE-2026-101595 | Oracle Agile Product Lifecycle Management for Process | Supply Chain Relationship Mgmt | HTTP | No | 5.4 | Network | Low | Low | Required | Changed | Low | Low | None | 6.2.4 |  | 
| CVE-2026-101741 | Oracle Agile Engineering Data Management | Engineering Communication Interface | HTTP | Yes | 5.3 | Adjacent Network | High | None | None | Un- changed | High | None | None | 6.2.1 |  | 
| CVE-2026-101745 | Oracle Agile Engineering Data Management | Engineering Communication Interface | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | Low | None | None | 6.2.1 |  | 
| CVE-2026-101716 | Oracle Agile PLM | Web Client | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | Low | None | None | 9.3.6 |  | 
| CVE-2026-101734 | Oracle Agile Engineering Data Management | Engineering Communication Interface | HTTP | No | 4.3 | Network | Low | Low | None | Un- changed | Low | None | None | 6.2.1 |  | 
| CVE-2026-101591 | Oracle Agile Product Lifecycle Management for Process | Product Quality Management | HTTP | No | 4.3 | Network | Low | Low | None | Un- changed | Low | None | None | 6.2.4 |  | 
| CVE-2026-101740 | Oracle Agile Engineering Data Management | Engineering Communication Interface | None | No | 3.6 | Local | High | Low | None | Un- changed | Low | Low | None | 6.2.1 |  | 
| CVE-2026-101738 | Oracle Agile Engineering Data Management | Engineering Communication Interface | HTTP | No | 3.1 | Network | High | Low | None | Un- changed | None | Low | None | 6.2.1 |  | 

- The patch for CVE-2026-68569 also addresses CVE-2026-65182, CVE-2026-65183, CVE-2026-65637, CVE-2026-65905, CVE-2026-65927, CVE-2026-66299, CVE-2026-66422, CVE-2026-68525, CVE-2026-68763, and CVE-2026-73180.
- The patch for CVE-2026-54512 also addresses CVE-2026-54513.

- Oracle Agile PLM
  - Acollect: CVE-2026-101561 \[VEX Justification: vulnerable\_code\_not\_in\_execute\_path\].

This Critical Patch Update contains 28 new security patches for Oracle Systems.  9 of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cpuoct2026verbose.html#SUNS)

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-60432 | Oracle Solaris | Image Packaging System | HTTP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 11.3, 11.4 |  | 
| CVE-2026-101537 | Oracle Solaris | Utility | TCP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 11.4 |  | 
| CVE-2026-47025 | Oracle Solaris | Utility | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 11.3, 11.4 |  | 
| CVE-2026-91527 | Oracle ZFS Storage Appliance Kit | Core | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 8.8 |  | 
| CVE-2026-91348 | Oracle Solaris | Utility | None | No | 8.4 | Local | Low | None | None | Un- changed | High | High | High | 11.3, 11.4 |  | 
| CVE-2026-91252 | Oracle Solaris | Services | HTTP | Yes | 8.2 | Network | Low | None | None | Un- changed | Low | None | High | 11.4 |  | 
| CVE-2026-91253 | Oracle Solaris | Kernel | None | No | 7.8 | Local | Low | Low | None | Un- changed | High | High | High | 11.4 |  | 
| CVE-2026-60662 | Oracle Solaris | Services | None | No | 7.8 | Local | Low | Low | None | Un- changed | High | High | High | 11.4 |  | 
| CVE-2026-91537 | Oracle Solaris | Utility | None | No | 7.8 | Local | Low | Low | None | Un- changed | High | High | High | 11.4 |  | 
| CVE-2026-87417 | Oracle Solaris | Image Packaging System | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | High | None | None | 11.4 |  | 
| CVE-2026-91254 | Oracle Solaris | Kernel | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 11.4 |  | 
| CVE-2026-91255 | Oracle Solaris | Kernel | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 11.4 |  | 
| CVE-2026-91242 | Oracle Solaris | Plugins | None | No | 7.4 | Local | Low | High | Required | Changed | High | High | None | 11.4 |  | 
| CVE-2026-87421 | Oracle Solaris | Image Packaging System | HTTP | Yes | 7.1 | Network | Low | None | Required | Un- changed | High | Low | None | 11.4 |  | 
| CVE-2026-91256 | Oracle Solaris | Services | HTTP | No | 7.1 | Network | Low | Low | None | Un- changed | Low | None | High | 11.4 |  | 
| CVE-2026-91336 | Oracle Solaris | Utility | None | No | 6.5 | Local | Low | Low | None | Changed | None | High | None | 11.4 |  | 
| CVE-2026-87411 | Oracle Solaris | Filesystems | None | No | 5.5 | Local | Low | Low | None | Un- changed | None | None | High | 11.4 |  | 
| CVE-2026-87413 | Oracle Solaris | Filesystems | None | No | 5.5 | Local | Low | Low | None | Un- changed | None | None | High | 11.4 |  | 
| CVE-2026-60453 | Oracle Solaris | X Window System | None | No | 5.3 | Local | Low | Low | None | Un- changed | Low | Low | Low | 11.4 |  | 
| CVE-2026-101597 | Oracle ZFS Storage Appliance Kit | Core | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | Low | None | None | 8.8 |  | 
| CVE-2026-91208 | Oracle Solaris | Services | None | No | 5.1 | Local | High | None | None | Un- changed | None | None | High | 11.4 |  | 
| CVE-2026-91324 | Oracle Solaris | Libraries | None | No | 4.7 | Local | High | None | Required | Un- changed | None | None | High | 11.4 |  | 
| CVE-2026-91244 | Oracle Solaris | Services | None | No | 4.7 | Local | High | Low | None | Un- changed | None | None | High | 11.4 |  | 
| CVE-2026-87423 | Oracle Solaris | X Window System | None | No | 4.5 | Local | High | Low | None | Un- changed | Low | Low | Low | 11.4 |  | 
| CVE-2026-91209 | Oracle Solaris | X Window System | None | No | 4.2 | Local | High | Low | Required | Un- changed | Low | Low | Low | 11.4 |  | 
| CVE-2026-91249 | Oracle Solaris | Libraries | None | No | 3.3 | Local | Low | Low | None | Un- changed | Low | None | None | 11.4 |  | 
| CVE-2026-87414 | Oracle Solaris | Image Packaging System | TLS | Yes | 3.1 | Network | High | None | Required | Un- changed | None | Low | None | 11.4 |  | 
| CVE-2026-87422 | Oracle Solaris | Services | None | No | 2.5 | Local | High | None | Required | Un- changed | None | Low | None | 11.4 |  | 

This Critical Patch Update contains 8 new security patches, plus additional third party patches noted below, for Oracle Utilities Applications.  7 of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cpuoct2026verbose.html#UTIL)

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-68497 | Oracle Utilities Application Framework | Security (jackson-databind) | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 4.4.0.2.0, 4.4.0.3.0, 4.4.0.4.0, 4.5.0.0.0, 4.5.0.1.1, 4.5.0.1.3, 4.5.0.2.0, 25.4, 25.10, 26.4, 26.10 |  | 
| CVE-2026-42587 | Oracle Utilities Network Management System | Third Party (Netty) | HTTP/2 | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 2.5.0.2.0-2.5.0.2.11, 2.6.0.1.0-2.6.0.1.12, 2.6.0.2.0-2.6.0.2.9, 25.12.0.0.0-25.12.0.0.2 |  | 
| CVE-2026-41239 | Oracle Utilities Application Framework | Security (DOMPurify) | HTTP | Yes | 6.8 | Network | High | None | Required | Un- changed | High | High | None | 4.4.0.2.0, 4.4.0.3.0, 4.4.0.4.0, 4.5.0.0.0, 4.5.0.1.1, 4.5.0.1.3, 4.5.0.2.0, 25.4, 25.10, 26.4, 26.10 |  | 
| CVE-2026-49844 | Oracle Utilities Application Framework | Security (Apache Log4j) | HTTP | Yes | 5.9 | Network | High | None | None | Un- changed | None | High | None | 4.4.0.2.0, 4.4.0.3.0, 4.4.0.4.0, 4.5.0.0.0, 4.5.0.1.1, 4.5.0.1.3, 4.5.0.2.0, 25.4, 25.10, 26.4, 26.10 |  | 
| CVE-2026-101517 | Oracle Utilities Network Management System | System Wide | None | No | 5.5 | Local | Low | Low | None | Un- changed | High | None | None | 2.4.0.1.0-2.4.0.1.33, 2.5.0.1.0-2.5.0.1.18, 2.5.0.2.0-2.5.0.2.11, 2.6.0.1.0-2.6.0.1.12, 2.6.0.2.0-2.6.0.2.9, 25.12.0.0.0-25.12.0.0.2 |  | 
| CVE-2026-64607 | Oracle Utilities Application Framework | Security (Apache HttpClient) | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | None | None | Low | 4.4.0.2.0, 4.4.0.3.0, 4.4.0.4.0, 4.5.0.0.0, 4.5.0.1.1, 4.5.0.1.3, 4.5.0.2.0, 25.4, 25.10, 26.4, 26.10 |  | 
| CVE-2026-101589 | Oracle Utilities Network Management System | System Wide | HTTPS | Yes | 5.3 | Network | Low | None | None | Un- changed | Low | None | None | 2.6.0.1.0-2.6.0.1.12, 2.6.0.2.0-2.6.0.2.10, 25.12.0.0.0-25.12.0.0.2 |  | 
| CVE-2026-101605 | Oracle Utilities Network Management System | System Wide | HTTPS | Yes | 5.3 | Network | Low | None | None | Un- changed | Low | None | None | 2.4.0.1.0-2.4.0.1.33, 2.5.0.1.0-2.5.0.1.18, 2.5.0.2.0-2.5.0.2.11, 2.6.0.1.0-2.6.0.1.12, 2.6.0.2.0-2.6.0.2.10, 25.12.0.0.0-25.12.0.0.2 |  | 

- The patch for CVE-2026-68497 also addresses CVE-2026-19032, CVE-2026-54512, CVE-2026-54513, CVE-2026-54514, CVE-2026-54515, CVE-2026-54516, CVE-2026-54517, CVE-2026-54518, CVE-2026-59888, CVE-2026-59889, and CVE-2026-77310.
- The patch for CVE-2026-41239 also addresses CVE-2026-41238.
- The patch for CVE-2026-64607 also addresses CVE-2026-54399.
- The patch for CVE-2026-42587 also addresses CVE-2026-41417, CVE-2026-42578, CVE-2026-42579, CVE-2026-42580, CVE-2026-42581, CVE-2026-42583, CVE-2026-42584, CVE-2026-42585, CVE-2026-42586, and CVE-2026-44248.

- Oracle Utilities Application Framework
  - Security: CVE-2026-83405 \[VEX Justification: inline\_mitigations\_already\_exist\].

This Critical Patch Update contains 6 new security patches for Oracle Virtualization.  None of these vulnerabilities may be remotely exploitable without authentication, i.e., none may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cpuoct2026verbose.html#OVIR)

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-87322 | Oracle VM VirtualBox | Core | ICMP | No | 8.4 | Adjacent Network | Low | High | None | Changed | High | High | High | 7.2.20 |  | 
| CVE-2026-87301 | Oracle VM VirtualBox | Core | None | No | 8.4 | Local | Low | Low | None | Changed | High | None | High | 7.2.16 |  | 
| CVE-2026-101598 | Oracle VM VirtualBox | Core | None | No | 7.8 | Local | Low | Low | None | Un- changed | High | High | High | 7.2.20 |  | 
| CVE-2026-101599 | Oracle VM VirtualBox | Core | None | No | 7.5 | Local | High | Low | Required | Changed | High | High | High | 7.2.20 |  | 
| CVE-2026-87303 | Oracle VM VirtualBox | Core | None | No | 5.9 | Local | Low | Low | Required | Changed | None | None | High | 7.2.16 |  | 
| CVE-2026-87311 | Oracle VM VirtualBox | Core | None | No | 5.6 | Local | High | Low | None | Changed | None | None | High | 7.2.16 |  |
