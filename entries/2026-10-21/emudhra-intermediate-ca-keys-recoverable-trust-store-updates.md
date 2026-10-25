---
schema: 1
kind: incident
title: "eMudhra: the private keys of eight intermediate CA certificates were trivially recoverable, so anyone could forge trusted HTTPS certificates; browsers block them, clients with their own trust store or no revocation checking need an update (CVE-2026-111943 in Go)"
headline: "Eight eMudhra CA keys were guessable; Java needs a second update, and Python, Go, Rust and curl stacks need theirs"
summary: >
  On 2026-10-17 a researcher reported that the private keys of eight eMudhra intermediate CA certificates had been generated with
  too little randomness, so anyone could recover them and forge trusted HTTPS certificates for any site. Firefox, Chrome, Apple
  and Microsoft platforms block the intermediates and eMudhra revoked them, but software that keeps its own trust store or does not
  check revocation stays exposed until updated: Go fixed it in 1.27.3 and 1.26.10 as CVE-2026-111943, Python added a built-in
  denylist as CVE-2026-115557, and Oracle and OpenJDK's Java update of 2026-10-21 (CVE-2026-91403) was followed on 2026-10-24 by a
  second alert, CVE-2026-114820 (CVSS 3.1 9.1), that removes four root CAs and that OpenJDK says even a runtime updated in the past
  few days needs. Chrome removes the emSign ECC Root CA - G3 root on 2026-10-27; no exploitation is reported.
discovered_at: "2026-10-21T03:43:00Z"
updated_at: "2026-10-25T03:36:20Z"
event_date: "2026-10-20"
run_id: 2026-10-21T0256Z-intel
priority: notable
immediate_action: null
tags: [supply-chain, patch-available]
regions: [global]
sectors: []
entities: ["incident:emudhra-intermediate-ca-key-compromise-2026-10", "product:oracle-java-se", "product:oracle-graalvm-for-jdk", "product:openjdk", "product:cpython", "product:cisco-secure-firewall-management-center", "product:cisco-duo-access-gateway", "product:cisco-duo-network-gateway", "product:cisco-thousandeyes-enterprise-agent", "product:cisco-ios-xr-software"]
techniques: [T1557]
affected_products: ["Oracle Java SE", "Oracle GraalVM for JDK", "OpenJDK", "CPython", "Cisco Secure Firewall Management Center", "Cisco Duo Access Gateway", "Cisco Duo Network Gateway", "Cisco ThousandEyes Enterprise Agent", "Cisco IOS XR Software"]
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
    affected: "Oracle Java SE 8u511-b32, 8u511-perf-b32, 11.0.33.0.2, 17.0.21.0.2, 21.0.13.0.2, 25.0.5.0.2, 27.0.1.0.2; Oracle GraalVM for JDK 17.0.21.0.2 and 21.0.13.0.2; Oracle GraalVM Enterprise Edition 21.3.20.0.2; OpenJDK 27.0.1.0.2, 25.0.5.0.2, 21.0.13.0.2, 17.0.21.0.2, 11.0.32.1, 8u504 and earlier"
    fixed: "the Java updates of Oracle's Security Alert CVE-2026-114820 (build numbers in Oracle's Patch Availability Document) and the OpenJDK update whose release note names JDK-8395690; until updated, delete the cacerts aliases emsignrootcag1, emsignrootcag2, emsigneccrootcag3 and comodoaaaca or enable revocation checking"
  - id: CVE-2026-115557
    cvss: "9.4 (CVSS 4.0)"
    epss: null
    type: logic-flaw
    vector: user-interaction
    auth: pre-auth
    status: [mitigation-only]
    affected: "CPython before 3.16.0 per ENISA's record"
    fixed: "the announcement of 2026-10-24 names no release carrying the ssl denylist; the incident tracker lists Python 3.15.1, 3.14.9 and 3.13.17 and pip 26.2.2 as patched, and Christian Heimes says in the announcement thread that pip before 26.2.2 keeps trusting the compromised intermediates whatever the system trust store holds"
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
  - quote: "This Security Alert addresses CVE-2026-114820 by providing Java updates which removes the set of impacted root CA certificates related to eMudhra."
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
verification: multi-source
sourcing_note: >
  The Chrome Root Program and Mozilla describe their own handling, the incident tracker is maintained by a Mozilla
  cryptography engineer, and the weak-key cause and eMudhra's explanation come through BleepingComputer's account of
  Mozilla's incident report. Google counts eight subordinate CAs and six TLS intermediates, and Microsoft's block date
  rests on the tracker alone.
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
  - "Update every non-browser TLS client that keeps its own CA bundle or does not check revocation, starting with standalone Java runtimes, including those already updated on 2026-10-21 (Oracle's Security Alert CVE-2026-114820 or the OpenJDK update), pip 26.2.2 or later in every Python environment, Go 1.27.3 or 1.26.10, and the CA bundles and base images the incident tracker lists, rebuild container images that embed an older bundle, then confirm with curl against the tracker's test host that the client rejects the certificate."
  - "Replace before 2026-10-27 every TLS certificate your organisation holds that chains to emSign ECC Root CA - G3, by hand where the ACME client does not support ACME Renewal Information, because standard ACME clients do not replace a certificate outside its renewal window."
  - "Apply Cisco's remediation for the products its eMudhra advisory lists as impacted: a TLS policy on Secure Firewall Management Center that blocks the known eMudhra issuers, Duo Access Gateway 3.2.0, Duo Network Gateway 3.4.1, Duo Agentic Authorization Connector 1.0.1 and ThousandEyes Enterprise Agent (Application-hosting Agent 5.2.2) now, and Meraki MV Smart Camera Firmware (2026-11-18), IOS XR 26.4.1 (2026-11-30) and Ultra Cloud Core Subscriber Microservices Infrastructure 2026.04.1 (November 2026) when they ship; other Cisco products are still under investigation."
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
migrated_from: null
---

On 2026-10-17 a researcher reported to the Chrome Root Program, and Mozilla received a report the same day, that the private keys of eight eMudhra subordinate CA certificates were compromised: the keys were generated with insufficient randomness, which lets anyone forge trusted HTTPS certificates to impersonate any website against clients that have not removed trust in those CAs ([Google, 2026-10-20](https://blog.google/security/protecting-chrome-and-android-users-from-compromised-emudhra-intermediate-ca-certificates/); [Mozilla, 2026-10-20](https://blog.mozilla.org/security/2026/10/20/protecting-firefox-users-following-the-compromise-of-emudhra-intermediate-certificates/)). BleepingComputer, citing Mozilla's incident report, says all eight were P-384 keys generated in April 2025 with values below 256, so testing 256 numbers recovers a key, and that eMudhra blames a key-generation script error and found no evidence of end-user certificates ([BleepingComputer, 2026-10-20](https://www.bleepingcomputer.com/news/security/mozilla-google-apple-block-compromised-emudhra-ca-certificates/)). Google reports that no certificates chaining to the six TLS intermediates were logged to Certificate Transparency before it blocked them, so CT-enforcing clients such as Chrome could not have been attacked ([Google, 2026-10-20](https://blog.google/security/protecting-chrome-and-android-users-from-compromised-emudhra-intermediate-ca-certificates/)); the tracker adds that many clients outside browsers do not enforce CT and that it is not known whether attackers used the flaw against them ([Dennis Jackson, 2026-10-20](https://emudhra.we-have-a-problem.com/)).

Chrome blocked the intermediates on 2026-10-17, Firefox through OneCRL the same day, Microsoft platforms on 2026-10-20 and Apple devices on 2026-10-22, and eMudhra revoked all eight ([Dennis Jackson, 2026-10-20](https://emudhra.we-have-a-problem.com/); [BleepingComputer, 2026-10-20](https://www.bleepingcomputer.com/news/security/mozilla-google-apple-block-compromised-emudhra-ca-certificates/)). Google removed the root that signed them, emSign ECC Root CA - G3, from the Chrome Root Store, with the removal expected to reach devices on 2026-10-27, after which some legitimate certificates chaining to it will stop working in Chrome ([Google, 2026-10-20](https://blog.google/security/protecting-chrome-and-android-users-from-compromised-emudhra-intermediate-ca-certificates/)); Mozilla removes the signing root from NSS 3.131.1 to protect applications that use its trust store without OneCRL ([Mozilla, 2026-10-20](https://blog.mozilla.org/security/2026/10/20/protecting-firefox-users-following-the-compromise-of-emudhra-intermediate-certificates/)). Go 1.27.3 and 1.26.10 filter chains that contain the intermediates in crypto/x509, tracked as CVE-2026-111943 ([Go team, 2026-10-20](https://groups.google.com/g/golang-announce/c/66pojueaQek)).

Standalone OpenJDK runtimes, unlike operating-system packages, carry their own keystore ([OpenJDK, 2026-10-24](https://openjdk.org/emudhra)). Oracle's Security Alert of 2026-10-21 for CVE-2026-91403 (CVSS 3.1 9.1, component JSSE, remotely exploitable without authentication through the component's APIs, for example a web service that supplies data to them) provided Java updates that distrust the impacted eMudhra intermediate CA certificates ([Oracle, 2026-10-21](https://www.oracle.com/security-alerts/alert-cve-2026-91403.html)), and a second Security Alert of 2026-10-24, CVE-2026-114820 (CVSS 3.1 9.1, same component and exposure), provides updates that remove the impacted root CA certificates and lists Oracle Java SE 8u511-b32, 11.0.33.0.2, 17.0.21.0.2, 21.0.13.0.2, 25.0.5.0.2 and 27.0.1.0.2 as affected ([Oracle, 2026-10-24](https://www.oracle.com/security-alerts/alert-cve-2026-114820.html)). The OpenJDK advisory of 2026-10-24 lists 27.0.1.0.2, 25.0.5.0.2, 21.0.13.0.2, 17.0.21.0.2, 11.0.32.1 and 8u504 and earlier as affected ([OpenJDK, 2026-10-24](https://openjdk.org/groups/vulnerability/advisories/2026-10-24)), and OpenJDK's guidance tells users of a standalone runtime to act immediately even if they updated in the past few days, preferably by installing an update whose release note names JDK-8395690 and CVE-2026-114820 ([OpenJDK, 2026-10-24](https://openjdk.org/emudhra)). If no update is available, OpenJDK gives two alternatives: delete the aliases emsignrootcag1, emsignrootcag2, emsigneccrootcag3 and comodoaaaca from the runtime's cacerts keystore and restart it, or enable revocation checking with -Dcom.sun.net.ssl.checkRevocation=true and -Dcom.sun.security.enableCRLDP=true for TLS clients and use jarsigner -verify -revcheck -strict for signed JARs on JDK 17 and later; the step is repeated for every installed runtime ([OpenJDK, 2026-10-24](https://openjdk.org/emudhra)). OpenJDK packages from Arch Linux, Fedora, Gentoo, Oracle Linux and Red Hat Enterprise Linux most likely use the operating system's certificates, so updating those is likely sufficient; Debian and its derivatives, Devuan and Ubuntu among them, need a manual workaround because updating ca-certificates and ca-certificates-java does not refresh the keystore (as superuser, remove /etc/ssl/certs/java/cacerts and run update-ca-certificates --fresh), and the FreeBSD and Homebrew packages need an updated package ([OpenJDK, 2026-10-24](https://openjdk.org/emudhra)). NCSC.ch published an advisory on 2026-10-22 and lists the exploitation status as unknown ([NCSC.ch, 2026-10-22](https://security-hub.ncsc.admin.ch/#/posts/13091)).

**Exposure:** any software that keeps its own CA bundle or does not check revocation keeps trusting the intermediates until updated; the tracker lists fixed versions for Python (3.15.1, 3.14.9 and 3.13.17, and pip 26.2.2), Python certifi, rustls-webpki, the curl CA bundle, the Composer ca-bundle, Erlang certifi and several distributions' ca-certificates packages, shows Node.js, Bun and FreeBSD as fixed, and lists Bottlerocket, Godot, LibreOffice and RHEL 7 as still pending ([Dennis Jackson, 2026-10-20](https://emudhra.we-have-a-problem.com/)). The tracker adds that macOS blocks the intermediates but its built-in curl reads /etc/ssl/cert.pem without a revocation check and the file was not updated ([Dennis Jackson, 2026-10-20](https://emudhra.we-have-a-problem.com/)). A client's state is read with the tracker's test hosts: a certificate error means the client does not trust the intermediates ([Dennis Jackson, 2026-10-20](https://emudhra.we-have-a-problem.com/)).

**Detection:** eMudhra says it found no evidence that the intermediates were used to issue end-user certificates ([BleepingComputer, 2026-10-20](https://www.bleepingcomputer.com/news/security/mozilla-google-apple-block-compromised-emudhra-ca-certificates/)), so a server certificate chain seen in TLS session metadata, proxy or EDR network telemetry that contains one of the eight intermediates or their Sectigo cross-signs, which the tracker lists, is worth treating as a possible forged certificate ([Dennis Jackson, 2026-10-20](https://emudhra.we-have-a-problem.com/)). Google reports that no certificates chaining to the six TLS intermediates were logged to Certificate Transparency before it blocked them, so CT monitoring will not show one ([Google, 2026-10-20](https://blog.google/security/protecting-chrome-and-android-users-from-compromised-emudhra-intermediate-ca-certificates/)).

**Triage:** a site that still chains to emSign ECC Root CA - G3 failing in Chrome after 2026-10-27 is the announced root removal, not an attack ([Google, 2026-10-20](https://blog.google/security/protecting-chrome-and-android-users-from-compromised-emudhra-intermediate-ca-certificates/)).

**Defender takeaway:** update trust bundles and toolchains on every non-browser client, rebuild container images that embed an old bundle, and do not rely on revocation or CT for those clients; website operators with certificates chaining to emSign ECC Root CA - G3 must install a certificate from another hierarchy before 2026-10-27 ([Google, 2026-10-20](https://blog.google/security/protecting-chrome-and-android-users-from-compromised-emudhra-intermediate-ca-certificates/)). A Java runtime already updated on 2026-10-21 needs the update of 2026-10-24 as well ([OpenJDK, 2026-10-24](https://openjdk.org/emudhra)), and an ACME client will not replace a certificate under that root outside its renewal window unless it supports ACME Renewal Information, so trigger the renewal by hand ([The Hacker News, 2026-10-22](https://thehackernews.com/2026/10/emudhra-to-exit-global-ssltls-business.html)).

## Update — 2026-10-23T03:43:28Z

On 2026-10-21 Oracle issued Security Alert CVE-2026-91403 and the OpenJDK project an advisory for the same event, which reaches Java runtimes as well; Oracle says it also applies to sandboxed Java Web Start and applet clients ([Oracle, 2026-10-21](https://www.oracle.com/security-alerts/alert-cve-2026-91403.html)). Affected are Oracle Java SE 8u511, 8u511-perf, 11.0.33, 17.0.21, 21.0.13, 25.0.5 and 27.0.1, GraalVM for JDK 17.0.21 and 21.0.13 and GraalVM Enterprise Edition 21.3.20, and OpenJDK lists 27.0.1, 25.0.5, 21.0.13, 17.0.21, 11.0.32.1 and 8u504 and earlier ([Oracle, 2026-10-21](https://www.oracle.com/security-alerts/alert-cve-2026-91403.html); [OpenJDK, 2026-10-21](https://openjdk.org/groups/vulnerability/advisories/2026-10-21)). Compare the full build string, not the release number, against Oracle's affected list. NCSC.ch's advisory of 2026-10-22 lists the exploitation status as unknown and the OpenJDK guidance as the temporary mitigation ([NCSC.ch, 2026-10-22](https://security-hub.ncsc.admin.ch/#/posts/13091)).

## Update — 2026-10-25T03:36:20Z

Oracle's second Security Alert of 2026-10-24, CVE-2026-114820 (CVSS 3.1 9.1, component JSSE, remotely exploitable without authentication through the component's APIs), provides Java updates that remove the impacted root CA certificates related to eMudhra ([Oracle, 2026-10-24](https://www.oracle.com/security-alerts/alert-cve-2026-114820.html)). Its affected list names Oracle Java SE 8u511-b32, 11.0.33.0.2, 17.0.21.0.2, 21.0.13.0.2, 25.0.5.0.2 and 27.0.1.0.2, and the OpenJDK advisory of the same day lists 27.0.1.0.2, 25.0.5.0.2, 21.0.13.0.2, 17.0.21.0.2, 11.0.32.1 and 8u504 and earlier as affected ([Oracle, 2026-10-24](https://www.oracle.com/security-alerts/alert-cve-2026-114820.html); [OpenJDK, 2026-10-24](https://openjdk.org/groups/vulnerability/advisories/2026-10-24)). OpenJDK tells users of a standalone runtime to act immediately even if they updated in the past few days, by installing an update whose release note names JDK-8395690 and CVE-2026-114820 or, failing that, by deleting the cacerts aliases emsignrootcag1, emsignrootcag2, emsigneccrootcag3 and comodoaaaca or enabling revocation checking ([OpenJDK, 2026-10-24](https://openjdk.org/emudhra)). The same page now says Debian, Devuan and Ubuntu OpenJDK packages need the keystore recreated by hand, because updating ca-certificates and ca-certificates-java does not refresh it, which replaces the earlier statement that updating the operating system's certificates suffices there ([OpenJDK, 2026-10-24](https://openjdk.org/emudhra)).

The Python Software Foundation announced CVE-2026-115557 on 2026-10-24: the ssl module now carries a denylist of known compromised certificates that is rejected whatever the SSLContext policy, so it works without revocation checking ([Python Software Foundation, 2026-10-24](https://mail.python.org/archives/list/security-announce@python.org/thread/FNAJMZV6XQYLVPABNINDMF3VF66AYLW4/)). ENISA's record scores it 9.4 (CVSS 4.0) and lists CPython before 3.16.0 as affected, and the announcement names no release that carries the denylist ([ENISA EUVD, 2026-10-24](https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-109299)). The incident tracker lists Python 3.15.1, 3.14.9 and 3.13.17 and pip 26.2.2 as patched, and Christian Heimes stresses in the announcement thread that pip before 26.2.2 keeps trusting the compromised intermediates whatever the system trust store holds, because it always loads its own vendored certifi ([Dennis Jackson, 2026-10-20](https://emudhra.we-have-a-problem.com/); [Python Discourse, 2026-10-20](https://discuss.python.org/t/information-for-python-users-regarding-emudhra-emsign-ca-certificate-security-incident/109576)).

Cisco's informational advisory, version 1.1 of 2026-10-24, lists as impacted with remediation a TLS policy that blocks the known eMudhra issuers on Secure Firewall Management Center, Duo Access Gateway 3.2.0, Duo Network Gateway 3.4.1, Duo Agentic Authorization Connector 1.0.1, ThousandEyes Enterprise Agent (Application-hosting Agent 5.2.2, 2026-10-23), Meraki MV Smart Camera Firmware (2026-11-18), IOS XR 26.4.1 (2026-11-30) and Ultra Cloud Core Subscriber Microservices Infrastructure 2026.04.1 (November 2026), keeps further products under investigation, and says Cisco PSIRT is not aware of malicious use ([Cisco PSIRT, 2026-10-24](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-emudhra-info-ScS22A1r)).

eMudhra's board decided on 2026-10-22 to leave the global SSL/TLS certificate business, and its G1 RSA roots keep serving customers during the transition ([eMudhra, 2026-10-22](https://emudhra.com/en/press-release/emudhra-to-exit-global-ssl-tls-certificate-business)). The Hacker News relays Chrome's count of about 30,800 unexpired certificates under the emSign ECC Root CA - G3, which Chrome stops trusting on 2026-10-27, as of 2026-10-21, 99.9 percent of them issued through InCommon, and relays Chrome's point that standard ACME clients do not replace a certificate outside its renewal window unless they support ACME Renewal Information or someone steps in by hand ([The Hacker News, 2026-10-22](https://thehackernews.com/2026/10/emudhra-to-exit-global-ssltls-business.html)).
