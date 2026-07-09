---
schema: 1
kind: incident
horizon: operational
title: "Groupe 3R confirms Akira attribution and darknet publication of stolen data in its own forensic update"
headline: "Swiss radiology network Groupe 3R confirms via its own forensics that Akira was behind its April attack and has published stolen data"
summary: >
  Groupe 3R (Réseau Radiologique Romand), a 20-site medical-imaging network across seven
  Romandie cantons, has now confirmed through its own forensic investigation that the
  2026-04-30 ransomware attack was carried out by Akira and that stolen corporate/administrative
  documents have since been published on the darknet — closing the attribution gap left when
  Akira first listed the victim on 2026-05-08. The operator refused to pay, rebuilt all 20 sites,
  and acknowledged it may never establish with certainty whether medical data was exfiltrated.
discovered_at: "2026-07-09T12:25:00Z"
event_date: "2026-07-07"
run_id: 2026-07-09T1211Z-intel
priority: notable
immediate_action: null
tags: [ransomware, data-breach]
regions: [switzerland]
sectors: [healthcare]
entities: [incident:groupe-3r-akira-2026, actor:akira]
cves: []
sources:
  - url: "https://www.swisscybersecurity.net/news/2026-05-07/cyberangriff-legt-westschweizer-radiologie-netzwerk-erneut-lahm"
    publisher: "SwissCybersecurity.net"
    date: "2026-07-07"
    role: primary
  - url: "https://www.ictjournal.ch/news/2026-07-06/donnees-volees-systemes-retablis-le-groupe-3r-fait-le-point-apres-la-cyberattaque"
    publisher: "ICTjournal.ch"
    date: "2026-07-06"
    role: corroborating
closed_sources: []
evidence: []
verification: single-source-victim
sourcing_note: "Single-source-victim carve-out: both outlets carry the same origin — Groupe 3R's own post-incident statement/forensic conclusion — so this is single-origin victim disclosure re-reported by two Swiss trade outlets rather than two independent investigations; credibility rated 2 accordingly. Underlying event (attack 2026-04-30, Akira leak-site listing 2026-05-08) is already tracked; this entry carries only the delta."
confidence: high
update_of: 2026-05-10/groupe-3r-r-seau-radiologique-romand-akira-ransomware-claims
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: C
  credibility: 2
watchlist_hit: false
actions:
  - "Swiss/EU healthcare operators previously targeted should not treat a single successful defence as retiring the threat model: Groupe 3R has now been hit twice inside twelve months — by different attackers in April 2025 and by Akira in April 2026 — so budget for recurring hardening reviews of edge/remote-access exposure rather than assuming one incident closes the risk."
  - "Ensure egress monitoring and object-level access logging on PACS/RIS/backup infrastructure are in place now: Groupe 3R's admission that exfiltration scope may be structurally unknowable after the fact shows post-hoc forensics cannot substitute for pre-existing telemetry."
migrated_from: null
---

**UPDATE (originally covered 2026-05-10):** Groupe 3R (Réseau Radiologique Romand), the network of 20 medical-imaging centres across seven Romandie cantons (Geneva, Vaud, Valais, Fribourg, Neuchâtel, Berne), has now confirmed through its own forensic investigation — not merely the attacker's leak-site claim — that the 30 April 2026 ransomware attack was carried out by Akira, and that stolen corporate and administrative documents have since been published on the darknet ([SwissCybersecurity.net, 2026-07-07](https://www.swisscybersecurity.net/news/2026-05-07/cyberangriff-legt-westschweizer-radiologie-netzwerk-erneut-lahm); [ICTjournal.ch, 2026-07-06](https://www.ictjournal.ch/news/2026-07-06/donnees-volees-systemes-retablis-le-groupe-3r-fait-le-point-apres-la-cyberattaque)). This closes the attribution gap left open when Akira first listed the victim on 2026-05-08. The operator states medical data was encrypted (disrupting availability) but that no publication of medical data has been observed to date, while candidly acknowledging that whether medical data was also exfiltrated "may never be clarified with absolute certainty" — an unusually frank admission of incomplete forensic visibility that is itself the transferable lesson here.

Groupe 3R refused to pay the ransom, filed a criminal complaint with cantonal police on the attack date (forwarded to the Federal Public Prosecutor on 2026-05-12) and notified the Federal Office for Cybersecurity (BACS). As of this update all 20 centres are running on rebuilt, ISO-27001-partner infrastructure (RIS, PACS, telephony and teleradiology restored) but the referring-physician portal remained in security testing before redeployment — over two months post-incident. The activity is consistent with Akira's documented playbook: `T1486 Data Encrypted for Impact` (medical-data encryption), `T1567 Exfiltration Over Web Service` (darknet publication), typically preceded by edge-device / external-remote-service initial access. **Defender takeaway:** the two-month realistic mean-time-to-recovery for a full RIS/PACS rebuild is a useful business-continuity benchmark for healthcare operators, and the "we may never know what was taken" outcome is the concrete argument for egress monitoring and object-level access logging on imaging and backup infrastructure before an incident, not after.
