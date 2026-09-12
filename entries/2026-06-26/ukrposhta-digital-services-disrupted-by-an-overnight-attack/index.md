---
schema: 1
kind: incident
title: "Ukrposhta digital services disrupted by an overnight attack; pro-Russian hacktivists claim a prior data theft"
headline: "Ukrposhta digital services disrupted by an overnight attack; pro-Russian hacktivists claim a prior data theft"
summary: "Ukraine's national postal operator Ukrposhta confirmed on 25 June that an overnight \"hostile cyberattack\" on its IT systems disrupted its mobile app and digital services, with engineers restoring functionality through the day (The Record, 2026-06-25; New Voice of Ukraine, 2026-06-25)."
discovered_at: "2026-06-26T04:54:38Z"
event_date: 2026-06-25
run_id: 2026-06-26-6bbe4619
priority: notable
immediate_action: null
tags:
  - hacktivism
  - data-breach
  - russia-nexus
regions:
  - europe
sectors:
  - transport
  - public-sector
entities: []
cves: []
sources:
  - url: "https://therecord.media/ukraine-state-postal-operator-reports-disruption"
    publisher: The Record
    role: primary
  - url: "https://english.nv.ua/business/cyberattack-disrupts-ukrposhta-app-and-digital-services-50619276.html"
    publisher: New Voice of Ukraine
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
migrated_from: briefs/2026-06-26.md
---

Ukraine's national postal operator Ukrposhta confirmed on 25 June that an overnight "hostile cyberattack" on its IT systems disrupted its mobile app and digital services, with engineers restoring functionality through the day ([The Record, 2026-06-25](https://therecord.media/ukraine-state-postal-operator-reports-disruption); [New Voice of Ukraine, 2026-06-25](https://english.nv.ua/business/cyberattack-disrupts-ukrposhta-app-and-digital-services-50619276.html)). A pro-Russian group styling itself the "IT Army of Russia" — distinct from Ukraine's civilian IT Army — separately claimed it had breached Ukrposhta infrastructure weeks earlier and exfiltrated a user database; Recorded Future News states it could not independently verify that claim, and Ukrposhta has not confirmed any data compromise. Treat the exfiltration as an unverified leak-site-style assertion until the operator says otherwise.

**Defender takeaway:** the pattern — public service disruption timed to a hacktivist data-theft claim — is the recurring playbook against European postal, logistics and other citizen-facing public operators. The hardening lesson is structural: keep internet-facing app/API tiers segmented from back-end customer databases so a front-end outage cannot be parlayed into (or conflated with) a data-store compromise.
