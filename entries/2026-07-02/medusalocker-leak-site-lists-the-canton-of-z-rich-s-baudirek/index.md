---
schema: 1
kind: incident
title: "MedusaLocker leak site lists the Canton of Zürich's Baudirektion — unconfirmed claim"
headline: "MedusaLocker leak site lists the Canton of Zürich's Baudirektion — unconfirmed claim"
summary: "A Swiss cantonal government department appears on a ransomware leak site. MedusaLocker's site listed the Baudirektion of the Canton of Zürich (bd.zh.ch) on 1 July, claiming 772 extracted emails — unconfirmed by the Canton and uncorroborated by any press or NCSC.ch advisory as of this run (Ransomware.live). Treat as a watch item, not a confirmed breach."
discovered_at: "2026-07-02T04:55:17Z"
event_date: 2026-07-01
run_id: 2026-07-02-6551f8c2
priority: high
immediate_action: null
tags:
  - ransomware
  - data-breach
regions:
  - switzerland
sectors:
  - public-sector
entities: []
cves: []
sources:
  - url: "https://www.ransomware.live/id/QmRAbWVkdXNhbG9ja2Vy"
    publisher: Ransomware.live
    role: primary
closed_sources: []
evidence: []
verification: single-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-07-02.md
---

The MedusaLocker ransomware group added a listing on 2026-07-01 for a victim named "Bd" with the domain **bd.zh.ch**, the domain used by the Baudirektion (Building/Construction Directorate) of the Canton of Zürich, a Swiss cantonal-government department. The group's own claim text records "772 emails extracted; Domain: bd.zh.ch," with no ransom figure or data sample published ([Ransomware.live, 2026-07-01](https://www.ransomware.live/id/QmRAbWVkdXNhbG9ja2Vy)). **This is a dark-web leak-site claim only — it is not confirmed by the Canton of Zürich or by any independent reporting.** Targeted searches for a cantonal statement, an NCSC.ch (BACS) advisory, or Swiss press coverage returned nothing in this window. The same MedusaLocker posting wave on 1 July (~22:28–22:33 UTC) also listed other European entities in immediate succession, including a French municipality — consistent with a batch-style listing rather than a single targeted disclosure. No initial-access vector or exploited product is available from the listing.

**Why it matters to us:** direct relevance to a Swiss cantonal-government reader base. Treat as an early, unconfirmed situational-awareness signal — verify against an official cantonal or NCSC.ch statement before acting, and, if you operate `*.zh.ch` infrastructure, quietly confirm whether the Baudirektion or shared cantonal services were affected. No defender action beyond monitoring is warranted on an unverified leak-site claim.
