---
schema: 1
kind: vulnerability
title: 'Citrix NetScaler ADC and Gateway: 28 flaws fixed on 2026-11-12, among them CVE-2026-120868 (CVSS 4.0 9.3) in packet processing on every deployment in default configuration, plus an unauthenticated NetScaler Console authentication bypass (CVE-2026-120869); no exploitation reported'
headline: 'NetScaler: 28 flaws fixed, one reaches every default ADC and Gateway; update to 14.1-73.57 or 13.1-64.39'
summary: Cloud Software Group's bulletin CTX697305 of 2026-11-12 fixes 28 flaws in customer-managed NetScaler ADC and Gateway, 9 of them scored CVSS 4.0 9.0 or above; CVE-2026-120868 (9.3) needs no feature or authentication and affects every deployment in default configuration, and CVE-2026-107412 (9.5) reaches Gateway and AAA virtual servers. The fixed builds are 14.1-73.57, 13.1-64.39, 14.1-73.58 FIPS and 13.1-37.293, and bulletin CTX697320 fixes an unauthenticated NetScaler Console authentication bypass in 14.1-74.34; the bulletins describe the impact as unpredictable behaviour or denial of service, offer no workaround and state no exploitation status, while CERT-EU writes that Citrix reports none and no source reports an attack.
discovered_at: '2026-11-13T04:00:00Z'
updated_at: null
event_date: '2026-11-12'
run_id: 2026-11-13T0256Z-intel
priority: high
immediate_action: null
tags:
  - vulnerabilities
  - pre-auth
  - default-config
  - dos
  - patch-available
regions:
  - global
sectors: []
entities:
  - product:citrix-netscaler
  - product:citrix-netscaler-console
techniques:
  - T1190
  - T1499.004
affected_products:
  - Citrix NetScaler ADC
  - Citrix NetScaler Gateway
  - Citrix NetScaler Console
cves:
  - id: CVE-2026-120868
    cvss: 9.3 (CVSS 4.0, bulletin)
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: default-config
    status:
      - patch-available
    affected: before 14.1-73.57, before 13.1-64.39, before 14.1-73.58 FIPS and before 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
    fixed: 14.1-73.57, 13.1-64.39, 14.1-73.58 FIPS and 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
  - id: CVE-2026-107407
    cvss: 9.3 (CVSS 4.0, bulletin)
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
    affected: before 14.1-73.57, before 13.1-64.39, before 14.1-73.58 FIPS and before 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
    fixed: 14.1-73.57, 13.1-64.39, 14.1-73.58 FIPS and 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
  - id: CVE-2026-107408
    cvss: 9.3 (CVSS 4.0, bulletin)
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
    affected: before 14.1-73.57, before 13.1-64.39, before 14.1-73.58 FIPS and before 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
    fixed: 14.1-73.57, 13.1-64.39, 14.1-73.58 FIPS and 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
  - id: CVE-2026-107409
    cvss: 9.3 (CVSS 4.0, bulletin)
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
    affected: before 14.1-73.57, before 13.1-64.39, before 14.1-73.58 FIPS and before 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
    fixed: 14.1-73.57, 13.1-64.39, 14.1-73.58 FIPS and 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
  - id: CVE-2026-107410
    cvss: 9.3 (CVSS 4.0, bulletin)
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
    affected: before 14.1-73.57, before 13.1-64.39, before 14.1-73.58 FIPS and before 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
    fixed: 14.1-73.57, 13.1-64.39, 14.1-73.58 FIPS and 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
  - id: CVE-2026-107411
    cvss: 8.7 (CVSS 4.0, bulletin)
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
    affected: before 14.1-73.57, before 13.1-64.39, before 14.1-73.58 FIPS and before 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
    fixed: 14.1-73.57, 13.1-64.39, 14.1-73.58 FIPS and 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
  - id: CVE-2026-107412
    cvss: 9.5 (CVSS 4.0, bulletin)
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
    affected: before 14.1-73.57, before 13.1-64.39, before 14.1-73.58 FIPS and before 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
    fixed: 14.1-73.57, 13.1-64.39, 14.1-73.58 FIPS and 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
  - id: CVE-2026-107413
    cvss: 8.7 (CVSS 4.0, bulletin)
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
    affected: before 14.1-73.57, before 13.1-64.39, before 14.1-73.58 FIPS and before 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
    fixed: 14.1-73.57, 13.1-64.39, 14.1-73.58 FIPS and 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
  - id: CVE-2026-107414
    cvss: 8.7 (CVSS 4.0, bulletin)
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
    affected: before 14.1-73.57, before 13.1-64.39, before 14.1-73.58 FIPS and before 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
    fixed: 14.1-73.57, 13.1-64.39, 14.1-73.58 FIPS and 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
  - id: CVE-2026-107415
    cvss: 9.3 (CVSS 4.0, bulletin)
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
    affected: before 14.1-73.57, before 13.1-64.39, before 14.1-73.58 FIPS and before 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
    fixed: 14.1-73.57, 13.1-64.39, 14.1-73.58 FIPS and 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
  - id: CVE-2026-111333
    cvss: 6.9 (CVSS 4.0, bulletin)
    epss: null
    type: memory-corruption
    vector: local
    auth: pre-auth
    status:
      - patch-available
    affected: before 14.1-73.57, before 13.1-64.39, before 14.1-73.58 FIPS and before 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
    fixed: 14.1-73.57, 13.1-64.39, 14.1-73.58 FIPS and 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
  - id: CVE-2026-111334
    cvss: 9.3 (CVSS 4.0, bulletin)
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
    affected: before 14.1-73.57, before 13.1-64.39, before 14.1-73.58 FIPS and before 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
    fixed: 14.1-73.57, 13.1-64.39, 14.1-73.58 FIPS and 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
  - id: CVE-2026-111335
    cvss: 6.9 (CVSS 4.0, bulletin)
    epss: null
    type: dos
    vector: local
    auth: pre-auth
    status:
      - patch-available
    affected: before 14.1-73.57, before 13.1-64.39, before 14.1-73.58 FIPS and before 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
    fixed: 14.1-73.57, 13.1-64.39, 14.1-73.58 FIPS and 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
  - id: CVE-2026-111336
    cvss: 8.3 (CVSS 4.0, bulletin)
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
    affected: before 14.1-73.57, before 13.1-64.39, before 14.1-73.58 FIPS and before 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
    fixed: 14.1-73.57, 13.1-64.39, 14.1-73.58 FIPS and 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
  - id: CVE-2026-111337
    cvss: 8.7 (CVSS 4.0, bulletin)
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
    affected: before 14.1-73.57, before 13.1-64.39, before 14.1-73.58 FIPS and before 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
    fixed: 14.1-73.57, 13.1-64.39, 14.1-73.58 FIPS and 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
  - id: CVE-2026-111338
    cvss: 6.9 (CVSS 4.0, bulletin)
    epss: null
    type: info-disclosure
    vector: local
    auth: post-auth
    status:
      - patch-available
    affected: before 14.1-73.57, before 13.1-64.39, before 14.1-73.58 FIPS and before 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
    fixed: 14.1-73.57, 13.1-64.39, 14.1-73.58 FIPS and 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
  - id: CVE-2026-111339
    cvss: 6.9 (CVSS 4.0, bulletin)
    epss: null
    type: memory-corruption
    vector: local
    auth: post-auth
    status:
      - patch-available
    affected: before 14.1-73.57, before 13.1-64.39, before 14.1-73.58 FIPS and before 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
    fixed: 14.1-73.57, 13.1-64.39, 14.1-73.58 FIPS and 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
  - id: CVE-2026-111340
    cvss: 8.7 (CVSS 4.0, bulletin)
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
    affected: before 14.1-73.57, before 13.1-64.39, before 14.1-73.58 FIPS and before 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
    fixed: 14.1-73.57, 13.1-64.39, 14.1-73.58 FIPS and 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
  - id: CVE-2026-111341
    cvss: 8.7 (CVSS 4.0, bulletin)
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
    affected: before 14.1-73.57, before 13.1-64.39, before 14.1-73.58 FIPS and before 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
    fixed: 14.1-73.57, 13.1-64.39, 14.1-73.58 FIPS and 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
  - id: CVE-2026-111342
    cvss: 8.7 (CVSS 4.0, bulletin)
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
    affected: before 14.1-73.57, before 13.1-64.39, before 14.1-73.58 FIPS and before 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
    fixed: 14.1-73.57, 13.1-64.39, 14.1-73.58 FIPS and 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
  - id: CVE-2026-120860
    cvss: 8.7 (CVSS 4.0, bulletin)
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
    affected: before 14.1-73.57, before 13.1-64.39, before 14.1-73.58 FIPS and before 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
    fixed: 14.1-73.57, 13.1-64.39, 14.1-73.58 FIPS and 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
  - id: CVE-2026-120861
    cvss: 8.7 (CVSS 4.0, bulletin)
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
    affected: before 14.1-73.57, before 13.1-64.39, before 14.1-73.58 FIPS and before 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
    fixed: 14.1-73.57, 13.1-64.39, 14.1-73.58 FIPS and 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
  - id: CVE-2026-120862
    cvss: 8.7 (CVSS 4.0, bulletin)
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
    affected: before 14.1-73.57, before 13.1-64.39, before 14.1-73.58 FIPS and before 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
    fixed: 14.1-73.57, 13.1-64.39, 14.1-73.58 FIPS and 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
  - id: CVE-2026-120863
    cvss: 8.7 (CVSS 4.0, bulletin)
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
    affected: before 14.1-73.57, before 13.1-64.39, before 14.1-73.58 FIPS and before 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
    fixed: 14.1-73.57, 13.1-64.39, 14.1-73.58 FIPS and 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
  - id: CVE-2026-120864
    cvss: 9.3 (CVSS 4.0, bulletin)
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
    affected: before 14.1-73.57, before 13.1-64.39, before 14.1-73.58 FIPS and before 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
    fixed: 14.1-73.57, 13.1-64.39, 14.1-73.58 FIPS and 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
  - id: CVE-2026-120865
    cvss: 8.7 (CVSS 4.0, bulletin)
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
    affected: before 14.1-73.57, before 13.1-64.39, before 14.1-73.58 FIPS and before 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
    fixed: 14.1-73.57, 13.1-64.39, 14.1-73.58 FIPS and 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
  - id: CVE-2026-120866
    cvss: 7.7 (CVSS 4.0, bulletin)
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
    affected: before 14.1-73.57, before 13.1-64.39, before 14.1-73.58 FIPS and before 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
    fixed: 14.1-73.57, 13.1-64.39, 14.1-73.58 FIPS and 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
  - id: CVE-2026-120867
    cvss: 8.7 (CVSS 4.0, bulletin)
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
    affected: before 14.1-73.57, before 13.1-64.39, before 14.1-73.58 FIPS and before 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
    fixed: 14.1-73.57, 13.1-64.39, 14.1-73.58 FIPS and 13.1-37.293 (13.1-FIPS and 13.1-NDcPP)
  - id: CVE-2026-120869
    cvss: 9.4 (CVSS 4.0, bulletin, adjacent vector; the CVE record says 9.3 with a network vector)
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
    affected: NetScaler Console before 14.1-74.34
    fixed: NetScaler Console 14.1-74.34
sources:
  - url: https://support.citrix.com/external/article/CTX697305/citrix-netscaler-adc-and-citrix-netscale.html
    publisher: Cloud Software Group (CTX697305)
    date: '2026-11-12'
    role: primary
  - url: https://support.citrix.com/external/article/CTX697320/citrix-netscaler-console-security-bullet.html
    publisher: Cloud Software Group (CTX697320)
    date: '2026-11-12'
    role: primary
  - url: https://cert.europa.eu/publications/security-advisories/2026-020/
    publisher: CERT-EU (advisory 2026-020)
    date: '2026-11-12'
    role: corroborating
  - url: https://security-hub.ncsc.admin.ch/#/posts/13175
    publisher: NCSC Switzerland (Cyber Security Hub post 13175)
    date: '2026-11-12'
    role: corroborating
  - url: https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-124482
    publisher: ENISA EUVD (EUVD-2026-124482)
    date: '2026-11-12'
    role: corroborating
  - url: https://www.heise.de/news/Angreifer-koennen-Citrix-NetScaler-ADC-und-NetScaler-Gateway-lahmlegen-11522940.html
    publisher: heise online
    date: '2026-11-12'
    role: corroborating
closed_sources: []
evidence:
  - quote: All NetScaler ADC and NetScaler Gateway deployments (Default configuration / No additional feature required)
    publisher: Cloud Software Group (CTX697305)
    source_url: https://support.citrix.com/external/article/CTX697305/citrix-netscaler-adc-and-citrix-netscale.html
  - quote: Ten of the flaws are scored as having a high impact on confidentiality, integrity and availability. However, the vendor bulletin describes their impact only as unpredictable behaviour or denial of service
    publisher: CERT-EU (advisory 2026-020)
    source_url: https://cert.europa.eu/publications/security-advisories/2026-020/
  - quote: Internet-facing Gateway and AAA appliances should be upgraded first.
    publisher: CERT-EU (advisory 2026-020)
    source_url: https://cert.europa.eu/publications/security-advisories/2026-020/
verification: multi-source
sourcing_note: The bulletins are the vendor's own and the only source for the per-row scores, preconditions and builds; CERT-EU, NCSC Switzerland and heise restate them. The Console score differs between the bulletin (9.4, adjacent) and Citrix's CVE record and ENISA's record (9.3, network); both are Citrix data. Citrix revised CTX697305 on 2026-11-12 to correct seven mistyped CVE numbers, now CVE-2026-111333 to CVE-2026-111339, and the CVE List held no record for those ids or for CVE-2026-120860 to CVE-2026-120867 when they were checked on 2026-11-13. No source says how a memory overflow could lead beyond a crash.
confidence: high
references:
  - 2026-10-23/netscaler-php2shell-management-gui-fixes-2026-10-27
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - Upgrade every customer-managed NetScaler ADC and Gateway to 14.1-73.57, 13.1-64.39 (14.1-73.58 FIPS; 13.1-37.293 for 13.1-FIPS and 13.1-NDcPP) and the NetScaler Console to 14.1-74.34, internet-facing Gateway and AAA appliances first, because CVE-2026-120868 affects every unpatched appliance in default configuration and neither bulletin offers a workaround; keep the management address (NSIP) and the Console IP off networks that untrusted hosts can reach.
updates: []
migrated_from: null
---

Cloud Software Group's bulletin CTX697305 of 2026-11-12 fixes 28 flaws in customer-managed NetScaler ADC and NetScaler Gateway ([Cloud Software Group, 2026-11-12](https://support.citrix.com/external/article/CTX697305/citrix-netscaler-adc-and-citrix-netscale.html)). The bulletin describes the impact as unpredictable or erroneous behaviour or denial of service, while its CVSS 4.0 vectors score confidentiality, integrity and availability impact High on ten rows, and no source says that code execution is possible ([CERT-EU, 2026-11-12](https://cert.europa.eu/publications/security-advisories/2026-020/)). The row that applies everywhere is CVE-2026-120868 (9.3), a memory overflow in packet processing with the precondition "All NetScaler ADC and NetScaler Gateway deployments (Default configuration / No additional feature required)" and no authentication or user interaction ([Cloud Software Group, 2026-11-12](https://support.citrix.com/external/article/CTX697305/citrix-netscaler-adc-and-citrix-netscale.html)). CVE-2026-107412 (9.5) covers several overflows on an appliance configured as a Gateway (SSL VPN, ICA Proxy, CVPN or RDP Proxy) or an AAA virtual server, which CERT-EU, citing the vendor, says can be reached without authentication ([CERT-EU, 2026-11-12](https://cert.europa.eu/publications/security-advisories/2026-020/)); further rows at 9.3 or 8.7 each depend on one configured feature, such as an SMPP, DNS-over-HTTPS or PUSH virtual server or a SAML, WebAuth, email OTP, certificate or LDAP authentication action, and CVE-2026-120863 needs only a path from an untrusted host to the management address NSIP or NSIP6 ([Cloud Software Group, 2026-11-12](https://support.citrix.com/external/article/CTX697305/citrix-netscaler-adc-and-citrix-netscale.html)). Bulletin CTX697320 fixes CVE-2026-120869, an unauthenticated authentication bypass on the NetScaler Console, scored 9.4 with an adjacent vector in the bulletin ([Cloud Software Group, 2026-11-12](https://support.citrix.com/external/article/CTX697320/citrix-netscaler-console-security-bullet.html)) and 9.3 with a network vector in ENISA's record ([ENISA EUVD, 2026-11-12](https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-124482)).

The fixed builds are 14.1-73.57, 13.1-64.39, 14.1-73.58 FIPS and 13.1-37.293 for 13.1-FIPS and 13.1-NDcPP ([Cloud Software Group, 2026-11-12](https://support.citrix.com/external/article/CTX697305/citrix-netscaler-adc-and-citrix-netscale.html)), and 14.1-74.34 for the Console ([Cloud Software Group, 2026-11-12](https://support.citrix.com/external/article/CTX697320/citrix-netscaler-console-security-bullet.html)); Secure Private Access Hybrid deployments must upgrade their NetScaler instances ([Cloud Software Group, 2026-11-12](https://support.citrix.com/external/article/CTX697305/citrix-netscaler-adc-and-citrix-netscale.html)). Neither bulletin states an exploitation status or a workaround. CERT-EU writes that Citrix reports no exploitation and no confirmed public proof of concept ([CERT-EU, 2026-11-12](https://cert.europa.eu/publications/security-advisories/2026-020/)), NCSC Switzerland lists the exploitation status as unknown ([NCSC Switzerland, 2026-11-12](https://security-hub.ncsc.admin.ch/#/posts/13175)), and none of the CVEs is in CISA's catalog. heise reports that Citrix will publish NetScaler security fixes monthly on a fixed date close to Patch Tuesday from now on, with out-of-cycle updates for urgent cases such as active exploitation ([heise, 2026-11-12](https://www.heise.de/news/Angreifer-koennen-Citrix-NetScaler-ADC-und-NetScaler-Gateway-lahmlegen-11522940.html)).

**Exposure:** every customer-managed NetScaler ADC or Gateway below the fixed build of its branch is in scope for CVE-2026-120868 whatever its configuration; the other rows apply where the named feature is configured, which the bulletin tells you to find with configuration searches such as `add vpn vserver`, `add authentication vserver` or `add authentication samlAction` ([Cloud Software Group, 2026-11-12](https://support.citrix.com/external/article/CTX697305/citrix-netscaler-adc-and-citrix-netscale.html)).

**Detection:** no source states a detection method or a check for compromise. The stated impact is a crash or denial of service, so unexplained packet-engine restarts, core files or reboots after inbound traffic to a Gateway or AAA virtual server are the telemetry to review; this is an inference, not a source statement. Where a logout had occurred, /var/log/httperror.log can hold authentication material (one of the rows), so limit who can read that file ([Cloud Software Group, 2026-11-12](https://support.citrix.com/external/article/CTX697305/citrix-netscaler-adc-and-citrix-netscale.html)).

**Defender takeaway:** upgrade internet-facing Gateway and AAA appliances first, then every other ADC, to the fixed build of the branch, because CVE-2026-120868 needs no feature ([CERT-EU, 2026-11-12](https://cert.europa.eu/publications/security-advisories/2026-020/)) and neither bulletin offers a workaround ([Cloud Software Group, 2026-11-12](https://support.citrix.com/external/article/CTX697305/citrix-netscaler-adc-and-citrix-netscale.html); [Cloud Software Group, 2026-11-12](https://support.citrix.com/external/article/CTX697320/citrix-netscaler-console-security-bullet.html)); keep NSIP and the Console IP on a management network.
