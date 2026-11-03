# extract: served via jina
Title: NetApp Product Security

URL Source: https://security.netapp.com/advisory/NTAP-20261021-0021

Markdown Content:
October 2026 PHP Vulnerabilities in NetApp Products

#### Summary

PHP versions 8.2.x prior to 8.2.35, 8.3.x prior to 8.3.36, 8.4.x prior to 8.4.27 and 8.5.x prior to 8.5.12 are susceptible to vulnerabilities referred to as php2shell which when successfully exploited could lead to unauthenticated remote code execution.

#### Impact

Successful exploitation of these vulnerabilities could lead to disclosure of sensitive information, addition or modification of data, or Denial of Service (DoS).

ONTAP 9:  
 Affected only by CVE-2026-109618. An unauthenticated attacker could potentially gain access as the www user but would be restricted to the PHP jail, limiting the scope of exploit.

#### Vulnerability Scoring Details

| CVE ID | CVSS Score | Vector |
| --- | --- | --- |
| [CVE-2026-109618](https://nvd.nist.gov/vuln/detail/CVE-2026-109618) | CRITICAL (9.2) | CVSS:4.0/AV:N/AC:H/AT:P/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N |
| [CVE-2026-109619](https://nvd.nist.gov/vuln/detail/CVE-2026-109619) | CRITICAL (9.2) | CVSS:4.0/AV:N/AC:H/AT:P/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N |

#### Exploitation and Public Announcements

NetApp is aware of public discussion of this vulnerability.

#### References

NetApp will continue to update this advisory as additional information becomes available.

**This advisory should be considered the single source of current, up-to-date, authorized and accurate information from NetApp regarding Full Support products and versions.**

This document is provided solely for informational purposes. All information is based upon NetApp’s current knowledge and understanding of the hardware and software products tested by NetApp, and the methodology and assumptions used by NetApp. NetApp is not responsible for any errors or omissions that may be contained herein, and no warranty, representation, or other legal commitment or obligation is being provided by NetApp. © 2026 NetApp, Inc. All rights reserved. No portions of this document may be reproduced without prior written consent of NetApp, Inc.

Links/Buttons:
- [Security Portal](https://security.netapp.com/)
- [Security Advisories](https://security.netapp.com/advisory)
- [CVE-2026-109618](https://nvd.nist.gov/vuln/detail/CVE-2026-109618)
- [CVE-2026-109619](https://nvd.nist.gov/vuln/detail/CVE-2026-109619)
- [https://www.php.net/archive/2026.php#2026-10-21-5](https://www.php.net/archive/2026.php#2026-10-21-5)
- [https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w](https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w)
- [https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp](https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp)
