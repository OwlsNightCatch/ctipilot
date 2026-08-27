---
schema: 1
kind: vulnerability
horizon: strategic
title: >
  2026-W34 vulnerability status roll-up — seven flaws crossed into reported exploitation this
  week; six were catalogue listings against fixes that had existed for weeks or months, and the
  seventh went from out-of-band patch to exploitation in two days with no catalogue involved at
  all
headline: >
  Nothing crossed into exploitation this week that was not already fixed — the catalogue is
  trailing the patch, not leading it
summary: >
  Consolidated status of the vulnerabilities this pipeline covered operationally in ISO week
  2026-W34, each set against when it was first covered. Six were catalogued or recorded as
  exploited by an authority: CVE-2025-62593 (Ray), CVE-2026-33824 (Windows IKE Extension),
  CVE-2026-55040 (SharePoint Server), CVE-2026-64849 (MLflow), CVE-2026-73570 (Zimbra
  Collaboration) and the chained pair CVE-2026-72529 / CVE-2026-72530 (TrueConf Server) — and
  every one of the six had a fix available before the determination arrived, four months ahead for
  the Windows IKE flaw, two for TrueConf, four weeks for Zimbra, so a listing is functioning as
  lagging confirmation rather than early warning. The seventh is the one that behaved differently:
  GitLab's CVE-2026-19478, patched out of band on 17 August, was reported under exploitation about
  two days after disclosure and Switzerland's NCSC changed its own advisory to actively exploited
  on 21 August, with no catalogue listing anywhere in the sequence. Continuing exploitation: PTC
  Windchill via CVE-2026-12569, Metabase via CVE-2026-72898, and the GeoServer jsonArrayContains
  SQL injection, which gained a fix on 14 August and still has no CVE. The critical tail with no
  established exploitation is led by Keycloak's CVE-2026-18963 at CVSS 9.1, eight critical Cisco
  Crosswork and Secure Workload flaws of which five are CVSS 10.0 and which no earlier fire
  covered, Citrix NetScaler's CVE-2026-19490 at 9.3 — whose exploitation status the Swiss
  authority and CERT-EU now disagree about — and three unauthenticated CVSS 10.0 flaws in Oracle's
  August release. One correction to this pipeline's own earlier coverage: every Red Hat product
  listed against the Keycloak flaw is either Fixed or Not affected — the operational entry of 19
  August recorded one product as affected with no erratum, and the vendor's record does not
  support that.
discovered_at: "2026-08-23T23:55:00Z"
updated_at: "2026-08-24T09:15:00Z"
event_date: 2026-08-20
run_id: 2026-08-23T2311Z-weekly
priority: high
immediate_action: null
tags:
  - vulnerabilities
  - actively-exploited
  - cisa-kev
  - enisa-critical
  - pre-auth
  - rce
  - auth-bypass
  - no-patch
  - patch-available
  - sqli
  - info-disclosure
  - path-traversal
regions:
  - global
  - europe
  - switzerland
sectors:
  - public-sector
  - technology
  - healthcare
  - finance
  - manufacturing
  - energy
  - telco
entities:
  - "actor:clop"
  - "campaign:clop-windchill-flexplm-extortion-2026"
  - "incident:metabase-sqli-zeroday-2026-08"
  - "actor:head-mare"
techniques:
  - T1190
  - T1552
  - T1078
affected_products:
  - Ray
  - Cisco Crosswork Network Controller
  - Cisco Secure Workload
  - Microsoft Windows
  - Microsoft SharePoint Server
  - MLflow
  - Zimbra Collaboration
  - TrueConf Server
  - PTC Windchill
  - Metabase
  - GeoServer
  - Keycloak
  - GitLab
  - Citrix NetScaler ADC
  - Citrix NetScaler Gateway
  - Oracle Internet Directory
  - Forminator Forms
  - User Profile Builder
  - misp-stix
  - Cisco Crosswork Data Gateway
  - Cisco Crosswork Planning
  - Cisco Crosswork Workflow Manager
cves:
  - id: CVE-2026-20030
    cvss: "10.0"
    epss: null
    type: sqli
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
    affected: Cisco Crosswork 7.2.1 and earlier / 2.1.1 and earlier
    fixed: 7.2.1-SP / 2.1.1-SP
  - id: CVE-2026-20357
    cvss: "10.0"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
    affected: Cisco Crosswork 7.2.1 and earlier / 2.1.1 and earlier
    fixed: 7.2.1-SP / 2.1.1-SP
  - id: CVE-2026-20358
    cvss: "10.0"
    epss: null
    type: path-traversal
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
    affected: Cisco Crosswork 7.2.1 and earlier / 2.1.1 and earlier
    fixed: 7.2.1-SP / 2.1.1-SP
  - id: CVE-2026-20359
    cvss: "9.9"
    epss: null
    type: info-disclosure
    vector: zero-click
    auth: post-auth
    status:
      - patch-available
    affected: Cisco Crosswork 7.2.1 and earlier / 2.1.1 and earlier
    fixed: 7.2.1-SP / 2.1.1-SP
  - id: CVE-2026-20315
    cvss: "10.0"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
    affected: "Cisco Secure Workload 3.10 and earlier; 4.0"
    fixed: "3.10.9.1; 4.0.4.16"
  - id: CVE-2026-20317
    cvss: "10.0"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
    affected: "Cisco Secure Workload 3.10 and earlier; 4.0"
    fixed: "3.10.9.1; 4.0.4.16"
  - id: CVE-2026-20318
    cvss: "9.6"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: post-auth
    status:
      - patch-available
    affected: "Cisco Secure Workload 3.10 and earlier; 4.0"
    fixed: "3.10.9.1; 4.0.4.16"
  - id: CVE-2026-20231
    cvss: "9.9"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: post-auth
    status:
      - patch-available
    affected: "Cisco Secure Workload 3.10 and earlier; 4.0"
    fixed: "3.10.9.1; 4.0.4.16"
  - id: CVE-2026-20319
    cvss: "7.5"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
    affected: "Cisco Secure Workload 3.10 and earlier; 4.0"
    fixed: "3.10.9.1; 4.0.4.16"
sources:
  - url: "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    publisher: CISA Known Exploited Vulnerabilities catalog (version 2026.08.21)
    date: 2026-08-21
    role: primary
  - url: "https://euvd.enisa.europa.eu/vulnerability/CVE-2026-73570"
    publisher: ENISA EU Vulnerability Database
    date: 2026-08-13
    role: primary
  - url: "https://access.redhat.com/security/cve/CVE-2026-18963"
    publisher: Red Hat Product Security
    date: 2026-08-18
    role: primary
  - url: "https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-2-4-released/"
    publisher: GitLab
    date: 2026-08-17
    role: primary
  - url: "https://cert.europa.eu/publications/security-advisories/2026-010/"
    publisher: CERT-EU
    date: 2026-08-19
    role: primary
  - url: "https://www.oracle.com/security-alerts/cspuaug2026.html"
    publisher: Oracle
    date: 2026-08-18
    role: primary
  - url: "https://geoserver.org/announcements/vulnerability/2026/08/14/geoserver-3-0-1-released.html"
    publisher: GeoServer project
    date: 2026-08-14
    role: primary
  - url: "https://security-hub.ncsc.admin.ch/#/posts/12844"
    publisher: NCSC Switzerland (BACS) — Cyber Security Hub
    date: 2026-08-17
    role: corroborating
  - url: "https://security-hub.ncsc.admin.ch/#/posts/12856"
    publisher: NCSC Switzerland (BACS) — Cyber Security Hub
    date: 2026-08-21
    role: primary
  - url: "https://www.securityweek.com/critical-gitlab-flaw-exploited-shortly-after-disclosure/"
    publisher: SecurityWeek
    date: 2026-08-20
    role: corroborating
  - url: "https://security-hub.ncsc.admin.ch/#/posts/12863"
    publisher: NCSC Switzerland (BACS) — Cyber Security Hub
    date: 2026-08-21
    role: primary
  - url: "https://security-hub.ncsc.admin.ch/#/posts/12867"
    publisher: NCSC Switzerland (BACS) — Cyber Security Hub
    date: 2026-08-21
    role: primary
  - url: "https://ics-cert.kaspersky.com/publications/reports/2026/08/12/head-mare-exploits-vulnerabilities-in-trueconf-server-to-deliver-phantomcore-malware/"
    publisher: Kaspersky ICS CERT
    date: 2026-08-12
    role: corroborating
  - url: "https://security-hub.ncsc.admin.ch/#/posts/12860"
    publisher: NCSC Switzerland (BACS) — Cyber Security Hub
    date: 2026-08-18
    role: corroborating
  - url: "https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69414"
    publisher: Microsoft Security Response Center
    date: 2026-08-14
    role: primary
  - url: "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-crosswork-UzDTU9Vh"
    publisher: Cisco PSIRT
    date: 2026-08-19
    role: primary
  - url: "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-csw1-shSvndWP"
    publisher: Cisco PSIRT
    date: 2026-08-19
    role: primary
  - url: "https://advisories.ncsc.nl/advisory?id=NCSC-2026-0323"
    publisher: NCSC-NL
    date: 2026-08-21
    role: corroborating
closed_sources: []
evidence:
  - quote: Cisco has grouped these issues by their underlying vulnerability class - Common Weakness Enumeration (CWE) - and assigned a single Common Vulnerabilities and Exposures Identifier (CVE ID) to each CWE grouping.
    publisher: Cisco PSIRT
  - quote: The CVSS score that is assigned to each CVE ID represents the maximum potential severity of the single most impactful underlying vulnerability within that specific CWE category.
    publisher: Cisco PSIRT
  - quote: There are no workarounds that address these vulnerabilities.
    publisher: Cisco PSIRT
  - quote: The Cisco PSIRT is not aware of any public announcements or malicious use of the vulnerabilities that are described in this advisory.
    publisher: Cisco PSIRT
  - quote: "The Cluster, Agent, and Connector software of Cisco Secure Workload need to be upgraded to resolve all of these vulnerabilities. For SaaS deployments, Cisco has upgraded the Cluster software, and customers need to upgrade only the Agent and Connector software."
    publisher: Cisco PSIRT
verification: multi-source
sourcing_note: >
  This roll-up carries only each flaw's trajectory across the week; the per-flaw mechanism,
  affected and fixed versions, exploitation evidence and detection guidance live in the referenced
  operational entries, each of which was composed and verified against the vendor or authority
  record cited here. No CVE identifiers are carried in this entry's frontmatter for that reason —
  the operational entries own the structured records. Where two authorities give different
  exploitation determinations for the same identifier, the divergence is treated in this week's
  separate multi-day entry rather than resolved here. Two transport limits are disclosed rather
  than hidden. The CISA catalogue was re-fetched in full during this run (version 2026.08.21) and
  every catalogue date above is read from it, which is also how the Zimbra listing of 2026-08-21 —
  later than the operational entry that first covered the flaw — was found. Microsoft's
  update-guide pages and ENISA's vulnerability records are both client-rendered and returned no
  readable content on any transport available this run (the reader relay's credit pool is
  exhausted across every key), so the ShieldBreak detail attributed to Microsoft's advisory is
  carried exactly as this pipeline's verified entry of 18 August recorded it from that page, with
  France's CERT-FR advisory of 17 August independently confirming the identifier and its relay.
confidence: high
references:
  - 2026-08-18/cve-2025-62593-ray-dashboard-dns-rebinding-browser-rce-kev
  - 2026-07-31/unit42-autonomous-deepseek-hermes-netscaler-cve-2026-3055
  - 2026-07-14/microsoft-july-2026-patch-tuesday-two-exploited-zero-days
  - 2026-08-20/cve-2026-64849-mlflow-webhook-ssrf-redirect-bypass-kev
  - 2026-08-20/cve-2026-73570-zimbra-snmp-command-injection-exploited
  - 2026-08-23/trueconf-server-kev-head-mare-trojanized-installer
  - 2026-06-20/ptc-windchill-cve-2026-12569-unauthenticated-java-deserializ
  - 2026-08-09/metabase-unauth-sqli-zeroday-exploited-framework-tally
  - 2026-08-15/geoserver-jsonarraycontains-unauth-sqli-zeroday-exploited
  - 2026-08-19/cve-2026-18963-keycloak-reset-credentials-account-takeover
  - 2026-08-19/cve-2026-19478-gitlab-graphql-unauth-data-destruction
  - 2026-08-20/cve-2026-19490-netscaler-gateway-aaa-auth-bypass
  - 2026-08-20/oracle-august-2026-cpu-three-unauthenticated-cvss-10
  - 2026-08-19/cve-2026-15748-forminator-forms-unauth-file-upload-rce
  - 2026-08-19/cve-2026-15826-user-profile-builder-type-confusion-admin
  - 2026-08-12/shieldbreak-defender-rogueplanet-patch-bypass-no-fix
  - 2026-08-23/misp-stix-import-trust-boundary-dos-parser-state
  - 2026-08-08/cisco-ios-xe-august-2026-hardening-release-cwe-grouped-cves
weekly_section: weekly-vuln-rollup
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions:
  - "Upgrade Crosswork Data Gateway, Network Controller, Planning and Workflow Manager to 7.2.1-SP or 2.1.1-SP, and Secure Workload to 3.10.9.1 or 4.0.4.16 — Cisco states there is no workaround for any of the nine, so patching is the only remediation. On Secure Workload SaaS, do not treat this as handled: Cisco has upgraded the cluster software but the agent and connector software is still the customer's to upgrade."
updates:
  - at: "2026-08-24T09:15:00Z"
    run_id: 2026-08-22T0410Z-intel
    type: update
    summary: >
      Cisco published two internal-security-review hardening advisories covering Crosswork network
      orchestration and Secure Workload microsegmentation, together carrying nine CVEs, five of them
      scored 10.0. The structure is the operationally important part: Cisco grouped multiple
      internally found bugs by weakness class and assigned one CVE per class, scored at the worst
      underlying bug, so no individual flaw can be assessed and remediation is by release rather than
      by finding. Reading the vendor's own CVSS vectors, six of the nine need no authentication and
      three need only low privilege — not the uniform unauthenticated set the score list suggests.
      Cisco states it is not aware of malicious use and that no workarounds exist. On Secure Workload
      SaaS, Cisco has upgraded the cluster but the agent and connector software remains the customer's
      to patch.
    fields:
      - actions
      - affected_products
      - cves
      - evidence
      - references
      - sectors
      - sources
      - tags
      - techniques
      - body
    merged_from: 2026-08-24/cisco-crosswork-secure-workload-nine-cwe-grouped-cves
migrated_from: null
---

### Newly exploited or newly catalogued this week

Seven flaws crossed the line. Six of them share a property more instructive than any of them individually — **all six already had a fix**, and three had had one for a month or more — and the seventh, at the end of this list, is the exception that shows what the other six are missing.

- **CVE-2025-62593 — Ray.** CISA catalogued it as exploited on 2026-08-17 ([CISA KEV catalog v2026.08.21, 2026-08-21](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)). The dashboard's only guard against browser-borne requests is a User-Agent prefix check that Firefox and Safari let a page overwrite, so with DNS rebinding a developer's own browser becomes the path into a cluster that was never internet-exposed. Fixed in Ray 2.52.0 — the first release to offer authentication at all, and it is off by default. First covered 2026-08-18.
- **CVE-2026-33824 — Windows IKE and AuthIP IPsec Keying Modules.** Catalogued 2026-08-18, four months after the April cumulative updates carried the fix. Pre-authentication double free on UDP 500 and 4500, code execution in the Local System context. First covered 2026-08-10 as patched-but-not-exploited; that is the field that changed.
- **CVE-2026-55040 — Microsoft SharePoint Server.** Catalogued 2026-08-18. Pre-authentication weak-authentication bypass allowing impersonation, patched in July for Subscription Edition, 2019 and Enterprise Server 2016. First covered 2026-08-13 as proof-of-concept-public on honeypot replay evidence. For this constituency it lands on an estate this pipeline has already covered two intrusions into — the Swiss federal IT provider BIT and canton Graubünden each disclosed an on-premises SharePoint breach in early August, and no source ties either to this identifier.
- **CVE-2026-64849 — MLflow.** Catalogued 2026-08-19 with a 2026-09-02 remediation date. The webhook URL guard resolves the hostname, rejects non-public addresses at registration, then throws the answer away and follows redirects without re-validating — so one redirect turns an unauthenticated tracking server into a reader of its own cloud instance-metadata service. Fixed in MLflow 3.15.0. First covered 2026-08-20.
- **CVE-2026-73570 — Zimbra Collaboration.** ENISA's database recorded it exploited since 2026-08-18, and CISA catalogued it on 2026-08-21 — after this pipeline's operational coverage, so this is a fresh delta for the week ([CISA KEV catalog v2026.08.21, 2026-08-21](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)). Pre-authentication command injection in the SNMP monitoring component reaching OS command execution as the Zimbra user; only where the optional `zimbra-snmp` package is installed and notifications are enabled. Fixed 2026-07-21 in ZCS 10.1.20 — a month before the identifier existed. First covered 2026-08-20.
- **CVE-2026-72529 and CVE-2026-72530 — TrueConf Server.** Both catalogued 2026-08-20 ([CISA KEV catalog v2026.08.21, 2026-08-21](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)). Chained, they take an unauthenticated attacker from port 4307/TCP — open by default per the vendor's documentation — to command execution as SYSTEM. Fixed 2026-06-18 in 5.3.9, 5.4.9 and 5.5.5 — two months before the listing — by the coordinating CNA's account ([Kaspersky ICS CERT, 2026-08-12](https://ics-cert.kaspersky.com/publications/reports/2026/08/12/head-mare-exploits-vulnerabilities-in-trueconf-server-to-deliver-phantomcore-malware/)); the same research places the operators' use of the chain from at least July 2026, and the referenced operational entry carries that detail with its own citation. First covered 2026-08-23.

- **CVE-2026-19478 — GitLab.** Released outside the scheduled cadence on 2026-08-17 at CVSS 9.4, with the companion CSRF flaw CVE-2026-19650 at 7.1; an unauthenticated caller can modify or delete public projects and user data, every release line from 18.2 onward is affected, and GitLab.com and Dedicated were already patched, so the exposure is entirely self-managed instances ([GitLab, 2026-08-17](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-2-4-released/)). Exploitation began roughly two days after public disclosure, per an attack-surface-management firm reported by SecurityWeek ([SecurityWeek, 2026-08-20](https://www.securityweek.com/critical-gitlab-flaw-exploited-shortly-after-disclosure/)), and Switzerland's NCSC amended its own advisory on 2026-08-21 to change the recorded exploitation status from unknown to actively exploited, citing that coverage ([NCSC-CH, 2026-08-21](https://security-hub.ncsc.admin.ch/#/posts/12856)). Unlike the six above, no catalogue was involved and the fix was six days old — this is the one flaw on the week's list a normal patch queue would most plausibly still be holding.

### Continuing exploitation

- **CVE-2026-12569 — PTC Windchill.** Cl0p's extortion wave continues; the week's delta is a published reverse engineering of the custom implant rather than a change in exploitation status. Status detail in this week's long-running entry.
- **CVE-2026-72898 — Metabase.** The exploited CVSS 10.0 password-reset SQL injection is unchanged; the delta is the downstream count, now nine publicly confirmed organisations reached through credentials the compromised instances held.
- **GeoServer `jsonArrayContains` SQL injection — still no CVE.** Exploited since before it had a fix; GeoServer 3.0.1, 2.28.5 and 2.27.6 shipped on 2026-08-14, which the project calls an urgent update for production systems ([GeoServer project, 2026-08-14](https://geoserver.org/announcements/vulnerability/2026/08/14/geoserver-3-0-1-released.html)), and Switzerland's NCSC appended the fixed versions to its own advisory on 2026-08-17 while still recording the flaw as actively exploited ([NCSC-CH, 2026-08-17](https://security-hub.ncsc.admin.ch/#/posts/12844)). The absence of an identifier keeps it invisible to a purely CVE-driven patch process.

### Critical, no exploitation reported

- **CVE-2026-18963 — Keycloak, CVSS 9.1.** The reset-credentials flow can be driven to completion without the verification email being clicked, yielding unauthenticated takeover of any account including administrators. Fixed 2026-08-18 in Red Hat build of Keycloak 26.4.15 and 26.6.6, and the two fixed streams are not equivalent: 26.6.6 closes five flaws, two of them further account-takeover and credential-disclosure paths on the same identity surface. **A correction to this pipeline's coverage of 19 August belongs here.** That entry recorded the `keycloak-services` component as Affected with no erratum in the JBoss Enterprise Application Platform Expansion Pack, and therefore part of the estate as having nothing to apply. Re-read this week, Red Hat's own product-state table for this CVE carries eleven Fixed rows and two Not-affected rows, and the Expansion Pack is one of the two — state "Not affected", justification "Component not Present"; Red Hat Single Sign-On 7 is the other, justified as vulnerable code not present ([Red Hat Product Security, 2026-08-18](https://access.redhat.com/security/cve/CVE-2026-18963)). No Red Hat product is recorded as affected and unfixed. An estate that deferred this flaw on the basis of that earlier reading should treat it as fully patchable today.
- **CVE-2026-19490 — Citrix NetScaler ADC and Gateway, CVSS 9.3**, with CVE-2026-19489 alongside it. The exposure boundary is wider than the headline: on 14.1-43.56 and 13.1-61.28 and later the bypass applies only where a SAML action is configured, but on earlier builds and 13.1 FIPS any Gateway or AAA virtual server configuration is enough ([CERT-EU, 2026-08-19](https://cert.europa.eu/publications/security-advisories/2026-010/)). Its exploitation status is itself contested: Switzerland's NCSC amended its advisory on 2026-08-21 to record the flaw as actively exploited, and the only supporting coverage it cites for that change is a single post on a social-media platform ([NCSC-CH, 2026-08-21](https://security-hub.ncsc.admin.ch/#/posts/12863)) — a basis this pipeline does not treat as establishing exploitation, so the flaw stays in this section with the divergence recorded.
- **Cisco Crosswork and Secure Workload — eight critical flaws, five of them at CVSS 10.0.** Not previously covered by this pipeline and recovered by this week's review: CVE-2026-20030 (SQL injection in Crosswork applications), CVE-2026-20357 (missing authentication for a critical function in Crosswork), CVE-2026-20358 (external control of the file system in Crosswork), CVE-2026-20315 (improper access control in Secure Workload) and CVE-2026-20317 (improper authentication in Secure Workload) all carry CVSS 3.1 10.0; CVE-2026-20359 (insufficiently protected credentials) and CVE-2026-20231 (command injection) carry 9.9, and CVE-2026-20318 (path traversal) 9.6. Switzerland's NCSC relayed the two Cisco advisories on 2026-08-21, recording that successful exploitation lets unauthenticated remote attackers execute arbitrary commands, bypass authentication and gain full control over affected systems, with vendor patches available and exploitation status unknown ([NCSC-CH, 2026-08-21](https://security-hub.ncsc.admin.ch/#/posts/12867)). Affected are Crosswork Data Gateway, Crosswork Network Controller, Crosswork Planning and Secure Workload in both SaaS and on-premises deployments — network-management and workload-security platforms that sit above the estate they manage, which is what makes a 10.0 on them worth sequencing ahead of its score.
- **Oracle August 2026 Critical Security Patch Update** — 943 patches, three of them unauthenticated CVSS 10.0 with Privileges Required and User Interaction both None: CVE-2026-61241 in the LDAP server of Oracle Internet Directory, and CVE-2026-70880 and CVE-2026-70921 in the Hyperion products ([Oracle, 2026-08-18](https://www.oracle.com/security-alerts/cspuaug2026.html)).
- **Two WordPress plugin flaws at CVSS 9.8** — CVE-2026-15748 in Forminator Forms (600,000+ installs, unauthenticated arbitrary file upload to code execution, fixed 1.56.2) and CVE-2026-15826 in User Profile Builder (40,000+ installs, a type coercion that logs an anonymous registrant in as user ID 1, fixed 3.16.5). Both were patched before their root causes went public, and both reached this pipeline through Switzerland's NCSC Cyber Security Hub bundle of 2026-08-18 ([NCSC-CH, 2026-08-18](https://security-hub.ncsc.admin.ch/#/posts/12860)).

### No fix exists

- **CVE-2026-69414 — the ShieldBreak Defender privilege-escalation bypass.** Microsoft acknowledged it, rated it Important at CVSS 7.8, records it publicly disclosed but not exploited, assesses exploitation as more likely, and states a security update is still being worked on ([Microsoft Security Response Center, 2026-08-14](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69414)). Switzerland's NCSC and France's CERT-FR both relayed the identifier on 2026-08-17.
- **The `misp-stix` trio (CVE-2026-77710, CVE-2026-77755, CVE-2026-77761).** Disclosed 2026-08-21 against the library MISP and other platforms use to convert between MISP and STIX. No tagged release carries the fixes; remediation is individual commits. Directly relevant to anyone running an intelligence-ingestion pipeline, including this one.

**Defender takeaway:** the sequencing lesson of this week is that an exploitation feed is trailing indicator, not an early-warning system. Every flaw that crossed into confirmed exploitation had a fix available first, in three cases long before — so an estate that patches only what a catalogue flags is, by construction, patching after exploitation begins. The one flaw that crossed under its own steam is the counter-example worth keeping: GitLab's CVE-2026-19478 went from an out-of-band patch to reported exploitation in about two days with no catalogue involved at any point. Otherwise the flaws that would have needed out-of-band handling were the ones with no exploitation signal and a mechanic that forces the timeline anyway: an identity provider whose account-recovery path is the account-takeover path and is reachable by anyone who can reach the realm, an authentication bypass on internet-facing remote-access appliances whose precondition on older builds is simply having the service configured, and five CVSS 10.0 flaws on network-management and workload-security platforms that sit above the estate they manage. Sequence on reachability and mechanics; use the catalogue to confirm you were right, not to decide.

## Update — 2026-08-24T09:15:00Z

Cisco published two hardening advisories out of internal security review on 2026-08-19 covering Crosswork — its network orchestration, planning and workflow platform — and Secure Workload, its workload microsegmentation product. Together they carry nine CVEs, five of them scored 10.0 and two more 9.9 ([Cisco PSIRT, 2026-08-19](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-crosswork-UzDTU9Vh), [Cisco PSIRT, 2026-08-19](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-csw1-shSvndWP)). The number to read past is the score; the structure behind it is what changes a defender's options. Cisco states it grouped the issues by underlying weakness class and assigned one CVE identifier per grouping, and that each score represents the maximum potential severity of the single most impactful underlying bug within that class ([Cisco PSIRT, 2026-08-19](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-crosswork-UzDTU9Vh)). One identifier can therefore stand for several distinct bugs, and no individual flaw is assessable from the advisory — the estate is triaged by release, not by finding. This pipeline recorded the identical construction in Cisco's August IOS XE hardening release, so it now reads as a settled disclosure practice on internally found bug batches rather than a one-off.

The authentication picture is more mixed than a list of tens implies, and the vendor's own vectors settle it. On Crosswork, CVE-2026-20030 (SQL injection), CVE-2026-20357 (missing authentication for a critical function) and CVE-2026-20358 (external control of a file path) all carry `PR:N` at 10.0, while CVE-2026-20359 (insufficiently protected credentials, 9.9) carries `PR:L` and therefore needs an existing low-privilege account. On Secure Workload, CVE-2026-20315 (improper access control) and CVE-2026-20317 (improper authentication) are `PR:N` at 10.0 and CVE-2026-20319 (a memory-buffer restriction failure, 7.5, availability impact only) is `PR:N`, while CVE-2026-20231 (injection, 9.9) and CVE-2026-20318 (improper input validation, 9.6) are both `PR:L`. NCSC-NL's independently published record for the Secure Workload cluster carries the same five vectors ([NCSC-NL, 2026-08-21](https://advisories.ncsc.nl/advisory?id=NCSC-2026-0323)). Six unauthenticated and three at low privilege is not a reassuring split: low privilege on an orchestration or microsegmentation control plane means any read-only API consumer or delegated operator role is a sufficient foothold.

Cisco is explicit that it is not aware of any public announcements or malicious use of these vulnerabilities, and equally explicit that there are no workarounds that address them ([Cisco PSIRT, 2026-08-19](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-csw1-shSvndWP)). Two further details change the work involved. Cisco credits the discovery to internal security testing "using existing testing processes as well as frontier AI models" ([Cisco PSIRT, 2026-08-19](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-crosswork-UzDTU9Vh)) — the second Cisco hardening batch this month attributed partly to model-assisted internal review, which is a plausible explanation for why these arrive in classes rather than singly. And on Secure Workload SaaS, the fix is not fully server-side: Cisco states the cluster, agent and connector software all need upgrading and that for SaaS deployments it has upgraded the cluster while customers must still upgrade the agent and connector ([Cisco PSIRT, 2026-08-19](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-csw1-shSvndWP)). A SaaS tenant that assumed its provider had closed this out has client-side work outstanding.

Because the advisories describe weakness classes rather than reachable interfaces, there is no honest per-flaw detection guidance to give and this entry does not invent any. What is available is exposure reduction and the audit trail these platforms already produce: establish which interfaces of each product answer from outside the management network at all, and treat the low-privilege accounts on both platforms as part of the blast radius rather than as a trust boundary — service accounts and delegated operator roles on an orchestration platform are the foothold three of these nine flaws need. Both products' own audit logging is the place a defender would see the consequence of exploitation rather than the attempt: configuration writes, policy changes and credential reads that do not correspond to a change request.
