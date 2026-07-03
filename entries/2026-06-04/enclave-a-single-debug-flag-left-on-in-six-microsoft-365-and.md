---
schema: 1
kind: research
horizon: operational
title: "Enclave: a single debug flag left on in six Microsoft 365 Android apps allowed silent OAuth-token theft"
headline: "Enclave: a single debug flag left on in six Microsoft 365 Android apps allowed silent OAuth-token theft"
summary: "Researchers at Enclave found a shared Android SDK across six Microsoft 365 apps shipped setIsDebugMode(true) in production, disabling the AccountManager check that restricts token sharing to trusted Microsoft apps — so any co-installed third-party app could silently obtain long-lived OAuth tokens for the signed-in …"
discovered_at: "2026-06-04T05:00:10Z"
event_date: 2026-06-03
run_id: 2026-06-04-51b23ffa
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - identity
  - mobile
  - cloud
  - patch-available
regions:
  - global
sectors:
  - public-sector
entities: []
cves:
  - id: CVE-2026-42832
    cvss: "7.7"
    epss: null
    type: null
    vector: local
    auth: post-auth
    status:
      - patch-available
  - id: CVE-2026-41101
    cvss: "7.1"
    epss: null
    type: null
    vector: local
    auth: post-auth
    status:
      - patch-available
  - id: CVE-2026-41102
    cvss: "7.1"
    epss: null
    type: null
    vector: local
    auth: post-auth
    status:
      - patch-available
  - id: CVE-2026-41100
    cvss: "4.4"
    epss: null
    type: null
    vector: local
    auth: post-auth
    status:
      - patch-available
sources:
  - url: "https://www.securityweek.com/exclusive-how-one-line-of-code-put-billions-of-microsoft-android-app-downloads-at-risk/"
    publisher: SecurityWeek (exclusive)
    role: primary
  - url: "https://thehackernews.com/2026/06/microsoft-365-android-apps-let-any-app.html"
    publisher: The Hacker News
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
migrated_from: briefs/2026-06-04.md
---

Researchers at Enclave found a shared Android SDK across six Microsoft 365 apps shipped `setIsDebugMode(true)` in production, disabling the AccountManager check that restricts token sharing to trusted Microsoft apps — so any co-installed third-party app could silently obtain long-lived OAuth tokens for the signed-in Microsoft identity with no prompt ([SecurityWeek, 2026-06-02](https://www.securityweek.com/exclusive-how-one-line-of-code-put-billions-of-microsoft-android-app-downloads-at-risk/) · [The Hacker News, 2026-06-03](https://thehackernews.com/2026/06/microsoft-365-android-apps-let-any-app.html)). Affected: Word (CVE-2026-41101), PowerPoint (CVE-2026-41102), Excel (CVE-2026-42832), Microsoft 365 Copilot (CVE-2026-41100), Loop and OneNote — collectively billions of installs; Teams was unaffected because its flag was correctly `false`. Tokens granted read/write to Exchange mail, OneDrive and Calendar. Microsoft fixed all six in the 12 May 2026 cycle; no ITW reported pre-patch. Enforce minimum-version compliance for these apps via Intune/MDM on BYOD fleets and, where logs exist, review AccountManager token requests from non-Microsoft packages.
