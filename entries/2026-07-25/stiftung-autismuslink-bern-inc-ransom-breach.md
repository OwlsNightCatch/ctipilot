---
schema: 1
kind: incident
horizon: operational
title: "Swiss autism-support foundation Stiftung Autismuslink confirms data-theft cyberattack; INC Ransom claims it"
headline: "Bern foundation's own notice confirms exfiltration and server encryption; INC Ransom posts a leak-site claim"
summary: >
  Stiftung Autismuslink, a Bern-based Swiss foundation serving young people with autism, published a signed
  notice confirming a cyberattack detected 2026-06-29 in which "larger volumes of data" were exfiltrated and
  its server temporarily encrypted; the INC Ransom RaaS group posted a matching leak-site claim on 2026-07-24.
  Exposed data includes cantonal education-directorate (BKD) contracts, Swiss disability-insurance (IV) service
  agreements and the complete 2016-2023 client dossier archive — directly relevant to Swiss cantonal/communal
  social-services and education defenders.
discovered_at: "2026-07-25T04:38:26Z"
event_date: "2026-07-24"
run_id: 2026-07-25T0409Z-intel
priority: notable
immediate_action: null
tags: [ransomware, data-breach]
regions: [switzerland, europe]
sectors: [public-sector, healthcare, education]
entities: [actor:inc-ransom]
techniques: [T1486, T1005]
affected_products: []
cves: []
sources:
  - url: "https://autismuslink.ch/wp-content/uploads/2026_07_Informationsschreiben_zum_Serverausfall_Extern.pdf"
    publisher: "Stiftung Autismuslink (victim statement)"
    date: "2026-07"
    role: primary
  - url: "https://www.ransomware.live/id/YXV0aXNtdXNsaW5rLmNoQGluY3JhbnNvbQ=="
    publisher: "Ransomware.live (INC Ransom leak-site listing)"
    date: "2026-07-24"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Ende Juni wurde unsere IT-Infrastruktur Opfer eines Cyberangriffs. Nach aktueller Erkenntnis wurden grössere Datenmengen durch die Angreifer abgezogen und unser Server vorübergehend verschlüsselt."
    publisher: "Stiftung Autismuslink (victim statement)"
  - quote: "Backupsysteme der Stiftung Autismuslink wurden kontrolliert und sind nicht vom Angriff betroffen."
    publisher: "Stiftung Autismuslink (victim statement)"
verification: multi-source
sourcing_note: "The attack, exfiltration and temporary encryption are the victim's own first-party statement (Admiralty A for its own incident); the INC Ransom attribution rests on the group's leak-site claim (via Ransomware.live), which matches the victim identity and timeline but is not confirmed by the foundation. Initial-access vector and ransomware payload are not disclosed."
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: null
---

Stiftung Autismuslink — a Bern-based foundation providing school, coaching and vocational-integration services to adolescents and young adults with autism — published a signed victim notice confirming a cyberattack: "Ende Juni wurde unsere IT-Infrastruktur Opfer eines Cyberangriffs. Nach aktueller Erkenntnis wurden grössere Datenmengen durch die Angreifer abgezogen und unser Server vorübergehend verschlüsselt" (end of June our IT infrastructure fell victim to a cyberattack; larger volumes of data were exfiltrated and our server temporarily encrypted) ([Stiftung Autismuslink, 2026-07](https://autismuslink.ch/wp-content/uploads/2026_07_Informationsschreiben_zum_Serverausfall_Extern.pdf)). The foundation states the irregularity was detected Monday 2026-06-29, the system was immediately isolated from the internet, an external IT provider (Infoguard) was engaged for forensics the same day, the relevant authorities were notified and a criminal complaint filed with the police. Backups were verified unaffected. The INC Ransom (Incransom) double-extortion group posted a leak-site claim against autismuslink.ch on 2026-07-24 consistent in victim identity and timeline ([Ransomware.live, 2026-07-24](https://www.ransomware.live/id/YXV0aXNtdXNsaW5rLmNoQGluY3JhbnNvbQ==)) — a relatively rare case of same-day victim self-disclosure and leak-site claim converging.

The disclosure event (site notice plus leak-site claim) is what falls in this window; the underlying intrusion dates to late June. What makes it relevant beyond a single victim is the data class: per the foundation, affected material includes service agreements with the Swiss disability insurance (IV) and a cantonal education/culture directorate (BKD), teacher contracts, doctors' certificates and the complete client dossier archive 2016-2023 for minors and young adults. **Defender takeaway:** the relevance is the target class, not this single victim — Swiss cantonal and communal social-services and education bodies running comparable long-lived case-management archives of highly sensitive personal data on minors and vulnerable adults share Autismuslink's exposure profile, and INC Ransom is a double-extortion RaaS active since ~2023 that both encrypts and exfiltrates for leverage. The victim's own account is the practical lesson: immediate network isolation on first detection and verified-clean, segmented backups are what turned a server-encryption event into a recoverable one here, and are the controls that most directly determine whether a comparable intrusion becomes a full outage.
