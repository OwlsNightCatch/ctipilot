---
schema: 1
kind: threat
title: "AA26-281A: China-linked actors enabled by Integrity Technology Group scan with MicroScan, spray Exchange and Microsoft 365 passwords and steal mail, and five old flaws from the scanner's scripts enter CISA KEV"
headline: "Joint advisory: Flax Typhoon-consistent actors spray Exchange and Microsoft 365, steal mail and keep SoftEther access"
summary: >
  The FBI, CISA, NSA, NCSC UK and partners from five more countries published AA26-281A on 2026-10-08 on China-linked actors
  enabled by Integrity Technology Group, whose tactics the advisory calls consistent with Flax Typhoon: open-source and
  MicroScan vulnerability scanning, XSS credential harvesting, password spraying against Exchange and Microsoft 365
  interfaces, SoftEther VPN persistence, DCSync and bulk mail theft through Exchange Web Services. Five of the eight old
  flaws the advisory lists as successfully exploited (ProFTPD, ISC BIND, Apache Struts, ONLYOFFICE Docs, Strapi) were added
  to CISA's KEV catalog the same day; the FBI also seized the domains behind MicroScan and the FishHub phishing tool.
discovered_at: "2026-10-09T03:43:00Z"
updated_at: null
event_date: "2026-10-08"
run_id: 2026-10-09T0255Z-intel
priority: notable
immediate_action: null
tags: [nation-state, espionage, law-enforcement, cisa-kev]
regions: [global]
sectors: [public-sector, healthcare, manufacturing, technology]
entities: ["actor:integrity-technology-group", "actor:flax-typhoon", "tool:microscan", "tool:fishhub"]
techniques: [T1595.002, T1190, T1059.006, T1189, T1059.007, T1110.001, T1110.003, T1114.002, T1133, T1059.001, T1059.004, T1036.003, T1003.006, T1074.001, T1560.003, T1020]
affected_products: ["ProFTPD", "ISC BIND", "Apache Struts", "ONLYOFFICE Docs", "Strapi", "GNU Bash", "Ivanti Pulse Connect Secure", "GitLab", "Microsoft Exchange Server"]
cves:
  - id: CVE-2015-3306
    cvss: null
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev]
    affected: "ProFTPD 1.3.5"
    fixed: "not stated in AA26-281A or the CISA catalogue"
  - id: CVE-2015-5477
    cvss: null
    epss: null
    type: dos
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev, patch-available]
    affected: "ISC BIND 9.x before 9.9.7-P2 and 9.10.x before 9.10.2-P3"
    fixed: "9.9.7-P2; 9.10.2-P3"
  - id: CVE-2016-3081
    cvss: null
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev, patch-available]
    affected: "Apache Struts 2.3.19 to 2.3.20.2, 2.3.21 to 2.3.24.1 and 2.3.25 to 2.3.28 with Dynamic Method Invocation enabled"
    fixed: "2.3.20.3; 2.3.24.3; 2.3.28.1 (Apache S2-032), or disable Dynamic Method Invocation"
  - id: CVE-2021-3199
    cvss: null
    epss: null
    type: path-traversal
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev]
    affected: "ONLYOFFICE DocumentServer 5.1.5 through 5.6.2, when JWT is used"
    fixed: "not stated in AA26-281A; the CISA catalogue links the 5.6.3 changelog"
  - id: CVE-2023-22894
    cvss: null
    epss: null
    type: info-disclosure
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev, patch-available]
    affected: "Strapi up to 4.5.5 per AA26-281A; Strapi's own disclosure lists 3.2.1 up to but excluding 4.8.0"
    fixed: "4.8.0 (Strapi disclosure); CISA notes the product may be end-of-life"
  - id: CVE-2014-6278
    cvss: null
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev, patch-available]
    affected: "GNU Bash through 4.3 patch bash43-026"
    fixed: "patch bash43-027, as linked by the CISA catalogue"
  - id: CVE-2019-11510
    cvss: null
    epss: null
    type: path-traversal
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev, patch-available]
    affected: "Pulse Connect Secure 8.2 before 8.2R12.1, 8.3 before 8.3R7.1 and 9.0 before 9.0R3.4"
    fixed: "8.2R12.1; 8.3R7.1; 9.0R3.4"
  - id: CVE-2021-22205
    cvss: null
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev]
    affected: "GitLab all versions starting from 11.9"
    fixed: "not stated in AA26-281A or the CISA catalogue"
sources:
  - url: "https://www.ic3.gov/CSA/2026/261008.pdf"
    publisher: "FBI, CISA, NSA, NCSC UK and partners (joint advisory AA26-281A)"
    date: "2026-10-08"
    role: primary
  - url: "https://www.justice.gov/opa/pr/justice-department-and-fbi-seize-vulnerability-scanning-and-spear-phishing-tools-operated"
    publisher: "U.S. Department of Justice"
    date: "2026-10-08"
    role: primary
  - url: "https://www.ncsc.gov.uk/news/china-linked-actors-called-out-by-uk-and-international-partners-for-targeting-sensitive-data"
    publisher: "NCSC UK"
    date: "2026-10-08"
    role: corroborating
  - url: "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    publisher: "CISA Known Exploited Vulnerabilities Catalog"
    date: "2026-10-08"
    role: corroborating
  - url: "https://cwiki.apache.org/confluence/display/WW/S2-032"
    publisher: "Apache Struts (S2-032)"
    date: "2021-02-13"
    role: corroborating
  - url: "https://strapi.io/blog/security-disclosure-of-vulnerabilities-cve"
    publisher: "Strapi"
    date: "2023-04-17"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The activity in the advisory is reported to be consistent with campaigns also publicly known as Flax Typhoon, Ethereal Panda and Red Juliett among others."
    publisher: "NCSC UK"
    source_url: "https://www.ncsc.gov.uk/news/china-linked-actors-called-out-by-uk-and-international-partners-for-targeting-sensitive-data"
  - quote: "Integrity Tech has contracts with the PRC government."
    publisher: "U.S. Department of Justice"
    source_url: "https://www.justice.gov/opa/pr/justice-department-and-fbi-seize-vulnerability-scanning-and-spear-phishing-tools-operated"
  - quote: "Network defenders should include these interfaces when defending against EBurst."
    publisher: "FBI, CISA, NSA, NCSC UK and partners (joint advisory AA26-281A)"
    source_url: "https://www.ic3.gov/CSA/2026/261008.pdf"
verification: single-source-national-cert
sourcing_note: >
  The advisory, the Justice Department release and the NCSC UK page all rest on the FBI's investigations, so they are one
  assessment with several publishers; the advisory does not tie the eight CVEs to victims or dates and presents them as
  recovered from MicroScan's scripts. CISA's catalogue says the Strapi flaw needs access to the admin panel, while Strapi's
  own disclosure says an unauthenticated attacker can exploit it; the pre-auth rating follows Strapi.
confidence: high
references:
  - "2026-08-28/doj-fbi-qscan-qtrouter-prc-hacking-as-a-service-takedown"
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

The FBI, CISA, NSA, NCSC UK and partners from Australia, Canada, Japan, New Zealand and Spain describe Integrity Technology Group as a China-based company with links to the Chinese government that builds and sells cyber tools, hosts infrastructure and compromises networks; the actors it enables use tactics consistent with Flax Typhoon, Ethereal Panda and Red Juliett, among others ([FBI IC3, AA26-281A, 2026-10-08](https://www.ic3.gov/CSA/2026/261008.pdf)). The Justice Department says the FBI seized the domains of MicroScan and the FishHub phishing platform, both operated by Integrity Tech ([U.S. Department of Justice, 2026-10-08](https://www.justice.gov/opa/pr/justice-department-and-fbi-seize-vulnerability-scanning-and-spear-phishing-tools-operated)). Victims include U.S. government services, other critical sectors and organisations in Southeast Asia, Africa and North America; the advisory names no Swiss victim ([FBI IC3, AA26-281A, 2026-10-08](https://www.ic3.gov/CSA/2026/261008.pdf)).

The chain starts with open-source scanners and MicroScan, a Python-based web application of 1,300-plus scripts, used since at least 2017 ([FBI IC3, AA26-281A, 2026-10-08](https://www.ic3.gov/CSA/2026/261008.pdf)). Initial access has mostly come since January 2021 from command-line exploit utilities, and additionally from a cross-site-scripting payload that overlays a login form and offers a ZIP holding an executable that starts a process named like the Windows DiagTrack service ([FBI IC3, AA26-281A, 2026-10-08](https://www.ic3.gov/CSA/2026/261008.pdf)). The actors spray and guess passwords with the EBurst tool against Exchange and Microsoft 365 (ECP, EWS, OAB, OWA, RPC, API, MAPI, PowerShell, Autodiscover, ActiveSync) ([FBI IC3, AA26-281A, 2026-10-08](https://www.ic3.gov/CSA/2026/261008.pdf)). Persistence is a SoftEther VPN client, often named conhost.exe or dllhost.exe, which endpoint tools are less likely to flag ([FBI IC3, AA26-281A, 2026-10-08](https://www.ic3.gov/CSA/2026/261008.pdf)). Collection uses a PHP bot and a Linux utility that read mail through Exchange Web Services and Microsoft 365 with application client, tenant and secret values, and a DCSync tool that replicates directory data from a domain controller; mail was stolen from government, law-enforcement and healthcare bodies in Southeast Asia ([FBI IC3, AA26-281A, 2026-10-08](https://www.ic3.gov/CSA/2026/261008.pdf)).

Appendix B lists eight successfully exploited CVEs recovered from MicroScan's scripts: ProFTPD 1.3.5, ISC BIND 9.x, Apache Struts 2.3.19 to 2.3.28, ONLYOFFICE DocumentServer 5.1.5 through 5.6.2 and Strapi up to 4.5.5, plus GNU Bash through 4.3, Pulse Connect Secure and GitLab from 11.9 ([FBI IC3, AA26-281A, 2026-10-08](https://www.ic3.gov/CSA/2026/261008.pdf)); CISA added the first five to its catalogue on 2026-10-08 ([CISA KEV catalogue, 2026-10-08](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)). Apache names Struts 2.3.20.3, 2.3.24.3 and 2.3.28.1 as fixed ([Apache Struts, 2021-02-13](https://cwiki.apache.org/confluence/display/WW/S2-032)) and Strapi names 4.8.0 ([Strapi, 2023-04-17](https://strapi.io/blog/security-disclosure-of-vulnerabilities-cve)).

**Exposure:** internet-facing Exchange and Microsoft 365 sign-in without a second factor, web applications open to cross-site scripting, and the eight products at the versions above; an inventory and the Exchange authentication logs show whether an organisation is in scope ([FBI IC3, AA26-281A, 2026-10-08](https://www.ic3.gov/CSA/2026/261008.pdf)).

**Detection:** authentication logs across the Exchange interfaces for failed sign-ins spread over many accounts from one source, mailbox reads by connected applications nobody registered, a SoftEther client presented as conhost.exe or dllhost.exe in process and service-installation telemetry, directory-replication requests that reach a domain controller from a host that is not one, and web access logs for traversal, command-injection and enumeration attempts ([FBI IC3, AA26-281A, 2026-10-08](https://www.ic3.gov/CSA/2026/261008.pdf)).

**Triage:** conhost.exe and dllhost.exe are legitimate Windows names, so the file's path, signature and network behaviour separate a downloaded SoftEther client from the system binary ([FBI IC3, AA26-281A, 2026-10-08](https://www.ic3.gov/CSA/2026/261008.pdf)).

**Defender takeaway:** hunt Exchange and Microsoft 365 logs for spraying across interfaces and mailbox access by unknown applications, confirm multifactor authentication on webmail and VPN, and treat an internet-facing instance of any of the eight products as a possible intrusion point rather than patch debt.
