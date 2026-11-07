---
schema: 1
kind: vulnerability
title: "CVE-2026-109618 / CVE-2026-109619, Cisco Expressway, Ultra-Reliable Wireless Backhaul, Duo Access Gateway and ISE Portal Builder: Cisco's final PHP2Shell advisory names Expressway 15.5.21 and Duo Access Gateway 3.2.0 as the fixes and knows of no malicious use against its products"
headline: "Cisco's final PHP2Shell advisory: Expressway needs 15.5.21, Duo Access Gateway 3.2.0; Cisco knows of no malicious use"
summary: >
  Cisco's advisory cisco-sa-php-october26-Jj384Daq, final at version 1.10 on 2026-10-30, lists Expressway Series and Expressway Select Series
  (fixed release 15.5.21, workaround in the bug record), Ultra-Reliable Wireless Backhaul and Unified Industrial Wireless Software (fixed
  release 26.2.1.9, listed for November 2026, workaround in the bug record), Duo Access Gateway (3.2.0) and ISE Portal Builder (fix deployed,
  no customer action required) as affected by the PHP flaws CVE-2026-109618 and CVE-2026-109619. Cisco knows of no malicious use against a Cisco product,
  although CISA added both flaws to its Known Exploited Vulnerabilities catalog on 2026-10-26.
discovered_at: "2026-10-28T03:50:00Z"
updated_at: "2026-10-31T03:41:32Z"
event_date: "2026-10-27"
run_id: 2026-10-28T0256Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, rce, pre-auth, cisa-kev, patch-available]
regions: [global]
sectors: []
entities: ["product:php", "tool:php2shell", "product:cisco-expressway-series", "product:cisco-expressway-select-series", "product:cisco-ultra-reliable-wireless-backhaul", "product:cisco-unified-industrial-wireless-software", "product:cisco-duo-access-gateway", "product:cisco-identity-services-engine-portal-builder"]
techniques: [T1190]
affected_products: ["Cisco Expressway Series", "Cisco Expressway Select Series", "Cisco Ultra-Reliable Wireless Backhaul", "Cisco Unified Industrial Wireless Software", "Cisco Duo Access Gateway", "Cisco Identity Services Engine Portal Builder"]
cves:
  - id: CVE-2026-109618
    cvss: "n/a"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [cisa-kev, patch-available]
    affected: "Expressway Series and Expressway Select Series, Ultra-Reliable Wireless Backhaul and Unified Industrial Wireless Software, Duo Access Gateway and Identity Services Engine Portal Builder; the advisory gives no version ranges (its bug records CSCwx37062 and CSCwx37073 carry platform-specific information)"
    fixed: "Expressway 15.5.21; Ultra-Reliable Wireless Backhaul and Unified Industrial Wireless Software 26.2.1.9 (November 2026); Duo Access Gateway 3.2.0; ISE Portal Builder fix deployed, no customer action required"
  - id: CVE-2026-109619
    cvss: "n/a"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [cisa-kev, patch-available]
    affected: "Expressway Series and Expressway Select Series, Ultra-Reliable Wireless Backhaul and Unified Industrial Wireless Software, Duo Access Gateway and Identity Services Engine Portal Builder; the advisory gives no version ranges (its bug records CSCwx37062 and CSCwx37073 carry platform-specific information)"
    fixed: "Expressway 15.5.21; Ultra-Reliable Wireless Backhaul and Unified Industrial Wireless Software 26.2.1.9 (November 2026); Duo Access Gateway 3.2.0; ISE Portal Builder fix deployed, no customer action required"
sources:
  - url: "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-php-october26-Jj384Daq"
    publisher: "Cisco PSIRT (cisco-sa-php-october26-Jj384Daq, version 1.9)"
    date: "2026-10-28"
    role: primary
  - url: "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-php-october26-Jj384Daq"
    publisher: "Cisco PSIRT (cisco-sa-php-october26-Jj384Daq, version 1.10)"
    date: "2026-10-30"
    role: primary
  - url: "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-vcs-static-cred-hr7EWZ8t"
    publisher: "Cisco PSIRT (cisco-sa-vcs-static-cred-hr7EWZ8t, Expressway Series Remote Code Execution Vulnerability)"
    date: "2026-10-21"
    role: corroborating
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
  - quote: "The Cisco PSIRT is not aware of any malicious use of these vulnerabilities against any Cisco product."
    publisher: "Cisco PSIRT (cisco-sa-php-october26-Jj384Daq, version 1.9)"
    source_url: "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-php-october26-Jj384Daq"
  - quote: "If a product is not listed within this advisory, Cisco's review indicates that the product is not affected by this vulnerability."
    publisher: "Cisco PSIRT (cisco-sa-php-october26-Jj384Daq, version 1.9)"
    source_url: "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-php-october26-Jj384Daq"
  - quote: "For this product, the attacker must be authenticated as an administrator to exploit this vulnerability."
    publisher: "Cisco PSIRT (cisco-sa-php-october26-Jj384Daq, version 1.9)"
    source_url: "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-php-october26-Jj384Daq"
  - quote: "Updated fix status for ISE Portal Builder and fixed release for Ultra-Reliable Wireless Backhaul (URWB) and Unified Industrial Wireless Software."
    publisher: "Cisco PSIRT (cisco-sa-php-october26-Jj384Daq, version 1.10)"
    source_url: "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-php-october26-Jj384Daq"
  - quote: "Fix deployed, no customer action required."
    publisher: "Cisco PSIRT (cisco-sa-php-october26-Jj384Daq, version 1.10)"
    source_url: "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-php-october26-Jj384Daq"
verification: single-source
sourcing_note: >
  Cisco is the disclosing party for its own products; its advisory is the only source for the product statuses, the fixed releases and the
  statement that it knows of no malicious use. The flaws themselves are in the PHP runtime. The advisory carries no CVSS score except the 6.6
  it gives for the Ultra-Reliable Wireless Backhaul row, and no affected-version ranges; its bug records carry
  platform-specific information, workarounds and fixed releases. The listing of both PHP flaws in CISA's Known Exploited Vulnerabilities
  catalog comes from the catalog itself.
confidence: high
references: ["2026-10-21/php-critical-release-pre-announced-cve-2026-109618-109619", "2026-10-22/cve-2026-76466-cisco-expressway-cluster-unauth-root-rce", "2026-10-22/pan-os-panorama-php2shell-mgmt-interface-no-fixed-release", "2026-10-23/netscaler-php2shell-management-gui-fixes-2026-10-27", "2026-10-25/qnap-synology-php2shell-qts-quts-hero-fixed-others-unfixed", "2026-10-27/php2shell-ot-products-netmodule-nrsw-no-fix-macmon-schneider", "2026-10-28/hpe-clearpass-php2shell-hotfixes-hpesbnw05171", "2026-10-21/emudhra-intermediate-ca-keys-recoverable-trust-store-updates", "2026-10-27/camping-care-tcs-camping-data-theft-php-flaw-whatsapp-fraud"]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Upgrade every Cisco Expressway-C, Expressway-E and Expressway Select unit to 15.5.21, including units already moved to X15.5.20 for CVE-2026-76466, which Cisco's table does not name as the PHP2Shell fix, and until then apply the workaround in bug CSCwx37062; take any Duo Access Gateway to 3.2.0."
updates:
  - at: "2026-10-29T04:58:00Z"
    run_id: 2026-10-29T0255Z-intel
    type: update
    summary: >
      Cisco revised the advisory to version 1.9 on 2026-10-28 and moved the fixed-release date for Ultra-Reliable Wireless Backhaul and Unified Industrial Wireless Software 27.1.1 from March 2027 to
      November 2026; the earlier statement that there is no fixed release before March 2027 is replaced.
    fields: [summary, updated_at, cves, sources, evidence, body]
  - at: "2026-10-31T03:41:32Z"
    run_id: 2026-10-31T0256Z-intel
    type: update
    summary: >
      Cisco's PHP2Shell advisory, revised to version 1.10 on 2026-10-30, now lists 26.2.1.9 (Nov 2026) as
      the fixed release for Ultra-Reliable Wireless Backhaul and Unified Industrial Wireless Software,
      replacing 27.1.1, and shows ISE Portal Builder as fix deployed with no customer action required.
    fields: [summary, cves, sources, evidence, body]
migrated_from: null
---

Cisco's advisory cisco-sa-php-october26-Jj384Daq, published on 2026-10-21 and final at version 1.10 on 2026-10-30, lists Expressway, Ultra-Reliable Wireless Backhaul, Duo Access Gateway and ISE Portal Builder as affected by CVE-2026-109618 and CVE-2026-109619, the PHP flaws behind PHP2Shell ([Cisco PSIRT, 2026-10-30](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-php-october26-Jj384Daq)). Expressway Series and Expressway Select Series (bug CSCwx37062) have fixed release 15.5.21 and a workaround described in the bug record; Ultra-Reliable Wireless Backhaul and Unified Industrial Wireless Software (bug CSCwx37073) have fixed release 26.2.1.9, listed for November 2026, and a workaround, and there the attacker must be authenticated as an administrator, which lowers the CVSS 3.1 score to 6.6; Duo Access Gateway is fixed in 3.2.0; and ISE Portal Builder has a fix deployed with no customer action required ([Cisco PSIRT, 2026-10-30](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-php-october26-Jj384Daq)). The advisory gives no affected-version ranges and no workaround steps; its bug records carry platform-specific information, workarounds and fixed releases, and a product it does not list is, in Cisco's review, not affected ([Cisco PSIRT, 2026-10-28](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-php-october26-Jj384Daq)).

Cisco says it is aware that a public announcement is available and knows of no malicious use of the flaws against any Cisco product ([Cisco PSIRT, 2026-10-28](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-php-october26-Jj384Daq)); CISA added both flaws to its Known Exploited Vulnerabilities catalog on 2026-10-26 ([CISA KEV, 2026-10-27](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)). For Expressway the PHP fix is 15.5.21 ([Cisco PSIRT, 2026-10-28](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-php-october26-Jj384Daq)), while the release Cisco names for the unauthenticated root command execution on clustered units, CVE-2026-76466, is X15.5.20 ([Cisco PSIRT, 2026-10-21](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-vcs-static-cred-hr7EWZ8t)).

**Exposure:** every Expressway Series and Expressway Select unit and every Duo Access Gateway not on a release Cisco lists as fixed (15.5.21 and 3.2.0), since Cisco gives no affected-version ranges; the advisory names no version-check command and no component that runs the PHP; its bug records CSCwx37062 and CSCwx37073 carry platform-specific information ([Cisco PSIRT, 2026-10-28](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-php-october26-Jj384Daq)).

**Detection:** Cisco publishes no indicator and reports no attack on its products, but lists Snort rules 67359 and 67360 as action links for the advisory ([Cisco PSIRT, 2026-10-28](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-php-october26-Jj384Daq)); beyond that, CISA's PHP alert advises monitoring for PHP worker processes launching shells or downloading tools ([CISA, 2026-10-21](https://www.cisa.gov/news-events/alerts/2026/10/21/critical-vulnerabilities-php-require-immediate-patching)), which on these products would be processes started by the web worker account (an inference, since Cisco does not describe how they run PHP).

**Defender takeaway:** move Expressway to 15.5.21 and Duo Access Gateway to 3.2.0, the fixed releases the table names ([Cisco PSIRT, 2026-10-28](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-php-october26-Jj384Daq)); an Expressway already upgraded to X15.5.20 for the clustered-device flaw ([Cisco PSIRT, 2026-10-21](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-vcs-static-cred-hr7EWZ8t)) is not named as fixed in the PHP table, which lists only 15.5.21 (an inference from the table, not a Cisco statement), so apply the bug record's workaround until 15.5.21 is installed ([Cisco PSIRT, 2026-10-28](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-php-october26-Jj384Daq)). Ultra-Reliable Wireless Backhaul has no fixed release before November 2026, so its workaround is the control until then.

## Update — 2026-10-29T04:58:00Z

Cisco published version 1.9 of the advisory on 2026-10-28 to update the fix availability date for Ultra-Reliable Wireless Backhaul and Unified Industrial Wireless Software: release 27.1.1 is now listed for November 2026 instead of March 2027, and the workaround in bug CSCwx37073 remains the control until it ships ([Cisco PSIRT, 2026-10-28](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-php-october26-Jj384Daq)). The other rows are unchanged, and Cisco still knows of no malicious use against its products ([Cisco PSIRT, 2026-10-28](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-php-october26-Jj384Daq)).

## Update — 2026-10-31T03:41:32Z

Cisco revised the advisory to version 1.10 on 2026-10-30, updating the fix status for ISE Portal Builder and the fixed release for Ultra-Reliable Wireless Backhaul and Unified Industrial Wireless Software ([Cisco PSIRT, 2026-10-30](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-php-october26-Jj384Daq)). The table now lists release 26.2.1.9 (Nov 2026) for that wireless software instead of 27.1.1, and shows ISE Portal Builder as "Fix deployed, no customer action required" instead of offline for remediation; Cisco also added Webex Events to the products it confirms are not vulnerable ([Cisco PSIRT, 2026-10-30](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-php-october26-Jj384Daq)). Expressway 15.5.21 and Duo Access Gateway 3.2.0 are unchanged.
