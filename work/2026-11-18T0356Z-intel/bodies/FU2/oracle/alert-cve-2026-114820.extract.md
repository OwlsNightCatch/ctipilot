---
title: Oracle Security Alert Advisory - CVE-2026-114820
url: https://www.oracle.com/security-alerts/alert-cve-2026-114820.html
hostname: oracle.com
description: Oracle Security Alert Advisory - CVE-2026-114820
sitename: oracle.com
date: "2026-10-24"
tags: ['Security, Alert, Advisory, CVE-2026-114820']
fingerprint: "96fbf5b380b6955b"
---
This Security Alert addresses CVE-2026-114820 by providing Java updates that remove the set of impacted root CA certificates related to eMudhra. To address this CVE, update to the latest Java version or apply the recommended mitigations. For more information refer to the Patch Availability Document below and [https://ops.java/emudhra](https://ops.java/emudhra). Additional Oracle products that bundle or embed Java will continue to be added to this advisory as patches become available.

Security vulnerabilities addressed by this Security Alert affect the products listed below.

**Please click on the links in the Patch Availability Document column below to access the documentation for patch availability information and installation instructions.** 

Patches released through the Security Alert program are provided only for product versions that are covered under the Premier Support or Extended Support phases of the  [Lifetime Support Policy](https://www.oracle.com/us/support/lifetime-support/index.html?ssSourceSiteId=otnen). Oracle recommends that customers plan product upgrades to ensure that patches released through the Security Alert program are available for the versions they are currently running.

Product releases that are not under Premier Support or Extended Support are not tested for the presence of vulnerabilities addressed by this Security Alert. However, it is likely that earlier versions of affected releases are also affected by these vulnerabilities. As a result, Oracle recommends that customers upgrade to supported versions.

Risk matrices list only security vulnerabilities that are newly addressed by the patches associated with this advisory. Risk matrices for previous security patches can be found in [previous Critical Patch Update advisories, Critical Security Patch Update advisories and Alerts](https://www.oracle.com/security-alerts). An English text version of the risk matrices provided in this document is  [here](https://www.oracle.com/security-alerts/cve-2026-114820verbose.html).

Security vulnerabilities are scored using CVSS version 3.1 (see [Oracle CVSS Scoring](https://www.oracle.com/security-alerts/cvssscoringsystem.html) for an explanation of how Oracle applies CVSS version 3.1).

Oracle conducts an analysis of each security vulnerability addressed by a Security Alert. Oracle does not disclose detailed information about this security analysis to customers, but the resulting Risk Matrix and associated documentation provide information about conditions required to exploit the vulnerability and the potential impact of a successful exploit. Oracle provides this information so that customers may conduct their own risk analysis based on the particulars of their product usage. For more information, see [Oracle vulnerability disclosure policies](https://www.oracle.com/corporate/security-practices/assurance/vulnerability/disclosure/).

Third party component vulnerabilities that are deemed not exploitable in the context of their inclusion in an Oracle product are listed, with [VEX](https://www.oracle.com/security-alerts/cpufaq.html#vex) justifications, below the respective Oracle product's risk matrix.

The protocol in the risk matrix implies that all of its secure variants are affected as well. For example, if HTTP is listed as an affected protocol, it implies that HTTPS is also affected. The secure variant of a protocol is listed in the risk matrix only if it is the *only* variant affected.

The following people or organizations reported security vulnerabilities addressed by this Security Alert to Oracle: None credited in this Security Alert.

| Date | Note | 
|---|---|
| 2026-October-30 | Rev 2. Added Oracle Autonomous Health Framework, Oracle Database Serve, Oracle Global Lifecycle Management OPatch, Oracle Hospitality Cruise Shipboard Property Management (SPMS) | 
| 2026-October-24 | Rev 1. Initial Release | 


This Security Alert contains 3 new security patches for Oracle Database Products divided as follows:

- 1 new security patch for Oracle Database Products
- 1 new security patch for Oracle Autonomous Health Framework
- 1 new security patch for Oracle Global Lifecycle Management


This Security Alert contains 1 new security patch for Oracle Database Products.  This vulnerability is remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  This patch is not applicable to client-only installations, i.e., installations that do not have the Oracle Database Server installed. The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cve-2026-114820verbose.html#DB)

| CVE ID | Component | Package and/or Privilege Required | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-114820 | RDBMS (Java) | None | Multiple | Yes | 9.1 | Network | Low | None | None | Un- changed | High | High | None | 19.3-19.32, 21.3-21.23, 23.4.0-23.26.3 |  | 

This Security Alert contains 1 new security patch for Oracle Autonomous Health Framework.  This vulnerability is remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cve-2026-114820verbose.html#AHTF)

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-114820 | Oracle Autonomous Health Framework | Trace File Analyzer (Java) | Multiple | Yes | 9.1 | Network | Low | None | None | Un- changed | High | High | None | 26.3-26.10 |  | 

This Security Alert contains 1 new security patch for Oracle Global Lifecycle Management.  This vulnerability is remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cve-2026-114820verbose.html#GLM)

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-114820 | Oracle Global Lifecycle Management OPatch | Patch Installer (Java) | Multiple | Yes | 9.1 | Network | Low | None | None | Un- changed | High | High | None | 12.2.0.1.16-12.2.0.1.52 |  | 

This Security Alert contains 1 new security patch for Oracle Hospitality Applications.  This vulnerability is remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cve-2026-114820verbose.html#HOSP)

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-114820 | Oracle Hospitality Cruise Shipboard Property Management (SPMS) | Next-Gen SPMS (Java) | Multiple | Yes | 9.1 | Network | Low | None | None | Un- changed | High | High | None | 23.3.4, 23.3.5, 23.3.6 |  | 

This Security Alert contains 1 new security patch for Oracle Java SE.  This vulnerability is remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials.  The English text form of this Risk Matrix can be found [here.](https://www.oracle.com/security-alerts/cve-2026-114820verbose.html#JAVA)

| CVE ID | Product | Component | Protocol | Remote Exploit without Auth.? | CVSS VERSION 3.1 RISK (see [Risk Matrix Definitions](https://www.oracle.com/security-alerts/advisorymatrixglossary.html)) |  |  |  |  |  |  |  |  | Supported Versions Affected | Notes | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | Base Score | Attack Vector | Attack Complex | Privs Req'd | User Interact | Scope | Confid- entiality | Inte- grity | Avail- ability |  |  | 
| CVE-2026-114820 | Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition | JSSE | Multiple | Yes | 9.1 | Network | Low | None | None | Un- changed | High | High | None | Oracle Java SE: 8u511-b32, 8u511-perf-b32, 11.0.33.0.2, 17.0.21.0.2, 21.0.13.0.2, 25.0.5.0.2, 27.0.1.0.2; Oracle GraalVM for JDK: 17.0.21.0.2, 21.0.13.0.2; Oracle GraalVM Enterprise Edition: 21.3.20.0.2 | See Note 1 | 

1. This vulnerability can be exploited by using APIs in the specified Component, e.g., through a web service which supplies data to the APIs. This vulnerability also applies to Java deployments, typically in clients running sandboxed Java Web Start applications or sandboxed Java applets, that load and run untrusted code (e.g., code that comes from the internet) and rely on the Java sandbox for security.
