---
schema: 1
kind: vulnerability
title: "GLPI 10.0.25 and 11.0.7 fix seven CVEs: three stored XSS flaws and missing-authorization bugs that let users delete files and items"
headline: "GLPI patches stored XSS and missing-authorization flaws in 10.0.25 and 11.0.7; no exploitation reported"
summary: >
  GLPI released 10.0.25 and 11.0.7 on 2026-04-29 with fixes for seven CVEs: three stored cross-site
  scripting flaws rated High (knowledge base, ITIL costs, asset locks), arbitrary file and item deletion
  by authenticated users (High), arbitrary file access and an unauthorized export of form structure
  (Medium). CERT-FR relayed the fixes on 2026-05-07; no exploitation is reported.
discovered_at: "2026-05-08T05:00:10Z"
event_date: "2026-04-29"
run_id: 2026-05-08-migrated
priority: routine
immediate_action: null
tags:
  - vulnerabilities
  - patch-available
regions:
  - europe
sectors: []
entities: []
cves:
  - id: CVE-2026-32312
    cvss: "5.1"
    epss: null
    type: info-disclosure
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "11.x before 11.0.7"
    fixed: "11.0.7"
  - id: CVE-2026-40108
    cvss: "7.1"
    epss: null
    type: xss
    vector: user-interaction
    auth: post-auth
    status: [patch-available]
    affected: "11.x before 11.0.7"
    fixed: "11.0.7"
  - id: CVE-2026-42317
    cvss: "7.0"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "10.x before 10.0.25; 11.x before 11.0.7"
    fixed: "10.0.25 / 11.0.7"
  - id: CVE-2026-42318
    cvss: "7.0"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "10.x before 10.0.25; 11.x before 11.0.7"
    fixed: "10.0.25 / 11.0.7"
  - id: CVE-2026-42320
    cvss: "5.9"
    epss: null
    type: info-disclosure
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "10.x before 10.0.25; 11.x before 11.0.7"
    fixed: "10.0.25 / 11.0.7"
  - id: CVE-2026-42321
    cvss: "8.4"
    epss: null
    type: xss
    vector: user-interaction
    auth: post-auth
    status: [patch-available]
    affected: "10.x before 10.0.25"
    fixed: "10.0.25"
  - id: CVE-2026-5385
    cvss: "8.4"
    epss: null
    type: xss
    vector: user-interaction
    auth: post-auth
    status: [patch-available]
    affected: "10.x before 10.0.25; 11.x before 11.0.7"
    fixed: "10.0.25 / 11.0.7"
sources:
  - url: "https://github.com/glpi-project/glpi/releases/tag/11.0.7"
    publisher: "GLPI"
    date: "2026-04-29"
    role: primary
  - url: "https://github.com/glpi-project/glpi/releases/tag/10.0.25"
    publisher: "GLPI"
    date: "2026-04-29"
    role: primary
  - url: "https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0551/"
    publisher: "CERT-FR"
    date: "2026-05-07"
    role: corroborating
  - url: "https://github.com/glpi-project/glpi/security/advisories/GHSA-cg63-qchq-q626"
    publisher: "GLPI"
    role: corroborating
  - url: "https://github.com/glpi-project/glpi/security/advisories/GHSA-2fg5-jg72-h338"
    publisher: "GLPI"
    role: corroborating
  - url: "https://github.com/glpi-project/glpi/security/advisories/GHSA-w7mr-3vwm-2j22"
    publisher: "GLPI"
    role: corroborating
  - url: "https://github.com/glpi-project/glpi/security/advisories/GHSA-hwjc-8228-55x4"
    publisher: "GLPI"
    role: corroborating
  - url: "https://github.com/glpi-project/glpi/security/advisories/GHSA-rhmv-j773-4gvh"
    publisher: "GLPI"
    role: corroborating
  - url: "https://github.com/glpi-project/glpi/security/advisories/GHSA-jf72-cvjh-px5w"
    publisher: "GLPI"
    role: corroborating
  - url: "https://github.com/glpi-project/glpi/security/advisories/GHSA-58j6-94cf-gcx5"
    publisher: "GLPI"
    role: corroborating
closed_sources: []
evidence: []
verification: single-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
techniques: [T1190, T1059.007]
classification:
  reliability: A
  credibility: 2
migrated_from: briefs/2026-05-08.md
updates:
  - at: "2026-10-11T14:17:26Z"
    run_id: 2026-10-11T1307Z-audit
    type: correction
    summary: >
      The vulnerability classes were wrong for six of the seven CVEs: none is an SSRF, a policy bypass or a data-integrity flaw, and none is a reflected XSS. GLPI's release notes give three stored XSS flaws, file and item deletion, file access and a form-structure export. CERT-FR's advisory is dated 2026-05-07, not 2026-04-29, which is the vendor release date. The GLPI release notes become the primary sources, each CVE gets its own class, branch and severity, an unsourced deployment claim is removed, and the priority moves to routine. GLPI's per-CVE advisories do carry CVSS 4.0 scores, from 5.1 to 8.4, which replace the statement that none were published; the takeaway scopes the stored XSS risk to the privileged accounts the advisories require. All seven per-CVE advisories are cited for the scores.
    fields: [title, headline, summary, event_date, priority, cves, techniques, sources, verification, classification, body]
---

GLPI released versions 11.0.7 and 10.0.25 on 2026-04-29 as security releases ([GLPI, 2026-04-29](https://github.com/glpi-project/glpi/releases/tag/11.0.7)) ([GLPI, 2026-04-29](https://github.com/glpi-project/glpi/releases/tag/10.0.25)). The CVE-assigned fixes are three stored cross-site scripting flaws rated High, in the knowledge base (CVE-2026-5385, both branches), in ITIL costs (CVE-2026-40108, 11.x) and in asset locks (CVE-2026-42321, 10.x); arbitrary file deletion by a technician (CVE-2026-42317, High) and arbitrary item deletion via planning (CVE-2026-42318, High); arbitrary file access (CVE-2026-42320, Medium); and an unauthorized export of form structure (CVE-2026-32312, Medium, 11.x) ([GLPI, 2026-04-29](https://github.com/glpi-project/glpi/releases/tag/11.0.7)) ([GLPI, 2026-04-29](https://github.com/glpi-project/glpi/releases/tag/10.0.25)). GLPI's per-CVE advisories score the seven flaws from 5.1 to 8.4 under CVSS 4.0 ([GLPI, GHSA-cg63-qchq-q626](https://github.com/glpi-project/glpi/security/advisories/GHSA-cg63-qchq-q626)) ([GLPI, GHSA-2fg5-jg72-h338](https://github.com/glpi-project/glpi/security/advisories/GHSA-2fg5-jg72-h338)) ([GLPI, GHSA-w7mr-3vwm-2j22](https://github.com/glpi-project/glpi/security/advisories/GHSA-w7mr-3vwm-2j22)) ([GLPI, GHSA-hwjc-8228-55x4](https://github.com/glpi-project/glpi/security/advisories/GHSA-hwjc-8228-55x4)) ([GLPI, GHSA-rhmv-j773-4gvh](https://github.com/glpi-project/glpi/security/advisories/GHSA-rhmv-j773-4gvh)) ([GLPI, GHSA-jf72-cvjh-px5w](https://github.com/glpi-project/glpi/security/advisories/GHSA-jf72-cvjh-px5w)) ([GLPI, GHSA-58j6-94cf-gcx5](https://github.com/glpi-project/glpi/security/advisories/GHSA-58j6-94cf-gcx5)). CERT-FR relayed the releases in CERTFR-2026-AVI-0551 on 2026-05-07, covering GLPI before 10.0.25 and before 11.0.7 ([CERT-FR, 2026-05-07](https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0551/)). No source reports exploitation.

**Exposure:** GLPI installations before 10.0.25 on the 10.x branch or before 11.0.7 on the 11.x branch ([GLPI, 2026-04-29](https://github.com/glpi-project/glpi/releases/tag/11.0.7)) ([GLPI, 2026-04-29](https://github.com/glpi-project/glpi/releases/tag/10.0.25)).

**Defender takeaway:** a standard patch-cycle upgrade; the stored XSS flaws matter most where the technician or administrator accounts that can write knowledge-base, cost or asset content are shared or weakly protected, because technicians and administrators later view that content.

## Correction — 2026-10-11T14:17:26Z

GLPI's release notes classify the seven CVEs as stored cross-site scripting (CVE-2026-5385, CVE-2026-40108, CVE-2026-42321), arbitrary file and item deletion (CVE-2026-42317, CVE-2026-42318), arbitrary file access (CVE-2026-42320) and an unauthorized export of form structure (CVE-2026-32312) ([GLPI, 2026-04-29](https://github.com/glpi-project/glpi/releases/tag/11.0.7)) ([GLPI, 2026-04-29](https://github.com/glpi-project/glpi/releases/tag/10.0.25)). The earlier text called CVE-2026-32312 an SSRF, listed four of the CVEs as stored or reflected XSS, and described CVE-2026-5385 as a policy bypass and CVE-2026-40108 as a data-integrity flaw. CERT-FR published its advisory on 2026-05-07 ([CERT-FR, 2026-05-07](https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0551/)); 2026-04-29 is the date of GLPI's releases. GLPI's per-CVE advisories do carry CVSS 4.0 scores, from 5.1 to 8.4 ([GLPI, GHSA-cg63-qchq-q626](https://github.com/glpi-project/glpi/security/advisories/GHSA-cg63-qchq-q626)) ([GLPI, GHSA-2fg5-jg72-h338](https://github.com/glpi-project/glpi/security/advisories/GHSA-2fg5-jg72-h338)), and the stored XSS risk sits with the privileged accounts that can write the affected content.
