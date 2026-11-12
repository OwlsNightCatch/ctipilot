---
schema: 1
kind: vulnerability
title: "CVE-2026-109618 / CVE-2026-109619, PHP2Shell in management servers and storage: Trend Micro released critical patches for Apex Central and Apex One server on 2026-11-11 while Mobile Security for Enterprise and Deep Discovery Analyzer still await theirs, Quest KACE SMA and SDA have fixes and should block ports 80, 443 and 52230 until patched, and NetApp ONTAP 9 is affected by CVE-2026-109618 only, inside the PHP jail"
headline: "PHP2Shell: Trend Micro Apex Central, Apex One PHP patches out; Quest KACE, NetApp ONTAP fixed; Trend advisory lags"
summary: >
  Trend Micro posted Critical Patch build 7351 for Apex Central and build 20113 for Apex One Service Pack 1 on 2026-11-11, each upgrading PHP to 8.2.35 (the Apex One readme does not name the flaw), while its advisory, last updated 2026-11-04, still shows both as awaiting patches and lists Mobile Security for Enterprise (due on 2026-11-17) and Deep Discovery Analyzer (due on 2026-11-12) as impacted, with critical patches for Deep Discovery Inspector and Email Inspector; Quest says all KACE SMA and SDA versions
  are affected, with SMA 15.0 CU5 and 15.1 CU2 and the SDA 9.3 hotfix out and advice to block ports 80, 443 and 52230 until applied; and NetApp's advisory lists ONTAP 9 as affected only by CVE-2026-109618, with attacker access as the
  www user restricted to the PHP jail and hotfix builds from 9.12.1P20HF1 to 9.19.1P4. NetApp says it is aware of public discussion of the vulnerability and none of the three vendors reports an exploited case on its page, although CISA lists both flaws as exploited.
discovered_at: "2026-10-29T04:50:00Z"
updated_at: "2026-11-12T04:18:00Z"
event_date: "2026-10-28"
run_id: 2026-10-29T0255Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, rce, pre-auth, cisa-kev, patch-available]
regions: [global]
sectors: []
entities: ["tool:php2shell", "product:php", "product:trend-micro-apex-central", "product:trend-micro-apex-one", "product:trend-micro-mobile-security-for-enterprise", "product:quest-kace-systems-management-appliance", "product:quest-kace-systems-deployment-appliance", "product:netapp-ontap-9"]
techniques: [T1190]
affected_products: ["Trend Micro Apex Central", "Trend Micro Apex One", "Trend Micro Mobile Security for Enterprise", "Quest KACE Systems Management Appliance", "Quest KACE Systems Deployment Appliance", "NetApp ONTAP 9"]
cves:
  - id: CVE-2026-109618
    cvss: "9.2 (NetApp, CVSS 4.0)"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [cisa-kev, patch-available]
    affected: "Trend Micro Apex Central, Apex One on-premises server and Mobile Security for Enterprise (versions not given); Quest KACE SMA and SDA, all versions; NetApp ONTAP 9 (releases not enumerated)"
    fixed: "Trend Micro: Apex Central Critical Patch build 7351 and Apex One Service Pack 1 Critical Patch build 20113 (its readme names no flaw), both released 2026-11-11 with PHP 8.2.35; Mobile Security for Enterprise due 2026-11-17 and Deep Discovery Analyzer due 2026-11-12, no patch posted on 2026-11-12; Deep Discovery Inspector and Email Inspector critical patches listed as of 2026-10-30; Quest KACE SMA 15.0 CU5 (15.0.378) and 15.1 CU2 (15.1.177), SDA 9.3 hotfix 9.3.313 (9.3.312 where already installed); NetApp ONTAP 9.12.1P20HF1, 9.13.1P21HF1, 9.14.1P18HF1, 9.15.1P20HF1, 9.16.1P16HF1, 9.17.1P11HF1, 9.17.1P12, 9.18.1P8HF1, 9.19.1P3HF1 and 9.19.1P4"
  - id: CVE-2026-109619
    cvss: "9.2 (NetApp, CVSS 4.0)"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [cisa-kev, patch-available]
    affected: "Trend Micro Apex Central, Apex One on-premises server and Mobile Security for Enterprise (versions not given); Quest KACE SMA and SDA, all versions; NetApp ONTAP 9 is not affected by this flaw"
    fixed: "Trend Micro: Apex Central Critical Patch build 7351 and Apex One Service Pack 1 Critical Patch build 20113 (its readme names no flaw), both released 2026-11-11 with PHP 8.2.35; Mobile Security for Enterprise due 2026-11-17 and Deep Discovery Analyzer due 2026-11-12, no patch posted on 2026-11-12; Deep Discovery Inspector and Email Inspector critical patches listed as of 2026-10-30; Quest KACE SMA 15.0 CU5 (15.0.378) and 15.1 CU2 (15.1.177), SDA 9.3 hotfix 9.3.313 (9.3.312 where already installed)"
sources:
  - url: "https://success.trendmicro.com/en-US/solution/KA-0024802"
    publisher: "Trend Micro (KA-0024802)"
    date: "2026-10-28"
    role: primary
  - url: "https://support.quest.com/kace-systems-management-appliance/kb/4385046/quest-kace-response-to-cve-2026-109618-and-cve-2026-109619-php2shell"
    publisher: "Quest Software (KB 4385046)"
    date: "2026-10-28"
    role: primary
  - url: "https://success.trendmicro.com/en-US/solution/KA-0024802"
    publisher: "Trend Micro (KA-0024802, status table as of 2026-10-30)"
    date: "2026-10-30"
    role: primary
  - url: "https://success.trendmicro.com/en-US/solution/KA-0024802"
    publisher: "Trend Micro (KA-0024802, status table as of 2026-11-02)"
    date: "2026-11-02"
    role: corroborating
  - url: "https://support.quest.com/kace-systems-management-appliance/kb/4385046/quest-kace-response-to-cve-2026-109618-and-cve-2026-109619-php2shell"
    publisher: "Quest Software (KB 4385046, updated 2026-10-29)"
    date: "2026-10-29"
    role: primary
  - url: "https://success.trendmicro.com/en-US/solution/KA-0024802"
    publisher: "Trend Micro (KA-0024802, status table as of 2026-11-04)"
    date: "2026-11-04"
    role: corroborating
  - url: "https://files.trendmicro.com/documentation/readme/CP/apexcentral_win_en_criticalpatch_b7351_Readme.html"
    publisher: "Trend Micro (Apex Central Critical Patch build 7351 readme)"
    date: "2026-11-05"
    role: primary
  - url: "https://files.trendmicro.com/documentation/readme/Apex%20One/2020/apex_one_2019_win_cp_b20113_EN_hotfix_Readme.html"
    publisher: "Trend Micro (Apex One Critical Patch build 20113 readme)"
    date: "2026-11-09"
    role: primary
  - url: "https://downloadcenter.trendmicro.com/index.php?regs=nabu&prodid=1746"
    publisher: "Trend Micro Download Center (Apex Central)"
    date: "2026-11-11"
    role: corroborating
  - url: "https://downloadcenter.trendmicro.com/index.php?regs=nabu&prodid=1745"
    publisher: "Trend Micro Download Center (Apex One)"
    date: "2026-11-11"
    role: corroborating
  - url: "https://downloadcenter.trendmicro.com/index.php?regs=nabu&prodid=1646"
    publisher: "Trend Micro Download Center (Deep Discovery Analyzer)"
    date: "2026-11-12"
    role: corroborating
  - url: "https://downloadcenter.trendmicro.com/index.php?regs=nabu&prodid=83"
    publisher: "Trend Micro Download Center (Mobile Security for Enterprise)"
    date: "2026-11-12"
    role: corroborating
  - url: "https://security.netapp.com/advisory/NTAP-20261021-0021"
    publisher: "NetApp (NTAP-20261021-0021)"
    date: "2026-10-26"
    role: primary
  - url: "https://security.netapp.com/adv_api/advisory/NTAP-20261021-0021"
    publisher: "NetApp (NTAP-20261021-0021, advisory data)"
    date: "2026-10-26"
    role: primary
  - url: "https://security.netapp.com/advisory/NTAP-20261021-0021"
    publisher: "NetApp (NTAP-20261021-0021, initial release)"
    date: "2026-10-21"
    role: primary
  - url: "https://security.netapp.com/adv_api/advisory/NTAP-20261021-0021"
    publisher: "NetApp (NTAP-20261021-0021, advisory data revision 10.0)"
    date: "2026-10-29"
    role: primary
  - url: "https://security.netapp.com/adv_api/advisory/NTAP-20261021-0021"
    publisher: "NetApp (NTAP-20261021-0021, advisory data, revision 11.0)"
    date: "2026-11-03"
    role: primary
  - url: "https://security.netapp.com/adv_api/advisory/NTAP-20261021-0021"
    publisher: "NetApp (NTAP-20261021-0021, advisory data, revision 12.0, final)"
    date: "2026-11-04"
    role: primary
  - url: "https://kb.netapp.com/on-prem/ontap/Ontap_OS/OS-KBs/How_to_apply_ONTAP_workarounds_for_PHP2SHELL_vulnerabilities"
    publisher: "NetApp Knowledge Base"
    date: "2026-10-26"
    role: corroborating
  - url: "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    publisher: "CISA Known Exploited Vulnerabilities catalog"
    date: "2026-10-28"
    role: corroborating
closed_sources: []
evidence:
  - quote: "At this time, TrendAI has not seen any active instances or scenarios of successful exploitation of either of the vulnerabilities in our products or services."
    publisher: "Trend Micro (KA-0024802)"
    source_url: "https://success.trendmicro.com/en-US/solution/KA-0024802"
  - quote: "This Critical Patch upgrades the PHP module to build 8.2.35"
    publisher: "Trend Micro (Apex Central Critical Patch build 7351 readme)"
    source_url: "https://files.trendmicro.com/documentation/readme/CP/apexcentral_win_en_criticalpatch_b7351_Readme.html"
  - quote: "This Critical Patch updates the PHP module to version 8.2.35 to protect against a potential security issue."
    publisher: "Trend Micro (Apex One Critical Patch build 20113 readme)"
    source_url: "https://files.trendmicro.com/documentation/readme/Apex%20One/2020/apex_one_2019_win_cp_b20113_EN_hotfix_Readme.html"
  - quote: "DDEI 5.1: CP 4902"
    publisher: "Trend Micro (KA-0024802, status table as of 2026-10-30)"
    source_url: "https://success.trendmicro.com/en-US/solution/KA-0024802"
  - quote: "Critical Patch ETA: Nov. 17"
    publisher: "Trend Micro (KA-0024802, status table as of 2026-10-30)"
    source_url: "https://success.trendmicro.com/en-US/solution/KA-0024802"
  - quote: "Block all public Internet access to the KACE SMA and SDA systems."
    publisher: "Quest Software (KB 4385046)"
    source_url: "https://support.quest.com/kace-systems-management-appliance/kb/4385046/quest-kace-response-to-cve-2026-109618-and-cve-2026-109619-php2shell"
  - quote: "An unauthenticated attacker could potentially gain access as the www user but would be restricted to the PHP jail, limiting the scope of exploit."
    publisher: "NetApp (NTAP-20261021-0021, advisory data)"
    source_url: "https://security.netapp.com/adv_api/advisory/NTAP-20261021-0021"
verification: single-source
sourcing_note: >
  Each vendor is the disclosing party for its own products and its page is the only source for that vendor's status, versions, fixes and mitigations. Trend Micro's table is dated as of 2026-11-04 and lags its Download Center, which dates both Apex patches 2026-11-11; the Apex One readme does not name PHP2Shell, so its link to this flaw rests on the PHP 8.2.35 update, the Download Center date and the advisory's patch ETA. The table's affected versions are not stated. NetApp's advisory page renders only in a browser, and its fix table and impact text were
  read from the advisory data behind the page. None of the three pages carries a post-compromise check.
confidence: high
references: ["2026-10-21/php-critical-release-pre-announced-cve-2026-109618-109619", "2026-10-22/pan-os-panorama-php2shell-mgmt-interface-no-fixed-release", "2026-10-23/netscaler-php2shell-management-gui-fixes-2026-10-27", "2026-10-25/qnap-synology-php2shell-qts-quts-hero-fixed-others-unfixed", "2026-10-27/php2shell-ot-products-netmodule-nrsw-no-fix-macmon-schneider", "2026-10-28/cisco-php2shell-expressway-urwb-duo-access-gateway-fixes", "2026-10-28/hpe-clearpass-php2shell-hotfixes-hpesbnw05171", "2026-05-15/cve-2026-46300-linux-kernel-local-privilege-escalation-via-x", "2026-10-27/camping-care-tcs-camping-data-theft-php-flaw-whatsapp-fraud", "2026-10-29/check-point-php2shell-sk1000302-portal-and-vpn-gateways", "2026-10-29/f5-big-ip-php2shell-k000163821-critical-releases"]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Install Trend Micro's Apex Central Critical Patch build 7351 and Apex One Service Pack 1 Critical Patch build 20113 (both released 2026-11-11; the Apex One readme updates PHP to 8.2.35 without naming the flaw) on every server now, without waiting for the advisory page to change, and keep their consoles on administrator networks until done; for Mobile Security for Enterprise (patch due 2026-11-17, mitigation from Trend Micro support) and Deep Discovery Analyzer (due 2026-11-12) keep the interim mitigation until the patch ships; install the critical patches the table lists for Deep Discovery Inspector and Email Inspector."
  - "Install KACE SMA 15.0 CU5 or 15.1 CU2 and the SDA 9.3 hotfix 9.3.313 (9.3.312 where already installed), and until then block inbound ports 80, 443 and 52230 to every appliance, as Quest advises."
updates:
  - at: "2026-10-31T03:40:59Z"
    run_id: 2026-10-31T0256Z-intel
    type: update
    summary: >
      Trend Micro's PHP2Shell advisory, updated 2026-10-30, now lists critical patches for Deep Discovery
      Inspector and Email Inspector and adds Mobile Security for Enterprise as impacted with a patch due
      on 2026-11-17; the Apex Central and Apex One server patches stay due on 2026-11-11. Quest published
      KACE SDA hotfix 9.3.313 and NetApp added ONTAP 9.19.1P4 to its fixed builds, both on 2026-10-29.
    fields: [summary, affected_products, cves, sources, evidence, sourcing_note, actions, body, entities]
  - at: "2026-11-01T14:05:02Z"
    run_id: 2026-11-01T1312Z-audit
    type: correction
    internal: true
    summary: >
      The title turned Trend Micro's patch ETA of 2026-11-11 into a firm date; it now says the patches are
      expected then. The Exposure line's Trend Micro citation is dated to the 2026-10-30 status table that
      lists Mobile Security for Enterprise.
    fields: [body, title]
  - at: "2026-11-03T03:47:17Z"
    run_id: 2026-11-03T0256Z-intel
    type: update
    summary: >
      Trend Micro's status table of 2026-11-02 shows Trend Micro Web Security in the cloud fixed and the
      TWS Authentication Agent impacted with a mitigation and no patch date, and NetApp's revision 11.0
      adds ONTAP 9 hotfix builds 9.12.1P20HF1 and 9.13.1P21HF1.
    fields: [sources, body, summary, cves, sourcing_note]
  - at: "2026-11-08T14:02:15Z"
    run_id: 2026-11-08T1309Z-audit
    type: update
    summary: >
      NetApp's advisory reached its final revision, 12.0, on 2026-11-04 and adds ONTAP 9.17.1P12 to the
      fixed builds.
    fields: [body, cves, sources]
  - at: "2026-11-12T04:18:00Z"
    run_id: 2026-11-12T0255Z-intel
    type: update
    summary: >
      Trend Micro released critical patches for Apex Central (build 7351, whose readme names PHP2Shell) and Apex One Service Pack 1 (build 20113, whose readme names no flaw) on 2026-11-11, both upgrading PHP to 8.2.35, while its advisory, last updated 2026-11-04, still shows both as awaiting patches; Mobile Security for Enterprise and Deep Discovery Analyzer remain pending.
    fields: [title, headline, summary, cves, sources, evidence, sourcing_note, actions, body]
migrated_from: null
---

Trend Micro's Download Center dates Critical Patch build 7351 for Apex Central and Critical Patch build 20113 for Apex One Service Pack 1 to 2026-11-11 ([Trend Micro Download Center, 2026-11-11](https://downloadcenter.trendmicro.com/index.php?regs=nabu&prodid=1746); [Trend Micro Download Center, 2026-11-11](https://downloadcenter.trendmicro.com/index.php?regs=nabu&prodid=1745)). The Apex Central readme says the patch upgrades the bundled PHP module to build 8.2.35 and names PHP2Shell ([Trend Micro, 2026-11-05](https://files.trendmicro.com/documentation/readme/CP/apexcentral_win_en_criticalpatch_b7351_Readme.html)); the Apex One readme says it updates the PHP module to 8.2.35 and resolves a potential remote code execution issue without naming the flaw ([Trend Micro, 2026-11-09](https://files.trendmicro.com/documentation/readme/Apex%20One/2020/apex_one_2019_win_cp_b20113_EN_hotfix_Readme.html)). The customer advisory KA-0024802, last updated 2026-11-04, still shows both products as impacted with a critical patch ETA of 11 November, Mobile Security for Enterprise impacted with a patch due on 2026-11-17 and Deep Discovery Analyzer due on 2026-11-12 and critical patches for Deep Discovery Inspector and Email Inspector ([Trend Micro, 2026-11-04](https://success.trendmicro.com/en-US/solution/KA-0024802)). Trend Micro says it has not seen successful exploitation in its products or services ([Trend Micro, 2026-11-04](https://success.trendmicro.com/en-US/solution/KA-0024802)).

Quest's knowledge-base article says all versions of the KACE Systems Management Appliance (SMA) and Systems Deployment Appliance (SDA) are affected and that CVE-2026-115560 does not affect them; KACE SMA 15.0 CU5 (15.0.378) and 15.1 CU2 (15.1.177) with PHP 8.4.27 were published on 2026-10-23, the cumulative updates 15.0 Patch 4 and 15.1 Patch 1 do not contain the fix, and the SDA 9.3 hotfix 9.3.312 with PHP 8.3.36 followed ([Quest Software, 2026-10-29](https://support.quest.com/kace-systems-management-appliance/kb/4385046/quest-kace-response-to-cve-2026-109618-and-cve-2026-109619-php2shell)). Until an appliance is updated Quest says to block all public internet access and, because a potentially exploitable communication path remains after the agent tunnel on port 52230 is established, to block inbound web traffic including ports 80, 443 and 52230 ([Quest Software, 2026-10-29](https://support.quest.com/kace-systems-management-appliance/kb/4385046/quest-kace-response-to-cve-2026-109618-and-cve-2026-109619-php2shell)).

NetApp's advisory lists ONTAP 9 as affected only by CVE-2026-109618, scored CVSS 4.0 9.2, where an unauthenticated attacker could potentially gain access as the www user but would be restricted to the PHP jail, and lists hotfix builds from 9.12.1P20HF1 to 9.19.1P4, 9.17.1P12 among them ([NetApp, 2026-11-04](https://security.netapp.com/adv_api/advisory/NTAP-20261021-0021)). NetApp's knowledge-base article names all ONTAP web services as affected, System Manager, the SPI web portal, the REST API, ZAPI and HTTP and HTTPS access, and recommends upgrading and then undoing any workaround ([NetApp Knowledge Base, 2026-10-26](https://kb.netapp.com/on-prem/ontap/Ontap_OS/OS-KBs/How_to_apply_ONTAP_workarounds_for_PHP2SHELL_vulnerabilities)). CISA lists both PHP flaws as exploited since 2026-10-26, although none of the three vendors reports an exploited case ([CISA KEV, 2026-10-28](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)).

**Exposure:** a Trend Micro Apex Central, Apex One or Mobile Security for Enterprise server whose console or web endpoints a hostile network can reach; any KACE SMA or SDA, whose web ports and agent port 52230 are named; any ONTAP 9 cluster whose web services are reachable and that runs a release other than the fixed builds ([Trend Micro, 2026-11-02](https://success.trendmicro.com/en-US/solution/KA-0024802); [Quest Software, 2026-10-29](https://support.quest.com/kace-systems-management-appliance/kb/4385046/quest-kace-response-to-cve-2026-109618-and-cve-2026-109619-php2shell); [NetApp Knowledge Base, 2026-10-26](https://kb.netapp.com/on-prem/ontap/Ontap_OS/OS-KBs/How_to_apply_ONTAP_workarounds_for_PHP2SHELL_vulnerabilities)).

**Detection:** none of the three vendors publishes an indicator. For a management server or appliance that was reachable before its fix, the telemetry to review is shells and downloads started by its web service and outbound connections the server initiates; this is an inference, since the pages do not describe the attack.

**Defender takeaway:** install the Apex Central and Apex One patches now, because Trend Micro's advisory page lags its Download Center, and keep the Trend Micro, KACE and ONTAP management interfaces off untrusted networks until each is fixed; Trend Micro asks customers to restrict the impacted consoles to trusted addresses ([Trend Micro, 2026-11-04](https://success.trendmicro.com/en-US/solution/KA-0024802)).

## Update — 2026-10-31T03:40:59Z

Trend Micro's customer advisory KA-0024802 now reads last updated 2026-10-30, with its status table as of Oct. 30 ([Trend Micro, 2026-10-30](https://success.trendmicro.com/en-US/solution/KA-0024802)). The table now lists critical patches for Deep Discovery Inspector, one per listed line from CP 1077 on 7.0 to CP 1200 on 6.5, and for Deep Discovery Email Inspector 5.1 (CP 4902), which Trend Micro had listed as due on 2026-10-30 ([Trend Micro, 2026-10-30](https://success.trendmicro.com/en-US/solution/KA-0024802)). Trend Micro Mobile Security for Enterprise is newly listed as impacted, with a critical patch due on 2026-11-17 and mitigation through Trend Micro support ([Trend Micro, 2026-10-30](https://success.trendmicro.com/en-US/solution/KA-0024802)). Apex Central and the Apex One on-premises server stay due on 2026-11-11, Deep Discovery Analyzer on 2026-11-12 and the Trend Micro Web Security cloud service on 2026-11-06, and Trend Micro still says it has seen no exploitation in its products ([Trend Micro, 2026-10-30](https://success.trendmicro.com/en-US/solution/KA-0024802)). Quest's knowledge-base article now also lists KACE SDA hotfix 9.3.313, published on 2026-10-29, which covers systems on hotfix versions 9.3.305-9.3.111 and on GA version 9.3.304 ([Quest Software, 2026-10-29](https://support.quest.com/kace-systems-management-appliance/kb/4385046/quest-kace-response-to-cve-2026-109618-and-cve-2026-109619-php2shell)), and NetApp's advisory data adds ONTAP 9.19.1P4 to the fixed builds in revision 10.0 of 2026-10-29 ([NetApp, 2026-10-29](https://security.netapp.com/adv_api/advisory/NTAP-20261021-0021)).

## Update — 2026-11-03T03:47:17Z

Trend Micro's status table, last updated 2026-11-02, shows Trend Micro Web Security in the cloud fixed on 2026-10-30 and lists the TWS Authentication Agent as impacted, with a mitigation and no patch date; the on-premises gateway and enforcement agent are not impacted ([Trend Micro, 2026-11-02](https://success.trendmicro.com/en-US/solution/KA-0024802)). NetApp's revision 11.0 of 2026-11-03 adds the ONTAP 9 hotfix builds 9.12.1P20HF1 and 9.13.1P21HF1 ([NetApp, 2026-11-03](https://security.netapp.com/adv_api/advisory/NTAP-20261021-0021)).

## Update — 2026-11-08T14:02:15Z

NetApp's revision 12.0 of 2026-11-04 adds ONTAP 9.17.1P12 to the fixed builds and gives the advisory final status ([NetApp, 2026-11-04](https://security.netapp.com/adv_api/advisory/NTAP-20261021-0021)).

## Update — 2026-11-12T04:18:00Z

Trend Micro's Download Center dates critical patches for Apex Central (build 7351) and Apex One Service Pack 1 (build 20113) to 2026-11-11 ([Trend Micro Download Center, 2026-11-11](https://downloadcenter.trendmicro.com/index.php?regs=nabu&prodid=1746); [Trend Micro Download Center, 2026-11-11](https://downloadcenter.trendmicro.com/index.php?regs=nabu&prodid=1745)). The Apex Central readme says its patch upgrades the PHP module to 8.2.35 and names PHP2Shell ([Trend Micro, 2026-11-05](https://files.trendmicro.com/documentation/readme/CP/apexcentral_win_en_criticalpatch_b7351_Readme.html)); the Apex One readme says it updates the PHP module to 8.2.35 and does not name the flaw ([Trend Micro, 2026-11-09](https://files.trendmicro.com/documentation/readme/Apex%20One/2020/apex_one_2019_win_cp_b20113_EN_hotfix_Readme.html)). Its advisory has not been revised since 2026-11-04 and still lists the 11 November ETA; Mobile Security for Enterprise (due 2026-11-17) and Deep Discovery Analyzer (due 2026-11-12) still show as impacted ([Trend Micro, 2026-11-04](https://success.trendmicro.com/en-US/solution/KA-0024802)), and the Download Center pages of those two products list no matching patch as of 2026-11-12 ([Trend Micro Download Center, 2026-11-12](https://downloadcenter.trendmicro.com/index.php?regs=nabu&prodid=1646); [Trend Micro Download Center, 2026-11-12](https://downloadcenter.trendmicro.com/index.php?regs=nabu&prodid=83)).
