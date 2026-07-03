---
schema: 1
kind: annual-report
horizon: strategic
weekly_section: weekly-annual-reports
title: Mandiant M-Trends 2026
headline: Mandiant M-Trends 2026
summary: "M-Trends 2026 (published 2026-03-23, first covered 2026-05-07) reinforces three cross-cutting trends visible in this week's incidents: voice phishing surged to the second most prevalent initial-access vector at 11% (overtaking email phishing at 6%) driven by IT help-desk impersonation and SaaS OAuth token theft …"
discovered_at: "2026-05-04T05:00:26Z"
event_date: 2026-05-07
run_id: 2026-W19-a5788b22
priority: notable
immediate_action: null
tags:
  - nation-state
  - espionage
  - ransomware
regions:
  - global
sectors: []
entities:
  - "report:mtrends-2026"
  - "campaign:cl-sta-1132"
  - "actor:embargo"
  - "actor:akira"
cves: []
sources:
  - url: "https://cloud.google.com/blog/topics/threat-intelligence/m-trends-2026"
    publisher: Google Cloud / Mandiant — M-Trends 2026
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
migrated_from: briefs/weekly/2026-W19.md
---

M-Trends 2026 (published 2026-03-23, first covered 2026-05-07) reinforces three cross-cutting trends visible in this week's incidents: voice phishing surged to the second most prevalent initial-access vector at 11% (overtaking email phishing at 6%) driven by IT help-desk impersonation and SaaS OAuth token theft — directly evidenced this week in the ADT vishing → Okta SSO → Salesforce pivot and in MuddyWater's Teams external-access helpdesk pretext (§ 7); ransomware initial access via prior compromise doubled to 30% — implicit in the access-broker / ransomware-affiliate model behind Akira, Embargo, and Qilin's targeting of European victims; and edge-device persistence on VPNs, routers, and network appliances without EDR coverage remains the dominant initial-access technique for state-sponsored espionage — directly mirrored in CL-STA-1132's PAN-OS exploitation and in Ivanti EPMM's named EU victims. The reframe IOCTA does not give but M-Trends does: median dwell time globally has *increased* to 14 days (up from 11 in 2024) and espionage-focused intrusions average 122-day median dwell — i.e. when the Ivanti EPMM and PAN-OS post-compromise hunting horizons land on retrospective log review back to March/April, that horizon is consistent with Mandiant's observed espionage dwell envelope. ([Google Cloud / Mandiant M-Trends 2026, 2026-03-23](https://cloud.google.com/blog/topics/threat-intelligence/m-trends-2026); [daily 2026-05-07](/briefs/2026-05-07/)).
