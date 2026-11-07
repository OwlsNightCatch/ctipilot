Title: Security Advisory

URL Source: https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0014

Published Time: Fri, 15 Aug 2025 20:21:44 GMT

Markdown Content:
SonicWall SonicOS Affected By Multiple Vulnerabilities

8.8

Advisory ID SNWLID-2026-0014
First Published 2026-11-06
Last Updated 2026-11-06
Workaround false
Status Applicable
CVE CVE-2026-77708, CVE-2026-77709, CVE-2026-82308, CVE-2026-107154, CVE-2026-107155, CVE-2026-19703, CVE-2026-19868
CWE CWE-121, CWE-122, CWE-942, CWE-798, CWE-916, CWE-308, CWE-291
CVSS v3 8.8
CVSS Vector CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
Direct Link[](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0014)

1) CVE-2026-107155 - Permissive Cross-domain Policy Vulnerability

A permissive cross-domain policy vulnerability has been identified in the SonicOS management interface, which in specific conditions could potentially enable a remote unauthenticated attacker to perform unauthorized operations.

CVSS Score: 8.8  
CVSS Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H  
CWE-942: Permissive Cross-domain Security Policy with Untrusted Domains

2) CVE-2026-107154 - Session Validation Vulnerability

A session validation vulnerability has been identified in the SonicOS management interface, which in specific conditions could potentially enable a remote unauthenticated attacker to perform unauthorized operations.

CVSS Score: 8.8  
CVSS Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H  
CWE-291: Reliance on IP Address for Authentication

3) CVE-2026-82308 - Pre-authentication Heap Buffer Overflow Vulnerability in SSL-VPN

A pre-authentication heap-based buffer overflow vulnerability has been identified in the SonicOS SSL-VPN service, which could potentially enable a remote unauthenticated attacker to cause an application level denial of service.

CVSS Score: 7.5  
CVSS Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H  
CWE-122: Heap-based Buffer Overflow

4) CVE-2026-19868 - SSLVPN Authentication Enforcement Vulnerability via Alternate Authentication Methods

An authentication enforcement vulnerability in SonicOS SSLVPN service may allow a user with valid credentials for an alternate authentication method to bypass SAML authentication controls. Successful exploitation may also bypass SAML-enforced multi-factor authentication (MFA).

IMPORTANT: SonicWall PSIRT has investigated a report indicating potential exploitation of this vulnerability. Customers are strongly urged to upgrade to the latest release as soon as possible to mitigate the associated risks.

NOTE: This vulnerability ONLY impacts the SonicOS SSLVPN interface or service if SAML is enabled for SSLVPN logins.

CVSS Score: 7.1  
CVSS Vector: CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:C/C:H/I:L/A:N  
CWE-308: Use of Single-factor Authentication

5)CVE-2026-77708 - Pre-authentication Stack Buffer Overflow Vulnerability in TACACS+

A pre-authentication stack-based buffer overflow vulnerability has been identified in the SonicOS TACACS+ authentication client, which in specific conditions could potentially enable a remote unauthenticated attacker to cause an application level denial of service.

CVSS Score: 5.9  
CVSS Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:H  
CWE-121: Stack-based Buffer Overflow

6)CVE-2026-77709 - Pre-authentication Heap Buffer Overflow Vulnerability in TACACS+

A pre-authentication heap-based buffer overflow vulnerability has been identified in the SonicOS TACACS+ authentication client, which in specific conditions could potentially enable a remote unauthenticated attacker to cause an application level denial of service.

CVSS Score: 5.9  
CVSS Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:H  
CWE-122: Heap-based Buffer Overflow

7)CVE-2026-19703 - Weak Password Hashing

A weak password hashing vulnerability has been identified on SonicOS virtual appliances, which in specific conditions could potentially enable an attacker with existing local access to disclose a platform credential. The credential provides access to a limited subset of platform settings.

CVSS Score: 5.2  
CVSS Vector: CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:L/A:N  
CWE-916: Use of Password Hash With Insufficient Computational Effort  
CWE-798: Use of Hard-coded Credentials

None.

Links/Buttons:
- [](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0014)
