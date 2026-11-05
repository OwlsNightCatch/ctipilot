---
title: Vulnerabilities in Node.js (CVE-2026-111497, CVE-2026-105482, CVE-2026-105483, CVE-2026-106069) on Splunk Products - October 2026
url: https://advisory.splunk.com/advisories/SVD-2026-1015
hostname: splunk.com
description: "On October 21, 2026, Node.js announced the availability of fixes for multiple vulnerabilities across the following supported release lines: 22.x, 24.x, and 26.x. These vulnerabilities impact critical operations such as the Brotli decoder, DNS resolution, and TLS certificate validation. The vulnerabilities pose risks for remote code execution and traffic interception. For more information, see [Node.js Security Release](https://nodejs.org/en/blog/vulnerability/october-2026-security-releases). The following vulnerabilities have a Security Impact Rating (SIR) of High and are addressed in this advisory: * CVE-2026-111497 - Brotli decoder out-of-bounds write; potential remote code execution * CVE-2026-105482 - DNS resolution truncation involving embedded NUL characters * CVE-2026-105483 - TLS hostname validation bypass using fullwidth IP digits * CVE-2026-106069 - TLS hostname validation bypass with noncanonical IP addresses Splunk is investigating to determine which products may be affected by these vulnerabilities. As the investigation progresses, Splunk will update this advisory with information about affected products."
sitename: Splunk Vulnerability Disclosure
date: "2026-10-28"
fingerprint: "6813c5d4c4fe938a"
---

# Vulnerabilities in Node.js (CVE-2026-111497, CVE-2026-105482, CVE-2026-105483, CVE-2026-106069) on Splunk Products - October 2026

**Advisory ID:** SVD-2026-1015

**Published:** 2026-10-28

**Last Updated:** 2026-11-04

## Description

On October 21, 2026, Node.js announced the availability of fixes for multiple vulnerabilities across the following supported release lines: 22.x, 24.x, and 26.x.

These vulnerabilities impact critical operations such as the Brotli decoder, DNS resolution, and TLS certificate validation. The vulnerabilities pose risks for remote code execution and traffic interception. For more information, see [Node.js Security Release](https://nodejs.org/en/blog/vulnerability/october-2026-security-releases).

The following vulnerabilities have a Security Impact Rating (SIR) of High and are addressed in this advisory:

- CVE-2026-111497 - Brotli decoder out-of-bounds write; potential remote code execution
- CVE-2026-105482 - DNS resolution truncation involving embedded NUL characters
- CVE-2026-105483 - TLS hostname validation bypass using fullwidth IP digits
- CVE-2026-106069 - TLS hostname validation bypass with noncanonical IP addresses

Splunk is investigating to determine which products may be affected by these vulnerabilities. As the investigation progresses, Splunk will update this advisory with information about affected products.

## Product Status

### Under Investigation

Splunk is actively investigating the following to determine if they are affected by the vulnerabilities:

| Product | 
|---|
| Splunk Observability Cloud | 
| Splunk Observability OpenTelemetry Collectors | 
| AppDynamics On-Premises (other components) | 
| Galileo | 

### Affected Products

Splunk found the following products include packages affected by the vulnerabilities:

| Product | 
|---|
| Splunk Enterprise\* | 
| Splunk Visual Exporter\*\* | 
| Splunk SOAR Automation Broker | 
| Splunk UBA | 
| Splunk Attack Analyzer | 
| Python for Scientific Computing | 
| AppDynamics SaaS | 
| AppDynamics Reporting Service | 
| AppDynamics Synthetic Services | 
| AppDynamics Virtual Appliance | 
| Smartlook | 

\*Splunk Enterprise versions 10.0 and lower are vulnerable. To address the Node.js runtime bundled with Splunk Enterprise, we recommend upgrading to Splunk Enterprise 10.2 or higher. This upgrade does not remediate the Splunk Visual Exporter app; see the mitigation below. Splunk plans to upgrade the vulnerable packages in a future Splunk Enterprise 10.0 release.

\*\*All Splunk Enterprise versions include the vulnerable Splunk Visual Exporter app. As a potential mitigation, disable or remove the Splunk Visual Exporter app. See [Manage app and add-on objects](https://help.splunk.com/en/splunk-enterprise/administer/admin-manual/10.0/meet-splunk-apps/manage-app-and-add-on-objects).

### Unaffected Products

Splunk confirmed the following products are unaffected by the vulnerabilities:

| Product | 
|---|
| Splunk Cloud Platform | 
| Splunk Universal Forwarder | 
| Splunk Apps & Add-ons (not listed) | 
| Splunk Enterprise Security | 
| Splunk SOAR Cloud | 
| Splunk SOAR | 
| Splunk SOAR Connectors | 
| Splunk ITSI | 
| Splunk Otel JS SDK | 
| Splunk On-Call | 
| AppDynamics Agents | 

## Changelog

- 2026-11-04: Updated Product Status section.
