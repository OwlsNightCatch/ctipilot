---
title: CVE-2026-85097 Exploited in the Wild — Bricksforge | Previdian
author: Ryan Dewhurst
url: https://previdian.com/CVE-2026-85097
hostname: previdian.com
description: "CVE-2026-85097 exploitation intelligence for Bricksforge: confirmed exploitation in the wild, CISA KEV status, timeline, and PoCs."
sitename: Previdian
date: "2026-10-08"
fingerprint: "81106711c7b05481"
---
What it is

CVE-2026-85097 is an unauthenticated vulnerability affecting Bricksforge. The Bricksforge plugin for WordPress is vulnerable to unauthenticated arbitrary file upload in versions up to, and including, 3.1.8.9. This is...

Vulnerability report

Exploited in the wild
              High confidence
              Not in CISA KEV

Bricksforge \<= 3.1.8.9 Unauthenticated Arbitrary File Upload Arbitrary File Access

Bricksforge · 0 to \<= 3.1.8.9

- Severity
- CVSS 9.8 · Critical
- Confidence
- High
- Exploit status
- Exploited in the wild
- EPSS
- 0.3%
- First observed
- —
- Last observed
- —

Decision summary

Direct answers before the deeper technical record.

Is it exploited?

Yes. Previdian tracks this CVE as a known exploited vulnerability. Confidence is high. Also confirmed by third-party sources.

Who is affected?

Bricksforge 0 to \<= 3.1.8.9.

What should we do?

Prioritize remediation. Validate affected assets and apply vendor fixes on an accelerated timeline.

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
- Exploitation Reported
- 12 Oct 2026
- Attack vector
- Remote
- Complexity
- Low
- Privileges
- None
- User interaction
- None

wordpress
              
              
                php

- [CVE Record](https://www.cve.org/CVERecord?id=CVE-2026-85097) CVE.org · CVE Record
      
      https://www.cve.org/CVERecord?id=CVE-2026-85097
- [wordfence.com/threat-intel/vulnerabilities/id/e993c929-f17...](https://www.wordfence.com/threat-intel/vulnerabilities/id/e993c929-f175-43a7-92e6-9d3b089b8dde?source=cve) wordfence.com · CVE Record
      
      https://www.wordfence.com/threat-intel/vulnerabilities/id/e993c929-f1...
- [bricksforge.io/version-changelog](https://bricksforge.io/version-changelog/) bricksforge.io · CVE Record
      
      https://bricksforge.io/version-changelog/

Exploitation evidence

Third-party attestation and first-party sensor observation are shown separately so teams can judge the evidence chain.

The Hacker News

A trusted third party reported exploitation.

GitHub

Public scanner or PoC coverage increases practical exploitability.

Per-source evidence links for KEV attestations are available through the Previdian Pro API.

| Source | Added | 
|---|---|
| The Hacker News First | 2026-10-12 09:42 UTC | 
| SOCRadar | 2026-10-13 07:20 UTC | 

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

Recent mention · SOCRadar

CVE-2026-85097: Bricksforge WordPress Plugin Flaw Exploited for Unauthenticated RCE Threat actors are actively exploiting CVE-2026-85097, a maximum-severity (CVSS 10.0) vulnerability in the Bricksforge plugin for WordPress. The flaw lets unauthenticated attackers upload and...

SOCRadar · 12 Oct 2026

CVE-2026-85097: Bricksforge WordPress Plugin Flaw Exploited for Unauthenticated RCE Threat actors are actively exploiting CVE-2026-85097, a maximum-severity (CVSS 10.0) vulnerability in the Bricksforge plugin for WordPress. The flaw lets unauthenticated attackers upload and execute arbitrary PHP code on vulnerable sites, resulting in remote code execution (RCE). Patchstack first observed exploitation attempts on October 7, 2026, \[…\]

Recent mention · The Hacker News

The Hacker News · 12 Oct 2026

Ravie LakshmananOct 12, 2026Vulnerability / Web Security A maximum-severity security flaw impacting the Bricksforge plugin for WordPress has come under active exploitation in the wild, according to Patchstack. The critical vulnerability in question is CVE-2026-85097 (CVSS score: 10.0), which allows unauthenticated attackers to upload and execute arbitrary PHP code on vulnerable WordPress websites, resulting in remote code execution (RCE). The security flaw impacts Bricksforge versions up to and including 3.1.8.9. Patches have been released in version 3.1.8.10. Bricksforge is a WordPress...

These PoCs are unverified and could contain malware. Use at your own risk.

github · Created 2026-10-15 12:41:13 UTC · 0 stars · AI assessment 86%

CVE-2026-85097 — Bricksforge \<= 3.1.8.9 unauth file upload to RCE. GIF/PHP polyglot + temporaryFileUploads.url mismatch. python3 exploit.py --url http://TARGET

github · Created 2026-10-14 17:30:09 UTC · 0 stars · AI assessment 84%

github · Created 2026-10-14 01:08:11 UTC · 0 stars · AI assessment 90%

For WordPress

github · Created 2026-10-13 05:39:40 UTC · 0 stars · AI assessment 90%

POC CVE-2026-85097

github · Created 2026-10-12 16:15:51 UTC · 0 stars · AI assessment 90%

CVE-2026-85097 – Bricksforge WordPress Plugin Unauth File Upload to RCE Toolkit (CVSS 10.0) | Red/Blue Team suite for Bricksforge Pro Forms \< 3.1.8.9. 2 tools: Full Exploit (polyglot upload, web shell, mass scan, OPSEC, SQLite/JSON output) + SafeChecker (version detect, non-intrusive audit). Ethical & educational use only.

github · Created 2026-10-10 04:51:32 UTC · 0 stars · AI assessment 90%

Timeline

1. 07:20 UTC ### KEV confirmed by SOCRadar Exploitation attested by an external source
2. 09:42 UTC ### Added to Previdian KEV Feed High-confidence, third-party attested exploitation
3. 04:51 UTC ### Public PoC available Public proof-of-concept code published
4. 06:42 UTC ### CVE published Vulnerability disclosed publicly
5. 01:41 UTC ### CVE ID reserved Identifier reserved by the CNA

Pro API

Confidence, exploit status, sensor telemetry, PoCs, scanner integrations, mentions, and tags are available programmatically for VM, SOC, and CTI workflows.

- Evidence confidence and provenance
- First-party sensor telemetry
- PoC and scanner references
- Affected versions and enrichment
- Automation-ready JSON delivery

GET /api/v2/pro/kevs/CVE-2026-85097

Sample API response```
{
  "cve_id": "CVE-2026-85097",
  "confidence": "High",
  "cvss_score": 9.8,
  "cvss_estimated": false,
  "epss_score": 0.00312,
  "exploit_status": {
    "exploited_in_the_wild": true,
    "active_exploitation_observed": false
  },
  "sensor_telemetry": { "attempts": 0, "sensors": 0 }
}
```
