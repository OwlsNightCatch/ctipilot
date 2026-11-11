---
schema: 1
kind: vulnerability
title: "CVE-2026-76954 and CVE-2026-85101, Synology DSM (SA-26:19): a pre-authentication SQL injection in the Auth API (CVSS 9.8) allows arbitrary file read and write, and an rsync authentication bypass reads and writes files; fixed in DSM 7.4.1-90080-1, 7.3.2-86009-5, 7.2.2-72806-10 and 7.2.1-69057-13, no mitigation"
headline: "Synology DSM: pre-auth SQL injection in the Auth API gives file read and write; update to the fixed build of your branch"
summary: >
  Synology's advisory SA-26:19 of 2026-11-10 (severity Critical, no mitigation) fixes two DSM flaws reachable without credentials: an SQL injection in the Auth API that lets remote attackers read or write arbitrary files and cause denial of service (CVE-2026-76954, CVSS 9.8), and an authentication bypass in the rsync service that lets remote attackers read specific files, write arbitrary files and cause limited denial of service (CVE-2026-85101, 8.6). The fixed builds are DSM 7.4.1-90080-1, 7.3.2-86009-5, 7.2.2-72806-10 and 7.2.1-69057-13; no exploitation or public proof of concept is mentioned.
discovered_at: "2026-11-11T03:39:00Z"
updated_at: null
event_date: "2026-11-10"
run_id: 2026-11-11T0256Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, pre-auth, sqli, auth-bypass, patch-available]
regions: [global]
sectors: []
entities: ["product:synology-diskstation-manager-dsm"]
techniques: [T1190]
affected_products: ["Synology DiskStation Manager (DSM)"]
cves:
  - id: CVE-2026-76954
    cvss: "9.8"
    epss: null
    type: sqli
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "DSM before 7.2.1-69057-13, 7.2.2-72806-10, 7.3.2-86009-5 and 7.4.1-90080-1"
    fixed: "7.4.1-90080-1, 7.3.2-86009-5, 7.2.2-72806-10, 7.2.1-69057-13"
  - id: CVE-2026-85101
    cvss: "8.6"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "DSM before 7.2.1-69057-13, 7.2.2-72806-10, 7.3.2-86009-5 and 7.4.1-90080-1"
    fixed: "7.4.1-90080-1, 7.3.2-86009-5, 7.2.2-72806-10, 7.2.1-69057-13"
sources:
  - url: "https://www.synology.com/en-global/support/security/Synology_SA_26_19"
    publisher: "Synology (security advisory SA-26:19)"
    date: "2026-11-10"
    role: primary
  - url: "https://www.cert.cyber.gouv.fr/avis/CERTFR-2026-AVI-1493/"
    publisher: "CERT-FR (avis CERTFR-2026-AVI-1493)"
    date: "2026-11-10"
    role: corroborating
closed_sources: []
evidence:
  - quote: "An improper neutralization of special elements used in an SQL command vulnerability in the Auth API in Synology DiskStation Manager (DSM) before 7.2.1-69057-13, 7.2.2-72806-10, 7.3.2-86009-5, and 7.4.1-90080-1 allows remote attackers to read or write arbitrary files and conduct denial-of-service attacks."
    publisher: "Synology"
    source_url: "https://www.synology.com/en-global/support/security/Synology_SA_26_19"
verification: single-source
sourcing_note: >
  Synology's advisory carries the flaws, scores and fixed builds; CERT-FR lists the same advisory and is a restatement, not an independent assessment. No exploitation or public proof of concept is mentioned in either source.
confidence: high
references: ["2026-09-22/cve-2026-13684-synology-dsm-unauth-file-read-write"]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Update every Synology DSM to 7.4.1-90080-1, 7.3.2-86009-5, 7.2.2-72806-10 or 7.2.1-69057-13, taking the management interface and rsync of any NAS that is reachable from the internet offline until it is updated, because Synology lists no mitigation for either flaw."
updates: []
migrated_from: null
---

Synology's advisory SA-26:19 of 2026-11-10, severity Critical, fixes two DiskStation Manager flaws that need no credentials and lists no mitigation ([Synology, 2026-11-10](https://www.synology.com/en-global/support/security/Synology_SA_26_19)). CVE-2026-76954 (CVSS 9.8) is an SQL injection in the Auth API that lets remote attackers read or write arbitrary files and cause denial of service; CVE-2026-85101 (8.6) is an authentication bypass in the rsync service that lets remote attackers read specific files, write arbitrary files and cause limited denial of service ([Synology, 2026-11-10](https://www.synology.com/en-global/support/security/Synology_SA_26_19)). DSM is fixed in 7.4.1-90080-1, 7.3.2-86009-5, 7.2.2-72806-10 and 7.2.1-69057-13 ([Synology, 2026-11-10](https://www.synology.com/en-global/support/security/Synology_SA_26_19); [CERT-FR, 2026-11-10](https://www.cert.cyber.gouv.fr/avis/CERTFR-2026-AVI-1493/)). The sources mention neither exploitation nor a public proof of concept.

**Exposure:** DSM 7.2.1, 7.2.2, 7.3 and 7.4 below those builds with the management interface reachable (and the rsync service enabled for CVE-2026-85101); the build shows under Control Panel, Info Center.

**Detection:** DSM web and Auth API access logs for SQL syntax or errors in authentication requests, rsync sessions from addresses that are not backup partners, and files in shared folders or system paths that appeared after such requests. After patching, a device that was reachable from the internet needs a check of its scheduled tasks and user accounts, because the file-write primitive can plant persistence.

**Defender takeaway:** update every DSM to the fixed build of its branch now and keep the management interface and rsync off the internet until it is installed; Synology offers no other control, and a NAS holds the backups and shares an intruder wants.
