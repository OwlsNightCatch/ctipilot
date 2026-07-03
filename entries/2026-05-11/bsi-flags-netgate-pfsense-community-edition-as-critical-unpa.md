---
schema: 1
kind: threat
horizon: operational
title: "BSI flags Netgate pfSense Community Edition as critical-unpatched — CVE-2025-69690 / CVE-2025-69691 authenticated root RCE, vendor refuses to fix"
headline: "BSI flags Netgate pfSense Community Edition as critical-unpatched — CVE-2025-69690 / CVE-2025-69691 authenticated root RCE, vendor refuses to fix"
summary: "BSI flags Netgate pfSense Community Edition as critical-unpatched. Netgate refuses to patch two authenticated root-RCE CVEs (CVE-2025-69690 / CVE-2025-69691) on the grounds that admins are expected to have shell privilege — BSI's WID-SEC-2026-1435 advisory (2026-05-08) explicitly rates the unpatched state \"kritisch\" (Full Disclosure, 2026-02-16). Relevant for DACH cantonal / municipal / SME deployments using the free CE build."
discovered_at: "2026-05-11T05:00:00Z"
event_date: 2026-05-08
run_id: 2026-05-11-migrated
priority: high
immediate_action: null
tags:
  - vulnerabilities
  - rce
  - no-patch
  - default-config
regions:
  - dach
  - europe
sectors:
  - public-sector
  - education
  - healthcare
entities: []
cves:
  - id: CVE-2025-69690
    cvss: "8.8"
    epss: null
    type: rce
    vector: user-interaction
    auth: admin-required
    status:
      - no-patch
      - mitigation-only
  - id: CVE-2025-69691
    cvss: "9.9"
    epss: null
    type: rce
    vector: user-interaction
    auth: admin-required
    status:
      - no-patch
      - mitigation-only
sources:
  - url: "https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1435"
    publisher: "BSI WID-SEC-2026-1435, 2026-05-08"
    role: primary
  - url: "https://seclists.org/fulldisclosure/2026/Feb/16"
    publisher: "Full Disclosure, 2026-02-16"
    role: corroborating
  - url: "https://www.cve.news/cve-2025-69691/"
    publisher: "cve.news — CVE-2025-69691 analysis, 2026-05-08"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-11.md
---

BSI published WID-SEC-2026-1435 on 2026-05-08 rating two authenticated remote code execution vulnerabilities in Netgate pfSense Community Edition as `kritisch` and explicitly `UNGEPATCHT` in the BSI advisory feed ([BSI WID-SEC-2026-1435, 2026-05-08](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1435)). CVE-2025-69691 (CVSS 9.9) affects pfSense CE 2.8.0: the XMLRPC API endpoint `/xmlrpc.php` exposes the `pfsense.exec_php` method, which executes arbitrary PHP as root when invoked with any Basic Auth credentials — including default admin passwords on Internet-exposed deployments ([Full Disclosure, 2026-02-16](https://seclists.org/fulldisclosure/2026/Feb/16); [cve.news analysis of CVE-2025-69691, 2026-05-08](https://www.cve.news/cve-2025-69691/)). CVE-2025-69690 (CVSS 8.8) affects pfSense CE 2.7.2 via unsafe deserialization in the configuration backup/restore path — uploading a crafted backup containing a serialized PHP object with a malicious `post_reboot_commands` property yields root RCE on restore (same primary disclosure thread).

Netgate's position, restated in the Full Disclosure thread, is that both behaviours are expected for authenticated administrators and that no patch will be issued. BSI taking a national-CERT position on the unpatched state three months after researcher disclosure is the in-window signal: this elevates pfSense CE from "vendor accepts behaviour" to "EU national authority recommends mitigation." pfSense Community Edition is licence-free and commonly deployed at the perimeter of Swiss cantonal, municipal, healthcare, education and SME networks where commercial pfSense+ subscriptions are out of reach. The pfSense+ commercial product is reportedly not affected by the same code paths.

**Why it matters to us:** Treat any Internet-exposed pfSense CE management interface (HTTPS web GUI, XMLRPC endpoint, SSH) as a credential-theft single-point-of-failure rather than a hardened control plane. Block the XMLRPC interface at the network level for any CE 2.8.0 deployment that cannot disable it administratively, restrict the web GUI to a management VLAN, rotate any admin passwords that ever traversed unencrypted networks, and audit `system.xml` for unexplained `post_reboot_commands` entries (CVE-2025-69690 persistence indicator). Because exploitation requires existing admin credentials, the operative attack chain is [T1078 Valid Accounts](https://attack.mitre.org/techniques/T1078/) (after credential theft) → [T1059.004 Unix Shell](https://attack.mitre.org/techniques/T1059/004/); for an Internet-exposed management plane, [T1190 Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/) remains the framing for the initial brute-force / credential-stuffing pivot.
