---
schema: 1
kind: vulnerability
title: "Drupal core 11.4.13, 11.3.22 and 10.6.22 fix CVE-2026-132165 (SA-CORE-2026-017, Critical): under specific conditions an attacker can use the installer to reinstall Drupal, which can lead to site takeover or remote code execution; the only workaround is securing the installer, and no exploitation is reported"
headline: "Drupal 11.4.13, 11.3.22, 10.6.22 fix an installer reinstall to takeover or RCE (SA-017, Critical); update now"
summary: >
  Drupal published SA-CORE-2026-017 (CVE-2026-132165, Critical 18 of 25) and SA-CORE-2026-018 (CVE-2026-132166, Moderately critical, not directly exploitable) on 2026-11-18: under specific conditions an attacker can use the installer to attempt to reinstall Drupal, which can lead to site takeover or remote code execution. Fixed in 11.4.13, 11.3.22 and 10.6.22, the only workaround is securing the installer, and no source reports exploitation, although the Security Team had warned that exploits might be developed within hours or days.
discovered_at: "2026-11-18T05:09:00Z"
updated_at: "2026-11-19T05:02:14Z"
event_date: "2026-11-18"
run_id: 2026-11-18T0356Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, pre-auth, rce, patch-available]
regions: [global]
sectors: [technology]
entities: []
techniques: [T1190]
affected_products: ["Drupal Core"]
cves:
  - id: CVE-2026-132165
    cvss: "n/a"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "<10.6.22 || >=11.0.0 <11.3.22 || >=11.4.0 <11.4.13"
    fixed: "11.4.13, 11.3.22, 10.6.22"
  - id: CVE-2026-132166
    cvss: "n/a"
    epss: null
    type: deserialization
    vector: zero-click
    auth: admin-required
    status: [patch-available]
    affected: "<10.6.22 || >=11.0.0 <11.3.22 || >=11.4.0 <11.4.13"
    fixed: "11.4.13, 11.3.22, 10.6.22"
sources:
  - url: "https://www.drupal.org/psa-2026-11-16"
    publisher: "Drupal Security Team (PSA-2026-11-16)"
    date: "2026-11-16"
    role: primary
  - url: "https://security-hub.ncsc.admin.ch/#/posts/13196"
    publisher: "NCSC.ch Cyber Security Hub"
    date: "2026-11-17"
    role: corroborating
  - url: "https://www.drupal.org/sa-core-2026-017"
    publisher: "Drupal Security Team (SA-CORE-2026-017)"
    date: "2026-11-18"
    role: primary
  - url: "https://www.drupal.org/sa-core-2026-018"
    publisher: "Drupal Security Team (SA-CORE-2026-018)"
    date: "2026-11-18"
    role: primary
  - url: "https://advisories.ncsc.nl/2026/ncsc-2026-0507.html"
    publisher: "NCSC-NL"
    date: "2026-11-18"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The Drupal Security Team urges you to reserve time for core updates at that time because exploits might be developed within hours or days."
    publisher: "Drupal Security Team (PSA-2026-11-16)"
    source_url: "https://www.drupal.org/psa-2026-11-16"
  - quote: "The vulnerabilities are currently rated as critical and at least one can be exploited by anonymous users."
    publisher: "Drupal Security Team (PSA-2026-11-16)"
    source_url: "https://www.drupal.org/psa-2026-11-16"
  - quote: "Neither the Security Team nor any other party is able to release any more information about this vulnerability until the announcement is made."
    publisher: "Drupal Security Team (PSA-2026-11-16)"
    source_url: "https://www.drupal.org/psa-2026-11-16"
  - quote: "Under specific conditions, an attacker can use the installer to attempt to reinstall Drupal. This can lead to a site takeover or remote code execution."
    publisher: "Drupal Security Team (SA-CORE-2026-017)"
    source_url: "https://www.drupal.org/sa-core-2026-017"
  - quote: "This issue is not directly exploitable."
    publisher: "Drupal Security Team (SA-CORE-2026-018)"
    source_url: "https://www.drupal.org/sa-core-2026-018"
verification: single-source
sourcing_note: >
  The Drupal Security Team is the disclosing party and the only source for the flaws; NCSC-NL restates the advisories and NCSC.ch's Security Hub rated exploitation unknown on 2026-11-17, before the release. The SA-CORE-2026-018 page answered the fetch tools with a client challenge, so its fields were read from Drupal's own advisory feed item for it.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Update every Drupal site to 11.4.13, 11.3.22 or 10.6.22 now and move sites on end-of-life lines (Drupal 11.2.x and 10.5.x and below) to a supported branch, and where the update has to wait secure the installer as Drupal's instructions for securing install.php describe, because SA-CORE-2026-017 lets an attacker who reaches the installer attempt a reinstall that can end in site takeover or remote code execution."
updates:
  - at: "2026-11-19T05:02:14Z"
    run_id: 2026-11-19T0355Z-intel
    type: update
    summary: >
      Drupal published the announced core security release on 2026-11-18: SA-CORE-2026-017
      (CVE-2026-132165, Critical, installer reinstall leading to site takeover or remote code execution)
      and SA-CORE-2026-018 (CVE-2026-132166, not directly exploitable), fixed in 11.4.13, 11.3.22 and
      10.6.22. No exploitation is reported.
    fields: [actions, body, cves, event_date, evidence, headline, priority, sources, sourcing_note, summary, tags, title, updated_at]
migrated_from: null
---

Drupal shipped its announced core security release on 2026-11-18. SA-CORE-2026-017 (CVE-2026-132165, rated Critical 18 of 25, with access complexity Complex, access none, exploit status Proof, meaning a proof of concept exists with documented methods for developing an exploit in the wild, and target distribution Uncommon, meaning only uncommon module configurations are exploitable) says that under specific conditions an attacker can use the installer to attempt to reinstall Drupal, which can lead to a site takeover or remote code execution ([Drupal Security Team, 2026-11-18](https://www.drupal.org/sa-core-2026-017)). SA-CORE-2026-018 (CVE-2026-132166, Moderately critical 14 of 25) is a gadget chain that Drupal says is not directly exploitable: a separate vulnerability must be present to let an attacker pass unsafe input to unserialize() ([Drupal Security Team, 2026-11-18](https://www.drupal.org/sa-core-2026-018)).

Both advisories cover core before 10.6.22, from 11.0.0 before 11.3.22 and from 11.4.0 before 11.4.13, fixed in 11.4.13, 11.3.22 and 10.6.22; Drupal 11.2.x and below and 10.5.x and below are end-of-life and receive no security coverage ([Drupal Security Team, 2026-11-18](https://www.drupal.org/sa-core-2026-017)). The only workaround Drupal gives is to secure the installer; it adds that some exploit paths are mitigated if the web server cannot write to or change permissions on settings.php, and that sites on Drupal Steward are already protected from SA-CORE-2026-017's known attack vectors ([Drupal Security Team, 2026-11-18](https://www.drupal.org/sa-core-2026-017)). The pre-announcement had warned that exploits might be developed within hours or days ([Drupal Security Team, 2026-11-16](https://www.drupal.org/psa-2026-11-16)); NCSC.ch's Security Hub rated exploitation unknown on 2026-11-17 ([NCSC.ch, 2026-11-17](https://security-hub.ncsc.admin.ch/#/posts/13196)), and neither advisory reports exploitation.

**Exposure:** any Drupal site on core before 10.6.22, 11.3.22 or 11.4.13, though Drupal's own rating says only uncommon module configurations are exploitable, and every site on an end-of-life line, which has no fix; NCSC-NL says the condition arises when the installer is not correctly secured or removed after the initial installation (translated from Dutch) ([NCSC-NL, 2026-11-18](https://advisories.ncsc.nl/2026/ncsc-2026-0507.html)).

**Detection:** web access logs for requests to the installer on a site that is already installed, which follows from the mechanism; Drupal's advisory names no indicators of compromise.

**Defender takeaway:** update each site to 11.4.13, 11.3.22 or 10.6.22 now and move end-of-life sites to a supported branch; where the update waits, secure the installer. Drupal advises upgrading even behind Steward, in case additional attack vectors are discovered ([Drupal Security Team, 2026-11-18](https://www.drupal.org/sa-core-2026-017)).

## Update — 2026-11-19T05:02:14Z

The release the pre-announcement described is out. Drupal published SA-CORE-2026-017 (CVE-2026-132165, Critical 18 of 25) and SA-CORE-2026-018 (CVE-2026-132166, Moderately critical 14 of 25, not directly exploitable) on 2026-11-18, fixed in Drupal 11.4.13, 11.3.22 and 10.6.22 ([Drupal Security Team, 2026-11-18](https://www.drupal.org/sa-core-2026-017), [Drupal Security Team, 2026-11-18](https://www.drupal.org/sa-core-2026-018)). SA-CORE-2026-017 says an attacker can use the installer to attempt to reinstall Drupal, which can lead to a site takeover or remote code execution, and the only workaround is to secure the installer ([Drupal Security Team, 2026-11-18](https://www.drupal.org/sa-core-2026-017)). The 18 of 25 rating in the pre-announcement is SA-CORE-2026-017's; neither advisory reports exploitation.
