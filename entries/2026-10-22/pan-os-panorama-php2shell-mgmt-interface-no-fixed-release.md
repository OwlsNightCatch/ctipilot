---
schema: 1
kind: vulnerability
title: "CVE-2026-109618 / CVE-2026-109619, Palo Alto Networks PAN-OS and Panorama: the PHP2Shell flaws affect every release, reaching PAN-OS through its management web interface; eleven hotfixes are out and the rest are due by 2026-10-30"
headline: "Palo Alto: eleven PAN-OS hotfixes for PHP2Shell are out, nine still due by 30 October; CISA now lists the PHP flaws"
summary: >
  Palo Alto Networks' advisory of 2026-10-21, revised on 2026-10-27, lists every release of PAN-OS 12.2, 12.1, 11.2, 11.1 and 10.2 and of
  Panorama as affected by the PHP flaws CVE-2026-109618 and CVE-2026-109619 through the management web interface (the HTTPS web UI and the
  XML API service). Eleven hotfixes are released (10.2.13-h27, 10.2.16-h12, 10.2.18-h13, 11.1.4-h38, 11.1.6-h40, 11.1.10-h36, 11.1.13-h16,
  11.1.16-h4, 11.2.10-h16, 12.1.7-h11 and 12.2.4-h1) and nine others carry estimated dates up to 2026-10-30. Palo Alto scores the
  PAN-OS impact as availability only (CVSS-B 8.7 with management reachable from the internet, 7.1 behind a jump box) and knows of no
  malicious exploitation against its products, although CISA added both PHP flaws to its Known Exploited Vulnerabilities catalog on
  2026-10-26; GlobalProtect and the captive portal are not affected.
discovered_at: "2026-10-22T03:41:00Z"
updated_at: "2026-10-27T05:15:00Z"
event_date: "2026-10-21"
run_id: 2026-10-22T0256Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, rce, pre-auth, cisa-kev, patch-available]
regions: [global]
sectors: []
entities: ["product:php", "product:palo-alto-networks-pan-os", "product:palo-alto-networks-panorama"]
techniques: [T1190]
affected_products: ["Palo Alto Networks PAN-OS", "Palo Alto Networks Panorama"]
cves:
  - id: CVE-2026-109618
    cvss: "8.7 (CVSS-B 4.0, Palo Alto's rating of the PAN-OS impact, availability only)"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [cisa-kev, patch-available, mitigation-only]
    affected: "PAN-OS 12.2, 12.1, 11.2, 11.1 and 10.2 (all releases); Panorama (PAN-OS software on virtual and M-Series appliances; the advisory table has no separate Panorama row); WildFire Appliance WF-500 and WF-500-B are listed as unaffected after the correction of 2026-10-23"
    fixed: "Released per the advisory's revisions of 2026-10-25 to 2026-10-27: 10.2.13-h27, 10.2.16-h12, 10.2.18-h13, 11.1.4-h38, 11.1.6-h40, 11.1.10-h36, 11.1.13-h16, 11.1.16-h4, 11.2.10-h16 (11.2.10-h17 adds the Brotli fix), 12.1.7-h11 and 12.2.4-h1; estimated dates: 12.1.4-h13 (10/29), 12.1.10-h3 (10/30); 11.2.4-h23 (10/30), 11.2.7-h23 (10/29), 11.2.13-h4 (10/27), 11.2.16-h1 (10/28); 11.1.7-h12 (10/30); 10.2.7-h39 (10/30), 10.2.10-h42 (10/29); Panorama: the table no longer distinguishes it from the PAN-OS trains"
  - id: CVE-2026-109619
    cvss: "8.7 (CVSS-B 4.0, Palo Alto's rating of the PAN-OS impact, availability only)"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [cisa-kev, patch-available, mitigation-only]
    affected: "PAN-OS 12.2, 12.1, 11.2, 11.1 and 10.2 (all releases); Panorama (PAN-OS software on virtual and M-Series appliances; the advisory table has no separate Panorama row); WildFire Appliance WF-500 and WF-500-B are listed as unaffected after the correction of 2026-10-23"
    fixed: "Released per the advisory's revisions of 2026-10-25 to 2026-10-27: 10.2.13-h27, 10.2.16-h12, 10.2.18-h13, 11.1.4-h38, 11.1.6-h40, 11.1.10-h36, 11.1.13-h16, 11.1.16-h4, 11.2.10-h16 (11.2.10-h17 adds the Brotli fix), 12.1.7-h11 and 12.2.4-h1; estimated dates: 12.1.4-h13 (10/29), 12.1.10-h3 (10/30); 11.2.4-h23 (10/30), 11.2.7-h23 (10/29), 11.2.13-h4 (10/27), 11.2.16-h1 (10/28); 11.1.7-h12 (10/30); 10.2.7-h39 (10/30), 10.2.10-h42 (10/29); Panorama: the table no longer distinguishes it from the PAN-OS trains"
sources:
  - url: "https://security.paloaltonetworks.com/CVE-2026-109618"
    publisher: "Palo Alto Networks PSIRT (advisory, Impact of Critical Vulnerabilities in PHP on Palo Alto Networks Products)"
    date: "2026-10-21"
    role: primary
  - url: "https://security.paloaltonetworks.com/CVE-2026-109618"
    publisher: "Palo Alto Networks PSIRT (advisory, revised 2026-10-23)"
    date: "2026-10-23"
    role: primary
  - url: "https://security.paloaltonetworks.com/CVE-2026-109618"
    publisher: "Palo Alto Networks PSIRT (advisory, revised 2026-10-24)"
    date: "2026-10-24"
    role: primary
  - url: "https://security.paloaltonetworks.com/CVE-2026-109618"
    publisher: "Palo Alto Networks PSIRT (advisory, revised 2026-10-25)"
    date: "2026-10-25"
    role: primary
  - url: "https://security.paloaltonetworks.com/json/CVE-2026-109618"
    publisher: "Palo Alto Networks PSIRT (advisory record with revision history)"
    date: "2026-10-25"
    role: primary
  - url: "https://security.paloaltonetworks.com/CVE-2026-109618"
    publisher: "Palo Alto Networks PSIRT (advisory, revised 2026-10-27)"
    date: "2026-10-27"
    role: primary
  - url: "https://security.paloaltonetworks.com/json/CVE-2026-109618"
    publisher: "Palo Alto Networks PSIRT (advisory record with revision history, 2026-10-27)"
    date: "2026-10-27"
    role: primary
  - url: "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    publisher: "CISA Known Exploited Vulnerabilities catalog (version 2026.10.26)"
    date: "2026-10-26"
    role: corroborating
  - url: "https://unit42.paloaltonetworks.com/cve-2026-109618-cve-2026-109619/"
    publisher: "Palo Alto Networks Unit 42 (threat brief, revised 2026-10-25)"
    date: "2026-10-25"
    role: corroborating
  - url: "https://www.php.net/archive/2026.php#2026-10-21-5"
    publisher: "PHP (security advisory)"
    date: "2026-10-21"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Current analysis shows no impact of CVE-2026-115560 on PAN-OS (NGFW and Panorama)."
    publisher: "Palo Alto Networks PSIRT (advisory, revised 2026-10-25)"
    source_url: "https://security.paloaltonetworks.com/CVE-2026-109618"
  - quote: "This issue will be fixed in the upcoming releases of PAN-OS."
    publisher: "Palo Alto Networks PSIRT (advisory, revised 2026-10-25)"
    source_url: "https://security.paloaltonetworks.com/CVE-2026-109618"
  - quote: "removed the ETA for 10.2.18-h13, 11.1.16-h4 and 11.2.10-h16 as these versions are released"
    publisher: "Palo Alto Networks PSIRT (advisory record with revision history)"
    source_url: "https://security.paloaltonetworks.com/json/CVE-2026-109618"
  - quote: "Removed the ETAs for 10.2.13-h27 and 10.2.16-h12 as these versions are released."
    publisher: "Palo Alto Networks PSIRT (advisory record with revision history, 2026-10-27)"
    source_url: "https://security.paloaltonetworks.com/json/CVE-2026-109618"
  - quote: "The only exception is 11.2.10-h16 which only includes the fix for PHP vulnerabilities; 11.2.10-h17 includes fixes for both vulnerabilities."
    publisher: "Palo Alto Networks PSIRT (advisory, revised 2026-10-27)"
    source_url: "https://security.paloaltonetworks.com/CVE-2026-109618"
  - quote: "This issue strictly affects the management web interface, which includes the HTTPS web UI and XML API service."
    publisher: "Palo Alto Networks PSIRT (advisory, Impact of Critical Vulnerabilities in PHP on Palo Alto Networks Products)"
    source_url: "https://security.paloaltonetworks.com/CVE-2026-109618"
  - quote: "This issue will be fixed in the upcoming releases of PAN-OS."
    publisher: "Palo Alto Networks PSIRT (advisory, Impact of Critical Vulnerabilities in PHP on Palo Alto Networks Products)"
    source_url: "https://security.paloaltonetworks.com/CVE-2026-109618"
  - quote: "Palo Alto Networks is not aware of any malicious exploitation of this issue against our products."
    publisher: "Palo Alto Networks PSIRT (advisory, Impact of Critical Vulnerabilities in PHP on Palo Alto Networks Products)"
    source_url: "https://security.paloaltonetworks.com/CVE-2026-109618"
  - quote: "No special configuration is required to be affected by this issue."
    publisher: "Palo Alto Networks PSIRT (advisory, Impact of Critical Vulnerabilities in PHP on Palo Alto Networks Products)"
    source_url: "https://security.paloaltonetworks.com/CVE-2026-109618"
  - quote: "Although WildFire Cloud was previously impacted, a remediation patch was deployed on October 22, 2026."
    publisher: "Palo Alto Networks PSIRT (advisory, revised 2026-10-23)"
    source_url: "https://security.paloaltonetworks.com/CVE-2026-109618"
  - quote: "This issue is applicable to PAN-OS software on PA-Series and VM-Series firewalls and on Panorama (virtual and M-Series)."
    publisher: "Palo Alto Networks PSIRT (advisory, revised 2026-10-24)"
    source_url: "https://security.paloaltonetworks.com/CVE-2026-109618"
verification: single-source
sourcing_note: >
  Palo Alto Networks' advisory is the first-party record for its own products and the only source for the PAN-OS and Panorama
  impact. The two flaws themselves are described by the PHP project. On 2026-10-25 the
  advisory's revision history calls 10.2.18-h13, 11.1.16-h4 and 11.2.10-h16 released while its unrevised solution text still
  speaks of upcoming releases. The listing of both PHP flaws in CISA's Known Exploited Vulnerabilities catalog comes from the catalog itself.
confidence: high
references:
  - "2026-10-21/php-critical-release-pre-announced-cve-2026-109618-109619"
  - "2026-10-15/cve-2026-0322-pan-os-management-interface-code-injection"
  - "2026-05-30/cve-2026-0257-palo-alto-pan-os-globalprotect-pre-auth-authen"
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Install the released hotfix for your maintenance release on every PA-Series and VM-Series firewall and Panorama: 10.2.13-h27, 10.2.16-h12, 10.2.18-h13, 11.1.4-h38, 11.1.6-h40, 11.1.10-h36, 11.1.13-h16, 11.1.16-h4, 11.2.10-h16 (11.2.10-h17 adds the Brotli fix), 12.1.7-h11 or 12.2.4-h1; for every other release, restrict the management interface to a jump box or trusted internal addresses, Palo Alto's recommended mitigation, until its hotfix ships, due 2026-10-27 to 2026-10-30."
updates:
  - at: "2026-10-23T03:42:16Z"
    run_id: 2026-10-23T0256Z-intel
    type: update
    summary: >
      Palo Alto Networks' revised advisory now also lists the WildFire appliances WF-500 and WF-500-B as
      affected by the PHP flaws in all versions, schedules hotfix builds of every PAN-OS train between
      2026-10-26 and 2026-10-30, and leaves Panorama and WF-500 undated; Cortex XCORE (SaaS) and WildFire
      Cloud are already remediated.
    fields: [title, headline, summary, entities, affected_products, cves, sources, evidence, body]
  - at: "2026-10-24T03:37:34Z"
    run_id: 2026-10-24T0255Z-intel
    type: update
    summary: >
      Palo Alto Networks' advisory now lists the WildFire appliances WF-500 and WF-500-B as unaffected, a
      correction its timeline dates 2026-10-23, has no separate Panorama row while a note keeps Panorama
      in scope, and extends the Threat Prevention coverage; the PAN-OS hotfix dates of 2026-10-26 to
      2026-10-30 and the exploitation statement are unchanged.
    fields: [affected_products, body, cves, entities, evidence, headline, sources, summary, title]
  - at: "2026-10-25T14:00:17Z"
    run_id: 2026-10-25T1308Z-audit
    type: update
    summary: >
      Palo Alto's revision of 2026-10-25 lists the first three PAN-OS hotfixes (10.2.18-h13, 11.1.16-h4,
      11.2.10-h16) as released, although its solution text still speaks of upcoming releases; the
      remaining hotfixes are due 2026-10-27 to 2026-10-30, and Palo Alto's current analysis finds no
      impact of CVE-2026-115560 on PAN-OS.
    fields: [title, headline, summary, cves, sources, evidence, body, tags, sourcing_note]
  - at: "2026-10-26T03:40:53Z"
    run_id: 2026-10-26T0256Z-intel
    type: correction
    summary: >
      The entry said Unit 42 had seen a proof of concept of the PHP flaws; Unit 42's brief, revised on
      2026-10-25, no longer says so, and the statement is removed.
    fields: [body, evidence, sources, sourcing_note]
  - at: "2026-10-27T05:15:00Z"
    run_id: 2026-10-27T0256Z-intel
    type: update
    summary: >
      Palo Alto Networks now records eleven PAN-OS hotfixes as released (10.2.13-h27, 10.2.16-h12,
      10.2.18-h13, 11.1.4-h38, 11.1.6-h40, 11.1.10-h36, 11.1.13-h16, 11.1.16-h4, 11.2.10-h16, 12.1.7-h11
      and 12.2.4-h1) with nine others due by 2026-10-30; CISA added both PHP flaws to its Known Exploited
      Vulnerabilities catalog on 2026-10-26, while Palo Alto still reports no malicious exploitation
      against its products.
    fields: [actions, body, cves, evidence, headline, sources, sourcing_note, summary, tags, title]
migrated_from: null
---

Palo Alto Networks' advisory of 2026-10-21 lists every release of PAN-OS 12.2, 12.1, 11.2, 11.1 and 10.2 and of Panorama as affected by CVE-2026-109618 and CVE-2026-109619, with no fixed build released at the time ([Palo Alto Networks, 2026-10-21](https://security.paloaltonetworks.com/CVE-2026-109618)); the revision of 2026-10-23 gave estimated dates from 2026-10-26 to 2026-10-30 for hotfix builds of every PAN-OS train and noted that Cortex XCORE (SaaS) and WildFire Cloud were remediated on 2026-10-21 and 2026-10-22 ([Palo Alto Networks, 2026-10-23](https://security.paloaltonetworks.com/CVE-2026-109618)). The advisory's timeline dates a correction of the WildFire appliances WF-500 and WF-500-B to 2026-10-23, and the table now lists them as unaffected, although the revision that morning had listed them as affected; the table no longer distinguishes Panorama, a note says the issue applies to PAN-OS software on PA-Series and VM-Series firewalls and on Panorama (virtual and M-Series), and the mitigation text covers PAN-OS and Panorama together ([Palo Alto Networks, 2026-10-24](https://security.paloaltonetworks.com/CVE-2026-109618)). The revision of 2026-10-24 added updated threat-signature and content-version details ([Palo Alto Networks, 2026-10-24](https://security.paloaltonetworks.com/CVE-2026-109618)). The two flaws are the unauthenticated remote-code-execution bugs in the PHP runtime that the PHP project fixed in its releases of the same day ([PHP, 2026-10-21](https://www.php.net/archive/2026.php#2026-10-21-5)). Palo Alto says no special configuration is required to be affected, that the issue strictly affects the management web interface, which includes the HTTPS web UI and the XML API service, and that a dataplane interface is affected only where a management profile is attached to it ([Palo Alto Networks, 2026-10-21](https://security.paloaltonetworks.com/CVE-2026-109618)). It states that the GlobalProtect portal and gateway and the captive portal are not impacted ([Palo Alto Networks, 2026-10-21](https://security.paloaltonetworks.com/CVE-2026-109618)).

Palo Alto describes the flaws as remote code execution but scores their impact on its own product CVSS-B 8.7 (severity high, urgency moderate), with high availability impact and none on confidentiality or integrity, against a vendor-level 9.2 with high impact on all three, and says the risk is highest where management access is allowed from external addresses on the internet; restricting management to a single jump box lowers its rating to 7.1, and it is not aware of any malicious exploitation against its products ([Palo Alto Networks, 2026-10-21](https://security.paloaltonetworks.com/CVE-2026-109618)). Until fixes ship, Palo Alto recommends restricting management access to trusted internal addresses and offers Threat Prevention coverage (Threat IDs 543004 and 97622 to 97625 and twenty further IDs from 97643 to 97678, Applications and Threats content versions 9162, 9163, 9164 and later) that applies only when management traffic is routed through a dataplane interface, the certificate for inbound management traffic has been replaced, inbound management traffic is decrypted so the firewall can inspect it, and threat prevention is enabled on that traffic ([Palo Alto Networks, 2026-10-24](https://security.paloaltonetworks.com/CVE-2026-109618)).

**Exposure:** every PAN-OS firewall and Panorama appliance below its train's hotfix, whatever the configuration, through its management web interface; the service is reachable from the internet where the management port, or a dataplane interface carrying a management profile, answers HTTPS or XML API requests from outside the administrator range ([Palo Alto Networks, 2026-10-21](https://security.paloaltonetworks.com/CVE-2026-109618)).

**Detection:** in management-plane access and system logs, any request from an address outside the administrator range, though Palo Alto does not say which logs record request bodies; in threat logs, hits on the Threat IDs above where the signatures are active and the four conditions hold. Palo Alto publishes no flaw-specific indicator and reports no exploitation of its products, so no post-compromise check is defined yet ([Palo Alto Networks, 2026-10-21](https://security.paloaltonetworks.com/CVE-2026-109618)).

**Defender takeaway:** move management access behind a jump box or trusted internal addresses now, on Panorama as on PAN-OS, and remove management profiles from dataplane interfaces that face untrusted networks; Palo Alto lists no workaround beyond that restriction and the Threat Prevention coverage. Install the hotfix released for your maintenance line (10.2.13, 10.2.16, 10.2.18, 11.1.4, 11.1.6, 11.1.10, 11.1.13, 11.1.16, 11.2.10, 12.1.7 or 12.2.4) ([Palo Alto Networks, 2026-10-27](https://security.paloaltonetworks.com/json/CVE-2026-109618)) and the other trains' hotfixes as they ship by 2026-10-30 ([Palo Alto Networks, 2026-10-27](https://security.paloaltonetworks.com/CVE-2026-109618)).

## Update — 2026-10-23T03:42:16Z

Palo Alto Networks revised its advisory on 2026-10-23: the WildFire appliances WF-500 and WF-500-B are now listed as affected in all versions, and the footnotes say Cortex XCORE (SaaS) was remediated on 2026-10-21 and WildFire Cloud on 2026-10-22 ([Palo Alto Networks, 2026-10-23](https://security.paloaltonetworks.com/CVE-2026-109618)). The advisory now also gives estimated availability dates for hotfix builds of every supported PAN-OS train, from 2026-10-26 (for example 10.2.18-h13, 11.1.16-h4 and 11.2.10-h16) to 2026-10-30, while Panorama and the WildFire appliances remain with no date ([Palo Alto Networks, 2026-10-23](https://security.paloaltonetworks.com/CVE-2026-109618)). Palo Alto still states that it is not aware of malicious exploitation against its products, and the Threat Prevention coverage and the jump-box restriction are unchanged ([Palo Alto Networks, 2026-10-23](https://security.paloaltonetworks.com/CVE-2026-109618)). The advisory names the management web interface only for PAN-OS and does not say which interface of the WildFire appliances is reachable.

## Update — 2026-10-24T03:37:34Z

Palo Alto Networks' advisory now lists the WildFire appliances WF-500 and WF-500-B, which an earlier revision of 2026-10-23 had listed as affected, as unaffected, a correction its timeline dates 2026-10-23, and the table no longer distinguishes Panorama while a note says the issue applies to PAN-OS software on PA-Series and VM-Series firewalls and on Panorama (virtual and M-Series) and the mitigation text covers PAN-OS and Panorama together ([Palo Alto Networks, 2026-10-24](https://security.paloaltonetworks.com/CVE-2026-109618)). The estimated hotfix dates for PAN-OS, 2026-10-26 to 2026-10-30, the CVSS-B scores of 8.7 and 7.1, and the statement that Palo Alto Networks is not aware of malicious exploitation against its products are unchanged; on 2026-10-24 the advisory added updated threat-signature and content-version details, and the Threat Prevention coverage now lists twenty further Threat IDs, from 97643 to 97678 ([Palo Alto Networks, 2026-10-24](https://security.paloaltonetworks.com/CVE-2026-109618)).

## Update — 2026-10-25T14:00:17Z

Palo Alto Networks' revision of 2026-10-25 removed the estimated dates of 10.2.18-h13, 11.1.16-h4 and 11.2.10-h16 "as these versions are released" ([Palo Alto Networks, 2026-10-25](https://security.paloaltonetworks.com/json/CVE-2026-109618)); the advisory's solution text, unrevised, still says the issue will be fixed in upcoming releases of PAN-OS, and every other hotfix carries an estimated date from 2026-10-27 to 2026-10-30 ([Palo Alto Networks, 2026-10-25](https://security.paloaltonetworks.com/CVE-2026-109618)). The FAQ adds that Palo Alto's current analysis shows no impact on PAN-OS firewalls or Panorama of CVE-2026-115560, the new vulnerability PHP announced, and Palo Alto still knows of no malicious exploitation against its products ([Palo Alto Networks, 2026-10-25](https://security.paloaltonetworks.com/CVE-2026-109618)).

## Correction — 2026-10-26T03:40:53Z

Unit 42's brief, revised on 2026-10-25, no longer says that it has seen a proof of concept of the PHP flaws ([Unit 42, 2026-10-25](https://unit42.paloaltonetworks.com/cve-2026-109618-cve-2026-109619/)).

## Update — 2026-10-27T05:15:00Z

Palo Alto Networks' advisory now records eleven PAN-OS hotfixes as released: 10.2.18-h13, 11.1.16-h4 and 11.2.10-h16 (revision of 2026-10-25), 11.1.4-h38, 11.1.6-h40, 11.1.10-h36 and 11.1.13-h16 (2026-10-26), and 10.2.13-h27, 10.2.16-h12, 12.1.7-h11 and 12.2.4-h1 (2026-10-27) ([Palo Alto Networks, 2026-10-27](https://security.paloaltonetworks.com/json/CVE-2026-109618)). Nine hotfixes still carry estimated dates from 2026-10-27 to 2026-10-30, among them 12.1.4-h13, 12.1.10-h3 and four 11.2 lines, and the FAQ says 11.2.10-h16 carries only the PHP fix while 11.2.10-h17 carries the PHP and the Brotli fixes ([Palo Alto Networks, 2026-10-27](https://security.paloaltonetworks.com/CVE-2026-109618)). Palo Alto still says it is not aware of malicious exploitation of this issue against its products ([Palo Alto Networks, 2026-10-27](https://security.paloaltonetworks.com/CVE-2026-109618)). CISA added both PHP flaws to its Known Exploited Vulnerabilities catalog on 2026-10-26, as the PHP flaws themselves rather than as a PAN-OS finding ([CISA KEV, 2026-10-26](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)).
