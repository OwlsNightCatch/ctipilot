---
schema: 1
kind: vulnerability
title: "CVE-2026-109593 and CVE-2026-109594, SonicWall GMS 9.5.2 and earlier: an unauthenticated network attacker may read internal GMS files (CVSS 3.1 9.1), and SonicWall says the end-of-life product gets no fix and has no workaround"
headline: "SonicWall GMS 9.5.2 and earlier: unauthenticated file read, no fix will ship; replace with NSM"
summary: >
  SonicWall's advisory SNWLID-2026-0019 of 2026-11-03 says an unauthenticated attacker with network access to SonicWall GMS 9.5.2 and earlier
  may read internal GMS files (CVE-2026-109593, CVSS 3.1 9.1), with a post-authentication SQL injection beside it (CVE-2026-109594, 6.8).
  The product reached end of support on 2026-09-30, so SonicWall releases no fix, names no workaround and urges migration to Network Security
  Manager; the advisory says nothing about exploitation.
discovered_at: "2026-11-05T03:59:00Z"
updated_at: null
event_date: "2026-11-03"
run_id: 2026-11-05T0255Z-intel
priority: routine
immediate_action: null
tags: [vulnerabilities, pre-auth, info-disclosure, no-patch]
regions: [global]
sectors: []
entities: ["product:sonicwall-gms"]
techniques: [T1190, T1005]
affected_products: ["SonicWall GMS"]
cves:
  - id: CVE-2026-109593
    cvss: "9.1"
    epss: null
    type: info-disclosure
    vector: zero-click
    auth: pre-auth
    status: [no-patch]
    affected: "SonicWall GMS Virtual Appliance and Windows, 9.5.2 and earlier versions"
    fixed: "none: the product has reached end of life and SonicWall will release no remediation; no workaround"
  - id: CVE-2026-109594
    cvss: "6.8"
    epss: null
    type: sqli
    vector: zero-click
    auth: post-auth
    status: [no-patch]
    affected: "SonicWall GMS Virtual Appliance and Windows, 9.5.2 and earlier versions"
    fixed: "none: the product has reached end of life and SonicWall will release no remediation; no workaround"
sources:
  - url: "https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0019"
    publisher: "SonicWall PSIRT (SNWLID-2026-0019)"
    date: "2026-11-03"
    role: primary
  - url: "https://www.sonicwall.com/support/product-notification/gms-eol-announcement/250502113335697"
    publisher: "SonicWall (GMS end-of-life announcement)"
    date: "2025-05-05"
    role: corroborating
  - url: "https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0011"
    publisher: "SonicWall PSIRT (SNWLID-2026-0011)"
    date: "2026-08-11"
    role: corroborating
  - url: "https://www.cert.cyber.gouv.fr/avis/CERTFR-2026-AVI-1456/"
    publisher: "CERT-FR (CERTFR-2026-AVI-1456)"
    date: "2026-11-04"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The affected product has reached End-of-Life (EOL). As a result, no remediation or security update will be released for these vulnerabilities."
    publisher: "SonicWall PSIRT (SNWLID-2026-0019)"
    source_url: "https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0019"
  - quote: "An unauthenticated attacker with network access to the SonicWall GMS 9.5.2 and earlier versions may be able to read internal GMS files, potentially exposing sensitive information."
    publisher: "SonicWall PSIRT (SNWLID-2026-0019)"
    source_url: "https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0019"
verification: single-source
sourcing_note: >
  SonicWall's advisory is the first-party source; CERT-FR relays it. The advisory names no file, says nothing about exploitation or a proof of
  concept, and scores availability high although the described impact is a file read, a score reported here as the vendor gives it.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Find every SonicWall GMS instance on 9.5.2 or earlier, Virtual Appliance or Windows, cut its reachability from untrusted networks and schedule its replacement with Network Security Manager, because SonicWall will release no fix and names no workaround."
updates: []
migrated_from: null
---

SonicWall's advisory SNWLID-2026-0019 of 2026-11-03 covers the end-of-life Global Management System: an unauthenticated attacker with network access to GMS 9.5.2 and earlier may be able to read internal GMS files, potentially exposing sensitive information (CVE-2026-109593, CVSS 3.1 9.1), and a post-authentication SQL injection under specific conditions could let an authenticated attacker access or modify data (CVE-2026-109594, 6.8) ([SonicWall, 2026-11-03](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0019)). The advisory lists no workaround and no fixed version, says no remediation or security update will be released because the product has reached end of life, and strongly encourages migration to Network Security Manager ([SonicWall, 2026-11-03](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0019)). End of support was 2026-09-30 ([SonicWall, 2025-05-05](https://www.sonicwall.com/support/product-notification/gms-eol-announcement/250502113335697)), and the previous GMS advisory of 2026-08-11 named 9.5.2 as the fixed build for its flaws, so the last fixed build is itself affected now ([SonicWall, 2026-08-11](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0011)). The advisory does not say which files are exposed or whether anyone exploits the flaw, and CERT-FR relays it ([CERT-FR, 2026-11-04](https://www.cert.cyber.gouv.fr/avis/CERTFR-2026-AVI-1456/)).

**Exposure:** a GMS Virtual Appliance or Windows installation on 9.5.2 or earlier that is reachable from a network the operator does not trust; every such installation is unpatchable ([SonicWall, 2026-11-03](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0019)).

**Defender takeaway:** with no fix and no workaround the levers are reachability and replacement: take any GMS instance off untrusted networks and migrate to Network Security Manager, as SonicWall urges ([SonicWall, 2026-11-03](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0019)).
