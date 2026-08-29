---
schema: 1
kind: threat
title: "Swiss Federal Audit Office: federal cyber-governance split leaves strategic oversight without a complete incident picture"
headline: "Swiss Federal Audit Office: federal cyber-governance split leaves strategic oversight without a complete incident picture"
summary: "Switzerland's Federal Audit Office (EFK) found that the two-year-old federal cyber-governance split leaves the strategic-oversight body (FS BIS/SEPOS) without a complete picture of incidents in federal systems, because BACS has no legal authority to forward incident reports independently and agencies must opt in to sharing via the Cyber Security Hub (SwissCybersecurity.net, 2026-06-19). The operational consequence: SEPOS-level threat analysis may be blind to incidents BACS already holds."
discovered_at: "2026-06-22T04:52:26Z"
event_date: 2026-06-19
run_id: 2026-06-22-dece656d
priority: high
immediate_action: null
tags:
  - law-enforcement
  - eu-nexus
regions:
  - switzerland
sectors:
  - public-sector
entities: []
cves: []
sources:
  - url: "https://www.swisscybersecurity.net/news/2026-06-19/neue-cyberaufsicht-kaempft-mit-anlaufschwierigkeiten"
    publisher: SwissCybersecurity.net
    role: primary
  - url: "https://www.efk.admin.ch/wp-content/uploads/publikationen/berichte/wirtschaft_und_verwaltung/informatikprojekte/25152/25152-wik-sepos-fs-bis_d.pdf"
    publisher: EFK report 25152
    role: corroborating
  - url: "https://www.netzwoche.ch/news/2026-06-19/neue-cyberaufsicht-kaempft-mit-anlaufschwierigkeiten"
    publisher: Netzwoche
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
migrated_from: briefs/2026-06-22.md
---

Switzerland's Federal Audit Office (Eidgenössische Finanzkontrolle, EFK) published an audit on 2026-06-19 of the federal cybersecurity structure reorganised two years ago, finding that the strategic-oversight body — FS BIS, within SEPOS — does not have a complete view of security-relevant events in federal systems ([SwissCybersecurity.net, 2026-06-19](https://www.swisscybersecurity.net/news/2026-06-19/neue-cyberaufsicht-kaempft-mit-anlaufschwierigkeiten); [EFK report 25152, 2026-06-19](https://www.efk.admin.ch/wp-content/uploads/publikationen/berichte/wirtschaft_und_verwaltung/informatikprojekte/25152/25152-wik-sepos-fs-bis_d.pdf)). The audit names three concrete gaps: the contracted requirements-management ("Vorgabenmanagement") support that BACS owes FS BIS is not being delivered at the agreed scope under the existing service-level agreement; BACS has no legal authority to forward incident reports to SEPOS/FS BIS on its own, so reporting depends on each affected agency opting in to sharing via the Cyber Security Hub platform; and incident-response coordination between the two bodies was inconsistent across cases, with stakeholders sometimes unaware of measures the peer body had already taken ([Netzwoche, 2026-06-19](https://www.netzwoche.ch/news/2026-06-19/neue-cyberaufsicht-kaempft-mit-anlaufschwierigkeiten)). The EFK explicitly rejected a further reorganisation (folding the function into BACS) and instead recommends that BACS and FS BIS leadership resolve their differences and clarify roles at management level.

**Defender takeaway:** For a Swiss federal SOC the instructive part is the structural visibility gap, not an active intrusion. Because the Cyber Security Hub sharing path is opt-in and BACS cannot relay incident data to SEPOS without the originating agency's consent, the federal strategic threat picture can be missing incidents that BACS already holds — meaning cross-agency correlation and trend analysis at SEPOS level may be working from an incomplete dataset. Federal and cantonal bodies should treat their own Cyber Security Hub reporting posture as a deliberate decision (confirm whether SEPOS data-sharing is enabled), and recognise that "we reported it to BACS" does not guarantee the strategic-oversight layer ever saw it.
