---
schema: 1
kind: incident
title: "eMudhra: the private keys of eight intermediate CA certificates were trivially recoverable, so anyone could forge trusted HTTPS certificates; browsers block them, clients with their own trust store or no revocation checking need an update (CVE-2026-111943 in Go)"
headline: "Eight eMudhra CA keys were guessable; browsers are protected, Go, Java, Python, Rust and curl stacks need updates"
summary: >
  On 2026-10-17 a researcher reported that the private keys of eight eMudhra intermediate CA certificates had been generated with
  too little randomness, so anyone could recover them and forge trusted HTTPS certificates for any site. Firefox, Chrome, Apple
  and Microsoft platforms now block the intermediates and eMudhra revoked them, but software that keeps its own trust store or
  does not check revocation stays exposed until updated; Go fixed it in 1.27.3 and 1.26.10 as CVE-2026-111943, Oracle and OpenJDK
  shipped a Java distrust update on 2026-10-21 as CVE-2026-91403 (CVSS 3.1 9.1), and Chrome removes the emSign ECC Root CA - G3 root
  on 2026-10-27. No exploitation is reported.
discovered_at: "2026-10-21T03:43:00Z"
updated_at: "2026-10-23T03:43:28Z"
event_date: "2026-10-20"
run_id: 2026-10-21T0256Z-intel
priority: notable
immediate_action: null
tags: [supply-chain, patch-available]
regions: [global]
sectors: []
entities: ["incident:emudhra-intermediate-ca-key-compromise-2026-10", "product:oracle-java-se", "product:oracle-graalvm-for-jdk", "product:openjdk"]
techniques: [T1557]
affected_products: ["Oracle Java SE", "Oracle GraalVM for JDK", "OpenJDK"]
cves:
  - id: CVE-2026-91403
    cvss: "9.1 (CVSS 3.1)"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [patch-available, mitigation-only]
    affected: "Oracle Java SE 8u511, 8u511-perf, 11.0.33, 17.0.21, 21.0.13, 25.0.5, 27.0.1; Oracle GraalVM for JDK 17.0.21 and 21.0.13; Oracle GraalVM Enterprise Edition 21.3.20; OpenJDK 27.0.1, 25.0.5, 21.0.13, 17.0.21, 11.0.32.1, 8u504 and earlier"
    fixed: "the Java updates of Oracle's Security Alert and the OpenJDK advisory of 2026-10-21 (the tracker lists builds 27.0.1.0.2, 25.0.5.0.2, 21.0.13.0.2, 17.0.21.0.2, 11.0.33.0.2 and 8u511); until updated, replace blocked.certs (blacklisted.certs on Java 8) or enable revocation checking"
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
  - quote: "If you use a standalone OpenJDK Java runtime, we recommend that you update it as soon as possible, since it likely contains the compromised certificates."
    publisher: "OpenJDK (Vulnerability Advisory 2026/10/21)"
    source_url: "https://openjdk.org/groups/vulnerability/advisories/2026-10-21"
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
  - "Update the trust store or toolchain of every non-browser TLS client that keeps its own CA bundle or does not check revocation (every standalone Java runtime through Oracle's alert for CVE-2026-91403 or the OpenJDK update, or until then replace its blocked.certs file, blacklisted.certs on Java 8, with the vendor's version or enable revocation checking, while distribution OpenJDK packages need only the updated operating-system certificates; Go 1.27.3 or 1.26.10, Python certifi 2026.10.19, rustls-webpki 0.103.16, webpki-roots 1.0.10, the curl CA bundle of 2026-10-20, the distribution ca-certificates package, container base images) and rebuild images that embed an older bundle, then confirm with curl against the tracker's test host that the client now rejects the certificate; replace before 2026-10-27 every TLS certificate your organisation holds that chains to emSign ECC Root CA - G3."
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
migrated_from: null
---

On 2026-10-17 a researcher reported to the Chrome Root Program, and Mozilla received a report the same day, that the private keys of eight eMudhra subordinate CA certificates were compromised: the keys were generated with insufficient randomness, which lets anyone forge trusted HTTPS certificates to impersonate any website against clients that have not removed trust in those CAs ([Google, 2026-10-20](https://blog.google/security/protecting-chrome-and-android-users-from-compromised-emudhra-intermediate-ca-certificates/); [Mozilla, 2026-10-20](https://blog.mozilla.org/security/2026/10/20/protecting-firefox-users-following-the-compromise-of-emudhra-intermediate-certificates/)). BleepingComputer, citing Mozilla's incident report, says all eight were P-384 keys generated in April 2025 with values below 256, so testing 256 numbers recovers a key, and that eMudhra blames a key-generation script error and found no evidence of end-user certificates ([BleepingComputer, 2026-10-20](https://www.bleepingcomputer.com/news/security/mozilla-google-apple-block-compromised-emudhra-ca-certificates/)). Google reports that no certificates chaining to the six TLS intermediates were logged to Certificate Transparency before it blocked them, so CT-enforcing clients such as Chrome could not have been attacked ([Google, 2026-10-20](https://blog.google/security/protecting-chrome-and-android-users-from-compromised-emudhra-intermediate-ca-certificates/)); the tracker adds that many clients outside browsers do not enforce CT and that it is not known whether attackers used the flaw against them ([Dennis Jackson, 2026-10-20](https://emudhra.we-have-a-problem.com/)).

Chrome blocked the intermediates on 2026-10-17, Firefox through OneCRL the same day, Microsoft platforms on 2026-10-20 and Apple devices on 2026-10-22, and eMudhra revoked all eight ([Dennis Jackson, 2026-10-20](https://emudhra.we-have-a-problem.com/); [BleepingComputer, 2026-10-20](https://www.bleepingcomputer.com/news/security/mozilla-google-apple-block-compromised-emudhra-ca-certificates/)). Google removed the root that signed them, emSign ECC Root CA - G3, from the Chrome Root Store, with the removal expected to reach devices on 2026-10-27, after which some legitimate certificates chaining to it will stop working in Chrome ([Google, 2026-10-20](https://blog.google/security/protecting-chrome-and-android-users-from-compromised-emudhra-intermediate-ca-certificates/)); Mozilla removes the signing root from NSS 3.131.1 to protect applications that use its trust store without OneCRL ([Mozilla, 2026-10-20](https://blog.mozilla.org/security/2026/10/20/protecting-firefox-users-following-the-compromise-of-emudhra-intermediate-certificates/)). Go 1.27.3 and 1.26.10 filter chains that contain the intermediates in crypto/x509, tracked as CVE-2026-111943 ([Go team, 2026-10-20](https://groups.google.com/g/golang-announce/c/66pojueaQek)).

Standalone Java runtimes keep their own trust store ([OpenJDK, 2026-10-21](https://openjdk.org/groups/vulnerability/advisories/2026-10-21)). Oracle's Security Alert of 2026-10-21 for CVE-2026-91403 (CVSS 3.1 9.1, component JSSE, remotely exploitable without authentication through the component's APIs, for example a web service that supplies data to them) provides Java updates that distrust the impacted eMudhra intermediate CA certificates ([Oracle, 2026-10-21](https://www.oracle.com/security-alerts/alert-cve-2026-91403.html)), and the OpenJDK advisory of the same day says a standalone OpenJDK runtime likely contains the compromised certificates and should be updated as soon as possible ([OpenJDK, 2026-10-21](https://openjdk.org/groups/vulnerability/advisories/2026-10-21)). If a runtime cannot be updated, OpenJDK gives two alternatives: replace the runtime's blocked.certs file (blacklisted.certs on Java 8) with the vendor's version, or enable revocation checking with -Dcom.sun.net.ssl.checkRevocation=true and -Dcom.sun.security.enableCRLDP=true for TLS clients, and use jarsigner -verify -revcheck -strict for signed JARs on JDK 17 and later; the step is repeated for every installed runtime ([OpenJDK, 2026-10-21](https://openjdk.org/groups/vulnerability/advisories/2026-10-21)). OpenJDK packages from Arch Linux, Debian, Devuan, Fedora, Gentoo, Oracle Linux, Red Hat Enterprise Linux and Ubuntu use the operating system's certificates, so updating those suffices, which is not true of the FreeBSD and Homebrew packages ([OpenJDK, 2026-10-21](https://openjdk.org/groups/vulnerability/advisories/2026-10-21)). NCSC.ch published an advisory on 2026-10-22 and lists the exploitation status as unknown ([NCSC.ch, 2026-10-22](https://security-hub.ncsc.admin.ch/#/posts/13091)).

**Exposure:** any software that keeps its own CA bundle or does not check revocation keeps trusting the intermediates until updated; the tracker lists fixed versions for Java, Python certifi, rustls-webpki, the curl CA bundle and several distributions' ca-certificates packages, and shows Node.js, Bun and FreeBSD as fixed and the Composer ca-bundle, Erlang certifi, Bottlerocket and Godot as still pending ([Dennis Jackson, 2026-10-20](https://emudhra.we-have-a-problem.com/)). The tracker adds that macOS blocks the intermediates but its built-in curl reads /etc/ssl/cert.pem without a revocation check and the file was not updated ([Dennis Jackson, 2026-10-20](https://emudhra.we-have-a-problem.com/)). A client's state is read with the tracker's test hosts: a certificate error means the client does not trust the intermediates ([Dennis Jackson, 2026-10-20](https://emudhra.we-have-a-problem.com/)).

**Detection:** eMudhra says it found no evidence that the intermediates were used to issue end-user certificates ([BleepingComputer, 2026-10-20](https://www.bleepingcomputer.com/news/security/mozilla-google-apple-block-compromised-emudhra-ca-certificates/)), so a server certificate chain seen in TLS session metadata, proxy or EDR network telemetry that contains one of the eight intermediates or their Sectigo cross-signs, which the tracker lists, is worth treating as a possible forged certificate ([Dennis Jackson, 2026-10-20](https://emudhra.we-have-a-problem.com/)). Google reports that no certificates chaining to the six TLS intermediates were logged to Certificate Transparency before it blocked them, so CT monitoring will not show one ([Google, 2026-10-20](https://blog.google/security/protecting-chrome-and-android-users-from-compromised-emudhra-intermediate-ca-certificates/)).

**Triage:** a site that still chains to emSign ECC Root CA - G3 failing in Chrome after 2026-10-27 is the announced root removal, not an attack ([Google, 2026-10-20](https://blog.google/security/protecting-chrome-and-android-users-from-compromised-emudhra-intermediate-ca-certificates/)).

**Defender takeaway:** update trust bundles and toolchains on every non-browser client, rebuild container images that embed an old bundle, and do not rely on revocation or CT for those clients; website operators with certificates chaining to emSign ECC Root CA - G3 must install a certificate from another hierarchy before 2026-10-27 ([Google, 2026-10-20](https://blog.google/security/protecting-chrome-and-android-users-from-compromised-emudhra-intermediate-ca-certificates/)).

## Update — 2026-10-23T03:43:28Z

On 2026-10-21 Oracle issued Security Alert CVE-2026-91403 and the OpenJDK project an advisory for the same event, which reaches Java runtimes as well; Oracle says it also applies to sandboxed Java Web Start and applet clients ([Oracle, 2026-10-21](https://www.oracle.com/security-alerts/alert-cve-2026-91403.html)). Affected are Oracle Java SE 8u511, 8u511-perf, 11.0.33, 17.0.21, 21.0.13, 25.0.5 and 27.0.1, GraalVM for JDK 17.0.21 and 21.0.13 and GraalVM Enterprise Edition 21.3.20, and OpenJDK lists 27.0.1, 25.0.5, 21.0.13, 17.0.21, 11.0.32.1 and 8u504 and earlier ([Oracle, 2026-10-21](https://www.oracle.com/security-alerts/alert-cve-2026-91403.html); [OpenJDK, 2026-10-21](https://openjdk.org/groups/vulnerability/advisories/2026-10-21)). The tracker lists the fixed Java builds as 27.0.1.0.2, 25.0.5.0.2, 21.0.13.0.2, 17.0.21.0.2, 11.0.33.0.2 and 8u511 ([Dennis Jackson, 2026-10-20](https://emudhra.we-have-a-problem.com/)), so compare the full build string, not the release number, against the affected list; the tracker's 8u511 as fixed sits against Oracle's 8u511 as affected, and the sources do not reconcile the two. NCSC.ch's advisory of 2026-10-22 lists the exploitation status as unknown and the OpenJDK guidance as the temporary mitigation ([NCSC.ch, 2026-10-22](https://security-hub.ncsc.admin.ch/#/posts/13091)).
