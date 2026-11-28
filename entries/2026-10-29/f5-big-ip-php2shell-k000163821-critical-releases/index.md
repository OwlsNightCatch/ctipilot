---
schema: 1
kind: vulnerability
title: "CVE-2026-109618 / CVE-2026-109619, F5 BIG-IP: the PHP2Shell flaws reach the Configuration utility of every module and the APM and SSL Orchestrator access profiles on 17.1.0 to 17.1.3, 17.5.0 to 17.5.1 and 21.1.0, and F5's cumulative critical releases 17.1.3.7, 17.5.1.11 and 21.1.0.4 carry the fix"
headline: "F5 BIG-IP is affected by PHP2Shell: fixes are in 17.1.3.7, 17.5.1.11 and 21.1.0.4; APM data plane and TMUI exposed"
summary: >
  F5's release notes for BIG-IP 17.1.3.7, 17.5.1.11 and 21.1.0.4, each updated on 2026-10-24, list K000163821 as the fix for the PHP flaws CVE-2026-109618 and CVE-2026-109619 and call each a critical release whose only new changes are PHP fixes.
  NCSC-NL's record of K000163821 puts BIG-IP 17.1.0 to 17.1.3, 17.5.0 to 17.5.1 and 21.1.0 in scope, through the Configuration utility of all modules and through the access-profile data plane of APM and SSL Orchestrator;
  F5's article itself could not be read, and nothing found reports an attack on BIG-IP, although CISA lists both flaws as exploited.
discovered_at: "2026-10-29T04:49:00Z"
updated_at: null
event_date: "2026-10-24"
run_id: 2026-10-29T0255Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, rce, pre-auth, cisa-kev, patch-available]
regions: [global]
sectors: []
entities: ["tool:php2shell", "product:php", "product:f5-big-ip", "product:f5-big-ip-access-policy-manager-apm", "product:f5-big-ip-ssl-orchestrator"]
techniques: [T1190]
affected_products: ["F5 BIG-IP", "F5 BIG-IP Access Policy Manager", "F5 BIG-IP SSL Orchestrator"]
cves:
  - id: CVE-2026-109618
    cvss: "n/a"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [cisa-kev, patch-available]
    affected: "BIG-IP 17.1.0 to 17.1.3, 17.5.0 to 17.5.1 and 21.1.0 (Configuration utility of all modules; APM and SSL Orchestrator access-profile data plane), as NCSC-NL records F5's K000163821; earlier affected releases remain vulnerable"
    fixed: "17.1.3.7, 17.5.1.11 and 21.1.0.4"
  - id: CVE-2026-109619
    cvss: "n/a"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [cisa-kev, patch-available]
    affected: "BIG-IP 17.1.0 to 17.1.3, 17.5.0 to 17.5.1 and 21.1.0 (Configuration utility of all modules; APM and SSL Orchestrator access-profile data plane), as NCSC-NL records F5's K000163821; earlier affected releases remain vulnerable"
    fixed: "17.1.3.7, 17.5.1.11 and 21.1.0.4"
sources:
  - url: "https://techdocs.f5.com/kb/en-us/products/big-ip_ltm/releasenotes/related/relnote-supplement-bigip-21-1-0-4.html"
    publisher: "F5 (BIG-IP 21.1.0.4 release notes)"
    date: "2026-10-24"
    role: primary
  - url: "https://techdocs.f5.com/kb/en-us/products/big-ip_ltm/releasenotes/related/relnote-supplement-bigip-17-5-1-11.html"
    publisher: "F5 (BIG-IP 17.5.1.11 release notes)"
    date: "2026-10-24"
    role: primary
  - url: "https://techdocs.f5.com/kb/en-us/products/big-ip_ltm/releasenotes/related/relnote-supplement-bigip-17-1-3-7.html"
    publisher: "F5 (BIG-IP 17.1.3.7 release notes)"
    date: "2026-10-24"
    role: primary
  - url: "https://raw.githubusercontent.com/NCSC-NL/php2shell/main/software/changelog_software_list.md"
    publisher: "NCSC-NL (PHP2Shell software status list)"
    date: "2026-10-26"
    role: corroborating
  - url: "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    publisher: "CISA Known Exploited Vulnerabilities catalog"
    date: "2026-10-28"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The only new changes in this release are PHP vulnerability fixes."
    publisher: "F5 (BIG-IP 21.1.0.4 release notes)"
    source_url: "https://techdocs.f5.com/kb/en-us/products/big-ip_ltm/releasenotes/related/relnote-supplement-bigip-21-1-0-4.html"
  - quote: "F5 K000163821, updated 2026-10-24, lists fixes in 17.1.3.7, 17.5.1.11 and 21.1.0.4 for both CVEs."
    publisher: "NCSC-NL (PHP2Shell software status list)"
    source_url: "https://raw.githubusercontent.com/NCSC-NL/php2shell/main/software/changelog_software_list.md"
verification: single-source
sourcing_note: >
  The fixed builds come from F5's own release notes. F5's advisory K000163821 is a page that only renders in a browser session and could not be read, so the affected releases and the
  exposed components are NCSC-NL's record of that article, which compiles F5's statement and is not an independent assessment, and F5's wording on exploitation and on mitigations is unread. The F5
  release notes name no branch other than 17.1, 17.5 and 21.1, and nothing found reports exploitation of BIG-IP.
confidence: medium
references: ["2026-10-21/php-critical-release-pre-announced-cve-2026-109618-109619", "2026-10-22/pan-os-panorama-php2shell-mgmt-interface-no-fixed-release", "2026-10-23/netscaler-php2shell-management-gui-fixes-2026-10-27", "2026-10-25/qnap-synology-php2shell-qts-quts-hero-fixed-others-unfixed", "2026-10-27/php2shell-ot-products-netmodule-nrsw-no-fix-macmon-schneider", "2026-10-28/cisco-php2shell-expressway-urwb-duo-access-gateway-fixes", "2026-10-28/hpe-clearpass-php2shell-hotfixes-hpesbnw05171", "2026-05-15/cve-2026-46300-linux-kernel-local-privilege-escalation-via-x", "2026-10-27/camping-care-tcs-camping-data-theft-php-flaw-whatsapp-fraud", "2026-10-29/check-point-php2shell-sk1000302-portal-and-vpn-gateways", "2026-10-29/php2shell-trend-micro-apex-quest-kace-netapp-ontap"]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Update every F5 BIG-IP on 17.1, 17.5 or 21.1 to 17.1.3.7, 17.5.1.11 or 21.1.0.4, systems that publish an APM or SSL Orchestrator access profile first, because NCSC-NL records the access-profile data plane as exposed as well as the Configuration utility."
updates: []
migrated_from: null
---

F5's release notes for BIG-IP 17.1.3.7, 21.1.0.4 and 17.5.1.11, each updated on 2026-10-24, list K000163821 as the reference for the fix of the PHP vulnerabilities CVE-2026-109618 and CVE-2026-109619 and describe each build as a critical release whose only new changes are PHP vulnerability fixes and which is cumulative and includes earlier hardened and critical releases ([F5, 2026-10-24](https://techdocs.f5.com/kb/en-us/products/big-ip_ltm/releasenotes/related/relnote-supplement-bigip-21-1-0-4.html); [F5, 2026-10-24](https://techdocs.f5.com/kb/en-us/products/big-ip_ltm/releasenotes/related/relnote-supplement-bigip-17-5-1-11.html); [F5, 2026-10-24](https://techdocs.f5.com/kb/en-us/products/big-ip_ltm/releasenotes/related/relnote-supplement-bigip-17-1-3-7.html)). NCSC-NL records F5 as confirming that BIG-IP 17.1.0 to 17.1.3, 17.5.0 to 17.5.1 and 21.1.0 are vulnerable through the Configuration utility control plane in all modules and, for APM and SSL Orchestrator, through the access-profile data plane, and that earlier affected releases stay vulnerable until updated ([NCSC-NL, 2026-10-26](https://raw.githubusercontent.com/NCSC-NL/php2shell/main/software/changelog_software_list.md)). CISA lists both PHP flaws as exploited since 2026-10-26; nothing found reports an attack on BIG-IP ([CISA KEV, 2026-10-28](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)).

**Exposure:** a BIG-IP on 17.1.0 to 17.1.3, 17.5.0 to 17.5.1 or 21.1.0 whose Configuration utility is reachable from a network the attacker can reach, or that publishes an APM or SSL Orchestrator access profile ([NCSC-NL, 2026-10-26](https://raw.githubusercontent.com/NCSC-NL/php2shell/main/software/changelog_software_list.md)).

**Detection:** F5's article on exploitation and mitigations could not be read and no indicator is published in the sources found. The telemetry to review on an exposed system is access to the Configuration utility and the access-profile web paths from untrusted sources, and shells or downloads started by the web service; this is an inference, not an F5 statement.

**Defender takeaway:** move to the cumulative critical release of your train and read K000163821 in a browser for F5's own mitigation list; until then keep the Configuration utility off untrusted networks, and treat an APM or SSL Orchestrator system that was exposed and unpatched as needing a compromise check.
