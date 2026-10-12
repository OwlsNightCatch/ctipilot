---
title: CVE-2026-85097 PoC and Scanner Context — Bricksforge | Previdian
author: Ryan Dewhurst
url: https://previdian.com/CVE-2026-85097
hostname: previdian.com
description: "CVE-2026-85097 exploitation intelligence for Bricksforge: CISA KEV status, timeline, and PoCs."
sitename: Previdian
date: "2026-10-08"
fingerprint: b586fe01e7b454a1
---
What it is

CVE-2026-85097 is an unauthenticated vulnerability affecting Bricksforge. The Bricksforge plugin for WordPress is vulnerable to unauthenticated arbitrary file upload in versions up to, and including, 3.1.8.9. This is...

Vulnerability report

Bricksforge \<= 3.1.8.9 Unauthenticated Arbitrary File Upload Arbitrary File Access

Bricksforge · 0 to \<= 3.1.8.9

- Severity
- CVSS 9.8 · Critical
- Confidence
- —
- Exploit status
- PoC available
- EPSS
- 0.3%
- First observed
- —
- Last observed
- —

Decision summary

Direct answers before the deeper technical record.

Is it exploited?

Previdian records an exploitation-related signal (poc available). This CVE has not been added as a known exploited vulnerability.

Who is affected?

Bricksforge 0 to \<= 3.1.8.9.

What should we do?

Track for updates. Assess relevance to your asset inventory and enrichment workflows.

Overview

The Bricksforge plugin for WordPress is vulnerable to unauthenticated arbitrary file upload in versions up to, and including, 3.1.8.9. This is due to insufficient validation of the attacker-controlled URL field in the 'temporaryFileUploads' parameter during form submission. An unauthenticated attacker can first obtain a valid nonce via the bricksforge\_regenerate\_nonce AJAX endpoint, then upload a GIF/PHP polyglot file to the temporary upload directory where MIME type validation is correctly performed.

Subsequently, the attacker can submit a form with a crafted 'temporaryFileUploads' parameter where the server-side file path points to the validated GIF file, but the attacker-controlled url field ends with a .php extension. This makes it possible for unauthenticated attackers to upload and execute arbitrary PHP code on the server.

Vendor
      Product
      Affected
      Status

Bricksforge
                    Affected

Bricksforge

Through 3.1.8.9

Affected

- Published
- 08 Oct 2026
- Exploitation date
- —
- Attack vector
- Remote
- Complexity
- Low
- Privileges
- None
- User interaction
- None

- [CVE Record](https://www.cve.org/CVERecord?id=CVE-2026-85097) CVE.org · CVE Record
      
      https://www.cve.org/CVERecord?id=CVE-2026-85097
- [wordfence.com/threat-intel/vulnerabilities/id/e993c929-f17...](https://www.wordfence.com/threat-intel/vulnerabilities/id/e993c929-f175-43a7-92e6-9d3b089b8dde?source=cve) wordfence.com · CVE Record
      
      https://www.wordfence.com/threat-intel/vulnerabilities/id/e993c929-f1...
- [bricksforge.io/version-changelog](https://bricksforge.io/version-changelog/) bricksforge.io · CVE Record
      
      https://bricksforge.io/version-changelog/

Exploitation evidence

These signals relate to exploitability. Previdian has not added this CVE as a known exploited vulnerability.

GitHub

Public scanner or PoC coverage increases practical exploitability.

Detection

Make the evidence actionable in scanner, SOC, and edge-control workflows.

- Request targets
- User-Agents
- Callback hosts
- 0
- 0
- 0

Request targets and User-Agents available in Pro. Callback host details available in Enterprise.

No scanner integrations recorded yet.

No Previdian virtual patch is currently available. Future rules ship for ModSecurity, Cloudflare, and AWS WAF.

No detection artifacts or sensor request patterns are available for this CVE yet.

Check back as sensor telemetry and scanner integrations are updated.

Risk and context

CVSS v3.1

9.8
            Critical

Potential damage if exploited. Separate from whether attackers are using it.

`CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`
      EPSS

0.3%

Estimated chance of exploitation in the next 30 days. Previdian's warning comes from evidence, not this score.

These PoCs are unverified and could contain malware. Use at your own risk.

github · Created 2026-10-10 04:51:32 UTC · 0 stars · AI assessment 90%

Timeline

1. 04:51 UTC ### Public PoC available Public proof-of-concept code published
2. 06:42 UTC ### CVE published Vulnerability disclosed publicly
3. 01:41 UTC ### CVE ID reserved Identifier reserved by the CNA

Pro API

Confidence, exploit status, sensor telemetry, PoCs, scanner integrations, mentions, and tags are available programmatically for VM, SOC, and CTI workflows.

- Evidence confidence and provenance
- First-party sensor telemetry
- PoC and scanner references
- Affected versions and enrichment
- Automation-ready JSON delivery

GET /api/v2/pro/kevs/CVE-2026-85097

Free JSON includes basic KEV fields```
{
  "cve_id": "CVE-2026-85097",
  "confidence": null,
  "cvss_score": 9.8,
  "cvss_estimated": false,
  "epss_score": 0.00312,
  "exploit_status": {
    "exploited_in_the_wild": false,
    "active_exploitation_observed": false
  },
  "sensor_telemetry": { "attempts": 0, "sensors": 0 }
}
```
