# FU2 deep read: primary-source claim sheets for five publishing items

Run `2026-11-18T0356Z-intel` | follow-up FU2 | worker model Sonnet 5.5 (`claude-sonnet-5-5`) | started 2026-11-18T04:36:43Z | fetched 2026-11-18 between ~04:40Z and ~05:10Z.

How to use this file
- Every table row is `claim | source URL | verbatim passage | saved body`. The passage is an exact, contiguous substring of the saved body named in the last column (under `work/2026-11-18T0356Z-intel/bodies/FU2/`). The generator checked every passage by exact substring match after writing: **488 passages checked, 0 not found** (a failing row would carry the marker `[NOT FOUND IN BODY]`/`[CHECK FAILED]`). In the markdown a literal pipe inside a passage is escaped as `\|` (table syntax only); `grep -F` the passage against the named body file, not against this markdown.
- Statements marked "assessment", "inference" or "derived" are this reader's, not a source's, and say so. Modality words are kept exactly as the sources use them ("could", "may", "is working on").
- Generator scripts (re-runnable) are in `bodies/FU2/_build/`.
- No IOCs are reproduced (no hashes, no exfiltration endpoint, no attacker addresses).

## 0. Headline: what changed versus the first pass

| item | one-line change |
|---|---|
| 6 Oracle CSPU | Every first-pass number reproduces from the 655 matrix rows (62 rows >= 9.0 across 57 CVEs; 56 unauthenticated rows across 51 CVEs; EBS 19; Database 9.9 rows need Create Session). But "21 product families" and "640 CVEs" are Tenable's figures, not Oracle's; the T3/IIOP row is 9.8 (only TopLink CVE-2026-91569 is 10.0); Java SE matrix includes CVE-2026-114938 at 8.1; new: the patch for EBS row CVE-2026-114918 "also addresses CVE-2025-61882" (KEV); no third-party exploitation or write-up found for any >= 9.0 row; only CVE-2026-111497 is on KEV. Full 56-row table below. |
| 7 Mitel MiCollab | First pass confirmed. Added: Mitel itself says 10.3 (10.3.0.18) and earlier is affected and needs the KB000129195 patch, while CERT-FR and BSI both say "before 10.3.0.18" (BSI lists 10.3.0.18 as fixed); 10.3.0.18 is the build that fixed MISA-2026-0006 in July, so July-patched sites are still in scope; no CVE ids in EUVD or NVD as of 2026-11-18; the MTLVULN-1864 impact sentence is garbled ("requires could allow"); advisory carries no exploitation statement either way. |
| 11 agent-framework PyPI | Three more independent detectors (Wiz, StepSecurity, Aikido) plus StepSecurity's PyPI quarantine times (1.26.1 at 21:06:16Z; 1.26.2 uploaded 2 min 23 s later, quarantined 21:16:44Z); the "31 substrings / 60 files" figures are the 1.26.1 profile (1.26.2: 35 / 80 per StepSecurity and Wiz); PyPI JSON shows 1.26.0 as latest and no 1.26.1/1.26.2; still NO Microsoft or PyPI statement found, and GitHub (microsoft/agent-framework) was unreadable from this session. |
| 12 N-able HF3 | Release notes confirm the first pass. New since the covered entry: Huntress (2026-11-17 8:30 ET) reports N-able CNA scores for all 17 CVEs (3 critical 9.3/9.3/9.2, 8 high, 6 medium), says public PoC code for all 17 appeared the evening of 16 Nov and that it has not observed exploitation; N-able's own HF3 notice and release notes still name neither 4EverAble2Shell, Agent2Shell nor the Axis CVE, so "HF3 fixes them" is unsupported, but the stated Legacy-API precondition is now permanently blocked. Extra lead: N-able Mail Assure/SpamExperts security incident (N-able, 2026-11-18 03:05Z). |
| 13 Axis OS | PDF read in full (one page). First-pass sentence "Axis phrases the advisory as an HTTP/2 flaw reachable on the device web interface" is NOT supported by the PDF (no such words); Axis lists no tracks or fixed versions, only "AXIS OS 6.50.5.10 or higher", CVSS 9.8, no known public exploits or exploitation "to Axis' knowledge", a service release "within the next couple of weeks", and the two System.HTTP2 workaround parameters. Axis registry (page date 2026-11-17) lists no released version. |

## 1. ORACLE CSPU 2026-11-17 (Critical Security Patch Update, Rev 1)

Primary: https://www.oracle.com/security-alerts/cspunov2026.html (read with `extract`, served `trafilatura-direct`; raw HTML also saved as `oracle/cspunov2026.raw.html` and parsed into `oracle/cspunov2026.rows.json`: 655 matrix rows). Oracle's own English text version of the same matrices: https://www.oracle.com/security-alerts/cspunov2026verbose.html (saved `oracle/cspunov2026verbose.extract.md`). Fetched 2026-11-18 ~04:40-04:55Z.

### 1.1 Totals and what Oracle itself states vs what is derived

| claim | source URL | verbatim passage | saved body |
|---|---|---|---|
| Oracle states the patch total (655) and that the matrices cover "the product families listed below"; Oracle states NO count of product families and NO CVE count | https://www.oracle.com/security-alerts/cspunov2026.html | "This Critical Security Patch Update contains 655 new security patches across the product families listed below." | `oracle/cspunov2026.extract.md` |
| Advisory is Rev 1, initial release 2026-11-17 (no later revision at fetch time) | https://www.oracle.com/security-alerts/cspunov2026.html | "2026-November-17 \| Rev 1. Initial Release." | `oracle/cspunov2026.extract.md` |
| Oracle says risk matrices list only newly addressed vulnerabilities | https://www.oracle.com/security-alerts/cspunov2026.html | "Risk matrices list only security vulnerabilities that are newly addressed by the patches associated with this advisory." | `oracle/cspunov2026.extract.md` |
| Oracle groups Database Server, APEX, Autonomous Health Framework, Global Lifecycle Management and REST Data Services under "Oracle Database Products" in its lead-in (20 patches) | https://www.oracle.com/security-alerts/cspunov2026.html | "This Critical Security Patch Update contains 20 new security patches for Oracle Database Products divided as follows:" | `oracle/cspunov2026.extract.md` |
| Oracle: scoring is CVSS 3.1 | https://www.oracle.com/security-alerts/cspunov2026.html | "Security vulnerabilities are scored using CVSS version 3.1" | `oracle/cspunov2026.extract.md` |
| Oracle: patches only for Premier/Extended Support versions; unsupported releases are not tested | https://www.oracle.com/security-alerts/cspunov2026.html | "Patches released through the Critical Security Patch Update program are provided only for product versions that are covered under the Premier Support or Extended Support phases" | `oracle/cspunov2026.extract.md` |
| Oracle: unsupported releases likely also affected | https://www.oracle.com/security-alerts/cspunov2026.html | "it is likely that earlier versions of affected releases are also affected by these vulnerabilities" | `oracle/cspunov2026.extract.md` |
| Oracle: interim relief is blocking the network protocols an attack requires (no vendor-specific workaround per CVE) | https://www.oracle.com/security-alerts/cspunov2026.html | "it may be possible to reduce the risk of successful attack by blocking network protocols required by an attack" | `oracle/cspunov2026.extract.md` |
| Next release dates | https://www.oracle.com/security-alerts/cspunov2026.html | "15 December 2026 (CSPU)" | `oracle/cspunov2026.extract.md` |
| Next release dates (quarterly CPU) | https://www.oracle.com/security-alerts/cspunov2026.html | "19 January 2027 (CPU)" | `oracle/cspunov2026.extract.md` |
| Tenable (independent, derived from the matrices): 640 unique CVEs in 655 updates across 21 product families | https://www.tenable.com/blog/oracle-november-2026-critical-security-patch-update-addresses-640-cves-cve-2026-114938 | "This CSPU contains fixes for 640 unique CVEs in 655 security updates across 21 Oracle product families." | `oracle/tenable.extract.md` |
| Tenable: 62 critical patches across 57 CVEs (critical = CVSS 9.0+; includes rows that need privileges) | https://www.tenable.com/blog/oracle-november-2026-critical-security-patch-update-addresses-640-cves-cve-2026-114938 | "This month's update includes 62 critical patches across 57 CVEs." | `oracle/tenable.extract.md` |
| Tenable severity table row | https://www.tenable.com/blog/oracle-november-2026-critical-security-patch-update-addresses-640-cves-cve-2026-114938 | "\| Critical \| 62 \| 57 \|" | `oracle/tenable.extract.md` |
| Tenable states Oracle introduced CSPUs in May 2026 | https://www.tenable.com/blog/oracle-november-2026-critical-security-patch-update-addresses-640-cves-cve-2026-114938 | "Beginning in May 2026, Oracle introduced CSPUs as a monthly release cycle" | `oracle/tenable.extract.md` |

Derived by this read from the 655 parsed matrix rows (not stated by Oracle; reproducible from `oracle/cspunov2026.rows.json`): 655 rows = 640 distinct CVE ids (matches Tenable); 62 rows at CVSS 3.1 >= 9.0 = 57 distinct CVEs (matches Tenable); of those 62, 56 rows (51 distinct CVEs) have "Remote Exploit without Auth.? = Yes" and 6 rows need privileges (listed in 1.4). Rows at 10.0: 6 (all unauthenticated). The matrices form 21 risk-matrix sections (Database Products DB, APEX, Autonomous Health Framework, REST Data Services, Application Testing Suite, Commerce, Communications, Construction and Engineering, E-Business Suite, Enterprise Manager, Financial Services, Fusion Middleware, Analytics, Hyperion, Java SE, JD Edwards, MySQL, PeopleSoft, Siebel CRM, Supply Chain, Virtualization) plus Global Lifecycle Management (no matrix, third-party VEX only). The "affected products" table lists 62 product/version lines under 26 Patch Availability Document family labels (my count). Oracle's own lead-in groups DB, APEX, AHF, GLM and ORDS as "20 new security patches for Oracle Database Products".

### 1.2 Oracle's own per-family patch and unauthenticated-row statements (sum of "remotely exploitable without authentication" = 303 rows; Oracle states no grand total)

| family (Oracle section) | patches: Oracle sentence (verbatim) | unauthenticated: Oracle sentence (verbatim) |
|---|---|---|
| Oracle Database Products | "This Critical Security Patch Update contains 7 new security patches, plus additional third party patches noted below, for Oracle Database Products." | "3 of these vulnerabilities may be remotely exploitable without authentication" |
| Oracle APEX | "This Critical Security Patch Update contains 2 new security patches for Oracle APEX." | "Both of these vulnerabilities may be remotely exploitable without authentication" |
| Oracle Autonomous Health Framework | "This Critical Security Patch Update contains 3 new security patches for Oracle Autonomous Health Framework." | "All of these vulnerabilities may be remotely exploitable without authentication" |
| Oracle REST Data Services | "This Critical Security Patch Update contains 8 new security patches for Oracle REST Data Services." | "5 of these vulnerabilities may be remotely exploitable without authentication" |
| Oracle Application Testing Suite | "This Critical Security Patch Update contains 3 new security patches for Oracle Application Testing Suite." | "1 of these vulnerabilities may be remotely exploitable without authentication" |
| Oracle Commerce | "This Critical Security Patch Update contains 6 new security patches for Oracle Commerce." | "All of these vulnerabilities may be remotely exploitable without authentication" |
| Oracle Communications | "This Critical Security Patch Update contains 31 new security patches for Oracle Communications." | "21 of these vulnerabilities may be remotely exploitable without authentication" |
| Oracle Construction and Engineering | "This Critical Security Patch Update contains 2 new security patches for Oracle Construction and Engineering." | "Both of these vulnerabilities may be remotely exploitable without authentication" |
| Oracle E-Business Suite | "This Critical Security Patch Update contains 71 new security patches for Oracle E-Business Suite." | "19 of these vulnerabilities may be remotely exploitable without authentication" |
| Oracle Enterprise Manager | "This Critical Security Patch Update contains 5 new security patches for Oracle Enterprise Manager." | "3 of these vulnerabilities may be remotely exploitable without authentication" |
| Oracle Financial Services Applications | "This Critical Security Patch Update contains 11 new security patches for Oracle Financial Services Applications." | "1 of these vulnerabilities may be remotely exploitable without authentication" |
| Oracle Fusion Middleware | "This Critical Security Patch Update contains 71 new security patches for Oracle Fusion Middleware." | "53 of these vulnerabilities may be remotely exploitable without authentication" |
| Oracle Analytics | "This Critical Security Patch Update contains 29 new security patches for Oracle Analytics." | "9 of these vulnerabilities may be remotely exploitable without authentication" |
| Oracle Hyperion | "This Critical Security Patch Update contains 267 new security patches for Oracle Hyperion." | "107 of these vulnerabilities may be remotely exploitable without authentication" |
| Oracle Java SE | "This Critical Security Patch Update contains 11 new security patches for Oracle Java SE." | "All of these vulnerabilities may be remotely exploitable without authentication" |
| Oracle JD Edwards | "This Critical Security Patch Update contains 1 new security patch for Oracle JD Edwards." | "This vulnerability is not remotely exploitable without authentication" |
| Oracle MySQL | "This Critical Security Patch Update contains 10 new security patches for Oracle MySQL." | "3 of these vulnerabilities may be remotely exploitable without authentication" |
| Oracle PeopleSoft | "This Critical Security Patch Update contains 13 new security patches for Oracle PeopleSoft." | "6 of these vulnerabilities may be remotely exploitable without authentication" |
| Oracle Siebel CRM | "This Critical Security Patch Update contains 19 new security patches for Oracle Siebel CRM." | "9 of these vulnerabilities may be remotely exploitable without authentication" |
| Oracle Supply Chain | "This Critical Security Patch Update contains 74 new security patches for Oracle Supply Chain." | "36 of these vulnerabilities may be remotely exploitable without authentication" |
| Oracle Virtualization | "This Critical Security Patch Update contains 11 new security patches for Oracle Virtualization." | "3 of these vulnerabilities may be remotely exploitable without authentication" |

(All sentences from https://www.oracle.com/security-alerts/cspunov2026.html, saved `oracle/cspunov2026.extract.md`. The page puts a non-breaking space between the two sentences, so quote them separately.)

### 1.3 Rows reachable over the network WITHOUT authentication at CVSS 3.1 >= 9.0 (56 rows, 51 CVEs), grouped by product family

Reading key. "Oracle wording" is the verbatim sentence from Oracle's English text version of the matrices (https://www.oracle.com/security-alerts/cspunov2026verbose.html); the matrix cells (Protocol, "Remote Exploit without Auth.? = Yes", Privs Req'd = None, UI) are from https://www.oracle.com/security-alerts/cspunov2026.html and were verified row by row against the saved extract. Oracle publishes no exploit prerequisites beyond the matrix: no default-config statement, no "feature must be enabled" note and no Notes-column entry exists on any of these 56 rows (the Notes column is non-empty only on the 11 Java SE rows). UI = "Required" rows are marked; they remain unauthenticated and network-reachable but need a person other than the attacker to act.

**Oracle Fusion Middleware (WebLogic Server, Access Manager, Platform Security for Java, SDP, ADF, Managed File Transfer)** (15 rows)

| CVE | product / component | protocol | CVSS | vector | supported versions affected | Oracle wording (verbatim) |
|---|---|---|---|---|---|---|
| CVE-2026-114824 | Oracle Platform Security for Java / Centralized Thirdparty Jars | HTTP | 10.0 (scope change) | AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H | 12.2.1.4.0, 14.1.2.0.0 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Platform Security for Java." |
| CVE-2026-114835 | Oracle Access Manager / Admin Console | HTTP | 10.0 (scope change) | AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H | 12.2.1.4.0, 14.1.2.1.0 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Access Manager." |
| CVE-2026-91500 | Oracle Access Manager / Authentication Engine | HTTP | 10.0 (scope change) | AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:L | 12.2.1.4.0, 14.1.2.1.0 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Access Manager." |
| CVE-2026-91510 | Oracle Access Manager / Authentication Engine | HTTP | 10.0 (scope change) | AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:L | 12.2.1.4.0, 14.1.2.1.0 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Access Manager." |
| CVE-2026-91569 | Oracle WebLogic Server / TopLink Integration | HTTP | 10.0 (scope change) | AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H | 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0, 15.1.1.0.0 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle WebLogic Server." |
| CVE-2026-114826 | Service Delivery Platform / Messaging Enabler | SOAP | 9.8 | AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H | 14.1.2.0.0 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via SOAP to compromise Service Delivery Platform." |
| CVE-2026-91456 | Oracle WebLogic Server / Core | SOAP | 9.8 | AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H | 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0, 15.1.1.0.0 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via SOAP to compromise Oracle WebLogic Server." |
| CVE-2026-91470 | Oracle WebLogic Server / Core | T3, IIOP | 9.8 | AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H | 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0, 15.1.1.0.0 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via T3, IIOP to compromise Oracle WebLogic Server." |
| CVE-2026-91570 | Oracle WebLogic Server / TopLink Integration | HTTP | 9.8 | AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H | 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0, 15.1.1.0.0 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle WebLogic Server." |
| CVE-2026-91583 | Oracle WebLogic Server / TopLink Integration | HTTP | 9.8 | AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H | 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0, 15.1.1.0.0 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle WebLogic Server." |
| CVE-2026-91585 | Oracle WebLogic Server / TopLink Integration | TCP | 9.8 | AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H | 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0, 15.1.1.0.0 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via TCP to compromise Oracle WebLogic Server." |
| CVE-2026-91469 | Oracle WebLogic Server / Core | HTTP | 9.4 | AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:H/A:H | 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0, 15.1.1.0.0 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle WebLogic Server." |
| CVE-2026-91507 | Oracle Access Manager / Authentication Engine | HTTP | 9.3 (scope change) | AV:N/AC:L/PR:N/UI:N/S:C/C:L/I:H/A:N | 12.2.1.4.0, 14.1.2.1.0 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Access Manager." |
| CVE-2026-8763 | Oracle Managed File Transfer / MFT Runtime Server (Bouncy Castle Java Library) | HTTPS | 9.1 | AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N | 12.2.1.4.0 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTPS to compromise Oracle Managed File Transfer." |
| CVE-2026-91618 | Oracle Application Development Framework (ADF) / Security Framework | HTTP | 9.1 | AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N | 12.2.1.4.0 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Application Development Framework (ADF)." |

**Oracle Analytics** (1 rows)

| CVE | product / component | protocol | CVSS | vector | supported versions affected | Oracle wording (verbatim) |
|---|---|---|---|---|---|---|
| CVE-2026-114784 | Oracle Business Intelligence Enterprise Edition / Platform Security | HTTP | 10.0 (scope change) | AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H | 8.2.0.0.0, 26.01.0.0.0 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Business Intelligence Enterprise Edition." |

**Oracle E-Business Suite** (6 rows)

| CVE | product / component | protocol | CVSS | vector | supported versions affected | Oracle wording (verbatim) |
|---|---|---|---|---|---|---|
| CVE-2026-114863 | Oracle Universal Work Queue / Media Integration issues | HTTP | 9.8 | AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H | 12.2.3-12.2.15 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Universal Work Queue." |
| CVE-2026-114880 | Document Management and Collaboration / Attachments | HTTP | 9.8 | AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H | 12.2.3-12.2.15 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Document Management and Collaboration." |
| CVE-2026-114924 | Oracle Application Object Library / Core | HTTP | 9.8 | AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H | 12.2.3-12.2.15 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Application Object Library." |
| CVE-2026-114925 | Oracle Applications Framework / REST Services | HTTP | 9.8 | AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H | 12.2.3-12.2.15 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Applications Framework." |
| CVE-2026-101691 | Oracle Mobile Field Service / Admin UI | HTTP | 9.3 (scope change) | AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:L/A:N | 12.2.3-12.2.15 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Mobile Field Service." |
| CVE-2026-114881 | Document Management and Collaboration / Attachments | HTTP | 9.1 | AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:H | 12.2.3-12.2.15 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Document Management and Collaboration." |

**Oracle PeopleSoft** (3 rows)

| CVE | product / component | protocol | CVSS | vector | supported versions affected | Oracle wording (verbatim) |
|---|---|---|---|---|---|---|
| CVE-2026-111497 | PeopleSoft Enterprise PeopleTools / OpenSearch Dashboards (Node.js) | HTTP | 9.8 | AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H | 8.61-8.63 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise PeopleSoft Enterprise PeopleTools." |
| CVE-2026-114934 | PeopleSoft Enterprise PeopleTools / Integration Broker | HTTP | 9.3 (scope change) | AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:L/A:N | 8.61-8.63 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise PeopleSoft Enterprise PeopleTools." |
| CVE-2026-114862 | PeopleSoft Enterprise PeopleTools / Weblogic | HTTP | 9.1 | AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N | 8.61-8.63 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise PeopleSoft Enterprise PeopleTools." |

**Oracle Database Products: APEX** (2 rows)

| CVE | product / component | protocol | CVSS | vector | supported versions affected | Oracle wording (verbatim) |
|---|---|---|---|---|---|---|
| CVE-2026-114849 | Oracle APEX / General | HTTPS | 9.8 | AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H | 24.1.22, 24.2.21, 26.1.5, 26.2.0 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTPS to compromise Oracle APEX." |
| CVE-2026-114850 | Oracle APEX / General | HTTPS | 9.8 | AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H | 24.1.22, 24.2.21, 26.1.5, 26.2.0 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTPS to compromise Oracle APEX." |

**Oracle Database Products: REST Data Services** (2 rows)

| CVE | product / component | protocol | CVSS | vector | supported versions affected | Oracle wording (verbatim) |
|---|---|---|---|---|---|---|
| CVE-2026-114849 | Oracle REST Data Services / Core | HTTPS | 9.8 | AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H | 24.2.0-26.3.0 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTPS to compromise Oracle REST Data Services." |
| CVE-2026-114856 | Oracle REST Data Services / General | HTTPS | 9.6 (UI Required) (scope change) | AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H | 24.2.0-26.3.0 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTPS to compromise Oracle REST Data Services." |

**Oracle Database Products: Autonomous Health Framework** (1 rows)

| CVE | product / component | protocol | CVSS | vector | supported versions affected | Oracle wording (verbatim) |
|---|---|---|---|---|---|---|
| CVE-2026-114847 | Oracle Autonomous Health Framework / Developer triaging platform | HTTP | 9.1 | AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N | 26.4-26.10 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Autonomous Health Framework." |

**Oracle Hyperion** (11 rows)

| CVE | product / component | protocol | CVSS | vector | supported versions affected | Oracle wording (verbatim) |
|---|---|---|---|---|---|---|
| CVE-2026-115047 | Oracle Hyperion Infrastructure Technology / Installation and Configuration | HTTP | 9.8 | AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H | 11.2.26.0.000 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Hyperion Infrastructure Technology." |
| CVE-2026-115048 | Oracle Hyperion Infrastructure Technology / Common Security | HTTP | 9.8 | AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H | 11.2.26.0.000 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Hyperion Infrastructure Technology." |
| CVE-2026-115080 | Oracle Hyperion Infrastructure Technology / Installation and Configuration | HTTP | 9.8 | AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H | 11.2.26.0.000 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Hyperion Infrastructure Technology." |
| CVE-2026-115086 | Oracle Hyperion Planning / Security | RMI | 9.8 | AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H | 11.2.26.0.000 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via RMI to compromise Oracle Hyperion Planning." |
| CVE-2026-115089 | Oracle Hyperion Planning / Application Development Framework | HTTP | 9.8 | AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H | 11.2.26.0.000 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Hyperion Planning." |
| CVE-2026-114785 | Oracle Hyperion Planning / Security | HTTP | 9.6 (UI Required) (scope change) | AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H | 11.2.26.0.000 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Hyperion Planning." |
| CVE-2026-114956 | Oracle Hyperion Planning / Security | HTTP | 9.3 (UI Required) (scope change) | AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:N | 11.2.26.0.000 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Hyperion Planning." |
| CVE-2026-115139 | Oracle Hyperion Infrastructure Technology / Installation and Configuration | HTTP | 9.3 (UI Required) (scope change) | AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:N | 11.2.26.0.000 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Hyperion Infrastructure Technology." |
| CVE-2026-115050 | Oracle Hyperion Infrastructure Technology / Installation and Configuration | HTTP | 9.1 | AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N | 11.2.26.0.000 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Hyperion Infrastructure Technology." |
| CVE-2026-127362 | Oracle Hyperion Financial Close Management / Reconciliation Manage | HTTP | 9.1 | AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N | 11.2.26.0.000 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Hyperion Financial Close Management." |
| CVE-2026-127369 | Oracle Hyperion Financial Close Management / Reconciliation Manage | Oracle Net | 9.1 | AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N | 11.2.26.0.000 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via Oracle Net to compromise Oracle Hyperion Financial Close Management." |

**Oracle Supply Chain** (5 rows)

| CVE | product / component | protocol | CVSS | vector | supported versions affected | Oracle wording (verbatim) |
|---|---|---|---|---|---|---|
| CVE-2026-127324 | Oracle AutoVue / Security | HTTP | 9.8 | AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H | 21.1.0 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle AutoVue." |
| CVE-2026-127325 | Oracle AutoVue / Security | HTTP | 9.8 | AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H | 21.1.0 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle AutoVue." |
| CVE-2026-127326 | Oracle AutoVue / Security | HTTP | 9.8 | AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H | 21.1.0 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle AutoVue." |
| CVE-2026-127327 | Oracle AutoVue / Security | HTTP | 9.8 | AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H | 21.1.0 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle AutoVue." |
| CVE-2026-101356 | Oracle Agile PLM / File Manager (Apache Tomcat) | HTTP/2 | 9.1 | AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:H | 9.3.6 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP/2 to compromise Oracle Agile PLM." |

**Oracle Communications** (7 rows)

| CVE | product / component | protocol | CVSS | vector | supported versions affected | Oracle wording (verbatim) |
|---|---|---|---|---|---|---|
| CVE-2026-111497 | Oracle Communications Diameter Signaling Router / PMAC (Node.js) | HTTP | 9.8 | AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H | 9.0.0.0.0-9.3.0.0.0 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Communications Diameter Signaling Router." |
| CVE-2026-111497 | Oracle Communications Unified Assurance / Core (Brotli) | HTTP | 9.8 | AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H | 6.1.1-7.0.0 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Communications Unified Assurance." |
| CVE-2026-1229 | Oracle Communications Unified Assurance / Core (CIRCL) | HTTP | 9.8 | AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H | 6.1.1-7.0.0 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Communications Unified Assurance." |
| CVE-2026-41889 | Oracle Communications Unified Assurance / Core (PostgreSQL) | SQL | 9.8 | AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H | 6.1.1-7.0.0 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via SQL to compromise Oracle Communications Unified Assurance." |
| CVE-2026-114820 | Oracle Communications Element Manager / Core (Java) | HTTPS | 9.1 | AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N | 9.0.3-9.0.5 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTPS to compromise Oracle Communications Element Manager." |
| CVE-2026-114820 | Oracle Communications Unified Assurance / Core (Java) | HTTPS | 9.1 | AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N | 6.1.1-7.0.0 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTPS to compromise Oracle Communications Unified Assurance." |
| CVE-2026-114820 | Oracle Communications Unified Inventory Management / Security (Java) | HTTPS | 9.1 | AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N | 7.5.0, 7.5.1, 7.6.0, 7.7.0, 7.8.0, 8.0.1, 8.26.0 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTPS to compromise Oracle Communications Unified Inventory Management." |

**Oracle Enterprise Manager** (1 rows)

| CVE | product / component | protocol | CVSS | vector | supported versions affected | Oracle wording (verbatim) |
|---|---|---|---|---|---|---|
| CVE-2026-10050 | Oracle Enterprise Manager Base Platform / Agent Next Gen (Eclipse Jetty) | HTTP | 9.1 | AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:H | 13.5, 24.1 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Enterprise Manager Base Platform." |

**Oracle MySQL** (2 rows)

| CVE | product / component | protocol | CVSS | vector | supported versions affected | Oracle wording (verbatim) |
|---|---|---|---|---|---|---|
| CVE-2026-115557 | MySQL Shell / Shell: Core Client (Python) | HTTP | 9.8 | AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H | 26.10.0 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise MySQL Shell." |
| CVE-2026-114952 | MySQL Server, MySQL Cluster / Client programs | MySQL Protocol | 9.1 | AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N | MySQL Server: 8.4.0-8.4.13, 9.7.0-9.7.4, 26.10; MySQL Cluster: 8.0.0-8.0.50, 8.4.0-8.4.13, 9.7.0-9.7.4, 26.10 | "Easily exploitable vulnerability allows unauthenticated attacker with network access via multiple protocols to compromise MySQL Server, MySQL Cluster." |

Machine-readable copy of the 56 rows: `work/2026-11-18T0356Z-intel/bodies/FU2/oracle/oracle-unauth-ge9.tsv`.

Note on scope: "unauthenticated" here is Oracle's "Remote Exploit without Auth.? = Yes" column; every one of the 56 rows also has Attack Vector Network, Attack Complexity Low and Privs Req'd None (checked), and 52 of 56 also have User Interaction None. The four UI-Required rows are CVE-2026-114856 (ORDS General, 9.6), CVE-2026-114785 (Hyperion Planning Security, 9.6), CVE-2026-115139 and CVE-2026-114956 (Hyperion, 9.3).

### 1.4 Rows at >= 9.0 that are NOT unauthenticated (6 rows) - do not count these as pre-auth

| CVE | product / component | CVSS | Oracle's privilege wording (verbatim) |
|---|---|---|---|
| CVE-2026-114819 | Oracle Database Server / Oracle Text (Database (DB)) | 9.9 | "Easily exploitable vulnerability allows low privileged attacker having Create Session privilege with network access via Oracle Net to compromise Oracle Text." |
| CVE-2026-114822 | Oracle Database Server / RDBMS (Database (DB)) | 9.9 | "Easily exploitable vulnerability allows low privileged attacker having Create Session privilege with network access via Oracle Net to compromise RDBMS." |
| CVE-2026-114848 | Oracle Database Server / Oracle Text (Database (DB)) | 9.9 | "Easily exploitable vulnerability allows low privileged attacker having Create Session privilege with network access via Oracle Net to compromise Oracle Text." |
| CVE-2026-114978 | Oracle Hyperion Financial Management / Security (Hyperion) | 9.9 | "Easily exploitable vulnerability allows low privileged attacker with network access via HTTP to compromise Oracle Hyperion Financial Management." |
| CVE-2026-114980 | Oracle AutoVue / Security Related Issues (Supply Chain) | 9.9 | "Easily exploitable vulnerability allows low privileged attacker with network access via HTTP to compromise Oracle AutoVue." |
| CVE-2026-91561 | Oracle Service Bus / Core (Fusion Middleware) | 9.6 | "Easily exploitable vulnerability allows low privileged attacker with network access via RMI to compromise Oracle Service Bus." |

Database 9.9 rows confirmed: Oracle's matrix has a "Package and/or Privilege Required" column for the Database table and lists "Create Session" for all three, with "Remote Exploit without Auth.? = No":

| claim | source URL | verbatim passage | saved body |
|---|---|---|---|
| CVE-2026-114819 Oracle Text 9.9: needs Create Session, not unauthenticated | https://www.oracle.com/security-alerts/cspunov2026.html | "\| CVE-2026-114819 \| Oracle Text \| Create Session \| Oracle Net \| No \| 9.9 \|" | `oracle/cspunov2026.extract.md` |
| CVE-2026-114848 Oracle Text 9.9: needs Create Session, not unauthenticated | https://www.oracle.com/security-alerts/cspunov2026.html | "\| CVE-2026-114848 \| Oracle Text \| Create Session \| Oracle Net \| No \| 9.9 \|" | `oracle/cspunov2026.extract.md` |
| CVE-2026-114822 RDBMS 9.9: needs Create Session, not unauthenticated | https://www.oracle.com/security-alerts/cspunov2026.html | "\| CVE-2026-114822 \| RDBMS \| Create Session \| Oracle Net \| No \| 9.9 \|" | `oracle/cspunov2026.extract.md` |
| Oracle: only 3 Database Products-table rows are unauthenticated (these are the third-party OpenSSL 7.5, Python 7.4, Apache HttpClient 4.3 rows) | https://www.oracle.com/security-alerts/cspunov2026.html | "3 of these vulnerabilities may be remotely exploitable without authentication" | `oracle/cspunov2026.extract.md` |
| Oracle wording for the 9.9 Oracle Text row | https://www.oracle.com/security-alerts/cspunov2026verbose.html | "Easily exploitable vulnerability allows low privileged attacker having Create Session privilege with network access via Oracle Net to compromise Oracle Text." | `oracle/cspunov2026verbose.extract.md` |
| Unauthenticated Database-table rows are third-party components, max 7.5 | https://www.oracle.com/security-alerts/cspunov2026.html | "\| CVE-2026-72897 \| RDBMS (OpenSSL) \| None \| TLS \| Yes \| 7.5 \|" | `oracle/cspunov2026.extract.md` |

Pre-release headline check (the "22 unauthenticated EBS rows" and "unauthenticated Database/APEX rows up to 9.9" came from the 2026-11-12 pre-release page as recorded in `state/coverage_backlog.md` row B of run 2026-11-17T0355Z; that page was replaced by the published advisory, so the pre-release text itself could not be re-read and only the published numbers are confirmed here):

| claim | source URL | verbatim passage | saved body |
|---|---|---|---|
| E-Business Suite: published page says 71 patches, 19 unauthenticated (NOT 22) | https://www.oracle.com/security-alerts/cspunov2026.html | "19 of these vulnerabilities may be remotely exploitable without authentication" | `oracle/cspunov2026.extract.md` |
| Tenable independently counts 19 unauthenticated EBS rows | https://www.tenable.com/blog/oracle-november-2026-critical-security-patch-update-addresses-640-cves-cve-2026-114938 | "\| Oracle E-Business Suite \| 71 \| 19 \|" | `oracle/tenable.extract.md` |
| APEX: both rows unauthenticated at 9.8 (not 9.9) | https://www.oracle.com/security-alerts/cspunov2026.html | "Both of these vulnerabilities may be remotely exploitable without authentication" | `oracle/cspunov2026.extract.md` |
| APEX row CVE-2026-114849: 9.8, HTTPS, supported 24.1.22, 24.2.21, 26.1.5, 26.2.0 | https://www.oracle.com/security-alerts/cspunov2026.html | "\| CVE-2026-114849 \| Oracle APEX \| General \| HTTPS \| Yes \| 9.8 \|" | `oracle/cspunov2026.extract.md` |

### 1.5 Brotli CVE-2026-111497 (CISA KEV) - three rows

| claim | source URL | verbatim passage | saved body |
|---|---|---|---|
| Row 1: Communications Diameter Signaling Router, component labelled PMAC (Node.js), 9.8, HTTP, unauthenticated; supported 9.0.0.0.0-9.3.0.0.0 | https://www.oracle.com/security-alerts/cspunov2026.html | "\| CVE-2026-111497 \| Oracle Communications Diameter Signaling Router \| PMAC (Node.js) \| HTTP \| Yes \| 9.8 \|" | `oracle/cspunov2026.extract.md` |
| Row 2: Communications Unified Assurance, component labelled Core (Brotli), 9.8, HTTP, unauthenticated; supported 6.1.1-7.0.0 (the only row that says "Brotli") | https://www.oracle.com/security-alerts/cspunov2026.html | "\| CVE-2026-111497 \| Oracle Communications Unified Assurance \| Core (Brotli) \| HTTP \| Yes \| 9.8 \|" | `oracle/cspunov2026.extract.md` |
| Row 3: PeopleSoft PeopleTools, component labelled OpenSearch Dashboards (Node.js), 9.8, HTTP, unauthenticated; supported 8.61-8.63 | https://www.oracle.com/security-alerts/cspunov2026.html | "\| CVE-2026-111497 \| PeopleSoft Enterprise PeopleTools \| OpenSearch Dashboards (Node.js) \| HTTP \| Yes \| 9.8 \|" | `oracle/cspunov2026.extract.md` |
| Oracle states the same CVE id appears in every matrix it affects | https://www.oracle.com/security-alerts/cspunov2026.html | "A vulnerability that affects multiple products will appear with the same CVE ID in all risk matrices." | `oracle/cspunov2026.extract.md` |
| Footnote under the Communications table | https://www.oracle.com/security-alerts/cspunov2026.html | "The patch for CVE-2026-111497 also addresses CVE-2026-105482, CVE-2026-105483, and CVE-2026-106069." | `oracle/cspunov2026.extract.md` |
| Footnote under the PeopleSoft table | https://www.oracle.com/security-alerts/cspunov2026.html | "The patch for CVE-2026-111497 also addresses CVE-2026-105481, CVE-2026-105482, CVE-2026-105483, CVE-2026-106069, CVE-2026-106070, CVE-2026-106071, CVE-2026-106072, CVE-2026-106073, and CVE-2026-106074." | `oracle/cspunov2026.extract.md` |
| CISA KEV: CVE-2026-111497 = Google Brotli, added 2026-10-27, ransomware use Unknown | https://www.cisa.gov/known-exploited-vulnerabilities-catalog (via `fetch_source.py cisa-kev`, catalogVersion 2026.11.17) | "KEV CVE-2026-111497 \| vendorProject: Google \| product: Brotli \| vulnerabilityName: Google Brotli Unchecked Return Value Vulnerability \| dateAdded: 2026-10-27 \| knownRansomwareCampaignUse: Unknown" | `oracle/kev-records.txt` |

Caveat: only the Unified Assurance row names Brotli; Oracle labels the other two rows "Node.js". Tying all three rows to the Brotli flaw rests on the shared CVE id plus CISA KEV naming CVE-2026-111497 as Google Brotli, not on any Oracle sentence about Node.js bundling Brotli. Oracle does not say the KEV-listed flaw is exploited in Oracle products. It is the only one of the 640 matrix CVEs on KEV (checked by set intersection against the 1782-entry catalogue fetched 2026-11-18); `oracle/cisa-kev.json`.

### 1.6 Java SE and CVE-2026-114938 (Java4Shell)

| claim | source URL | verbatim passage | saved body |
|---|---|---|---|
| Java SE section: 11 patches, all flagged remotely exploitable without authentication | https://www.oracle.com/security-alerts/cspunov2026.html | "All of these vulnerabilities may be remotely exploitable without authentication" | `oracle/cspunov2026.extract.md` |
| The matrix INCLUDES CVE-2026-114938: component Compiler, protocol Multiple, unauthenticated, CVSS 8.1 (so it is not in the >= 9.0 set) | https://www.oracle.com/security-alerts/cspunov2026.html | "\| CVE-2026-114938 \| Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition \| Compiler \| Multiple \| Yes \| 8.1 \|" | `oracle/cspunov2026.extract.md` |
| Oracle wording for the row ("Difficult to exploit"; Attack Complexity High) | https://www.oracle.com/security-alerts/cspunov2026verbose.html | "Difficult to exploit vulnerability allows unauthenticated attacker with network access via multiple protocols to compromise Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition." | `oracle/cspunov2026verbose.extract.md` |
| Oracle wording: takeover | https://www.oracle.com/security-alerts/cspunov2026verbose.html | "Successful attacks of this vulnerability can result in takeover of Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition." | `oracle/cspunov2026verbose.extract.md` |
| Supported versions Oracle lists for the row (note: plain 8u511b33 and 11.0.33.0.3 are NOT in this row; 8u511b33-perf, 17, 21, 25 and 27 are) | https://www.oracle.com/security-alerts/cspunov2026verbose.html | "Supported versions that are affected are Oracle Java SE: 8u511b33-perf, 17.0.21.0.3, 21.0.13.0.3, 25.0.5.0.3, 27.0.1.0.3; Oracle GraalVM for JDK: 17.0.21.0.3 and 21.0.13.0.3; Oracle GraalVM Enterprise Edition: 21.3.20.0.3." | `oracle/cspunov2026verbose.extract.md` |
| Oracle note 1 attached to the row (server-side web-service exposure, not only applets) | https://www.oracle.com/security-alerts/cspunov2026.html | "1. This vulnerability can only be exploited by supplying data to APIs in the specified Component without using Untrusted Java Web Start applications or Untrusted Java applets, such as through a web service." | `oracle/cspunov2026.extract.md` |
| Oracle: Java scores assume applet/Web Start user has administrator privileges | https://www.oracle.com/security-alerts/cspunov2026.html | "The CVSS scores below assume that a user running a Java applet or Java Web Start application has administrator privileges" | `oracle/cspunov2026.extract.md` |
| Highest Java SE row in this CSPU is 8.1; there is no Java SE row at >= 9.0 | https://www.oracle.com/security-alerts/cspunov2026.html | "\| CVE-2026-114938 \| Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition \| Compiler \| Multiple \| Yes \| 8.1 \|" | `oracle/cspunov2026.extract.md` |
| Tenable: CVSS 8.1, details expected, FAQ planned | https://www.tenable.com/blog/oracle-november-2026-critical-security-patch-update-addresses-640-cves-cve-2026-114938 | "technical details about this vulnerability are expected to be released soon" | `oracle/tenable.extract.md` |
| Oracle credits the finders of CVE-2026-114938 | https://www.oracle.com/security-alerts/cspunov2026.html | "Albert Yang: CVE-2026-114938" | `oracle/cspunov2026.extract.md` |
| Oracle credits the finders of CVE-2026-114938 (second credit) | https://www.oracle.com/security-alerts/cspunov2026.html | "Quang Luong of Calif.io: CVE-2026-114938" | `oracle/cspunov2026.extract.md` |

### 1.7 Exploitation, disclosure and write-up status of the >= 9.0 rows

| claim | source URL | verbatim passage | saved body |
|---|---|---|---|
| Oracle flags no row as exploited or publicly disclosed; its only exploitation language is generic (about already-patched flaws and unpatched customers) | https://www.oracle.com/security-alerts/cspunov2026.html | "Oracle continues to periodically receive reports of attempts to maliciously exploit vulnerabilities for which Oracle has already released security patches." | `oracle/cspunov2026.extract.md` |
| Oracle generic sentence, second half | https://www.oracle.com/security-alerts/cspunov2026.html | "it has been reported that attackers have been successful because targeted customers had failed to apply available Oracle patches" | `oracle/cspunov2026.extract.md` |
| Oracle reminds customers of four earlier Security Alerts (Oct 21: CVE-2026-91403; Oct 24: CVE-2026-114820; Oct 25: CVE-2026-109618 and CVE-2026-109619); these are NOT new rows except CVE-2026-114820 | https://www.oracle.com/security-alerts/cspunov2026.html | "Oracle released Security Alerts on October 21, 2026 for" | `oracle/cspunov2026.extract.md` |
| CVE-2026-114820 appears in three Communications rows at 9.1 (Element Manager, Unified Assurance, Unified Inventory Management) | https://www.oracle.com/security-alerts/cspunov2026.html | "\| CVE-2026-114820 \| Oracle Communications Element Manager \| Core (Java) \| HTTPS \| Yes \| 9.1 \|" | `oracle/cspunov2026.extract.md` |
| Oracle Security Alert for CVE-2026-114820 describes it as removal of root CA certificates (eMudhra), not an exploited code flaw | https://www.oracle.com/security-alerts/alert-cve-2026-114820.html | "This Security Alert addresses CVE-2026-114820 by providing Java updates that remove the set of impacted root CA certificates related to eMudhra." | `oracle/alert-cve-2026-114820.extract.md` |
| CISA KEV: PHP CVE-2026-109618 and CVE-2026-109619 (Oracle Security Alert of Oct 25) are on KEV since 2026-10-26; they are not rows of this CSPU (set intersection) | https://www.cisa.gov/known-exploited-vulnerabilities-catalog (via `fetch_source.py cisa-kev`, catalogVersion 2026.11.17) | ""vulnerabilityName": "PHP Memory Corruption Vulnerability"" | `oracle/cisa-kev.json` |
| Footnote: the patch for the EBS row CVE-2026-114918 ALSO ADDRESSES CVE-2025-61882 (KEV, Cl0p-era EBS flaw) | https://www.oracle.com/security-alerts/cspunov2026.html | "The patch for CVE-2026-114918 also addresses CVE-2025-61882." | `oracle/cspunov2026.extract.md` |
| That EBS row: Oracle Concurrent Processing / BI Publisher Integration, 8.7, high privileges required (not unauthenticated) | https://www.oracle.com/security-alerts/cspunov2026.html | "\| CVE-2026-114918 \| Oracle Concurrent Processing \| BI Publisher Integration \| HTTP \| No \| 8.7 \|" | `oracle/cspunov2026.extract.md` |
| Oracle wording for it: "high privileged attacker" | https://www.oracle.com/security-alerts/cspunov2026verbose.html | "Easily exploitable vulnerability allows high privileged attacker with network access via HTTP to compromise Oracle Concurrent Processing." | `oracle/cspunov2026verbose.extract.md` |
| CISA KEV: CVE-2025-61882 = Oracle E-Business Suite, added 2025-10-06, ransomware use Known | https://www.cisa.gov/known-exploited-vulnerabilities-catalog (via `fetch_source.py cisa-kev`, catalogVersion 2026.11.17) | "KEV CVE-2025-61882 \| vendorProject: Oracle \| product: E-Business Suite \| vulnerabilityName: Oracle E-Business Suite Unspecified Vulnerability \| dateAdded: 2025-10-06 \| knownRansomwareCampaignUse: Known" | `oracle/kev-records.txt` |
| Oracle credits ZDI-affiliated researchers for CVE-2026-114849 (APEX/ORDS, 9.8): an anonymous researcher | https://www.oracle.com/security-alerts/cspunov2026.html | "An Anonymous researcher working with Trend Micro's Zero Day Initiative: CVE-2026-114849" | `oracle/cspunov2026.extract.md` |
| Oracle credits ZDI-affiliated researchers for CVE-2026-114850 (APEX 9.8) and CVE-2026-114822 (RDBMS 9.9) | https://www.oracle.com/security-alerts/cspunov2026.html | "Ikotas Labs working with Trend Micro's Zero Day Initiative: CVE-2026-114822, CVE-2026-114850" | `oracle/cspunov2026.extract.md` |
| Oracle credit for CVE-2026-114835 (Access Manager Admin Console 10.0) | https://www.oracle.com/security-alerts/cspunov2026.html | "Phuoc Pham & Son Tran from starfishsec.com: CVE-2026-114835" | `oracle/cspunov2026.extract.md` |
| Oracle credit for CVE-2026-114819 (Oracle Text 9.9, needs Create Session) | https://www.oracle.com/security-alerts/cspunov2026.html | "Zheng Yu of depthfirst: CVE-2026-114819" | `oracle/cspunov2026.extract.md` |
| Oracle credit for CVE-2026-114925 (EBS Applications Framework REST Services 9.8) | https://www.oracle.com/security-alerts/cspunov2026.html | "Tomais Williamson: CVE-2026-114925" | `oracle/cspunov2026.extract.md` |
| NCSC-NL covers only the Java row so far (advisory NCSC-2026-0495, published 2026-11-17 21:55Z) | https://advisories.ncsc.nl/advisory?id=NCSC-2026-0495 | "In dit beveiligingsadvies gaan we uitsluitend in op CVE-2026-114938, de rest van de kwetsbaarheden zal hierin later worden aangevuld." | `oracle/ncsc-nl-recent.txt` |
| NCSC-NL: Java compiler flaw not easy to exploit because of multiple requirements | https://advisories.ncsc.nl/advisory?id=NCSC-2026-0495 | "niet eenvoudig te misbruiken" | `oracle/ncsc-nl-recent.txt` |
| NCSC-CH Security Hub post 13198 is the Java4Shell advisory (edited into it from the pre-release CSPU text) | https://security-hub.ncsc.admin.ch/#/posts/13198 | "[Advisory] Java4Shell (CVE-2026-114938): Critical Remote Code Execution, Patch Now" | `oracle/ncsc-csh-recent.txt` |

Absence checks (all fetched 2026-11-18 between 04:40Z and 04:56Z; an absence is "not found", never "does not exist"):

- BSI CERT-Bund RSS (`bsi-rss`, saved `oracle/bsi-rss.txt`): the only Oracle items are [UPDATE] entries on older WID-SEC ids (Java SE x4, MySQL x3, all pubDate 2026-11-17 07:27-11:07Z); no new Oracle CSPU advisory yet.
- CERT-EU (`cert-eu recent 20` returned its 10 most recent advisories, newest dated 2026-11-12, `oracle/cert-eu-recent.txt`) and CERT-FR (`cert-fr avis-recent 30`, 30 avis dated 2026-11-13..17, `oracle/cert-fr-recent.txt`): no Oracle CSPU item.
- ENISA EUVD: `api/search?text=oracle&fromDate=2026-11-16&toDate=2026-11-18` returns 583 Oracle records (all 6 pages read, `oracle/euvd-oracle-search*.json`); none carries `exploitedSince`; the EUVD "exploited" feed (`oracle/euvd-exploited.json`) lists none of the 640 CSPU CVEs.
- CISA KEV: only CVE-2026-111497 of the 640 (above). Neither CVE-2025-61882 nor CVE-2023-44487 is a CSPU row; they appear only in "also addresses" footnotes (CVE-2026-27135 Communications BRM nghttp2 row 7.5 also addresses CVE-2023-44487).
- Public write-ups: WebSearch queries for CVE-2026-114835 / CVE-2026-91470 / CVE-2026-114849 / CVE-2026-114850 / CVE-2026-114819 / "starfishsec" / "depthfirst" / ZDI / Rapid7 / Qualys returned no page naming these ids (search engine index of the last 36 h is thin; this is weak evidence of absence). Tenable lists its plugins as "will appear" (not yet). No Rapid7, ZDI, Qualys or SANS write-up found for the CSPU.

### 1.8 Strongest rows for a Swiss public-sector defender (analyst ranking on stated facts; the ranking is an assessment of this read, not an Oracle or third-party claim)

Ranking facts used: (a) Oracle marks the row unauthenticated, network, low complexity, no privileges; (b) Oracle's CVSS 3.1 score and whether "scope change" is flagged; (c) the component is a gateway, identity or web-facing tier that is commonly published (assessment); (d) supported versions are current branches, i.e. patches exist for what is deployed; (e) no row has a public write-up or exploitation report at fetch time, so none can be ranked up on exploitation.

1. **WebLogic Server** (12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0, 15.1.1.0.0): CVE-2026-91569 TopLink Integration HTTP 10.0 scope change; CVE-2026-91470 Core T3, IIOP 9.8; CVE-2026-91456 Core SOAP 9.8; CVE-2026-91570 and CVE-2026-91583 TopLink HTTP 9.8; CVE-2026-91585 TopLink TCP 9.8; CVE-2026-91469 Core HTTP 9.4. Oracle wording for each: "unauthenticated attacker with network access" ending in "takeover of Oracle WebLogic Server" (CVE-2026-91470 row verbatim: "Easily exploitable vulnerability allows unauthenticated attacker with network access via T3, IIOP to compromise Oracle WebLogic Server."). Seven unauthenticated rows on one product; T3/IIOP is the one with a protocol-level interim control (block the protocol), which Oracle's generic text endorses.
2. **Oracle Access Manager** (12.2.1.4.0, 14.1.2.1.0): CVE-2026-114835 Admin Console 10.0, CVE-2026-91500 and CVE-2026-91510 Authentication Engine 10.0, CVE-2026-91507 Authentication Engine 9.3, all HTTP, all "scope change". Identity/SSO tier (assessment: large blast radius; Oracle itself flags that "attacks may significantly impact additional products"). Oracle's credit line names starfishsec.com for CVE-2026-114835.
3. **Oracle Platform Security for Java** (12.2.1.4.0, 14.1.2.0.0): CVE-2026-114824 "Centralized Thirdparty Jars", HTTP, 10.0 scope change. It is a library component present under WebLogic/Fusion Middleware domains (assessment); Oracle states no prerequisites.
4. **Oracle Business Intelligence Enterprise Edition**: CVE-2026-114784 Platform Security, HTTP, 10.0 scope change; the matrix row lists 8.2.0.0.0 and 26.01.0.0.0 only (the affected-products table also lists 12.2.1.4.0 for BI EE, so 12.2.1.4.0 is NOT in this CVE row: check before asserting).
5. **E-Business Suite 12.2.3-12.2.15** (6 rows): CVE-2026-114880 and CVE-2026-114881 Document Management and Collaboration/Attachments (9.8, 9.1), CVE-2026-114924 Application Object Library/Core (9.8), CVE-2026-114925 Applications Framework/REST Services (9.8), CVE-2026-114863 Universal Work Queue/Media Integration issues (9.8), CVE-2026-101691 Mobile Field Service/Admin UI (9.3), all HTTP. ERP in cantonal and communal finance and HR (assessment). Context facts: CISA KEV lists EBS CVE-2025-61882 with ransomware use "Known", and this CSPU's footnote says the patch for the EBS row CVE-2026-114918 (needs high privileges) also addresses CVE-2025-61882.
6. **APEX and ORDS**: CVE-2026-114849 (9.8; one id in the APEX row and the ORDS Core row), CVE-2026-114850 (APEX 9.8), CVE-2026-114856 (ORDS General 9.6, user interaction), all HTTPS; APEX supported 24.1.22, 24.2.21, 26.1.5, 26.2.0; ORDS 24.2.0-26.3.0. Oracle credits several researchers "working with Trend Micro's Zero Day Initiative" for -114849 and -114850 (whether ZDI will publish a technical advisory is an assessment from general practice, not from a source fetched here; no ZDI advisory found yet).
7. **PeopleSoft PeopleTools 8.61-8.63**: CVE-2026-111497 (Node.js/OpenSearch Dashboards, 9.8, KEV via Brotli), CVE-2026-114934 Integration Broker 9.3 scope change, CVE-2026-114862 Weblogic 9.1.
8. Lower on the list: Hyperion (11 unauthenticated rows, all 11.2.26.0.000, mostly HTTP/RMI; typically internal finance, assessment); Supply Chain/AutoVue (4 rows at 9.8, version 21.1.0, niche) and Agile PLM Tomcat HTTP/2 9.1; MySQL Shell (Python) 9.8 and MySQL Server/Cluster "Client programs" 9.1 over the MySQL protocol; Enterprise Manager Agent Next Gen (Eclipse Jetty) 9.1; Autonomous Health Framework 9.1; Communications (telecom estates: DSR, Unified Assurance, Element Manager, UIM); Service Delivery Platform SOAP 9.8; Managed File Transfer (Bouncy Castle) 9.1; ADF Security Framework 9.1.
9. Not in the >= 9.0 set although often asked about: Oracle HTTP Server (only CVE-2026-9545, WebLogic Server Proxy Plug-in (curl), 7.5); Java SE (max 8.1); Database Server unauthenticated rows (max 7.5).

### 1.9 Contradictions with, and unsupported statements in, the first pass (item 6)

- CONFIRMED: 655 patches; 62 rows >= 9.0 / 57 CVEs; 56 unauthenticated rows / 51 CVEs; family counts (Hyperion 107, Fusion Middleware 53, Supply Chain 36, Communications 21, EBS 19, Analytics 9, Siebel 9, PeopleSoft 6, ORDS 5, MySQL 3, Database 3, Enterprise Manager 3, Virtualization 3, Java SE 11, APEX 2); EBS 19 (not 22); Database 9.9 rows need Create Session; the three Brotli rows; Java SE matrix includes CVE-2026-114938 at 8.1.
- NOT SUPPORTED AS WORDED: "655 new security patches across 21 product families" attributes "21" to the advisory. Oracle writes "across the product families listed below" and never counts them; 21 is Tenable's count (and equals the number of risk-matrix sections). "640 CVEs" is likewise Tenable's figure (reproduced here from the rows), not an Oracle statement.
- NOT SUPPORTED AS WORDED: the headline lumps "WebLogic T3/IIOP and TopLink ... at 10.0". Only the TopLink Integration row CVE-2026-91569 is 10.0; the T3/IIOP row CVE-2026-91470 is 9.8. The six 10.0 rows are CVE-2026-114835, -91500, -91510 (Access Manager), -114824 (Platform Security for Java), -91569 (WebLogic TopLink), -114784 (BI EE).
- "none flagged exploited or publicly disclosed by Oracle": supported only in the sense that the page contains no such flag at all (Oracle's matrices have no exploited/disclosed column). The page does not say "not exploited"; it carries the generic warning quoted in 1.7.
- The first pass lists the unauthenticated >= 9.0 rows by family but omits Commerce (6 unauthenticated rows, none >= 9.0), Construction and Engineering (2, none >= 9.0), Application Testing Suite (1) and Financial Services (1); none of these has a row >= 9.0, so nothing material is lost.
- Not in the first pass: the "also addresses CVE-2025-61882" footnote (1.7) and the EUVD/NCSC/BSI absence checks.

### 1.10 Open gaps (Oracle)

- Pre-release page text (652 patches; EBS 22; DB/APEX 9.9 unauthenticated) not re-readable; only `state/coverage_backlog.md` records it.
- Oracle publishes no per-CVE exploit prerequisites, default-configuration statements or patch-number mapping on the page itself (patch numbers sit in My Oracle Support notes CPU433, CPU454, KA923, KA1182, which need a login).
- No third-party exploit or write-up found for any >= 9.0 row except the Java row; check again at the next fire, especially ZDI advisories for CVE-2026-114849/-114850/-114822/-114848 and any Calif/depthfirst/starfishsec posts.


## 2. MITEL MiCollab MISA-2026-0012

Primary: https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012 (read with `extract`, `trafilatura-direct`, fetched 2026-11-18 ~04:43Z; raw HTML also saved `mitel/misa-2026-0012.raw.html`). Page metadata date 2026-11-16.

### 2.1 Advisory facts

| claim | source URL | verbatim passage | saved body |
|---|---|---|---|
| Advisory id and dates (first issue = last update = 2026-11-16, revision 1.0) | https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012 | "First Issue Date: 2026-11-16" | `mitel/misa-2026-0012.extract.md` |
| Last updated | https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012 | "Last Updated: 2026-11-16" | `mitel/misa-2026-0012.extract.md` |
| Revision | https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012 | "Revision: 1.0" | `mitel/misa-2026-0012.extract.md` |
| Revision history shows only the initial version (no later revision at fetch time) | https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012 | "\| 1.0 \| 2026-11-16 \| Initial version \|" | `mitel/misa-2026-0012.extract.md` |
| Affected versions (single row; no other branch named) | https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012 | "10.3 (10.3.0.18) and earlier" | `mitel/misa-2026-0012.extract.md` |
| Fix: patch for 10.3 (10.3.0.18) PLUS upgrade; "or upgrade to a later release" (no later release number is named) | https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012 | "Mitel provided a patch available for release 10.3 (10.3.0.18) that addresses these vulnerabilities. Upgrade to this release and apply the provided patch, or upgrade to a later release." | `mitel/misa-2026-0012.extract.md` |
| Patch KB (title lists all five ids) | https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012 | "MiCollab Security Update, MTLVULN-1861, MTLVULN-1862, MTLVULN-1863, MTLVULN-1864, MTLVULN-1877" | `mitel/misa-2026-0012.extract.md` |
| KB id | https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012 | "KB000129195" | `mitel/misa-2026-0012.extract.md` |
| KB is behind the customer portal; partners can help | https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012 | "If you do not have access to this link, please contact your Mitel Authorized Partner for support." | `mitel/misa-2026-0012.extract.md` |
| Fix will also ship in later releases (future tense; no release named) | https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012 | "The security update will be included in later MiCollab releases." | `mitel/misa-2026-0012.extract.md` |
| Scope limiter: only supported versions assessed; End-of-Support products not considered | https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012 | "Product statements are related only to supported product versions. Products that have reached End of Support status are not considered." | `mitel/misa-2026-0012.extract.md` |
| Mitigation (verbatim; AWV component; patch is the recommended action, mitigation is the fallback) | https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012 | "For customers who are not currently able to implement the recommended solution in a timely manner, the risk may be mitigated by restricting external access to the AWV component. For further details, please refer to the security Knowledge Base article." | `mitel/misa-2026-0012.extract.md` |
| Chaining statement | https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012 | "Exploiting these vulnerabilities together can significantly amplify their impact." | `mitel/misa-2026-0012.extract.md` |
| CVE status | https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012 | "Note: The above issue is referenced here by our internal tracking ID. A CVE identifier has been requested but is not yet assigned" | `mitel/misa-2026-0012.extract.md` |
| Summary severity line | https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012 | "The identified vulnerabilities carry varied levels of severity including critical" | `mitel/misa-2026-0012.extract.md` |

### 2.2 Each MTLVULN row (CVSS 3.1 vector as published by Mitel; no CVE ids)

| claim | source URL | verbatim passage | saved body |
|---|---|---|---|
| MTLVULN-1861 Medium 5.3: arbitrary file upload, unauthenticated, weak file-type validation | https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012 | "\| MiCollab \| MTLVULN-1861 \| Medium / 5.3 \| AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N \|" | `mitel/misa-2026-0012.extract.md` |
| MTLVULN-1862 Critical 9.0: XML injection, AC:H, scope changed | https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012 | "\| MiCollab \| MTLVULN-1862 \| Critical / 9.0 \| AV:N/AC:H/PR:N/UI:N/S:C/C:H/I:H/A:H \|" | `mitel/misa-2026-0012.extract.md` |
| MTLVULN-1863 Medium 5.9: unauthorized access, AC:H, confidentiality only | https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012 | "\| MiCollab \| MTLVULN-1863 \| Medium / 5.9 \| AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N \|" | `mitel/misa-2026-0012.extract.md` |
| MTLVULN-1864 Critical 10.0: blind command injection, scope changed, C:N I:H A:H | https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012 | "\| MiCollab \| MTLVULN-1864 \| Critical / 10.0 \| AV:N/AC:L/PR:N/UI:N/S:C/C:N/I:H/A:H \|" | `mitel/misa-2026-0012.extract.md` |
| MTLVULN-1877 Medium 5.3: authentication bypass | https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012 | "\| MiCollab \| MTLVULN-1877 \| Medium / 5.3 \| AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N \|" | `mitel/misa-2026-0012.extract.md` |
| MTLVULN-1861 text (component AWV; file upload) | https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012 | "could allow an unauthenticated attacker to conduct an arbitrary file upload attack due to insufficient file type validation." | `mitel/misa-2026-0012.extract.md` |
| MTLVULN-1861 impact | https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012 | "A successful exploit of this vulnerability could allow an attacker to upload arbitrary files to the target system." | `mitel/misa-2026-0012.extract.md` |
| MTLVULN-1862 text: "pre-staged malicious content" is a stated precondition | https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012 | "could allow an unauthenticated attacker to leverage pre-staged malicious content to conduct an XML injection attack due to insufficient parameter validation." | `mitel/misa-2026-0012.extract.md` |
| MTLVULN-1862 impact (arbitrary commands; C, I and A) | https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012 | "A successful exploit of this vulnerability could allow an attacker to execute arbitrary commands within the context of the system, with potential impacts on the confidentiality, integrity and availability of the system." | `mitel/misa-2026-0012.extract.md` |
| MTLVULN-1863 text: needs knowledge of a system-generated random identifier or pre-staged content | https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012 | "with knowledge of a specific system-generated random identifier or pre-staged content, to conduct an unauthorized access attack due to improper authentication mechanisms." | `mitel/misa-2026-0012.extract.md` |
| MTLVULN-1863 limiter: does not give access to arbitrary files elsewhere | https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012 | "The vulnerability is limited to the affected functionality and does not provide unrestricted access to arbitrary files elsewhere on the system." | `mitel/misa-2026-0012.extract.md` |
| MTLVULN-1864 text: blind command injection, unauthenticated; NOTE the sentence that follows is garbled in the original ("requires could allow") and may have lost a stated precondition | https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012 | "could allow an unauthenticated attacker to conduct a blind command injection attack due to insufficient parameter sanitization. A successful exploit of this vulnerability requires could allow an attacker to execute arbitrary commands within the context of the system, with potential impacts to the integrity, and availability of the system." | `mitel/misa-2026-0012.extract.md` |
| MTLVULN-1877 text | https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012 | "could allow an unauthenticated attacker to conduct an authentication bypass attack due to improper handling of authentication." | `mitel/misa-2026-0012.extract.md` |
| MTLVULN-1877 impact | https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012 | "A successful exploit of this vulnerability could allow an attacker to bypass authentication controls and perform unauthorized actions within the context of the application." | `mitel/misa-2026-0012.extract.md` |

### 2.3 Exploitation statement

The advisory contains NO statement either way about exploitation or public exploits: every occurrence of "exploit" on the page (6 lines, listed by `grep -n -i exploit mitel/misa-2026-0012.extract.md`) is conditional ("if successfully exploited") or the chaining sentence above. The first pass wrote "No exploitation or public PoC is stated in the advisory" - that is accurate as an absence, and must not be rendered as "Mitel says it is not exploited".

### 2.4 CVE assignment since publication (checked 2026-11-18)

| claim | source URL | verbatim passage | saved body |
|---|---|---|---|
| Mitel page still says CVE requested, not assigned | https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012 | "A CVE identifier has been requested but is not yet assigned" | `mitel/misa-2026-0012.extract.md` |
| ENISA EUVD search text=micollab, 2026-11-10..2026-11-18: zero records | https://euvdservices.enisa.europa.eu/api/search?text=micollab&fromDate=2026-11-10&toDate=2026-11-18&page=0&size=50 | "{"items":[],"total":0}" | `mitel/euvd-micollab.json` |
| ENISA EUVD search text=mitel, same window: zero records | https://euvdservices.enisa.europa.eu/api/search?text=mitel&fromDate=2026-11-10&toDate=2026-11-18&page=0&size=50 | "{"items":[],"total":0}" | `mitel/euvd-mitel.json` |
| NVD CVE API keywordSearch=MiCollab, published 2026-11-10..2026-11-18: zero results | https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch=MiCollab&pubStartDate=2026-11-10T00:00:00.000&pubEndDate=2026-11-18T23:59:59.000 | ""totalResults":0" | `mitel/nvd-micollab.json` |
| BSI CSAF lists five vulnerability objects with no CVE id (release date only) | https://wid.cert-bund.de/.well-known/csaf/white/2026/wid-sec-w-2026-4608.json | ""release_date": "2026-11-16T23:00:00.000+00:00"" | `mitel/wid-sec-2026-4608.csaf.json` |

### 2.5 Third-party authorities (none states exploitation)

| claim | source URL | verbatim passage | saved body |
|---|---|---|---|
| CERT-FR lists the advisory the next day (CERTFR-2026-AVI-1547; initial version 17 November 2026) | https://www.cert.cyber.gouv.fr/avis/CERTFR-2026-AVI-1547/ | "17 novembre 2026 Version initiale" | `mitel/certfr-avi-1547.rawtext.txt` |
| CERT-FR affected range: "before 10.3.0.18" - differs from Mitel ("10.3 (10.3.0.18) and earlier") | https://www.cert.cyber.gouv.fr/avis/CERTFR-2026-AVI-1547/ | "- MiCollab versions antérieures à 10.3.0.18" | `mitel/certfr-avi-1547.extract.md` |
| CERT-FR risk summary: some of them allow remote code execution, remote denial of service and loss of confidentiality (CERT-FR's wording, not Mitel's) | https://www.cert.cyber.gouv.fr/avis/CERTFR-2026-AVI-1547/ | "Certaines d'entre elles permettent à un attaquant de provoquer une exécution de code arbitraire à distance, un déni de service à distance et une atteinte à la confidentialité des données." | `mitel/certfr-avi-1547.extract.md` |
| CERT-FR points to Mitel bulletin 2026-0012 of 16 November 2026 | https://www.cert.cyber.gouv.fr/avis/CERTFR-2026-AVI-1547/ | "Bulletin de sécurité Mitel 2026-0012 du 16 novembre 2026" | `mitel/certfr-avi-1547.extract.md` |
| BSI WID-SEC-2026-4608 (hoch, initial 2026-11-16T23:00Z, generated 2026-11-17 11:57Z): remote anonymous attacker; manipulate files, run code with service rights, bypass security, disclose information | https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-4608 | "Ein entfernter, anonymer Angreifer kann mehrere Schwachstellen in Mitel MiCollab ausnutzen, um Dateien zu manipulieren, beliebigen Programmcode mit den Rechten des Dienstes auszuführen, Sicherheitsmaßnahmen zu umgehen, Informationen offenzulegen, oder nicht spezifizierte Angriffe durchzuführen." | `mitel/wid-sec-2026-4608.decoded.txt` |
| BSI product tree: affected "<10.3.0.18", fixed 10.3.0.18 (again differs from Mitel) | https://wid.cert-bund.de/.well-known/csaf/white/2026/wid-sec-w-2026-4608.json | ""name": "<10.3.0.18"" | `mitel/wid-sec-2026-4608.csaf.json` |
| BSI severity | https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-4608 | "aggregate_severity: hoch" | `mitel/wid-sec-2026-4608.decoded.txt` |

### 2.6 Version table

| source | affected | fixed / action |
|---|---|---|
| Mitel MISA-2026-0012 | MiCollab 10.3 (10.3.0.18) and earlier (supported versions only) | patch from KB000129195 on release 10.3 (10.3.0.18), or a later release; no later release number named |
| CERT-FR AVI-1547 (17 Nov) | versions before 10.3.0.18 | see vendor bulletin |
| BSI WID-SEC-2026-4608 (CSAF product tree) | < 10.3.0.18 | 10.3.0.18 listed as fixed |
| Mitel MISA-2026-0006 (2026-07-22, prior entry `2026-07-24/mitel-micollab-awv-unauth-command-injection`) | 10.0 (10.0.0.26) to 10.2 SP1 FP2 (10.2.1.205) and 9.8 SP3 FP2 (9.8.3.203) and earlier | "Upgrade to version 10.3 (10.3.0.18) or subsequent releases"; patches for 10.2 SP1 FP2 and 9.8 SP3 FP2 (KB000128275) |

| claim | source URL | verbatim passage | saved body |
|---|---|---|---|
| Prior advisory MISA-2026-0006 fixed MTLVULN-1694 (9.8) in 10.3 (10.3.0.18) | https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0006 | "This issue is addressed in MiCollab version 10.3 (10.3.0.18)." | `mitel/misa-2026-0006.extract.md` |
| Prior advisory affected range for 0006 | https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0006 | "10.0 (10.0.0.26) to 10.2 SP1 FP2 (10.2.1.205) and 9.8 SP3 FP2 (9.8.3.203) and earlier" | `mitel/misa-2026-0006.extract.md` |
| Prior row MTLVULN-1694 Critical / 9.8 | https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0006 | "\| MiCollab \| MTLVULN-1694 \| Critical / 9.8 \| AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H \|" | `mitel/misa-2026-0006.extract.md` |

Consequence stated by the two Mitel pages together (inference, labelled): a site that moved to 10.3.0.18 after MISA-2026-0006 in July is within "10.3 (10.3.0.18) and earlier" of MISA-2026-0012 and still needs the new patch. Mitel does not say this in words.

### 2.7 Contradictions with the first pass (item 7) and open gaps

- CONFIRMED: affected 10.3 (10.3.0.18) and earlier; each MTLVULN row and score (1864 10.0, 1862 9.0, 1863 5.9, 1861 5.3, 1877 5.3); KB000129195; mitigation sentence; no CVE ids yet; no exploitation statement in the advisory; CERT-FR AVI-1547 on 2026-11-17 and BSI WID-SEC-2026-4608.
- First pass says CERT-FR words the range as "before 10.3.0.18"; confirmed. Not in the first pass: BSI's own product tree also says "<10.3.0.18" with 10.3.0.18 fixed, i.e. both CERTs differ from Mitel.
- First pass summary calls MTLVULN-1862 "XML injection that lets an unauthenticated attacker leverage pre-staged malicious content to execute commands": consistent with the page, but the page states the XML injection "could allow an attacker to execute arbitrary commands" (a possibility), so keep "could".
- First pass cites BSI as "describes ... bypass security measures": confirmed (BSI line above). BSI lists "Windows, Linux, MacOS X, UNIX" as OS (BSI boilerplate, not Mitel).
- NEW: the MTLVULN-1864 impact sentence is garbled in the original ("requires could allow"); a precondition may have been deleted. Mitel's vector still scores it PR:N/UI:N/AC:L.
- OPEN: "and earlier" is not mapped to branches: the page names only 10.3 and gives no patch for 10.2 or 9.8 branches, although MISA-2026-0006 had patches for 10.2 SP1 FP2 and 9.8 SP3 FP2. Whether those branches are affected, fixed or simply unsupported is not stated. The KB (portal login) probably says; it could not be read.
- OPEN: no later release number is named although the page says "or upgrade to a later release" and "will be included in later MiCollab releases".
- OPEN: Mitel's own security-advisory index was not separately checked for a revision after 2026-11-16 (the advisory page itself shows revision 1.0 only). No CERT or vendor states exploitation as of 2026-11-18 ~04:45Z.


## 3. AGENT-FRAMEWORK PYPI COMPROMISE (2026-11-17)

Sources read in full with `extract` (all `trafilatura-direct`, fetched 2026-11-18 ~04:50-05:05Z): Socket (https://socket.dev/blog/agent-framework-pypi-package-compromised-with-credential-stealer), SafeDep (https://safedep.io/blog/microsoft-agent-framework-pypi-compromise; its Timeline block is a script-rendered component that `extract` drops, so it was recovered from the raw HTML into `agentfw/safedep.timeline.txt`), and three further independent detectors found by WebSearch: Wiz (https://www.wiz.io/blog/malicious-version-of-microsofts-agent-framework-published-to-pypi), StepSecurity (https://www.stepsecurity.io/blog/microsoft-agent-framework-pypi-package-compromised), Aikido (https://www.aikido.dev/blog/two-malicious-agent-framework-releases-hit-pypi-in-33-minutes), plus OpenSourceMalware (https://opensourcemalware.com/blog/agent-framework-pypi-compromised). PyPI state read from the PyPI JSON API (https://pypi.org/pypi/agent-framework/json). No Microsoft or PyPI statement could be found or read (see 3.8). All IOC material (hashes, endpoint) is deliberately omitted here.

### 3.1 Affected versions, timeline, state on PyPI

| claim | source URL | verbatim passage | saved body |
|---|---|---|---|
| Socket: compromised on 17 Nov, versions 1.26.1 and 1.26.2 | https://socket.dev/blog/agent-framework-pypi-package-compromised-with-credential-stealer | "PyPI package was compromised on November 17th, affecting versions 1.26.1 and 1.26.2." | `agentfw/socket.extract.md` |
| SafeDep: official Microsoft metapackage; any environment that installs them | https://safedep.io/blog/microsoft-agent-framework-pypi-compromise | "steal credentials from any environment that installs them." | `agentfw/safedep.extract.md` |
| SafeDep: last clean release is 1.26.0 | https://safedep.io/blog/microsoft-agent-framework-pypi-compromise | "The last clean release is 1.26.0." | `agentfw/safedep.extract.md` |
| SafeDep affected-versions table: 1.26.1 wheel only, malicious, removed | https://safedep.io/blog/microsoft-agent-framework-pypi-compromise | "wheel only, 10,402 bytes" | `agentfw/safedep.extract.md` |
| SafeDep: status wording | https://safedep.io/blog/microsoft-agent-framework-pypi-compromise | "Malicious, removed from PyPI" | `agentfw/safedep.extract.md` |
| SafeDep: 1.26.0 is last clean | https://safedep.io/blog/microsoft-agent-framework-pypi-compromise | "Last clean release" | `agentfw/safedep.extract.md` |
| SafeDep timeline (UTC): 1.26.1 published 20:35; flagged 20:57 | https://safedep.io/blog/microsoft-agent-framework-pypi-compromise | "20:35 \| agent-framework 1.26.1 published \| Malicious \| A single wheel, where every earlier release shipped a wheel and an sdist. \| 20:57 \| SafeDep flags 1.26.1" | `agentfw/safedep.timeline.txt` |
| SafeDep timeline: 1.26.2 published 21:08 (1.26.1 already gone); flagged 21:12; 1.26.2 removed after 21:12 | https://safedep.io/blog/microsoft-agent-framework-pypi-compromise | "21:08 \| agent-framework 1.26.2 published \| Malicious \| 1.26.1 is gone from PyPI." | `agentfw/safedep.timeline.txt` |
| SafeDep timeline: flagged 21:12 | https://safedep.io/blog/microsoft-agent-framework-pypi-compromise | "21:12 \| SafeDep flags 1.26.2" | `agentfw/safedep.timeline.txt` |
| SafeDep timeline: removal | https://safedep.io/blog/microsoft-agent-framework-pypi-compromise | "After 21:12 \| 1.26.2 removed from PyPI \| Removed \| 1.26.0 is again the newest version on PyPI." | `agentfw/safedep.timeline.txt` |
| SafeDep: detection latency | https://safedep.io/blog/microsoft-agent-framework-pypi-compromise | "SafeDep flagged version 1.26.1 22 minutes after it was published on 17 November 2026." | `agentfw/safedep.extract.md` |
| SafeDep: second release | https://safedep.io/blog/microsoft-agent-framework-pypi-compromise | "Once 1.26.1 came off PyPI, 1.26.2 shipped the same stealer under different file names, and SafeDep flagged it 4 minutes after upload." | `agentfw/safedep.extract.md` |
| StepSecurity: upload and PyPI quarantine times (UTC) for both versions | https://www.stepsecurity.io/blog/microsoft-agent-framework-pypi-package-compromised | "Version 1.26.1 was uploaded at 20:35:20 UTC on November 17 and quarantined at 21:06:16 UTC. Version 1.26.2 followed at 21:08:39 UTC, just 2 minutes 23 seconds after the first quarantine, and was quarantined at 21:16:44 UTC." | `agentfw/stepsecurity.extract.md` |
| StepSecurity: PyPI quarantined both releases; attacker still able to publish after the first quarantine | https://www.stepsecurity.io/blog/microsoft-agent-framework-pypi-package-compromised | "PyPI has quarantined both releases, but the attacker demonstrated continued publishing access by uploading 1.26.2 after 1.26.1 was already quarantined." | `agentfw/stepsecurity.extract.md` |
| StepSecurity: whether access persists is not established | https://www.stepsecurity.io/blog/microsoft-agent-framework-pypi-package-compromised | "It does not establish whether that access remains available now." | `agentfw/stepsecurity.extract.md` |
| Wiz: both unavailable as of 21:30 UTC; 1.26.0 most recent safe | https://www.wiz.io/blog/malicious-version-of-microsofts-agent-framework-published-to-pypi | "As of 21:30 UTC, both versions were no longer available on PyPI." | `agentfw/wiz.extract.md` |
| Wiz: safe version | https://www.wiz.io/blog/malicious-version-of-microsofts-agent-framework-published-to-pypi | "The most recent safe version is 1.26.0." | `agentfw/wiz.extract.md` |
| Wiz: legitimate 1.26.0 published 2026-11-12 18:25 | https://www.wiz.io/blog/malicious-version-of-microsofts-agent-framework-published-to-pypi | "\| 2026-11-12 18:25 \| Legitimate 1.26.0 published (wheel + sdist, alongside agent-framework-core 1.26.0) \|" | `agentfw/wiz.extract.md` |
| Aikido: exposure window for an unpinned install | https://www.aikido.dev/blog/two-malicious-agent-framework-releases-hit-pypi-in-33-minutes | "between 20:35 UTC and roughly 21:20 UTC on Nov 17, 2026" | `agentfw/aikido.extract.md` |
| Aikido: both removed | https://www.aikido.dev/blog/two-malicious-agent-framework-releases-hit-pypi-in-33-minutes | "Both have been removed from PyPI." | `agentfw/aikido.extract.md` |
| OpenSourceMalware: says PyPI quarantined "the Microsoft publisher" (differs from StepSecurity: releases) | https://opensourcemalware.com/blog/agent-framework-pypi-compromised | "PyPI quarantined the Microsoft publisher because unauthorized publishing access is believed to remain active" | `agentfw/osm.extract.md` |
| Own check, PyPI JSON API 2026-11-18: latest = 1.26.0; 1.26.1 and 1.26.2 absent from the release list (not merely yanked) | https://pypi.org/pypi/agent-framework/json | "releases 1.26.1 present: False ; 1.26.2 present: False" | `agentfw/pypi-releases.txt` |
| Own check: latest version on PyPI | https://pypi.org/pypi/agent-framework/json | "PROJECT agent-framework \| info.version (latest): 1.26.0" | `agentfw/pypi-releases.txt` |
| Own check: metapackage 1.26.0 depends on agent-framework-core[all]==1.26.0; core and foundry show no upload after 2026-11-12 (siblings looked at: core, foundry) | https://pypi.org/pypi/agent-framework/json | "requires_dist: ['agent-framework-core[all]==1.26.0']" | `agentfw/pypi-releases.txt` |

Version table: clean up to and including **1.26.0** (published 2026-11-12 18:25 UTC, wheel + sdist); malicious **1.26.1** (published 2026-11-17 20:35:20 UTC, quarantined 21:06:16 per StepSecurity, wheel only 10,402 bytes) and **1.26.2** (published 21:08:39 UTC, quarantined 21:16:44 per StepSecurity, wheel only 10,449 bytes). Download volume: SafeDep "about 192,000 downloads a month", Aikido "about 190,000 downloads a month", Wiz "about 41,000 downloads a week"; nobody knows how many installs the two bad versions received (SafeDep, OpenSourceMalware).

| claim | source URL | verbatim passage | saved body |
|---|---|---|---|
| Package size / install count unknown (SafeDep) | https://safedep.io/blog/microsoft-agent-framework-pypi-compromise | "and gets about 192,000 downloads a month. How many installs the two bad versions got is not known yet." | `agentfw/safedep.extract.md` |
| Wiz download figure | https://www.wiz.io/blog/malicious-version-of-microsofts-agent-framework-published-to-pypi | "The package gets about 41,000 downloads a week." | `agentfw/wiz.extract.md` |
| OpenSourceMalware: demand statistics are not victim counts | https://opensourcemalware.com/blog/agent-framework-pypi-compromised | "Public download statistics for agent-framework show demand for the project as a whole, but they don't say how many times 1.26.1 or 1.26.2 were installed." | `agentfw/osm.extract.md` |

### 3.2 Mechanism: the .pth startup hook (behaviour only)

| claim | source URL | verbatim passage | saved body |
|---|---|---|---|
| Socket: on interpreter start the .pth line imports a module that launches collection in the background | https://socket.dev/blog/agent-framework-pypi-package-compromised-with-credential-stealer | "imports a module that launches collection in a background process/thread." | `agentfw/socket.extract.md` |
| SafeDep: nothing has to import the package (a pip install in CI suffices) | https://safedep.io/blog/microsoft-agent-framework-pypi-compromise | "Nothing has to import the package." | `agentfw/safedep.extract.md` |
| SafeDep: the host process returns at once; no visible delay | https://safedep.io/blog/microsoft-agent-framework-pypi-compromise | "The host process returns at once, so a test run or build shows no delay." | `agentfw/safedep.extract.md` |
| Socket: no persistent on-disk execution marker; fresh process trees re-trigger collection | https://socket.dev/blog/agent-framework-pypi-package-compromised-with-credential-stealer | "Fresh process trees can trigger collection again; there is no persistent on-disk execution marker." | `agentfw/socket.extract.md` |
| Wiz: runs on every interpreter start, import not needed | https://www.wiz.io/blog/malicious-version-of-microsofts-agent-framework-published-to-pypi | "Python runs `.pth` files on every interpreter start, so the credential stealer runs whenever Python starts in that environment, even if `agent-framework` is never imported." | `agentfw/wiz.extract.md` |
| StepSecurity: a detached collector child can outlive its parent; removing the package does not stop it | https://www.stepsecurity.io/blog/microsoft-agent-framework-pypi-package-compromised | "The child can outlive its parent interpreter; survival beyond the job depends on runner cleanup and container or VM teardown." | `agentfw/stepsecurity.extract.md` |
| StepSecurity: scope of the hook depends on which site-packages the interpreter processes | https://www.stepsecurity.io/blog/microsoft-agent-framework-pypi-package-compromised | "This does not automatically affect every virtual environment sharing a base interpreter" | `agentfw/stepsecurity.extract.md` |
| StepSecurity: non-Python steps do not trigger it | https://www.stepsecurity.io/blog/microsoft-agent-framework-pypi-package-compromised | "Non-Python steps do not themselves trigger the hook, although a previously started collector may still be running." | `agentfw/stepsecurity.extract.md` |
| Wiz/StepSecurity/Socket agree no second stage | https://www.stepsecurity.io/blog/microsoft-agent-framework-pypi-package-compromised | "The inspected payloads contain no remote-code-loading second stage." | `agentfw/stepsecurity.extract.md` |
| Socket: same | https://socket.dev/blog/agent-framework-pypi-package-compromised-with-credential-stealer | "The reported payloads do not download or execute additional code." | `agentfw/socket.extract.md` |
| 1.26.1 vs 1.26.2: 1.26.2 restores the clean package initializer, so checking only that file misses it | https://socket.dev/blog/agent-framework-pypi-package-compromised-with-credential-stealer | "The legitimate package initializer is restored byte-for-byte" | `agentfw/socket.extract.md` |
| Wiz: a check on 1.26.1 file names misses 1.26.2 | https://www.wiz.io/blog/malicious-version-of-microsofts-agent-framework-published-to-pypi | "Searching only for the 1.26.1 file names will miss this version." | `agentfw/wiz.extract.md` |
| SafeDep: same point | https://safedep.io/blog/microsoft-agent-framework-pypi-compromise | "A check for 1.26.1’s file names or hashes misses 1.26.2." | `agentfw/safedep.extract.md` |

Behaviour summary for the composer (all from the sources above): 1.26.1 ships a one-line startup file in site-packages plus a module appended to the package initializer; 1.26.2 ships a different startup file plus a new top-level module and leaves the initializer clean. The collector sets a run-once environment marker so child interpreters skip it, forks and detaches on Unix (daemon thread elsewhere), swallows all errors, and makes one HTTPS POST to a public request-capture service (webhook.site) carrying a compressed, base64-encoded JSON document. Both Socket and StepSecurity say it is not encryption.

### 3.3 What it collects and the tokens it requests

| claim | source URL | verbatim passage | saved body |
|---|---|---|---|
| Socket: environment secrets by substring match, not an allowlist | https://socket.dev/blog/agent-framework-pypi-package-compromised-with-credential-stealer | "substring-based matching, not a fixed variable allowlist" | `agentfw/socket.extract.md` |
| SafeDep (1.26.1 description): env vars matching 31 substrings, each value capped at 8,000 characters | https://safedep.io/blog/microsoft-agent-framework-pypi-compromise | "whose names contain any of 31 substrings, including" | `agentfw/safedep.extract.md` |
| SafeDep: credential files up to 60, each under 256 KB (Azure CLI JSON, pip.conf, .npmrc, .netrc, git credentials, Docker config, Hugging Face token, Azure AI Foundry, Azure DevOps agent .credentials) | https://safedep.io/blog/microsoft-agent-framework-pypi-compromise | "up to 60 under 256 KB each." | `agentfw/safedep.extract.md` |
| SafeDep: other processes' environments, up to 300 /proc/PID/environ files; reaches other jobs on shared runners | https://safedep.io/blog/microsoft-agent-framework-pypi-compromise | "On a shared or self-hosted runner, that reaches secrets belonging to other jobs." | `agentfw/safedep.extract.md` |
| SafeDep: it also records host context | https://safedep.io/blog/microsoft-agent-framework-pypi-compromise | "It also records the hostname, user, working directory and" | `agentfw/safedep.extract.md` |
| Socket: it requests fresh tokens, not only copies existing secrets | https://socket.dev/blog/agent-framework-pypi-package-compromised-with-credential-stealer | "They actively request fresh Azure managed-identity and CI federation tokens rather than merely copying existing secrets." | `agentfw/socket.extract.md` |
| SafeDep: rotating stored secrets does not cover newly issued tokens | https://safedep.io/blog/microsoft-agent-framework-pypi-compromise | "Rotating stored secrets does not cover those." | `agentfw/safedep.extract.md` |
| Wiz: Azure managed-identity tokens for 12 resources from IMDS or the App Service identity endpoint | https://www.wiz.io/blog/malicious-version-of-microsofts-agent-framework-published-to-pypi | "**Azure managed-identity tokens** from IMDS or the App Service identity endpoint for 12 resources: ARM, Graph, Key Vault, Storage, Cognitive Services, Azure AI/ML, Search, Container Registry, Azure DevOps, and AzureADTokenExchange" | `agentfw/wiz.extract.md` |
| Wiz: Azure DevOps OIDC token via SYSTEM_ACCESSTOKEN and SYSTEM_OIDCREQUESTURI for api://AzureADTokenExchange | https://www.wiz.io/blog/malicious-version-of-microsofts-agent-framework-published-to-pypi | "**Azure DevOps OIDC tokens**: if `SYSTEM_ACCESSTOKEN` and `SYSTEM_OIDCREQUESTURI` are set, it requests an OIDC token for `api://AzureADTokenExchange`" | `agentfw/wiz.extract.md` |
| StepSecurity: Azure DevOps OIDC and managed-identity requests in BOTH versions; GitHub Actions OIDC in 1.26.2 only | https://www.stepsecurity.io/blog/microsoft-agent-framework-pypi-package-compromised | "- **GitHub Actions OIDC** (1.26.2 only): uses `ACTIONS_ID_TOKEN_REQUEST_URL` and `ACTIONS_ID_TOKEN_REQUEST_TOKEN` (or the runtime token) to request JWTs for the audiences `api://AzureADTokenExchange` and `https://management.azure.com/`." | `agentfw/stepsecurity.extract.md` |
| StepSecurity: GitHub OIDC issuance needs the job permission; Azure exchange needs a federated trust; payload only collects the response | https://www.stepsecurity.io/blog/microsoft-agent-framework-pypi-package-compromised | "GitHub OIDC issuance requires the relevant job permission, normally `id-token: write`." | `agentfw/stepsecurity.extract.md` |
| StepSecurity: the payload does not itself perform the Azure exchange; static analysis shows attempts not successes | https://www.stepsecurity.io/blog/microsoft-agent-framework-pypi-package-compromised | "static analysis establishes the attempts, not successful issuance or subsequent cloud access" | `agentfw/stepsecurity.extract.md` |
| Wiz: where an Entra federated credential trusts the workflow, the OIDC tokens can be exchanged for Azure access | https://www.wiz.io/blog/malicious-version-of-microsofts-agent-framework-published-to-pypi | "Where an Entra ID federated credential trusts the workflow, these tokens can be exchanged for Azure access, with no stored secret needed." | `agentfw/wiz.extract.md` |
| Wiz: stolen managed-identity / exchanged tokens valid up to 24 hours (Wiz claim) | https://www.wiz.io/blog/malicious-version-of-microsofts-agent-framework-published-to-pypi | "Stolen managed-identity and OIDC-exchanged tokens are valid for up to 24 hours." | `agentfw/wiz.extract.md` |
| Aikido: Azure DevOps OIDC request lacks a serviceConnectionId so the exchange step may fail depending on the pipeline | https://www.aikido.dev/blog/two-malicious-agent-framework-releases-hit-pypi-in-33-minutes | "The request here doesn't pass a `serviceConnectionId`, so this step may fail depending on the pipeline" | `agentfw/aikido.extract.md` |

Version differences (a real inconsistency across sources): SafeDep says "The rest of the collector is unchanged" for 1.26.2 and gives 31 substrings / 60 files without a version split; StepSecurity says 35 substrings and up to 80 files for 1.26.2 (31 and 60 for 1.26.1); Wiz says 1.26.2 raised the file cap from 60 to 80 and added GitHub-hosted runner paths; Socket lists the 1.26.2 additions (ACTIONS, OIDC, RUNNER, ARM_).

| claim | source URL | verbatim passage | saved body |
|---|---|---|---|
| SafeDep: rest of collector unchanged in 1.26.2 | https://safedep.io/blog/microsoft-agent-framework-pypi-compromise | "The rest of the collector is unchanged." | `agentfw/safedep.extract.md` |
| StepSecurity: 35 substrings in 1.26.2, 31 in 1.26.1 | https://www.stepsecurity.io/blog/microsoft-agent-framework-pypi-package-compromised | "any variable whose name contains one of 35 substrings in 1.26.2 (31 in 1.26.1)" | `agentfw/stepsecurity.extract.md` |
| StepSecurity: up to 80 files in 1.26.2, 60 in 1.26.1 | https://www.stepsecurity.io/blog/microsoft-agent-framework-pypi-package-compromised | "up to 80 files (60 in 1.26.1)" | `agentfw/stepsecurity.extract.md` |
| Wiz: file cap 60 to 80 in 1.26.2 | https://www.wiz.io/blog/malicious-version-of-microsofts-agent-framework-published-to-pypi | "the file cap rose from 60 to 80." | `agentfw/wiz.extract.md` |

### 3.4 Exfiltration, in behaviour terms

| claim | source URL | verbatim passage | saved body |
|---|---|---|---|
| Socket: collected JSON is zlib-compressed, base64-encoded and POSTed to the webhook (one request) | https://socket.dev/blog/agent-framework-pypi-package-compromised-with-credential-stealer | "Collected JSON is zlib-compressed, base64-encoded, and POSTed to the decoded webhook with" | `agentfw/socket.extract.md` |
| StepSecurity: one exfiltration attempt, errors suppressed, no retry | https://www.stepsecurity.io/blog/microsoft-agent-framework-pypi-package-compromised | "Each collector makes one exfiltration attempt, suppresses failures, and has no retry loop." | `agentfw/stepsecurity.extract.md` |
| Wiz: the destination is a free-tier anonymous webhook.site bin; at most 50 requests were captured (Wiz states it confirmed this) | https://www.wiz.io/blog/malicious-version-of-microsofts-agent-framework-published-to-pypi | "We have confirmed the attackers token was on the free tier, and a maximum of 50 requests were captured." | `agentfw/wiz.extract.md` |
| SafeDep: proxy/egress logs showing a POST to the destination identify hosts that sent data | https://safedep.io/blog/microsoft-agent-framework-pypi-compromise | "Proxy and egress logs that show a POST to it mark the hosts that sent data." | `agentfw/safedep.extract.md` |
| Wiz: status-code reading for a defender (200 accepted; 410/429 suggests rejected) | https://www.wiz.io/blog/malicious-version-of-microsofts-agent-framework-published-to-pypi | "A 200 means that host's data was accepted. A 410/429 suggests it was rejected." | `agentfw/wiz.extract.md` |

### 3.5 Provenance and cause (what is and is not known)

| claim | source URL | verbatim passage | saved body |
|---|---|---|---|
| SafeDep: how the attacker got publishing access is not known | https://safedep.io/blog/microsoft-agent-framework-pypi-compromise | "How the attacker got publishing access is not known yet." | `agentfw/safedep.extract.md` |
| StepSecurity: initial access vector, account/credential and uploader identity not established | https://www.stepsecurity.io/blog/microsoft-agent-framework-pypi-package-compromised | "The available evidence does not establish the initial access vector, the specific account or credential used, or the uploader's identity." | `agentfw/stepsecurity.extract.md` |
| Wiz: root cause unconfirmed | https://www.wiz.io/blog/malicious-version-of-microsofts-agent-framework-published-to-pypi | "The root cause hasn't been confirmed." | `agentfw/wiz.extract.md` |
| Wiz: no matching release tag; main branch does not contain the malicious code | https://www.wiz.io/blog/malicious-version-of-microsofts-agent-framework-published-to-pypi | "and the main branch doesn't contain the malicious code." | `agentfw/wiz.extract.md` |
| Wiz: 1.26.1 was wheel only (clean releases ship wheel + sdist) | https://www.wiz.io/blog/malicious-version-of-microsofts-agent-framework-published-to-pypi | "1.26.1 was a wheel only" | `agentfw/wiz.extract.md` |
| StepSecurity: both bad wheels shipped without a provenance attestation; absence alone does not identify the upload mechanism | https://www.stepsecurity.io/blog/microsoft-agent-framework-pypi-package-compromised | "and had no published provenance attestation." | `agentfw/stepsecurity.extract.md` |
| SafeDep: the clean 1.26.0 also has no attestation, so consumers could not tell the uploads apart | https://safedep.io/blog/microsoft-agent-framework-pypi-compromise | "PyPI has no attestation for 1.26.0 either" | `agentfw/safedep.extract.md` |
| SafeDep: second Microsoft PyPI package with rogue releases in six months (durabletask, stolen API token, May); no evidence of a link | https://safedep.io/blog/microsoft-agent-framework-pypi-compromise | "The payloads and infrastructure share nothing, so there is no evidence the two incidents are linked." | `agentfw/safedep.extract.md` |
| OpenSourceMalware: "account compromise is likely" (its assessment) | https://opensourcemalware.com/blog/agent-framework-pypi-compromised | "an account compromise is likely" | `agentfw/osm.extract.md` |
| StepSecurity: satellite packages checked had no uploads after 12 Nov (not a blanket finding) | https://www.stepsecurity.io/blog/microsoft-agent-framework-pypi-package-compromised | "had no uploads after November 12 at the time of that check." | `agentfw/stepsecurity.extract.md` |

### 3.6 Telemetry a defender checks (as the sources state it)

| claim | source URL | verbatim passage | saved body |
|---|---|---|---|
| SafeDep: look for the versions in lockfiles and requirement files | https://safedep.io/blog/microsoft-agent-framework-pypi-compromise | "Look for the versions in lockfiles and requirement files." | `agentfw/safedep.extract.md` |
| SafeDep: look for either startup file on machines/images/runners WITHOUT starting that environment's Python (starting it re-runs the stealer) | https://safedep.io/blog/microsoft-agent-framework-pypi-compromise | "On machines, images and runners, look for either startup file without starting the environment’s Python. Starting it would run the stealer again." | `agentfw/safedep.extract.md` |
| SafeDep: treat everything reachable from an environment that installed either version as exposed | https://safedep.io/blog/microsoft-agent-framework-pypi-compromise | "Treat every secret reachable from an environment that installed either version as exposed." | `agentfw/safedep.extract.md` |
| SafeDep: review sign-in and activity logs of managed identities and federated credentials from install time onward | https://safedep.io/blog/microsoft-agent-framework-pypi-compromise | "Review sign-in and activity logs for the managed identities and federated credentials that environment could use, from the install time onward." | `agentfw/safedep.extract.md` |
| SafeDep: rotation does not undo tokens already issued | https://safedep.io/blog/microsoft-agent-framework-pypi-compromise | "Rotation does not undo the tokens it had issued." | `agentfw/safedep.extract.md` |
| StepSecurity: removing the package alone does not terminate a detached payload process nor establish credentials are safe | https://www.stepsecurity.io/blog/microsoft-agent-framework-pypi-package-compromised | "Removing the package alone does not terminate a detached payload process or establish that credentials are safe." | `agentfw/stepsecurity.extract.md` |
| StepSecurity: rotating static secrets does not necessarily invalidate already-issued identity tokens | https://www.stepsecurity.io/blog/microsoft-agent-framework-pypi-package-compromised | "rotating static secrets does not necessarily invalidate already-issued identity tokens" | `agentfw/stepsecurity.extract.md` |
| Wiz: check proxy and DNS logs and treat a 200 from the capture service as data accepted | https://www.wiz.io/blog/malicious-version-of-microsofts-agent-framework-published-to-pypi | "A 200 means that host's data was accepted. A 410/429 suggests it was rejected." | `agentfw/wiz.extract.md` |
| Wiz: for workflows that installed 1.26.2 with id-token: write, treat GitHub OIDC tokens (both audiences) as exposed | https://www.wiz.io/blog/malicious-version-of-microsofts-agent-framework-published-to-pypi | "treat GitHub OIDC tokens for `api://AzureADTokenExchange` and https://management.azure.com/ as exposed. Review the Entra ID federated credentials that trust those repositories and workflows" | `agentfw/wiz.extract.md` |
| Socket: avoid the versions; remove and rotate | https://socket.dev/blog/agent-framework-pypi-package-compromised-with-credential-stealer | "Avoid installing either version; if installed, remove them and rotate potentially exposed credentials." | `agentfw/socket.extract.md` |
| SafeDep: pin to the clean version with hashes and hold newer releases until Microsoft confirms clean | https://safedep.io/blog/microsoft-agent-framework-pypi-compromise | "and hold off on any newer release until Microsoft confirms it is clean." | `agentfw/safedep.extract.md` |

### 3.7 Microsoft and PyPI response

- PyPI: quarantine of both releases (StepSecurity with timestamps; Wiz "no longer available" by ~21:30Z; SafeDep "removed"); the project page and JSON API show 1.26.0 as the only 1.26 release and latest as of 2026-11-18 ~05:00Z (own check above). OpenSourceMalware alone says the "Microsoft publisher" was quarantined and publishing access is "believed" to remain; StepSecurity says that whether access persists is not established.
- Microsoft: NO statement found. WebSearch (three queries including "Microsoft spokesperson") found no Microsoft or PyPI statement. The microsoft/agent-framework GitHub repository, its security advisories and issues could not be read from this session (GitHub is proxied: `url`, `extract`, `WebFetch` all returned HTTP 404 for github.com/microsoft/agent-framework and its API; `gh` access not enabled), so absence of a GitHub advisory is unverified. Wiz states (not Microsoft) that there is no python-1.26.1 tag or release in the microsoft/agent-framework repository (3.5 table).
- No fixed or newer clean release: PyPI latest is still 1.26.0; no 1.26.3 exists on PyPI (JSON API); SafeDep advises waiting for Microsoft to confirm any newer release.

### 3.8 Contradictions with the first pass (item 11) and open gaps

- CONFIRMED: affected 1.26.1 and 1.26.2 only; removed from PyPI; 1.26.0 last clean; .pth mechanism; SafeDep flagged 1.26.1 22 minutes after publication and 1.26.2 4 minutes after upload; collects env vars, credential files, /proc environments; requests Azure DevOps federation, managed-identity and (1.26.2) GitHub OIDC tokens; webhook.site exfiltration; about 192,000 downloads a month (SafeDep); durabletask precedent; no Microsoft statement.
- INACCURATE/INCOMPLETE as worded: "collects environment variables matching about 31 name substrings, up to 60 credential files" is the 1.26.1 profile. For 1.26.2, StepSecurity and Wiz give 35 substrings and up to 80 files (SafeDep says the collector is otherwise unchanged and does not split the numbers). Report both versions or say "31 to 35 substrings, 60 to 80 files depending on version (StepSecurity)".
- INACCURATE/INCOMPLETE: the first pass says both versions are "removed"; the more precise state (StepSecurity) is PyPI quarantine at 21:06:16Z (1.26.1) and 21:16:44Z (1.26.2), and 1.26.2 was uploaded 2 min 23 s after the first quarantine. That ordering is the strongest sign the publishing path was still under attacker control.
- ADDED: Wiz, StepSecurity and Aikido are further independent detectors; the first pass named only Socket and SafeDep. Socket published 2026-11-17 (extract metadata date 2026-11-17); SafeDep carries a 2026-11-18 date (page metadata `datePublished 2026-11-18T00:00:00Z`) but its timeline is all 2026-11-17 UTC.
- OPEN: Microsoft and PyPI own statements; GitHub repo/advisory state (unreadable from this session); whether agent-framework siblings (core, foundry, openai, redis, postgres, purview, tools) stayed clean beyond the two spot checks (own PyPI JSON: core and foundry no upload after 2026-11-12; StepSecurity: five other satellites checked no uploads after 2026-11-12); install count; root cause; whether publishing access persists.
- Not a vendor statement, so do not write "Microsoft confirmed": none of the above is Microsoft speaking.


## 4. N-ABLE N-central 2026.4 Hotfix 3 (build 2026.4.1.39)

Primary: https://status.n-able.com/2026/11/16/n-central-2026-4-hf3-release-notes/ (read with `extract`; the direct transports returned a shell so the page was served by the jina reader, fetched 2026-11-18 ~04:50Z; jina metadata `Published Time: 2026-11-16T21:04:35+00:00`). N-able's own status/advisory channel (uptime.n-able.com, a script-rendered page) was read with the jina reader at 2026-11-18 ~05:00Z: event pages https://uptime.n-able.com/event/202669/ (HF3 notice) and https://uptime.n-able.com/event/202613/ (12-13 Nov updates), and the dashboard root https://uptime.n-able.com/ (page header "Last Updated: Nov 18, 2026 04:47:39 UTC"). Huntress (updated 2026-11-16 7 PM ET and 2026-11-17 8:30 AM ET): https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains. N-able CNA records via ENISA EUVD: https://euvdservices.enisa.europa.eu/api/search?text=N-central&fromDate=2026-11-14&toDate=2026-11-18&page=0&size=50.

### 4.1 Release facts

| claim | source URL | verbatim passage | saved body |
|---|---|---|---|
| Build number | https://status.n-able.com/2026/11/16/n-central-2026-4-hf3-release-notes/ | "Build Number:2026.4.1.39" | `nable/hf3.extract.md` |
| Date | https://status.n-able.com/2026/11/16/n-central-2026-4-hf3-release-notes/ | "Last Updated:November 16th, 2026" | `nable/hf3.extract.md` |
| Vendor labels it a critical security update; builds on HF2 | https://status.n-able.com/2026/11/16/n-central-2026-4-hf3-release-notes/ | "N-central 2026.4 Hotfix 3 is a critical security update." | `nable/hf3.extract.md` |
| Supersedes GA, HF1 and HF2 builds | https://status.n-able.com/2026/11/16/n-central-2026-4-hf3-release-notes/ | "This release builds on and supersedes N-central 2026.4 (build 2026.4.0.27), N-central 2026.4 Hotfix 1 (build 2026.4.0.32), and N-central 2026.4 Hotfix 2 (build 2026.4.1.26)." | `nable/hf3.extract.md` |
| Scope: includes everything in HF2 | https://status.n-able.com/2026/11/16/n-central-2026-4-hf3-release-notes/ | "This hotfix builds on the existing N-central 2026.4 Hotfix 2 release and includes everything delivered in it." | `nable/hf3.extract.md` |
| Authentication and access control | https://status.n-able.com/2026/11/16/n-central-2026-4-hf3-release-notes/ | "We have added missing authentication and permission checks to additional server operations." | `nable/hf3.extract.md` |
| Agent and Probe security: Agent/Probe-to-server authentication and session handling (not the HF2 Agent-to-Probe change) | https://status.n-able.com/2026/11/16/n-central-2026-4-hf3-release-notes/ | "We have improved how Agents and Probes authenticate with, and communicate to, the N-central server, including session handling." | `nable/hf3.extract.md` |
| Agents/Probes direction clarified | https://status.n-able.com/2026/11/16/n-central-2026-4-hf3-release-notes/ | "This is communication from Agents and Probes to the N-central server. It is separate from the Agent-to-Probe communication changes in Hotfix 2." | `nable/hf3.extract.md` |
| File and import handling | https://status.n-able.com/2026/11/16/n-central-2026-4-hf3-release-notes/ | "We have added additional validation to file publishing, file path, and XML import handling." | `nable/hf3.extract.md` |
| Legacy API change (config option removed; permanently blocked) | https://status.n-able.com/2026/11/16/n-central-2026-4-hf3-release-notes/ | "We have removed the configuration option for legacy APIs, and legacy APIs are now permanently blocked." | `nable/hf3.extract.md` |
| User management | https://status.n-able.com/2026/11/16/n-central-2026-4-hf3-release-notes/ | "We have made improvements to how user accounts are managed and secured." | `nable/hf3.extract.md` |
| Agents and Probes: unpatched ones can be impersonated; everyone must upgrade them | https://status.n-able.com/2026/11/16/n-central-2026-4-hf3-release-notes/ | "Agents and Probes that are not upgraded are susceptible to impersonation." | `nable/hf3.extract.md` |
| Who upgrades what | https://status.n-able.com/2026/11/16/n-central-2026-4-hf3-release-notes/ | "All customers, hosted and on-premise, must upgrade all of their Agents and Probes to the latest version to be fully protected." | `nable/hf3.extract.md` |
| Hosted servers upgraded by N-able; on-prem must upgrade | https://status.n-able.com/2026/11/16/n-central-2026-4-hf3-release-notes/ | "Hosted N-central servers are upgraded by N-able." | `nable/hf3.extract.md` |
| Agents/Probes must go to HF3 even if already on HF2 | https://status.n-able.com/2026/11/16/n-central-2026-4-hf3-release-notes/ | "you must upgrade all of your Agents and Probes to the latest version, 2026.4.1 HF3, whether or not you have already upgraded them to Hotfix 2." | `nable/hf3.extract.md` |
| Agent verification: devices must report SMBIOS ID or machine ID; otherwise the server rejects them | https://status.n-able.com/2026/11/16/n-central-2026-4-hf3-release-notes/ | "If both are missing, N-central rejects the connection." | `nable/hf3.extract.md` |
| Inactive Assets tab: where it is | https://status.n-able.com/2026/11/16/n-central-2026-4-hf3-release-notes/ | "A new Inactive Assets tab under Configuration > Asset Discovery > Discovered Assets" | `nable/hf3.extract.md` |
| Network setup: appliance token behaviour section | https://status.n-able.com/2026/11/16/n-central-2026-4-hf3-release-notes/ | "then find the **Appliance token behaviour** section." | `nable/hf3.extract.md` |
| Post-upgrade review of inactive agents | https://status.n-able.com/2026/11/16/n-central-2026-4-hf3-release-notes/ | "After upgrading, allow time for your Agents to reconnect, then review the Inactive Assets tab for any Agents that need attention." | `nable/hf3.extract.md` |
| Known issue: remote control other than Take Control disabled | https://status.n-able.com/2026/11/16/n-central-2026-4-hf3-release-notes/ | "Remote control functionality other than Take Control is disabled. Take Control continues to work as expected." | `nable/hf3.extract.md` |
| Known issue: Intune integration blocked | https://status.n-able.com/2026/11/16/n-central-2026-4-hf3-release-notes/ | "The Intune integration is currently blocked." | `nable/hf3.extract.md` |
| Upgrade directly to 2026.4.1.39 from listed versions | https://status.n-able.com/2026/11/16/n-central-2026-4-hf3-release-notes/ | "Upgrade directly to 2026.4.1.39 from:" | `nable/hf3.extract.md` |

### 4.2 The 17 CVE ids fixed (N-able release notes list; N-able CNA CVSS 4.0 from EUVD)

The release notes give an id and a one-line title per CVE and no scores. N-able, as CNA, published scores and descriptions that EUVD mirrors; Huntress (2026-11-17 8:30 ET) confirms the scores come from N-able and that NVD has not scored them yet. Authentication wording is the CNA's.

| CVE | release-note title (verbatim) | CNA CVSS 4.0 (EUVD id) | Huntress severity | CNA description (verbatim) |
|---|---|---|---|---|
| CVE-2026-129271 | "N-central Patch Management Local Privilege Escalation" | 8.5 (EUVD-2026-126956) | high | "The Patch Management Engine in N-central is vulnerable to LPE via attacker controlled metadata" |
| CVE-2026-129272 | "MMS3 appliance authentication bypass via predictable passcode" | 9.3 (EUVD-2026-126957) | critical | "N-able N-central before 2026.4.1 HF3 uses a predictable credential to authenticate appliances to an agent-facing API. A remote, unauthenticated attacker who knows or guesses an appliance identifier can obtain a valid appliance token and session and impersonate that appliance." |
| CVE-2026-129273 | "Audit Export syslog injection allows root command execution" | 8.6 (EUVD-2026-126958) | high | "N-able N-central before 2026.4.1 HF3 does not neutralise control characters in an Audit Export setting before writing it to the system logging configuration. An authenticated attacker with product administrator privileges can inject configuration and execute commands as root on the N-central server." |
| CVE-2026-129274 | "ServerMMS2 task result submission missing authentication" | 8.7 (EUVD-2026-126959) | high | "N-able N-central before 2026.4.1 HF3 does not authenticate callers of the ServerMMS2 RemoteExecutionTaskSubmit operation or verify task ownership. A remote, unauthenticated attacker can submit forged results for remote execution tasks belonging to any customer." |
| CVE-2026-129275 | "repositoryItemGet missing authentication discloses policies" | 8.2 (EUVD-2026-126960) | high | "N-able N-central before 2026.4.1 HF3 allows the repositoryItemGet operation to be called without authentication. A remote, unauthenticated attacker who knows a policy identifier can download the Automation Manager policy of any customer, including embedded scripts and parameter values." |
| CVE-2026-129276 | "ServerMMS2 asset data submission missing authentication" | 6.9 (EUVD-2026-126961) | medium | "N-able N-central before 2026.4.1 HF3 does not authenticate callers of the ServerMMS2 AssetDiscoSimplifiedInfoSubmit operation. A remote, unauthenticated attacker can overwrite the asset data recorded for any appliance." |
| CVE-2026-129277 | "ServerMMS maintenance action read missing authentication" | 6.9 (EUVD-2026-126962) | medium | "N-able N-central before 2026.4.1 HF3 does not authenticate callers of the MaintActionGet operation. A remote, unauthenticated attacker can read and cancel the pending maintenance actions of any appliance." |
| CVE-2026-129278 | "Take Control audit log tampering without authentication" | 6.9 (EUVD-2026-126963) | medium | "N-able N-central before 2026.4.1 HF3 does not authenticate callers of the ServerII2 remoteControlMSPAStartEndTimeSubmit operation. A remote, unauthenticated attacker can alter the recorded state and times of Take Control remote control tasks and the associated audit log entries." |
| CVE-2026-129279 | "Password reset response discrepancy allows user enumeration" | 6.9 (EUVD-2026-126964) | medium | "The password reset function in N-able N-central before 2026.4.1 HF3 returns distinguishable responses for valid and invalid accounts. A remote, unauthenticated attacker can enumerate the email addresses of valid user accounts." |
| CVE-2026-129280 | "ServerUI SOAP operations missing authorisation checks" | 9.3 (EUVD-2026-126965) | critical | "Multiple ServerUI and ServerUI2 SOAP operations in N-able N-central before 2026.4.1 HF3 do not verify the caller's session, permissions or customer scope. A remote attacker, in some cases without authentication, can read device and patch data, test passwords of user accounts, send messages to managed agents, and modify device and service settings belonging to other customers." |
| CVE-2026-129281 | "View-only users can set DeviceExecute configuration" | 8.5 (EUVD-2026-126966) | high | "N-able N-central before 2026.4.1 HF3 checks only a view permission for ServerII2 operations that write device execution configuration. An authenticated user with view-only access to a device can set configuration that the Windows agent on that device acts on." |
| CVE-2026-129282 | "Test email sendmail argument injection, missing authorisation" | 8.7 (EUVD-2026-126967) | high | "The test email delivery function in N-able N-central before 2026.4.1 HF3 does not check permissions, lacks CSRF protection, and passes sender and recipient values to the mail program without neutralising option characters. An authenticated attacker can inject arguments into the mail command executed on the server." |
| CVE-2026-129283 | "N-central custom service import XML external entity injection" | 7.1 (EUVD-2026-126968) | high | "The custom service import in N-able N-central before 2026.4.1 HF3 processes XML external entities. An authenticated attacker can upload a crafted service definition to read files accessible to the N-central service account or cause the server to make outbound requests." |
| CVE-2026-129284 | "Report Manager and Data Export settings SSRF" | 5.3 (EUVD-2026-126969) | medium | "N-able N-central before 2026.4.1 HF3 does not validate connection targets in the Report Manager and Data Export settings. An authenticated attacker can cause the server to connect to arbitrary hosts, including loopback and internal addresses, and can use the responses to probe internal network services." |
| CVE-2026-129285 | "XMPP action response origin validation error" | 5.3 (EUVD-2026-126970) | medium | "N-able N-central before 2026.4.1 HF3 does not verify that an action response received over XMPP originates from the appliance the request was sent to. An attacker with the credentials of one appliance can forge responses on behalf of another appliance." |
| CVE-2026-129286 | "SIS GenericFiles version path traversal leads to RCE" | 9.2 (EUVD-2026-126971) | critical | "N-able N-central before 2026.4.1 HF3 does not validate version values and download locations in software update metadata. An attacker able to supply or modify the update metadata received by the server can write files outside the download directory and execute code as the N-central service account." |
| CVE-2026-129287 | "SIS repository parser XML external entity injection" | 8.3 (EUVD-2026-126972) | high | "N-able N-central before 2026.4.1 HF3 processes XML external entities in software repository files. An attacker able to supply or modify the repository files received by the server can read files accessible to the N-central service account or cause the server to make outbound requests." |

| claim | source URL | verbatim passage | saved body |
|---|---|---|---|
| N-able release notes introduce the list | https://status.n-able.com/2026/11/16/n-central-2026-4-hf3-release-notes/ | "N-central 2026.4 Hotfix 3 fixes the following vulnerabilities:" | `nable/hf3.extract.md` |
| Huntress: all 17 scored by N-able as CNA; 3 critical, 8 high, 6 medium; NVD not yet scored | https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains | "N-able has now published CVSS 4.0 scores and official descriptions for all 17 CVEs fixed in N-central 2026.4 Hotfix 3 (build 2026.4.1.39). Three are rated critical severity, eight high severity, and six medium severity." | `nable/huntress.extract.md` |
| Huntress: scores assigned by N-able as CNA | https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains | "All scores were assigned by N-able as the CVE Numbering Authority. NVD has not yet published its own scoring." | `nable/huntress.extract.md` |
| Huntress: CVE-2026-129272 is the impersonation issue behind the instruction to upgrade Agents and Probes | https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains | "This is the impersonation issue behind N-able's instruction to upgrade every Agent and Probe." | `nable/huntress.extract.md` |
| Huntress: patch management engine fix needs component 2.14.4.5829 or later (CVE-2026-129271) | https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains | "CVE-2026-129271 (8.5): Patch Management Engine local privilege escalation, fixed in Patch Management Component 2.14.4.5829" | `nable/huntress.extract.md` |
| Huntress: full-stack update advice (server, Agents, Probes, Patch Management Engine) | https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains | "Confirm the full stack is updated: the server to 2026.4.1.39, every Agent and Probe to 2026.4.1 HF3, and the Patch Management Engine to 2.14.4.5829 or later. A patched server alone does not close the impersonation issues." | `nable/huntress.extract.md` |
| Huntress: CVE-2026-129275 exposes Automation Manager policies incl. embedded scripts/parameters (rotate embedded secrets) | https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains | "Rotate secrets in Automation Manager policies. Any credentials or API keys embedded in policies on a server that was exposed before patching should be treated as potentially disclosed (CVE-2026-129275)." | `nable/huntress.extract.md` |
| Huntress: Take Control audit records from an unpatched server may be altered (CVE-2026-129278) | https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains | "Don't rely on Take Control audit records from an unpatched server during an investigation. They could have been altered (CVE-2026-129278)." | `nable/huntress.extract.md` |
| Huntress: user enumeration -> expect password attacks; enforce MFA (CVE-2026-129279) | https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains | "Valid account emails may have been enumerated (CVE-2026-129279), so make sure MFA is enforced on all N-central accounts." | `nable/huntress.extract.md` |
| BSI CERT-Bund WID-SEC-2026-4609 (hoch, 2026-11-16T23:00Z) lists 17 CVEs and "<2026.4.1.39" as affected, 2026.4 Hotfix 3 as fixed | https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-4609 | ""name": "<2026.4.1.39"" | `nable/wid-sec-2026-4609.csaf.json` |

Version table: affected = N-central builds before 2026.4.1.39 per the CNA wording "before 2026.4.1 HF3" (CVE-2026-129271's CNA text has no version); fixed = 2026.4.1.39 (HF3) plus Agents and Probes at 2026.4.1 HF3 (and, for CVE-2026-129271, Patch Management Component 2.14.4.5829 or later per Huntress). Supported direct-upgrade sources: 2025.4, 2026.1, 2026.2, 2026.3, 2026.3.1 HF1-HF4, 2026.4, 2026.4 HF1 (2026.4.0.32), 2026.4 HF2 (2026.4.1.26).

### 4.3 Agents and Probes; Legacy API; the named chains (4EverAble2Shell, Agent2Shell)

| claim | source URL | verbatim passage | saved body |
|---|---|---|---|
| Release notes: Agent verification checks and impersonation protection | https://status.n-able.com/2026/11/16/n-central-2026-4-hf3-release-notes/ | "N-central 2026.4 Hotfix 3 improves how N-central verifies and manages the Agents that connect to it. This update helps protect against Agent impersonation" | `nable/hf3.extract.md` |
| Huntress: HF3 removes the Legacy API option, which several PoCs used | https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains | "The hotfix also removes the configuration option for legacy APIs, a feature that was leveraged in several of the proofs of concept (POCs) that emerged for the recent CVEs." | `nable/huntress.extract.md` |
| N-able (via Huntress 13 Nov): Agent2Shell exploitation, like 4EverAble2Shell, requires the non-default Legacy API | https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains | "Additionally, N-able confirmed that Agent2Shell exploitation (like 4EverAble2Shell) requires the non-default Legacy API to be enabled." | `nable/huntress.extract.md` |
| Huntress 12 Nov: HF2 with Legacy API disabled is not exposed to the 4EverAble2Shell chain | https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains | "Servers running 2026.4 HF2 with Legacy API disabled are not exposed to this exploit chain." | `nable/huntress.extract.md` |
| N-able 12 Nov notice (own channel): "developing additional remediation" | https://uptime.n-able.com/event/202613/ | "Our teams are actively assessing the new disclosures, developing additional remediation, and working to safely restore affected functionality." | `nable/uptime-202613.jina.md` |
| N-able 12 Nov notice: Legacy API off by default; instructions to disable | https://uptime.n-able.com/event/202613/ | "Legacy API access is disabled by default. If you enabled it, follow these instructions:" | `nable/uptime-202613.jina.md` |
| N-able HF3 notice (own channel, event 202669, started 2026-11-16 21:00 UTC): framed as a response to "non-responsible communication" | https://uptime.n-able.com/event/202669/ | "As part of our continued response to the non-responsible communication of critical vulnerabilities affecting N-central," | `nable/uptime-202669.jina.md` |
| N-able HF3 notice: refers to the 9 Nov and 12 Nov announcements but names no chain and states no CVE-to-chain mapping | https://uptime.n-able.com/event/202669/ | "The vulnerabilities announced on November 9 and November 12 are specific to N-central. No other N-able products are at risk from these vulnerabilities." | `nable/uptime-202669.jina.md` |
| N-able HF3 notice: generic description only | https://uptime.n-able.com/event/202669/ | "HF3 builds on the protections delivered in HF2 and includes further improvements across authentication and access controls, Agent and Probe communications, file handling, server components, legacy APIs, and user management." | `nable/uptime-202669.jina.md` |
| N-able HF3 notice: legacy APIs permanently blocked | https://uptime.n-able.com/event/202669/ | "Removed the configuration option for legacy APIs. Legacy APIs are now permanently blocked." | `nable/uptime-202669.jina.md` |
| N-able HF3 notice: CVEs are in the HF2 and HF3 release notes | https://uptime.n-able.com/event/202669/ | "Please see Release Notes for" | `nable/uptime-202669.jina.md` |
| N-able event 202669 start time on the dashboard | https://uptime.n-able.com/ | "ID: 202669 Start: Nov 16, 2026 21:00:00 UTC End: N/A Severity: Major Outage Status: Identified" | `nable/uptime-202609.jina.md` |

Name check (grep over the saved bodies, count of matches for "4EverAble2Shell", "Agent2Shell", "Able2Shell", "Axis", "CVE-2026-90436"): release notes `nable/hf3.extract.md` = 0; N-able HF3 notice `nable/uptime-202669.jina.md` = 0; N-able 12-13 Nov page `nable/uptime-202613.jina.md` = 0. So **neither the HF3 release notes nor N-able's HF3 notice names 4EverAble2Shell, Agent2Shell or the Apache Axis CVE-2026-90436**, and neither says they are fixed. What N-able does say: the Legacy API (the precondition N-able itself stated for both chains) is now permanently blocked; HF3 hardens Agent/Probe authentication (relevant to Agent2Shell-type impersonation, mapping not stated by N-able except that Huntress ties CVE-2026-129272 to the impersonation instruction). "No fix for the named chains" can therefore no longer be written as N-able's current statement: N-able has made no statement either way after HF3, and the stated precondition is removed. Do not write "HF3 fixes 4EverAble2Shell".

### 4.4 Exploitation and public PoC (post-HF3)

| claim | source URL | verbatim passage | saved body |
|---|---|---|---|
| Huntress 17 Nov: public PoC for ALL 17 HF3 CVEs released the evening of 16 Nov, shortly after the hotfix; unpatched servers should be treated as exposed (single source for the PoC claim) | https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains | "Public proof-of-concept code for all 17 CVEs was released on the evening of November 16, shortly after the hotfix. Any unpatched server should be treated as exposed." | `nable/huntress.extract.md` |
| Huntress 17 Nov: no exploitation of these issues observed in its partners' environments | https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains | "As of this writing, Huntress has not observed exploitation of these issues in our partners' environments." | `nable/huntress.extract.md` |
| Huntress 16 Nov (7 PM ET): no evidence of exploitation in the wild for the HF3 CVEs | https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains | "We have not seen evidence of exploitation in the wild." | `nable/huntress.extract.md` |
| N-able 12 Nov (own channel): "no signs of compromise" | https://uptime.n-able.com/event/202613/ | "we have seen no signs of compromise. We are continuing to monitor closely and will provide updates as needed." | `nable/uptime-202613.jina.md` |
| N-able 13 Nov 03:50 UTC (own channel): identified IOCs; working with those specific customers | https://uptime.n-able.com/event/202613/ | "Through our ongoing investigation today, we have identified Indicators of Compromise (IOCs) and are working closely with those specific customers to assess and mitigate any potential risks." | `nable/uptime-202613.jina.md` |
| N-able 13 Nov 13:40 UTC: IOCs relevant only to customers that have not disabled the Legacy API (per Huntress) | https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains | "In an [<u>update to its security advisory</u>](https://uptime.n-able.com/) on November 13 at 13:40:25 UTC, N-able said that it has identified Indicators of Compromise (IoCs) for customers that haven't disabled the Legacy API." | `nable/huntress.extract.md` |
| Tenable FAQ (last update 16 Nov, not about HF3): Huntback 21 servers, 19 on HF2 | https://www.tenable.com/blog/able2shell-frequently-asked-questions-for-reported-n-able-n-central-zero-day-vulnerabilities | "On November 12, the security firm huntback reported that a newer exploit chain, 4EverAble2Shell, was used to install cryptocurrency miners on 21 live N-central servers it identified, 19 of which reported running Hotfix 2." | `nable/tenable-faq.extract.md` |
| NCSC-CH Security Hub post 13163 last modified 2026-11-16 09:34Z (BEFORE HF3): exploitation status "Actively exploited" | https://security-hub.ncsc.admin.ch/#/posts/13163 | ""lastModified": "2026-11-16T09:34:43.742878Z"" | `nable/ncsc-csh-13163.json` |
| NCSC-CH 13163 (pre-HF3): "additional fixes are still expected" | https://security-hub.ncsc.admin.ch/#/posts/13163 | "additional fixes are still expected to adress additional vulnerabilities" | `nable/ncsc-csh-13163.json` |
| Own check: none of the 17 HF3 ids, CVE-2026-90436 or the seven HF2 ids is on CISA KEV | https://www.cisa.gov/known-exploited-vulnerabilities-catalog (via `fetch_source.py cisa-kev`) | "on KEV: none of the 25 ids checked" | `nable/kev-check.txt` |
| NCSC-CH 13163: edit reason | https://security-hub.ncsc.admin.ch/#/posts/13163 | "Updated with claims of active exploitation" | `nable/ncsc-csh-13163.json` |

Net status: exploitation of the 4EverAble2Shell chain against HF2-with-Legacy-API-on servers is reported by Huntback/Previdian (already in the entry); for the 17 new HF3 CVEs the only post-HF3 statements are Huntress's (PoC public since the evening of 16 Nov; no exploitation seen in its partners' environments, as of 17 Nov 8:30 ET). No CISA KEV listing for any of CVE-2026-129271..129287, CVE-2026-90436 or the seven HF2 ids (catalogVersion 2026.11.17, released 2026-11-17T17:53Z, own check recorded in `nable/kev-check.txt`).

### 4.5 What changed vs the covered entry, and an extra N-able lead

- Covered entry `2026-11-10/n-able-n-central-33-unpatched-flaws-public-pocs-offline`: last records 2026-11-14 (update: Agent2Shell also needs the Legacy API; IOCs published; "N-able still has no fix") and 2026-11-15 (internal correction). HF3 (2026-11-16) is the follow-up hotfix the 2026-11-13 record said was planned.
- The entry's `fixed` text "N-able has no fix for this chain and plans a follow-up hotfix" for CVE-2026-90436 is now stale as a statement about N-able's position: the follow-up hotfix exists, but N-able does not say it fixes the Axis chain (see 4.3).
- NEW EXTRA LEAD (not one of the five items; separate incident): N-able Mail Assure and SpamExperts Hosted Cloud security incident. N-able's uptime page (update "Nov 18, 2026 03:05:09 UTC", read 2026-11-18 ~05:00Z):

| claim | source URL | verbatim passage | saved body |
|---|---|---|---|
| N-able: unauthorized access to one server of the Mail Assure / SpamExperts Hosted Cloud | https://uptime.n-able.com/ | "We are aware of unauthorized access to one of the servers in the Mail Assure and SpamExperts Hosted Cloud." | `nable/uptime-202609.jina.md` |
| N-able: unrelated to the N-central incident | https://uptime.n-able.com/ | "This is unrelated to the N-central incident." | `nable/uptime-202609.jina.md` |
| N-able: no evidence of customer data compromise at this time; UI and API access disabled; mail flow unaffected | https://uptime.n-able.com/ | "at this time we do not have evidence that customer data was compromised, including access to tenants’ mailboxes." | `nable/uptime-202609.jina.md` |
| N-able: earlier 16 Nov statement attributed the disruption to configuration and dependencies; later determined to be a security incident | https://uptime.n-able.com/ | "As we continued our investigation, we determined that the disruption was caused by a security incident affecting the Mail Assure and SpamExperts Hosted Cloud environment." | `nable/uptime-202609.jina.md` |
| Timestamp of that update | https://uptime.n-able.com/ | "Nov 18, 2026 03:05:09 UTC" | `nable/uptime-202609.jina.md` |

Mail Assure / SpamExperts is an email-security service used by MSPs and some public bodies (assessment); it is a vendor incident disclosure from the vendor's own status channel, still "Identified" at fetch, worth a separate look by the S4 sweep (suppliers).

### 4.6 Contradictions with the first pass (item 12) and open gaps

- CONFIRMED: build 2026.4.1.39; date 2026-11-16; builds on HF2 (2026.4.1.26) and HF1; the 17 ids CVE-2026-129271 to -129287 and their release-note titles; Legacy API permanently blocked; Agent/Probe authentication and session hardening, separate from the HF2 Agent-to-Probe change; unpatched Agents/Probes susceptible to impersonation; on-prem upgrade servers, hosted by N-able, all upgrade Agents/Probes; known issues (remote control other than Take Control; Intune); BSI WID-SEC-2026-4609 with 17 CVEs; the release notes do not mention 4EverAble2Shell, Agent2Shell or the Axis CVE by name.
- WORDING TO FIX: first pass groups "-129274 to -129277, -129280" as "missing authentication ... and ServerUI SOAP operations". The release-note title for -129280 is "ServerUI SOAP operations missing authorisation checks" (CNA: "in some cases without authentication"); -129277 is "ServerMMS maintenance action read missing authentication" (MaintActionGet read AND cancel per the CNA).
- NOT IN THE FIRST PASS (material): (1) N-able CNA CVSS 4.0 scores now exist (3 critical: -129272 9.3, -129280 9.3, -129286 9.2; 8 high; 6 medium); (2) Huntress states public PoC code for all 17 CVEs appeared the evening of 16 Nov, and that unpatched servers should be treated as exposed; (3) Huntress has not observed exploitation of the 17 in its partners' environments; (4) the Patch Management Engine component fix level 2.14.4.5829; (5) N-able's own HF3 notice and its 12-13 Nov statements (read from its uptime channel); (6) the separate Mail Assure/SpamExperts incident.
- The first pass sentence "NCSC-CH advisory 13163 (edited 2026-11-16 09:34Z, before HF3) already states actively exploited and 'additional fixes are still expected'" is confirmed verbatim (4.4); it predates HF3, so its "fixes still expected" is superseded by HF3 for the 17 CVEs.
- OPEN: which HF3 CVE(s), if any, close the Apache Axis chain (CVE-2026-90436) and the Agent2Shell chains: not stated by N-able, Huntress or Tenable. The N-able security-advisory pages on me.n-able.com (customer portal) were not read. The single-source PoC claim (Huntress) is uncorroborated. No other media coverage of HF3 was found by WebSearch (index thin).


## 5. AXIS OS and Apache mod_http2 (CVE-2026-119618)

Primary: https://www.axis.com/dam/public/permalink/294609/cve-2026-119618pdf-en-US_294609.pdf (one-page PDF; read with `python3 tools/fetch_source.py pdf` on 2026-11-18 ~04:50Z: "2024 chars from 5/27 streams", per-font ToUnicode decode, text-layer PDF, no OCR needed). The extractor emits one text run per line and splits tokens around hyphens and "://", so the saved raw text (`axis/axis-cve-2026-119618.pdf.txt`) is unreadable as prose; passages below are quoted from a whitespace-normalized copy (`axis/axis-cve-2026-119618.normalized.txt`: lines joined, split hyphens and punctuation re-attached, no word changed). A copy saved through `url --direct` could not be parsed by `pdftotext` (flate stream errors) and was discarded, so `fetch_source.py pdf` is the only working reader found; `pdfinfo` on that copy showed creator "Microsoft Word for Microsoft 365", created Mon Nov 16 07:20:54 2026 UTC, 1 page. Axis's own registry page: https://help.axis.com/en-us/security-advisories (extract; page date 2026-11-17).

### 5.1 What the Axis PDF says

| claim | source URL | verbatim passage | saved body |
|---|---|---|---|
| Advisory title, date, version | https://www.axis.com/dam/public/permalink/294609/cve-2026-119618pdf-en-US_294609.pdf | "Security Advisory CVE-2026-119618 – 2026-11-16 (v1.0)" | `axis/axis-cve-2026-119618.normalized.txt` |
| Affected products, solutions and services: one line; NO tracks, branches or fixed versions are enumerated | https://www.axis.com/dam/public/permalink/294609/cve-2026-119618pdf-en-US_294609.pdf | "Affected products, solutions, and services • AXIS OS 6.50.5.10 or higher" | `axis/axis-cve-2026-119618.normalized.txt` |
| Root cause attribution: the Apache project fixed it in httpd 2.4.71 on 11 Nov 2026 | https://www.axis.com/dam/public/permalink/294609/cve-2026-119618pdf-en-US_294609.pdf | "The Apache Software Foundation released Apache HTTP Server 2.4.71 on November 11, 2026, fixing CVE-2026-119618," | `axis/axis-cve-2026-119618.normalized.txt` |
| CVSS Axis gives (9.8 Critical), impact, auth state ("administrator-access" is the PDF text; the hyphen may be a line-break artefact) | https://www.axis.com/dam/public/permalink/294609/cve-2026-119618pdf-en-US_294609.pdf | "a CVSS 9.8 Critical remote code execution vulnerability that would allow an unauthenticated attacker to gain administrator-access to the Axis network device." | `axis/axis-cve-2026-119618.normalized.txt` |
| Exploitation and public exploits (Axis' knowledge only) | https://www.axis.com/dam/public/permalink/294609/cve-2026-119618pdf-en-US_294609.pdf | "To Axis’ knowledge, no known exploits exist publicly as of today and Axis is not aware that this has been exploited in its network products." | `axis/axis-cve-2026-119618.normalized.txt` |
| Planned service release: all affected AXIS OS tracks, "within the next couple of weeks", exact timelines to follow | https://www.axis.com/dam/public/permalink/294609/cve-2026-119618pdf-en-US_294609.pdf | "Axis is working on a service release for all affected AXIS OS tracks within the next couple of weeks, more accurate timelines will be provided in time." | `axis/axis-cve-2026-119618.normalized.txt` |
| Release-note wording Axis announces | https://www.axis.com/dam/public/permalink/294609/cve-2026-119618pdf-en-US_294609.pdf | "The release notes will state the following: Updated Apache to version 2.4.71 to increase overall cybersecurity." | `axis/axis-cve-2026-119618.normalized.txt` |
| Devices outside the tracks but still supported | https://www.axis.com/dam/public/permalink/294609/cve-2026-119618pdf-en-US_294609.pdf | "Axis devices not included in these tracks and still under support will receive a patch according to their planned maintenance and release schedule." | `axis/axis-cve-2026-119618.normalized.txt` |
| Update recommendation | https://www.axis.com/dam/public/permalink/294609/cve-2026-119618pdf-en-US_294609.pdf | "It is recommended to update the Axis device software." | `axis/axis-cve-2026-119618.normalized.txt` |
| Workaround, introduction (verbatim) | https://www.axis.com/dam/public/permalink/294609/cve-2026-119618pdf-en-US_294609.pdf | "As an immediate workaround, configure the Axis device as below to prevent the vulnerability exploitation. Once an update has been provided, this setting can be reverted again." | `axis/axis-cve-2026-119618.normalized.txt` |
| Workaround, setting 1 (device parameter via param.cgi; the PDF text layer shows "HTTP(S) :// <DEVICE-IP> /axis-cgi/..." with spaces) | https://www.axis.com/dam/public/permalink/294609/cve-2026-119618pdf-en-US_294609.pdf | "/axis-cgi/param.cgi?action=update&System.HTTP2.AllowH2=no" | `axis/axis-cve-2026-119618.normalized.txt` |
| Workaround, setting 2 | https://www.axis.com/dam/public/permalink/294609/cve-2026-119618pdf-en-US_294609.pdf | "/axis-cgi/param.cgi?action=update&System.HTTP2.AllowH2c=no" | `axis/axis-cve-2026-119618.normalized.txt` |
| Bulk deployment | https://www.axis.com/dam/public/permalink/294609/cve-2026-119618pdf-en-US_294609.pdf | "Use Axis Device Manager or any other device configuration tool to mass-deploy this configuration accordingly." | `axis/axis-cve-2026-119618.normalized.txt` |
| Contact | https://www.axis.com/dam/public/permalink/294609/cve-2026-119618pdf-en-US_294609.pdf | "For further assistance and questions, please contact Axis Technical Support." | `axis/axis-cve-2026-119618.normalized.txt` |

Not in the PDF (confirmed by reading all of `axis/axis-cve-2026-119618.normalized.txt`): any mention of mod_http2, "HTTP/2" prose, the device web interface, a list of AXIS OS tracks or release numbers, a fixed AXIS OS version, an LTS-track list, authentication/privilege wording beyond "unauthenticated", an exploit-prerequisite statement, or the CVSS vector. The only HTTP/2 references are the two parameter names in the workaround (System.HTTP2.AllowH2 and System.HTTP2.AllowH2c).

### 5.2 Axis registry, CERT-FR and the Apache primary

| claim | source URL | verbatim passage | saved body |
|---|---|---|---|
| Axis registry row for AXIS OS: 9.8 Critical, Affected = Yes; "patched by upgrading to Apache version 2.4.71"; no released AXIS OS version listed (page date 2026-11-17) | https://help.axis.com/en-us/security-advisories | "The vulnerability is patched by upgrading to Apache version 2.4.71. For an immediate workaround follow the mitigation steps in the security advisory." | `axis/axis-help-advisories.extract.md` |
| Registry row cells | https://help.axis.com/en-us/security-advisories | "9.8 (Critical) \| Yes \| [Axis Security Advisory](https://www.axis.com/dam/public/permalink/294609/cve-2026-119618pdf-en-US_294609.pdf)" | `axis/axis-help-advisories.extract.md` |
| Registry page date | https://help.axis.com/en-us/security-advisories | "date: "2026-11-17"" | `axis/axis-help-advisories.extract.md` |
| CERT-FR (CERTFR-2026-AVI-1549; initial version 17 November 2026): affected = all versions from 6.50.5.10 | https://www.cert.cyber.gouv.fr/avis/CERTFR-2026-AVI-1549/ | "- Axis OS toutes versions à partir de 6.50.5.10" | `axis/certfr-avi-1549.extract.md` |
| CERT-FR: Axis says a fix will be available within a few weeks | https://www.cert.cyber.gouv.fr/avis/CERTFR-2026-AVI-1549/ | "Axis déclare qu'un correctif sera disponible d'ici quelques semaines." | `axis/certfr-avi-1549.extract.md` |
| CERT-FR: a workaround is provided | https://www.cert.cyber.gouv.fr/avis/CERTFR-2026-AVI-1549/ | "Une mesure de contournement est fournie." | `axis/certfr-avi-1549.extract.md` |
| CERT-FR: risk = remote arbitrary code execution | https://www.cert.cyber.gouv.fr/avis/CERTFR-2026-AVI-1549/ | "- Exécution de code arbitraire à distance" | `axis/certfr-avi-1549.extract.md` |
| CERT-FR revision history (only initial version, 17 Nov 2026) | https://www.cert.cyber.gouv.fr/avis/CERTFR-2026-AVI-1549/ | "17 novembre 2026 Version initiale" | `axis/certfr-avi-1549.rawtext.txt` |
| Apache httpd security page: CVE-2026-119618 is mod_http2 assign_headers heap corruption and RCE, rated critical | https://httpd.apache.org/security/vulnerabilities_24.html | "(critical):mod\_http2: heap corruption and RCE in assign\_headers" | `axis/apache-vulns24.extract.md` |
| Apache: affected httpd 2.4.55 through 2.4.70; mod_h2 2.0.8 through 2.0.42 | https://httpd.apache.org/security/vulnerabilities_24.html | "can lead to RCE. This issue affects Apache HTTP Server: from 2.4.55 through 2.4.70. Affected releases of mod\_h2 from GitHub: from 2.0.8 through 2.0.42." | `axis/apache-vulns24.extract.md` |
| Apache: fixed in 2.4.71, released 2026-11-11; finders Anthropic's OSS Scanner and Google Cloud VR | https://httpd.apache.org/security/vulnerabilities_24.html | "Update 2.4.71 released 2026-11-11 Affects 2.4.55 through 2.4.70" | `axis/apache-vulns24.extract.md` |
| Apache: finder credit | https://httpd.apache.org/security/vulnerabilities_24.html | "finder: Anthropic's OSS Scanner, as vulnerability ANT-2026-MAPKT6MZ" | `axis/apache-vulns24.extract.md` |
| Context: AXIS OS 12.11 (active track) release flyer says Apache was updated to 2.4.67 there (inside the Apache-affected 2.4.55-2.4.70 range) | https://www.axis.com/dam/public/permalink/274172/axis-os-1211-release-flyer-en-US_274172.pdf | "Apache has been updated to version 2.4.67 and curl has been updated to version 8.20." | `axis/axis-os-1211-release-flyer.normalized.txt` |
| Context: Axis explains tracks: active track and LTS tracks (a new LTS track every two years, maintained five years) | https://www.axis.com/dam/public/permalink/274172/axis-os-1211-release-flyer-en-US_274172.pdf | "An LTS track has a fixed feature set, and a new track is issued every two years and maintained for five years." | `axis/axis-os-1211-release-flyer.normalized.txt` |

### 5.3 Version table

| item | value | source |
|---|---|---|
| Affected AXIS OS | "AXIS OS 6.50.5.10 or higher" (CERT-FR: "toutes versions à partir de 6.50.5.10"); tracks not enumerated | Axis PDF; CERT-FR |
| Underlying component | Apache HTTP Server 2.4.55 through 2.4.70 affected, mod_http2 `assign_headers()`; fixed 2.4.71 (2026-11-11) | Apache |
| Axis CVSS | 9.8 Critical (Axis states the number; no vector in the PDF) | Axis PDF; registry |
| Fixed AXIS OS | none released as of 2026-11-18 ~05:00Z: "working on a service release for all affected AXIS OS tracks within the next couple of weeks" (dated 2026-11-16) | Axis PDF; registry lists no released version |
| Devices outside those tracks, still supported | patch "according to their planned maintenance and release schedule" | Axis PDF |
| Workaround | System.HTTP2.AllowH2=no and System.HTTP2.AllowH2c=no via /axis-cgi/param.cgi?action=update; revert after update | Axis PDF |

### 5.4 Contradictions with the first pass (item 13) and open gaps

- CONFIRMED: 6.50.5.10 or higher; Apache 2.4.71 of 2026-11-11; "CVSS 9.8" stated by Axis; unauthenticated, administrator access; "To Axis' knowledge, no known exploits exist publicly ... not aware that this has been exploited"; service release for all affected tracks "within the next couple of weeks"; "more accurate timelines will be provided in time"; release-note wording; devices outside the tracks; workaround parameters and Axis Device Manager bulk deployment; CERT-FR AVI-1549 (initial version 17 November 2026).
- NOT SUPPORTED BY THE PAGE: the first pass summary says "Axis phrases the advisory as an HTTP/2 flaw reachable on the device web interface". The Axis PDF never says "HTTP/2 flaw" or "web interface"; it says only that Apache fixed CVE-2026-119618 and gives two HTTP2 device parameters as the workaround. The mod_http2 attribution is the Apache project's (Apache page above); the inference that the workaround disables the vulnerable path is the analyst's.
- WORDING: the first pass title says "calls for a service release within weeks"; the PDF says Axis "is working on a service release ... within the next couple of weeks". It is a plan, not a date, and the PDF says more accurate timelines will follow. "Axis has no fixed release yet" is true as of the PDF and the registry (no released version listed, checked 2026-11-18).
- WORDING: "no exploitation known to Axis" is accurate but note the two limbs: "no known exploits exist publicly" (about public exploit code) and "Axis is not aware that this has been exploited in its network products". Neither is a statement about Apache httpd generally; the store entry for the Apache issue holds that.
- OPEN: the AXIS OS tracks and release numbers affected; the AXIS OS release carrying Apache 2.4.71; whether PoC code for CVE-2026-119618 exists (the Axis statement is as of 2026-11-16; the Apache and distribution coverage is in the existing store entry, not re-read here); Axis's later timeline update. The Axis PDF has no revision after v1.0 and the registry shows no released version.
- The Axis registry also lists other Apache-related rows (CVE-2026-49975 and CVE-2026-48913, patched by upgrading to Apache 2.4.68), i.e. Axis handles Apache CVEs by bundling a newer Apache in a service release, consistent with the release-note wording above.


## 6. Unreadable or unverified (cross-item)

- github.com/microsoft/agent-framework (repo, issues, security advisories) and api.github.com: HTTP 404 through `url`, `extract` and `WebFetch` (the sandbox proxy only enables repositories attached to the session); `gh` access not enabled. Item 11: Microsoft statement unverified.
- Mitel KB000129195 and N-able/Oracle My Oracle Support notes (CPU433, CPU454, KA923, KA1182): customer-login pages, not read.
- Oracle pre-release page (652 patches): replaced by the published advisory; only `state/coverage_backlog.md` records its numbers.
- Axis PDF: readable only through `fetch_source.py pdf` (the raw download through `url --direct` is corrupted by the proxy path); text layer is token-per-line, normalized copy saved.
- uptime.n-able.com is script-rendered: readable only through the jina reader (two of three keys were out of balance, the third worked; the pool may be dead at the next fire).

## 7. Source-health notes for the main agent (recipes that worked or failed)

- `extract` served every page here directly except the N-able HF3 release notes (served by jina) and the Axis PDF (use `pdf`).
- `safedep.io` article: `extract` silently drops the "Timeline" block (script-rendered component); recover from `url --direct` raw HTML (the section text is in the HTML).
- Oracle: `extract` reads the advisory and the "verbose" English matrices; the raw HTML carries the "Affected Products and Patch Information" table that `extract` drops.
- N-able uptime dashboard event pages: `jina <URL>` works (event/202669, event/202613); `extract` returns the empty shell.
- EUVD: `api/search?text=<vendor>&fromDate&toDate&page&size` works through `url --direct` and pages with `page=N`.
