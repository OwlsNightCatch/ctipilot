---
title: Vulnerabilities
url: https://app.opencve.io/cve/CVE-2026-90817
hostname: opencve.io
description: An unauthenticated Remote Code Execution vulnerability was found in the survey passthrough routing and Data Import processing logic, in which a malicious user could potentially exploit it by manipulating HTTP requests to access an unintended controller route from a public survey context and by supplying a crafted file-path/stream parameter during import handling. If successfully exploited, this could allow the attacker to remotely execute arbitrary code on the REDCap server. The attacker does not have to be authenticated in order to exploit this, but exploitation requires knowledge of a valid public survey hash. This vulnerability exists in REDCap 13.3.0 and higher.
sitename: app.opencve.io
date: "2026-11-18"
fingerprint: b41a17b6bc185657
---
#### Technical impact

An unauthenticated remote code execution vulnerability exists in the survey passthrough routing and Data Import processing logic of REDCap. By manipulating HTTP requests, an attacker can access an unintended controller route from a public survey context and supply a crafted file-path/stream parameter during import handling. If successful, the attacker can run arbitrary code on the REDCap server. The flaw does not require authentication, but it does require knowledge of a valid public survey hash.

#### Affected Systems

Vendors: Vanderbilt University. Product: REDCap. Versions 13.3.0 and newer are affected up to the patched releases; the fix is available in REDCap 16.0.49 LTS, 17.3.10 LTS, and 17.4.4 Standard releases.

#### Risk and Exploitability

The CVSS score of 9.8 indicates an extremely high severity. The EPSS score of 3% indicates a low but non‑negligible exploitation probability, while the lack of authentication and the ability to execute arbitrary code render exploitation likely to be mission critical if discovered. The vulnerability is not listed in the CISA KEV catalog, yet it remains a high‑risk target. The attack vector is inferred to involve crafted HTTP traffic directed at the REDCap server, exploiting the public survey pathway without user credentials. The necessary prerequisite of a known public survey hash modestly reduces exposure, but the potential impact of remote code execution makes prompt mitigation imperative.
