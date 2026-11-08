---
title: oss-security
url: https://www.openwall.com/lists/oss-security/2026/11/04/9
hostname: openwall.com
sitename: openwall.com
date: "2026-11-04"
fingerprint: "893496167414f222"
---
|   |  | 

|  | 

|  [Hash Suite - Windows password security audit tool. GUI, reports in PDF.](https://hashsuite.openwall.net) | 

Message-ID: \<CAEvdU\_2iBxNTR=q0qJHtMbJn4mjtmLrXJ7XzdpYvgFvd6p1FhQ@mail.gmail.com>
Date: Wed, 4 Nov 2026 17:12:59 +0100
From: Jacopo Cappellato \<jacopoc@...che.org>
To: oss-security@...ts.openwall.com
Subject: Apache OFBiz: CVE Announcements
Multiple security vulnerabilities have been identified in Apache
OFBiz, including some critical issues.
Affected versions: All versions prior to 24.09.08.
Mitigation:
Users are advised to upgrade to Apache OFBiz 24.09.08, which addresses
these vulnerabilities.
Vulnerabilities:
CVE-2026-66903: Authenticated Path Traversal in Catalog Image Management
CVE-2026-68524: Pre-Authentication Remote Code Execution via
Attacker-Controlled Screen Definition Loading
CVE-2026-71901: Dispatch arbitrary internal services on SFA component
CVE-2026-73577: Unauthenticated path-suffix view authorization bypass
CVE-2026-73578: Unauthenticated saved-view authorization bypass with RCE impact
CVE-2026-73580: Unauthenticated HR organization and employee disclosure
CVE-2026-74841: Denial of Service via unauthenticated userTenantId in
multitenant mode
CVE-2026-76150: Authenticated path traversal and missing authorization
check in replaceImageToExistImage
CVE-2026-76152: Authenticated path traversal and missing authorization
check in imageCrop and imageRotate services
CVE-2026-81734: Missing authorization - catalog quick-admin product writes
CVE-2026-81744: Authorization bypass - self-grant content OWNER
CVE-2026-81808: Missing authorization - search-result bulk catalog mutation
CVE-2026-81815: SQL injection - performFind ignore-case values, MySQL/MariaDB
CVE-2026-81816: XML external entity injection (XXE)
CVE-2026-81828: Server-side request forgery in SurveyWrapper
CVE-2026-82894: Content renderer runs a service name stored on the row
CVE-2026-82902: Unfiltered server-side URL fetch in webtools viewdatafile
CVE-2026-82904: Unbounded multi-form row count from a parameter name
CVE-2026-82907: externalLoginKey honoured pre-auth, reusable and unbound
CVE-2026-82910: renderLink compiles link parameters as FreeMarker source
CVE-2026-82912: Unsandboxed Groovy compiled from a service parameter
CVE-2026-82916: webtools xmldsdump exports any entity to any path
CVE-2026-82960: Widget use-when Expression Injection Bypasses Groovy
Sandbox for authenticated RCE
CVE-2026-83538: Unauthenticated disclosure through HR, Catalog, and
Order Manager helpers
CVE-2026-83542: Unauthenticated RCE via login-page widget injection
CVE-2026-84183: Content Manager VIEW-only RCE in updateLayout
CVE-2026-84728: Cross-tenant authorization bypass in mapped-domain login
CVE-2026-85627: Authenticated Code Execution Vulnerability
CVE-2026-92887: REST API authentication bypassed by default when the
auth attribute is omitted from a .rest.xml operation
CVE-2026-97355: Hard-coded Credentials in AdminServer Enable
Unauthenticated Denial of Service
CVE-2026-97356: Insufficiently Protected Credentials in ViewFile
Enable Authentication Bypass
CVE-2026-100168: Missing Authorization vulnerability
CVE-2026-100228: Improper Input Validation in Order Returns Enables
Unauthorized Refund Price Manipulation
CVE-2026-105325: Missing authorization in payment application services
allows view-only users to modify payment allocations
CVE-2026-105330: Use of Hard-coded Cryptographic Key in JWT Token
Authentication Enables Unauthenticated Administrative Access
CVE-2026-105461: Missing authorization in updateOrderItems allows
view-only users to modify order prices and quantities
CVE-2026-109129: Authorization Bypass Through User-Controlled Key in
OrderServices Enables Unauthorized Payment Preference Modification
CVE-2026-109837: Authorization Bypass Through User-Controlled Key in
Order Returns Enables Cross-Party OrderItem Association
CVE-2026-109856: Missing Authorization in Financial Account Services
Enables Unauthorized Balance Manipulation
CVE-2026-109928: Incorrect Authentication Algorithm Implementation in
Password Reset Enables Full Account Takeover
CVE-2026-114229: Reflected Cross-site Scripting in Catalog Image
Viewer Enables Script Execution in a User Session
CVE-2026-114233: Incorrect Privilege Assignment in Order Manager
Enables Unauthorized Modification of Approved Orders
CVE-2026-114235: Direct Request in Order Manager Enables Unauthorized
Tracking Number Modification
CVE-2026-114271: Authorization Bypass Through User-Controlled Key in
Shopping Lists Enables Cross-Party Shopping List Modification
CVE-2026-114272: Authorization Bypass Through User-Controlled Key in
Content Viewing Enables Unauthorized Content Disclosure
CVE-2026-114277: Janrain Engage Social Login Improperly Binds External
Identities to Local Accounts
References:
- Apache OFBiz: [https://ofbiz.apache.org/](https://ofbiz.apache.org/)
- CVE details: [https://www.cve.org/](https://www.cve.org/)

[Powered by blists](https://www.openwall.com/blists/) - [more mailing lists](https://lists.openwall.net)

Please check out the
[Open Source Software Security Wiki](https://oss-security.openwall.org/wiki/), which is counterpart to this
[mailing list](https://oss-security.openwall.org/wiki/mailing-lists/oss-security).

Confused about [mailing lists](https://www.openwall.com/lists/) and their use?
[Read about mailing lists on Wikipedia](https://en.wikipedia.org/wiki/Electronic_mailing_list)
and check out these
[guidelines on proper formatting of your messages](https://www.complang.tuwien.ac.at/anton/mail-news-errors.html).
