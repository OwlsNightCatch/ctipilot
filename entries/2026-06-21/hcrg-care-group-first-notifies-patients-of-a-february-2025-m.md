---
schema: 1
kind: incident
horizon: operational
title: HCRG Care Group first notifies patients of a February 2025 Medusa breach — 16 months on
headline: HCRG Care Group first notifies patients of a February 2025 Medusa breach — 16 months on
summary: "HCRG Care Group, described by the cited source as a major UK-based healthcare services provider, has begun notifying patients in June 2026 of a Medusa ransomware attack that occurred in February 2025 — more than 16 months after the incident (HIPAA Pulse, 2026-06-18)."
discovered_at: "2026-06-21T04:54:57Z"
event_date: 2026-06-18
run_id: 2026-06-21-2b75e32c
priority: notable
immediate_action: null
tags:
  - ransomware
  - data-breach
  - eu-nexus
regions:
  - uk
  - europe
sectors:
  - healthcare
  - public-sector
entities: []
cves: []
sources:
  - url: "https://hipaapulse.com/uk-more-than-one-year-later-hcrg-is-first-notifying-patients-of-33ec763c"
    publisher: HIPAA Pulse
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
migrated_from: briefs/2026-06-21.md
---

HCRG Care Group, described by the cited source as a major UK-based healthcare services provider, has begun notifying patients in June 2026 of a Medusa ransomware attack that occurred in February 2025 — more than 16 months after the incident ([HIPAA Pulse, 2026-06-18](https://hipaapulse.com/uk-more-than-one-year-later-hcrg-is-first-notifying-patients-of-33ec763c)). The Medusa gang publicly claimed the attack and asserted data theft at the time, and analysis of the stolen dataset circulated well before formal notifications, meaning affected individuals could have learned of their exposure from media coverage rather than from the provider. UK-GDPR sets two distinct clocks — supervisor notification within 72 hours under Article 33 and notification to affected individuals "without undue delay" under Article 34 — and a 16-month gap to individual notification is precisely the kind of timeline the latter is meant to prevent. `[SINGLE-SOURCE]`

**Defender takeaway:** The instructive gap is between the 72-hour supervisor clock and the "without undue delay" individual clock. Healthcare and public-sector data processors should document their Article 34 risk-assessment reasoning contemporaneously, because post-hoc review reliably asks why individual notification was delayed and what interim harm resulted — a question that becomes sharper for organisations with UK-GDPR exposure while the ICO itself is mid-leadership-transition (see above).
