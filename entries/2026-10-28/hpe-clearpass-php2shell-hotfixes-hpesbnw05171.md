---
schema: 1
kind: vulnerability
title: "CVE-2026-109618 / CVE-2026-109619, HPE Networking ClearPass Policy Manager: bulletin HPESBNW05171 lists the 6.14, 6.12 and 6.11 trains as affected by the PHP2Shell flaws and names a hotfix patch for each (CVSS 3.1 9.8)"
headline: "HPE ClearPass 6.14, 6.12 and 6.11 are affected by PHP2Shell; a hotfix patch exists for each train"
summary: >
  HPE Networking's bulletin HPESBNW05171, released on 2026-10-22 and revised on 2026-10-23 and 2026-10-29, lists ClearPass Policy Manager 6.14.0 and earlier and 6.11.15 and earlier as affected by the PHP flaws CVE-2026-109618 and CVE-2026-109619, each scored CVSS 3.1 9.8, adds the 6.12 train in its machine-readable record, and names a hotfix patch for 6.14.1, 6.12.8 and 6.11.16.
  HPE asks customers to consider removing guest portals and all management interfaces from public access until the affected instances are upgraded; the bulletin says nothing about exploitation of ClearPass, although CISA added both flaws to its Known Exploited Vulnerabilities catalog on 2026-10-26.
discovered_at: "2026-10-28T03:51:00Z"
updated_at: "2026-10-30T03:53:29Z"
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
    affected: "ClearPass Policy Manager 6.14.0 and earlier in the 6.14 train and 6.11.15 and earlier in the 6.11 train per the advisory note, and per its machine-readable record the 6.14, 6.11 and, since revision 3, 6.12 trains below the hotfix boundaries 6.14.1, 6.11.16 and 6.12.8; versions past end of maintenance are presumed affected and versions past end of support were not assessed"
    fixed: "ClearPass 6.14.1 Hotfix Patch, ClearPass 6.12.8 Hotfix Patch and ClearPass 6.11.16 Hotfix Patch, from the HPE Networking Support Portal"
  - id: CVE-2026-109619
    cvss: "9.8"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [cisa-kev, patch-available]
    affected: "ClearPass Policy Manager 6.14.0 and earlier in the 6.14 train and 6.11.15 and earlier in the 6.11 train per the advisory note, and per its machine-readable record the 6.14, 6.11 and, since revision 3, 6.12 trains below the hotfix boundaries 6.14.1, 6.11.16 and 6.12.8; versions past end of maintenance are presumed affected and versions past end of support were not assessed"
    fixed: "ClearPass 6.14.1 Hotfix Patch, ClearPass 6.12.8 Hotfix Patch and ClearPass 6.11.16 Hotfix Patch, from the HPE Networking Support Portal"
sources:
  - url: "https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05171.json"
    publisher: "HPE Networking (CSAF advisory HPESBNW05171, revision 2, superseded at this URL by revision 3)"
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
  - url: "https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05171.json"
    publisher: "HPE Networking (CSAF advisory HPESBNW05171, revision 3)"
    date: "2026-10-29"
    role: primary
closed_sources: []
evidence:
  - quote: "ClearPass versions 6.14.0 and earlier in the 6.14 release train"
    publisher: "HPE Networking (CSAF advisory HPESBNW05171, revision 3)"
    source_url: "https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05171.json"
  - quote: "ClearPass 6.14.1 Hotfix Patch to Address PHP Vulnerabilities CVE-2026-109618 and CVE-2026-109619"
    publisher: "HPE Networking (CSAF advisory HPESBNW05171, revision 3)"
    source_url: "https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05171.json"
  - quote: "Customers should also consider removing guest portals and all management interfaces from public access until the affected ClearPass instances have been upgraded."
    publisher: "HPE Networking (CSAF advisory HPESBNW05171, revision 3)"
    source_url: "https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05171.json"
  - quote: "Updated Affected and Resolution sections of this security advisory to exceptionally include ClearPass 6.12.8 software release."
    publisher: "HPE Networking (CSAF advisory HPESBNW05171, revision 3)"
    source_url: "https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05171.json"
verification: single-source
sourcing_note: >
  HPE Networking is the disclosing party for its own product and its CSAF record, revision 3, is the only source for the affected versions, the scores and the fixes. The bulletin gives no detection guidance and does not say whether ClearPass has been attacked. Its affected-products note (6.14.0 and earlier, 6.11.15 and earlier) and its machine-readable record (6.14.1, 6.11.16 and 6.12.8 as boundaries) differ on the boundary versions, and revision 2's wording that named 6.14.1 and 6.11.16 as versions with some mitigation is no longer in the bulletin. The flaws themselves are in the PHP runtime. The listing of both flaws in CISA's catalog comes from the catalog itself.
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
  - "Install the HPE ClearPass 6.14.1, 6.12.8 or 6.11.16 hotfix patch for CVE-2026-109618 and CVE-2026-109619 on every ClearPass Policy Manager node from the HPE Networking Support Portal, and until it is installed take the guest portal and the CLI and web management interfaces off public networks, confining management to a dedicated layer 2 segment or behind firewall policy."
updates:
  - at: "2026-10-30T03:53:29Z"
    run_id: 2026-10-30T0255Z-intel
    type: update
    summary: >
      HPE's revision 3 of bulletin HPESBNW05171, dated 2026-10-29, exceptionally adds ClearPass 6.12.8
      with a hotfix patch beside the 6.14.1 and 6.11.16 trains, and its affected-products note now reads
      6.14.0 and earlier and 6.11.15 and earlier; the earlier wording that named 6.14.1 and 6.11.16 as
      versions with some mitigation is gone. The title, headline, summary, CVE records, evidence, action
      and text now follow revision 3.
    fields: [actions, body, cves, evidence, headline, sources, sourcing_note, summary, title]
migrated_from: null
---

HPE Networking's bulletin HPESBNW05171, released on 2026-10-22 and revised on 2026-10-23 and 2026-10-29, covers CVE-2026-109618 and CVE-2026-109619, the PHP flaws behind PHP2Shell, in ClearPass Policy Manager and scores each CVSS 3.1 9.8 with network access, no privileges and no user interaction ([HPE Networking, 2026-10-29](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05171.json)). Its affected-products note lists ClearPass 6.14.0 and earlier in the 6.14 release train and 6.11.15 and earlier in the 6.11 train, while its machine-readable record also lists the 6.12 train and gives 6.14.1, 6.11.16 and 6.12.8 as the boundaries; the bulletin does not reconcile the two ([HPE Networking, 2026-10-29](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05171.json)). The fix is a hotfix patch for each train, 6.14.1, 6.12.8 (added in revision 3, which HPE says "exceptionally" includes 6.12.8) and 6.11.16, downloadable from the HPE Networking Support Portal; versions past end of maintenance are presumed affected and are not covered, and HPE has not assessed versions past end of support, which it says should be considered potentially impacted ([HPE Networking, 2026-10-29](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05171.json)).

HPE recommends confining the CLI and web management interfaces to a dedicated layer 2 segment or VLAN, or controlling them with firewall policy at layer 3 and above, and asks customers to consider removing guest portals and all management interfaces from public access until the affected ClearPass instances have been upgraded ([HPE Networking, 2026-10-29](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05171.json)). Other HPE Networking products and software versions it does not list are not known to be affected, and for Mist products the bulletin points to a Juniper reference advisory ([HPE Networking, 2026-10-29](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05171.json)). CISA added both PHP flaws to its Known Exploited Vulnerabilities catalog on 2026-10-26 ([CISA KEV, 2026-10-27](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)); the bulletin itself says nothing about exploitation of ClearPass ([HPE Networking, 2026-10-29](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05171.json)).

**Exposure:** every ClearPass Policy Manager on the 6.14, 6.12 or 6.11 train without the hotfix patch; the guest portal and the management interfaces are the surfaces HPE asks to take off public access ([HPE Networking, 2026-10-29](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05171.json)).

**Detection:** HPE gives no indicator and no post-patch check; CISA's PHP alert advises monitoring for PHP worker processes launching shells or downloading tools ([CISA, 2026-10-21](https://www.cisa.gov/news-events/alerts/2026/10/21/critical-vulnerabilities-php-require-immediate-patching)), which on a ClearPass node would be processes started by the web worker account (an inference, since HPE does not describe how ClearPass runs PHP).

**Defender takeaway:** install the hotfix patch for 6.14.1, 6.12.8 or 6.11.16 on every node now, the remediation HPE's bulletin names, and take any guest portal or management interface reachable from untrusted networks off public access, as HPE asks ([HPE Networking, 2026-10-29](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05171.json)).

## Update — 2026-10-30T03:53:29Z

HPE's revision 3 of bulletin HPESBNW05171, dated 2026-10-29, updates its affected and resolution sections to exceptionally include ClearPass 6.12.8 ([HPE Networking, 2026-10-29](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05171.json)). A ClearPass 6.12.8 hotfix patch for CVE-2026-109618 and CVE-2026-109619 is now named beside the 6.14.1 and 6.11.16 patches, downloadable from the HPE Networking Support Portal ([HPE Networking, 2026-10-29](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05171.json)). The affected-products note of this revision reads 6.14.0 and earlier in the 6.14 train and 6.11.15 and earlier in the 6.11 train, while its machine-readable record gives 6.14.1, 6.11.16 and 6.12.8 as boundaries, and the wording of revision 2 that named 6.14.1 and 6.11.16 as versions providing some level of mitigation is no longer in the bulletin ([HPE Networking, 2026-10-29](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05171.json)). The bulletin still says nothing about exploitation of ClearPass.
