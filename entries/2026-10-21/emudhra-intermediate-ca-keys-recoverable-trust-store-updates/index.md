---
schema: 1
kind: incident
title: "eMudhra: the private keys of eight intermediate CA certificates were trivially recoverable, so anyone could forge trusted HTTPS certificates; browsers block them, clients with their own trust store or no revocation checking need an update (CVE-2026-111943 in Go)"
headline: "Eight eMudhra CA keys were guessable; Windows drops seven certificates, and Java, Python, Go and GitLab need updates"
summary: >
  On 2026-10-17 a researcher reported that the private keys of eight eMudhra intermediate CA certificates had been generated with
  too little randomness, so anyone could recover them and forge trusted HTTPS certificates for any site. Firefox, Chrome, Apple
  and Microsoft platforms block the intermediates and eMudhra revoked them; Microsoft went further on 2026-10-26 and removed seven
  eMudhra-hierarchy certificates from the Windows trust list, and from the Edge trust list on 2026-10-27. Software that keeps its own
  trust store or does not check revocation stays exposed until updated: Go fixed it in 1.27.3 and 1.26.10 as CVE-2026-111943, GitLab
  in its releases of 2026-10-29, Python added a built-in denylist as CVE-2026-115557, and Java needs the second update of 2026-10-24
  (CVE-2026-114820, CVSS 3.1 9.1) even on a runtime updated in the past few days. Chrome's removal of the emSign ECC Root CA - G3 root
  was due on 2026-10-27; Cisco's advisory dates its ISE fixes to December 2026 and April 2027, and no exploitation is reported.
discovered_at: "2026-10-21T03:43:00Z"
updated_at: "2026-11-01T03:32:20Z"
event_date: "2026-10-20"
run_id: 2026-10-21T0256Z-intel
priority: notable
immediate_action: null
tags: [supply-chain, patch-available]
regions: [global]
sectors: []
entities: ["incident:emudhra-intermediate-ca-key-compromise-2026-10", "product:oracle-java-se", "product:oracle-graalvm-for-jdk", "product:openjdk", "product:cpython", "product:cisco-secure-firewall-management-center", "product:cisco-duo-access-gateway", "product:cisco-duo-network-gateway", "product:cisco-thousandeyes-enterprise-agent", "product:cisco-ios-xr-software", "product:microsoft-windows", "product:microsoft-edge", "product:gitlab", "product:cisco-identity-services-engine", "product:oracle-database-server", "product:oracle-autonomous-health-framework", "product:oracle-global-lifecycle-management-opatch", "product:oracle-hospitality-cruise-shipboard-property-management"]
techniques: [T1557]
affected_products: ["Oracle Java SE", "Oracle GraalVM for JDK", "OpenJDK", "CPython", "Cisco Secure Firewall Management Center", "Cisco Duo Access Gateway", "Cisco Duo Network Gateway", "Cisco ThousandEyes Enterprise Agent", "Cisco IOS XR Software", "Microsoft Windows", "Microsoft Edge", "GitLab", "Cisco Identity Services Engine", "Oracle Database Server", "Oracle Autonomous Health Framework", "Oracle Global Lifecycle Management OPatch", "Oracle Hospitality Cruise Shipboard Property Management"]
cves:
  - id: CVE-2026-91403
    cvss: "9.1 (CVSS 3.1)"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [patch-available, mitigation-only]
    affected: "Oracle Java SE 8u511, 8u511-perf, 11.0.33, 17.0.21, 21.0.13, 25.0.5, 27.0.1; Oracle GraalVM for JDK 17.0.21 and 21.0.13; Oracle GraalVM Enterprise Edition 21.3.20; OpenJDK 27.0.1, 25.0.5, 21.0.13, 17.0.21, 11.0.32.1, 8u504 and earlier"
    fixed: "superseded by the Java updates of Oracle's Security Alert CVE-2026-114820 and the OpenJDK advisory of 2026-10-24: Oracle's second alert lists the builds 27.0.1.0.2, 25.0.5.0.2, 21.0.13.0.2, 17.0.21.0.2, 11.0.33.0.2 and 8u511-b32 as affected, and OpenJDK says to act even on runtimes updated in the past few days"
  - id: CVE-2026-114820
    cvss: "9.1 (CVSS 3.1)"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [patch-available, mitigation-only]
    affected: "Oracle Java SE 8u511-b32, 8u511-perf-b32, 11.0.33.0.2, 17.0.21.0.2, 21.0.13.0.2, 25.0.5.0.2, 27.0.1.0.2; Oracle GraalVM for JDK 17.0.21.0.2 and 21.0.13.0.2; Oracle GraalVM Enterprise Edition 21.3.20.0.2; OpenJDK 27.0.1.0.2, 25.0.5.0.2, 21.0.13.0.2, 17.0.21.0.2, 11.0.32.1, 8u504 and earlier; Oracle Database Server 19.3-19.32, 21.3-21.23 and 23.4.0-23.26.3 (RDBMS, Java; not applicable to client-only installations), Oracle Autonomous Health Framework Trace File Analyzer 26.3-26.10, Oracle Global Lifecycle Management OPatch 12.2.0.1.16-12.2.0.1.52 and Oracle Hospitality Cruise Shipboard Property Management Next-Gen SPMS 23.3.4-23.3.6 (revision 2 of 2026-10-30)"
    fixed: "the Java updates of Oracle's Security Alert CVE-2026-114820 (build numbers in Oracle's Patch Availability Document) and the OpenJDK update whose release note names JDK-8395690; until updated, delete the cacerts aliases emsignrootcag1, emsignrootcag2, emsigneccrootcag3 and comodoaaaca or enable revocation checking; the incident tracker lists Oracle JDK 27.0.1.0.3, 25.0.5.0.3, 21.0.13.0.3, 17.0.21.0.3, 11.0.33.0.3 and 8u511 b33 as fixed and OpenJDK builds as pending"
  - id: CVE-2026-115557
    cvss: "9.4 (CVSS 4.0)"
    epss: null
    type: logic-flaw
    vector: user-interaction
    auth: pre-auth
    status: [patch-available]
    affected: "CPython 3.15.0 before 3.15.2, 3.14.0 before 3.14.10, 3.13.0 before 3.13.18, 3.12.0 before 3.12.16, every release before 3.11.18, and 3.16.0a1 before 3.16.0 per ENISA's record"
    fixed: "Python 3.15.2, 3.14.10, 3.13.18, 3.12.16 and 3.11.18 carry the ssl denylist (Python Insider, 2026-10-26), which the post says makes normal uses of pip safe even if pip is not updated; Christian Heimes says in the announcement thread that pip before 26.2.2 keeps trusting the compromised intermediates whatever the system trust store holds, because it always loads its own vendored certifi"
sources:
  - url: "https://blog.google/security/protecting-chrome-and-android-users-from-compromised-emudhra-intermediate-ca-certificates/"
    publisher: "Google (Chrome Root Program and Android Security)"
    date: "2026-10-20"
    role: primary
  - url: "https://emudhra.we-have-a-problem.com/"
    publisher: "Dennis Jackson (eMudhra intermediate CA compromise incident tracker)"
    date: "2026-10-20"
    role: primary
  - url: "https://blog.mozilla.org/security/2026/10/20/protecting-firefox-users-following-the-compromise-of-emudhra-intermediate-certificates/"
    publisher: "Mozilla Security Blog"
    date: "2026-10-20"
    role: corroborating
  - url: "https://groups.google.com/g/golang-announce/c/66pojueaQek"
    publisher: "Go team (golang-announce)"
    date: "2026-10-20"
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/mozilla-google-apple-block-compromised-emudhra-ca-certificates/"
    publisher: "BleepingComputer"
    date: "2026-10-20"
    role: corroborating
  - url: "https://www.oracle.com/security-alerts/alert-cve-2026-91403.html"
    publisher: "Oracle (Security Alert CVE-2026-91403)"
    date: "2026-10-21"
    role: primary
  - url: "https://openjdk.org/groups/vulnerability/advisories/2026-10-21"
    publisher: "OpenJDK (Vulnerability Advisory 2026/10/21)"
    date: "2026-10-21"
    role: primary
  - url: "https://security-hub.ncsc.admin.ch/#/posts/13091"
    publisher: "NCSC.ch Security Hub (advisory 13091)"
    date: "2026-10-22"
    role: corroborating
  - url: "https://www.oracle.com/security-alerts/alert-cve-2026-114820.html"
    publisher: "Oracle (Security Alert CVE-2026-114820)"
    date: "2026-10-24"
    role: primary
  - url: "https://openjdk.org/groups/vulnerability/advisories/2026-10-24"
    publisher: "OpenJDK (Vulnerability Advisory 2026/10/24)"
    date: "2026-10-24"
    role: primary
  - url: "https://openjdk.org/emudhra"
    publisher: "OpenJDK (Compromised Certificates and OpenJDK Java Runtimes)"
    date: "2026-10-24"
    role: corroborating
  - url: "https://mail.python.org/archives/list/security-announce@python.org/thread/FNAJMZV6XQYLVPABNINDMF3VF66AYLW4/"
    publisher: "Python Software Foundation (security-announce, CVE-2026-115557)"
    date: "2026-10-24"
    role: primary
  - url: "https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-109299"
    publisher: "ENISA EUVD (EUVD-2026-109299)"
    date: "2026-10-24"
    role: corroborating
  - url: "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-emudhra-info-ScS22A1r"
    publisher: "Cisco PSIRT (cisco-sa-emudhra-info, version 1.1)"
    date: "2026-10-24"
    role: corroborating
  - url: "https://discuss.python.org/t/information-for-python-users-regarding-emudhra-emsign-ca-certificate-security-incident/109576"
    publisher: "Python Discourse (eMudhra information for Python users)"
    date: "2026-10-20"
    role: corroborating
  - url: "https://thehackernews.com/2026/10/emudhra-to-exit-global-ssltls-business.html"
    publisher: "The Hacker News"
    date: "2026-10-22"
    role: corroborating
  - url: "https://emudhra.com/en/press-release/emudhra-to-exit-global-ssl-tls-certificate-business"
    publisher: "eMudhra (press release)"
    date: "2026-10-22"
    role: corroborating
  - url: "https://www.microsoft.com/en-us/msrc/blog/2026/10/microsoft-response-to-compromised-emudhra-certificate-authority-keys"
    publisher: "Microsoft Security Response Center (updated 2026-10-27)"
    date: "2026-10-26"
    role: primary
  - url: "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-emudhra-info-ScS22A1r"
    publisher: "Cisco PSIRT (cisco-sa-emudhra-info, version 1.5)"
    date: "2026-10-30"
    role: primary
  - url: "https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-5-3-released/"
    publisher: "GitLab (patch release 19.5.3, date of its patch-release feed entry)"
    date: "2026-10-29"
    role: primary
  - url: "https://blog.python.org/2026/10/python-3152-31410-31318-31216-31118/"
    publisher: "Python Insider (release post; the page carries no date, 2026-10-26 is the date of its blog feed entry)"
    date: "2026-10-26"
    role: primary
  - url: "https://emudhra.we-have-a-problem.com/"
    publisher: "Dennis Jackson (eMudhra intermediate CA compromise incident tracker, update of 28 October)"
    date: "2026-10-28"
    role: primary
  - url: "https://www.oracle.com/security-alerts/alert-cve-2026-114820.html"
    publisher: "Oracle (Security Alert CVE-2026-114820, revision 2)"
    date: "2026-10-30"
    role: primary
closed_sources: []
evidence:
  - quote: "enabling anyone to forge trusted HTTPS certificates to impersonate any website against clients that have not yet removed trust in those CAs."
    publisher: "Google (Chrome Root Program and Android Security)"
    source_url: "https://blog.google/security/protecting-chrome-and-android-users-from-compromised-emudhra-intermediate-ca-certificates/"
  - quote: "many other clients do not consume revocation information and require software updates to ensure they no longer trust the compromised intermediates."
    publisher: "Dennis Jackson (eMudhra intermediate CA compromise incident tracker)"
    source_url: "https://emudhra.we-have-a-problem.com/"
  - quote: "We do not know if attackers exploited the flawed key generation to target these clients."
    publisher: "Dennis Jackson (eMudhra intermediate CA compromise incident tracker)"
    source_url: "https://emudhra.we-have-a-problem.com/"
  - quote: "crypto/x509: mitigation for security concerns with a specific Certificate Authority"
    publisher: "Go team (golang-announce)"
    source_url: "https://groups.google.com/g/golang-announce/c/66pojueaQek"
  - quote: "This Security Alert addresses CVE-2026-91403 by providing Java updates which distrusts the set of impacted intermediate CA certificates related to eMudhra."
    publisher: "Oracle (Security Alert CVE-2026-91403)"
    source_url: "https://www.oracle.com/security-alerts/alert-cve-2026-91403.html"
  - quote: "This Security Alert addresses CVE-2026-114820 by providing Java updates that remove the set of impacted root CA certificates related to eMudhra."
    publisher: "Oracle (Security Alert CVE-2026-114820)"
    source_url: "https://www.oracle.com/security-alerts/alert-cve-2026-114820.html"
  - quote: "take one of the following actions immediately — even if you have updated your runtime in the past few days."
    publisher: "OpenJDK (Compromised Certificates and OpenJDK Java Runtimes)"
    source_url: "https://openjdk.org/emudhra"
  - quote: "Python has added a denylist for known compromised certificates to the \"ssl\" module to ensure user safety even without certificate revocation configured."
    publisher: "Python Software Foundation (security-announce, CVE-2026-115557)"
    source_url: "https://mail.python.org/archives/list/security-announce@python.org/thread/FNAJMZV6XQYLVPABNINDMF3VF66AYLW4/"
  - quote: "Chrome has told eMudhra that standard ACME clients do not replace certificates outside their renewal window unless they support ACME Renewal Information (ARI) or someone steps in by hand."
    publisher: "The Hacker News"
    source_url: "https://thehackernews.com/2026/10/emudhra-to-exit-global-ssltls-business.html"
  - quote: "On October 26, Microsoft released an out-of-band Windows update that removes seven certificates associated with the affected hierarchies: six eMudhra G3 roots and an AAA Certificate Services cross-sign, from the Windows trust list."
    publisher: "Microsoft Security Response Center"
    source_url: "https://www.microsoft.com/en-us/msrc/blog/2026/10/microsoft-response-to-compromised-emudhra-certificate-authority-keys"
  - quote: "GitLab has removed trust for eight eMudhra intermediate CA certificates whose private keys have been compromised."
    publisher: "GitLab"
    source_url: "https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-5-3-released/"
  - quote: "The Cisco PSIRT is not aware of any malicious use of the issue that is described in this advisory."
    publisher: "Cisco PSIRT"
    source_url: "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-emudhra-info-ScS22A1r"
verification: multi-source
sourcing_note: >
  The Chrome Root Program and Mozilla describe their own handling, the incident tracker is maintained by a Mozilla
  cryptography engineer, and the weak-key cause and eMudhra's explanation come through BleepingComputer's account of
  Mozilla's incident report. Google counts eight subordinate CAs and six TLS intermediates. Microsoft's own post states its block of
  2026-10-20 and its removal of seven certificates from the Windows and Edge trust lists; Cisco's advisory is at version 1.5, and GitLab's page
  carries no date, so 2026-10-29 is the date of its patch-release feed entry.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions:
  - "Update every non-browser TLS client that keeps its own CA bundle or does not check revocation to a fixed version: standalone Java runtimes, including those already updated on 2026-10-21, to the update of Oracle's Security Alert CVE-2026-114820 or OpenJDK (Oracle Database Server, Autonomous Health Framework and OPatch installations too), Python 3.15.2, 3.14.10, 3.13.18, 3.12.16 or 3.11.18 together with pip 26.2.2 or later, Go 1.27.3 or 1.26.10, and self-managed GitLab to a fixed patch release together with GitLab Runner 19.5.1; then confirm with curl against the incident tracker's test host that the client rejects the certificate."
  - "Replace, by hand where the ACME client does not support ACME Renewal Information, every TLS certificate your organisation holds that chains to emSign ECC Root CA - G3 or to another of the seven certificates Microsoft removed from the Windows and Edge trust lists, because Chrome's removal of the G3 root was due on 2026-10-27 and the Windows change takes effect when the trust-list update reaches a device; deliver the updated Disallowed Certificate Trust List and the trust-list changes Microsoft describes, including its out-of-band update of 2026-10-26, to Windows devices that do not receive automatic certificate-trust updates."
  - "Apply Cisco's remediation now for the products its eMudhra advisory (version 1.5) lists with a fix or a procedure available: the guidance for Secure Firewall ASA, FTD and FMC, Secure Email Gateway and Secure Email and Web Manager (run the updatenow command where updates are manual), Duo Access Gateway 3.2.0, Duo Network Gateway 3.4.1, Duo Agentic Authorization Connector 1.0.1 and ThousandEyes Enterprise Agent (Application-hosting Agent 5.2.2)."
updates:
  - at: "2026-10-23T03:43:28Z"
    run_id: 2026-10-23T0256Z-intel
    type: update
    summary: >
      Standalone Java runtimes keep their own trust store: Oracle's Security Alert CVE-2026-91403 (CVSS
      3.1 9.1) and the OpenJDK advisory of 2026-10-21 ship the distrust update, the tracker lists the
      fixed builds, replacing blocked.certs or enabling revocation checking is the stop-gap, and NCSC.ch
      lists the exploitation status as unknown.
    fields: [headline, summary, affected_products, cves, sources, evidence, actions, body, entities]
  - at: "2026-10-25T03:36:20Z"
    run_id: 2026-10-25T0256Z-intel
    type: update
    summary: >
      Oracle's second Security Alert of 2026-10-24, CVE-2026-114820 (CVSS 3.1 9.1), removes four root CAs
      and lists Java SE builds such as 27.0.1.0.2 as affected, and OpenJDK says even a runtime updated in
      the past few days needs it, so a standalone Java runtime updated on 2026-10-21 needs the new update
      or the same stop-gap again; OpenJDK now says Debian, Devuan and Ubuntu packages need the keystore
      recreated by hand. Python announces a built-in ssl denylist (CVE-2026-115557) without naming a
      release, so pip 26.2.2 is the Python fix to apply now; Cisco lists the products it has fixes for;
      and eMudhra is leaving the global TLS business, and standard ACME clients do not replace the
      affected certificates outside their renewal window unless they support ACME Renewal Information.
    fields: [headline, summary, cves, affected_products, entities, sources, evidence, actions, body]
  - at: "2026-11-01T03:32:20Z"
    run_id: 2026-11-01T0256Z-intel
    type: update
    summary: >
      Microsoft removed seven eMudhra-hierarchy certificates from the Windows trust list in an out-of-band
      update of 2026-10-26 and from the Edge trust list on 2026-10-27; Cisco's advisory reached version
      1.5 on 2026-10-30 with ISE fixes dated December 2026 and April 2027; GitLab's releases of 2026-10-29
      distrust the eight intermediates, with GitLab Runner and the AI Gateway needing separate updates;
      Python's releases of 2026-10-26 carry the built-in denylist; and Oracle's revision of 2026-10-30
      extends the Java alert to Oracle Database Server, Autonomous Health Framework and OPatch.
      Certificates that chain to the removed roots need replacing, and disconnected Windows devices need
      the updated trust lists.
    fields: [headline, summary, entities, affected_products, sources, evidence, sourcing_note, actions, body, cves]
  - at: "2026-11-01T13:46:55Z"
    run_id: 2026-11-01T1312Z-audit
    type: correction
    summary: >
      Python 3.15.1, 3.14.9 and 3.13.17, which the 2026-10-25 section listed as patched, predate the ssl
      denylist; the protected releases are 3.15.2, 3.14.10, 3.13.18, 3.12.16 and 3.11.18, and the tracker
      clause that carried the earlier versions is removed.
    fields: [body, evidence]
migrated_from: null
---

On 2026-10-17 a researcher reported to the Chrome Root Program, and Mozilla received a report the same day, that the private keys of eight eMudhra subordinate CA certificates were compromised: the keys were generated with insufficient randomness, which lets anyone forge trusted HTTPS certificates to impersonate any website against clients that have not removed trust in those CAs ([Google, 2026-10-20](https://blog.google/security/protecting-chrome-and-android-users-from-compromised-emudhra-intermediate-ca-certificates/); [Mozilla, 2026-10-20](https://blog.mozilla.org/security/2026/10/20/protecting-firefox-users-following-the-compromise-of-emudhra-intermediate-certificates/)). BleepingComputer, citing Mozilla's incident report, says all eight were P-384 keys generated in April 2025 with values below 256, so testing 256 numbers recovers a key, and that eMudhra blames a key-generation script error and found no evidence of end-user certificates ([BleepingComputer, 2026-10-20](https://www.bleepingcomputer.com/news/security/mozilla-google-apple-block-compromised-emudhra-ca-certificates/)). Google reports that no certificates chaining to the six TLS intermediates were logged to Certificate Transparency before it blocked them, so CT-enforcing clients such as Chrome could not have been attacked ([Google, 2026-10-20](https://blog.google/security/protecting-chrome-and-android-users-from-compromised-emudhra-intermediate-ca-certificates/)); the tracker says it is not known whether attackers used the flaw against other clients ([Dennis Jackson, 2026-10-20](https://emudhra.we-have-a-problem.com/)).

Chrome blocked the intermediates on 2026-10-17, Firefox through OneCRL the same day, Microsoft platforms on 2026-10-20 and Apple devices on 2026-10-22, and eMudhra revoked all eight ([Dennis Jackson, 2026-10-20](https://emudhra.we-have-a-problem.com/); [BleepingComputer, 2026-10-20](https://www.bleepingcomputer.com/news/security/mozilla-google-apple-block-compromised-emudhra-ca-certificates/)). Microsoft went further: an out-of-band Windows update of 2026-10-26 removes seven certificates, six eMudhra G3 roots and an AAA Certificate Services cross-sign, from the Windows trust list, and the same seven left the Edge trust list on 2026-10-27 ([Microsoft, 2026-10-26](https://www.microsoft.com/en-us/msrc/blog/2026/10/microsoft-response-to-compromised-emudhra-certificate-authority-keys)). Google removed the root that signed them, emSign ECC Root CA - G3, from the Chrome Root Store, with the removal expected to reach devices on 2026-10-27, after which some legitimate certificates chaining to it will stop working in Chrome ([Google, 2026-10-20](https://blog.google/security/protecting-chrome-and-android-users-from-compromised-emudhra-intermediate-ca-certificates/)). Go 1.27.3 and 1.26.10 filter chains that contain the intermediates in crypto/x509, tracked as CVE-2026-111943 ([Go team, 2026-10-20](https://groups.google.com/g/golang-announce/c/66pojueaQek)), and GitLab's release of 2026-10-29 removes trust for the eight intermediates in self-managed CE and EE, with GitLab Runner 19.5.1 and the AI Gateway needing separate updates ([GitLab, 2026-10-29](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-5-3-released/)).

Oracle's Security Alert of 2026-10-21 for CVE-2026-91403 (CVSS 3.1 9.1, component JSSE, remotely exploitable without authentication through the component's APIs) provided Java updates that distrust the impacted eMudhra intermediate CA certificates ([Oracle, 2026-10-21](https://www.oracle.com/security-alerts/alert-cve-2026-91403.html)), and a second Security Alert of 2026-10-24, CVE-2026-114820 (CVSS 3.1 9.1, same component and exposure), provides updates that remove the impacted root CA certificates and, from its revision of 2026-10-30, also covers the Java component of Oracle Database Server (not client-only installations), Autonomous Health Framework and OPatch ([Oracle, 2026-10-30](https://www.oracle.com/security-alerts/alert-cve-2026-114820.html)). OpenJDK's guidance tells users of a standalone runtime to act immediately even if they updated in the past few days, preferably by installing an update whose release note names JDK-8395690 and CVE-2026-114820 ([OpenJDK, 2026-10-24](https://openjdk.org/emudhra)). If no update is available, OpenJDK gives two alternatives: delete the aliases emsignrootcag1, emsignrootcag2, emsigneccrootcag3 and comodoaaaca from the runtime's cacerts keystore and restart it, repeating for each installation, or enable revocation checking with -Dcom.sun.net.ssl.checkRevocation=true and -Dcom.sun.security.enableCRLDP=true on the application's java command line ([OpenJDK, 2026-10-24](https://openjdk.org/emudhra)). OpenJDK packages from Red Hat, Oracle Linux, Fedora, Arch Linux and Gentoo most likely use the operating system's certificates; Debian, Devuan and Ubuntu need a manual workaround because updating ca-certificates and ca-certificates-java does not refresh the keystore (as superuser, remove /etc/ssl/certs/java/cacerts and run update-ca-certificates --fresh) ([OpenJDK, 2026-10-24](https://openjdk.org/emudhra)).

**Exposure:** any software that keeps its own CA bundle or does not check revocation keeps trusting the intermediates until updated; Python 3.15.2, 3.14.10, 3.13.18, 3.12.16 and 3.11.18 carry a built-in denylist ([Python Insider, 2026-10-26](https://blog.python.org/2026/10/python-3152-31410-31318-31216-31118/)), and the tracker lists fixed versions for pip (26.2.2), certifi, rustls-webpki, the curl CA bundle and distribution packages and lists Bottlerocket, HarmonyOS, certbot, containerd, Godot and LibreOffice as still pending; its update of 28 October says the git, curl and python3 that ship with macOS still trust them ([Dennis Jackson, 2026-10-28](https://emudhra.we-have-a-problem.com/)). A client's state is read with the tracker's test hosts: a certificate error means the client does not trust the intermediates ([Dennis Jackson, 2026-10-20](https://emudhra.we-have-a-problem.com/)).

**Detection:** eMudhra says it found no evidence that the intermediates were used to issue end-user certificates ([BleepingComputer, 2026-10-20](https://www.bleepingcomputer.com/news/security/mozilla-google-apple-block-compromised-emudhra-ca-certificates/)), so a server certificate chain seen in TLS session metadata, proxy or EDR network telemetry that contains one of the eight intermediates or their Sectigo cross-signs, which the tracker lists, is worth treating as a possible forged certificate ([Dennis Jackson, 2026-10-20](https://emudhra.we-have-a-problem.com/)). CT monitoring will not show one, because Google found no certificate chaining to the six TLS intermediates logged before it blocked them ([Google, 2026-10-20](https://blog.google/security/protecting-chrome-and-android-users-from-compromised-emudhra-intermediate-ca-certificates/)).

**Triage:** a site that still chains to emSign ECC Root CA - G3 failing in Chrome after 2026-10-27, or a certificate that chains to one of the seven certificates Microsoft removed failing in Windows or Edge once the change reaches the device, is the announced root removal, not an attack ([Google, 2026-10-20](https://blog.google/security/protecting-chrome-and-android-users-from-compromised-emudhra-intermediate-ca-certificates/); [Microsoft, 2026-10-26](https://www.microsoft.com/en-us/msrc/blog/2026/10/microsoft-response-to-compromised-emudhra-certificate-authority-keys)).

**Defender takeaway:** update trust bundles and toolchains on every non-browser client, rebuild container images that embed an old bundle, and do not rely on revocation or CT for those clients; website operators with certificates chaining to emSign ECC Root CA - G3 need one from another hierarchy now, Chrome's removal of that root having been due to reach devices on 2026-10-27 ([Google, 2026-10-20](https://blog.google/security/protecting-chrome-and-android-users-from-compromised-emudhra-intermediate-ca-certificates/)), and Windows devices that do not receive automatic certificate-trust updates need the updated Disallowed Certificate Trust List and the trust-list changes, including Microsoft's out-of-band update of 2026-10-26 ([Microsoft, 2026-10-26](https://www.microsoft.com/en-us/msrc/blog/2026/10/microsoft-response-to-compromised-emudhra-certificate-authority-keys)). A Java runtime updated in the past few days needs the update of 2026-10-24 ([OpenJDK, 2026-10-24](https://openjdk.org/emudhra)), and an ACME client will not replace a certificate under that root outside its renewal window unless it supports ACME Renewal Information, so trigger the renewal by hand ([The Hacker News, 2026-10-22](https://thehackernews.com/2026/10/emudhra-to-exit-global-ssltls-business.html)).

## Update — 2026-10-23T03:43:28Z

On 2026-10-21 Oracle issued Security Alert CVE-2026-91403 and the OpenJDK project an advisory for the same event, which reaches Java runtimes as well; Oracle says it also applies to sandboxed Java Web Start and applet clients ([Oracle, 2026-10-21](https://www.oracle.com/security-alerts/alert-cve-2026-91403.html)). Affected are Oracle Java SE 8u511, 8u511-perf, 11.0.33, 17.0.21, 21.0.13, 25.0.5 and 27.0.1, GraalVM for JDK 17.0.21 and 21.0.13 and GraalVM Enterprise Edition 21.3.20, and OpenJDK lists 27.0.1, 25.0.5, 21.0.13, 17.0.21, 11.0.32.1 and 8u504 and earlier ([Oracle, 2026-10-21](https://www.oracle.com/security-alerts/alert-cve-2026-91403.html); [OpenJDK, 2026-10-21](https://openjdk.org/groups/vulnerability/advisories/2026-10-21)). NCSC.ch's advisory of 2026-10-22 lists the exploitation status as unknown and the OpenJDK guidance as the temporary mitigation ([NCSC.ch, 2026-10-22](https://security-hub.ncsc.admin.ch/#/posts/13091)).

## Update — 2026-10-25T03:36:20Z

Oracle's second Security Alert of 2026-10-24, CVE-2026-114820 (CVSS 3.1 9.1, component JSSE, remotely exploitable without authentication through the component's APIs), provides Java updates that remove the impacted root CA certificates related to eMudhra ([Oracle, 2026-10-24](https://www.oracle.com/security-alerts/alert-cve-2026-114820.html)). Its affected list names Oracle Java SE 8u511-b32, 11.0.33.0.2, 17.0.21.0.2, 21.0.13.0.2, 25.0.5.0.2 and 27.0.1.0.2, and the OpenJDK advisory of the same day lists 27.0.1.0.2, 25.0.5.0.2, 21.0.13.0.2, 17.0.21.0.2, 11.0.32.1 and 8u504 and earlier as affected ([Oracle, 2026-10-24](https://www.oracle.com/security-alerts/alert-cve-2026-114820.html); [OpenJDK, 2026-10-24](https://openjdk.org/groups/vulnerability/advisories/2026-10-24)). OpenJDK tells users of a standalone runtime to act immediately even if they updated in the past few days, by installing an update whose release note names JDK-8395690 and CVE-2026-114820 or, failing that, by deleting the cacerts aliases emsignrootcag1, emsignrootcag2, emsigneccrootcag3 and comodoaaaca or enabling revocation checking ([OpenJDK, 2026-10-24](https://openjdk.org/emudhra)). The same page now says Debian, Devuan and Ubuntu OpenJDK packages need the keystore recreated by hand, because updating ca-certificates and ca-certificates-java does not refresh it, which replaces the earlier statement that updating the operating system's certificates suffices there ([OpenJDK, 2026-10-24](https://openjdk.org/emudhra)).

The Python Software Foundation announced CVE-2026-115557 on 2026-10-24: the ssl module now carries a denylist of known compromised certificates that is rejected whatever the SSLContext policy, so it works without revocation checking ([Python Software Foundation, 2026-10-24](https://mail.python.org/archives/list/security-announce@python.org/thread/FNAJMZV6XQYLVPABNINDMF3VF66AYLW4/)). ENISA's record scores it 9.4 (CVSS 4.0) and lists CPython before 3.16.0 as affected, and the announcement names no release that carries the denylist ([ENISA EUVD, 2026-10-24](https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-109299)). The Python releases that carry the ssl denylist are 3.15.2, 3.14.10, 3.13.18, 3.12.16 and 3.11.18 ([Python Insider, 2026-10-26](https://blog.python.org/2026/10/python-3152-31410-31318-31216-31118/)), and Christian Heimes stresses in the announcement thread that pip before 26.2.2 keeps trusting the compromised intermediates whatever the system trust store holds, because it always loads its own vendored certifi ([Dennis Jackson, 2026-10-20](https://emudhra.we-have-a-problem.com/); [Python Discourse, 2026-10-20](https://discuss.python.org/t/information-for-python-users-regarding-emudhra-emsign-ca-certificate-security-incident/109576)).

Cisco's informational advisory, version 1.1 of 2026-10-24, lists as impacted with remediation a TLS policy that blocks the known eMudhra issuers on Secure Firewall Management Center, Duo Access Gateway 3.2.0, Duo Network Gateway 3.4.1, Duo Agentic Authorization Connector 1.0.1, ThousandEyes Enterprise Agent (Application-hosting Agent 5.2.2, 2026-10-23), Meraki MV Smart Camera Firmware (2026-11-18), IOS XR 26.4.1 (2026-11-30) and Ultra Cloud Core Subscriber Microservices Infrastructure 2026.04.1 (November 2026), keeps further products under investigation, and says Cisco PSIRT is not aware of malicious use ([Cisco PSIRT, 2026-10-24](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-emudhra-info-ScS22A1r)).

eMudhra's board decided on 2026-10-22 to leave the global SSL/TLS certificate business, and its G1 RSA roots keep serving customers during the transition ([eMudhra, 2026-10-22](https://emudhra.com/en/press-release/emudhra-to-exit-global-ssl-tls-certificate-business)). The Hacker News relays Chrome's count of about 30,800 unexpired certificates under the emSign ECC Root CA - G3, which Chrome stops trusting on 2026-10-27, as of 2026-10-21, 99.9 percent of them issued through InCommon, and relays Chrome's point that standard ACME clients do not replace a certificate outside its renewal window unless they support ACME Renewal Information or someone steps in by hand ([The Hacker News, 2026-10-22](https://thehackernews.com/2026/10/emudhra-to-exit-global-ssltls-business.html)).

## Update — 2026-11-01T03:32:20Z

Microsoft released an out-of-band Windows update on 2026-10-26 that removes seven certificates associated with the affected hierarchies, six eMudhra G3 roots and an AAA Certificate Services cross-sign, from the Windows trust list, and removed the same seven from the Edge trust list on 2026-10-27; removing a root is a separate and broader decision than blocking the compromised intermediates, which Microsoft had done through its Disallowed Certificate Trust List on 2026-10-20 ([Microsoft, 2026-10-26](https://www.microsoft.com/en-us/msrc/blog/2026/10/microsoft-response-to-compromised-emudhra-certificate-authority-keys)). Microsoft tells organizations to keep automatic trust-list updates flowing, to make sure disconnected Windows devices receive the updated trust lists, and to replace certificates that chain to one of the seven before the change reaches their devices, and it warns that software that does not check revocation or the disallowed list could still accept certificates tied to the compromised keys if trust is restored locally ([Microsoft, 2026-10-26](https://www.microsoft.com/en-us/msrc/blog/2026/10/microsoft-response-to-compromised-emudhra-certificate-authority-keys)).

Cisco's advisory is at version 1.5 of 2026-10-30. It lists remediation for Secure Firewall ASA, FTD and FMC (guidance page), Secure Email Gateway and Secure Email and Web Manager (updated automatically to Trusted Root 2.8, with the updatenow command where updates are manual) and Packaged and Unified Contact Center Enterprise (CSCwx36769); it dates the fixes for ISE and ISE-PIC to ISE 3.5P5 in December 2026 and 3.3P13 and 3.4P8 in April 2027, and still lists IOS XE Software, MDS 9000 and Nexus switches among the impacted products under investigation; Cisco says it is not aware of malicious use ([Cisco PSIRT, 2026-10-30](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-emudhra-info-ScS22A1r)). GitLab's patch release of 2026-10-29 removes trust for the eight intermediates in self-managed CE and EE and says GitLab Runner 19.5.1 and the AI Gateway must be updated separately because they verify certificates on their own ([GitLab, 2026-10-29](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-5-3-released/)). Python's expedited releases of 2026-10-26, 3.15.2, 3.14.10, 3.13.18, 3.12.16 and 3.11.18, now carry the built-in denylist for the compromised intermediates ([Python Insider, 2026-10-26](https://blog.python.org/2026/10/python-3152-31410-31318-31216-31118/)). Oracle's revision 2 of Security Alert CVE-2026-114820, dated 2026-10-30, adds the Java component of Oracle Database Server (19.3 to 19.32, 21.3 to 21.23 and 23.4.0 to 23.26.3, not client-only installations), Autonomous Health Framework Trace File Analyzer 26.3 to 26.10, OPatch 12.2.0.1.16 to 12.2.0.1.52 and Hospitality Cruise Shipboard Property Management 23.3.4 to 23.3.6, each remotely exploitable without authentication at CVSS 3.1 9.1 ([Oracle, 2026-10-30](https://www.oracle.com/security-alerts/alert-cve-2026-114820.html)).

## Correction — 2026-11-01T13:46:55Z

Python 3.15.1, 3.14.9 and 3.13.17 do not carry the protection: the releases whose ssl module blocks the compromised eMudhra keys are 3.15.2, 3.14.10, 3.13.18, 3.12.16 and 3.11.18 ([Python Insider, 2026-10-26](https://blog.python.org/2026/10/python-3152-31410-31318-31216-31118/)). A host on 3.15.1, 3.14.9 or 3.13.17 still needs the later release.
