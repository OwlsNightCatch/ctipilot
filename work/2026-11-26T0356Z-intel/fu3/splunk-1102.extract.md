---
title: Vulnerability in Java (CVE-2026-114938) on Splunk Products - November 2026
url: https://advisory.splunk.com/advisories/SVD-2026-1102
hostname: splunk.com
description: "On November 18, Oracle announced the availability of fixes for a vulnerability in OpenJDK that could lead to remote code execution identified by: - CVE-2026-114938 For information about these vulnerabilities, see [Oracle Critical Security Patch Update Advisory - November 2026](https://www.oracle.com/security-alerts/cspunov2026.html). This vulnerability is being referenced as Java4shell."
sitename: Splunk Vulnerability Disclosure
date: "2026-11-18"
fingerprint: f91a95d4cffc90c8
language: en
image: https://advisory.splunk.com/assets/img/logo_color.jpg
filedate: "2026-11-26"
---

# Vulnerability in Java (CVE-2026-114938) on Splunk Products - November 2026

**Advisory ID:** SVD-2026-1102

**Published:** 2026-11-18

**Last Updated:** 2026-11-25

## Description

On November 18, Oracle announced the availability of fixes for a vulnerability in OpenJDK that could lead to remote code execution identified by:

- CVE-2026-114938

For information about these vulnerabilities, see [Oracle Critical Security Patch Update Advisory - November 2026](https://www.oracle.com/security-alerts/cspunov2026.html). This vulnerability is being referenced as Java4shell.

## Product Status

Splunk is investigating its product line to determine which products are affected by this vulnerability. As the investigation progresses, Splunk will update this advisory with information about affected products. If a product is not listed as unaffected or affected it’s currently under investigation.

### Affected Products

Splunk is developing fixes for the products listed below and will update this advisory with fixed release information as it becomes available. Splunk confirmed the following products are affected by the vulnerability:

| Product | Remediation Information | 
|---|---|
| AppDynamics On-Premises Virtual Appliance | Upgrade to 26.7.2 or higher | 
| AppDynamics On-Premises Events Service\* | Upgrade to 26.7.4 or higher | 
| AppDynamics On-Premises EUM Server\* | In progress | 
| AppDynamics Enterprise Console\* | Upgrade to 26.7.4 or higher | 
| AppDynamics On-Premises Controller\* | Upgrade to 26.7.4 or higher | 
| AppDynamics Analytics Agent | Upgrade to 26.10.2 or higher | 
| AppDynamics Machine Agent | Upgrade to 26.8.1 or higher | 
| AppDynamics Private Synthetic Agent | In progress | 
| AppDynamics Database Agent | Upgrade to 26.7.2 or higher | 
| AppDynamics Python Agent | Upgrade to 26.7.3 or higher | 
| AppDynamics PHP Agent | Upgrade to 26.9.1 or higher | 
| AppDynamics Apache Web Server Agent | Upgrade to 26.9.1 or higher | 
| Splunk Attack Analyzer | Mitigated | 
| Splunk Observability Cloud | In progress | 
| Splunk UBA | In progress | 

\*As a mitigation, turn off the affected Base64 intrinsic by adding `-XX:-UseBASE64Intrinsics` to the JVM startup options. Verify that the running JVM reports `UseBASE64Intrinsics = false`. This mitigation might reduce performance or cause application instability.

### Unaffected Products

Splunk confirmed the following products are unaffected by the vulnerability:

| Product | 
|---|
| Splunk Cloud Platform\* | 
| Splunk Enterprise | 
| Splunk Universal Forwarder | 
| Splunk DB Connect\* | 
| Splunk Apps & Add-ons | 
| Splunk SOAR Cloud | 
| Splunk SOAR | 
| Splunk SOAR Connectors | 
| Splunk Enterprise Security | 
| Splunk IT Service Intelligence (ITSI)\* | 
| Splunk On-Call | 
| Splunk OpenTelemetry Collector | 
| Splunk Synthetics Runner | 
| AppDynamics SaaS | 
| AppDynamics Java Agent\*\* | 
| AppDynamics Agents (not listed) | 

\* Splunk IT Service Intelligence and Splunk DB Connect use a separately installed Java runtime. Customers running these apps on self-managed hosts should update the Java runtime to a supported version that includes the fix for CVE-2026-114938. Splunk Cloud Platform deployments using Java-dependent apps rely on a Java runtime provided by Splunk. Splunk is updating Java for applicable deployments.

\*\* The AppDynamics Java Agent uses a separately installed Java runtime. Customers running these apps on self-managed hosts should update the Java runtime to a supported version that includes the fix for CVE-2026-114938.

## Changelog

- 2026-11-25: Added Splunk UBA and AppDynamics Apache Web Server Agent to affected products. Added fix versions for AppDynamics PHP Agent, AppDynamics Python Agent, and AppDynamics Apache Web Server Agent.
- 2026-11-24: Updated Product Status adding Splunk Observability Cloud and AppDynamics On-Premises Controller to affected and Splunk Enterprise Security to unaffected. Added fix versions for AppDynamics On-Premises Virtual Appliance, AppDynamics On-Premises Events Service, AppDynamics Enterprise Console, AppDynamics On-Premises Controller, AppDynamics Analytics Agent, AppDynamics Machine Agent, and AppDynamics Database Agent. Deployed mitigation to Splunk Attack Analyzer.
- 2026-11-20: Updated Product Status. Added potential mitigation for AppDynamics On-Premises Events Service, EUM Server, and Enterprise Console.
- 2026-11-19: Updated Product Status.
- 2026-11-18: Updated Product Status.
