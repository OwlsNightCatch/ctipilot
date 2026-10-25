---
schema: 1
kind: vulnerability
title: "CVE-2026-109618 / CVE-2026-109619, Palo Alto Networks PAN-OS and Panorama: the PHP2Shell flaws affect every release, reaching PAN-OS through its management web interface; the first PAN-OS hotfixes are out and the rest are due by 2026-10-30"
headline: "Palo Alto: PHP2Shell affects PAN-OS and Panorama; first PAN-OS hotfixes out, the rest due by 30 October"
summary: >
  Palo Alto Networks' advisory of 2026-10-21, revised on 2026-10-25, lists every release of PAN-OS 12.2, 12.1, 11.2, 11.1 and 10.2 as
  affected by the two PHP runtime flaws, CVE-2026-109618 and CVE-2026-109619, and notes that the issue applies to PAN-OS software on
  PA-Series and VM-Series firewalls and on Panorama; its revision of 2026-10-25 lists 10.2.18-h13, 11.1.16-h4 and 11.2.10-h16 as released (the solution text still
  speaks of upcoming releases), the other hotfixes carry estimated dates from 2026-10-27 to 2026-10-30, and the table no longer distinguishes Panorama, which the note and the mitigation text cover together with PAN-OS. The WildFire appliances WF-500 and WF-500-B, which an earlier revision of
  2026-10-23 listed as affected, are now listed as unaffected after a correction its timeline dates 2026-10-23. Cortex XCORE (SaaS) and WildFire Cloud were already remediated. The PAN-OS exposure is the
  management web interface (the HTTPS web UI and the XML API service); Palo Alto scores the PAN-OS impact as availability only,
  CVSS-B 8.7 where management is reachable from the internet and 7.1 behind a jump box, against 9.2 for the PHP flaws themselves,
  and knows of no malicious exploitation against its products; its analysis finds no impact of CVE-2026-115560, the new PHP flaw,
  on PAN-OS. GlobalProtect and the captive portal are not affected.
discovered_at: "2026-10-22T03:41:00Z"
updated_at: "2026-10-25T14:00:17Z"
event_date: "2026-10-21"
run_id: 2026-10-22T0256Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, rce, pre-auth, patch-available]
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
    status: [patch-available, mitigation-only]
    affected: "PAN-OS 12.2, 12.1, 11.2, 11.1 and 10.2 (all releases); Panorama (PAN-OS software on virtual and M-Series appliances; the advisory table has no separate Panorama row); WildFire Appliance WF-500 and WF-500-B are listed as unaffected after the correction of 2026-10-23"
    fixed: "10.2.18-h13, 11.1.16-h4 and 11.2.10-h16, listed as released in the advisory's revision of 2026-10-25; the remaining hotfix ETAs: 12.2.4-h1 (10/28); 12.1.4-h13 (10/29), 12.1.7-h11 (10/28), 12.1.10-h3 (10/30); 11.2.4-h23 (10/30), 11.2.7-h23 (10/29), 11.2.10-h16 (released), 11.2.13-h4 (10/27), 11.2.16-h1 (10/28); 11.1.4-h38 (10/29), 11.1.6-h40 (10/29), 11.1.7-h12 (10/30), 11.1.10-h36 (10/28), 11.1.13-h16 (10/27), 11.1.16-h4 (released); 10.2.7-h39 (10/30), 10.2.10-h42 (10/29), 10.2.13-h27 (10/27), 10.2.16-h12 (10/28), 10.2.18-h13 (released); Panorama: the table no longer distinguishes it from the PAN-OS trains"
  - id: CVE-2026-109619
    cvss: "8.7 (CVSS-B 4.0, Palo Alto's rating of the PAN-OS impact, availability only)"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available, mitigation-only]
    affected: "PAN-OS 12.2, 12.1, 11.2, 11.1 and 10.2 (all releases); Panorama (PAN-OS software on virtual and M-Series appliances; the advisory table has no separate Panorama row); WildFire Appliance WF-500 and WF-500-B are listed as unaffected after the correction of 2026-10-23"
    fixed: "10.2.18-h13, 11.1.16-h4 and 11.2.10-h16, listed as released in the advisory's revision of 2026-10-25; the remaining hotfix ETAs: 12.2.4-h1 (10/28); 12.1.4-h13 (10/29), 12.1.7-h11 (10/28), 12.1.10-h3 (10/30); 11.2.4-h23 (10/30), 11.2.7-h23 (10/29), 11.2.10-h16 (released), 11.2.13-h4 (10/27), 11.2.16-h1 (10/28); 11.1.4-h38 (10/29), 11.1.6-h40 (10/29), 11.1.7-h12 (10/30), 11.1.10-h36 (10/28), 11.1.13-h16 (10/27), 11.1.16-h4 (released); 10.2.7-h39 (10/30), 10.2.10-h42 (10/29), 10.2.13-h27 (10/27), 10.2.16-h12 (10/28), 10.2.18-h13 (released); Panorama: the table no longer distinguishes it from the PAN-OS trains"
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
  - url: "https://unit42.paloaltonetworks.com/cve-2026-109618-cve-2026-109619/"
    publisher: "Palo Alto Networks Unit 42 (threat brief)"
    date: "2026-10-21"
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
  - quote: "Unit 42 has seen proof of concept of these vulnerabilities."
    publisher: "Palo Alto Networks Unit 42 (threat brief)"
    source_url: "https://unit42.paloaltonetworks.com/cve-2026-109618-cve-2026-109619/"
  - quote: "Although WildFire Cloud was previously impacted, a remediation patch was deployed on October 22, 2026."
    publisher: "Palo Alto Networks PSIRT (advisory, revised 2026-10-23)"
    source_url: "https://security.paloaltonetworks.com/CVE-2026-109618"
  - quote: "This issue is applicable to PAN-OS software on PA-Series and VM-Series firewalls and on Panorama (virtual and M-Series)."
    publisher: "Palo Alto Networks PSIRT (advisory, revised 2026-10-24)"
    source_url: "https://security.paloaltonetworks.com/CVE-2026-109618"
verification: single-source
sourcing_note: >
  Palo Alto Networks' advisory is the first-party record for its own products and the only source for the PAN-OS and Panorama
  impact; Unit 42 is the same vendor's brief. The two flaws themselves are described by the PHP project. On 2026-10-25 the
  advisory's revision history calls 10.2.18-h13, 11.1.16-h4 and 11.2.10-h16 released while its unrevised solution text still
  speaks of upcoming releases.
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
actions: []
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
migrated_from: null
---

Palo Alto Networks' advisory of 2026-10-21 lists every release of PAN-OS 12.2, 12.1, 11.2, 11.1 and 10.2 and of Panorama as affected by CVE-2026-109618 and CVE-2026-109619, with no fixed build released at the time ([Palo Alto Networks, 2026-10-21](https://security.paloaltonetworks.com/CVE-2026-109618)); the revision of 2026-10-23 gave estimated dates from 2026-10-26 to 2026-10-30 for hotfix builds of every PAN-OS train and noted that Cortex XCORE (SaaS) and WildFire Cloud were remediated on 2026-10-21 and 2026-10-22 ([Palo Alto Networks, 2026-10-23](https://security.paloaltonetworks.com/CVE-2026-109618)). The advisory's timeline dates a correction of the WildFire appliances WF-500 and WF-500-B to 2026-10-23, and the table now lists them as unaffected, although the revision that morning had listed them as affected; the table no longer distinguishes Panorama, a note says the issue applies to PAN-OS software on PA-Series and VM-Series firewalls and on Panorama (virtual and M-Series), and the mitigation text covers PAN-OS and Panorama together ([Palo Alto Networks, 2026-10-24](https://security.paloaltonetworks.com/CVE-2026-109618)). The revision of 2026-10-24 added updated threat-signature and content-version details ([Palo Alto Networks, 2026-10-24](https://security.paloaltonetworks.com/CVE-2026-109618)). The two flaws are the unauthenticated remote-code-execution bugs in the PHP runtime that the PHP project fixed in its releases of the same day ([PHP, 2026-10-21](https://www.php.net/archive/2026.php#2026-10-21-5)). Palo Alto says no special configuration is required to be affected, that the issue strictly affects the management web interface, which includes the HTTPS web UI and the XML API service, and that a dataplane interface is affected only where a management profile is attached to it ([Palo Alto Networks, 2026-10-21](https://security.paloaltonetworks.com/CVE-2026-109618)). It states that the GlobalProtect portal and gateway and the captive portal are not impacted ([Palo Alto Networks, 2026-10-21](https://security.paloaltonetworks.com/CVE-2026-109618)).

Palo Alto describes the flaws as remote code execution but scores their impact on its own product CVSS-B 8.7 (severity high, urgency moderate), with high availability impact and none on confidentiality or integrity, against a vendor-level 9.2 with high impact on all three, and says the risk is highest where management access is allowed from external addresses on the internet; restricting management to a single jump box lowers its rating to 7.1, and it is not aware of any malicious exploitation against its products ([Palo Alto Networks, 2026-10-21](https://security.paloaltonetworks.com/CVE-2026-109618)). Unit 42 says it has seen proof of concept of the PHP flaws ([Unit 42, 2026-10-21](https://unit42.paloaltonetworks.com/cve-2026-109618-cve-2026-109619/)). Until fixes ship, Palo Alto recommends restricting management access to trusted internal addresses and offers Threat Prevention coverage (Threat IDs 543004 and 97622 to 97625 and twenty further IDs from 97643 to 97678, Applications and Threats content versions 9162, 9163, 9164 and later) that applies only when management traffic is routed through a dataplane interface, the certificate for inbound management traffic has been replaced, inbound management traffic is decrypted so the firewall can inspect it, and threat prevention is enabled on that traffic ([Palo Alto Networks, 2026-10-24](https://security.paloaltonetworks.com/CVE-2026-109618)).

**Exposure:** every PAN-OS firewall and Panorama appliance below its train's hotfix, whatever the configuration, through its management web interface; the service is reachable from the internet where the management port, or a dataplane interface carrying a management profile, answers HTTPS or XML API requests from outside the administrator range ([Palo Alto Networks, 2026-10-21](https://security.paloaltonetworks.com/CVE-2026-109618)).

**Detection:** in management-plane access and system logs, any request from an address outside the administrator range, though Palo Alto does not say which logs record request bodies; in threat logs, hits on the Threat IDs above where the signatures are active and the four conditions hold. Palo Alto publishes no flaw-specific indicator and reports no exploitation of its products, so no post-compromise check is defined yet ([Palo Alto Networks, 2026-10-21](https://security.paloaltonetworks.com/CVE-2026-109618)).

**Defender takeaway:** move management access behind a jump box or trusted internal addresses now, on Panorama as on PAN-OS, and remove management profiles from dataplane interfaces that face untrusted networks; Palo Alto lists no workaround beyond that restriction and the Threat Prevention coverage. Install 10.2.18-h13, 11.1.16-h4 or 11.2.10-h16 now where the firewall runs that maintenance line, which the advisory's revision history calls released ([Palo Alto Networks, 2026-10-25](https://security.paloaltonetworks.com/json/CVE-2026-109618)), and the other trains' hotfixes as they ship by 2026-10-30 ([Palo Alto Networks, 2026-10-25](https://security.paloaltonetworks.com/CVE-2026-109618)).

## Update — 2026-10-23T03:42:16Z

Palo Alto Networks revised its advisory on 2026-10-23: the WildFire appliances WF-500 and WF-500-B are now listed as affected in all versions, and the footnotes say Cortex XCORE (SaaS) was remediated on 2026-10-21 and WildFire Cloud on 2026-10-22 ([Palo Alto Networks, 2026-10-23](https://security.paloaltonetworks.com/CVE-2026-109618)). The advisory now also gives estimated availability dates for hotfix builds of every supported PAN-OS train, from 2026-10-26 (for example 10.2.18-h13, 11.1.16-h4 and 11.2.10-h16) to 2026-10-30, while Panorama and the WildFire appliances remain with no date ([Palo Alto Networks, 2026-10-23](https://security.paloaltonetworks.com/CVE-2026-109618)). Palo Alto still states that it is not aware of malicious exploitation against its products, and the Threat Prevention coverage and the jump-box restriction are unchanged ([Palo Alto Networks, 2026-10-23](https://security.paloaltonetworks.com/CVE-2026-109618)). The advisory names the management web interface only for PAN-OS and does not say which interface of the WildFire appliances is reachable.

## Update — 2026-10-24T03:37:34Z

Palo Alto Networks' advisory now lists the WildFire appliances WF-500 and WF-500-B, which an earlier revision of 2026-10-23 had listed as affected, as unaffected, a correction its timeline dates 2026-10-23, and the table no longer distinguishes Panorama while a note says the issue applies to PAN-OS software on PA-Series and VM-Series firewalls and on Panorama (virtual and M-Series) and the mitigation text covers PAN-OS and Panorama together ([Palo Alto Networks, 2026-10-24](https://security.paloaltonetworks.com/CVE-2026-109618)). The estimated hotfix dates for PAN-OS, 2026-10-26 to 2026-10-30, the CVSS-B scores of 8.7 and 7.1, and the statement that Palo Alto Networks is not aware of malicious exploitation against its products are unchanged; on 2026-10-24 the advisory added updated threat-signature and content-version details, and the Threat Prevention coverage now lists twenty further Threat IDs, from 97643 to 97678 ([Palo Alto Networks, 2026-10-24](https://security.paloaltonetworks.com/CVE-2026-109618)).

## Update — 2026-10-25T14:00:17Z

Palo Alto Networks' revision of 2026-10-25 removed the estimated dates of 10.2.18-h13, 11.1.16-h4 and 11.2.10-h16 "as these versions are released" ([Palo Alto Networks, 2026-10-25](https://security.paloaltonetworks.com/json/CVE-2026-109618)); the advisory's solution text, unrevised, still says the issue will be fixed in upcoming releases of PAN-OS, and every other hotfix carries an estimated date from 2026-10-27 to 2026-10-30 ([Palo Alto Networks, 2026-10-25](https://security.paloaltonetworks.com/CVE-2026-109618)). The FAQ adds that Palo Alto's current analysis shows no impact on PAN-OS firewalls or Panorama of CVE-2026-115560, the new vulnerability PHP announced, and Palo Alto still knows of no malicious exploitation against its products ([Palo Alto Networks, 2026-10-25](https://security.paloaltonetworks.com/CVE-2026-109618)).
