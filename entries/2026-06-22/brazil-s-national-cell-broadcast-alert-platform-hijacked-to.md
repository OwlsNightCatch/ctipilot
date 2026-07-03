---
schema: 1
kind: incident
horizon: operational
title: "Brazil's national Cell Broadcast alert platform hijacked to push fake \"Extreme Alert\" messages to ~30M phones"
headline: "Brazil's national Cell Broadcast alert platform hijacked to push fake \"Extreme Alert\" messages to ~30M phones"
summary: "Brazil's national Cell Broadcast emergency-alert platform was hijacked overnight 19–20 June to push fake \"Extreme Alert\" notifications to ~30M phones across seven states, forcing the system offline. Cell Broadcast deliberately bypasses opt-outs and silent mode, so an administrative-plane compromise is a high-impact leverage point — the same EU-mandated technology underpins Switzerland's ALERTSWISS (The Next Web, 2026-06-20)."
discovered_at: "2026-06-22T04:52:27Z"
event_date: 2026-06-20
run_id: 2026-06-22-dece656d
priority: high
immediate_action: null
tags:
  - data-breach
  - disinformation
regions:
  - latam
  - europe
sectors:
  - public-sector
  - telco
  - transport
entities: []
cves: []
sources:
  - url: "https://thenextweb.com/news/brazil-civil-defense-alert-hack-misanthropy-cell-broadcast"
    publisher: The Next Web
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
migrated_from: briefs/2026-06-22.md
---

An unidentified actor gained unauthorised access to Brazil's national Cell Broadcast emergency-alert platform overnight 19–20 June 2026 and sent at least ten unauthorised "Extreme Alert" notifications — the highest-severity tier, reserved for imminent-danger events — to roughly 30 million phones across seven states ([The Next Web, 2026-06-20](https://thenextweb.com/news/brazil-civil-defense-alert-hack-misanthropy-cell-broadcast)). The Ministry of Integration and Regional Development took the platform offline at 01:30 on 20 June after confirming the intrusion; Brazil's Federal Police opened an investigation and no actor has been formally attributed (a person who claimed responsibility on X had their posts removed, but police have not confirmed the claim). The specific access vector — compromised administrative credential, API key, or platform vulnerability — has not been disclosed. Cell Broadcast is architecturally designed to bypass user opt-outs and to activate devices that are on silent, which is exactly what makes administrative-plane control of it so consequential. `[SINGLE-SOURCE]` on the primary technical detail

**Why it matters to us:** This is a demonstrator for a risk class, not a Brazil-specific story. The EU Electronic Communications Code (Directive 2018/1972) mandates Cell Broadcast-based public-warning systems across member states, and Switzerland's Federal Office for Civil Protection (BABS) runs the same technology as ALERTSWISS. The incident points at the administration interface — privileged access to the broadcast console — rather than radio-side spoofing, so operators should prioritise MFA and PAM on alert-platform admin accounts, least-privilege on broadcast-issuing roles, and anomaly detection on outbound broadcast commands (volume, severity tier, off-hours issuance). A false high-severity alert is both a public-safety and a public-trust event.
