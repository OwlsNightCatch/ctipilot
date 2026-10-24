---
title: Vulnerabilities in PHP (CVE-2026-109618, CVE-2026-109619) on Splunk Products - October 2026
url: https://advisory.splunk.com/advisories/SVD-2026-1013
hostname: splunk.com
description: "On October 21, the PHP Foundation announced the availability of a Critical PHP Security release addressing two critical vulnerabilities: - CVE-2026-109618 - RCE via OOM corruption - CVE-2026-109619 - RCE via stale global state For information about these vulnerabilities, see the advisories [GHSA-w8hw-w9fx-j79w](https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w) and [GHSA-6wmf-4rv5-p3rp](https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp). These vulnerabilities are being referenced as PHP2shell. Splunk is investigating to determine which products may be affected by these vulnerabilities and the impact on each affected product. Currently, no Splunk products are known to be affected. This advisory will be updated as information is available."
sitename: Splunk Vulnerability Disclosure
date: "2026-10-22"
fingerprint: "6338c5d20af6a1c9"
---

# Vulnerabilities in PHP (CVE-2026-109618, CVE-2026-109619) on Splunk Products - October 2026

**Advisory ID:** SVD-2026-1013

**Published:** 2026-10-22

**Last Updated:** 2026-10-23

## Description

On October 21, the PHP Foundation announced the availability of a Critical PHP Security release addressing two critical vulnerabilities:

- CVE-2026-109618 - RCE via OOM corruption
- CVE-2026-109619 - RCE via stale global state

For information about these vulnerabilities, see the advisories [GHSA-w8hw-w9fx-j79w](https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w) and [GHSA-6wmf-4rv5-p3rp](https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp). These vulnerabilities are being referenced as PHP2shell.

Splunk is investigating to determine which products may be affected by these vulnerabilities and the impact on each affected product. Currently, no Splunk products are known to be affected. This advisory will be updated as information is available.

## Product Status

| Product | Status | 
|---|---|
| Splunk Cloud Platform | Unaffected | 
| Splunk Enterprise | Unaffected | 
| Splunk Universal Forwarder | Unaffected | 
| Splunk Enterprise Security | Unaffected | 
| Splunk ITSI | Unaffected | 
| Splunk SOAR Cloud | Unaffected | 
| Splunk SOAR | Unaffected | 
| Splunk SOAR Connectors | Unaffected | 
| Splunk UBA | Unaffected | 
| Splunk Attack Analyzer | Unaffected | 
| Splunk Observability Cloud | Unaffected | 
| Splunk Observability OpenTelemetry Collectors | Unaffected | 
| Splunk On-Call | Unaffected | 
| Splunk Apps & Add-ons | Unaffected | 
| AppDynamics SaaS | Unaffected | 
| AppDynamics On-Premises | Unaffected | 
| AppDynamics Agents | Unaffected | 
| AppDynamics PHP Agent | Unaffected | 
| Galileo | Unaffected | 
| WideField | Unaffected | 
| Smartlook | Under Investigation | 
| Cisco Secure Endpoint - Cloud (including the Orbital component) | Unaffected | 
| Cisco Secure Endpoint - Private Cloud | Unaffected | 
| Cisco Secure Malware Analytics - Cloud | Unaffected | 
| Cisco Secure Malware Analytics - Private Cloud | Unaffected | 
| Cisco XDR | Unaffected | 

The AppDynamics PHP Agent injects Splunk AppDynamics instrumentation into PHP applications at runtime, but does not include or install PHP. See the [AppDynamics PHP Agent documentation](https://help.splunk.com/en/appdynamics-on-premises/application-performance-monitoring/26.9.0/install-app-server-agents/php-agent) for more information. Splunk strongly recommends that customers update their PHP installations immediately.

The [Zabbix integration for Splunk On-Call](https://help.splunk.com/en/splunk-observability-cloud/splunk-on-call/integrations-with-splunk-on-call/zabbix-integration-for-splunk-on-call) runs on Zabbix but does not include or install Zabbix or PHP. Splunk strongly recommends that customers update their PHP installations immediately.

## Changelog

- 2026-10-23: Added Cisco Secure Endpoint - Cloud (including the Orbital component), Cisco Secure Endpoint - Private Cloud, Cisco Secure Malware Analytics - Cloud, Cisco Secure Malware Analytics - Private Cloud, and Cisco XDR as unaffected
- 2026-10-23: Added information and documentation links clarifying that the AppDynamics PHP Agent and the Zabbix integration for Splunk On-Call do not include or install PHP.
- 2026-10-23: Updated Splunk On-Call and AppDynamics SaaS to unaffected.
- 2026-10-23: Added Splunk UBA and Splunk Attack Analyzer to Product Status as Unaffected.
