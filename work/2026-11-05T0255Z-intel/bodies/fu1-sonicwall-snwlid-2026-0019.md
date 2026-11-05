Title: Security Advisory

URL Source: https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0019

Markdown Content:
End-Of-Life (EOL) SonicWall GMS Multiple Vulnerabilities

9.1

Advisory ID SNWLID-2026-0019
First Published 2026-11-03
Last Updated 2026-11-03
Workaround false
Status Applicable
CVE CVE-2026-109593, CVE-2026-109594
CWE CWE-636, CWE-89
CVSS v3 9.1
CVSS Vector CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:H
Direct Link[](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0019)

1) CVE-2026-109593 - End-of-Life (EOL) SonicWall GMS Unauthenticated File Read Vulnerability

An unauthenticated attacker with network access to the SonicWall GMS 9.5.2 and earlier versions may be able to read internal GMS files, potentially exposing sensitive information.

CVSS Score: 9.1  
CVSS Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:H  
 CWE-636: Not Failing Securely ('Failing Open')

2) CVE-2026-109594 - End-of-Life (EOL) SonicWall GMS Authenticated SQL Injection Vulnerability

Post-authentication Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability has been identified in the End-of-Life SonicWall GMS 9.5.2 and earlier versions which in specific conditions could potentially allow an authenticated attacker to access or modify information stored in the GMS database.

CVSS Score: 6.8  
 CVSS Vector: CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:N/A:N  
CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')

None.

**Important:** The affected product has reached End-of-Life (EOL). As a result, no remediation or security update will be released for these vulnerabilities. Organizations using the product should be aware of the associated security risks and are strongly encouraged to upgrade to the SonicWall Network Security Manager (NSM).

Links/Buttons:
- [](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0019)
