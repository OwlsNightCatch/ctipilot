---
title: Mitel Product Security Advisory MISA-2026-0013
url: https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0013
hostname: mitel.com
sitename: Mitel
date: "2026-11-18"
fingerprint: be51dde68a9ab91b
language: en
image: https://www.mitel.com/sites/default/files/2026-03/social-hero-home-2-1200x630px.jpg
filedate: "2026-11-28"
---
# Mitel Product Security Advisory MISA-2026-0013

## OpenScape 4000 and OpenScape 4000 Manager Unauthorized Access and Command Injection Vulnerabilities

Advisory ID: MISA-2026-0013

First Issue Date: 2026-11-18

Last Updated: 2026-11-18

Revision: 1.0

### **Summary**

An unauthorized access vulnerability, MTLVULN-1785, has been identified in the Platform component of OpenScape 4000 and OpenScape 4000 Manager, which if successfully exploited, could allow an unauthenticated attacker to conduct an unauthorized access attack due to improper authentication mechanisms. A successful exploit could allow an attacker to obtain sensitive information and gain unauthorized access to the system, with potential impacts to the confidentiality, integrity, and availability of the system. The vulnerability severity is rated as critical.

A command injection vulnerability, MTLVULN-1786, has been identified in the Platform component of OpenScape 4000 and OpenScape 4000 Manager, which if successfully exploited, could allow an unauthenticated attacker to conduct a command injection attack due to insufficient parameter sanitization. A successful exploit of this vulnerability could allow an attacker to execute arbitrary commands within the context of the system, with potential impacts to the confidentiality, integrity, and availability of the system. The vulnerability severity is rated as critical.

A command injection vulnerability, MTLVULN-1793, has been identified in the Platform component of OpenScape 4000 and OpenScape 4000 Manager, which if successfully exploited, could allow an unauthenticated attacker with adjacent network access to conduct a command injection attack due to insufficient parameter sanitization. A successful exploit of this vulnerability could allow an attacker to execute arbitrary commands within the context of the system, with potential impacts to the confidentiality, integrity, and availability of the system. The vulnerability severity is rated as critical.

Mitel is recommending customers with affected product versions update to the latest release.

### **Affected Products and Solutions**

This security advisory provides information on the following products:

| **PRODUCT NAME**  | **VERSION(S) AFFECTED**  | **SOLUTION(S) AVAILABLE**  | 
| OpenScape 4000 | V11 R0.22 through V11 R2.11, and V10 R1.68 and earlier | Upgrade to OpenScape 4000 version V11 R2.14 or later. Mitel has provided PLT HF5 that is available for version V11 R1.26. Upgrade to this release and apply the provided hotfix, or upgrade to a later release. Mitel has provided a patch that is available for releases V10 R0.28 to V11 R0.22. Upgrade to one of these releases and apply the provided patch. Please see the associated Knowledge Base article for release notes, installation instructions, and additional information regarding these updates. | 
| OpenScape 4000 Manager | V11 R0.22 through V11 R2.11, and V10 R1.34, V10 R1.42, V10 R1.54 and V10 R1.68 | Upgrade to OpenScape 4000 version V11 R2.14 or later. Mitel has provided PLT HF5 that is available for version V11 R1.26. Upgrade to this release and apply the provided hotfix, or upgrade to a later release. Mitel has provided a patch that is available for releases V10 R1.34 to V11 R0.22. Upgrade to one of these releases and apply the provided patch. Please see the associated Knowledge Base article for release notes, installation instructions, and additional information regarding these updates. | 

Product statements are related only to supported product versions. Products which have reached End of Support status are not considered.


### **Vulnerability Severity**

The following products have been identified as affected:

| **PRODUCT NAME**  | **CVE ID**  | **SEVERITY**  | **CVSS 3.1 BASE SCORE**  | 
| OpenScape 4000 and OpenScape 4000 Manager | MTLVULN-1785 | Critical / 10.0 | AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H | 
| OpenScape 4000 and OpenScape 4000 Manager | MTLVULN-1786 | Critical / 10.0 | AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H | 
| OpenScape 4000 and OpenScape 4000 Manager | MTLVULN-1793 | Critical / 9.6 | AV:A/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H | 

Note: The above issue is referenced here by our internal tracking ID. A CVE identifier has been requested but is not yet assigned

The severity of the vulnerabilities is rated critical.


### **Mitigations / Workarounds**

For customers who are not able to implement the recommended solution in a timely manner, enabling Security Mode restricted access can be used as a workaround to prevent exploitation of these vulnerabilities. For further details, please refer to the associated Security Knowledge Base article.


### **Solution/ Recommended Action**

These issues are corrected in OpenScape 4000 V11 R2.14. Also, Mitel has provided PLT HF5 for version OpenScape 4000 V11 R1.26, and patch for releases V10 R0.28 to V11 R0.22.

These issues are corrected in OpenScape 4000 Manager version V11 R2.14. Also, Mitel has provided PLT HF5 for version OpenScape 4000 Manager V11 R1.26 and patch for releases V10 R1.34 to V11 R0.22.

Customers are advised to upgrade to one of these releases and apply the corresponding update, or upgrade to a later release.

Please see Mitel Security Knowledge Base article [KB000129263](https://mitel.service-now.com/mitel?id=kb_article&sys_id=3843741e3b209350b2eb202a85e45a08) "OpenScape 4000 Security Update, MTLVULN-1785, MTLVULN-1786, MTLVULN-1793".

If you do not have access to this link, please contact your Mitel Authorized Partner for support.

For further information, please contact Mitel Product Support.


### **Revision History**

| **Version**  | **Date**  | **Description**  | 
| 1.0 | 2026-11-18 | Initial version | 


## **Publisher and Legal Disclaimer**

**Publisher: Mitel PSIRT / [\[email protected\]](https://www.mitel.com/cdn-cgi/l/email-protection)**

The information provided in this advisory is provided "as is" without warranty of any kind. The information is subject to change without notice. Mitel and its affiliates do not guarantee and accept no legal liability whatsoever arising from or connected to the accuracy, reliability, currency or completeness of the information provided. No part of this document can be reproduced or transmitted in any form or by any means - electronic or mechanical - for any purpose without written permission from Mitel Networks Corporation.
