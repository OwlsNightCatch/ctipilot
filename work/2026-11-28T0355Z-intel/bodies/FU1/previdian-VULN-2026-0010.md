---
title: VULN-2026-0010 Exploitation Attempts Observed by Our Honeypots — Cacti
author: Ryan Dewhurst
url: https://previdian.com/VULN-2026-0010
hostname: previdian.com
description: "VULN-2026-0010 exploitation intelligence for Cacti: confirmed exploitation attempts, Previdian sensor telemetry, CISA KEV status, observed attempts, timeline, PoCs, and virtual patch availability."
sitename: Previdian
date: "2026-11-26"
fingerprint: ad04b759ef3e1681
language: en
image: https://previdian.com/VULN-2026-0010/og.png?v=1795780798
pagetype: website
filedate: "2026-11-28"
---
What it is

VULN-2026-0010 is an unauthenticated vulnerability affecting Cacti. Cacti 1.2.31 contains an unauthenticated second-order SQL injection vulnerability when guest access is enabled.

Vulnerability Intelligence

Exploitation Attempts Observed by Our Honeypots
          No CVE Assigned Yet
          Confirmed Confidence
          Not in CISA KEV
          CVSS 9.8 · Critical

Cacti SQL Injection

VULN-2026-0010 is an unauthenticated second-order SQL injection vulnerability in Cacti Cacti that can lead to arbitrary operating system command execution when guest access is enabled; it has a CVSS score of 9.8. It is network-accessible, requires no authentication or user interaction, and has low attack complexity. “Four Requests to Shell: Ek0ms's Cacti 0-Day Chain,” a general reference from Raven AI, provides additional public reporting. Previdian sensors recorded 22 exploitation attempts from 1 unique attacker IP beginning on 2026-11-27; the vulnerability is not listed in CISA KEV. A public proof of concept titled “Four Requests to Root: A Cacti 0day” is available.

This initial assessment is based on Previdian sensor evidence, a public proof of concept, and a Raven AI reference.

Prioritize patching and hunt for exploitation attempts against internet-facing systems.

AI-generated. Assessed 27 Nov 2026.

Early Warning

Previdian customers had 1 day of early warning before it was added to the Previdian KEV feed.

Previdian customers were following this vulnerability from 26 Nov 2026, before Previdian KEV on 27 Nov 2026, and it is not yet in CISA KEV.

- Exploitation
  Exploitation Attempts Observed by Our Honeypots
- Confidence
  Confirmed
- Attack Surface
  Cacti
- Defender Action
  Prioritize Patching

Exploitation attempts observed by Previdian sensors. They do not show that the target was vulnerable or that the attempt succeeded.

216

Attempts observed

21

Unique attacker IPs

9

Attacker countries

DE · EG · ID · MA · MY · RO · SG · TR · US

1

Sensors observed

VULN-2026-0010 exploitation attempts over the last 7 days

Daily events observed by Previdian sensors

Updated 28 Nov 2026

22 Nov
            23 Nov
            24 Nov
            25 Nov
            26 Nov
            27 Nov
            28 Nov

Decision summary

Direct answers before the deeper technical record.

Have exploitation attempts been observed?

Yes. Previdian sensors have observed 216 exploitation attempts, 21 unique attacker IPs, and 9 countries targeting VULN-2026-0010. First observed Nov 27, 2026; last observed Nov 28, 2026. Confidence is confirmed.

Who is affected?

Cacti.

What should we do?

Patch immediately, validate internet-facing exposure, and monitor for matching requests.

Overview

Cacti 1.2.31 contains an unauthenticated second-order SQL injection vulnerability when guest access is enabled. Insufficient validation of guest-controlled user settings allows a remote attacker to manipulate SQL queries and modify polling configurations, leading to arbitrary operating system command execution with the privileges of the affected application process.

A public proof of concept is available. No official patch has been identified.

- Published
  26 Nov 2026
- Exploitation Attempts Reported
  27 Nov 2026
- Attack vector
  Remote
- Complexity
  Low
- Privileges
  None
- User interaction
  None
- Severity
  CVSS 9.8 · Critical
- EPSS
  —
- First Observed
  27 Nov 2026
- Last Observed
  28 Nov 2026

- [Four Requests to Shell: Ek0ms's Cacti 0-Day Chain](https://ravenai.sh/blog/four-requests-to-shell-cacti) Raven AI · General
      
      https://ravenai.sh/blog/four-requests-to-shell-cacti

Exploitation evidence

Third-party attestation and first-party sensor observation are shown separately so teams can judge the evidence chain.

Previdian

Previdian sensors observed exploitation attempts targeting this vulnerability.

Previdian sensor

Public scanner or PoC coverage increases practical exploitability.

Per-source evidence links for KEV attestations are available through the Previdian API.

| Source | Added | 
|---|---|
| Previdian Sensors First | 2026-11-27 11:59 UTC | 

Operational indicators for this CVE are listed under
      [Detection](https://previdian.com/VULN-2026-0010#detection).

Sensor telemetry

Previdian sensor observations are exploitation attempts targeting this vulnerability. They do not show that the target was vulnerable or that the attempt succeeded. The cards and chart show volume, unique attackers, and daily activity.

First observed 27 Nov 2026 · Last observed 28 Nov 2026

Enterprise includes sensor region and window summaries, plus raw IPs, paths, User-Agents, and payloads.

Detection

Make the evidence actionable in scanner, SOC, and edge-control workflows.

- Request targets
- User-Agents
- Callback hosts
  1
  8
  0

Request targets, User-Agents, and callback host details are available on Enterprise.

No scanner integrations recorded yet.

Previdian virtual patch guidance is available for this CVE.

AWS WAF
            Cloudflare
            ModSecurity

Attacker IP indicators observed. Available on Enterprise.

Sensor-derived attacker IP indicators are available on Enterprise under Detection and through the API.

Compensating WAF rules for this CVE.

Enterprise feature. Virtual patch rule content and deployable vendor exports (ModSecurity, Cloudflare, AWS WAF) are available to Previdian Enterprise users.

Risk and context

CVSS v3.1

9.8
            Critical

Potential damage if exploited. Separate from whether attackers are using it.

`CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`
      EPSS

—

Estimated chance of exploitation in the next 30 days. Previdian's warning comes from evidence, not this score.

These PoCs are unverified and could contain malware. Use at your own risk.

public · Created 2026-11-26 19:44:00 UTC

API

Confidence, exploit status, sensor telemetry, PoCs, scanner integrations, mentions, and tags are available programmatically for VM, SOC, and CTI workflows.

- Evidence confidence and provenance
- First-party sensor telemetry
- PoC and scanner references
- Affected versions and enrichment
- Automation-ready JSON delivery

GET /api/v2/enterprise/kevs/VULN-2026-0010

Sample API response```
{
  "cve_id": "VULN-2026-0010",
  "confidence": "Confirmed",
  "cvss_score": 9.8,
  "cvss_estimated": false,
  "epss_score": null,
  "exploit_status": {
    "exploited_in_the_wild": true,
    "active_exploitation_observed": true
  },
  "sensor_telemetry": { "attempts": 216, "sensors": 1 }
}
```
Timeline

1. 14:17 UTC ### Virtual patch available Compensating WAF rule available to block exploitation
2. 08:48 UTC ### Indicators of compromise added (21) Indicators of compromise recorded
3. 08:48 UTC ### Observed by Previdian sensors Previdian sensors observed exploitation attempts targeting this vulnerability.
4. 19:44 UTC ### Public PoC available Public proof-of-concept code published
5. 18:43 UTC ### Added to the Previdian watchlist Previdian customers had 1 day of early warning before Previdian KEV.
6. 18:40 UTC ### VULN published Vulnerability disclosed publicly
