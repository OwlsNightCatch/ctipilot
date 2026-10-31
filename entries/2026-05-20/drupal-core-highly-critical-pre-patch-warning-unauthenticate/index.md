---
schema: 1
kind: vulnerability
title: "CVE-2026-9082: anonymous SQL injection in Drupal core on PostgreSQL, Highly critical, exploited and CISA KEV-listed"
headline: "Drupal core CVE-2026-9082: anonymous SQL injection on PostgreSQL sites, exploited in the wild from 2026-05-22"
summary: >
  Drupal's SA-CORE-2026-004 (2026-05-20), pre-announced in PSA-2026-05-18, fixes CVE-2026-9082, an
  anonymous SQL injection in Drupal core's database abstraction API that affects only sites using
  PostgreSQL and can lead to information disclosure and in some cases privilege escalation or remote
  code execution. Drupal confirmed exploit attempts in the wild on 2026-05-22, raising its risk score
  from 20 to 23 of 25, and CISA added the flaw to its KEV catalog the same day; the fixed releases are
  11.3.10, 11.2.12, 11.1.10, 10.6.9, 10.5.10 and 10.4.10.
discovered_at: "2026-05-20T05:00:00Z"
updated_at: "2026-05-23T05:00:10Z"
event_date: 2026-05-18
run_id: 2026-05-20-a0f7b07f
priority: critical
immediate_action:
  title: "Update Drupal core sites on PostgreSQL to 11.3.10, 11.2.12, 11.1.10, 10.6.9, 10.5.10 or 10.4.10"
  action: >
    CVE-2026-9082 (SA-CORE-2026-004, 2026-05-20) is an anonymous SQL injection in Drupal core's
    database abstraction API that only affects sites using PostgreSQL; Drupal confirmed exploit attempts
    in the wild on 2026-05-22 and CISA added it to its KEV catalog the same day. Update to 11.3.10,
    11.2.12, 11.1.10, 10.6.9, 10.5.10 or 10.4.10, or on Drupal 9.5 and 8.9 apply the best-effort patch
    file by hand; sites behind Drupal Steward are protected against known attack vectors but should still
    update. Imperva observed over 15,000 attack attempts against almost 6,000 sites, most of them probing.
tags:
  - vulnerabilities
  - sqli
  - pre-auth
  - actively-exploited
  - cisa-kev
  - patch-available
regions:
  - global
sectors: []
entities: []
techniques: [T1190, T1595.002]
affected_products:
  - "Drupal Core"
cves:
  - id: CVE-2026-9082
    cvss: "9.8"
    epss: null
    type: sqli
    vector: zero-click
    auth: pre-auth
    status:
      - exploited
      - cisa-kev
      - patch-available
    affected: "8.9.0 before 10.4.10, 10.5.0 before 10.5.10, 10.6.0 before 10.6.9, 11.0.0 before 11.1.10, 11.2.0 before 11.2.12, 11.3.0 before 11.3.10 (PostgreSQL sites only)"
    fixed: "10.4.10, 10.5.10, 10.6.9, 11.1.10, 11.2.12, 11.3.10; best-effort patch files for 9.5 and 8.9"
sources:
  - url: "https://www.drupal.org/psa-2026-05-18"
    publisher: "Drupal Security Team (PSA-2026-05-18)"
    date: "2026-05-18"
    role: primary
  - url: "https://security-hub.ncsc.admin.ch/#/posts/12584"
    publisher: "NCSC.ch Security Hub"
    date: "2026-05-19"
    role: corroborating
  - url: "https://www.securityweek.com/drupal-to-patch-highly-critical-vulnerability-at-risk-of-quick-exploitation/"
    publisher: "SecurityWeek"
    date: "2026-05-19"
    role: corroborating
  - url: "https://www.theregister.com/security/2026/05/19/drupal-warns-admins-to-brace-for-highly-critical-core-patch/5242728"
    publisher: "The Register"
    date: "2026-05-19"
    role: corroborating
  - url: "https://thehackernews.com/2026/05/drupal-to-release-urgent-core-security.html"
    publisher: "The Hacker News"
    date: "2026-05-19"
    role: corroborating
  - url: "https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1579"
    publisher: "BSI WID-SEC-2026-1579"
    date: "2026-05-18"
    role: corroborating
  - url: "https://www.drupal.org/sa-core-2026-004"
    publisher: "Drupal Security Team (SA-CORE-2026-004)"
    date: "2026-05-20"
    role: primary
  - url: "https://www.csoonline.com/article/4175329/drupal-admins-rushing-to-patch-maximum-severity-sql-injection-vulnerability.html"
    publisher: "CSO Online"
    date: "2026-05-20"
    role: corroborating
  - url: "https://www.imperva.com/blog/imperva-customers-protected-against-cve-2026-9082-in-drupal-core/"
    publisher: "Imperva"
    date: "2026-05-21"
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/drupal-critical-sql-injection-flaw-now-targeted-in-attacks/"
    publisher: "BleepingComputer"
    date: "2026-05-22"
    role: corroborating
  - url: "https://slcyber.io/research-center/keys-to-the-kingdom-anonymous-sql-injection-in-drupal-core-cve-2026-9082/"
    publisher: "Searchlight Cyber"
    date: "2026-05-21"
    role: corroborating
  - url: "https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-31153"
    publisher: "ENISA EUVD-2026-31153"
    date: "2026-05-20"
    role: corroborating
  - url: "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    publisher: "CISA KEV catalog"
    date: "2026-05-22"
    role: corroborating
  - url: "https://www.drupal.org/drupal-security-team/security-risk-levels-defined"
    publisher: "Drupal Security Team (security risk levels)"
    date: null
    role: corroborating
  - url: "https://www.bk.admin.ch/en/standard-service-websites"
    publisher: "Swiss Federal Chancellery"
    date: "2026-02-24"
    role: corroborating
closed_sources: []
evidence:
  - quote: "exploits might be developed within hours or days."
    publisher: "Drupal Security Team (PSA-2026-05-18)"
    source_url: "https://www.drupal.org/psa-2026-05-18"
  - quote: "This issue is being protected by Drupal Steward."
    publisher: "Drupal Security Team (PSA-2026-05-18)"
    source_url: "https://www.drupal.org/psa-2026-05-18"
  - quote: "A vulnerability in this API allows an attacker to send specially crafted requests, resulting in arbitrary SQL injection for sites using PostgreSQL databases."
    publisher: "Drupal Security Team (SA-CORE-2026-004)"
    source_url: "https://www.drupal.org/sa-core-2026-004"
  - quote: "The risk score has been updated to reflect that exploit attempts are now being detected in the wild."
    publisher: "Drupal Security Team (SA-CORE-2026-004)"
    source_url: "https://www.drupal.org/sa-core-2026-004"
  - quote: "Since CVE-2026-9082 was released, Imperva has observed over 15,000 attack attempts targeting almost 6,000 individual sites across 65 countries."
    publisher: "Imperva"
    source_url: "https://www.imperva.com/blog/imperva-customers-protected-against-cve-2026-9082-in-drupal-core/"
  - quote: "Most of the observed activity so far appears to be probing."
    publisher: "Imperva"
    source_url: "https://www.imperva.com/blog/imperva-customers-protected-against-cve-2026-9082-in-drupal-core/"
  - quote: "There are two anonymous entry points that we have confirmed reach this loop with attacker-controlled array keys: the JSON login endpoint and the JSON:API filter syntax."
    publisher: "Searchlight Cyber"
    source_url: "https://slcyber.io/research-center/keys-to-the-kingdom-anonymous-sql-injection-in-drupal-core-cve-2026-9082/"
verification: multi-source
sourcing_note: >
  The Drupal Security Team's PSA and SA-CORE-2026-004 carry the flaw, the versions, the risk scores and
  the exploitation status; CISA's KEV listing and Imperva's attack telemetry are independent of Drupal,
  and Searchlight Cyber supplies the code-level mechanism. NCSC.ch, BSI and the trade press restate the
  advisories.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions: []
updates:
  - at: "2026-05-21T05:00:07Z"
    run_id: 2026-05-21-77cdc4cd
    type: update
    summary: >
      Drupal patches "highly critical" pre-auth SQL injection (CVE-2026-9082) on PostgreSQL-backed
      installs of Drupal 8.9–11.3; the Security Team warned that "exploits might be developed within
      hours or days" of advisory release. EU/CH government portals and university CMSes are the
      primary exposed surface (Drupal Security Team, 2026-05-20; NCSC-CH, 2026-05-19).
    fields:
      - cves
      - priority
      - sectors
      - sources
      - tags
      - body
    merged_from: 2026-05-21/drupal-sa-core-2026-004-cve-2026-9082-ships-highly-critical
  - at: "2026-05-23T05:00:10Z"
    run_id: 2026-05-23-852c21c8
    type: update
    summary: >
      Drupal CVE-2026-9082 now actively exploited; CISA KEV-listed 2026-05-22. Drupal updated
      SA-CORE-2026-004 to confirm in-the-wild exploit attempts on PostgreSQL-backed sites; Imperva
      measured 15,000+ attempts against ~6,000 sites across 65 countries; NCSC.ch Security Hub flipped
      post 12584 to "Actively exploited" the same day (Drupal Security Team, 2026-05-22 · Imperva,
      2026-05-21 · NCSC-CH, 2026-05-22).
    fields:
      - actions
      - cves
      - evidence
      - immediate_action
      - priority
      - sources
      - tags
      - body
    merged_from: 2026-05-23/drupal-cve-2026-9082-cisa-kev-addition-active-exploitation-c
  - at: "2026-10-21T16:06:42Z"
    run_id: 2026-10-21T1148Z-audit
    type: correction
    summary: >
      Drupal's 20 of 25 is its top tier, Highly critical, and rose to 23 of 25 on 2026-05-22; Drupal
      Steward protected sites before the patch, only Drupal 9 and 8.9 needed manual patch files, and the
      CNA scores CVE-2026-9082 CVSS 9.8 rather than 6.5. Switching databases is not a sourced control,
      Imperva's figures are attack attempts that were mostly probing, and no source names Swiss, EU or
      university Drupal sites as targets.
    fields: [actions, affected_products, body, classification, cves, evidence, headline, immediate_action, kind, regions, sectors, sources, sourcing_note, summary, tags, techniques, title]
    merged_from: [2026-05-20/prepare-emergency-drupal-patch-window-for-today-17-00-21-00]
migrated_from: briefs/2026-05-20.md
---

The Drupal Security Team pre-announced a Highly critical core release on 2026-05-18, scored 20 of 25 (AC:None, A:None, E:Theoretical, TD:Uncommon), and urged administrators to reserve the 2026-05-20 window from 17:00 to 21:00 UTC because "exploits might be developed within hours or days" ([Drupal PSA-2026-05-18](https://www.drupal.org/psa-2026-05-18)). SA-CORE-2026-004 followed on 2026-05-20 with CVE-2026-9082: a flaw in core's database abstraction API lets an anonymous attacker send specially crafted requests that result in arbitrary SQL injection on sites using PostgreSQL, which can lead to information disclosure and in some cases privilege escalation, remote code execution or other attacks ([Drupal SA-CORE-2026-004](https://www.drupal.org/sa-core-2026-004)). Searchlight Cyber traced it to the PostgreSQL entity-query override of the case-insensitive `IN` operator, which builds SQL placeholder names from the keys of the submitted value array, so attacker-chosen JSON object keys reach the SQL text through two anonymous entry points, the JSON login endpoint and the JSON:API filter syntax ([Searchlight Cyber, 2026-05-21](https://slcyber.io/research-center/keys-to-the-kingdom-anonymous-sql-injection-in-drupal-core-cve-2026-9082/)). The fixed releases are 11.3.10, 11.2.12, 11.1.10, 10.6.9, 10.5.10 and 10.4.10, and Drupal 9 and 8.9 sites are told to try applying a best-effort patch file by hand ([Drupal SA-CORE-2026-004](https://www.drupal.org/sa-core-2026-004)); Drupal 7 is not affected ([Drupal PSA-2026-05-18](https://www.drupal.org/psa-2026-05-18)). On 2026-05-22 Drupal raised the risk score to 23 of 25 because exploit attempts were being detected in the wild ([Drupal SA-CORE-2026-004](https://www.drupal.org/sa-core-2026-004)), and CISA added the flaw to its Known Exploited Vulnerabilities catalog the same day ([CISA KEV catalog, 2026-05-22](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)); the Drupal CNA scores it CVSS 9.8 ([ENISA EUVD-2026-31153](https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-31153)). By 2026-05-21 Imperva had observed over 15,000 attack attempts against almost 6,000 sites in 65 countries, most of it probing ([Imperva, 2026-05-21](https://www.imperva.com/blog/imperva-customers-protected-against-cve-2026-9082-in-drupal-core/)).

**Exposure:** Drupal core sites on PostgreSQL running a version from 8.9.0 before 10.4.10, 10.5.0 before 10.5.10, 10.6.0 before 10.6.9, 11.0.0 before 11.1.10, 11.2.0 before 11.2.12 or 11.3.0 before 11.3.10 ([Drupal SA-CORE-2026-004](https://www.drupal.org/sa-core-2026-004)); on MySQL and SQLite the `IN` compilation never enters the vulnerable loop ([Searchlight Cyber, 2026-05-21](https://slcyber.io/research-center/keys-to-the-kingdom-anonymous-sql-injection-in-drupal-core-cve-2026-9082/)). The releases for the supported branches (11.3, 11.2, 10.6 and 10.5) also carry Symfony and Twig security updates, which Drupal highly recommends whether or not the SQL injection affects a site, since exposure to those upstream issues depends on site configuration and contributed modules ([Drupal SA-CORE-2026-004](https://www.drupal.org/sa-core-2026-004)).

**Detection:** web access logs. The observed probes hit JSON:API routes, especially `/jsonapi/node/article`, with crafted filter parameters using the `IN` operator, crafted array keys, PostgreSQL `pg_sleep` timing checks and UNION-style probes, several of them carrying Nuclei-style markers, and Imperva also points to `/user/login?_format=json` requests ([Imperva, 2026-05-21](https://www.imperva.com/blog/imperva-customers-protected-against-cve-2026-9082-in-drupal-core/)). A successful injection can make all non-public data accessible and let the attacker modify or delete any data ([Drupal PSA-2026-05-18](https://www.drupal.org/psa-2026-05-18)) and can escalate privileges ([Drupal SA-CORE-2026-004](https://www.drupal.org/sa-core-2026-004)), so patching does not close a past compromise: on a PostgreSQL site that ran an affected version after 2026-05-20, review user accounts and role assignments for changes nobody made.

**Triage:** most of this traffic is automated probing that tests whether a site is vulnerable ([Imperva, 2026-05-21](https://www.imperva.com/blog/imperva-customers-protected-against-cve-2026-9082-in-drupal-core/)); a probe against a MySQL or SQLite site, or one already on a fixed release, is noise, while the same request against an unpatched PostgreSQL site is an attempt that calls for the account review above ([Drupal SA-CORE-2026-004](https://www.drupal.org/sa-core-2026-004)).

**Defender takeaway:** every Drupal core site on PostgreSQL that was not on a fixed release by 2026-05-22 is in scope for that review; sites behind the Drupal Steward web application firewall were protected from known attack vectors but Drupal still told them to upgrade ([CSO Online, 2026-05-20](https://www.csoonline.com/article/4175329/drupal-admins-rushing-to-patch-maximum-severity-sql-injection-vulnerability.html)), and sites on other databases take the release for its Symfony and Twig fixes ([Drupal SA-CORE-2026-004](https://www.drupal.org/sa-core-2026-004)).

## Update — 2026-05-21T05:00:07Z

Drupal published SA-CORE-2026-004 on 2026-05-20 with CVE-2026-9082: a vulnerability in core's database abstraction API allows an attacker to send specially crafted requests resulting in arbitrary SQL injection for sites using PostgreSQL, it can be exploited by anonymous users, and it "can lead to information disclosure, and in some cases privilege escalation, remote code execution, or other attacks" ([Drupal SA-CORE-2026-004](https://www.drupal.org/sa-core-2026-004)). The pre-announcement had scored it 20 of 25 and warned that "exploits might be developed within hours or days" ([Drupal PSA-2026-05-18](https://www.drupal.org/psa-2026-05-18)).

Affected versions run from 8.9.0 up to (not including) 10.4.10, 10.5.0 before 10.5.10, 10.6.0 before 10.6.9, 11.0.0 before 11.1.10, 11.2.0 before 11.2.12 and 11.3.0 before 11.3.10, and the fixed releases are 10.4.10, 10.5.10, 10.6.9, 11.1.10, 11.2.12 and 11.3.10; Drupal 9 and 8.9 sites get best-effort patch files to apply manually ([Drupal SA-CORE-2026-004](https://www.drupal.org/sa-core-2026-004)), and Drupal 7 is not affected ([Drupal PSA-2026-05-18](https://www.drupal.org/psa-2026-05-18)). Sites using the Drupal Steward web application firewall are already protected from known attack vectors but should upgrade in the near future ([CSO Online, 2026-05-20](https://www.csoonline.com/article/4175329/drupal-admins-rushing-to-patch-maximum-severity-sql-injection-vulnerability.html)). NCSC.ch had carried the pre-announcement on 2026-05-19 ([NCSC.ch Security Hub](https://security-hub.ncsc.admin.ch/#/posts/12584)).

## Update — 2026-05-23T05:00:10Z

On 2026-05-22 Drupal updated SA-CORE-2026-004, raising the risk score to 23 of 25 because exploit attempts are now being detected in the wild ([Drupal SA-CORE-2026-004](https://www.drupal.org/sa-core-2026-004)); NCSC.ch marked Security Hub post 12584 as actively exploited the same day ([NCSC.ch Security Hub](https://security-hub.ncsc.admin.ch/#/posts/12584)), and CISA added CVE-2026-9082 to its Known Exploited Vulnerabilities catalog on 2026-05-22 ([CISA KEV catalog, 2026-05-22](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)).

Imperva observed over 15,000 attack attempts targeting almost 6,000 sites across 65 countries, most of it probing of JSON:API routes, with Gaming and Financial Services sites drawing almost half the attacks ([Imperva, 2026-05-21](https://www.imperva.com/blog/imperva-customers-protected-against-cve-2026-9082-in-drupal-core/)). Searchlight Cyber's analysis shows attacker-controlled array keys, sent as JSON object keys to the anonymous JSON login endpoint or through the JSON:API filter syntax, reaching the placeholder names that the PostgreSQL entity-query override builds for the case-insensitive `IN` operator ([Searchlight Cyber, 2026-05-21](https://slcyber.io/research-center/keys-to-the-kingdom-anonymous-sql-injection-in-drupal-core-cve-2026-9082/)).

## Correction — 2026-10-21T16:06:42Z

A score of 20 of 25 is Drupal's top tier, Highly critical, which covers 20 to 25, not the second-highest ([Drupal security risk levels](https://www.drupal.org/drupal-security-team/security-risk-levels-defined)); it stayed below 25 because no exploit existed yet and only uncommon configurations were affected ([The Register, 2026-05-19](https://www.theregister.com/security/2026/05/19/drupal-warns-admins-to-brace-for-highly-critical-core-patch/5242728)), and on 2026-05-22 it rose to 23 of 25 with exploitation detected ([Drupal SA-CORE-2026-004](https://www.drupal.org/sa-core-2026-004)). A mitigation did exist before the patch: the PSA said the issue was protected by Drupal Steward ([Drupal PSA-2026-05-18](https://www.drupal.org/psa-2026-05-18)). Only Drupal 9 and 8.9 sites were left with patch files to apply by hand; the end-of-life 11.1.x and 10.4.x lines received full releases, 11.1.10 and 10.4.10 ([Drupal SA-CORE-2026-004](https://www.drupal.org/sa-core-2026-004)).

The Drupal CNA scores CVE-2026-9082 CVSS 9.8 ([ENISA EUVD-2026-31153](https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-31153)); 6.5 is NIST's score ([BleepingComputer, 2026-05-22](https://www.bleepingcomputer.com/news/security/drupal-critical-sql-injection-flaw-now-targeted-in-attacks/)). Moving a site off PostgreSQL is not a control any source offers; the sourced interim measure is Drupal Steward. Imperva's figures count attack attempts, mostly probing, aimed chiefly at Gaming and Financial Services sites ([Imperva, 2026-05-21](https://www.imperva.com/blog/imperva-customers-protected-against-cve-2026-9082-in-drupal-core/)). No source names Swiss, EU or university Drupal sites as targets or says Drupal dominates Swiss public portals; the Federal Administration's standard web platform is based on Livingdocs ([Swiss Federal Chancellery](https://www.bk.admin.ch/en/standard-service-websites)).
