---
schema: 1
kind: research
title: "Citizen Lab: Cellebrite UFED used by Russian authorities three months after the vendor's Russia pull-out"
headline: "Citizen Lab: Cellebrite UFED used by Russian authorities three months after the vendor's Russia pull-out"
summary: "Citizen Lab published a forensic investigation (2026-06-25) confirming that Russian authorities used Cellebrite UFED / UFED 4PC / UFED Physical Analyzer to extract data from the iPhone 12 of opposition activist Andrey Pivovarov on 17 June 2021 — three months after Cellebrite cancelled its Russian contracts in …"
discovered_at: "2026-06-27T05:17:44Z"
event_date: 2026-06-25
run_id: 2026-06-27-40e791d4
priority: notable
immediate_action: null
tags:
  - espionage
  - nation-state
  - mobile
  - russia-nexus
regions:
  - russia-cis
  - europe
sectors:
  - public-sector
  - media
  - legal-services
entities: []
cves: []
sources:
  - url: "https://citizenlab.ca/research/russia-breaks-into-human-rights-activists-phone-with-cellebrite/"
    publisher: Citizen Lab
    role: primary
  - url: "https://therecord.media/russia-used-cellebrite-tool-after-company-pulled-out-of-country"
    publisher: The Record
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
migrated_from: briefs/2026-06-27.md
---

Citizen Lab published a forensic investigation (2026-06-25) confirming that Russian authorities used **Cellebrite UFED / UFED 4PC / UFED Physical Analyzer** to extract data from the iPhone 12 of opposition activist Andrey Pivovarov on 17 June 2021 — three months after Cellebrite cancelled its Russian contracts in March 2021 ([Citizen Lab, 2026-06-25](https://citizenlab.ca/research/russia-breaks-into-human-rights-activists-phone-with-cellebrite/)). Two independent evidence streams corroborate: on-device `MobileLockdown` records show a USB connection to a Host ID previously attributed to Cellebrite hardware, and an official forensic report authored by the MVD (Interior Ministry) Forensic Expert Center — commissioned by the Investigative Committee — explicitly names the UFED tooling and lists extracted WhatsApp/Telegram/Viber data with keyword searches for opposition figures ([The Record, 2026-06-25](https://therecord.media/russia-used-cellebrite-tool-after-company-pulled-out-of-country)). The operational lessons are blunt: physical seizure plus closed forensic tooling bypasses device encryption and end-to-end-encrypted messaging entirely; vendor contract cancellations and export controls are not a reliable technical barrier to tool proliferation; and `MobileLockdown` USB-host records are forensically valuable for identifying which extraction device touched a phone.
**Defender takeaway:** For Swiss diplomatic, parliamentary and law-enforcement staff travelling to higher-risk jurisdictions, threat models must treat device seizure as an out-of-band bypass of all software-based controls — pairing this with today's § 1 Signal advisory, sensitive comms should assume both the device and its backups are reachable by a capable adversary.
