---
schema: 1
kind: incident
horizon: operational
title: "Groupe 3R (Réseau Radiologique Romand) — Akira ransomware claims 48 GB; 20 imaging centres across seven Swiss cantons, second attack in twelve months"
headline: "Groupe 3R (Réseau Radiologique Romand) — Akira ransomware claims 48 GB; 20 imaging centres across seven Swiss cantons, second attack in twelve months"
summary: "Groupe 3R (Réseau Radiologique Romand) listed by Akira on its leak site as a 48 GB victim — 20 medical-imaging centres across seven Romandie cantons (Geneva, Vaud, Valais, Fribourg, Neuchâtel, Berne and a seventh), patient records and employee identity documents in scope. Victim disclosed the attack on 2026-04-30 via its own site, notified BACS/OFCS, filed criminal complaint, and stated it will not pay ransom. Second cyberattack on the same Swiss imaging operator within twelve months."
discovered_at: "2026-05-10T05:00:00Z"
event_date: 2026-05-07
run_id: 2026-05-10-001
priority: high
immediate_action: null
tags:
  - ransomware
  - organized-crime
  - data-breach
regions:
  - switzerland
sectors:
  - healthcare
entities:
  - "incident:groupe-3r-akira-2026"
  - "actor:akira"
cves: []
sources:
  - url: "https://www.groupe3r.ch/fr/information-importante-perturbation-de-nos-services-7268/"
    publisher: "Groupe 3R victim statement, 2026-04-30"
    role: primary
  - url: "https://www.ictjournal.ch/news/2026-05-06/le-reseau-radiologique-romand-a-nouveau-victime-dune-cyberattaque-ses-systemes"
    publisher: "ICTjournal.ch, 2026-05-06"
    role: corroborating
  - url: "https://www.blick.ch/fr/suisse/romande/cyberattaque-le-groupe-romand-3r-de-radiologie-cible-id21930477.html"
    publisher: "Blick.ch, 2026-05-07"
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
migrated_from: briefs/2026-05-10.md
---

Akira listed Groupe 3R on its dark-web leak site on approximately 2026-05-08, claiming an attack dated 2026-04-30 and threatening release of 48 GB including employee identity documents (passports, driving licences, national IDs), patient records (addresses, phone numbers, medical data), payment information, and signed NDAs ([Groupe 3R victim statement, 2026-04-30](https://www.groupe3r.ch/fr/information-importante-perturbation-de-nos-services-7268/) · [ICTjournal.ch, 2026-05-06](https://www.ictjournal.ch/news/2026-05-06/le-reseau-radiologique-romand-a-nouveau-victime-dune-cyberattaque-ses-systemes) · [Blick.ch, 2026-05-07](https://www.blick.ch/fr/suisse/romande/cyberattaque-le-groupe-romand-3r-de-radiologie-cible-id21930477.html)). Groupe 3R operates 20 medical-imaging centres across seven Romandie cantons (Vaud, Valais, Fribourg, Genève, Neuchâtel, Berne, and a further canton listed in the operator statement) — making this a direct Swiss critical-health-infrastructure incident. The operator confirmed the attack publicly via its own website on 2026-04-30, notified the Federal Office for Cybersecurity (BACS/OFCS), filed a criminal complaint, and explicitly stated it will not pay ransom. Legacy examination data remains inaccessible at the time of the public update; new examination data security has been restored on rebuilt infrastructure. Data-exfiltration was not confirmed by the victim; Akira's leak-site post asserts 48 GB exfiltrated. The operator's own statement notes this is its second cyberattack within twelve months and characterises the prior April 2025 incident as having involved different attackers and methodology.

Akira's documented playbook against European healthcare and small-to-mid enterprise targets emphasises edge-device initial access (Cisco ASA / FTD CVEs, Fortinet SSL-VPN CVEs, VMware ESXi authenticated RCE) and intermittent file-encryption to evade EDR file-IO heuristics; ATT&CK techniques observed across recent Akira incidents include [T1190 Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/), [T1133 External Remote Services](https://attack.mitre.org/techniques/T1133/), [T1486 Data Encrypted for Impact](https://attack.mitre.org/techniques/T1486/), and [T1567 Exfiltration Over Web Service](https://attack.mitre.org/techniques/T1567/).

**Defender takeaway:** Swiss and DACH healthcare operators with internet-exposed Cisco ASA/FTD, Fortinet SSL-VPN, or VMware ESXi management interfaces should validate that all 2025–2026 Akira-targeted CVEs are patched, that EDR rules trigger on intermittent-encryption file-IO patterns (write-then-skip-then-write of fixed-block ranges), and that radiology-modality VLANs are network-segmented from corporate AD; PACS/RIS environments tend to co-tenant with Windows file shares, providing trivial east-west reach once an attacker lands. Imaging operators that depend on a single ransomware-targeted partner should review business-continuity arrangements: this is the second 3R outage inside a year and referrers will already have continuity questions.
