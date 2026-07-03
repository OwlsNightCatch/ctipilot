---
schema: 1
kind: policy
horizon: strategic
weekly_section: weekly-policy
title: Poland NIS2 transposition in force 3 April 2026 — water-sector essential-entity status would now apply to the ABW-named facilities
headline: Poland NIS2 transposition in force 3 April 2026 — water-sector essential-entity status would now apply to the ABW-named facilities
summary: "Poland's amended National Cybersecurity System Act (UKSC) entered into force on 3 April 2026, implementing NIS2 with a full compliance deadline of 3 April 2027 and first audit deadline 3 April 2028 (Addleshaw Goddard, 2026-02-26 · SecurityWeek, 2026-05-08)."
discovered_at: "2026-05-04T05:00:51Z"
event_date: 2026-05-08
run_id: 2026-W19-a5788b22
priority: notable
immediate_action: null
tags:
  - law-enforcement
  - ot-ics
  - eu-nexus
regions:
  - europe
sectors:
  - water
  - public-sector
entities: []
cves: []
sources:
  - url: "https://www.addleshawgoddard.com/en/insights/insights-briefings/2026/technology/nis2-directive-finally-implemented-poland-what-businesses-need-know/"
    publisher: Addleshaw Goddard — NIS2 implemented in Poland
    role: primary
  - url: "https://www.securityweek.com/polish-security-agency-reports-ics-breaches-at-five-water-treatment-plants/"
    publisher: SecurityWeek — Polish security agency reports ICS breaches
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
migrated_from: briefs/weekly/2026-W19.md
---

Poland's amended National Cybersecurity System Act (UKSC) entered into force on **3 April 2026**, implementing NIS2 with a full compliance deadline of 3 April 2027 and first audit deadline 3 April 2028 ([Addleshaw Goddard, 2026-02-26](https://www.addleshawgoddard.com/en/insights/insights-briefings/2026/technology/nis2-directive-finally-implemented-poland-what-businesses-need-know/) · [SecurityWeek, 2026-05-08](https://www.securityweek.com/polish-security-agency-reports-ics-breaches-at-five-water-treatment-plants/)). "Drinking water supply and distribution" and "wastewater management" are now designated essential-entity sectors in Polish law — meaning the five municipal water treatment facilities ABW documented as breached during 2025 (Jabłonna Lacka, Szczytno, Małdyty, Tolkmicko, Sierakowo; § 4 / § 7) would, if attacked today, fall under NIS2 incident-reporting obligations. The attack vectors ABW attributes to APT28 / APT29 / UNC1151 (default credentials, internet-exposed ICS) are addressable by NIS2 Article 21 minimum security measures. The remaining policy gap: the breached small municipal operators are precisely the sub-threshold entities whose NIS2 coverage status is borderline under size-cap rules; the EC's NIS2 amendment introduces a "small mid-cap" important-entity category but does not resolve this specific small-municipality water-supply gap (member-state discretion). **What defenders need to do differently:** OT environments in small Polish municipalities with recently-transposed NIS2 obligations should treat the UKSC registration deadline (3 October 2026) as the immediate action item, and the 2025 ABW-documented attack vectors as the first patch-sprint target. For Swiss / EU operators reading: the ABW recommendation to extend essential-entity coverage below headcount threshold is now backed by both a documented compromise pattern *and* a freshly-transposed national NIS2 framework.
