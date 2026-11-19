---
title: Changelog
url: https://docs.airlock.com/gateway/8.5/index/1755485389146.html
hostname: airlock.com
sitename: docs.airlock.com
date: "2011-06-02"
fingerprint: e618d4489fb3b410
---
# Changelog

## Changelog Airlock Gateway 8.5.3

The following list shows the changes from Airlock Gateway 8.5.2 to 8.5.3.

NEW: AP-38772 Added a file permissions watcher for ncipher HSM keys (CASE-37334)
FIX: AD-601 Reduced false positives of SQL\_001 (CASE-37430, CASE-37293) 
FIX: AP-38614 Enable delay after failed password change attempts in the Configuration Center
FIX: AP-38615 Fixed XSS vulnerability in the Configuration Center change password form
FIX: AP-38633 Fix buffer overflow when decoding HTML entities
FIX: AP-38635 Added expiry check of authentication tokens in the Configuration Center
FIX: AP-38844 Support encrypted cookies issued by Airlock Gateway >= 8.6.0 to ease downgrades (CASE-37413)
FIX: AP-38908 Disallow POST-as-GET requests in Configuration Center
FIX: AP-38958 Fix duplicate detection in IP Address Lists (CASE-37465)
UPD: AP-38432 Updated to curl 8.20.1
UPD: AP-38654 Updated geolocation data and library (DB-IP)
UPD: AP-38657 Updated Anomaly Shield components
UPD: AP-38658 Updated OS components
UPD: AP-38661 Updated Elasticsearch/Kibana to 9.5.4
UPD: AP-38662 Updated Airlock components

## Changelog Airlock Gateway 8.5.2

The following list shows the changes from Airlock Gateway 8.5.1 to 8.5.2.

NEW: AP-38314 Added installed hotfixes information to REST API /system/status/node resource
FIX: AP-38255 Corrected read-only users missing permissions for regex tester buttons on global deny-rule details page
FIX: AP-38279 Correctly handle kernel hotfixes in updates (CASE-37127)
FIX: AP-38190 Stabilized failover behavior on activations with IP changes (CASE-36983, CASE-37102)
CHG: AP-31776 Added virtual host information to Let's Encrypt Events (CASE-32306, CASE-37113, CASE-37114)
CHG: AP-37889 Increased allowed header names length for multipart requests from 31 to 40 characters (CASE-36857)
UPD: AP-38033 Updated BrightCloud Threat Intelligence SDK to 5.38.2
UPD: AP-38120 Updated Elasticsearch/Kibana to 9.4.2
UPD: AP-38121 Updated geolocation data and library (DB-IP)
UPD: AP-38122 Updated OS components
UPD: AP-38124 Updated Python libraries
UPD: AP-38216 Updated mod\_md to 2.6.11
UPD: AP-38358 Updated Airlock components

## Changelog Airlock Gateway 8.5.1

The following list shows the changes from Airlock Gateway 8.5 to 8.5.1.

```
FIX: AP-37264 Correctly hide close button in warning dialogs
FIX: AP-37870 Corrected possible use of outdated ssh keys after activation
FIX: AP-38030 Fixed missing external account binding with ACME DNS-01 (CASE-36939)
FIX: AP-38058 Improved ID descriptions in the REST API documentation (CASE-36239) 
FIX: AP-38080 Mitigate OpenSSH GSSAPI flaw (CVE-2026-3497)
CHG: AP-37940 Add a selection of PKCS algorithms (rsa_pkcs1_sha256/_sha384/_sha512) to the 
              default TLS signature algorithms again to ensure broader TLSv1.2 compatibility
UPD: AP-37902 Update Airlock Gateway components
UPD: AP-37944 Update OS components
UPD: AP-37945 Update geolocation data and library (DB-IP)
UPD: AP-37946 Update Elasticsearch/Kibana to 9.3.1
UPD: AP-37950 Update Python libraries
```
## Changelog Airlock Gateway 8.5

The following lists show the changes from Airlock Gateway 8.4 to 8.5.

### New

NEW: AD-119 Added new deny rule AS\_030 to filter LDAP attacks
NEW: AD-258 Added new deny rule XSS\_060 for prototype pollution in parameter names or JSON keys (CASE-36202)
NEW: AD-354 Added new deny rule SAN\_130 to validate \`expect\` header
NEW: AD-389 Added new deny rule SAN\_140 to block deprecated graphql content-types
NEW: AP-28742 Added REST endpoint to configure notification channels (CASE-30766)
NEW: AP-36708 Web listener: Limit the total size of the request line and all request headers to 32 KB
NEW: AP-36796 Support for unattended installation (PXE/ISO)
NEW: AP-36798 Kickstart config from ISO may be used for PXE
NEW: AP-36799 Allow setting SSH public key in unattended installation
NEW: AP-36806 Added new REST Endpoints to access all deny rules and groups (CASE-36239)
NEW: AP-36848 Default content type patterns and custom rules for content parsing can be managed in the Configuration Center and via REST API
NEW: AP-36869 The TLS group "X25519MLKEM768" (post quantum cryptography/PQC) is available and enabled
NEW: AP-36936 Bootloader files for PXE are now included in ISO
NEW: AP-37026 Added the front-end TLS group to the log message "WR-SG-TLS-SESS-START" (log field "front\_tls\_group"), to the environment cookie "AL\_ENV\_SSL\_GROUP" and to the rewrite variable "%SSL\_GROUP%"
NEW: AP-37058 Allow to configure native JSON type log fields via Expert Settings
NEW: AP-37112 Support ACME certificate retrieval via DNS-01 challenge

### Fixes

FIX: AD-112 Refined handling of globbing in UNIX deny rules to reduce false positives (CASE-35973)
FIX: AD-315 Reduced false positives of various deny rules
FIX: AD-364 Reduced false positives of deny rule SAN\_040 (CASE-36472)
FIX: AD-401 Reduced false positives of deny rule PHP\_004 (CASE-36586)
FIX: AP-30149 Configuration Center: Only consider mappings with locking enabled in "Pull Settings from Source Mapping" (CASE-36178)
FIX: AP-35471 Config diff now correctly handles deleted certificates in the Configuration Center (CASE-35348)
FIX: AP-36048 Corrected REST endpoint /system/status/sessions/
FIX: AP-36187 Mention the username in the details of the event EVENT\_SY-C-CCLOGIN-OK
FIX: AP-36291 Eased a race condition when reconfiguring the firewall to allow access to the ACME endpoints
FIX: AP-36562 Sanitized entity names in the Configuration Center to prevent errors upon delete. (CASE-36131)
FIX: AP-36703 System hardening: Reduce the number of ext-apache threads
FIX: AP-36705 mod\_reqtimeout now works correctly with a body timeout - previously, connections could be closed because of a body timeout even after the body had been sent (CASE-36192)
FIX: AP-36877 Title of Deny Rule exception panel in the Configuration Center now indicates the context of the exceptions
FIX: AP-36917 Deletion of an ICAP service in the Configuration Center now triggers an error message if it's still in use (CASE-36310)
FIX: AP-36972 Added Configuration Center user role "airlock-readonly-session-viewer-details" (CASE-36224)
FIX: AP-37038 Suppress "new models available" notification if Anomaly Shield is disabled (CASE-36300)
FIX: AP-37050 Anomaly Shield: Also support the old endpoint for Client Behavior analysis results for a smooth transition
FIX: AP-37082 Fixed listing of back-ends with default ports in REST API (CASE-36356, CASE-36417)
FIX: AP-37123 Re-enabled the option "FollowSymLinks" for ext-apache, this prevents the log message AH00670 (CASE-36386, CASE-36402)
FIX: AP-37425 Anomaly Shield: Optimized models for a smaller memory and disk footprint
FIX: AP-37520 Added missing field multipleSingleLineRegex on REST endpoint for default deny-rules
FIX: AP-37637 Support core dumps bigger than 1 GB (CASE-36558)
FIX: AP-37645 REST: Correctly report IDs of IP address lists in mapping relationships to blacklists and blacklist exceptions (CASE-36655)
FIX: AP-37651 Reduce logging during Cookie-Check in Log Only mode
FIX: AP-37656 Reload Security Gateway process on back-end client certificate change (CASE-36669)
FIX: AP-37661 Fixed Security Gateway crash on config reload if Out-of-band Checks with custom host header is configured
FIX: AP-37667 Removed hard session store size limit

### Changes

CHG: AD-111 Improved and refined various UNIX, SQL, XSS and LDAP deny rules
CHG: AD-404 Reduced false positives of "Signature" and "Signature-Input" headers for problematic deny rules (CASE-36608)
CHG: AP-15979 Decreased the Apache I/O timeout from 300 seconds to 30 seconds
CHG: AP-16113 Removed deny rule SAN\_010 from security levels basic and standard
CHG: AP-16437 Discard potential system secrets in 'Collect system log'
CHG: AP-19918 Enforce UTF-8 for JSON content
CHG: AP-33307 Enabled SNI for TLS connections to external syslog servers (CASE-33568)
CHG: AP-36704 Hardening of HTTP/2 defaults
CHG: AP-36795 Adjusted deny rule group processing order: Sanity is processed as the third group
CHG: AP-36880 The Add-On Tomcat is now an optional package and supports installation of Tomcat 9 or Tomcat 11
CHG: AP-36942 Prevent generic operationId naming in OpenAPI specification of the REST interface (CASE-36270)
CHG: AP-36981 Removed Microsoft mapping templates from Configuration Center
CHG: AP-37025 Anomaly Shield exclusions will affect the current request only, not the session
CHG: AP-37172 Stricter character set encoding normalization of request URL
CHG: AP-37224 Use JSON as default format for new log forward entries
CHG: AP-37274 Restrict access to REST interface to users with role airlock-administrator
CHG: AP-37276 Defined default request\_timeout of 10s for kerberos environments
CHG: AP-37281 Added readline support to sqlite3 CLI
CHG: AP-37292 Disabled obsolescent TLS signature algorithms like SHA1 by default
CHG: AP-37585 Log messages SY-AA-AUTH-OK and SY-ALEC-48100 now use the term "role" instead of "credential"

### Updates

UPD: AP-31461 Updated Bootstrap to 5.3.8
UPD: AP-36464 Updated jansson to 2.14.1
UPD: AP-36894 Updated Spring Security to 6.5.7
UPD: AP-37193 Updated cloud-init to 24.4
UPD: AP-37390 Updated syslog-ng to 4.10.2-2
UPD: AP-37392 Updated geolocation data (DB-IP)
UPD: AP-37393 Updated BrightCloud Threat Intelligence SDK to 5.38.1
UPD: AP-37399 Updated Kerberos to 1.22.1
UPD: AP-37400 Updated c-icap to 0.6.4
UPD: AP-37403 Updated nettle to 3.10.2
UPD: AP-37415 Updated nghttp2 to 1.68.0
UPD: AP-37418 Updated PCRE2 to 10.47
UPD: AP-37386 Updated httpd to 2.4.65
UPD: AP-37387 Updated libcurl to 8.17.0
UPD: AP-37388 Updated Elasticsearch/Kibana to 8.19.6
UPD: AP-37398 Updated OpenSSL to 3.5.4
UPD: AP-37404 Updated jsoncons to 1.4.3
UPD: AP-37405 Updated expat to 2.7.3
UPD: AP-37406 Updated libmicrohttp to 1.0.2
UPD: AP-37408 Updated Redis to 8.2.3
UPD: AP-37411 Updated Protobuf to 33.1
UPD: AP-37412 Updated Boost to 1.89.0
UPD: AP-37414 Updated SQLite to v3.51.0, SQLite-jdbc to v3.51.0.0
UPD: AP-37419 Updated available versions of the Tomcat instance for Add-on Modules to 9.0.112 and 11.0.14
UPD: AP-37420 Updated Tomcat to 11.0.14 (Configuration Center)
