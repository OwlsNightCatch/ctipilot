---
schema: 1
kind: threat
horizon: operational
title: "LAUNDRY BEAR's Zimbra zero-click, unpacked: ZimReaper's CSS-@import sanitizer bypass and an app-password that survives a password reset"
headline: "Proofpoint adds the mechanics the Zimbra joint advisory omitted — including a persistence trick patching doesn't remove"
summary: >
  Proofpoint's writeup of the LAUNDRY BEAR (TA488/Void Blizzard) Zimbra CVE-2025-66376 campaign adds the
  technical mechanics the 16-nation joint advisory did not spell out: the CSS-@import sanitizer-bypass-by-
  reassembly that reconstructs an executing <svg onload=eval(atob(...))>, DNS-tunnelled exfiltration, and a
  persistent "ZimbraWeb" application-specific password created via the SOAP API that survives both a user
  password reset and the CVE-2025-66376 patch.
discovered_at: "2026-07-25T04:38:26Z"
event_date: "2026-07-23"
run_id: 2026-07-25T0409Z-intel
priority: notable
immediate_action: null
tags: [nation-state, espionage, russia-nexus, zero-click, identity, phishing]
regions: [europe, global]
sectors: [public-sector, defense, energy]
entities: [actor:laundry-bear, tool:ulej-flowerbed]
techniques: [T1566, T1203, T1539, T1098, T1071.004, T1114.002]
affected_products: ["Zimbra Collaboration Suite"]
cves: []
sources:
  - url: "https://www.proofpoint.com/us/blog/threat-insight/ta488-targets-zimbra-mailservers-half-click-exploits"
    publisher: "Proofpoint Threat Research"
    date: "2026-07-23"
    role: primary
  - url: "https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-204a"
    publisher: "CISA (joint advisory AA26-204A)"
    date: "2026-07-24"
    role: corroborating
closed_sources: []
evidence:
  - quote: "the sanitizer fails to recognize it as executable markup, while the browser successfully reconstructs `<svg onload=\"eval(atob('…'))\">` and executes it."
    publisher: "Proofpoint Threat Research"
  - quote: "Proofpoint has not observed TA458 using CVE-2025-66376, despite the group's regular access to webmail XSS zero-days."
    publisher: "Proofpoint Threat Research"
verification: multi-source
sourcing_note: "Technical-mechanics delta on the already-covered joint advisory (AA26-204A). ZimReaper is tracked in the registry as an alias of LAUNDRY BEAR's Ulej/Flowerbed tooling; Proofpoint tracks the post-exploitation credential-theft/persistence component under the ZimReaper name."
confidence: high
update_of: 2026-07-24/laundry-bear-zimbra-zero-click-cve-2025-66376
references: [2026-07-25/ta458-roundpress-webmail-zero-days-sogo-cve-2026-8496]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "On any Zimbra account touched by the CVE-2025-66376 campaign, revoke application-specific passwords via the admin console — not just reset the user password: the attacker-created 'ZimbraWeb' app-password survives a password reset and the patch and grants standalone IMAP/POP3/SMTP mailbox access."
migrated_from: null
---

**UPDATE (originally covered 2026-07-24):** The prior entry covered the 16-nation joint advisory (AA26-204A) on LAUNDRY BEAR's (TA488 / Void Blizzard) zero-click Zimbra campaign exploiting CVE-2025-66376. Proofpoint's own two-part writeup adds mechanics the advisory did not detail ([Proofpoint, 2026-07-23](https://www.proofpoint.com/us/blog/threat-insight/ta488-targets-zimbra-mailservers-half-click-exploits)).

The exploit defeats Zimbra's client-side HTML sanitizer by tag-splitting: a fake CSS `@import` directive is fragmented across HTML tags so that the sanitizer strips each `@import` sequence individually, but "the browser successfully reconstructs `<svg onload="eval(atob('…'))">` and executes it" — a sanitizer-bypass-by-reassembly, where the surviving characters rejoin into valid executing script ([Proofpoint, 2026-07-23](https://www.proofpoint.com/us/blog/threat-insight/ta488-targets-zimbra-mailservers-half-click-exploits)). The resulting payload — which Proofpoint attributes to LAUNDRY BEAR's post-exploitation tooling and names ZimReaper — steals CSRF tokens, browser-autofill credentials, 2FA scratch codes and the Zimbra version/URL, exfiltrating tokens via DNS tunneling (Base32-encoded subdomains carrying a session id and a plaintext token-type label) and mail archives via HTTP POST.

The operationally important delta is persistence: after exploitation ZimReaper issues a `CreateAppSpecificPasswordRequest` to mint a Zimbra application-specific password labelled "ZimbraWeb" that bypasses 2FA and grants IMAP/POP3/SMTP access, then exfiltrates it via DNS for direct mailbox access ([Proofpoint, 2026-07-23](https://www.proofpoint.com/us/blog/threat-insight/ta488-targets-zimbra-mailservers-half-click-exploits)). Because that credential is independent of the primary account password, it survives a password reset and the CVE-2025-66376 patch alike. **Defender takeaway:** anyone who responded to the original advisory by patching and forcing password resets has not necessarily evicted the attacker — the app-specific password must be enumerated and revoked separately. Proofpoint also assesses that the sibling GRU actor TA458 (see references) was *not* observed using CVE-2025-66376 despite its own webmail zero-day access, suggesting the exploit was allocated to TA488 by "upstream Russian intelligence taskmasters" and deconflicted between the two clusters; Proofpoint has seen no TA488 activity since February 2026. **Triage:** hunt for a Zimbra SOAP/REST call creating a new application-specific password shortly after an anomalous webmail message-render event on the same account — benign app-password provisioning is user-initiated from account settings, not API-driven immediately after a message open; anomalous DNS query volume/entropy from the mail-server host is a second, independent hook for the exfiltration channel.
