---
schema: 1
kind: vulnerability
title: 'N-able N-central: a researcher published exploits for 33 alleged flaws and N-able shipped 2026.4 Hotfix 2 (build 2026.4.1.26) with seven CVE ids, but a second disclosure adds 4EverAble2Shell, a chain through Apache Axis (CVE-2026-90436) and a root escalation that works against Hotfix 2 when the Legacy API is on and is exploited on at least 21 production servers, and Agent2Shell, SYSTEM commands on managed Windows agents, with no fix yet for either'
headline: 'N-central: 4EverAble2Shell exploited on 21+ servers, Agent2Shell adds SYSTEM on agents; disable Legacy API'
summary: 'An independent researcher published proof-of-concept code on 2026-11-08 and 2026-11-09 for what Huntress counts as 33 critical flaws in N-able''s N-central remote monitoring and management appliance, and N-able released 2026.4 Hotfix 2 (build 2026.4.1.26) on 2026-11-10 with seven CVE ids; on-premises customers must upgrade their servers, then Agents and Probes. On 2026-11-12 the researcher published a second chain, 4EverAble2Shell, that pairs an Apache Axis 1.x flaw (CVE-2026-90436) with a separate root escalation and works against Hotfix 2 when the Legacy API is turned on and reachable: Huntback reports at least 21 production servers, 19 of them on Hotfix 2, running a cryptominer, Previdian''s honeypot recorded attempts at the chain, and Huntress''s latest guidance is that a Hotfix 2 server with the Legacy API disabled is not exposed to it. The same disclosure includes Agent2Shell, whose chains give an unauthenticated attacker who can reach the server SYSTEM commands on managed Windows endpoints and which N-able confirms also needs the Legacy API; N-able has published indicators of compromise for customers that have not disabled it, has no fix for the new claims and plans a follow-up hotfix; the Legacy API is off by default and keeping it disabled is the stated protection.'
discovered_at: '2026-11-10T03:51:00Z'
updated_at: "2026-11-14T04:00:03Z"
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
  - no-patch
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
    auth: post-auth
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
    auth: post-auth
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
      - no-patch
    affected: Apache Axis 1.x through 1.4 as embedded in on-premises N-central with the Legacy API turned on and reachable, builds through 2026.4.1.26 (Hotfix 2)
    fixed: 'none released: the Apache Axis project offers a source patch but does not expect to release an Axis 1.x fix (The Hacker News quotes Previdian saying patches were released on 2026-11-06); N-able has no fix for this chain and plans a follow-up hotfix'
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
verification: multi-source
sourcing_note: 'N-able''s release notes for Hotfix 2 carry the build, the scope and the upgrade order; the CVE descriptions are those Huntress lists, with scores and affected-version wording from N-able''s CNA records in ENISA''s vulnerability database (the records say before 26.4.1 or 2026.4.1, and the build is 2026.4.1.26). Seven records do not map one to one onto the researcher''s 33 flaws, and the CNA records carry CVSS 4.0 vectors, which give the scores here: they require no privileges for CVE-2026-125883 and CVE-2026-125881, low privileges for CVE-2026-125878 and CVE-2026-91000 and high privileges for CVE-2026-125879, CVE-2026-125880 and CVE-2026-125882, and for some records they describe the flaw differently from Huntress, so the flaw types and vectors listed follow Huntress. The status page where N-able reports the scanning activity is a script-rendered page that could not be read, so that statement comes from Huntress. The count of 33 flaws, the tested build and every technical claim about them are the researcher''s, and no source has validated them individually. BleepingComputer dates the repository to the evening of 8 November, while Censys dates the disclosure to 8 November and the proof-of-concept release to 9 November. The researcher''s repository holds proof-of-concept exploit code and is deliberately not linked. The exploitation of the second chain rests on Huntback''s count from a mining pool''s public rig list and on Previdian''s honeypot, reported by BleepingComputer and Tenable; N-able said on 2026-11-12, as Tenable and BleepingComputer report, that it had seen no signs of compromise, and on 2026-11-13, as Huntress relays, that it has identified indicators of compromise for customers that have not disabled the Legacy API; N-able''s own status pages could not be read, so every N-able statement after 2026-11-10 is as relayed, and no victim has confirmed. Huntress''s Agent2Shell indicators come from static analysis of the proof of concept and none was observed in an attack. Previdian''s page shows no CVE assigned yet for the chain.'
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
  - Confirm on every on-premises N-central server, yours or your IT provider's, that the Legacy API is disabled and not reachable from the internet, and keep Hotfix 2 (build 2026.4.1.26) and the Agent and Probe upgrades in place; on any server that had the Legacy API on, check the web logs for POST requests to the Axis endpoint /dms/services/ServerUI carrying a SOAP fault and the host for a symlink at the N-central flag file path, and treat a hit as a full compromise, because Hotfix 2 does not fix the chain and 19 of the 21 compromised servers Huntback found already ran it.
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
migrated_from: null
---
An independent researcher published what Huntress counts as 33 critical flaws in the N-central appliance, chaining into four exploits, and N-able took its hosted environments offline on 2026-11-09 ([Huntress, 2026-11-09](https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains)); the chain BleepingComputer calls most critical abuses an unauthenticated XML external entity flaw to steal a trusted local session and run commands as the service user ([BleepingComputer, 2026-11-09](https://www.bleepingcomputer.com/news/security/n-able-takes-cloud-platform-offline-after-30-plus-zero-days-published/)).

On 2026-11-10 N-able released N-central 2026.4 Hotfix 2, build 2026.4.1.26, "a critical security update", for which Huntress lists seven CVE ids ([N-able, 2026-11-10](https://status.n-able.com/2026/11/10/n-central-2026-4-hf2-release-notes/); [Huntress, 2026-11-10](https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains); [N-able CNA record, 2026-11-10](https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-122942); [N-able CNA record, 2026-11-10](https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-122961)). N-able reported scanning for that set but no successful exploitation ([Huntress, 2026-11-10](https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains)), and none of the seven is in CISA's catalog ([Tenable, 2026-11-12](https://www.tenable.com/blog/able2shell-frequently-asked-questions-for-reported-n-able-n-central-zero-day-vulnerabilities)).

On 2026-11-12 the researcher published a second set. 4EverAble2Shell is unauthenticated command execution as root that requires the Legacy API to be enabled, per BleepingComputer; it chains CVE-2026-90436, an Apache Axis 1.x deserialization flaw for which Apache does not expect a fix, with a root escalation in N-central's maintenance helper ([BleepingComputer, 2026-11-12](https://www.bleepingcomputer.com/news/security/new-n-able-4everable2shell-zero-day-exploited-hours-after-poc-released/); [Apache Axis project, 2026-11-06](https://openwall.com/lists/oss-security/2026/11/06/12); [Huntback, 2026-11-12](https://huntback.io/blog/ncentral-4everable2shell-miners-on-live-servers)). Huntback counts at least 21 servers, 19 of them on Hotfix 2, in North America, South Africa and Europe but not Switzerland, and Previdian's honeypot recorded attempts at the chain ([Huntback, 2026-11-12](https://huntback.io/blog/ncentral-4everable2shell-miners-on-live-servers); [Previdian, 2026-11-12](https://previdian.com/VULN-2026-0009)). Agent2Shell is a set of more than ten issues in how the server talks to Windows Agents and Probes, two chains of which let an unauthenticated attacker who can reach the server run commands as SYSTEM on managed endpoints; N-able confirmed it also requires the non-default Legacy API ([The Hacker News, 2026-11-12](https://thehackernews.com/2026/11/new-n-central-exploits-work-against.html); [Huntress, 2026-11-13](https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains)). N-able has published indicators of compromise for customers that have not disabled the Legacy API, has no fix for the new claims and plans a follow-up hotfix ([Huntress, 2026-11-13](https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains); [Tenable, 2026-11-12](https://www.tenable.com/blog/able2shell-frequently-asked-questions-for-reported-n-able-n-central-zero-day-vulnerabilities)).

**Exposure:** an on-premises N-central server, yours or an IT provider's: below build 2026.4.1.26 for the first set, and any build up to Hotfix 2 for the second when the Legacy API, off by default, is on and reachable ([Huntress, 2026-11-13](https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains)). A compromised server reaches the systems N-central manages ([Field Effect, 2026-11-09](https://fieldeffect.com/blog/n-central-offline-alleged-zero-days)).

**Detection:** in N-central's authentication and audit logs from 2026-11-08 onward, unexpected logins, new administrator accounts and changes to stored credentials or API integrations; on managed endpoints, unscheduled software deployments, scripts and remote-control sessions ([Huntress, 2026-11-09](https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains); [Field Effect, 2026-11-09](https://fieldeffect.com/blog/n-central-offline-alleged-zero-days)). For 4EverAble2Shell, Huntback names POST requests to the Axis endpoint /dms/services/ServerUI, a symlink at the N-central flag file path, a systemd unit or cron entry relaunching a miner and a hidden miner directory under /tmp or /var/tmp ([Huntback, 2026-11-12](https://huntback.io/blog/ncentral-4everable2shell-miners-on-live-servers)). Huntress's Agent2Shell indicators come from static analysis of the proof of concept, not attacks seen: SYSTEM PowerShell with an encoded command spawned by the Agent, where PowerShell as an Agent child is common and the command is what matters ([Huntress, 2026-11-13](https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains)).

**Defender takeaway:** upgrade on-premises servers to Hotfix 2, then Agents and Probes, and confirm the Legacy API is disabled and not internet-reachable, because Hotfix 2 does not fix 4EverAble2Shell and 19 of the 21 compromised servers already ran it ([Huntback, 2026-11-12](https://huntback.io/blog/ncentral-4everable2shell-miners-on-live-servers)); treat a hit as a full compromise, ask each IT provider managing your endpoints through N-central whether it runs a server on premises and has upgraded it, and rotate the administrator, service and integration credentials the platform holds where activity looks unauthorised ([Field Effect, 2026-11-09](https://fieldeffect.com/blog/n-central-offline-alleged-zero-days)).

## Update — 2026-11-11T03:49:03Z

N-able released N-central 2026.4 Hotfix 2, build 2026.4.1.26, on 2026-11-10 as a critical security update; hosted servers are already upgraded, on-premises customers must upgrade their own servers, and every customer must upgrade Agents first and then Probes ([N-able, 2026-11-10](https://status.n-able.com/2026/11/10/n-central-2026-4-hf2-release-notes/)). Huntress lists seven CVE ids for the fixed flaws and relays N-able's status-page statement that it observed "scanning activity associated with the published proof-of-concept code" but no evidence that any customer environment was successfully exploited; Huntress has seen no exploitation in its partners' environments, and N-able's guidance is to keep on-premises servers offline until the upgrade is complete ([Huntress, 2026-11-10](https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains)). After the hotfix the built-in remote control is temporarily disabled and Take Control still works ([N-able, 2026-11-10](https://status.n-able.com/2026/11/10/n-central-2026-4-hf2-release-notes/)).

## Update — 2026-11-13T03:54:38Z

The researcher's second exploit set, 4EverAble2Shell, published on 2026-11-12, works against Hotfix 2 builds when the Legacy API is turned on and reachable, and no fix exists. It pairs CVE-2026-90436 in the Apache Axis 1.x SOAP engine ([Apache Axis project, 2026-11-06](https://openwall.com/lists/oss-security/2026/11/06/12)) with a separate root escalation ([Huntback, 2026-11-12](https://huntback.io/blog/ncentral-4everable2shell-miners-on-live-servers); [BleepingComputer, 2026-11-12](https://www.bleepingcomputer.com/news/security/new-n-able-4everable2shell-zero-day-exploited-hours-after-poc-released/)). Huntback counts at least 21 production servers, 19 of them on Hotfix 2, mining for one operator ([Huntback, 2026-11-12](https://huntback.io/blog/ncentral-4everable2shell-miners-on-live-servers)), Previdian's honeypot recorded attempts at the chain ([Previdian, 2026-11-12](https://previdian.com/VULN-2026-0009)), and BleepingComputer relays both ([BleepingComputer, 2026-11-12](https://www.bleepingcomputer.com/news/security/new-n-able-4everable2shell-zero-day-exploited-hours-after-poc-released/)). N-able said on 2026-11-12 that it had seen no signs of compromise, had no fix for the new claims and planned a follow-up hotfix ([Tenable, 2026-11-12](https://www.tenable.com/blog/able2shell-frequently-asked-questions-for-reported-n-able-n-central-zero-day-vulnerabilities)); Huntress says a Hotfix 2 server with the Legacy API disabled is not exposed to this chain ([Huntress, 2026-11-12](https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains)).

## Update — 2026-11-14T04:00:03Z

The researcher's 2026-11-12 disclosure also includes Agent2Shell, which The Hacker News describes as more than ten zero-day flaws used to run commands as SYSTEM on managed Windows agents, assuming the attacker knows the target appliance ID ([The Hacker News, 2026-11-12](https://thehackernews.com/2026/11/new-n-central-exploits-work-against.html)). Huntress describes it as a set of more than ten issues in how the N-central server communicates with Windows Agents and Probes, two chains of which let an unauthenticated attacker who can reach the server run commands on managed Windows endpoints, including as SYSTEM ([Huntress, 2026-11-13](https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains)). Huntress relays that N-able confirmed Agent2Shell, like 4EverAble2Shell, requires the non-default Legacy API to be enabled, which settles the question Huntress and Tenable had left open on 2026-11-12, and that on 2026-11-13 at 13:40 UTC N-able said it had identified indicators of compromise for customers that have not disabled the Legacy API ([Huntress, 2026-11-13](https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains)); the statement that N-able had seen no signs of compromise dates from 2026-11-12 ([Tenable, 2026-11-12](https://www.tenable.com/blog/able2shell-frequently-asked-questions-for-reported-n-able-n-central-zero-day-vulnerabilities)). Huntress has not observed exploitation of these issues in its partners' environments, and its Agent2Shell indicators come from static analysis of the proof of concept, not from attacks seen ([Huntress, 2026-11-13](https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains)). Tenable adds that N-able has temporarily deactivated the Intune integration for on-premises customers running it ([Tenable, 2026-11-12](https://www.tenable.com/blog/able2shell-frequently-asked-questions-for-reported-n-able-n-central-zero-day-vulnerabilities)).
