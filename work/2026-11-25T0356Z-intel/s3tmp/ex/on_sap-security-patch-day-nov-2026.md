---
title: "SAP Security Notes: November 2026 Patch Day"
author: Thomas Fritsch
url: https://onapsis.com/blog/sap-security-patch-day-nov-2026/
hostname: onapsis.com
description: "Record-breaking numbers of HotNews and High Priority Notes Navigating November’s Historic SAP Security Patch DayWatch Onapsis to talk through November’s Vulnerabilities.On Demand Webinar Note: This blog contains ongoing coverage. Updates will be posted continuously below as confirmed information becomes available. Highlights of November SAP Security Notes analysis include: SAP has published the record-breaking number of..."
sitename: Onapsis Research Labs
date: "2026-11-12"
tags: ['Thomas Fritsch', 'Onapsis Research Labs', 'SAP Security Notes', 'SAP vulnerabilities']
fingerprint: d50bfdb66eb5f883
language: en
image: https://onapsis.com/wp-content/uploads/NEW-BRAND-Blog-images-1070x595-1-1.png
pagetype: article
filedate: "2026-11-25"
---
## Record-breaking numbers of *HotNews* and *High Priority* Notes

**Navigating November’s Historic SAP Security Patch Day**

Watch Onapsis to talk through November’s Vulnerabilities.

**On Demand Webinar**

Highlights of November SAP Security Notes analysis include:

- **November Summary –** 43 new and updated SAP security patches released, including 12 HotNews Notes and 13 High Priority Notes
- **Four CVSS 10.0 –** Memory corruptions in ICM and SAP Web Dispatcher, Missing Authentication in SAP NW AS ABAP and ABAP Platform and Broken Access Control in SAP Gateway
- **Onapsis Research Labs Contribution –** Our team supported SAP in patching 36 vulnerabilities, covered by 25 SAP Security Notes, including 7 tagged as *HotNews* and 10 tagged as *High Priority.* *14 of the 36 Vulnerabilities, leading to 7 Security Notes were found in collaboration with [XBOW](https://xbow.com/).*

SAP has published the record-breaking number of 43 new and updated SAP Security Notes in its November Patch Day, including 12 *HotNews* Notes and 13 *High Priority* Notes. 24 SAP Security Notes were published in collaboration with the Onapsis Research Labs.

## The *HotNews* Notes in Detail

The Onapsis Research Labs (ORL) supported SAP in patching seven of twelve HotNews Notes.

SAP Security Note [#3798345](https://me.sap.com/notes/3798345), tagged with a CVSS score of 10.0, patches a Broken Access Control vulnerability in SAP Gateway. The **Onapsis Research Labs (ORL)** detected that an unauthenticated attacker with network access to the SAP Gateway could exploit a vulnerability in the application to potentially perform unauthorized actions within the application environment. The vulnerability is caused by the fact that SAP Gateway activates the default Access Control List with high privileges allowing categorization of external attackers as internal application servers. After implementing the SAP Security Note, customers must manually set a profile parameter to be secure. The vulnerability is tracked under [CVE-2026-89103](https://www.cve.org/CVERecord?id=CVE-2026-89103) and is dubbed **PROXYGATE** by the Onapsis Research Labs.  **More information on the PROXYGATE vulnerability can be found here**

SAP Security Note [#3778530](https://me.sap.com/notes/3778530), tagged with a CVSS score of 10.0, patches a Memory Corruption vulnerability in SAP NetWeaver AS ABAP (Internet Communication Manager). **Our ORL team** recognized that some size/length parameters in WebSocket control frames are not properly validated. This allows an unauthenticated attacker sending specially crafted network traffic to trigger a memory corruption condition in the affected functionality. Successful exploitation could allow the attacker to execute arbitrary code and fully compromise the system. As a workaround, support for WebSocket can be disabled. But since this has a significant impact on interactive and integration scenarios, it is not recommended.

SAP Security Note [#3778556](https://me.sap.com/notes/3778556), tagged with a CVSS score of 10, addresses almost the same vulnerability in SAP Web Dispatcher and is also credited to the **Onapsis Research Labs**. In the referenced FAQ Note [#3778788](https://me.sap.com/notes/3778788), SAP explains how this SAP Security Note is related to [#3778530](https://me.sap.com/notes/3778530). Important: The Web Dispatcher that is part of SAP HANA Extended Application Services Classic Model and Advanced Model is also affected. SAP Content Server is not affected.

The vulnerabilities, affecting ICM and SAP Web Dispatcher, were dubbed **ICM2SHELL** by the Onapsis Research Labs.  **More information on the ICM2SHELL vulnerability can be found here**

SAP Security Note [#3849308](https://me.sap.com/notes/3849308), tagged with a CVSS score of 10.0, addresses a Missing Authentication vulnerability in SAP NetWeaver AS ABAP and ABAP Platform (SAML2 Service Provider). The vulnerability is caused by an insufficient verification of incoming authentication assertions under certain configurations. If not patched, unauthenticated attackers could submit specially crafted data to bypass authentication and impersonate arbitrary users, including privileged accounts. This could result in a full system compromise

**The ORL team** supported SAP in patching a Missing Authorization Check vulnerability in S4CRM. Certain remote-enabled function modules do not perform necessary authorization checks and lack sufficient input validation. As a result, an attacker with low privileges could send specially crafted input through a remote interface to inject and execute arbitrary code within the affected system.  Successful exploitation could extend the attacker’s reach beyond the vulnerable component, resulting in a high impact on confidentiality, integrity and availability. SAP Security Note [#3834842](https://me.sap.com/notes/3834842), tagged with a CVSS of 9.9, introduces appropriate authorization checks as well as code to identify and prevent any injection.

Another *HotNews* Note that SAP has published **in collaboration with our ORL team** is SAP Security Note [#3792735](https://me.sap.com/notes/3792735), tagged with a CVSS score of 9.9. Researchers of the team detected certain internal functionality in SAP NetWeaver Application Server ABAP and ABAP Platform that does not perform necessary authorization checks. When acting as a low privileged attacker, they could invoke affected functionality to execute arbitrary operating system commands on the underlying host. Successful exploitation could impact resources beyond the vulnerable component, resulting in a high impact on confidentiality, integrity and availability of the system.

**The ORL team, in collaboration with [XBOW](https://xbow.com/), also supported SAP** in patching a CVSS 9.9 Code Injection vulnerability in  SAP NetWeaver Knowledge Management (XML Forms). Under certain conditions, an authenticated user with access to the vulnerable functionality could cause an unauthorized XSL transformation to be processed, potentially leading to arbitrary code execution in the application context. The vulnerability is patched with SAP Security Note [#3809153](https://me.sap.com/notes/3809153) by restricting request-selected XSL transformations to only those explicitly configured for the current XML Forms project. Any unconfigured or unresolved transformation identifiers are now rejected.

SAP Security Note [#3805589](https://me.sap.com/notes/3805589), tagged with a CVSS score of 9.9, was initially released on SAP’s October patch day and patches a critical Code Injection vulnerability in SAP S/4HANA (Manage Substitution/Validation Rules). The updated note contains additional correction instructions for S4CORE 105 and 106.

Two *HotNews* Notes affect SAP Business AI Platform and were published by SAP between October and November patch day:

SAP Security Note [#3843368](https://me.sap.com/notes/3843368), tagged with a CVSS score of 9.8 was initially released on October 28 and patches a Memory Corruption vulnerability in Node.js Brotli decoder. The vulnerability allows an attacker to leverage an error-handling flaw in the Brotli decoder’s block-switch processing. Under certain conditions, this can cause memory corruption (out-of-bounds write) leading to high impact on confidentiality, integrity and availability. The note comes with detailed solution descriptions for SAP BTP, Cloud Foundry and Kyma Runtime and other Brotli consumers.

SAP Security Note [#3846599](https://me.sap.com/notes/3846599), tagged with a CVSS score of 9.8, patches two Remote Code Execution vulnerabilities ([CVE-2026-109618](https://www.cve.org/CVERecord?id=CVE-2026-109618), [CVE-2026-109619](https://www.cve.org/CVERecord?id=CVE-2026-109619)) in SAP Business AI Platform, which are collectively known as the php2shell Remote Code Execution (RCE) chain. Both vulnerabilities are network-exploitable, require no privileges and no user interaction, and affect all active PHP 8.x minor lines (8.2.x, 8.3.x, 8.4.x, 8.5.x). They can be chained together in a combined attack vector, where the memory corruption condition established by [CVE-2026-109618](https://www.cve.org/CVERecord?id=CVE-2026-109618) could be further exploited. The note comes with detailed solution descriptions for SAP BTP, Cloud Foundry and Kyma Runtime.

SAP Security Note [#3804858](https://me.sap.com/notes/3804858), tagged with a CVSS score of 9.6, patches two Cross-Site Request Forgery (CSRF) vulnerabilities in SAP Web Dispatcher and Internet Communication Manager (ICM) as well as in SAP HANA XSA Web Dispatcher. The vulnerabilities were **reported by the ORL team** after detecting that they allow unauthenticated attackers to trick a logged-on administrator into visiting a malicious link. Visiting the link could cause unintended actions in the administrator’s session. While the vulnerability in SAP Web Dispatcher and ICM could lead to a full system compromise, SAP HANA XSA Web Dispatcher can only be compromised temporarily, with high impact on confidentiality, but only partial impact on integrity, and availability.

SAP Security Note

[**#3799117**](https://me.sap.com/notes/3799117), tagged with a CVSS score of 9.1, patches an XML External Entity (XXE) Vulnerability in SAP BusinessObjects Business Intelligence Platform (Web Intelligence). The application does not properly restrict external entity resolution when processing OLAP connection requests. An authenticated attacker could exploit this vulnerability to access restricted resources, enabling them to read sensitive files on the server and reach internal systems that are not otherwise exposed, impacting resources beyond the vulnerable component, resulting in a high impact on confidentiality and a low impact on both integrity and availability.

## The High Priority Notes in Detail

The Onapsis Research Labs (ORL) supported SAP in patching ten of thirteen High Priority Notes.

SAP Security Note [#3769130](https://me.sap.com/notes/3769130), tagged with a CVSS score of 8.9, patches multiple vulnerabilities in Application Server ABAP of SAP NetWeaver and ABAP Platform.

Due to improper RFC protocol validation in the SAP Kernel used by the Application Server ABAP of SAP NetWeaver and ABAP Platform, an unauthenticated attacker can send a crafted RFC request that exploits logical errors in memory management, leading to memory corruption ([CVE-2026-76966](https://www.cve.org/CVERecord?id=CVE-2026-76966)).

SAP NetWeaver Application Server ABAP and ABAP Platform does not properly initialize memory in certain internal components. Under certain conditions, an attacker with low privileges could disclose uninitialized memory contents under specific conditions ([CVE-2026-109796](https://www.cve.org/CVERecord?id=CVE-2026-109796)).

SAP Security Note [#3809953](https://me.sap.com/notes/3809953), tagged with a CVSS score of 8.2, addresses a Memory Corruption vulnerability in SAP NetWeaver (Internet Graphics Service). **The ORL team** recognized that SAP IGS does not sufficiently validate certain input values within incoming requests. This allows an unauthenticated user to send a specially crafted request to trigger an out-of-bounds memory write in a worker process. Successful exploitation could result in memory corruption or repeated termination of the affected process.

SAP Security Note [#3803832](https://me.sap.com/notes/3803832), tagged with a CVSS score of 7.7, describes a Memory Corruption vulnerability in SAP Web Dispatcher. Researchers from **the ORL team** identified certain inputs during processing that are not properly validated and could therefore lead to memory corruption. SAP Web Dispatcher is only affected when configured in front of an Application Server ABAP or Java and its profile contains either “MSHOST” or “MSSHOST”. In this case, an attacker authenticated with non-administrative permissions could exploit this vulnerability by providing specially crafted input, causing the Web Dispatcher process to terminate without user interaction. As a result, the Web Dispatcher and all backend systems reachable through it become unavailable, leading to a high impact on availability.

Another Memory Corruption vulnerability was detected by **our ORL team** in Application Server ABAP of SAP NetWeaver and ABAP Platform (SAP Message Server).They were able to send specially crafted network requests as an unauthenticated attacker to two vulnerable endpoints of the Message Server. By triggering the vulnerability, the attacker could cause the server to crash and disrupt active connections, leading to a denial of service condition. SAP Security Note [#3789273](https://me.sap.com/notes/3789273), tagged with a CVSS score of 7.5, patches the two endpoints.

**The Onapsis Research Labs** detected that SAP Message Server is affected by another Memory Corruption vulnerability. They realized that SAP Message Server does not properly size memory allocations when handling certain HTTP requests. This allows an unauthenticated attacker sending a specially crafted request to trigger a heap buffer overflow in affected functionality. SAP Security Note [#3805570](https://me.sap.com/notes/3805570), tagged with a CVSS score of 7.5, resolves the issue by correcting the memory allocation to prevent buffer overflows. Leaving SAP Message Server unpatched, a successful exploitation can cause the component to abort and remain unavailable until it is restarted by the framework, resulting in a high impact on availability of the system.

A denial of service condition could also be triggered by a Memory Corruption vulnerability in Application Server ABAP for SAP NetWeaver and ABAP Platform, that was recently detected **by our researchers.** Acting as an unauthenticated attacker, they were able to send specially crafted requests to the application. If processed by the application, these requests could trigger a memory corruption condition in the parsing routine, which could cause the affected processes to crash and restart. A sustained denial of service situation could be triggered by repeatedly sending such requests. SAP Security Note [#3792915](https://me.sap.com/notes/3792915), tagged with a CVSS score of 7.5, introduces proper validation of boundary conditions to prevent memory corruption scenarios.

SAP Security Note [#3805681](https://me.sap.com/notes/3805681), tagged with a CVSS score of 7.5, patches a Denial of Service vulnerability in SAP NetWeaver Application Server ABAP, ABAP Platform and SAP Web Dispatcher. **The ORL team** could send specially crafted requests to a component as an unauthenticated attacker that does not sufficiently handle resource consumption when processing these requests. With such requests, an attacker can cause excessive resource utilization and service disruption. SAP NetWeaver AS Java and SAP HANA XSC Web Dispatcher are not affected by the vulnerability.

**Our team** supported SAP also in patching a Denial of Service vulnerability in SAP NetWeaver Application Server ABAP (Internet Communication Manager) and SAP Web Dispatcher. Our researchers detected that ICM and SAP Web Dispatcher do not sufficiently validate certain header values processed during inbound request handling.This enables unauthenticated attackers sending a specially crafted request to cause the affected process to become unavailable. SAP Security Note [#3808627](https://me.sap.com/notes/3808627), tagged with a CVSS score of 7.5, patches the issue in both components by improving validation and error handling when parsing request headers.

SAP Security Note [#3809934](https://me.sap.com/notes/3809934), tagged with a CVSS score of 7.5, patches 2 vulnerabilities in SAP NetWeaver (Internet Graphics Service) that could both result in a repeated termination of the worker process. The corresponding Out-of-Bounds Read and Integer Overflow vulnerabilities can be fixed by implementing the SAP IGS patch. A workaround is not available.

A Missing Authentication check vulnerability in SAP NetWeaver AS Java EDM Application was identified by **the Onapsis Research Labs in collaboration with [XBOW](https://xbow.com/)**. They noticed that the application does not perform an authentication check for certain web service requests. An unauthenticated attacker could send a specially crafted request to retrieve sensitive business information resulting in high impact on confidentiality. By implementing SAP Security Note [#3810485](https://me.sap.com/notes/3810485), The issue is fixed by removing the EDM application from customers’ systems as part of SUM updates. SAP has also removed the EDM application from SAP Marketplace. As a temporary workaround, a filter can be added to disable the EDM application.

SAP Security Note [#3842766](https://me.sap.com/notes/3842766), tagged with a CVSS score of 7.5, patches an Insufficient Input Validation vulnerability in SAP Host Agent. Under certain conditions, an attacker with low privileges could abuse the vulnerable functionality to influence an internal component into loading a malicious file under a privileged account. Successful exploitation could lead to persistent code execution. **The ORL team** supported SAP in patching the issue. SAP Host Agent will not load malicious files from untrusted sources in the affected scenario anymore. In an unpatched environment, SAP Host Agent must have a specialized SAP internal monitoring configuration active to enable the exploit.

SAP Security Note [#3808552](https://me.sap.com/notes/3808552), tagged with a CVSS score of 7.5, addresses an Information Disclosure vulnerability in SAP NetWeaver (SAP Message Server). Improper handling of certain malformed requests could be leveraged by an unauthenticated attacker to send specially crafted input. Successful exploitation could allow the attacker to retrieve sensitive information, resulting in a high impact on confidentiality.

SAP Security Note [#3833364](https://me.sap.com/notes/3833364), tagged with a CVSS score of 7.2, patches a Code Injection vulnerability in SAP ABAP Developer Tools (AMDP Data Preview). The application does not perform sufficient validation and authorization checks within certain affected functionality. An attacker with high privileges could submit specially crafted input to inject and execute arbitrary code on the system. Successful exploitation could allow the attacker to fully compromise the system.

## Onapsis Contribution

The Onapsis Research Labs (ORL) contributed significantly to SAP’s November Patch Day. In addition to seven *HotNews* Notes and ten *High Priority* Note, the ORL supported SAP in patching eight additional SAP Security Notes:

SAP Security [#3805959](https://me.sap.com/notes/3805959), tagged with a CVSS score of 6.5, patches a Server-Side Request Forgery vulnerability in SAP NetWeaver and ABAP Platform (Application Server ABAP). The vulnerability is caused by insecure default settings for an internal HTTP component. A low-privileged authenticated attacker could trick a victim to interact with a malicious server which allows the attacker to access sensitive information belonging to the victim and modify limited non-sensitive information. The note patches the vulnerability by introducing an additional allowlist check to ensure that HTTP client requests are only sent to permitted destinations. More details can be found in the referenced FAQ note [#3834382](https://me.sap.com/notes/3834382).

**The ORL team, in collaboration with [XBOW](https://xbow.com/)**, supported SAP in patching an Information Disclosure vulnerability and Missing Authorization Check vulnerability in SAP NetWeaver Application Server Java (NWDI Cockpit). Both vulnerabilities are tagged with a CVSS score of 6.5 and can be patched by implementing SAP Security Note [#3839977](https://me.sap.com/notes/3839977). While the first one has a high impact on the system’s confidentiality, the second one impacts integrity since it allows unauthorized modifications.

SAP Security Note [#3786876](https://me.sap.com/notes/3786876), tagged with a CVSS score of 6.4, patches a Weak Cryptography vulnerability in SAP NetWeaver and ABAP Platform (Application Server ABAP). **The ORL team** detected a weak HMAC cryptography calculation when receiving an RFC callback in SAP NetWeaver and ABAP Platform (Application Server ABAP). An authenticated attacker with high privileges and access to a network segment between application servers on an SAP system could intercept network communication between application servers and change the identity of the caller, enabling the execution of unauthorized function calls on the target server with escalated privileges. The patch hardens HMAC calculation for RFC callbacks in the SAP Kernel.

SAP Security Note [#3797108](https://me.sap.com/notes/3797108), tagged with a CVSS score of 6.1, patches a CSS Injection vulnerability in SAP NetWeaver Application Server Java (Web Dynpro Java). The ORL team detected in collaboration with [XBOW](https://xbow.com/) that Web Dynpro Java does not sufficiently validate certain request parameters used to resolve styling resources in the application. Acting as an unauthenticated attacker, our team could craft a malicious link that, when clicked by an authenticated victim, causes the victim’s browser to load attacker-controlled styling content within the trusted application context. Successful exploitation could allow the attacker to redress the trusted user interface for phishing purposes and exfiltrate limited web page content, resulting in a low impact on confidentiality and integrity. The issue has been fixed by introducing stricter host validation for theme resource requests.

SAP Security Note [#3806484](https://me.sap.com/notes/3806484), tagged with a CVSS score of 6.1, addresses a Cross-Site Scripting vulnerability in SAP NetWeaver Visual Composer. **The ORL team** identified certain request data that lacks sufficient input validation and output encoding. This allows an unauthenticated attacker to craft a malicious link containing specially crafted input. If a victim clicks the link, the injected script executes in the victim’s browser within the context of the affected application, leading to a low impact on confidentiality and integrity.

SAP Security Note [#3835738](https://me.sap.com/notes/3835738), tagged with a CVSS score of 5.8, patches a Server-Side Request Forgery vulnerability in SAP NetWeaver AS Java (Web Services) that was identified by **the ORL team in collaboration with [XBOW](https://xbow.com/)**. They noticed that an unauthenticated attacker could craft a SOAP request that causes the server to return a SOAP fault to a URL under the attacker’s control. A successful exploitation allows the attacker to disclose information about connected systems, impacting confidentiality, while integrity and availability remain unaffected. After implementing the patch, customers need to configure the a whitelist property in the Visual Administrator or via the Config Tool under the webservices service properties.

Another vulnerability that was patched in collaboration with the **ORL team and** [**XBOW**](https://xbow.com/) is described in SAP Security Note [#3792447](https://me.sap.com/notes/3792447), tagged with a CVSS score of 5.3. Due to Broken Access Control in SAP NetWeaver Process Integration (Process Integration Test Tool), the researchers could invoke affected SOAP operations exposed over HTTP without proper access control. Successful exploitation could allow disclosure of information accessible through the affected service, resulting in a low impact on confidentiality. An exploit does not require authentication.

**The ORL team and** [**XBOW**](https://xbow.com/) supported SAP in patching a Cross Site Request Forgery (CSRF) vulnerability in SAP NetWeaver Enterprise Portal.They noticed that the Portal application does not sufficiently protect certain server-side actions against cross-site request forgery. This allows an unauthenticated attacker to craft a malicious link that, when clicked by an authenticated user, triggers an unintended action on the server. Successful exploitation could allow the attacker to modify non-sensitive information. SAP Security Note [#3801587](https://me.sap.com/notes/3801587), tagged with a CVSS score of 4.3, patches the vulnerability by adding appropriate CSRF-protection to the affected endpoints.

## Summary & Conclusions

SAP’s November Patch Day has broken several records. With forty-three new and updated SAP Security Notes, including twelve *HotNews* and thirteen *High Priority* Notes, SAP administrators will be very busy this week. It was also a record-holding patch day for the Onapsis Research Labs. We could support SAP in patching thirty-six vulnerabilities, covered by twenty-five SAP Security Notes, including seven tagged as *HotNews* and ten tagged as *High Priority* Notes.

| **SAP Note** | **Type** | **Description** | **Priority** | **CVSS** | 
| 3849308 | New | \[CVE-2026-120017\] Missing Authentication in SAP NetWeaver AS ABAP and ABAP Platform (SAML2 Service Provider) BC-SEC-LGN-SML | HotNews | 10 | 
| 3798345 | New | \[CVE-2026-89103\] Broken Access Control in SAP Gateway BC-CST-GW | HotNews | 10 | 
| 3778556 | New | \[CVE-2026-89126\] Memory Corruption vulnerability in SAP Web Dispatcher BC-CST-WDP | HotNews | 10 | 
| 3778530 | New | \[CVE-2026-76964\] Memory Corruption Vulnerability in SAP NetWeaver AS ABAP (Internet Communication Manager) BC-CST-IC | HotNews | 10 | 
| 3834842 | Update | \[CVE-2026-109795\] Missing authorization check in S4CRM CRM-BF-SVY | HotNews | 9.9 | 
| 3809153 | New | \[CVE-2026-109803\] Code Injection vulnerability in SAP NetWeaver Knowledge Management (XML Forms) EP-KM-CM | HotNews | 9.9 | 
| 3792735 | New | \[CVE-2026-76965\] OS Command Injection vulnerability in ABAP Application Server for SAP NetWeaver and ABAP Platform BC-SRV-COM-FTP | HotNews | 9.9 | 
| 3805589 | Update | \[CVE-2026-89107\] Code Injection vulnerability in SAP S/4HANA (Manage Substitution/Validation Rules) FI-SL-VSR | HotNews | 9.9 | 
| 3846599 | New | \[Multiple CVEs\] Remote Code Execution vulnerability in PHP affecting SAP Business AI Platform BC-CP-CF-BLDP | HotNews | 9.8 | 
| 3843368 | New | \[CVE-2026-111497\] Memory Corruption in Node.js Brotli decoder affecting SAP Business AI Platform BC-CP-SEC-VUL | HotNews | 9.8 | 
| 3804858 | New | \[CVE-2026-89119\] Cross-Site Request Forgery (CSRF) vulnerability in SAP Web Dispatcher and Internet Communication Manager BC-CST-WDP | HotNews | 9.6 | 
| 3799117 | New | \[CVE-2026-109798\] XML External Entity (XXE) Vulnerability in SAP BusinessObjects Business Intelligence Platform (Web Intelligence) BI-BIP-SL | HotNews | 9.1 | 
| 3769130 | New | \[CVE-2026-76966\] Multiple vulnerabilities in Application Server ABAP of SAP NetWeaver and ABAP Platform BC-MID-RFC | High | 8.9 | 
| 3809953 | New | \[CVE-2026-120008\] Memory Corruption Vulnerability in SAP NetWeaver (Internet Graphics Service) BC-FES-IGS | High | 8.2 | 
| 3803832 | New | \[CVE-2026-109800\] Memory Corruption vulnerability in SAP Web Dispatcher BC-CST-WDP | High | 7.7 | 
| 3789273 | New | \[CVE-2026-76973\] Memory Corruption vulnerability in Application Server ABAP of SAP NetWeaver and ABAP Platform (SAP Message Server) BC-CST-MS | High | 7.5 | 
| 3792915 | New | \[CVE-2026-76970\] Memory Corruption vulnerability in Application Server ABAP for SAP NetWeaver and ABAP Platform BC-ABA-SC | High | 7.5 | 
| 3842766 | New | \[CVE-2026-120015\] Insufficient Input Validation in SAP Host Agent BC-CCM-HAG | High | 7.5 | 
| 3810485 | New | \[CVE-2026-89114\] Missing Authentication check in SAP NetWeaver AS Java EDM Application BC-DWB-JAV-J2E | High | 7.5 | 
| 3809934 | New | \[Multiple CVEs\] Multiple Vulnerabilities in SAP NetWeaver (Internet Graphics Service) BC-FES-IGS | High | 7.5 | 
| 3808627 | New | \[CVE-2026-109793\] Denial of Service (DoS) vulnerability in SAP NetWeaver Application Server ABAP (Internet Communication Manager) and SAP Web Dispatcher BC-CST-DP | High | 7.5 | 
| 3808552 | New | \[CVE-2026-109804\] Information Disclosure in SAP NetWeaver (SAP Message Server) BC-CST-MS | High | 7.5 | 
| 3805681 | New | \[CVE-2026-109794\] Denial of Service vulnerability in SAP NetWeaver Application Server ABAP, ABAP Platform and SAP Web Dispatcher BC-CST-IC | High | 7.5 | 
| 3805570 | New | \[CVE-2026-120010\] Memory Corruption vulnerability in SAP NetWeaver Application Server (SAP Message Server) BC-CST-MS | High | 7.5 | 
| 3833364 | New | \[CVE-2026-120009\] Code Injection vulnerability in SAP ABAP Developer Tools (AMDP Data Preview) BC-DWB-AIE-DP | High | 7.2 | 
| 3805959 | New | \[CVE-2026-109811\] Server-Side Request Forgery (SSRF) vulnerability in SAP NetWeaver and ABAP Platform (Application Server ABAP) BC-MID-ICF | Medium | 6.5 | 
| 3839977 | New | \[Multiple CVEs\] Security Vulnerabilities SAP NetWeaver Application Server Java (NWDI Cockpit) BC-CTS-DI | Medium | 6.5 | 
| 3793716 | New | \[CVE-2026-109802\] Denial of Service (DoS) vulnerability in SAP NetWeaver Application Server for ABAP BC-MID-RFC | Medium | 6.5 | 
| 3756450 | Update | \[CVE-2026-44766\] – SQL Injection vulnerability in SAP S/4HANA (Intercompany Matching and Reconciliation) FIN-CS-ICR | Medium | 6.5 | 
| 3786876 | New | \[CVE-2026-109805\] Weak Cryptography in SAP NetWeaver and ABAP Platform (Application Server ABAP) BC-MID-RFC | Medium | 6.4 | 
| 3703856 | Update | \[CVE-2026-24309\] Missing Authorization check in SAP NetWeaver Application Server for ABAP BC-DB-ORA-CCM | Medium | 6.4 | 
| 3806484 | New | \[CVE-2026-120016\] Cross-Site Scripting (XSS) vulnerability in SAP NetWeaver Visual Composer EP-VC-RTM | Medium | 6.1 | 
| 3797108 | New | \[CVE-2026-109810\] CSS Injection vulnerability in SAP NetWeaver Application Server Java (Web Dynpro Java) BC-WD-JAV | Medium | 6.1 | 
| 3782056 | New | \[CVE-2026-89125\] Insecure Storage of Sensitive Information in SAP Web Dispatcher and Internet Communication Manager BC-CST-WDP | Medium | 6 | 
| 3835738 | Update | \[CVE-2026-89129\] Server-Side Request Forgery in SAP NetWeaver AS Java (Web Services) BC-JAS-SEC-WSS | Medium | 5.8 | 
| 3671819 | Update | \[CVE-2026-76976\] Cross-Site Scripting (XSS) vulnerability in SAP NetWeaver Application Server ABAP (Applications based on SAP GUI for HTML) BC-FES-CTL | Medium | 5.4 | 
| 3792447 | New | \[CVE-2026-89128\] Broken Access Control in SAP NetWeaver Process Integration (Process Integration Test Tool) BC-XI-PIT | Medium | 5.3 | 
| 3803144 | New | \[CVE-2026-73635\] Denial of service (DoS) in SAP Business Objects BI-BIP-CMC | Medium | 5.3 | 
| 3740168 | New | \[CVE-2026-89115\] Information Disclosure vulnerability in SAP Start Service and SAP Microsoft Management Console BC-CST-STS | Medium | 4.4 | 
| 3801587 | New | \[CVE-2026-89131\] Cross Site Request Forgery (CSRF) vulnerability in SAP NetWeaver Enterprise Portal EP-PIN-NAV | Medium | 4.3 | 
| 3101986 | Update | Prepare CSP support for On-Premise down port for code dependency in SAP WebClient UI CA-WUI-UI | Medium | 4.1 | 
| 3155685 | Update | \[CVE-2026-44768\] Security misconfiguration in SAP WebClient UI CA-WUI-UI | Medium | 4.1 | 
| 3802244 | New | \[CVE-2026-109808\] Missing Authorisation Check in SAP Solution Tools Plug-In (ST-PI) SV-SMG-SDD | Low | 3.1 | 

As always, the Onapsis Research Labs is already updating [The Onapsis Platform](https://www.onapsis.com/what-we-do/the-onapsis-platform) to incorporate the newly published vulnerabilities into the product so that our customers can protect their businesses.

For more information about the latest SAP security issues and our continuous efforts to share knowledge with the security community, subscribe to our monthly [Defender’s Monthly Newsletter](https://www.linkedin.com/build-relation/newsletter-follow?entityUrn=7052366453508870144).

**About XBOW**

[XBOW](https://xbow.com/) is the autonomous offensive security company. The platform continuously tests applications, chains real attack paths, and proves exploitability with working evidence. More than 150 security teams use XBOW to find exploitable vulnerabilities before attackers do.
