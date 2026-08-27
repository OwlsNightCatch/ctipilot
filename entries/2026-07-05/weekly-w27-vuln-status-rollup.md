---
schema: 1
kind: vulnerability
horizon: strategic
weekly_section: weekly-vuln-rollup
title: "Vulnerability status roll-up — 2026-W27: what moved, what to patch on the exploited-flaw clock vs the monthly cycle"
headline: "Vuln status roll-up 2026-W27 — exploited, KEV-listed, working-exploit, and weaponisation-likely items"
summary: "The week's vulnerability status at a glance for a public-sector estate: newly exploited/KEV (SimpleHelp CVE-2026-48558, Oracle EBS CVE-2026-46817, SharePoint CVE-2026-45659, Kemp LoadMaster CVE-2026-8037); working-exploit or PoC (DirtyClone Linux LPE CVE-2026-43503, libssh2 CVE-2026-55200, Citrix NetScaler CVE-2026-8451); and weaponisation-likely-but-not-yet-exploited (six CVSS 10.0 Adobe ColdFusion RCEs, Control Web Panel CVE-2026-57517, Coolify CVE-2026-34038)."
discovered_at: "2026-07-05T23:30:00Z"
event_date: null
run_id: 2026-07-05T2305Z-weekly
priority: high
immediate_action: null
tags:
  - vulnerabilities
  - actively-exploited
  - cisa-kev
  - rce
  - patch-available
regions:
  - global
  - europe
sectors:
  - public-sector
  - finance
  - technology
entities: []
cves: []
sources:
  - url: "https://helpx.adobe.com/security/products/coldfusion/apsb26-68.html"
    publisher: Adobe PSIRT (APSB26-68)
    role: primary
  - url: "https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-45659"
    publisher: Microsoft MSRC
    role: primary
  - url: "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    publisher: CISA KEV feed
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: "Consolidated status view; each CVE's full sourcing lives in the operational entry that first covered it (see references and inline links). Frontmatter cves[] is intentionally empty — the operational entries own the CVE index; this entry is the week's status lens."
confidence: high
classification: null
update_of: null
references:
  - "2026-06-30/cve-2026-48558-simplehelp-rmm-oidc-sso-authentication-bypass"
  - "2026-07-01/oracle-e-business-suite-cve-2026-46817-pre-auth-rce-in-the-p"
  - "2026-07-02/cve-2026-45659-microsoft-sharepoint-server-authenticated-des"
  - "2026-06-30/cve-2026-8037-progress-kemp-loadmaster-pre-auth-rce-via-unin"
  - "2026-06-27/cve-2026-43503-linux-kernel-dirtyclone-page-cache-corruption"
  - "2026-06-28/cve-2026-55200-libssh2-heap-out-of-bounds-write-in-ssh2-tran"
  - "2026-07-01/cve-2026-8451-citrix-netscaler-adc-gateway-pre-auth-saml-mem"
  - "2026-07-02/cve-2026-48276-48277-48281-48282-48283-48316-adobe-coldfusio"
  - "2026-07-03/cve-2026-57517-control-web-panel-pre-auth-sqli-to-rce"
  - "2026-07-03/cve-2026-34038-coolify-authenticated-command-injection-to-rc"
  - "2026-06-20/cve-2026-52806-gogs-self-hosted-git-server-argument-injectio"
  - "2026-06-30/cert-polska-discloses-a-jar-parser-confusion-rce-in-the-szaf"
  - "2026-07-02/cve-2026-14439-altium-enterprise-server-altium-365-authentic"
  - "2026-07-05/cve-2026-59509-cve-search-fetch-cve-data-nosql"
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions:
  - "Patch on the exploited-flaw clock, not the monthly cycle: SimpleHelp (v5.5.16/v6.0 RC2), Oracle EBS (May 2026 CPU), SharePoint (May 2026 SU — Microsoft still rates it 'Exploitation Less Likely', but it is KEV-listed), Kemp LoadMaster (v7.2.63.2)."
  - "Patch the weaponisation-likely-but-not-yet-exploited set before a PoC lands: Adobe ColdFusion 2025 Update 10 / 2023 Update 21 (six CVSS 10.0 unauth RCEs, Adobe Priority 1); Control Web Panel; Coolify."
  - "Patch the working-exploit/PoC items on your standard emergency cadence: DirtyClone Linux kernel LPE (default Debian/Fedora), libssh2 pre-auth heap write, Citrix NetScaler (test exposure with the public artefact generator)."
---

This is the week's vulnerability state as a single scannable view — the CVE detail and full sourcing live in the operational entries that first covered each item (§ references); the value here is the current status and the patch-priority framing.

**Newly exploited / KEV-listed this week (assume-compromise if exposed and unpatched).** SimpleHelp RMM **CVE-2026-48558** (CVSS 10.0 OIDC auth bypass) moved to active exploitation + CISA KEV, deploying the Djinn infostealer (this week's top story). Oracle E-Business Suite **CVE-2026-46817** (pre-auth RCE) saw its first in-the-wild exploitation. Microsoft SharePoint Server **CVE-2026-45659** (CWE-502 deserialization, Site-Member RCE) was added to CISA KEV on 2026-07-01 — the first public confirmation of exploitation, and notable because Microsoft's own advisory still rates it "Exploitation Less Likely," a contradiction defenders should resolve toward the exploitation evidence ([Microsoft MSRC](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-45659); [CISA KEV feed, 2026-07-01](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)). Progress Kemp LoadMaster **CVE-2026-8037** (pre-auth RCE) drew exploitation attempts the day its PoC dropped (covered in this week's edge-appliance entry).

**Working exploit or public PoC (patch on emergency cadence).** DirtyClone Linux-kernel LPE **CVE-2026-43503** now has a confirmed working exploit on default Debian/Fedora; the libssh2 pre-auth heap write **CVE-2026-55200** has a public PoC; Citrix NetScaler **CVE-2026-8451** has a public susceptibility-testing artefact.

**Weaponisation-likely, not yet exploited (patch before the PoC lands).** Adobe's APSB26-68 fixed **six CVSS 10.0** unauthenticated RCE paths in ColdFusion 2025/2023 — two unrestricted-file-upload, three input-validation, one path-traversal — all Adobe Priority 1 ("high risk of being targeted"), with Adobe stating no known in-the-wild exploits yet; ColdFusion's history of rapid weaponisation of unauth file-upload primitives makes this a same-week patch priority for any internet-facing instance ([Adobe PSIRT APSB26-68, 2026-06-30](https://helpx.adobe.com/security/products/coldfusion/apsb26-68.html)). Control Web Panel **CVE-2026-57517** (pre-auth SQLi→RCE) and Coolify **CVE-2026-34038** (authenticated command injection, CVSS 9.9) round out the high-impact patch set.

**Also patched this week (standard cycle, no exploitation):** Gogs **CVE-2026-52806** (now abused for cryptojacking), the SzafirHost e-signature client JAR parser-confusion RCE **CVE-2026-13165** (CERT Polska — EU public-sector e-signature relevance), Altium Enterprise Server **CVE-2026-14439**, and cve-search **CVE-2026-59509**. Full per-CVE detail in § references.
