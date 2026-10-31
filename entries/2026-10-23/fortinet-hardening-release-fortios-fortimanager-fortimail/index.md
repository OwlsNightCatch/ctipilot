---
schema: 1
kind: vulnerability
title: "Fortinet coordinated security hardening release: critical and high-severity fixes in FortiOS 8.0.2, 7.6.8, 7.4.13 and 7.2.14, FortiManager, FortiAnalyzer, FortiMail and FortiAuthenticator, with the advisories withheld until 2026-11-10"
headline: "Fortinet ships out-of-cycle critical and high fixes for FortiOS and four more products; CVEs wait until 10 November"
summary: >
  Fortinet announced on 2026-10-21 a coordinated release of critical and high-severity fixes for FortiOS, FortiManager and
  FortiAnalyzer (scheduled for 2026-10-22, after recent FortiMail and FortiAuthenticator releases), found through its
  AI-assisted testing, and urges every customer to upgrade at once, internet-facing devices first. The CVE advisories follow
  only on 2026-11-10, so there are no identifiers to triage by; NCSC.ch lists the exploitation status as unknown, and the
  FortiMail builds are the ones that already fix CVE-2026-104286, which Fortinet reports as exploited.
discovered_at: "2026-10-23T03:38:30Z"
updated_at: null
event_date: "2026-10-22"
run_id: 2026-10-23T0256Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, patch-available]
regions: [global]
sectors: []
entities: ["product:fortinet-fortios", "product:fortinet-fortimanager", "product:fortinet-fortianalyzer", "product:fortinet-fortimail", "product:fortinet-fortiauthenticator"]
techniques: [T1190]
affected_products: ["Fortinet FortiOS", "Fortinet FortiManager", "Fortinet FortiAnalyzer", "Fortinet FortiMail", "Fortinet FortiAuthenticator"]
cves: []
sources:
  - url: "https://www.fortinet.com/blog/ciso-collective/fortinet-releases-security-hardening-release-for-multiple-products"
    publisher: "Fortinet (CISO Collective blog)"
    date: "2026-10-21"
    role: primary
  - url: "https://security-hub.ncsc.admin.ch/#/posts/13092"
    publisher: "NCSC.ch Security Hub (advisory 13092)"
    date: "2026-10-22"
    role: corroborating
  - url: "https://www.heise.de/news/Ausserplanmaessige-Fortinet-Updates-Details-Fehlanzeige-aber-dringend-11497171.html"
    publisher: "heise online"
    date: "2026-10-22"
    role: corroborating
  - url: "https://fortiguard.fortinet.com/psirt/FG-IR-26-175"
    publisher: "Fortinet PSIRT (FG-IR-26-175)"
    date: "2026-10-01"
    role: corroborating
closed_sources: []
evidence:
  - quote: "We strongly urge every customer to plan and promptly complete these upgrades as soon as the releases are available, prioritizing internet-facing devices."
    publisher: "Fortinet (CISO Collective blog)"
    source_url: "https://www.fortinet.com/blog/ciso-collective/fortinet-releases-security-hardening-release-for-multiple-products"
  - quote: "These releases include critical and high-severity fixes."
    publisher: "Fortinet (CISO Collective blog)"
    source_url: "https://www.fortinet.com/blog/ciso-collective/fortinet-releases-security-hardening-release-for-multiple-products"
  - quote: "public advisories will be made available at the next Patch Tuesday on November 10"
    publisher: "Fortinet (CISO Collective blog)"
    source_url: "https://www.fortinet.com/blog/ciso-collective/fortinet-releases-security-hardening-release-for-multiple-products"
verification: single-source
sourcing_note: >
  Fortinet's own post is the first-party source for the releases, the fixed versions and the disclosure schedule; NCSC.ch's
  advisory and heise restate it, so they add reach, not an independent assessment. No CVE identifiers exist yet, and Fortinet's
  tables list no row for FortiOS 7.0 or 6.4, which is not a statement about whether those branches are affected. The FortiMail
  overlap rests on a comparison of Fortinet's two published fix tables.
confidence: high
references: ["2026-10-16/peerstitch-fortigate-implant-cve-2025-61624-fortimanager", "2026-10-02/cve-2026-104286-fortimail-path-traversal-zero-day-kev"]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Upgrade every internet-facing FortiOS (8.0.2, 7.6.8, 7.4.13 or 7.2.14), FortiManager and FortiAnalyzer (8.0.2, 7.6.8, 7.4.12 or 7.2.13), FortiMail (8.0.2, 7.6.7 or 7.4.9; 7.2 moves to 7.4 or later) and FortiAuthenticator (8.0.4 or 6.6.11) now rather than in the November cycle, saving the configuration first; where the upgrade has to wait, restrict HTTPS and SSH administration to trusted addresses or disable it on external interfaces and keep FortiManager administration off the internet."
updates: []
migrated_from: null
---

Fortinet announced on 2026-10-21 a coordinated set of security updates for FortiOS, FortiManager and FortiAnalyzer, scheduled for 2026-10-22 and following recent releases for FortiMail and FortiAuthenticator ([Fortinet, 2026-10-21](https://www.fortinet.com/blog/ciso-collective/fortinet-releases-security-hardening-release-for-multiple-products)). Fortinet says the releases fix vulnerabilities found through its frontier-AI-assisted testing programme, that they include critical and high-severity fixes, and that customers should treat them as a priority change rather than routine maintenance, because AI tools can help adversaries reverse-engineer patches and build working exploits in hours or days, patch differences show where the weakness sits, and AI can chain lower-severity flaws ([Fortinet, 2026-10-21](https://www.fortinet.com/blog/ciso-collective/fortinet-releases-security-hardening-release-for-multiple-products)). The public advisories will appear only at the next Patch Tuesday, 2026-11-10 ([Fortinet, 2026-10-21](https://www.fortinet.com/blog/ciso-collective/fortinet-releases-security-hardening-release-for-multiple-products)). NCSC.ch's advisory describes the fixes as ones that might allow attackers to gain unauthorized control over affected security infrastructure and lists the current exploitation status as unknown ([NCSC.ch, 2026-10-22](https://security-hub.ncsc.admin.ch/#/posts/13092)).

Fortinet's tables name these affected and fixed versions: FortiOS 8.0.0 to 8.0.1 (fixed 8.0.2), 7.6.0 to 7.6.7 (7.6.8), 7.4.0 to 7.4.12 (7.4.13) and 7.2.0 to 7.2.13 (7.2.14); FortiManager and FortiAnalyzer 8.0.0 to 8.0.1 (8.0.2), 7.6.0 to 7.6.7 (7.6.8), 7.4.0 to 7.4.11 (7.4.12) and 7.2.0 to 7.2.12 (7.2.13); FortiMail 8.0.0 to 8.0.1 (8.0.2), 7.6.0 to 7.6.6 (7.6.7), 7.4.0 to 7.4.8 (7.4.9) and 7.2.0 to 7.2.9 (upgrade to the 7.4 branch or later); FortiAuthenticator 8.0.0 to 8.0.3 (8.0.4) and 6.6.0 to 6.6.10 (6.6.11) ([Fortinet, 2026-10-21](https://www.fortinet.com/blog/ciso-collective/fortinet-releases-security-hardening-release-for-multiple-products)). FortiSASE updates automatically, FortiManager Cloud may need a manual update, and public-cloud instances follow their cloud partners' release processes ([Fortinet, 2026-10-21](https://www.fortinet.com/blog/ciso-collective/fortinet-releases-security-hardening-release-for-multiple-products)). heise online lists the same fixed builds and the same 2026-11-10 disclosure date ([heise online, 2026-10-22](https://www.heise.de/news/Ausserplanmaessige-Fortinet-Updates-Details-Fehlanzeige-aber-dringend-11497171.html)).

The FortiMail rows are identical to the fix table of Fortinet's advisory FG-IR-26-175, an unauthenticated path traversal in the FortiMail IBE webmail service (CVE-2026-104286) that Fortinet reports as exploited in the wild ([Fortinet PSIRT, 2026-10-01](https://fortiguard.fortinet.com/psirt/FG-IR-26-175)). Those FortiMail builds therefore already fix a flaw under attack, and the post does not say whether they carry further fixes; for FortiOS, FortiManager, FortiAnalyzer and FortiAuthenticator no source states exploitation.

**Exposure:** FortiOS, FortiManager, FortiAnalyzer, FortiMail and FortiAuthenticator on a version listed above; Fortinet tells customers to inventory every FortiManager and FortiOS instance and to start with those reachable from the internet ([Fortinet, 2026-10-21](https://www.fortinet.com/blog/ciso-collective/fortinet-releases-security-hardening-release-for-multiple-products)). Its tables name no row for FortiOS 7.0 or 6.4, and the post does not say whether those branches are affected ([Fortinet, 2026-10-21](https://www.fortinet.com/blog/ciso-collective/fortinet-releases-security-hardening-release-for-multiple-products)).

**Detection:** Fortinet advises watching logs for unusual administrative access and unapproved configuration changes before and after patching, which means administrator authentication and configuration-change records on the firewalls and the management servers ([Fortinet, 2026-10-21](https://www.fortinet.com/blog/ciso-collective/fortinet-releases-security-hardening-release-for-multiple-products)). With no CVE details published, no flaw-specific indicator or post-compromise check exists yet.

**Defender takeaway:** upgrade internet-facing units first, inside the change windows of 2026-10-22 and 2026-10-23 that Fortinet suggested, after backing up configurations (FortiMail units still below the fixed builds are exposed to the exploited flaw, not only to the unknown ones); until the advisories of 2026-11-10 there is no identifier to match a scanner finding or an alert against, so the fixed-version list is the only scope statement. Where an upgrade has to wait, restrict administrative HTTPS and SSH to trusted addresses or disable them on external interfaces, keep FortiManager administration off the internet and manage devices out of band, and enforce MFA for every administrator account ([Fortinet, 2026-10-21](https://www.fortinet.com/blog/ciso-collective/fortinet-releases-security-hardening-release-for-multiple-products)).
