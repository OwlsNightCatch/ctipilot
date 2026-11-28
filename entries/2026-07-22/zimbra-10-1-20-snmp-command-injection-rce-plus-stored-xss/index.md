---
schema: 1
kind: vulnerability
title: "Zimbra Collaboration Suite 10.1.20 — permanent fix for an SNMP command-injection RCE plus four stored-XSS bugs; NCSC-CH and BSI both flag the release"
headline: "Zimbra ships 10.1.20 with the permanent fix for an SNMP command-injection RCE; NCSC-CH and BSI flag it for on-prem mail operators"
summary: >
  Zimbra released Collaboration Suite (ZCS) 10.1.20 on 2026-07-20 fixing nine security issues, and both
  NCSC-CH and BSI CERT-Bund flagged it on 2026-07-21. The headline flaw is a command-injection RCE in the
  SNMP monitoring component (exploitable when SNMP notifications are enabled; first disclosed 26 June, now
  permanently fixed, no CVE assigned), alongside four Classic Web Client stored-XSS bugs and three CVE'd
  access-control/forwarding-bypass issues (CVE-2026-50055/-10631/-50054, currently RESERVED on NVD). No
  in-the-wild exploitation is reported; on-prem Zimbra remains common self-hosted webmail for CH/EU SMEs
  and public-sector bodies.
discovered_at: "2026-07-22T04:34:31Z"
event_date: "2026-07-21"
run_id: 2026-07-22T0409Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, rce, patch-available]
regions: [global]
sectors: [public-sector, technology]
entities: []
techniques: [T1190, T1059, T1114.003]
affected_products: ["Zimbra Collaboration Suite", "Zimbra Classic Web Client"]
cves:
  - id: CVE-2026-50055
    cvss: null
    epss: null
    type: info-disclosure
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "≤ 10.1.19"
    fixed: "10.1.20"
  - id: CVE-2026-10631
    cvss: null
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "≤ 10.1.19"
    fixed: "10.1.20"
  - id: CVE-2026-50054
    cvss: null
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "≤ 10.1.19"
    fixed: "10.1.20"
sources:
  - url: "https://security-hub.ncsc.admin.ch/#/posts/12782"
    publisher: "NCSC-CH Cyber Security Hub"
    date: "2026-07-21"
    role: primary
  - url: "https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2429"
    publisher: "BSI CERT-Bund (WID-SEC-2026-2429)"
    date: "2026-07-21"
    role: primary
  - url: "https://blog.zimbra.com/2026/07/patch-release-update-zimbra-10-1-20/"
    publisher: "Zimbra / Synacor"
    date: "2026-07-20"
    role: primary
  - url: "https://thehackernews.com/2026/07/zimbra-patches-critical-snmp-command.html"
    publisher: "The Hacker News"
    date: "2026-07-21"
    role: corroborating
closed_sources: []
evidence:
  - quote: "A command injection vulnerability in the SNMP monitoring component when SNMP notifications are enabled. (Permanent fix for the vulnerability disclosed in our security advisory on 26th June 2026)"
    publisher: "Zimbra / Synacor"
  - quote: "A mail forwarding restriction bypass that could allow authenticated users to exfiltrate email despite mail forwarding restrictions being enabled."
    publisher: "Zimbra / Synacor"
verification: multi-source
sourcing_note: "Release facts and the nine issue descriptions are from Zimbra's own advisory (no CVE numbers given there). BSI's advisory (WID-SEC-2026-2429) lists three assigned CVE IDs — CVE-2026-50055/-10631/-50054 — but carries no per-CVE descriptions (all three are RESERVED on NVD/MITRE with no CVSS/description). Only The Hacker News maps a specific CVE to an issue (CVE-2026-50055 = mail-forwarding bypass); the issue mapping for the other two IDs is not stated in any cited source and is left unattributed. The headline SNMP command-injection carries no CVE; Zimbra withholds specifics 'in line with industry best practices' pending patch adoption. No source reports in-the-wild exploitation."
confidence: medium
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
  - "Upgrade on-prem Zimbra to ZCS 10.1.20; where SNMP notifications are not operationally required, disable them to remove the command-injection attack surface entirely rather than relying on the still-undisclosed-detail fix."
migrated_from: null
---

Zimbra shipped Collaboration Suite (ZCS) **10.1.20** on 2026-07-20, fixing nine security issues; NCSC-CH and BSI CERT-Bund both flagged the release on 2026-07-21 ([NCSC-CH, 2026-07-21](https://security-hub.ncsc.admin.ch/#/posts/12782); [BSI CERT-Bund, 2026-07-21](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2429)). The headline flaw is a **command-injection vulnerability in Zimbra's SNMP monitoring component**, exploitable when SNMP notifications are enabled, that lets an attacker execute arbitrary OS commands on the mail server; Zimbra describes 10.1.20 as the permanent fix for a vulnerability it first disclosed in a 26 June 2026 advisory and has withheld a CVE identifier and technical specifics "in line with industry best practices" pending wider patch adoption ([Zimbra, 2026-07-20](https://blog.zimbra.com/2026/07/patch-release-update-zimbra-10-1-20/); [The Hacker News, 2026-07-21](https://thehackernews.com/2026/07/zimbra-patches-critical-snmp-command.html)). Four **stored cross-site-scripting** bugs in the Classic Web Client round out the un-CVE'd issues: malicious attachment filenames, crafted fields, and rendered attachments can each trigger script execution inside a victim's authenticated webmail session.

Three issues received CVE identifiers, listed in BSI's advisory: **CVE-2026-50055**, **CVE-2026-10631** and **CVE-2026-50054** — all three currently RESERVED on NVD/MITRE. The Hacker News maps CVE-2026-50055 to the mail-forwarding restriction bypass (letting an authenticated attacker exfiltrate mail even where forwarding restrictions are enforced) ([The Hacker News, 2026-07-21](https://thehackernews.com/2026/07/zimbra-patches-critical-snmp-command.html)); the other two correspond to the release's EWS-extension access-control and mailbox-delegation authorization fixes described in Zimbra's own advisory, but the cited sources do not state which CVE maps to which issue. The release also fixes an SSRF in Zimbra's Nextcloud integration. This is the second Zimbra security release inside two weeks, following ZCS 10.1.19's 10 July fix for a separate Classic Web Client crafted-email code-execution bug.

**Defender takeaway:** no in-the-wild exploitation is reported, but Zimbra webmail has a long history of rapid post-disclosure weaponisation, and the command-injection surface is server-side OS command execution — treat the upgrade as more urgent than the "no exploitation yet" status alone would suggest for any internet-exposed instance. Detection concept: in process-creation telemetry with parent lineage, the anchor is any child process (a shell, an interpreter) spawned by the SNMP/Swatchdog monitoring service account — that daemon should never spawn a shell, so such an event is a direct command-injection tell. For the Classic Web Client XSS issues, watch for anomalous script execution or session-token reuse immediately after a user opens an email carrying an unusual attachment filename or crafted header field.
