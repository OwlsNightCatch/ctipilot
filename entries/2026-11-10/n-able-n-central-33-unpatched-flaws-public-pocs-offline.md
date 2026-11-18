---
schema: 1
kind: vulnerability
title: 'N-able N-central: 33 alleged flaws published, and Hotfix 3 (build 2026.4.1.39, 2026-11-16) now fixes 17 more CVE ids and blocks the Legacy API permanently, which 4EverAble2Shell (Apache Axis CVE-2026-90436, exploited on at least 21 servers) and Agent2Shell need; N-able does not say either chain is fixed, and public proof-of-concept code exists for the 17'
headline: 'N-central: Hotfix 3 fixes 17 more CVEs and blocks the Legacy API; 4EverAble2Shell exploited; upgrade Agents too'
summary: 'An independent researcher published proof-of-concept code on 2026-11-08 and 2026-11-09 for what Huntress counts as 33 critical flaws in N-able''s N-central appliance, and a second disclosure on 2026-11-12 added 4EverAble2Shell, a chain through Apache Axis (CVE-2026-90436) that works against Hotfix 2 when the Legacy API is on and is exploited on at least 21 production servers, and Agent2Shell, SYSTEM commands on managed Windows endpoints. Hotfix 2 (build 2026.4.1.26, 2026-11-10) fixed seven CVE ids and Hotfix 3 (build 2026.4.1.39, 2026-11-16) fixes 17 more, hardens how Agents and Probes authenticate and blocks the Legacy API permanently, but N-able does not name either chain or say it is fixed; Huntress reports public proof-of-concept code for all 17 and no exploitation of them in its partners'' environments. Every on-premises server and every Agent and Probe must be on Hotfix 3, including those already on Hotfix 2.'
discovered_at: '2026-11-10T03:51:00Z'
updated_at: "2026-11-18T05:12:35Z"
event_date: '2026-11-09'
run_id: 2026-11-10T0255Z-intel
priority: high
immediate_action: null
tags:
  - vulnerabilities
  - supply-chain
  - rce
  - pre-auth
  - poc-public
  - actively-exploited
  - patch-available
regions:
  - global
sectors:
  - technology
entities:
  - incident:n-able-n-central-able2shell-disclosure-2026-11
techniques:
  - T1190
  - T1059
  - T1068
  - T1136
  - T1552
  - T1070
  - T1070.004
  - T1105
  - T1496.001
  - T1543.002
  - T1053.003
  - T1072
affected_products:
  - N-able N-central
  - Apache Axis
cves:
  - id: CVE-2026-125883
    cvss: '9.3'
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status:
      - poc-public
      - patch-available
    affected: 'N-central before 2026.4 Hotfix 2 (CNA wording: before 26.4.1); multiple XML external entity flaws'
    fixed: N-central 2026.4 Hotfix 2, build 2026.4.1.26
  - id: CVE-2026-125881
    cvss: '9.3'
    epss: null
    type: ssrf
    vector: zero-click
    auth: pre-auth
    status:
      - poc-public
      - patch-available
    affected: 'N-central before 2026.4 Hotfix 2 (CNA wording: before 26.4.1); schema-hint SSRF through service-import schema validation'
    fixed: N-central 2026.4 Hotfix 2, build 2026.4.1.26
  - id: CVE-2026-125878
    cvss: '8.7'
    epss: null
    type: rce
    vector: zero-click
    auth: post-auth
    status:
      - poc-public
      - patch-available
    affected: 'N-central before 2026.4 Hotfix 2 (CNA wording: before 26.4.1); multiple OGNL injection flaws per Huntress'
    fixed: N-central 2026.4 Hotfix 2, build 2026.4.1.26
  - id: CVE-2026-125882
    cvss: '8.6'
    epss: null
    type: path-traversal
    vector: zero-click
    auth: admin-required
    status:
      - poc-public
      - patch-available
    affected: 'N-central before 2026.4 Hotfix 2 (CNA wording: before 26.4.1); remote code execution through a file-repository upload path traversal per Huntress'
    fixed: N-central 2026.4 Hotfix 2, build 2026.4.1.26
  - id: CVE-2026-125879
    cvss: '8.6'
    epss: null
    type: priv-esc
    vector: local
    auth: admin-required
    status:
      - poc-public
      - patch-available
    affected: 'N-central before 2026.4 Hotfix 2 (CNA wording: before 26.4.1); local privilege escalation to root through a writable syslog-ng configuration per Huntress'
    fixed: N-central 2026.4 Hotfix 2, build 2026.4.1.26
  - id: CVE-2026-91000
    cvss: '8.4'
    epss: null
    type: priv-esc
    vector: local
    auth: post-auth
    status:
      - poc-public
      - patch-available
    affected: 'N-central before 2026.4 Hotfix 2 (CNA wording: before 2026.4.1); insecure inter-process channels lead to local privilege escalation per Huntress'
    fixed: N-central 2026.4 Hotfix 2, build 2026.4.1.26
  - id: CVE-2026-125880
    cvss: '8.3'
    epss: null
    type: xss
    vector: user-interaction
    auth: admin-required
    status:
      - poc-public
      - patch-available
    affected: 'N-central before 2026.4 Hotfix 2 (CNA wording: before 26.4.1); stored XSS through patch metadata in an administrator context per Huntress'
    fixed: N-central 2026.4 Hotfix 2, build 2026.4.1.26
  - id: CVE-2026-90436
    cvss: null
    epss: null
    type: deserialization
    vector: zero-click
    auth: pre-auth
    status:
      - exploited
      - mitigation-only
    affected: Apache Axis 1.x through 1.4 as embedded in on-premises N-central with the Legacy API turned on and reachable, builds through 2026.4.1.26 (Hotfix 2)
    fixed: 'Hotfix 3 (build 2026.4.1.39) blocks the Legacy API that the chain needs permanently, but N-able does not say it fixes the Axis flaw, and the Apache Axis project offers a source patch but does not expect to release an Axis 1.x fix'
  - id: CVE-2026-129271
    cvss: '8.5'
    epss: null
    type: priv-esc
    vector: local
    auth: post-auth
    status:
      - poc-public
      - patch-available
    affected: 'N-central Patch Management Component before 2.14.4.5829 per the CNA record; Patch Management Engine local privilege escalation through attacker-controlled metadata'
    fixed: 'Patch Management Component 2.14.4.5829 or later; N-able lists the id under N-central 2026.4 Hotfix 3, build 2026.4.1.39'
  - id: CVE-2026-129272
    cvss: '9.3'
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status:
      - poc-public
      - patch-available
    affected: 'N-central builds before 2026.4 Hotfix 3 (CNA wording: before 2026.4.1 HF3); appliance authentication to an agent-facing API with a predictable credential, which lets an unauthenticated attacker impersonate an appliance'
    fixed: N-central 2026.4 Hotfix 3, build 2026.4.1.39, with Agents and Probes at 2026.4.1 HF3
  - id: CVE-2026-129273
    cvss: '8.6'
    epss: null
    type: rce
    vector: zero-click
    auth: admin-required
    status:
      - poc-public
      - patch-available
    affected: 'N-central builds before 2026.4 Hotfix 3 (CNA wording: before 2026.4.1 HF3); Audit Export setting injected into the syslog configuration, command execution as root by a product administrator'
    fixed: N-central 2026.4 Hotfix 3, build 2026.4.1.39, with Agents and Probes at 2026.4.1 HF3
  - id: CVE-2026-129274
    cvss: '8.7'
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status:
      - poc-public
      - patch-available
    affected: 'N-central builds before 2026.4 Hotfix 3 (CNA wording: before 2026.4.1 HF3); ServerMMS2 RemoteExecutionTaskSubmit without authentication, forged task results for any customer'
    fixed: N-central 2026.4 Hotfix 3, build 2026.4.1.39, with Agents and Probes at 2026.4.1 HF3
  - id: CVE-2026-129275
    cvss: '8.2'
    epss: null
    type: info-disclosure
    vector: zero-click
    auth: pre-auth
    status:
      - poc-public
      - patch-available
    affected: 'N-central builds before 2026.4 Hotfix 3 (CNA wording: before 2026.4.1 HF3); repositoryItemGet without authentication, download of any customer''s Automation Manager policy with embedded scripts and parameters'
    fixed: N-central 2026.4 Hotfix 3, build 2026.4.1.39, with Agents and Probes at 2026.4.1 HF3
  - id: CVE-2026-129276
    cvss: '6.9'
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status:
      - poc-public
      - patch-available
    affected: 'N-central builds before 2026.4 Hotfix 3 (CNA wording: before 2026.4.1 HF3); ServerMMS2 AssetDiscoSimplifiedInfoSubmit without authentication, overwrite of asset data'
    fixed: N-central 2026.4 Hotfix 3, build 2026.4.1.39, with Agents and Probes at 2026.4.1 HF3
  - id: CVE-2026-129277
    cvss: '6.9'
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status:
      - poc-public
      - patch-available
    affected: 'N-central builds before 2026.4 Hotfix 3 (CNA wording: before 2026.4.1 HF3); MaintActionGet without authentication, read and cancel of pending maintenance actions'
    fixed: N-central 2026.4 Hotfix 3, build 2026.4.1.39, with Agents and Probes at 2026.4.1 HF3
  - id: CVE-2026-129278
    cvss: '6.9'
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status:
      - poc-public
      - patch-available
    affected: 'N-central builds before 2026.4 Hotfix 3 (CNA wording: before 2026.4.1 HF3); remoteControlMSPAStartEndTimeSubmit without authentication, alteration of Take Control task state, times and audit log entries'
    fixed: N-central 2026.4 Hotfix 3, build 2026.4.1.39, with Agents and Probes at 2026.4.1 HF3
  - id: CVE-2026-129279
    cvss: '6.9'
    epss: null
    type: info-disclosure
    vector: zero-click
    auth: pre-auth
    status:
      - poc-public
      - patch-available
    affected: 'N-central builds before 2026.4 Hotfix 3 (CNA wording: before 2026.4.1 HF3); password reset responses that distinguish valid accounts, user enumeration'
    fixed: N-central 2026.4 Hotfix 3, build 2026.4.1.39, with Agents and Probes at 2026.4.1 HF3
  - id: CVE-2026-129280
    cvss: '9.3'
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status:
      - poc-public
      - patch-available
    affected: 'N-central builds before 2026.4 Hotfix 3 (CNA wording: before 2026.4.1 HF3); ServerUI and ServerUI2 SOAP operations that do not verify session, permissions or customer scope, in some cases without authentication'
    fixed: N-central 2026.4 Hotfix 3, build 2026.4.1.39, with Agents and Probes at 2026.4.1 HF3
  - id: CVE-2026-129281
    cvss: '8.5'
    epss: null
    type: priv-esc
    vector: zero-click
    auth: post-auth
    status:
      - poc-public
      - patch-available
    affected: 'N-central builds before 2026.4 Hotfix 3 (CNA wording: before 2026.4.1 HF3); view-only users can write device execution configuration that the Windows agent acts on'
    fixed: N-central 2026.4 Hotfix 3, build 2026.4.1.39, with Agents and Probes at 2026.4.1 HF3
  - id: CVE-2026-129282
    cvss: '8.7'
    epss: null
    type: rce
    vector: zero-click
    auth: post-auth
    status:
      - poc-public
      - patch-available
    affected: 'N-central builds before 2026.4 Hotfix 3 (CNA wording: before 2026.4.1 HF3); test email delivery passes option characters to the mail program, argument injection by an authenticated attacker'
    fixed: N-central 2026.4 Hotfix 3, build 2026.4.1.39, with Agents and Probes at 2026.4.1 HF3
  - id: CVE-2026-129283
    cvss: '7.1'
    epss: null
    type: info-disclosure
    vector: zero-click
    auth: post-auth
    status:
      - poc-public
      - patch-available
    affected: 'N-central builds before 2026.4 Hotfix 3 (CNA wording: before 2026.4.1 HF3); XML external entity injection in the custom service import, file read and outbound requests by an authenticated attacker'
    fixed: N-central 2026.4 Hotfix 3, build 2026.4.1.39, with Agents and Probes at 2026.4.1 HF3
  - id: CVE-2026-129284
    cvss: '5.3'
    epss: null
    type: ssrf
    vector: zero-click
    auth: post-auth
    status:
      - poc-public
      - patch-available
    affected: 'N-central builds before 2026.4 Hotfix 3 (CNA wording: before 2026.4.1 HF3); Report Manager and Data Export settings connect to arbitrary hosts, loopback and internal addresses included'
    fixed: N-central 2026.4 Hotfix 3, build 2026.4.1.39, with Agents and Probes at 2026.4.1 HF3
  - id: CVE-2026-129285
    cvss: '5.3'
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: post-auth
    status:
      - poc-public
      - patch-available
    affected: 'N-central builds before 2026.4 Hotfix 3 (CNA wording: before 2026.4.1 HF3); XMPP action responses not tied to the appliance that received the request, forged responses between appliances'
    fixed: N-central 2026.4 Hotfix 3, build 2026.4.1.39, with Agents and Probes at 2026.4.1 HF3
  - id: CVE-2026-129286
    cvss: '9.2'
    epss: null
    type: path-traversal
    vector: zero-click
    auth: pre-auth
    status:
      - poc-public
      - patch-available
    affected: 'N-central builds before 2026.4 Hotfix 3 (CNA wording: before 2026.4.1 HF3); software update metadata version and download location not validated, file write and code execution as the service account by an attacker who can supply the metadata'
    fixed: N-central 2026.4 Hotfix 3, build 2026.4.1.39, with Agents and Probes at 2026.4.1 HF3
  - id: CVE-2026-129287
    cvss: '8.3'
    epss: null
    type: info-disclosure
    vector: zero-click
    auth: pre-auth
    status:
      - poc-public
      - patch-available
    affected: 'N-central builds before 2026.4 Hotfix 3 (CNA wording: before 2026.4.1 HF3); XML external entity injection in software repository files, file read and outbound requests by an attacker who can supply the files'
    fixed: N-central 2026.4 Hotfix 3, build 2026.4.1.39, with Agents and Probes at 2026.4.1 HF3
sources:
  - url: https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains
    publisher: Huntress
    date: '2026-11-09'
    role: primary
  - url: https://www.bleepingcomputer.com/news/security/n-able-takes-cloud-platform-offline-after-30-plus-zero-days-published/
    publisher: BleepingComputer
    date: '2026-11-09'
    role: corroborating
  - url: https://fieldeffect.com/blog/n-central-offline-alleged-zero-days
    publisher: Field Effect
    date: '2026-11-09'
    role: corroborating
  - url: https://censys.com/advisory/n-able-n-central/
    publisher: Censys
    date: '2026-11-09'
    role: corroborating
  - url: https://status.n-able.com/2026/11/10/n-central-2026-4-hf2-release-notes/
    publisher: N-able (N-central 2026.4 HF2 release notes)
    date: '2026-11-10'
    role: primary
  - url: https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-122942
    publisher: N-able CNA record CVE-2026-125883, via ENISA EUVD
    date: '2026-11-10'
    role: corroborating
  - url: https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-122961
    publisher: N-able CNA record CVE-2026-125881, via ENISA EUVD
    date: '2026-11-10'
    role: corroborating
  - url: https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains
    publisher: Huntress (update of 2026-11-10)
    date: '2026-11-10'
    role: corroborating
  - url: https://www.bleepingcomputer.com/news/security/new-n-able-4everable2shell-zero-day-exploited-hours-after-poc-released/
    publisher: BleepingComputer
    date: '2026-11-12'
    role: corroborating
  - url: https://huntback.io/blog/ncentral-4everable2shell-miners-on-live-servers
    publisher: Huntback
    date: '2026-11-12'
    role: corroborating
  - url: https://previdian.com/VULN-2026-0009
    publisher: Previdian
    date: '2026-11-12'
    role: corroborating
  - url: https://thehackernews.com/2026/11/new-n-central-exploits-work-against.html
    publisher: The Hacker News
    date: '2026-11-12'
    role: corroborating
  - url: https://www.tenable.com/blog/able2shell-frequently-asked-questions-for-reported-n-able-n-central-zero-day-vulnerabilities
    publisher: Tenable
    date: '2026-11-12'
    role: corroborating
  - url: https://openwall.com/lists/oss-security/2026/11/06/12
    publisher: Apache Axis project (via oss-security)
    date: '2026-11-06'
    role: corroborating
  - url: https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains
    publisher: Huntress (updates of 2026-11-12)
    date: '2026-11-12'
    role: corroborating
  - url: https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains
    publisher: Huntress (updates of 2026-11-13)
    date: '2026-11-13'
    role: corroborating
  - url: https://status.n-able.com/2026/11/16/n-central-2026-4-hf3-release-notes/
    publisher: N-able (N-central 2026.4 HF3 release notes)
    date: '2026-11-16'
    role: primary
  - url: https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains
    publisher: Huntress (updates of 2026-11-17)
    date: '2026-11-17'
    role: corroborating
closed_sources: []
evidence:
  - quote: N-able said it has not seen active exploitation of the vulnerabilities as of November 9 at 15:15:00 UTC.
    publisher: Huntress
    source_url: https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains
  - quote: One of the most critical exploit chains abuses an unauthenticated XXE vulnerability in N-central's service-import functionality to steal a trusted local session, reset an account password, and execute commands on the server as the nable user.
    publisher: BleepingComputer
    source_url: https://www.bleepingcomputer.com/news/security/n-able-takes-cloud-platform-offline-after-30-plus-zero-days-published/
  - quote: Several of the published PoCs describe unauthenticated attack paths, so if they work as described, network reachability is a prerequisite for exploitation.
    publisher: Field Effect
    source_url: https://fieldeffect.com/blog/n-central-offline-alleged-zero-days
  - quote: As of November 9, 2026, N-able has published no mechanism detail, affected versions, or fixed versions.
    publisher: Censys
    source_url: https://censys.com/advisory/n-able-n-central/
  - quote: N-central 2026.4 Hotfix 2 is a critical security update.
    publisher: N-able
    source_url: https://status.n-able.com/2026/11/10/n-central-2026-4-hf2-release-notes/
  - quote: All customers, both hosted and on-premises, must upgrade their Agents and Probes.
    publisher: N-able
    source_url: https://status.n-able.com/2026/11/10/n-central-2026-4-hf2-release-notes/
  - quote: scanning activity associated with the published proof-of-concept code
    publisher: Huntress
    source_url: https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains
  - quote: Servers running 2026.4 HF2 with Legacy API disabled are not exposed to this exploit chain.
    publisher: Huntress (updates of 2026-11-12)
    source_url: https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains
  - quote: The servers that had applied the patch were compromised just the same.
    publisher: Huntback
    source_url: https://huntback.io/blog/ncentral-4everable2shell-miners-on-live-servers
  - quote: "Additionally, N-able confirmed that Agent2Shell exploitation (like 4EverAble2Shell) requires the non-default Legacy API to be enabled."
    publisher: Huntress
    source_url: https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains
  - quote: "on November 13 at 13:40:25 UTC, N-able said that it has identified Indicators of Compromise (IoCs) for customers that haven't disabled the Legacy API."
    publisher: Huntress
    source_url: https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains
  - quote: N-central 2026.4 Hotfix 3 is a critical security update.
    publisher: N-able
    source_url: https://status.n-able.com/2026/11/16/n-central-2026-4-hf3-release-notes/
  - quote: We have removed the configuration option for legacy APIs, and legacy APIs are now permanently blocked.
    publisher: N-able
    source_url: https://status.n-able.com/2026/11/16/n-central-2026-4-hf3-release-notes/
  - quote: Public proof-of-concept code for all 17 CVEs was released on the evening of November 16, shortly after the hotfix.
    publisher: Huntress (updates of 2026-11-17)
    source_url: https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains
verification: multi-source
sourcing_note: 'N-able''s release notes carry the builds, scope and upgrade order; the CVE descriptions are Huntress''s, with CVSS 4.0 scores and affected versions from N-able''s CNA records in ENISA''s database. The 33-flaw count and every technical claim are the researcher''s and unvalidated; BleepingComputer dates the repository to the evening of 8 November, Censys the disclosure to 8 November and the proof of concept to 9 November. Exploitation of the second chain rests on Huntback''s mining-pool count and Previdian''s honeypot as BleepingComputer and Tenable report, the proof-of-concept claim for the 17 new ids on Huntress alone, and N-able''s statements are as those sources relay them.'
confidence: medium
references:
  - 2026-11-11/confluence-dc-cve-2026-90436-apache-axis-remote-api-rce
  - 2026-08-03/cve-2026-18577-n-able-n-central-auth-bypass-exploited
  - 2026-09-07/cve-2026-86206-86207-86218-n-able-n-central-third-chain
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - Upgrade every on-premises N-central server to 2026.4 Hotfix 3 (build 2026.4.1.39) and every Agent and Probe to 2026.4.1 HF3 even if already on Hotfix 2, confirm the Legacy API is disabled and not reachable from the internet, and on any server that had the Legacy API on check the web logs for POST requests to the Axis endpoint /dms/services/ServerUI carrying a SOAP fault and the host for a symlink at the N-central flag file path, treating a hit as a full compromise, because public proof-of-concept code exists for all 17 new CVE ids, Hotfix 2 did not stop 4EverAble2Shell and N-able does not say Hotfix 3 fixes it.
updates:
  - at: '2026-11-11T03:49:03Z'
    run_id: 2026-11-11T0256Z-intel
    type: update
    summary: N-able released N-central 2026.4 Hotfix 2 (build 2026.4.1.26) on 2026-11-10 with seven CVE ids, which replaces the entry's statements that no fix, no CVE ids and no affected or fixed builds existed, and reports scanning activity associated with the public proof-of-concept code but no evidence of successful exploitation; on-premises servers must be upgraded and every Agent and Probe upgraded too.
    fields:
      - title
      - headline
      - summary
      - tags
      - cves
      - sources
      - evidence
      - sourcing_note
      - actions
      - body
  - at: '2026-11-13T03:54:38Z'
    run_id: 2026-11-13T0256Z-intel
    type: update
    summary: The researcher's second exploit set, 4EverAble2Shell, chains Apache Axis CVE-2026-90436 with a root escalation, works against Hotfix 2 when the Legacy API is on and is exploited on at least 21 production servers per Huntback, with attempts recorded on Previdian's honeypot; N-able has no fix yet and says it has seen no signs of compromise.
    fields:
      - title
      - headline
      - summary
      - tags
      - techniques
      - affected_products
      - cves
      - sources
      - evidence
      - sourcing_note
      - references
      - actions
      - body
  - at: "2026-11-14T04:00:03Z"
    run_id: 2026-11-14T0255Z-intel
    type: update
    summary: >
      N-able confirmed via Huntress that Agent2Shell, the researcher's other chain set that gives an
      unauthenticated attacker SYSTEM commands on managed Windows endpoints, also needs the non-default
      Legacy API, and N-able has published indicators of compromise for customers that have not disabled
      it; N-able still has no fix, and its earlier statement that it saw no signs of compromise predates
      the indicators.
    fields: [title, headline, summary, techniques, sources, evidence, sourcing_note, body]
  - at: "2026-11-15T15:01:23Z"
    run_id: 2026-11-15T1407Z-audit
    type: correction
    internal: true
    summary: >
      N-able requires every customer to upgrade Agents and Probes and recommends Agents first; the summary
      and the 2026-11-11 section no longer present the order as mandatory.
    fields: [summary, body]
  - at: "2026-11-18T05:12:35Z"
    run_id: 2026-11-18T0356Z-intel
    type: update
    summary: >
      N-able released Hotfix 3 (build 2026.4.1.39, 2026-11-16): 17 more CVE ids fixed, Agent and Probe
      authentication hardened, the Legacy API permanently blocked, and every Agent and Probe must be
      upgraded even from Hotfix 2. N-able does not say Hotfix 3 fixes 4EverAble2Shell or Agent2Shell, and
      Huntress reports public proof-of-concept code for all 17 ids.
    fields: [actions, body, cves, evidence, headline, sources, sourcing_note, summary, tags, title]
migrated_from: null
---
An independent researcher published what Huntress counts as 33 critical flaws in the N-central appliance, chaining into four exploits, and N-able took its hosted environments offline on 2026-11-09 ([Huntress, 2026-11-09](https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains)).

On 2026-11-10 N-able released N-central 2026.4 Hotfix 2, build 2026.4.1.26, for which Huntress lists seven CVE ids ([N-able, 2026-11-10](https://status.n-able.com/2026/11/10/n-central-2026-4-hf2-release-notes/); [Huntress, 2026-11-10](https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains); [N-able CNA record, 2026-11-10](https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-122942); [N-able CNA record, 2026-11-10](https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-122961)).

On 2026-11-12 the researcher published a second set. 4EverAble2Shell is unauthenticated command execution as root that requires the Legacy API to be enabled, per BleepingComputer; it chains CVE-2026-90436, an Apache Axis 1.x deserialization flaw for which Apache does not expect a fix, with a root escalation in N-central's maintenance helper ([BleepingComputer, 2026-11-12](https://www.bleepingcomputer.com/news/security/new-n-able-4everable2shell-zero-day-exploited-hours-after-poc-released/); [Apache Axis project, 2026-11-06](https://openwall.com/lists/oss-security/2026/11/06/12); [Huntback, 2026-11-12](https://huntback.io/blog/ncentral-4everable2shell-miners-on-live-servers)). Huntback counts at least 21 servers, 19 of them on Hotfix 2, in North America, South Africa and Europe but not Switzerland, and Previdian's sensors recorded attempts at the chain ([Huntback, 2026-11-12](https://huntback.io/blog/ncentral-4everable2shell-miners-on-live-servers); [Previdian, 2026-11-12](https://previdian.com/VULN-2026-0009)). Agent2Shell is a set of more than ten issues in how the server talks to Windows Agents and Probes, two chains of which let an unauthenticated attacker who can reach the server run commands as SYSTEM on managed endpoints; N-able confirmed it also requires the non-default Legacy API ([The Hacker News, 2026-11-12](https://thehackernews.com/2026/11/new-n-central-exploits-work-against.html); [Huntress, 2026-11-13](https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains)). N-able has published indicators of compromise for customers that have not disabled the Legacy API ([Huntress, 2026-11-13](https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains)). Hotfix 3 of 2026-11-16 fixes 17 more CVE ids, hardens how Agents and Probes authenticate and blocks the Legacy API permanently, without naming 4EverAble2Shell or Agent2Shell or saying either is fixed ([N-able, 2026-11-16](https://status.n-able.com/2026/11/16/n-central-2026-4-hf3-release-notes/)); Huntress reports public proof-of-concept code for all 17 and no exploitation of them in its partners' environments ([Huntress, 2026-11-17](https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains)).

**Exposure:** an on-premises N-central server, yours or an IT provider's, below build 2026.4.1.39, and for the second set any build up to Hotfix 2 when the Legacy API, off by default, is on and reachable ([Huntress, 2026-11-13](https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains)); an Agent or Probe not on Hotfix 3 can be impersonated ([N-able, 2026-11-16](https://status.n-able.com/2026/11/16/n-central-2026-4-hf3-release-notes/)). A compromised server reaches the systems N-central manages ([Field Effect, 2026-11-09](https://fieldeffect.com/blog/n-central-offline-alleged-zero-days)).

**Detection:** in N-central's authentication and audit logs from 2026-11-08 onward, unexpected logins, new administrator accounts and changes to stored credentials or API integrations; on managed endpoints, unscheduled software deployments, scripts and remote-control sessions ([Huntress, 2026-11-09](https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains); [Field Effect, 2026-11-09](https://fieldeffect.com/blog/n-central-offline-alleged-zero-days)). For 4EverAble2Shell, Huntback names POST requests to the Axis endpoint /dms/services/ServerUI, a symlink at the N-central flag file path, a systemd unit or cron entry relaunching a miner and a hidden miner directory under /tmp or /var/tmp ([Huntback, 2026-11-12](https://huntback.io/blog/ncentral-4everable2shell-miners-on-live-servers)). Huntress's Agent2Shell indicators are static analysis only: SYSTEM PowerShell with an encoded command spawned by the Agent, where an Agent child PowerShell is common and the command is what matters ([Huntress, 2026-11-13](https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains)).

**Defender takeaway:** upgrade on-premises servers to Hotfix 3, then every Agent and Probe, those already on Hotfix 2 included ([N-able, 2026-11-16](https://status.n-able.com/2026/11/16/n-central-2026-4-hf3-release-notes/)), and confirm the Legacy API is disabled and not internet-reachable, because Hotfix 2 did not stop 4EverAble2Shell, 19 of the 21 compromised servers already ran it ([Huntback, 2026-11-12](https://huntback.io/blog/ncentral-4everable2shell-miners-on-live-servers)) and N-able does not say Hotfix 3 fixes it; treat a hit as a full compromise and rotate the administrator, service and integration credentials the platform holds where activity looks unauthorised ([Field Effect, 2026-11-09](https://fieldeffect.com/blog/n-central-offline-alleged-zero-days)). Ask each IT provider managing your endpoints through N-central whether it runs a server on premises and has upgraded it.

## Update — 2026-11-11T03:49:03Z

N-able released N-central 2026.4 Hotfix 2, build 2026.4.1.26, on 2026-11-10 as a critical security update; hosted servers are already upgraded, on-premises customers must upgrade their own servers, and every customer must upgrade Agents and Probes, Agents first as N-able recommends ([N-able, 2026-11-10](https://status.n-able.com/2026/11/10/n-central-2026-4-hf2-release-notes/)). Huntress lists seven CVE ids for the fixed flaws and relays N-able's status-page statement that it observed "scanning activity associated with the published proof-of-concept code" but no evidence that any customer environment was successfully exploited; Huntress has seen no exploitation in its partners' environments, and N-able's guidance is to keep on-premises servers offline until the upgrade is complete ([Huntress, 2026-11-10](https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains)). After the hotfix the built-in remote control is temporarily disabled and Take Control still works ([N-able, 2026-11-10](https://status.n-able.com/2026/11/10/n-central-2026-4-hf2-release-notes/)).

## Update — 2026-11-13T03:54:38Z

The researcher's second exploit set, 4EverAble2Shell, published on 2026-11-12, works against Hotfix 2 builds when the Legacy API is turned on and reachable, and no fix exists. It pairs CVE-2026-90436 in the Apache Axis 1.x SOAP engine ([Apache Axis project, 2026-11-06](https://openwall.com/lists/oss-security/2026/11/06/12)) with a separate root escalation ([Huntback, 2026-11-12](https://huntback.io/blog/ncentral-4everable2shell-miners-on-live-servers); [BleepingComputer, 2026-11-12](https://www.bleepingcomputer.com/news/security/new-n-able-4everable2shell-zero-day-exploited-hours-after-poc-released/)). Huntback counts at least 21 production servers, 19 of them on Hotfix 2, mining for one operator ([Huntback, 2026-11-12](https://huntback.io/blog/ncentral-4everable2shell-miners-on-live-servers)), Previdian's sensors recorded attempts at the chain ([Previdian, 2026-11-12](https://previdian.com/VULN-2026-0009)), and BleepingComputer relays both ([BleepingComputer, 2026-11-12](https://www.bleepingcomputer.com/news/security/new-n-able-4everable2shell-zero-day-exploited-hours-after-poc-released/)). N-able said on 2026-11-12 that it had seen no signs of compromise, had no fix for the new claims and planned a follow-up hotfix ([Tenable, 2026-11-12](https://www.tenable.com/blog/able2shell-frequently-asked-questions-for-reported-n-able-n-central-zero-day-vulnerabilities)); Huntress says a Hotfix 2 server with the Legacy API disabled is not exposed to this chain ([Huntress, 2026-11-12](https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains)).

## Update — 2026-11-14T04:00:03Z

The researcher's 2026-11-12 disclosure also includes Agent2Shell, which The Hacker News describes as more than ten zero-day flaws used to run commands as SYSTEM on managed Windows agents, assuming the attacker knows the target appliance ID ([The Hacker News, 2026-11-12](https://thehackernews.com/2026/11/new-n-central-exploits-work-against.html)). Huntress describes it as a set of more than ten issues in how the N-central server communicates with Windows Agents and Probes, two chains of which let an unauthenticated attacker who can reach the server run commands on managed Windows endpoints, including as SYSTEM ([Huntress, 2026-11-13](https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains)). Huntress relays that N-able confirmed Agent2Shell, like 4EverAble2Shell, requires the non-default Legacy API to be enabled, which settles the question Huntress and Tenable had left open on 2026-11-12, and that on 2026-11-13 at 13:40 UTC N-able said it had identified indicators of compromise for customers that have not disabled the Legacy API ([Huntress, 2026-11-13](https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains)); the statement that N-able had seen no signs of compromise dates from 2026-11-12 ([Tenable, 2026-11-12](https://www.tenable.com/blog/able2shell-frequently-asked-questions-for-reported-n-able-n-central-zero-day-vulnerabilities)). Huntress has not observed exploitation of these issues in its partners' environments, and its Agent2Shell indicators come from static analysis of the proof of concept, not from attacks seen ([Huntress, 2026-11-13](https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains)). Tenable adds that N-able has temporarily deactivated the Intune integration for on-premises customers running it ([Tenable, 2026-11-12](https://www.tenable.com/blog/able2shell-frequently-asked-questions-for-reported-n-able-n-central-zero-day-vulnerabilities)).

## Update — 2026-11-18T05:12:35Z

N-able released N-central 2026.4 Hotfix 3, build 2026.4.1.39, on 2026-11-16 as a critical security update that builds on and supersedes Hotfix 2; it fixes 17 further CVE ids, adds missing authentication and permission checks to server operations, hardens how Agents and Probes authenticate with the server, adds validation to file publishing, path and XML import handling, and permanently blocks the legacy APIs ([N-able, 2026-11-16](https://status.n-able.com/2026/11/16/n-central-2026-4-hf3-release-notes/)). Agents and Probes that are not upgraded are susceptible to impersonation, and all customers, hosted and on-premises, must upgrade every Agent and Probe to 2026.4.1 HF3 whether or not they already run Hotfix 2 ([N-able, 2026-11-16](https://status.n-able.com/2026/11/16/n-central-2026-4-hf3-release-notes/)).

The release notes name neither 4EverAble2Shell nor Agent2Shell nor the Apache Axis flaw and do not say they are fixed; what changes is the Legacy API, which N-able itself said both chains need and which is now blocked permanently ([N-able, 2026-11-16](https://status.n-able.com/2026/11/16/n-central-2026-4-hf3-release-notes/); [Huntress, 2026-11-17](https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains)). Among the 17 ids, the release notes title CVE-2026-129272 "MMS3 appliance authentication bypass via predictable passcode", CVE-2026-129280 "ServerUI SOAP operations missing authorisation checks" and CVE-2026-129286 "SIS GenericFiles version path traversal leads to RCE", and Huntress counts three critical, eight high and six medium scores, all assigned by N-able as CVE numbering authority ([N-able, 2026-11-16](https://status.n-able.com/2026/11/16/n-central-2026-4-hf3-release-notes/); [Huntress, 2026-11-17](https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains)).

Huntress reports that public proof-of-concept code for all 17 CVE ids appeared on the evening of 2026-11-16, shortly after the hotfix, says any unpatched server should be treated as exposed, and has not observed exploitation of them in its partners' environments ([Huntress, 2026-11-17](https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains)). Field Effect reports that technical details on 24 further N-central vulnerabilities were published and are reported to be addressed by Hotfix 3, a count that the 17 CVE ids in N-able's notes do not reconcile ([Field Effect, 2026-11-09](https://fieldeffect.com/blog/n-central-offline-alleged-zero-days)). Huntress advises confirming the Patch Management Engine is at 2.14.4.5829 or later, rotating secrets embedded in Automation Manager policies on a server that was exposed before patching, not relying on Take Control audit records from an unpatched server, and enforcing MFA on all N-central accounts ([Huntress, 2026-11-17](https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains)).
