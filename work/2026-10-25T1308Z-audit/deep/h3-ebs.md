# extract: served via trafilatura-direct
---
title: "CVE-2026-101767: Critical Oracle EBS SQL Injection RCE"
url: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-101767/
hostname: horizon3.ai
description: Horizon3 researchers discovered a critical Oracle E-Business Suite vulnerability (CVSS 9.8) enabling unauthenticated SQL injection and remote code execution. Review the attack chain, patches, mitigations, and NodeZero Rapid Response test.
sitename: Horizon3
date: "2026-10-20"
fingerprint: e59cb79352d737c1
---
# CVE-2026-101767

## **Oracle E-Business Suite TCF SQL Injection and Remote Code Execution**

CVE-2026-101767 is an unauthenticated SQL injection vulnerability in Oracle E-Business Suite (EBS) that can be chained to achieve remote code execution. Discovered by Horizon3.ai’s attack research team, the vulnerability allows an attacker with network access to the affected Thin Client Framework (TCF) servlet to execute SQL as the APPS database user, then run operating system commands as the EBS application account. The vulnerability has a CVSS 3.1 score of **9.8 (Critical)**.

## **Technical Details**

Oracle identifies the affected product as Oracle Application Object Library, Core component. Exploitation requires network access over HTTP or HTTPS, with no authentication or user interaction required.

The vulnerability affects the TCF servlet at `/OA_HTML/AppsTCFServer`, implemented by `oracle.apps.fnd.tcf.SocketServer`. This endpoint is permitted through the default EBS URL firewall configuration.

An attacker can send a crafted request to the vulnerable servlet to execute SQL with the privileges of the APPS database user. The attack chain also enables operating system command execution with the privileges of the EBS application account.

Successful exploitation allows an attacker to read or modify application data accessible to APPS and execute commands on the application host. Depending on the deployment, affected data may include financial, payroll, HR, and procurement records. Operating system access is governed by the permissions of the compromised EBS application account.

Internet-facing EBS web tiers present the most direct exposure. Internal deployments are also at risk if an attacker can reach the vulnerable servlet from a compromised system or another accessible network segment.

**CVSS 3.1:** 9.8 (Critical)

**Vector:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Stop Guessing, Start Proving

## **NodeZero® Proactive Security Platform Rapid Response**

A NodeZero Rapid Response test has been developed to safely validate whether this vulnerability can be exploited in your environment. The test uses real attack techniques to give teams immediate clarity on exploitable exposure.

- **Run the Rapid Response test:** Launch the test from NodeZero to determine whether exploitation is possible.
- **Patch immediately:** Apply the applicable Oracle October 2026 Critical Patch Update patches.
- **Re-run the test:** Verify that the vulnerability is no longer exploitable after remediation.

## **Affected Versions & Patch**

### Affected

Oracle Application Object Library in Oracle E-Business Suite versions **12.2.3 through 12.2.15**, inclusive.

### Fixed

Oracle addressed CVE-2026-101767 in its **October 2026 Critical Patch Update**, released on **October 20, 2026**.

Apply the patches applicable to your installation using the Oracle E-Business Suite patch availability documentation referenced in the advisory, **My Oracle Support Note KA923**.

### Mitigations

Until the applicable patches are installed:

- Remove `/OA_HTML/AppsTCFServer`, associated with `oracle.apps.fnd.tcf.SocketServer`, from the EBS URL firewall allowlist.
- Restrict access to the EBS web tier to trusted networks.
- Monitor the EBS application host and database for signs of compromise.

Apply access restrictions across all untrusted network paths to the servlet. These measures reduce exposure but do not replace patching.

### Indicators of Compromise:

- Unauthenticated POST requests to `/OA_HTML/AppsTCFServer` that instantiate the Gantt data-server class (`oracle.apps.jtf.gantt.server.GanttDataServer`), followed by backend database activity.
- SQL reconnaissance shortly after unauthenticated web requests (database version, current user, directory objects).
- Unexpected files in `$APPLPTMP` and the `oracle` account spawning `/bin/sh` via the Concurrent Manager to run OS commands.

## **Timeline**

- **July 24, 2026 Horizon3 Discloses Zero Day to Oracle.** Horizon3 Rapid Response customer assets are assessed and notified.
- **October 20, 2026:** Oracle published its October 2026 Critical Patch Update advisory and released security patches addressing CVE-2026-101767.
