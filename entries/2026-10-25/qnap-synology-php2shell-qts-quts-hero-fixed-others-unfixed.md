---
schema: 1
kind: vulnerability
title: "CVE-2026-109618 / CVE-2026-109619, QNAP QTS, QuTS hero and QuTScloud: the PHP2Shell flaws reach the NAS web components before authentication; fixed builds of 2026-10-23, QVR Surveillance, TVR OS and Notes Station 3 now fixed, QNE (ADRA) still unfixed"
headline: "PHP2Shell hits QNAP NAS before login: QTS, QuTS hero, QVR, TVR OS and Notes Station 3 fixed, QNE still unfixed"
summary: >
  QNAP's advisory QSA-26-18 says the PHP2Shell flaws CVE-2026-109618 and CVE-2026-109619 (CVSS 4.0 9.2) affect the PHP in the web
  components of QTS, QuTS hero, QuTScloud and several QNAP applications and can be triggered before authentication, and fixed builds dated
  2026-10-23 are out for QTS, QuTS hero and QuTScloud. As of 2026-10-28 (revision V1.2) the table lists QVR Surveillance (ARM32) 3.0.3.1756, TVR OS 1.0.5
  and Notes Station 3 3.9.15 as resolved; QNE (ADRA) has its own advisory, QSA-26-19, with no fixed version and QNAP says to keep devices off the internet; QNAP has seen scanning and
  exploitation attempts in the wild but no reports of exploitation targeting its products, and CISA added both flaws to its Known Exploited
  Vulnerabilities catalog on 2026-10-26. Synology's advisory fixes its PHP packages (except the end-of-life PHP 7.3), Mail Station and Calendar.
discovered_at: "2026-10-25T14:10:55Z"
updated_at: "2026-10-31T03:39:49Z"
event_date: "2026-10-22"
run_id: 2026-10-25T1308Z-audit
priority: notable
immediate_action: null
tags: [vulnerabilities, rce, pre-auth, cisa-kev, patch-available]
regions: [global]
sectors: []
entities: ["product:php", "product:qnap-qts", "product:qnap-quts-hero", "product:qnap-qutscloud", "product:qnap-note-station-3", "product:qnap-qne", "product:qnap-qvr-surveillance", "product:qnap-tvr-os", "product:synology-mail-station", "product:synology-calendar"]
techniques: [T1190]
affected_products: ["QNAP QTS", "QNAP QuTS hero", "QNAP QuTScloud", "QNAP Note Station 3", "QNAP QNE", "QNAP QVR Surveillance", "QNAP TVR OS", "Synology Mail Station", "Synology Calendar", "PHP"]
cves:
  - id: CVE-2026-109618
    cvss: "9.2 (CVSS 4.0, as stated by QNAP for the PHP flaw)"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [cisa-kev, patch-available]
    affected: "QTS 6.1.0 and 5.2.11 and earlier, QuTS hero h6.1.0, h6.0.x, h5.3.x and h5.2.11 and earlier, QuTScloud c5.2.9 and earlier, Notes Station 3 3.9.14 and earlier, QNE (ADRA) 1.0.7 and earlier, QVR Surveillance 3.0.3 and earlier (ARM32 models), TVR OS 1.0.4 and earlier; Synology PHP 7.3 to 8.4 packages, Mail Station and Synology Calendar"
    fixed: "QTS 6.1.0.3656 and 5.2.11.3661, QuTS hero h6.1.0.3656, h6.0.2.3656 (also for h5.3.x) and h5.2.11.3661, QuTScloud c5.2.9.3661 (builds of 2026-10-23), QVR Surveillance 3.0.3.1756, TVR OS 1.0.5 and Notes Station 3 3.9.15 (listed as resolved as of 2026-10-28); no fix yet for QNE (ADRA), which has its own advisory QSA-26-19; Synology PHP 7.4.33-0131, 8.0.30-0122, 8.1.34-0120, 8.2.35-0171, 8.3.36-0051, 8.4.27-0051, Mail Station 30000002.3.19-20333 and Calendar 3.0.4-21435, no fix for the end-of-life PHP 7.3 package"
  - id: CVE-2026-109619
    cvss: "9.2 (CVSS 4.0, as stated by QNAP for the PHP flaw)"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [cisa-kev, patch-available]
    affected: "QTS 6.1.0 and 5.2.11 and earlier, QuTS hero h6.1.0, h6.0.x, h5.3.x and h5.2.11 and earlier, QuTScloud c5.2.9 and earlier, Notes Station 3 3.9.14 and earlier, QNE (ADRA) 1.0.7 and earlier, QVR Surveillance 3.0.3 and earlier (ARM32 models), TVR OS 1.0.4 and earlier; Synology PHP 7.3 to 8.4 packages, Mail Station and Synology Calendar"
    fixed: "QTS 6.1.0.3656 and 5.2.11.3661, QuTS hero h6.1.0.3656, h6.0.2.3656 (also for h5.3.x) and h5.2.11.3661, QuTScloud c5.2.9.3661 (builds of 2026-10-23), QVR Surveillance 3.0.3.1756, TVR OS 1.0.5 and Notes Station 3 3.9.15 (listed as resolved as of 2026-10-28); no fix yet for QNE (ADRA), which has its own advisory QSA-26-19; Synology PHP 7.4.33-0131, 8.0.30-0122, 8.1.34-0120, 8.2.35-0171, 8.3.36-0051, 8.4.27-0051, Mail Station 30000002.3.19-20333 and Calendar 3.0.4-21435, no fix for the end-of-life PHP 7.3 package"
sources:
  - url: "https://www.qnap.com/en/security-advisory/qsa-26-18"
    publisher: "QNAP PSIRT (QSA-26-18, revision V1.1)"
    date: "2026-10-24"
    role: primary
  - url: "https://www.qnap.com/en/security-advisory/qsa-26-18"
    publisher: "QNAP PSIRT (QSA-26-18, affected-products table as of 2026-10-27)"
    date: "2026-10-27"
    role: primary
  - url: "https://www.qnap.com/en/security-advisory/qsa-26-18"
    publisher: "QNAP PSIRT (QSA-26-18, revision V1.2)"
    date: "2026-10-28"
    role: primary
  - url: "https://www.qnap.com/en/security-advisory/qsa-26-19"
    publisher: "QNAP PSIRT (QSA-26-19, QNE (ADRA))"
    date: "2026-10-22"
    role: primary
  - url: "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    publisher: "CISA Known Exploited Vulnerabilities catalog (version 2026.10.26)"
    date: "2026-10-26"
    role: corroborating
  - url: "https://www.qnap.com/en/security-news/2026/qnap-statement-on-critical-php-vulnerabilities-php2shell-assessment-and-mitigation-guidance"
    publisher: "QNAP (statement on PHP2Shell)"
    date: "2026-10-22"
    role: primary
  - url: "https://www.synology.com/security/advisory/Synology_SA_26_14"
    publisher: "Synology PSIRT (Synology-SA-26:14)"
    date: "2026-10-22"
    role: primary
closed_sources: []
evidence:
  - quote: "Both vulnerabilities can be triggered before any application-level authentication takes place."
    publisher: "QNAP PSIRT (QSA-26-18, revision V1.1)"
    source_url: "https://www.qnap.com/en/security-advisory/qsa-26-18"
  - quote: "QNAP PSIRT has observed scanning activity and exploitation attempts targeting these vulnerabilities in the wild."
    publisher: "QNAP (statement on PHP2Shell)"
    source_url: "https://www.qnap.com/en/security-news/2026/qnap-statement-on-critical-php-vulnerabilities-php2shell-assessment-and-mitigation-guidance"
  - quote: "QNAP has not received reports of exploitation targeting QNAP products."
    publisher: "QNAP PSIRT (QSA-26-18, revision V1.1)"
    source_url: "https://www.qnap.com/en/security-advisory/qsa-26-18"
  - quote: "QVR Surveillance 3.0.3 and earlier (ARM32 models)Resolved QVR Surveillance 3.0.3.1756"
    publisher: "QNAP PSIRT (QSA-26-18, affected-products table as of 2026-10-27)"
    source_url: "https://www.qnap.com/en/security-advisory/qsa-26-18"
  - quote: "TVR OS 1.0.4 and earlier Resolved TVR OS 1.0.5"
    publisher: "QNAP PSIRT (QSA-26-18, affected-products table as of 2026-10-27)"
    source_url: "https://www.qnap.com/en/security-advisory/qsa-26-18"
  - quote: "Notes Station 3 3.9.14 and earlier Resolved Notes Station 3 3.9.15"
    publisher: "QNAP PSIRT (QSA-26-18, revision V1.2)"
    source_url: "https://www.qnap.com/en/security-advisory/qsa-26-18"
  - quote: "QNE (ADRA) 1.0.7 and earlier Fixing To be announced"
    publisher: "QNAP PSIRT (QSA-26-19, QNE (ADRA))"
    source_url: "https://www.qnap.com/en/security-advisory/qsa-26-19"
  - quote: "Until fixed versions are available, the most effective protection is to keep the device off the internet."
    publisher: "QNAP PSIRT (QSA-26-18, revision V1.1)"
    source_url: "https://www.qnap.com/en/security-advisory/qsa-26-18"
  - quote: "The built-in PHP in OS is not exposed to external attack surfaces, and the risk of exploitation is considered very low."
    publisher: "Synology PSIRT (Synology-SA-26:14)"
    source_url: "https://www.synology.com/security/advisory/Synology_SA_26_14"
verification: single-source
sourcing_note: >
  Each vendor's advisory is the first-party source for its own products, fixed builds and mitigations; the two flaws themselves
  are in the PHP runtime and are covered by the related PHP, PAN-OS and NetScaler entries. QNAP's statement reports scanning and
  exploitation attempts against the PHP flaws in general, and its advisory reports none against QNAP products. The listing of both PHP flaws in CISA's Known Exploited Vulnerabilities catalog comes from the catalog itself.
confidence: high
references: ["2026-10-21/php-critical-release-pre-announced-cve-2026-109618-109619", "2026-10-22/pan-os-panorama-php2shell-mgmt-interface-no-fixed-release", "2026-10-23/netscaler-php2shell-management-gui-fixes-2026-10-27"]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Update every QNAP NAS on QTS, QuTS hero or QuTScloud to the builds of 2026-10-23 (QTS 6.1.0.3656 or 5.2.11.3661, QuTS hero h6.1.0.3656, h6.0.2.3656 (h5.3.x included) or h5.2.11.3661, QuTScloud c5.2.9.3661), every QVR Surveillance (ARM32 models) to 3.0.3.1756, every TVR OS to 1.0.5 and every Notes Station 3 to 3.9.15, and take any QNAP device running QNE (ADRA) off the internet until QNAP lists a fix."
updates:
  - at: "2026-10-27T03:42:00Z"
    run_id: 2026-10-27T0256Z-intel
    type: update
    summary: >
      QNAP's advisory table now lists QVR Surveillance (ARM32) 3.0.3.1756 and TVR OS 1.0.5 as resolved,
      leaving Notes Station 3 and QNE (ADRA) without a fix, and no longer names QuMagie as affected; CISA
      added both PHP flaws to its Known Exploited Vulnerabilities catalog on 2026-10-26.
    fields: [actions, body, cves, evidence, headline, sources, sourcing_note, summary, tags, title, affected_products, entities]
  - at: "2026-10-31T03:39:49Z"
    run_id: 2026-10-31T0256Z-intel
    type: update
    summary: >
      QNAP's advisory QSA-26-18 now lists Notes Station 3 as resolved by 3.9.15 (revision V1.2,
      2026-10-28), while QNE (ADRA), moved to its own advisory QSA-26-19, still has no fixed version.
    fields: [title, headline, summary, cves, sources, evidence, actions, body]
migrated_from: null
---

QNAP's advisory QSA-26-18 says the PHP2Shell flaws CVE-2026-109618 and CVE-2026-109619 (CVSS 4.0 9.2) affect the PHP used in the web components of its operating systems and several of its applications, can be triggered before any application-level authentication, and could let an unauthenticated remote attacker execute code on the device ([QNAP, 2026-10-24](https://www.qnap.com/en/security-advisory/qsa-26-18)). Its revision of 2026-10-24 lists fixed builds dated 2026-10-23 for QTS (6.1.0.3656 and 5.2.11.3661), QuTS hero (h6.1.0.3656, h6.0.2.3656, which also covers h5.3.x, and h5.2.11.3661) and QuTScloud (c5.2.9.3661), while revision V1.2 of 2026-10-28 lists Notes Station 3 3.9.14 and earlier as resolved by 3.9.15 and the table lists QVR Surveillance 3.0.3 and earlier on ARM32 models as resolved by 3.0.3.1756 and TVR OS 1.0.4 and earlier as resolved by 1.0.5 ([QNAP, 2026-10-28](https://www.qnap.com/en/security-advisory/qsa-26-18)). QNE (ADRA) 1.0.7 and earlier has its own advisory, QSA-26-19, and its fixed version is still to be announced ([QNAP, 2026-10-22](https://www.qnap.com/en/security-advisory/qsa-26-19)). QNAP's PSIRT says it has observed scanning and exploitation attempts against the flaws in the wild and blocked attempts against its own website, online store and cloud services ([QNAP, 2026-10-22](https://www.qnap.com/en/security-news/2026/qnap-statement-on-critical-php-vulnerabilities-php2shell-assessment-and-mitigation-guidance)), and its advisory says it has received no reports of exploitation targeting QNAP products ([QNAP, 2026-10-24](https://www.qnap.com/en/security-advisory/qsa-26-18)). PHP inside Container Station containers or third-party applications is not covered by QNAP's updates ([QNAP, 2026-10-24](https://www.qnap.com/en/security-advisory/qsa-26-18)).

Synology's advisory Synology-SA-26:14 rates its PHP 7.3 to 8.4 packages, Mail Station and Synology Calendar critical and lists fixed releases for each except the end-of-life PHP 7.3 package, which gets no fix; Synology says the PHP built into DSM is not exposed to external attack surfaces and considers the risk of exploitation very low ([Synology, 2026-10-22](https://www.synology.com/security/advisory/Synology_SA_26_14)).

**Exposure:** a QNAP NAS on QTS, QuTS hero or QuTScloud below the fixed builds, or a QNAP device running QVR Surveillance (ARM32 models) below 3.0.3.1756, TVR OS below 1.0.5, Notes Station 3 below 3.9.15 or QNE (ADRA), whose management or web ports are reachable from outside, which QNAP ties to router port forwarding, UPnP and myQNAPcloud publishing; the management ports default to 8080 and 443 ([QNAP, 2026-10-24](https://www.qnap.com/en/security-advisory/qsa-26-18)). On Synology, a DSM with one of the listed PHP packages, Mail Station or Calendar installed ([Synology, 2026-10-22](https://www.synology.com/security/advisory/Synology_SA_26_14)).

**Detection:** QNAP's compromise check is a review of QuLog Center for unexpected logins or access and a Security Center and Malware Remover scan with current definitions; if compromise is suspected it says to disconnect the device and change all passwords ([QNAP, 2026-10-24](https://www.qnap.com/en/security-advisory/qsa-26-18)).

**Defender takeaway:** update QTS, QuTS hero, QuTScloud, Notes Station 3, QVR Surveillance (ARM32 models) and TVR OS now; for QNE (ADRA), which has no fix, remove internet exposure (port forwarding, UPnP, myQNAPcloud publishing), use a VPN for remote access and allow the management ports only from trusted subnets, which QNAP says reduces exposure without fixing the flaws and does not protect against local devices that are already compromised ([QNAP, 2026-10-24](https://www.qnap.com/en/security-advisory/qsa-26-18)). On Synology, update the listed packages; the PHP 7.3 package gets no fix ([Synology, 2026-10-22](https://www.synology.com/security/advisory/Synology_SA_26_14)).

## Update — 2026-10-27T03:42:00Z

As of 2026-10-27 QNAP's advisory table lists QVR Surveillance 3.0.3 and earlier (ARM32 models) as resolved by QVR Surveillance 3.0.3.1756 and TVR OS 1.0.4 and earlier as resolved by TVR OS 1.0.5, while Notes Station 3 3.9.14 and earlier and QNE (ADRA) 1.0.7 and earlier remain in "Fixing" with the fixed version to be announced; QuMagie is no longer among the listed affected products, and the revision history still ends at V1.1 of 2026-10-24, so these table changes carry no dated revision ([QNAP, 2026-10-27](https://www.qnap.com/en/security-advisory/qsa-26-18)). QNAP still says it has received no reports of exploitation targeting QNAP products ([QNAP, 2026-10-27](https://www.qnap.com/en/security-advisory/qsa-26-18)). CISA added both PHP flaws to its Known Exploited Vulnerabilities catalog on 2026-10-26, as flaws in PHP rather than as a QNAP finding ([CISA KEV, 2026-10-26](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)).

## Update — 2026-10-31T03:39:49Z

QNAP revised advisory QSA-26-18 to V1.2 on 2026-10-28 ("Notes Station 3 Resolved Published"), and its table now lists Notes Station 3 3.9.14 and earlier as resolved by Notes Station 3 3.9.15 ([QNAP, 2026-10-28](https://www.qnap.com/en/security-advisory/qsa-26-18)). QNE (ADRA) 1.0.7 and earlier is no longer in that table: it has its own advisory, QSA-26-19, released on 2026-10-22, whose status is Fixing and whose fixed version is still to be announced ([QNAP, 2026-10-22](https://www.qnap.com/en/security-advisory/qsa-26-19)). Both advisories still say QNAP has received no reports of exploitation targeting QNAP products, and QSA-26-19 repeats that until fixed versions are available the most effective protection is to keep the device off the internet ([QNAP, 2026-10-22](https://www.qnap.com/en/security-advisory/qsa-26-19)).
