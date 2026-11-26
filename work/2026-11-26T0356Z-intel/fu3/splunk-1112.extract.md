---
title: Vulnerabilities in NGINX affecting Splunk Products - November 2026
url: https://advisory.splunk.com/advisories/SVD-2026-1112
hostname: splunk.com
description: "On November 18, 2026, NGINX announced the availability of a fix for multiple critical vulnerabilities in NGINX that could lead to remote code execution. The vulnerabilities affect NGINX versions 1.9.5 through 1.31.8 and is fixed in 1.31.9 (mainline) and 1.30.7 (stable). The vulnerabilities were identified by the following CVEs: - CVE-2026-123007: NGINX ngx_http_v2_module vulnerability - CVE-2026-123634: NGINX resolver vulnerability - CVE-2026-123633: NGINX ngx_http_v2_module vulnerability - CVE-2026-121810: NGINX ngx_http_v3_module vulnerability - CVE-2026-113425: NGINX ngx_mail_proxy_module vulnerability For more information, see the [NGINX Security Advisories](https://nginx.org/en/security_advisories.html). Splunk has not identified evidence of attempted or successful exploitation of these vulnerabilities in Splunk managed environments."
sitename: Splunk Vulnerability Disclosure
date: "2026-11-19"
fingerprint: e83245d4c6f4c582
language: en
image: https://advisory.splunk.com/assets/img/logo_color.jpg
filedate: "2026-11-26"
---

# Vulnerabilities in NGINX affecting Splunk Products - November 2026

**Advisory ID:** SVD-2026-1112

**Published:** 2026-11-19

**Last Updated:** 2026-11-25

## Description

On November 18, 2026, NGINX announced the availability of a fix for multiple critical vulnerabilities in NGINX that could lead to remote code execution. The vulnerabilities affect NGINX versions 1.9.5 through 1.31.8 and is fixed in 1.31.9 (mainline) and 1.30.7 (stable).

The vulnerabilities were identified by the following CVEs:

- CVE-2026-123007: NGINX ngx\_http\_v2\_module vulnerability
- CVE-2026-123634: NGINX resolver vulnerability
- CVE-2026-123633: NGINX ngx\_http\_v2\_module vulnerability
- CVE-2026-121810: NGINX ngx\_http\_v3\_module vulnerability
- CVE-2026-113425: NGINX ngx\_mail\_proxy\_module vulnerability

For more information, see the [NGINX Security Advisories](https://nginx.org/en/security_advisories.html).

Splunk has not identified evidence of attempted or successful exploitation of these vulnerabilities in Splunk managed environments.

## Product Status

Splunk is investigating its product line to determine which products are affected by this vulnerability. As the investigation progresses, Splunk will update this advisory with information about affected products. If a product is not listed as unaffected or affected it’s currently under investigation.

### Affected Products

Splunk is developing fixes for the products listed below and will update this advisory with fixed release information as it becomes available. Splunk confirmed the following products are affected by the vulnerability:

| Product | 
|---|
| Splunk Cloud Platform | 
| SOAR | 
| SOAR Cloud | 
| Splunk Attack Analyzer | 
| Splunk On-Call | 
| Splunk Observability Cloud | 
| AppDynamics SaaS | 
| AppDynamics On-Premises Virtual Appliance | 

### Unaffected Products

Splunk confirmed the following products are unaffected by the vulnerability:

| Product | 
|---|
| Splunk Enterprise | 
| Splunk Universal Forwarder | 
| Splunk Apps & Add-ons | 
| Splunk Add-on for NGINX | 
| Splunk Enterprise Security | 
| SOAR Connectors | 
| NGINX SOAR Connector | 

## Changelog

- 2026-11-25: Added Splunk On-Call as affected and Splunk Apps & Add-ons as unaffected. Explicitly listed the NGINX SOAR connector as unaffected.
- 2026-11-24: Updated Product Status adding Splunk Attack Analyzer and Splunk Observability Cloud as affected and SOAR Connectors as unaffected.
- 2026-11-20: Updated Product Status.
