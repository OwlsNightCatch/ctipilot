---
schema: 1
kind: vulnerability
title: "CVE-2026-109618 / CVE-2026-109619, Check Point Force, Spark and Cloud firewalls: the PHP2Shell flaws reach the web interfaces of gateways that run Mobile Access, SSL Network Extender, SAML-realm VPN, the Identity Awareness captive portal, UserCheck or Zero Phishing; hotfixes since 2026-10-23, the R81.20 package reissued on 2026-10-28 (CVSS 9.2)"
headline: "Check Point: PHP2Shell hits gateway VPN and portal web interfaces; hotfixes out, R81.20 package reissued 28 October"
summary: >
  Check Point's advisory sk1000302, last modified 2026-10-29, says the PHP flaws CVE-2026-109618 and CVE-2026-109619 (CVSS 9.2 each) can give remote code execution through the web interfaces of
  Force, Spark and Cloud firewalls that use Mobile Access, SSL Network Extender VPN, SAML-realm VPN authentication, the Identity Awareness captive portal, the UserCheck portal or Zero Phishing.
  Hotfixes exist for R81.20, R82, R82.10 and R82.20 and for Spark R82.00 and R81.10; the R81.20 package was reissued on 2026-10-28 for gateways that use Mobile Access, and a hotfix for the end-of-support gateway release R81.10 followed on 2026-10-29. The sk makes no statement on exploitation of Check Point products,
  and CISA lists both flaws as exploited.
discovered_at: "2026-10-29T04:48:00Z"
updated_at: "2026-10-30T03:54:02Z"
event_date: "2026-10-28"
run_id: 2026-10-29T0255Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, rce, pre-auth, cisa-kev, patch-available]
regions: [global]
sectors: []
entities: ["tool:php2shell", "product:php", "product:check-point-security-gateway", "product:check-point-force-firewalls", "product:check-point-cloud-firewall", "product:check-point-spark-firewall"]
techniques: [T1190]
affected_products: ["Check Point Force Firewalls", "Check Point Spark Firewalls", "Check Point Cloud Firewall"]
cves:
  - id: CVE-2026-109618
    cvss: "9.2 (Check Point)"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [cisa-kev, patch-available]
    affected: "Force, Spark and Cloud firewalls on R81.20, R82, R82.10 and R82.20 (R80 to R81.10 are end of support) and Spark R81.10.x and R82.00.x, with Mobile Access Portal, Remote Access VPN with SSL Network Extender, SAML-realm VPN, Identity Awareness Captive Portal, UserCheck Portal or Zero Phishing in use"
    fixed: "release-specific hotfix packages, also planned for the Jumbo Hotfix Accumulators of 2026-11-11; Spark R82.00.11 (build 998002823) and R81.10.17 (build 996004992); a hotfix for the R81.10 gateway release, published 2026-10-29"
  - id: CVE-2026-109619
    cvss: "9.2 (Check Point)"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [cisa-kev, patch-available]
    affected: "Force, Spark and Cloud firewalls on R81.20, R82, R82.10 and R82.20 (R80 to R81.10 are end of support) and Spark R81.10.x and R82.00.x, with Mobile Access Portal, Remote Access VPN with SSL Network Extender, SAML-realm VPN, Identity Awareness Captive Portal, UserCheck Portal or Zero Phishing in use"
    fixed: "release-specific hotfix packages, also planned for the Jumbo Hotfix Accumulators of 2026-11-11; Spark R82.00.11 (build 998002823) and R81.10.17 (build 996004992); a hotfix for the R81.10 gateway release, published 2026-10-29"
sources:
  - url: "https://support.checkpoint.com/results/sk/sk1000302"
    publisher: "Check Point (sk1000302)"
    date: "2026-10-28"
    role: primary
  - url: "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    publisher: "CISA Known Exploited Vulnerabilities catalog"
    date: "2026-10-28"
    role: corroborating
  - url: "https://support.checkpoint.com/results/sk/sk1000302"
    publisher: "Check Point (sk1000302, hotfix note of 2026-10-29)"
    date: "2026-10-29"
    role: primary
closed_sources: []
evidence:
  - quote: "Under certain circumstances, PHP vulnerabilities may allow Remote Code Execution through firewall web interfaces."
    publisher: "Check Point (sk1000302)"
    source_url: "https://support.checkpoint.com/results/sk/sk1000302"
  - quote: "Check Point products are not vulnerable to CVE-2026-115560."
    publisher: "Check Point (sk1000302)"
    source_url: "https://support.checkpoint.com/results/sk/sk1000302"
  - quote: "This Hotfix implements the PHP 7.4 published fix for CVE-2026-109618 and CVE-2026-109619."
    publisher: "Check Point (sk1000302)"
    source_url: "https://support.checkpoint.com/results/sk/sk1000302"
  - quote: "Released Hotfix for R81.10"
    publisher: "Check Point (sk1000302, hotfix note of 2026-10-29)"
    source_url: "https://support.checkpoint.com/results/sk/sk1000302"
verification: single-source
sourcing_note: >
  Check Point is the disclosing party for its own products and sk1000302, a page its support site renders from a data feed, is the only source for the affected features, versions, hotfixes and the
  interim mitigation; the page carries no exploitation statement and no post-compromise check, and the CISA listing of both flaws concerns PHP generally, not Check Point gateways. NCSC-NL's status list
  gives 2026-11-11 for the Jumbo fix, which the sk also calls planned, and the sk's hotfix section adds the hotfixes available since 2026-10-23.
confidence: high
references: ["2026-10-21/php-critical-release-pre-announced-cve-2026-109618-109619", "2026-10-22/pan-os-panorama-php2shell-mgmt-interface-no-fixed-release", "2026-10-23/netscaler-php2shell-management-gui-fixes-2026-10-27", "2026-10-25/qnap-synology-php2shell-qts-quts-hero-fixed-others-unfixed", "2026-10-27/php2shell-ot-products-netmodule-nrsw-no-fix-macmon-schneider", "2026-10-28/cisco-php2shell-expressway-urwb-duo-access-gateway-fixes", "2026-10-28/hpe-clearpass-php2shell-hotfixes-hpesbnw05171", "2026-05-15/cve-2026-46300-linux-kernel-local-privilege-escalation-via-x", "2026-10-27/camping-care-tcs-camping-data-theft-php-flaw-whatsapp-fraud", "2026-10-29/f5-big-ip-php2shell-k000163821-critical-releases", "2026-10-29/php2shell-trend-micro-apex-quest-kace-netapp-ontap"]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Install the Check Point hotfix for your release on every gateway, cluster member and security-group member that uses Mobile Access, SSL Network Extender, SAML-realm VPN, the Identity Awareness captive portal, UserCheck or Zero Phishing, put the R81.20 package of 2026-10-28 on Jumbo Hotfix Accumulator take 166 or later wherever Mobile Access is used, and until the hotfix is in apply Check Point's cp-httpd.conf mitigation, which you remove before installing it."
updates:
  - at: "2026-10-30T03:54:02Z"
    run_id: 2026-10-30T0255Z-intel
    type: update
    summary: >
      Check Point's sk1000302 now notes a hotfix for the end-of-support R81.10 gateway release, published
      on 2026-10-29 at 11:30 GMT; the entry recorded hotfixes only for R81.20, R82, R82.10, R82.20 and
      Spark. The summary, the CVE records and the hotfix paragraph name it.
    fields: [body, cves, evidence, sources, summary]
migrated_from: null
---

Check Point's advisory sk1000302, created on 2026-10-21 and last modified on 2026-10-29, says that under certain circumstances the PHP flaws CVE-2026-109618 and CVE-2026-109619, both scored CVSS 9.2, may allow remote code execution through firewall web interfaces ([Check Point, 2026-10-29](https://support.checkpoint.com/results/sk/sk1000302)). Affected are Force, Spark and Cloud firewalls that use one or more of Mobile Access Portal (not Spark), Remote Access VPN with SSL Network Extender (not Spark), Remote Access VPN with SAML realm authentication, the Identity Awareness captive portal, the UserCheck portal and Zero Phishing, on R81.20, R82, R82.10 and R82.20 and on Spark R81.10.x and R82.00.x; R80 to R81.10 and the older Spark lines are end of support and also listed ([Check Point, 2026-10-29](https://support.checkpoint.com/results/sk/sk1000302)). Check Point's portal and SaaS services are already patched, Security Management and Log Servers are not affected, and its products are not vulnerable to the third PHP issue, CVE-2026-115560 ([Check Point, 2026-10-29](https://support.checkpoint.com/results/sk/sk1000302)).

The hotfix, first published on 2026-10-23, implements the PHP 7.4 fix, is compatible with every Jumbo Hotfix Accumulator take, goes on each gateway, cluster member, security-group member or standalone server and needs a reboot; the R82, R82.10 and R82.20 packages were reissued on 2026-10-26 to support standalone deployments, and the R81.20 package was reissued on 2026-10-28 to fix a Mobile Access problem, must sit on take 166 or higher and is required where the Mobile Access Portal is used ([Check Point, 2026-10-29](https://support.checkpoint.com/results/sk/sk1000302)). For the gateway packages the fix is also planned for the Jumbo Hotfix Accumulators of 2026-11-11, and Spark has R82.00.11 (build 998002823) and R81.10.17 (build 996004992) ([Check Point, 2026-10-29](https://support.checkpoint.com/results/sk/sk1000302)); a hotfix for the end-of-support R81.10 gateway release was published on 2026-10-29 at 11:30 GMT ([Check Point, 2026-10-29](https://support.checkpoint.com/results/sk/sk1000302)). Until a hotfix is installed, Check Point's mitigation is a block in cp-httpd.conf that denies requests with a multipart Content-Type, followed by a restart of the portals, which is removed before installing the hotfix; R82.20 gateways are also protected by the "PHP Remote Code Execution" IPS signature even when IPS is not enabled ([Check Point, 2026-10-29](https://support.checkpoint.com/results/sk/sk1000302)). CISA lists both PHP flaws as exploited since 2026-10-26, and the sk makes no statement on exploitation of Check Point gateways ([CISA KEV, 2026-10-28](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)).

**Exposure:** a gateway on a listed release with at least one of the six portal or VPN features in use; a gateway with none of them is outside the scope Check Point states ([Check Point, 2026-10-29](https://support.checkpoint.com/results/sk/sk1000302)).

**Detection:** Check Point publishes no indicator and no post-compromise check. The web daemon's access logs for the portal paths, shells or downloads started by the gateway's web process, and outbound connections that the gateway itself initiates are the telemetry to review on a gateway that faced the internet before the fix; this is an inference, since the sk does not describe the attack.

**Defender takeaway:** install the hotfix on every gateway that publishes a portal or VPN; where it has to wait, apply the cp-httpd.conf mitigation, and treat a gateway that was exposed and unpatched as needing a compromise check, because Check Point's page does not say whether patching removes a foothold.

## Update — 2026-10-30T03:54:02Z

Check Point's sk1000302 carries a new note of 2026-10-29 at 11:30 GMT, "Released Hotfix for R81.10" ([Check Point, 2026-10-29](https://support.checkpoint.com/results/sk/sk1000302)). R81.10 is an end-of-support gateway release that the sk still lists as affected, so a gateway on it now has a hotfix to install. The other hotfixes and the exploitation statement are unchanged.
