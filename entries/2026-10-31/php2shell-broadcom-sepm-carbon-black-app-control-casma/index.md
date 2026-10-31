---
schema: 1
kind: vulnerability
title: "CVE-2026-109618 / CVE-2026-109619, Broadcom Symantec Endpoint Protection Manager, Carbon Black App Control Server, CloudSOC SpanVA and Content Analysis and Malware Analysis: PHP2Shell reaches the endpoint-security management servers; App Control Server 8.12.2 and 8.13.2 are the fixes Broadcom names"
headline: "PHP2Shell hits Broadcom endpoint-security servers: App Control 8.12.2 or 8.13.2; SEPM fix builds unconfirmed"
summary: >
  Broadcom's Enterprise Security Group advisory 39404, last revised on 2026-10-30, lists Carbon Black App Control Server, Symantec Endpoint Protection Manager (SEPM), the CloudSOC SpanVA Appliance and, since 2026-10-30, Content Analysis and Malware Analysis (CASMA) as affected by the PHP flaws CVE-2026-109618 and CVE-2026-109619, and gives no versions, fixes or workarounds. Broadcom's article 459982 names App Control Server 8.12.2 and 8.13.2 as the fixes for all supported versions; the SEPM builds 14.3.27716.10000 and 14.4.494.0000 rest on a community report that NCSC-NL's tracker accepts, because Broadcom's SEPM advisory needs a login. CISA lists both PHP flaws as exploited, and Broadcom's advisory says nothing about attacks on these products.
discovered_at: "2026-10-31T03:49:00Z"
updated_at: null
event_date: "2026-10-30"
run_id: 2026-10-31T0256Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, pre-auth, rce, cisa-kev, patch-available]
regions: [global]
sectors: []
entities: ["tool:php2shell", "product:php", "product:symantec-endpoint-protection-manager", "product:carbon-black-app-control-server", "product:cloudsoc-spanva-appliance", "product:content-analysis-and-malware-analysis"]
techniques: [T1190]
affected_products: ["Symantec Endpoint Protection Manager", "Carbon Black App Control Server", "CloudSOC SpanVA Appliance", "Content Analysis and Malware Analysis"]
cves:
  - id: CVE-2026-109618
    cvss: "n/a"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [cisa-kev, patch-available]
    affected: "Carbon Black App Control Server, all supported versions; Symantec Endpoint Protection Manager, CloudSOC SpanVA Appliance and Content Analysis and Malware Analysis (CASMA), with no versions stated in Broadcom's umbrella advisory"
    fixed: "App Control Server 8.12.2 and 8.13.2 (Broadcom article 459982); SEPM 14.3.27716.10000 and 14.4.494.0000 per NCSC-NL's tracker, which accepted a community report citing Broadcom's login-gated advisory and did not verify it; no fix stated for CloudSOC SpanVA or CASMA"
  - id: CVE-2026-109619
    cvss: "n/a"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [cisa-kev, patch-available]
    affected: "Carbon Black App Control Server, all supported versions; Symantec Endpoint Protection Manager, CloudSOC SpanVA Appliance and Content Analysis and Malware Analysis (CASMA), with no versions stated in Broadcom's umbrella advisory"
    fixed: "App Control Server 8.12.2 and 8.13.2 (Broadcom article 459982); SEPM 14.3.27716.10000 and 14.4.494.0000 per NCSC-NL's tracker, which accepted a community report citing Broadcom's login-gated advisory and did not verify it; no fix stated for CloudSOC SpanVA or CASMA"
sources:
  - url: "https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/39404"
    publisher: "Broadcom Enterprise Security Group (advisory 39404, revised 2026-10-30)"
    date: "2026-10-30"
    role: primary
  - url: "https://knowledge.broadcom.com/external/article?articleNumber=459982"
    publisher: "Broadcom (knowledge article 459982)"
    date: "2026-10-22"
    role: primary
  - url: "https://raw.githubusercontent.com/NCSC-NL/php2shell/main/software/changelog_software_list.md"
    publisher: "NCSC-NL (PHP2Shell software status list)"
    date: "2026-10-30"
    role: corroborating
  - url: "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    publisher: "CISA KEV catalog"
    date: "2026-10-26"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Broadcom's Enterprise Security Group is investigating CVE-2026-109618 and CVE-2026-109619"
    publisher: "Broadcom Enterprise Security Group (advisory 39404, revised 2026-10-30)"
    source_url: "https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/39404"
  - quote: "2026-10-30 12:00 PT - Content Analysis and Malware Analysis moved to Affected"
    publisher: "Broadcom Enterprise Security Group (advisory 39404, revised 2026-10-30)"
    source_url: "https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/39404"
  - quote: "These releases exclusively contain PHP-related changes."
    publisher: "Broadcom (knowledge article 459982)"
    source_url: "https://knowledge.broadcom.com/external/article?articleNumber=459982"
  - quote: "users already on version 8.13 must upgrade directly to 8.13.2"
    publisher: "Broadcom (knowledge article 459982)"
    source_url: "https://knowledge.broadcom.com/external/article?articleNumber=459982"
  - quote: "The maintainer accepts issue #30's reported SEPM 14.3.27716.10000 and 14.4.494.0000 updates as fixes for both PHP2Shell CVEs."
    publisher: "NCSC-NL (PHP2Shell software status list)"
    source_url: "https://raw.githubusercontent.com/NCSC-NL/php2shell/main/software/changelog_software_list.md"
verification: single-source
sourcing_note: >
  Broadcom is the disclosing party for its own products, and its advisory and knowledge article are the only first-party sources; the umbrella advisory states no versions, fixes or workarounds. Broadcom's SEPM advisory (39421) is not readable without a login, so the SEPM fix builds come from NCSC-NL's tracker, whose maintainer accepted a community report that cites it and did not verify it, and that reading carries reduced confidence. Product statuses on the umbrella page have moved between investigation and affected, CASMA most recently on 2026-10-30, so the page should be read again before relying on a status.
confidence: medium
references: ["2026-10-21/php-critical-release-pre-announced-cve-2026-109618-109619", "2026-10-22/pan-os-panorama-php2shell-mgmt-interface-no-fixed-release", "2026-10-23/netscaler-php2shell-management-gui-fixes-2026-10-27", "2026-10-25/qnap-synology-php2shell-qts-quts-hero-fixed-others-unfixed", "2026-10-27/php2shell-ot-products-netmodule-nrsw-no-fix-macmon-schneider", "2026-10-28/cisco-php2shell-expressway-urwb-duo-access-gateway-fixes", "2026-10-28/hpe-clearpass-php2shell-hotfixes-hpesbnw05171", "2026-10-29/check-point-php2shell-sk1000302-portal-and-vpn-gateways", "2026-10-29/f5-big-ip-php2shell-k000163821-critical-releases", "2026-10-29/php2shell-trend-micro-apex-quest-kace-netapp-ontap", "2026-05-15/cve-2026-46300-linux-kernel-local-privilege-escalation-via-x", "2026-10-27/camping-care-tcs-camping-data-theft-php-flaw-whatsapp-fraud"]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Install Carbon Black App Control Server 8.12.2 or 8.13.2 (8.13.2 where the server already runs 8.13), confirm the SEPM fix build against Broadcom's login-gated advisory 39421 before treating 14.3.27716.10000 or 14.4.494.0000 as the target, and until each server is fixed limit the management console of every SEPM, App Control Server, CloudSOC SpanVA appliance and CASMA to administrator networks."
updates: []
migrated_from: null
---

Broadcom's Enterprise Security Group advisory 39404, published on 2026-10-21 and last revised on 2026-10-30, lists four products as affected by the PHP flaws CVE-2026-109618 and CVE-2026-109619: Carbon Black App Control Server (moved to affected on 2026-10-22), Symantec Endpoint Protection Manager (SEPM, 2026-10-22), the CloudSOC SpanVA Appliance (2026-10-23) and Content Analysis and Malware Analysis (CASMA), which moved from under investigation to affected on 2026-10-30; the page states no versions, fixes or workarounds, and lists Content Analysis (CAS), the Symantec Endpoint Protection agent, Symantec Endpoint Security, Data Loss Prevention, Cloud Secure Web Gateway and Zero Trust Network Access among the products that are not vulnerable ([Broadcom, 2026-10-30](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/39404)). CISA added both PHP flaws to its Known Exploited Vulnerabilities catalog on 2026-10-26 ([CISA KEV catalog, 2026-10-26](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)); Broadcom's advisory says nothing about attacks on these products.

Broadcom's article 459982 says the App Control Server is affected in all supported versions and that builds 8.12.2 and 8.13.2 are available and contain only PHP-related changes: an installation on 8.12 or earlier may take either, one already on 8.13 must take 8.13.2 ([Broadcom, 2026-10-22](https://knowledge.broadcom.com/external/article?articleNumber=459982)). For SEPM, NCSC-NL's tracker lists builds 14.3.27716.10000 and 14.4.494.0000 as the fixes, on the strength of a community report that cites Broadcom's SEPM advisory, which needs a login and which the maintainer did not verify ([NCSC-NL, 2026-10-30](https://raw.githubusercontent.com/NCSC-NL/php2shell/main/software/changelog_software_list.md)). No fix is stated for the CloudSOC SpanVA Appliance or CASMA.

**Exposure:** a Symantec Endpoint Protection Manager, Carbon Black App Control Server, CloudSOC SpanVA appliance or CASMA whose management console or web service a hostile network can reach; Broadcom gives no version ranges, so every instance not on a fixed build counts. The flaws, CVE-2026-109618 and CVE-2026-109619, are in the PHP runtime.

**Detection:** Broadcom publishes no indicator. For a server that was reachable before its fix, review shells and downloads started by the console's web service and outbound connections the server initiates; this is an inference, since the pages do not describe how these products run PHP.

**Defender takeaway:** put these consoles on administrator networks now and on fixed builds as soon as they exist: App Control Server has its fix, SEPM's rests on an unverified reading, and CloudSOC SpanVA and CASMA have none. Re-read Broadcom's advisory 39404 before relying on a status, because CASMA changed on 2026-10-30.
