---
schema: 1
kind: vulnerability
horizon: operational
title: DNS-resolver patch cluster — Unbound 1.25.1 (11 CVEs) and ISC BIND 9.18.49 / 9.20.23
headline: DNS-resolver patch cluster — Unbound 1.25.1 (11 CVEs) and ISC BIND 9.18.49 / 9.20.23
summary: "A DNS-resolver patch cluster landed the same week — Unbound 1.25.1 fixes 11 CVEs including a CVSS 9.8 pre-auth DNSSEC use-after-free (CVE-2026-33278), and ISC BIND 9.18.49/9.20.23 fix a DoH use-after-free (CVE-2026-3593) and a single-query DoS (CVE-2026-5946). No exploitation reported; patch recursive infrastructure."
discovered_at: "2026-05-24T05:00:02Z"
event_date: 2026-05-20
run_id: 2026-05-24-f1fd8070
priority: high
immediate_action: null
tags:
  - vulnerabilities
  - pre-auth
  - rce
  - dos
  - patch-available
regions:
  - global
sectors:
  - technology
  - telco
entities: []
cves:
  - id: CVE-2026-33278
    cvss: "9.8"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
  - id: CVE-2026-42944
    cvss: "7.5"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
  - id: CVE-2026-3593
    cvss: "7.4"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
  - id: CVE-2026-5946
    cvss: "7.5"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
sources:
  - url: "https://nlnetlabs.nl/news/2026/May/20/unbound-1.25.1-released/"
    publisher: "NLnet Labs — Unbound 1.25.1 release, 2026-05-20"
    role: primary
  - url: "https://nlnetlabs.nl/downloads/unbound/CVE-2026-33278.txt"
    publisher: "NLnet Labs — CVE-2026-33278 advisory, 2026-05-20"
    role: corroborating
  - url: "https://kb.isc.org/docs/cve-2026-5946"
    publisher: "ISC BIND CVE-2026-5946, 2026-05-20"
    role: corroborating
  - url: "https://kb.isc.org/docs/cve-2026-3593"
    publisher: "ISC BIND CVE-2026-3593, 2026-05-20"
    role: corroborating
  - url: "https://ccb.belgium.be/advisories/warning-nlnet-labs-has-addressed-multiple-vulnerabilities-unbound-dns-resolver-could"
    publisher: "CCB Belgium, 2026-05-20"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-24.md
---

Two of the most widely deployed open-source DNS resolvers shipped coordinated security releases on 2026-05-20. **NLnet Labs Unbound 1.25.1** fixes 11 CVEs; the headline issue is CVE-2026-33278 (CWE-416 use-after-free; CVSS 9.8 per CCB Belgium), where a struct-assignment bug overwrites a destination pointer during deep-copying of DS sub-query structures when NSEC3 budget exhaustion forces a suspend — a remote unauthenticated attacker who controls a DNSSEC-signed domain can crash the daemon or potentially execute code (affected 1.19.1–1.25.0) ([NLnet Labs, 2026-05-20](https://nlnetlabs.nl/downloads/unbound/CVE-2026-33278.txt)). CVE-2026-42944 (heap overflow, CVSS 7.5 per CCB Belgium) is reachable in the default configuration — `answer-cookie` and `pad-responses` are on by default — when a reply encodes multiple NSID / DNS-Cookie / EDNS-Padding options ([CCB Belgium, 2026-05-20](https://ccb.belgium.be/advisories/warning-nlnet-labs-has-addressed-multiple-vulnerabilities-unbound-dns-resolver-could)). **ISC BIND** 9.18.49 / 9.20.23 fix CVE-2026-3593 (CVSS 7.4 use-after-free in the DoH/HTTP-2 path; 9.20.x only, 9.18.x lacks DoH) and CVE-2026-5946 (CVSS 7.5 DoS — a single query bearing a non-Internet CLASS such as CHAOS/HESIOD or an ANY/NONE meta-class crashes `named` in the NOTIFY/UPDATE/recursion paths, affecting the very widely deployed 9.18 branch) ([ISC, 2026-05-20](https://kb.isc.org/docs/cve-2026-5946)).

No in-the-wild exploitation or public PoC is reported for any of these as of the advisories. They earn § 2 placement on the combination of CVSS-9.8 pre-auth memory-safety reach and the ubiquity of these resolvers across EU/CH government, ISP and critical-infrastructure DNS. Detection is limited to crash telemetry — `unbound` / `named` dying with SIGSEGV/SIGABRT in `dnssec_*` or `http_*` / `isc_tls_*` frames, or `named` crashing immediately after a CHAOS/HESIOD/ANY-class query. Patch recursive and authoritative infrastructure to Unbound 1.25.1, BIND 9.18.49 or 9.20.23.


#### CVE Summary Table

| CVE | Product | CVSS | EPSS | KEV | Exploited | Patch | Source |
|---|---|---|---|---|---|---|---|
| CVE-2026-48172 | LiteSpeed User-End cPanel plugin | 10.0 | n/a | No | Yes (ITW) | plugin v2.4.7 / WHM v5.3.1.0 | [LiteSpeed](https://blog.litespeedtech.com/2026/05/21/security-update-for-litespeed-cpanel-plugin/) |
| CVE-2026-33278 | NLnet Labs Unbound | 9.8 | n/a | No | No | Unbound 1.25.1 | [NLnet Labs](https://nlnetlabs.nl/downloads/unbound/CVE-2026-33278.txt) |
| CVE-2026-42944 | NLnet Labs Unbound | 7.5 | n/a | No | No | Unbound 1.25.1 | [NLnet Labs](https://nlnetlabs.nl/downloads/unbound/CVE-2026-42944.txt) |
| CVE-2026-3593 | ISC BIND 9 (DoH) | 7.4 | n/a | No | No | BIND 9.20.23 | [ISC](https://kb.isc.org/docs/cve-2026-3593) |
| CVE-2026-5946 | ISC BIND 9 | 7.5 | n/a | No | No | BIND 9.18.49 / 9.20.23 | [ISC](https://kb.isc.org/docs/cve-2026-5946) |
