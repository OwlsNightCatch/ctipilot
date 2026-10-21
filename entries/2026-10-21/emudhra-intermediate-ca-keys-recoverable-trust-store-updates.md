---
schema: 1
kind: incident
title: "eMudhra: the private keys of eight intermediate CA certificates were trivially recoverable, so anyone could forge trusted HTTPS certificates; browsers block them, clients with their own trust store or no revocation checking need an update (CVE-2026-111943 in Go)"
headline: "Eight eMudhra CA keys were guessable; browsers are protected, Go, Python, Rust and curl stacks need updates"
summary: >
  On 2026-10-17 a researcher reported that the private keys of eight eMudhra intermediate CA certificates had been generated with
  too little randomness, so anyone could recover them and forge trusted HTTPS certificates for any site. Firefox, Chrome, Apple
  and Microsoft platforms now block the intermediates and eMudhra revoked them, but software that keeps its own trust store or
  does not check revocation stays exposed until updated; Go fixed it in 1.27.3 and 1.26.10 as CVE-2026-111943, and Chrome removes
  the emSign ECC Root CA - G3 root on 2026-10-27. No exploitation is reported.
discovered_at: "2026-10-21T03:43:00Z"
updated_at: null
event_date: "2026-10-20"
run_id: 2026-10-21T0256Z-intel
priority: notable
immediate_action: null
tags: [supply-chain, patch-available]
regions: [global]
sectors: []
entities: ["incident:emudhra-intermediate-ca-key-compromise-2026-10"]
techniques: [T1557]
affected_products: []
cves: []
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
  - "Update the trust store or toolchain of every non-browser TLS client that keeps its own CA bundle or does not check revocation (Go 1.27.3 or 1.26.10, Python certifi 2026.10.19, rustls-webpki 0.103.16, webpki-roots 1.0.10, the curl CA bundle of 2026-10-20, the distribution ca-certificates package, container base images) and rebuild images that embed an older bundle, then confirm with curl against the tracker's test host that the client now rejects the certificate; replace before 2026-10-27 every TLS certificate your organisation holds that chains to emSign ECC Root CA - G3."
updates: []
migrated_from: null
---

On 2026-10-17 a researcher reported to the Chrome Root Program, and Mozilla received a report the same day, that the private keys of eight eMudhra subordinate CA certificates were compromised: the keys were generated with insufficient randomness, which lets anyone forge trusted HTTPS certificates to impersonate any website against clients that have not removed trust in those CAs ([Google, 2026-10-20](https://blog.google/security/protecting-chrome-and-android-users-from-compromised-emudhra-intermediate-ca-certificates/); [Mozilla, 2026-10-20](https://blog.mozilla.org/security/2026/10/20/protecting-firefox-users-following-the-compromise-of-emudhra-intermediate-certificates/)). BleepingComputer, citing Mozilla's incident report, says all eight were P-384 keys generated in April 2025 with values below 256, so testing 256 numbers recovers a key, and that eMudhra blames a key-generation script error and found no evidence of end-user certificates ([BleepingComputer, 2026-10-20](https://www.bleepingcomputer.com/news/security/mozilla-google-apple-block-compromised-emudhra-ca-certificates/)). Google reports that no certificates chaining to the six TLS intermediates were logged to Certificate Transparency before it blocked them, so CT-enforcing clients such as Chrome could not have been attacked ([Google, 2026-10-20](https://blog.google/security/protecting-chrome-and-android-users-from-compromised-emudhra-intermediate-ca-certificates/)); the tracker adds that many clients outside browsers do not enforce CT and that it is not known whether attackers used the flaw against them ([Dennis Jackson, 2026-10-20](https://emudhra.we-have-a-problem.com/)).

Chrome blocked the intermediates on 2026-10-17, Firefox through OneCRL the same day, Apple devices on 2026-10-19 and Microsoft platforms on 2026-10-20, and eMudhra revoked all eight ([Dennis Jackson, 2026-10-20](https://emudhra.we-have-a-problem.com/); [BleepingComputer, 2026-10-20](https://www.bleepingcomputer.com/news/security/mozilla-google-apple-block-compromised-emudhra-ca-certificates/)). Google removed the root that signed them, emSign ECC Root CA - G3, from the Chrome Root Store, with the removal expected to reach devices on 2026-10-27, after which some legitimate certificates chaining to it will stop working in Chrome ([Google, 2026-10-20](https://blog.google/security/protecting-chrome-and-android-users-from-compromised-emudhra-intermediate-ca-certificates/)); Mozilla removes the signing root from NSS 3.131.1 to protect applications that use its trust store without OneCRL ([Mozilla, 2026-10-20](https://blog.mozilla.org/security/2026/10/20/protecting-firefox-users-following-the-compromise-of-emudhra-intermediate-certificates/)). Go 1.27.3 and 1.26.10 filter chains that contain the intermediates in crypto/x509, tracked as CVE-2026-111943 ([Go team, 2026-10-20](https://groups.google.com/g/golang-announce/c/66pojueaQek)).

**Exposure:** any software that keeps its own CA bundle or does not check revocation keeps trusting the intermediates until updated; the tracker lists fixed versions for Python certifi, rustls-webpki, the curl CA bundle and several distributions' ca-certificates packages, and shows Node.js, Bun and FreeBSD as pending as of 2026-10-20 ([Dennis Jackson, 2026-10-20](https://emudhra.we-have-a-problem.com/)). The tracker adds that macOS blocks the intermediates but its built-in curl reads /etc/ssl/cert.pem without a revocation check and the file was not updated ([Dennis Jackson, 2026-10-20](https://emudhra.we-have-a-problem.com/)). A client's state is read with the tracker's test hosts: a certificate error means the client does not trust the intermediates ([Dennis Jackson, 2026-10-20](https://emudhra.we-have-a-problem.com/)).

**Detection:** eMudhra says it found no evidence that the intermediates were used to issue end-user certificates ([BleepingComputer, 2026-10-20](https://www.bleepingcomputer.com/news/security/mozilla-google-apple-block-compromised-emudhra-ca-certificates/)), so a server certificate chain seen in TLS session metadata, proxy or EDR network telemetry that contains one of the eight intermediates or their Sectigo cross-signs, which the tracker lists, is worth treating as a possible forged certificate ([Dennis Jackson, 2026-10-20](https://emudhra.we-have-a-problem.com/)). Google reports that no certificates chaining to the six TLS intermediates were logged to Certificate Transparency before it blocked them, so CT monitoring will not show one ([Google, 2026-10-20](https://blog.google/security/protecting-chrome-and-android-users-from-compromised-emudhra-intermediate-ca-certificates/)).

**Triage:** a site that still chains to emSign ECC Root CA - G3 failing in Chrome after 2026-10-27 is the announced root removal, not an attack ([Google, 2026-10-20](https://blog.google/security/protecting-chrome-and-android-users-from-compromised-emudhra-intermediate-ca-certificates/)).

**Defender takeaway:** update trust bundles and toolchains on every non-browser client, rebuild container images that embed an old bundle, and do not rely on revocation or CT for those clients; website operators with certificates chaining to emSign ECC Root CA - G3 must install a certificate from another hierarchy before 2026-10-27 ([Google, 2026-10-20](https://blog.google/security/protecting-chrome-and-android-users-from-compromised-emudhra-intermediate-ca-certificates/)).
