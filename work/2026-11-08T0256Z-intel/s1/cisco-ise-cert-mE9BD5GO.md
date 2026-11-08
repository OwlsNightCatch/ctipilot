---
title: "Cisco Security Advisory: Cisco Identity Services Engine Authorization Bypass Vulnerability"
url: https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ise-cert-mE9BD5GO
hostname: cisco.com
description: A vulnerability in the authorization mechanism of Cisco Identity Services Engine (ISE) and Cisco ISE Passive Identity Connector (ISE-PIC) could allow an unauthenticated, remote attacker to obtain an endpoint identity certificate. This vulnerability is due to improper authorization checks. An attacker could exploit this vulnerability by sending a crafted request to an affected device. A successful exploit could allow the attacker to bypass authorization to obtain an endpoint certificate. Cisco has released software updates that address this vulnerability. There are no workarounds that address this vulnerability. This advisory is available at the following link:https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ise-cert-mE9BD5GO
sitename: sec.cloudapps.cisco.com
date: "2026-04-11"
fingerprint: ec7219c34852e78d
---
# Cisco Security Advisory

# Cisco Identity Services Engine Authorization Bypass Vulnerability

[Base 5.3](https://sec.cloudapps.cisco.com/security/center/cvssCalculator.x?version=3.1&vector=CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N)

**Click Icon to Copy Verbose Score**

CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N/E:X/RL:X/RC:X

- A vulnerability in the authorization mechanism of Cisco Identity Services Engine (ISE) and Cisco ISE Passive Identity Connector (ISE-PIC) could allow an unauthenticated, remote attacker to obtain an endpoint identity certificate. This vulnerability is due to improper authorization checks. An attacker could exploit this vulnerability by sending a crafted request to an affected device. A successful exploit could allow the attacker to bypass authorization to obtain an endpoint certificate. Cisco has released software updates that address this vulnerability. There are no workarounds that address this vulnerability. This advisory is available at the following link:
[https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ise-cert-mE9BD5GO](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ise-cert-mE9BD5GO)

- ## Vulnerable Products At the time of publication, this vulnerability affected Cisco ISE and Cisco ISE-PIC, regardless of device configuration. For information about which Cisco software releases were vulnerable at the time of publication, see the [Fixed Software](https://sec.cloudapps.cisco.com#fs) section of this advisory. See the Details section in the bug ID(s) at the top of this advisory for the most complete and current information.
## Products Confirmed Not Vulnerable Only products listed in the [Vulnerable Products](https://sec.cloudapps.cisco.com#vp) section of this advisory are known to be affected by this vulnerability.


- There are no workarounds that address this vulnerability.


- Cisco considers any workarounds and mitigations (if applicable) to be temporary solutions until an upgrade to a fixed software release is available. To remediate this vulnerability and avoid future exposure as described in this advisory, Cisco strongly recommends that customers upgrade to the fixed software indicated in this advisory. ### Fixed Releases At the time of publication, the release information in the following table was accurate. See the Details section in the bug ID(s) at the top of this advisory for the most complete and current information. The left column lists Cisco software releases, and the right column indicates whether a release was affected by the vulnerability that is described in this advisory and which release included the fix for this vulnerability. Cisco ISE or ISE-PIC Release First Fixed Release 3.1 3.1 Patch 12 3.2 3.2 Patch 11 3.3 3.3 Patch 12 3.4 3.4 Patch 7 3.5\* 3.5 Patch 4 \*Cisco ISE-PIC has reached the end-of-sale date. Release 3.4 is the last supported release. **Note:** These fixes are also included as part of the broader hardening improvements that are disclosed in the security advisory [Cisco Identity Services Engine Hardening Release: September 2026](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-ise-XU5EwX5T).
For instructions on upgrading a device, see the Upgrade Guides on the [Cisco Identity Service Engine](https://www.cisco.com/c/en/us/support/security/identity-services-engine/series.html) support page.
The Cisco Product Security Incident Response Team (PSIRT) validates only the affected and fixed release information that is documented in this advisory.

- The Cisco PSIRT is not aware of any public announcements or malicious use of the vulnerability that is described in this advisory.

- Cisco would like to thank independent security researcher Nicholas Michael Kloster for reporting this vulnerability.

- To learn about Cisco security vulnerability disclosure policies and publications, see the [Security Vulnerability Policy](http://www.cisco.com/web/about/security/psirt/security_vulnerability_policy.html). This document also contains instructions for obtaining fixed software and receiving security vulnerability information from Cisco.
For additional information on Cisco's vulnerability management, disclosure cadence, and software patching strategy, see [Cisco's Transition to a Risk-Based Vulnerability Disclosure Model](https://sec.cloudapps.cisco.com/security/center/resources/risk-based-disclosure).

- Version Description Section Status Date 1.1 Added the middle name of the researcher. Source Final 2026-NOV-04 1.0 Initial public release. - Final 2026-NOV-04 [Show Less]

- ### SOFTWARE DOWNLOADS AND TECHNICAL SUPPORT The [Cisco Support and Downloads](https://www.cisco.com/c/en/us/support/index.html) page on Cisco.com provides information about licensing and downloads. This page can also display customer device support coverage for customers who use the My Devices tool. Please note that customers may download only software that was procured from Cisco directly or through a Cisco authorized reseller or partner and for which the license is still valid.
Customers who purchase directly from Cisco but do not hold a Cisco service contract and customers who make purchases through third-party vendors but are unsuccessful in obtaining fixed software through their point of sale should obtain upgrades by contacting the [Cisco Technical Assistance Center (TAC)](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html). Customers should have the product serial number available and be prepared to provide the URL of this advisory as evidence of entitlement to a free upgrade.
When [considering software upgrades](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#fixes), customers are advised to regularly consult [the advisories](https://www.cisco.com/go/psirt) for the relevant Cisco products to determine exposure and a complete upgrade solution. In all cases, customers should ensure that the devices to be upgraded contain sufficient memory and confirm that current hardware and software configurations will continue to be supported properly by the new release. If the information is not clear, customers are advised to contact the [Cisco Technical Assistance Center (TAC)](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html) or their contracted maintenance providers.
### LEGAL DISCLAIMER DETAILS CISCO DOES NOT MAKE ANY EXPRESS OR IMPLIED GUARANTEES OR WARRANTIES OF ANY KIND, INCLUDING THE WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR USE. WITHOUT LIMITING THE GENERALITY OF THE FOREGOING, CISCO DOES NOT GUARANTEE THE ACCURACY OR COMPLETENESS OF THIS INFORMATION. THIS DOCUMENT IS PROVIDED ON AN "AS IS" BASIS. YOUR USE OF THE INFORMATION ON THE DOCUMENT OR MATERIALS LINKED FROM THE DOCUMENT IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS DOCUMENT AT ANY TIME. Copies or summaries of the information contained in this Security Advisory may lack important information or contain factual errors. Customers are advised to visit the [Cisco Security Advisories](https://www.cisco.com/go/psirt) page for the most recent version of this Security Advisory. The Cisco Product Security Incident Response Team (PSIRT) assesses only the affected and fixed release information that is documented in this advisory. See the [Cisco Security Vulnerability Policy](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#fixes) for more information.
