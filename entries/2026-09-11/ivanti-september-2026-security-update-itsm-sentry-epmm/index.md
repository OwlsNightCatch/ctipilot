---
schema: 1
kind: vulnerability
title: "Ivanti September 2026 Security Update — ten CVEs across Neurons for ITSM, Sentry and EPMM, two unauthenticated CVSS 9.8 deserialization RCEs"
headline: "Ivanti discloses two unauthenticated pre-auth RCEs in Neurons for ITSM, crediting LLM-assisted review with surfacing several of the disclosed flaws"
summary: >
  Ivanti's 2026-09-08 security update fixes ten CVEs across Neurons for ITSM, Sentry and EPMM.
  Two unauthenticated CVSS 9.8 deserialization flaws in Neurons for ITSM (CVE-2026-12744,
  CVE-2026-12745) reach remote code execution with no credentials; a further seven authenticated
  escalation/RCE flaws and one Sentry authentication bypass round out the set. Ivanti states none
  of the ten is known to be exploited, and credits large-language-model-assisted review with
  finding several of the ITSM flaws that traditional tooling had missed.
discovered_at: "2026-09-11T04:35:00Z"
event_date: "2026-09-08"
run_id: 2026-09-11T0410Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, rce, priv-esc, auth-bypass, patch-available]
regions: [global]
sectors: [public-sector, technology]
entities: []
techniques: [T1190, T1068]
affected_products: ["Ivanti Neurons for ITSM", "Ivanti Sentry", "Ivanti Endpoint Manager Mobile (EPMM)"]
cves:
  - id: CVE-2026-12744
    cvss: "9.8"
    epss: 0.0217
    type: deserialization
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "2025.2, 2025.3, 2025.4, 2026.1 (on-premises); Neurons for ITSM Cloud/SaaS also listed as affected by NCSC-NL"
    fixed: "September 2026 patch for the listed on-prem versions; also included in the 2026.2 line scheduled for 2026-09-21"
  - id: CVE-2026-12745
    cvss: "9.8"
    epss: 0.0209
    type: deserialization
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "2025.2, 2025.3, 2025.4, 2026.1 (on-premises); Neurons for ITSM Cloud/SaaS also listed as affected by NCSC-NL"
    fixed: "September 2026 patch for the listed on-prem versions; also included in the 2026.2 line scheduled for 2026-09-21"
  - id: CVE-2026-12645
    cvss: "9.9"
    epss: 0.0123
    type: priv-esc
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "2025.2, 2025.3, 2025.4, 2026.1 (on-premises); Neurons for ITSM Cloud/SaaS also listed as affected by NCSC-NL"
    fixed: "September 2026 patch for the listed on-prem versions; also included in the 2026.2 line scheduled for 2026-09-21"
  - id: CVE-2026-12646
    cvss: "9.9"
    epss: 0.0119
    type: priv-esc
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "2025.2, 2025.3, 2025.4, 2026.1 (on-premises); Neurons for ITSM Cloud/SaaS also listed as affected by NCSC-NL"
    fixed: "September 2026 patch for the listed on-prem versions; also included in the 2026.2 line scheduled for 2026-09-21"
  - id: CVE-2026-12647
    cvss: "9.9"
    epss: 0.0119
    type: priv-esc
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "2025.2, 2025.3, 2025.4, 2026.1 (on-premises); Neurons for ITSM Cloud/SaaS also listed as affected by NCSC-NL"
    fixed: "September 2026 patch for the listed on-prem versions; also included in the 2026.2 line scheduled for 2026-09-21"
  - id: CVE-2026-12650
    cvss: "9.9"
    epss: 0.0146
    type: deserialization
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "2025.2, 2025.3, 2025.4, 2026.1 (on-premises); Neurons for ITSM Cloud/SaaS also listed as affected by NCSC-NL"
    fixed: "September 2026 patch for the listed on-prem versions; also included in the 2026.2 line scheduled for 2026-09-21"
  - id: CVE-2026-12651
    cvss: "8.8"
    epss: 0.0146
    type: deserialization
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "2025.2, 2025.3, 2025.4, 2026.1 (on-premises); Neurons for ITSM Cloud/SaaS also listed as affected by NCSC-NL"
    fixed: "September 2026 patch for the listed on-prem versions; also included in the 2026.2 line scheduled for 2026-09-21"
  - id: CVE-2026-12648
    cvss: "8.8"
    epss: 0.0146
    type: deserialization
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "2025.2, 2025.3, 2025.4, 2026.1 (on-premises); Neurons for ITSM Cloud/SaaS also listed as affected by NCSC-NL"
    fixed: "September 2026 patch for the listed on-prem versions; also included in the 2026.2 line scheduled for 2026-09-21"
  - id: CVE-2026-83527
    cvss: "8.1"
    epss: 0.0145
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "versions before R10.8.2 / R10.7.3 / R10.6.4"
    fixed: "R10.8.2 / R10.7.3 / R10.6.4"
  - id: CVE-2026-18851
    cvss: "8.8"
    epss: 0.0102
    type: priv-esc
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "versions before 12.10.0.0 / 12.9.0.2 / 12.8.0.4"
    fixed: "12.10.0.0 / 12.9.0.2 / 12.8.0.4"
sources:
  - url: "https://www.ivanti.com/blog/september-2026-security-update"
    publisher: "Ivanti (vendor blog)"
    date: "2026-09-08"
    role: primary
  - url: "https://advisories.ncsc.nl/advisory?id=NCSC-2026-0358"
    publisher: "NCSC-NL (advisory NCSC-2026-0358, Neurons for ITSM)"
    date: "2026-09-09"
    role: corroborating
  - url: "https://advisories.ncsc.nl/advisory?id=NCSC-2026-0357"
    publisher: "NCSC-NL (advisory NCSC-2026-0357, Sentry)"
    date: "2026-09-09"
    role: corroborating
  - url: "https://advisories.ncsc.nl/advisory?id=NCSC-2026-0359"
    publisher: "NCSC-NL (advisory NCSC-2026-0359, EPMM)"
    date: "2026-09-09"
    role: corroborating
  - url: "https://www.securityweek.com/ivanti-patches-critical-flaws-across-enterprise-security-products/"
    publisher: "SecurityWeek"
    date: "2026-09-09"
    role: corroborating
  - url: "https://cybersecuritynews.com/multiple-ivanti-vulnerabilities/"
    publisher: "Cyber Security News"
    date: "2026-09-08"
    role: corroborating
closed_sources: []
evidence:
  - quote: "We have no evidence of these vulnerabilities being exploited in the wild."
    publisher: "Ivanti"
    source_url: "https://www.ivanti.com/blog/september-2026-security-update"
  - quote: "These vulnerabilities do not impact any other Ivanti solutions."
    publisher: "Ivanti"
    source_url: "https://www.ivanti.com/blog/september-2026-security-update"
  - quote: "these ITSM flaws were uncovered through the company's use of advanced large language models integrated into its product security and engineering workflows, marking a rare instance of AI-assisted vulnerability discovery being credited in a formal advisory."
    publisher: "Cyber Security News"
    source_url: "https://cybersecuritynews.com/multiple-ivanti-vulnerabilities/"
  - quote: "According to Ivanti's advisory, only CVE-2026-12744 and CVE-2026-12745 can be exploited without authentication."
    publisher: "SecurityWeek"
    source_url: "https://www.securityweek.com/ivanti-patches-critical-flaws-across-enterprise-security-products/"
verification: multi-source
sourcing_note: >
  Ivanti's own blog post confirms the ten-CVE count, the no-exploitation statement and the
  AI-assisted-discovery claim verbatim, but does not itself carry per-CVE CVSS vectors or affected
  version ranges; the linked per-CVE advisory pages (forums.ivanti.com) render only a Salesforce
  community JS shell on every transport tried and are not cited. Per-CVE CVSS scores and vectors
  are independently cross-verified against NVD's CVE 2.0 API; the CWE class and unauthenticated-vs
  -authenticated precondition for each CVE come from NCSC-NL's three independent per-product
  advisories (ITSM, Sentry, EPMM); the specific affected ITSM release list (2025.2/2025.3/2025.4/2026.1)
  and fixed-version dates come from SecurityWeek, since NCSC-NL's own ITSM advisory (NCSC-2026-0358)
  states only that Ivanti shipped the fix "in versie 2026.2" without giving the affected-release
  breakdown. Cyber Security News's article separately claims the Cloud/SaaS edition was already
  patched across all landscapes on 2026-08-09, requiring no customer action — that specific claim
  could not be independently re-confirmed (the article is unreachable on re-fetch, Cloudflare
  robot-challenge) and is not carried in the body, since it sits in tension with NCSC-NL's own
  product-status listing, which names the Cloud/SaaS edition as affected without any pre-patched
  qualifier.
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
  - "Patch Ivanti Neurons for ITSM to the September 2026 release now — CVE-2026-12744 and CVE-2026-12745 are unauthenticated, no-interaction deserialization flaws reaching full remote code execution on any internet-exposed instance."
updates: []
migrated_from: null
---

Ivanti's 2026-09-08 security update discloses ten CVEs across three product lines, none reported exploited ([Ivanti, 2026-09-08](https://www.ivanti.com/blog/september-2026-security-update)). Neurons for ITSM carries the most severe pair: CVE-2026-12744 and CVE-2026-12745, both CVSS 9.8 unauthenticated deserialization-of-untrusted-data flaws reaching remote code execution on the server with no credentials and no user interaction ([SecurityWeek, 2026-09-09](https://www.securityweek.com/ivanti-patches-critical-flaws-across-enterprise-security-products/)). Six further ITSM flaws need low-privilege authentication first: three missing-authorization bugs (CVE-2026-12645/12646/12647, CVSS 9.9) and three further deserialization paths (CVE-2026-12650 at 9.9, CVE-2026-12651/12648 at 8.8) all escalate an authenticated low-privilege session to code execution or full administrative control ([SecurityWeek, 2026-09-09](https://www.securityweek.com/ivanti-patches-critical-flaws-across-enterprise-security-products/); [Cyber Security News, 2026-09-08](https://cybersecuritynews.com/multiple-ivanti-vulnerabilities/)). Ivanti Sentry carries CVE-2026-83527 (CVSS 8.1), a high-attack-complexity authentication bypass that lets a remote unauthenticated attacker obtain administrative access to the Sentry platform ([NCSC-NL NCSC-2026-0357, 2026-09-09](https://advisories.ncsc.nl/advisory?id=NCSC-2026-0357)). Ivanti Endpoint Manager Mobile carries CVE-2026-18851 (CVSS 8.8), a missing-authorization flaw letting an authenticated low-privilege user escalate to full administrator ([NCSC-NL NCSC-2026-0359, 2026-09-09](https://advisories.ncsc.nl/advisory?id=NCSC-2026-0359)).

The September patch covers on-premises Neurons for ITSM versions 2025.2, 2025.3, 2025.4 and 2026.1; the fixes are also included in the 2026.2 release line, scheduled for 2026-09-21 ([SecurityWeek, 2026-09-09](https://www.securityweek.com/ivanti-patches-critical-flaws-across-enterprise-security-products/)). NCSC-NL's advisory additionally lists the Cloud/SaaS edition of Neurons for ITSM as affected, without stating a separate cloud remediation date ([NCSC-NL NCSC-2026-0358, 2026-09-09](https://advisories.ncsc.nl/advisory?id=NCSC-2026-0358)). Sentry is fixed in R10.8.2/R10.7.3/R10.6.4, EPMM in 12.10.0.0/12.9.0.2/12.8.0.4 ([SecurityWeek, 2026-09-09](https://www.securityweek.com/ivanti-patches-critical-flaws-across-enterprise-security-products/)). Ivanti states it has no evidence of exploitation for any of the ten and that no other Ivanti product is affected ([Ivanti, 2026-09-08](https://www.ivanti.com/blog/september-2026-security-update)). Notably, Ivanti states it has integrated multiple advanced large language models into its product-security and engineering workflows to identify vulnerabilities "especially those that are difficult to identify with traditional tooling, such as SAST and DAST," and credits this with surfacing some of the flaws disclosed today ([Ivanti, 2026-09-08](https://www.ivanti.com/blog/september-2026-security-update)) — a rare instance of AI-assisted vulnerability discovery being credited directly in a formal vendor advisory ([Cyber Security News, 2026-09-08](https://cybersecuritynews.com/multiple-ivanti-vulnerabilities/)).

**Defender takeaway:** the two unauthenticated ITSM RCEs are the priority — no credentials, no user interaction, full code execution on the server — so treat "no known exploitation today" as a narrow window rather than a reason to defer. Internet-exposed Neurons for ITSM instances should be patched first, with the six authenticated-escalation ITSM flaws following on the normal cycle once the unauthenticated pair is closed; Sentry and EPMM sit on their own separate advisories and release cycles.

