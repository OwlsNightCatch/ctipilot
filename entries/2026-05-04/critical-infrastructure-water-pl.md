---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-sector-patterns
title: Critical infrastructure water (PL)
headline: Critical infrastructure water (PL)
summary: "Polish water-sector OT intrusions — ABW 2025 Annual Report (published 2026-05-07) names five municipal facilities (Jabłonna Lacka, Szczytno, Małdyty, Tolkmicko, Sierakowo) and formally attributes the campaign to APT28 (GRU), APT29 (SVR), and UNC1151 (Belarus-affiliated, Ghostwriter information operations). All five facilities fell below the NIS2 essential-entity threshold at intrusion time — the report explicitly highlights the coverage gap for small municipal operators. (daily 2026-05-08 first coverage · daily 2026-05-09 UPDATE with attribution + NIS2 framing)"
discovered_at: "2026-05-04T05:00:15Z"
event_date: 2026-05-09
run_id: 2026-W19-a5788b22
priority: high
immediate_action: null
tags:
  - nation-state
  - hacktivism
  - ot-ics
  - actively-exploited
  - russia-nexus
  - disinformation
regions:
  - europe
sectors:
  - water
  - public-sector
entities: []
cves: []
sources:
  - url: "https://www.securityweek.com/polish-security-agency-reports-ics-breaches-at-five-water-treatment-plants/"
    publisher: SecurityWeek — Polish security agency reports ICS breaches at five water treatment plants
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

Five Polish municipal water-treatment facilities (Jabłonna Lacka, Szczytno, Małdyty, Tolkmicko, Sierakowo) had their OT networks penetrated with pump control parameters modified; manual override at at least one site prevented service disruption ([daily 2026-05-08](/briefs/2026-05-08/)). The ABW 2025 Annual Report (published 2026-05-07) formally attributed the campaign to **APT28** (GRU) and **APT29** (SVR), with **UNC1151** (Belarusian-linked, Ghostwriter cluster) named in the same attribution discussion ([SecurityWeek — Polish security agency reports ICS breaches at five water treatment plants](https://www.securityweek.com/polish-security-agency-reports-ics-breaches-at-five-water-treatment-plants/) · [daily 2026-05-09 UPDATE](/briefs/2026-05-09/)) — materially more granular than the initial "pro-Russian hacktivist" framing. All five facilities were below the NIS2 essential-entity headcount threshold at intrusion time. Cross-cutting theme: small municipal CI operators sit below regulatory coverage but inside hostile-state targeting; Dragos's 8th annual OT YiR (§ 6) reinforces with 65 percent of assessed sites carrying insecure remote-access conditions and hidden IT/OT network paths surfacing during routine penetration tests. Swiss / EU water, energy, and utility operators should re-validate IT-OT segmentation and authentication posture on industrial-gateway and SCADA management interfaces as a direct action carried into 2026-W20.
