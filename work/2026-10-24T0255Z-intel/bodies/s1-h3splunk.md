---
title: Critical Splunk Enterprise Vulnerability
url: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-76268/
hostname: horizon3.ai
description: "CVE-2026-76268: A critical missing-authentication flaw in Splunk Enterprise could allow unauthenticated OS command execution. Review affected versions, exploit conditions, and patches."
sitename: Horizon3
date: "2026-10-22"
fingerprint: "6c82d514c2a491c3"
---
# CVE-2026-76268

## Splunk Enterprise Patroni REST API Missing Authentication Vulnerability

CVE-2026-76268 is a critical missing authentication vulnerability in Splunk Enterprise. An unauthenticated attacker with network access to the Patroni REST API on a search head cluster member could execute attacker-controlled operating-system commands. Splunk rates the vulnerability **9.8 (Critical) under CVSS v3.1**. Its advisory does not report active exploitation. [Splunk Vulnerability Disclosure](https://advisory.splunk.com/advisories/SVD-2026-1001) A public repository contains code presented as a proof of concept for this CVE. [GitHub](https://github.com/murrez/CVE-2026-76268)

## Technical Details

The vulnerability exists because the Patroni REST API does not require authentication for critical configuration operations. An attacker who can reach the affected interface on a search head cluster member could abuse those operations to execute operating-system commands.

- **Weakness:** CWE-306, Missing Authentication for Critical Function.
- **Attack vector:** Network access to the affected Patroni REST API.
- **Authentication:** No credentials or existing privileges required.
- **User interaction:** None required.
- **Impact:** Operating-system command execution, with potentially high impact to confidentiality, integrity, and availability.
- **CVSS v3.1:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H

Internet exposure is not required. An attacker with internal network access to the affected interface could also exploit the vulnerability.

### Stop Guessing, Start Proving

## NodeZero® Proactive Security Platform Rapid Response

A NodeZero Rapid Response test has been developed to safely validate whether this vulnerability can be exploited in your environment. The test executes real attack techniques without causing damage, giving teams immediate clarity on exposure.

- **Run the Rapid Response test:** Launch from the NodeZero platform to determine whether exploitation is possible.
- **Patch immediately:** Upgrade to a fixed version or apply the vendor-recommended workaround where appropriate.
- **Re-run the test:** Verify that the vulnerability is no longer exploitable after remediation.

## Affected versions & patch

### Affected

- Splunk Enterprise **10.4.0 through 10.4.2**.
- Splunk Enterprise **10.2.0 through 10.2.6**.

Splunk Enterprise **10.0.x and 9.4.x are not affected by this CVE**.

### Fixed

- Splunk Enterprise **10.4.3 or later in the 10.4 branch**.
- Splunk Enterprise **10.2.7 or later in the 10.2 branch**.

### Mitigations

If you cannot immediately upgrade and **do not use Edge Processor, OpAmp, or SPL2 data pipelines**, Splunk recommends disabling the PostgreSQL sidecar.

In $SPLUNK\_HOME/etc/system/local/server.conf, set:

```
[postgres]
disabled = true
```
Restart Splunk Enterprise to apply the change. Use this workaround only when the listed features are unused.

## Timeline

- **October 7, 2026:** Splunk published advisory SVD-2026-1001, identifying the vulnerability and fixed versions 10.4.3 and 10.2.7. 
- **October 7, 2026:** The CVE record was published.
- **\[Month Day, 2026\]:** Horizon3 released the NodeZero Rapid Response test for CVE-2026-76268.
