---
title: Splunk November 2026 Update Fixes 146 Flaws, Including RCE CVE-2026-131253
author: Do Son
url: https://securityonline.info/splunk-security-updates-november-2026/
hostname: securityonline.info
description: TL;DR On November 18, 2026, Splunk shipped five advisories that fix 146 bugs across its core tools and apps. These Splunk security updates patch high-risk code execution and login bypass flaws rat…
sitename: Daily CyberSecurity
date: "2026-11-19"
categories: ['Vulnerability News']
tags: ['CVE-2026-131202', 'CVE-2026-131253', 'CVE-2026-76536', 'Splunk', 'Splunk Enterprise', 'Splunk SOAR', 'Vulnerability']
fingerprint: "6c53e51486ecc28a"
language: en
image: https://securityonline.info/wp-content/uploads/2026/11/splunk-technology.webp
pagetype: article
filedate: "2026-11-25"
---
## TL;DR

On November 18, 2026, Splunk shipped five advisories that fix 146 bugs across its core tools and apps. These Splunk security updates patch high-risk code execution and login bypass flaws rated up to CVSS 9.9. Admins should apply the Splunk security updates November 2026 patches right away to keep their hosts safe.

- **Total:** 7 CVEs
- **Severity:** 5 Critical · 2 High
- **Actively exploited:** None confirmed
- **Highest severity:** 9.9 (Critical · CVSSv3) — [CVE-2026-131253](https://securityonline.info/cve-watchtower/cve-2026-131253/)
- **Action:** Apply the latest security updates now

**Splunk**CVE the moment it's exploited.

[Get free email alerts](https://securityonline.info/cve-alerts/)

Notable CVEs

| CVE | CVSS (CVSSv3) | Type | Fixed in | Status | 
|---|---|---|---|---|
| [CVE-2026-131253](https://securityonline.info/cve-watchtower/cve-2026-131253/) | 9.9 | CWE-94 | 8.8.0 | Not exploited | 
| [CVE-2026-131287](https://securityonline.info/cve-watchtower/cve-2026-131287/) | 9.6 | CWE-863 | 8.8.0 | Not exploited | 
| [CVE-2026-76536](https://securityonline.info/cve-watchtower/cve-2026-76536/) | 9.4 | CWE-287 | 10.4.5, 10.2.9, 10.0.12 (+1) | Not exploited | 
| [CVE-2026-76535](https://securityonline.info/cve-watchtower/cve-2026-76535/) | 9.1 | CWE-287 | 10.6.1, 10.4.5, 10.2.9 (+2) | Not exploited | 
| [CVE-2026-131202](https://securityonline.info/cve-watchtower/cve-2026-131202/) | 9.1 | CWE-22 | 8.7.0 | Not exploited | 
| [CVE-2026-131304](https://securityonline.info/cve-watchtower/cve-2026-131304/) | 8.1 | CWE-639 | 2.0.0 | Not exploited | 
| [CVE-2026-131299](https://securityonline.info/cve-watchtower/cve-2026-131299/) | 7.5 | CWE-611 | 8.1.7 | Not exploited | 

## Why It Matters

Splunk notes that more than 15,000 firms in 110 countries use its data tools to watch for threats. Likewise, market tracker HG Insights counts over 1,700 large firms that run Splunk Enterprise Security. Since teams store key logs and response steps inside these apps, unpatched nodes give threat actors prime targets.

So far, security teams have seen no active attacks in the wild and no public exploit code for these 146 bugs. Still, the large number of critical API flaws makes fast patching vital for all defenders.

## How the Attack Works

### Splunk SOAR Code Execution

The largest set of fixes sits in [Splunk advisory SVD-2026-1108](https://advisory.splunk.com/advisories/SVD-2026-1108), which patches 59 bugs in Splunk SOAR. At the top of the list, [CVE-2026-131253](https://securityonline.info/cve-watchtower/cve-2026-131253/) holds a CVSS score of 9.9. In this flaw, the App Wizard puts user-supplied names straight into new connector code without checks. As a result, a logged-in user with app and playbook rights can run arbitrary code on the host.

In addition, [CVE-2026-131287](https://securityonline.info/cve-watchtower/cve-2026-131287/) earns a 9.6 CVSS score. When an admin deletes a source code repo and reuses its name, old playbook links point to the new repo. This flaw lets an attacker run rogue playbook code.

### Splunk Enterprise Login Bypass

Next, [Splunk advisory SVD-2026-1103](https://advisory.splunk.com/advisories/SVD-2026-1103) fixes 38 flaws in Splunk Enterprise. Two critical login bypass bugs stand out in this release. First, [CVE-2026-76536](https://securityonline.info/cve-watchtower/cve-2026-76536/) (CVSS 9.4) hits standalone hosts where clustering is off. Because the cluster REST API accepts an empty shared secret, remote attackers with no login can read or change cluster settings.

Second, [CVE-2026-76535](https://securityonline.info/cve-watchtower/cve-2026-76535/) (CVSS 9.1) occurs because the RapidDiag REST API also accepts an empty shared key. Thus, a remote attacker with no login can run Search Processing Language (SPL) queries as a valid user.

### Splunk Enterprise Security Path Traversal and SPL Injection

Meanwhile, [Splunk advisory SVD-2026-1106](https://advisory.splunk.com/advisories/SVD-2026-1106) resolves 42 bugs in Splunk Enterprise Security and the Splunk App for PCI Compliance. Flashpoint researcher Klevis Luli found [CVE-2026-131202](https://securityonline.info/cve-watchtower/cve-2026-131202/), a critical path traversal flaw rated CVSS 9.1. By pairing lookup file uploads with the Configuration Checker tool, an ess\_admin user can write files outside safe paths and run arbitrary code. Most other flaws in this group involve SPL injection in Mission Control and dashboard views.

### Splunk App for Stream and AI Assistant Bugs

Furthermore, [Splunk advisory SVD-2026-1110](https://advisory.splunk.com/advisories/SVD-2026-1110) fixes three flaws in Splunk App for Stream. The main bug, [CVE-2026-131299](https://securityonline.info/cve-watchtower/cve-2026-131299/) (CVSS 7.5), allows XML External Entity (XXE) injection on port 8089. Because the upload endpoint parses XML files without blocking external links, remote attackers with no login can read local files.

Finally, [Splunk advisory SVD-2026-1111](https://advisory.splunk.com/advisories/SVD-2026-1111) patches four REST API access flaws in Splunk AI Assistant. Notably, [CVE-2026-131304](https://securityonline.info/cve-watchtower/cve-2026-131304/) (CVSS 8.1) trusts a client-supplied tenant ID, letting low-level users read another tenant’s data.

## Affected Versions

These Splunk security updates affect five product lines prior to the November 2026 releases:

- **Core Platform:** Splunk Enterprise versions below 10.6.1, 10.4.5, 10.2.9, 10.0.12, and 9.4.17.
- **SIEM Suite:** Splunk Enterprise Security and PCI Compliance versions below 8.7.0.
- **Automation Engine:** Splunk SOAR versions below 8.8.0.
- **Data Capture:** Splunk App for Stream versions below 8.1.7.
- **AI Add-On:** Splunk AI Assistant versions below 2.0.0.

## Patch and Mitigation Steps

Teams should apply these Splunk security updates right away across all affected hosts. Upgrade Splunk Enterprise to 10.6.1, 10.4.5, 10.2.9, 10.0.12, or 9.4.17, and move Splunk Enterprise Security to 8.7.0. Also, update Splunk SOAR to 8.8.0, Splunk App for Stream to 8.1.7, and Splunk AI Assistant to 2.0.0.

If you cannot patch at once, apply the vendor workarounds now. On Splunk Enterprise, set a strong pass4SymmKey value of at least 12 characters under the clustering stanza in server.conf. In addition, turn off unused apps such as Splunk App for Stream, Splunk AI Assistant, or RapidDiag until you finish the upgrade.

#### Support Our Threat Intelligence

Find our vulnerability reports and weekly recaps helpful? Support our work today and unlock a **100% ad-free** reading experience!
