---
title: "15.1.2 Patch Release"
url: https://downloads.seppmail.com/extrelnotes/151/ERN15.1.html
hostname: seppmail.com
sitename: downloads.seppmail.com
date: "2026-09-28"
fingerprint: a890ef12c16d98fb
filedate: "2026-11-26"
---
*Tip: All changes are tracked in the Gateway documentation, see [the information in the last row of the documentation agreement](https://docs.seppmail.com/en/02_intro_01_documentation-agreements.html).*

For the latest 15.0 releases, see [https://downloads.seppmail.com/extrelnotes/150/ERN15.0.html](https://downloads.seppmail.com/extrelnotes/150/ERN15.0.html)

For the latest 14.1 releases, see [https://downloads.seppmail.com/extrelnotes/141/ERN14.1.html](https://downloads.seppmail.com/extrelnotes/141/ERN14.1.html)

For the latest 14.0 releases, see [https://downloads.seppmail.com/extrelnotes/140/ERN14.0.html](https://downloads.seppmail.com/extrelnotes/140/ERN14.0.html)

For the latest 13.1 releases, see [https://downloads.seppmail.com/extrelnotes/131/ERN13.1.html](https://downloads.seppmail.com/extrelnotes/131/ERN13.1.html)

> **SEPPMAIL Gateway news via Statuspal** As of July 2025, SEPPMAIL Secure E-Mail Gateway customers and partners can register for Statuspal messages under the link [https://seppmail.statuspal.eu/#subscribe](https://seppmail.statuspal.eu/#subscribe). Information about the Gateway is now also published here.


- **Internal Reference:** 65639
- **Issue Type:** Bug
- **Docs Link:** none

An error in a script that processes user data in satellite systems meant that the correct exchange of this data was no longer working. This has been fixed now.

- **Issue Type:** Bug
- **Docs Link:** none

There was an error in the code for the automatic issuance and trust setup of domain certificates, which prevented automatic processing on the update servers. This has been fixed now.

- **Issue Type:** Maintenance
- **Docs Link:** none

There was a bug which meant that, in certain situations, modifications to the LDAP were reapplied when the LDAP entry was reused. This has been fixed now.

An error in the script designed to clean up orphaned LFM files caused a number of errors that prevented this task from being carried out. This has been fixed now.

- **Internal Reference:** 66073
- **Issue Type:** Bug
- **Docs Link:** none

CC recipients were not included in the log view. This has been fixed now.

- **Internal Reference:** 48486
- **Issue Type:** Feature
- **Docs Link:** [Log View Filter](https://docs.seppmail.com/en/07_mi_13_logs.html)

It is now possible to export the log view (for file based and DB based logging) via a new "Export CSV..." button. The export will contain all shown/filtered entries.

*Export CSV...*

An error prevented the progress of the DB based log cache build from being displayed correctly. This has been fixed now.

- **Issue Type:** Task
- **Docs Link:** none

In some cases, the /etc partition had been set up too small, which occasionally led to problems because configuration files could not be written to it. This has been fixed now.

In this ticket, the REST API was modified to invalidate user API tokens after the timeout period configured for the admin GUI

The REST endpoint for authentication (/auth) now also respects the MFA settings and logs the login attempts accordingly in the audit log.

In some REST endpoints, additional LDAP filter values have been escaped so that LDAP filter injection is no longer possible.

- **Issue Type:** Vulnerability
- **Docs Link:** none

Internal helper functions used for command execution have been hardened.

- **Issue Type:** Feature
- **Docs Link:** [GINA Domain Settings](https://docs.seppmail.com/en/07_mi_17_gd__gina-domains.html#s_tlssettings)

The "Curves" setting under GINA Domains was renamed to "Groups". There it is now possible to select groups with post quantum support like X25519MLKEM768.

*Groups setting in GINA Domains*

- **Issue Type:** Vulnerability
- **Affected versions:** \<15.1.2
- **CVE-ID:** [CVE-2026-124840](https://www.cve.org/CVERecord?id=CVE-2026-124840)
- **CVSS Score:** 9.2
- **Description:** In GINA, a session created by answering the security question was also accepted by the account registration and settings workflows. An attacker who knows the security answer could replace the password and take over the account.
- **Fix Description:** Security question recovery now uses a separate session purpose that is only accepted by the recovery workflow.

- **Issue Type:** Vulnerability
- **Affected versions:** \<15.1.2
- **CVE-ID:** [CVE-2026-124843](https://www.cve.org/CVERecord?id=CVE-2026-124843)
- **CVSS Score:** 9.2
- **Description:** If the appliance-specific key material could not be loaded, a hard-coded fallback secret was used for cryptographic operations, which could allow encrypted Large File Transfer attachments to be decrypted outside the appliance.
- **Fix Description:** Large File Transfer encryption no longer falls back to the hard-coded secret and is refused if the required key is not available.

- **Issue Type:** Vulnerability
- **Internal reference:** 66289
- **Affected versions:** \<15.1.2
- **CVE-ID:** [CVE-2026-130637](https://www.cve.org/CVERecord?id=CVE-2026-130637)
- **CVSS Score:** 9.3
- **Description:** Request values reflected on the GINA login page were processed by the template engine, which could allow an unauthenticated attacker to read attributes of any GINA account and take it over.
- **Fix Description:** Values supplied with the request are no longer expanded as template placeholders.

- **Issue Type:** Vulnerability
- **Affected versions:** \<15.1.2
- **CVE-ID:** [CVE-2026-124844](https://www.cve.org/CVERecord?id=CVE-2026-124844)
- **CVSS Score:** 8.7
- **Description:** Files uploaded to GINA by unauthenticated requests were not removed, which could allow an attacker to fill up the disk.
- **Fix Description:** Uploads are limited to the maximum message size of the GINA domain, and upload files not used by the request are removed.

- **Issue Type:** Vulnerability
- **Affected versions:** \<15.1.2
- **CVE-ID:** [CVE-2026-124838](https://www.cve.org/CVERecord?id=CVE-2026-124838)
- **CVSS Score:** 8.5
- **Description:** The local socket of the configuration service was accessible to every local user, which could allow an attacker with local code execution to run commands with elevated privileges.
- **Fix Description:** Access to the socket is restricted to authorized system accounts, and command data passed to the configuration service is now escaped.

- **Issue Type:** Vulnerability
- **Affected versions:** \<15.1.2
- **CVE-ID:** [CVE-2026-124842](https://www.cve.org/CVERecord?id=CVE-2026-124842)
- **CVSS Score:** 8.3
- **Description:** An unauthenticated GINA request could reset the password of a registered account without answering the security question.
- **Fix Description:** The unauthenticated reset is now only executed for unregistered accounts; registered accounts must complete the configured reset procedure.

- **Issue Type:** Vulnerability
- **Affected versions:** \<15.1.2
- **CVE-ID:** [CVE-2026-124839](https://www.cve.org/CVERecord?id=CVE-2026-124839)
- **CVSS Score:** 7.7
- **Description:** A specially crafted GINA account address could lead to command execution with elevated privileges by a maintenance script during system start.
- **Fix Description:** The account address is no longer passed to a shell command.

- **Issue Type:** Vulnerability
- **Affected versions:** \<15.1.2
- **CVE-ID:** [CVE-2026-124841](https://www.cve.org/CVERecord?id=CVE-2026-124841)
- **CVSS Score:** 6.9
- **Description:** Wildcard characters in account addresses were not escaped in LDAP lookups of GINA, which could cause a lookup to select a different account than intended.
- **Fix Description:** All values used in these LDAP filters are now escaped.

- **Issue Type:** Vulnerability
- **Affected versions:** \<15.1.2
- **CVE-ID:** [CVE-2026-124836](https://www.cve.org/CVERecord?id=CVE-2026-124836)
- **CVSS Score:** 6.3
- **Description:** Values taken from a message were inserted into the LDAP filters of the ldap\_compare and ldap\_read rule commands without escaping, which could allow a sender to alter the result of an LDAP-based rule.
- **Fix Description:** All message values substituted into these LDAP filters are now escaped.

- **Issue Type:** Vulnerability
- **Affected versions:** \<15.1.2
- **CVE-ID:** [CVE-2026-124837](https://www.cve.org/CVERecord?id=CVE-2026-124837)
- **CVSS Score:** 6.3
- **Description:** A specially crafted DKIM signature could inject forged authentication results into the Authentication-Results header, which were then covered by the ARC seal of the gateway.
- **Fix Description:** Values copied from a DKIM signature into the Authentication-Results header are now validated.

- **Issue Type:** Vulnerability
- **Affected versions:** \<15.1.2
- **CVE-ID:** [CVE-2026-124845](https://www.cve.org/CVERecord?id=CVE-2026-124845)
- **CVSS Score:** 6.3
- **Description:** A client-supplied HTTP header could make the GINA domain lookup fail, so the request was processed with the \[default\] GINA domain settings instead of those of the requested domain.
- **Fix Description:** Requests for a GINA domain that cannot be resolved are now rejected instead of falling back to the \[default\] domain.

In the GINA GUI, it was possible for a user to click the "Send" button several times, thereby triggering the email multiple times. This then caused problems in the Rule Engine, as the second email could no longer access the necessary data because the first one had already cleared the data behind it. This has been fixed now.

After creating a managed domain, the page for editing the domain opens automatically. Due to an error, the page did not load correctly, meaning it was not possible to customise the domain. This has been fixed now.

- **Internal Reference:** 64886
- **Issue Type:** Bug
- **Docs Link:** none

The HTML preview function for templates and disclaimers in the admin GUI had stopped working. This has been fixed now.

Fixed an issue where disclaimer and template configuration JSON files were not written in UTF-8 encoding, which could corrupt special characters. Everything is now in UTF-8.

Added a system configuration option in system.conf to disable the collection of customer summary data, which can take a long time on large installations.

Until now, it was not possible to import a standard backup of a multi-customer system as a new customer onto another system. This is now possible.

Up to now, we have only had the maintenance node in a cluster create and send a database backup. This carries the risk that, if that backup is corrupted, another cluster node would still have a backup available. Now, each node creates a backup again, but only the maintenance node sends it via email.

- **Internal Reference:** 65345
- **Issue Type:** Bug
- **Docs Link:** none

In version 15.1.0, we introduced a feature to send warning emails if the backup could not be sent. As some customers download the backup via SCP and have therefore not set up any backup operators, they were receiving these warning emails due to the absence of backup operators. We are now able to recognise this situation and will refrain from sending warning emails if SCP backup is configured and no backup operators have been set up.

We have reduced the maximum size of the code dumps to be written to 5 MB. This prevents the /tmp partition from being flooded with core files when a relevant error occurs, while still allowing us to detect it.

- **Internal Reference:** 64604
- **Issue Type:**
- **Docs Link:** none

The Content-ID headers of disclaimer inline images and attachments are now RFC 2045 compliant.

- Updated OpenSSL to version 3.5.9
- Updated OpenSSH to version 10.6

Added error handling so the database logging page loads correctly even if a log entry contains empty data.

- **Internal Reference:** 65463
- **Issue Type:** Bug
- **Docs Link:** none

Fixed an issue where rotated mail log files could not be viewed and rebuilding the mail log archive index caused errors.

A bug in the code meant that temporary files were not deleted during mail log indexing, which resulted in the /tmp partition becoming full for customers with a very large number of mail logs whenever everything had to be re-indexed. This has been fixed now.

Adapted the D-Trust MPKI connector to the new connector specification 2.28.

Fixed an issue where the SwissSignREST MPKI connector settings were not loaded in the Admin GUI.

- **Issue Type:**
- **Docs Link:** none

Updated the GlobalSign root CA certificate chain so that GlobalSign certificates can be issued correctly.

Certificate orders via the SwissSignREST connector that are not issued in time are now kept as pending requests and completed later, preventing duplicate certificates.

Fixed a regression where external DNS names could no longer be resolved after a local DNS zone was configured with the built-in DNS resolver. Specifically, the root anchor key for DNSSEC had been updated/replaced. We are now ensuring that it is reloaded.

Fixed an issue in the OpenBSD kernel that prevented hard disks from being detected on Azure systems.

Fixed the error handling of PUT /v1/ssl, which returned an internal server error instead of the actual error message.

Fixed PUT /webmail/domain/{domainName} failing with an internal server error when "Initial password via SMS" is enabled.

If signing or encryption is requested and no key material exists, a key or certificate is now generated automatically (and a local user created if necessary) instead of bouncing the message, provided automatic key generation and user creation are enabled.

In the RuleSet function `make_lft`, there was an issue when the email to be processed contained recipients for whom LFT was permitted and others for whom it was not. This has now been fixed.

If "Delete expired certificates automatically" and "Automatically check revocation status every day" are enabled, revoked certificates are now deleted automatically as well.

Fixed an issue where the result of a CRL check did not override the OCSP check result, so revoked certificates were not marked as revoked.

- **Issue Type:** Vulnerability
- **Affected versions:** \<15.1.1
- **CVE-ID:** [CVE-2026-114424](https://www.cve.org/CVERecord?id=CVE-2026-114424)
- **CVSS Score:** 9.2
- **Description:** Improper handling of replacement values in address replacement rules could allow a remote sender to execute arbitrary commands on the appliance if a ruleset uses values taken from the message as replacement.
- **Fix Description:** The evaluation of replacement values in address replacement rules was hardened to prevent code execution.

- **Issue Type:** Vulnerability
- **Affected versions:** \<15.1.1
- **CVE-ID:** [CVE-2026-114425](https://www.cve.org/CVERecord?id=CVE-2026-114425)
- **CVSS Score:** 9.2
- **Description:** Specially crafted attachment metadata in an incoming message could cause the Large File Transfer processing to read or delete arbitrary files on the appliance.
- **Fix Description:** Attachment metadata received with a message is now validated before any file is accessed.

- **Issue Type:** Vulnerability
- **Affected versions:** \<15.1.1
- **CVE-ID:** [CVE-2026-114421](https://www.cve.org/CVERecord?id=CVE-2026-114421)
- **CVSS Score:** 6.9
- **Description:** Insufficient input escaping in account lookups combined with missing validation in the password recovery process could allow an unauthenticated attacker to discover GINA accounts without a password and take them over.
- **Fix Description:** LDAP filter values are now escaped, and the password recovery only asks registered users with configured security questions.

- **Issue Type:** Vulnerability
- **Affected versions:** \<15.1.1
- **CVE-ID:** [CVE-2026-114420](https://www.cve.org/CVERecord?id=CVE-2026-114420)
- **CVSS Score:** 8.3
- **Description:** Insufficient input escaping in account lookups combined with missing validation in the password recovery process could allow an unauthenticated attacker to discover GINA accounts without a password and take them over.
- **Fix Description:** LDAP filter values are now escaped, and the password recovery only asks registered users with configured security questions.

- **Issue Type:** Vulnerability
- **Affected versions:** \<15.1.1
- **CVE-ID:** [CVE-2026-114426](https://www.cve.org/CVERecord?id=CVE-2026-114426)
- **CVSS Score:** 8.7
- **Description:** The file upload interface processed request data before checking authentication, which could allow an unauthenticated attacker to exhaust disk space and worker processes.
- **Fix Description:** Authentication is now checked before upload data is processed, and the upload size is limited.

From version 15.1.1 onwards, we will only support self-signed PGP keys, and the use of third-party-signed keys will be disabled.

PGP messages that are not actually encrypted (NULL encryption) are now detected and no longer marked as encrypted.

We have implemented support for the QEMU Guest Agent (qemu-ga). This requires only a serial interface.

- **Internal Reference:** 65183
- **Issue Type:** Bug
- **Docs Link:** none

Fixed an issue where GINA read receipts were only sent for the first recipient of a message sent to multiple recipients.

**With this release, the GINAv2 beta phase ends, and the GINAv2 options have been removed from the GINA domain settings. The final version of GINAv2 is nearly complete and will be released soon.**

- **Release Date:** September 29th, 2026
- **SEPPMAIL version:** 15.1.0.1
- **Author:** Birgit Grossmann
- [15.1.0.1 Hotfix Release](https://downloads.seppmail.com/extrelnotes/151/ERN15.1.html#15101-hotfix-release)

Fixed internal server error in edit GINA domain page.

- **Release Date:** September 28th, 2026
- **SEPPMAIL version:** 15.1
- **Author:** Birgit Grossmann
- [15.1 Feature Release](https://downloads.seppmail.com/extrelnotes/151/ERN15.1.html#151-feature-release)

- **Internal Reference:** 10498
- **Issue Type:** Maintenance
- **Docs Link:** [Key Server](https://docs.seppmail.com/en/07_mi_07_mp__mail-processing.html#rg_keyserver)

It is now possible to test one or all key server connections in the Mail Processing settings.

*Test connection(s)*

In the past we saw sometimes that the LDAP size increased very fast without any reason. To prevent a complete loss of the DB, we now implemented a bloating detection to warn the admin that something might be broken with the LDAP.

- **Internal Reference:** 50293
- **Issue Type:** Feature
- **Docs Link:** [Visible sections for this customer](https://docs.seppmail.com/en/07_mi_24_cust_01_cec__create-newedit-settings-for-customer.html#ca_visiblesectionsforthiscustomer)

It is now possible to restrict the sections/menus accessible for customer admins. The feature is configured in the Customer Management "Edit settings for customer '\<customername>' ".

*Edit settings for customer '\<customername>'*

*Example for a restricted menu view*

The appliance now also checks the LFM partition regarding the used space. The admin will get a watchdog warning if the LFM partition is over 85% full.

- **Internal Reference:** 61609
- **Issue Type:** Feature
- **Docs Link:** [Notification mails for expirations](https://docs.seppmail.com/en/07_mi_21_certs_03_advanced-settings.html#as_notification)

This feature makes it possible to actively send notification mails to external users if their public S/MIME certificate is going to expire, with the request to send us a mail signed with their new S/MIME cert so we can collect it. For the notification mail there are a number of new templates. The admin can create new templates but has to follow the naming convention "cert\_expiry\_notify\_\<2 char country code>".

*Advanced Settings*

*New default mail templates in Mail System*

*Example notification mail*

- **Internal Reference:** 58065
- **Issue Type:** Maintenance
- **Docs Link:** none

If the creation and/or sending of a backup during the nightly backup fails, we will now add a notification to the admin GUI and add this warning to the daily digest.

In the past we used an openssl shell call for the revocation test against a CRL. Now we use direct Perl code which makes the calls faster and less resource-intensive.

- **Internal Reference:** 59182
- **Issue Type:** Maintenance
- **Docs Link:** none

The appliance now also does an audit for all RestAPI calls modifying any data. This gives us the possibility to analyze who added, changed or deleted any data via RestAPI.

A value was missing from the smimeKeyType enumeration in the REST API OpenAPI schema. This resulted in a schema validation error when retrieving a list of certificates if any of them had this missing smimeKeyType. This has been fixed now.

- **Internal Reference:** 53253
- **Issue Type:** Feature
- **Docs Link:** [PostgreSQL setting in Mail Processing](https://docs.seppmail.com/en/07_mi_07_mp__mail-processing.html#postgresqlclient) and [Rule Engine Documentation: Access To external PostgreSQL databases](https://docs.seppmail.com/en/08_cr_07_psql__access-to-external-postgres-databases.html)

It is now possible to access Postgres from the Rule Engine. For this, a configuration file has to be uploaded in the Mail Processing. See the linked Rule Engine documentation for more details.

*Setting without uploaded PostgreSQL configuration*

*Setting with uploaded PostgreSQL configuration*

- **Issue Type:** Feature
- **Docs Link:** none

Starting with 15.1.0 we will add the X-SM-Actions header to every mail processed by SEPPMAIL. We will use this header later in the Outlook AddIn to do a categorization for incoming mail.

This header is also part of the DKIM and ARC signature so a manipulation will be detected. The header will also be deleted before the Rule Engine processes the mail.

To make the code more secure against command injections, we now always use argument escaping whenever we hand over an argument to a shell call.

- **Issue Type:** Security
- **Docs Link:** none

In one of the Emposo findings it was possible to inject JavaScript code in the Admin GUI via a manipulated Message-ID. We fixed it and added some more mechanisms to prevent this kind of attack.

This is one of the Emposo findings. It was possible for a RestAPI token without MSP privileges to add, change or delete RootCA certificates. Now only MSP token are allowed to do so.

- **Internal Reference:** 64911
- **Issue Type:** Bug
- **Docs Link:** none

There was a bug in the CSS parsing software when handling the attributes of a CSS class that were already specified. This lead to a situation where both attribute values were written to the secure-email.html. This has been fixed now.

- **Internal Reference:** 45475
- **Issue Type:** Feature
- **Docs Link:** [Restrict mail attachments to configured MIME types](https://docs.seppmail.com/en/07_mi_17_gd_02_cgs__change-gina-settings-for.html#es_restrictmailattachmentstoconfiguredmimetypes)

In the GINA Domain settings in the "Write GINA Email" section it is now possible to restrict the file types of uploaded attachments. These follow the same rules as the type parameter of the partoftype() RuleSet function.

*Restrict mail attachments to configured MIME types*

--- end of document ---
