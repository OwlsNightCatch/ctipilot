---
schema: 1
kind: vulnerability
title: "Check Point Quantum Security Gateway / Management Server / Spark Firewall: two unauthenticated CVSS 9.8 pre-auth RCE flaws in VPN certificate processing (CVE-2026-85103 heap overflow, CVE-2026-85102 improper cert validation)"
headline: "Two pre-auth code-execution flaws sit in the certificate-processing step every VPN negotiation runs before a user ever authenticates"
summary: >
  Check Point published two Critical (CVSS 9.8) advisories for VPN
  certificate-handling flaws discovered internally and reachable before
  authentication completes: CVE-2026-85103, a heap overflow in certificate
  ASN.1 decoding on the Security Gateway and Management Server, and
  CVE-2026-85102, an improper-certificate-validation flaw enabling
  unauthenticated RCE on the Security Gateway and Spark Firewall. No
  exploitation is reported; no workaround exists for the locally-managed
  Spark Firewall or Remote Access VPN.
discovered_at: "2026-09-10T04:45:00Z"
updated_at: null
event_date: "2026-09-07"
run_id: 2026-09-10T0410Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, rce, pre-auth]
regions: [global]
sectors: [public-sector]
entities: []
techniques: [T1190]
affected_products: ["Check Point Security Gateway", "Check Point Security Management Server", "Check Point Spark Firewall"]
cves:
  - id: CVE-2026-85103
    cvss: "9.8"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "R81.20, R82, R82.10 and end-of-support R80/R80.10/R80.20/R80.30/R80.40/R81/R81.10 lines and their .x builds; R82.20 confirmed not affected"
    fixed: "LivePatch Take 24 (automatic if enabled) or Jumbo Hotfix Accumulator (R82.10 Take 44+, R82 Take 126+, R81.20 Take 166+)"
  - id: CVE-2026-85102
    cvss: "9.8"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "R81.20, R82, R82.10 and end-of-support R80.x/R81.x lines; Spark Firewall"
    fixed: "LivePatch Take 24 / Jumbo HFA; dedicated Spark Firewall builds R82.00.10 Build 2325+ / R81.10.17 Build 4968+"
sources:
  - url: "https://support.checkpoint.com/results/sk/sk1000118/"
    publisher: "Check Point (vendor advisory sk1000118)"
    date: "2026-09-07"
    role: primary
  - url: "https://support.checkpoint.com/results/sk/sk1000117/"
    publisher: "Check Point (vendor advisory sk1000117)"
    date: "2026-09-07"
    role: primary
  - url: "https://forkast.news/check-point-quantum-vpn-drops-two-cvss-9-8-cves-in-the-same-certificate-path-vpn-infrastructure-joins-the-auth-gap/"
    publisher: "Forkast News"
    date: "2026-09-09"
    role: corroborating
closed_sources: []
evidence:
  - quote: "A heap overflow in the VPN certificate ASN.1 decoding flow may allow a remote attacker to remotely execute arbitrary code on the management and Security Gateway."
    publisher: "Check Point (vendor advisory sk1000118)"
  - quote: "Improper validation of certificate data during VPN negotiation may allow an unauthenticated remote attacker to execute arbitrary code on the Security Gateway."
    publisher: "Check Point (vendor advisory sk1000117)"
  - quote: "Both vulnerabilities were discovered internally by Check Point, and there are no reports of active exploitation as of September 9, 2026."
    publisher: "Forkast News"
verification: multi-source
sourcing_note: "Forkast News reports on and distinguishes Check Point's own advisories rather than independently assessing the flaws; credibility reflects a single technical assessor (Check Point, discovered internally) with a second publisher."
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
  - "Apply LivePatch Take 24 or the appropriate Jumbo Hotfix Accumulator to every Check Point Security Gateway, Management Server and Spark Firewall now — no workaround exists for Remote Access VPN or the locally-managed Spark Firewall short of patching."
updates: []
migrated_from: null
---

Check Point published two Critical-severity advisories (last modified 2026-09-09) for its VPN certificate-handling code, both triggered during certificate processing before authentication completes and both discovered internally with no external researcher credited ([Check Point, advisory sk1000118, 2026-09-07](https://support.checkpoint.com/results/sk/sk1000118/); [sk1000117, 2026-09-07](https://support.checkpoint.com/results/sk/sk1000117/)). CVE-2026-85103 (CVSS 9.8) is "a heap overflow in the VPN certificate ASN.1 decoding flow" that "may allow a remote attacker to remotely execute arbitrary code on the management and Security Gateway" ([Check Point, sk1000118](https://support.checkpoint.com/results/sk/sk1000118/)). CVE-2026-85102 (CVSS 9.8, CWE-295 improper certificate validation) is an authentication-bypass-to-RCE in Remote Access and Site-to-Site VPN negotiation: "improper validation of certificate data during VPN negotiation may allow an unauthenticated remote attacker to execute arbitrary code on the Security Gateway" ([Check Point, sk1000117](https://support.checkpoint.com/results/sk/sk1000117/)), reachable against the Security Gateway and Spark Firewall. Affected: R81.20, R82, R82.10, and the end-of-support R80/R80.10/R80.20/R80.30/R80.40/R81/R81.10 lines and their .x builds; R82.20 is confirmed not affected. "Both vulnerabilities were discovered internally by Check Point, and there are no reports of active exploitation as of September 9, 2026" ([Forkast News, 2026-09-09](https://forkast.news/check-point-quantum-vpn-drops-two-cvss-9-8-cves-in-the-same-certificate-path-vpn-infrastructure-joins-the-auth-gap/)) — this is a distinct certificate-processing defect from the June 2026 IKEv1 key-exchange flaw (CVE-2026-50751) already on CISA KEV. Fix is delivered via Check Point LivePatch Take 24 (automatic if enabled) or Jumbo Hotfix Accumulator (R82.10 Take 44+, R82 Take 126+, R81.20 Take 166+), plus dedicated Spark Firewall builds (R82.00.10 Build 2325+, R81.10.17 Build 4968+). No workaround exists for the locally-managed Spark Firewall; for Site-to-Site VPN the only interim mitigation is disabling implied VPN rules and manually restricting UDP/500 and UDP/4500 to specific peer IPs, which does not apply to Remote Access VPN.

**Defender takeaway:** patching is the only control for both flaws — there is no interim mitigation for Remote Access VPN or the Spark Firewall, so gateways that cannot take the hotfix immediately should be treated as exposed rather than assumed covered by a workaround.
