---
title: SSA-935812
url: https://cert-portal.siemens.com/productcert/html/ssa-935812.html
hostname: siemens.com
sitename: cert-portal.siemens.com
date: "2026-11-20"
fingerprint: a431ff4625322ec5
filedate: "2026-11-28"
---
| Publication Date: |  | 
| Last Update: |  | 
| Current Version: | V1.0 | 
| CVSS v3.1 Base Score: | 8.1 | 
| CVSS v4.0 Base Score: | 9.2 | 

| Affected Product and Versions | Remediation | 
|---|---|
| All versions | Currently no fix is available | 
| All versions | Currently no fix is available | 
| All versions | Currently no fix is available | 
| All versions | Currently no fix is available | 
| All versions | Currently no fix is available | 

| Known Not Affected Products | Reason | 
|---|---|
| All versions not affected by                        [all CVEs](https://cert-portal.siemens.com/productcert/html/ssa-935812.html#cves-section) | This product is not affected because HTTP/2 is disabled, and HTTP/3 and SSI are not used. (Vulnerable Code Not in Execute Path) | 
| All versions not affected by                        [all CVEs](https://cert-portal.siemens.com/productcert/html/ssa-935812.html#cves-section) | This product is not affected because HTTP/2 is disabled, and HTTP/3 and SSI are not used. (Vulnerable Code Not in Execute Path) | 
| All versions not affected by                        [all CVEs](https://cert-portal.siemens.com/productcert/html/ssa-935812.html#cves-section) | This product is not affected because HTTP/2 is disabled, and HTTP/3 and SSI are not used. (Vulnerable Code Not in Execute Path) | 
| All versions not affected by                        [all CVEs](https://cert-portal.siemens.com/productcert/html/ssa-935812.html#cves-section) | This product is not affected because HTTP/2 is disabled, and HTTP/3 and SSI are not used. (Vulnerable Code Not in Execute Path) | 
| All versions not affected by                        [all CVEs](https://cert-portal.siemens.com/productcert/html/ssa-935812.html#cves-section) | This product is not affected because HTTP/2 is disabled, and HTTP/3 and SSI are not used. (Vulnerable Code Not in Execute Path) | 

- CVE-2026-121810
- The following measure can be configured using a Web Application Firewall (WAF) or a reverse proxy: Disable HTTP/3/QUIC on affected services.
- CVE-2026-123007
- The following measure can be configured using a Web Application Firewall (WAF) or a reverse proxy: Disable HTTP/2 on affected listeners.
- CVE-2026-123633
- The following measure can be configured using a Web Application Firewall (WAF) or a reverse proxy: Disable HTTP/2 on affected listeners.
- CVE-2026-123634
- Avoid the use of SSI and mirror directives, and do not use variables when configuring the proxy server name.

Please follow the [General Security Recommendations](https://cert-portal.siemens.com/productcert/html/ssa-935812.html#general-recommendations).

As a general security measure, Siemens strongly recommends to protect network access to devices with appropriate mechanisms. In order to operate the devices in a protected IT environment, Siemens recommends to configure the environment according to Siemens' operational guidelines for Industrial Security (Download: [https://www.siemens.com/cert/operational-guidelines-industrial-security](https://www.siemens.com/cert/operational-guidelines-industrial-security)), and to follow the recommendations in the product manuals.
Additional information on Industrial Security by Siemens can be found at: [https://www.siemens.com/industrialsecurity](https://www.siemens.com/industrialsecurity)






This chapter describes all vulnerabilities (CVE-IDs) addressed in this security advisory. Wherever applicable, it also documents the product-specific impact of the individual vulnerabilities.

| CVSS v3.1 Base Score | 8.1 | 
| CVSS v3.1 Vector | CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H | 
| CVSS v4.0 Base Score | 9.2 | 
| CVSS v4.0 Vector | CVSS:4.0/AV:N/AC:H/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N | 
| CWE | CWE-416: Use After Free | 

| CVSS v3.1 Base Score | 8.1 | 
| CVSS v3.1 Vector | CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H | 
| CVSS v4.0 Base Score | 9.2 | 
| CVSS v4.0 Vector | CVSS:4.0/AV:N/AC:H/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N | 
| CWE | CWE-191: Integer Underflow (Wrap or Wraparound) | 

| V1.0 (2026-11-20): | Publication Date |
