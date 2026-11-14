---
schema: 1
kind: vulnerability
title: 'CVE-2026-109618 / CVE-2026-109619 and CVE-2026-123039, Check Point Force, Spark and Cloud firewalls: PHP2Shell on the Mobile Access and VPN web interfaces, chained with a local root escalation, is exploited against unpatched gateways (implant, ESXi wiper); the fix is in Jumbo takes R81.20 take 174, R82 take 132, R82.10 take 52 and R82.20 take 14'
headline: 'Check Point gateways exploited (PHP2Shell, root escalation): Jumbo R81.20 t174, R82 t132, R82.10 t52, R82.20 t14'
summary: Check Point Research reports that from 2026-10-30 an attacker exploited unpatched Check Point gateways through the Mobile Access portal with PHP2Shell (CVE-2026-109618 and CVE-2026-109619), escalated to root with CVE-2026-123039 (CVSS 7.8, a local flaw in the dynamic_server process that Check Point says was exploited against a couple of dozen customers), installed a persistent backdoor and in the first wave deleted files on a VMware ESXi host. The fix for both is in Jumbo Hotfix Accumulator R81.20 take 174, R82 take 132, R82.10 take 52 and R82.20 take 14 or later, with none listed for R81.10 or R81, and the standalone PHP hotfix is not stated to cover CVE-2026-123039; sk1000302 itself carries no statement on exploitation.
discovered_at: '2026-10-29T04:48:00Z'
updated_at: '2026-11-13T03:59:06Z'
event_date: '2026-10-28'
run_id: 2026-10-29T0255Z-intel
priority: high
immediate_action: null
tags:
  - vulnerabilities
  - rce
  - pre-auth
  - actively-exploited
  - cisa-kev
  - patch-available
  - priv-esc
regions:
  - global
sectors: []
entities:
  - tool:php2shell
  - product:php
  - product:check-point-security-gateway
  - product:check-point-force-firewalls
  - product:check-point-cloud-firewall
  - product:check-point-spark-firewall
techniques:
  - T1190
  - T1068
  - T1505.003
  - T1055
  - T1090
  - T1046
  - T1021.004
  - T1078
  - T1485
  - T1602.002
  - T1070
affected_products:
  - Check Point Force Firewalls
  - Check Point Spark Firewalls
  - Check Point Cloud Firewall
cves:
  - id: CVE-2026-109618
    cvss: 9.2 (Check Point)
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status:
      - exploited
      - cisa-kev
      - patch-available
    affected: Force, Spark and Cloud firewalls on R81.20, R82, R82.10 and R82.20 (R80 to R81.10 are end of support) and Spark R81.10.x and R82.00.x, with Mobile Access Portal, Remote Access VPN with SSL Network Extender, SAML-realm VPN, Identity Awareness Captive Portal, UserCheck Portal or Zero Phishing in use
    fixed: Jumbo Hotfix Accumulator R82.20 take 14, R82.10 take 52, R82 take 132 and R81.20 take 174 or later; release-specific standalone hotfix packages (the R81.20 package of 2026-10-28 on take 166 or higher where Mobile Access is used); Spark R82.00.11 starting from build B998002843 and R81.10.17 starting from B996005005; a hotfix for the R81.10 gateway release, published 2026-10-29
  - id: CVE-2026-109619
    cvss: 9.2 (Check Point)
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status:
      - exploited
      - cisa-kev
      - patch-available
    affected: Force, Spark and Cloud firewalls on R81.20, R82, R82.10 and R82.20 (R80 to R81.10 are end of support) and Spark R81.10.x and R82.00.x, with Mobile Access Portal, Remote Access VPN with SSL Network Extender, SAML-realm VPN, Identity Awareness Captive Portal, UserCheck Portal or Zero Phishing in use
    fixed: Jumbo Hotfix Accumulator R82.20 take 14, R82.10 take 52, R82 take 132 and R81.20 take 174 or later; release-specific standalone hotfix packages (the R81.20 package of 2026-10-28 on take 166 or higher where Mobile Access is used); Spark R82.00.11 starting from build B998002843 and R81.10.17 starting from B996005005; a hotfix for the R81.10 gateway release, published 2026-10-29
  - id: CVE-2026-123039
    cvss: 7.8 (Check Point)
    epss: '0.01274'
    type: priv-esc
    vector: local
    auth: post-auth
    status:
      - exploited
      - cisa-kev
      - patch-available
    affected: Check Point Force firewalls, Security Management and Log Servers, Multi-Domain Security Management and Log Servers and Maestro Orchestrator on R82.20, R82.10, R82, R81.20, R81.10 and R81; Spark firewalls and Smart-1 Cloud are not affected
    fixed: 'Jumbo Hotfix Accumulator R82.20 take 14, R82.10 take 52, R82 take 132 and R81.20 take 174 or later; no fix listed for R81.10 or R81; mitigation until then: stop the dynamic_server process and prevent it from restarting'
sources:
  - url: https://support.checkpoint.com/results/sk/sk1000302
    publisher: Check Point (sk1000302)
    date: '2026-10-28'
    role: primary
  - url: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
    publisher: CISA Known Exploited Vulnerabilities catalog
    date: '2026-10-26'
    role: corroborating
  - url: https://support.checkpoint.com/results/sk/sk1000302
    publisher: Check Point (sk1000302, hotfix note of 2026-10-29)
    date: '2026-10-29'
    role: primary
  - url: https://support.checkpoint.com/results/sk/sk1000302
    publisher: Check Point (sk1000302, modified 2026-11-12)
    date: '2026-11-12'
    role: primary
  - url: https://support.checkpoint.com/results/sk/sk1000362
    publisher: Check Point (sk1000362, CVE-2026-123039, modified 2026-11-12)
    date: '2026-11-12'
    role: primary
  - url: https://research.checkpoint.com/2026/php2shell-exploitation-on-check-point-gateway/
    publisher: Check Point Research
    date: '2026-11-12'
    role: primary
closed_sources: []
evidence:
  - quote: Under certain circumstances, PHP vulnerabilities may allow Remote Code Execution through firewall web interfaces.
    publisher: Check Point (sk1000302)
    source_url: https://support.checkpoint.com/results/sk/sk1000302
  - quote: Check Point products are not vulnerable to CVE-2026-115560.
    publisher: Check Point (sk1000302)
    source_url: https://support.checkpoint.com/results/sk/sk1000302
  - quote: This Hotfix implements the PHP 7.4 published fix for CVE-2026-109618 and CVE-2026-109619.
    publisher: Check Point (sk1000302)
    source_url: https://support.checkpoint.com/results/sk/sk1000302
  - quote: Released Hotfix for R81.10
    publisher: Check Point (sk1000302, hotfix note of 2026-10-29)
    source_url: https://support.checkpoint.com/results/sk/sk1000302
  - quote: Check Point observed an active exploit of this vulnerability against a couple of dozen customers.
    publisher: Check Point (sk1000362, CVE-2026-123039, modified 2026-11-12)
    source_url: https://support.checkpoint.com/results/sk/sk1000362
  - quote: The first wave, on October 30, targeted Israeli organizations and included destructive activity against some of them.
    publisher: Check Point Research
    source_url: https://research.checkpoint.com/2026/php2shell-exploitation-on-check-point-gateway/
  - quote: Any command that does not use this wrapper may indicate that a command was executed as root through the socket and requires investigation.
    publisher: Check Point (sk1000362, CVE-2026-123039, modified 2026-11-12)
    source_url: https://support.checkpoint.com/results/sk/sk1000362
verification: single-source
sourcing_note: Check Point is the disclosing party and its three documents, sk1000302, sk1000362 and Check Point Research's report, are one assessor; CISA's Known Exploited Vulnerabilities catalogue lists CVE-2026-123039 from 2026-11-13 without describing its evidence, so the listing may rest on Check Point's own report and is not counted as independent confirmation of exploitation. sk1000302 carries no exploitation statement and no post-compromise check, and the CISA listing of the two PHP flaws concerns PHP generally, not Check Point gateways. Whether the standalone PHP hotfix also closes CVE-2026-123039 is not stated; sk1000362 lists only Jumbo takes as the fix. Check Point Research names no victim country other than Israel and leaves attribution open; indicators are deliberately not carried.
confidence: high
references:
  - 2026-10-21/php-critical-release-pre-announced-cve-2026-109618-109619
  - 2026-10-22/pan-os-panorama-php2shell-mgmt-interface-no-fixed-release
  - 2026-10-23/netscaler-php2shell-management-gui-fixes-2026-10-27
  - 2026-10-25/qnap-synology-php2shell-qts-quts-hero-fixed-others-unfixed
  - 2026-10-27/php2shell-ot-products-netmodule-nrsw-no-fix-macmon-schneider
  - 2026-10-28/cisco-php2shell-expressway-urwb-duo-access-gateway-fixes
  - 2026-10-28/hpe-clearpass-php2shell-hotfixes-hpesbnw05171
  - 2026-05-15/cve-2026-46300-linux-kernel-local-privilege-escalation-via-x
  - 2026-10-27/camping-care-tcs-camping-data-theft-php-flaw-whatsapp-fraud
  - 2026-10-29/f5-big-ip-php2shell-k000163821-critical-releases
  - 2026-10-29/php2shell-trend-micro-apex-quest-kace-netapp-ontap
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - Install a Jumbo Hotfix Accumulator at or above R81.20 take 174, R82 take 132, R82.10 take 52 or R82.20 take 14 on every Check Point gateway, management server, log server, Multi-Domain server and Maestro, because it carries both the PHP2Shell fix and the fix for CVE-2026-123039, and until it is in apply the cp-httpd.conf mitigation and stop the dynamic_server process; replace R81.10 and R81 systems, for which no fix for CVE-2026-123039 is listed.
  - On every gateway that ran Mobile Access, SSL Network Extender, SAML-realm VPN, the captive portal, UserCheck or Zero Phishing before the hotfix, search /var/log/dynamicCli.log for commands that do not use the legitimate Clish wrapper and the Mobile Access login-template directory for PHP files nobody deployed, and treat a hit as a compromise, because the implant has backup and snapshot persistence and one attacker moved from a gateway to an ESXi host.
updates:
  - at: '2026-10-30T03:54:02Z'
    run_id: 2026-10-30T0255Z-intel
    type: update
    summary: Check Point's sk1000302 now notes a hotfix for the end-of-support R81.10 gateway release, published on 2026-10-29 at 11:30 GMT; the entry recorded hotfixes only for R81.20, R82, R82.10, R82.20 and Spark. The summary, the CVE records and the hotfix paragraph name it.
    fields:
      - body
      - cves
      - evidence
      - sources
      - summary
  - at: '2026-11-13T03:59:06Z'
    run_id: 2026-11-13T0256Z-intel
    type: update
    summary: Check Point Research confirms exploitation of unpatched Check Point gateways from 2026-10-30 (PHP2Shell, then the root escalation CVE-2026-123039, exploited against a couple of dozen customers, with a persistent backdoor and an ESXi wiper); the Jumbo takes now carry both fixes.
    fields:
      - title
      - headline
      - summary
      - priority
      - tags
      - techniques
      - cves
      - actions
      - sources
      - evidence
      - sourcing_note
      - body
  - at: "2026-11-14T04:02:02Z"
    run_id: 2026-11-14T0255Z-intel
    type: improvement
    internal: true
    summary: >
      CISA's Known Exploited Vulnerabilities catalogue added CVE-2026-123039 on 2026-11-13 (due
      2026-11-16); its CVE record now carries the cisa-kev status and an EPSS value, and the sourcing note
      says the listing is not counted as independent confirmation.
    fields: [cves, sourcing_note]
migrated_from: null
---

Check Point's advisory sk1000302 says that under certain circumstances the PHP flaws CVE-2026-109618 and CVE-2026-109619, both scored CVSS 9.2, may allow remote code execution through firewall web interfaces; affected are Force, Spark and Cloud firewalls that use Mobile Access Portal (not Spark), Remote Access VPN with SSL Network Extender (not Spark) or with SAML realm authentication, the Identity Awareness captive portal, the UserCheck portal or Zero Phishing, on R81.20, R82, R82.10 and R82.20 and on Spark R81.10.x and R82.00.x, and end-of-support lines are also listed ([Check Point, 2026-11-12](https://support.checkpoint.com/results/sk/sk1000302)). The standalone hotfix of 2026-10-23 implements the PHP 7.4 fix and needs a reboot ([Check Point, 2026-10-29](https://support.checkpoint.com/results/sk/sk1000302)); the sk now says the fix is included in Jumbo Hotfix Accumulator R82.20 take 14, R82.10 take 52, R82 take 132 and R81.20 take 174, names Spark fixes from builds B998002843 and B996005005, and keeps the R81.10 hotfix ([Check Point, 2026-11-12](https://support.checkpoint.com/results/sk/sk1000302)). Until then, Check Point's mitigation is a cp-httpd.conf block denying multipart Content-Type requests, removed before the hotfix ([Check Point, 2026-10-29](https://support.checkpoint.com/results/sk/sk1000302)).

Check Point Research reports that from 2026-10-30, about a week after the fix, an attacker exploited unpatched gateways through Mobile Access portals with PHP2Shell and escalated to root with CVE-2026-123039: the first wave targeted Israeli organisations and included destructive activity against some, and a wider wave on 2026-11-02 targeted organisations in several countries ([Check Point Research, 2026-11-12](https://research.checkpoint.com/2026/php2shell-exploitation-on-check-point-gateway/)). CVE-2026-123039 is a local escalation: the root dynamic_server process runs whatever command it receives on a world-writable local socket without authenticating the caller, and Check Point says it observed an active exploit against a couple of dozen customers ([Check Point, 2026-11-12](https://support.checkpoint.com/results/sk/sk1000362)). After root the attacker placed PHP web shells in the directory the Mobile Access portal uses for its login pages and the TSGA implant, a root-run passive backdoor that Check Point says provides encrypted remote access, configuration theft, backup and snapshot persistence, process injection and firewall-log tampering; it ran a scanner, moved by SSH to a VMware ESXi host and ran a wiper there ([Check Point Research, 2026-11-12](https://research.checkpoint.com/2026/php2shell-exploitation-on-check-point-gateway/)). The standalone PHP hotfix text names only the two PHP CVEs ([Check Point, 2026-10-29](https://support.checkpoint.com/results/sk/sk1000302)), and sk1000362 lists no Jumbo take for R81.10 or R81, so protection there is not stated ([Check Point, 2026-11-12](https://support.checkpoint.com/results/sk/sk1000362)).

**Exposure:** for the PHP flaws, a gateway on a listed release with at least one of the six portal or VPN features in use ([Check Point, 2026-11-12](https://support.checkpoint.com/results/sk/sk1000302)); for CVE-2026-123039, a Force gateway, management or log server, Multi-Domain server or Maestro on R81 to R82.20 below those Jumbo takes ([Check Point, 2026-11-12](https://support.checkpoint.com/results/sk/sk1000362)).

**Detection:** the vulnerable daemon logs every command it receives to /var/log/dynamicCli.log, and Check Point says any command that does not use the legitimate Clish wrapper may indicate a command executed as root and requires investigation ([Check Point, 2026-11-12](https://support.checkpoint.com/results/sk/sk1000362)); Check Point Research also describes the web-shell, listener and SSH-to-ESXi behavior above ([Check Point Research, 2026-11-12](https://research.checkpoint.com/2026/php2shell-exploitation-on-check-point-gateway/)).

**Defender takeaway:** install the Jumbo take that carries both fixes on gateways and on management and log servers, apply the cp-httpd.conf mitigation and stop dynamic_server where it has to wait ([Check Point, 2026-11-12](https://support.checkpoint.com/results/sk/sk1000302); [Check Point, 2026-11-12](https://support.checkpoint.com/results/sk/sk1000362)), and treat a gateway that was exposed and unpatched since 2026-10-30 as needing a compromise check, because a hotfix is not stated to remove an implant already installed, which is an inference from the persistence Check Point Research describes ([Check Point Research, 2026-11-12](https://research.checkpoint.com/2026/php2shell-exploitation-on-check-point-gateway/)).

## Update — 2026-10-30T03:54:02Z

Check Point's sk1000302 carries a new note of 2026-10-29 at 11:30 GMT, "Released Hotfix for R81.10" ([Check Point, 2026-10-29](https://support.checkpoint.com/results/sk/sk1000302)). R81.10 is an end-of-support gateway release that the sk still lists as affected, so a gateway on it now has a hotfix to install. The other hotfixes and the exploitation statement are unchanged.

## Update — 2026-11-13T03:59:06Z

Check Point Research reports that exploitation of unpatched Check Point gateways began on 2026-10-30 and says it escalated to root with a second flaw, CVE-2026-123039, which Check Point rates CVSS 7.8 and says it saw exploited against a couple of dozen customers ([Check Point Research, 2026-11-12](https://research.checkpoint.com/2026/php2shell-exploitation-on-check-point-gateway/); [Check Point, 2026-11-12](https://support.checkpoint.com/results/sk/sk1000362)). The attacker left PHP web shells and a root-run backdoor with backup and snapshot persistence, and in the first wave moved by SSH from the gateway to a VMware ESXi host and deleted files there ([Check Point Research, 2026-11-12](https://research.checkpoint.com/2026/php2shell-exploitation-on-check-point-gateway/)); sk1000302 itself still carries no exploitation statement ([Check Point, 2026-11-12](https://support.checkpoint.com/results/sk/sk1000302)). The fix for both flaws is in Jumbo Hotfix Accumulator R82.20 take 14, R82.10 take 52, R82 take 132 and R81.20 take 174 or later ([Check Point, 2026-11-12](https://support.checkpoint.com/results/sk/sk1000302); [Check Point, 2026-11-12](https://support.checkpoint.com/results/sk/sk1000362)), none is listed for R81.10 or R81 ([Check Point, 2026-11-12](https://support.checkpoint.com/results/sk/sk1000362)), and the Spark fixes are now stated as builds from B998002843 and B996005005 ([Check Point, 2026-11-12](https://support.checkpoint.com/results/sk/sk1000302)). Check Point Research describes the TSGA backdoor and its embedded TSProxy library as modified variants of PhiliKit, a framework ESET associated with the China-nexus cluster UNC5221, and says the evidence does not allow a high-confidence assessment of who ran the operation: a single actor, an initial access broker or a false-flag operation all remain plausible ([Check Point Research, 2026-11-12](https://research.checkpoint.com/2026/php2shell-exploitation-on-check-point-gateway/)).
