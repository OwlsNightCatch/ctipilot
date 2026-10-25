---
schema: 1
kind: vulnerability
title: "CVE-2026-109618 / CVE-2026-109619, QNAP QTS, QuTS hero and QuTScloud: the PHP2Shell flaws reach the NAS web components before authentication; fixed builds of 2026-10-23, other QNAP products still unfixed"
headline: "PHP2Shell hits QNAP NAS before login: QTS and QuTS hero builds of 23 October fix it, other QNAP products still unfixed"
summary: >
  QNAP's advisory QSA-26-18 says the PHP2Shell flaws CVE-2026-109618 and CVE-2026-109619 (CVSS 4.0 9.2) affect the PHP in the web
  components of QTS, QuTS hero, QuTScloud and several QNAP applications and can be triggered before any application-level
  authentication. Fixed QTS, QuTS hero and QuTScloud builds dated 2026-10-23 are out; Note Station 3, QNE (ADRA), QVR Surveillance
  (ARM32) and TVR OS have no fix yet, QuMagie is listed as affected without a fix row, and QNAP says to keep devices off the internet
  until fixes ship. QNAP has seen scanning and
  exploitation attempts against the flaws in the wild but no reports of exploitation targeting its products. Synology's
  advisory fixes its PHP packages (except the end-of-life PHP 7.3), Mail Station and Calendar and rates the PHP built into DSM
  as not exposed.
discovered_at: "2026-10-25T14:10:55Z"
updated_at: null
event_date: "2026-10-22"
run_id: 2026-10-25T1308Z-audit
priority: notable
immediate_action: null
tags: [vulnerabilities, rce, pre-auth, patch-available]
regions: [global]
sectors: []
entities: ["product:php", "product:qnap-qts", "product:qnap-quts-hero", "product:qnap-qutscloud", "product:qnap-note-station-3", "product:qnap-qne", "product:qnap-qvr-surveillance", "product:qnap-tvr-os", "product:qnap-qumagie", "product:synology-mail-station", "product:synology-calendar"]
techniques: [T1190]
affected_products: ["QNAP QTS", "QNAP QuTS hero", "QNAP QuTScloud", "QNAP Note Station 3", "QNAP QNE", "QNAP QVR Surveillance", "QNAP TVR OS", "QNAP QuMagie", "Synology Mail Station", "Synology Calendar", "PHP"]
cves:
  - id: CVE-2026-109618
    cvss: "9.2 (CVSS 4.0, as stated by QNAP for the PHP flaw)"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "QTS 6.1.0 and 5.2.11 and earlier, QuTS hero h6.1.0, h6.0.x and h5.2.11 and earlier, QuTScloud c5.2.9 and earlier, QuMagie 2.10.1 and earlier, Note Station 3 3.9.14 and earlier, QNE (ADRA) 1.0.7 and earlier, QVR Surveillance 3.0.3 and earlier (ARM32 models), TVR OS 1.0.4 and earlier; Synology PHP 7.3 to 8.4 packages, Mail Station and Synology Calendar"
    fixed: "QTS 6.1.0.3656 and 5.2.11.3661, QuTS hero h6.1.0.3656, h6.0.2.3656 and h5.2.11.3661, QuTScloud c5.2.9.3661 (builds of 2026-10-23); no fix yet for Note Station 3, QNE, QVR Surveillance or TVR OS as of 2026-10-25, and no fix row for QuMagie; Synology PHP 7.4.33-0131, 8.0.30-0122, 8.1.34-0120, 8.2.35-0171, 8.3.36-0051, 8.4.27-0051, Mail Station 30000002.3.19-20333 and Calendar 3.0.4-21435, no fix for the end-of-life PHP 7.3 package"
  - id: CVE-2026-109619
    cvss: "9.2 (CVSS 4.0, as stated by QNAP for the PHP flaw)"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "QTS 6.1.0 and 5.2.11 and earlier, QuTS hero h6.1.0, h6.0.x and h5.2.11 and earlier, QuTScloud c5.2.9 and earlier, QuMagie 2.10.1 and earlier, Note Station 3 3.9.14 and earlier, QNE (ADRA) 1.0.7 and earlier, QVR Surveillance 3.0.3 and earlier (ARM32 models), TVR OS 1.0.4 and earlier; Synology PHP 7.3 to 8.4 packages, Mail Station and Synology Calendar"
    fixed: "QTS 6.1.0.3656 and 5.2.11.3661, QuTS hero h6.1.0.3656, h6.0.2.3656 and h5.2.11.3661, QuTScloud c5.2.9.3661 (builds of 2026-10-23); no fix yet for Note Station 3, QNE, QVR Surveillance or TVR OS as of 2026-10-25, and no fix row for QuMagie; Synology PHP 7.4.33-0131, 8.0.30-0122, 8.1.34-0120, 8.2.35-0171, 8.3.36-0051, 8.4.27-0051, Mail Station 30000002.3.19-20333 and Calendar 3.0.4-21435, no fix for the end-of-life PHP 7.3 package"
sources:
  - url: "https://www.qnap.com/en/security-advisory/qsa-26-18"
    publisher: "QNAP PSIRT (QSA-26-18, revision V1.1)"
    date: "2026-10-24"
    role: primary
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
  exploitation attempts against the PHP flaws in general, and its advisory reports none against QNAP products.
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
  - "Update every QNAP NAS on QTS, QuTS hero or QuTScloud to the builds of 2026-10-23 (QTS 6.1.0.3656 or 5.2.11.3661, QuTS hero h6.1.0.3656, h6.0.2.3656 or h5.2.11.3661, QuTScloud c5.2.9.3661), and take any QNAP device running Note Station 3, QNE, QVR Surveillance, TVR OS or QuMagie off the internet until QNAP lists a fix."
updates: []
migrated_from: null
---

QNAP's advisory QSA-26-18 says the PHP2Shell flaws CVE-2026-109618 and CVE-2026-109619 (CVSS 4.0 9.2) affect the PHP used in the web components of its operating systems and several of its applications, can be triggered before any application-level authentication, and could let an unauthenticated remote attacker execute code on the device ([QNAP, 2026-10-24](https://www.qnap.com/en/security-advisory/qsa-26-18)). Its revision of 2026-10-24 lists fixed builds dated 2026-10-23 for QTS (6.1.0.3656 and 5.2.11.3661), QuTS hero (h6.1.0.3656, h6.0.2.3656 and h5.2.11.3661) and QuTScloud (c5.2.9.3661), while Note Station 3 3.9.14 and earlier, QNE (ADRA) 1.0.7 and earlier, QVR Surveillance 3.0.3 and earlier on ARM32 models and TVR OS 1.0.4 and earlier are still being fixed with no date announced, and QuMagie 2.10.1 and earlier is named as affected without a row in the fix table ([QNAP, 2026-10-24](https://www.qnap.com/en/security-advisory/qsa-26-18)). QNAP's PSIRT says it has observed scanning and exploitation attempts against the flaws in the wild and blocked attempts against its own website, online store and cloud services ([QNAP, 2026-10-22](https://www.qnap.com/en/security-news/2026/qnap-statement-on-critical-php-vulnerabilities-php2shell-assessment-and-mitigation-guidance)), and its advisory says it has received no reports of exploitation targeting QNAP products ([QNAP, 2026-10-24](https://www.qnap.com/en/security-advisory/qsa-26-18)). PHP inside Container Station containers or third-party applications is not covered by QNAP's updates ([QNAP, 2026-10-24](https://www.qnap.com/en/security-advisory/qsa-26-18)).

Synology's advisory Synology-SA-26:14 rates its PHP 7.3 to 8.4 packages, Mail Station and Synology Calendar critical and lists fixed releases for each except the end-of-life PHP 7.3 package, which gets no fix; Synology says the PHP built into DSM is not exposed to external attack surfaces and considers the risk of exploitation very low ([Synology, 2026-10-22](https://www.synology.com/security/advisory/Synology_SA_26_14)).

**Exposure:** a QNAP NAS on QTS, QuTS hero or QuTScloud below the fixed builds, or a QNAP device running Note Station 3, QNE (ADRA), QVR Surveillance, TVR OS or QuMagie, whose management or web ports are reachable from outside, which QNAP ties to router port forwarding, UPnP and myQNAPcloud publishing; the management ports default to 8080 and 443 ([QNAP, 2026-10-24](https://www.qnap.com/en/security-advisory/qsa-26-18)). On Synology, a DSM with one of the listed PHP packages, Mail Station or Calendar installed ([Synology, 2026-10-22](https://www.synology.com/security/advisory/Synology_SA_26_14)).

**Detection:** QNAP's compromise check is a review of QuLog Center for unexpected logins or access and a Security Center and Malware Remover scan with current definitions; if compromise is suspected it says to disconnect the device and change all passwords ([QNAP, 2026-10-24](https://www.qnap.com/en/security-advisory/qsa-26-18)).

**Defender takeaway:** update QTS, QuTS hero and QuTScloud now; for the QNAP products without a fix, remove internet exposure (port forwarding, UPnP, myQNAPcloud publishing), use a VPN for remote access and allow the management ports only from trusted subnets, which QNAP says reduces exposure without fixing the flaws and does not protect against local devices that are already compromised ([QNAP, 2026-10-24](https://www.qnap.com/en/security-advisory/qsa-26-18)). On Synology, update the listed packages; the PHP 7.3 package gets no fix ([Synology, 2026-10-22](https://www.synology.com/security/advisory/Synology_SA_26_14)).
