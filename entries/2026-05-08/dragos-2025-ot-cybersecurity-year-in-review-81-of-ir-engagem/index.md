---
schema: 1
kind: research
title: "Dragos OT Cybersecurity Year in Review (2025 data): 81% of assessments found poor IT/OT segmentation and 73% of all-time IR cases involved compromised VPN or jump-host credentials"
headline: "Dragos: poor IT/OT segmentation in 81% of assessments, and compromised VPN or jump-host credentials involved in 73% of its all-time incident cases"
summary: "Dragos's ninth annual OT Cybersecurity Year in Review, released 2026-02-17 and summarised again on 2026-05-07, finds poor IT/OT segmentation in 81% of its assessments, compromised VPN or jump-host credentials in 73% of all-time incident cases, adequate OT monitoring in only 46% of assessments, and 119 ransomware groups hitting 3,300 industrial organisations in 2025."
discovered_at: "2026-05-08T05:00:11Z"
event_date: 2026-02-17
run_id: 2026-05-08-migrated
priority: notable
immediate_action: null
tags:
  - ot-ics
regions:
  - global
sectors: []
entities:
  - "report:dragos-2025-ot-frontlines"
techniques: [T1133, T1078]
cves: []
sources:
  - url: "https://www.dragos.com/blog/dragos-2026-ot-cybersecurity-year-in-review"
    publisher: "Dragos, Inc."
    date: "2026-02-17"
    role: primary
  - url: "https://www.dragos.com/blog/ot-cybersecurity-lessons-learned-frontlines"
    publisher: "Dragos, Inc."
    date: "2026-05-07"
    role: corroborating
closed_sources: []
evidence:
  - quote: "81 percent of assessments identified poor IT/OT segmentation. 73 percent of all-time IR cases involved compromised VPN or jumphost credentials."
    publisher: "Dragos, Inc."
verification: single-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-08.md
updates:
  - at: "2026-09-30T07:14:50Z"
    run_id: 2026-09-30T0639Z-audit
    type: correction
    summary: >
      The 81% figure was called a share of incident-response engagements, where Dragos gives it as a
      share of assessments; a Frontlines IR Edition Dragos never published was named; and figures
      and framing no Dragos page states were carried: a 62% remote-access entry vector, 34% of
      intrusions reaching the process level, NIS2 asset-inventory gaps, IEC 62443 as the reference
      architecture and a Swiss SARI link. The text is rewritten from Dragos's release post and its
      2026-05-07 follow-up, cited to those pages instead of an index. The title and headline say
      compromised credentials were involved in 73% of all-time IR cases, as Dragos writes, and the
      ransomware-misclassification sentence follows Dragos's wording.
    fields: [title, headline, summary, event_date, techniques, sources, evidence, classification, body]
---

Dragos released its ninth annual OT Cybersecurity Year in Review, covering 2025, on 2026-02-17. Its field findings: "81 percent of assessments identified poor IT/OT segmentation. 73 percent of all-time IR cases involved compromised VPN or jumphost credentials", only 46% of assessments found adequate OT network monitoring, 56% of penetration tests abused living-off-the-land tools without triggering alerts, and 30% of incident cases began with operational issues the asset owner could not explain ([Dragos, 2026-02-17](https://www.dragos.com/blog/dragos-2026-ot-cybersecurity-year-in-review)). Dragos tracked 119 ransomware groups affecting 3,300 industrial organisations in 2025, up from 80 groups in 2024, and says many incidents are mislabelled as IT incidents when Windows servers hosting SCADA software or engineering workstations are compromised, and that ransomware groups target VMware ESXi hypervisors hosting OT applications ([Dragos, 2026-02-17](https://www.dragos.com/blog/dragos-2026-ot-cybersecurity-year-in-review)). A 2026-05-07 follow-up adds that 49% of Dragos Services reports carried elevated remote-access findings and 53% identified internet-facing systems ([Dragos, 2026-05-07](https://www.dragos.com/blog/ot-cybersecurity-lessons-learned-frontlines)).

**Exposure:** OT networks reachable from enterprise IT, and remote access into OT through VPN or jump hosts protected by reusable credentials.

**Detection:** interactive logins into OT jump hosts or engineering workstations from new source addresses or outside maintenance windows, and any traffic crossing the IT/OT boundary that no documented conduit explains.

**Defender takeaway:** the two findings point at the same fix, so put phishing-resistant MFA and session brokering on every VPN and jump-host path into OT, and treat an unexplained process anomaly as a trigger for a security investigation, since Dragos found 82% of organisations lack that criterion ([Dragos, 2026-02-17](https://www.dragos.com/blog/dragos-2026-ot-cybersecurity-year-in-review)).

## Correction — 2026-09-30T07:14:50Z

The earlier text said 81% of incident-response engagements found no meaningful segmentation and quoted a 62% remote-access entry vector, a 34% process-level figure, NIS2 inventory gaps and IEC 62443 guidance. Dragos's figure is "81 percent of assessments identified poor IT/OT segmentation" ([Dragos, 2026-02-17](https://www.dragos.com/blog/dragos-2026-ot-cybersecurity-year-in-review)), and the other figures appear on no Dragos page, so they are removed. Dragos's credential figure is that compromised VPN or jump-host credentials were involved in 73% of all-time incident cases, not that they caused them or were stolen ([Dragos, 2026-02-17](https://www.dragos.com/blog/dragos-2026-ot-cybersecurity-year-in-review)).
