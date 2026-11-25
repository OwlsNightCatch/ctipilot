---
title: Oracle Critical Security Patch Update Advisory - November 2026
url: https://www.oracle.com/security-alerts/cspunov2026.html
hostname: oracle.com
description: Oracle Critical Security Patch Update Advisory - November 2026
sitename: oracle.com
date: "2026-11-12"
tags: ['CSPU', 'Critical Security Patch Update', 'Security', 'November 2026']
fingerprint: "555d763bc592b53b"
language: en
filedate: "2026-11-25"
---
A Critical Security Patch Update (CSPU) provides targeted, high-priority security fixes in a smaller, more focused format, making them easier to apply with minimal disruption. Critical Security Patch Updates complement Oracle’s existing quarterly cumulative Critical Patch Updates (CPUs).  These patches address vulnerabilities in Oracle code and in third party components included in Oracle products.  Prior Critical Patch Update and Critical Security Patch Update advisories should be reviewed for information regarding earlier published security patches.  Refer to [Critical Patch Updates, Critical Security Patch Updates, Security Alerts and Bulletins](https://www.oracle.com/security-alerts/) for information about Oracle Security advisories.

**Oracle continues to periodically receive reports of attempts to maliciously exploit vulnerabilities for which Oracle has already released security patches. In some instances, it has been reported that attackers have been successful because targeted customers had failed to apply available Oracle patches. Oracle therefore strongly recommends that customers remain on actively-supported versions and apply security patches without delay.**

This Critical Security Patch Update contains 655 new security patches across the product families listed below. Please note that a My Oracle Support (MOS) note summarizing the content of this Critical Security Patch Update and other Oracle Software Security Assurance activities is located at  [November 2026 Critical Security Patch Update: Executive Summary and Analysis](https://support.oracle.com/support/?documentId=CPU433).

**Please note that Oracle released Security Alerts on October 21, 2026 for [CVE-2026-91403](https://www.oracle.com/security-alerts/alert-cve-2026-91403.html), on October 24, 2026 for [CVE-2026-114820](https://www.oracle.com/security-alerts/alert-cve-2026-114820.html) and on October 25, 2026 for [CVE-2026-109618](https://www.oracle.com/security-alerts/alert-cve-2026-109618.html) and [CVE-2026-109619](https://www.oracle.com/security-alerts/alert-cve-2026-109618.html). Customers of affected Oracle product(s) are strongly advised to apply the patches that were announced in these Security Alerts as well as those contained in this Critical Security Patch Update.**

Security vulnerabilities addressed by this Critical Security Patch Update affect the products listed below.

**Please click on the links in the Patch Availability Document column below to access the documentation for patch availability information and installation instructions.** 

Risk matrices list only security vulnerabilities that are newly addressed by the patches associated with this advisory. Risk matrices for previous security patches can be found in [previous Critical Patch Update advisories, Critical Security Patch Update advisories and Alerts](https://www.oracle.com/security-alerts). An English text version of the risk matrices provided in this document is  [here](https://www.oracle.com/security-alerts/cspunov2026verbose.html).

Several vulnerabilities addressed in this Critical Security Patch Update affect multiple products. Each vulnerability is identified by a [CVE ID](https://cve.org). A vulnerability that affects multiple products will appear with the same CVE ID in all risk matrices.

Security vulnerabilities are scored using CVSS version 3.1 (see [Oracle CVSS Scoring](https://www.oracle.com/security-alerts/cvssscoringsystem.html) for an explanation of how Oracle applies CVSS version 3.1).

Oracle conducts an analysis of each security vulnerability addressed by a Critical Security Patch Update. Oracle does not disclose detailed information about this security analysis to customers, but the resulting Risk Matrix and associated documentation provide information about conditions required to exploit the vulnerability and the potential impact of a successful exploit. Oracle provides this information so that customers may conduct their own risk analysis based on the particulars of their product usage. For more information, see [Oracle vulnerability disclosure policies](https://www.oracle.com/corporate/security-practices/assurance/vulnerability/disclosure/).

Third party component vulnerabilities that are deemed not exploitable in the context of their inclusion in an Oracle product are listed, with [VEX](https://www.oracle.com/security-alerts/cpufaq.html#vex) justifications, below the respective Oracle product's risk matrix.

The protocol in the risk matrix implies that all of its secure variants are affected as well. For example, if HTTP is listed as an affected protocol, it implies that HTTPS is also affected. The secure variant of a protocol is listed in the risk matrix only if it is the *only* variant affected.

**Due to the threat posed by a successful attack, Oracle strongly recommends that customers apply Critical Security Patch Update security patches as soon as possible**. Until you apply the Critical Security Patch Update patches, it may be possible to reduce the risk of successful attack by blocking network protocols required by an attack. For attacks that require certain privileges or access to certain packages, removing the privileges or the ability to access the packages from users that do not need the privileges may help reduce the risk of successful attack. Both approaches may break application functionality, so Oracle strongly recommends that customers test changes on non-production systems. Neither approach should be considered a long-term solution as neither corrects the underlying problem.

Oracle strongly recommends that customers apply security patches as soon as possible. For customers that have skipped one or more security patches and are concerned about products that do not have security patches announced in this Critical Security Patch Update, please review [previous Critical Patch Update and Critical Security Patch Update advisories](https://www.oracle.com/security-alerts) to determine appropriate actions.

Patches released through the Critical Security Patch Update program are provided only for product versions that are covered under the Premier Support or Extended Support phases of the  [Lifetime Support Policy](https://www.oracle.com/us/support/lifetime-support/index.html?ssSourceSiteId=otnen). Oracle recommends that customers plan product upgrades to ensure that patches released through the Critical Security Patch Update program are available for the versions they are currently running.

Product releases that are not under Premier Support or Extended Support are not tested for the presence of vulnerabilities addressed by this Critical Security Patch Update. However, it is likely that earlier versions of affected releases are also affected by these vulnerabilities. As a result, Oracle recommends that customers upgrade to supported versions.

The following people or organizations reported security vulnerabilities addressed by this Critical Security Patch Update to Oracle:

- Albert Yang: CVE-2026-114938
- Alexander Dezhinov, Stanislav Dukhin, Nikita Kozlov: CVE-2026-114944
- An Anonymous researcher working with Trend Micro's Zero Day Initiative: CVE-2026-114849
- Anwar Dawa: CVE-2026-127411, CVE-2026-127412, CVE-2026-127420, CVE-2026-127421, CVE-2026-127422, CVE-2026-127423, CVE-2026-127425, CVE-2026-127426, CVE-2026-127427
- Binbin Xu of Tencent YUNDING LAB CodeBuddy Security: CVE-2026-114944
- Connor Laidlaw of Platform Security working with Trend Micro's Zero Day Initiative: CVE-2026-114849
- Dhanush Arvind: CVE-2026-127413, CVE-2026-127428
- Duy Nguyen: CVE-2026-114857
- Frank Wu of NebuSec: CVE-2026-114950
- Ikotas Labs working with Trend Micro's Zero Day Initiative: CVE-2026-114822, CVE-2026-114850
- Juraj Somorovsky of Ruhr-University Bochum: CVE-2026-114947
- Kentaro Takeda of YouMind: CVE-2026-114952
- Matthew Keeley of Platform Security working with Trend Micro's Zero Day Initiative: CVE-2026-114849
- Maximilian Radoy of Paderborn University: CVE-2026-114947
- Myungyong Lee (2peopledesu): CVE-2026-127414
- Nam Nguyen of VinSOC working with Trend Micro's Zero Day Initiative: CVE-2026-114848, CVE-2026-114849
- Nicholas Carlini of Anthropic: CVE-2026-114940
- Phuoc Pham & Son Tran from starfishsec.com: CVE-2026-114835
- Pierre\_Adams: CVE-2026-101550
- Quang Luong of Calif.io: CVE-2026-114938
- Sankara Gosu of ALDAR Corporate: CVE-2026-114918
- Sven Hebrok of Paderborn University: CVE-2026-114947
- Taisic Yun of Xint working with Trend Micro Zero Day Initiative: CVE-2026-114849
- Thanh Vu of VinSOC working with Trend Micro's Zero Day Initiative: CVE-2026-114848, CVE-2026-114849
- Tin Huynh of VinSOC working with Trend Micro's Zero Day Initiative: CVE-2026-114848, CVE-2026-114849
- Tomais Williamson: CVE-2026-114925
- Zheng Yu of depthfirst: CVE-2026-114819
- Zorta Zenith: CVE-2026-114827

Oracle acknowledges people who have contributed to our Security-In-Depth program (see [FAQ](https://www.oracle.com/security-alerts/cpufaq.html)). People are acknowledged for Security-In-Depth contributions if they provide information, observations or suggestions pertaining to security vulnerability issues that result in significant modification of Oracle code or documentation in future releases, but are not of such a critical nature that they are distributed in Critical Security Patch Updates.

In this Critical Security Patch Update, Oracle recognizes the following for contributions to Oracle's Security-In-Depth program:

- Bruno Halltari working with Trend Micro's Zero Day Initiative
- Nikolaos Mourousias working with Trend Micro's Zero Day Initiative

Security patches are released on the third Tuesday of each month. The next four dates are:

- 15 December 2026 (CSPU)
- 19 January 2027 (CPU)
- 16 February 2027 (CSPU)
- 16 March 2027 (CSPU)

| Date | Note | 
|---|---|
| 2026-November-17 | Rev 1. Initial Release. | 


This Critical Security Patch Update contains 20 new security patches for Oracle Database Products divided as follows:

- 7 new security patches for Oracle Database Products
- 2 new security patches for Oracle APEX
- 3 new security patches for Oracle Autonomous Health Framework
- No new security patches for Oracle Global Lifecycle Management, but third party patches are provided
- 8 new security patches for Oracle REST Data Services


This Critical Security Patch Update contains 7 new security patches, plus additional third party patches noted below, for Oracle Database Products.  3 of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  None of these patches are applicable to client-only installations, i.e., installations that do not have the Oracle Database Server installed. The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cspunov2026verbose.html#DB)

| CVE ID | Component | Package and/or Privilege Required | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-114819 | Oracle Text | Create Session | Oracle Net | No | 9.9 | Network | Low | Low | None | Changed | High | High | High | 19.3-19.32, 21.3-21.24, 23.4.0-23.26.3 |  | 
| CVE-2026-114848 | Oracle Text | Create Session | Oracle Net | No | 9.9 | Network | Low | Low | None | Changed | High | High | High | 19.3-19.33, 21.3-21.24, 23.4.0-23.26.3 |  | 
| CVE-2026-114822 | RDBMS | Create Session | Oracle Net | No | 9.9 | Network | Low | Low | None | Changed | High | High | High | 23.4.0-23.26.4 |  | 
| CVE-2026-72897 | RDBMS (OpenSSL) | None | TLS | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 19.32-19.33, 23.4.0-23.26.4 |  | 
| CVE-2026-115557 | RDBMS (Python) | None | Multiple | Yes | 7.4 | Network | High | None | None | Un- changed | High | High | None | 21.3-21.24, 23.4.0-23.26.3 |  | 
| CVE-2026-89425 | Fleet Patching and Provisioning (jackson-core) | None | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | None | None | High | 19.3-19.33, 21.3-21.24, 23.4.0-23.26.4 |  | 
| CVE-2026-64607 | RDBMS (Apache HttpClient) | None | HTTP | Yes | 4.3 | Network | Low | None | Required | Un- changed | None | None | Low | 19.3-19.33, 21.3-21.24, 23.4.0-23.26.4 |  | 

- The patch for CVE-2026-115557 also addresses CVE-2024-3220, CVE-2026-102633, CVE-2026-114583, and CVE-2026-77214.
- The patch for CVE-2026-72897 also addresses CVE-2026-35189, CVE-2026-35191, CVE-2026-42772, CVE-2026-54872, CVE-2026-54873, CVE-2026-54875, CVE-2026-75804, CVE-2026-75805, CVE-2026-75806, CVE-2026-77696, CVE-2026-84782, and CVE-2026-84784.
- The patch for CVE-2026-89425 also addresses CVE-2026-89407.

- Fleet Patching and Provisioning (Apache MINA SSHD): CVE-2026-77185 and CVE-2026-93994 \[VEX Justification: vulnerable\_code\_not\_in\_execute\_path\].
- Oracle SQLcl (Apache MINA SSHD): CVE-2026-77185 and CVE-2026-93994 \[VEX Justification: vulnerable\_code\_not\_in\_execute\_path\].
- RDBMS (DBI): CVE-2026-111879, CVE-2026-102633, CVE-2026-108518 and CVE-2026-77214 \[VEX Justification: vulnerable\_code\_not\_present\].
- RDBMS (jackson-core): CVE-2026-89425 and CVE-2026-89407 \[VEX Justification: vulnerable\_code\_cannot\_be\_controlled\_by\_adversary\].
- RDBMS (jline): CVE-2026-77421 \[VEX Justification: vulnerable\_code\_not\_in\_execute\_path\].
- RDBMS (jline): CVE-2026-77422 \[VEX Justification: vulnerable\_code\_not\_in\_execute\_path\].
- RDBMS (jline): CVE-2026-77420 \[VEX Justification: vulnerable\_code\_not\_in\_execute\_path\].
- RDBMS (jsoup): CVE-2026-75140 \[VEX Justification: vulnerable\_code\_not\_in\_execute\_path\].

This Critical Security Patch Update contains 2 new security patches for Oracle APEX.  Both of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cspunov2026verbose.html#APEX)

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-114849 | Oracle APEX | General | HTTPS | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 24.1.22, 24.2.21, 26.1.5, 26.2.0 |  | 
| CVE-2026-114850 | Oracle APEX | General | HTTPS | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 24.1.22, 24.2.21, 26.1.5, 26.2.0 |  | 

This Critical Security Patch Update contains 3 new security patches for Oracle Autonomous Health Framework.  All of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cspunov2026verbose.html#AHTF)

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-114847 | Oracle Autonomous Health Framework | Developer triaging platform | HTTP | Yes | 9.1 | Network | Low | None | None | Un- changed | High | High | None | 26.4-26.10 |  | 
| CVE-2026-19445 | Oracle Autonomous Health Framework | AHFCOMMON (Python) | TLS | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 26.4-26.9 |  | 
| CVE-2026-102274 | Oracle Autonomous Health Framework | AHFCOMMON (PyJWT) | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 26.8-26.9 |  | 

- The patch for CVE-2026-102274 also addresses CVE-2026-101917, CVE-2026-101918, CVE-2026-102265, CVE-2026-102266, CVE-2026-102267, CVE-2026-102268, CVE-2026-102269, CVE-2026-102270, CVE-2026-102271, CVE-2026-102272, and CVE-2026-102273.
- The patch for CVE-2026-19445 also addresses CVE-2026-11972 and CVE-2026-19553.

This Critical Security Patch Update contains no new security patches for exploitable vulnerabilities but does include third party patches, noted below, for the following non-exploitable third party CVEs for Oracle Global Lifecycle Management.  Please refer to previous Critical Security Patch Update Advisories if the last Critical Security Patch Update was not applied for Oracle Global Lifecycle Management.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cspunov2026verbose.html#GLM)

- Oracle Global Lifecycle Management OPatch
  - Patch Installer (jackson-core): CVE-2026-89425 and CVE-2026-89407 \[VEX Justification: vulnerable\_code\_cannot\_be\_controlled\_by\_adversary\].

This Critical Security Patch Update contains 8 new security patches for Oracle REST Data Services.  5 of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cspunov2026verbose.html#REST)

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-114849 | Oracle REST Data Services | Core | HTTPS | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 24.2.0-26.3.0 |  | 
| CVE-2026-114856 | Oracle REST Data Services | General | HTTPS | Yes | 9.6 | Network | Low | None | Required | Changed | High | High | High | 24.2.0-26.3.0 |  | 
| CVE-2026-114857 | Oracle REST Data Services | PL/SQL Gateway | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 24.2.0-26.3.0 |  | 
| CVE-2026-114852 | Oracle REST Data Services | Core | HTTP | No | 8.1 | Network | Low | Low | None | Un- changed | High | High | None | 24.2.0-26.3.0 |  | 
| CVE-2026-114853 | Oracle REST Data Services | Core | HTTP | Yes | 6.5 | Network | Low | None | None | Un- changed | Low | Low | None | 24.2.0-26.3.0 |  | 
| CVE-2026-114855 | Oracle REST Data Services | Core | HTTPS | Yes | 6.5 | Network | Low | None | None | Un- changed | Low | Low | None | 24.2.0-26.3.0 |  | 
| CVE-2026-114851 | Oracle REST Data Services | Core | HTTP | No | 6.4 | Network | Low | Low | None | Changed | Low | Low | None | 24.2.0-26.3.0 |  | 
| CVE-2026-114854 | Oracle REST Data Services | Core | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | Low | None | None | 24.2.0-26.3.0 |  | 

This Critical Security Patch Update contains 3 new security patches for Oracle Application Testing Suite.  1 of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cspunov2026verbose.html#OATS)

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-114859 | Oracle Application Testing Suite | Test Manager for Web Apps | None | No | 8.8 | Local | Low | Low | None | Changed | High | High | High | 13.3.0.1 |  | 
| CVE-2026-114860 | Oracle Application Testing Suite | Test Manager for Web Apps | TLS | Yes | 8.7 | Network | High | None | None | Changed | High | High | None | 13.3.0.1 |  | 
| CVE-2026-114861 | Oracle Application Testing Suite | OpenScript | None | No | 7.8 | Local | Low | Low | None | Un- changed | High | High | High | 13.3.0.1 |  | 

This Critical Security Patch Update contains 6 new security patches for Oracle Commerce.  All of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cspunov2026verbose.html#OCOM)

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-68481 | Oracle Commerce Guided Search / Oracle Commerce Experience Manager | Content Acquisition System (Apache CXF) | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | High | None | None | 11.4.0 |  | 
| CVE-2026-42402 | Oracle Commerce Guided Search / Oracle Commerce Experience Manager | Content Acquisition System (Apache Neethi) | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 11.4.0 |  | 
| CVE-2026-97791 | Oracle Commerce Platform | Dynamo Application Framework (Apache CXF) | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 11.4.0 |  | 
| CVE-2026-66144 | Oracle Commerce Platform | Dynamo Application Framework (Apache Neethi) | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 11.4.0 |  | 
| CVE-2026-64607 | Oracle Commerce Guided Search / Oracle Commerce Experience Manager | Experience Manager (Apache HttpClient) | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | None | None | Low | 11.4.0 |  | 
| CVE-2026-64607 | Oracle Commerce Platform | Endeca Integration (Apache HttpClient) | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | None | None | Low | 11.4.0 |  | 

- The patch for CVE-2026-66144 also addresses CVE-2026-66142 and CVE-2026-66143.
- The patch for CVE-2026-68481 also addresses CVE-2026-54225, CVE-2026-57817, CVE-2026-57818, CVE-2026-57819, CVE-2026-61466, CVE-2026-63687, CVE-2026-64958, CVE-2026-65432, CVE-2026-65583, CVE-2026-66909, and CVE-2026-68079.
- The patch for CVE-2026-64607 also addresses CVE-2026-54399 and CVE-2026-54428.
- The patch for CVE-2026-97791 also addresses CVE-2026-100227, CVE-2026-107937, CVE-2026-107938, CVE-2026-108039, CVE-2026-54225, CVE-2026-57817, CVE-2026-57818, CVE-2026-57819, CVE-2026-61466, CVE-2026-63687, CVE-2026-64958, CVE-2026-65432, CVE-2026-65583, CVE-2026-66909, CVE-2026-68079, CVE-2026-68481, CVE-2026-71575, CVE-2026-73179, CVE-2026-78384, CVE-2026-79650, CVE-2026-86463, and CVE-2026-97468.

This Critical Security Patch Update contains 31 new security patches for Oracle Communications.  21 of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cspunov2026verbose.html#CGBU)

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-111497 | Oracle Communications Diameter Signaling Router | PMAC (Node.js) | HTTP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 9.0.0.0.0-9.3.0.0.0 |  | 
| CVE-2026-111497 | Oracle Communications Unified Assurance | Core (Brotli) | HTTP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 6.1.1-7.0.0 |  | 
| CVE-2026-1229 | Oracle Communications Unified Assurance | Core (CIRCL) | HTTP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 6.1.1-7.0.0 |  | 
| CVE-2026-41889 | Oracle Communications Unified Assurance | Core (PostgreSQL) | SQL | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 6.1.1-7.0.0 |  | 
| CVE-2026-114820 | Oracle Communications Element Manager | Core (Java) | HTTPS | Yes | 9.1 | Network | Low | None | None | Un- changed | High | High | None | 9.0.3-9.0.5 |  | 
| CVE-2026-114820 | Oracle Communications Unified Assurance | Core (Java) | HTTPS | Yes | 9.1 | Network | Low | None | None | Un- changed | High | High | None | 6.1.1-7.0.0 |  | 
| CVE-2026-114820 | Oracle Communications Unified Inventory Management | Security (Java) | HTTPS | Yes | 9.1 | Network | Low | None | None | Un- changed | High | High | None | 7.5.0, 7.5.1, 7.6.0, 7.7.0, 7.8.0, 8.0.1, 8.26.0 |  | 
| CVE-2026-93546 | Oracle Communications Unified Assurance | Core (Apache HTTP Server) | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 6.1.1-7.0.0 |  | 
| CVE-2026-76957 | Oracle Communications Billing and Revenue Management | BRM Server (LibExpat) | None | No | 7.8 | Local | Low | Low | None | Un- changed | High | High | High | 15.0.0.0.0, 15.0.1.0.0, 15.1.0.0.0, 15.2.0.0.0 |  | 
| CVE-2026-89161 | Oracle Communications Billing and Revenue Management | BRM Server (PCRE2) | None | No | 7.8 | Local | Low | Low | None | Un- changed | High | High | High | 15.0.0.0.0, 15.0.1.0.0, 15.1.0.0.0, 15.2.0.0.0 |  | 
| CVE-2026-27135 | Oracle Communications Billing and Revenue Management | BRM Server (Nghttp2) | HTTP/2 | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 15.0.0.0.0, 15.0.1.0.0, 15.1.0.0.0, 15.2.0.0.0 |  | 
| CVE-2026-9076 | Oracle Communications Billing and Revenue Management | BRM Server (OpenSSL) | TLS | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 15.0.0.0.0, 15.0.1.0.0, 15.1.0.0.0, 15.2.0.0.0 |  | 
| CVE-2026-91777 | Oracle Communications Service Catalog and Design | Third Party Patch (jackson-databind) | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 8.0-8.26 |  | 
| CVE-2026-87022 | Oracle Communications Unified Assurance | Core (Apache Tomcat) | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | High | None | 6.1.1-7.0.0 |  | 
| CVE-2026-88816 | Oracle Communications Unified Assurance | Core (DBI) | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 6.1.1-7.00 |  | 
| CVE-2026-54297 | Oracle Communications Unified Assurance | Core (Faraday) | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 6.1.1-7.0.0 |  | 
| CVE-2026-47737 | Oracle Communications Unified Assurance | Core (Puma) | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | High | None | 6.1.1-7.0.0 |  | 
| CVE-2026-102278 | Oracle Communications Unified Assurance | Core (brace-expansion) | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 6.1.1-7.0.0 |  | 
| CVE-2026-91777 | Oracle Communications Unified Assurance | Core (jackson-databind) | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 6.1.1-7.0.0 |  | 
| CVE-2026-85396 | Oracle Communications Unified Assurance | Core (rubyzip) | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | High | None | 6.1.1-7.0.0 |  | 
| CVE-2026-9547 | Oracle Communications Billing and Revenue Management | BRM Server (curl) | SFTP | Yes | 7.4 | Network | High | None | None | Un- changed | High | High | None | 15.0.0.0.0, 15.0.1.0.0, 15.1.0.0.0, 15.2.0.0.0 |  | 
| CVE-2026-3198 | Oracle Communications Unified Assurance | Core (MLflow) | HTTP | No | 7.1 | Network | Low | Low | None | Un- changed | High | Low | None | 6.1.1-7.0.0 |  | 
| CVE-2026-41989 | Oracle Communications Diameter Signaling Router | Automated Test Suite (libgcrypt) | None | No | 6.7 | Local | High | None | None | Un- changed | None | High | High | 9.0.0.0.0, 9.0.1.0.0, 9.1.0.0.0 |  | 
| CVE-2026-57438 | Oracle Communications Unified Assurance | Core (Nokogiri) | None | No | 6.6 | Local | Low | Low | None | Un- changed | Low | Low | High | 6.1.1-7.0.0 |  | 
| CVE-2026-67420 | Oracle Communications Unified Assurance | Core (Pivotal RabbitMQ) | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | None | High | None | 7.0.0 |  | 
| CVE-2026-54522 | Oracle Communications Unified Assurance | Core (msgpack-ruby) | HTTP | Yes | 6.5 | Network | Low | None | None | Un- changed | Low | Low | None | 6.1.1-7.0.0 |  | 
| CVE-2026-53495 | Oracle Communications Unified Assurance | Core (containerd) | None | No | 6.5 | Local | Low | Low | None | Changed | High | None | None | 7.0.0 |  | 
| CVE-2026-71557 | Oracle Communications Unified Assurance | Core (git) | HTTP | No | 6.3 | Network | Low | Low | Required | Un- changed | None | High | Low | 6.1.1-7.0.0 |  | 
| CVE-2026-47242 | Oracle Communications Unified Assurance | Core (NET::IMAP) | None | No | 6.1 | Local | Low | None | Required | Un- changed | High | Low | None | 6.1.1-7.0.0 |  | 
| CVE-2026-63435 | Oracle Communications Unified Assurance | Core (Ruby Mail) | SMTP | Yes | 5.3 | Network | Low | None | None | Un- changed | None | Low | None | 6.1.1-7.0.0 |  | 
| CVE-2026-22018 | Oracle Communications Element Manager | Core (Java) | HTTP | Yes | 3.7 | Network | High | None | None | Un- changed | None | None | Low | 9.0.0-9.0.5 |  | 

- The patch for CVE-2026-47242 also addresses CVE-2026-47240.
- The patch for CVE-2026-67420 also addresses CVE-2026-61837, CVE-2026-66067, CVE-2026-66069, CVE-2026-67223, CVE-2026-67226, CVE-2026-67227, CVE-2026-67228, CVE-2026-67234, CVE-2026-67236, CVE-2026-67237, CVE-2026-67238, CVE-2026-67239, CVE-2026-67240, CVE-2026-67241, CVE-2026-67242, CVE-2026-67406, CVE-2026-67407, CVE-2026-67408, CVE-2026-67409, CVE-2026-67410, CVE-2026-67411, CVE-2026-67412, CVE-2026-67413, CVE-2026-67414, CVE-2026-67415, CVE-2026-67416, CVE-2026-67418, and CVE-2026-67419.
- The patch for CVE-2026-53495 also addresses CVE-2026-46680, CVE-2026-47262, CVE-2026-50195, CVE-2026-53488, CVE-2026-53489, and CVE-2026-53492.
- The patch for CVE-2026-87022 also addresses CVE-2026-73581, CVE-2026-75973, CVE-2026-76183, CVE-2026-77756, CVE-2026-77762, CVE-2026-77791, CVE-2026-78383, CVE-2026-78437, CVE-2026-79677, CVE-2026-86248, and CVE-2026-86350.
- The patch for CVE-2026-57438 also addresses CVE-2026-57235, CVE-2026-57236, CVE-2026-57434, CVE-2026-57435, CVE-2026-57436, and CVE-2026-57437.
- The patch for CVE-2026-76957 also addresses CVE-2026-41080, CVE-2026-45186, and CVE-2026-66046.
- The patch for CVE-2026-54297 also addresses CVE-2026-33637.
- The patch for CVE-2026-88816 also addresses CVE-2026-88815.
- The patch for CVE-2026-27135 also addresses CVE-2023-35945 and CVE-2023-44487.
- The patch for CVE-2026-93546 also addresses CVE-2026-42356, CVE-2026-42528, CVE-2026-46729, CVE-2026-47360, CVE-2026-48005, CVE-2026-56153, CVE-2026-56154, CVE-2026-56449, CVE-2026-57941, CVE-2026-58415, CVE-2026-59685, CVE-2026-59797, CVE-2026-63045, CVE-2026-63292, CVE-2026-63686, CVE-2026-63718, CVE-2026-73636, CVE-2026-73637, and CVE-2026-79768.
- The patch for CVE-2026-71557 also addresses CVE-2026-25934, CVE-2026-33762, CVE-2026-34165, CVE-2026-41506, CVE-2026-45022, CVE-2026-45570, CVE-2026-45571, and CVE-2026-71556.
- The patch for CVE-2026-22018 also addresses CVE-2026-22003, CVE-2026-22007, CVE-2026-22013, CVE-2026-22016, CVE-2026-22021, CVE-2026-34268, CVE-2026-34282, CVE-2026-41254, CVE-2026-46968, CVE-2026-47010, CVE-2026-47013, CVE-2026-47021, CVE-2026-47027, CVE-2026-47030, CVE-2026-47034, CVE-2026-47035, CVE-2026-47057, CVE-2026-47058, CVE-2026-47059, CVE-2026-47063, CVE-2026-60147, CVE-2026-60164, CVE-2026-60166, CVE-2026-60526, CVE-2026-60589, CVE-2026-61308, CVE-2026-62574, and CVE-2026-70907.
- The patch for CVE-2026-89161 also addresses CVE-2026-13221.
- The patch for CVE-2026-102278 also addresses CVE-2026-102276 and CVE-2026-102277.
- The patch for CVE-2026-41989 also addresses CVE-2026-41990.
- The patch for CVE-2026-47737 also addresses CVE-2026-47736.
- The patch for CVE-2026-91777 also addresses CVE-2026-18401, CVE-2026-19032, CVE-2026-68494, CVE-2026-68497, CVE-2026-83557, CVE-2026-89407, CVE-2026-89425, and CVE-2026-91776.
- The patch for CVE-2026-41889 also addresses CVE-2026-33815 and CVE-2026-33816.
- The patch for CVE-2026-9076 also addresses CVE-2025-69419, CVE-2025-69420, CVE-2025-69421, CVE-2026-28387, CVE-2026-28388, CVE-2026-28390, CVE-2026-34180, CVE-2026-45447, and CVE-2026-54874.
- The patch for CVE-2026-111497 also addresses CVE-2026-105482, CVE-2026-105483, and CVE-2026-106069.
- The patch for CVE-2026-3198 also addresses CVE-2026-10803, CVE-2026-115886, CVE-2026-116690, CVE-2026-116691, CVE-2026-116692, CVE-2026-118623, CVE-2026-118624, CVE-2026-118625, CVE-2026-118626, CVE-2026-118627, CVE-2026-118628, and CVE-2026-71211.
- The patch for CVE-2026-9547 also addresses CVE-2025-0725, CVE-2026-10536, CVE-2026-11856, CVE-2026-12064, CVE-2026-13608, CVE-2026-18924, CVE-2026-19931, CVE-2026-5773, CVE-2026-6276, CVE-2026-80230, CVE-2026-80231, CVE-2026-82208, CVE-2026-82209, CVE-2026-8286, CVE-2026-8924, CVE-2026-8927, CVE-2026-8932, and CVE-2026-9079.

This Critical Security Patch Update contains 2 new security patches for Oracle Construction and Engineering.  Both of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cspunov2026verbose.html#PVA)

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-75140 | Primavera Unifier | Platform (jsoup) | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 22.12.0-22.12.15, 23.12.0-23.12.16 |  | 
| CVE-2026-49844 | Primavera Unifier | Logging (Apache Log4j) | HTTP | Yes | 5.9 | Network | High | None | None | Un- changed | None | High | None | 22.12.0-22.12.15, 23.12.0-23.12.16 |  | 

- The patch for CVE-2026-75140 also addresses CVE-2026-71497.

This Critical Security Patch Update contains 71 new security patches for Oracle E-Business Suite.  19 of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cspunov2026verbose.html#EBS)

Oracle E-Business Suite products include Oracle Database and Oracle Fusion Middleware components that are affected by the vulnerabilities listed in the Oracle Database and Oracle Fusion Middleware sections. The exposure of Oracle E-Business Suite products is dependent on the Oracle Database and Oracle Fusion Middleware versions being used. Oracle Database and Oracle Fusion Middleware security updates are not listed in the Oracle E-Business Suite risk matrix. However, since vulnerabilities affecting Oracle Database and Oracle Fusion Middleware versions may affect Oracle E-Business Suite products, Oracle recommends that customers apply the November 2026 Critical Security Patch Update to the Oracle Database and Oracle Fusion Middleware components of Oracle E-Business Suite. For information on what patches need to be applied to your environments, refer to Oracle E-Business Suite Release 12 Critical Security Patch Update Knowledge Document (November 2026), [My Oracle Support Note KA923](https://support.oracle.com/support/?documentId=KA923).

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-114880 | Document Management and Collaboration | Attachments | HTTP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-114924 | Oracle Application Object Library | Core | HTTP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-114925 | Oracle Applications Framework | REST Services | HTTP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-114863 | Oracle Universal Work Queue | Media Integration issues | HTTP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101691 | Oracle Mobile Field Service | Admin UI | HTTP | Yes | 9.3 | Network | Low | None | None | Changed | High | Low | None | 12.2.3-12.2.15 |  | 
| CVE-2026-114881 | Document Management and Collaboration | Attachments | HTTP | Yes | 9.1 | Network | Low | None | None | Un- changed | High | None | High | 12.2.3-12.2.15 |  | 
| CVE-2026-114917 | Oracle Applications Framework | Personalization | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-114896 | Oracle Collaborative Planning | Horizontal View | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-114897 | Oracle iProcurement | Redirection | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101657 | Oracle Mobile Field Service | Admin UI | HTTPS | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-83362 | Oracle Purchasing | Internal Operations | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-114916 | Oracle Applications Framework | Security | HTTP | No | 8.7 | Network | Low | Low | Required | Changed | High | High | None | 12.2.3-12.2.15 |  | 
| CVE-2026-114918 | Oracle Concurrent Processing | BI Publisher Integration | HTTP | No | 8.7 | Network | Low | High | None | Changed | High | High | None | 12.2.3-12.2.15 |  | 
| CVE-2026-114876 | Oracle iStore | Shopping Cart | HTTP | Yes | 8.6 | Network | Low | None | None | Changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-114904 | Oracle E-Business Suite Integrated SOA Gateway | SOA Provider | None | No | 8.2 | Local | Low | High | None | Changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101659 | Oracle Mobile Field Service | Admin UI | HTTP | No | 8.2 | Network | High | Low | None | Changed | High | High | None | 12.2.3-12.2.15 |  | 
| CVE-2026-114909 | Oracle iProcurement | Requisition Management | HTTP | No | 8.1 | Network | Low | Low | None | Un- changed | High | High | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101652 | Oracle Mobile Field Service | Internal Operations | HTTP | No | 8.1 | Network | Low | Low | None | Un- changed | High | High | None | 12.2.3-12.2.15 |  | 
| CVE-2026-114887 | Oracle Mobile Field Service | Internal Operations | HTTP | No | 8.1 | Network | Low | Low | None | Un- changed | High | High | None | 12.2.3-12.2.15 |  | 
| CVE-2026-114914 | Oracle Purchasing | Endeca | HTTP | No | 8.1 | Network | Low | Low | None | Un- changed | High | High | None | 12.2.3-12.2.15 |  | 
| CVE-2026-114871 | Oracle Sales Online | Internal Operations | HTTP | No | 8.1 | Network | Low | Low | None | Un- changed | High | High | None | 12.2.3-12.2.15 |  | 
| CVE-2026-114874 | Oracle iProcurement | Internal operations | HTTP | No | 7.7 | Network | Low | Low | None | Changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-114865 | Oracle Sales Online | Internal Operations | HTTP | No | 7.6 | Network | Low | Low | Required | Changed | High | Low | None | 12.2.3-12.2.15 |  | 
| CVE-2026-114866 | Oracle Sales Online | Internal Operations | HTTP | No | 7.6 | Network | Low | Low | Required | Changed | High | Low | None | 12.2.3-12.2.15 |  | 
| CVE-2026-114901 | Oracle E-Business Suite Integrated SOA Gateway | SOA Provider | HTTP | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-114911 | Oracle iProcurement | Approval List and Workflow | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | High | None | 12.2.3-12.2.15 |  | 
| CVE-2026-114885 | Oracle Mobile Field Service | Admin UI | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-114882 | Oracle Product Workbench | Internal Operations | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | High | None | 12.2.3-12.2.15 |  | 
| CVE-2026-114906 | Oracle Purchasing | Internal Operations | HTTP | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-114907 | Oracle Purchasing | Internal Operations | HTTP | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-83365 | Oracle Purchasing | Internal Operations | HTTP | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-114912 | Oracle Purchasing | Internal Operations | HTTP | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-114864 | Oracle Sales Online | Internal Operations | HTTP | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-114903 | Oracle E-Business Suite Integrated SOA Gateway | Web Service Provider | SOAP | Yes | 7.4 | Network | High | None | None | Un- changed | High | High | None | 12.2.3-12.2.15 |  | 
| CVE-2026-114877 | Oracle iStore | Shopping Cart | HTTP | Yes | 7.4 | Network | High | None | None | Un- changed | High | High | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101663 | Oracle Mobile Field Service | Admin UI | HTTP | Yes | 7.4 | Network | High | None | None | Un- changed | High | High | None | 12.2.3-12.2.15 |  | 
| CVE-2026-114872 | Oracle Sales Online | Internal Operations | HTTP | Yes | 7.4 | Network | Low | None | Required | Changed | None | High | None | 12.2.3-12.2.15 |  | 
| CVE-2026-114894 | Oracle Universal Work Queue | Media Integration issues | HTTP | Yes | 7.4 | Network | High | None | None | Un- changed | High | High | None | 12.2.3-12.2.15 |  | 
| CVE-2026-114869 | Applications DBA | AD Utilities | None | No | 7.3 | Local | Low | Low | Required | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-114888 | Oracle Mobile Field Service | Admin UI | None | No | 7.3 | Local | Low | Low | None | Changed | High | Low | None | 12.2.3-12.2.15 |  | 
| CVE-2026-101838 | Oracle Contracts | Internal Operations | HTTP | No | 7.2 | Network | Low | High | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-101839 | Oracle Contracts | Internal Operations | HTTP | No | 7.2 | Network | Low | High | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-114884 | Oracle Lease and Finance Management | Internal Operations | HTTP | No | 7.2 | Network | Low | High | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-114902 | Oracle Product Hub | Internal Operations | HTTP | No | 7.2 | Network | Low | High | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-114883 | Oracle Teleservice | Service Request Form | HTTP | No | 7.2 | Network | Low | High | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-114898 | Applications DBA | AD Utilities | None | No | 7.1 | Local | Low | Low | None | Un- changed | High | High | None | 12.2.3-12.2.15 |  | 
| CVE-2026-114915 | Oracle E-Business Suite Secure Enterprise Search | Search Integration Engine | HTTPS | No | 7.1 | Network | Low | Low | None | Un- changed | High | None | Low | 12.2.3-12.2.15 |  | 
| CVE-2026-114873 | Oracle iProcurement | Internal operations | HTTP | No | 7.1 | Network | Low | Low | None | Un- changed | High | Low | None | 12.2.3-12.2.15 |  | 
| CVE-2026-114878 | Oracle iStore | Shopping Cart | HTTP | No | 7.1 | Network | Low | Low | None | Un- changed | High | Low | None | 12.2.3-12.2.15 |  | 
| CVE-2026-114913 | Oracle Purchasing | Internal Operations | HTTP | No | 7.1 | Network | Low | Low | None | Un- changed | None | Low | High | 12.2.3-12.2.15 |  | 
| CVE-2026-114867 | Oracle Sales Online | Internal Operations | HTTP | No | 7.1 | Network | Low | Low | None | Un- changed | Low | High | None | 12.2.3-12.2.15 |  | 
| CVE-2026-114921 | Oracle Flow Manufacturing | Internal Operations | HTTP | No | 6.8 | Network | High | Low | None | Un- changed | High | High | None | 12.2.3-12.2.15 |  | 
| CVE-2026-114891 | Oracle Sourcing | Internal Operations | HTTP | Yes | 6.8 | Network | High | None | None | Changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-114895 | Oracle Mobile Field Service | Internal Operations | None | No | 6.7 | Local | Low | High | None | Un- changed | High | High | High | 12.2.3-12.2.15 |  | 
| CVE-2026-114899 | Oracle Applications Manager | Command Line - RapidClone | None | No | 6.5 | Local | Low | Low | None | Changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-114900 | Oracle Bills of Material | Internal Operations | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-114868 | Oracle Engineering | Change Management | HTTP | Yes | 6.5 | Network | Low | None | None | Un- changed | Low | Low | None | 12.2.3-12.2.15 |  | 
| CVE-2026-114910 | Oracle iProcurement | Requisition Management | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | None | High | None | 12.2.3-12.2.15 |  | 
| CVE-2026-114879 | Oracle iStore | Shopping Cart | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-114886 | Oracle Mobile Field Service | Internal Operations | None | No | 6.5 | Local | Low | Low | None | Changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-114908 | Oracle Purchasing | Internal Operations | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-114923 | Oracle Purchasing | Internal Operations | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-114892 | Oracle Sourcing | Internal Operations | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-114890 | Oracle Trade Management | Claim LOV | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-114870 | Oracle Trading Community | Party Search UI | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-114920 | Oracle Web Applications Desktop Integrator | File download | HTTPS | Yes | 6.1 | Network | Low | None | Required | Changed | Low | Low | None | 12.2.3-12.2.15 |  | 
| CVE-2026-114905 | Oracle Workflow | Workflow Notification Mailer | HTTPS | Yes | 5.9 | Network | High | None | None | Un- changed | High | None | None | 12.2.3-12.2.15 |  | 
| CVE-2026-114889 | Oracle Order Management | Product Diagnostic Tools | HTTP | No | 5.5 | Network | Low | High | None | Un- changed | Low | High | None | 12.2.3-12.2.15 |  | 
| CVE-2026-114893 | Oracle Email Center | Message Component | HTTP | No | 5.4 | Network | Low | Low | Required | Changed | Low | Low | None | 12.2.3-12.2.15 |  | 
| CVE-2026-114875 | Oracle iProcurement | Internal operations | HTTP | No | 5.4 | Network | Low | Low | Required | Changed | Low | Low | None | 12.2.3-12.2.15 |  | 
| CVE-2026-114919 | Oracle Mobile Field Service | Admin UI | HTTP | No | 5.0 | Network | High | High | None | Un- changed | High | None | Low | 12.2.3-12.2.15 |  | 

- The patch for CVE-2026-114918 also addresses CVE-2025-61882.

This Critical Security Patch Update contains 5 new security patches for Oracle Enterprise Manager.  3 of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  None of these patches are applicable to client-only installations, i.e., installations that do not have Oracle Enterprise Manager installed. The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cspunov2026verbose.html#EM)

Oracle Enterprise Manager products include Oracle Database and Oracle Fusion Middleware components that are affected by the vulnerabilities listed in the Oracle Database and Oracle Fusion Middleware sections. The exposure of Oracle Enterprise Manager products is dependent on the Oracle Database and Oracle Fusion Middleware versions being used. Oracle Database and Oracle Fusion Middleware security updates are not listed in the Oracle Enterprise Manager risk matrix. However, since vulnerabilities affecting Oracle Database and Oracle Fusion Middleware versions may affect Oracle Enterprise Manager products, Oracle recommends that customers apply the November 2026 Critical Security Patch Update to the Oracle Database and Oracle Fusion Middleware components of Enterprise Manager. For information on what patches need to be applied to your environments, refer to Critical Security Patch Update November 2026 Patch Availability Document for Oracle Products, [My Oracle Support Note CPU454](https://support.oracle.com/support/?documentId=CPU454).

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-10050 | Oracle Enterprise Manager Base Platform | Agent Next Gen (Eclipse Jetty) | HTTP | Yes | 9.1 | Network | Low | None | None | Un- changed | High | None | High | 13.5, 24.1 |  | 
| CVE-2026-114829 | Oracle Enterprise Manager Base Platform | Job System | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 13.5, 24.1 |  | 
| CVE-2026-34478 | Oracle Enterprise Manager Base Platform | Diagnostic Kit (Apache Log4j) | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | High | None | 13.5, 24.1 |  | 
| CVE-2025-14813 | Oracle Enterprise Manager Base Platform | Agent Next Gen (Bouncy Castle Java Library) | HTTPS | Yes | 7.5 | Network | Low | None | None | Un- changed | High | None | None | 13.5, 24.1 |  | 
| CVE-2026-114830 | Oracle Enterprise Manager Base Platform | Agent Next Gen | None | No | 6.1 | Local | Low | Low | None | Un- changed | High | Low | None | 13.5, 24.1 |  | 

- The patch for CVE-2026-34478 also addresses CVE-2026-34477, CVE-2026-34479, CVE-2026-34480, and CVE-2026-34481.

This Critical Security Patch Update contains 11 new security patches for Oracle Financial Services Applications.  1 of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cspunov2026verbose.html#IFLX)

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-114846 | Oracle Financial Services Customer Screening | User Interface | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | High | None | None | 8.1.2.10 |  | 
| CVE-2026-114842 | Oracle Financial Services Enterprise Case Management | ECM | HTTP | No | 6.8 | Network | High | Low | None | Un- changed | High | High | None | 8.1.2.10 |  | 
| CVE-2026-114836 | Oracle Financial Services Enterprise Case Management | Web UI | HTTP | No | 6.8 | Network | High | Low | None | Un- changed | High | High | None | 8.1.2.10 |  | 
| CVE-2026-114837 | Oracle Financial Services Enterprise Case Management | Web UI | HTTP | No | 6.8 | Network | High | Low | None | Un- changed | High | High | None | 8.1.2.10 |  | 
| CVE-2026-114838 | Oracle Financial Services Enterprise Case Management | Web UI | HTTP | No | 6.8 | Network | High | Low | None | Un- changed | High | High | None | 8.1.2.10 |  | 
| CVE-2026-114845 | Oracle Financial Services Regulatory Reporting | Platform | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 8.1.2.10 |  | 
| CVE-2026-114841 | Oracle Financial Services Regulatory Reporting | Internal Operations | None | No | 5.5 | Local | Low | Low | None | Un- changed | High | None | None | 8.1.2.10 |  | 
| CVE-2026-114843 | Oracle Financial Services Enterprise Case Management | Web UI | HTTP | No | 5.4 | Network | Low | Low | None | Un- changed | Low | Low | None | 8.1.2.10 |  | 
| CVE-2026-114844 | Oracle Financial Services Enterprise Case Management | Web UI | HTTP | No | 5.4 | Network | Low | Low | None | Un- changed | Low | Low | None | 8.1.2.10 |  | 
| CVE-2026-114839 | Oracle Financial Services Enterprise Case Management | Installer | None | No | 4.4 | Local | Low | High | None | Un- changed | High | None | None | 8.1.2.10 |  | 
| CVE-2026-114840 | Oracle Financial Services Regulatory Reporting | Internal Operations | None | No | 4.4 | Local | Low | High | None | Un- changed | High | None | None | 8.1.2.10 |  | 

This Critical Security Patch Update contains 71 new security patches for Oracle Fusion Middleware.  53 of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cspunov2026verbose.html#FMW)

To get the full list of current and previously released Critical Security Patch Update and Critical Patch Update patches for Oracle Fusion Middleware products, refer to [My Oracle Support Doc ID KA1182](https://support.oracle.com/support/?documentId=KA1182).

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-114835 | Oracle Access Manager | Admin Console | HTTP | Yes | 10.0 | Network | Low | None | None | Changed | High | High | High | 12.2.1.4.0, 14.1.2.1.0 |  | 
| CVE-2026-91500 | Oracle Access Manager | Authentication Engine | HTTP | Yes | 10.0 | Network | Low | None | None | Changed | High | High | Low | 12.2.1.4.0, 14.1.2.1.0 |  | 
| CVE-2026-91510 | Oracle Access Manager | Authentication Engine | HTTP | Yes | 10.0 | Network | Low | None | None | Changed | High | High | Low | 12.2.1.4.0, 14.1.2.1.0 |  | 
| CVE-2026-114824 | Oracle Platform Security for Java | Centralized Thirdparty Jars | HTTP | Yes | 10.0 | Network | Low | None | None | Changed | High | High | High | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91569 | Oracle WebLogic Server | TopLink Integration | HTTP | Yes | 10.0 | Network | Low | None | None | Changed | High | High | High | 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0, 15.1.1.0.0 |  | 
| CVE-2026-91570 | Oracle WebLogic Server | TopLink Integration | HTTP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0, 15.1.1.0.0 |  | 
| CVE-2026-91583 | Oracle WebLogic Server | TopLink Integration | HTTP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0, 15.1.1.0.0 |  | 
| CVE-2026-91456 | Oracle WebLogic Server | Core | SOAP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0, 15.1.1.0.0 |  | 
| CVE-2026-91470 | Oracle WebLogic Server | Core | T3, IIOP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0, 15.1.1.0.0 |  | 
| CVE-2026-91585 | Oracle WebLogic Server | TopLink Integration | TCP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0, 15.1.1.0.0 |  | 
| CVE-2026-114826 | Service Delivery Platform | Messaging Enabler | SOAP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 14.1.2.0.0 |  | 
| CVE-2026-91561 | Oracle Service Bus | Core | RMI | No | 9.6 | Network | Low | Low | None | Changed | High | High | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91469 | Oracle WebLogic Server | Core | HTTP | Yes | 9.4 | Network | Low | None | None | Un- changed | Low | High | High | 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0, 15.1.1.0.0 |  | 
| CVE-2026-91507 | Oracle Access Manager | Authentication Engine | HTTP | Yes | 9.3 | Network | Low | None | None | Changed | Low | High | None | 12.2.1.4.0, 14.1.2.1.0 |  | 
| CVE-2026-91618 | Oracle Application Development Framework (ADF) | Security Framework | HTTP | Yes | 9.1 | Network | Low | None | None | Un- changed | High | High | None | 12.2.1.4.0 |  | 
| CVE-2026-8763 | Oracle Managed File Transfer | MFT Runtime Server (Bouncy Castle Java Library) | HTTPS | Yes | 9.1 | Network | Low | None | None | Un- changed | High | High | None | 12.2.1.4.0 |  | 
| CVE-2026-114827 | Oracle Managed File Transfer | MFT Runtime Server | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91566 | Oracle Service Bus | Core | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91556 | Service Delivery Platform | Messaging Enabler | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 14.1.2.0.0 |  | 
| CVE-2026-91509 | Oracle Access Manager | Authentication Engine | SAML | Yes | 8.7 | Network | High | None | None | Changed | High | High | None | 12.2.1.4.0, 14.1.2.1.0 |  | 
| CVE-2026-91548 | Oracle Platform Security for Java | Centralized Thirdparty Jars | HTTP | Yes | 8.6 | Network | Low | None | None | Changed | High | None | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91587 | Oracle WebCenter Portal | Composer | HTTP | Yes | 8.6 | Network | Low | None | None | Changed | High | None | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91671 | Oracle Access Manager | Authentication Engine | HTTP | No | 8.5 | Network | High | Low | None | Changed | High | High | High | 12.2.1.4.0, 14.1.2.1.0 |  | 
| CVE-2026-91558 | Service Delivery Platform | Messaging Enabler | HTTPS | Yes | 8.3 | Adjacent Network | High | None | None | Changed | High | High | High | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91533 | Oracle Access Manager | Authentication Engine | HTTP | Yes | 8.2 | Network | Low | None | None | Un- changed | High | Low | None | 12.2.1.4.0, 14.1.2.1.0 |  | 
| CVE-2026-91543 | Oracle Access Manager | Authentication Engine | TCP | Yes | 8.2 | Network | Low | None | None | Un- changed | High | Low | None | 12.2.1.4.0, 14.1.2.1.0 |  | 
| CVE-2026-91522 | Oracle Access Manager | Authentication Engine | SAML | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 12.2.1.4.0, 14.1.2.1.0 |  | 
| CVE-2026-114825 | Oracle WebCenter Sites | WebCenter Sites | HTTP | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 12.2.1.4.0 |  | 
| CVE-2026-91564 | Oracle Access Manager | Authentication Engine | LDAP | Yes | 7.5 | Network | Low | None | None | Un- changed | High | None | None | 12.2.1.4.0, 14.1.2.1.0 |  | 
| CVE-2026-91516 | Oracle Access Manager | Authentication Engine | TCP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 12.2.1.4.0, 14.1.2.1.0 |  | 
| CVE-2026-54428 | Oracle Business Process Management Suite | Human workflow 11g+ (Apache HttpComponents) | HTTP/2 | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-9545 | Oracle HTTP Server | Oracle Weblogic Server Proxy Plug-in for Oracle HTTP Server (curl) | HTTPS | Yes | 7.5 | Network | Low | None | None | Un- changed | High | None | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91551 | Oracle Platform Security for Java | Centralized Thirdparty Jars | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | High | None | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-59649 | Oracle SOA Suite | B2B Engine (Bouncy Castle Java Library) | HTTPS | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 12.2.1.4.0 |  | 
| CVE-2026-75596 | Service Delivery Platform | Messaging Enabler (Netty) | TLS | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 14.1.2.0.0 |  | 
| CVE-2026-91403 | Oracle Middleware Common Libraries and Tools | Thirdparty Patch (Certifi) | Multiple | Yes | 7.4 | Network | High | None | None | Un- changed | High | High | None | 14.1.2.0.0 |  | 
| CVE-2026-91586 | Oracle WebCenter Portal | Composer | HTTP | Yes | 7.4 | Network | Low | None | Required | Changed | High | None | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91540 | Oracle Access Manager | Authentication Engine | SAML | No | 7.3 | Network | High | High | Required | Changed | High | High | None | 12.2.1.4.0, 14.1.2.1.0 |  | 
| CVE-2026-91531 | Oracle Access Manager | Authentication Engine | HTTP | Yes | 7.2 | Network | Low | None | None | Changed | Low | Low | None | 12.2.1.4.0, 14.1.2.1.0 |  | 
| CVE-2026-91498 | Oracle Access Manager | Authentication Engine | SAML | Yes | 7.2 | Network | Low | None | None | Changed | Low | Low | None | 12.2.1.4.0, 14.1.2.1.0 |  | 
| CVE-2026-91621 | Oracle WebCenter Content | Content Server | HTTP | Yes | 6.9 | Network | High | None | Required | Changed | Low | High | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91666 | Oracle WebCenter Content | Content Server | HTTP | Yes | 6.9 | Network | High | None | Required | Changed | High | Low | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91575 | Oracle Identity Manager Connector | Cisco WebX Connector | HTTP | Yes | 6.8 | Network | High | None | None | Changed | High | None | None | 12.2.1.4.0, 14.1.2.1.0 |  | 
| CVE-2026-91571 | Oracle Identity Manager Connector | Core | SOAP | Yes | 6.8 | Network | High | None | None | Changed | High | None | None | 12.2.1.4.0, 14.1.2.1.0 |  | 
| CVE-2026-91626 | Oracle WebCenter Content | Content Server | HTTP | Yes | 6.8 | Network | High | None | Required | Un- changed | High | High | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91525 | Oracle WebCenter Portal | Composer | HTTP | No | 6.8 | Network | High | Low | None | Un- changed | High | High | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91675 | Oracle Identity Manager Connector | Fusion Apps | HTTP | Yes | 6.5 | Adjacent Network | Low | None | None | Un- changed | High | None | None | 12.2.1.4.0, 14.1.2.1.0 |  | 
| CVE-2026-91578 | Oracle Identity Manager Connector | Generic REST | None | No | 6.5 | Local | Low | Low | None | Changed | High | None | None | 12.2.1.4.0, 14.1.2.1.0 |  | 
| CVE-2026-91560 | Oracle Platform Security for Java | Centralized Thirdparty Jars | HTTP | Yes | 6.5 | Network | High | None | None | Un- changed | High | Low | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91667 | Oracle WebCenter Content | Content Server | HTTP | Yes | 6.5 | Network | Low | None | Required | Un- changed | None | High | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91529 | Oracle WebCenter Portal | Composer | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | None | High | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91567 | Oracle WebCenter Portal | Composer | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | None | High | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91544 | Oracle Application Development Framework (ADF) | ADF Faces | HTTP | Yes | 6.1 | Network | Low | None | Required | Changed | Low | Low | None | 14.1.2.0.0 |  | 
| CVE-2026-91620 | Oracle WebCenter Content | Content Server | HTTP | Yes | 6.1 | Network | Low | None | Required | Changed | Low | Low | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-114832 | Helidon | helidon-security-jwt | HTTP | No | 5.9 | Network | High | Low | None | Un- changed | Low | High | None | 3.0.0-3.2.22 |  | 
| CVE-2026-91677 | Oracle Identity Manager Connector | Millennium | HTTP | Yes | 5.9 | Network | High | None | None | Un- changed | High | None | None | 12.2.1.4.0, 14.1.2.1.0 |  | 
| CVE-2026-49844 | Oracle Managed File Transfer | MFT Runtime Server (Apache Log4j) | HTTP | Yes | 5.9 | Network | High | None | None | Un- changed | None | High | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91416 | Oracle WebLogic Server | Core | HTTP | No | 5.9 | Network | High | High | None | Un- changed | High | High | None | 12.2.1.4.0 |  | 
| CVE-2026-114823 | Oracle Business Process Management Suite | Human workflow 11g+ | HTTP | No | 5.4 | Network | Low | Low | Required | Changed | Low | Low | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-114833 | Helidon | helidon-security | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | Low | None | None | 3.0.0-3.2.22,4.0.0-4.5.6 |  | 
| CVE-2026-91572 | Oracle Identity Manager Connector | SAP ERP+ | HTTP | Yes | 5.3 | Adjacent Network | High | None | None | Un- changed | High | None | None | 12.2.1.4.0, 14.1.2.1.0 |  | 
| CVE-2026-64607 | Oracle SOA Suite | FMW Control (Apache HttpClient) | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | None | None | Low | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91673 | Oracle Identity Manager Connector | Generic REST | None | No | 4.1 | Local | High | High | None | Un- changed | High | None | None | 12.2.1.4.0, 14.1.2.1.0 |  | 
| CVE-2026-114831 | Helidon | helidon-webserver-static-content | HTTP | Yes | 3.7 | Network | High | None | None | Un- changed | None | None | Low | 3.0.0-3.2.22,4.0.0-4.5.6,27.0.0-27.0.1 |  | 
| CVE-2026-91619 | Oracle Application Development Framework (ADF) | ADF Faces | HTTP | Yes | 3.7 | Network | High | None | None | Un- changed | None | Low | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-91670 | Oracle Application Development Framework (ADF) | ADF Faces | HTTP | Yes | 3.7 | Network | High | None | None | Un- changed | Low | None | None | 12.2.1.4.0, 14.1.2.0.0 |  | 
| CVE-2026-114834 | Helidon | helidon-data-jakarta-persistence | None | No | 3.3 | Local | Low | Low | None | Un- changed | Low | None | None | 4.0.0-4.5.6,27.0.0-27.0.1 |  | 
| CVE-2026-91674 | Oracle Identity Manager Connector | Generic REST | None | No | 3.3 | Local | Low | Low | None | Un- changed | Low | None | None | 12.2.1.4.0, 14.1.2.1.0 |  | 
| CVE-2026-91676 | Oracle Identity Manager Connector | Millennium | None | No | 3.3 | Local | Low | Low | None | Un- changed | Low | None | None | 12.2.1.4.0, 14.1.2.1.0 |  | 
| CVE-2026-91678 | Service Delivery Platform | Installer | None | No | 3.3 | Local | Low | Low | None | Un- changed | Low | None | None | 14.1.2.0.0 |  | 
| CVE-2026-91679 | Oracle WebCenter Content | Content Portal Suite | HTTP | Yes | 3.1 | Network | High | None | Required | Un- changed | Low | None | None | 12.2.1.4.0, 14.1.2.0.0 |  | 

- The patch for CVE-2026-75596 also addresses CVE-2026-59903 and CVE-2026-75595.
- The patch for CVE-2026-9545 also addresses CVE-2026-6276, CVE-2026-6429, CVE-2026-7168, and CVE-2026-8924.
- The patch for CVE-2026-59649 also addresses CVE-2026-12817, CVE-2026-14682, and CVE-2026-59640.
- The patch for CVE-2026-8763 also addresses CVE-2026-12185, CVE-2026-12802, CVE-2026-12803, CVE-2026-12816, CVE-2026-12817, CVE-2026-12852, CVE-2026-12860, CVE-2026-13506, CVE-2026-14682, CVE-2026-58059, CVE-2026-58060, CVE-2026-58061, CVE-2026-58062, CVE-2026-59638, CVE-2026-59639, CVE-2026-59640, CVE-2026-59641, CVE-2026-59642, CVE-2026-59643, CVE-2026-59644, CVE-2026-59645, CVE-2026-59646, CVE-2026-59649, CVE-2026-59650, and CVE-2026-59651.
- The patch for CVE-2026-54428 also addresses CVE-2026-54399.

This Critical Security Patch Update contains 29 new security patches for Oracle Analytics.  9 of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cspunov2026verbose.html#ANLY)

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-114784 | Oracle Business Intelligence Enterprise Edition | Platform Security | HTTP | Yes | 10.0 | Network | Low | None | None | Changed | High | High | High | 8.2.0.0.0, 26.01.0.0.0 |  | 
| CVE-2026-114814 | Oracle Business Intelligence Enterprise Edition | Analytics Actions | SOAP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 8.2.0.0.0, 26.01.0.0.0 |  | 
| CVE-2026-114783 | Oracle Business Intelligence Enterprise Edition | BI Platform Security | HTTP | Yes | 8.6 | Network | Low | None | None | Changed | High | None | None | 8.2.0.0.0, 12.2.1.4.0, 26.01.0.0.0 |  | 
| CVE-2026-114815 | Oracle Business Intelligence Enterprise Edition | BI Foundation | HTTP | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 12.2.1.4.0 |  | 
| CVE-2026-114817 | Oracle Business Intelligence Enterprise Edition | BI Platform Security | HTTP | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 8.2.0.0.0, 12.2.1.4.0, 26.01.0.0.0 |  | 
| CVE-2026-114813 | Oracle Business Intelligence Enterprise Edition | Platform Security | HTTP | No | 8.1 | Network | Low | Low | None | Un- changed | None | High | High | 8.2.0.0.0, 26.01.0.0.0 |  | 
| CVE-2026-114793 | Oracle Business Intelligence Enterprise Edition | Analytics Server | None | No | 7.8 | Local | Low | None | Required | Un- changed | High | High | High | 8.2.0.0.0, 12.2.1.4.0, 26.01.0.0.0 |  | 
| CVE-2026-114792 | Oracle Business Intelligence Enterprise Edition | Installation | None | No | 7.8 | Local | Low | None | Required | Un- changed | High | High | High | 8.2.0.0.0, 12.2.1.4.0, 26.01.0.0.0 |  | 
| CVE-2026-114794 | Oracle Business Intelligence Enterprise Edition | Platform Security | None | No | 7.8 | Local | Low | None | Required | Un- changed | High | High | High | 8.2.0.0.0, 26.01.0.0.0 |  | 
| CVE-2026-114790 | Oracle Business Intelligence Enterprise Edition | Platform Security | HTTP | No | 6.8 | Network | Low | High | None | Changed | High | None | None | 8.2.0.0.0, 12.2.1.4.0, 26.01.0.0.0 |  | 
| CVE-2026-114798 | Oracle Business Intelligence Enterprise Edition | Platform Security | None | No | 6.7 | Local | Low | High | None | Un- changed | High | High | High | 26.01.0.0.0 |  | 
| CVE-2026-114801 | Oracle Business Intelligence Enterprise Edition | Platform Security | None | No | 6.7 | Local | Low | High | None | Un- changed | High | High | High | 26.01.0.0.0 |  | 
| CVE-2026-114802 | Oracle Business Intelligence Enterprise Edition | Platform Security | None | No | 6.7 | Local | Low | High | None | Un- changed | High | High | High | 8.2.0.0.0, 12.2.1.4.0, 26.01.0.0.0 |  | 
| CVE-2026-114804 | Oracle Business Intelligence Enterprise Edition | Platform Security | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | None | None | High | 26.01.0.0.0 |  | 
| CVE-2026-114796 | Oracle Business Intelligence Enterprise Edition | Analytics Web General | HTTP | No | 6.4 | Network | Low | Low | None | Changed | Low | Low | None | 8.2.0.0.0, 12.2.1.4.0, 26.01.0.0.0 |  | 
| CVE-2026-114803 | Oracle Business Intelligence Enterprise Edition | BI Search | HTTP | No | 6.4 | Network | High | Low | None | Un- changed | Low | Low | High | 8.2.0.0.0, 12.2.1.4.0, 26.01.0.0.0 |  | 
| CVE-2026-114786 | Oracle Business Intelligence Enterprise Edition | ICAP Client API | HTTP | No | 6.4 | Network | Low | Low | None | Changed | Low | Low | None | 8.2.0.0.0, 26.01.0.0.0 |  | 
| CVE-2026-114797 | Oracle BI Publisher | BI Publisher Security | HTTP | Yes | 6.1 | Network | Low | None | Required | Changed | Low | Low | None | 12.2.1.4.0 |  | 
| CVE-2026-114789 | Oracle BI Publisher | Web Server | HTTP | Yes | 6.1 | Network | Low | None | Required | Changed | Low | Low | None | 12.2.1.4.0 |  | 
| CVE-2026-114800 | Oracle Business Intelligence Enterprise Edition | Visual Analyzer | HTTP | Yes | 6.1 | Network | Low | None | Required | Changed | Low | Low | None | 8.2.0.0.0, 12.2.1.4.0, 26.01.0.0.0 |  | 
| CVE-2026-49844 | Oracle Business Intelligence Enterprise Edition | Platform Security (Apache Log4j) | HTTP | Yes | 5.9 | Network | High | None | None | Un- changed | None | High | None | 8.2.0.0.0, 26.01.0.0.0 |  | 
| CVE-2026-49844 | Oracle Business Intelligence Enterprise Edition | Visual Analyzer (Apache Log4j) | HTTP | Yes | 5.9 | Network | High | None | None | Un- changed | None | High | None | 8.2.0.0.0, 26.01.0.0.0 |  | 
| CVE-2026-114810 | Oracle BI Publisher | E-Business Suite - XDO | None | No | 5.5 | Local | Low | Low | None | Un- changed | High | None | None | 12.2.1.4.0 |  | 
| CVE-2026-114808 | Oracle Business Intelligence Enterprise Edition | Platform Security | None | No | 5.5 | Local | Low | None | Required | Un- changed | None | None | High | 12.2.1.4.0 |  | 
| CVE-2026-114787 | Oracle Business Intelligence Enterprise Edition | BI Platform Security | HTTP | No | 5.4 | Network | Low | Low | None | Un- changed | Low | Low | None | 8.2.0.0.0, 26.01.0.0.0 |  | 
| CVE-2026-114805 | Oracle Business Intelligence Enterprise Edition | Analytics Web General | HTTP | No | 5.3 | Network | High | Low | None | Un- changed | None | None | High | 8.2.0.0.0, 12.2.1.4.0, 26.01.0.0.0 |  | 
| CVE-2026-114811 | Oracle BI Publisher | Web Service API | HTTP | No | 4.3 | Network | Low | Low | None | Un- changed | Low | None | None | 8.2.0.0.0, 12.2.1.4.0, 26.01.0.0.0 |  | 
| CVE-2026-114807 | Oracle Business Intelligence Enterprise Edition | Platform Security | None | No | 3.9 | Local | High | High | None | Un- changed | Low | Low | Low | 26.01.0.0.0 |  | 
| CVE-2026-114806 | Oracle Business Intelligence Enterprise Edition | Platform Security | None | No | 3.6 | Local | High | Low | None | Un- changed | Low | Low | None | 26.01.0.0.0 |  | 

This Critical Security Patch Update contains 267 new security patches for Oracle Hyperion.  107 of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cspunov2026verbose.html#HYP)

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-114978 | Oracle Hyperion Financial Management | Security | HTTP | No | 9.9 | Network | Low | Low | None | Changed | High | High | High | 11.2.26.0.000 |  | 
| CVE-2026-115048 | Oracle Hyperion Infrastructure Technology | Common Security | HTTP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 11.2.26.0.000 |  | 
| CVE-2026-115047 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | HTTP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 11.2.26.0.000 |  | 
| CVE-2026-115080 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | HTTP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 11.2.26.0.000 |  | 
| CVE-2026-115089 | Oracle Hyperion Planning | Application Development Framework | HTTP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 11.2.26.0.000 |  | 
| CVE-2026-115086 | Oracle Hyperion Planning | Security | RMI | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 11.2.26.0.000 |  | 
| CVE-2026-114785 | Oracle Hyperion Planning | Security | HTTP | Yes | 9.6 | Network | Low | None | Required | Changed | High | High | High | 11.2.26.0.000 |  | 
| CVE-2026-115139 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | HTTP | Yes | 9.3 | Network | Low | None | Required | Changed | High | High | None | 11.2.26.0.000 |  | 
| CVE-2026-114956 | Oracle Hyperion Planning | Security | HTTP | Yes | 9.3 | Network | Low | None | Required | Changed | High | High | None | 11.2.26.0.000 |  | 
| CVE-2026-127362 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTP | Yes | 9.1 | Network | Low | None | None | Un- changed | High | High | None | 11.2.26.0.000 |  | 
| CVE-2026-127369 | Oracle Hyperion Financial Close Management | Reconciliation Manage | Oracle Net | Yes | 9.1 | Network | Low | None | None | Un- changed | High | High | None | 11.2.26.0.000 |  | 
| CVE-2026-115050 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | HTTP | Yes | 9.1 | Network | Low | None | None | Un- changed | High | High | None | 11.2.26.0.000 |  | 
| CVE-2026-115070 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 11.2.26.0.000 |  | 
| CVE-2026-115074 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 11.2.26.0.000 |  | 
| CVE-2026-127335 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 11.2.26.0.000 |  | 
| CVE-2026-127371 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 11.2.26.0.000 |  | 
| CVE-2026-115071 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTPS | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 11.2.26.0.000 |  | 
| CVE-2026-115133 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTPS | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 11.2.26.0.000 |  | 
| CVE-2026-114979 | Oracle Hyperion Financial Management | Security | SQL | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 11.2.26.0.000 |  | 
| CVE-2026-115049 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 11.2.26.0.000 |  | 
| CVE-2026-115054 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 11.2.26.0.000 |  | 
| CVE-2026-115142 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 11.2.26.0.000 |  | 
| CVE-2026-127418 | Oracle Hyperion Infrastructure Technology | Lifecycle Management | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 11.2.26.0.000 |  | 
| CVE-2026-115067 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | LDAP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 11.2.26.0.000 |  | 
| CVE-2026-115131 | Oracle Hyperion Planning | Application Development Framework | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 11.2.26.0.000 |  | 
| CVE-2026-115087 | Oracle Hyperion Planning | Security | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 11.2.26.0.000 |  | 
| CVE-2026-115128 | Oracle Hyperion Planning | Security | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 11.2.26.0.000 |  | 
| CVE-2026-115120 | Oracle Hyperion Financial Management | Security | HTTP | No | 8.7 | Network | Low | Low | Required | Changed | High | High | None | 11.2.26.0.000 |  | 
| CVE-2026-115164 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | T3, IIOP | No | 8.7 | Network | Low | High | None | Changed | High | High | None | 11.2.26.0.000 |  | 
| CVE-2026-115088 | Oracle Hyperion Planning | Security | HTTP | Yes | 8.7 | Network | High | None | None | Changed | High | High | None | 11.2.26.0.000 |  | 
| CVE-2026-127370 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTPS | Yes | 8.6 | Network | Low | None | None | Un- changed | High | Low | Low | 11.2.26.0.000 |  | 
| CVE-2026-115173 | Oracle Hyperion Infrastructure Technology | Common Security | HTTP | No | 8.5 | Network | Low | Low | None | Changed | High | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-115179 | Oracle Hyperion Infrastructure Technology | Common Security | None | No | 8.4 | Local | Low | Low | None | Changed | High | High | None | 11.2.26.0.000 |  | 
| CVE-2026-127357 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTP | No | 8.3 | Network | Low | Low | None | Un- changed | Low | High | High | 11.2.26.0.000 |  | 
| CVE-2026-115078 | Oracle Hyperion Financial Management | Security | HTTP | Yes | 8.2 | Network | Low | None | None | Un- changed | High | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-114958 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | HTTP | Yes | 8.2 | Network | Low | None | None | Un- changed | High | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-115082 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | HTTP | Yes | 8.2 | Network | Low | None | Required | Changed | High | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-115166 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | HTTP | Yes | 8.2 | Network | Low | None | None | Un- changed | High | None | Low | 11.2.26.0.000 |  | 
| CVE-2026-115060 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | None | No | 8.2 | Local | Low | High | None | Changed | High | High | High | 11.2.26.0.000 |  | 
| CVE-2026-115092 | Oracle Hyperion Planning | Application Development Framework | HTTP | No | 8.2 | Network | High | Low | None | Changed | High | High | None | 11.2.26.0.000 |  | 
| CVE-2026-127372 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTP | No | 8.1 | Network | Low | Low | None | Un- changed | High | High | None | 11.2.26.0.000 |  | 
| CVE-2026-115062 | Oracle Hyperion Financial Management | Security | SOAP | No | 8.1 | Network | Low | Low | None | Un- changed | High | High | None | 11.2.26.0.000 |  | 
| CVE-2026-115153 | Oracle Hyperion Infrastructure Technology | Common Security | HTTP | Yes | 8.1 | Network | Low | None | Required | Un- changed | High | High | None | 11.2.26.0.000 |  | 
| CVE-2026-115172 | Oracle Hyperion Infrastructure Technology | Common Security | HTTP | No | 8.1 | Network | Low | Low | None | Un- changed | High | High | None | 11.2.26.0.000 |  | 
| CVE-2026-115046 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | HTTP | No | 8.1 | Network | Low | Low | None | Un- changed | High | High | None | 11.2.26.0.000 |  | 
| CVE-2026-115059 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | HTTP | Yes | 8.1 | Network | Low | None | Required | Un- changed | None | High | High | 11.2.26.0.000 |  | 
| CVE-2026-115066 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | HTTP | No | 8.1 | Network | Low | Low | None | Un- changed | High | High | None | 11.2.26.0.000 |  | 
| CVE-2026-115081 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | HTTP | Yes | 8.1 | Network | Low | None | Required | Un- changed | None | High | High | 11.2.26.0.000 |  | 
| CVE-2026-115150 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | HTTP | No | 8.1 | Network | Low | Low | None | Un- changed | None | High | High | 11.2.26.0.000 |  | 
| CVE-2026-115157 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | HTTP | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 11.2.26.0.000 |  | 
| CVE-2026-127415 | Oracle Hyperion Infrastructure Technology | Lifecycle Management | HTTP | Yes | 8.1 | Network | Low | None | Required | Un- changed | None | High | High | 11.2.26.0.000 |  | 
| CVE-2026-127416 | Oracle Hyperion Infrastructure Technology | Lifecycle Management | HTTP | No | 8.1 | Network | Low | Low | None | Un- changed | None | High | High | 11.2.26.0.000 |  | 
| CVE-2026-115051 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | HTTPS | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 11.2.26.0.000 |  | 
| CVE-2026-115151 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | RMI | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 11.2.26.0.000 |  | 
| CVE-2026-115130 | Oracle Hyperion Planning | Application Development Framework | HTTP | No | 8.1 | Network | Low | Low | None | Un- changed | High | High | None | 11.2.26.0.000 |  | 
| CVE-2026-114788 | Oracle Hyperion Planning | Security | HTTP | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 11.2.26.0.000 |  | 
| CVE-2026-115094 | Oracle Hyperion Planning | Security | RMI | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 11.2.26.0.000 |  | 
| CVE-2025-48734 | Oracle Hyperion Planning | Security (Apache Commons BeanUtils) | RMI | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 11.2.26.0.000 |  | 
| CVE-2026-114818 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | None | No | 7.8 | Local | Low | None | Required | Un- changed | High | High | High | 11.2.26.0.000 |  | 
| CVE-2026-114828 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | None | No | 7.8 | Local | Low | Low | None | Un- changed | High | High | High | 11.2.26.0.000 |  | 
| CVE-2026-115076 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTP | No | 7.7 | Network | Low | Low | None | Changed | High | None | None | 11.2.26.0.000 |  | 
| CVE-2026-127349 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTP | No | 7.7 | Network | Low | Low | None | Changed | High | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115170 | Oracle Hyperion Infrastructure Technology | Common Security | HTTP | No | 7.7 | Network | Low | Low | None | Changed | High | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115158 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | HTTP | No | 7.7 | Network | Low | Low | None | Changed | High | None | None | 11.2.26.0.000 |  | 
| CVE-2026-114809 | Oracle Hyperion Planning | Security | HTTP | No | 7.7 | Network | Low | Low | None | Changed | High | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115129 | Oracle Hyperion Planning | Security | HTTP | No | 7.7 | Network | Low | Low | None | Changed | High | None | None | 11.2.26.0.000 |  | 
| CVE-2026-127340 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTP | No | 7.6 | Network | Low | Low | Required | Changed | High | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-115117 | Oracle Hyperion Financial Management | Security | HTTP | No | 7.6 | Network | Low | Low | None | Un- changed | Low | High | Low | 11.2.26.0.000 |  | 
| CVE-2026-115058 | Oracle Hyperion Infrastructure Technology | Common Security | HTTP | No | 7.6 | Network | Low | Low | Required | Changed | High | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-115143 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | HTTP | No | 7.6 | Network | Low | Low | Required | Changed | High | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-115176 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | HTTP | No | 7.6 | Network | Low | Low | Required | Changed | High | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-127351 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | High | None | None | 11.2.26.0.000 |  | 
| CVE-2026-127373 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | High | None | None | 11.2.26.0.000 |  | 
| CVE-2026-101693 | Oracle Hyperion Financial Data Quality Management, Enterprise Edition | Security | HTTP | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 11.2.26.0.000 |  | 
| CVE-2026-115065 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | HTTP | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 11.2.26.0.000 |  | 
| CVE-2026-115146 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | High | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115155 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | HTTP | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 11.2.26.0.000 |  | 
| CVE-2026-114955 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | Oracle Net | Yes | 7.5 | Network | Low | None | None | Un- changed | High | None | None | 11.2.26.0.000 |  | 
| CVE-2026-114799 | Oracle Hyperion Planning | Security | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | High | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115101 | Oracle Hyperion Planning | Security | HTTP | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 11.2.26.0.000 |  | 
| CVE-2026-127360 | Oracle Hyperion Financial Close Management | Reconciliation Manage | SMB | Yes | 7.4 | Network | High | None | None | Un- changed | High | High | None | 11.2.26.0.000 |  | 
| CVE-2026-101848 | Oracle Hyperion Financial Data Quality Management, Enterprise Edition | Security | HTTPS | Yes | 7.4 | Network | High | None | None | Un- changed | High | High | None | 11.2.26.0.000 |  | 
| CVE-2026-115160 | Oracle Hyperion Infrastructure Technology | Common Security | HTTP | Yes | 7.4 | Network | High | None | None | Un- changed | High | High | None | 11.2.26.0.000 |  | 
| CVE-2026-115163 | Oracle Hyperion Infrastructure Technology | Common Security | HTTP | Yes | 7.4 | Network | High | None | None | Un- changed | High | High | None | 11.2.26.0.000 |  | 
| CVE-2026-115053 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | HTTPS | Yes | 7.4 | Network | High | None | None | Un- changed | High | High | None | 11.2.26.0.000 |  | 
| CVE-2026-115178 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | HTTPS | Yes | 7.4 | Network | High | None | None | Un- changed | High | High | None | 11.2.26.0.000 |  | 
| CVE-2026-115138 | Oracle Hyperion Planning | Security | HTTP | Yes | 7.4 | Network | High | None | None | Un- changed | High | High | None | 11.2.26.0.000 |  | 
| CVE-2026-115124 | Oracle Hyperion Planning | Security | HTTPS | Yes | 7.4 | Network | High | None | None | Un- changed | High | High | None | 11.2.26.0.000 |  | 
| CVE-2026-115140 | Oracle Hyperion Planning | Security | HTTPS | Yes | 7.4 | Network | High | None | None | Un- changed | High | High | None | 11.2.26.0.000 |  | 
| CVE-2026-115141 | Oracle Hyperion Planning | Security | Oracle Net | Yes | 7.4 | Network | High | None | None | Un- changed | High | High | None | 11.2.26.0.000 |  | 
| CVE-2026-115072 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | HTTP | No | 7.2 | Network | Low | High | None | Un- changed | High | High | High | 11.2.26.0.000 |  | 
| CVE-2026-115057 | Oracle Hyperion Financial Management | Security | HTTP | No | 7.1 | Network | Low | Low | None | Un- changed | High | None | Low | 11.2.26.0.000 |  | 
| CVE-2026-115061 | Oracle Hyperion Financial Management | Security | HTTP | Yes | 7.1 | Network | Low | None | Required | Un- changed | High | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-115063 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | HTTP | No | 7.1 | Network | Low | Low | None | Un- changed | High | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-115064 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | HTTP | No | 7.1 | Network | Low | Low | None | Un- changed | High | None | Low | 11.2.26.0.000 |  | 
| CVE-2026-115159 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | HTTP | No | 7.1 | Network | Low | Low | None | Un- changed | High | None | Low | 11.2.26.0.000 |  | 
| CVE-2026-115177 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | HTTP | No | 7.1 | Network | Low | Low | None | Un- changed | None | High | Low | 11.2.26.0.000 |  | 
| CVE-2026-115077 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | None | No | 7.0 | Local | High | Low | None | Un- changed | High | High | High | 11.2.26.0.000 |  | 
| CVE-2026-114992 | Oracle Hyperion Data Relationship Management | Access and security | HTTP | No | 6.9 | Network | Low | High | Required | Changed | High | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-115021 | Oracle Hyperion Data Relationship Management | Access and security | HTTP | Yes | 6.8 | Network | High | None | Required | Un- changed | High | High | None | 11.2.26.0.000 |  | 
| CVE-2026-115119 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTP | Yes | 6.8 | Adjacent Network | High | None | None | Un- changed | High | High | None | 11.2.26.0.000 |  | 
| CVE-2026-115122 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTP | Yes | 6.8 | Adjacent Network | High | None | None | Un- changed | High | High | None | 11.2.26.0.000 |  | 
| CVE-2026-115126 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTP | No | 6.8 | Network | High | Low | None | Un- changed | High | High | None | 11.2.26.0.000 |  | 
| CVE-2026-115148 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTP | No | 6.8 | Network | High | Low | None | Un- changed | High | High | None | 11.2.26.0.000 |  | 
| CVE-2026-127350 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTP | No | 6.8 | Network | High | Low | None | Un- changed | High | High | None | 11.2.26.0.000 |  | 
| CVE-2026-127359 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTP | No | 6.8 | Network | High | Low | None | Un- changed | High | High | None | 11.2.26.0.000 |  | 
| CVE-2026-127342 | Oracle Hyperion Financial Close Management | Reconciliation Manage | SQL | No | 6.8 | Network | High | Low | None | Un- changed | High | High | None | 11.2.26.0.000 |  | 
| CVE-2026-114954 | Oracle Hyperion Financial Close Management | Close Manager | T3, IIOP | Yes | 6.8 | Adjacent Network | High | None | None | Un- changed | High | High | None | 11.2.26.0.000 |  | 
| CVE-2026-115154 | Oracle Hyperion Infrastructure Technology | Common Security | HTTP | No | 6.8 | Network | High | Low | None | Un- changed | High | High | None | 11.2.26.0.000 |  | 
| CVE-2026-115056 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | HTTP | No | 6.8 | Network | Low | High | None | Changed | High | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115099 | Oracle Hyperion Planning | Application Development Framework | HTTP | Yes | 6.8 | Network | High | None | Required | Un- changed | High | High | None | 11.2.26.0.000 |  | 
| CVE-2026-115091 | Oracle Hyperion Financial Close Management | Reconciliation Manage | SQL | No | 6.6 | Network | High | High | None | Un- changed | High | High | High | 11.2.26.0.000 |  | 
| CVE-2026-114998 | Oracle Hyperion Data Relationship Management | Access and security | HTTP | Yes | 6.5 | Network | Low | None | Required | Un- changed | High | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115001 | Oracle Hyperion Data Relationship Management | Access and security | HTTP | Yes | 6.5 | Network | Low | None | None | Un- changed | None | Low | Low | 11.2.26.0.000 |  | 
| CVE-2026-115014 | Oracle Hyperion Data Relationship Management | Access and security | HTTP | Yes | 6.5 | Adjacent Network | Low | None | None | Un- changed | High | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115022 | Oracle Hyperion Data Relationship Management | Access and security | HTTP | Yes | 6.5 | Network | Low | None | Required | Un- changed | None | High | None | 11.2.26.0.000 |  | 
| CVE-2026-114997 | Oracle Hyperion Data Relationship Management | Access and security | None | No | 6.5 | Local | Low | Low | None | Changed | High | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115095 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTP | No | 6.5 | Network | Low | High | None | Un- changed | High | High | None | 11.2.26.0.000 |  | 
| CVE-2026-127347 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTP | No | 6.5 | Network | Low | High | None | Un- changed | High | High | None | 11.2.26.0.000 |  | 
| CVE-2026-127352 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115181 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTPS | No | 6.5 | Network | Low | Low | None | Un- changed | None | High | None | 11.2.26.0.000 |  | 
| CVE-2026-115055 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115069 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | HTTP | Yes | 6.5 | Network | High | None | None | Un- changed | None | Low | High | 11.2.26.0.000 |  | 
| CVE-2026-115144 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | None | High | None | 11.2.26.0.000 |  | 
| CVE-2026-115161 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115156 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | None | No | 6.5 | Local | Low | Low | None | Changed | High | None | None | 11.2.26.0.000 |  | 
| CVE-2026-114795 | Oracle Hyperion Infrastructure Technology | Common Security | SSH | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115105 | Oracle Hyperion Planning | Security | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | None | High | None | 11.2.26.0.000 |  | 
| CVE-2026-115112 | Oracle Hyperion Planning | Security | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115132 | Oracle Hyperion Planning | Security | HTTP | Yes | 6.5 | Network | Low | None | Required | Un- changed | None | High | None | 11.2.26.0.000 |  | 
| CVE-2026-114962 | Oracle Hyperion Profitability and Cost Management | Deployment | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | None | High | None | 11.2.26.0.000 |  | 
| CVE-2026-114964 | Oracle Hyperion Profitability and Cost Management | Deployment | None | No | 6.5 | Local | Low | Low | None | Changed | High | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115002 | Oracle Hyperion Data Relationship Management | Access and security | HTTP | No | 6.4 | Network | Low | Low | None | Changed | Low | Low | None | 11.2.26.0.000 |  | 
| CVE-2022-23305 | Oracle Hyperion Planning | Security (Apache Log4j) | HTTP | No | 6.4 | Network | High | Low | None | Un- changed | Low | Low | High | 11.2.26.0.000 |  | 
| CVE-2026-114975 | Oracle Hyperion Workspace | UI and Visualization | HTTP | No | 6.4 | Network | Low | Low | None | Changed | Low | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-115006 | Oracle Hyperion Data Relationship Management | Access and security | HTTP | No | 6.2 | Network | High | High | None | Un- changed | High | High | Low | 11.2.26.0.000 |  | 
| CVE-2026-114782 | Oracle Hyperion Infrastructure Technology | Common Events | HTTP | Yes | 6.1 | Network | Low | None | Required | Changed | Low | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-115175 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | HTTP | Yes | 6.1 | Network | Low | None | Required | Changed | Low | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-115134 | Oracle Hyperion Planning | Application Development Framework | HTTP | Yes | 6.1 | Network | Low | None | Required | Changed | Low | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-114791 | Oracle Hyperion Planning | Security | HTTP | Yes | 6.1 | Network | Low | None | Required | Changed | Low | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-114965 | Oracle Hyperion Profitability and Cost Management | Deployment | HTTP | Yes | 6.1 | Network | Low | None | Required | Changed | Low | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-114972 | Oracle Hyperion Profitability and Cost Management | Deployment | HTTP | Yes | 6.1 | Network | Low | None | Required | Changed | Low | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-114999 | Oracle Hyperion Data Relationship Management | Access and security | None | No | 6.0 | Local | Low | High | None | Un- changed | High | High | None | 11.2.26.0.000 |  | 
| CVE-2026-115000 | Oracle Hyperion Data Relationship Management | Access and security | None | No | 6.0 | Local | Low | High | None | Changed | High | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115005 | Oracle Hyperion Data Relationship Management | Access and security | HTTP | No | 5.9 | Network | High | Low | None | Un- changed | Low | High | None | 11.2.26.0.000 |  | 
| CVE-2026-115016 | Oracle Hyperion Data Relationship Management | Access and security | HTTP | Yes | 5.9 | Network | High | None | None | Un- changed | None | None | High | 11.2.26.0.000 |  | 
| CVE-2026-115018 | Oracle Hyperion Data Relationship Management | Access and security | HTTP | Yes | 5.9 | Network | High | None | None | Un- changed | None | None | High | 11.2.26.0.000 |  | 
| CVE-2026-115032 | Oracle Hyperion Data Relationship Management | Access and security | HTTP | Yes | 5.9 | Network | High | None | None | Un- changed | High | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115127 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTP | Yes | 5.9 | Network | High | None | Required | Un- changed | High | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-127343 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTP | No | 5.9 | Network | High | Low | None | Un- changed | High | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-127363 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTP | No | 5.9 | Network | High | Low | None | Un- changed | High | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-114816 | Oracle Hyperion Planning | Security | HTTP | No | 5.9 | Network | High | Low | None | Un- changed | High | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-115145 | Oracle Hyperion Planning | Security | RMI | Yes | 5.9 | Network | High | None | None | Un- changed | High | None | None | 11.2.26.0.000 |  | 
| CVE-2026-114963 | Oracle Hyperion Profitability and Cost Management | Deployment | HTTP | No | 5.9 | Network | High | High | None | Un- changed | High | High | None | 11.2.26.0.000 |  | 
| CVE-2023-2976 | Oracle Hyperion Planning | Security (Google Guava) | HTTP | Yes | 5.6 | Network | High | None | None | Un- changed | Low | Low | Low | 11.2.26.0.000 |  | 
| CVE-2026-115013 | Oracle Hyperion Data Relationship Management | Access and security | None | No | 5.5 | Local | Low | Low | None | Un- changed | High | None | None | 11.2.26.0.000 |  | 
| CVE-2026-127377 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTP | No | 5.5 | Network | Low | High | None | Un- changed | Low | High | None | 11.2.26.0.000 |  | 
| CVE-2026-115090 | Oracle Hyperion Financial Close Management | Reconciliation Manage | None | No | 5.5 | Local | Low | Low | None | Un- changed | High | None | None | 11.2.26.0.000 |  | 
| CVE-2026-101702 | Oracle Hyperion Financial Data Quality Management, Enterprise Edition | Security | None | No | 5.5 | Local | Low | Low | None | Un- changed | High | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115085 | Oracle Hyperion Infrastructure Technology | Common Security | None | No | 5.5 | Local | Low | Low | None | Un- changed | High | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115162 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | None | No | 5.5 | Local | Low | Low | None | Un- changed | High | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115168 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | None | No | 5.5 | Local | Low | Low | None | Un- changed | High | None | None | 11.2.26.0.000 |  | 
| CVE-2026-114971 | Oracle Hyperion Profitability and Cost Management | Deployment | None | No | 5.5 | Local | Low | Low | None | Un- changed | High | None | None | 11.2.26.0.000 |  | 
| CVE-2026-114995 | Oracle Hyperion Data Relationship Management | Access and security | HTTP | No | 5.4 | Network | Low | Low | Required | Changed | Low | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-115003 | Oracle Hyperion Data Relationship Management | Access and security | HTTP | Yes | 5.4 | Network | Low | None | Required | Un- changed | Low | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-115024 | Oracle Hyperion Data Relationship Management | Access and security | HTTP | No | 5.4 | Network | Low | Low | None | Un- changed | Low | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-127358 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTP | No | 5.4 | Network | Low | Low | Required | Changed | Low | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-127374 | Oracle Hyperion Financial Close Management | Security | HTTP | Yes | 5.4 | Network | Low | None | Required | Un- changed | Low | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-115068 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | HTTP | Yes | 5.4 | Network | Low | None | Required | Un- changed | Low | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-115136 | Oracle Hyperion Planning | Application Development Framework | HTTP | No | 5.4 | Network | Low | Low | None | Un- changed | Low | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-115107 | Oracle Hyperion Planning | Security | HTTP | No | 5.4 | Network | Low | Low | Required | Changed | Low | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-115113 | Oracle Hyperion Planning | Security | HTTP | No | 5.4 | Network | Low | Low | Required | Changed | Low | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-114993 | Oracle Hyperion Data Relationship Management | Access and security | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | Low | None | None | 11.2.26.0.000 |  | 
| CVE-2026-114994 | Oracle Hyperion Data Relationship Management | Access and security | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | Low | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115017 | Oracle Hyperion Data Relationship Management | Access and security | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | None | None | Low | 11.2.26.0.000 |  | 
| CVE-2026-115027 | Oracle Hyperion Data Relationship Management | Access and security | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | Low | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115034 | Oracle Hyperion Data Relationship Management | Access and security | SOAP | Yes | 5.3 | Network | Low | None | None | Un- changed | Low | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115093 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTP | No | 5.3 | Network | High | Low | None | Un- changed | None | High | None | 11.2.26.0.000 |  | 
| CVE-2026-115096 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTP | No | 5.3 | Network | High | Low | None | Un- changed | None | High | None | 11.2.26.0.000 |  | 
| CVE-2026-115165 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTP | No | 5.3 | Network | High | Low | None | Un- changed | High | None | None | 11.2.26.0.000 |  | 
| CVE-2026-127341 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTP | No | 5.3 | Network | High | Low | None | Un- changed | High | None | None | 11.2.26.0.000 |  | 
| CVE-2026-127368 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | Low | None | None | 11.2.26.0.000 |  | 
| CVE-2026-127375 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | Low | None | None | 11.2.26.0.000 |  | 
| CVE-2026-127376 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | Low | None | None | 11.2.26.0.000 |  | 
| CVE-2026-127346 | Oracle Hyperion Financial Close Management | Reconciliation Manage | T3, IIOP | Yes | 5.3 | Adjacent Network | High | None | None | Un- changed | High | None | None | 11.2.26.0.000 |  | 
| CVE-2026-114812 | Oracle Hyperion Infrastructure Technology | Common Security | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | Low | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115167 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | Low | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115100 | Oracle Hyperion Planning | Security | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | Low | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115102 | Oracle Hyperion Planning | Security | HTTP | No | 5.3 | Network | High | Low | None | Un- changed | None | High | None | 11.2.26.0.000 |  | 
| CVE-2026-115106 | Oracle Hyperion Planning | Security | HTTP | Yes | 5.3 | Network | High | None | Required | Un- changed | None | High | None | 11.2.26.0.000 |  | 
| CVE-2026-115116 | Oracle Hyperion Planning | Security | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | Low | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115125 | Oracle Hyperion Planning | Security | HTTP | No | 5.3 | Network | High | Low | None | Un- changed | High | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115147 | Oracle Hyperion Planning | Security | HTTP | No | 5.3 | Network | High | Low | None | Un- changed | High | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115149 | Oracle Hyperion Planning | Security | HTTP | No | 5.3 | Network | High | Low | None | Un- changed | High | None | None | 11.2.26.0.000 |  | 
| CVE-2026-114974 | Oracle Hyperion Profitability and Cost Management | Deployment | HTTPS | Yes | 5.3 | Network | Low | None | None | Un- changed | Low | None | None | 11.2.26.0.000 |  | 
| CVE-2026-114960 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | None | No | 5.2 | Local | High | High | None | Un- changed | Low | Low | High | 11.2.26.0.000 |  | 
| CVE-2026-115031 | Oracle Hyperion Data Relationship Management | Access and security | SOAP | No | 5.0 | Network | Low | Low | None | Changed | Low | None | None | 11.2.26.0.000 |  | 
| CVE-2026-127365 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTP | Yes | 4.8 | Network | High | None | None | Un- changed | Low | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-114959 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | HTTP | Yes | 4.8 | Network | High | None | None | Un- changed | Low | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-115110 | Oracle Hyperion Planning | Security | HTTP | Yes | 4.8 | Network | High | None | None | Un- changed | Low | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-115111 | Oracle Hyperion Planning | Security | HTTP | Yes | 4.8 | Network | High | None | None | Un- changed | Low | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-115023 | Oracle Hyperion Data Relationship Management | Access and security | HTTP | Yes | 4.7 | Network | High | None | Required | Changed | Low | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-115004 | Oracle Hyperion Data Relationship Management | Access and security | None | No | 4.7 | Local | High | Low | None | Un- changed | High | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115083 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | HTTP | Yes | 4.7 | Network | High | None | Required | Changed | Low | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-115079 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | None | No | 4.7 | Local | High | Low | None | Un- changed | None | None | High | 11.2.26.0.000 |  | 
| CVE-2026-114996 | Oracle Hyperion Data Relationship Management | Access and security | None | No | 4.4 | Local | Low | High | None | Un- changed | High | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115011 | Oracle Hyperion Data Relationship Management | Access and security | None | No | 4.4 | Local | Low | High | None | Un- changed | High | None | None | 11.2.26.0.000 |  | 
| CVE-2026-127379 | Oracle Hyperion Financial Close Management | Reconciliation Manage | None | No | 4.4 | Local | Low | High | None | Un- changed | High | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115137 | Oracle Hyperion Planning | Security | HTTP | No | 4.4 | Network | High | Low | Required | Changed | Low | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-115008 | Oracle Hyperion Data Relationship Management | Access and security | HTTP | No | 4.3 | Network | Low | Low | None | Un- changed | Low | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115097 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTP | No | 4.3 | Network | Low | Low | None | Un- changed | Low | None | None | 11.2.26.0.000 |  | 
| CVE-2026-127344 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTP | No | 4.3 | Network | Low | Low | None | Un- changed | Low | None | None | 11.2.26.0.000 |  | 
| CVE-2026-127355 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTP | No | 4.3 | Network | Low | Low | None | Un- changed | None | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-115169 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | HTTP | No | 4.3 | Network | Low | Low | None | Un- changed | Low | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115103 | Oracle Hyperion Planning | Security | HTTP | No | 4.3 | Network | Low | Low | None | Un- changed | Low | None | None | 11.2.26.0.000 |  | 
| CVE-2026-114969 | Oracle Hyperion Profitability and Cost Management | Deployment | HTTP | No | 4.3 | Network | Low | Low | None | Un- changed | Low | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115109 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTP | No | 4.2 | Network | High | Low | None | Un- changed | Low | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-127356 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTP | Yes | 4.2 | Network | High | None | Required | Un- changed | Low | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-101550 | Oracle Hyperion Financial Management | Security | HTTP | No | 4.2 | Network | High | High | Required | Un- changed | High | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115135 | Oracle Hyperion Planning | Security | HTTP | No | 4.2 | Network | High | Low | None | Un- changed | Low | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-127367 | Oracle Hyperion Financial Close Management | Reconciliation Manage | None | No | 4.1 | Local | High | High | None | Un- changed | None | High | None | 11.2.26.0.000 |  | 
| CVE-2026-115015 | Oracle Hyperion Data Relationship Management | Access and security | HTTP | Yes | 3.7 | Network | High | None | None | Un- changed | Low | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115019 | Oracle Hyperion Data Relationship Management | Access and security | HTTP | Yes | 3.7 | Network | High | None | None | Un- changed | None | None | Low | 11.2.26.0.000 |  | 
| CVE-2026-115020 | Oracle Hyperion Data Relationship Management | Access and security | HTTP | Yes | 3.7 | Network | High | None | None | Un- changed | None | None | Low | 11.2.26.0.000 |  | 
| CVE-2026-115028 | Oracle Hyperion Data Relationship Management | Access and security | HTTP | Yes | 3.7 | Network | High | None | None | Un- changed | Low | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115098 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTP | Yes | 3.7 | Network | High | None | None | Un- changed | None | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-115118 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTP | Yes | 3.7 | Network | High | None | None | Un- changed | Low | None | None | 11.2.26.0.000 |  | 
| CVE-2026-127353 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTP | Yes | 3.7 | Network | High | None | None | Un- changed | None | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-127364 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTP | Yes | 3.7 | Network | High | None | None | Un- changed | Low | None | None | 11.2.26.0.000 |  | 
| CVE-2026-127378 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTP | Yes | 3.7 | Network | High | None | None | Un- changed | Low | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115108 | Oracle Hyperion Planning | Security | HTTP | Yes | 3.7 | Network | High | None | None | Un- changed | Low | None | None | 11.2.26.0.000 |  | 
| CVE-2022-23457 | Oracle Hyperion Planning | Security (Enterprise Security API for Java (Legacy)) | HTTP | Yes | 3.7 | Network | High | None | None | Un- changed | Low | None | None | 11.2.26.0.000 |  | 
| CVE-2026-114970 | Oracle Hyperion Profitability and Cost Management | Deployment | HTTP | Yes | 3.7 | Network | High | None | None | Un- changed | Low | None | None | 11.2.26.0.000 |  | 
| CVE-2026-127348 | Oracle Hyperion Financial Close Management | Reconciliation Manage | None | No | 3.6 | Local | High | None | Required | Un- changed | Low | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-115026 | Oracle Hyperion Data Relationship Management | Access and security | HTTP | No | 3.5 | Network | Low | Low | Required | Un- changed | None | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-115029 | Oracle Hyperion Data Relationship Management | Access and security | HTTP | Yes | 3.4 | Network | High | None | Required | Changed | None | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-114967 | Oracle Hyperion Profitability and Cost Management | Deployment | None | No | 3.4 | Local | Low | High | None | Un- changed | None | Low | Low | 11.2.26.0.000 |  | 
| CVE-2026-115012 | Oracle Hyperion Data Relationship Management | Access and security | None | No | 3.3 | Local | Low | Low | None | Un- changed | Low | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115033 | Oracle Hyperion Data Relationship Management | Access and security | None | No | 3.3 | Local | Low | Low | None | Un- changed | Low | None | None | 11.2.26.0.000 |  | 
| CVE-2026-127305 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTP | No | 3.3 | Network | High | High | None | Un- changed | Low | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-127366 | Oracle Hyperion Financial Close Management | Reconciliation Manage | None | No | 3.3 | Local | Low | Low | None | Un- changed | Low | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115075 | Oracle Hyperion Infrastructure Technology | Common Security | None | No | 3.3 | Local | Low | Low | None | Un- changed | Low | None | None | 11.2.26.0.000 |  | 
| CVE-2026-114966 | Oracle Hyperion Profitability and Cost Management | Deployment | None | No | 3.3 | Local | Low | Low | None | Un- changed | Low | None | None | 11.2.26.0.000 |  | 
| CVE-2026-114973 | Oracle Hyperion Profitability and Cost Management | Deployment | None | No | 3.3 | Local | Low | Low | None | Un- changed | Low | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115007 | Oracle Hyperion Data Relationship Management | Access and security | HTTP | Yes | 3.1 | Network | High | None | Required | Un- changed | Low | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115009 | Oracle Hyperion Data Relationship Management | Access and security | HTTP | No | 3.1 | Network | High | Low | None | Un- changed | Low | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115025 | Oracle Hyperion Data Relationship Management | Access and security | HTTP | No | 3.1 | Network | High | Low | None | Un- changed | Low | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115030 | Oracle Hyperion Data Relationship Management | Access and security | HTTP | No | 3.1 | Network | High | Low | None | Un- changed | Low | None | None | 11.2.26.0.000 |  | 
| CVE-2026-127345 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTP | No | 3.1 | Network | High | Low | None | Un- changed | None | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-127354 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTP | No | 3.1 | Network | High | Low | None | Un- changed | Low | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115180 | Oracle Hyperion Financial Close Management | Reconciliation Manage | SMTP | Yes | 3.1 | Adjacent Network | High | None | None | Un- changed | Low | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115073 | Oracle Hyperion Infrastructure Technology | Common Security | HTTP | No | 3.1 | Network | High | Low | None | Un- changed | Low | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115084 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | HTTP | Yes | 3.1 | Network | High | None | Required | Un- changed | None | Low | None | 11.2.26.0.000 |  | 
| CVE-2021-35043 | Oracle Hyperion Planning | Application Development Framework (AntiSamy) | HTTP | No | 3.1 | Network | High | Low | None | Un- changed | None | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-114968 | Oracle Hyperion Profitability and Cost Management | Deployment | HTTP | No | 3.1 | Network | High | Low | None | Un- changed | None | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-115115 | Oracle Hyperion Financial Close Management | Reconciliation Manage | None | No | 3.0 | Local | High | High | None | Un- changed | Low | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-114961 | Oracle Hyperion Infrastructure Technology | Installation and Configuration | None | No | 3.0 | Local | High | High | None | Un- changed | None | Low | Low | 11.2.26.0.000 |  | 
| CVE-2026-127417 | Oracle Hyperion Infrastructure Technology | Lifecycle Management | HTTP | No | 2.7 | Network | Low | High | None | Un- changed | Low | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115104 | Oracle Hyperion Financial Close Management | Reconciliation Manage | None | No | 2.5 | Local | High | Low | None | Un- changed | Low | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115123 | Oracle Hyperion Planning | Application Development Framework | None | No | 2.5 | Local | High | Low | None | Un- changed | Low | None | None | 11.2.26.0.000 |  | 
| CVE-2026-114957 | Oracle Hyperion Planning | Security | None | No | 2.5 | Local | High | Low | None | Un- changed | None | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-127361 | Oracle Hyperion Financial Close Management | Reconciliation Manage | HTTP | No | 2.0 | Network | High | High | Required | Un- changed | None | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-115010 | Oracle Hyperion Data Relationship Management | Access and security | None | No | 1.9 | Local | High | High | None | Un- changed | None | None | Low | 11.2.26.0.000 |  | 
| CVE-2026-115171 | Oracle Hyperion Financial Close Management | Reconciliation Manage | None | No | 1.9 | Local | High | High | None | Un- changed | None | Low | None | 11.2.26.0.000 |  | 
| CVE-2026-115174 | Oracle Hyperion Financial Close Management | Reconciliation Manage | None | No | 1.9 | Local | High | High | None | Un- changed | Low | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115114 | Oracle Hyperion Planning | Security | None | No | 1.9 | Local | High | High | None | Un- changed | Low | None | None | 11.2.26.0.000 |  | 
| CVE-2026-115152 | Oracle Hyperion Planning | Security | None | No | 1.9 | Local | High | High | None | Un- changed | Low | None | None | 11.2.26.0.000 |  | 

This Critical Security Patch Update contains 11 new security patches for Oracle Java SE.  All of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cspunov2026verbose.html#JAVA)

The CVSS scores below assume that a user running a Java applet or Java Web Start application has administrator privileges (typical on Windows). When the user does not run with administrator privileges (typical on Solaris and Linux), the corresponding CVSS impact scores for Confidentiality, Integrity, and Availability are "Low" instead of "High", lowering the CVSS Base Score. For example, a Base Score of 9.6 becomes 7.1.


Java Management Service, available to all users, can help you find vulnerable Java versions in your systems. Java SE Subscribers and customers running in Oracle Cloud can use Java Management Service to update Java Runtimes and to do further security reviews like identifying potentially vulnerable third party libraries used by your Java programs. Existing Java Management Service user [click here](https://cloud.oracle.com/jms/overview) to log in to your dashboard. [The Java Management Service Documentation](https://docs.oracle.com/en-us/iaas/jms/index.html) provides a list of features available to everyone and those available only to customers. [Learn more about using Java Management Service](https://www.oracle.com/java/jms/) to monitor and secure your Java Installations.

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-114938 | Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition | Compiler | Multiple | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | Oracle Java SE: 8u511b33-perf, 17.0.21.0.3, 21.0.13.0.3, 25.0.5.0.3, 27.0.1.0.3; Oracle GraalVM for JDK: 17.0.21.0.3, 21.0.13.0.3; Oracle GraalVM Enterprise Edition: 21.3.20.0.3 | See Note 1 | 
| CVE-2026-86144 | Oracle Java SE, Oracle JavaFX | JavaFX (libxml2) | Multiple | Yes | 7.5 | Network | High | None | Required | Un- changed | High | High | High | Oracle Java SE: 8u511b33; Oracle JavaFX: 21.0.13, 25.0.5, 27.0.1 | See Note 2 | 
| CVE-2026-114939 | Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition | JGSS | Multiple | Yes | 7.4 | Network | High | None | None | Un- changed | High | High | None | Oracle Java SE: 8u511b33, 8u511b33-perf, 11.0.33.0.3, 17.0.21.0.3, 21.0.13.0.3, 25.0.5.0.3, 27.0.1.0.3; Oracle GraalVM for JDK: 17.0.21.0.3, 21.0.13.0.3; Oracle GraalVM Enterprise Edition: 21.3.20.0.3 | See Note 2 | 
| CVE-2026-114940 | Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition | JSSE | TLS | Yes | 7.4 | Network | High | None | None | Un- changed | High | High | None | Oracle Java SE: 8u511b33, 8u511b33-perf, 11.0.33.0.3, 17.0.21.0.3, 21.0.13.0.3, 25.0.5.0.3, 27.0.1.0.3; Oracle GraalVM for JDK: 17.0.21.0.3, 21.0.13.0.3; Oracle GraalVM Enterprise Edition: 21.3.20.0.3 | See Note 3 | 
| CVE-2026-114941 | Oracle Java SE, Oracle GraalVM for JDK | Compiler | Multiple | Yes | 7.0 | Network | High | None | None | Un- changed | Low | Low | High | Oracle Java SE: 21.0.13.0.3, 25.0.5.0.3, 27.0.1.0.3; Oracle GraalVM for JDK: 21.0.13.0.3 | See Note 1 | 
| CVE-2026-114942 | Oracle Java SE, Oracle GraalVM for JDK | Libraries | Multiple | Yes | 7.0 | Network | High | None | None | Un- changed | Low | Low | High | Oracle Java SE: 21.0.13.0.3, 25.0.5.0.3, 27.0.1.0.3; Oracle GraalVM for JDK: 21.0.13.0.3 | See Note 1 | 
| CVE-2026-114943 | Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition | Hotspot | Multiple | Yes | 6.5 | Network | High | None | None | Un- changed | None | Low | High | Oracle Java SE: 8u511b33-perf, 11.0.33.0.3, 17.0.21.0.3, 21.0.13.0.3, 25.0.5.0.3, 27.0.1.0.3; Oracle GraalVM for JDK: 17.0.21.0.3, 21.0.13.0.3; Oracle GraalVM Enterprise Edition: 21.3.20.0.3 | See Note 3 | 
| CVE-2026-114944 | Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition | Core Java Libraries | Multiple | Yes | 5.9 | Network | High | None | None | Un- changed | None | High | None | Oracle Java SE: 8u511b33, 8u511b33-perf, 11.0.33.0.3, 17.0.21.0.3, 21.0.13.0.3, 25.0.5.0.3, 27.0.1.0.3; Oracle GraalVM for JDK: 17.0.21.0.3, 21.0.13.0.3; Oracle GraalVM Enterprise Edition: 21.3.20.0.3 | See Note 3 | 
| CVE-2026-114945 | Oracle Java SE, Oracle GraalVM for JDK | Libraries | Multiple | Yes | 5.3 | Network | Low | None | None | Un- changed | None | Low | None | Oracle Java SE: 21.0.13.0.3, 25.0.5.0.3, 27.0.1.0.3; Oracle GraalVM for JDK: 21.0.13.0.3 | See Note 3 | 
| CVE-2026-114946 | Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition | Compiler | Multiple | Yes | 4.8 | Network | High | None | None | Un- changed | Low | Low | None | Oracle Java SE: 8u511b33, 8u511b33-perf, 11.0.33.0.3, 17.0.21.0.3, 21.0.13.0.3, 25.0.5.0.3, 27.0.1.0.3; Oracle GraalVM for JDK: 17.0.21.0.3, 21.0.13.0.3; Oracle GraalVM Enterprise Edition: 21.3.20.0.3 | See Note 3 | 
| CVE-2026-114947 | Oracle Java SE | JSSE | TLS | Yes | 3.7 | Network | High | None | None | Un- changed | None | Low | None | Oracle Java SE: 25.0.5.0.3, 27.0.1.0.3 | See Note 2 | 

1. This vulnerability can only be exploited by supplying data to APIs in the specified Component without using Untrusted Java Web Start applications or Untrusted Java applets, such as through a web service.
2. This vulnerability applies to Java deployments, typically in clients running sandboxed Java Web Start applications or sandboxed Java applets, that load and run untrusted code (e.g., code that comes from the internet) and rely on the Java sandbox for security. This vulnerability does not apply to Java deployments, typically in servers, that load and run only trusted code (e.g., code installed by an administrator).
3. This vulnerability can be exploited by using APIs in the specified Component, e.g., through a web service which supplies data to the APIs. This vulnerability also applies to Java deployments, typically in clients running sandboxed Java Web Start applications or sandboxed Java applets, that load and run untrusted code (e.g., code that comes from the internet) and rely on the Java sandbox for security.

- The patch for CVE-2026-86144 also addresses CVE-2026-86137, CVE-2026-86138, CVE-2026-86139, CVE-2026-86140, CVE-2026-86141, CVE-2026-86142, and CVE-2026-86143.

This Critical Security Patch Update contains 1 new security patch for Oracle JD Edwards.  This vulnerability is not remotely exploitable without authentication, i.e., may not be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cspunov2026verbose.html#JDE)

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-114926 | JD Edwards EnterpriseOne Localizations | LATAM | None | No | 6.5 | Local | Low | Low | None | Changed | High | None | None | 9.2 |  | 

This Critical Security Patch Update contains 10 new security patches for Oracle MySQL.  3 of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cspunov2026verbose.html#MSQL)

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-115557 | MySQL Shell | Shell: Core Client (Python) | HTTP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 26.10.0 |  | 
| CVE-2026-114952 | MySQL Server, MySQL Cluster | Client programs | MySQL Protocol | Yes | 9.1 | Network | Low | None | None | Un- changed | High | High | None | MySQL Server: 8.4.0-8.4.13, 9.7.0-9.7.4, 26.10; MySQL Cluster: 8.0.0-8.0.50, 8.4.0-8.4.13, 9.7.0-9.7.4, 26.10 |  | 
| CVE-2026-92392 | MySQL Server, MySQL Cluster | Server: Packaging (curl) | HTTP/2 | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | MySQL Server: 8.4.0-8.4.13, 9.7.0-9.7.4, 26.10; MySQL Cluster: 8.0.0-8.0.50, 8.4.0-8.4.13, 9.7.0-9.7.4, 26.10 |  | 
| CVE-2026-114951 | MySQL Server, MySQL Cluster | Server: Logging | MySQL Protocol | No | 7.2 | Network | Low | High | None | Un- changed | High | High | High | MySQL Server: 8.4.0-8.4.13, 9.7.0-9.7.4, 26.10; MySQL Cluster: 8.0.0-8.0.50, 8.4.0-8.4.13, 9.7.0-9.7.4, 26.10 |  | 
| CVE-2026-114950 | MySQL Server, MySQL Cluster | Server: Optimizer | MySQL Protocol | No | 7.2 | Network | Low | High | None | Un- changed | High | High | High | MySQL Server: 8.4.0-8.4.13, 9.7.0-9.7.4, 26.10; MySQL Cluster: 8.0.0-8.0.50, 8.4.0-8.4.13, 9.7.0-9.7.4, 26.10 |  | 
| CVE-2026-114949 | MySQL Server, MySQL Cluster | Server: Replication | MySQL Protocol | No | 7.2 | Network | Low | High | None | Un- changed | High | High | High | MySQL Server: 8.4.0-8.4.13, 9.7.0-9.7.4, 26.10; MySQL Cluster: 8.0.0-8.0.50, 8.4.0-8.4.13, 9.7.0-9.7.4, 26.10 |  | 
| CVE-2026-127428 | MySQL Server, MySQL Cluster | Server: GIS | MySQL Protocol | No | 7.1 | Network | Low | Low | None | Un- changed | Low | None | High | MySQL Server: 8.4.0-8.4.13, 9.7.0-9.7.4, 26.10; MySQL Cluster: 8.0.0-8.0.50, 8.4.0-8.4.13, 9.7.0-9.7.4, 26.10 |  | 
| CVE-2026-114953 | MySQL Server, MySQL Cluster | Server: Replication | MySQL Protocol | No | 6.5 | Network | Low | Low | None | Un- changed | None | None | High | MySQL Server: 8.4.0-8.4.13, 9.7.0-9.7.4, 26.10; MySQL Cluster: 8.0.0-8.0.50, 8.4.0-8.4.13, 9.7.0-9.7.4, 26.10 |  | 
| CVE-2026-114122 | MySQL Workbench | Workbench (electron) | None | No | 3.9 | Local | High | High | None | Changed | Low | None | Low | 26.10.0 |  | 
| CVE-2026-114948 | MySQL Cluster | Cluster: JS module | None | No | 2.5 | Local | High | Low | None | Un- changed | Low | None | None | 8.0.0-8.0.50, 8.4.0-8.4.13, 9.7.0-9.7.4, 26.10 |  | 

- The patch for CVE-2026-114122 also addresses CVE-2026-113800 and CVE-2026-114124.
- The patch for CVE-2026-115557 also addresses CVE-2024-3220, CVE-2026-102633, CVE-2026-114583, and CVE-2026-77214.
- The patch for CVE-2026-92392 also addresses CVE-2026-107928, CVE-2026-107929, CVE-2026-86409, CVE-2026-86410, CVE-2026-86411, CVE-2026-86412, CVE-2026-86413, CVE-2026-86414, CVE-2026-86415, CVE-2026-87861, CVE-2026-87862, CVE-2026-87863, CVE-2026-87864, CVE-2026-87865, CVE-2026-87866, CVE-2026-92386, CVE-2026-92387, CVE-2026-92388, CVE-2026-92389, CVE-2026-92390, CVE-2026-92391, CVE-2026-94265, and CVE-2026-94266.

This Critical Security Patch Update contains 13 new security patches for Oracle PeopleSoft.  6 of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cspunov2026verbose.html#PS)

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-111497 | PeopleSoft Enterprise PeopleTools | OpenSearch Dashboards (Node.js) | HTTP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 8.61-8.63 |  | 
| CVE-2026-114934 | PeopleSoft Enterprise PeopleTools | Integration Broker | HTTP | Yes | 9.3 | Network | Low | None | None | Changed | High | Low | None | 8.61-8.63 |  | 
| CVE-2026-114862 | PeopleSoft Enterprise PeopleTools | Weblogic | HTTP | Yes | 9.1 | Network | Low | None | None | Un- changed | High | High | None | 8.61-8.63 |  | 
| CVE-2026-114928 | PeopleSoft Enterprise PeopleTools | Application Server | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 8.61-8.63 |  | 
| CVE-2026-114937 | PeopleSoft Enterprise PeopleTools | Updates Environment Mgmt | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 8.61-8.63 |  | 
| CVE-2024-41311 | PeopleSoft Enterprise PeopleTools | XML Publisher (libheif) | HTTP | Yes | 8.8 | Network | Low | None | Required | Un- changed | High | High | High | 8.61-8.63 |  | 
| CVE-2026-114932 | PeopleSoft Enterprise PeopleTools | Test Framework | HTTP | No | 8.7 | Network | Low | High | None | Changed | High | High | None | 8.61-8.63 |  | 
| CVE-2026-114933 | PeopleSoft Enterprise PeopleTools | Security | HTTP | Yes | 8.2 | Network | Low | None | None | Un- changed | High | Low | None | 8.61-8.63 |  | 
| CVE-2026-114931 | PeopleSoft Enterprise PeopleTools | Test Framework | None | No | 7.8 | Local | High | Low | None | Changed | High | High | High | 8.61-8.63 |  | 
| CVE-2026-114929 | PeopleSoft Enterprise PeopleTools | Application Server | HTTP | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 8.61-8.63 |  | 
| CVE-2026-114930 | PeopleSoft Enterprise PeopleTools | Application Server | HTTP | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 8.61-8.63 |  | 
| CVE-2026-114935 | PeopleSoft Enterprise PeopleTools | Integration Broker | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | High | None | None | 8.61-8.63 |  | 
| CVE-2026-114927 | PeopleSoft Enterprise PeopleTools | Report Distribution | HTTP | No | 7.2 | Network | Low | High | None | Un- changed | High | High | High | 8.61-8.63 |  | 

- The patch for CVE-2024-41311 also addresses CVE-2024-38949.
- The patch for CVE-2026-111497 also addresses CVE-2026-105481, CVE-2026-105482, CVE-2026-105483, CVE-2026-106069, CVE-2026-106070, CVE-2026-106071, CVE-2026-106072, CVE-2026-106073, and CVE-2026-106074.

This Critical Security Patch Update contains 19 new security patches for Oracle Siebel CRM.  9 of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cspunov2026verbose.html#SECR)

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-115035 | Siebel CRM Deployment | Siebel Remote | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 17.0-26.9 |  | 
| CVE-2026-115044 | Siebel CRM Integration | EAI | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 17.0-26.9 |  | 
| CVE-2026-114976 | Siebel CRM Deployment | Cloud Gateway | HTTP | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 22.3-26.9 |  | 
| CVE-2026-68497 | Siebel CRM Administration | Data Archival (jackson-databind) | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 25.12-26.9 |  | 
| CVE-2026-54428 | Siebel CRM Administration | Data Archival (Apache HttpComponents) | HTTP/2 | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 25.12-26.9 |  | 
| CVE-2026-114977 | Siebel CRM Deployment | Siebel Management Console | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | High | None | None | 17.0-26.9 |  | 
| CVE-2026-54428 | Siebel CRM End User | Open UI (Apache HttpComponents) | HTTP/2 | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 17.0-26.9 |  | 
| CVE-2026-40984 | Siebel CRM Integration | Open Integration (Requests) | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 25.12-26.9 |  | 
| CVE-2026-59949 | Siebel CRM Integration | Open Integration (lz4-java) | HTTP | Yes | 6.5 | Network | High | None | None | Un- changed | Low | None | High | 25.12-26.9 |  | 
| CVE-2026-127410 | Siebel CRM Development | Integration - Scripting | None | No | 6.3 | Local | High | Low | None | Un- changed | High | High | None | 17.0-26.9 |  | 
| CVE-2026-115038 | Siebel CRM Deployment | Server Infrastructure | None | No | 6.0 | Local | Low | High | None | Un- changed | High | None | High | 17.0-26.9 |  | 
| CVE-2026-115037 | Siebel CRM Deployment | Server Infrastructure | TCP | Yes | 5.9 | Network | High | None | None | Un- changed | None | None | High | 17.0-26.9 |  | 
| CVE-2026-115036 | Siebel CRM Deployment | Server Infrastructure | None | No | 5.5 | Local | Low | Low | None | Un- changed | High | None | None | 17.0-26.9 |  | 
| CVE-2026-115052 | Siebel CRM Deployment | Siebel Remote | None | No | 5.5 | Local | Low | Low | None | Un- changed | High | None | None | 17.0-26.9 |  | 
| CVE-2026-115039 | Siebel CRM Deployment | Server Infrastructure | HTTP | No | 5.3 | Network | High | Low | None | Un- changed | None | None | High | 17.0-26.9 |  | 
| CVE-2026-115043 | Siebel CRM Deployment | Server Infrastructure | HTTP | Yes | 4.8 | Network | High | None | None | Un- changed | Low | None | Low | 17.0-26.9 |  | 
| CVE-2026-115042 | Siebel CRM Deployment | Server Infrastructure | None | No | 4.4 | Local | Low | High | None | Un- changed | High | None | None | 17.0-26.9 |  | 
| CVE-2026-115041 | Siebel CRM Deployment | Server Infrastructure | None | No | 3.3 | Local | Low | Low | None | Un- changed | None | None | Low | 17.0-26.9 |  | 
| CVE-2026-115040 | Siebel CRM Deployment | Server Infrastructure | None | No | 1.9 | Local | High | High | None | Un- changed | Low | None | None | 17.0-26.9 |  | 

- The patch for CVE-2026-40984 also addresses CVE-2026-40983.
- The patch for CVE-2026-68497 also addresses CVE-2026-19032 and CVE-2026-83557.
- The patch for CVE-2026-54428 also addresses CVE-2026-40983, CVE-2026-40984, and CVE-2026-54399.

This Critical Security Patch Update contains 74 new security patches for Oracle Supply Chain.  36 of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cspunov2026verbose.html#SCP)

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-114980 | Oracle AutoVue | Security Related Issues | HTTP | No | 9.9 | Network | Low | Low | None | Changed | High | High | High | 21.1.0 |  | 
| CVE-2026-127324 | Oracle AutoVue | Security | HTTP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 21.1.0 |  | 
| CVE-2026-127325 | Oracle AutoVue | Security | HTTP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 21.1.0 |  | 
| CVE-2026-127326 | Oracle AutoVue | Security | HTTP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 21.1.0 |  | 
| CVE-2026-127327 | Oracle AutoVue | Security | HTTP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 21.1.0 |  | 
| CVE-2026-101356 | Oracle Agile PLM | File Manager (Apache Tomcat) | HTTP/2 | Yes | 9.1 | Network | Low | None | None | Un- changed | High | None | High | 9.3.6 |  | 
| CVE-2026-127307 | Oracle AutoVue | Security | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 21.1.0 |  | 
| CVE-2026-127334 | Oracle AutoVue | Security | HTTP | No | 8.8 | Network | Low | Low | None | Un- changed | High | High | High | 21.1.0 |  | 
| CVE-2026-127306 | Oracle AutoVue | Security Related Issues | HTTP | Yes | 8.6 | Network | Low | None | None | Changed | High | None | None | 21.1.0 |  | 
| CVE-2026-127308 | Oracle AutoVue | Security | HTTP | Yes | 8.1 | Network | Low | None | Required | Un- changed | High | High | None | 21.1.0 |  | 
| CVE-2026-127328 | Oracle AutoVue | Security | HTTP | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 21.1.0 |  | 
| CVE-2026-127329 | Oracle AutoVue | Security | HTTP | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 21.1.0 |  | 
| CVE-2026-127330 | Oracle AutoVue | Security | HTTP | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 21.1.0 |  | 
| CVE-2026-127402 | Oracle AutoVue | Security | HTTP | Yes | 8.1 | Network | High | None | None | Un- changed | High | High | High | 21.1.0 |  | 
| CVE-2026-127337 | Oracle AutoVue | Security | None | No | 7.9 | Local | Low | None | None | Changed | High | Low | None | 21.1.0 |  | 
| CVE-2022-38171 | Oracle AutoVue | Security (xpdf) | None | No | 7.8 | Local | Low | None | Required | Un- changed | High | High | High | 21.1.0.7 |  | 
| CVE-2026-127392 | Product Lifecycle Analytics | Installation Issues | None | No | 7.7 | Local | High | Low | None | Changed | High | High | Low | 3.6.1 |  | 
| CVE-2026-127331 | Oracle AutoVue | Security | HTTP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 21.1.0 |  | 
| CVE-2026-114981 | Oracle AutoVue | Security Related Issues | HTTP | No | 7.5 | Network | High | Low | None | Un- changed | High | High | High | 21.1.0 |  | 
| CVE-2026-127394 | Product Lifecycle Analytics | Installation Issues | None | No | 7.2 | Local | High | Low | Required | Changed | High | High | None | 3.6.1 |  | 
| CVE-2026-127319 | Oracle AutoVue | Security | HTTP | No | 7.1 | Network | Low | Low | None | Un- changed | High | Low | None | 21.1.0 |  | 
| CVE-2026-127339 | Oracle AutoVue | Security | None | No | 7.1 | Local | Low | None | None | Changed | None | High | None | 21.1.0 |  | 
| CVE-2026-101563 | Oracle Agile PLM | Security | HTTP | No | 6.8 | Network | High | Low | None | Un- changed | High | High | None | 9.3.6 |  | 
| CVE-2026-127320 | Oracle AutoVue | Security | HTTP | Yes | 6.8 | Adjacent Network | High | None | None | Un- changed | High | High | None | 21.1.0 |  | 
| CVE-2026-114984 | Oracle AutoVue | Security Related Issues | HTTP | No | 6.8 | Network | High | Low | None | Un- changed | None | High | High | 21.1.0 |  | 
| CVE-2026-127313 | Oracle AutoVue | Security | HTTPS | Yes | 6.8 | Adjacent Network | High | None | None | Un- changed | High | High | None | 21.1.0 |  | 
| CVE-2026-127408 | Oracle Agile Engineering Data Management | Engineering Communication Interface | None | No | 6.7 | Local | Low | High | None | Un- changed | High | High | High | 6.2.1 |  | 
| CVE-2026-127400 | Oracle Agile Product Lifecycle Management for Process | Product Quality Management | HTTP | No | 6.6 | Network | High | High | None | Un- changed | High | High | High | 6.2.4 |  | 
| CVE-2026-127390 | Product Lifecycle Analytics | Installation Issues | HTTP | No | 6.6 | Network | High | High | None | Un- changed | High | High | High | 3.6.1 |  | 
| CVE-2026-127405 | Oracle Agile Engineering Data Management | Engineering Communication Interface | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 6.2.1 |  | 
| CVE-2026-127384 | Oracle Agile PLM | Folders, Files & Attachments | HTTP | Yes | 6.5 | Network | Low | None | Required | Un- changed | High | None | None | 9.3.6 |  | 
| CVE-2026-127396 | Oracle Agile Product Lifecycle Management for Process | Product Quality Management | HTTP | Yes | 6.5 | Network | Low | None | None | Un- changed | Low | Low | None | 6.2.4 |  | 
| CVE-2026-127310 | Oracle AutoVue | Security | HTTP | No | 6.5 | Network | Low | Low | None | Un- changed | High | None | None | 21.1.0 |  | 
| CVE-2026-127393 | Product Lifecycle Analytics | Installation Issues | None | No | 6.5 | Local | Low | Low | None | Changed | High | None | None | 3.6.1 |  | 
| CVE-2026-127385 | Oracle Agile PLM | Gantt Chart | HTTP | No | 6.4 | Network | High | Low | Required | Un- changed | High | High | None | 9.3.6 |  | 
| CVE-2026-127403 | Oracle Agile Engineering Data Management | Engineering Communication Interface | TCP | No | 6.3 | Network | High | Low | None | Changed | High | None | None | 6.2.1 |  | 
| CVE-2026-114989 | Oracle AutoVue | Security Related Issues | HTTP | No | 6.3 | Network | Low | Low | None | Un- changed | Low | Low | Low | 21.1.0 |  | 
| CVE-2026-127380 | Oracle Agile PLM | Import | HTTP | Yes | 6.1 | Network | Low | None | Required | Changed | Low | Low | None | 9.3.6 |  | 
| CVE-2026-127381 | Oracle Agile PLM | Web Client | HTTP | Yes | 6.1 | Network | Low | None | Required | Changed | Low | Low | None | 9.3.6 |  | 
| CVE-2026-127383 | Oracle Agile PLM | Web Client | HTTP | Yes | 6.1 | Network | Low | None | Required | Changed | Low | Low | None | 9.3.6 |  | 
| CVE-2026-127395 | Oracle Agile Product Lifecycle Management for Process | Product Quality Management | HTTP | Yes | 6.1 | Network | Low | None | Required | Changed | Low | Low | None | 6.2.4 |  | 
| CVE-2026-127311 | Oracle AutoVue | Security | HTTP | Yes | 6.1 | Network | Low | None | Required | Changed | Low | Low | None | 21.1.0 |  | 
| CVE-2026-114982 | Oracle AutoVue | Security Related Issues | None | No | 6.0 | Local | Low | High | None | Un- changed | None | High | High | 21.1.0 |  | 
| CVE-2026-127382 | Oracle Agile PLM | Security | HTTP | Yes | 5.9 | Network | High | None | None | Un- changed | High | None | None | 9.3.6 |  | 
| CVE-2026-127387 | Oracle Agile PLM | Security | HTTP | Yes | 5.9 | Network | High | None | None | Un- changed | High | None | None | 9.3.6 |  | 
| CVE-2026-127321 | Oracle AutoVue | Security | HTTP | Yes | 5.9 | Network | High | None | None | Un- changed | High | None | None | 21.1.0 |  | 
| CVE-2026-127336 | Oracle AutoVue | Security | HTTP | Yes | 5.9 | Network | High | None | Required | Un- changed | High | Low | None | 21.1.0 |  | 
| CVE-2026-127391 | Product Lifecycle Analytics | Installation Issues | None | No | 5.7 | Local | High | High | None | Un- changed | High | High | None | 3.6.1 |  | 
| CVE-2026-127386 | Oracle Agile PLM | Security | HTTP | Yes | 5.6 | Network | High | None | None | Un- changed | Low | Low | Low | 9.3.6 |  | 
| CVE-2026-114983 | Oracle AutoVue | Security Related Issues | HTTP | Yes | 5.6 | Network | High | None | None | Un- changed | Low | Low | Low | 21.1.0 |  | 
| CVE-2026-127389 | Oracle Agile PLM | Security | HTTP | No | 5.5 | Network | Low | High | None | Un- changed | High | Low | None | 9.3.6 |  | 
| CVE-2026-127398 | Oracle Agile Product Lifecycle Management for Process | Product Quality Management | HTTP | Yes | 5.4 | Network | Low | None | Required | Un- changed | Low | Low | None | 6.2.4 |  | 
| CVE-2026-127399 | Oracle Agile Product Lifecycle Management for Process | Product Quality Management | HTTP | No | 5.4 | Network | Low | Low | Required | Changed | Low | Low | None | 6.2.4 |  | 
| CVE-2026-127312 | Oracle AutoVue | Security | HTTP | Yes | 5.4 | Network | Low | None | Required | Un- changed | Low | Low | None | 21.1.0 |  | 
| CVE-2026-127388 | Oracle Agile PLM | Folders, Files & Attachments | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | Low | None | None | 9.3.6 |  | 
| CVE-2026-127401 | Oracle Agile Product Lifecycle Management for Process | Product Quality Management | HTTP | No | 5.3 | Network | High | Low | None | Un- changed | None | None | High | 6.2.4 |  | 
| CVE-2026-127309 | Oracle AutoVue | Security | HTTP | Yes | 5.3 | Network | Low | None | None | Un- changed | Low | None | None | 21.1.0 |  | 
| CVE-2026-127322 | Oracle AutoVue | Security | HTTP | Yes | 5.3 | Network | High | None | Required | Un- changed | High | None | None | 21.1.0 |  | 
| CVE-2026-127404 | Oracle Agile Engineering Data Management | Engineering Communication Interface | HTTP | No | 5.0 | Network | High | High | None | Un- changed | Low | High | None | 6.2.1 |  | 
| CVE-2026-127409 | Oracle Agile Engineering Data Management | Engineering Communication Interface | HTTP | Yes | 4.8 | Network | High | None | None | Un- changed | Low | Low | None | 6.2.1 |  | 
| CVE-2026-127406 | Oracle Agile Engineering Data Management | Engineering Communication Interface | None | No | 4.5 | Local | High | Low | None | Un- changed | Low | Low | Low | 6.2.1 |  | 
| CVE-2026-127397 | Oracle Agile Product Lifecycle Management for Process | Product Quality Management | HTTP | No | 4.3 | Network | Low | Low | None | Un- changed | Low | None | None | 6.2.4 |  | 
| CVE-2026-114990 | Oracle AutoVue | Core | HTTP | No | 4.3 | Network | Low | Low | None | Un- changed | None | None | Low | 21.1.0 |  | 
| CVE-2026-114991 | Oracle AutoVue | Security Related Issues | HTTP | No | 4.3 | Network | Low | Low | None | Un- changed | None | None | Low | 21.1.0 |  | 
| CVE-2026-127333 | Oracle AutoVue | Security | Multiple | Yes | 4.3 | Adjacent Network | Low | None | None | Un- changed | Low | None | None | 21.1.0 |  | 
| CVE-2026-127332 | Oracle AutoVue | Security | None | No | 4.0 | Local | High | None | None | Un- changed | None | Low | Low | 21.1.0 |  | 
| CVE-2026-127323 | Oracle AutoVue | Security | HTTP | Yes | 3.7 | Network | High | None | None | Un- changed | Low | None | None | 21.1.0 |  | 
| CVE-2026-114988 | Oracle AutoVue | Security Related Issues | None | No | 3.6 | Local | High | Low | None | Un- changed | Low | Low | None | 21.1.0 |  | 
| CVE-2026-114987 | Oracle AutoVue | Security Related Issues | None | No | 3.4 | Local | Low | High | None | Un- changed | Low | None | Low | 21.1.0 |  | 
| CVE-2026-127407 | Oracle Agile Engineering Data Management | Engineering Communication Interface | None | No | 3.3 | Local | Low | Low | None | Un- changed | Low | None | None | 6.2.1 |  | 
| CVE-2026-127314 | Oracle AutoVue | Security | None | No | 3.3 | Local | Low | Low | None | Un- changed | Low | None | None | 21.1.0.7 |  | 
| CVE-2026-127318 | Oracle AutoVue | Security | HTTP | Yes | 3.1 | Adjacent Network | High | None | None | Un- changed | Low | None | None | 21.1.0.7 |  | 
| CVE-2026-114985 | Oracle AutoVue | Security Related Issues | None | No | 3.0 | Local | High | High | None | Un- changed | None | Low | Low | 21.1.0.7 |  | 
| CVE-2026-114986 | Oracle AutoVue | Security Related Issues | None | No | 3.0 | Local | High | High | None | Un- changed | None | Low | Low | 21.1.0.7 |  | 

- The patch for CVE-2026-101356 also addresses CVE-2026-101296, CVE-2026-68569, CVE-2026-74048, CVE-2026-74049, CVE-2026-88041, and CVE-2026-93446.

This Critical Security Patch Update contains 11 new security patches for Oracle Virtualization.  3 of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cspunov2026verbose.html#OVIR)

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-127421 | Oracle VM VirtualBox | Core | None | No | 8.6 | Local | Low | None | Required | Changed | High | High | High | 7.2.22 |  | 
| CVE-2026-127425 | Oracle VM VirtualBox | Core | None | No | 8.1 | Local | Low | High | None | Changed | Low | High | High | 7.2.22 |  | 
| CVE-2026-127413 | Oracle VM VirtualBox | Core | RDP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 7.2.22 |  | 
| CVE-2026-127427 | Oracle VM VirtualBox | Core | RDP | Yes | 7.5 | Network | Low | None | None | Un- changed | None | None | High | 7.2.22 |  | 
| CVE-2026-127426 | Oracle VM VirtualBox | Core | TFTP | Yes | 7.4 | Adjacent Network | Low | None | None | Changed | High | None | None | 7.2.22 |  | 
| CVE-2026-127414 | Oracle VM VirtualBox | Core | None | No | 7.1 | Local | Low | None | Required | Un- changed | None | High | High | 7.2.22 |  | 
| CVE-2026-127422 | Oracle VM VirtualBox | Core | None | No | 7.1 | Local | Low | None | Required | Un- changed | None | High | High | 7.2.22 |  | 
| CVE-2026-127423 | Oracle VM VirtualBox | Core | None | No | 7.1 | Local | Low | None | Required | Un- changed | None | High | High | 7.2.22 |  | 
| CVE-2026-127411 | Oracle VM VirtualBox | Core | None | No | 6.7 | Local | Low | High | None | Changed | Low | None | High | 7.2.22 |  | 
| CVE-2026-127412 | Oracle VM VirtualBox | Core | None | No | 6.7 | Local | Low | High | None | Changed | Low | None | High | 7.2.22 |  | 
| CVE-2026-127420 | Oracle VM VirtualBox | Core | None | No | 4.4 | Local | Low | None | Required | Un- changed | Low | Low | None | 7.2.22 |  |
