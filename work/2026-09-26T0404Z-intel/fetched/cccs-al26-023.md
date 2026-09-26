# extract: served via trafilatura-direct
---
title: AL26-023 - Vulnerability Impacting Microsoft SharePoint Server - CVE-2026-65660 - Canadian Centre for Cyber Security
author: Communications Security Establishment Canada
url: https://www.cyber.gc.ca/
hostname: cyber.gc.ca
description: AL26-023 - Vulnerability Impacting Microsoft SharePoint Server - CVE-2026-65660
sitename: Canadian Centre for Cyber Security
date: "2026-09-24"
---
**Number:** AL26-023**Date:** September 24, 2026

## Audience

This Alert is intended for IT professionals and managers.

## Purpose

An Alert is used to raise awareness of a recently identified cyber threat that may impact cyber information assets, and to provide additional detection and mitigation advice to recipients. The Canadian Centre for Cyber Security ("Cyber Centre") is also available to provide additional assistance regarding the content of this Alert to recipients as requested.

## Details

The Canadian Centre for Cyber Security (Cyber Centre) is aware of active exploitation of a vulnerability affecting Microsoft SharePoint Server<sup>[Footnote 1](https://www.cyber.gc.ca#fn1)</sup>. In response to the Microsoft security advisory, released on August 11, 2026<sup>[Footnote 2](https://www.cyber.gc.ca#fn2)</sup>, the Cyber Centre issued AV26-804 Update 3<sup>[Footnote 3](https://www.cyber.gc.ca#fn3)</sup> on September 24, 2026.

Tracked as CVE-2026-65660<sup>[Footnote 4](https://www.cyber.gc.ca#fn4)</sup>, this vulnerability is an Improper Control of Generation of Code ('Code Injection') (CWE-94)<sup>[Footnote 5](https://www.cyber.gc.ca#fn5)</sup> vulnerability affecting multiple versions of Microsoft SharePoint Server, that could allow an authenticated attacker to execute arbitrary code on vulnerable SharePoint servers.

Chained with other SharePoint vulnerabilities, this vulnerability can achieve pre-authentication remote code execution on SharePoint servers configured to permit anonymous access. Organizations that have not fully applied prior SharePoint security updates may therefore face an elevated risk of compromise.

## Suggested actions

The Cyber Centre recommends that organizations upgrade affected Microsoft SharePoint instances to a fixed version:

| Affected products | Affected versions | Fixed Versions | 
|---|---|---|
| Microsoft SharePoint Enterprise Server 2016 | All versions prior to 16.0.5565.1001 | Version 16.0.5565.1001 | 
| Microsoft SharePoint Server 2019 | All Versions prior to 16.0.10417.20198 | Version 16.0.10417.20198 | 
| Microsoft SharePoint Server Subscription Edition | All versions prior to 16.0.19725.20522 | Version 16.0.19725.20522 | 

**Important note:** Microsoft SharePoint Enterprise Server 2016<sup>[Footnote 6](https://www.cyber.gc.ca#fn6)</sup> and Server 2019<sup>[Footnote 7](https://www.cyber.gc.ca#fn7)</sup> are **end of life** as of **July 15, 2026**. Organizations are urged to migrate to a supported version.

The Cyber Centre also recommends organizations to:

- Identify all on-premises SharePoint Server instances, particularly those exposed to the Internet, and ensure they are running supported versions of Microsoft SharePoint Server.
- Apply the latest Microsoft security updates to all affected SharePoint Server deployments, including SharePoint Server Subscription Edition, SharePoint Server 2019, and SharePoint Server 2016.
- Reduce the attack surface by restricting or eliminating direct internet exposure of SharePoint servers where possible, limiting access to SharePoint Central Administration and other management interfaces.
- Strengthen access controls by reviewing SharePoint environments for unnecessary or inactive accounts, removing unused accounts, and enforcing multi-factor authentication (MFA) for administrators and other privileged users.
- Harden SharePoint deployments by enabling Antimalware Scan Interface (AMSI) integration for SharePoint web applications and configuring AMSI Request Body Scan Mode to Full Mode where operationally feasible.
- Monitor for indicators of compromise and exploitation activity, including:
	
  - unusual administrative activity or suspicious authenticated access attempts
  - unexpected web part modifications or unauthorized configuration changes
  - unauthorized authentication attempts and privilege escalation activity
  - suspicious access to IIS machine keys
  - evidence of deserialization attacks, web shell deployment, or malicious process execution
  - unusual requests targeting SharePoint services
  - Microsoft Defender or AMSI detections related to SharePoint exploitation activity
- Conduct ongoing log and security monitoring of SharePoint, IIS, endpoint security, and authentication logs to detect and investigate suspicious activity.

In addition, the Cyber Centre strongly recommends that organizations review and implement the Cyber Centre’s Top 10 IT Security Actions with an emphasis on the following topics<sup>[Footnote 8](https://www.cyber.gc.ca#fn8)</sup>:

- patch operating systems and applications
- harden operating systems and applications
- isolate web-facing applications

Should activity matching the content of this alert be discovered, recipients are encouraged to report via [My Cyber Portal](https://www.cyber.gc.ca/en/incident-management), or email [contact@cyber.gc.ca](mailto:contact@cyber.gc.ca).
