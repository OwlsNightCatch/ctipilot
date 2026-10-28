---
schema: 1
kind: vulnerability
title: "CVE-2026-109618 / CVE-2026-109619, HPE Networking ClearPass Policy Manager: bulletin HPESBNW05171 lists 6.14.1 and 6.11.16 and below as affected by the PHP2Shell flaws and names hotfix patches for both (CVSS 3.1 9.8)"
headline: "HPE ClearPass through 6.14.1 and 6.11.16 is affected by PHP2Shell; hotfix patches exist for both trains"
summary: >
  HPE Networking's bulletin HPESBNW05171, released on 2026-10-22 and revised on 2026-10-23, lists ClearPass Policy Manager 6.14.1 and below
  and 6.11.16 and below (both released 2026-09-29) as affected by the PHP flaws CVE-2026-109618 and CVE-2026-109619, each scored CVSS 3.1
  9.8, and names a hotfix patch for each train. HPE asks customers to consider removing guest portals and all management interfaces from
  public access until ClearPass runs a version providing some level of mitigation, which it names as 6.14.1 and 6.11.16; the bulletin says
  nothing about exploitation of ClearPass, although CISA added both flaws to its Known Exploited Vulnerabilities catalog on 2026-10-26.
discovered_at: "2026-10-28T03:51:00Z"
updated_at: null
event_date: "2026-10-23"
run_id: 2026-10-28T0256Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, rce, pre-auth, cisa-kev, patch-available]
regions: [global]
sectors: []
entities: ["product:php", "tool:php2shell", "product:hpe-networking-clearpass-policy-manager"]
techniques: [T1190]
affected_products: ["HPE Networking ClearPass Policy Manager"]
cves:
  - id: CVE-2026-109618
    cvss: "9.8"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [cisa-kev, patch-available]
    affected: "ClearPass Policy Manager 6.14.1 and below and 6.11.16 and below (both released 2026-09-29); versions past end of maintenance are presumed affected and versions past end of support were not assessed"
    fixed: "ClearPass 6.14.1 Hotfix Patch and ClearPass 6.11.16 Hotfix Patch, from the HPE Networking Support Portal"
  - id: CVE-2026-109619
    cvss: "9.8"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [cisa-kev, patch-available]
    affected: "ClearPass Policy Manager 6.14.1 and below and 6.11.16 and below (both released 2026-09-29); versions past end of maintenance are presumed affected and versions past end of support were not assessed"
    fixed: "ClearPass 6.14.1 Hotfix Patch and ClearPass 6.11.16 Hotfix Patch, from the HPE Networking Support Portal"
sources:
  - url: "https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05171.json"
    publisher: "HPE Networking (CSAF advisory HPESBNW05171, revision 2)"
    date: "2026-10-23"
    role: primary
  - url: "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    publisher: "CISA Known Exploited Vulnerabilities catalog (version 2026.10.27)"
    date: "2026-10-27"
    role: corroborating
  - url: "https://www.cisa.gov/news-events/alerts/2026/10/21/critical-vulnerabilities-php-require-immediate-patching"
    publisher: "CISA (alert, Critical Vulnerabilities in PHP Require Immediate Patching)"
    date: "2026-10-21"
    role: corroborating
closed_sources: []
evidence:
  - quote: "ClearPass 6.14.1 (released on Sep 29, 2026) and below"
    publisher: "HPE Networking (CSAF advisory HPESBNW05171, revision 2)"
    source_url: "https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05171.json"
  - quote: "ClearPass 6.14.1 Hotfix Patch to Address PHP Vulnerabilities CVE-2026-109618 and CVE-2026-109619"
    publisher: "HPE Networking (CSAF advisory HPESBNW05171, revision 2)"
    source_url: "https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05171.json"
  - quote: "a version providing some level of mitigation"
    publisher: "HPE Networking (CSAF advisory HPESBNW05171, revision 2)"
    source_url: "https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05171.json"
  - quote: "customers are asked to consider removing guest portals and all management interfaces from public access"
    publisher: "HPE Networking (CSAF advisory HPESBNW05171, revision 2)"
    source_url: "https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05171.json"
verification: single-source
sourcing_note: >
  HPE Networking is the disclosing party for its own product and its CSAF record is the only source for the affected versions, the scores and
  the fixes. The bulletin does not say whether ClearPass has been attacked and gives no detection guidance. The flaws themselves are in the PHP runtime. The bulletin is inconsistent: its workaround text names 6.14.1 and 6.11.16 as versions
  providing some level of mitigation, while its affected list covers 6.14.1 and 6.11.16 and below and its remediation names hotfix patches
  for both. The listing of both flaws in CISA's catalog comes from the catalog itself.
confidence: high
references: ["2026-10-21/php-critical-release-pre-announced-cve-2026-109618-109619", "2026-10-22/pan-os-panorama-php2shell-mgmt-interface-no-fixed-release", "2026-10-23/netscaler-php2shell-management-gui-fixes-2026-10-27", "2026-10-25/qnap-synology-php2shell-qts-quts-hero-fixed-others-unfixed", "2026-10-27/php2shell-ot-products-netmodule-nrsw-no-fix-macmon-schneider", "2026-10-28/cisco-php2shell-expressway-urwb-duo-access-gateway-fixes", "2026-10-27/camping-care-tcs-camping-data-theft-php-flaw-whatsapp-fraud"]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Install the HPE ClearPass 6.14.1 or 6.11.16 hotfix patch for CVE-2026-109618 and CVE-2026-109619 on every ClearPass Policy Manager node from the HPE Networking Support Portal, and until it is installed take the guest portal and the CLI and web management interfaces off public networks, confining management to a dedicated layer 2 segment or behind firewall policy."
updates: []
migrated_from: null
---

HPE Networking's bulletin HPESBNW05171, released on 2026-10-22 and revised on 2026-10-23 to cover hotfix releases, lists ClearPass Policy Manager 6.14.1 and below and 6.11.16 and below, both released on 2026-09-29, as affected by CVE-2026-109618 and CVE-2026-109619, the PHP flaws behind PHP2Shell, and scores each CVSS 3.1 9.8 with network access, no privileges and no user interaction ([HPE Networking, 2026-10-23](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05171.json)). The fix is a hotfix patch for 6.14.1 and one for 6.11.16, downloadable from the HPE Networking Support Portal; versions past end of maintenance are presumed affected and are not covered by the bulletin, and HPE has not assessed versions past end of support, which it says should be considered potentially impacted ([HPE Networking, 2026-10-23](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05171.json)).

HPE recommends confining the CLI and web management interfaces to a dedicated layer 2 segment or VLAN, or controlling them with firewall policy at layer 3 and above, and asks customers to consider removing guest portals and all management interfaces from public access until ClearPass instances have been upgraded to "a version providing some level of mitigation", which it names as 6.14.1 and 6.11.16, although the same bulletin lists 6.14.1 and 6.11.16 and below as affected and names the hotfix patches as the remediation ([HPE Networking, 2026-10-23](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05171.json)). Other HPE Aruba Networking products it does not list are not known to be affected, and for Mist products the bulletin points to a Juniper reference advisory ([HPE Networking, 2026-10-23](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05171.json)). CISA added both PHP flaws to its Known Exploited Vulnerabilities catalog on 2026-10-26 ([CISA KEV, 2026-10-27](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)); the bulletin itself says nothing about exploitation of ClearPass ([HPE Networking, 2026-10-23](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05171.json)).

**Exposure:** every ClearPass Policy Manager on 6.14.1 or 6.11.16 and below without the hotfix; HPE asks customers to consider removing guest portals and all management interfaces from public access ([HPE Networking, 2026-10-23](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05171.json)).

**Detection:** HPE gives no indicator and no post-patch check; CISA's PHP alert advises monitoring for PHP worker processes launching shells or downloading tools ([CISA, 2026-10-21](https://www.cisa.gov/news-events/alerts/2026/10/21/critical-vulnerabilities-php-require-immediate-patching)), which on a ClearPass node would be processes started by the web worker account (an inference, since HPE does not describe how ClearPass runs PHP).

**Defender takeaway:** install the hotfix patch for 6.14.1 or 6.11.16 on every node now, the remediation HPE's bulletin names, and take any guest portal or management interface reachable from untrusted networks off public access, as HPE asks ([HPE Networking, 2026-10-23](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05171.json)).
