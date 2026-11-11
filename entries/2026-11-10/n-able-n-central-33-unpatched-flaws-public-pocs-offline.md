---
schema: 1
kind: vulnerability
title: "N-able N-central: a researcher published proof-of-concept code for 33 alleged flaws, among them an unauthenticated XML external entity chain to remote code execution; N-able took hosted N-central offline and on 2026-11-10 shipped 2026.4 Hotfix 2 (build 2026.4.1.26) with seven CVE ids"
headline: "N-central Hotfix 2 (2026.4.1.26): upgrade servers, then Agents and Probes; scanning seen, no exploitation confirmed"
summary: >
  An independent researcher published write-ups and proof-of-concept code on 2026-11-08 and 2026-11-09 for what Huntress counts as 33 critical flaws in N-able's N-central remote monitoring and management appliance, tested on pre-release build 2026.4.0.31, which chain into four exploits, three to remote code execution and one to root; one chain starts with an unauthenticated XML external entity flaw. N-able took hosted N-central offline on 2026-11-09 and on 2026-11-10 released 2026.4 Hotfix 2, build 2026.4.1.26, which hosted servers already run; on-premises customers must upgrade their servers, and every customer must upgrade Agents and then Probes.
  N-able's status page reports scanning activity associated with the published proof-of-concept code but no evidence of a successful exploitation of any customer environment, and seven CVE ids have been assigned.
discovered_at: "2026-11-10T03:51:00Z"
updated_at: "2026-11-11T03:49:03Z"
event_date: "2026-11-09"
run_id: 2026-11-10T0255Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, supply-chain, rce, pre-auth, poc-public, patch-available]
regions: [global]
sectors: [technology]
entities: ["incident:n-able-n-central-able2shell-disclosure-2026-11"]
techniques: [T1190, T1059, T1068, T1136, T1552, T1070]
affected_products: ["N-able N-central"]
cves:
  - id: CVE-2026-125883
    cvss: "9.3"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [poc-public, patch-available]
    affected: "N-central before 2026.4 Hotfix 2 (CNA wording: before 26.4.1); multiple XML external entity flaws"
    fixed: "N-central 2026.4 Hotfix 2, build 2026.4.1.26"
  - id: CVE-2026-125881
    cvss: "9.3"
    epss: null
    type: ssrf
    vector: zero-click
    auth: pre-auth
    status: [poc-public, patch-available]
    affected: "N-central before 2026.4 Hotfix 2 (CNA wording: before 26.4.1); schema-hint SSRF through service-import schema validation"
    fixed: "N-central 2026.4 Hotfix 2, build 2026.4.1.26"
  - id: CVE-2026-125878
    cvss: "8.7"
    epss: null
    type: rce
    vector: zero-click
    auth: post-auth
    status: [poc-public, patch-available]
    affected: "N-central before 2026.4 Hotfix 2 (CNA wording: before 26.4.1); multiple OGNL injection flaws per Huntress"
    fixed: "N-central 2026.4 Hotfix 2, build 2026.4.1.26"
  - id: CVE-2026-125882
    cvss: "8.6"
    epss: null
    type: path-traversal
    vector: zero-click
    auth: post-auth
    status: [poc-public, patch-available]
    affected: "N-central before 2026.4 Hotfix 2 (CNA wording: before 26.4.1); remote code execution through a file-repository upload path traversal per Huntress"
    fixed: "N-central 2026.4 Hotfix 2, build 2026.4.1.26"
  - id: CVE-2026-125879
    cvss: "8.6"
    epss: null
    type: priv-esc
    vector: local
    auth: post-auth
    status: [poc-public, patch-available]
    affected: "N-central before 2026.4 Hotfix 2 (CNA wording: before 26.4.1); local privilege escalation to root through a writable syslog-ng configuration per Huntress"
    fixed: "N-central 2026.4 Hotfix 2, build 2026.4.1.26"
  - id: CVE-2026-91000
    cvss: "8.4"
    epss: null
    type: priv-esc
    vector: local
    auth: post-auth
    status: [poc-public, patch-available]
    affected: "N-central before 2026.4 Hotfix 2 (CNA wording: before 2026.4.1); insecure inter-process channels lead to local privilege escalation per Huntress"
    fixed: "N-central 2026.4 Hotfix 2, build 2026.4.1.26"
  - id: CVE-2026-125880
    cvss: "8.3"
    epss: null
    type: xss
    vector: user-interaction
    auth: admin-required
    status: [poc-public, patch-available]
    affected: "N-central before 2026.4 Hotfix 2 (CNA wording: before 26.4.1); stored XSS through patch metadata in an administrator context per Huntress"
    fixed: "N-central 2026.4 Hotfix 2, build 2026.4.1.26"
sources:
  - url: "https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains"
    publisher: "Huntress"
    date: "2026-11-09"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/n-able-takes-cloud-platform-offline-after-30-plus-zero-days-published/"
    publisher: "BleepingComputer"
    date: "2026-11-09"
    role: corroborating
  - url: "https://fieldeffect.com/blog/n-central-offline-alleged-zero-days"
    publisher: "Field Effect"
    date: "2026-11-09"
    role: corroborating
  - url: "https://censys.com/advisory/n-able-n-central/"
    publisher: "Censys"
    date: "2026-11-09"
    role: corroborating
  - url: "https://status.n-able.com/2026/11/10/n-central-2026-4-hf2-release-notes/"
    publisher: "N-able (N-central 2026.4 HF2 release notes)"
    date: "2026-11-10"
    role: primary
  - url: "https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-122942"
    publisher: "N-able CNA record CVE-2026-125883, via ENISA EUVD"
    date: "2026-11-10"
    role: corroborating
  - url: "https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-122961"
    publisher: "N-able CNA record CVE-2026-125881, via ENISA EUVD"
    date: "2026-11-10"
    role: corroborating
  - url: "https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains"
    publisher: "Huntress (update of 2026-11-10)"
    date: "2026-11-10"
    role: corroborating
closed_sources: []
evidence:
  - quote: "N-able said it has not seen active exploitation of the vulnerabilities as of November 9 at 15:15:00 UTC."
    publisher: "Huntress"
    source_url: "https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains"
  - quote: "One of the most critical exploit chains abuses an unauthenticated XXE vulnerability in N-central's service-import functionality to steal a trusted local session, reset an account password, and execute commands on the server as the nable user."
    publisher: "BleepingComputer"
    source_url: "https://www.bleepingcomputer.com/news/security/n-able-takes-cloud-platform-offline-after-30-plus-zero-days-published/"
  - quote: "Several of the published PoCs describe unauthenticated attack paths, so if they work as described, network reachability is a prerequisite for exploitation."
    publisher: "Field Effect"
    source_url: "https://fieldeffect.com/blog/n-central-offline-alleged-zero-days"
  - quote: "As of November 9, 2026, N-able has published no mechanism detail, affected versions, or fixed versions."
    publisher: "Censys"
    source_url: "https://censys.com/advisory/n-able-n-central/"
  - quote: "N-central 2026.4 Hotfix 2 is a critical security update."
    publisher: "N-able"
    source_url: "https://status.n-able.com/2026/11/10/n-central-2026-4-hf2-release-notes/"
  - quote: "All customers, both hosted and on-premises, must upgrade their Agents and Probes."
    publisher: "N-able"
    source_url: "https://status.n-able.com/2026/11/10/n-central-2026-4-hf2-release-notes/"
  - quote: "scanning activity associated with the published proof-of-concept code"
    publisher: "Huntress"
    source_url: "https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains"
verification: multi-source
sourcing_note: >
  N-able's release notes for Hotfix 2 carry the build, the scope and the upgrade order; the CVE descriptions are those Huntress lists, with scores and affected-version wording from N-able's CNA records in ENISA's vulnerability database (the records say before 26.4.1 or 2026.4.1, and the build is 2026.4.1.26). Seven records do not map one to one onto the researcher's 33 flaws, and the CNA records carry CVSS 4.0 vectors, which give the scores here: they require no privileges for CVE-2026-125883 and CVE-2026-125881, low privileges for CVE-2026-125878 and CVE-2026-91000 and high privileges for CVE-2026-125879, CVE-2026-125880 and CVE-2026-125882, and for some records they describe the flaw differently from Huntress, so the flaw types and vectors listed follow Huntress. The status page where N-able reports the scanning activity is a script-rendered page that could not be read, so that statement comes from Huntress. The count of 33 flaws, the tested build and every technical claim about them are the researcher's, and no source has validated them individually. BleepingComputer dates the repository to the evening of 8 November, while Censys dates the disclosure to 8 November and the proof-of-concept release to 9 November. The researcher's repository holds proof-of-concept exploit code and is deliberately not linked.
confidence: medium
references:
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
  - "Upgrade every on-premises N-central server to 2026.4 Hotfix 2 (build 2026.4.1.26), keeping it offline until the upgrade is complete as N-able advises, then upgrade every Agent and, after the Agents, every Probe, hosted or not; ask each IT provider that manages your endpoints through N-central whether it runs a server on premises and has done this, because the researcher's proof-of-concept code is public and N-able has seen scanning for it."
updates:
  - at: "2026-11-11T03:49:03Z"
    run_id: 2026-11-11T0256Z-intel
    type: update
    summary: >
      N-able released N-central 2026.4 Hotfix 2 (build 2026.4.1.26) on 2026-11-10 with seven CVE ids,
      which replaces the entry's statements that no fix, no CVE ids and no affected or fixed builds
      existed, and reports scanning activity associated with the public proof-of-concept code but no
      evidence of successful exploitation; on-premises servers must be upgraded and every Agent and Probe
      upgraded too.
    fields: [title, headline, summary, tags, cves, sources, evidence, sourcing_note, actions, body]
migrated_from: null
---

An independent researcher published what Huntress counts as 33 critical flaws in the N-central appliance, which chain into four exploits, three leading to remote code execution and one to privilege escalation to root, tested on pre-release build 2026.4.0.31 ([Huntress, 2026-11-09](https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains); [BleepingComputer, 2026-11-09](https://www.bleepingcomputer.com/news/security/n-able-takes-cloud-platform-offline-after-30-plus-zero-days-published/)). One chain BleepingComputer calls most critical abuses an unauthenticated XML external entity flaw in the service-import function to steal a trusted local session, reset an account password and run commands as the service user ([BleepingComputer, 2026-11-09](https://www.bleepingcomputer.com/news/security/n-able-takes-cloud-platform-offline-after-30-plus-zero-days-published/)); Field Effect reads the material as a mix of authenticated and unauthenticated flaws, with Python proof-of-concept code ([Field Effect, 2026-11-09](https://fieldeffect.com/blog/n-central-offline-alleged-zero-days)). N-able took its hosted environments offline on 2026-11-09 ([Huntress, 2026-11-09](https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains)).

On 2026-11-10 N-able released N-central 2026.4 Hotfix 2, build 2026.4.1.26, "a critical security update" that supersedes 2026.4 and Hotfix 1: it strengthens authentication and permission checks, removes legacy mobile device management, adds validation to file and log handling and hardens the server, the Agent and Probe communication and the web and sign-in protections ([N-able, 2026-11-10](https://status.n-able.com/2026/11/10/n-central-2026-4-hf2-release-notes/)). Hosted servers are upgraded by N-able; on-premises customers must upgrade their own servers, and all customers must upgrade Agents and Probes, Agents first, because a Probe on 2026.4.1.26 or later cannot communicate with an Agent or Patch Management Engine below that level until both are upgraded, which disables features such as the offline patch cache; built-in remote control is temporarily disabled while Take Control works ([N-able, 2026-11-10](https://status.n-able.com/2026/11/10/n-central-2026-4-hf2-release-notes/)). Huntress lists seven CVE ids assigned to the fixed flaws, among them CVE-2026-125883 for multiple XML external entity flaws, CVE-2026-125881 for a server-side request forgery through service-import schema validation, CVE-2026-125878 for multiple OGNL injection flaws and CVE-2026-125882 for remote code execution through a file-repository upload path traversal ([Huntress, 2026-11-10](https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains); [N-able CNA record, 2026-11-10](https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-122942); [N-able CNA record, 2026-11-10](https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-122961)).

N-able said it had seen no active exploitation as of 2026-11-09 15:15 UTC ([Huntress, 2026-11-09](https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains)); its status page now reports "scanning activity associated with the published proof-of-concept code" but no evidence that a customer environment was successfully exploited, and Huntress has seen none in its partners' environments ([Huntress, 2026-11-10](https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains)). Censys counts 1,728 N-central web consoles on the internet ([Censys, 2026-11-09](https://censys.com/advisory/n-able-n-central/)).

**Exposure:** an N-central server below build 2026.4.1.26, yours or an IT provider's, whose web interface is reachable beyond a dedicated administration network; Field Effect says several published proofs of concept describe unauthenticated attack paths, and a compromised server can reach large numbers of the systems N-central manages ([Field Effect, 2026-11-09](https://fieldeffect.com/blog/n-central-offline-alleged-zero-days)).

**Detection:** in N-central's authentication and audit logs from 2026-11-08 onward, unexpected logins, new administrator accounts, privilege and configuration changes and changes to stored credentials or API integrations ([Huntress, 2026-11-09](https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains); [Field Effect, 2026-11-09](https://fieldeffect.com/blog/n-central-offline-alleged-zero-days)); on managed endpoints, software deployments, scripts, remote-control sessions and automation-policy changes the provider did not schedule, as when attackers sprayed downstream environments with unauthorised scripts during the earlier CVE-2026-86218 exploitation ([Field Effect, 2026-11-09](https://fieldeffect.com/blog/n-central-offline-alleged-zero-days); [Huntress, 2026-11-09](https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains)).

**Defender takeaway:** upgrade on-premises servers to Hotfix 2 before they go back online, then Agents and Probes in that order ([N-able, 2026-11-10](https://status.n-able.com/2026/11/10/n-central-2026-4-hf2-release-notes/); [Huntress, 2026-11-10](https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains)); ask each IT provider that manages your endpoints through N-central whether it runs a server on premises and has upgraded it; and where activity looks unauthorised, rotate the administrator, service and integration credentials the platform holds ([Field Effect, 2026-11-09](https://fieldeffect.com/blog/n-central-offline-alleged-zero-days)).

## Update — 2026-11-11T03:49:03Z

N-able released N-central 2026.4 Hotfix 2, build 2026.4.1.26, on 2026-11-10 as a critical security update; hosted servers are already upgraded, on-premises customers must upgrade their own servers, and every customer must upgrade Agents first and then Probes ([N-able, 2026-11-10](https://status.n-able.com/2026/11/10/n-central-2026-4-hf2-release-notes/)). Huntress lists seven CVE ids for the fixed flaws and relays N-able's status-page statement that it observed "scanning activity associated with the published proof-of-concept code" but no evidence that any customer environment was successfully exploited; Huntress has seen no exploitation in its partners' environments, and N-able's guidance is to keep on-premises servers offline until the upgrade is complete ([Huntress, 2026-11-10](https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains)). After the hotfix the built-in remote control is temporarily disabled and Take Control still works ([N-able, 2026-11-10](https://status.n-able.com/2026/11/10/n-central-2026-4-hf2-release-notes/)).
