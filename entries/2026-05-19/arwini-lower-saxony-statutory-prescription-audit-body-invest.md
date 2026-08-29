---
schema: 1
kind: incident
title: "ARWINI (Lower Saxony statutory-prescription audit body) — investigators confirm data exfiltration after 4 May intrusion; Kairos ransomware group claims 2.87 TB; ~70,000 GDPR Art. 9 records in scope"
headline: "ARWINI (Lower Saxony statutory-prescription audit body) — investigators confirm data exfiltration after 4 May intrusion; Kairos ransomware group claims 2.87"
summary: "ARWINI prescription-review body (Lower Saxony) — investigators confirm data exfiltration, ~70,000 GDPR Art. 9 patient records likely affected; Kairos ransomware group claims theft of 2.87 TB (Deutsches Ärzteblatt, 2026-05-18; Heise Security, 2026-05-18). Statutory health-insurance auditor for KVN/AOK; Polizeidirektion Hannover is the investigating authority; data offered for sale on Kairos leak site."
discovered_at: "2026-05-19T05:00:00Z"
event_date: 2026-05-18
run_id: 2026-05-19-2505c918
priority: high
immediate_action: null
tags:
  - ransomware
  - data-breach
regions:
  - dach
  - europe
sectors:
  - healthcare
  - public-sector
entities:
  - "incident:arwini-lower-saxony-statutory-prescription-audit-body-data"
  - "actor:kairos-extortion"
cves: []
sources:
  - url: "https://www.aerzteblatt.de/news/hackerangriff-auf-rezeptprufer-c259a70c-595b-4770-9d84-87f6c8338c0c"
    publisher: "Deutsches Ärzteblatt"
    role: primary
  - url: "https://www.heise.de/news/Niedersachsen-Datenabfluss-bei-Wirtschaftsprueferverein-im-Gesundheitswesen-11297772.html"
    publisher: Heise Security
    role: corroborating
  - url: "https://borncity.com/blog/2026/05/16/cyberangriff-auf-die-arwini-rezeptpruefung-in-niedersachsen-mit-datenabfluss/"
    publisher: Borns IT Blog
    role: corroborating
closed_sources: []
evidence:
  - quote: "Nach dem Cyberangriff auf einen Wirtschaftsprüfverein des Gesundheitswesens bestätigen Ermittler einen Datenabfluss"
    publisher: Heise Security
  - quote: "Laut ARWINI ist es wahrscheinlich, dass personenbezogene und besonders schützenswerte Daten betroffen sind"
    publisher: Borns IT Blog citing ARWINI
  - quote: Kairos ransomware group has claimed the attack
    publisher: Heise Security
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
migrated_from: briefs/2026-05-19.md
---

Investigators confirmed on 2026-05-18 that the cyberattack on ARWINI — the *Arbeitsgemeinschaft Wirtschaftlichkeitsprüfung Niedersachsen e.V.*, which audits prescription cost-effectiveness for statutory-health-insurance (GKV) patients in Lower Saxony via data exchange with Kassenärztliche Vereinigung Niedersachsen (KVN), AOK and other insurers — resulted in confirmed exfiltration of personal data ([Deutsches Ärzteblatt, 2026-05-18](https://www.aerzteblatt.de/news/hackerangriff-auf-rezeptprufer-c259a70c-595b-4770-9d84-87f6c8338c0c); [Heise Security, 2026-05-18](https://www.heise.de/news/Niedersachsen-Datenabfluss-bei-Wirtschaftsprueferverein-im-Gesundheitswesen-11297772.html)). Intrusion signs were detected on ARWINI servers on 2026-05-04 and all systems were shut down on the same day; ARWINI's own statement, cited by Borns IT Blog on 2026-05-16, said particularly sensitive personal data (besondere Kategorien — GDPR Art. 9) are likely affected, with health and billing data on ≥70,000 patients in scope ([Borns IT Blog, 2026-05-16](https://borncity.com/blog/2026/05/16/cyberangriff-auf-die-arwini-rezeptpruefung-in-niedersachsen-mit-datenabfluss/)). The Polizeidirektion Hannover is the investigating authority; the Landesbeauftragter für Datenschutz Niedersachsen (LfD) and BSI have been notified under the GDPR 72-hour rule and the German KRITIS / NIS2UmsuCG framework. Heise reports the *Kairos* ransomware group has claimed the attack and is threatening to sell approximately 2.87 TB of stolen data on its leak site, with attackers' leak-site claim dated 2026-05-11. The technical pattern is consistent with double-extortion ransomware now in the operator-leak-site phase.

**Why it matters to us:** GKV bodies and their mandated third-party auditors are NIS2 entities; the supply-chain relationship between KVN/AOK and ARWINI is precisely the data-processor scope hit by NMDL/IGJ in the Netherlands (covered 2026-05-14). Defender pattern: any GKV / AHV / cantonal health-insurance data-exchange counterparty should be inventoried as an in-scope critical-supplier under §8b BSI-Gesetz / NIS2UmsuCG, with breach-notification playbooks rehearsed for the 72-hour GDPR clock from a third party's detection event, not just one's own. Monitor for downstream phishing using GKV billing-data lures targeting affected patient cohorts.
