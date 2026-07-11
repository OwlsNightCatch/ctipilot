---
schema: 1
kind: incident
horizon: operational
title: "Dutch National Police arrest 35-year-old over AFC Ajax fan-data breach — misconfigured API access-control and shared keys exposed 300,000+ accounts and 42,000 season-ticket records"
headline: "Dutch National Police arrest 35-year-old over AFC Ajax fan-data breach — misconfigured API access-control and shared keys exposed 300,000+ accounts and 42,000"
summary: "Dutch National Police arrested a 35-year-old from Buren over the AFC Ajax data breach. Per BleepingComputer and The Record (citing the Dutch police release), the underlying API access-control flaw and shared keys exposed ~300,000 fan accounts and ~42,000 season-ticket records; Ajax filed Article 33 to the Dutch DPA following the original March 2026 disclosure (BleepingComputer, 2026-05-27; The Record, 2026-05-27; Ajax victim statement, 2026-03-25). The recurring pattern — REST/mobile-app backend with shared-key API access-control — is directly transferable to public-sector citizen portals."
discovered_at: "2026-05-28T05:00:03Z"
event_date: 2026-05-27
run_id: 2026-05-28-3e33200a
priority: high
immediate_action: null
tags:
  - data-breach
  - law-enforcement
  - identity
regions:
  - europe
sectors:
  - media
entities:
  - "incident:afc-ajax-amsterdam-arrest-2026-05-26-300k-fan-records-shared-keys-misconfigured"
cves: []
sources:
  - url: "https://www.bleepingcomputer.com/news/security/dutch-police-arrests-suspect-linked-to-ajax-football-club-hack/"
    publisher: BleepingComputer
    role: primary
  - url: "https://therecord.media/dutch-police-arrest-man-over-cyber-breach-ajax-football"
    publisher: The Record
    role: corroborating
  - url: "https://nltimes.nl/2026/05/26/man-35-arrested-hack-targeting-ajax-app-fan-data"
    publisher: NL Times
    role: corroborating
  - url: "https://english.ajax.nl/articles/information-about-data-breach-at-ajax/"
    publisher: AFC Ajax statement
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
migrated_from: briefs/2026-05-28.md
---

Dutch National Police arrested a 35-year-old man from the municipality of Buren on 2026-05-26 on suspicion of computer trespass (`computervredebreuk`) against AFC Ajax Amsterdam, following an investigation triggered by Ajax's own disclosure in late March 2026 ([BleepingComputer, 2026-05-27](https://www.bleepingcomputer.com/news/security/dutch-police-arrests-suspect-linked-to-ajax-football-club-hack/); [The Record, 2026-05-27](https://therecord.media/dutch-police-arrest-man-over-cyber-breach-ajax-football); [NL Times, 2026-05-26](https://nltimes.nl/2026/05/26/man-35-arrested-hack-targeting-ajax-app-fan-data); [AFC Ajax victim statement, 2026-03-25](https://english.ajax.nl/articles/information-about-data-breach-at-ajax/)). Investigators searched the suspect's residence and seized multiple digital storage devices. Ajax's own statement (issued at the time of the original March 2026 disclosure) attributes the breach to an unauthorised actor who accessed Ajax systems and exfiltrated data; BleepingComputer and The Record, citing the Dutch police release, report the underlying API flaw exposed more than 300,000 fan accounts and 42,000+ season-ticket holders ([BleepingComputer, 2026-05-27](https://www.bleepingcomputer.com/news/security/dutch-police-arrests-suspect-linked-to-ajax-football-club-hack/); [The Record, 2026-05-27](https://therecord.media/dutch-police-arrest-man-over-cyber-breach-ajax-football)). RTL reporting cited in BleepingComputer notes the attacker demonstrated the ability to reassign a VIP season ticket in seconds and modify stadium-ban records. Ajax filed an Article 33 GDPR notification to the Dutch Autoriteit Persoonsgegevens (AP) and a criminal complaint; the underlying gap has since been patched.

**Defender takeaway:** the recurring pattern — REST or mobile-app backend with shared API keys and weak per-object authorisation checks — is directly transferable to public-sector citizen portals (tax, transport, identity, healthcare appointment systems). Hunt hypothesis: review application logs for sequential ID enumeration on resource endpoints (`/ticket/{id}`, `/account/{id}`) from authenticated low-privilege sessions; alert on cross-account modification requests where the authenticated principal does not own the target object (textbook BOLA / IDOR signal — mapped to `T1190` Exploit Public-Facing Application and `T1078` Valid Accounts). Hardening: enforce per-object ABAC at the API gateway; rotate any "shared" backend API keys; treat the mobile/REST estate as in-scope for the same threat model as the customer web front.
