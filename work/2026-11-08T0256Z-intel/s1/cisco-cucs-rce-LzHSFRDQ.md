---
title: "Cisco Security Advisory: Cisco UCS Central Software Remote Code Execution Vulnerability"
url: https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cucs-rce-LzHSFRDQ
hostname: cisco.com
description: A vulnerability in the web-based management interface of Cisco UCS Central Software could allow an authenticated, remote attacker to achieve remote code execution or conduct information disclosure attacks on an affected device. This vulnerability is due to insufficient validation of user-supplied input in an HTTP request. An attacker could exploit this vulnerability by sending a crafted HTTP request to an affected endpoint on an affected device. A successful exploit could allow the attacker to execute arbitrary commands, write arbitrary files to the filesystem, and obtain sensitive information. To exploit this vulnerability, the attacker must have valid user credentials on the affected device. Cisco has released software updates that address this vulnerability There are no workarounds that address this vulnerability. This advisory is available at the following link:https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cucs-rce-LzHSFRDQ
sitename: sec.cloudapps.cisco.com
date: "2026-04-11"
fingerprint: ec7219564852a30d
---
# Cisco Security Advisory

# Cisco UCS Central Software Remote Code Execution Vulnerability

[Base 7.6](https://sec.cloudapps.cisco.com/security/center/cvssCalculator.x?version=3.1&vector=CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:L/A:L)

**Click Icon to Copy Verbose Score**

CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:L/A:L/E:X/RL:X/RC:X

- A vulnerability in the web-based management interface of Cisco UCS Central Software could allow an authenticated, remote attacker to achieve remote code execution or conduct information disclosure attacks on an affected device. This vulnerability is due to insufficient validation of user-supplied input in an HTTP request. An attacker could exploit this vulnerability by sending a crafted HTTP request to an affected endpoint on an affected device. A successful exploit could allow the attacker to execute arbitrary commands, write arbitrary files to the filesystem, and obtain sensitive information. To exploit this vulnerability, the attacker must have valid user credentials on the affected device. Cisco has released software updates that address this vulnerability There are no workarounds that address this vulnerability. This advisory is available at the following link:
[https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cucs-rce-LzHSFRDQ](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cucs-rce-LzHSFRDQ)

- ## Vulnerable Products This vulnerability affects Cisco UCS Central Software, regardless of device configuration. For information about which Cisco software releases are vulnerable, see the [Fixed Software](https://sec.cloudapps.cisco.com#fs) section of this advisory.
## Products Confirmed Not Vulnerable Only products listed in the [Vulnerable Products](https://sec.cloudapps.cisco.com#vp) section of this advisory are known to be affected by this vulnerability.


- There are no workarounds that address this vulnerability.


- Cisco considers any workarounds and mitigations (if applicable) to be temporary solutions until an upgrade to a fixed software release is available. To remediate this vulnerability and avoid future exposure as described in this advisory, Cisco strongly recommends that customers upgrade to the fixed software indicated in this advisory. ### Fixed Releases In the following table, the left column lists Cisco software releases. The right column indicates whether a release is affected by the vulnerability that is described in this advisory and the first release that includes the fix for this vulnerability. Customers are advised to upgrade to an appropriate [fixed software release](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#fixes) as indicated in this section.
Cisco UCS Central Software First Fixed Release 2.0 and earlier Migrate to a fixed release. 2.1 2.1(2c) The Cisco Product Security Incident Response Team (PSIRT) validates only the affected and fixed release information that is documented in this advisory.

- The Cisco PSIRT is not aware of any public announcements or malicious use of the vulnerability that is described in this advisory.

- Cisco would like to thank Anand Murugan of Gulf Business Machines (GBM) for reporting this vulnerability.

- To learn about Cisco security vulnerability disclosure policies and publications, see the [Security Vulnerability Policy](http://www.cisco.com/web/about/security/psirt/security_vulnerability_policy.html). This document also contains instructions for obtaining fixed software and receiving security vulnerability information from Cisco.
For additional information on Cisco's vulnerability management, disclosure cadence, and software patching strategy, see [Cisco's Transition to a Risk-Based Vulnerability Disclosure Model](https://sec.cloudapps.cisco.com/security/center/resources/risk-based-disclosure).

- Version Description Section Status Date 1.0 Initial public release. - Final 2026-NOV-04 [Show Less]

- ### SOFTWARE DOWNLOADS AND TECHNICAL SUPPORT The [Cisco Support and Downloads](https://www.cisco.com/c/en/us/support/index.html) page on Cisco.com provides information about licensing and downloads. This page can also display customer device support coverage for customers who use the My Devices tool. Please note that customers may download only software that was procured from Cisco directly or through a Cisco authorized reseller or partner and for which the license is still valid.
Customers who purchase directly from Cisco but do not hold a Cisco service contract and customers who make purchases through third-party vendors but are unsuccessful in obtaining fixed software through their point of sale should obtain upgrades by contacting the [Cisco Technical Assistance Center (TAC)](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html). Customers should have the product serial number available and be prepared to provide the URL of this advisory as evidence of entitlement to a free upgrade.
When [considering software upgrades](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#fixes), customers are advised to regularly consult [the advisories](https://www.cisco.com/go/psirt) for the relevant Cisco products to determine exposure and a complete upgrade solution. In all cases, customers should ensure that the devices to be upgraded contain sufficient memory and confirm that current hardware and software configurations will continue to be supported properly by the new release. If the information is not clear, customers are advised to contact the [Cisco Technical Assistance Center (TAC)](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html) or their contracted maintenance providers.
### LEGAL DISCLAIMER DETAILS CISCO DOES NOT MAKE ANY EXPRESS OR IMPLIED GUARANTEES OR WARRANTIES OF ANY KIND, INCLUDING THE WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR USE. WITHOUT LIMITING THE GENERALITY OF THE FOREGOING, CISCO DOES NOT GUARANTEE THE ACCURACY OR COMPLETENESS OF THIS INFORMATION. THIS DOCUMENT IS PROVIDED ON AN "AS IS" BASIS. YOUR USE OF THE INFORMATION ON THE DOCUMENT OR MATERIALS LINKED FROM THE DOCUMENT IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS DOCUMENT AT ANY TIME. Copies or summaries of the information contained in this Security Advisory may lack important information or contain factual errors. Customers are advised to visit the [Cisco Security Advisories](https://www.cisco.com/go/psirt) page for the most recent version of this Security Advisory. The Cisco Product Security Incident Response Team (PSIRT) assesses only the affected and fixed release information that is documented in this advisory. See the [Cisco Security Vulnerability Policy](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#fixes) for more information.
