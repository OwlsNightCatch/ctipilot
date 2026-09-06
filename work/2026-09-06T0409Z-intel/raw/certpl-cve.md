# extract: served via trafilatura-direct
---
title: Vulnerabilities in Mikrotik RouterOS software
url: https://cert.pl/en/posts/2026/09/mikrotik-routeros-cve/
hostname: cert.pl
description: CERT Polska has found 6 vulnerabilities (from CVE-2026-67276 to CVE-2026-67279, CVE-2026-67281 and CVE-2026-86060) in Mikrotik RouterOS software.
sitename: cert.pl
date: "2026-09-05"
---
| **CVE ID** | [CVE-2026-67276](https://www.cve.org/CVERecord?id=CVE-2026-67276) | 
| **Publication date** | 05 September 2026 | 
| **Vendor** | Mikrotik | 
| **Product** | RouterOS | 
| **Vulnerable versions** | From 7.24 below 7.24.2 From 7.0.0 below 7.23.4 From 6.0.0 below 6.49.21 | 
| **Vulnerability type (CWE)** | Improper verification of cryptographic signature ( [CWE-347](https://cwe.mitre.org/data/definitions/347.html) ) | 
| **Report source** | Own research | 
| **CVE ID** | [CVE-2026-67277](https://www.cve.org/CVERecord?id=CVE-2026-67277) | 
| **Publication date** | 05 September 2026 | 
| **Vendor** | Mikrotik | 
| **Product** | RouterOS | 
| **Vulnerable versions** | From 7.24 below 7.24.2 From 7.0.0 below 7.23.4 From 6.0.0 below 6.49.21 | 
| **Vulnerability type (CWE)** | Missing authentication for critical function ( [CWE-306](https://cwe.mitre.org/data/definitions/306.html) ) | 
| **Report source** | Own research | 
| **CVE ID** | [CVE-2026-67278](https://www.cve.org/CVERecord?id=CVE-2026-67278) | 
| **Publication date** | 05 September 2026 | 
| **Vendor** | Mikrotik | 
| **Product** | RouterOS | 
| **Vulnerable versions** | From 7.24 below 7.24.2 From 7.0.0 below 7.23.4 From 6.0.0 below 6.49.21 | 
| **Vulnerability type (CWE)** | Improper verification of cryptographic signature ( [CWE-347](https://cwe.mitre.org/data/definitions/347.html) ) | 
| **Report source** | Own research | 
| **CVE ID** | [CVE-2026-67279](https://www.cve.org/CVERecord?id=CVE-2026-67279) | 
| **Publication date** | 05 September 2026 | 
| **Vendor** | Mikrotik | 
| **Product** | RouterOS | 
| **Vulnerable versions** | From 7.24 below 7.24.2 From 7.0.0 below 7.23.4 From 6.0.0 below 6.49.21 | 
| **Vulnerability type (CWE)** | Improper enforcement of behavioral workflow ( [CWE-841](https://cwe.mitre.org/data/definitions/841.html) ) | 
| **Report source** | Own research | 
| **CVE ID** | [CVE-2026-67281](https://www.cve.org/CVERecord?id=CVE-2026-67281) | 
| **Publication date** | 05 September 2026 | 
| **Vendor** | Mikrotik | 
| **Product** | RouterOS | 
| **Vulnerable versions** | From 7.24 below 7.24.2 From 7.0.0 below 7.23.4 From 6.0.0 below 6.49.21 | 
| **Vulnerability type (CWE)** | Access of uninitialized pointer ( [CWE-824](https://cwe.mitre.org/data/definitions/824.html) ) | 
| **Report source** | Own research | 
| **CVE ID** | [CVE-2026-86060](https://www.cve.org/CVERecord?id=CVE-2026-86060) | 
| **Publication date** | 05 September 2026 | 
| **Vendor** | Mikrotik | 
| **Product** | RouterOS | 
| **Vulnerable versions** | From 7.24 below 7.24.2 From 7.0.0 below 7.23.4 From 6.0.0 below 6.49.21 | 
| **Vulnerability type (CWE)** | Improper neutralization of argument delimiters in a command ('argument injection') ( [CWE-88](https://cwe.mitre.org/data/definitions/88.html) ) | 
| **Report source** | Own research | 

## Description

During its own research, CERT Polska discovered vulnerabilities in MikroTik RouterOS software and participated in coordinating their disclosure. Details on how these vulnerabilities were found, along with other related information, are available in [our separate article](https://cert.pl/en/posts/2026/09/vulnerabilities-in-mikrotik-routeros-actively-exploited/).

The vulnerability [CVE-2026-67276](https://www.cve.org/CVERecord?id=CVE-2026-67276): RouterOS does not compare the complete RSA public key when matching an SSH authentication request to an authorized user key, checking the key type and modulus but omitting the exponent. Because signature verification uses the client-supplied key, an attacker knowing an authorized RSA modulus can supply a key with exponent one, forge a valid signature, and open an SSH command channel as the target user without the private key.

The vulnerability [CVE-2026-67277](https://www.cve.org/CVERecord?id=CVE-2026-67277): RouterOS accepts a "related" btest connection before the corresponding primary session has completed authentication. An unauthenticated client can use this state to start an IPv4 UDP test. With "random-data=false", the sender transmits an uninitialized tail from a kernel packet buffer. A separate unchecked, inverted packet-size interval causes unsigned integer underflow, anomalously large fragmented output, and can restart the RouterOS kernel.

The vulnerability [CVE-2026-67278](https://www.cve.org/CVERecord?id=CVE-2026-67278): MikroTik RouterOS accepts malformed RSA/PKCS#1 v1.5 signatures during X.509 validation. Because its trust store includes an e=3 root CA, an attacker controlling or redirecting an outbound RouterOS TLS connection can use the root’s public certificate - without its private key - to forge a trusted intermediate and issue certificates for arbitrary hostnames, enabling TLS server impersonation.

The vulnerability [CVE-2026-67279](https://www.cve.org/CVERecord?id=CVE-2026-67279): RouterOS SSH enters the connection protocol after a client-requested rekey even though user authentication was never attempted, allowing an unauthenticated client to open a session channel and send an exec request. On affected builds the server dispatches the command, enabling unauthenticated creation, overwrite, and reconstruction of files in the RouterOS managed file namespace, including support files containing configuration and diagnostic data.

The vulnerability [CVE-2026-67281](https://www.cve.org/CVERecord?id=CVE-2026-67281): RouterOS WebFig contains an unauthenticated file-read vulnerability in the `/jsproxy` path where a newly allocated session retains a stale uninitialized principal pointer used for file authorization. An unauthenticated attacker can prepare the allocator so that the file-serving path dereferences this pointer with sufficient rights, then supply parent-directory components in an encrypted URI to escape the WebFig file namespace and disclose root-owned files, including configuration stores containing credentials.

The vulnerability [CVE-2026-86060](https://www.cve.org/CVERecord?id=CVE-2026-86060): RouterOS contains an argument-handling flaw in the SSH login path involving usernames that begin with a prohibited character, allowing for the trusted RouterOS policy mask to be changed, leading to privilege escalation. Exploitation requires an unauthenticated SSH session to reach the RouterOS login helper.

These issues were fixed in versions: 6.49.21 (Long-term), 7.23.4 (Long-term) and 7.24.2 (Stable).

More about the coordinated vulnerability disclosure process at CERT Polska can be found at

[https://cert.pl/en/cvd/](https://cert.pl/en/cvd/).
