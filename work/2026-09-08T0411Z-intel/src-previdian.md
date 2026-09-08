# extract: served via trafilatura-direct
---
title: CVE-2026-19490 Exploitation Observed — ADC, Gateway | Previdian
author: Ryan Dewhurst
url: https://previdian.com/CVE-2026-19490
hostname: previdian.com
description: "CVE-2026-19490 exploitation intelligence for ADC, Gateway: confirmed active exploitation, Previdian sensor telemetry, CISA KEV status, observed attempts, timeline, and PoCs."
sitename: Previdian
date: "2026-08-19"
---
What it is

CVE-2026-19490 is an unauthenticated NetScaler ADC and NetScaler Gateway Security Bulletin for CVE-2026-19490. Vulnerability in NetScaler ADC and NetScaler Gateway. This issue affects ADC: from 14.1 through 73.32 and...

Vulnerability report

              Active exploitation observed
              Medium confidence
              Not in CISA KEV
          

        
              [NetScaler](https://previdian.com/vendors/netscaler) / ADC · 14.1 to <= 73.32
          

- Severity
- CVSS 9.3 · Critical
- Confidence
- Medium
- Exploit status
- Observed in sensors
- EPSS
- 3.4%
- First observed
- 03 Sep 2026
- Last observed
- 07 Sep 2026

Decision summary

Direct answers before the deeper technical record.

Is it exploited?

Yes. Previdian sensors observed exploitation attempts with medium confidence.

Who is affected?

NetScaler / ADC 14.1 to <= 73.32.

What should we do?

Patch immediately, validate internet-facing exposure, and monitor for matching requests.

Overview

This issue affects ADC: from 14.1 through 73.32 and from 13.1 through 63.21; Gateway: from 14.1 through 73.32 and from 13.1 through 63.21.

      Vendor
      Product
      Affected
      Status
    

      
        NetScaler
        
          ADC
        
        Through 73.32
        
            Affected
        
      

      
        NetScaler
        
          ADC
        
        Through 63.21
        
            Affected
        
      

      
        NetScaler
        
          Gateway
        
        Through 73.32
        
            Affected
        
      

      
        NetScaler
        
          Gateway
        
        Through 63.21
        
            Affected
        
      

- Published
- 19 Aug 2026
- Exploitation Reported
- 03 Sep 2026
- Attack vector
- Remote
- Complexity
- Low
- Privileges
- None
- User interaction
- None

- 
  
  
    [CVE Record](https://www.cve.org/CVERecord?id=CVE-2026-19490) CVE.org · CVE Record
      
      https://www.cve.org/CVERecord?id=CVE-2026-19490
- 
  
  
    [support.citrix.com/support-home/kbsearch/article](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX696939) support.citrix.com · CVE Record
      
      https://support.citrix.com/support-home/kbsearch/article?articleNumbe...

Exploitation evidence

Third-party attestation and first-party sensor observation are shown separately so teams can judge the evidence chain.

Previdian

Independent exploitation attestation added to the Previdian record.

Previdian sensor

First-party sensor telemetry confirms matching exploitation attempts.

GitHub

Public scanner or PoC coverage increases practical exploitability.

Per-source evidence links for KEV attestations are available through the Previdian Pro API.

| Source | Added | 
|---|---|
| Previdian First | 2026-09-03 11:43 UTC | 

      Operational indicators for this CVE are listed under
      [Detection](https://previdian.com#detection).
    

Sensor telemetry

Aggregate observations show the scale, recency, and distribution of activity without overstating sparse data.

18

Attempts observed

9

Unique attacker IPs

5

Attacker countries

AU · DE · JP · TW · US

1

Sensors observed

CVE-2026-19490 exploitation attempts over the last 7 days

Daily events observed by Previdian sensors

Updated 08 Sep 2026

            2 Sep
            3 Sep
            4 Sep
            5 Sep
            6 Sep
            7 Sep
            8 Sep
      

    First observed 03 Sep 2026 · Last observed 07 Sep 2026

Pro adds sensor region and window summaries. Enterprise adds raw IPs, paths, User-Agents, and payloads.

Detection

Make the evidence actionable in scanner, SOC, and edge-control workflows.

- Request targets
- User-Agents
- Callback hosts
- 16
- 5
- 0

Request targets and User-Agents available in Pro. Callback host details available in Enterprise.

No scanner integrations recorded yet.

No Previdian virtual patch is currently available. Future rules ship for ModSecurity, Cloudflare, and AWS WAF.

Attacker IP indicators observed · available in Pro and Enterprise.

Sensor-derived attacker IP indicators are available to Pro and Enterprise accounts under Detection and through the Pro API.

Risk and context

CVSS v4.0

          9.3
            Critical
        

          `CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:L/SI:L/SA:L`
      EPSS

3.4%

Recent mention · BleepingComputer

Attackers have begun targeting a critical-severity Citrix NetScaler auth bypass flaw (CVE-2026-19490) in the wild, according to vulnerability intelligence company Previdian. [...]

BleepingComputer · 04 Sep 2026

Recent mention · CERT Polska

CERT Polska · 21 Aug 2026

Zespół CERT Polska informuje o podatnościach znalezionych w produktach NetScaler ADC (dawniej Citrix ADC) oraz NetScaler Gateway (dawniej Citrix Gateway).Producent opublikował biuletyn bezpieczeństwa opisujący dwie podatności: CVE-2026-19489 oraz CVE-2026-19490.Szczególnie istotna jest luka CVE-2026-19490, która umożliwia obejście mechanizmów uwierzytelniania na urządzeniach skonfigurowanych jako Gateway (SSL VPN, ICA Proxy, CVPN, RDP Proxy) lub AAA vserver. W wybranych wersjach jej wykorzystanie wymaga dodatkowej konfiguracji SAML.Druga podatność (CVE-2026-19489) dotyczy możliwości...

Recent mention · Rapid7

Rapid7 · 19 Aug 2026

OverviewOn August 19, 2026, a security advisory was published for CVE-2026-19490, a critical authentication bypass vulnerability affecting Citrix NetScaler ADC and NetScaler Gateway. The vulnerability carries a CVSS v4.0 base score of 9.3 and can be exploited remotely by an unauthenticated attacker over the network without user interaction or elevated privileges.NetScaler ADC and NetScaler Gateway are widely deployed enterprise networking products commonly positioned at or near the network perimeter. NetScaler ADC provides application delivery, traffic management, load balancing, SSL/TLS...

These PoCs are unverified and could contain malware. Use at your own risk.

github · Created 2026-09-02 15:43:53 UTC · 0 stars · AI assessment 90%

NetScaler ADC/Gateway SAML unsigned-assertion bypass via HTTP-Redirect binding (CTX696939) - root cause analysis + PoC

Timeline

1. 
        
          
        ### Observed by Previdian sensorsEvidence-backed exploitation signal
2. 
        
          
        ### Indicators of compromise added (9)Indicators of compromise recorded
3. 
        
          
        ### Public PoC availablePublic proof-of-concept code published
4. 
        
          
        ### Added to the Previdian watchlistPro and Enterprise Watch users had 2 weeks of early warning before Previdian confirmed it as a KEV.
5. 
        
          
        ### CVE publishedVulnerability disclosed publicly
6. 
        
          
        ### CVE ID reservedIdentifier reserved by the CNA

Pro API

Confidence, exploit status, sensor telemetry, PoCs, scanner integrations, mentions, and tags are available programmatically for VM, SOC, and CTI workflows.

- Evidence confidence and provenance
- First-party sensor telemetry
- PoC and scanner references
- Affected versions and enrichment
- Automation-ready JSON delivery

GET /api/v2/pro/kevs/CVE-2026-19490

Free JSON includes basic KEV fields```
{
  "cve_id": "CVE-2026-19490",
  "confidence": "Medium",
  "cvss_score": 9.3,
  "cvss_estimated": false,
  "epss_score": 0.03372,
  "exploit_status": {
    "exploited_in_the_wild": true,
    "active_exploitation_observed": true
  },
  "sensor_telemetry": { "attempts": 18, "sensors": 1 }
}
```
