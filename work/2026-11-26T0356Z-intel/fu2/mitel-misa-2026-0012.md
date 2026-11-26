---
title: Mitel Product Security Advisory MISA-2026-0012
url: https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012
hostname: mitel.com
sitename: Mitel
date: "2026-11-16"
fingerprint: bc539cd3ae937083
language: en
image: https://www.mitel.com/sites/default/files/2026-03/social-hero-home-2-1200x630px.jpg
filedate: "2026-11-26"
---
# Mitel Product Security Advisory MISA-2026-0012

## MiCollab Multiple Vulnerabilities

Advisory ID: MISA-2026-0012

First Issue Date: 2026-11-16

Last Updated: 2026-11-24

Revision: 2.0

### **Summary**

An arbitrary file upload vulnerability, CVE-2026-133275 (MTLVULN-1861), has been identified in the Audio, Web and Video Conferencing (AWV) Component of MiCollab, which, if successfully exploited, could allow an unauthenticated attacker to conduct an arbitrary file upload attack due to insufficient file type validation. A successful exploit of this vulnerability could allow an attacker to upload arbitrary files to the target system. The vulnerability severity is rated as medium.

An XML injection vulnerability, CVE-2026-133303 (MTLVULN-1862), has been identified in the Audio, Web and Video Conferencing (AWV) component of MiCollab, which, if successfully exploited, could allow an unauthenticated attacker to leverage pre-staged malicious content to conduct an XML injection attack due to insufficient parameter validation. A successful exploit of this vulnerability could allow an attacker to execute arbitrary commands within the context of the system, with potential impacts on the confidentiality, integrity and availability of the system. The vulnerability severity is rated as critical.

An unauthorized access vulnerability, CVE-2026-133311 (MTLVULN-1863), has been identified in the Audio, Web, and Video Conferencing (AWV) Component of MiCollab, which, if successfully exploited, could allow an unauthenticated attacker, with knowledge of a specific system-generated random identifier or pre-staged content, to conduct an unauthorized access attack due to improper authentication mechanisms. A successful exploit of this vulnerability could allow an attacker to obtain sensitive information. The vulnerability is limited to the affected functionality and does not provide unrestricted access to arbitrary files elsewhere on the system. The vulnerability severity is rated as medium.

A command injection vulnerability, CVE-2026-133323 (MTLVULN-1864), has been identified in the Audio, Web, and Video Conferencing (AWV) Component of MiCollab, which, if successfully exploited, could allow an unauthenticated attacker to conduct a blind command injection attack due to insufficient parameter sanitization. A successful exploit of this vulnerability requires could allow an attacker to execute arbitrary commands within the context of the system, with potential impacts to the integrity, and availability of the system. The vulnerability severity is rated as critical.

An authentication bypass vulnerability, CVE-2026-133324 (MTLVULN-1877), has been identified in the Audio, Web, and Video Conferencing (AWV) Component of MiCollab, which, if successfully exploited, could allow an unauthenticated attacker to conduct an authentication bypass attack due to improper handling of authentication. A successful exploit of this vulnerability could allow an attacker to bypass authentication controls and perform unauthorized actions within the context of the application. The vulnerability severity is rated as medium.

Exploiting these vulnerabilities together can significantly amplify their impact.

Mitel is recommending customers with affected product versions apply the fixes in the highlighted solution.

### **Affected Products and Solutions**

This security advisory provides information on the following products:

| **PRODUCT NAME**  | **VERSION(S) AFFECTED**  | **SOLUTION(S) AVAILABLE**  | 
| MiCollab | 10.3 (10.3.0.18) and earlier  | Mitel provided a patch available for release 10.3 (10.3.0.18) that addresses these vulnerabilities. Upgrade to this release and apply the provided patch, or upgrade to a later release.  See the Security Knowledge Base article KB000129195 for instructions on applying the available patch. | 

Product statements are related only to supported product versions. Products that have reached End of Support status are not considered.


### **Vulnerability Severity**

The following products have been identified as affected:

| **PRODUCT NAME**  | **CVE ID**  | **SEVERITY**  | **CVSS 3.1 BASE SCORE**  | 
| MiCollab | CVE-2026-133275 (MTLVULN-1861) | Medium / 5.3 | AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N | 
| MiCollab | CVE-2026-133303 (MTLVULN-1862) | Critical / 9.0 | AV:N/AC:H/PR:N/UI:N/S:C/C:H/I:H/A:H | 
| MiCollab | CVE-2026-133311 (MTLVULN-1863) | Medium / 5.9 | AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N | 
| MiCollab | CVE-2026-133323 (MTLVULN-1864) | Critical / 10.0 | AV:N/AC:L/PR:N/UI:N/S:C/C:N/I:H/A:H | 
| MiCollab | CVE-2026-133324 (MTLVULN-1877) | Medium / 5.3 | AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N | 

Note: The above issues are referenced by their CVE identifiers and Mitel's internal tracking ID.

The identified vulnerabilities carry varied levels of severity including critical.


### **Mitigations / Workarounds**

For customers who are not currently able to implement the recommended solution in a timely manner, the risk may be mitigated by restricting external access to the AWV component. For further details, please refer to the security Knowledge Base article.


### **Solution/ Recommended Action**

Mitel provided a patch available for release 10.3 (10.3.0.18) that addresses these vulnerabilities. Upgrade to this release and apply the provided patch, or upgrade to a later release.

The security update will be included in later MiCollab releases.

Please see Mitel Knowledge Base article [KB000129195](https://mitel.service-now.com/mitel?id=kb_article&sys_id=3e441c0d97285b10cd1b3a871153afc5), “MiCollab Security Update, MTLVULN-1861, MTLVULN-1862, MTLVULN-1863, MTLVULN-1864, MTLVULN-1877”.

If you do not have access to this link, please contact your Mitel Authorized Partner for support.

For further information, please contact Mitel Product Support.


### **References**

CVE-2026-133275, CVE-2026-133303, CVE-2026-133311, CVE-2026-133323, CVE-2026-133324


### **Revision History**

| **Version**  | **Date**  | **Description**  | 
| 1.0 | 2026-11-16 | Initial version | 
| 2.0 | 2026-11-24 | Updated the CVE Numbers | 


## **Publisher and Legal Disclaimer**

**Publisher: Mitel PSIRT / [\[email protected\]](https://www.mitel.com/cdn-cgi/l/email-protection)**

The information provided in this advisory is provided "as is" without warranty of any kind. The information is subject to change without notice. Mitel and its affiliates do not guarantee and accept no legal liability whatsoever arising from or connected to the accuracy, reliability, currency or completeness of the information provided. No part of this document can be reproduced or transmitted in any form or by any means - electronic or mechanical - for any purpose without written permission from Mitel Networks Corporation.
