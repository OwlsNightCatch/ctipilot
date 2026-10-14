---
schema: 1
kind: vulnerability
title: "Adobe October 2026 bulletins: unauthenticated CVSS 9.0 to 10.0 flaws, most leading to code execution, in ColdFusion (APSB26-144), Experience Manager (APSB26-152) and Commerce and Magento (APSB26-153), none reported exploited"
headline: "Adobe fixes unauthenticated CVSS 10.0 flaws in ColdFusion, Experience Manager and Commerce; no exploitation known"
summary: >
  Adobe's 2026-10-13 bulletins fix five unauthenticated network flaws at CVSS 9.0 to 10.0 in ColdFusion 2025 and 2023 (fixed in 2025.0.14 and 2023.0.26), three unauthenticated CVSS 10.0 code-execution flaws in Experience Manager (Cloud Service 2026.9.28386 or per-issue hotfixes) and two code-execution flaws (CVSS 10.0 and 9.8) in Adobe Commerce and Magento Open Source (2026-oct builds). Adobe says it knows of no exploitation of any of them; each needs no account, so exposure rather than exploitation status decides the order.
discovered_at: "2026-10-14T03:41:00Z"
updated_at: null
event_date: "2026-10-13"
run_id: 2026-10-14T0255Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, rce, pre-auth, patch-available]
regions: [global]
sectors: [technology]
entities: ["product:adobe-coldfusion", "product:adobe-commerce", "product:adobe-experience-manager", "product:magento-open-source"]
techniques: [T1190]
affected_products: ["Adobe ColdFusion", "Adobe Experience Manager", "Adobe Commerce", "Magento Open Source"]
cves:
  - id: CVE-2026-105899
    cvss: "10.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "ColdFusion 2025 up to 2025.0.13, 2023 up to 2023.0.25"
    fixed: "2025.0.14, 2023.0.26"
  - id: CVE-2026-106622
    cvss: "10.0"
    epss: null
    type: ssrf
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "ColdFusion 2025 up to 2025.0.13, 2023 up to 2023.0.25"
    fixed: "2025.0.14, 2023.0.26"
  - id: CVE-2026-106624
    cvss: "9.8"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "ColdFusion 2025 up to 2025.0.13, 2023 up to 2023.0.25"
    fixed: "2025.0.14, 2023.0.26"
  - id: CVE-2026-106621
    cvss: "9.1"
    epss: null
    type: priv-esc
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "ColdFusion 2025 up to 2025.0.13, 2023 up to 2023.0.25"
    fixed: "2025.0.14, 2023.0.26"
  - id: CVE-2026-106619
    cvss: "9.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "ColdFusion 2025 up to 2025.0.13, 2023 up to 2023.0.25"
    fixed: "2025.0.14, 2023.0.26"
  - id: CVE-2026-90532
    cvss: "10.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "AEM Cloud Service 2026.9.28187 and earlier, AEM 6.5 up to Service Pack 25, AEM 6.5 LTS up to Service Pack 3"
    fixed: "Cloud Service 2026.9.28386; per-issue hotfixes on 6.5 Service Pack 25 and 6.5 LTS Service Pack 3"
  - id: CVE-2026-48383
    cvss: "10.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "AEM Cloud Service 2026.9.28187 and earlier, AEM 6.5 up to Service Pack 25, AEM 6.5 LTS up to Service Pack 3"
    fixed: "Cloud Service 2026.9.28386; per-issue hotfixes on 6.5 Service Pack 25 and 6.5 LTS Service Pack 3"
  - id: CVE-2026-48382
    cvss: "10.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "AEM Cloud Service 2026.9.28187 and earlier, AEM 6.5 up to Service Pack 25, AEM 6.5 LTS up to Service Pack 3"
    fixed: "Cloud Service 2026.9.28386; per-issue hotfixes on 6.5 Service Pack 25 and 6.5 LTS Service Pack 3"
  - id: CVE-2026-103849
    cvss: "10.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Adobe Commerce 2.4.4 to 2.4.9 and Magento Open Source 2.4.6 to 2.4.9, builds up to the 2026-sep release"
    fixed: "2026-oct builds (Magento Open Source: 2.4.9, 2.4.8 and 2.4.7 only)"
  - id: CVE-2026-92909
    cvss: "9.8"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Adobe's note for this CVE reads B2B and the bulletin gives no per-CVE product mapping; the bulletin lists Adobe Commerce 2.4.4 to 2.4.9, Magento Open Source 2.4.6 to 2.4.9 and Adobe Commerce B2B 1.3.3 to 1.5.3 as affected, builds up to the 2026-sep release"
    fixed: "the 2026-oct builds the bulletin lists per product (Magento Open Source: 2.4.9, 2.4.8 and 2.4.7 only; Adobe Commerce B2B: 1.5.3, 1.5.2, 1.4.2, 1.3.4 and 1.3.3 2026-oct builds)"
sources:
  - url: "https://www.adobe.com/trust/security/products/coldfusion/apsb26-144"
    publisher: "Adobe"
    date: "2026-10-13"
    role: primary
  - url: "https://www.adobe.com/trust/security/products/experience-manager/apsb26-152"
    publisher: "Adobe"
    date: "2026-10-13"
    role: primary
  - url: "https://www.adobe.com/trust/security/products/commerce/apsb26-153"
    publisher: "Adobe"
    date: "2026-10-13"
    role: primary
closed_sources: []
evidence: []
verification: single-source
sourcing_note: "Adobe is the only source; it is the vendor and the disclosing party for its own products. Adobe's ColdFusion summary calls the update priority 2 while its solution table rates both fixes priority 1."
confidence: high
references:
  - 2026-08-28/adobe-august-2026-coldfusion-campaign-classic-cvss10
  - 2026-09-08/stylesmuggler-cve-2026-75650-magento-adobe-commerce-rce
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Update every internet-facing ColdFusion server to 2025.0.14 or 2023.0.26, every AEM instance to Cloud Service 2026.9.28386 or the per-issue hotfixes for 6.5 Service Pack 25 and 6.5 LTS Service Pack 3, and Adobe Commerce and Magento Open Source to the 2026-oct build of the installed 2.4.x line (together with the CVE-2026-75650 hotfix from the September APSB26-146 update where it is missing); Magento Open Source 2.4.6 has no listed fix."
updates: []
migrated_from: null
---

Adobe's 2026-10-13 bulletins put critical fixes into three server products: ColdFusion, Experience Manager and Commerce. Adobe says it is not aware of any exploits in the wild for the ColdFusion issues ([Adobe ColdFusion APSB26-144, 2026-10-13](https://www.adobe.com/trust/security/products/coldfusion/apsb26-144)). ColdFusion 2025 up to 2025.0.13 and 2023 up to 2023.0.25 are affected and 2025.0.14 and 2023.0.26 fix them; the bulletin lists five network flaws that need no privileges at CVSS 9.0 or above: an unrestricted file upload leading to arbitrary code execution (CVE-2026-105899, 10.0), a server-side request forgery rated privilege escalation (CVE-2026-106622, 10.0), an input-validation flaw leading to code execution (CVE-2026-106624, 9.8), a code injection rated privilege escalation (CVE-2026-106621, 9.1) and a further input-validation code-execution flaw (CVE-2026-106619, 9.0, high complexity), besides code-execution flaws that need a low-privileged account at 9.9 ([Adobe ColdFusion APSB26-144, 2026-10-13](https://www.adobe.com/trust/security/products/coldfusion/apsb26-144)).

Experience Manager APSB26-152 covers Cloud Service 2026.9.28187 and earlier, 6.5 up to Service Pack 25 and 6.5 LTS up to Service Pack 3: three incorrect-authorization flaws that lead to arbitrary code execution are scored 10.0 with no privileges required (CVE-2026-90532, CVE-2026-48383, CVE-2026-48382), fixed by Cloud Service 2026.9.28386 and, on 6.5 and 6.5 LTS, by per-issue hotfixes, and Adobe is not aware of exploits of these either ([Adobe Experience Manager APSB26-152, 2026-10-13](https://www.adobe.com/trust/security/products/experience-manager/apsb26-152)). Commerce and Magento APSB26-153 fixes a template-engine injection leading to code execution (CVE-2026-103849, 10.0, which Adobe marks as needing no authentication) and an incorrect-authorization code-execution flaw (CVE-2026-92909, 9.8, which Adobe's note tags B2B) in builds up to the 2026-sep release; the fixes are the 2026-oct builds, Adobe Commerce B2B has its own 2026-oct builds, Magento Open Source gets them for 2.4.9, 2.4.8 and 2.4.7, and Adobe asks customers to apply the CVE-2026-75650 hotfix from its September APSB26-146 update as well, and Adobe is likewise not aware of exploits ([Adobe Commerce APSB26-153, 2026-10-13](https://www.adobe.com/trust/security/products/commerce/apsb26-153)).

**Exposure:** ColdFusion 2025 and 2023, Experience Manager Cloud Service, 6.5 and 6.5 LTS, and Adobe Commerce or Magento Open Source 2.4.x that untrusted networks can reach; none of the flaws named by CVE id above needs an account.

**Detection:** Adobe publishes no exploit behavior. As an inference from the flaw classes: after unexpected requests to upload or administrative endpoints, look for new script files in web-accessible directories (the upload flaw), and for outbound requests from the application server to internal addresses (the request forgery).

**Defender takeaway:** update internet-facing ColdFusion, Experience Manager and Commerce or Magento instances first, because the flaws need no login and the order is set by exposure; Adobe reports no exploitation as of 2026-10-13.
