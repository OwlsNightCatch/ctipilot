---
schema: 1
kind: vulnerability
horizon: operational
title: "Zimbra Classic Web Client: crafted-email code execution fixed in ZCS 10.1.19, surfaced by NCSC-CH (no CVE, exploitation unknown)"
headline: "NCSC-CH flags a Zimbra Classic Web Client flaw where opening a crafted email runs script in the webmail session — patch to ZCS 10.1.19"
summary: >
  Zimbra patched a Classic Web Client security issue in ZCS 10.1.19 (2026-07-07) where a specially
  crafted email runs malicious code when opened, exposing mailbox contents, session data and account
  settings; heise describes it as stored cross-site scripting. Switzerland's NCSC-CH surfaced it in its
  own advisory on 2026-07-10 with exploitation status "unknown" and no CVE assigned. Only the legacy
  Classic Web Client is affected — the Modern Web Client is not. Public-sector and telecom Zimbra
  operators across Europe should identify Classic Web Client use and upgrade.
discovered_at: "2026-07-10T20:34:32Z"
event_date: "2026-07-07"
run_id: 2026-07-10T2009Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, patch-available]
regions: [switzerland, europe]
sectors: [public-sector, telco]
entities: []
techniques: [T1203, T1059.007, T1539]
affected_products: ["Zimbra Collaboration Suite Classic Web Client"]
cves: []
sources:
  - url: "https://blog.zimbra.com/2026/07/patch-release-update-zimbra-10-1-19/"
    publisher: "Zimbra"
    date: "2026-07-07"
    role: primary
  - url: "https://security-hub.ncsc.admin.ch/#/posts/12757"
    publisher: "NCSC-CH / GovCERT.ch"
    date: "2026-07-10"
    role: corroborating
  - url: "https://www.heise.de/news/Zimbra-Collaboration-Suite-Kritische-Luecke-macht-Classic-Web-Client-angreifbar-11356522.html"
    publisher: "heise online"
    date: "2026-07-07"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The update fixes a security issue in the Classic Web Client where a specially crafted email could run malicious code when the email is opened. If exploited, it could allow access to mailbox information, session data, or account settings."
    publisher: "Zimbra"
  - quote: "Current exploitation status: UNKNOWN"
    publisher: "NCSC-CH / GovCERT.ch"
verification: multi-source
sourcing_note: "No CVE assigned by Zimbra or NCSC-CH as of this run; NCSC-CH lists exploitation status as unknown (no confirmed in-the-wild abuse). Zimbra rates the patch severity High and deployment risk Low. Included on the strength of the home-region national authority (NCSC-CH) issuing its own advisory for the constituency; the client-side, no-CVE, unknown-exploitation profile is why confidence is medium and priority is notable, not high."
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
  - "Identify Zimbra tenants still using the Classic Web Client and upgrade to ZCS ≥ 10.1.19; as an immediate interim step, move users to the Modern Web Client, which is not affected."
  - "Prioritise internet-facing Zimbra webmail — the flaw is unauthenticated and triggers on message open, so exposure is proportional to who can send mail to affected mailboxes."
migrated_from: null
---

Zimbra released ZCS 10.1.19 on 2026-07-07 to fix a Classic Web Client issue in which "a specially crafted email could run malicious code when the email is opened," potentially granting access to mailbox information, session data or account settings ([Zimbra, 2026-07-07](https://blog.zimbra.com/2026/07/patch-release-update-zimbra-10-1-19/)); heise online covered it the same day as a stored cross-site-scripting flaw in the legacy webmail UI ([heise online, 2026-07-07](https://www.heise.de/news/Zimbra-Collaboration-Suite-Kritische-Luecke-macht-Classic-Web-Client-angreifbar-11356522.html)). Switzerland's NCSC-CH added the item to its Cyber Security Hub on 2026-07-10, describing it as allowing unauthenticated remote attackers to reach session data, account settings and mailbox contents when a victim opens a malicious email, and explicitly recording the exploitation status as unknown ([NCSC-CH / GovCERT.ch, 2026-07-10](https://security-hub.ncsc.admin.ch/#/posts/12757)). Only the Classic Web Client is affected; Zimbra and heise recommend switching users to the Modern Web Client as an interim mitigation.

**Defender takeaway:** the observable behavior is client-side script execution inside an authenticated webmail session triggered by message rendering — in webmail/application logs and browser telemetry, watch for anomalous outbound requests or session-token access originating from the webmail origin immediately after a message is opened, and for mailbox operations (rule creation, forwarding, bulk reads) that follow such a sequence. **Triage:** legitimate HTML mail renders inline content routinely, so a single rendered message is not the signal; the discriminator is script execution that reaches the session store or drives mailbox/account-setting changes rather than merely displaying content. The honest caveats are that no CVE has been assigned and no exploitation has been confirmed — the actionable reason to move now is that a national authority for the constituency chose to publish it and the affected surface is an unauthenticated, on-open path in a webmail platform still used across European public-sector and telecom environments.
