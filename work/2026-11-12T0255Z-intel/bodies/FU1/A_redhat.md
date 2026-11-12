---
title: CVE-2026-119618
url: https://access.redhat.com/security/cve/CVE-2026-119618
hostname: redhat.com
description: CVE Details App
sitename: access.redhat.com
date: "2026-11-11"
fingerprint: f738f550fd200041
---
# CVE-2026-119618

## Description

A flaw was found in the mod\_http2 module of the Apache HTTP Server (httpd), the standard web server used across Red Hat Enterprise Linux and other products. HTTP/2 allows a client to send many requests at the same time over a single connection, and the module handles these concurrent requests using multiple threads. Due to a thread-safety flaw, one thread can modify memory that belongs to another thread, corrupting the server's internal memory. A remote attacker who can reach the web server could exploit this flaw to execute arbitrary commands on the server without any authentication, potentially leading to a complete takeover of the affected system, unauthorized access to sensitive data, and service disruption. Only servers that have HTTP/2 enabled are affected; servers configured to serve only HTTP/1.1 are not vulnerable.

## Statement

The Red Hat Product Security team has assessed the severity of this vulnerability as Critical. It allows unauthenticated remote code execution, and public research has demonstrated a reliable exploit against a default-configured server with the mod\_http2 module enabled. Successful exploitation allows an attacker to execute arbitrary commands, gain full control of the server process, and access or modify sensitive information.

The vulnerability's root cause is a thread-safety flaw in the mod\_http2 module's handling of concurrent HTTP/2 requests: a worker thread writes into memory owned by the connection thread through a shared, lock-free allocator. This issue affects servers with HTTP/2 (h2 or h2c) enabled via the Protocols directive; servers serving only HTTP/1.1 are not affected.

Because exploitation depends on HTTP/2 stream workers sharing an allocator with the connection, the severity of this flaw varies across Red Hat products. The mod\_http2 packages shipped in Red Hat Enterprise Linux 9 and Red Hat Enterprise Linux 10 allocate each HTTP/2 stream from a separate allocator, which substantially increases the complexity of exploiting the flaw. The severity for Red Hat Enterprise Linux 9 and Red Hat Enterprise Linux 10 is therefore rated Important rather than Critical. Versions of mod\_http2 prior to 2.0.8 do not contain the affected code, and Red Hat Enterprise Linux 8 and earlier are not affected. Refer to the affected packages table for the severity assigned to each Red Hat product.

## Common Vulnerability Scoring System (CVSS) Score Details

#### Info alert:Important note

CVSS scores for open source components depend on vendor-specific factors (e.g. version or build chain). Therefore, Red Hat's score and impact rating can be different from NVD and other vendors. Red Hat remains the authoritative [CVE Naming Authority (CNA)](https://www.cve.org/ProgramOrganization/CNAs) source for its products and services (see [Red Hat classifications](https://access.redhat.com/security/updates/classification#cvss)).

### CVSS v3 Score Breakdown

|  | Red Hat | NVD | cve.org | 
|---|---|---|---|
| Base Score | 9.8 | N/A | N/A | 
| Attack Vector | Network | N/A | N/A | 
| Attack Complexity | Low | N/A | N/A | 
| Privileges Required | None | N/A | N/A | 
| User Interaction | None | N/A | N/A | 
| Scope | Unchanged | N/A | N/A | 
| Confidentiality | High | N/A | N/A | 
| Integrity Impact | High | N/A | N/A | 
| Availability Impact | High | N/A | N/A | 

### Vector

Red Hat: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H

## Understanding the Weakness (CWE)

### Availability

Technical Impact: DoS: Crash, Exit, or Restart; DoS: Resource Consumption (CPU); DoS: Resource Consumption (Memory)

An attacker could provide unexpected values and cause a program crash or arbitrary control of resource allocation, leading to excessive consumption of resources such as memory and CPU.

### Confidentiality

Technical Impact: Read Memory; Read Files or Directories

An attacker could read confidential data if they are able to control resource references.

### Integrity,Confidentiality,Availability

Technical Impact: Modify Memory; Execute Unauthorized Code or Commands

An attacker could use malicious input to modify data or possibly alter control flow in unexpected ways, including arbitrary command execution.

## Acknowledgements

Red Hat would like to thank Anthony Weems (Google Cloud Vulnerability Research) and Simon Scannell (Google Cloud Vulnerability Research) for reporting this issue.

## Frequently Asked Questions

Not sure what something means? Check out our [Security Glossary](https://access.redhat.com/security/glossary).

Want to get errata notifications? [Sign up here](https://www.redhat.com/wapps/ugc/protected/notif.html?extIdCarryOver=true&sc_cid=701f2000001Css5AAC).
