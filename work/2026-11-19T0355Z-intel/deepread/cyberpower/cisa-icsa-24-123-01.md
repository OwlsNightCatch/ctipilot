Title: CyberPower PowerPanel business | CISA

URL Source: https://www.cisa.gov/news-events/ics-advisories/icsa-24-123-01

Markdown Content:
[**View CSAF**](https://github.com/cisagov/CSAF)

## 1. EXECUTIVE SUMMARY

*   **CVSS v3** 9.8
*   **ATTENTION:** Exploitable remotely/Low attack complexity
*   **Vendor:** CyberPower
*   **Equipment:** PowerPanel Business
*   **Vulnerabilities:** Use of Hard-coded Password, Relative Path Traversal, Use of Hard-coded Credentials, Active Debug Code, Storing Passwords in a Recoverable Format, Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection'), Use of Hard-coded Cryptographic Key, Incorrect Authorization

## 2. RISK EVALUATION

Successful exploitation of these vulnerabilities could result in an attacker bypassing authentication and gaining administrator privileges, forging JWT tokens to bypass authentication, writing arbitrary files to the server and acheiving code execution, gaining access to services with the privileges of a Powerpanel Business application, gaining access to the testing or production server, learning passwords and authenticating with user or administrator privileges, injecting SQL syntax, writing arbitrary files to the system, executing remote code, impersonating any client in the system and sending malicious data, or obtaining data from throughout the system after gaining access to any device.

## 3. TECHNICAL DETAILS

### 3.1 AFFECTED PRODUCTS

The following versions of PowerPanel Business, a business management software, are affected:

*   PowerPanel Business: 4.9.0 and prior

### 3.2 Vulnerability Overview

#### **3.2.1**[**USE OF HARD-CODED PASSWORD CWE-259**](https://cwe.mitre.org/data/definitions/259.html)

The application code contains a hard-coded set of authentication credentials. This could result in an attacker bypassing authentication and gaining administrator privileges.

[CVE-2024-34025](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2024-34025) has been assigned to this vulnerability. A CVSS v3 base score of 9.8 has been calculated; the CVSS vector string is ([AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.0#CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H)).

A CVSS v4 score has also been calculated for [CVE-2024-34025](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2024-34025). A base score of 9.3 has been calculated; the CVSS vector string is ([CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N](https://www.first.org/cvss/calculator/4.0#CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N)).

#### **3.2.2**[**USE OF HARD-CODED PASSWORD CWE-259**](https://cwe.mitre.org/data/definitions/259.html)

The application code contains a hard-coded JWT signing key. This could result in an attacker forging JWT tokens to bypass authentication.

[CVE-2024-33625](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2024-33625) has been assigned to this vulnerability. A CVSS v3 base score of 9.8 has been calculated; the CVSS vector string is ([AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.0#CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H)).

A CVSS v4 score has also been calculated for [CVE-2024-33625](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2024-33625). A base score of 9.3 has been calculated; the CVSS vector string is ([CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N](https://www.first.org/cvss/calculator/4.0#CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N)).

#### **3.2.3**[**RELATIVE PATH TRAVERSAL CWE-23**](https://cwe.mitre.org/data/definitions/23.html)

A specially crafted Zip file containing path traversal characters can be imported to the server, which allows file writing to the server outside the intended scope, and could allow an attacker to achieve remote code execution.

[CVE-2024-33615](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2024-33615) has been assigned to this vulnerability. A CVSS v3 base score of 8.8 has been calculated; the CVSS vector string is ([AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.0#CVSS:3.0/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H)).

A CVSS v4 score has also been calculated for [CVE-2024-33615](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2024-33615). A base score of 8.7 has been calculated; the CVSS vector string is ([CVSS:4.0/AV:N/AC:L/AT:N/PR:L/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N](https://www.first.org/cvss/calculator/4.0#CVSS:4.0/AV:N/AC:L/AT:N/PR:L/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N)).

#### **3.2.4**[**USE OF HARD-CODED CREDENTIALS CWE-798**](https://cwe.mitre.org/data/definitions/798.html)

Hard-coded credentials are used by the platform to authenticate to the database, other services, and the cloud. This could result in an attacker gaining access to services with the privileges of a Powerpanel Business application.

[CVE-2024-32053](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2024-32053) has been assigned to this vulnerability. A CVSS v3 base score of 9.8 has been calculated; the CVSS vector string is ([AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.0#CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H)).

A CVSS v4 score has also been calculated for [CVE-2024-32053](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2024-32053). A base score of 9.3 has been calculated; the CVSS vector string is ([CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N](https://www.first.org/cvss/calculator/4.0#CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N)).

#### **3.2.5**[**ACTIVE DEBUG CODE CWE-489**](https://cwe.mitre.org/data/definitions/489.html)

Hard-coded credentials for the test server can be found in the production code. This might result in an attacker gaining access to the testing or production server.

[CVE-2024-32047](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2024-32047) has been assigned to this vulnerability. A CVSS v3 base score of 9.8 has been calculated; the CVSS vector string is ([AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.0#CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H)).

A CVSS v4 score has also been calculated for [CVE-2024-32047](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2024-32047). A base score of 9.3 has been calculated; the CVSS vector string is ([CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N](https://www.first.org/cvss/calculator/4.0#CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N)).

#### **3.2.6**[**STORING PASSWORDS IN A RECOVERABLE FORMAT CWE-257**](https://cwe.mitre.org/data/definitions/257.html)

The key used to encrypt passwords stored in the database can be found in the application code, allowing the passwords to be recovered.

[CVE-2024-32042](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2024-32042) has been assigned to this vulnerability. A CVSS v3 base score of 4.9 has been calculated; the CVSS vector string is ([AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:N/A:N](https://www.first.org/cvss/calculator/3.0#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:N/A:N)).

A CVSS v4 score has also been calculated for [CVE-2024-32042](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2024-32042). A base score of 6.9 has been calculated; the CVSS vector string is ([CVSS:4.0/AV:N/AC:L/AT:N/PR:H/UI:N/VC:H/VI:N/VA:N/SC:N/SI:N/SA:N](https://www.first.org/cvss/calculator/4.0#CVSS:4.0/AV:N/AC:L/AT:N/PR:H/UI:N/VC:H/VI:N/VA:N/SC:N/SI:N/SA:N)).

#### **3.2.7**[**IMPROPER NEUTRALIZATION OF SPECIAL ELEMENTS USED IN AN SQL COMMAND ('SQL INJECTION') CWE-89**](https://cwe.mitre.org/data/definitions/89.html)

An attacker with certain MQTT permissions can create malicious messages to all Power Panel devices. This could result in an attacker injecting SQL syntax, writing arbitrary files to the system, and executing remote code.

[CVE-2024-31856](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2024-31856) has been assigned to this vulnerability. A CVSS v3 base score of 8.8 has been calculated; the CVSS vector string is ([AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.0#CVSS:3.0/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H)).

A CVSS v4 score has also been calculated for [CVE-2024-31856](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2024-31856). A base score of 8.7 has been calculated; the CVSS vector string is ([CVSS:4.0/AV:N/AC:L/AT:N/PR:L/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N](https://www.first.org/cvss/calculator/4.0#CVSS:4.0/AV:N/AC:L/AT:N/PR:L/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N)).

#### **3.2.8**[**USE OF HARD-CODED CRYPTOGRAPHIC KEY CWE-321**](https://cwe.mitre.org/data/definitions/321.html)

The devices Power Panel manages use identical certificates based on a hard-coded cryptographic key. This can allow an attacker to impersonate any client in the system and send malicious data.

[CVE-2024-31410](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2024-31410) has been assigned to this vulnerability. A CVSS v3 base score of 6.5 has been calculated; the CVSS vector string is ([AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:H/A:N](https://www.first.org/cvss/calculator/3.0#CVSS:3.0/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:H/A:N)).

A CVSS v4 score has also been calculated for [CVE-2024-31410](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2024-31410). A base score of 7.1 has been calculated; the CVSS vector string is ([CVSS:4.0/AV:N/AC:L/AT:N/PR:L/UI:N/VC:N/VI:H/VA:N/SC:N/SI:N/SA:N](https://www.first.org/cvss/calculator/4.0#CVSS:4.0/AV:N/AC:L/AT:N/PR:L/UI:N/VC:N/VI:H/VA:N/SC:N/SI:N/SA:N)).

Certain MQTT wildcards are not blocked on the system, which might result in an attacker obtaining data from throughout the system after gaining access to any device.

[CVE-2024-31409](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2024-31409) has been assigned to this vulnerability. A CVSS v3 base score of 6.5 has been calculated; the CVSS vector string is ([AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N](https://www.first.org/cvss/calculator/3.0#CVSS:3.0/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N)).

A CVSS v4 score has also been calculated for [CVE-2024-31409](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2024-31409). A base score of 6.0 has been calculated; the CVSS vector string is ([CVSS:4.0/AV:N/AC:L/AT:P/PR:L/UI:N/VC:H/VI:N/VA:N/SC:N/SI:N/SA:N](https://www.first.org/cvss/calculator/4.0#CVSS:4.0/AV:N/AC:L/AT:P/PR:L/UI:N/VC:H/VI:N/VA:N/SC:N/SI:N/SA:N)).

### 3.3 BACKGROUND

*   **CRITICAL INFRASTRUCTURE SECTORS:** Critical Manufacturing
*   **COUNTRIES/AREAS DEPLOYED:** Worldwide
*   **COMPANY HEADQUARTERS LOCATION:** United States

### 3.4 RESEARCHER

Amir Preminger and Noam Moshe of Claroty Team82 Research reported these vulnerabilities to CISA.

## 4. MITIGATIONS

CyberPower has released a new version of PowerPanel Business that fixes these vulnerabilities:

PowerPanel Business: Update to [v4.10.1 or later version](https://www.cyberpower.com/global/en/product/sku/powerpanel_business_for_windows#downloads)

CISA recommends users take defensive measures to minimize the risk of exploitation of these vulnerabilities, such as:

*   Minimize network exposure for all control system devices and/or systems, ensuring they are [not accessible from the internet](https://www.cisa.gov/uscert/ics/alerts/ICS-ALERT-10-301-01).
*   Locate control system networks and remote devices behind firewalls and isolating them from business networks.
*   When remote access is required, use more secure methods, such as Virtual Private Networks (VPNs), recognizing VPNs may have vulnerabilities and should be updated to the most current version available. Also recognize VPN is only as secure as the connected devices.

CISA reminds organizations to perform proper impact analysis and risk assessment prior to deploying defensive measures.

CISA also provides a section for [control systems security recommended practices](https://www.cisa.gov/resources-tools/resources/ics-recommended-practices) on the ICS webpage on [cisa.gov/ics](https://www.cisa.gov/topics/industrial-control-systems). Several CISA products detailing cyber defense best practices are available for reading and download, including [Improving Industrial Control Systems Cybersecurity with Defense-in-Depth Strategies](https://us-cert.cisa.gov/sites/default/files/recommended_practices/NCCIC_ICS-CERT_Defense_in_Depth_2016_S508C.pdf).

CISA encourages organizations to implement recommended cybersecurity strategies for [proactive defense of ICS assets](https://www.cisa.gov/sites/default/files/publications/Cybersecurity_Best_Practices_for_Industrial_Control_Systems.pdf).

Additional mitigation guidance and recommended practices are publicly available on the ICS webpage at [cisa.gov/ics](https://www.cisa.gov/topics/industrial-control-systems) in the technical information paper, [ICS-TIP-12-146-01B--Targeted Cyber Intrusion Detection and Mitigation Strategies](https://www.cisa.gov/uscert/ics/tips/ICS-TIP-12-146-01B).

Organizations observing suspected malicious activity should follow established internal procedures and report findings to CISA for tracking and correlation against other incidents.

No known public exploitation specifically targeting these vulnerabilities has been reported to CISA at this time.

## 5. UPDATE HISTORY

*   May 2, 2024: Initial Publication
*   May 6, 2024: Additional CVSS scores added
*   August 12, 2025: Revision - Updated CWE

Links/Buttons:
- [Skip to main content](https://www.cisa.gov/news-events/ics-advisories/icsa-24-123-01#main)
- [Staying Secure at Events](https://www.cisa.gov/staying-secure-large-scale-events)
- [no-cost Cyber Services](https://www.cisa.gov/resources-tools/resources/free-cybersecurity-services-and-tools)
- [Cybersecurity Awareness Month](https://www.cisa.gov/cybersecurity-awareness-month)
- [KEV Catalog](https://www.cisa.gov/kev)
- [Report A Cyber Issue](https://www.cisa.gov/report)
- [](mailto:?subject=CyberPower%20PowerPanel%20business&body=https://www.cisa.gov/news-events/ics-advisories/icsa-24-123-01)
- [Topics](https://www.cisa.gov/topics)
- [Cybersecurity Best Practices](https://www.cisa.gov/topics/cybersecurity-best-practices)
- [Cyber Threats and Response](https://www.cisa.gov/topics/cyber-threats-and-response)
- [Critical Infrastructure Security and Resilience](https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience)
- [Election Security](https://www.cisa.gov/topics/election-security)
- [Emergency Communications](https://www.cisa.gov/topics/emergency-communications)
- [Industrial Control Systems](https://www.cisa.gov/topics/industrial-control-systems)
- [Information and Communications Technology Supply Chain Security](https://www.cisa.gov/topics/information-communications-technology-supply-chain-security)
- [Partnerships and Collaboration](https://www.cisa.gov/topics/partnerships-and-collaboration)
- [Physical Security](https://www.cisa.gov/topics/physical-security)
- [Risk Management](https://www.cisa.gov/topics/risk-management)
- [How can we help?](https://www.cisa.gov/audiences)
- [Government](https://www.cisa.gov/topics/government)
- [Educational Institutions](https://www.cisa.gov/topics/educational-institutions)
- [Industry](https://www.cisa.gov/topics/industry)
- [State, Local, Tribal, and Territorial](https://www.cisa.gov/topics/state-local-tribal-and-territorial)
- [Individuals and Families](https://www.cisa.gov/topics/individuals-and-families)
- [Small and Medium Businesses](https://www.cisa.gov/topics/small-and-medium-businesses)
- [Find Help Locally](https://www.cisa.gov/audiences/find-help-locally)
- [Faith-Based Community](https://www.cisa.gov/audiences/faith-based-community)
- [Executives](https://www.cisa.gov/audiences/executives)
- [High-Risk Communities](https://www.cisa.gov/audiences/high-risk-communities)
- [Spotlight](https://www.cisa.gov/spotlight)
- [Resources & Tools](https://www.cisa.gov/resources-tools)
- [All Resources & Tools](https://www.cisa.gov/resources-tools/all-resources-tools)
- [Services](https://www.cisa.gov/resources-tools/services)
- [Programs](https://www.cisa.gov/resources-tools/programs)
- [Resources](https://www.cisa.gov/resources-tools/resources)
- [Training](https://www.cisa.gov/resources-tools/training)
- [Groups](https://www.cisa.gov/resources-tools/groups)
- [News & Events](https://www.cisa.gov/news-events)
- [Directives](https://www.cisa.gov/news-events/directives)
- [News](https://www.cisa.gov/news-events/news)
- [Events](https://www.cisa.gov/news-events/events)
- [Cybersecurity Alerts & Advisories](https://www.cisa.gov/news-events/cybersecurity-advisories)
- [Request a CISA Speaker](https://www.cisa.gov/news-events/request-speaker)
- [Congressional Testimony](https://www.cisa.gov/news-events/congressional-testimony)
- [CISA Conferences](https://www.cisa.gov/news-events/cisa-conferences)
- [CISA Live!](https://www.cisa.gov/cisa-live)
- [Careers](https://www.cisa.gov/careers)
- [Benefits & Perks](https://www.cisa.gov/careers/benefits-perks)
- [Hiring and Recruitment](https://www.cisa.gov/careers/hiring-and-recruitment)
- [New Employee Orientation & Onboarding](https://www.cisa.gov/careers/new-employee-orientation-and-onboarding)
- [Students & Recent Graduates](https://www.cisa.gov/careers/students-recent-graduates-employment-opportunities)
- [Veteran and Military Spouses](https://www.cisa.gov/careers/veteran-and-military-spouse-employment-opportunities)
- [About](https://www.cisa.gov/about)
- [Divisions & Offices](https://www.cisa.gov/about/divisions-offices)
- [Regions](https://www.cisa.gov/about/regions)
- [Leadership](https://www.cisa.gov/about/leadership)
- [Doing Business with CISA](https://www.cisa.gov/about/doing-business-cisa)
- [Site Links](https://www.cisa.gov/site-links)
- [CISA GitHub](https://www.cisa.gov/cisa-github)
- [CISA Central](https://www.cisa.gov/about/cisa-central)
- [Contact Us](https://www.cisa.gov/about/contact-us)
- [Subscribe](https://public.govdelivery.com/accounts/USDHSCISA/subscriber/new?topic_id=USDHSCISA_138)
- [Transparency and Accountability](https://www.cisa.gov/about/transparency-and-accountability)
- [Policies & Plans](https://www.cisa.gov/about/policies-plans)
- [ICS Advisories](https://www.cisa.gov/news-events/ics-advisories)
- [Opens in a new window](https://www.linkedin.com/sharing/share-offsite/?url=https://www.cisa.gov/news-events/ics-advisories/icsa-24-123-01)
- [Industrial Control System Vulnerabilities](https://www.cisa.gov/topics/industrial-control-systems/industrial-control-system-vulnerabilities)
- [View CSAF](https://github.com/cisagov/CSAF)
- [USE OF HARD-CODED PASSWORD CWE-259](https://cwe.mitre.org/data/definitions/259.html)
- [CVE-2024-34025](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2024-34025)
- [AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.0#CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H)
- [CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N](https://www.first.org/cvss/calculator/4.0#CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N)
- [CVE-2024-33625](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2024-33625)
- [RELATIVE PATH TRAVERSAL CWE-23](https://cwe.mitre.org/data/definitions/23.html)
- [CVE-2024-33615](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2024-33615)
- [AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.0#CVSS:3.0/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H)
- [CVSS:4.0/AV:N/AC:L/AT:N/PR:L/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N](https://www.first.org/cvss/calculator/4.0#CVSS:4.0/AV:N/AC:L/AT:N/PR:L/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N)
- [USE OF HARD-CODED CREDENTIALS CWE-798](https://cwe.mitre.org/data/definitions/798.html)
- [CVE-2024-32053](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2024-32053)
- [ACTIVE DEBUG CODE CWE-489](https://cwe.mitre.org/data/definitions/489.html)
- [CVE-2024-32047](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2024-32047)
- [STORING PASSWORDS IN A RECOVERABLE FORMAT CWE-257](https://cwe.mitre.org/data/definitions/257.html)
- [CVE-2024-32042](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2024-32042)
- [AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:N/A:N](https://www.first.org/cvss/calculator/3.0#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:N/A:N)
- [CVSS:4.0/AV:N/AC:L/AT:N/PR:H/UI:N/VC:H/VI:N/VA:N/SC:N/SI:N/SA:N](https://www.first.org/cvss/calculator/4.0#CVSS:4.0/AV:N/AC:L/AT:N/PR:H/UI:N/VC:H/VI:N/VA:N/SC:N/SI:N/SA:N)
- [IMPROPER NEUTRALIZATION OF SPECIAL ELEMENTS USED IN AN SQL COMMAND ('SQL INJECTION') CWE-89](https://cwe.mitre.org/data/definitions/89.html)
- [CVE-2024-31856](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2024-31856)
- [USE OF HARD-CODED CRYPTOGRAPHIC KEY CWE-321](https://cwe.mitre.org/data/definitions/321.html)
- [CVE-2024-31410](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2024-31410)
- [AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:H/A:N](https://www.first.org/cvss/calculator/3.0#CVSS:3.0/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:H/A:N)
- [CVSS:4.0/AV:N/AC:L/AT:N/PR:L/UI:N/VC:N/VI:H/VA:N/SC:N/SI:N/SA:N](https://www.first.org/cvss/calculator/4.0#CVSS:4.0/AV:N/AC:L/AT:N/PR:L/UI:N/VC:N/VI:H/VA:N/SC:N/SI:N/SA:N)
- [INCORRECT AUTHORIZATION CWE-863](https://cwe.mitre.org/data/definitions/863.html)
- [CVE-2024-31409](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2024-31409)
- [AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N](https://www.first.org/cvss/calculator/3.0#CVSS:3.0/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N)
- [CVSS:4.0/AV:N/AC:L/AT:P/PR:L/UI:N/VC:H/VI:N/VA:N/SC:N/SI:N/SA:N](https://www.first.org/cvss/calculator/4.0#CVSS:4.0/AV:N/AC:L/AT:P/PR:L/UI:N/VC:H/VI:N/VA:N/SC:N/SI:N/SA:N)
- [v4.10.1 or later version](https://www.cyberpower.com/global/en/product/sku/powerpanel_business_for_windows#downloads)
- [not accessible from the internet](https://www.cisa.gov/uscert/ics/alerts/ICS-ALERT-10-301-01)
- [control systems security recommended practices](https://www.cisa.gov/resources-tools/resources/ics-recommended-practices)
- [Improving Industrial Control Systems Cybersecurity with Defense-in-Depth Strategies](https://us-cert.cisa.gov/sites/default/files/recommended_practices/NCCIC_ICS-CERT_Defense_in_Depth_2016_S508C.pdf)
- [proactive defense of ICS assets](https://www.cisa.gov/sites/default/files/publications/Cybersecurity_Best_Practices_for_Industrial_Control_Systems.pdf)
- [ICS-TIP-12-146-01B--Targeted Cyber Intrusion Detection and Mitigation Strategies](https://www.cisa.gov/uscert/ics/tips/ICS-TIP-12-146-01B)
- [Notification](https://www.cisa.gov/notification)
- [Privacy & Use](https://www.cisa.gov/privacy-policy)
- [Critical Manufacturing Sector](https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience/critical-infrastructure-sectors/critical-manufacturing-sector)
- [product survey](https://cisasurvey.gov1.qualtrics.com/jfe/form/SV_9n4TtB8uttUPaM6?product=https://www.cisa.gov/news-events/ics-advisories/icsa-24-123-01)
- [Dorsett Controls InfoScan](https://www.cisa.gov/news-events/ics-advisories/icsa-26-321-01)
- [Siemens Industrial Automation Software Products](https://www.cisa.gov/news-events/ics-advisories/icsa-26-321-03)
- [Siemens Industrial Software Products](https://www.cisa.gov/news-events/ics-advisories/icsa-26-321-04)
- [Siemens meta-iot2050](https://www.cisa.gov/news-events/ics-advisories/icsa-26-321-11)
- [Return to top](https://www.cisa.gov/news-events/ics-advisories/icsa-24-123-01#top)
- [Facebook](https://www.facebook.com/CISA)
- [X](https://x.com/CISAgov)
- [LinkedIn](https://www.linkedin.com/company/cybersecurity-and-infrastructure-security-agency)
- [YouTube](https://www.youtube.com/@cisagov)
- [Instagram](https://www.instagram.com/cisagov)
- [RSS](https://www.cisa.gov/subscribe-updates-cisa)
- [1-844-Say-CISA](tel:1-844-Say-CISA)
- [contact@cisa.dhs.gov](mailto:contact@cisa.dhs.gov)
- [Budget and Performance](https://www.dhs.gov/performance-financial-reports)
- [DHS.gov](https://www.dhs.gov/)
- [FOIA Requests](https://www.dhs.gov/foia)
- [No FEAR Act](https://www.cisa.gov/no-fear-act)
- [Office of Inspector General](https://www.oig.dhs.gov/)
- [The White House](https://www.whitehouse.gov/)
- [USA.gov](https://www.usa.gov/)
- [Website Feedback](https://www.cisa.gov/forms/feedback)
