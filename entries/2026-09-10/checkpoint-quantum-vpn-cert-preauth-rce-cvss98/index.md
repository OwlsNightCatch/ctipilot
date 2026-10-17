---
schema: 1
kind: vulnerability
title: "Check Point Quantum Security Gateway / Management Server / Spark Firewall: two unauthenticated CVSS 9.8 pre-auth RCE flaws in VPN certificate processing (CVE-2026-85103 heap overflow, CVE-2026-85102 improper cert validation)"
headline: "Two pre-auth code-execution flaws sit in the certificate-processing step every VPN negotiation runs before a user ever authenticates"
summary: >
  Check Point published two Critical (CVSS 9.8) advisories for VPN
  certificate-handling flaws discovered internally and reachable before
  authentication completes: CVE-2026-85103, a heap overflow in certificate
  ASN.1 decoding on the Security Gateway, Spark Firewall and every Security
  Management Server, whether or not it runs VPN, and
  CVE-2026-85102, an improper-certificate-validation flaw enabling
  unauthenticated RCE on the Security Gateway and Spark Firewall.
  CVE-2026-85102 is now under confirmed active exploitation against Spark
  Firewall customers globally since 2026-09-12. Check Point's interim
  rule-based mitigation for Site-to-Site and Remote Access VPN does not apply
  to the locally managed Spark Firewall, where patching is the only control.
discovered_at: "2026-09-10T04:45:00Z"
updated_at: "2026-09-29T22:57:23Z"
event_date: "2026-09-07"
run_id: 2026-09-10T0410Z-intel
priority: critical
immediate_action:
  title: "Confirm every Check Point Spark Firewall, Security Gateway and Management Server is patched, then hunt Mobile Access logs for the active exploitation wave"
  action: >
    Check Point confirms active exploitation of CVE-2026-85102 against Spark
    Firewall customers globally since 2026-09-12, three days after the fix
    shipped, via certificate-based Mobile Access logins from anonymization
    infrastructure (VPN services and proxies). Any Spark Firewall, Security
    Gateway or Security Management Server not yet on LivePatch Take 24 / the
    appropriate Jumbo Hotfix Accumulator is exposed now, a management server
    even where VPN is not configured. Review Mobile Access logs for anomalous
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
    affected: "Security Gateway, Spark Firewall and every Security Management Server deployment regardless of configuration, including with VPN unused; R81.20, R82, R82.10, R81.10.x, R82.00.x and end-of-support R80/R80.10/R80.20/R80.30/R80.40/R81/R81.10; R82.20 confirmed not affected"
    fixed: "LivePatch Take 24 (automatic if enabled) or Jumbo Hotfix Accumulator (R82.10 Take 44+, R82 Take 126+, R81.20 Take 166+, R81.10 Take 190+); Spark Firewall R82.00.10 Build 2325+ / R81.10.17 Build 4968+"
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
  - quote: "A heap overflow in the VPN certificate ASN.1 decoding flow may allow an attacker to remotely execute arbitrary code on the Security Management Server and Security Gateway."
    publisher: "Check Point (vendor advisory sk1000118)"
  - quote: "All Security Management Server deployments are vulnerable, regardless of configuration, and require the fix described below."
    publisher: "Check Point (vendor advisory sk1000118)"
  - quote: "Gateways that participate only in encryption communities where authentication is based on a Pre-Shared Key are not vulnerable."
    publisher: "Check Point (vendor advisory sk1000117)"
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
references:
  - "2026-09-23/cve-2026-93616-check-point-security-mgmt-path-traversal"
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Apply LivePatch Take 24 or the appropriate Jumbo Hotfix Accumulator to every Check Point Security Gateway, Security Management Server and Spark Firewall now, including management servers with no VPN configured, which Check Point states are vulnerable regardless of configuration; if the offline LivePatch package was used on R82.10 JHF Take 24 or lower / R82 JHF Take 107 or lower / R81.20 JHF Take 146 or lower, also install the hardened Take 26 — the locally managed Spark Firewall has no workaround short of patching."
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
  - at: "2026-09-29T22:57:23Z"
    run_id: 2026-09-29T2134Z-audit
    type: update
    summary: >
      Check Point revised sk1000118 on 2026-09-18: every Security Management Server deployment is
      vulnerable to CVE-2026-85103 regardless of configuration, including one with VPN not in use, and
      the Spark Firewall is listed as affected. Both advisories now give an interim rule-based
      mitigation for Remote Access VPN as well as Site-to-Site VPN, which the entry had said did not
      exist, and sk1000117 states that Site-to-Site gateways authenticating only with pre-shared keys
      are not vulnerable to CVE-2026-85102. The R81.10 Jumbo Hotfix Take 190 also carries the fix. The
      fix list in the analysis now includes it. The entry points to the separate exploited management
      flaw CVE-2026-93616, whose affected builds include the minimum CVE-2026-85103 fix levels.
    fields: [summary, immediate_action, cves, evidence, actions, references, body]
migrated_from: null
---

Check Point created two Critical-severity advisories on 2026-09-07, disclosed them with the fixes on 2026-09-09 and revised them on 2026-09-18 (sk1000118) and 2026-09-24 (sk1000117), for its VPN certificate-handling code, both triggered during certificate processing before authentication completes and both discovered internally with no external researcher credited ([Check Point, advisory sk1000118, 2026-09-07](https://support.checkpoint.com/results/sk/sk1000118/); [sk1000117, 2026-09-07](https://support.checkpoint.com/results/sk/sk1000117/)). CVE-2026-85103 (CVSS 9.8) is "a heap overflow in the VPN certificate ASN.1 decoding flow" that "may allow an attacker to remotely execute arbitrary code on the Security Management Server and Security Gateway", and Check Point now adds that every Security Management Server deployment is vulnerable regardless of configuration, including one where VPN is not in use ([Check Point, sk1000118](https://support.checkpoint.com/results/sk/sk1000118/)). CVE-2026-85102 (CVSS 9.8, CWE-295 improper certificate validation) is an authentication-bypass-to-RCE in Remote Access and Site-to-Site VPN negotiation: "improper validation of certificate data during VPN negotiation may allow an unauthenticated remote attacker to execute arbitrary code on the Security Gateway" ([Check Point, sk1000117](https://support.checkpoint.com/results/sk/sk1000117/)), reachable against the Security Gateway and Spark Firewall. Affected: R81.20, R82, R82.10, and the end-of-support R80/R80.10/R80.20/R80.30/R80.40/R81/R81.10 lines and their .x builds; R82.20 is confirmed not affected. Both vulnerabilities were discovered internally by Check Point; there were no reports of active exploitation as of the 2026-09-09 disclosure ([Forkast News, 2026-09-09](https://forkast.news/check-point-quantum-vpn-drops-two-cvss-9-8-cves-in-the-same-certificate-path-vpn-infrastructure-joins-the-auth-gap/)), but CVE-2026-85102 is now under confirmed active exploitation (see the Update below) — this is a distinct certificate-processing defect from the June 2026 IKEv1 key-exchange flaw (CVE-2026-50751) already on CISA KEV. Fix is delivered via Check Point LivePatch Take 24 (automatic if enabled) or Jumbo Hotfix Accumulator (R82.10 Take 44+, R82 Take 126+, R81.20 Take 166+, R81.10 Take 190+), plus dedicated Spark Firewall builds (R82.00.10 Build 2325+, R81.10.17 Build 4968+). No workaround exists for the locally-managed Spark Firewall. For a system that cannot take the fix, Check Point's interim mitigation replaces the VPN implied rules with explicit ones: for Site-to-Site VPN, UDP/500 and UDP/4500 allowed only from the specific peer addresses, and for Remote Access VPN, explicit rules for the required services restricted to the client address ranges where that is possible ([Check Point, sk1000117](https://support.checkpoint.com/results/sk/sk1000117/)).

**Defender takeaway:** patching is the real control for both flaws. The interim rules narrow who can reach the VPN service without removing the flaw, they do not exist for the locally managed Spark Firewall, and a Security Management Server needs the fix whether or not it runs VPN, so a device that cannot take the hotfix immediately should be treated as exposed rather than assumed covered by a workaround. With CVE-2026-85102 now under active exploitation (see the Update below), an unpatched Spark Firewall or Security Gateway is a live target, not a theoretical one.

## Update — 2026-09-23T04:37:00Z

CISA added CVE-2026-85102 to its Known Exploited Vulnerabilities catalog on 2026-09-22 ([CISA KEV, catalogue version 2026.09.22](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)), and Check Point's own advisory confirms the reason: "Check Point disclosed the vulnerability and released fixes on September 9, 2026. At the time, we had no evidence of exploitation. We are now observing exploitation attempts against Check Point Spark customers globally" ([Check Point Research, 2026-09-22](https://blog.checkpoint.com/security/security-advisory-action-required-active-exploitation-of-cve-2026-85102-and-a-management-pre-authentication-vulnerability-cve-2026-93616/)). "Starting September 12, 2026, we observed a wave of exploitation attempts against Spark customers. The attempts originated from anonymization infrastructure, including VPN services and proxies" ([Check Point Research, 2026-09-22](https://blog.checkpoint.com/security/security-advisory-action-required-active-exploitation-of-cve-2026-85102-and-a-management-pre-authentication-vulnerability-cve-2026-93616/)) — three days after the 2026-09-09 fix shipped. Check Point's own advisory sk1000117 carries a September 14 update explaining why some already-patched customers remained exposed during that wave: for customers who installed the Offline LivePatch Package while running R82.10 Jumbo Hotfix Take 24 or lower, R82 Jumbo Hotfix Take 107 or lower, or R81.20 Jumbo Hotfix Take 146 or lower, "following additional research, we identified a rare scenario in which customers must install Check Point Live Patch Take 26, which provides enhanced coverage for this CVE" ([Check Point Support, sk1000117, updated 2026-09-14](https://support.checkpoint.com/results/sk/sk1000117)) — a coverage gap in the original fix, closed by a second, hardened LivePatch issued five days after the initial patch and two days after exploitation attempts began. CVE-2026-85103, the companion heap-overflow certificate-decoding flaw, is unaffected by this gap and remains not confirmed exploited. Check Point's own hunting guidance: review logs for anomalous certificate-based Mobile Access logins without limiting the search to the observed certificate subjects, and treat follow-on internal port or service scanning from a logged-in Mobile Access session as second-stage activity warranting investigation.

## Update — 2026-09-29T22:57:23Z

Check Point's revision of sk1000118 on 2026-09-18 widens the population that needs CVE-2026-85103's fix. Its clarification reads: "All Security Management Server deployments are vulnerable, regardless of configuration, and require the fix described below". The flaw does not depend on any management configuration, and a management server is vulnerable even when VPN is neither used nor configured. The advisory now also lists the Spark Firewall among the affected products, and the R81.10 Jumbo Hotfix Accumulator from Take 190 carries the fix ([Check Point, sk1000118, updated 2026-09-18](https://support.checkpoint.com/results/sk/sk1000118/)). A Management Server that was left out of the patch round because it terminates no VPN is therefore in scope.

Both advisories now also give an interim mitigation for Remote Access VPN, which this entry had said did not exist: disable the Remote Access VPN implied rules and create explicit access rules for the services the clients need (UDP/500, UDP/4500, TCP/443 and, where used, TCP/80), limited to the clients' address ranges where possible ([Check Point, sk1000117, updated 2026-09-24](https://support.checkpoint.com/results/sk/sk1000117/)) ([Check Point, sk1000118, updated 2026-09-18](https://support.checkpoint.com/results/sk/sk1000118/)). It is for systems that cannot take the fix, carries the vendor's warning that a wrong rule set breaks connectivity, and does not apply to the locally managed Spark Firewall ([Check Point, sk1000117, updated 2026-09-24](https://support.checkpoint.com/results/sk/sk1000117/)) ([Check Point, sk1000118, updated 2026-09-18](https://support.checkpoint.com/results/sk/sk1000118/)). For CVE-2026-85102, sk1000117 now narrows the Site-to-Site exposure to gateways that use or allow certificate-based authentication. Gateways that participate only in communities authenticating with pre-shared keys are not vulnerable, while a community with dynamic-IP or Large Scale VPN gateways enables certificate authentication ([Check Point, sk1000117, updated 2026-09-24](https://support.checkpoint.com/results/sk/sk1000117/)).

A Management Server brought only to the minimum fix builds is not finished. Check Point lists Security Management at R82.10 Jumbo Hotfix Take 44 or lower, R82 Take 126 or lower, R81.20 Take 166 or lower and R81.10 Take 190 or lower as affected by CVE-2026-93616, a separate pre-authentication management flaw it has seen exploited ([Check Point Research, 2026-09-22](https://blog.checkpoint.com/security/security-advisory-action-required-active-exploitation-of-cve-2026-85102-and-a-management-pre-authentication-vulnerability-cve-2026-93616/)). The highest affected builds are the minimum fix builds listed above, so a server at exactly that level still needs the other flaw's own fix.
