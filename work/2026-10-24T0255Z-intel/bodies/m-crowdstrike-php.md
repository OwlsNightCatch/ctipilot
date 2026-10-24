---
title: "PHP2Shell: Obstacles to Weaponizing Likely Constrain Immediate Exploitation"
url: https://www.crowdstrike.com/en-us/blog/obstacles-to-weaponizing-php2shell-likely-constrain-exploitation/
hostname: crowdstrike.com
description: Threat actors have not yet exploited PHP2Shell, but the speed with which they attempted to weaponize the vulns highlights how swiftly attackers adopt new exploits.
sitename: CrowdStrike
date: "2026-10-23"
fingerprint: b0b21581aea2958b
---
On October 21, 2026, [PHP disclosed two critical severity vulnerabilities](https://www.crowdstrike.com/en-us/blog/crowdstrike-protects-customers-from-php-rce-zero-days/) (now tracked as CVE-2026-109618 and CVE-2026-109619 and dubbed PHP2Shell) affecting multiple PHP versions. These vulnerabilities, which potentially allow an unauthenticated threat actor to achieve remote code execution (RCE) under certain conditions, are exploitable in products running vulnerable PHP versions.

Due to their severity and the fact that PHP powers approximately 70% of all websites on the internet,<sup>1</sup> including WordPress, these vulnerabilities have received widespread media and industry attention prior to and immediately after disclosure. Industry sources have disclosed proof-of-concept (POC) code related to these vulnerabilities or other alleged PHP vulnerabilities. Many of the ones CrowdStrike Counter Adversary Operations has analyzed are crash POCs that only prove a vulnerability exists; converting them to a reliable POC exploit capable of reliably achieving RCE is not trivial or guaranteed.

To exploit these vulnerabilities, attackers must adapt the POC exploit for the specific PHP version and application (e.g., WordPress). This adaptation presents a meaningful barrier to would-be threat actors, as it requires the exploit developer to know and use the same versions of Docker containers, packages, and other elements used by targeted applications.

At this time, CrowdStrike Counter Adversary Operations has not observed successful exploitation of these vulnerabilities in the wild or within our honeypot environments. Additionally, we have not identified any fully weaponized exploit, or any POC exploit, sufficient to widely achieve applicable exploitation. Despite the attention PHP2Shell is receiving, only testing, probing, and unsuccessful exploitation attempts have been observed at this time.

Threat actors have several viable alternative vulnerabilities capable of achieving unauthenticated RCE against many applications that use PHP reliably and at scale. Many opportunistic threat actors may currently favor proven effective exploits and other attack vectors as they are not able to successfully leverage PHP2Shell in the near term.

## CVE-2026-109618 and CVE-2026-109619 Overview

On October 21, 2026, PHP disclosed CVE-2026-109618 and CVE-2026-109619, which affect the following versions:

- Earlier than 8.2.35
- Earlier than 8.3.36
- Earlier than 8.4.27
- Earlier than 8.5.12

Preliminary analysis by industry sources and the vendor suggests many older versions, including end-of-life PHP versions, are also impacted by these vulnerabilities and may receive limited patches to fix them.

CrowdStrike Counter Adversary Operations reproduced a POC exploit achieving RCE with the privileges of the running `mod_php` or the PHP-FPM worker processes, both of which should be unprivileged in most cases, as dictated by the least privileges principle.

### Understanding PHP Workers and Request Handling

A PHP worker is a long-running process that executes PHP requests. Instead of starting a new PHP interpreter for every HTTP request, the server reuses workers to reduce startup overhead. Under normal conditions, request-specific data is initialized when a request begins and released when it ends, while process-level state persists for the worker's lifetime. Consequently, two unrelated requests may be handled sequentially by the same worker. This distinction is critical for cross-request vulnerabilities: Memory left in an inconsistent state by one request may affect a subsequent request only if the request reaches the same persistent worker.

`mod_php` and PHP-FPM are the two most common PHP deployment and web server integration models. They use different server APIs (SAPIs), which define how the PHP engine receives and processes web requests.

With `mod_php`, PHP is loaded directly into Apache as a module, and PHP code executes within Apache worker processes.

With PHP-FPM, PHP runs as a separate service composed of a master process and a pool of workers. A web server such as Apache or Nginx forwards requests to these workers using the FastCGI protocol, typically through a Unix socket or a TCP connection.

In both models, workers are reused across multiple requests. This reuse is relevant to vulnerabilities that leave a corrupted or stale state behind for subsequent requests.

During technical analysis of CVE-2026-109618 and CVE-2026-109619, CrowdStrike Counter Adversary Operations identified three distinct flaws that, if exploited, can enable RCE.

CVE-2026-109618 aligns with the partial hashTable insertion flaw, and CVE-2026-109619 aligns with the persistent serialization-context use-after-free and session-global use-after-free flaws.

### CVE-2026-109618 Partial HashTable Insertion

PHP uses `HashTable` structures internally to store collections of key-value pairs, including arrays and HTTP request variables. Each stored entry is represented by a `bucket`, which contains the value together with information such as the value’s key and type. PHP uses the `HashTable`’s entry count to determine which `buckets` contain valid data and must be processed or released.

The vulnerability stems from a memory corruption during HTTP request-variable parsing. If a memory allocation fails while PHP is adding a new `HashTable` entry, the entry count may be updated before the corresponding bucket is fully initialized. During request shutdown, PHP may then treat this incomplete `bucket` as valid and attempt to access or release invalid data. This can result in an invalid memory access, memory corruption, or termination of the PHP process, potentially leading to execution of arbitrary code.

### CVE-2026-109619: Persistent Serialization-Context Use-After-Free

PHP’s `serialize()` function converts a PHP value, such as an array or object, into an encoded string that can be stored or transmitted. The corresponding `unserialize()` function reconstructs the original PHP value from that string. While these operations are running, PHP maintains an internal serialization context to track objects, references, and recursive data structures.

`zend_bailout()`, PHP’s internal emergency mechanism for stopping execution after a fatal error, immediately transfers control to a recovery point, so normal function returns and cleanup code may be skipped unless they are handled explicitly.

PHP contains a cross-request use-after-free vulnerability in its serialization-context handling. If a fatal error causes `zend_bailout()` to interrupt `serialize()` or `unserialize()`, PHP may leave the internal context pointing to memory owned by the current request. That memory is released when the request ends, but the PHP worker may remain alive and retain the stale pointer. A later request handled by the same worker may then access or modify the released memory. Based on the configuration, successful exploitation may allow an attacker to disclose memory, crash the PHP worker, or execute arbitrary code.

### CVE-2026-109619: Session-Global Use-After-Free

PHP’s session upload-progress feature allows an application to monitor a file upload’s progress. When enabled, PHP detects a specific field in a multipart or form-data request and creates a temporary progress record in the user’s session before the PHP script begins executing. As upload data arrives, PHP periodically opens the session, updates the number of processed bytes, writes the session data, and releases the session lock. When the upload finishes or is cancelled, PHP removes the progress record and clears the related internal state.

PHP contains a cross-request use-after-free vulnerability in the session upload-progress life cycle. If a fatal error interrupts multipart request processing before upload-progress cleanup finishes, PHP may skip the code that normally closes the session and clears its internal state. The current request’s memory is then released, but the persistent PHP worker may still retain pointers to that memory. A later request handled by the same worker may access or modify the released memory.

Depending on the configuration, successful exploitation may cause memory disclosure or corruption, crash the PHP worker, leave a session lock permanently held, or make the affected service unavailable.

## Assessment

Exploit developers are unlikely to create a single universal exploit that works reliably across all affected PHP deployments. The creation of a POC exploit capable of reliable remote exploitation is feasible, however, against specific deployment profiles, such as a fixed Docker image or a known combination of PHP, libc, SAPI, and web application versions. For such cases, an attacker can calibrate exploit offsets and heap grooming in advance, producing an exploit that reliably applies to any system running that same unmodified package or image release.

In the short to long term, advanced threat actors will likely attempt to exploit this vulnerability against high-value targets where alternative exploitation methods are less feasible. However, if a public exploit overcoming the aforementioned exploitation challenges becomes available for a widely used PHP deployment, many additional threat actors will almost certainly seek to leverage it immediately.

The widespread media and industry attention surrounding this vulnerability will almost certainly incentivize both threat actors and security researchers to discover additional PHP vulnerabilities in the short to long term.

Although threat actors have not yet successfully exploited PHP2Shell, the rapid speed with which they attempted to weaponize these vulnerabilities highlights how swiftly attackers integrate new exploits into their operational capabilities, frequently aided by public research from industry sources. This trend, combined with the recurring pattern of vulnerability discovery, rediscovery, and patch circumvention, which is currently accelerated by AI-assisted vulnerability research, underscores the critical necessity for organizations to remain vigilant in patching and hardening their environments against emerging threats.

## Recommendations

These recommendations can be implemented to help protect against the activity described in this report:

- Patch all applications using PHP to the latest version as soon as possible, prioritizing the patching of internet-facing applications
- Rebuild container images and restart all Apache and PHP-FPM workers after deployment to remove any stale process state
- Disable session upload progress (via `session.upload_progress.enabled = Off`) unless explicitly required; this blocks the upload-progress paths associated with the serialization-context and session-global use-after-free conditions, but does not mitigate the `HashTable` vulnerability
- Disable file uploads (via `file_uploads = Off`) where they are not needed; apply this per application or PHP pool whenever possible to avoid unnecessary functional impact
- Limit request bodies before they reach PHP; configure Apache, NGINX, a reverse proxy, or a WAF to restrict body size, upload size, upload duration, parameter-name length, nesting depth, and the number of form fields, and eject unusually large URL-encoded keys and malformed or abnormal multipart requests
- Run each PHP application under a separate, minimally privileged account and prevent PHP workers from modifying application code or accessing unrelated secrets

#### Additional Resources

<sup>1</sup> https\[:\]//w3techs\[.\]com/technologies/history\_overview/programming\_language/ms/y ||

https\[:\]//thenextweb\[.\]com/news/why-php-continues-to-be-a-popular-but-divisive-programming-language
