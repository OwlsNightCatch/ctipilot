---
schema: 1
kind: incident
horizon: operational
title: "BravoX ransomware leaks 220 GB from a Vaud fiduciary, exposing ~15 municipalities' data and a cantonal minister's tax file"
headline: "A breached Vaud accounting firm spilled 15 municipalities' administrative data — the fiduciary was the pivot, not any government network"
summary: >
  The BravoX ransomware group published ~220 GB / 100,000+ files stolen from an Yverdon-les-Bains fiduciary firm,
  exposing administrative and tax records of some fifteen Nord Vaudois municipalities and the personal tax file of
  Vaud State Councillor Vassilis Venizelos. No ransom was paid; the firm notified the cantonal data-protection
  commissioner and Switzerland's Federal Office for Cybersecurity (BACS/OFCS).
discovered_at: "2026-07-24T04:36:09Z"
event_date: "2026-07-18"
run_id: 2026-07-24T0409Z-intel
priority: notable
immediate_action: null
tags: [ransomware, data-breach, organized-crime]
regions: [switzerland, europe]
sectors: [public-sector, legal-services]
entities: [actor:bravox, incident:bravox-yverdon-fiduciary-vaud-municipalities-2026]
techniques: [T1486, T1657]
affected_products: []
cves: []
sources:
  - url: "https://www.letemps.ch/suisse/vaud/le-piratage-d-une-fiduciaire-vaudoise-expose-sur-le-dark-web-100-000-dossiers-de-clients-dont-celui-d-un-conseiller-d-etat"
    publisher: "Le Temps"
    date: "2026-07-22"
    role: primary
  - url: "https://www.24heures.ch/cyberattaque-les-donnees-fiscales-de-vassilis-venizelos-fuitent-454052188828"
    publisher: "24 heures"
    date: "2026-07-23"
    role: corroborating
  - url: "https://www.20min.ch/fr/story/vaud-fiduciaire-piratee-des-communes-et-un-conseiller-d-etat-touches-103607546"
    publisher: "20 minutes (CH)"
    date: "2026-07-23"
    role: corroborating
  - url: "https://socradar.io/blog/dark-web-profile-bravox-ransomware/"
    publisher: "SOCRadar"
    date: "2026-01-26"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Le 18 juillet, quelque 220 Go de données y ont été publiées, soit plus de 100 000 dossiers."
    publisher: "Le Temps"
  - quote: "Aucune rançon n'a été versée. Une plainte pénale a été déposée et le préposé à la protection des données ainsi que l'Office fédéral de la cybersécurité ont été informés."
    publisher: "24 heures"
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions: []
migrated_from: null
---

The extortion group **BravoX** — a Ransomware-as-a-Service operation first profiled on the RAMP underground forum in January 2026, which vets affiliates and by convention avoids CIS-based victims ([SOCRadar, 2026-01-26](https://socradar.io/blog/dark-web-profile-bravox-ransomware/)) — breached an accounting/fiduciary firm in Yverdon-les-Bains (canton Vaud) around 30 June 2026, and on 18 July published roughly 220 GB (over 100,000 files) on its Tor leak site ([Le Temps, 2026-07-22](https://www.letemps.ch/suisse/vaud/le-piratage-d-une-fiduciaire-vaudoise-expose-sur-le-dark-web-100-000-dossiers-de-clients-dont-celui-d-un-conseiller-d-etat)). The firm's own account describes a "connection problem" to its server that led its IT provider to isolate affected systems, revoke compromised access and restore from an external backup; no negotiation took place and no ransom was paid ([Le Temps, 2026-07-22](https://www.letemps.ch/suisse/vaud/le-piratage-d-une-fiduciaire-vaudoise-expose-sur-le-dark-web-100-000-dossiers-de-clients-dont-celui-d-un-conseiller-d-etat)). The leaked dataset spans individuals, businesses and institutions, and includes administrative and tax records of some fifteen Nord Vaudois municipalities (Corcelles-près-Concise and Belmont-sur-Yverdon among those named) and the personal tax file of Vaud State Councillor Vassilis Venizelos and his spouse ([24 heures, 2026-07-23](https://www.24heures.ch/cyberattaque-les-donnees-fiscales-de-vassilis-venizelos-fuitent-454052188828)). The firm filed a criminal complaint and notified both the cantonal data-protection commissioner and the Federal Office for Cybersecurity (BACS/OFCS) — Switzerland's mandatory critical-incident reporting channel ([24 heures, 2026-07-23](https://www.24heures.ch/cyberattaque-les-donnees-fiscales-de-vassilis-venizelos-fuitent-454052188828)).

**Defender takeaway:** No government network was touched — the exposure of cantonal and municipal data ran entirely through a private supplier holding tax and administrative records on public administration's behalf. Swiss cantonal and municipal security teams should treat their outsourced fiduciary, accounting and payroll providers as in-scope for the personal and fiscal data those providers process, and confirm those firms carry incident-reporting obligations, tested offline backups (which limited this firm's operational impact) and data-protection notification duties in contract. The exposure is structural, not incidental: the municipal outsourcing model for fiduciary and accounting services concentrates cantonal and municipal personal and tax data inside private firms whose security posture the public bodies do not directly control.
