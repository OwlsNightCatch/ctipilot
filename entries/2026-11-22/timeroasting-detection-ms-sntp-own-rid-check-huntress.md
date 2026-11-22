---
schema: 1
kind: research
title: "Huntress on timeroasting: the unauthenticated MS-SNTP sweep that harvests crackable MACs for computer and trust accounts leaves no logon event, Defender for Identity raised no alert in its tests, modern Windows sends an extended authenticator Huntress now has a cracker for, and the signal that holds is a host asking a domain controller to sign for an account other than its own"
headline: "Timeroasting leaves no logon event; Huntress shows the signal that holds is a host requesting another account's RID"
summary: >
  Huntress reverse-engineered the MS-SNTP signing code on a patched Windows Server 2025 domain controller and reports that timeroasting, an unauthenticated UDP/123 request that makes a domain controller return a password-derived MAC for any computer or trust account, produces no authentication event for the targeted accounts and raised no Defender for Identity alert across eleven test runs. Modern Windows clients send a 120-byte extended authenticator that public tools could not crack; Huntress published a reference cracker and a hashcat module for it. Packet size is not a usable signal: the check that holds is a source host requesting a RID other than its own computer account, with volume as the fallback.
discovered_at: "2026-11-22T15:08:00Z"
updated_at: null
event_date: "2026-11-19"
run_id: 2026-11-22T1407Z-audit
priority: notable
immediate_action: null
tags: [identity, default-config]
regions: [global]
sectors: [technology]
entities: []
techniques: [T1110.002]
affected_products: ["Microsoft Windows Server", "Microsoft Active Directory"]
cves: []
sources:
  - url: "https://www.huntress.com/blog/detecting-timeroasting"
    publisher: "Huntress"
    date: "2026-11-19"
    role: primary
closed_sources: []
evidence:
  - quote: "Timeroasting leaves no authentication event for the targeted account."
    publisher: "Huntress"
    source_url: "https://www.huntress.com/blog/detecting-timeroasting"
  - quote: "During this testing, none of them fired on timeroasting."
    publisher: "Huntress"
    source_url: "https://www.huntress.com/blog/detecting-timeroasting"
  - quote: "Do not build on packet size."
    publisher: "Huntress"
    source_url: "https://www.huntress.com/blog/detecting-timeroasting"
verification: single-source
sourcing_note: >
  Huntress's own reverse engineering and lab tests on one patched domain controller; the technique itself is Tom Tervoort's 2023 research, which Huntress cites. No second party has reproduced the Defender for Identity result or the extended-form cracker.
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

Timeroasting abuses MS-SNTP, Microsoft's authentication extension to NTP: a client names an account by its RID, and the domain controller answers with a MAC computed with that account's password-derived key, without the client authenticating first; the reachable accounts are computer and trust accounts, and the MAC is then cracked offline with no further contact and no lockout ([Huntress, 2026-11-19](https://www.huntress.com/blog/detecting-timeroasting)). Huntress names the crackable population as image-built or never-rotated machines, hand-set trusts and non-Windows joins, and says a pre-created account still on its lowercase-name default falls instantly while a normal random machine secret would not ([Huntress, 2026-11-19](https://www.huntress.com/blog/detecting-timeroasting)).

Reading w32time.dll and netlogon.dll on a fully patched Windows Server 2025 domain controller, Huntress documents two authenticator forms: a 68-byte legacy form with an MD5 MAC, which public tools emit and hashcat cracks, and a 120-byte extended form using HMAC-SHA512, which modern Windows clients send by default and which had no public cracker ([Huntress, 2026-11-19](https://www.huntress.com/blog/detecting-timeroasting)). The patched controller answered extended-form requests that asked for the previous key, and Huntress published a reference implementation and a hashcat module for it that awaits a mode number upstream, so an extended-form capture can no longer be read as uncrackable ([Huntress, 2026-11-19](https://www.huntress.com/blog/detecting-timeroasting)). Across eleven runs over five hours, with the sensor confirmed live by a control DCSync, Defender for Identity raised no alert on the MS-SNTP traffic; its "Suspicious SAM Account Name Change" alert, which names timeroasting, fires on a sAMAccountName change (event 5136), the fingerprint of the targeted variant, not of the unauthenticated sweep ([Huntress, 2026-11-19](https://www.huntress.com/blog/detecting-timeroasting)).

**Exposure:** Windows domain controllers, which answer MS-SNTP for computer and trust accounts (Huntress tested one patched Windows Server 2025 controller, and Samba AD controllers do not implement the extended form); the accounts at risk are those whose secret is weak, hand-set or never rotated ([Huntress, 2026-11-19](https://www.huntress.com/blog/detecting-timeroasting)).

**Detection:** network and host telemetry, not authentication logs: the targeted accounts generate no 4768, 4769, 4624 or 4776 events. On the domain controller, Windows Filtering Platform audit event 5156 records w32time accepting the UDP/123 connection when that subcategory is enabled; on any other host, a process other than the time service sending UDP/123 to a domain controller is a high-signal EDR hit ([Huntress, 2026-11-19](https://www.huntress.com/blog/detecting-timeroasting)). The rule that holds for both forms and even a single packet resolves the source address to its computer account and flags a request for any other RID; a source asking for many RIDs in a short window is the weaker volumetric fallback ([Huntress, 2026-11-19](https://www.huntress.com/blog/detecting-timeroasting)).

**Triage:** packet size separates nothing on a modern fleet, where members send the 120-byte form as normal time sync and the public tools emit 68 bytes; domain controllers can legitimately request a trust account's RID during hierarchy synchronization, so they need an allowlist ([Huntress, 2026-11-19](https://www.huntress.com/blog/detecting-timeroasting)). A machine account that authenticates and then sprays shares is delegation abuse, not timeroasting ([Huntress, 2026-11-19](https://www.huntress.com/blog/detecting-timeroasting)).

**Defender takeaway:** do not treat Defender for Identity or authentication analytics as coverage; collect UDP/123 telemetry from domain controllers and build the own-RID check, and reset pre-created, image-built and hand-set computer and trust account secrets, since those are the ones a sweep can crack.
