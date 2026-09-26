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
  unauthenticated RCE on the Security Gateway and Spark Firewall.
  CVE-2026-85102 is now under confirmed active exploitation against Spark
  Firewall customers globally since 2026-09-12; no workaround exists for the
  locally-managed Spark Firewall or Remote Access VPN.
discovered_at: "2026-09-10T04:45:00Z"
updated_at: "2026-09-23T04:37:00Z"
event_date: "2026-09-07"
run_id: 2026-09-10T0410Z-intel
priority: critical
immediate_action:
  title: "Confirm every Check Point Spark Firewall and Security Gateway is patched, then hunt Mobile Access logs for the active exploitation wave"
  action: >
    Check Point confirms active exploitation of CVE-2026-85102 against Spark
    Firewall customers globally since 2026-09-12, three days after the fix
    shipped, via certificate-based Mobile Access logins from anonymization
    infrastructure (VPN services and proxies). Any Spark Firewall or Security
    Gateway not yet on LivePatch Take 24 / the appropriate Jumbo Hotfix
    Accumulator is exposed now. Review Mobile Access logs for anomalous
    certificate-based logins and any follow-on internal port/service scanning
    from suspicious Mobile Access sessions, regardless of whether the device
    has already been patched.
tags: [vulnerabilities, rce, pre-auth, actively-exploited, cisa-kev]
regions: [global]
sectors: [public-sector]
entities: ["product:check-point-security-gateway", "product:check-point-security-management-server", "product:check-point-spark-firewall"]
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
    epss: "0.0033"
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev, patch-available]
    affected: "R81.20, R82, R82.10 and end-of-support R80.x/R81.x lines; Spark Firewall"
    fixed: "LivePatch Take 24 / Jumbo HFA; dedicated Spark Firewall builds R82.00.10 Build 2325+ / R81.10.17 Build 4968+ — offline LivePatch installs on R82.10 JHF Take 24 or lower / R82 JHF Take 107 or lower / R81.20 JHF Take 146 or lower need the hardened Take 26 (2026-09-14) for full coverage"
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
  - url: "https://blog.checkpoint.com/security/security-advisory-action-required-active-exploitation-of-cve-2026-85102-and-a-management-pre-authentication-vulnerability-cve-2026-93616/"
    publisher: "Check Point Research (blog)"
    date: "2026-09-22"
    role: primary
  - url: "https://thehackernews.com/2026/09/check-point-warns-of-management-server.html"
    publisher: "The Hacker News"
    date: "2026-09-22"
    role: corroborating
  - url: "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    publisher: "CISA KEV"
    date: "2026-09-22"
    role: corroborating
closed_sources: []
evidence:
  - quote: "A heap overflow in the VPN certificate ASN.1 decoding flow may allow a remote attacker to remotely execute arbitrary code on the management and Security Gateway."
    publisher: "Check Point (vendor advisory sk1000118)"
  - quote: "Improper validation of certificate data during VPN negotiation may allow an unauthenticated remote attacker to execute arbitrary code on the Security Gateway."
    publisher: "Check Point (vendor advisory sk1000117)"
  - quote: "Both vulnerabilities were discovered internally by Check Point, and there are no reports of active exploitation as of September 9, 2026."
    publisher: "Forkast News"
  - quote: "Check Point disclosed the vulnerability and released fixes on September 9, 2026. At the time, we had no evidence of exploitation. We are now observing exploitation attempts against Check Point Spark customers globally."
    publisher: "Check Point Research (blog)"
    source_url: "https://blog.checkpoint.com/security/security-advisory-action-required-active-exploitation-of-cve-2026-85102-and-a-management-pre-authentication-vulnerability-cve-2026-93616/"
  - quote: "Starting September 12, 2026, we observed a wave of exploitation attempts against Spark customers. The attempts originated from anonymization infrastructure, including VPN services and proxies"
    publisher: "Check Point Research (blog)"
    source_url: "https://blog.checkpoint.com/security/security-advisory-action-required-active-exploitation-of-cve-2026-85102-and-a-management-pre-authentication-vulnerability-cve-2026-93616/"
  - quote: "Following additional research, we identified a rare scenario in which customers must install Check Point Live Patch Take 26, which provides enhanced coverage for this CVE."
    publisher: "Check Point (vendor advisory sk1000117)"
    source_url: "https://support.checkpoint.com/results/sk/sk1000117"
verification: multi-source
sourcing_note: "Forkast News reports on and distinguishes Check Point's own advisories rather than independently assessing the flaws; credibility reflects a single technical assessor (Check Point, discovered internally) with a second publisher. The 2026-09-22 exploitation confirmation is Check Point's own telemetry, corroborated by The Hacker News as a second publisher relaying the same advisory."
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
  - "Apply LivePatch Take 24 or the appropriate Jumbo Hotfix Accumulator to every Check Point Security Gateway, Management Server and Spark Firewall now; if the offline LivePatch package was used on R82.10 JHF Take 24 or lower / R82 JHF Take 107 or lower / R81.20 JHF Take 146 or lower, also install the hardened Take 26 — no workaround exists for Remote Access VPN or the locally-managed Spark Firewall short of patching."
  - "Review Mobile Access logs for anomalous certificate-based logins and any follow-on internal port/service scanning from suspicious Mobile Access sessions on every Spark Firewall, whether or not it has already been patched."
updates:
  - at: "2026-09-23T04:37:00Z"
    run_id: 2026-09-23T0405Z-intel
    type: update
    summary: >
      CISA added CVE-2026-85102 to its Known Exploited Vulnerabilities catalog on 2026-09-22, and
      Check Point's own advisory confirms a wave of exploitation attempts against Spark Firewall
      customers globally beginning 2026-09-12, three days after the fix shipped, using
      certificate-based Mobile Access logins from anonymization infrastructure. A September 14
      advisory update also reveals a coverage gap in the original fix affecting offline LivePatch
      installs on specific older hotfix baselines, closed by a second, hardened LivePatch (Take 26)
      issued two days after exploitation began. Exploitation status moves from unexploited to
      confirmed exploited; priority moves from high to critical. CVE-2026-85103 is unaffected and
      remains not confirmed exploited.
    fields: [summary, priority, immediate_action, cves, tags, sources, evidence, actions, sourcing_note, entities, body]
migrated_from: null
---

Check Point published two Critical-severity advisories (last modified 2026-09-09) for its VPN certificate-handling code, both triggered during certificate processing before authentication completes and both discovered internally with no external researcher credited ([Check Point, advisory sk1000118, 2026-09-07](https://support.checkpoint.com/results/sk/sk1000118/); [sk1000117, 2026-09-07](https://support.checkpoint.com/results/sk/sk1000117/)). CVE-2026-85103 (CVSS 9.8) is "a heap overflow in the VPN certificate ASN.1 decoding flow" that "may allow a remote attacker to remotely execute arbitrary code on the management and Security Gateway" ([Check Point, sk1000118](https://support.checkpoint.com/results/sk/sk1000118/)). CVE-2026-85102 (CVSS 9.8, CWE-295 improper certificate validation) is an authentication-bypass-to-RCE in Remote Access and Site-to-Site VPN negotiation: "improper validation of certificate data during VPN negotiation may allow an unauthenticated remote attacker to execute arbitrary code on the Security Gateway" ([Check Point, sk1000117](https://support.checkpoint.com/results/sk/sk1000117/)), reachable against the Security Gateway and Spark Firewall. Affected: R81.20, R82, R82.10, and the end-of-support R80/R80.10/R80.20/R80.30/R80.40/R81/R81.10 lines and their .x builds; R82.20 is confirmed not affected. Both vulnerabilities were discovered internally by Check Point; there were no reports of active exploitation as of the 2026-09-09 disclosure ([Forkast News, 2026-09-09](https://forkast.news/check-point-quantum-vpn-drops-two-cvss-9-8-cves-in-the-same-certificate-path-vpn-infrastructure-joins-the-auth-gap/)), but CVE-2026-85102 is now under confirmed active exploitation (see the Update below) — this is a distinct certificate-processing defect from the June 2026 IKEv1 key-exchange flaw (CVE-2026-50751) already on CISA KEV. Fix is delivered via Check Point LivePatch Take 24 (automatic if enabled) or Jumbo Hotfix Accumulator (R82.10 Take 44+, R82 Take 126+, R81.20 Take 166+), plus dedicated Spark Firewall builds (R82.00.10 Build 2325+, R81.10.17 Build 4968+). No workaround exists for the locally-managed Spark Firewall; for Site-to-Site VPN the only interim mitigation is disabling implied VPN rules and manually restricting UDP/500 and UDP/4500 to specific peer IPs, which does not apply to Remote Access VPN.

**Defender takeaway:** patching is the only control for both flaws — there is no interim mitigation for Remote Access VPN or the Spark Firewall, so gateways that cannot take the hotfix immediately should be treated as exposed rather than assumed covered by a workaround. With CVE-2026-85102 now under active exploitation (see the Update below), an unpatched Spark Firewall or Security Gateway is a live target, not a theoretical one.

## Update — 2026-09-23T04:37:00Z

CISA added CVE-2026-85102 to its Known Exploited Vulnerabilities catalog on 2026-09-22 ([CISA KEV, catalogue version 2026.09.22](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)), and Check Point's own advisory confirms the reason: "Check Point disclosed the vulnerability and released fixes on September 9, 2026. At the time, we had no evidence of exploitation. We are now observing exploitation attempts against Check Point Spark customers globally" ([Check Point Research, 2026-09-22](https://blog.checkpoint.com/security/security-advisory-action-required-active-exploitation-of-cve-2026-85102-and-a-management-pre-authentication-vulnerability-cve-2026-93616/)). "Starting September 12, 2026, we observed a wave of exploitation attempts against Spark customers. The attempts originated from anonymization infrastructure, including VPN services and proxies" ([Check Point Research, 2026-09-22](https://blog.checkpoint.com/security/security-advisory-action-required-active-exploitation-of-cve-2026-85102-and-a-management-pre-authentication-vulnerability-cve-2026-93616/)) — three days after the 2026-09-09 fix shipped. Check Point's own advisory sk1000117 carries a September 14 update explaining why some already-patched customers remained exposed during that wave: for customers who installed the Offline LivePatch Package while running R82.10 Jumbo Hotfix Take 24 or lower, R82 Jumbo Hotfix Take 107 or lower, or R81.20 Jumbo Hotfix Take 146 or lower, "following additional research, we identified a rare scenario in which customers must install Check Point Live Patch Take 26, which provides enhanced coverage for this CVE" ([Check Point Support, sk1000117, updated 2026-09-14](https://support.checkpoint.com/results/sk/sk1000117)) — a coverage gap in the original fix, closed by a second, hardened LivePatch issued five days after the initial patch and two days after exploitation attempts began. CVE-2026-85103, the companion heap-overflow certificate-decoding flaw, is unaffected by this gap and remains not confirmed exploited. Check Point's own hunting guidance: review logs for anomalous certificate-based Mobile Access logins without limiting the search to the observed certificate subjects, and treat follow-on internal port or service scanning from a logged-in Mobile Access session as second-stage activity warranting investigation.
