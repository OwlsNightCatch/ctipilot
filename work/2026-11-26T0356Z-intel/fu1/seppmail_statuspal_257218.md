---
title: New Appliance Release 15.1.2
url: https://seppmail.statuspal.eu/info_notices/257218
hostname: statuspal.eu
description: SEPPmail's status page provides information on the current status and incident history of SEPPmail.
sitename: seppmail.statuspal.eu
date: "2026-11-25"
fingerprint: bb98cbd665e71cfb
language: en
filedate: "2026-11-26"
---
# New Appliance Release 15.1.2

### Updates

[Information](https://seppmail.statuspal.eu/info_notices/257218#activity-id-547278)

A new SEPPmail Appliance release has been published. Please see the [revision history](https://docs.seppmail.com/ch/20_revision-history.html) and the [extended release notes](https://downloads.seppmail.com/extrelnotes/151/ERN15.1.html) for further details.

## Patch release 15.1.2 (Released 2026-11-24)

### Background tasks

- Fixed an issue where a GINA satellite failed to send users and keys.

### CfgServer

- Fixed the S/MIME signature generation used to automatically trust domain certificates.

### Database

- Fixed an issue where an LDAP modification repeated previous changes when the same entry was modified again.

### Large files

- Fixed the handling of orphaned files during the cleanup of expired Large File Transfer data.

### Logging

- Added an export of the filtered mail log entries as a CSV file.
- Fixed the progress display while the database log cache is being rebuilt.

### Operating system

- Increased the size of the /etc partition to provide sufficient free space for configuration files.

### RestAPI

- The REST login now enforces the administrator MFA policy, answers all failed logins uniformly with HTTP 403, and records successful logins in the audit log.
- Values supplied by the client are now escaped in the LDAP search filters of several REST endpoints.

### Security

- **Affected versions:** \<15.1.2 - **CVE-ID:** [CVE-2026-124840](https://www.cve.org/CVERecord?id=CVE-2026-124840) - **CVSS Score:** 9.2
**Description:** In GINA, a session created by answering the security question was also accepted by the account registration and settings workflows. An attacker who knows the security answer could replace the password and take over the account.
**Fix Description:** Security question recovery now uses a separate session purpose that is only accepted by the recovery workflow.
- **Affected versions:** \<15.1.2 - **CVE-ID:** [CVE-2026-124843](https://www.cve.org/CVERecord?id=CVE-2026-124843) - **CVSS Score:** 9.2
**Description:** If the appliance-specific key material could not be loaded, a hard-coded fallback secret was used for cryptographic operations, which could allow encrypted Large File Transfer attachments to be decrypted outside the appliance.
**Fix Description:** Large File Transfer encryption no longer falls back to the hard-coded secret and is refused if the required key is not available.
- **Affected versions:** \<15.1.2 - **CVE-ID:** [CVE-2026-130637](https://www.cve.org/CVERecord?id=CVE-2026-130637) - **CVSS Score:** 9.3
**Description:** Request values reflected on the GINA login page were processed by the template engine, which could allow an unauthenticated attacker to read attributes of any GINA account and take it over.
**Fix Description:** Values supplied with the request are no longer expanded as template placeholders.
- **Affected versions:** \<15.1.2 - **CVE-ID:** [CVE-2026-124844](https://www.cve.org/CVERecord?id=CVE-2026-124844) - **CVSS Score:** 8.7
**Description:** Files uploaded to GINA by unauthenticated requests were not removed, which could allow an attacker to fill up the disk.
**Fix Description:** Uploads are limited to the maximum message size of the GINA domain, and upload files not used by the request are removed.
- **Affected versions:** \<15.1.2 - **CVE-ID:** [CVE-2026-124838](https://www.cve.org/CVERecord?id=CVE-2026-124838) - **CVSS Score:** 8.5
**Description:** The local socket of the configuration service was accessible to every local user, which could allow an attacker with local code execution to run commands with elevated privileges.
**Fix Description:** Access to the socket is restricted to authorized system accounts, and command data passed to the configuration service is now escaped.
- **Affected versions:** \<15.1.2 - **CVE-ID:** [CVE-2026-124842](https://www.cve.org/CVERecord?id=CVE-2026-124842) - **CVSS Score:** 8.3
**Description:** An unauthenticated GINA request could reset the password of a registered account without answering the security question.
**Fix Description:** The unauthenticated reset is now only executed for unregistered accounts; registered accounts must complete the configured reset procedure.
- **Affected versions:** \<15.1.2 - **CVE-ID:** [CVE-2026-124839](https://www.cve.org/CVERecord?id=CVE-2026-124839) - **CVSS Score:** 7.7
**Description:** A specially crafted GINA account address could lead to command execution with elevated privileges by a maintenance script during system start.
**Fix Description:** The account address is no longer passed to a shell command.
- **Affected versions:** \<15.1.2 - **CVE-ID:** [CVE-2026-124841](https://www.cve.org/CVERecord?id=CVE-2026-124841) - **CVSS Score:** 6.9
**Description:** Wildcard characters in account addresses were not escaped in LDAP lookups of GINA, which could cause a lookup to select a different account than intended.
**Fix Description:** All values used in these LDAP filters are now escaped.
- **Affected versions:** \<15.1.2 - **CVE-ID:** [CVE-2026-124836](https://www.cve.org/CVERecord?id=CVE-2026-124836) - **CVSS Score:** 6.3
**Description:** Values taken from a message were inserted into the LDAP filters of the ldap\_compare and ldap\_read rule commands without escaping, which could allow a sender to alter the result of an LDAP-based rule.
**Fix Description:** All message values substituted into these LDAP filters are now escaped.
- **Affected versions:** \<15.1.2 - **CVE-ID:** [CVE-2026-124837](https://www.cve.org/CVERecord?id=CVE-2026-124837) - **CVSS Score:** 6.3
**Description:** A specially crafted DKIM signature could inject forged authentication results into the Authentication-Results header, which were then covered by the ARC seal of the gateway.
**Fix Description:** Values copied from a DKIM signature into the Authentication-Results header are now validated.
- **Affected versions:** \<15.1.2 - **CVE-ID:** [CVE-2026-124845](https://www.cve.org/CVERecord?id=CVE-2026-124845) - **CVSS Score:** 6.3
**Description:** A client-supplied HTTP header could make the GINA domain lookup fail, so the request was processed with the \[default\] GINA domain settings instead of those of the requested domain.
**Fix Description:** Requests for a GINA domain that cannot be resolved are now rejected instead of falling back to the \[default\] domain.
- Added support for post-quantum key exchange groups such as X25519MLKEM768 to the web server TLS configuration.
- Hardened internal helper functions used for command execution.

### Webmail

- Fixed an issue where a GINA reply was sent twice if the Send button was clicked twice.

[← Back](https://seppmail.statuspal.eu)
