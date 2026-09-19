---
schema: 1
kind: vulnerability
title: "Adobe Campaign Classic APSB26-120 — three more unauthenticated CVSS 10.0 code-execution flaws, and last week's build 9398 is the version they affect"
headline: "Adobe ships a second Campaign Classic emergency fix in five days — build 9398 was the patch, and build 9398 is vulnerable"
summary: >
  Adobe published APSB26-120 on 2026-08-03 for seven flaws in on-premise Adobe Campaign Classic v7, fixed in
  ACC v7 7.4.3 build 9399. Three are unauthenticated, no-interaction CVSS 10.0 paths to arbitrary code
  execution — an SSRF (CVE-2026-48331), a template-engine injection (CVE-2026-48323) and a SQL injection
  (CVE-2026-48330) — and the affected range is "7.4.3 build 9398 and earlier", meaning the build Adobe shipped
  five days earlier to fix the previous critical wave. NCSC-NL states this is not an update of that advisory
  but a separate set of newly found flaws. Adobe reports no exploitation; on-premise and hybrid only.
discovered_at: "2026-08-07T04:41:00Z"
event_date: "2026-08-03"
run_id: 2026-08-07T0411Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, rce, pre-auth, sqli, priv-esc, patch-available]
regions: [global, europe]
sectors: [public-sector, finance, telco]
entities: ["trend:adobe-coldfusion-campaign-apsb26-68-69"]
techniques: [T1190, T1059]
affected_products: ["Adobe Campaign Classic"]
cves:
  - id: CVE-2026-48331
    cvss: "10.0"
    epss: null
    type: ssrf
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "ACC v7: 7.4.3 build 9398 and earlier"
    fixed: "ACC v7 7.4.3 build 9399"
  - id: CVE-2026-48323
    cvss: "10.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "ACC v7: 7.4.3 build 9398 and earlier"
    fixed: "ACC v7 7.4.3 build 9399"
  - id: CVE-2026-48330
    cvss: "10.0"
    epss: null
    type: sqli
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "ACC v7: 7.4.3 build 9398 and earlier"
    fixed: "ACC v7 7.4.3 build 9399"
  - id: CVE-2026-48326
    cvss: "9.9"
    epss: null
    type: sqli
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "ACC v7: 7.4.3 build 9398 and earlier"
    fixed: "ACC v7 7.4.3 build 9399"
  - id: CVE-2026-48333
    cvss: "9.8"
    epss: null
    type: priv-esc
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "ACC v7: 7.4.3 build 9398 and earlier"
    fixed: "ACC v7 7.4.3 build 9399"
  - id: CVE-2026-48317
    cvss: "9.6"
    epss: null
    type: rce
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "ACC v7: 7.4.3 build 9398 and earlier"
    fixed: "ACC v7 7.4.3 build 9399"
  - id: CVE-2026-48399
    cvss: "7.5"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "ACC v7: 7.4.3 build 9398 and earlier"
    fixed: "ACC v7 7.4.3 build 9399"
sources:
  - url: "https://helpx.adobe.com/security/products/campaign/apsb26-120.html"
    publisher: "Adobe PSIRT"
    date: "2026-08-03"
    role: primary
  - url: "https://advisories.ncsc.nl/2026/ncsc-2026-0278.html"
    publisher: "NCSC-NL"
    date: "2026-08-06"
    role: corroborating
  - url: "https://helpx.adobe.com/security/products/campaign/apsb26-114.html"
    publisher: "Adobe PSIRT (APSB26-114)"
    date: "2026-07-29"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Adobe is not aware of any exploits in the wild for any of the issues addressed in these updates."
    publisher: "Adobe PSIRT"
  - quote: "This security bulletin applies only to fully on-premise deployments of Adobe Campaign Classic and to the on-premise components of hybrid deployments."
    publisher: "Adobe PSIRT"
verification: multi-source
sourcing_note: >
  CVE-to-CWE-to-impact-to-CVSS mapping is transcribed from Adobe's own per-CVE table in APSB26-120, not
  inferred by position. Two other parties characterise CVE-2026-48331 differently from Adobe: NVD's description
  and NCSC-NL's advisory both describe the SSRF as enabling privilege escalation, where Adobe's own table
  records arbitrary code execution at CVSS 10.0. The vendor bulletin is the authority for its own product and is
  what this entry follows, but the disagreement is two-to-one against it on wording and is recorded here and in
  the run record rather than smoothed over. NCSC-NL surfaced the bulletin into this window and states explicitly
  that it is not an update of its earlier advisory for APSB26-114.
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Upgrade on-premise Adobe Campaign Classic to ACC v7 7.4.3 build 9399 — build 9398, applied as the fix for APSB26-114 on 2026-07-29, is inside the affected range for all seven of these flaws."
migrated_from: null
---

Five days after Adobe fixed two critical unauthenticated flaws in Campaign Classic with build 9398 — APSB26-114, dated 2026-07-29, also a Priority 1 update ([Adobe PSIRT, 2026-07-29](https://helpx.adobe.com/security/products/campaign/apsb26-114.html)) — it published a second bulletin whose affected range includes build 9398. APSB26-120, dated 2026-08-03, covers seven vulnerabilities in the on-premise campaign-management platform and records the affected versions as "ACC v7: 7.4.3 build 9398 and earlier", fixed in ACC v7 7.4.3 build 9399, at Adobe's highest priority rating of 1 ([Adobe PSIRT, 2026-08-03](https://helpx.adobe.com/security/products/campaign/apsb26-120.html)). Any operator who treated last week's build as the end state — which is what the previous advisory called for — is still carrying every flaw below.

Three of the seven need no authentication and no user interaction, each scored CVSS 10.0 with changed scope (`AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H`), and each independently sufficient for arbitrary code execution per Adobe's own impact column: CVE-2026-48331, a server-side request forgery (CWE-918); CVE-2026-48323, improper neutralization of special elements used in a template engine (CWE-1336); and CVE-2026-48330, a SQL injection (CWE-89). Four more carry a precondition: CVE-2026-48326 (CVSS 9.9) is a second SQL injection reaching code execution but requiring low privileges; CVE-2026-48333 (CVSS 9.8) is an incorrect-authorization flaw (CWE-863) giving unauthenticated privilege escalation; CVE-2026-48317 (CVSS 9.6) is an eval injection (CWE-95) needing low privileges; and CVE-2026-48399 (CVSS 7.5) is a violation of secure design principles (CWE-657) yielding a security-feature bypass. Adobe rates all seven Critical and states that it "is not aware of any exploits in the wild for any of the issues addressed in these updates" ([Adobe PSIRT, 2026-08-03](https://helpx.adobe.com/security/products/campaign/apsb26-120.html)). NCSC-NL relayed the bulletin on 2026-08-06 and is explicit that it is not an update of its own earlier Campaign Classic advisory but a separate set of newly found vulnerabilities ([NCSC-NL, 2026-08-06](https://advisories.ncsc.nl/2026/ncsc-2026-0278.html)).

Exposure is a question of who runs their own instance: the bulletin "applies only to fully on-premise deployments of Adobe Campaign Classic and to the on-premise components of hybrid deployments", with Adobe-hosted instances already remediated and needing no customer action ([Adobe PSIRT, 2026-08-03](https://helpx.adobe.com/security/products/campaign/apsb26-120.html)). This is the third distinct wave of critical unauthenticated code-execution-class disclosures against this product line since late June ([Adobe PSIRT, 2026-07-29](https://helpx.adobe.com/security/products/campaign/apsb26-114.html)), each at Adobe's top priority, which is itself the planning signal — a platform producing pre-auth CVSS-10.0 flaws on a roughly weekly cadence is one to move off the public internet rather than one to keep patching in place. Detection concepts, telemetry class first: with no public proof-of-concept and no reported exploitation, version state is the only reliable check, so inventory on-premise ACC instances against build 9399 rather than waiting for exploitation telemetry; where the application server's outbound traffic is logged, unexpected egress initiated by the ACC process is the observable class the SSRF would produce, and unexpected child processes spawned by the web or template-rendering service is what the template-injection and eval-injection paths would produce. Both are behavioural classes derived from the flaw types Adobe names, not from any reported intrusion — no cited source describes an actual attack against these CVEs, so nothing here should be read as a hunt for known activity. One bookkeeping change worth noting for anyone who tracks Adobe CVE counts: the bulletin states that effective 2026-08-11, Adobe may assign a single CVE identifier to internally discovered vulnerabilities sharing a severity rating and CWE category when a release includes systemic fixes, so future counts will understate flaw counts relative to this one.
