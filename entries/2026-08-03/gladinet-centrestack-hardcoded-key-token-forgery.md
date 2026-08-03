---
schema: 1
kind: vulnerability
horizon: operational
title: "CVE-2026-54363 and five siblings — Gladinet CentreStack: one cryptographic key shared across every installation forges a domain-administrator token, completing an unauthenticated RCE chain"
headline: "Six unauthenticated flaws in Gladinet CentreStack; a key identical in every install forges admin tokens"
summary: >
  Gladinet CentreStack, an internet-facing enterprise file-sharing and sync platform, carries six
  vulnerabilities disclosed on 2026-07-30 and fixed across releases 17.2 through 17.5. The most
  severe, CVE-2026-54363, derives the key protecting CentreStack's access tickets from a static
  value that is the same in every installation, so an unauthenticated attacker forges an
  authentication header, calls a privileged endpoint and obtains a domain-administrator ticket —
  what the discloser calls a complete unauthenticated remote code execution chain. Five siblings
  add unauthenticated account-setting access, OS-account creation, XXE file exfiltration, session
  injection and an authenticated SQL injection that writes files to disk. No exploitation is
  reported, but three earlier CentreStack flaws (CVE-2025-30406, CVE-2025-11371, CVE-2025-14611)
  reached the exploited-vulnerabilities catalog.
  Upgrade to 17.5, which is the only release that closes all six.
discovered_at: "2026-08-03T05:20:00Z"
event_date: "2026-07-30"
run_id: 2026-08-03T0409Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, auth-bypass, pre-auth, rce, sqli, info-disclosure, patch-available]
regions: [global]
sectors: [technology, public-sector]
entities: []
techniques: [T1190, T1606, T1136.001, T1552.001]
affected_products: ["Gladinet CentreStack"]
cves:
  - id: CVE-2026-54363
    cvss: "9.3"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "CentreStack before 17.5"
    fixed: "17.5"
    note: "CWE-321 hardcoded cryptographic key. A static SysNumber value is the entropy for AccessTicket encryption across all installations, letting an attacker forge x-glad-auth headers and obtain a domain-administrator IdentityTicket."
  - id: CVE-2026-54367
    cvss: "8.8"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "CentreStack before 17.2"
    fixed: "17.2"
    note: "CWE-306 missing authentication. Forged encrypted EntAcctId values reach account settings for any user GUID, including the system-wide cluster settings account."
  - id: CVE-2026-54365
    cvss: "8.7"
    epss: null
    type: deserialization
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "CentreStack before 17.3"
    fixed: "17.3"
    note: "CWE-306. Unauthenticated deserialization in GSNamespace.dll reaches NetUserAdd, creating arbitrary local OS accounts."
  - id: CVE-2026-54366
    cvss: "8.7"
    epss: null
    type: info-disclosure
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "CentreStack before 17.4"
    fixed: "17.4"
    note: "CWE-611 XXE at the unauthenticated SharePoint StorageConfig endpoint; out-of-band exfiltration of files such as Web.config."
  - id: CVE-2026-54368
    cvss: "8.7"
    epss: null
    type: sqli
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "CentreStack before 17.4"
    fixed: "17.4"
    note: "CWE-89 in GladDBFiles.SearchEx()/SearchExUnder() via the x-glad-filter header; reaches file write through PostgreSQL large-object functions. The only member of the batch that requires authentication."
  - id: CVE-2026-54364
    cvss: "6.9"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "CentreStack before 17.4"
    fixed: "17.4"
    note: "CWE-116. Newline and tab characters in AccountName inject session variables at SelectProvider.aspx, bypassing the IsValidRSession check."
sources:
  - url: "https://www.vulncheck.com/advisories/centrestack-hardcoded-key-token-forgery-rce"
    publisher: "VulnCheck"
    date: "2026-07-30"
    role: primary
  - url: "https://www.vulncheck.com/advisories/centrestack-unauthenticated-api-authorization-bypass"
    publisher: "VulnCheck"
    date: "2026-07-30"
    role: primary
  - url: "https://www.vulncheck.com/advisories/centrestack-unauthenticated-user-creation-via-deserialization-in-gsnamespace-dll"
    publisher: "VulnCheck"
    date: "2026-07-30"
    role: primary
  - url: "https://www.vulncheck.com/advisories/centrestack-xxe-via-sharepoint-storage-configuration"
    publisher: "VulnCheck"
    date: "2026-07-30"
    role: primary
  - url: "https://www.vulncheck.com/advisories/centrestack-sql-injection-via-x-glad-filter-header"
    publisher: "VulnCheck"
    date: "2026-07-30"
    role: primary
  - url: "https://www.vulncheck.com/advisories/centrestack-session-injection-via-selectprovider-aspx"
    publisher: "VulnCheck"
    date: "2026-07-30"
    role: primary
closed_sources: []
evidence:
  - quote: "CentreStack before 17.5 contains a hardcoded cryptographic key vulnerability that allows unauthenticated attackers to forge arbitrary encrypted tokens by exploiting a static SysNumber value used as entropy for AccessTicket.Encrypt() and AccessTicket.Decrypt() across all installations."
    publisher: "VulnCheck"
  - quote: "Attackers can use the hardcoded key to craft valid x-glad-auth headers and call privileged API endpoints such as acquiretenantbackuptoken to obtain a domain administrator IdentityTicket, enabling a complete unauthenticated remote code execution chain."
    publisher: "VulnCheck"
verification: single-source
sourcing_note: >
  All six flaws trace to per-vulnerability advisories from the disclosing research team, which is
  also the numbering authority's reporting source; the national vulnerability databases carry the
  same records rather than an independent assessment, so this is one assessor with several
  publishers. No vendor advisory page for this batch was reachable during the run — the vendor's
  site resolves only to a product homepage, which is not citable — so the discloser's per-CVE
  advisories are the most primary source available. The CVSS 4.0 base scores and affected/fixed
  ranges in this entry's CVE metadata are the numbering authority's own and are displayed on each
  cited advisory page alongside the mechanics. **First coverage, not fresh news:** the disclosure is dated 2026-07-30 and no
  in-window development has moved it — this pipeline did not cover it at the time and is publishing
  it now rather than leaving the gap open. The dates in this entry are the real ones.
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Upgrade internet-facing Gladinet CentreStack to 17.5 — the six flaws are fixed across four different releases (17.2, 17.3, 17.4, 17.5) and only 17.5 closes all of them, so an estate on 17.4 has the token-forgery flaw open."
  - "Because the token-forgery key is identical in every installation rather than per-tenant, treat administrator credentials and access tickets on any CentreStack instance that was internet-reachable before the upgrade as potentially forged: rotate administrator credentials and review the platform's local OS accounts for entries no administrator created."
migrated_from: null
---

Gladinet CentreStack is an enterprise file-sharing and sync platform typically deployed as an internet-facing portal, and on 2026-07-30 six vulnerabilities in it were disclosed with per-flaw technical write-ups. This entry is first coverage of that disclosure rather than a report of something that happened today — no development has moved it since, and the dates here are the disclosure's own. The reason it still matters three days on is the shape of the lead flaw and the platform's history: three earlier CentreStack vulnerabilities — CVE-2025-30406, CVE-2025-11371 and CVE-2025-14611 — have been added to the US authorities' catalog of exploited vulnerabilities, so this product line has a demonstrated record of disclosure being followed by in-the-wild abuse.

The lead flaw is CVE-2026-54363, and its defect is that the secret is not a secret. The advisory states that CentreStack "contains a hardcoded cryptographic key vulnerability that allows unauthenticated attackers to forge arbitrary encrypted tokens by exploiting a static SysNumber value used as entropy for AccessTicket.Encrypt() and AccessTicket.Decrypt() across all installations" ([VulnCheck, 2026-07-30](https://www.vulncheck.com/advisories/centrestack-hardcoded-key-token-forgery-rce)). Because that value is the same everywhere rather than generated per deployment, anyone who extracts it once can forge tokens against every CentreStack on the internet: the advisory continues that attackers "can use the hardcoded key to craft valid x-glad-auth headers and call privileged API endpoints such as acquiretenantbackuptoken to obtain a domain administrator IdentityTicket, enabling a complete unauthenticated remote code execution chain" ([VulnCheck, 2026-07-30](https://www.vulncheck.com/advisories/centrestack-hardcoded-key-token-forgery-rce)). There is no authentication step to defeat and no user to phish — it is a forged header on a request.

The five siblings are independent bugs rather than variants, and they are fixed in four different releases, which is the practical trap in this batch. CVE-2026-54367 lets an unauthenticated caller read, write or delete account settings for any user GUID — including the system-wide cluster settings account — by generating valid encrypted `EntAcctId` values with a static shared encryption key, exposing hosted tenant domains and administrator identities ([VulnCheck, 2026-07-30](https://www.vulncheck.com/advisories/centrestack-unauthenticated-api-authorization-bypass)). CVE-2026-54365 is an unauthenticated deserialization flaw in `GSNamespace.dll`: a crafted base64-encoded XML `StorageConfigure` parameter sent to one of three import endpoints reaches `InternalImportAdUserByUPN()`, which causes `GladinetCloudMonitor.exe` to call the Windows `NetUserAdd` API and create local OS accounts with attacker-chosen credentials ([VulnCheck, 2026-07-30](https://www.vulncheck.com/advisories/centrestack-unauthenticated-user-creation-via-deserialization-in-gsnamespace-dll)). CVE-2026-54366 is an XXE at the unauthenticated SharePoint `StorageConfig` endpoint that exfiltrates files out-of-band, `Web.config` among them ([VulnCheck, 2026-07-30](https://www.vulncheck.com/advisories/centrestack-xxe-via-sharepoint-storage-configuration)). CVE-2026-54364 injects session variables by embedding newline and tab characters in an `AccountName` parameter posted to `SelectProvider.aspx`, forging a `resellerid` variable that bypasses the `IsValidRSession` check ([VulnCheck, 2026-07-30](https://www.vulncheck.com/advisories/centrestack-session-injection-via-selectprovider-aspx)). CVE-2026-54368 is the only member requiring authentication: unsanitised interpolation of a `Field` parameter from the `x-glad-filter` header into `GladDBFiles.SearchEx()` reaches arbitrary SQL, and via PostgreSQL's large-object functions, arbitrary file writes to the server filesystem ([VulnCheck, 2026-07-30](https://www.vulncheck.com/advisories/centrestack-sql-injection-via-x-glad-filter-header)).

Detection follows the fact that every unauthenticated path here is an HTTP request to a named endpoint, so web-server and application access logs are the primary telemetry, not the endpoint agent. The observable classes are requests carrying an `x-glad-auth` header from source addresses that are not an established client, requests to the tenant-backup-token endpoint at all (a privileged administrative call that has no reason to arrive from the open internet), POSTs to the user-import endpoints named above, and `x-glad-filter` header values containing SQL syntax. On the host, the durable artifact of the account-creation flaw is a local OS account appearing without a corresponding administrative action, and the process lineage to look for is the CentreStack monitor service creating accounts or directories. Discriminating benign traffic is mostly a question of origin and endpoint pairing: legitimate CentreStack clients authenticate through the normal portal flow and do not call tenant-backup or user-import endpoints directly, so it is the combination of a privileged endpoint and an unexpected caller — rather than either alone — that is the signal. No proof-of-concept is public and no exploitation is reported for any of the six.

**Defender takeaway:** the upgrade target is 17.5 and nothing lower, because the fixes are spread across 17.2, 17.3, 17.4 and 17.5 and the most severe flaw is the one fixed last — an estate that patched to 17.4 has closed five of six and left the token forgery open. Beyond patching, the hardcoded-key mechanic has a consequence a version bump does not undo: because the key was never unique to your installation, any administrative ticket that existed while the instance was internet-reachable should be treated as forgeable rather than trusted, which makes credential rotation and a review of locally created OS accounts part of the remediation rather than an optional extra.
