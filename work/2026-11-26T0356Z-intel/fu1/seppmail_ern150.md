---
title: "15.0.7 Bugfix Release"
author: Vuln Missing Authorization
url: https://downloads.seppmail.com/extrelnotes/150/ERN15.0.html
hostname: seppmail.com
sitename: downloads.seppmail.com
date: "2025-11-04"
fingerprint: e0c46e12d565b039
filedate: "2026-11-26"
---
*Tip: All changes are tracked in the Gateway documentation, see [the information in the last row of the documentation agreement](https://docs.seppmail.com/en/02_intro_01_documentation-agreements.html).*

For the latest 14.1 releases, see [https://downloads.seppmail.com/extrelnotes/141/ERN14.1.html](https://downloads.seppmail.com/extrelnotes/141/ERN14.1.html)

For the latest 14.0 releases, see [https://downloads.seppmail.com/extrelnotes/140/ERN14.0.html](https://downloads.seppmail.com/extrelnotes/140/ERN14.0.html)

For the latest 13.1 releases, see [https://downloads.seppmail.com/extrelnotes/131/ERN13.1.html](https://downloads.seppmail.com/extrelnotes/131/ERN13.1.html)

> **SEPPMAIL Gateway news via Statuspal** As of July 2025, SEPPMAIL Secure E-Mail Gateway customers and partners can register for Statuspal messages under the link [https://seppmail.statuspal.eu/#subscribe](https://seppmail.statuspal.eu/#subscribe). Information about the Gateway is now also published here.


- **Release Date:** September 2th, 2026
- **SEPPMAIL version:** 15.0.7
- **Author:** Birgit Grossmann
- [15.0.7 Bugfix Release](https://downloads.seppmail.com/extrelnotes/150/ERN15.0.html#1507-bugfix-release)

- **Internal Reference:** 64063
- **Issue Type:** Maintenance
- **Docs Link:** none

Fixed an issue that could prevent a local user from being deleted when associated certificate revocation was processed.

- **Internal Reference:** 63328
- **Issue Type:** Maintenance
- **Docs Link:** none

Fixed an issue that prevented time zone settings from being changed or saved correctly.

- **Issue Type:** Maintenance
- **Docs Link:** none

Improved handling and logging of previously running background processes. This prevents overlapping processes from contributing to excessive resource consumption and system instability.

- **Internal Reference:** 63328
- **Issue Type:** Bug
- **Docs Link:** none

- **Issue Type:** Bug
- **Docs Link:** none

Fixed an issue in the connector.pl service which failed to stop first run injection connections.

- **Internal Reference:** 63155
- **Issue Type:** Bug
- **Docs Link:** none

Updated SSH-related configuration and warning handling to avoid unnecessary warnings when displaying cluster member status.

Corrected the API documentation so requests generated according to the specification are accepted as expected.

Corrected temporary directory handling to ensure required processing data remains available while the Rule Engine instance is in use.

- **Internal Reference:** 63349
- **Issue Type:** Maintenance
- **Docs Link:** none

Fixed an issue where generated LFT messages could be missing encrypted attachments due to incorrect output directory handling.

- **Internal Reference:** 63491
- **Issue Type:** Bug
- **Docs Link:** none

Improved logging to provide a clearer explanation when a revocation check is intentionally skipped.

- **Affected versions:** \<15.0.7
- **CVE-ID:** [CVE-2026-84830](https://www.cve.org/CVERecord?id=CVE-2026-84830)
- **CVSS Score:** 8.6
- **Description:** SEPPMAIL Secure Email Gateway before 15.0.7 contains a command injection vulnerability that allows authenticated administrators to execute commands with elevated privileges.
- **Fix Description:** All affected values will be escaped not.

- **Internal Reference:** SEC-100
- **Affected versions:** \<15.0.7
- **CVE-ID:** pending
- **CVSS Score:** 7.7
- **Description:** Under certain conditions, the authentication process could allow a user to gain access before all required multi-factor authentication steps had been completed.
- **Fix Description:** The authentication flow was tightened to ensure all required MFA checks are completed before access is granted.

- **Internal Reference:** SEC-99
- **Affected versions:** \<15.0.6
- **CVE-ID:** pending
- **CVSS Score:** 8.6
- **Description:** A vulnerability in the processing of specially crafted input could potentially lead to unintended command execution in the affected component.
- **Fix Description:** Additional validation and safer command-handling mechanisms were introduced to prevent malicious input from being executed.

Corrected an issue where cached webmail data could be validated using an incorrect value, potentially preventing it from being processed correctly.

Corrected session handling where certain values were not applied as expected, which could cause a session to remain in an incorrect state.

- **Release Date:** July 22th, 2026
- **SEPPMAIL version:** 15.0.6.1
- **Author:** Birgit Grossmann
- [15.0.6.1 Hotfix Release](https://downloads.seppmail.com/extrelnotes/150/ERN15.0.html#15061-hotfix-release)

- **Internal Reference:** 63115
- **Issue Type:** Bug
- **Docs Link:** none

An undefined value in the message object meant that log messages were no longer being written to the mailog. This has been fixed now.

- **Internal Reference:** 63128
- **Issue Type:** Bug
- **Docs Link:** none

For archived emails, the direction of the emails was not recognised, as this can change due to the new archive recipient compared with the original email. This has been fixed now.

- **Internal Reference:** 61880
- **Issue Type:** Bug
- **Docs Link:** [Time zone setting](https://docs.seppmail.com/en/07_mi_05_system.html#tz_timezoneselection)

In certain scenarios, it could happen that no valid time zone was configured, which led to various problems. Now, time zone "Europe/Zurich" is always used as fallback.

- **Internal Reference:** 61434
- **Issue Type:** Maintenance
- **Docs Link:** none

Since the latest version, the data specified under System > Comment has been correctly passed to the SNMP data. As a result, the value specified under ObjectID must now be an OID, and values that did not correspond to an OID previously prevented the SNMP service from running. We have now implemented both validation of the entered data and validation prior to transmission to SNMP, so that this issue no longer occurs.

- **Internal Reference:** 60013
- **Issue Type:** Feature
- **Docs Link:** [MPKI Trigger AutoRenew, for all MPKI connectors available](https://docs.seppmail.com/en/07_mi_10_mpki_03_digicert.html#s_triggerautorenew)

In the MPKI Connector Settings for Auto Renew, there is now a button labelled "Trigger AutoRenew...". This way, customers no longer have to wait until 10 pm for the renewal to be triggered and can initiate it themselves.

*MPKI Trigger AutoRenew*

- **Internal Reference:** 58159
- **Issue Type:** Feature
- **Docs Link:** [External Authentication for Users](https://docs.seppmail.com/en/07_mi_15_usr_04_advanced-settings.html#externalauthentication)

Under User > Advanced Settings, there is now an External Authentication section. Here, you can configure the Admin GUI to authenticate against an external LDAP server and set up the mapping of external AD groups to the appliance’s local groups.

Users authenticated externally are visible locally and behave in the same way as local users. The only difference is that their password cannot be changed, as this is set in the external LDAP server.

*External Authentication section*

- **Internal Reference:** 40648
- **Issue Type:** Feature
- **Docs Link:** [Login](https://docs.seppmail.com/en/07_mi_03_login-logout.html)

Previously, when logging in to the admin GUI, the second factor had to be entered after the password, which some customers found inconvenient and which also did not correspond to standard login practice. Now, the second factor is requested separately after login.

*MFA Code is entered separately*

- **Internal Reference:** 62253
- **Issue Type:** Bug
- **Docs Link:** none

It may happen that the check to see if the database is faulty does not report any errors, yet the database is still faulty and the system is unable to create a daily snapshot. We have now implemented an additional test, which triggers a corresponding error message via the watchdog, to detect such situations.

- **Internal Reference:** 61888
- **Issue Type:** Bug
- **Docs Link:** none

In the latest version, we have introduced a new hash algorithm for passwords. When a user logs in for the first time, we now rehash the password so that it is generated using the new hash algorithm.

However, this has caused a problem. If a cluster is updated, the update is carried out on the first member and the user logs in after the update has been successfully completed, the password is rehashed. Consequently, it is not possible to log in to the other cluster members, as they do not (yet) support the new hashing algorithm. Because the user can no longer log in, they are also unable to install an update which could resolve the problem.

We have now implemented a mechanism for future use which checks whether all appliances in the cluster are running the same version; only then is the password rehashed.

- **Internal Reference:** 61853
- **Issue Type:** Bug
- **Docs Link:** none

A bug in the latest version listed the IP addresses of the CARP interface as the IP addresses of the cluster members using it. As a result, it was subsequently no longer possible to configure the IP addresses of the cluster members, as the system assumed that the desired IP addresses had already been assigned. However, these were in fact the CARP IPs, which are the same on every cluster member. This has been fixed now.

update to OpenSSH to 10.4 to fix a list of security findings

update to OpenSSL version 3.0.21 to fix a list of security findings:

- **Internal Reference:** 62852
- **Issue Type:** Bug
- **Docs Link:** none

There was a problem with refreshing the Maillog cache, which is used for database-based logging. If the last refresh was still running when a new one was triggered, both would run simultaneously and interfere with each other in an undesirable way. This has now been resolved to ensure that the old process is terminated properly.

- **Internal Reference:** 62737
- **Issue Type:** Bug
- **Docs Link:** none

Until now, the incorrect size was being logged for LFT emails. This surprised some customers, as the size logged should not actually have triggered an LFT message. The size is now displayed correctly.

- **Internal Reference:** 57170
- **Issue Type:** Maintenance
- **Docs Link:** none

There were potentially confusing log lines like

```
Header 'X-ESWmail-LFM' does not exists - skip and return false
```
These are now only output on debug level in development.

- **Internal Reference:** 20396
- **Issue Type:** Bug
- **Docs Link:** none

When sorting the mail logs by date, a string comparison was carried out previously, which resulted in the sorting being rather meaningless in relation to the date. It is now sorted correctly.

- **Internal Reference:** 62882
- **Issue Type:** Bug
- **Docs Link:** none

An exception occurred in the RuleEngine if a Subject header was encoded as cp367 and this header was to be modified. This was due to the Perl encoding function for this character set. A fallback has now been implemented.

- **Internal Reference:** 61658
- **Issue Type:** Bug
- **Docs Link:** none

With the CertCentral MPKI Connector, there was an issue whereby an incorrect API key or an incorrect response from CertCentral meant that the page was no longer displayed in the admin GUI, making it impossible to correct the settings. Error handling has now been improved.

- **Internal Reference:** 63068
- **Issue Type:** Bug
- **Docs Link:** none

There was a minor bug in the RestAPI that became apparent when retrieving a CSR via the /ssl/csr endpoint. This has been fixed now.

- **Internal Reference:** 62316
- **Issue Type:** Bug
- **Docs Link:** none

In the /crypto/domain/{domainName} REST endpoint, an error occurred when saving to the database while uploading an external/public domain certificate. This has been fixed now.

- **Internal Reference:** 61848
- **Issue Type:** Maintenance
- **Docs Link:** none

As in larger installations with many entries, some requests may take quite a long time to complete, the timeout for REST calls has been increased from 300 to 900 seconds.

- **Internal Reference:** 61550
- **Issue Type:** Bug
- **Docs Link:** none

With the REST API, the problem was that you couldn’t apply the system settings because the endpoint did not allow that operation. This has been fixed now.

- **Internal Reference:** 61521
- **Issue Type:** Bug
- **Docs Link:** none

In the REST endpoint /system/ifaliasconfig, there was a problem when certain values were "undef" (specifically observed in the password field). This has been fixed now.

- **Internal Reference:** 62584
- **Issue Type:** Bug
- **Docs Link:** none

Following the switch to Sequoia GPG, an issue arose where non-standard PGP encryption could not be decrypted because no integrity data was available. We are now carrying out internal tests on such encryption and ignoring the integrity issues, as this integrity is not present anyway.

- **Internal Reference:** 62407
- **Issue Type:** Bug
- **Docs Link:** none

Until now, archived emails have been sent directly without any further processing. This means that no ARC signature is attached to the emails, which causes problems in the M365 environment, as these emails are rejected there. From now on, we will send the archived emails via the standard "deliver()" mechanism, ensuring that the emails are signed correctly.

- **Internal Reference:** 27196
- **Issue Type:** Bug
- **Docs Link:** none

Until now, there has been an issue with the requested signing of emails. If the automatic creation of users was disabled (meaning that key material was not automatically generated either), and the settings "Sign all outgoing emails if S/MIME certificate available" and "S/MIME sign outgoing emails with the following text in the subject" were enabled, and the sender included a corresponding tag in the subject line for signing, no signature was added if the user did not possess any key material. This was the case even though the signature had been requested in the subject line.

Now, such emails are bounced if signing was requested but was not possible.

- **Internal Reference:** 62855
- **Issue Type:** Bug
- **Docs Link:** none

In the GINA GUI, there was a situation where, if you replied to an email and uploaded an attachment, the last "To" field would disappear and you would no longer be able to enter any further email addresses. This has been fixed now.

- **Internal Reference:** 61937
- **Issue Type:** Bug
- **Docs Link:** none

In the latest version, the hashencrypt function was switched to AES-256-CBC with PBKDF2. In the process, a bug was introduced which, in certain situations, reported that decryption had been successful even though this was not the case, and the user saw a blank page in the GINA GUI. This has been fixed now.

- **Internal Reference:** 58870
- **Issue Type:** Bug
- **Docs Link:** none

An incorrect evaluation of an argument meant that unregistered GINA accounts were no longer automatically deleted. This has been fixed now.

- **Internal Reference:** 59634
- **Issue Type:** Bug
- **Docs Link:** none

In the detailed view for S/MIME certificates, an error occurred when attempting to view a CSR instead of an X.509 certificate. This has been fixed now.

- **Internal Reference:** 58876
- **Issue Type:** Maintenance
- **Docs Link:** none

Previously, it was possible to import any certificate into a GINA domain after creating a CSR, even if it did not match the CSR. This led to problems because the key material did not match. This is now checked.

- **Internal Reference:** 60306
- **Issue Type:** Bug
- **Docs Link:** none

Due to an unusable LDAP attribute, it was not possible to change the password for the "admin" user after the initial login. This has been fixed now.

- **Internal Reference:** 60341
- **Issue Type:** Maintenance
- **Docs Link:** [Use DHCP settings](https://docs.seppmail.com/en/07_mi_05_system.html#dns_usedhcpsettings)

Added the missing documentation for option "Use DHCP setting". If this setting is used, the configuration of local zones is disabled.

- **Internal Reference:** 61161
- **Issue Type:** Feature
- **Docs Link:** none

The HIN ruleset was no longer being generated automatically on HIN MGWs at startup. This has been fixed now. The MGWs now also fetch their list of public domain keys every half hour.

- **Internal Reference:** 61193
- **Issue Type:** Bug
- **Docs Link:** none

Automatic revocation did not work because it only took into account inactive users who had been disabled. However, the intended behaviour is an OR condition, that is either disabled or inactive. This has been fixed now.

- **Internal Reference:** 61258
- **Issue Type:** Maintenance
- **Docs Link:** none

There are sometimes more complex configurations for the cluster setup that were not handled until now. This functionality has now been improved and expanded.

- **Internal Reference:** 50355
- **Issue Type:** Feature
- **Docs Link:** none

This issue was raised to check whether the SCEP MPKI Connector is compatible with EJBCA, and it is. SEPPMAIL can therefore be connected to EJBCA via SCEP without any problems.

- **Internal Reference:** 60914
- **Issue Type:** Bug
- **Docs Link:** none

As part of the migration to Sequoia-PGP, the cryptographic backend had to be switched to Botan3, as it is the only one that supports both current and legacy algorithms for cryptographic processing.

- **Internal Reference:** 61036
- **Issue Type:** Bug
- **Docs Link:** none

Due to overly restrictive error handling, some data was not being returned via the REST API using the crypto keymaterial endpoint. This has been fixed now.

- **Internal Reference:** 60671
- **Issue Type:** Bug
- **Docs Link:** none

There was an error in /v1/mailsystem/template that prevented templates and disclaimers from being added. This has been fixed now.

- **Internal Reference:** 61028
- **Issue Type:** Bug
- **Docs Link:** none

When setting the values for 'maximumEncryptionLicenses' and 'maximumLFTLicenses' via the REST API, an issue arose if the value 0 was selected. This has been fixed now.

- **Internal Reference:** 61019
- **Issue Type:** Bug
- **Docs Link:** none

This issue handles a general MIME/PGP problem that was discovered by Andris Suter-Dörig of the Applied Cryptography Group at ETH Zurich.

When a MIME part is decrypted using PGP, it can, in principle, contain a MIME structure itself. If this is cleverly arranged and encrypted, the user’s email client may misinterpret such a MIME structure and potentially send the contents of the previously encrypted email to the attacker. For this reason, PGP-decrypted MIME parts are now always base64-encoded.

- **Internal Reference:** 57794
- **Issue Type:** Maintenance
- **Docs Link:** none

The hashencrypt function, which is used when sending SMS messages and in GINA cache mode, previously used an outdated encryption algorithm. This has now been changed to AES-256-CBC with PBKDF2. However, for compatibility reasons, old hashes can still be decrypted.

- **Internal Reference:** 57819
- **Issue Type:** Bug
- **Docs Link:** none

With this ticket, we are addressing another path traversal vulnerability in the PDF module identified by Infoguard [CVE-2026-8811](https://www.cve.org/CVERecord?id=CVE-2026-8811), which occurs when attachments are embedded in the PDF. They also identified vulnerabilities in the sshd configuration of the update server, which we have also resolved.

- **Internal Reference:** 57793
- **Issue Type:** Maintenance
- **Docs Link:** none

We have switched the password hashing algorithm to PBKDF2-SHA152 for all users authenticated against the local database. This applies to local GINA accounts and users (provided they have passwords).

- **Internal Reference:** 61204
- **Issue Type:** Bug
- **Docs Link:** none

A bug in the GINA password reset function (caused by trying to access an undefined value) has been fixed.

- **Release Date:** May 11th, 2026
- **SEPPMAIL version:** 15.0.4.3
- **Author:** Birgit Grossmann
- [15.0.4.3 Hotfix Release](https://downloads.seppmail.com/extrelnotes/150/ERN15.0.html#15043-hotfix-release)

- **Internal Reference:** 60824
- **Issue Type:** Bug
- **Docs Link:** none

In the CfgServer module Fetchmail, there was an error when accessing an array, which prevented Fetchmail from being configured and started, causing CfgServer to terminate. This has been fixed now.

- **Internal Reference:** 60785
- **Issue Type:** Maintenance
- **Docs Link:** none

By default, Sequoia-PGP blocks algorithms considered insecure. When we introduced Sequoia-PGP, we only permitted SHA-1 as an insecure algorithm. However, this has led to problems for some customers who use key material with indefinite validity that employs outdated algorithms considered obsolete, such as Elgamal or DSS.

With this hotfix, we are initially allowing all algorithms permitted in the original PGP once again. In the next few releases, we will gradually introduce warnings for outdated key material. After that, we will provide the option to block outdated key material, and in the final step, we will reverse the default setting to block algorithms considered insecure by default, allowing the customer to re-enable them at their own discretion.

- **Internal Reference:** 60823
- **Issue Type:** Bug
- **Docs Link:** none

Removing the redirect in the GINA GUI after a successful login resulted in an incorrect value being passed for the template to be displayed, which then led to the error "unexpected render Page". This has been fixed now.

- **Release Date:** May 8th, 2026
- **SEPPMAIL version:** 15.0.4.2
- **Author:** Birgit Grossmann
- [15.0.4.2 Hotfix Release](https://downloads.seppmail.com/extrelnotes/150/ERN15.0.html#15042-hotfix-release)

- **Internal Reference:** 60309
- **Issue Type:** Bug
- **Docs Link:** none

Due to an error in the Apache configuration file relating to the LDAP password entry at startup, Apache was unable to start. This has been fixed now.

- **Internal Reference:** 60519
- **Issue Type:** Bug
- **Docs Link:** none

A change to the DN for interim certificates resulted in old and new entries being mixed up due to a subtree search. This has been fixed now.

- **Internal Reference:** 60762
- **Issue Type:** Feature
- **Docs Link:** [MPKI Simple Certificate Enrollment Protocol](https://docs.seppmail.com/en/07_mi_10_mpki_09_simple-certificate-enrollment-protocol.html#dp_staticsubjectpart)

With the SCEP MPKI Connector, you can now configure the static subject to be used, including both default and domain-specific settings. In other words, the same settings as for the other MPKI Connectors.

*MPKI SCEP Static Subject Part*

- **Internal Reference:** 60698
- **Issue Type:** Bug
- **Docs Link:** none

The newly introduced Sequoia-PGP is capable, under certain as yet unknown circumstances, of causing the OpenBSD kernel to deadlock, thereby freezing the system. For the time being, we are reverting to the original GPG at the relevant point and will continue to investigate the cause.

- **Internal Reference:** 59992
- **Issue Type:** Bug
- **Docs Link:** none

Due to security risks, identified by WKO Inhouse [CVE-2026-9592](https://www.cve.org/CVERecord?id=CVE-2026-9592), we have removed the redirect that occurs after logging in to the GINA GUI.

- **Release Date:** April 28th, 2026
- **SEPPMAIL version:** 15.0.4.1
- **Author:** Birgit Grossmann
- [15.0.4.1 Hotfix Release](https://downloads.seppmail.com/extrelnotes/150/ERN15.0.html#15041-hotfix-release)

- **Internal Reference:** 60324
- **Issue Type:** Bug
- **Docs Link:** none

Failing to call `waitpid` after a `fork` caused the forked processes to remain running in the background. This eventually led to the user exhausting the maximum number of available PIDs and preventing any further processes from being started, so that the system was effectively dead. This has been fixed now.

- **Internal Reference:** 59144
- **Issue Type:** Bug
- **Docs Link:** none

In the Admin GUI under "Mail processing" >> "Show ruleset", there is a "Copy to Clipboard" function for downloading the current ruleset. However, this contained non-ASCII whitespace characters, which made it impossible to import these rulesets. The whitespace characters have now been corrected, and a ruleset downloaded this way can be imported without any problems.

- **Internal Reference:** 58923
- **Issue Type:** Bug
- **Docs Link:** none

The values entered under "System" in the "Comment" section should have been retrievable via SNMP, but they weren't. This has been fixed now.

- **Internal Reference:** 58905
- **Issue Type:** Bug
- **Docs Link:** none

Previously, if one tried to delete a single email from the list of emails in the queue, all emails in the queue would be deleted. This has now been fixed, and individual emails can be deleted without any issues.

- **Internal Reference:** 58891
- **Issue Type:** Bug
- **Docs Link:** none

An umlaut in the ClientID for the SwissSign REST MPKI Connector meant that the settings could not be saved. This has been fixed now.

- **Internal Reference:** 58873
- **Issue Type:** Maintenance
- **Docs Link:** [GINA Domain cleanup settings](https://docs.seppmail.com/en/07_mi_17_gd__gina-domains.html#s_ginacleanupsettings)

The GINA grace period settings were only relevant for non-client-capable systems. As all systems are now client-capable, multi-customer systems, these settings were removed here.

- **Internal Reference:** 55348
- **Issue Type:** Feature
- **Docs Link:** none

User, GINA Accounts, Managed Domains, GINA Domains and Mail Processing Groups now have a comment field. An example for Managed Domains:

*Managed Domain comment field*

- **Internal Reference:** 54586
- **Issue Type:** Maintenance
- **Docs Link:** [GINA Accounts](https://docs.seppmail.com/en/07_mi_18_ga__gina-accounts.html)

When the GINA Accounts page is loaded in the Admin GUI, the number of users displayed per customer is now limited. The default is 1,000. If you uncheck the box next to "Limit the number of returned accounts", all users will be displayed.

*Warning for limited output - uncheck "Limit the number of returned accounts", if desired*

- **Internal Reference:** 59843
- **Issue Type:** Maintenance
- **Docs Link:** [Gina Domain deletion](https://docs.seppmail.com/de/07_mi_17_gd_02_cgs__change-gina-settings-for.html#gina_domain_deletion)

Previously, when a GINA domain was deleted, the managed domains using that GINA domain were switched to the \[default\] GINA domain. The problem is that, as of a recent update, GINA messages can now only be read in the GINA domain for which they were created. As a result, deleting a GINA domain always means that old GINA emails for that domain can no longer be read.

For this reason, we are now preventing the deletion of GINA domains as long as they are still assigned to a managed domain. A warning will also be displayed indicating that the GINA domain still contains a certain number of GINA emails and when the last of these emails was created.

*Warnings regarding GINA domain deletion*

- **Internal Reference:** 58437
- **Issue Type:** Bug
- **Docs Link:** none

There was an issue with CSR generation when names containing the "+" character were used. The "+" character is now correctly escaped.

- **Internal Reference:** 59865
- **Issue Type:** Maintenance
- **Docs Link:** none

Due to stricter requirements from the Browser Forum, Harica had to create a new certificate chain for its MPKI service. This has been added to our system now, ensuring a seamless connection to Harica.

- **Internal Reference:** 59328
- **Issue Type:** Bug
- **Docs Link:** none

Customer admins were unable to view users (i.e. the users associated with the customer) in the admin GUI. This has been fixed now.

- **Internal Reference:** 57711
- **Issue Type:** Feature
- **Docs Link:** [Spamassassin Additional Config](https://docs.seppmail.com/en/07_mi_06_ms__mail-system.html#spamassassin_additional_config)

Some customers had encountered the problem that SpamAssassin checks were failing because the rate limit for certain RBLs had been reached. Previously, however, it was not possible to configure SpamAssassin to ignore these RBLs.

Now customers can modify the SpamAssassin configuration, and decide for themselves whether certain RBLs should be ignored.

*Spamassassin Additional Config*

- **Internal Reference:** 50919
- **Issue Type:** Bug
- **Docs Link:** none

ClamAV’s unofficial signatures were not updated if the system was configured to use a proxy. This has been fixed now in the freshclam configuration.

- **Internal Reference:** 58482
- **Issue Type:** Bug
- **Docs Link:** none

In the request to the /crypto/rootca endpoint of the REST API, the value "Factory" was missing from the enum list for the certOrigin value. This has been fixed now.

- **Internal Reference:** 57896
- **Issue Type:** Bug
- **Docs Link:** none

The newly introduced RuleEngine function `make_lft` wasn't working as intended. This has been fixed now.

For the following Vuln: issues, this comment applies:

In the beta version of GINAv2 on the appliance, various test endpoints were active which were intended solely for development purposes and should not have been included in the release. These have been removed. The relevant CVEs will be published later.

- **Internal Reference:** 58228
- **Issue Type:** Bug

- **Internal Reference:** 58226
- **Issue Type:** Bug

- **Internal Reference:** 58225
- **Issue Type:** Bug

- **Internal Reference:** 58223
- **Issue Type:** Bug

- **Internal Reference:** 58221
- **Issue Type:** Bug

- **Internal Reference:** 58218
- **Issue Type:** Bug

- **Internal Reference:** 58976
- **Issue Type:** Maintenance
- **Docs Link:** none

Switch to Sequoia-PGP to comply with RFC 9580 and to implement additional security features that are not possible with GPG2.

- **Internal Reference:** 58930
- **Issue Type:** Bug
- **Docs Link:** none

When processing SOAP requests, there was an issue with calculating the size of attached files, as these contained line breaks that disrupted the incremental processing of the Base64-encoded data. This has been fixed now.

- **Internal Reference:** 59728
- **Issue Type:** Bug
- **Docs Link:** none

When replying to an email in the GINA GUI using the "Reply" function and the option to change recipient addresses was disabled for the GINA domain, the CC field would appear after adding an attachment, allowing the sender to add any recipients. This has been fixed now.

- **Internal Reference:** 59658
- **Issue Type:** Bug
- **Docs Link:** none

If someone wrote an email via the GINA GUI and added attachments, and the recipient received and read that email as a GINA email, the file names in the ZIP archive were base64-encoded when downloading the single ZIP file with all attachments. This has been fixed now.

- **Internal Reference:** 58961
- **Issue Type:** Bug
- **Docs Link:** none

An infinite loop in the account activation process for GINA accounts was causing issues during activation. This has been fixed now.

- **Internal Reference:** 58726
- **Issue Type:** Bug
- **Docs Link:** none

When trying to compose an email in the GINA GUI, an error would be received due to a missing Perl module. This has been fixed now.

- **Release Date:** March 3rd, 2026
- **SEPPMAIL version:** 15.0.3
- **Author:** Birgit Grossmann
- [15.0.3 Bugfix Release](https://downloads.seppmail.com/extrelnotes/150/ERN15.0.html#1503-bugfix-release)

- **Internal Reference:** 57915
- **Issue Type:** Bug
- **Docs Link:** none

When creating a GINA domain with umlauts or other UTF8 characters, for example, there was a problem where the domain was displayed in the drop-down menu in Managed Domains but was not selected by default. This meant that the Managed Domain lost the GINA domain setting when the Managed Domain was saved. This has been fixed now.

- **Internal Reference:** 57456
- **Issue Type:** Bug
- **Docs Link:** none

In the Admin GUI under System, it was not possible to simply enter the bind IP for the Admin GUI as an IP without receiving an error message. However, if the IP was entered in such a way that it was accepted, it was in the wrong format and the Admin GUI did not load correctly. The validation of the entered IPs has now been corrected.

- **Internal Reference:** 57985
- **Issue Type:** Maintenance
- **Docs Link:** none

In the previous release, there was an issue with the CARP password. It was displayed and the default password was sometimes not used. This has been fixed.

- **Internal Reference:** 57295
- **Issue Type:** Bug
- **Docs Link:** none

There was a problem with passwords that contained the character ". This has been fixed now.

- **Internal Reference:** 57293
- **Issue Type:** Bug
- **Docs Link:** none

When the database was rebuilt during DB-based logging, the user received an error message stating that the DB was defective. This sometimes led to the user initiating the creation of the DB again. Now, the user receives a reasonable message stating that the DB is being created and the percentage of the process completed.

- **Internal Reference:** 55267
- **Issue Type:** Maintenance
- **Docs Link:** none

In order to offer users the option of better restricting the search period in the mail log view, we incorporated a feature in a previous version that rotates the mail log file at least once a day. Unfortunately, this resulted in the mail log file being rotated four times between midnight and 1 a.m. We have corrected this and the mail log is now rotated at least once every day, but only once between midnight and 1 a.m.

- **Internal Reference:** 55238
- **Issue Type:** Bug
- **Docs Link:** none

The browser form requires the first and last name to be entered for certain certificates. These are then stored in the CN of an S/MIME certificate as "FirstName LastName". However, the CN may only be 64 characters long, which causes problems with some names. We now also limit the length of first and last names in SwissSignRest MPKI so that they do not exceed 64 characters. Furthermore, improved verification of available products and overrides for the use of the pseudo attribute and for special characters has been incorporated.

*Form for entering certificate data*

- **Internal Reference:** 57556
- **Issue Type:** Maintenance
- **Docs Link:** none

There has been an update at GlobalSing regarding root and intermediate certificates, and ee have added them to our list of GlobalSign certificates. Users can add them in the MPKI settings for GlobalSign using the "Add or update..." button.

*Add or update root and intermediate certificates*

- **Internal Reference:** 57608
- **Issue Type:** Bug
- **Docs Link:** none

When creating a user in the core of the REST API, there was an error whereby users could specify their future groups and their existence was also verified, but the user was not added to the groups. We have now corrected this and when creating a user, their group memberships are set correctly.

- **Internal Reference:** 57571
- **Issue Type:** Bug
- **Docs Link:** none

With this ticket, we are closing a security vulnerability CVE-2026-2743 found by Infoguard. This concerned a possible path traversal in file.app, which is used by the Outlook add-in for bypassing LFT upload.

- **Internal Reference:** various
- **Issue Type:** Maintenance
- **Docs Link:** none

The following vulnerabilities have been fixed:

- High: S/MIME Signature Additional Certificate ([CVE-2026-29140](https://www.cve.org/CVERecord?id=CVE-2026-29140))
- High: Bounded Subject Tag Sanitization ([CVE-2026-29141](https://www.cve.org/CVERecord?id=CVE-2026-29141))
- High: Plaintext secure-mail.html ([CVE-2026-29142](https://www.cve.org/CVERecord?id=CVE-2026-29142))
- High: S/MIME Decryption Impersonation ([CVE-2026-29143](https://www.cve.org/CVERecord?id=CVE-2026-29143))
- High: Unicode Subject Tags ([CVE-2026-29144](https://www.cve.org/CVERecord?id=CVE-2026-29144))
- High: GINA State Confusion Account Takeover ([CVE-2026-29139](https://www.cve.org/CVERecord?id=CVE-2026-29139))
- Medium: PGP Decryption Recipient LDAP Injection ([CVE-2026-29131](https://www.cve.org/CVERecord?id=CVE-2026-29131))
- Low: ESWmail-Verify Bypass ([CVE-2026-29132](https://www.cve.org/CVERecord?id=CVE-2026-29132))
- Low: UID Regex Bypass ([CVE-2026-29133](https://www.cve.org/CVERecord?id=CVE-2026-29133))
- Low: GINA Domain Switch ([CVE-2026-29134](https://www.cve.org/CVERecord?id=CVE-2026-29134))
- Low: Webmail Password Tag Sanitization Bypass ([CVE-2026-29135](https://www.cve.org/CVERecord?id=CVE-2026-29135))
- Low: CA Notification HTML Injection ([CVE-2026-29136](https://www.cve.org/CVERecord?id=CVE-2026-29136))
- Low: Long Subject Untagging ([CVE-2026-29137](https://www.cve.org/CVERecord?id=CVE-2026-29137))
- Low: PGP Decryption Sender LDAP Injection ([CVE-2026-29138](https://www.cve.org/CVERecord?id=CVE-2026-29138))

- **Internal Reference:** 58005
- **Issue Type:** Bug
- **Docs Link:** none

When using our SOAP interface (only used by webcrypt), an incorrect and no longer existing function was used, which led to processing being interrupted. This has been fixed now.

- **Internal Reference:** 57548
- **Issue Type:** Maintenance
- **Docs Link:** none

The following HTML Headers are now added:

Documents (HTML)

`Cross-Origin-Opener-Policy: same-origin`

`Cross-Origin-Embedder-Policy: require-corp`

Static assets (JS/CSS/fonts/images/assest/... with exception of the mobiletest.css)

`Cross-Origin-Resource-Policy: same-origin`

Logout response:

`Clear-Site-Data: "cache", "cookies", "storage", "executionContexts"`

Legacy hardening:

`X-Permitted-Cross-Domain-Policies: none`

- **Internal Reference:** 57671
- **Issue Type:** Maintenance
- **Docs Link:** none

We have further completed and corrected the French translations.


- **Release Date:** February 6th, 2026
- **SEPPMAIL version:** 15.0.2.1
- **Author:** Birgit Grossmann

Update to OpenSSL version 3.0.19 to fix a list of security findings:


- **Internal Reference:** 54455
- **Issue Type:** Maintenance
- **Docs Link:** none

Previously, there was a problem when saving the TLS settings under "GINA Domains" if the option "Disallow insecure ciphers (breaks compatibility with older browsers, but necessary for PCI compliance)" was activated and ciphers were selected that were not permitted for this mode in the multi-select. This resulted in an error message stating that some of the selected ciphers were not permitted for PCI. Now, the unauthorised ciphers are simply ignored and removed from the selection, allowing to save without any problems.

- **Internal Reference:** 53728
- **Issue Type:** Maintenance
- **Docs Link:** [Mails currently in queue](https://docs.seppmail.com/en/07_mi_13_logs_02_mails-currently-in-queue.html)

Under Logs > "Mails currently in queue", you can now filter by From, To, Queue name and Status.

*Filters for "Mails currently in queue"*

- **Internal Reference:** 55268
- **Issue Type:** Bug
- **Docs Link:** none

Until now, frontend systems have not cleaned up/deleted the cached emails in GINA Cache mode. As a result, the local directory continued to grow. Starting with version 15.0.2, the local cache will also be cleaned up on frontend systems.

- **Internal Reference:** 55070
- **Issue Type:** Bug
- **Docs Link:** none

There was an error in the restore script for the daily snapshots in the event of a full snapshot restore. This has been fixed now.

- **Internal Reference:** 55101
- **Issue Type:** Maintenance
- **Docs Link:** none

When sending the daily backup and daily digest, we have not previously set the envelope sender for sending. This led to problems, especially in ExO environments. We now set the envelope sender to the postmaster (which must of course be configured).

- **Internal Reference:** 54336
- **Issue Type:** Maintenance
- **Docs Link:** none

Until now, we have not explicitly set the key usage of the CA certificate when creating the local CA. However, this causes problems for communication partners who must communicate in a BSI-compliant manner, as setting the keyUsage is a prerequisite here. Starting with version 15.0.2, the key usage for newly issued CAs will be set to "keyCertSign, cRLSign".

- **Internal Reference:** 55295
- **Issue Type:** Bug
- **Docs Link:** none

Only SwissSign Gold products require a first and last name, this has been adjusted now in the SwissSign MPKI Connector.

- **Internal Reference:** 55366
- **Issue Type:** Bug
- **Docs Link:** none

There was a problem in the REST API with targeted access to the key material of specified users or domains. If the user or domain was not found, all data was returned. Now we return an error message stating that the user or domain does not exist.

- **Internal Reference:** 54456
- **Issue Type:** Bug
- **Docs Link:** none

When setting customer settings in the REST API, there was a problem in that it was not possible to set empty values for maximumEncryptionLicenses and maximumLFTLicenses, but only positive integers. This meant that it was not possible to allow the customer an unlimited number of licences, but only a fixed number. Now it is possible to leave the value empty again and thus remove the licence limit.

- **Internal Reference:** 57148
- **Issue Type:** Bug
- **Docs Link:** none

A security-critical change in 15.0.1 caused incorrect processing, mainly when decrypting HIN-encrypted emails, because reprocessing the headers caused the rule set to select the wrong path for the next rules and marked decrypted emails as "encryption failed". This has been fixed now.

- **Internal Reference:** 54932
- **Issue Type:** Bug
- **Docs Link:** none

In a change in 15.0.1, which introduced more compliant parsing of email addresses, there was an error whereby we MIME-decoded email addresses and then parsed them. This is incorrect and led to "invalid email address" error messages. This has been fixed now.

- **Internal Reference:** 54925
- **Issue Type:** Maintenance
- **Docs Link:** none

Previously, when logging the size of the email, the size of attachments uploaded via bypass upload was not included. These are the attachments uploaded by the Outlook add-in for LFT. This is now logged.

- **Internal Reference:** 54881
- **Issue Type:** Maintenance
- **Docs Link:** none

Every change to the headers of an email is now logged - deleting, adding, replacing. This means that the customer can always see in the log when which headers were set. (Only the transfer of headers from decrypted emails is not yet logged.)

- **Internal Reference:** 53977
- **Issue Type:** Bug
- **Docs Link:** none

In the code for renewing S/MIME certificates issued by the local CA, there was an error that prevented automatic renewal if the MPKI connector was not also configured for the domain in question. We have now removed this dependency and the renewal of local certificates is working again.

- **Internal Reference:** 55350
- **Issue Type:** Bug
- **Docs Link:** none

There were some wrong translations in the GINA GUI, mostly in French. These are fixed now.

- **Internal Reference:** 55045
- **Issue Type:** Bug
- **Docs Link:** none

We used to have a mechanism to determine whether we were on a mobile device in a proper browser or just in an HTML viewer. However, this mechanism is no longer reliable, so we have removed it. But since all old GINA emails from before the removal still rely on one of the removed files, we have added it back, and the old GINA messages should now be readable again without any problems.

- **Internal Reference:** 54999
- **Issue Type:** Feature
- **Docs Link:** none

In version 15.0.0, we added logging of the X-Forwarded-For header for GINA. We now log this header for all web accesses.

- **Internal Reference:** 54796
- **Issue Type:** Maintenance
- **Docs Link:** none

During a penetration test, it was noticed that forms could be embedded in GINA emails. Form tags in HTML are now removed using "defang" when displayed in the GINA GUI.

- **Internal Reference:** 54596
- **Issue Type:** Maintenance
- **Docs Link:** none

In the GINA account detail views, "floating" was displayed for the time zone under "Account info". Now the time zone as configured under "System" is used.

- **Internal Reference:** 55088
- **Issue Type:** Maintenance
- **Docs Link:** none

We had the problem that when a large number of entries for the GINA cache mode were stored on an S3, the time required to retrieve and display a cached email was very high. However, since S3 only allows prefix searches, we had to change the naming of the cache entries so that access can now take place much faster.

- **Internal Reference:** 55220
- **Issue Type:** Bug
- **Docs Link:** none

Texts were added twice in GINA mail creation. This has been fixed now.


- **Internal Reference:** 53190
- **Issue Type:** Maintenance
- **Docs Link:** none

We no longer issue a warning about the absence of an LFT disc on hardware systems.

- **Internal Reference:** 51005
- **Issue Type:** Bug
- **Docs Link:** none

If you previously used the master template settings for the extended settings in the settings of a GINA domain and deactivated this for a domain-specific setting, you could save invalid settings that later led to malfunctions. This is no longer possible.

- **Internal Reference:** 53371
- **Issue Type:** Bug
- **Docs Link:** [Nutanix](https://docs.seppmail.com/en/07_mi_05_system.html#vt_qemuandnutanix)

With older Nutanix installations, there is a problem with the vioscsi driver, which leads to very long boot times. For this reason, it is actually possible to disable the vioscsi driver under Nutanix. The problem was that if someone switched to Nutanix from another platform, they previously could not disable the vioscsi driver beforehand. This is now possible.

- **Internal Reference:** 49344
- **Issue Type:** Feature
- **Docs Link:** [SMS Passwords](https://docs.seppmail.com/en/07_mi_17_gd__gina-domains.html#sp_useutfencoding)

As there were repeated UTF-8 encoding problems with SMS messaging, we have added a new option "Use UTF encoding" that allows to define whether data should be transferred as UTF-8 or not.

*Use UTF encoding*

- **Internal Reference:** 54734
- **Issue Type:** Maintenance
- **Docs Link:** none

Mainly in Azure environments, there was the problem that after about 10 minutes, the support connections were no longer usable, even though the connection was still visible on the SEPPMAIL side. We have now adjusted the parameters for the SSH connection so that it is automatically tested and kept open by the appliance.

- **Internal Reference:** 53209
- **Issue Type:** Feature
- **Docs Link:** none

There are two cron jobs that renew or revoke certificates when necessary. Previously, these wrote to the syslog without any recognisable affiliation. Now, the log entries for these jobs have the corresponding prefixes ‘Autorenew’ and ‘Autorevoke’, making them easy to filter.

- **Internal Reference:** 52581
- **Issue Type:** Maintenance
- **Docs Link:** none

In the code that detects on a frontend system that the backend is no longer accessible and switches to another configured backend, there was an error that prevented the desired behaviour. This has now been fixed and works as intended.

- **Internal Reference:** 54253
- **Issue Type:** Bug
- **Docs Link:** none

There was an error when manually importing a licence. This is fixed now.

- **Internal Reference:** 54266
- **Issue Type:** Maintenance
- **Docs Link:** none

Previously, the SMTPd.pl process, which receives emails from Postfix, passed them to the RuleEngine and then forwarded them, writing its error and debug output to /tmp. This meant that important information for error analysis was sometimes lost during a restart. Now the process writes to /var/log/SMTP.err, which is persistent.

- **Internal Reference:** 17362
- **Issue Type:** Feature
- **Docs Link:** none

The mail log is rotated at least once a day. This allows file-based logging to be filtered by day.

- **Internal Reference:** 52995
- **Issue Type:** Bug
- **Docs Link:** none

In the rare case that there were no emails in the mail log, DB-based logging incorrectly assumed that there was an error. Now, a corresponding message is displayed indicating that there are no entries.

- **Internal Reference:** 54017
- **Issue Type:** Bug
- **Docs Link:** none

When processing the mail log and adding this data to the database in DB-based logging, there were rare instances where the file used to prevent the same process from being called at the same time (i.e. a lock file) was not deleted after termination. This prevented the process from ever running again (until the next reboot). Now the file is deleted cleanly.

- **Internal Reference:** 48607
- **Issue Type:** Maintenance
- **Docs Link:** [Log archive type](https://docs.seppmail.com/en/07_mi_05_system.html#ls_logarchivetype)

To enable DB-based logging, we have now incorporated a test to check in advance whether there is sufficient disk space available. If not, DB-based logging will be prevented from being activated.

- **Internal Reference:** 54250
- **Issue Type:** Bug
- **Docs Link:** none

There were problems with the CN when issuing domain certificates using the SwissSign MPKI Connector. The CN of a certificate may only be a maximum of 64 characters long. Some domains are so long that this limit is exceeded. We are now trying to shorten them and if that does not help, we will refer you to SwissSign support.

- **Internal Reference:** 53446
- **Issue Type:** Maintenance
- **Docs Link:** [Revocation](https://docs.seppmail.com/en/07_mi_15_usr_04_advanced-settings.html#as_revocation)

In version 15.0.0, the automatic revocation of certificates for inactive users was introduced. However, as some customers wish to retain these certificates, we have now made this configurable under "Users" > "Advanced Settings" with the option "Automatically revoke certificates of inactive users".

- **Internal Reference:** 54037
- **Issue Type:** Bug
- **Docs Link:** [Harica settings](https://docs.seppmail.com/en/07_mi_10_mpki_02_harica.html#dp_umlauttransliteration)

There was/is a problem with umlauts using the Harica MPKI Connector. This is likely a problem on Harica's side, but until they resolve it, we implemented the setting "Umlaut Transliteration" to transliterate special characters and umlauts to avoid non-ASCII characters.

*Transliterate special characters and umlauts to avoid non-ASCII characters*

- **Internal Reference:** 53665
- **Issue Type:** Bug
- **Docs Link:** none

In the Nagios tests of local services, the static telnet test was previously used to check whether Postfix was still working. However, this led to errors. For this reason, we now use the designated smtp test.

- **Internal Reference:** 54374
- **Issue Type:** Bug
- **Docs Link:** none

Previously, authentication via the submission port was only considered sufficient for outgoing emails. Now this is also the case for internal emails.

- **Internal Reference:** 53477
- **Issue Type:** Bug
- **Docs Link:** none

When displaying the generated Ruleset in the Admin GUI, there was a problem whereby certain parts of if-else if-else branches were displayed incorrectly, especially when the conditions were negated. Internally, however, the Ruleset was correct; only the display was incorrect, and this has been fixed now.

- **Internal Reference:** 52596
- **Issue Type:** Bug
- **Docs Link:** none

With the ticket, a special treatment for the Incamail test mail address [mta@check.incamail.ch](mailto:mta@check.incamail.ch) has been added in the Ruleset. Otherwise, an attempt would be made to process an email to mta@check.

- **Internal Reference:** 53327
- **Issue Type:** Maintenance
- **Docs Link:** none

We received a very comprehensive security review (thank you to Andris Suter-Dörig working under the supervision of Matteo Scarlata and Prof. Kenny Paterson from the Applied Cryptography Research Group at ETH Zurich). This ticket closes the critical vulnerabilities and some of those classified as high.

- PDF Password CMDi ([CVE-2026-27441](https://www.cve.org/CVERecord?id=CVE-2026-27441))
- zip attachments path traversal ([CVE-2026-27442](https://www.cve.org/CVERecord?id=CVE-2026-27442))
- S/MIME decryption tag sanitisation bypass ([CVE-2026-27443](https://www.cve.org/CVERecord?id=CVE-2026-27443))
- header email address parsing ([CVE-2026-27444](https://www.cve.org/CVERecord?id=CVE-2026-27444))
- PGP signature reflection ([CVE-2026-27445](https://www.cve.org/CVERecord?id=CVE-2026-27445))
- missing PGP signature tag ([CVE-2026-2746](https://www.cve.org/CVERecord?id=CVE-2026-2746))
- PGP mixed plaintext and encrypted content ([CVE-2026-2747](https://www.cve.org/CVERecord?id=CVE-2026-2747))
- S/MIME certificate subject whitespace ([CVE-2026-2748](https://www.cve.org/CVERecord?id=CVE-2026-2748))

Further vulnerabilities will be closed in upcoming releases.

- **Internal Reference:** 54117
- **Issue Type:** Bug
- **Docs Link:** none

Previously, we only allowed the import of pure RSA or EV X.509 certificates. Flavours such as RASSSA-PSS were rejected. Now we allow any type of RSA and EC.

- **Internal Reference:** 52651
- **Issue Type:** Maintenance
- **Docs Link:** [Edit translation file](https://docs.seppmail.com/en/07_mi_17_gd_02_cgs_02_edit-translations-for-language-x.html#edittranslationfile)

It was recognised as problematic when both the password and the account to be used are specified in a text message ("for %s"). For this reason, we have adjusted the pwsend\_smstext text so that it no longer contains the account. If customers have already made adjustments themselves in these translations, they must take action and check their texts.

- **Internal Reference:** 54306
- **Issue Type:** Maintenance
- **Docs Link:** none

For caching GINA messages on external S3 storage, we now omit the determination of free space on the S3, as this information is not available for S3. This greatly speeds up the processing of GINA emails in cache mode, especially when there are already a large number of emails in the cache.

- **Internal Reference:** 53661
- **Issue Type:** Feature
- **Docs Link:** none

The company logo is now also displayed in pwsend.app, the web application that sends the GINA password via text message.

- **Internal Reference:** 54405
- **Issue Type:** Bug
- **Docs Link:** none

With this ticket, we have fixed a bug that prevented the login history of GINA accounts from being cleared.


- **Internal Reference:** 52950
- **Issue Type:** Bug
- **Docs Link:** none

The "Save and apply all" button in the Advanced System Settings did not ensure that the changes were actually saved and applied. This has been fixed now.

- **Internal Reference:** 34590
- **Issue Type:** Feature
- **Docs Link:** [Add/Edit Managed Domain](https://docs.seppmail.com/en/07_mi_06_ms_04_aemd__add-edit-managed-domain.html#dkimsettings) and [Mail System](https://docs.seppmail.com/en/07_mi_06_ms__mail-system.html#arcsettings)

Under "Managed Domains" it is now possible to regenerate DKIM and ARC keys. In addition, the Master ARC key can also be regenerated under "Mail System".

*Regenerate DKIM Key*

*Regenerate ARC Key*

- **Internal Reference:** 38708
- **Issue Type:** Feature
- **Docs Link:** [X.509 Root Certificates](https://docs.seppmail.com/en/07_mi_22_root__x509-root-certificates.html#rc_truststate)

When the SEPPMAIL Gateway performs its revocation checks for root CA certificates, it sets the status to "untrusted" if the CA certificate has been revoked.

- **Internal Reference:** 52235
- **Issue Type:** Maintenance
- **Docs Link:** none

The file.app, which we use to bypass the upload of LFT attachments, has not previously returned any error messages when an upload was unsuccessful. As a result, users were never able to tell whether the upload had been successful or not. From version 15.0.0 onwards, we have error codes with meaningful error descriptions.

- **Internal Reference:** 50724
- **Issue Type:** Feature
- **Docs Link:** none

The X-Forwarded-For IP address is now logged in the Apache access log for the GINA GUI. This also gives us information about whether there is a proxy in front of the system that sets the HTTP header.

- **Internal Reference:** 52772
- **Issue Type:** Maintenance
- **Docs Link:** [Mail System](https://docs.seppmail.com/en/07_mi_06_ms__mail-system.html#md_verifyrecipientaddressesusingsmtplookups)

By default, the setting for "Verify recipient addresses using SMTP lookups" under "Mail System" is now inactive (not checked). The setting is therefore deactivated for new installations.

- **Internal Reference:** 52747
- **Issue Type:** Feature
- **Docs Link:** [Mail System](https://docs.seppmail.com/en/07_mi_06_ms__mail-system.html#sp_enableclientcertificateverification)

Under "Mail System", you can disable client certificate verification in the submission port settings. This also means that Postfix no longer transmits the list of subjects of the root CA certificates, which causes problems in some Exchange installations because the list is too large.

*Enable or disable client certificate verification*

- **Internal Reference:** 52772
- **Issue Type:** Maintenance
- **Docs Link:** none

For SwissSign MPKI, the specification of GivenName and Surname is only necessary for Gold products. Both values are therefore only required for Gold products, and a corresponding error message is displayed if the two values cannot be determined for the Gold products.

- **Internal Reference:** 24760
- **Issue Type:** Feature
- **Docs Link:** [SwissSign REST MPKI](https://docs.seppmail.com/en/07_mi_10_mpki_12_swisssign_rest.html)

SEPPMAIL Gateway now offers a REST connection to the PKI of SwissSign.

*New SwissSign REST MPKI connector*

- **Internal Reference:** 45561
- **Issue Type:** Feature
- **Docs Link:** [Harica MPKI connector](https://docs.seppmail.com/en/07_mi_10_mpki_02_harica.html)

The new Harica MPKI connector replaces the no longer functional DFN connector.

*New Harica MPKI connector*

- **Internal Reference:** 44485
- **Issue Type:** Feature
- **Docs Link:** [Domain Encryption via SwissSign MPKI](https://docs.seppmail.com/en/07_mi_06_ms_04_aemd__add-edit-managed-domain.html#smimedomainencryption)

If the classic SwissSign MPKI Connector is used (not the new SwissSign Rest MPK Connector), it can now be used to issue domain certificates for managed domains.

*Generate new SwissSign S/MIME Key*

- **Internal Reference:** 48360
- **Issue Type:** Feature
- **Docs Link:** none

If a user's licence is revoked, either manually or after 3 months of inactivity, their S/MIME certificates will be revoked from version 15.0.0 onwards.

- **Internal Reference:** 45441
- **Issue Type:** Feature
- **Docs Link:** [Delete Customer](https://docs.seppmail.com/en/07_mi_24_cust_02_delete-customer.html#do_revokeusercertificatesbeforedeletion)

Previously, there was a problem that if a customer was exported from one appliance and then imported onto another appliance, deleting the customer on the original appliance would revoke all certificates belonging to the customer's users. This would also render all user certificates imported onto the new appliance useless. Now, when deleting a customer, you can choose whether or not to revoke the certificates or the users. Revocation is disabled by default.

*Revoke user certificates before deletion*

- **Internal Reference:** 51526
- **Issue Type:** Bug
- **Docs Link:** none

There was a discrepancy between the number of licensed users in the customer overview and the customer detail view. This has been fixed now.

- **Internal Reference:** 26668
- **Issue Type:** Maintenance
- **Docs Link:** none

Previously, the use of managed domains was not comprehensively searched for when they were deleted. This meant that some components retained the already deleted managed domains in their data. These references are now correctly cleared up.

- **Internal Reference:** 19394
- **Issue Type:** Feature
- **Docs Link:** none

It is now possible to manage encryption policies via the RestAPI.

- **Internal Reference:** 52868
- **Issue Type:** Feature
- **Docs Link:** [Import Customer](https://docs.seppmail.com/en/07_mi_24_cust_02_import-customer.html#id_filetoimport)

Backups from non-multi-customer appliances (extension .bak) can now be imported as a new customer.

*Import customer from Backup file*

- **Internal Reference:** 19871
- **Issue Type:** Maintenance
- **Docs Link:** none

Our internal CMS module, which handles encryption, decryption and signatures, has so far been very complicated and memory-intensive. We are now using a more elegant approach, which reduces memory consumption considerably and is a little faster.

- **Internal Reference:** 32424
- **Issue Type:** Maintenance
- **Docs Link:** [Mail Processing](https://docs.seppmail.com/en/07_mi_07_mp__mail-processing.html#rg_ht_hint1)

Previously, some headers were only written to the email via the RuleSet. This meant that these headers were not present in a self-written RuleSet, which in turn could lead to problems in the M365 environment, as the connectors created by our PowerShell module expect certain headers. These headers are now added directly by the RuleEngine functions.

- **Internal Reference:** 32616
- **Issue Type:** Feature
- **Docs Link:** [make\_lft()](https://docs.seppmail.com/en/08_cr_06_mh_11_ct_06_gina_make_lft.html) and [revert\_lft()](https://docs.seppmail.com/en/08_cr_06_mh_11_ct_06_gina_revert_lft.html)

There are two new functions for the RuleEngine that allow you to turn an email into an LFT message or revert an LFT message to an email. The functions are called make\_lft and revert\_lft, have no arguments, and return a corresponding value depending on success or failure, so that they can also be used in if conditions.

- **Internal Reference:** 47356
- **Issue Type:** Feature
- **Docs Link:** [getuserattr()](https://docs.seppmail.com/en/08_cr_05_ua_getuserattr.html)

The new RuleEngine function getusetattr( “ATTRIBUTE\_NAME”, “VARIABLE\_NAME” ) is available. It has two required parameters: one is the user attribute to be queried and the other is the variable to which the value should be written. The function returns true if it was successful, so it can also be used in IF conditions.

- **Internal Reference:** 52777
- **Issue Type:** Bug
- **Docs Link:** none

An error in the code meant that changes to the language settings of a GINA domain, i.e. the texts used in the language, were not applied. This has been fixed now.

- **Internal Reference:** 52606
- **Issue Type:** Bug
- **Docs Link:** none

When GINA user authentication against the appliance's internal database was enabled, failed login attempts were not logged, meaning that users were never locked out after reaching the maximum number of unsuccessful login attempts. This has been fixed now.

- **Internal Reference:** 12218
- **Issue Type:** Feature
- **Docs Link:** [Change GINA settings for...](https://docs.seppmail.com/en/07_mi_17_gd_02_cgs__change-gina-settings-for.html#certificatelogin)

The option "Certificate login" in the GINA settings has been removed.

--- end of document ---
