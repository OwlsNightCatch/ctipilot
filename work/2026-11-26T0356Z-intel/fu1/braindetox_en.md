---
title: "Juniper Session Smart: 10 CVEs, Fixes 7.0.5, 7.1.7, 7.2.3"
author: BrainDetox
url: https://braindetox.kr/en/posts/juniper_session_smart_security_update_2026_10.html
hostname: braindetox.kr
description: "Ten Juniper Session Smart Router and Conductor CVEs from KISA: fixed in 7.0.5, 7.1.7, 7.2.3, two score 9.8, two hinge on onboarding, no CISA KEV match."
sitename: BrainDetox
date: "2026-10-30"
categories: ['Tech & IT']
tags: ['Juniper', 'Session Smart Router', 'Session Smart Conductor', 'CVE-2026-103406', 'CVE-2026-103409', 'JSA112183', 'KISA security notice', 'security update', 'CVSS']
fingerprint: "36bd6f55eda882c9"
language: en
image: https://braindetox.kr/en/posts/images/juniper_session_smart_security_update_2026_10.png
pagetype: article
filedate: "2026-11-26"
---
# Juniper Session Smart: 10 CVEs, Fixes 7.0.5, 7.1.7, 7.2.3

## KISA notice of ten CVEs cross-read against NVD records: affected products, base scores, pre-onboarding exposure conditions, and exploitation status in one place

## What was published - the KISA notice and ten CVEs

KISA posted “Juniper Networks product security update advisory” on 2026-10-29. Its overview is two lines. Juniper Networks released security updates that resolve vulnerabilities in its products, and users running affected versions are advised to update to the latest version according to the resolution. The author is shown as the Vulnerability Management Center of the Digital Threat Response Division, and reference 1 is JSA112183 on the Juniper support portal.

The description section lists ten vulnerabilities: CVE-2026-103401, 103402, 103403, 103406, 103407, 103408, 103409, 103410, 103411, and CVE-2026-106079. The numbers 103404 and 103405 are not on the list. Neither the notice nor the NVD records say why the numbers are skipped, so no reason is guessed here. All ten records were published in NVD on 2026-10-28, and the only reference attached to each is the same Juniper advisory.

This article does three things. First, it counts the KISA tables and descriptions as written. Second, it carries over from the NVD records which component and which condition each vulnerability points to, together with the base score Juniper attached. Third, it searches the CISA Known Exploited Vulnerabilities catalog for the same identifiers. Facts and the interpretations drawn from them are kept apart, and any sentence containing an interpretation is marked “Interpretation”.

- Publisher: KISA Boho security notice, 2026-10-29. Vendor Juniper Networks, advisory number JSA112183.
- Products: Juniper Session Smart Router and Juniper Session Smart Conductor. Every one of the ten touches at least one of the two.
- KISA’s request: users of affected versions should update to the latest version according to the resolution. The notice adds a line to check the reference sites at the bottom and perform the update.
- Contact: KISA Cyber Civil Service Center, 118 without an area code.

## Ten at a glance - product, weakness, base score

The table below puts on one row the product split and weakness name from the KISA description lines, the component named in the NVD description, and the CVSS 3.1 base score and part of the vector that Juniper entered in NVD. Weakness names follow KISA wording; for some the NVD description spells the English name slightly differently. CVE-2026-103408, for example, is Stack-based Buffer Overflow in KISA and Stack Buffer Overflow in the NVD description. Both refer to the same DHCP client vulnerability.

| CVE | Product (KISA) | Weakness (KISA wording) | Component (NVD description) | Base score, vector | 
|---|---|---|---|---|
| CVE-2026-103401 | Router, Conductor | Link Following | Unauthenticated web server handlers | 8.8 · AV:N / PR:L | 
| CVE-2026-103402 | Router, Conductor | Insufficient Verification of Data Authenticity | PCLI | 8.8 · AV:N / PR:L | 
| CVE-2026-103403 | Router, Conductor | OS Command Injection | AccessManager | 8.8 · AV:N / PR:L | 
| CVE-2026-103406 | Conductor | OS Command Injection | AutomatedProvisioner | 9.8 · AV:N / PR:N | 
| CVE-2026-103407 | Router, Conductor | Path Traversal | ConfigDirector | 8.8 · AV:N / PR:L | 
| CVE-2026-103408 | Router | Stack-based Buffer Overflow | DHCP client | 8.8 · AV:A / PR:N | 
| CVE-2026-103409 | Router | Missing Authentication for Critical Function | Insecure endpoint running as root | 9.8 · AV:N / PR:N | 
| CVE-2026-103410 | Router | Integer Overflow or Wraparound | DPI certificate scanner | 7.5 · AV:N / PR:N | 
| CVE-2026-103411 | Router | Integer Underflow | DhcpMessageDecoder | 7.1 · AV:A / PR:N | 
| CVE-2026-106079 | Router, Conductor | OS Command Injection | AccessManager | 8.8 · AV:N / PR:L | 

- Router appears in nine CVEs. Only CVE-2026-103406 is Conductor-only and is the exception.
- Conductor appears in six CVEs: 103401, 103402, 103403, 103406, 103407 and 106079.
- AV in the vector is the attack path. AV:N is eight entries and AV:A is two (103408, 103411). AV:A is shown as ADJACENT\_NETWORK in the NVD record.
- PR in the vector is the privilege required. PR:N is five entries (103406, 103408, 103409, 103410, 103411) and PR:L is five (103401, 103402, 103403, 103407, 106079). All of these counts were tallied directly from the NVD records.

## Affected and fixed versions - reading the three-line table

The affected-products table in the KISA notice is long. It has 45 rows, but the shape is the same for all ten. Each product has three lines, and each line pairs an affected version with a fixed version. CVE-2026-103401, 103402, 103403, 103407 and 106079 have three lines each for Router and for Conductor, six lines per CVE (5 CVEs × 6 lines = 30), 103406 has three Conductor lines, and 103408, 103409, 103410 and 103411 have three Router lines each, twelve in total. That is 30 + 3 + 12 = 45 lines, and the row count was tallied directly from the notice table. The content of the lines is the same three pairs for all ten.

| Line | Affected version (KISA) | Fixed version (KISA) | 
|---|---|---|
| First | below 7.0.5 | 7.0.5 or later | 
| Second | below 7.1.7 | 7.1.7 or later | 
| Third | below 7.2.3 | 7.2.3 or later | 

- All ten share the same fixed versions. On the KISA table, moving to the fixed version for your own line, or later, covers all ten at once; this is a reading of the table structure, not a sentence from the Juniper advisory.
- Router and Conductor use the same fixed version numbers. There is no need to look up a different number for each product.
- Interpretation: it is natural to read the three lines as fixed versions for the 7.0, 7.1 and 7.2 lines. The notice itself never uses the word line and only states numeric comparisons. Whether this reading is right has to be checked against the Juniper advisory body.
- Whether a version with no row, for example a line older than 7.0.5, means no impact is a value the notice does not give.

## Reading the base scores - two at 9.8 and the conditions in the vectors

The CVSS 3.1 scores in the NVD records are values Juniper entered. The distribution is two at 9.8 (CVE-2026-103406, 103409), six at 8.8 (103401, 103402, 103403, 103407, 103408, 106079), one at 7.5 (103410) and one at 7.1 (103411), which sums to ten. All ten NVD records showed the status Awaiting Analysis on the retrieval date, 2026-10-30. The submitting source shown on the score entry is Juniper in all ten.

Scores are easy to read from the top down, but two entries at 8.8 can have different conditions. A vector with PR:L assumes the attacker already holds some low privilege, while PR:N assumes none is needed. The two 9.8 entries combine PR:N and AV:N with HIGH impact on confidentiality, integrity and availability. CVE-2026-103410, also PR:N and AV:N but HIGH on availability only, scores 7.5. The 8.8 group mixes the five PR:L entries with CVE-2026-103408, which carries the adjacent-network condition.

- The two at 9.8: CVE-2026-103406 (Conductor, AutomatedProvisioner, a remote attacker running commands as root through a specially crafted salt minion ID) and CVE-2026-103409 (Router, with a pre-onboarding condition). The NVD severity label is CRITICAL.
- The 7.5 and 7.1 entries weigh toward availability. 103410 has NONE for confidentiality and integrity and HIGH for availability only. 103411 has LOW for confidentiality and HIGH for availability.
- The score for CVE-2026-103410 is labelled Secondary in the NVD record. The other nine are Primary. The NVD record does not explain what the two labels mean.
- Description and vector have to be read together. The 103401 description says a local unprivileged user overwrites files through unauthenticated API endpoints, yet the vector is AV:N. The 103402 description assumes an attacker with write access to the model cache directory, while the vector is AV:N with PR:L. Only the fact that wording and vector notation use different terms is reported here. Which of the two better reflects real exposure is not written in the notice or the NVD record.
- A score measures how severe a vulnerability is; it does not tell you whether your own device is exposed. Exposure is decided by product, version, onboarding state and network position.

## Two entries with exposure conditions - before and after onboarding

Two NVD descriptions attach an exposure condition as a sentence. In both, the fork is whether the device has been onboarded to Mist or Conductor. The sentences read as follows.

- CVE-2026-103409 (Router): “Note that this vulnerability can only be exploited prior to the device being onboarded to Mist/Conductor. The issue can no longer be exploited once a device is onboarded to Mist/Conductor.”
- CVE-2026-103401 (Router, Conductor): “This vulnerability can be exploited on Mist-managed routers and on unmanaged Routers that have not yet been onboarded to a Conductor. Routers already managed by Conductor are not affected.”
- The two sentences set different conditions. 103409 says exploitation is no longer possible once onboarding to Mist/Conductor is done, while 103401 says exploitation is possible on Mist-managed routers. The records do not explain how a router onboarded to Mist is treated differently between the two.
- The descriptions of the other eight carry no onboarding condition. Whether that means they apply to every environment cannot be told from the NVD records.

The usable information is this. If your site has devices that are not yet onboarded, these two entries give a reason to list those devices and their exposure first. Conversely, even if every router is already under Conductor management, the record only says 103401 does not affect that setup, and the other eight have to be read separately.

## Conductor only, Router only

Of the ten, five touch both products, one touches Conductor only, and four touch Router only. By component name, the four Router-only entries are the DHCP client (103408), DhcpMessageDecoder (103411), the DPI certificate scanner (103410) and the insecure endpoint running as root (103409).

- CVE-2026-103406, the Conductor-only entry, is OS command injection in AutomatedProvisioner. The NVD description says a remote attacker can execute arbitrary commands as root via a specially crafted salt minion ID. The vector is PR:N.
- CVE-2026-103408, a Router-only entry, is described as letting an unauthenticated attacker on the local network achieve remote code execution via a malicious DHCP reply. The vector is AV:A.
- CVE-2026-103411 also uses a malicious DHCP reply as the path and is described as causing information disclosure and a denial of service. The score is 7.1.
- CVE-2026-103410 is described as an integer overflow in the DPI certificate scanner that leads to a denial of service through a specially crafted TLS server certificate. The score is 7.5.

The practical meaning of the split is to fix the scope of the check. Operating Router alone means reading nine entries, Conductor alone six, and operating both means all ten. In one line: Conductor is in six of the ten, Router in nine.

## Exploitation status - what zero KEV matches says

The KISA notice has no wording about exploitation, and neither do the NVD descriptions. So the CISA Known Exploited Vulnerabilities (KEV) JSON was fetched on 2026-10-30 and searched for all ten identifiers. The file carried catalog version 2026.10.29, release time 2026-10-29T19:09:34Z and a count of 1764 entries. None of the ten matched.

There is one more item. The NVD record of CVE-2026-103410 carries an SSVC assessment posted in the CISA Coordinator role (timestamp 2026-10-29T01:37:38Z), with the values exploitation: none, automatable: yes and technicalImpact: partial. The NVD records of the other nine had no such assessment. The exploitation value none is the judgement that assessment made at that moment.

- Fact: the KEV JSON retrieved on 2026-10-30 (version 2026.10.29) does not contain the ten identifiers.
- Fact: the SSVC entry for 103410 reads exploitation none, automatable yes, technicalImpact partial, timestamped 2026-10-29T01:37Z.
- Interpretation: having no KEV entry is not proof that no exploitation exists. This value belongs to the file retrieved on the day of the check (2026-10-30).
- Score and exploitation are different axes. How an exploitation fact changes the ordering is covered separately in the [article on exploited-vulnerability priority](https://braindetox.kr/en/posts/exploited_vulnerability_priority.html).

## Who is affected and how - scope table

The table splits which CVEs to read first by operating pattern. Every cell comes from facts in the sections above, and no update timing or priority is asserted.

| Operating pattern | CVEs that apply (KISA description lines) | What to look at first | 
|---|---|---|
| Running Session Smart Router | 9 (all except 103406) | Whether the version is below 7.0.5, 7.1.7 or 7.2.3 | 
| Running Session Smart Conductor | 6 (103401, 103402, 103403, 103406, 103407, 106079) | Whether the fixed version is applied for 103406 (score 9.8, remote, no privilege) | 
| Router not yet onboarded | 103409, 103401 | Onboarding state to Mist/Conductor and exposed network segments | 
| Router using DHCP on a shared segment | 103408, 103411 | Who can reach the segment where DHCP replies travel | 

- General users: if you do not use these two products, the notice does not apply to you. KISA advises users of affected versions to update.
- Security staff: the ten are bundled in one advisory and share fixed versions, so a single device inventory and version comparison can narrow the scope.
- Managed-service providers: confirming whether the entrusted devices include these products, and whether the onboarding state is known, is what settles the scope of responsibility.

## What you can do now - six questions to check

These are questions, not commands. Because the Juniper advisory body was not retrieved, no configuration paths or check commands are given, and only questions readable from the KISA notice and the NVD descriptions are listed.

- Does the organisation have Session Smart Router or Session Smart Conductor? If so, how many of each, and what is the current version of each device?
- Is each version at or above the fixed version of its own line among 7.0.5, 7.1.7 and 7.2.3? If the way lines are separated is unclear, read the affected-version sentence in the Juniper advisory body.
- Are there devices not yet onboarded to Mist or Conductor? If so, which network segment do they face?
- Does any Router interface receive DHCP replies? Since the 103408 and 103411 descriptions name the DHCP reply as the path, find out who can reach that segment.
- If you run Conductor, who can use the path that salt minions connect through? The 103406 description mentions a salt minion ID, so list the reachable range.
- Has the update procedure and any temporary mitigation been read in the body of JSA112183 on the Juniper support portal? That is what KISA means by checking the reference sites at the bottom.

Broader management checks are in the [summary of the KISA enterprise security hardening advisory](https://braindetox.kr/en/posts/kisa_enterprise_security_hardening_advisory_oct_2026.html). For another case that carries per-product fixed versions from a KISA notice into a table, see the [Synology security update summary](https://braindetox.kr/en/posts/synology_security_update_2026_10.html).

## Judgement criteria for ordering the update

No forecast beyond the source conclusions is given. The following turns the facts above into conditions.

- A. If your version is at or above the fixed version for its line: on the KISA table the ten do not apply. Still, compare once which line of the table your version string belongs to.
- B. If you run Conductor on a version below the fixed one: CVE-2026-103406 is there with score 9.8, PR:N and AV:N. The other five also apply to the same Conductor.
- C. If you have Router units not yet onboarded: the conditions of CVE-2026-103409 (score 9.8) and 103401 overlap with that state. A list of onboarding states is needed before a decision can stand.
- D. If updating at once is difficult: the KISA notice has no temporary mitigation wording. Read the mitigation guidance in the Juniper advisory body, and ask the vendor if there is none.
- E. Do not postpone solely because it is absent from KEV: look at the score, the exposure conditions and how important the service on the device is.

## What could not be confirmed

- The body of Juniper advisory JSA112183. The support portal address responded, but the retrieved page did not contain the advisory body, so there is no value for temporary mitigation, update procedure or the affected-version sentence.
- Whether reading the three-line affected-version table as fixed versions per line is correct. The KISA table gives only numeric comparisons.
- Whether versions older than 7.0.5 (6.x and so on) fall inside the affected range. The table has no row for them.
- The exposure conditions of the eight entries whose descriptions have no onboarding condition.
- The meaning of the Primary and Secondary labels in the NVD records, and why CVE-2026-103404 and 103405 are not on the list. The sources give no value.
- NVD’s own analysis score. The status was Awaiting Analysis on the retrieval date and the only score in the records was the one Juniper submitted; the records may change later.
- Exploitation information from sources other than KEV (vendor notices, security vendor reports). Only KEV was queried here.

## References

- [Juniper Networks product security update advisory (Korean)](https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&menuNo=205020&nttId=72249) - KISA Boho security notice, 2026-10-29. The list of ten, the affected-version table, fixed versions.
- [Juniper security advisory JSA112183](https://supportportal.juniper.net/JSA112183) - Juniper support portal. The page retrieved for this article had no body.
- [CVE-2026-103406 record](https://nvd.nist.gov/vuln/detail/CVE-2026-103406) - NVD. Conductor AutomatedProvisioner, score 9.8. The other nine can be read at addresses of the same form with the number changed.
- [CVE-2026-103409 record](https://nvd.nist.gov/vuln/detail/CVE-2026-103409) - NVD. Router, pre-onboarding condition, score 9.8.
- [Known Exploited Vulnerabilities catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) - CISA. Zero matches for the ten in the 2026.10.29 JSON.

## Frequently asked questions

### How many CVEs does the Juniper Session Smart advisory cover, and which products?

The KISA notice lists ten CVEs. Session Smart Router appears in nine of them and Session Smart Conductor in six, with five naming both. The per-product split was counted directly from the KISA description lines.

### What are the fixed versions?

The KISA table repeats the same three lines for every CVE: below 7.0.5 is fixed at 7.0.5 or later, below 7.1.7 at 7.1.7 or later, and below 7.2.3 at 7.2.3 or later. KISA told users to check the reference sites at the bottom and perform the update.

### Is any of these vulnerabilities already being exploited?

The CISA Known Exploited Vulnerabilities catalog (version 2026.10.29), fetched on 2026-10-30, was searched for all ten identifiers and returned zero matches. Absence from the catalog does not mean there is no exploitation, so scores and exposure conditions still matter when ordering work.

### Do any of the vulnerabilities depend on whether a device is onboarded?

Two NVD descriptions carry a condition. CVE-2026-103409 can only be exploited before the device is onboarded to Mist or Conductor. CVE-2026-103401 can be exploited on Mist-managed routers and on unmanaged routers not yet onboarded to a Conductor, while routers already managed by Conductor are not affected.

### Where is the Juniper advisory text and any temporary mitigation?

Reference 1 in the KISA notice is JSA112183 on the Juniper support portal. The page retrieved for this article did not contain the advisory body, so no mitigation wording is quoted. Read the advisory on the portal for the update procedure and any mitigation guidance.
