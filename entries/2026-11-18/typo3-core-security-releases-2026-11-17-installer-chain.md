---
schema: 1
kind: vulnerability
title: "TYPO3 core security releases of 2026-11-17 (ten advisories): a low-privileged backend user can write a file into the web root and re-enable the unauthenticated installer, which creates an administrator and leads to code execution (SA-026, SA-027 Critical), and TYPO3 states that a Form Framework flaw (SA-029) is actively exploited; fixed in 14.3.12, 13.4.40, 12.4.52 ELTS, 11.5.57 ELTS and 10.4.63 ELTS"
headline: "TYPO3: backend user to installer to admin and RCE (SA-027 Critical); Form Framework flaw SA-029 exploited; update now"
summary: >
  TYPO3 published ten core advisories on 2026-11-17 for 10.0.0 to 14.3.11, fixed in 14.3.12 LTS, 13.4.40 LTS, 12.4.52 ELTS, 11.5.57 ELTS and 10.4.63 ELTS. The one rated Critical (SA-027) lets a file named FIRST_INSTALL placed in the web root re-enable the installer without authentication, which creates an administrator and leads to remote code execution, and SA-026 lets any low-privileged backend user create such a file. TYPO3 states that SA-029, a Medium information disclosure in the Form Framework that can become cross-site scripting through uploaded HTML, is known to be actively exploited, naming no actor or victim.
discovered_at: "2026-11-18T05:10:00Z"
updated_at: null
event_date: "2026-11-17"
run_id: 2026-11-18T0356Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, rce, auth-bypass, actively-exploited, patch-available]
regions: [global]
sectors: [technology]
entities: []
techniques: [T1190, T1078, T1136, T1552.001]
affected_products: ["TYPO3 CMS"]
cves:
  - id: CVE-2026-119623
    cvss: "9.4"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "TYPO3 10.0.0 to 10.4.62, 11.0.0 to 11.5.56, 12.0.0 to 12.4.51, 13.0.0 to 13.4.39, 14.0.0 to 14.3.11"
    fixed: "10.4.63 ELTS, 11.5.57 ELTS, 12.4.52 ELTS, 13.4.40 LTS, 14.3.12 LTS"
  - id: CVE-2026-119622
    cvss: "7.1"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "TYPO3 10.0.0 to 10.4.62, 11.0.0 to 11.5.56, 12.0.0 to 12.4.51, 13.0.0 to 13.4.39, 14.0.0 to 14.3.11"
    fixed: "10.4.63 ELTS, 11.5.57 ELTS, 12.4.52 ELTS, 13.4.40 LTS, 14.3.12 LTS"
  - id: CVE-2026-125160
    cvss: "6.3"
    epss: null
    type: info-disclosure
    vector: zero-click
    auth: pre-auth
    status: [exploited, patch-available]
    affected: "TYPO3 10.0.0 to 10.4.62, 11.0.0 to 11.5.56, 12.0.0 to 12.4.51, 13.0.0 to 13.4.39, 14.0.0 to 14.3.11"
    fixed: "10.4.63 ELTS, 11.5.57 ELTS, 12.4.52 ELTS, 13.4.40 LTS, 14.3.12 LTS"
  - id: CVE-2026-119621
    cvss: "7.7"
    epss: null
    type: path-traversal
    vector: zero-click
    auth: admin-required
    status: [patch-available]
    affected: "TYPO3 10.0.0 to 10.4.62, 11.0.0 to 11.5.56, 12.0.0 to 12.4.51, 13.0.0 to 13.4.39, 14.0.0 to 14.3.11"
    fixed: "10.4.63 ELTS, 11.5.57 ELTS, 12.4.52 ELTS, 13.4.40 LTS, 14.3.12 LTS"
  - id: CVE-2026-125159
    cvss: "8.2"
    epss: null
    type: info-disclosure
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "TYPO3 10.0.0 to 10.4.62, 11.0.0 to 11.5.56, 12.0.0 to 12.4.51, 13.0.0 to 13.4.39, 14.0.0 to 14.3.11"
    fixed: "10.4.63 ELTS, 11.5.57 ELTS, 12.4.52 ELTS, 13.4.40 LTS, 14.3.12 LTS"
  - id: CVE-2026-125163
    cvss: "6.3"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "TYPO3 10.0.0 to 10.4.62, 11.0.0 to 11.5.56, 12.0.0 to 12.4.51, 13.0.0 to 13.4.39, 14.0.0 to 14.3.11"
    fixed: "10.4.63 ELTS, 11.5.57 ELTS, 12.4.52 ELTS, 13.4.40 LTS, 14.3.12 LTS"
  - id: CVE-2026-125162
    cvss: "8.2"
    epss: null
    type: dos
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "TYPO3 10.0.0 to 10.4.62, 11.0.0 to 11.5.56, 12.0.0 to 12.4.51, 13.0.0 to 13.4.39, 14.0.0 to 14.3.11 with cHash validation not enforced"
    fixed: "10.4.63 ELTS, 11.5.57 ELTS, 12.4.52 ELTS, 13.4.40 LTS, 14.3.12 LTS"
  - id: CVE-2026-125164
    cvss: "6.3"
    epss: null
    type: info-disclosure
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "TYPO3 10.0.0 to 10.4.62, 11.0.0 to 11.5.56, 12.0.0 to 12.4.51, 13.0.0 to 13.4.39, 14.0.0 to 14.3.11"
    fixed: "10.4.63 ELTS, 11.5.57 ELTS, 12.4.52 ELTS, 13.4.40 LTS, 14.3.12 LTS"
  - id: CVE-2026-125161
    cvss: "5.3"
    epss: null
    type: logic-flaw
    vector: user-interaction
    auth: pre-auth
    status: [patch-available]
    affected: "TYPO3 10.0.0 to 10.4.62, 11.0.0 to 11.5.56, 12.0.0 to 12.4.51, 13.0.0 to 13.4.39, 14.0.0 to 14.3.11"
    fixed: "10.4.63 ELTS, 11.5.57 ELTS, 12.4.52 ELTS, 13.4.40 LTS, 14.3.12 LTS"
  - id: CVE-2026-125165
    cvss: "5.3"
    epss: null
    type: ssrf
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "TYPO3 14.0.0 to 14.3.11"
    fixed: "14.3.12 LTS, with HTTP/allowed_hosts/dashboard_rss configured"
sources:
  - url: "https://news.typo3.com/security/advisory/typo3-core-sa-2026-027"
    publisher: "TYPO3 Security Team (TYPO3-CORE-SA-2026-027)"
    date: "2026-11-17"
    role: primary
  - url: "https://news.typo3.com/security/advisory/typo3-core-sa-2026-026"
    publisher: "TYPO3 Security Team (TYPO3-CORE-SA-2026-026)"
    date: "2026-11-17"
    role: primary
  - url: "https://news.typo3.com/security/advisory/typo3-core-sa-2026-029"
    publisher: "TYPO3 Security Team (TYPO3-CORE-SA-2026-029)"
    date: "2026-11-17"
    role: primary
  - url: "https://news.typo3.com/security/advisory/typo3-core-sa-2026-025"
    publisher: "TYPO3 Security Team (TYPO3-CORE-SA-2026-025)"
    date: "2026-11-17"
    role: primary
  - url: "https://news.typo3.com/security/advisory/typo3-core-sa-2026-028"
    publisher: "TYPO3 Security Team (TYPO3-CORE-SA-2026-028)"
    date: "2026-11-17"
    role: primary
  - url: "https://news.typo3.com/security/advisory/typo3-core-sa-2026-030"
    publisher: "TYPO3 Security Team (TYPO3-CORE-SA-2026-030)"
    date: "2026-11-17"
    role: primary
  - url: "https://news.typo3.com/security/advisory/typo3-core-sa-2026-031"
    publisher: "TYPO3 Security Team (TYPO3-CORE-SA-2026-031)"
    date: "2026-11-17"
    role: primary
  - url: "https://news.typo3.com/security/advisory/typo3-core-sa-2026-032"
    publisher: "TYPO3 Security Team (TYPO3-CORE-SA-2026-032)"
    date: "2026-11-17"
    role: primary
  - url: "https://news.typo3.com/security/advisory/typo3-core-sa-2026-033"
    publisher: "TYPO3 Security Team (TYPO3-CORE-SA-2026-033)"
    date: "2026-11-17"
    role: primary
  - url: "https://news.typo3.com/security/advisory/typo3-core-sa-2026-034"
    publisher: "TYPO3 Security Team (TYPO3-CORE-SA-2026-034)"
    date: "2026-11-17"
    role: primary
  - url: "https://news.typo3.com/article/typo3-14312-13440-12452-11557-and-10463-security-releases-published"
    publisher: "TYPO3 release announcement"
    date: "2026-11-17"
    role: corroborating
closed_sources: []
evidence:
  - quote: "This vulnerability is known to be actively exploited."
    publisher: "TYPO3 Security Team (TYPO3-CORE-SA-2026-029)"
    source_url: "https://news.typo3.com/security/advisory/typo3-core-sa-2026-029"
  - quote: "The installer then became accessible without authentication, allowing for example to change the database connection and to create a new administrator and system maintainer account"
    publisher: "TYPO3 Security Team (TYPO3-CORE-SA-2026-027)"
    source_url: "https://news.typo3.com/security/advisory/typo3-core-sa-2026-027"
  - quote: "any authenticated, low-privileged backend user, even without file mounts or module access, could create online media files with a partially controllable file name in the public web root."
    publisher: "TYPO3 Security Team (TYPO3-CORE-SA-2026-026)"
    source_url: "https://news.typo3.com/security/advisory/typo3-core-sa-2026-026"
verification: single-source
sourcing_note: >
  TYPO3 is the disclosing party and its own CVE numbering authority; the advisory pages carry the CVSS 4.0 vectors but no scores, so the scores in the CVE records are the ones TYPO3 published with the CVE records. TYPO3 states that SA-029 is actively exploited and gives no actor, victim, number of sites or behaviour; its reporter is a member of the TYPO3 Security Team, and an automated CISA ADP record made about twenty minutes after release lists exploitation as none. SA-027 is the only advisory rated Critical.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Update every TYPO3 instance to 14.3.12, 13.4.40, 12.4.52 ELTS, 11.5.57 ELTS or 10.4.63 ELTS now, and on 14.x configure HTTP/allowed_hosts/dashboard_rss; until then check the public web root and the project root for unexpected files whose name starts with FIRST_INSTALL and the backend for administrator or system maintainer accounts nobody created, because a low-privileged backend user can re-enable the installer and TYPO3 states that one flaw in the same release is actively exploited."
updates: []
migrated_from: null
---

TYPO3 released ten core advisories on 2026-11-17, fixed in 14.3.12 LTS, 13.4.40 LTS, 12.4.52 ELTS, 11.5.57 ELTS and 10.4.63 ELTS ([TYPO3, 2026-11-17](https://news.typo3.com/article/typo3-14312-13440-12452-11557-and-10463-security-releases-published)); versions 10.0.0 to 10.4.62, 11.0.0 to 11.5.56, 12.0.0 to 12.4.51, 13.0.0 to 13.4.39 and 14.0.0 to 14.3.11 are affected ([TYPO3 SA-027, 2026-11-17](https://news.typo3.com/security/advisory/typo3-core-sa-2026-027)). SA-027 is rated Critical: placing a file whose name starts with FIRST_INSTALL in the public web root or the project root re-enables the installer on a configured instance without authentication, which allows changing the database connection and creating a new administrator and system maintainer account, and that leads to remote code execution; leftover or restored marker files also work ([TYPO3 SA-027, 2026-11-17](https://news.typo3.com/security/advisory/typo3-core-sa-2026-027)). SA-026, rated High, supplies the file: the backend endpoint for adding online media accepts a target folder in the fallback storage, which points to the public web root, so any authenticated low-privileged backend user can create media files with a partially controllable name there ([TYPO3 SA-026, 2026-11-17](https://news.typo3.com/security/advisory/typo3-core-sa-2026-026)).

TYPO3 states that SA-029, a Medium information disclosure in the Form Framework, is known to be actively exploited, and names no actor, victim or behaviour ([TYPO3 SA-029, 2026-11-17](https://news.typo3.com/security/advisory/typo3-core-sa-2026-029)). A failed upload shows the raw storage error with the upload sub-folder, so an attacker can derive the public URL of an uploaded file, and where the form accepts HTML this becomes cross-site scripting unless the web server applies TYPO3's recommended Content-Security-Policy to the upload folder ([TYPO3 SA-029, 2026-11-17](https://news.typo3.com/security/advisory/typo3-core-sa-2026-029)). SA-032 closes the matching gap, an empty allowedMimeTypes list that was treated as no restriction and let unauthenticated visitors upload HTML or SVG to a public folder ([TYPO3 SA-032, 2026-11-17](https://news.typo3.com/security/advisory/typo3-core-sa-2026-032)). SA-028 lets ImageMagick's MVG coder disclose any web-server-readable file through a processed image; it needs ImageMagick with its default configuration allowing the MVG coder, and unauthenticated visitors reach it where such an upload form exists ([TYPO3 SA-028, 2026-11-17](https://news.typo3.com/security/advisory/typo3-core-sa-2026-028)). SA-025 is an Import/Export path traversal that writes arbitrary files and needs an administrator or a user enabled for import ([TYPO3 SA-025, 2026-11-17](https://news.typo3.com/security/advisory/typo3-core-sa-2026-025)). Four lesser flaws are an incomplete open-redirect fix (SA-030), page-cache flooding where cHash validation is not enforced (SA-031), file-dump token reuse (SA-033) and an SSRF in the 14.x Dashboard RSS widget (SA-034) ([TYPO3 SA-030, 2026-11-17](https://news.typo3.com/security/advisory/typo3-core-sa-2026-030); [SA-031](https://news.typo3.com/security/advisory/typo3-core-sa-2026-031); [SA-033](https://news.typo3.com/security/advisory/typo3-core-sa-2026-033); [SA-034](https://news.typo3.com/security/advisory/typo3-core-sa-2026-034)).

**Exposure:** any TYPO3 instance on an affected version; the installer chain needs only a low-privileged backend account, and the Form Framework flaws need a public form with an upload element ([TYPO3 SA-026, 2026-11-17](https://news.typo3.com/security/advisory/typo3-core-sa-2026-026); [TYPO3 SA-032, 2026-11-17](https://news.typo3.com/security/advisory/typo3-core-sa-2026-032)).

**Detection:** files whose name starts with FIRST_INSTALL in the web root or project root, and administrator or system maintainer accounts nobody created ([TYPO3 SA-027, 2026-11-17](https://news.typo3.com/security/advisory/typo3-core-sa-2026-027)); HTML or SVG files in the form upload folder and web-server logs for direct requests to them ([TYPO3 SA-032, 2026-11-17](https://news.typo3.com/security/advisory/typo3-core-sa-2026-032)).

**Defender takeaway:** update to the fixed release of each branch now. After updating, configure at least one allowed MIME type for every upload element, because an empty list now refuses uploads ([TYPO3 SA-032, 2026-11-17](https://news.typo3.com/security/advisory/typo3-core-sa-2026-032)); on 14.x configure the dashboard_rss allowed hosts, because the update alone does not mitigate SA-034 ([TYPO3 SA-034, 2026-11-17](https://news.typo3.com/security/advisory/typo3-core-sa-2026-034)); and deliver the form upload folder with a restrictive Content-Security-Policy, which nginx needs configured by hand ([TYPO3 SA-029, 2026-11-17](https://news.typo3.com/security/advisory/typo3-core-sa-2026-029)); and, after updating, configure image formats outside the default raster set, such as psd or ppm, explicitly in fileExtensionToMimeType so ImageMagick still processes them ([TYPO3 SA-028, 2026-11-17](https://news.typo3.com/security/advisory/typo3-core-sa-2026-028)).
