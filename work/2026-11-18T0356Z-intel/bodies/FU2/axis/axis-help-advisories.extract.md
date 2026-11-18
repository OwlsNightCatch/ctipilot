---
title: Security advisories
url: https://help.axis.com/en-us/security-advisories
hostname: axis.com
sitename: help.axis.com
date: "2026-11-17"
fingerprint: "97012867ed316f49"
---
# Security advisories

[Download PDF](https://help.axis.com/download/release_notes_security_advisories_t10217090_2611.pdf)

## About

The purpose of this registry is to proactively raise awareness and communicate about vulnerabilities that have been analyzed for Axis products and services.

- Axis and OpenSource vulnerabilities are listed below with CVE IDs (CVE = Common Vulnerabilities and Exposures).
- Axis vulnerabilities were previously listed with ACV IDs (ACV = Axis Critical Vulnerability), which changed when Axis was approved as a CVE Numbering Authority (CNA) in April 2021.

Please contact [Axis Technical Support](https://www.axis.com/support) in case you have found a CVE that was reported to be present in AXIS OS and is not registered below.

To learn more please watch the [YouTube video](https://www.youtube.com/watch?v=FkMmAV5gxno) about Vulnerability Management. For more information about Axis work with cybersecurity, see [Cybersecurity resources](https://www.axis.com/support/cybersecurity/resources).

## Axis CVEs

The Axis registry covers vulnerabilities that are specific to Axis products and services. We strongly recommend to update affected devices and services.

### Analytics

#### CVE 2023

| CVE number | CVSS severity | Released version | Security advisory / Vulnerability summary | 
| [CVE-2023-21412](https://www.cve.org/CVERecord?id=CVE-2023-21412) | 7.2 (High) | 2.8.4 | [Axis Security Advisory](https://www.axis.com/dam/public/0b/1c/96/cve-2023-2140712-en-US-409778.pdf) - AXIS License Plate Verifier: User provided input is not sanitized on the “search.cgi” allowing for SQL injections. | 
| [CVE-2023-21411](https://www.cve.org/CVERecord?id=CVE-2023-21411) | 7.2 (High) | 2.8.4 | [Axis Security Advisory](https://www.axis.com/dam/public/0b/1c/96/cve-2023-2140712-en-US-409778.pdf) - AXIS License Plate Verifier: User provided input is not sanitized in the “Settings > Access Control” configuration interface allowing for arbitrary code execution. | 
| [CVE-2023-21410](https://www.cve.org/CVERecord?id=CVE-2023-21410) | 7.2 (High) | 2.8.4 | [Axis Security Advisory](https://www.axis.com/dam/public/0b/1c/96/cve-2023-2140712-en-US-409778.pdf) - AXIS License Plate Verifier: User provided input is not sanitized on the AXIS License Plate Verifier specific “api.cgi” allowing for arbitrary code execution. | 
| [CVE-2023-21409](https://www.cve.org/CVERecord?id=CVE-2023-21409) | 8.4 (High) | 2.8.4 | [Axis Security Advisory](https://www.axis.com/dam/public/0b/1c/96/cve-2023-2140712-en-US-409778.pdf) - AXIS License Plate Verifier: Due to insufficient file permissions, unprivileged users could gain access to unencrypted administrator credentials allowing the configuration of the application. | 
| [CVE-2023-21408](https://www.cve.org/CVERecord?id=CVE-2023-21408) | 8.4 (High) | 2.8.4 | [Axis Security Advisory](https://www.axis.com/dam/public/0b/1c/96/cve-2023-2140712-en-US-409778.pdf) - AXIS License Plate Verifier: Due to insufficient file permissions, unprivileged users could gain access to unencrypted user credentials that are used in the integration interface towards 3rd party systems. | 
| [CVE-2023-21407](https://www.cve.org/CVERecord?id=CVE-2023-21407) | 8.8 (High) | 2.8.4 | [Axis Security Advisory](https://www.axis.com/dam/public/0b/1c/96/cve-2023-2140712-en-US-409778.pdf) - AXIS License Plate Verifier: A broken access control was found allowing for privileged escalation of the operator account to gain administrator privileges. | 

### AXIS Camera Station

#### CVE 2026

| CVE number | CVSS severity | Released version | Security advisory / Vulnerability summary | 
|---|---|---|---|
| [CVE-2026-63287](https://www.cve.org/CVERecord?id=CVE-2026-63287) | 6.5 (Medium) | Pro 6.18 5.59 | [Axis Security Advisory](https://www.axis.com/dam/public/bc/65/61/cve-2026-63287pdf-en-US-561253.pdf) - It was possible for an authenticated non-admin user to modify certain data objects without having the appropriate permissions, which could be used to tamper with audit log creation in AXIS Camera Station. | 
| [CVE-2026-63286](https://www.cve.org/CVERecord?id=CVE-2026-63286) | 7.1 (High) | Pro 6.20 | [Axis Security Advisory](https://www.axis.com/dam/public/c9/5c/29/cve-2026-63286pdf-en-US-560650.pdf) - Database backups were vulnerable to offline attacks. | 
| [CVE-2026-13387](https://www.cve.org/CVERecord?id=CVE-2026-13387) | 3.5 (Low) | Pro 6.18 | [Axis Security Advisory](https://www.axis.com/dam/public/d7/64/a2/cve-2026-13387pdf-en-US-561252.pdf) - A vulnerability related to URL redirection handling during the sign-out flow that could allow a user to be redirected to unintended external content under specific conditions | 
| [CVE-2026-13312](https://www.cve.org/CVERecord?id=CVE-2026-13312) | 9.9 (Critical) | Pro 6.17 5.59 SR 2 | [Axis Security Advisory](https://www.axis.com/dam/public/permalink/289342/cve-2026-13312pdf-en-US_289342.pdf) - A vulnerability that could allow an attacker to compromise a system. | 
| [CVE-2026-12964](https://www.cve.org/CVERecord?id=CVE-2026-12964) | 8.0 (High) | Pro 6.18 | [Axis Security Advisory](https://www.axis.com/dam/public/50/3b/39/cve-2026-12964pdf-en-US-561250.pdf) - A vulnerability allowing for privileged escalation of the viewer account to gain administrator privileges. | 
| [CVE-2026-12963](https://www.cve.org/CVERecord?id=CVE-2026-12963) | 7.4 (High) | Pro 6.18 5.59 | [Axis Security Advisory](https://www.axis.com/dam/public/c5/ba/15/cve-2026-12963pdf-en-US-561249.pdf) - A vulnerability that could allow a viewer account to gain unauthorized access to network attached storage devices on the server | 
| [CVE-2026-12389](https://www.cve.org/CVERecord?id=CVE-2026-12389) | 8.4 (High) | Pro 6.18 5.59 | [Axis Security Advisory](https://www.axis.com/dam/public/1a/bd/41/cve-2026-12389pdf-en-US-561248.pdf) - A vulnerability that could lead to a high privileged authenticated user performing a remote code execution attack. | 
| [CVE-2026-8372](https://www.cve.org/CVERecord?id=CVE-2026-8372) | 8.8 (High) | Pro 6.18 | [Axis Security Advisory](https://www.axis.com/dam/public/09/58/fa/cve-2026-8372pdf-en-US-561247.pdf) - A vulnerability that could allow an attacker to gain unauthorized access. | 
| [CVE-2026-4762](https://www.cve.org/CVERecord?id=CVE-2026-4762) | 8.8 (High) | Pro 6.18 | [Axis Security Advisory](https://www.axis.com/dam/public/1f/4b/66/cve-2026-4762pdf-en-US-561246.pdf) - A vulnerability to perform a privilege escalation attack on the server as a non-admin user. | 

#### CVE 2025

| CVE number | CVSS severity | Released version | Security advisory / Vulnerability summary | 
|---|---|---|---|
| [CVE-2025-13064](https://www.cve.org/CVERecord?id=CVE-2025-13064) | 5.7 (Medium) | Pro 6.14 | [Axis Security Advisory](https://www.axis.com/dam/public/a9/9e/94/cve-2025-13064pdf-en-US-519290.pdf) - A server-side injection made it possible for a malicious admin to manipulate the application to include a malicious script which is executed by the server. | 
| [CVE-2025-12757](https://www.cve.org/CVERecord?id=CVE-2025-12757) | 4.6 (Medium) | Pro 6.14 | [Axis Security Advisory](https://www.axis.com/dam/public/de/38/d3/cve-2025-12757pdf-en-US-519289.pdf) - A AXIS Camera Station Pro feature could be exploited in a way that allows a non-admin user to view information they are not permitted to. | 
| [CVE-2025-12063](https://www.cve.org/CVERecord?id=CVE-2025-12063) | 4.5 (Medium) | Pro 6.14 | [Axis Security Advisory](https://www.axis.com/dam/public/bc/f0/5a/cve-2025-12063pdf-en-US-519288.pdf) - A insecure direct object reference was found that could allow a non-admin user to modify or remove certain data objects without having the appropriate permissions | 
| [CVE-2025-11547](https://www.cve.org/CVERecord?id=CVE-2025-11547) | 7.8 (High) | Pro 6.13 | [Axis Security Advisory](https://www.axis.com/dam/public/permalink/253485/cve-2025-11547pdf-en-US_253485.pdf) - A non-admin user was able to perform a privilege escalation attack on the server. | 
| [CVE-2025-30026](https://www.cve.org/CVERecord?id=CVE-2025-30026) | 4.8 (Medium) | Pro 6.9 5.58 | [Axis Security Advisory](https://www.axis.com/dam/public/a3/42/92/cve-2025-30026pdf-en-US-485735.pdf) - This vulnerability could allow an attacker to bypass authentication requirements. | 
| [CVE-2025-30025](https://www.cve.org/CVERecord?id=CVE-2025-30025) | 4.8 (Medium) | Pro 6.8 5.58 | [Axis Security Advisory](https://www.axis.com/dam/public/f2/28/d2/cve-2025-30025pdf-en-US-517962.pdf) - This vulnerability could allow a local attacker to escalate privileges. | 
| [CVE-2025-30023](https://www.cve.org/CVERecord?id=CVE-2025-30023) | 9.0 (Critical) | Pro 6.9 5.58 | [Axis Security Advisory](https://www.axis.com/dam/public/9b/a5/72/cve-2025-30023pdf-en-US-485733.pdf) - This vulnerability could lead to an authenticated user performing a remote code execution attack. | 
| [CVE-2025-7622](https://www.cve.org/CVERecord?id=CVE-2025-7622) | 5.1 (Medium) | Pro 6.10 5.59 | [Axis Security Advisory](https://www.axis.com/dam/public/c5/9a/3c/cve-2025-7622pdf-en-US-492761.pdf) - A Server-Side Request Forgery (SSRF) vulnerability was discovered that allowed an authenticated attacker to access internal resources on the server. | 
| [CVE-2025-1056](https://www.cve.org/CVERecord?id=CVE-2025-1056) | 6.1 (Medium) | Pro 6.8 | [Axis Security Advisory](https://www.axis.com/dam/public/e4/2e/b2/cve-2025-1056pdf-en-US-479106.pdf) - It was possible for a non-admin user to modify a specific server-file to either create files or change the content of files in an admin-protected location. | 
| [CVE-2025-0926](https://www.cve.org/CVERecord?id=CVE-2025-0926) | 5.9 (Medium) | Pro 6.8 | [Axis Security Advisory](https://www.axis.com/dam/public/9d/fe/3f/cve-2025-0926pdf-en-US-479105.pdf) - It was possible for a non-admin user to remove system files causing a boot loop by redirecting a file deletion when recording video. | 

#### CVE 2024

| CVE number | CVSS severity | Released version | Security advisory / Vulnerability summary | 
|---|---|---|---|
| [CVE-2024-7696](https://www.cve.org/CVERecord?id=CVE-2024-7696) | 6.3 (Medium) | Pro 6.5 | [Axis Security Advisory](https://www.axis.com/dam/public/b3/53/03/cve-2024-7696-en-US-459552.pdf)- It was possible for an authenticated malicious client to tamper with audit log creation in AXIS Camera Station Pro, or perform a Denial-of-Service attack on the AXIS Camera Station server using maliciously crafted audit log entries. | 
| [CVE-2024-6831](https://www.cve.org/CVERecord?id=CVE-2024-6831) | 4.4 (Medium) | Pro 6.4 | [Axis Security Advisory](https://www.axis.com/dam/public/a2/9a/41/cve-2024-6831-en-US-455107.pdf) - It was possible to edit and/or remove views without the necessary permission due to a client-side-only check. | 
| [CVE-2024-6749](https://www.cve.org/CVERecord?id=CVE-2024-6749) | 6.3 (Medium) | Pro 6.4 | [Axis Security Advisory](https://www.axis.com/dam/public/e6/e8/1e/cve-2024-6749-en-US-455106.pdf) - The Incident report feature may expose sensitive credentials on the AXIS Camera Station windows client. If Incident report is not being used with credentials configured this flaw does not apply. | 
| [CVE-2024-6476](https://www.cve.org/CVERecord?id=CVE-2024-6476) | 4.2 (Medium) | Pro 6.4 | [Axis Security Advisory](https://www.axis.com/dam/public/e5/24/82/cve-2024-6476pdf-en-US-455104.pdf) - It was possible for a non-admin user to gain system privileges by redirecting a file deletion upon service restart. | 

### AXIS Device Manager

#### CVE 2025

| CVE number | CVSS severity | Released version | Security advisory / Vulnerability summary | 
|---|---|---|---|
| [CVE-2025-30025](https://www.cve.org/CVERecord?id=CVE-2025-30025) | 4.8 (Medium) | 5.32 | [Axis Security Advisory](https://www.axis.com/dam/public/f2/28/d2/cve-2025-30025pdf-en-US-517962.pdf) - This vulnerability could allow a local attacker to escalate privileges. | 
| [CVE-2025-30024](https://www.cve.org/CVERecord?id=CVE-2025-30024) | 6.8 (Medium) | 5.32 | [Axis Security Advisory](https://www.axis.com/dam/public/01/d9/24/cve-2025-30024pdf-en-US-485734.pdf) - This vulnerability could be exploited to carry out a man-in-the-middle attack. | 
| [CVE-2025-30023](https://www.cve.org/CVERecord?id=CVE-2025-30023) | 9.0 (Critical) | 5.32 | [Axis Security Advisory](https://www.axis.com/dam/public/9b/a5/72/cve-2025-30023pdf-en-US-485733.pdf) - This vulnerability could lead to an authenticated user performing a remote code execution attack. | 

#### CVE 2021

| CVE number | CVSS severity | Released version | Security advisory / Vulnerability summary | 
| [CVE-2021-31989](https://www.cve.org/CVERecord?id=CVE-2021-31989) | 5.3 (Medium) | 5.17 | [Axis Security Advisory](https://www.axis.com/files/tech_notes/CVE-2021-31989.pdf) - A user with permission to log on to the machine hosting the AXIS Device Manager client could under certain conditions extract a memory dump from the built-in Windows Task Manager application. The memory dump may potentially contain credentials of connected Axis devices. | 

### AXIS OS

#### CVE 2026

| CVE number | CVSS severity | Patched version | Security advisory / Vulnerability summary | 
| [CVE-2026-84751](https://www.cve.org/CVERecord?id=CVE-2026-84751) | 8.2 (High) | 13.0.59 12.11.137 11.11.x 10.12.x 9.80.x 8.40.x 6.50.5.x | This CVE will be externally disclosed on 9 February 2027, more detailed information will follow then. | 
| [CVE-2026-84735](https://www.cve.org/CVERecord?id=CVE-2026-84735) | 8.2 (High) | 13.1.34 12.11.139 11.11.235 10.12.358 | This CVE will be externally disclosed on 9 February 2027, more detailed information will follow then. | 
| [CVE-2026-81710](https://www.cve.org/CVERecord?id=CVE-2026-81710) | 5.3 (Medium) | 13.0.92 12.11.147 11.11.238 10.12.361 9.80.160 8.40.118 6.50.5.23 | This CVE will be externally disclosed on 9 February 2027, more detailed information will follow then. | 
| [CVE-2026-81709](https://www.cve.org/CVERecord?id=CVE-2026-81709) | 7.5 (High) | 13.0.92 12.11.137 11.11.x 10.12.x 9.80.x 8.40.x 6.50.5.x | This CVE will be externally disclosed on 9 February 2027, more detailed information will follow then. | 
| [CVE-2026-63290](https://www.cve.org/CVERecord?id=CVE-2026-63290) | 6.8 (Medium) | 13.0.x 12.11.x | This CVE will be externally disclosed on 9 February 2027, more detailed information will follow then. | 
| [CVE-2026-63288](https://www.cve.org/CVERecord?id=CVE-2026-63288) | 8.3 (High) | AXIS OS Secure Entry 12.11.106.1 | [Axis Security Advisory](https://www.axis.com/dam/public/fa/79/f5/cve-2026-63288pdf-en-US-561260.pdf) - A WebSocket request sent to a specific API endpoint allows unauthorized access to a separate API endpoint. This bypasses the intended authentication layer. | 
| [CVE-2026-63285](https://www.cve.org/CVERecord?id=CVE-2026-63285) | 6.4 (Medium) | 13.0.x 12.11.x | This CVE will be externally disclosed on 9 February 2027, more detailed information will follow then. | 
| [CVE-2026-63282](https://www.cve.org/CVERecord?id=CVE-2026-63282) | 6.5 (Medium) | 13.0.84 12.11.123 11.11.231 10.12.354 9.80.153 8.40.112 6.50.5.23 | [Axis Security Advisory](https://www.axis.com/dam/public/c5/06/79/cve-2026-63282pdf-en-US-561259.pdf) - Improper shell quote escaping when processing user-controlled input, potentially allowing command injection, which could lead to privilege escalation. | 
| [CVE-2026-14543](https://www.cve.org/CVERecord?id=CVE-2026-14543) | 3.9 (Low) | 13.0.42 12.11.84 11.11.224 10.12.348 | [Axis Security Advisory](https://www.axis.com/dam/public/cd/92/6b/cve-2026-14543pdf-en-US-561257.pdf) - The VAPIX Edge storage API, enabled the escalation of user privileges by circumventing filesystem isolation, granting unauthorized access to protected system resources. | 
| [CVE-2026-14542](https://www.cve.org/CVERecord?id=CVE-2026-14542) | 6.5 (Medium) | 13.0.83 12.11.123 11.11.228 10.12.352 | [Axis Security Advisory](https://www.axis.com/dam/public/12/1f/f8/cve-2026-14542pdf-en-US-561256.pdf) - The VAPIX SIP configuration API lacked sufficient input validation, which could potentially lead to privilege escalation. | 
| [CVE-2026-14174](https://www.cve.org/CVERecord?id=CVE-2026-14174) | 6.7 (Medium) | 13.0.x 12.11.x 11.11.x 10.12.x 9.80.x 8.40.x 6.50.x | This CVE will be externally disclosed on 9 February 2027, more detailed information will follow then. | 
| [CVE-2026-13409](https://www.cve.org/CVERecord?id=CVE-2026-13409) | 4.3 (Medium) | 13.0.31 12.11.84 11.11.218 10.12.345 9.80.148 | [Axis Security Advisory](https://www.axis.com/dam/public/ef/b3/81/cve-2026-13409pdf-en-US-561255.pdf) - The VAPIX API dynamicoverlay.cgi contained a flaw that results in a Denial-of-Service of the overlay functionality. | 
| [CVE-2026-9063](https://www.cve.org/CVERecord?id=CVE-2026-9063) | 6.7 (Medium) | 13.0.14 12.11.80 | [Axis Security Advisory](https://www.axis.com/dam/public/37/e2/7c/cve-2026-9063pdf-en-US-561254.pdf) - A locally authenticated user can achieve privilege escalation via an insecure configuration that leads to unauthorized code execution. | 
| [CVE-2026-6505](https://www.cve.org/CVERecord?id=CVE-2026-6505) | 5.1 (Medium) | 12.11.43 | [Axis Security Advisory](https://www.axis.com/dam/public/fd/16/ab/cve-2026-6505pdf-en-US-543641.pdf) - The ACAP framework contains a Time-of-Check to Time-of-Use (TOCTOU) race condition, which could potentially lead to privilege escalation. | 
| [CVE-2026-6181](https://www.cve.org/CVERecord?id=CVE-2026-6181) | 5.9 (Medium) | 12.11.13 11.11.207 | [Axis Security Advisory](https://www.axis.com/dam/public/9d/8a/ea/cve-2026-6181pdf-en-US-543646.pdf)- The Device Configuration Framework is vulnerable to an authentication bypass flaw. | 
| [CVE-2026-5304](https://www.cve.org/CVERecord?id=CVE-2026-5304) | 5.7 (Medium) | 12.11.12 | [Axis Security Advisory](https://www.axis.com/dam/public/21/37/f2/cve-2026-5304pdf-en-US-543644.pdf) - An ACAP configuration file lacks input validation, which could potentially lead to privilege escalation. | 
| [CVE-2026-5303](https://www.cve.org/CVERecord?id=CVE-2026-5303) | 5.7 (Medium) | 12.11.31 | [Axis Security Advisory](https://www.axis.com/dam/public/d5/e8/6e/cve-2026-5303pdf-en-US-543643.pdf) - The ACAP framework contains a Time-of-Check to Time-of-Use (TOCTOU) race condition, which could potentially lead to privilege escalation. | 
| [CVE-2026-4757](https://www.cve.org/CVERecord?id=CVE-2026-4757) | 7.2 (High) | 12.11.44 | [Axis Security Advisory](https://www.axis.com/dam/public/41/7d/0f/cve-2026-4757pdf-en-US-543642.pdf) - A VAPIX API parameter had improper input validation which could allow code execution and potentially lead to a privilege escalation. | 
| [CVE-2026-1185](https://www.cve.org/CVERecord?id=CVE-2026-1185) | 5.4 (Medium) | 12.10.37 | [Axis Security Advisory](https://www.axis.com/dam/public/69/df/8d/cve-2026-1185pdf-en-US-530733.pdf) - A configuration file on the local file system had improper input validation which could allow code execution and potentially lead to privilege escalation. | 
| [CVE-2026-0804](https://www.cve.org/CVERecord?id=CVE-2026-0804) | 6.7 (Medium) | 12.10.4 | [Axis Security Advisory](https://www.axis.com/dam/public/51/64/ea/cve-2026-0804pdf-en-US-530732.pdf) - An ACAP configuration file lacked sufficient input validation, which could allow a path traversal attack leading to potential privilege escalation. | 
| [CVE-2026-0802](https://www.cve.org/CVERecord?id=CVE-2026-0802) | 6.0 (Medium) | 12.9.33 | [Axis Security Advisory](https://www.axis.com/dam/public/67/b8/75/cve-2026-0802pdf-en-US-530731.pdf) - An ACAP configuration file lacked sufficient input validation, which could allow command injection and potentially lead to privilege escalation. | 
| [CVE-2026-0541](https://www.cve.org/CVERecord?id=CVE-2026-0541) | 6.7 (Medium) | 12.9.32 | [Axis Security Advisory](https://www.axis.com/dam/public/fa/50/c7/cve-2026-0541pdf-en-US-530730.pdf) - ACAP applications can gain elevated privileges due to improper input validation during the installation process, potentially leading to privilege escalation. | 


#### CVE 2025

| CVE number | CVSS severity | Patched version | Security advisory / Vulnerability summary | 
| [CVE-2025-30027](https://www.cve.org/CVERecord?id=CVE-2025-30027) | 6.7 (Medium) | 12.5.36 | [Axis Security Advisory](https://www.axis.com/dam/public/ab/9a/a5/cve-2025-30027pdf-en-US-492762.pdf) - An ACAP configuration file lacked sufficient input validation, which could allow for arbitrary code execution. | 
| [CVE-2025-11142](https://www.cve.org/CVERecord?id=CVE-2025-11142) | 7.1 (High) | 12.7.53 | [Axis Security Advisory](https://www.axis.com/dam/public/18/0e/90/cve-2025-11142pdf-en-US-519291.pdf) - The VAPIX API mediaclip.cgi did not have a sufficient input validation allowing for a possible remote code execution. | 
| [CVE-2025-9524](https://www.cve.org/CVERecord?id=CVE-2025-9524) | 4.3 (Medium) | 12.7.11 11.11.177 10.12.305 9.80.123 8.40.89 6.50.5.21 | [Axis Security Advisory](https://www.axis.com/dam/public/f1/f0/1e/cve-2025-9524pdf-en-US-504220.pdf) - The VAPIX API port.cgi did not have sufficient input validation, which may result in process crashes and impact usability. | 
| [CVE-2025-9055](https://www.cve.org/CVERecord?id=CVE-2025-9055) | 6.4 (Medium) | 12.7.53 | [Axis Security Advisory](https://www.axis.com/dam/public/23/a3/00/cve-2025-9055pdf-en-US-504219.pdf) - The VAPIX Edge storage API allowed a privilege escalation, enabling a VAPIX administrator-privileged user to gain Linux Root privileges. | 
| [CVE-2025-8998](https://www.cve.org/CVERecord?id=CVE-2025-8998) | 3.1 (Low) | 12.7.27 11.11.178 10.12.306 9.80.124 8.40.90 6.50.5.22 | [Axis Security Advisory](https://www.axis.com/dam/public/f5/62/80/cve-2025-8998pdf-en-US-504374.pdf) - It was possible to upload files with a specific name to a temporary directory, which may result in process crashes and impact usability. | 
| [CVE-2025-8108](https://www.cve.org/CVERecord?id=CVE-2025-8108) | 6.7 (Medium) | 12.7.33 | [Axis Security Advisory](https://www.axis.com/dam/public/38/20/aa/cve-2025-8108pdf-en-US-504218.pdf) - An ACAP configuration file had improper permissions and lacked input validation, which could potentially lead to privilege escalation. | 
| [CVE-2025-6779](https://www.cve.org/CVERecord?id=CVE-2025-6779) | 6.7 (Medium) | 12.6.40 | [Axis Security Advisory](https://www.axis.com/dam/public/92/9a/13/cve-2025-6779pdf-en-US-504217.pdf) - An ACAP configuration file had improper permissions, which could allow command injection and potentially lead to privilege escalation. | 
| [CVE-2025-6571](https://www.cve.org/CVERecord?id=CVE-2025-6571) | 6.0 (Medium) | 12.6.66 11.11.169 | [Axis Security Advisory](https://www.axis.com/dam/public/1f/f8/f0/cve-2025-6571pdf-en-US-504216.pdf) - A third-party component exposed its password in process arguments, allowing for low-privileged users to access it. | 
| [CVE-2025-6298](https://www.cve.org/CVERecord?id=CVE-2025-6298) | 6.7 (Medium) | 12.6.28 | [Axis Security Advisory](https://www.axis.com/dam/public/ef/91/c3/cve-2025-6298pdf-en-US-504215.pdf) - ACAP applications can gain elevated privileges due to improper input validation, potentially leading to privilege escalation. | 
| [CVE-2025-5718](https://www.cve.org/CVERecord?id=CVE-2025-5718) | 6.8 (Medium) | 12.6.30 | [Axis Security Advisory](https://www.axis.com/dam/public/3c/a4/6a/cve-2025-5718pdf-en-US-504214.pdf) - The ACAP Application framework allowed a privilege escalation through a symlink attack. | 
| [CVE-2025-5454](https://www.cve.org/CVERecord?id=CVE-2025-5454) | 6.4 (Medium) | 12.6.18 | [Axis Security Advisory](https://www.axis.com/dam/public/48/ab/82/cve-2025-5454pdf-en-US-504213.pdf) - An ACAP configuration file lacked sufficient input validation, which could allow a path traversal attack leading to potential privilege escalation. | 
| [CVE-2025-5452](https://www.cve.org/CVERecord?id=CVE-2025-5452) | 6.6 (Medium) | 12.6.69 | [Axis Security Advisory](https://www.axis.com/dam/public/39/ba/8b/cve-2025-5452pdf-en-US-504212.pdf) - A malicious ACAP application can gain access to admin-level service account credentials used by legitimate ACAP applications, leading to a potential privilege escalation of the malicious ACAP application. | 
| [CVE-2025-4645](https://www.cve.org/CVERecord?id=CVE-2025-4645) | 6.7 (Medium) | 12.6.7 | [Axis Security Advisory](https://www.axis.com/dam/public/69/47/ff/cve-2025-4645pdf-en-US-504211.pdf) - An ACAP configuration file lacked sufficient input validation, which could allow for arbitrary code execution. | 
| [CVE-2025-3892](https://www.cve.org/CVERecord?id=CVE-2025-3892) | 6.7 (Medium) | 12.5.31 | [Axis Security Advisory](https://www.axis.com/dam/public/ae/19/16/cve-2025-3892pdf-en-US-492760.pdf) - It was possible for ACAP applications to be executed with elevated privileges, potentially leading to privilege escalation. | 
| [CVE-2025-0361](https://www.cve.org/CVERecord?id=CVE-2025-0361) | 4.3 (Medium) | 12.3.56 11.11.141 | [Axis Security Advisory](https://www.axis.com/dam/public/f4/9b/13/cve-2025-0361pdf-en-US-474511.pdf) - The VAPIX Device Configuration framework allowed for unauthenticated username enumeration through the VAPIX Device Configuration SSH Management API. | 
| [CVE-2025-0360](https://www.cve.org/CVERecord?id=CVE-2025-0360) | 7.8 (High) | 12.2.41 11.11.135 | [Axis Security Advisory](https://www.axis.com/dam/public/b1/fe/46/cve-2025-0360pdf-en-US-466887.pdf) - The VAPIX Device Configuration framework was vulnerable to a flaw that could lead to an incorrect user privilege level in the VAPIX service account D-Bus API. | 
| [CVE-2025-0359](https://www.cve.org/CVERecord?id=CVE-2025-0359) | 8.5 (High) | 12.2.52 11.11.135 | [Axis Security Advisory](https://www.axis.com/dam/public/68/08/c5/cve-2025-0359pdf-en-US-466885.pdf) - The ACAP Application framework allowed applications to access restricted D-Bus methods within the framework. | 
| [CVE-2025-0358](https://www.cve.org/CVERecord?id=CVE-2025-0358) | 8.8 (High) | 12.4.0 | [Axis Security Advisory](https://www.axis.com/dam/public/35/90/85/cve-2025-0358pdf-en-US-483809.pdf) - The VAPIX Device Configuration framework allowed a privilege escalation, enabling a lower-privileged user to gain administrator privileges. | 
| [CVE-2025-0325](https://www.cve.org/CVERecord?id=CVE-2025-0325) | 4.3 (Medium) | 12.4.28 11.11.142 10.12.278 9.80.100 8.40.74 6.50.5.21 | [Axis Security Advisory](https://www.axis.com/dam/public/d0/ae/fe/cve-2025-0325pdf-en-US-483808.pdf) - A Guard Tour VAPIX API parameter allowed the use of arbitrary values and can be incorrectly called, allowing an attacker to block access to the guard tour configuration page in the web interface of the Axis device. | 
| [CVE-2025-0324](https://www.cve.org/CVERecord?id=CVE-2025-0324) | 9.4 (Critical) | 12.3.33 11.11.140 | [Axis Security Advisory](https://www.axis.com/dam/public/04/f3/1c/cve-2025-0324pdf-en-US-483807.pdf) - The VAPIX Device Configuration framework allowed a privilege escalation, enabling a lower-privileged user to gain administrator privileges. | 

#### CVE 2024

| CVE number | CVSS severity | Released version | Security advisory / Vulnerability summary | 
| [CVE-2024-47262](https://www.cve.org/CVERecord?id=CVE-2024-47262) | 5.3 (Medium) | 12.3.4 11.11.127 10.12.270 9.80.90 8.40.66 6.50.5.19 | [Axis Security Advisory](https://www.axis.com/dam/public/a3/18/6e/cve-2024-47262pdf-en-US-466884.pdf) - The VAPIX API param.cgi was vulnerable to a race condition attack allowing for an attacker to block access to the web interface of the Axis device. Other API endpoints or services not making use of param.cgi are not affected. | 
| [CVE-2024-47261](https://www.cve.org/CVERecord?id=CVE-2024-47261) | 4.3 (Medium) | 12.3.56 11.11.141 10.12.276 | [Axis Security Advisory](https://www.axis.com/dam/public/18/c5/b2/cve-2024-47261pdf-en-US-474505.pdf) - The VAPIX API uploadoverlayimage.cgi did not have sufficient input validation to allow an attacker to upload files to block access to create image overlays in the web interface of the Axis device. | 
| [CVE-2024-47260](https://www.cve.org/CVERecord?id=CVE-2024-47260) | 6.5 (Medium) | 12.3.1 11.11.135 10.12.270 9.80.89 | [Axis Security Advisory](https://www.axis.com/dam/public/1d/d3/ef/cve-2024-47260pdf-en-US-466883.pdf) - The VAPIX API mediaclip.cgi did not have a sufficient input validation allowing for uploading more audio clips then designed resulting in the Axis device running out of memory. | 
| [CVE-2024-47259](https://www.cve.org/CVERecord?id=CVE-2024-47259) | 3.5 (Low) | 12.2.52 11.11.126 | [Axis Security Advisory](https://www.axis.com/dam/public/13/cd/4a/cve-2024-47259pdf-en-US-466882.pdf) - The VAPIX API dynamicoverlay.cgi did not have a sufficient input validation allowing for a possible command injection leading to being able to transfer files to the Axis device with the purpose to exhaust system resources. | 
| [CVE-2024-47257](https://www.cve.org/CVERecord?id=CVE-2024-47257) | 7.5 (High) | 6.50.5.19 | [Axis Security Advisory](https://www.axis.com/dam/public/b7/76/b2/cve-2024-47257pdf-en-US-458044.pdf) - Selected Axis devices were vulnerable to handling certain ethernet frames which could lead to the Axis device becoming unavailable in the network. | 
| [CVE-2024-8772](https://www.cve.org/CVERecord?id=CVE-2024-8772) | 4.3 (Medium) | 12.1.28 11.11.118 10.12.259 9.80.84 | [Axis Security Advisory](https://www.axis.com/dam/public/permalink/231072/cve-2024-8772pdf-en-US_InternalID-231072.pdf) - The VAPIX API managedoverlayimages.cgi was vulnerable to a race condition attack allowing for an attacker to block access to the overlay configuration page in the web interface of the Axis device. | 
| [CVE-2024-8160](https://www.cve.org/CVERecord?id=CVE-2024-8160) | 3.8 (Low) | 12.1.21 11.11.116 10.12.257 | [Axis Security Advisory](https://www.axis.com/dam/public/permalink/231071/cve-2024-8160pdf-en-US_InternalID-231071.pdf) - The VAPIX API ftptest.cgi did not have a sufficient input validation allowing for a possible command injection leading to being able to transfer files from/to the Axis device. | 
| [CVE-2024-7784](https://www.cve.org/CVERecord?id=CVE-2024-7784) | 6.1 (Medium) | 12.0.47 11.11.85 10.12.247 | [Axis Security Advisory](https://www.axis.com/dam/public/ba/5f/4e/cve-2024-7784-en-US-448998.pdf) - Device tampering (commonly known as Secure Boot) in AXIS OS was vulnerable to a sophisticated attack to bypass this protection. This patch will enforce a downgrade restriction. For more information please review the security advisory. | 
| [CVE-2024-6979](https://www.cve.org/CVERecord?id=CVE-2024-6979) | 6.8 (Medium) | 11.11.94 | [Axis Security Advisory](https://www.axis.com/dam/public/c3/44/5b/cve-2024-6979-en-US-448997.pdf) - A broken access control was discovered which could lead to less-privileged operator- and/or viewer accounts having more privileges than designed. | 
| [CVE-2024-6509](https://www.cve.org/CVERecord?id=CVE-2024-6509) | 6.5 (Medium) | 11.11.93 10.12.249 9.80.78 8.40.59 6.50.5.19 | [Axis Security Advisory](https://www.axis.com/dam/public/f6/c6/f5/cve-2024-6509-en-US-458043.pdf) - The VAPIX API alwaysmulti.cgi was vulnerable for file globbing which could lead to resource exhaustion of the Axis device. | 
| [CVE-2024-6173](https://www.cve.org/CVERecord?id=CVE-2024-6173) | 6.5 (Medium) | 11.11.73 10.12.249 9.80.78 8.40.59 6.50.5.19 | [Axis Security Advisory](https://www.axis.com/dam/public/5a/87/a2/cve-2024-6173-en-US-458042.pdf) - A Guard Tour VAPIX API parameter allowed the use of arbitrary values allowing for an attacker to block access to the guard tour configuration page in the web interface of the Axis device. | 
| [CVE-2024-0067](https://www.cve.org/CVERecord?id=CVE-2024-0067) | 4.3 (Medium) | 11.11.73 10.12.249 9.80.78 8.40.59 | [Axis Security Advisory](https://www.axis.com/dam/public/c7/d0/91/cve-2024-0067-en-US-448994.pdf) - The VAPIX API ledlimit.cgi was vulnerable for path traversal attacks allowing to list folder/file names on the local file system of the Axis device. | 
| [CVE-2024-0066](https://www.cve.org/CVERecord?id=CVE-2024-0066) | 5.3 (Medium) | 11.10.61 10.12.236 9.80.69 8.40.48 6.50.5.18 5.51.7.8 | [Axis Security Advisory](https://www.axis.com/dam/public/03/49/2c/cve-2024-0066-en-US-442553.pdf) - A O3C feature may expose sensitive traffic between the client (Axis device) and (O3C) server. If O3C is not being used this flaw does not apply. | 
| [CVE-2024-0055](https://www.cve.org/CVERecord?id=CVE-2024-0055) | 6.5 (Medium) | 11.9.53 10.12.228 | [Axis Security Advisory](https://www.axis.com/dam/public/c4/00/c5/cve-2024-0055-en-US-432117.pdf) - The VAPIX APIs mediaclip.cgi and playclip.cgi was vulnerable for file globbing which could lead to a resource exhaustion attack. | 
| [CVE-2024-0054](https://www.cve.org/CVERecord?id=CVE-2024-0054) | 6.5 (Medium) | 11.9.53 10.12.228 9.80.58 8.40.43 6.50.5.17 | [Axis Security Advisory](https://www.axis.com/dam/public/76/f3/1d/cve-2024-0054-en-US-432116.pdf) -  The VAPIX APIs local\_list.cgi, create\_overlay.cgi and irissetup.cgi was vulnerable for file globbing which could lead to a resource exhaustion attack. | 

#### CVE 2023

| CVE number | CVSS severity | Released version | Security advisory / Vulnerability summary | 
| [CVE-2023-22984](https://www.cve.org/CVERecord?id=CVE-2023-22984) | 6.1 (Medium) | N/A | This CVE has been rejected as it is out-of-scope in accordance with our vulnerability management policy. Please follow our general [Security Advisory about CSRF and XSS attacks](https://www.axis.com/dam/public/ed/4f/ad/advisory-cross-site-request-forgery-en-US-358977.pdf) on how to mitigate these type of vulnerabilities. | 
| [CVE-2023-21418](https://www.cve.org/CVERecord?id=CVE-2023-21418) | 7.1 (High) | 11.7.57 10.12.213 9.80.49 8.40.37 6.50.5.15 | [Axis Security Advisory](https://www.axis.com/dam/public/49/93/55/cve-2023-21418-en-US-417792.pdf) - The VAPIX API irissetup.cgi was vulnerable to path traversal attacks that allows for file deletion. | 
| [CVE-2023-21417](https://www.cve.org/CVERecord?id=CVE-2023-21417) | 7.1 (High) | 11.7.57 10.12.208 9.80.49 | [Axis Security Advisory](https://www.axis.com/dam/public/2a/82/12/cve-2023-21417-en-US-417791.pdf) - The VAPIX API manageoverlayimage.cgi was vulnerable to path traversal attacks that allows for file/folder deletion. | 
| [CVE-2023-21416](https://www.cve.org/CVERecord?id=CVE-2023-21416) | 7.1 (High) | 11.7.57 10.12.213 | [Axis Security Advisory](https://www.axis.com/dam/public/35/2a/a6/cve-2023-21416-en-US-417790.pdf) - The VAPIX API dynamicoverlay.cgi was vulnerable to a Denial-of-Service attack allowing for an attacker to block access to the overlay configuration page in the web interface of the Axis device. | 
| [CVE-2023-21415](https://www.cve.org/CVERecord?id=CVE-2023-21415) | 6.5 (Medium) | 11.6.94 10.12.208 9.80.47 8.40.35 6.50.5.14 | [Axis Security Advisory](https://www.axis.com/dam/public/b6/55/e2/cve-2023-21415pdf-en-US-416245.pdf) - The VAPIX API overlay\_del.cgi was vulnerable to path traversal attacks that allows for file deletion. | 
| [CVE-2023-21414](https://www.cve.org/CVERecord?id=CVE-2023-21414) | 7.1 (High) | 11.6.94 10.12.208 | [Axis Security Advisory](https://www.axis.com/dam/public/45/3c/a1/cve-2023-21414pdf-en-US-412758.pdf) - Device tampering (commonly known as Secure Boot) in AXIS OS was vulnerable to a sophisticated attack to bypass this protection. This patch will enforce a downgrade restriction. For more information please review the secure advisory. | 
| [CVE-2023-21413](https://www.cve.org/CVERecord?id=CVE-2023-21413) | 9.1 (Critical) | 11.6.94 10.12.199 | [Axis Security Advisory](https://www.axis.com/dam/public/ad/ff/83/cve-2023-21413pdf-en-US-412755.pdf) - The application handling service in AXIS OS was vulnerable to command injection allowing an attacker to run arbitrary code. | 
| [CVE-2023-21406](https://www.cve.org/CVERecord?id=CVE-2023-21406) | 7.1 (High) | 1.65.5 | [Axis Security Advisory](https://www.axis.com/dam/public/1b/21/5f/cve-2023-21406-en-US-407245.pdf) - A heap-based buffer overflow was found in the pacsiod process which is handling the OSDP communication allowing to write outside of the allocated buffer. By appending invalid data to an OSDP message it was possible to write data beyond the heap allocated buffer. The data written outside the buffer could be used to execute arbitrary code. | 
| [CVE-2023-21405](https://www.cve.org/CVERecord?id=CVE-2023-21405) | 6.5 (Medium) | 11.7.12.2 11.5.54 10.12.200.1 10.12.182 1.65.5 | [Axis Security Advisory](https://www.axis.com/dam/public/7f/3a/ed/cve-2023-21405-en-US-407244.pdf) - When communicating over OSDP, a flaw was found that the OSDP message parser crashes the pacsiod process, causing a temporary unavailability of the door-controlling functionalities meaning that doors cannot be opened or closed. | 
| [CVE-2023-21404](https://www.cve.org/CVERecord?id=CVE-2023-21404) | 4.1 (Medium) | 11.4.52 | [Axis Security Advisory](https://www.axis.com/dam/public/07/0a/20/cve-2023-21404-en-US-398426.pdf) - A static RSA key was used to encrypt Axis-specific source code in legacy LUA-components. The encryption was applied to avoid non sensitive Axis- specific code from being easily human readable. | 
| [CVE-2023-5800](https://www.cve.org/CVERecord?id=CVE-2023-5800) | 5.4 (Medium) | 11.8.61 10.12.221 9.80.55 8.40.43 6.50.5.16 | [Axis Security Advisory](https://www.axis.com/dam/public/89/d9/99/cve-2023-5800-en-US-424339.pdf) - The VAPIX API create\_overlay.cgi did not have a sufficient input validation allowing for a possible remote code execution. | 
| [CVE-2023-5677](https://www.cve.org/CVERecord?id=CVE-2023-5677) | 6.3 (Medium) | 5.51.7.7 6.50.5.21 | [Axis Security Advisory](https://www.axis.com/dam/public/0a/47/d1/cve-2023-5677-en-US-483444.pdf) - The VAPIX API tcptest.cgi did not have a sufficient input validation allowing for a possible remote code execution. | 
| [CVE-2023-5553](https://www.cve.org/CVERecord?id=CVE-2023-5553) | 7.6 (High) | 11.7.57 10.12.213 | [Axis Security Advisory](https://www.axis.com/dam/public/0a/66/25/cve-2023-5553-en-US-417789.pdf) - Device tampering (commonly known as Secure Boot) in AXIS OS was vulnerable to a sophisticated attack to bypass this protection. This patch will enforce a downgrade restriction. For more information please review the secure advisory. | 

#### CVE 2021-2000

#### ACV

| CVE number | Patched | Security advisory / Vulnerability summary | 
| [ACV-2020-100004](https://www.axis.com/files/tech_notes/ACV-2020-100004.pdf) | Yes | [Axis Security Advisory](https://www.axis.com/files/tech_notes/ACV-2020-100004.pdf) | 
| [ACV-165813](https://www.axis.com/files/faq/Advisory_ACV-165813_Secure_boot.pdf) | Yes | [Axis Security Advisory](https://www.axis.com/files/faq/Advisory_ACV-165813_Secure_boot.pdf) | 
| [ACV-147453](https://www.axis.com/files/sales/Advisory_ACV-147453_A1001.pdf) | Yes | [Axis Security Advisory](https://www.axis.com/files/sales/Advisory_ACV-147453_A1001.pdf) | 
| [ACV-128401](https://www.axis.com/files/faq/Advisory_ACV-128401.pdf) | Yes | [Axis Security Advisory](https://www.axis.com/files/faq/Advisory_ACV-128401.pdf) | 
| [ACV-120444](https://www.axis.com/files/faq/Advisory_ACV-120444.pdf) | Yes | [Axis Security Advisory](https://www.axis.com/files/faq/Advisory_ACV-120444.pdf) | 
| [ACV-116267](<https://www.axis.com/files/faq/ACV116267_(CVE-2017-9765).pdf>) | Yes | [Axis Security Advisory](<https://www.axis.com/files/faq/ACV116267_(CVE-2017-9765).pdf>) | 

### Miscellaneous

#### CVE 2026

| CVE number | CVSS severity | Released version | Security advisory / Vulnerability summary | 
| [CVE-2026-14918](https://www.cve.org/CVERecord?id=CVE-2026-14918) | 5.3 (Medium) | Signed-Video-Framework 2.3.7 Signed media verifier 1.0.3 Axis File Player 3.1.10.0 | [Axis Security Advisory](https://www.axis.com/dam/public/3b/4f/06/cve-2026-14918pdf-en-US-561258.pdf) - The Signed Video Framework contained a out-of-bounds read issue in the Signed Video Framework which could lead the application using this framework to crash. The issue exclusively affects the tools used for the validation of signed content. The AXIS OS device's signed video functionality remains unaffected. | 
| [CVE-2026-8158](https://www.cve.org/CVERecord?id=CVE-2026-8158) | 5.3 (Medium) | Signed-Video-Framework 2.3.5 Signed media verifier 1.0.2 Axis File Player 3.1.9.0 | [Axis Security Advisory](https://www.axis.com/dam/public/6c/f3/ac/cve-2026-8158pdf-en-US-543645.pdf) - The Signed Video Framework contained a  buffer overflow issue which could lead the application using this framework to crash. The issue exclusively affects the tools used for the validation of signed content. The AXIS OS device's signed video functionality remains unaffected. | 

#### CVE 2025

| CVE number | CVSS severity | Released version | Security advisory / Vulnerability summary | 
| [CVE-2025-10714](https://www.cve.org/CVERecord?id=CVE-2025-10714) | 8.4 (High) | 5.6.0.0 | [Axis Security Advisory](https://www.axis.com/dam/public/a2/c7/8c/cve-2025-10714pdf-en-US-504221.pdf) - AXIS Optimizer was vulnerable to an unquoted search path vulnerability, which could potentially lead to privilege escalation within Microsoft Windows operating system. | 

#### CVE 2022

| CVE number | CVSS severity | Released version | Security advisory / Vulnerability summary | 
| [CVE-2022-23410](https://www.cve.org/CVERecord?id=CVE-2022-23410) | 7.8 (High) | 4.18.0 | [Axis Security Advisory](https://www.axis.com/files/tech_notes/CVE-2022-23410.pdf) - AXIS IP Utility allowed for remote code execution and local privilege escalation by the means of DLL hijacking. | 

## OpenSource CVEs

The OpenSource registry covers potential threats caused by 3rd party vulnerabilities of OpenSource components that are used in Axis products.

Severity rating

Since 2024, we have started adding the severity level to the table below. Note that it is only added for new CVE's.

Please note that the severity ratings provided for each CVE are based on calculations and assessments made by the respective open source providers. These ratings are not specific to Axis devices and do not necessarily reflect the severity of these vulnerabilities in the context of Axis products. The severity ratings provided here are intended to give a general indication of the potential impact as determined by the broader security community. If a CVSS rating is unavailable at [www.cve.org](https://www.cve.org/), we refer to the [National Vulnerability Database (NVD)](https://nvd.nist.gov/vuln/search) for the necessary information when available.

### AXIS Audio Manager

#### CVE 2026

| CVE number | CVSS severity | Affected | Security advisory / Vulnerability summary | 
| [CVE-2026-109619](https://www.cve.org/CVERecord?id=CVE-2026-109619) | (9.2) Critical | No | The AXIS Audio Manager family does not use the affected versions/components | 
| [CVE-2026-109618](https://www.cve.org/CVERecord?id=CVE-2026-109618) | (9.2) Critical | No | The AXIS Audio Manager family does not use the affected versions/components | 

### AXIS Camera Station

#### CVE 2026

| CVE number | CVSS severity | Affected | Security advisory / Vulnerability summary | 
| [CVE-2026-109619](https://www.cve.org/CVERecord?id=CVE-2026-109619) | (9.2) Critical | No | The AXIS Camera Station family does not use the affected versions/components | 
| [CVE-2026-109618](https://www.cve.org/CVERecord?id=CVE-2026-109618) | (9.2) Critical | No | The AXIS Camera Station family does not use the affected versions/components | 

### AXIS OS

#### CVE 2026

| CVE number | CVSS severity | Affected | Security advisory / Vulnerability summary | 
| [CVE-2026-123158](https://www.cve.org/CVERecord?id=CVE-2026-123158) | 8.1 (High) | No | AXIS OS devices do not use the affected versions/components. | 
| [CVE-2026-119618](https://www.cve.org/CVERecord?id=CVE-2026-119618) | 9.8 (Critical) | Yes | [Axis Security Advisory](https://www.axis.com/dam/public/permalink/294609/cve-2026-119618pdf-en-US_294609.pdf) - The vulnerability is patched by upgrading to Apache version 2.4.71. For an immediate workaround follow the mitigation steps in the security advisory. | 
| [CVE-2026-109619](https://www.cve.org/CVERecord?id=CVE-2026-109619) | 9.2 (Critical) | No | AXIS OS devices do not use the affected versions/components. | 
| [CVE-2026-109618](https://www.cve.org/CVERecord?id=CVE-2026-109618) | 9.2 (Critical) | No | AXIS OS devices do not use the affected versions/components. | 
| [CVE-2026-109163](https://www.cve.org/CVERecord?id=CVE-2026-109163) | Low | No | AXIS OS devices do not use the affected versions/components. | 
| [CVE-2026-106023](https://www.cve.org/CVERecord?id=CVE-2026-106023) | High | No | AXIS OS devices do not use the affected versions/components. | 
| [CVE-2026-98432](https://www.cve.org/CVERecord?id=CVE-2026-98432) | 9.8 (Critical) | Yes | While AXIS OS devices may use a vulnerable version, the vulnerability cannot be exploited remotely. To trigger it locally, an attacker would need to be authenticated and have elevated privileges on the Axis device. We will provide patches for the Linux Kernel LTS versions that are affected in a timely manner. | 
| [CVE-2026-49975](https://www.cve.org/CVERecord?id=CVE-2026-49975) | Medium | Yes | The vulnerability is patched by upgrading to Apache version 2.4.68. | 
| [CVE-2026-48913](https://www.cve.org/CVERecord?id=CVE-2026-48913) | Low | Yes | The vulnerability is patched by upgrading to Apache version 2.4.68. | 
| [CVE-2026-45447](https://www.cve.org/CVERecord?id=CVE-2026-45447) | High | Partly | Only affects AXIS OS 12.9 and higher. | 
| [CVE-2026-44631](https://www.cve.org/CVERecord?id=CVE-2026-44631) | Low | No | AXIS OS devices do not use the vulnerable functionality. | 
| [CVE-2026-44186](https://www.cve.org/CVERecord?id=CVE-2026-44186) | Medium | No | AXIS OS devices do not use the `mod_proxy_ftp` module. | 
| [CVE-2026-44185](https://www.cve.org/CVERecord?id=CVE-2026-44185) | Low | Yes | The vulnerability is patched by upgrading to Apache version 2.4.68. | 
| [CVE-2026-44119](https://www.cve.org/CVERecord?id=CVE-2026-44119) | Medium | No | AXIS OS devices do not use the vulnerable functionality. | 
| [CVE-2026-43951](https://www.cve.org/CVERecord?id=CVE-2026-43951) | Medium | Yes | The vulnerability is patched by upgrading to Apache version 2.4.68. | 
| [CVE-2026-43500](https://www.cve.org/CVERecord?id=CVE-2026-43500) | 8.8 (High) | No | AXIS OS devices do not have the affected function enabled. | 
| [CVE-2026-43284](https://www.cve.org/CVERecord?id=CVE-2026-43284) | 8.8 (High) | No | AXIS OS devices do not have the affected function enabled. | 
| [CVE-2026-42536](https://www.cve.org/CVERecord?id=CVE-2026-42536) | Low | No | AXIS OS devices do not use the `mod_xml2enc` module. | 
| [CVE-2026-42535](https://www.cve.org/CVERecord?id=CVE-2026-42535) | Medium | No | AXIS OS devices do not use the `mod_dav_fs` module. | 
| [CVE-2026-34356](https://www.cve.org/CVERecord?id=CVE-2026-34356) | Low | No | AXIS OS devices do not use the vulnerable functionality. | 
| [CVE-2026-34355](https://www.cve.org/CVERecord?id=CVE-2026-34355) | Medium | No | AXIS OS devices do not use the `mod_proxy_html` module. | 
| [CVE-2026-34059](https://www.cve.org/CVERecord?id=CVE-2026-34059) | Low | No | AXIS OS devices do not use the `mod_proxy_ajp` module. | 
| [CVE-2026-34032](https://www.cve.org/CVERecord?id=CVE-2026-34032) | Low | No | AXIS OS devices do not use the `mod_proxy_ajp` module. | 
| [CVE-2026-33857](https://www.cve.org/CVERecord?id=CVE-2026-33857) | Low | No | AXIS OS devices do not use the vulnerable functionality. | 
| [CVE-2026-33523](https://www.cve.org/CVERecord?id=CVE-2026-33523) | Low | No | AXIS OS devices do not use the vulnerable functionality. | 
| [CVE-2026-33007](https://www.cve.org/CVERecord?id=CVE-2026-33007) | Low | No | AXIS OS devices do not use the `mod_authn_socache` module. | 
| [CVE-2026-33006](https://www.cve.org/CVERecord?id=CVE-2026-33006) | Medium | Yes | The vulnerability is patched by upgrading to Apache version 2.4.67. | 
| [CVE-2026-31431](https://www.cve.org/CVERecord?id=CVE-2026-31431) | 7.8 (High) | Yes | [Axis Security Advisory](https://www.axis.com/dam/public/f6/e9/42/copy-fail-attackpdf-en-US-542709.pdf?v=20260629071143) - Axis deems the severity of this vulnerability as low as it requires the attacker to be authenticated. Nevertheless we will provide patches for affected and supported software tracks in a timely manner. | 
| [CVE-2026-29170](https://www.cve.org/CVERecord?id=CVE-2026-29170) | Low | No | AXIS OS devices do not use the `mod_proxy_ftp` module. | 
| [CVE-2026-29169](https://www.cve.org/CVERecord?id=CVE-2026-29169) | Low | No | AXIS OS devices do not use the `mod_dav_lock` module. | 
| [CVE-2026-29168](https://www.cve.org/CVERecord?id=CVE-2026-29168) | Low | No | AXIS OS devices do not use the `mod_md` unrestricted module. | 
| [CVE-2026-29167](https://www.cve.org/CVERecord?id=CVE-2026-29167) | Low | No | AXIS OS devices do not use the `mod_ldap` module. | 
| [CVE-2026-28780](https://www.cve.org/CVERecord?id=CVE-2026-28780) | Low | No | AXIS OS devices do not use the `mod_proxy_ajp` module. | 
| [CVE-2026-24072](https://www.cve.org/CVERecord?id=CVE-2026-24072) | Medium | No | AXIS OS devices do not use the `mod_rewrite` module. | 
| [CVE-2026-23918](https://www.cve.org/CVERecord?id=CVE-2026-23918) | High | Yes | The vulnerability is patched by upgrading to Apache version 2.4.67. | 
| [CVE-2026-22796](https://www.cve.org/CVERecord?id=CVE-2026-22796) | Medium | Yes | The vulnerability is patched by upgrading to OpenSSL 3.0.19. | 
| [CVE-2026-22795](https://www.cve.org/CVERecord?id=CVE-2026-22795) | Medium | Yes | The vulnerability is patched by upgrading to OpenSSL 3.0.19. | 

#### CVE 2025

| CVE number | CVSS severity | Affected | Security advisory / Vulnerability summary | 
| [CVE-2025-69421](https://www.cve.org/CVERecord?id=CVE-2025-69421) | High | Yes | The vulnerability is patched by upgrading to OpenSSL 3.0.19. | 
| [CVE-2025-69420](https://www.cve.org/CVERecord?id=CVE-2025-69420) | High | Yes | The vulnerability is patched by upgrading to OpenSSL 3.0.19. | 
| [CVE-2025-69419](https://www.cve.org/CVERecord?id=CVE-2025-69419) | High | Yes | The vulnerability is patched by upgrading to OpenSSL 3.0.19. | 
| [CVE-2025-69418](https://www.cve.org/CVERecord?id=CVE-2025-69418) | Medium | Yes | The vulnerability is patched by upgrading to OpenSSL 3.0.19. | 
| [CVE-2025-68160](https://www.cve.org/CVERecord?id=CVE-2025-68160) | Medium | Yes | The vulnerability is patched by upgrading to OpenSSL 3.0.19. | 
| [CVE-2025-66200](https://www.cve.org/CVERecord?id=CVE-2025-66200) | Medium | No | AXIS OS devices do not use the vulnerable functionality. | 
| [CVE-2025-65082](https://www.cve.org/CVERecord?id=CVE-2025-65082) | Low | No | AXIS OS devices do not use the vulnerable functionality. | 
| [CVE-2025-59775](https://www.cve.org/CVERecord?id=CVE-2025-59775) | Medium | No | AXIS OS devices do not run the Windows version of Apache. | 
| [CVE-2025-58098](https://www.cve.org/CVERecord?id=CVE-2025-58098) | Low | No | AXIS OS devices do not use the vulnerable functionality. | 
| [CVE-2025-55753](https://www.cve.org/CVERecord?id=CVE-2025-55753) | Low | No | AXIS OS devices do not use the mod\_md module. | 
| [CVE‑2025‑55182](https://www.cve.org/CVERecord?id=CVE-2025-55182) | 10.0 (Critical) | No | AXIS OS devices do not use the affected versions/components | 
| [CVE-2025-53020](https://www.cve.org/CVERecord?id=CVE-2025-53020) | Medium | Yes | The vulnerability is patched by upgrading to Apache version 2.4.64. | 
| [CVE-2025-49812](https://www.cve.org/CVERecord?id=CVE-2025-49812) | Medium | No | AXIS OS devices do not use the “SSLEngine optional” option. | 
| [CVE-2025-49630](https://www.cve.org/CVERecord?id=CVE-2025-49630) | Low | Yes | The vulnerability is patched by upgrading to Apache version 2.4.64. | 
| [CVE-2025-26466](https://www.cve.org/CVERecord?id=CVE-2025-26466) | 6.8 (Medium) | Yes | The vulnerability is patched by upgrading to OpenSSH 9.9p1 | 
| [CVE-2025-26465](https://www.cve.org/CVERecord?id=CVE-2025-26465) | 5.9 (Medium) | No | AXIS OS devices do not utilize the affected SSH client. | 
| [CVE-2025-23048](https://www.cve.org/CVERecord?id=CVE-2025-23048) | Medium | Yes | The vulnerability is patched by upgrading to Apache version 2.4.64. | 
| [CVE-2025-15467](https://www.cve.org/CVERecord?id=CVE-2025-15467) | High | Yes | The vulnerability is patched by upgrading to OpenSSL 3.0.19. | 
| [CVE-2025-15224](https://www.cve.org/CVERecord?id=CVE-2025-15224) | Low | Yes | The vulnerability is patched by upgrading to cURL version 8.18.0. This version will only be provided on AXIS OS 11.11 and higher. For older AXIS OS LTS tracks, support for that cURL version is currently not available as it requires OpenSSL 3.0.0 and higher. | 
| [CVE-2025-15079](https://www.cve.org/CVERecord?id=CVE-2025-15079) | Low | Yes | The vulnerability is patched by upgrading to cURL version 8.18.0. This version will only be provided on AXIS OS 11.11 and higher. For older AXIS OS LTS tracks, support for that cURL version is currently not available as it requires OpenSSL 3.0.0 and higher. | 
| [CVE-2025-14819](https://www.cve.org/CVERecord?id=CVE-2025-14819) | Low | Yes | The vulnerability is patched by upgrading to cURL version 8.18.0. This version will only be provided on AXIS OS 11.11 and higher. For older AXIS OS LTS tracks, support for that cURL version is currently not available as it requires OpenSSL 3.0.0 and higher. | 
| [CVE-2025-14524](https://www.cve.org/CVERecord?id=CVE-2025-14524) | Low | Yes | The vulnerability is patched by upgrading to cURL version 8.18.0. This version will only be provided on AXIS OS 11.11 and higher. For older AXIS OS LTS tracks, support for that cURL version is currently not available as it requires OpenSSL 3.0.0 and higher. | 
| [CVE-2025-14017](https://www.cve.org/CVERecord?id=CVE-2025-14017) | Medium | No | AXIS OS devices do not use the vulnerable functionality. | 
| [CVE-2025-13034](https://www.cve.org/CVERecord?id=CVE-2025-13034) | Medium | No | AXIS OS devices do not use the vulnerable functionality. | 

#### CVE 2024

| CVE number | CVSS severity | Affected | Security advisory / Vulnerability summary | 
| [CVE-2024-47252](https://www.cve.org/CVERecord?id=CVE-2024-47252) | Low | No | AXIS OS devices do not use the vulnerable functionality. | 
| [CVE-2024-43394](https://www.cve.org/CVERecord?id=CVE-2024-43394) | Medium | No | AXIS OS devices do not run the Windows version of Apache. | 
| [CVE-2024-43204](https://www.cve.org/CVERecord?id=CVE-2024-43204) | Low | No | AXIS OS devices do not use the mod\_proxy module. | 
| [CVE-2024-42516](https://www.cve.org/CVERecord?id=CVE-2024-42516) | Medium | Yes | The vulnerability is patched by upgrading to Apache version 2.4.64. | 
| [CVE-2024-40898](https://www.cve.org/CVERecord?id=CVE-2024-40898) | 7.5 (High) | No | AXIS OS devices do not run the Windows version of Apache. | 
| [CVE-2024-40725](https://www.cve.org/CVERecord?id=CVE-2024-40725) | 5.3 (Medium) | No | AXIS OS devices do not utilize the affected function. | 
| [CVE-2024-39884](https://www.cve.org/CVERecord?id=CVE-2024-39884) |  | No | AXIS OS devices do not utilize the affected function. | 
| [CVE-2024-39573](https://www.cve.org/CVERecord?id=CVE-2024-39573) | 7.5 (High) | Yes | The vulnerability is patched by upgrading to Apache version 2.4.60. | 
| [CVE-2024-38477](https://www.cve.org/CVERecord?id=CVE-2024-38477) | 7.5 (High) | Yes | The vulnerability is patched by upgrading to Apache version 2.4.60. | 
| [CVE-2024-38476](https://www.cve.org/CVERecord?id=CVE-2024-38476) | 9.8 (Critical) | Yes | The vulnerability is patched by upgrading to Apache version 2.4.60. | 
| [CVE-2024-38475](https://www.cve.org/CVERecord?id=CVE-2024-38475) |  | Yes | The vulnerability is patched by upgrading to Apache version 2.4.60. | 
| [CVE-2024-38474](https://www.cve.org/CVERecord?id=CVE-2024-38474) | 9.8 (Critical) | Yes | The vulnerability is patched by upgrading to Apache version 2.4.60. | 
| [CVE-2024-38473](https://www.cve.org/CVERecord?id=CVE-2024-38473) |  | Yes | The vulnerability is patched by upgrading to Apache version 2.4.60. | 
| [CVE-2024-38472](https://www.cve.org/CVERecord?id=CVE-2024-38472) |  | No | AXIS OS devices do not run the Windows version of Apache. | 
| [CVE-2024-36387](https://www.cve.org/CVERecord?id=CVE-2024-36387) |  | Yes | The vulnerability is patched by upgrading to Apache version 2.4.60. | 
| [CVE-2024-28960](https://www.cve.org/CVERecord?id=CVE-2024-28960) |  | No | AXIS OS Z-Wave device does not use Mbed TLS. | 
| [CVE-2024-28836](https://www.cve.org/CVERecord?id=CVE-2024-28836) |  | No | AXIS OS Z-Wave device does not use Mbed TLS. | 
| [CVE-2024-28755](https://www.cve.org/CVERecord?id=CVE-2024-28755) |  | No | AXIS OS Z-Wave device does not use Mbed TLS. | 
| [CVE-2024-27316](https://www.cve.org/CVERecord?id=CVE-2024-27316) | 7.5 (High) | Yes | The vulnerability is patched by upgrading to Apache version 2.4.59. | 
| [CVE-2024-26898](https://www.cve.org/CVERecord?id=CVE-2024-26898) | 7.8 (High) | No | AXIS OS devices do not use this ATA over Ethernet driver. | 
| [CVE-2024-24795](https://www.cve.org/CVERecord?id=CVE-2024-24795) |  | Yes | The vulnerability is patched by upgrading to Apache version 2.4.59. | 
| [CVE-2024-23775](https://www.cve.org/CVERecord?id=CVE-2024-23775) | 7.5 (High) | No | AXIS OS Z-Wave device does not use Mbed TLS. | 
| [CVE-2024-23744](https://www.cve.org/CVERecord?id=CVE-2024-23744) | 7.5 (High) | No | AXIS OS Z-Wave device does not use Mbed TLS. | 
| [CVE-2024-23170](https://www.cve.org/CVERecord?id=CVE-2024-23170) | 5.5 (Medium) | No | AXIS OS Z-Wave device does not use Mbed TLS. | 
| [CVE-2024-22472](https://www.cve.org/CVERecord?id=CVE-2024-22472) | 8.1 (High) | No | AXIS OS Z-Wave devices do not use the affected module. | 
| [CVE-2024-13176](https://www.cve.org/CVERecord?id=CVE-2024-13176) | Low | Yes | Once the versions are made available by OpenSSL, the vulnerability is patched by upgrading to: OpenSSL version 1.1.1zb - LTS 2022, LTS 2020, PSS 8.40, PSS 6.50. OpenSSL version 3.0.16 - Active track 12 and LTS 2024. | 
| [CVE-2024-9681](https://www.cve.org/CVERecord?id=CVE-2024-9681) | 6.5 (Medium) | Yes | The vulnerability is patched by upgrading to cURL version 8.11.0. | 
| [CVE-2024-9143](https://www.cve.org/CVERecord?id=CVE-2024-9143) |  | No | AXIS OS devices do not use "exotic" curves as referred to in the OpenSSL advisory. | 
| [CVE-2024-8957](https://www.cve.org/CVERecord?id=CVE-2024-8957) | 9.1 (Critical) | No | AXIS OS devices do not use the affected opensource packages and implementations. | 
| [CVE-2024-8956](https://www.cve.org/CVERecord?id=CVE-2024-8956) | 7.2 (High) | No | AXIS OS devices do not use the affected opensource packages and implementations. | 
| [CVE-2024-7264](https://www.cve.org/CVERecord?id=CVE-2024-7264) | 6.5 (Medium) | No | AXIS OS devices do not use the affected TLS backend. | 
| [CVE-2024-6387](https://www.cve.org/CVERecord?id=CVE-2024-6387) | 8.1 (High) | Yes | The vulnerability is patched by upgrading to OpenSSH version 9.8. | 
| [CVE-2024-5535](https://www.cve.org/CVERecord?id=CVE-2024-5535) | 6.5 (Medium) | Yes | The vulnerability is patched by upgrading to OpenSSL version 1.1.1za (AXIS OS 6.50, LTS 2018/2020/2022) and OpenSSL version 3.0.15 (LTS 2024/active track). | 
| [CVE-2024-3094](https://www.cve.org/CVERecord?id=CVE-2024-3094) | 10 (Critical) | No | AXIS OS devices are running a different XZ Utils version which is not affected. | 
| [CVE-2024-3052](https://www.cve.org/CVERecord?id=CVE-2024-3052) | 7.5 (High) | No | AXIS OS Z-Wave devices use a later version that is not affected. | 
| [CVE-2024-2466](https://www.cve.org/CVERecord?id=CVE-2024-2466) |  | No | AXIS OS devices do not use mbedTLS. | 
| [CVE-2024-2398](https://www.cve.org/CVERecord?id=CVE-2024-2398)	 | 8.6 (High) | Yes | The vulnerability is patched by upgrading to cURL version 8.7.1. | 
| [CVE-2024-2379](https://www.cve.org/CVERecord?id=CVE-2024-2379)	 |  | No | AXIS OS devices do not use wolfSSL. | 
| [CVE-2024-2004](https://www.cve.org/CVERecord?id=CVE-2024-2004)	 | 3.5 (Low) | Yes | The vulnerability is patched by upgrading to cURL version 8.7.1. | 

#### CVE 2023

| CVE number | Affected | Security advisory / Vulnerability summary | 
| [CVE-2023-51395](https://www.cve.org/CVERecord?id=CVE-2023-51395) | No | AXIS OS Z-Wave devices are running as controllers, not end devices. | 
| [CVE-2023-48795](https://www.cve.org/CVERecord?id=CVE-2023-48795) | Yes | The vulnerability is patched by upgrading to OpenSSH version 9.6. | 
| [CVE-2023-46446](https://www.cve.org/CVERecord?id=CVE-2023-46446) | No | AXIS OS devices do not include AsyncSSH. | 
| [CVE-2023-46445](https://www.cve.org/CVERecord?id=CVE-2023-46445) | No | AXIS OS devices do not include AsyncSSH. | 
| [CVE-2023-46219](https://www.cve.org/CVERecord?id=CVE-2023-46219) | Yes | The vulnerability is patched by upgrading to cURL version 8.5.0. | 
| [CVE-2023-46218](https://www.cve.org/CVERecord?id=CVE-2023-46218) | Yes | The vulnerability is patched by upgrading to cURL version 8.5.0. | 
| [CVE-2023-45802](https://www.cve.org/CVERecord?id=CVE-2023-45802) | Yes | The vulnerability is patched by upgrading to Apache version 2.4.58. | 
| [CVE-2023-45199](https://www.cve.org/CVERecord?id=CVE-2023-45199) | No | AXIS OS Z-Wave devices do not use MBED TLS. | 
| [CVE-2023-44487](https://www.cve.org/CVERecord?id=CVE-2023-44487) | No | AXIS OS devices use the affected library in a different, non-vulnerable way. | 
| [CVE-2023-43622](https://www.cve.org/CVERecord?id=CVE-2023-43622) | Yes | The vulnerability is patched by upgrading to Apache version 2.4.58. | 
| [CVE-2023-38709](https://www.cve.org/CVERecord?id=CVE-2023-38709) | Yes | The vulnerability is patched by upgrading to Apache version 2.4.59. | 
| [CVE-2023-38546](https://www.cve.org/CVERecord?id=CVE-2023-38546) | Yes | The vulnerability is patched by upgrading to cURL version 8.4.0. | 
| [CVE-2023-38545](https://www.cve.org/CVERecord?id=CVE-2023-38545) | Yes | The vulnerability is patched by upgrading to cURL version 8.4.0. | 
| [CVE-2023-38408](https://www.cve.org/CVERecord?id=CVE-2023-38408) | No | AXIS OS devices do not include the ssh-agent of OpenSSH. | 
| [CVE-2023-32001](https://www.cve.org/CVERecord?id=CVE-2023-32001) | Yes | The vulnerability ispatched by upgrading to cURL version 8.0.1. | 
| [CVE–2023–31122](https://www.cve.org/CVERecord?id=CVE-2023-31122) | No | AXIS OS devices do not use the mod\_macro module. | 
| [CVE-2023-28322](https://www.cve.org/CVERecord?id=CVE-2023-28322) | Yes | The vulnerability is patched by upgrading to cURL version 8.0.1. | 
| [CVE-2023-28321](https://www.cve.org/CVERecord?id=CVE-2023-28321) | Yes | The vulnerability is patched by upgrading to cURL version 8.0.1. | 
| [CVE-2023-28320](https://www.cve.org/CVERecord?id=CVE-2023-28320) | Yes | The vulnerability is patched by upgrading to cURL version 8.0.1. | 
| [CVE-2023-28319](https://www.cve.org/CVERecord?id=CVE-2023-28319) | Yes | The vulnerability is patched by upgrading to cURL version 8.0.1. | 
| [CVE-2023-27538](https://www.cve.org/CVERecord?id=CVE-2023-27538)  | Yes | The vulnerability is patched by upgrading to cURL version 8.0.1. | 
| [CVE-2023-27537](https://www.cve.org/CVERecord?id=CVE-2023-27537) | Yes | The vulnerability is patched by upgrading to cURL version 8.0.1. | 
| [CVE-2023-27536](https://www.cve.org/CVERecord?id=CVE-2023-27536) | Yes | The vulnerability is patched by upgrading to cURL version 8.0.1. | 
| [CVE-2023-27535](https://www.cve.org/CVERecord?id=CVE-2023-27535) | Yes | The vulnerability is patched by upgrading to cURL version 8.0.1. | 
| [CVE-2023-27534](https://www.cve.org/CVERecord?id=CVE-2023-27534)  | Yes | The vulnerability is patched by upgrading to cURL version 8.0.1. | 
| [CVE-2023-27533](https://www.cve.org/CVERecord?id=CVE-2023-27533)  | No | cURL’s GSS functionality is not used on AXIS OS devices. | 
| [CVE-2023-27522](https://www.cve.org/CVERecord?id=CVE-2023-27522) | No | AXIS OS devices do not use the mod\_proxy\_uwsgi module. | 
| [CVE-2023-26083](https://www.cve.org/CVERecord?id=CVE-2023-26083) | No | AXIS OS devices do not use this GPU Kernel driver. | 
| [CVE-2023-25690](https://www.cve.org/CVERecord?id=CVE-2023-25690) | Yes | The vulnerability is patched by upgrading to Apache version 2.4.56. | 
| [CVE-2023-25136](https://www.cve.org/CVERecord?id=CVE-2023-25136) | Yes | AXIS OS devices are running a different OpenSSH version which is not affected. | 
| [CVE-2023-23916](https://www.cve.org/CVERecord?id=CVE-2023-23916) | Yes | The vulnerability is patched by upgrading to cURL version 7.88.1. | 
| [CVE-2023-23915](https://www.cve.org/CVERecord?id=CVE-2023-23915) | No | AXIS OS devices are running a different cURL version which is not affected. | 
| [CVE-2023-23914](https://www.cve.org/CVERecord?id=CVE-2023-23914) | No | AXIS OS devices are running a different cURL version which is not affected. | 
| [CVE-2023-6246](https://www.cve.org/CVERecord?id=CVE-2023-6246) | Yes | Only AXIS OS 11 active track is affected. The vulnerability is patched by upgrading to glibc version 2.39. Other AXIS OS LTS tracks are not affected as root-privileges are already available to the user when logging in through SSH console. | 
| [CVE-2023-5678](https://www.cve.org/CVERecord?id=CVE-2023-5678) | Yes | The vulnerability is patched by upgrading to OpenSSL version 1.1.1x (AXIS OS 6.50, LTS 2018/2020/2022) & OpenSSL version 3.0.13 on active track. | 
| [CVE-2023-4807](https://www.cve.org/CVERecord?id=CVE-2023-4807) | No | AXIS OS devices do not use Windows XMM registers. | 
| [CVE-2023-4211](https://www.cve.org/CVERecord?id=CVE-2023-4211) | No | AXIS OS devices do not use this GPU Kernel driver. | 
| [CVE-2023-3817](https://www.cve.org/CVERecord?id=CVE-2023-3817)  | Yes | The vulnerability is patched by upgrading to OpenSSL version 1.1.1v. | 
| [CVE-2023-3446](https://www.cve.org/CVERecord?id=CVE-2023-3446)  | Yes | The vulnerability is patched by upgrading to OpenSSL version 1.1.1v. | 
| [CVE-2023-2588](https://www.cve.org/CVERecord?id=CVE-2022-2588) | No | AXIS OS devices do not have the affected function enabled. | 
| [CVE-2023-1018](https://www.cve.org/CVERecord?id=CVE-2023-1018)  | No | Through testing, the vulnerability cannot be exploited in TPM modules used by Axis devices. | 
| [CVE-2023-1017](https://www.cve.org/CVERecord?id=CVE-2023-1017)  | No | Through testing, the vulnerability cannot be exploited in TPM modules used by Axis devices. | 
| [CVE-2023-0466](https://www.cve.org/CVERecord?id=CVE-2023-0466) | No | AXIS OS devices do not utilize non-default certificate policy validation | 
| [CVE-2023-0465](https://www.cve.org/CVERecord?id=CVE-2023-0465) | No | AXIS OS devices do not utilize non-default certificate policy validation | 
| [CVE-2023-0464](https://www.cve.org/CVERecord?id=CVE-2023-0464) | No | AXIS OS devices do not utilize non-default certificate policy validation | 
| [CVE-2023-0401](https://www.cve.org/CVERecord?id=CVE-2023-0401) | No | AXIS OS devices are running a different OpenSSL track which is not affected. | 
| [CVE-2023-0286](https://www.cve.org/CVERecord?id=CVE-2023-0286)  | Yes | The vulnerability is patched by upgrading to OpenSSL version 1.1.1t. | 
| [CVE-2023-0217](https://www.cve.org/CVERecord?id=CVE-2023-0217) | No | AXIS OS devices are running a different OpenSSL track which is not affected. | 
| [CVE-2023-0216](https://www.cve.org/CVERecord?id=CVE-2023-0216) | No | AXIS OS devices are running a different OpenSSL track which is not affected. | 
| [CVE-2023-0215](https://www.cve.org/CVERecord?id=CVE-2023-0215) | Yes | The vulnerability is patched by upgrading to OpenSSL version 1.1.1t. | 

#### CVE 2022

| CVE number | Affected | Security advisory / Vulnerability summary | 
| [CVE-2022-46152](https://www.cve.org/CVERecord?id=CVE-2022-46152) | Yes | The vulnerability is patched on the AXIS OS active track and LTS 2022. Updating is recommended. | 
| [CVE-2022-43552](https://www.cve.org/CVERecord?id=CVE-2022-43552) | No | HTTP proxy tunnel functionality is not enabled on AXIS OS devices. | 
| [CVE-2022-43551](https://www.cve.org/CVERecord?id=CVE-2022-43551) | No | cURL’s HSTS functionality is not enabled on AXIS OS devices. | 
| [CVE-2022-42916](https://www.cve.org/CVERecord?id=CVE-2022-42916) | Yes | The vulnerability is patched by upgrading to cURL version 7.86.0. | 
| [CVE-2022-42915](https://www.cve.org/CVERecord?id=CVE-2022-42915) | Yes | The vulnerability is patched by upgrading to cURL version 7.86.0. | 
| [CVE-2022-42889](https://www.cve.org/CVERecord?id=CVE-2022-42889) | No | AXIS OS devices do not use the affected Apache Commons software package. | 
| [CVE-2022-42012](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42012) | No | While AXIS OS devices use some of the affected functions, all of these vulnerabilities require root access to be exploited and when root access is gained, full control over the device is already established. | 
| [CVE-2022-42011](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42011) | No | While AXIS OS devices use some of the affected functions, all of these vulnerabilities require root access to be exploited and when root access is gained, full control over the device is already established. | 
| [CVE-2022-42010](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42010) | No | While AXIS OS devices use some of the affected functions, all of these vulnerabilities require root access to be exploited and when root access is gained, full control over the device is already established. | 
| [CVE-2022-38181](https://www.cve.org/CVERecord?id=CVE-2022-38181) | No | AXIS OS devices do not use this GPU Kernel driver. | 
| [CVE-2022-37436](https://www.cve.org/CVERecord?id=CVE-2022-37436) | Yes | The vulnerability is patched by upgrading to Apache version 2.4.55. | 
| [CVE-2022-36760](https://www.cve.org/CVERecord?id=CVE-2022-36760) | No | AXIS OS devices do not use the mod\_proxy\_ajp module. | 
| [CVE-2022-35260](https://www.cve.org/CVERecord?id=CVE-2022-35260) | Yes | The vulnerability is patched by upgrading to cURL version 7.86.0. | 
| [CVE-2022-35252](https://www.cve.org/CVERecord?id=CVE-2022-35252) | No | AXIS OS devices do not use the cookie-engine of cURL. | 
| [CVE-2022-32221](https://www.cve.org/CVERecord?id=CVE-2022-32221) | Yes | The vulnerability is patched by upgrading to cURL version 7.86.0. | 
| [CVE-2022-32208](https://www.cve.org/CVERecord?id=CVE-2022-32208) | No | AXIS OS devices do not have Kerberos enabled. | 
| [CVE-2022-32207](https://www.cve.org/CVERecord?id=CVE-2022-32207) | Yes | The vulnerability is patched by upgrading to cURL version 7.84.0. | 
| [CVE-2022-32206](https://www.cve.org/CVERecord?id=CVE-2022-32206) | Yes | The vulnerability is patched by upgrading to cURL version 7.84.0. | 
| [CVE-2022-32205](https://www.cve.org/CVERecord?id=CVE-2022-32205) | Yes | The vulnerability is patched by upgrading to cURL version 7.84.0. | 
| [CVE-2022-31813](https://www.cve.org/CVERecord?id=CVE-2022-31813) | No | AXIS OS devices do not utilize IP based authentication. | 
| [CVE-2022-30556](https://www.cve.org/CVERecord?id=CVE-2022-30556) | Yes | The vulnerability is patched by upgrading to Apache 2.4.54. | 
| [CVE-2022-30522](https://www.cve.org/CVERecord?id=CVE-2022-30522) | No | AXIS OS devices do not use the mod\_sed module. | 
| [CVE-2022-30295](https://www.cve.org/CVERecord?id=CVE-2022-30295) | Yes | Affects AXIS P7701 Video Decoder. Other Axis devices that are running the latest AXIS OS LTS or active version do not use the uClibc or uClibc-ng library. We are currently awaiting the availability of an upstream patch to be available to judge if we can provide a service release that patches this vulnerability. | 
| [CVE-2022-30115](https://cve.report/CVE-2022-30115) | No |  | 
| [CVE-2022-29404](https://www.cve.org/CVERecord?id=CVE-2022-29404) | Yes | The vulnerability is patched by upgrading to Apache 2.4.54. | 
| [CVE-2022-28861](https://www.cve.org/CVERecord?id=CVE-2022-28861) | Yes | This vulnerability applies to Citilog software, not a vulnerability in AXIS OS itself. | 
| [CVE-2022-28860](https://www.cve.org/CVERecord?id=CVE-2022-28860) | Yes | This vulnerability applies to Citilog software, not a vulnerability in AXIS OS itself. | 
| [CVE-2022-28615](https://www.cve.org/CVERecord?id=CVE-2022-28615) | Yes | The vulnerability is patched by upgrading to Apache 2.4.54. | 
| [CVE-2022-28614](https://www.cve.org/CVERecord?id=CVE-2022-28614) | Yes | The vulnerability is patched by upgrading to Apache 2.4.54. | 
| [CVE-2022-28330](https://www.cve.org/CVERecord?id=CVE-2022-28330) | Yes | The vulnerability is patched by upgrading to Apache 2.4.54. | 
| [CVE-2022-27782](https://cve.report/CVE-2022-27782) | Yes | The vulnerability is patched by upgrading to cURL 7.83.1. | 
| [CVE-2022-27781](https://cve.report/CVE-2022-27781) | Yes | The vulnerability is patched by upgrading to cURL 7.83.1. | 
| [CVE-2022-27780](https://cve.report/CVE-2022-27780) | No |  | 
| [CVE-2022-27779](https://cve.report/CVE-2022-27779) | No |  | 
| [CVE-2022-27778](https://cve.report/CVE-2022-27778) | No |  | 
| [CVE-2022-27776](https://www.cve.org/CVERecord?id=CVE-2022-27776) | Yes | The vulnerability is patched in a timely manner on the AXIS OS active track and the LTS tracks. | 
| [CVE-2022-27775](https://www.cve.org/CVERecord?id=CVE-2022-27775) | Yes | The vulnerability is patched in a timely manner on the AXIS OS active track and the LTS tracks. | 
| [CVE-2022-27774](https://www.cve.org/CVERecord?id=CVE-2022-27774) | Yes | The vulnerability is patched in a timely manner on the AXIS OS active track and the LTS tracks. | 
| [CVE-2022-26377](https://www.cve.org/CVERecord?id=CVE-2022-26377) | No | AXIS OS devices do not use the mod\_proxy\_ajp module. | 
| [CVE-2022-22965](https://www.cve.org/CVERecord?id=CVE-2022-22965) | No | Not affected as JDK, Spring Cloud function and/or Apache Tomcat are not used. | 
| [CVE-2022-22963](https://www.cve.org/CVERecord?id=CVE-2022-22963) | No | Not affected as JDK, Spring Cloud function and/or Apache Tomcat are not used. | 
| [CVE-2022-23943](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23943) | No | AXIS OS devices do not use the mod\_sed module. | 
| [CVE-2022-22721](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-22721) | No | While AXIS OS devices use the core module, the command LimitXMLRequestBody is unused. | 
| [CVE-2022-22720](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-22720) | Yes | The vulnerability is patched by upgrading to Apache version 2.4.53. | 
| [CVE-2022-22719](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-22719) | No | AXIS OS devices do not use the mod\_lua module. | 
| [CVE-2022-22706](https://www.cve.org/CVERecord?id=CVE-2022-22706) | No |  | 
| [CVE-2022-4450](https://www.cve.org/CVERecord?id=CVE-2022-4450)   | Yes | The vulnerability is patched by upgrading to OpenSSL version 1.1.1t. | 
| [CVE-2022-4304](https://www.cve.org/CVERecord?id=CVE-2022-4304) | Yes | The vulnerability is patched by upgrading to OpenSSL version 1.1.1t. | 
| [CVE-2022-4203](https://www.cve.org/CVERecord?id=CVE-2022-4203) | No | AXIS OS devices are running a different OpenSSL track which is not affected. | 
| [CVE-2022-3786](https://www.cve.org/CVERecord?id=CVE-2022-3786) | No | AXIS OS devices are running a different OpenSSL track which is not affected. | 
| [CVE-2022-3602](https://www.cve.org/CVERecord?id=CVE-2022-3602) | No | AXIS OS devices are running a different OpenSSL track which is not affected. | 
| [CVE-2022-2586](https://www.cve.org/CVERecord?id=CVE-2022-2586) | Yes | All Axis products with Linux Kernel version 4.14 and onwards are affected by this vulnerability. Axis deems the severity of these vulnerabilities as low as it requires the attacker to be authenticated. Only after successful authentication can this vulnerability be exploited (=local exploit). We will provide patches for the Linux Kernel LTS versions that are affected in a timely manner. | 
| [CVE-2022-2585](https://www.cve.org/CVERecord?id=CVE-2022-2585) | Yes | All Axis products with Linux Kernel version 4.14 and onwards are affected by this vulnerability. We are awaiting upstream patches for the Linux Kernel LTS versions that are affected. The vulnerability is patched already for all Axis products with Linux Kernel version 5.15 and higher and has been patched for a number of products on Linux Kernel version 4.19. Axis deems the severity of these vulnerabilities as low as it requires the attacker to be authenticated. Only after successful authentication can this vulnerability be exploited (=local exploit). We will provide patches for the Linux Kernel LTS versions that are affected in a timely manner. | 
| [CVE-2022-2274](https://www.cve.org/CVERecord?id=CVE-2022-2274) | No | AXIS OS devices are running a different OpenSSL track which is not affected. | 
| [CVE-2022-2097](https://www.cve.org/CVERecord?id=CVE-2022-2097) | No | AXIS OS devices do not use an x86 architecture. | 
| [CVE-2022-2068](https://www.cve.org/CVERecord?id=CVE-2022-2068) | No | AXIS OS devices do not use the c\_rehash script. | 
| [CVE-2022-1292](https://www.cve.org/CVERecord?id=CVE-2022-1292) | No | AXIS OS devices do not use the c\_rehash script. | 
| [CVE-2022-0847](https://www.cve.org/CVERecord?id=CVE-2022-0847) | No | The affected Linux Kernel 5.8 is not used, AXIS OS devices utilizes lower versions of Linux Kernel on Linux Long-Term releases. | 
| [CVE-2022-0778](https://www.cve.org/CVERecord?id=CVE-2022-0778) | Yes | The vulnerability is patched by upgrading to OpenSSL version 1.1.1n. | 
| [CVE-2022-0336](https://www.cve.org/CVERecord?id=CVE-2022-0336) | No | This vulnerability is exploitable when Active Directory (AD/ADFS) services are used, which is a functionality that is not supported in AXIS OS devices. | 

#### CVE 2021

| CVE number | Affected | Security advisory / Vulnerability summary | 
| [CVE-2021-44790](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-44790) | No | AXIS OS devices do not use the mod\_lua module. | 
| [CVE-2021-44228](https://www.cve.org/CVERecord?id=CVE-2021-44228) | No | AXIS OS products only use the [vanilla Apache webserver](https://help.axis.com/axis-os-knowledge-base#apache-struts-and-apache-tomcat) and not Apache Log4j, which is vulnerable. A general statement for the Axis portfolio can be found [here](https://www.axis.com/support/product-security). | 
| [CVE-2021-44224](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-44224) | Yes | The vulnerability is patched by upgrading to Apache version 2.4.52. | 
| [CVE-2021-43523](https://www.cve.org/CVERecord?id=CVE-2021-43523) | Yes | Affects AXIS P7701 Video Decoder. Other Axis devices that are running the latest AXIS OS LTS or active version do not use the uClibc or uClibc-ng library. We are currently awaiting the availability of an upstream patch to be available to judgeif we can provide a service release that patches this vulnerability. | 
| [CVE-2021-42013](https://cve.report/CVE-2021-42013) | No |  | 
| [CVE-2021-41773](https://cve.report/CVE-2021-41773) | No |  | 
| [CVE-2021-41617](https://www.cve.org/CVERecord?id=CVE-2021-41617) | No | Not affected since the AXIS OS configuration for SSH doesn't include AuthorizedKeysCommand or AuthorizedPrincipalsCommand in its default configuration. | 
| [CVE-2021-41524](https://cve.report/CVE-2021-41524) | No |  | 
| [CVE-2021-40438](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-40438) | Yes | The vulnerability is patched in AXIS OS active track and the LTS tracks | 
| [CVE-2021-40146](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-40146) | No |  | 
| [CVE-2021-39275](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-39275) | Yes | The vulnerability is patched in AXIS OS active track and the LTS tracks | 
| [CVE-2021-36260](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-36260) | No |  | 
| [CVE-2021-36160](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-36160) | No |  | 
| [CVE-2021-34798](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-34798) | Yes | The vulnerability has been patched on the AXIS OS active track and the LTS tracks. | 
| [CVE-2021-33910](https://cve.report/CVE-2021-33910) | Yes | The vulnerability has been patched. Updating is recommended. | 
| [CVE-2021-33558](https://www.cve.org/CVERecord?id=CVE-2021-33558) | No | The affected 3 <sup>rd</sup> party component backup.html, preview.html, js/log.js, log.html, email.html, online-users.html, and config.js are not used in Axis products below version 5.70 that utilize the BOA webserver. Axis products with 5.70 and higher utilize the Apache webserver where these vulnerabilities do not apply as the BOA webserver has been removed. | 
| [CVE-2021-33193](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33193) | Yes | Affects AXIS OS 10.1 - 10.7. The vulnerability has been patched. Updating is recommended. | 
| [CVE-2021-32934](https://nvd.nist.gov/vuln/detail/CVE-2021-32934) | No |  | 
| [CVE-2021-31618](https://nvd.nist.gov/vuln/detail/CVE-2021-31618) | No |  | 
| [CVE-2021-31618](https://nvd.nist.gov/vuln/detail/CVE-2021-31618) | No |  | 
| [CVE-2021-31618](https://nvd.nist.gov/vuln/detail/CVE-2021-31618) | Yes | Affects AXIS OS 10.1 - 10.6. Has been patched in AXIS OS 10.7. | 
| [CVE-2021-30641](https://nvd.nist.gov/vuln/detail/CVE-2021-30641) | No |  | 
| [CVE-2021-29462](https://cve.report/CVE-2021-29462) | Yes | The vulnerability has been patched on the AXIS OS active track and the LTS tracks. | 
| [CVE-2021-29256](https://www.cve.org/CVERecord?id=CVE-2021-29256) | No | AXIS OS devices do not use this GPU Kernel driver. | 
| [CVE-2021-28664](https://www.cve.org/CVERecord?id=CVE-2021-28664) | No | AXIS OS devices do not use this GPU Kernel driver. | 
| [CVE-2021-28663](https://www.cve.org/CVERecord?id=CVE-2021-28663) | No | AXIS OS devices do not use this GPU Kernel driver. | 
| [CVE-2021-28372](https://www.cve.org/CVERecord?id=CVE-2021-28372) | No | Not affected since AXIS OS doesn’t utilize the ThroughTek (TUTK) TCP/IP stack application. | 
| [CVE-2021-27365](https://www.cve.org/CVERecord?id=CVE-2021-27365) | No | AXIS OS devices do not utilize ISCSI functionality. | 
| [CVE-2021-27219](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-27219) | Yes | The vulnerability has been patched on the LTS tracks. | 
| [CVE-2021-27218](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-27218) | Yes | The vulnerability has been patched on the LTS tracks. | 
| [CVE-2021-26691](https://nvd.nist.gov/vuln/detail/CVE-2021-26691) | No |  | 
| [CVE-2021-26690](https://nvd.nist.gov/vuln/detail/CVE-2021-26690) | No |  | 
| [CVE-2021-25677](https://nvd.nist.gov/vuln/detail/CVE-2021-25677) | No |  | 
| [CVE-2021-23841](https://nvd.nist.gov/vuln/detail/CVE-2021-23841) | No |  | 
| [CVE-2021-23840](https://nvd.nist.gov/vuln/detail/CVE-2021-23840) | No | The vulnerability has been patched on the AXIS OS active track and the LTS tracks. Updating is recommended. | 
| [CVE-2021-23839](https://nvd.nist.gov/vuln/detail/CVE-2021-23839) | No |  | 
| [CVE-2021-22947](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-22947) | Yes | The vulnerability has been patched on the AXIS OS active track and the LTS tracks. | 
| [CVE-2021-22946](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-22946) | Yes | The vulnerability has been patched on the AXIS OS active track and the LTS tracks. | 
| [CVE-2021-22945](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-22945) | No |  | 
| [CVE-2021-22901](https://nvd.nist.gov/vuln/detail/CVE-2021-22901) | No |  | 
| [CVE-2021-22898](https://nvd.nist.gov/vuln/detail/CVE-2021-22898) | No |  | 
| [CVE-2021-22897](https://nvd.nist.gov/vuln/detail/CVE-2021-22897) | No |  | 
| [CVE-2021-22890](https://nvd.nist.gov/vuln/detail/CVE-2021-22890) | No | The vulnerability has been patched on the AXIS OS active track and the LTS tracks. Updating is recommended. | 
| [CVE-2021-22876](https://nvd.nist.gov/vuln/detail/CVE-2021-22876) | No |  | 
| [CVE-2021-21727](https://nvd.nist.gov/vuln/detail/CVE-2021-21727) | No |  | 
| [CVE-2021-4160](https://www.cve.org/CVERecord?id=CVE-2021-4160) | Yes | The vulnerability is patched by upgrading to OpenSSL 1.1.1m. | 
| [CVE-2021-4104](https://www.cve.org/CVERecord?id=CVE-2021-4104) | No | AXIS OS products only use the [vanilla Apache webserver](https://help.axis.com/axis-os-knowledge-base#apache-struts-and-apache-tomcat) and not Apache Log4j, which is vulnerable. A general statement for the Axis portfolio can be found [here](https://www.axis.com/support/product-security). | 
| [CVE-2021-4034](https://www.cve.org/CVERecord?id=CVE-2021-4034) | No | Not affected since the Polkit's (PolicyKit) pkexec component is not used. | 
| [CVE-2021-4032](https://www.cve.org/CVERecord?id=CVE-2021-4032) | No | Not affected since x86-computing architecture platform is not used in AXIS OS products. AXIS OS products utilize MIPS- and ARM-based computing architecture instead. | 
| [CVE-2021-3712](https://nvd.nist.gov/vuln/detail/CVE-2021-3712) | Yes | The vulnerability has been patched on the AXIS OS active track and the LTS tracks. Updating is recommended. | 
| [CVE-2021-3658](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3658) | Yes | Affects AXIS OS 8.40 LTS and 9.80 LTS. The vulnerability has been patched on the LTS tracks. | 
| [CVE-2021-3450](https://nvd.nist.gov/vuln/detail/CVE-2021-3450) | No |  | 
| [CVE-2021-3449](https://nvd.nist.gov/vuln/detail/CVE-2021-3449) | Yes | The vulnerability has been patched on the AXIS OS active track and the LTS tracks. Updating is recommended. | 

#### CVE 2020

| CVE number | Affected | Security advisory / Vulnerability summary | 
| [CVE-2020-35452](https://nvd.nist.gov/vuln/detail/CVE-2020-35452) | Yes | The vulnerability has been patched on the AXIS OS active track and the LTS tracks. Updating is recommended. | 
| [CVE-2020-27738](https://nvd.nist.gov/vuln/detail/CVE-2020-27738) | No |  | 
| [CVE-2020-27737](https://nvd.nist.gov/vuln/detail/CVE-2020-27737) | No |  | 
| [CVE-2020-27736](https://nvd.nist.gov/vuln/detail/CVE-2020-27736) | No |  | 
| [CVE-2020-27009](https://nvd.nist.gov/vuln/detail/CVE-2020-27009) | No |  | 
| [CVE-2020-26558](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-26558) | Yes | Affects Axis body worn solution and Axis wireless cameras. The vulnerability has been patched on the AXIS OS active track and the LTS tracks. | 
| [CVE-2020-25112](https://nvd.nist.gov/vuln/detail/CVE-2020-25112) | No |  | 
| [CVE-2020-25111](https://nvd.nist.gov/vuln/detail/CVE-2020-25111) | No |  | 
| [CVE-2020-25110](https://nvd.nist.gov/vuln/detail/CVE-2020-25110) | No |  | 
| [CVE-2020-25109](https://nvd.nist.gov/vuln/detail/CVE-2020-25109) | No |  | 
| [CVE-2020-25108](https://nvd.nist.gov/vuln/detail/CVE-2020-25108) | No |  | 
| [CVE-2020-25107](https://nvd.nist.gov/vuln/detail/CVE-2020-25107) | No |  | 
| [CVE-2020-25066](https://nvd.nist.gov/vuln/detail/CVE-2020-25066) | No |  | 
| [CVE-2020-24383](https://nvd.nist.gov/vuln/detail/CVE-2020-24383) | No |  | 
| [CVE-2020-24341](https://nvd.nist.gov/vuln/detail/CVE-2020-24341) | No |  | 
| [CVE-2020-24340](https://nvd.nist.gov/vuln/detail/CVE-2020-24340) | No |  | 
| [CVE-2020-24339](https://nvd.nist.gov/vuln/detail/CVE-2020-24339) | No |  | 
| [CVE-2020-24338](https://nvd.nist.gov/vuln/detail/CVE-2020-24338) | No |  | 
| [CVE-2020-24337](https://nvd.nist.gov/vuln/detail/CVE-2020-24337) | No |  | 
| [CVE-2020-24336](https://nvd.nist.gov/vuln/detail/CVE-2020-24336) | No |  | 
| [CVE-2020-24335](https://nvd.nist.gov/vuln/detail/CVE-2020-24335) | No |  | 
| [CVE-2020-24334](https://nvd.nist.gov/vuln/detail/CVE-2020-24334) | No |  | 
| [CVE-2020-17470](https://nvd.nist.gov/vuln/detail/CVE-2020-17470) | No |  | 
| [CVE-2020-17469](https://nvd.nist.gov/vuln/detail/CVE-2020-17469) | No |  | 
| [CVE-2020-17468](https://nvd.nist.gov/vuln/detail/CVE-2020-17468) | No |  | 
| [CVE-2020-17467](https://nvd.nist.gov/vuln/detail/CVE-2020-17467) | No |  | 
| [CVE-2020-17445](https://nvd.nist.gov/vuln/detail/CVE-2020-17445) | No |  | 
| [CVE-2020-17444](https://nvd.nist.gov/vuln/detail/CVE-2020-17444) | No |  | 
| [CVE-2020-17443](https://nvd.nist.gov/vuln/detail/CVE-2020-17443) | No |  | 
| [CVE-2020-17442](https://nvd.nist.gov/vuln/detail/CVE-2020-17442) | No |  | 
| [CVE-2020-17441](https://nvd.nist.gov/vuln/detail/CVE-2020-17441) | No |  | 
| [CVE-2020-17440](https://nvd.nist.gov/vuln/detail/CVE-2020-17440) | No |  | 
| [CVE-2020-17439](https://nvd.nist.gov/vuln/detail/CVE-2020-17439) | No |  | 
| [CVE-2020-17438](https://nvd.nist.gov/vuln/detail/CVE-2020-17438) | No |  | 
| [CVE-2020-17437](https://nvd.nist.gov/vuln/detail/CVE-2020-17437) | No |  | 
| [CVE-2020-17049](https://www.cve.org/CVERecord?id=CVE-2020-17049) | No | This vulnerability is exploitable when Microsoft Kerberos services are used, which is a functionality that is not supported in AXIS OS devices. | 
| [CVE-2020-15795](https://nvd.nist.gov/vuln/detail/CVE-2020-15795) | No |  | 
| [CVE-2020-14871](https://nvd.nist.gov/vuln/detail/CVE-2020-14871) | No |  | 
| [CVE-2020-13988](https://nvd.nist.gov/vuln/detail/CVE-2020-13988) | No |  | 
| [CVE-2020-13987](https://nvd.nist.gov/vuln/detail/CVE-2020-13987) | No |  | 
| [CVE-2020-13986](https://nvd.nist.gov/vuln/detail/CVE-2020-13986) | No |  | 
| [CVE-2020-13985](https://nvd.nist.gov/vuln/detail/CVE-2020-13985) | No |  | 
| [CVE-2020-13984](https://nvd.nist.gov/vuln/detail/CVE-2020-13984) | No |  | 
| [CVE-2020-13950](https://nvd.nist.gov/vuln/detail/CVE-2020-13950) | Yes | The vulnerability has been patched on the AXIS OS active track and the LTS tracks. Updating is recommended. | 
| [CVE-2020-13938](https://nvd.nist.gov/vuln/detail/CVE-2020-13938) | No |  | 
| [CVE-2020-13848](https://cve.report/CVE-2020-13848) | Yes | Concerned customers can temporarily disable the parameter Network.UPnP.Enabled in Plain config to mitigate this. The vulnerability has been patched on the AXIS OS active track and the LTS tracks. | 
| [CVE-2020-12695](https://nvd.nist.gov/vuln/detail/CVE-2020-12695) | No |  | 
| [CVE-2020-11993](https://nvd.nist.gov/vuln/detail/CVE-2020-11993) | No |  | 
| [CVE-2020-11984](https://nvd.nist.gov/vuln/detail/CVE-2020-11984) | No |  | 
| [CVE-2020-11899](https://nvd.nist.gov/vuln/detail/CVE-2020-11899) | No |  | 
| [CVE-2020-11898](https://nvd.nist.gov/vuln/detail/CVE-2020-11898) | No |  | 
| [CVE-2020-11897](https://nvd.nist.gov/vuln/detail/CVE-2020-11897) | No |  | 
| [CVE-2020-11896](https://nvd.nist.gov/vuln/detail/CVE-2020-11896) | No |  | 
| [CVE-2020-11023](https://www.cve.org/CVERecord?id=CVE-2020-11023) | No | Axis deems the severity and impact of this vulnerability as low as it requires the attacker to be authenticated and no known exploits are available to negatively affect the Axis product. | 
| [CVE-2020-11022](https://www.cve.org/CVERecord?id=CVE-2020-11022) | No | Axis deems the severity and impact of this vulnerability as low as it requires the attacker to be authenticated and no known exploits are available to negatively affect the Axis product. | 
| [CVE-2020-10713](https://nvd.nist.gov/vuln/detail/CVE-2020-10713) | No |  | 
| [CVE-2020-9770](https://nvd.nist.gov/vuln/detail/CVE-2020-9770) | Yes | Affects Axis body worn and wireless devices and will be patched in a timely manner on the AXIS OS active track and the LTS tracks. | 
| [CVE-2020-9490](https://nvd.nist.gov/vuln/detail/CVE-2020-9490) | Yes | Products with AXIS OS 10.0 or lower are not affected. For newer AXIS OS versions, the vulnerability has been patched on the AXIS OS active track. Updating is recommended. | 
| [CVE-2020-9308](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-9308/) | Yes | AXIS OS devices use a different (not affected) version of libarchive or affected functions require root access to be exploited and when root access is gained, full control over the device is already established. | 
| [CVE-2020-7461](https://nvd.nist.gov/vuln/detail/CVE-2020-7461) | No |  | 
| [CVE-2020-3120](https://nvd.nist.gov/vuln/detail/CVE-2020-3120) | No |  | 
| [CVE-2020-3119](https://nvd.nist.gov/vuln/detail/CVE-2020-3119) | No |  | 
| [CVE-2020-3118](https://nvd.nist.gov/vuln/detail/CVE-2020-3118) | No |  | 
| [CVE-2020-3111](https://nvd.nist.gov/vuln/detail/CVE-2020-3111) | No |  | 
| [CVE-2020-3110](https://nvd.nist.gov/vuln/detail/CVE-2020-3110) | No |  | 
| [CVE-2020-1971](https://nvd.nist.gov/vuln/detail/CVE-2020-1971) | Yes | The vulnerability has been patched on the AXIS OS active track and the LTS tracks. Updating is recommended. | 
| [CVE-2020-1967](https://nvd.nist.gov/vuln/detail/CVE-2020-1967) | Yes | The vulnerability has been patched on the AXIS OS active track and the LTS tracks. Updating is recommended. | 
| [CVE-2020-1938](https://nvd.nist.gov/vuln/detail/CVE-2020-1938) | No |  | 
| [CVE-2020-1934](https://nvd.nist.gov/vuln/detail/CVE-2020-1934) | No |  | 
| [CVE-2020-1927](https://nvd.nist.gov/vuln/detail/CVE-2020-1927) | Yes | The vulnerability has been patched on the AXIS OS active track and the LTS tracks. Updating is recommended. | 
| [CVE-2020-1472](https://www.cve.org/CVERecord?id=CVE-2020-1472) | No | This vulnerability is exploited when the configuration property "server schannel" is enabled. This is not supported in AXIS OS devices, instead default settings are used which are deemed secure. | 

#### CVE 2019

| CVE number | Affected | Security advisory / Vulnerability summary | 
| [CVE-2019-1000020](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-1000020/) | No | AXIS OS devices use a different (not affected) version of libarchive or affected functions require root access to be exploited and when root access is gained, full control over the device is already established. | 
| [CVE-2019-1000019](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-1000019/) | No | AXIS OS devices use a different (not affected) version of libarchive or affected functions require root access to be exploited and when root access is gained, full control over the device is already established. | 
| [CVE-2019-19221](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-19221/) | No | AXIS OS devices use a different (not affected) version of libarchive or affected functions require root access to be exploited and when root access is gained, full control over the device is already established. | 
| [CVE-2019-17567](https://nvd.nist.gov/vuln/detail/CVE-2019-17567) | Yes | Affects Axis door stations/intercoms. The vulnerability has been patched. Updating is recommended. | 
| [CVE-2019-15916](https://cve.report/CVE-2019-15916) | Yes | Affects LTS 2016. The vulnerability has been patched. Updating is recommended. | 
| [CVE-2019-12450](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-12450) | Yes | Affects LTS 2018 and LTS 2016. The vulnerability has been patched. | 
| [CVE-2019-11358](https://www.cve.org/CVERecord?id=CVE-2019-11358) | Yes | Axis deems the severity and impact of this vulnerability as low as it requires the attacker to be authenticated and no known exploits are available to negatively affect the Axis product. | 
| [CVE-2019-11135](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11135) | No |  | 
| [CVE-2019-11091](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11091) | No |  | 
| [CVE-2019-10744](https://nvd.nist.gov/vuln/detail/CVE-2019-10744) | No |  | 
| [CVE-2019-9517](https://www.cve.org/CVERecord?id=CVE-2019-9517) | Yes | The vulnerability has been patched on the AXIS OS active track and the LTS tracks. Updating is recommended. | 
| [CVE-2019-1563](https://www.cve.org/CVERecord?id=CVE-2019-1563) | No |  | 
| [CVE-2019-1559](https://www.cve.org/CVERecord?id=CVE-2019-1559) | No |  | 
| [CVE-2019-1551](https://nvd.nist.gov/vuln/detail/CVE-2019-1551) | No |  | 
| [CVE-2019-1547](https://www.cve.org/CVERecord?id=CVE-2019-1547) | No |  | 
| [CVE-2019-1125](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-1125) | No |  | 

#### CVE 2018

| CVE number | Affected | Security advisory / Vulnerability summary | 
| [CVE-2018-1000880](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1000880) | No | AXIS OS devices use a different (not affected) version of libarchive or affected functions require root access to be exploited and when root access is gained, full control over the device is already established. | 
| [CVE-2018-1000879](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1000879) | No | AXIS OS devices use a different (not affected) version of libarchive or affected functions require root access to be exploited and when root access is gained, full control over the device is already established. | 
| [CVE-2018-1000878](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1000878)  | No | AXIS OS devices use a different (not affected) version of libarchive or affected functions require root access to be exploited and when root access is gained, full control over the device is already established. | 
| [CVE-2018-1000877](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1000877)  | No | AXIS OS devices use a different (not affected) version of libarchive or affected functions require root access to be exploited and when root access is gained, full control over the device is already established. | 
| [CVE-2018-25032](https://www.cve.org/CVERecord?id=CVE-2018-25032) | Yes | The vulnerability has been patched on the AXIS OS active track and the LTS tracks. | 
| [CVE-2018-12207](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12207) | No |  | 
| [CVE-2018-12130](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12130) | No |  | 
| [CVE-2018-12127](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12127) | No |  | 
| [CVE-2018-12126](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12126) | No |  | 
| [CVE-2018-10938](https://www.cve.org/CVERecord?id=CVE-2018-10938)  | No | Axis OS devices do not utilize CONFIG\_NETLABEL set. Additionally, the vulnerability was fixed in 4.9.125 and AXIS OS devices uses 4.9.206. | 
| [CVE-2018-3646](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646) | No |  | 
| [CVE-2018-3639](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3639) | No |  | 
| [CVE-2018-3620](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620) | No |  | 
| [CVE-2018-3615](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615) | No |  | 
| [CVE-2018-1285](https://www.cve.org/CVERecord?id=CVE-2018-1285) | No | Not affected since Apache log4net is not used in AXIS OS. | 

#### CVE 2017

| CVE number | Affected | Security advisory / Vulnerability summary | 
| [CVE-2017-9833](https://www.cve.org/CVERecord?id=CVE-2017-9833) | No | The affected 3 <sup>rd</sup> party component /cgi-bin/wapopen is not used in Axis products below version 5.70 that utilize the BOA webserver. Furthermore, input validation in our APIs are used which would prevent injections. Axis products with 5.70 and higher utilize the Apache webserver where these vulnerabilities do not apply as the BOA webserver has been removed. | 
| [CVE-2017-5754](https://www.axis.com/files/faq/advisory_meltdown_spectre.pdf) | No |  | 
| [CVE-2017-5753](https://www.axis.com/files/faq/advisory_meltdown_spectre.pdf) | Yes | Axis has delivered patches to the affected products. | 
| [CVE-2017-5715](https://www.axis.com/files/faq/advisory_meltdown_spectre.pdf) | Yes | Axis has delivered patches to the affected products. | 

#### CVE 2016

| CVE number | Affected | Security advisory / Vulnerability summary | 
| [CVE-2016-20009](https://nvd.nist.gov/vuln/detail/CVE-2016-20009) | No |  | 
| [CVE-2016-8863](https://www.axis.com/files/faq/Advisory_libupnp_CVE-2016-6255_CVE-2016-8863.pdf) | Yes | Axis has delivered patches to the affected products. | 
| [CVE-2016-7409](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-7409) | No |  | 
| [CVE-2016-7408](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-7408) | No |  | 
| [CVE-2016-7407](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-7407) | No |  | 
| [CVE-2016-7406](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-7406) | No |  | 
| [CVE-2016-6255](https://www.axis.com/files/faq/Advisory_libupnp_CVE-2016-6255_CVE-2016-8863.pdf) | Yes | Axis has delivered patches to the affected products. | 
| [CVE-2016-2183](https://nvd.nist.gov/vuln/detail/CVE-2016-2183) | Yes | The vulnerability has been patched on the active track and the LTS tracks. | 
| [CVE-2016-2147](https://www.axis.com/files/faq/Advisory_dhcp_CVE-2016-2147_CVE-2016-2148.pdf) | Yes | Axis has delivered patches to the affected products. | 
| [CVE-2016-2148](https://www.axis.com/files/faq/Advisory_dhcp_CVE-2016-2147_CVE-2016-2148.pdf) | Yes | Axis has delivered patches to the affected products. | 

#### CVE 2015

| CVE number | Affected | Security advisory / Vulnerability summary | 
| [CVE-2015-7547](https://www.axis.com/files/faq/CVE-2015-7547-glibc_getaddrinfo.pdf) | Yes | Axis has delivered patches to the affected products. | 
| [CVE-2015-0235](https://www.axis.com/files/faq/CVE-2015-0235-GHost-gethostbyname.pdf) | Yes | Axis has delivered patches to the affected products. | 
| [CVE-2015-0204](https://www.cve.org/CVERecord?id=CVE-2015-0204) | No |  | 

#### CVE 2014-1999

| CVE number | Affected | Security advisory / Vulnerability summary | 
| [CVE-2014-6271](https://www.axis.com/files/conformity/CVE-2014-6271-Shellshock-Axis.pdf) | No |  | 
| [CVE-2014-3566](https://www.axis.com/files/faq/CVE-2014-3566-SSL_Poodle.pdf) | Yes | Axis has delivered patches to the affected products. | 
| [CVE-2014-0224](https://www.axis.com/files/faq/CVE-2014-0224-OPENSSL-MITM.pdf) | Yes | Axis has delivered patches to the affected products. | 
| [CVE-2014-0160](https://www.axis.com/files/faq/Axis_no_HeartbleedBug_140411.pdf) | No |  | 
| [CVE-2013-0156](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-0156) | No | AXIS OS devices do not use Ruby on Rails. | 
| [CVE-2011-3389](https://www.cve.org/CVERecord?id=CVE-2011-3389) | No |  | 
| [CVE-2009-1955](https://nvd.nist.gov/vuln/detail/CVE-2009-1955) | No |  | 
| [CVE-2007-6750](https://nvd.nist.gov/vuln/detail/CVE-2007-6750) | No |  | 
| [CVE-2007-6514](https://nvd.nist.gov/vuln/detail/CVE-2007-6514) | No |  | 
| [CVE-2007-1743](https://nvd.nist.gov/vuln/detail/CVE-2007-1743) | No | AXIS OS devices are not affected due to their locked-down filesystem permissions. | 
| [CVE-2007-1742](https://nvd.nist.gov/vuln/detail/CVE-2007-1742) | No | AXIS OS devices are not affected due to their locked-down filesystem permissions. | 
| [CVE-2007-1741](https://nvd.nist.gov/vuln/detail/CVE-2007-1741) | No | AXIS OS devices are not affected due to their locked-down filesystem permissions. | 
| [CVE-2006-20001](https://www.cve.org/CVERecord?id=CVE-2006-20001) | No | AXIS OS devices do not use the mod\_dav module. | 
| [CVE-2005-1797](https://nvd.nist.gov/vuln/detail/CVE-2005-1797) | No |  | 
| [CVE-2005-0088](https://nvd.nist.gov/vuln/detail/CVE-2005-0088) | No |  | 
| [CVE-2002-20001](https://www.cve.org/CVERecord?id=CVE-2002-20001) | Yes | This is a known limitation of asymmetric cryptography and is not considered relevant by Axis since the web server in Axis devices supports only 20 concurrent connections at a time, which renders the attack vector ineffective. It’s recommended to use symmetric cryptography instead when connecting to Axis devices. | 
| [CVE-2002-0185](https://nvd.nist.gov/vuln/detail/CVE-2002-0185) | No |  | 
| [CVE-1999-1412](https://nvd.nist.gov/vuln/detail/CVE-1999-1412) | No |  | 
| [CVE-1999-1237](https://nvd.nist.gov/vuln/detail/CVE-1999-1237) | No |  | 

## Other vulnerabilities

This section addresses vulnerabilities and/or incidents that, while not classified as CVEs, have been investigated by Axis.

| Title | Details | 
| [NPM Supply Chain Attack](https://www.axis.com/dam/public/eb/68/8c/npm-supply-chain-attackpdf-en-US-503396.pdf) | Statement for the NPM Supply Chain Attack. | 
| [ONVIF / WS Discovery DDoS Attacks](https://www.axis.com/files/faq/Advisory_WS_Discovery_DDOS.pdf) | Statement for ONVIF-capable devices vulnerable for DDoS exploit. | 
| [Cross-Site Request Forgery (CSRF)](https://www.axis.com/files/faq/Advisory_Cross-Site_Request_Forgery.pdf) | Statement for Cross-Site Request Forgery in Axis products. | 
| [Exposed Axis products and their risks](https://www.axis.com/dam/public/7d/4b/3a/advisory-exposed-devices-en-US-432118.pdf) | Statement for exposed Axis products and their risks. |
